#!/usr/bin/env python3

from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE_PDF = ROOT / "pdf" / "partslist-vf700s-sabre_84-85_en-11082016-0807.pdf"
TEMP_DIR = ROOT / ".ocr"
TEMP_OUTPUT_DIR = ROOT / ".output"
FINAL_DIR = ROOT / "output" / "partslist-vf700s-sabre"
SECTIONS_DIR = FINAL_DIR / "sections"

SEARCHABLE_PDF = TEMP_OUTPUT_DIR / "partslist-vf700s-sabre-searchable.pdf"
SEARCHABLE_TEXT = TEMP_DIR / "partslist-vf700s-sabre.txt"
FINAL_PDF = FINAL_DIR / "partslist-vf700s-sabre-searchable.pdf"
FINAL_TEXT = FINAL_DIR / "partslist-vf700s-sabre-searchable.txt"
MANIFEST_PATH = FINAL_DIR / "manifest.json"


@dataclass(frozen=True)
class Section:
    order: int
    title: str
    slug: str
    start_page: int
    end_page: int


SECTIONS = [
    Section(0, "Front Matter and Reference Pages", "00-front-matter-and-reference-pages", 1, 12),
    Section(1, "Engine Section (B1)", "01-engine-section-b1", 13, 38),
    Section(2, "Frame Section (E1)", "02-frame-section-e1", 39, 78),
    Section(3, "Part Number Index", "03-part-number-index", 79, 84),
    Section(4, "Description Index", "04-description-index", 85, 91),
]


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def ensure_dirs() -> None:
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    SECTIONS_DIR.mkdir(parents=True, exist_ok=True)


def ensure_searchable_pdf() -> None:
    if SEARCHABLE_PDF.exists() and SEARCHABLE_TEXT.exists():
        return
    run(
        [
            "ocrmypdf",
            "--force-ocr",
            "--rotate-pages",
            "--deskew",
            "--optimize",
            "0",
            "--jobs",
            "4",
            "--skip-big",
            "50",
            "--sidecar",
            str(SEARCHABLE_TEXT),
            str(SOURCE_PDF),
            str(SEARCHABLE_PDF),
        ]
    )


def publish_full_outputs() -> None:
    shutil.copy2(SEARCHABLE_PDF, FINAL_PDF)
    shutil.copy2(SEARCHABLE_TEXT, FINAL_TEXT)


def split_sections() -> list[dict[str, object]]:
    manifest: list[dict[str, object]] = []
    for section in SECTIONS:
        pdf_path = SECTIONS_DIR / f"{section.slug}.pdf"
        txt_path = SECTIONS_DIR / f"{section.slug}.txt"
        run(
            [
                "qpdf",
                str(SEARCHABLE_PDF),
                "--pages",
                str(SEARCHABLE_PDF),
                f"{section.start_page}-{section.end_page}",
                "--",
                str(pdf_path),
            ]
        )
        run(["pdftotext", str(pdf_path), str(txt_path)])
        entry = {
            **asdict(section),
            "pdf_path": str(pdf_path.relative_to(ROOT)),
            "text_path": str(txt_path.relative_to(ROOT)),
        }
        manifest.append(entry)
    return manifest


def write_manifest(manifest: list[dict[str, object]]) -> None:
    payload = {
        "source_pdf": str(SOURCE_PDF.relative_to(ROOT)),
        "searchable_pdf": str(FINAL_PDF.relative_to(ROOT)),
        "searchable_text": str(FINAL_TEXT.relative_to(ROOT)),
        "sections": manifest,
        "notes": [
            "Page ranges are 1-based PDF page numbers.",
            "The parts catalog was OCR-processed with ocrmypdf because most fiche pages were image-only.",
            "Section boundaries were aligned to the top-level PDF outline: front matter, engine, frame, and indexes.",
        ],
    }
    MANIFEST_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    ensure_dirs()
    ensure_searchable_pdf()
    publish_full_outputs()
    manifest = split_sections()
    write_manifest(manifest)


if __name__ == "__main__":
    main()
