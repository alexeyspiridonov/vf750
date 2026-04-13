#!/usr/bin/env python3

from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE_PDF = ROOT / "pdf" / "Honda VF700,750,1100 v45,65 Sabre And Magna V-Fours 82-88 Haynes Service Manual Eng By Mosue.pdf"
TEMP_DIR = ROOT / ".ocr"
TEMP_OUTPUT_DIR = ROOT / ".output"
FINAL_DIR = ROOT / "output" / "haynes-manual"
SECTIONS_DIR = FINAL_DIR / "sections"

UNLOCKED_PDF = TEMP_DIR / "manual-unlocked.pdf"
SEARCHABLE_PDF = TEMP_OUTPUT_DIR / "honda-vf700-750-1100-haynes-searchable.pdf"
SEARCHABLE_TEXT = TEMP_DIR / "manual.txt"
FINAL_PDF = FINAL_DIR / "honda-vf700-750-1100-haynes-searchable.pdf"
FINAL_TEXT = FINAL_DIR / "honda-vf700-750-1100-haynes-searchable.txt"
MANIFEST_PATH = FINAL_DIR / "manifest.json"


@dataclass(frozen=True)
class Section:
    order: int
    title: str
    slug: str
    start_page: int
    end_page: int


SECTIONS = [
    Section(0, "Front Matter and Introductory Pages", "00-front-matter-and-introductory-pages", 1, 26),
    Section(1, "Tune-up and Routine Maintenance", "01-tune-up-and-routine-maintenance", 27, 47),
    Section(2, "Engine, Clutch and Transmission", "02-engine-clutch-and-transmission", 48, 99),
    Section(3, "Cooling System", "03-cooling-system", 100, 107),
    Section(4, "Fuel and Exhaust Systems", "04-fuel-and-exhaust-systems", 108, 131),
    Section(5, "Ignition System", "05-ignition-system", 132, 139),
    Section(6, "Frame, Suspension and Final Drive", "06-frame-suspension-and-final-drive", 140, 164),
    Section(7, "Brakes, Wheels and Tires", "07-brakes-wheels-and-tires", 165, 188),
    Section(8, "Electrical System", "08-electrical-system", 189, 247),
    Section(9, "Conversion Factors", "09-conversion-factors", 248, 248),
]


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def ensure_dirs() -> None:
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    SECTIONS_DIR.mkdir(parents=True, exist_ok=True)


def ensure_unlocked_pdf() -> None:
    if UNLOCKED_PDF.exists():
        return
    run(["qpdf", "--decrypt", str(SOURCE_PDF), str(UNLOCKED_PDF)])


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
            str(UNLOCKED_PDF),
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
            "The manual was OCR-processed with ocrmypdf after decrypting the original PDF wrapper with qpdf.",
            "Section boundaries were aligned to chapter title/content pages in the searchable PDF.",
        ],
    }
    MANIFEST_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    ensure_dirs()
    ensure_unlocked_pdf()
    ensure_searchable_pdf()
    publish_full_outputs()
    manifest = split_sections()
    write_manifest(manifest)


if __name__ == "__main__":
    main()
