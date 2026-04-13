#!/usr/bin/env python3

from __future__ import annotations

import json
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

import fitz
import pikepdf
import requests
from deep_translator import GoogleTranslator


ROOT = Path(__file__).resolve().parent.parent
EN_ROOT = ROOT / "manuals"
RU_ROOT = ROOT / "ru" / "manuals"
CACHE_PATH = ROOT / "ru" / ".translation-manuals-cache.json"
FONT_PATH = Path("/System/Library/Fonts/Supplemental/Arial Narrow.ttf")

MIN_FONT_SIZE = 4.5
MAX_FONT_SIZE = 16.0
TEXT_CHUNK_SIZE = 3200
TRANSLATION_BATCH_SIZE = 48
PDF_PAGE_WIDTH = 595
PDF_PAGE_HEIGHT = 842
PDF_MARGIN = 36
PDF_HEADER_Y = 24
PDF_BODY_FONT_SIZE = 9.5
PDF_HEADER_FONT_SIZE = 8
PDF_LINE_HEIGHT = 12.5


_requests_get = requests.get


def requests_get_with_timeout(*args, **kwargs):
    kwargs.setdefault("timeout", 30)
    return _requests_get(*args, **kwargs)


requests.get = requests_get_with_timeout


@dataclass(frozen=True)
class SectionSpec:
    slug: str
    start_page: int
    end_page: int


HAYNES_SECTIONS = [
    SectionSpec("00-front-matter-and-introductory-pages", 1, 26),
    SectionSpec("01-tune-up-and-routine-maintenance", 27, 47),
    SectionSpec("02-engine-clutch-and-transmission", 48, 99),
    SectionSpec("03-cooling-system", 100, 107),
    SectionSpec("04-fuel-and-exhaust-systems", 108, 131),
    SectionSpec("05-ignition-system", 132, 139),
    SectionSpec("06-frame-suspension-and-final-drive", 140, 164),
    SectionSpec("07-brakes-wheels-and-tires", 165, 188),
    SectionSpec("08-electrical-system", 189, 247),
    SectionSpec("09-conversion-factors", 248, 248),
]

PARTSLIST_SECTIONS = [
    SectionSpec("00-front-matter-and-reference-pages", 1, 12),
    SectionSpec("01-engine-section-b1", 13, 38),
    SectionSpec("02-frame-section-e1", 39, 78),
    SectionSpec("03-part-number-index", 79, 84),
    SectionSpec("04-description-index", 85, 91),
]

SHOP_MANUAL_EXTRACTS = [
    "03-shop-manual-maintenance",
    "04-shop-manual-fuel-system",
    "05-shop-manual-1983-addendum-carb-updates",
]


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def relative_ru_path(path: Path) -> str:
    return str(path.relative_to(ROOT / "ru"))


def is_untranslated_copy(src: Path, dst: Path) -> bool:
    if not src.exists() or not dst.exists():
        return False

    if src.suffix.lower() == ".pdf":
        return src.read_bytes() == dst.read_bytes()

    return src.read_text(encoding="utf-8", errors="ignore") == dst.read_text(encoding="utf-8", errors="ignore")


def pdf_line_text(line: dict[str, object]) -> str:
    return "".join(span["text"] for span in line["spans"]).strip()


def should_translate_text(text: str) -> bool:
    letters = sum(char.isalpha() for char in text)
    if not letters:
        return False

    latin_letters = sum("a" <= char.lower() <= "z" for char in text)
    return latin_letters / letters >= 0.45


class Translator:
    def __init__(self) -> None:
        self.client = GoogleTranslator(source="en", target="ru")
        self.cache = self._load_cache()

    def _load_cache(self) -> dict[str, str]:
        if not CACHE_PATH.exists():
            return {}
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))

    def save_cache(self) -> None:
        CACHE_PATH.write_text(json.dumps(self.cache, ensure_ascii=False, indent=2), encoding="utf-8")

    def translate_many(self, texts: list[str]) -> list[str]:
        pending = [text for text in texts if text not in self.cache]
        total_pending = len(pending)

        for index, text in enumerate(pending, start=1):
            self.cache[text] = self._translate_with_retries(text)

            if index % TRANSLATION_BATCH_SIZE == 0 or index == total_pending:
                self.save_cache()
                print(f"  translated batch progress: {index}/{total_pending}", flush=True)

        return [self.cache[text] for text in texts]

    def translate_text_file(self, src: Path, dst: Path) -> None:
        if dst.exists() and not is_untranslated_copy(src, dst):
            print(f"skip txt {relative_ru_path(dst)}: already translated or edited", flush=True)
            return

        source_text = src.read_text(encoding="utf-8", errors="ignore")
        translated_text = self.translate_long_text(source_text)
        dst.write_text(translated_text, encoding="utf-8")
        print(f"translated txt {relative_ru_path(dst)}", flush=True)

    def translate_long_text(self, text: str) -> str:
        if not text.strip():
            return text

        chunks = chunk_text(text, TEXT_CHUNK_SIZE)
        translated_chunks = self.translate_many(chunks)
        return "".join(translated_chunks)

    def _translate_with_retries(self, text: str, retries: int = 3) -> str:
        last_error: Exception | None = None
        for attempt in range(retries):
            try:
                return self.client.translate(text)
            except Exception as exc:  # pragma: no cover - network instability path
                last_error = exc
                time.sleep(1.0 + attempt)
        raise RuntimeError(f"failed to translate text after {retries} attempts: {last_error}") from last_error


