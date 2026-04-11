# Honda Sabre 1982 Cafe Racer Project

This repository is the technical base for a `1982 Honda VF750S Sabre` to `cafe racer` conversion.

It collects service documentation, parts catalogs, research notes, and reference materials for the project.

## Project Goal

- Understand the stock V45 Sabre platform in detail.
- Prepare and organize all service documentation into a searchable, structured format.
- Research key conversion areas: front end, EFI, electrical, and overall cafe racer design.
- Plan the visual and technical conversion into a cafe racer.

## Repository Structure

```
pdf/                          source PDFs (manuals, parts lists)
output/
  haynes-manual/              Haynes service manual — OCR, searchable, split by section
  partslist-vf700s-sabre/     VF700S parts catalog — OCR, searchable, split by section
  electrical-reference/       electrical materials collected into one package
scripts/                      Python scripts for PDF processing
images/                       reference images: stock, cafe-racer, Pinterest board downloads
howto.md                      common maintenance / repair / modification tasks
problems.txt                  common VF750 problems and fixes (English)
```

## Documentation

### Source PDFs

- [Honda VF700/750/1100 Haynes service manual](pdf/Honda%20VF700,750,1100%20v45,65%20Sabre%20And%20Magna%20V-Fours%2082-88%20Haynes%20Service%20Manual%20Eng%20By%20Mosue.pdf)
- [VF700S Sabre parts list (1984–1985)](pdf/partslist-vf700s-sabre_84-85_en-11082016-0807.pdf)

### Processed Output

The source PDFs have been converted into searchable PDFs with OCR text layers and split into sections:

- **Haynes manual** — 10 sections from front matter through electrical system and conversion factors.
- **Parts catalog** — 5 sections: front matter, engine (B1), frame (E1), part number index, description index.
- **Electrical reference** — a combined package with ignition system, electrical system, wiring diagrams (all models + 1982 750 Sabre specifically), electrical parts catalog, and troubleshooting notes.

Each output folder contains a `manifest.json` with source mappings and page ranges.

### Processing Scripts

- `scripts/process_haynes_manual.py` — OCR and split the Haynes service manual.
- `scripts/process_partslist.py` — OCR and split the parts catalog.
- `scripts/build_electrical_reference.py` — assemble the electrical reference package.

## Research Notes

| File | Topic |
|------|-------|
| `fork swap.txt` | Modern front-end conversion options for the VF750S / VF700S Sabre. Confirmed builds, donor parts, and warnings. |
| `ecu swap.txt` | EFI conversion research: throttle body options, ECU choices (Speeduino, Megasquirt, etc.), sensor requirements. |
| `sabre-cafe-racer-projects.txt` | Curated list of real Sabre cafe racer builds with links and analysis (Perry, HackAWeek, Balkan Moto, K-Speed, etc.). |
| `resources.txt` | Forums, wikis, parts sources, Facebook groups, Reddit, and YouTube channels for the VF750 platform. |
| `problems.txt` | Common VF750 / V45 platform problems with symptoms, causes, and practical fixes. |
| `howto.md` | Workshop-oriented how-to guide for common maintenance, diagnostics, repairs, and cafe racer conversion tasks. |

## Practical Guides

- `howto.md` consolidates the most typical jobs for the platform: valve adjustment, cam inspection, top-end oil mod, carb cleaning and sync, charging system checks, cooling service, clutch work, suspension service, shaft drive maintenance, brake service, and common cafe racer fabrication tasks.
- `problems.txt` summarizes the recurring failure points of the VF750 family: cam wear, top-end oiling, cam chain tensioners, charging system, carburetors, CDI failures, Pro-Link wear, and related troubleshooting.

## Image References

The `images/` folder now includes several reference groups:

- `images/stock/` — stock Sabre reference photos.
- `images/cafe-racer/` — collected Sabre cafe racer build photos.
- `images/pinterest/` — downloaded images from the `saber` Pinterest board for visual comparison and inspiration.
- root-level image files in `images/` — previously collected standalone references.

## Key References

- **[V4MuscleBike](https://v4musclebike.com/forums/)** — main community forum for the V45/V65 Sabre and Magna platform.
- **[VF1000 Forum / VF750 section](https://forum.vf1000.com/c/vf750/12)** — technical discussions including EFI and swap threads.
- **[V4 Honda BBS](https://www.v4hondabbs.com)** — general V4 Honda forum.
- **[CMSNL](https://www.cmsnl.com)** — parts diagrams and Honda microfiche.
- **[Partzilla](https://www.partzilla.com)** — OEM parts lookup.
- **Perry / 1984 VF700S Sabre Cafe** ([Inazuma Cafe](https://www.inazumacafe.com/2016/10/vf750-sabre-cafe.html), [CafeRacer.net](https://www.caferacer.net/threads/1984-honda-honda-vf700s-sabre-cafe.28714/)) — the most thoroughly documented modern front-end conversion on a Sabre.
- **HackAWeek / 1985 VF700S** ([site](https://hackaweek.com/hacks/the-1985-honda-vf700s-sabre-cafe-racer-conversion-begins/), [YouTube](https://www.youtube.com/watch?v=-bHv8hUwE5k)) — the best long-form video build series for a Sabre cafe racer.
- **[Balkan Moto / V45 Sabre](https://balkanmoto.com/builds/1982-83-honda-sabre-v45-cafe-racer.php)** — honest DIY build with lessons learned on the 1982–83 Sabre.

## Status

Active working repository for the `1982 Honda Sabre cafe racer` project.

Current state:

- source manuals have been processed into searchable, sectioned outputs;
- research notes cover EFI, front-end swaps, project references, and community resources;
- a practical service and modification guide has been added in `howto.md`;
- common VF750 issues have been consolidated in English in `problems.txt`;
- image references are now organized into stock, custom, and Pinterest-derived sets.
