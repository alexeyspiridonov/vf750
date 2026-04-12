#!/usr/bin/env python3

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "manuals" / "electrical-reference"
MANUALS_DIR = OUTPUT_DIR / "manuals"
PARTS_DIR = OUTPUT_DIR / "parts-catalog"

HAYNES_DIR = ROOT / "manuals" / "haynes-manual"
PARTSLIST_DIR = ROOT / "manuals" / "partslist-vf700s-sabre"
HAYNES_PDF = HAYNES_DIR / "honda-vf700-750-1100-haynes-searchable.pdf"
PARTSLIST_PDF = PARTSLIST_DIR / "partslist-vf700s-sabre-searchable.pdf"


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def ensure_source_outputs() -> None:
    if not HAYNES_PDF.exists():
        run(["python3", str(ROOT / "scripts" / "process_haynes_manual.py")])
    if not PARTSLIST_PDF.exists():
        run(["python3", str(ROOT / "scripts" / "process_partslist.py")])


def ensure_dirs() -> None:
    MANUALS_DIR.mkdir(parents=True, exist_ok=True)
    PARTS_DIR.mkdir(parents=True, exist_ok=True)


def copy_file(src: Path, dst: Path) -> None:
    shutil.copy2(src, dst)


def extract_pdf(src: Path, page_spec: str, dst_pdf: Path, dst_txt: Path) -> None:
    run(["qpdf", str(src), "--pages", str(src), page_spec, "--", str(dst_pdf)])
    run(["pdftotext", str(dst_pdf), str(dst_txt)])


def build_materials() -> list[dict[str, str]]:
    items: list[dict[str, str]] = []

    copies = [
        (
            HAYNES_DIR / "sections" / "05-ignition-system.pdf",
            MANUALS_DIR / "01-ignition-system.pdf",
        ),
        (
            HAYNES_DIR / "sections" / "05-ignition-system.txt",
            MANUALS_DIR / "01-ignition-system.txt",
        ),
        (
            HAYNES_DIR / "sections" / "08-electrical-system.pdf",
            MANUALS_DIR / "02-electrical-system.pdf",
        ),
        (
            HAYNES_DIR / "sections" / "08-electrical-system.txt",
            MANUALS_DIR / "02-electrical-system.txt",
        ),
    ]

    for src, dst in copies:
        copy_file(src, dst)
        items.append(
            {
                "type": "copy",
                "source": str(src.relative_to(ROOT)),
                "output": str(dst.relative_to(ROOT)),
            }
        )

    extracts = [
        (
            HAYNES_PDF,
            "220-247",
            MANUALS_DIR / "03-wiring-diagrams-all-models.pdf",
            MANUALS_DIR / "03-wiring-diagrams-all-models.txt",
            "All wiring diagram pages from the Haynes manual.",
        ),
        (
            HAYNES_PDF,
            "220-228",
            MANUALS_DIR / "04-wiring-diagram-1982-750-sabre.pdf",
            MANUALS_DIR / "04-wiring-diagram-1982-750-sabre.txt",
            "1982 750 Sabre wiring diagram pages from the Haynes manual.",
        ),
        (
            PARTSLIST_PDF,
            "39-41,59,68-71",
            PARTS_DIR / "01-electrical-components.pdf",
            PARTS_DIR / "01-electrical-components.txt",
            "84/85 VF700S electrical-related parts fiche pages: headlight, instruments, switches, battery, spark unit, signals, taillight, and wiring harness.",
        ),
    ]

    for src, page_spec, dst_pdf, dst_txt, note in extracts:
        extract_pdf(src, page_spec, dst_pdf, dst_txt)
        items.append(
            {
                "type": "extract",
                "source": str(src.relative_to(ROOT)),
                "pages": page_spec,
                "output_pdf": str(dst_pdf.relative_to(ROOT)),
                "output_txt": str(dst_txt.relative_to(ROOT)),
                "note": note,
            }
        )

    return items


def write_manifest(items: list[dict[str, str]]) -> None:
    payload = {
        "project_bike_context": "Honda Sabre cafe racer project. Local documentation covers multiple Sabre/Magna model years, so model-year differences must be verified before ordering parts or rewiring.",
        "sources": {
            "haynes_manual": str(HAYNES_PDF.relative_to(ROOT)),
            "parts_catalog": str(PARTSLIST_PDF.relative_to(ROOT)),
        },
        "outputs": items,
        "reference_docs": [
            "manuals/electrical-reference/notes/internet-sources.md",
            "manuals/electrical-reference/notes/common-issues.md",
            "manuals/cdi-reference/README.md",
            "manuals/cdi-reference/01-cdi-tech-and-timing.md",
            "manuals/cdi-reference/02-cdi-diagnostics-and-setup.md",
            "manuals/cdi-reference/03-cdi-replacement-options.md",
            "manuals/cdi-reference/sources.md",
        ],
        "notes": [
            "The parts catalog in this repository is specifically for the 1984-1985 VF700S Sabre.",
            "The Haynes manual covers 700/750/1100 V4 Sabre and Magna models, including the 1982 750 Sabre wiring diagrams.",
            "OCR on wiring diagrams and fiche pages is useful for search, but diagram pages remain visually primary documents.",
            "The stock VF750S ignition is better described as transistorized TCI / spark units than as classic CDI, even though owners often use CDI as a generic name.",
        ],
    }
    (OUTPUT_DIR / "manifest.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    ensure_source_outputs()
    ensure_dirs()
    items = build_materials()
    write_manifest(items)


if __name__ == "__main__":
    main()
