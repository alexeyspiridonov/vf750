import AppKit
import Foundation
import SwiftUI
import Translation

struct TranslationJob: Identifiable {
    let id: String
    let sourceURL: URL
    let destinationURL: URL
}

struct TextChunk {
    let id: String
    let text: String
}

@MainActor
final class TranslationCoordinator: ObservableObject {
    @Published var configuration: TranslationSession.Configuration?
    @Published var status: String = "Preparing translation jobs..."
    @Published var detail: String = ""

    private let rootURL: URL
    private let ruRootURL: URL
    private let sourceLanguage = Locale.Language(identifier: "en")
    private let targetLanguage = Locale.Language(identifier: "ru")
    private let maxChunkCharacters = 1000
    private let batchSize = 40
    private let maxFiles: Int?
    private let fileFilter: String?
    private let logURL: URL

    private(set) var jobs: [TranslationJob] = []
    private(set) var currentJobIndex = 0
    private var isProcessing = false

    init(rootURL: URL, maxFiles: Int?, fileFilter: String?) {
        self.rootURL = rootURL
        self.ruRootURL = rootURL.appendingPathComponent("ru", isDirectory: true)
        self.maxFiles = maxFiles
        self.fileFilter = fileFilter?.trimmingCharacters(in: .whitespacesAndNewlines)
        self.logURL = rootURL.appendingPathComponent("ru/.translation-txt.log")
        self.jobs = Self.discoverJobs(rootURL: rootURL, ruRootURL: ruRootURL, maxFiles: maxFiles, fileFilter: fileFilter)
        self.log("Initialized with \(jobs.count) job(s)")
    }

    func start() {
        log("start() called")
        guard !jobs.isEmpty else {
            status = "No pending TXT files found."
            detail = "All TXT files in ru/ either already differ from the source or do not have a matching source file."
            log("No pending jobs found")
            terminateSoon()
            return
        }

        status = "Ready to translate \(jobs.count) TXT files"
        log("Scheduling first translation pass")
        scheduleNextPass()
    }

    func process(session: TranslationSession) async {
        log("process(session:) invoked")
        guard !isProcessing else { return }
        guard currentJobIndex < jobs.count else {
            status = "Translation finished."
            detail = "Processed \(jobs.count) TXT files."
            log("No more jobs left")
            terminateSoon()
            return
        }

        isProcessing = true
        defer { isProcessing = false }

        do {
            while currentJobIndex < jobs.count {
                let job = jobs[currentJobIndex]
                let progressPrefix = "[\(currentJobIndex + 1)/\(jobs.count)]"
                status = "\(progressPrefix) \(job.sourceURL.lastPathComponent)"
                detail = job.destinationURL.path.replacingOccurrences(of: rootURL.path + "/", with: "")
                log("Starting job \(currentJobIndex + 1): \(job.id)")

                let sourceText = try String(contentsOf: job.sourceURL, encoding: .utf8)
                let translatedText = try await translate(text: sourceText, session: session, progressPrefix: progressPrefix)
                try translatedText.write(to: job.destinationURL, atomically: true, encoding: .utf8)
                log("Finished job \(job.id)")

                currentJobIndex += 1
            }

            status = "Translation finished."
            detail = "Processed \(jobs.count) TXT files."
            log("All jobs finished")
            terminateSoon()
        } catch {
            let failedJob = jobs[min(currentJobIndex, jobs.count - 1)]
            status = "Translation failed"
            detail = "\(failedJob.destinationURL.lastPathComponent): \(error.localizedDescription)"
            log("Translation failed for \(failedJob.id): \(error)")
            fputs("Translation failed for \(failedJob.sourceURL.path): \(error)\n", stderr)
            terminateSoon()
        }
    }

    private func translate(text: String, session: TranslationSession, progressPrefix: String) async throws -> String {
        let chunks = chunkText(text)
        guard !chunks.isEmpty else { return text }

        var translatedParts: [String] = []
        translatedParts.reserveCapacity(chunks.count)

        for batchStart in stride(from: 0, to: chunks.count, by: batchSize) {
            let batchEnd = min(batchStart + batchSize, chunks.count)
            let batch = Array(chunks[batchStart..<batchEnd])
            status = "\(progressPrefix) batch \(batchStart / batchSize + 1)/\(Int(ceil(Double(chunks.count) / Double(batchSize))))"
            log("Translating batch \(batchStart / batchSize + 1) with \(batch.count) chunk(s)")

            let requests = batch.map { TranslationSession.Request(sourceText: $0.text, clientIdentifier: $0.id) }
            let responses = try await session.translations(from: requests)
            let responseByID: [String: String] = Dictionary(uniqueKeysWithValues: responses.compactMap { response in
                guard let id = response.clientIdentifier else { return nil }
                return (id, response.targetText)
            })

            for chunk in batch {
                translatedParts.append(responseByID[chunk.id] ?? chunk.text)
            }
        }

        return translatedParts.joined()
    }