def chunk_text(text: str, max_chars: int) -> list[str]:
    raw_lines = text.splitlines(keepends=True)
    chunks: list[str] = []
    buffer = ""

    for line in raw_lines:
        if len(buffer) + len(line) > max_chars and buffer:
            chunks.append(buffer)
            buffer = ""

        if len(line) > max_chars:
            if buffer:
                chunks.append(buffer)
                buffer = ""
            for index in range(0, len(line), max_chars):
                chunks.append(line[index : index + max_chars])
            continue

        buffer += line

    if buffer:
        chunks.append(buffer)

    return chunks


def split_long_token(token: str, font: fitz.Font, font_size: float, max_width: float) -> list[str]:
    if not token:
        return [""]

    parts: list[str] = []
    current = ""
    for character in token:
        candidate = current + character
        if current and font.text_length(candidate, fontsize=font_size) > max_width:
            parts.append(current)
            current = character
        else:
            current = candidate
    if current:
        parts.append(current)
    return parts


def wrap_line(text: str, font: fitz.Font, font_size: float, max_width: float) -> list[str]:
    if not text:
        return [""]

    if font.text_length(text, fontsize=font_size) <= max_width:
        return [text]

    wrapped: list[str] = []
    current = ""

    for token in text.split():
        candidate = token if not current else f"{current} {token}"
        if font.text_length(candidate, fontsize=font_size) <= max_width:
            current = candidate
            continue

        if current:
            wrapped.append(current)
            current = ""

        if font.text_length(token, fontsize=font_size) <= max_width:
            current = token
            continue

        token_parts = split_long_token(token, font, font_size, max_width)
        wrapped.extend(token_parts[:-1])
        current = token_parts[-1]

    if current:
        wrapped.append(current)

    return wrapped or [""]


def create_text_page(doc: fitz.Document, title: str, page_number: int) -> fitz.Page:
    page = doc.new_page(width=PDF_PAGE_WIDTH, height=PDF_PAGE_HEIGHT)
    page.insert_font(fontname="ArialNarrowRU", fontfile=str(FONT_PATH))
    page.insert_text(
        (PDF_MARGIN, PDF_HEADER_Y),
        title,
        fontname="ArialNarrowRU",
        fontsize=PDF_HEADER_FONT_SIZE,
        color=(0.3, 0.3, 0.3),
    )
    page.insert_text(
        (PDF_PAGE_WIDTH - PDF_MARGIN - 20, PDF_HEADER_Y),
        str(page_number),
        fontname="ArialNarrowRU",
        fontsize=PDF_HEADER_FONT_SIZE,
        color=(0.3, 0.3, 0.3),
    )
    return page


def render_text_pdf(txt_path: Path, pdf_path: Path) -> None:
    text = txt_path.read_text(encoding="utf-8", errors="ignore").replace("\r\n", "\n")
    doc = fitz.open()
    font = fitz.Font(fontfile=str(FONT_PATH))
    max_width = PDF_PAGE_WIDTH - 2 * PDF_MARGIN

    page_number = 1
    page = create_text_page(doc, pdf_path.name, page_number)
    y = PDF_MARGIN + 18

    page_segments = text.split("\f")
    for segment_index, segment in enumerate(page_segments):
        for raw_line in segment.split("\n"):
            if not raw_line.strip():
                y += PDF_LINE_HEIGHT
            else:
                for wrapped_line in wrap_line(raw_line, font, PDF_BODY_FONT_SIZE, max_width):
                    if y > PDF_PAGE_HEIGHT - PDF_MARGIN:
                        page_number += 1
                        page = create_text_page(doc, pdf_path.name, page_number)
                        y = PDF_MARGIN + 18
                    page.insert_text(
                        (PDF_MARGIN, y),
                        wrapped_line,
                        fontname="ArialNarrowRU",
                        fontsize=PDF_BODY_FONT_SIZE,
                        color=(0, 0, 0),
                    )
                    y += PDF_LINE_HEIGHT

            if y > PDF_PAGE_HEIGHT - PDF_MARGIN:
                page_number += 1
                page = create_text_page(doc, pdf_path.name, page_number)
                y = PDF_MARGIN + 18

        if segment_index < len(page_segments) - 1:
            page_number += 1
            page = create_text_page(doc, pdf_path.name, page_number)
            y = PDF_MARGIN + 18

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(pdf_path, garbage=4, deflate=True)
    doc.close()


