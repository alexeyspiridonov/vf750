# CDI / Spark Unit Tech And Timing

## 1. What The Bike Actually Uses

For the early V45 Sabre ignition, the local manuals describe a battery-fed transistorized ignition system with:

- two pulse generator coils;
- two spark units;
- two ignition HT coils;
- wasted-spark operation.

The two spark units handle the cylinder pairs:

- cylinders `1 and 3`;
- cylinders `2 and 4`.

The spark units are mounted at the rear of the bike under the seat / rear fender area on the early 700/750 Sabre family.

## 2. Stock Timing Data

For the `1982-1983 750 Sabre`, the local manual set gives the practical timing checkpoints below:

| Item | Value |
| --- | --- |
| Idle timing | `10° BTDC` at idle |
| Advance starts | about `1,500 rpm` |
| Full advance | `37° BTDC` at `3,300 rpm` |

These numbers line up across the local factory-maintenance OCR and the local Haynes ignition section.

## 3. What Is Known About The Stock Advance Curve

The factory and Haynes material give inspection checkpoints, not a full point-by-point internal map for the spark units.

Practical interpretation:

- the bike sits at about `10° BTDC` at idle;
- timing stays near base timing until roughly `1,500 rpm`;
- the spark units then ramp advance electronically;
- by `3,300 rpm`, the system should be at `37° BTDC`.

That means the service literature gives a reliable `start point` and `full-advance point`, but not the complete hidden OEM curve between those checkpoints.

## 4. Important System Specs For Diagnosis

Relevant local specs:

| Item | Value |
| --- | --- |
| Pulse generator nominal resistance | `480 ohms +/- 10%` |
| Haynes check range for 1982-1986 models | `450 to 550 ohms` |
| System type | `12 V transistorized ignition` |
| Timing adjustment | `none` |

Relevant wire pairs for the pulse generators in the local Haynes OCR:

- `white/yellow` and `yellow` for one pickup pair;
- `white/blue` and `blue` for the other pickup pair.

Because the OCR is imperfect, always confirm wire colors against the local wiring diagram before depinning or repinning anything.

## 5. What Is Not Adjustable On The Stock Bike

The local manuals are explicit on the functional point:

- there is no normal ignition timing adjustment procedure;
- the system is checked with a timing light only;
- if timing is wrong, a component is faulty and should be tested or replaced.

This matters because many old-bike ignition problems get misdiagnosed as "timing drift". On this platform, drift is usually not adjustment-related. It is usually:

- a bad spark unit;
- a weak pulse generator signal;
- poor voltage supply;
- poor grounds;
- coil or connector problems.

## 6. Practical Stock-Curve Summary

If you want one working target for a stock-running VF750S, it is this:

- healthy 12 V supply;
- both spark units firing their bank cleanly;
- base timing around `10° BTDC`;
- clean advance progression to `37° BTDC` by `3,300 rpm`.

Anything outside that should be treated as a fault first, not as a tuning opportunity.