    private func chunkText(_ text: String) -> [TextChunk] {
        if text.isEmpty {
            return []
        }

        let rawLines = text.split(separator: "\n", omittingEmptySubsequences: false)
        var chunks: [TextChunk] = []
        var buffer = ""

        for (index, rawLine) in rawLines.enumerated() {
            let line = String(rawLine) + (index < rawLines.count - 1 ? "\n" : "")

            if buffer.count + line.count > maxChunkCharacters, !buffer.isEmpty {
                chunks.append(TextChunk(id: "chunk-\(chunks.count)", text: buffer))
                buffer.removeAll(keepingCapacity: true)
            }

            if line.count > maxChunkCharacters {
                if !buffer.isEmpty {
                    chunks.append(TextChunk(id: "chunk-\(chunks.count)", text: buffer))
                    buffer.removeAll(keepingCapacity: true)
                }

                var sliceStart = line.startIndex
                while sliceStart < line.endIndex {
                    let sliceEnd = line.index(sliceStart, offsetBy: maxChunkCharacters, limitedBy: line.endIndex) ?? line.endIndex
                    chunks.append(TextChunk(id: "chunk-\(chunks.count)", text: String(line[sliceStart..<sliceEnd])))
                    sliceStart = sliceEnd
                }
                continue
            }

            buffer += line
        }

        if !buffer.isEmpty {
            chunks.append(TextChunk(id: "chunk-\(chunks.count)", text: buffer))
        }

        return chunks
    }

    private func scheduleNextPass() {
        configuration = nil
        log("Scheduling next translationTask pass")
        Task { @MainActor [weak self] in
            guard let self else { return }
            self.configuration = TranslationSession.Configuration(source: self.sourceLanguage, target: self.targetLanguage)
        }
    }

    private func terminateSoon() {
        log("terminateSoon() called")
        Task { @MainActor in
            try? await Task.sleep(for: .seconds(1))
            NSApplication.shared.terminate(nil)
        }
    }

    private func log(_ message: String) {
        let formatter = ISO8601DateFormatter()
        let line = "[\(formatter.string(from: Date()))] \(message)\n"
        guard let data = line.data(using: .utf8) else { return }

        if FileManager.default.fileExists(atPath: logURL.path) {
            if let handle = try? FileHandle(forWritingTo: logURL) {
                try? handle.seekToEnd()
                try? handle.write(contentsOf: data)
                try? handle.close()
            }
        } else {
            try? data.write(to: logURL)
        }
    }

    private static func discoverJobs(rootURL: URL, ruRootURL: URL, maxFiles: Int?, fileFilter: String?) -> [TranslationJob] {
        guard let enumerator = FileManager.default.enumerator(
            at: ruRootURL,
            includingPropertiesForKeys: [.isRegularFileKey],
            options: [.skipsHiddenFiles]
        ) else {
            return []
        }

        var jobs: [TranslationJob] = []

        for case let destinationURL as URL in enumerator {
            guard destinationURL.pathExtension == "txt" else { continue }

            let relativePath = destinationURL.path.replacingOccurrences(of: ruRootURL.path + "/", with: "")
            if let fileFilter, !fileFilter.isEmpty, !relativePath.contains(fileFilter) {
                continue
            }

            let sourceURL = rootURL.appendingPathComponent(relativePath)
            guard FileManager.default.fileExists(atPath: sourceURL.path) else { continue }

            guard shouldTranslate(sourceURL: sourceURL, destinationURL: destinationURL) else { continue }

            jobs.append(TranslationJob(id: relativePath, sourceURL: sourceURL, destinationURL: destinationURL))

            if let maxFiles, jobs.count >= maxFiles {
                break
            }
        }

        return jobs.sorted { $0.id < $1.id }
    }

    private static func shouldTranslate(sourceURL: URL, destinationURL: URL) -> Bool {
        guard
            let sourceText = try? String(contentsOf: sourceURL, encoding: .utf8),
            let destinationText = try? String(contentsOf: destinationURL, encoding: .utf8)
        else {
            return false
        }

        if sourceText != destinationText {
            return false
        }

        return true
    }
}

struct TranslatorView: View {
    @StateObject private var coordinator: TranslationCoordinator

    init(rootURL: URL, maxFiles: Int?, fileFilter: String?) {
        _coordinator = StateObject(wrappedValue: TranslationCoordinator(rootURL: rootURL, maxFiles: maxFiles, fileFilter: fileFilter))
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("VF750 RU TXT Translator")
                .font(.title2)
                .bold()
            Text(coordinator.status)
                .font(.headline)
            Text(coordinator.detail)
                .font(.body)
                .textSelection(.enabled)
            Text("Jobs: \(coordinator.currentJobIndex)/\(coordinator.jobs.count)")
                .font(.caption)
                .foregroundStyle(.secondary)
        }
        .padding(20)
        .frame(minWidth: 720, minHeight: 180)
        .onAppear {
            coordinator.start()
        }
        .translationTask(coordinator.configuration) { session in
            await coordinator.process(session: session)
        }
    }
}

@main
struct TranslatorApp: App {
    private let rootURL: URL
    private let maxFiles: Int?
    private let fileFilter: String?

    init() {
        let arguments = CommandLine.arguments
        let currentDirectory = URL(fileURLWithPath: FileManager.default.currentDirectoryPath, isDirectory: true)

        func value(after flag: String) -> String? {
            guard let index = arguments.firstIndex(of: flag), index + 1 < arguments.count else { return nil }
            return arguments[index + 1]
        }

        self.rootURL = value(after: "--root").map { URL(fileURLWithPath: $0, isDirectory: true) } ?? currentDirectory
        self.maxFiles = value(after: "--max-files").flatMap(Int.init)
        self.fileFilter = value(after: "--filter")
    }

    var body: some Scene {
        WindowGroup {
            TranslatorView(rootURL: rootURL, maxFiles: maxFiles, fileFilter: fileFilter)
        }
        .windowResizability(.contentSize)
    }
}