def render_translated_pdfs() -> None:
    for pdf_path in sorted(RU_ROOT.rglob("*.pdf")):
        txt_path = pdf_path.with_suffix(".txt")
        if not txt_path.exists():
            continue
        render_text_pdf(txt_path, pdf_path)
        print(f"rendered pdf {relative_ru_path(pdf_path)}", flush=True)


def candidate_font_sizes(base_size: float, source_text: str, translated_text: str) -> list[float]:
    capped = min(base_size, MAX_FONT_SIZE)
    length_ratio = len(source_text) / max(len(translated_text), 1)
    heuristic = max(MIN_FONT_SIZE, round(capped * min(1.0, max(0.45, length_ratio * 1.1)) * 2) / 2)

    sizes = [heuristic, capped]
    current = min(heuristic, capped)
    while current > MIN_FONT_SIZE:
        current = round(current - 0.5, 2)
        sizes.append(current)
    sizes.append(MIN_FONT_SIZE)

    unique_sizes: list[float] = []
    for size in sorted(set(size for size in sizes if size >= MIN_FONT_SIZE), reverse=True):
        unique_sizes.append(size)
    return unique_sizes


def extract_pdf_lines(page: fitz.Page) -> list[dict[str, object]]:
    items: list[dict[str, object]] = []
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block["lines"]:
            text = pdf_line_text(line)
            if not text or not should_translate_text(text):
                continue
            bbox = fitz.Rect(line["bbox"])
            font_size = max(span["size"] for span in line["spans"])
            items.append({"bbox": bbox, "font_size": font_size, "text": text})
    return items


def translate_pdf(src: Path, dst: Path, translator: Translator) -> None:
    if dst.exists() and not is_untranslated_copy(src, dst):
        print(f"skip pdf {relative_ru_path(dst)}: already translated or edited", flush=True)
        return

    print(f"translate pdf {src.relative_to(ROOT)} -> {relative_ru_path(dst)}", flush=True)

    fit_doc = fitz.open()
    fit_page = fit_doc.new_page(width=400, height=600)
    fit_page.insert_font(fontname="ArialNarrowRU", fontfile=str(FONT_PATH))

    doc = fitz.open(src)
    unique_texts: dict[str, str] = {}
    page_items: list[list[dict[str, object]]] = []

    for page_index, page in enumerate(doc):
        items = extract_pdf_lines(page)
        page_items.append(items)
        for item in items:
            unique_texts.setdefault(item["text"], item["text"])
        print(f"  collected page {page_index + 1}/{doc.page_count}: {len(items)} line(s)", flush=True)

    translated_lookup: dict[str, str] = {}
    if unique_texts:
        translated_values = translator.translate_many(list(unique_texts))
        translated_lookup = dict(zip(unique_texts, translated_values, strict=True))

    for page_index, (page, items) in enumerate(zip(doc, page_items, strict=True)):
        page.insert_font(fontname="ArialNarrowRU", fontfile=str(FONT_PATH))
        for item in items:
            target = item["bbox"] + (-1, -1, 2, 2)
            page.add_redact_annot(target, fill=(1, 1, 1))
        page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
        page.insert_font(fontname="ArialNarrowRU", fontfile=str(FONT_PATH))

        for item in items:
            source_text = item["text"]
            translated_text = translated_lookup[source_text]
            target = item["bbox"] + (-1, -1, 2, 2)
            chosen_size = MIN_FONT_SIZE

            for size in candidate_font_sizes(item["font_size"], source_text, translated_text):
                fit_page.clean_contents()
                fit_page.insert_font(fontname="ArialNarrowRU", fontfile=str(FONT_PATH))
                rc = fit_page.insert_textbox(target, translated_text, fontname="ArialNarrowRU", fontsize=size, align=0)
                if rc >= 0:
                    chosen_size = size
                    break

            page.insert_textbox(
                target,
                translated_text,
                fontname="ArialNarrowRU",
                fontsize=chosen_size,
                align=0,
                color=(0, 0, 0),
                overlay=True,
            )

        print(f"  wrote page {page_index + 1}/{doc.page_count}", flush=True)

    dst.parent.mkdir(parents=True, exist_ok=True)
    doc.save(dst, garbage=4, deflate=True)
    fit_doc.close()
    doc.close()


