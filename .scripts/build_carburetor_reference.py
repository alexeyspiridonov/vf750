#!/usr/bin/env python3

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "manuals" / "carburetor-reference"
MANUALS_DIR = OUTPUT_DIR / "manuals"
PARTS_DIR = OUTPUT_DIR / "parts-catalog"

HAYNES_DIR = ROOT / "manuals" / "haynes-manual"
PARTSLIST_DIR = ROOT / "manuals" / "partslist-vf700s-sabre"

SHOP_MANUAL_PDF = ROOT / "manuals" / "Honda V 45 SABRE-VF750S 1982 Shop Manual.pdf"
PARTSLIST_PDF = PARTSLIST_DIR / "partslist-vf700s-sabre-searchable.pdf"


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def ensure_sources() -> None:
    required = [
        HAYNES_DIR / "sections" / "01-tune-up-and-routine-maintenance.pdf",
        HAYNES_DIR / "sections" / "01-tune-up-and-routine-maintenance.txt",
        HAYNES_DIR / "sections" / "04-fuel-and-exhaust-systems.pdf",
        HAYNES_DIR / "sections" / "04-fuel-and-exhaust-systems.txt",
        SHOP_MANUAL_PDF,
        PARTSLIST_PDF,
    ]
    missing = [path for path in required if not path.exists()]
    if missing:
        joined = "\n".join(str(path) for path in missing)
        raise FileNotFoundError(f"Missing required source files:\n{joined}")


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
            HAYNES_DIR / "sections" / "01-tune-up-and-routine-maintenance.pdf",
            MANUALS_DIR / "01-haynes-tune-up-and-routine-maintenance.pdf",
        ),
        (
            HAYNES_DIR / "sections" / "01-tune-up-and-routine-maintenance.txt",
            MANUALS_DIR / "01-haynes-tune-up-and-routine-maintenance.txt",
        ),
        (
            HAYNES_DIR / "sections" / "04-fuel-and-exhaust-systems.pdf",
            MANUALS_DIR / "02-haynes-fuel-and-exhaust-systems.pdf",
        ),
        (
            HAYNES_DIR / "sections" / "04-fuel-and-exhaust-systems.txt",
            MANUALS_DIR / "02-haynes-fuel-and-exhaust-systems.txt",
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
            SHOP_MANUAL_PDF,
            "39-60",
            MANUALS_DIR / "03-shop-manual-maintenance.pdf",
            MANUALS_DIR / "03-shop-manual-maintenance.txt",
            "Factory maintenance chapter with spark plugs, valve clearance, carb synchronization, idle speed, choke, and air cleaner service.",
        ),
        (
            SHOP_MANUAL_PDF,
            "61-82",
            MANUALS_DIR / "04-shop-manual-fuel-system.pdf",
            MANUALS_DIR / "04-shop-manual-fuel-system.txt",
            "Factory fuel-system chapter with carburetor removal, disassembly, float level, pilot screw, fuel tank, automatic fuel valve, and air cleaner details.",
        ),
        (
            SHOP_MANUAL_PDF,
            "365-371",
            MANUALS_DIR / "05-shop-manual-1983-addendum-carb-updates.pdf",
            MANUALS_DIR / "05-shop-manual-1983-addendum-carb-updates.txt",
            "1983 addendum pages that update lubrication, maintenance, air cleaner, and fuel-system details for the V45 Sabre/Magna family.",
        ),
        (
            PARTSLIST_PDF,
            "34-36",
            PARTS_DIR / "01-carburetor-assy-and-components.pdf",
            PARTS_DIR / "01-carburetor-assy-and-components.txt",
            "84/85 VF700S fiche pages for carburetor assembly, carburetor linkages, and carburetor component breakdown.",
        ),
        (
            PARTSLIST_PDF,
            "41-42",
            PARTS_DIR / "02-throttle-and-choke-cables.pdf",
            PARTS_DIR / "02-throttle-and-choke-cables.txt",
            "84/85 VF700S fiche pages covering the control levers and throttle/choke cable assemblies.",
        ),
        (
            PARTSLIST_PDF,
            "55-56",
            PARTS_DIR / "03-fuel-tank-and-fuel-valve.pdf",
            PARTS_DIR / "03-fuel-tank-and-fuel-valve.txt",
            "84/85 VF700S fiche pages for the fuel tank, manual fuel valve, hoses, and strainer pieces that feed the carb rack.",
        ),
        (
            PARTSLIST_PDF,
            "59-60",
            PARTS_DIR / "04-air-cleaner.pdf",
            PARTS_DIR / "04-air-cleaner.txt",
            "84/85 VF700S fiche pages for the air cleaner case, element, ducting, breather tubes, and related hardware.",
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
        "project_bike_context": "Honda Sabre cafe racer project. This package consolidates carburetor-related material for V45 Sabre work, but the repository mixes 1982 VF750S factory material, multi-year Haynes coverage, and an 84/85 VF700S parts fiche.",
        "sources": {
            "haynes_manual": str((HAYNES_DIR / "honda-vf700-750-1100-haynes-searchable.pdf").relative_to(ROOT)),
            "shop_manual": str(SHOP_MANUAL_PDF.relative_to(ROOT)),
            "parts_catalog": str(PARTSLIST_PDF.relative_to(ROOT)),
        },
        "outputs": items,
        "notes": [
            "The Haynes manual covers multiple Sabre and Magna years, not only the 1982 VF750S.",
            "The factory shop manual covers the 1982 V45 Sabre/VF750S and V45 Magna/VF750C, with a 1983 addendum near the end.",
            "The local parts catalog is specifically for the 1984-1985 VF700S Sabre, so fiche part numbers must be year-checked before ordering for a 1982 VF750S.",
        ],
    }
    (OUTPUT_DIR / "manifest.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    ensure_sources()
    ensure_dirs()
    items = build_materials()
    write_manifest(items)


if __name__ == "__main__":
    main()
