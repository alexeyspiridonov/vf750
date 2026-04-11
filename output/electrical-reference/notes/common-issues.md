# Common Electrical Issues

This is the high-signal summary for the Sabre platform based on the local manuals and the forum material collected in this project.

## 1. Charging Problems Are Very Often Connector Problems First

The recurring pattern across the Sabre and Magna V4 forums is:

- inspect the regulator/rectifier connectors first;
- inspect the 3 yellow stator wires first;
- inspect for heat damage, corrosion, looseness, or melted plastic first;
- only then move on to stator and regulator/rectifier testing.

Relevant sources:
- `manuals/02-electrical-system.pdf`
- `internet-sources.md` -> `Charging question - is this normal, or a sign?`
- `internet-sources.md` -> `Melted Regulator/Rectifier Plug`
- `internet-sources.md` -> `3 yellow wire fix`

## 2. The 3 Yellow Wire Connector Is A Known Weak Point

The stator-to-regulator 3-phase connector is a known heat and corrosion point on these bikes.

Typical failure pattern:
- connector oxidizes;
- resistance rises;
- connector heats up;
- plastic melts or hardens;
- charging drops or becomes intermittent.

Common community fix:
- eliminate the old connector and hardwire the three yellow wires correctly;
- or replace the connector with a modern sealed high-quality connector;
- or upgrade the regulator/rectifier and connector system together.

## 3. The Main Fuse / Starter Solenoid Assembly Is Another Known Weak Point

The original dogbone fuse and old solenoid setup are common trouble spots.

Practical issues:
- dogbone fuse ages badly;
- aftermarket solenoids often use different terminal arrangements;
- wires can be pinned incorrectly even when the connector body fits;
- a wrong pinout can create a direct short to ground.

Important recurring advice:
- verify the wire positions before energizing the bike;
- do not assume aftermarket replacement pin order is correct;
- treat the 30A main fuse as the main bike fuse, not a starter-motor fuse.

Relevant sources:
- `manuals/02-electrical-system.pdf`
- `internet-sources.md` -> `Solenoid replacement, MAIN FUSE FIX!`
- `internet-sources.md` -> `Starter fuse blows when battery is connected V45 Sabre`
- `internet-sources.md` -> `VF700s Starter Selenoid Replacement`

## 4. Weak Or Missing Spark Is Often Not Just "Bad CDI"

The manuals and forum threads repeatedly point to several real causes:

- bad spark unit / CDI box;
- weak battery during cranking;
- bad power feed to the spark unit;
- bad ground to the spark unit or coil;
- failing pulse generators;
- bad coil or coil wiring;
- front/rear bank issues that also affect tach behavior.

One especially useful diagnostic clue:
- on these bikes, rear-bank ignition issues can affect the tachometer behavior.

Relevant sources:
- `manuals/01-ignition-system.pdf`
- `internet-sources.md` -> `82 saber v45 spark`
- `internet-sources.md` -> `84 vf 750 sabre ignition problem`

## 5. Pulse Generator Resistance Matters

The pulse generators age and can fail with heat and time.

When chasing no-spark or one-bank spark issues:
- measure the pulse generators against the manual spec;
- do not stop at continuity alone;
- compare front and rear bank behavior where possible.

Use:
- `manuals/01-ignition-system.pdf`

## 6. Harness Problems Are Often Old-Age Problems, Not One Bad Component

On these motorcycles the harness problems are often cumulative:

- oxidized connectors;
- brittle insulation;
- prior owner repairs;
- bad grounds;
- corroded fuse contacts;
- hacked accessory wiring;
- heat damage near charging components.

If the harness is badly compromised:
- rebuild it on a board using the old loom as a pattern;
- do not simplify the harness until the stock system is understood and running correctly.

Relevant source:
- `internet-sources.md` -> `Rebuild wiring harness?`

## 7. Model-Year Scope Matters

This repository mixes references for:
- 1982 750 Sabre electrical diagrams in the Haynes manual;
- 1984-1985 VF700S parts fiche in the local parts catalog;
- multiple Sabre/Magna years in the forum material.

Practical rule:
- use the 1982 Sabre wiring diagram first for the project bike;
- use the VF700S fiche only for shared component families or when comparing assemblies;
- verify year-specific part numbers before ordering.