def merge_pdfs(parts: list[Path], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    merged = pikepdf.Pdf.new()
    for part in parts:
        src_pdf = pikepdf.Pdf.open(part)
        merged.pages.extend(src_pdf.pages)
    merged.save(output)


def copy_pdf(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def extract_pdf_pages(src: Path, page_spec: str, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    run(["qpdf", str(src), "--pages", str(src), page_spec, "--", str(dst)])


def translate_pending_text_files(translator: Translator) -> None:
    for dst in sorted(RU_ROOT.rglob("*.txt")):
        src = EN_ROOT / dst.relative_to(RU_ROOT)
        if not src.exists():
            continue
        translator.translate_text_file(src, dst)


def build_haynes_sections(translator: Translator) -> None:
    src_dir = EN_ROOT / "haynes-manual" / "sections"
    dst_dir = RU_ROOT / "haynes-manual" / "sections"
    for section in HAYNES_SECTIONS:
        translate_pdf(src_dir / f"{section.slug}.pdf", dst_dir / f"{section.slug}.pdf", translator)

    merge_pdfs(
        [dst_dir / f"{section.slug}.pdf" for section in HAYNES_SECTIONS],
        RU_ROOT / "haynes-manual" / "honda-vf700-750-1100-haynes-searchable.pdf",
    )


def build_partslist_sections(translator: Translator) -> None:
    src_dir = EN_ROOT / "partslist-vf700s-sabre" / "sections"
    dst_dir = RU_ROOT / "partslist-vf700s-sabre" / "sections"
    for section in PARTSLIST_SECTIONS:
        translate_pdf(src_dir / f"{section.slug}.pdf", dst_dir / f"{section.slug}.pdf", translator)

    merge_pdfs(
        [dst_dir / f"{section.slug}.pdf" for section in PARTSLIST_SECTIONS],
        RU_ROOT / "partslist-vf700s-sabre" / "partslist-vf700s-sabre-searchable.pdf",
    )


def build_shop_manual_extracts(translator: Translator) -> None:
    src_dir = EN_ROOT / "carburetor-reference" / "manuals"
    dst_dir = RU_ROOT / "carburetor-reference" / "manuals"
    for slug in SHOP_MANUAL_EXTRACTS:
        translate_pdf(src_dir / f"{slug}.pdf", dst_dir / f"{slug}.pdf", translator)


def rebuild_reference_pdfs() -> None:
    haynes_sections_dir = RU_ROOT / "haynes-manual" / "sections"
    partslist_pdf = RU_ROOT / "partslist-vf700s-sabre" / "partslist-vf700s-sabre-searchable.pdf"
    haynes_pdf = RU_ROOT / "haynes-manual" / "honda-vf700-750-1100-haynes-searchable.pdf"

    carb_manuals_dir = RU_ROOT / "carburetor-reference" / "manuals"
    copy_pdf(haynes_sections_dir / "01-tune-up-and-routine-maintenance.pdf", carb_manuals_dir / "01-haynes-tune-up-and-routine-maintenance.pdf")
    copy_pdf(haynes_sections_dir / "04-fuel-and-exhaust-systems.pdf", carb_manuals_dir / "02-haynes-fuel-and-exhaust-systems.pdf")

    carb_parts_dir = RU_ROOT / "carburetor-reference" / "parts-catalog"
    extract_pdf_pages(partslist_pdf, "34-36", carb_parts_dir / "01-carburetor-assy-and-components.pdf")
    extract_pdf_pages(partslist_pdf, "41-42", carb_parts_dir / "02-throttle-and-choke-cables.pdf")
    extract_pdf_pages(partslist_pdf, "55-56", carb_parts_dir / "03-fuel-tank-and-fuel-valve.pdf")
    extract_pdf_pages(partslist_pdf, "59-60", carb_parts_dir / "04-air-cleaner.pdf")

    electrical_manuals_dir = RU_ROOT / "electrical-reference" / "manuals"
    copy_pdf(haynes_sections_dir / "05-ignition-system.pdf", electrical_manuals_dir / "01-ignition-system.pdf")
    copy_pdf(haynes_sections_dir / "08-electrical-system.pdf", electrical_manuals_dir / "02-electrical-system.pdf")
    extract_pdf_pages(haynes_pdf, "220-247", electrical_manuals_dir / "03-wiring-diagrams-all-models.pdf")
    extract_pdf_pages(haynes_pdf, "220-228", electrical_manuals_dir / "04-wiring-diagram-1982-750-sabre.pdf")

    electrical_parts_dir = RU_ROOT / "electrical-reference" / "parts-catalog"
    extract_pdf_pages(partslist_pdf, "39-41,59,68-71", electrical_parts_dir / "01-electrical-components.pdf")


def main() -> None:
    if not FONT_PATH.exists():
        raise FileNotFoundError(f"Font not found: {FONT_PATH}")

    translator = Translator()
    translate_pending_text_files(translator)
    render_translated_pdfs()
    translator.save_cache()


if __name__ == "__main__":
    main()
