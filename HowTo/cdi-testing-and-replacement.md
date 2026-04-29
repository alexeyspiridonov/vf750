# CDI / TCI Spark Unit Testing And Replacement

Collected and verified notes.

Checked: 2026-04-29

## Scope

- project bike context: 1982 Honda VF750S / V45 Sabre
- Honda manual term: `spark unit`
- common forum terms: `CDI`, `igniter`, `black box`, `spark box`
- technical note: the stock VF750S system is a battery-fed transistorized / inductive ignition, so `TCI` is more accurate than classic capacitive-discharge `CDI`

## Short Answer

Do not start by buying a random universal CDI box.

The useful path is:

1. confirm the motorcycle has clean battery voltage, grounds, fuses, and switch power;
2. identify whether the fault is all four cylinders or one wasted-spark pair;
3. test pulse generators, coils, plug caps, HT leads, and spark-unit power;
4. only then replace the spark units with exact OEM, verified plug-and-play replacements, or a properly configured programmable TCI.

## Safety

- Keep fuel vapor away from spark testing.
- Use an insulated spark tester or a properly grounded spare plug.
- Do not crank with loose plug leads arcing near the tank or fuel bowls.
- Do not leave ignition powered for long periods with the engine stopped.
- Disconnect the battery before depinning connectors or changing ignition boxes.

## What The System Looks Like

The early VF750S ignition uses:

- two pulse generator coils;
- two spark units;
- two ignition HT coils;
- wasted-spark cylinder pairs;
- no normal timing adjustment.

Relevant stock timing checkpoints:

- idle timing: about `10 degrees BTDC`;
- advance begins after roughly `1,500 rpm`;
- full advance: about `37 degrees BTDC` by `3,300 rpm`.

Relevant pickup spec from the local manuals:

- pulse generator nominal resistance: `480 ohms +/- 10%`;
- Haynes check range for 1982-1986 models: `450 to 550 ohms`.

Use the local wiring diagram before depinning anything:

- `../Manuals/electrical-reference/manuals/04-wiring-diagram-1982-750-sabre.pdf`
- `../Manuals/cdi-reference/01-cdi-tech-and-timing.md`

## Common Failure Patterns

### No spark on all four cylinders

Most likely areas:

- low battery voltage during cranking;
- main fuse / starter-solenoid fuse trouble;
- ignition switch or kill switch;
- missing switched 12 V feed to the spark units or coils;
- bad common ground;
- connector corrosion.

### One cylinder pair is dead

Most likely areas:

- one spark unit;
- one pulse generator pair;
- one ignition coil;
- one plug-cap / HT-lead path;
- bank-specific connector or harness damage.

The local CDI reference maps the early 750 Sabre spark units to cylinder pairs:

- cylinders `1 and 3`;
- cylinders `2 and 4`.

### Misfire or shutdown gets worse hot

Most useful suspects:

- pulse generator resistance drifting hot;
- spark unit breaking down with heat or vibration;
- connector resistance rising with heat;
- weak charging voltage once the bike is warm;
- fuel starvation masquerading as ignition failure.

V4MuscleBike's `Here we go again` thread is a good warning example: a V45 Sabre owner installed an Ignitech TCIP4 after recurring igniter suspicion, but the discussion still pushed the diagnosis toward pulse generators, fuel delivery, and model-specific fuel-system logic. On the V45 Sabre, do not blindly follow Magna fuel-pump advice because the Sabre fuel system is different.

### Tachometer behaves strangely

Forum notes repeatedly connect rear-bank ignition faults with tachometer behavior. Treat it as a clue, not proof. Still test the wiring, pickups, coils, and spark units.

## Tools

- fully charged battery;
- multimeter;
- spark tester or spare known-good plug;
- timing light;
- wiring diagram;
- small probes or back-probe leads;
- contact cleaner;
- dielectric grease for reassembly, not as a conductor;
- notebook for cold and hot resistance readings.

## Diagnostic Procedure

### 1. Confirm battery and main power

Before testing ignition modules:

- charge the battery fully;
- measure voltage at rest;
- measure voltage while cranking;
- inspect the main fuse and starter-solenoid area;
- inspect the ignition switch and kill switch function.

Weak cranking voltage can look like bad ignition.

### 2. Inspect grounds and connectors

Clean and verify:

- battery negative to engine;
- battery negative to frame if present;
- coil grounds / mounting condition;
- spark-unit connectors;
- pulse-generator connectors;
- coil primary connectors;
- any prior-owner splices.

Do not skip this step. Old connector resistance is one of the recurring V4 failure themes.

### 3. Check spark on all four cylinders

Use the same method on each cylinder and write down the result.

Record:

- no spark on all four;
- weak spark on all four;
- no spark on one pair;
- intermittent spark after heat soak;
- spark present but engine still does not fire.

This split decides the next branch.

### 4. Identify the dead pair

If only two cylinders are dead, identify whether the dead pair follows the Honda wasted-spark grouping.

Then compare:

- spark output bank to bank;
- coil primary feed bank to bank;
- coil resistance bank to bank;
- pulse generator resistance bank to bank;
- connector condition bank to bank.

### 5. Measure the pulse generators cold

Measure both pulse generator circuits against the manual range.

Working target:

- `450 to 550 ohms` is the Haynes range for the 1982-1986 models;
- the Honda reference value is about `480 ohms +/- 10%`.

Continuity alone is not enough.

### 6. Measure the pulse generators hot if the fault is heat-related

If the bike runs cold and dies hot:

- ride or heat-soak until the fault appears;
- shut down safely;
- measure the pulse generators immediately;
- compare against the cold values.

A pickup can test acceptably cold and fail hot.

### 7. Check coils, plug caps, and HT leads

Follow the ignition manual for primary and secondary resistance.

Also inspect:

- cracked plug caps;
- loose HT leads;
- green corrosion at coil terminals;
- wrong resistance caps;
- old plugs masking the real spark quality.

### 8. Confirm power to the spark units

With the wiring diagram, verify that switched ignition power reaches the spark units and coils during cranking and running.

Check for voltage drop, not just open-circuit voltage. A corroded connector can read fine with no load and fail under use.

### 9. Swap spark units only if the connectors and part strategy allow it

If the two stock boxes are the same connector format and compatible for a quick isolation test:

- mark both boxes before removing them;
- swap them;
- test whether the dead cylinder pair follows the box.

If the fault follows the box, the box becomes the prime suspect.

Do not assume every year/model uses interchangeable boxes. Verify part numbers and connector colors.

### 10. Check timing with a strobe

Once the engine runs, verify:

- about `10 degrees BTDC` at idle;
- smooth advance;
- about `37 degrees BTDC` by `3,300 rpm`.

If timing is unstable or wrong, diagnose components. The stock system has no normal timing adjustment.

## Replacement Options

### Option A: Exact-code OEM or NOS spark units

Best when:

- the bike stays stock;
- the original harness is healthy;
- you can match the exact printed code and connector layout.

Pros:

- stock timing curve;
- easiest manual-based troubleshooting;
- least setup work.

Cons:

- used parts may already be heat-damaged;
- listings often mix VF years and models;
- no improvement to old connector or voltage-drop problems.

### Option B: Verified plug-and-play replacement modules

Best when:

- you want stock-style operation with newer electronics;
- you do not want to program timing maps;
- the vendor lists your exact model and box markings.

The CDI reference package tracks Carmo as a current stock-style replacement path, but verify your exact box codes before ordering.

Use:

- [CDI replacement options](../Manuals/cdi-reference/03-cdi-replacement-options.md)

### Option C: Ignitech SPARKER TCI

Best when:

- you want a modern inductive replacement;
- you want the system family to match the stock Honda TCI-style architecture;
- you do not need deep custom mapping.

Ignitech describes SPARKER TCI as inductive battery/transistor ignition for multi-cylinder carbureted motorcycles. That is the correct conceptual family for the VF750S, unlike a random capacitive CDI box.

### Option D: Ignitech TCIP4

Best when:

- you want programmable timing;
- the bike already has custom wiring work;
- you can verify pickup settings, coil strategy, and base timing.

V4MuscleBike has a direct V45 Sabre example where a 1982 VF750S owner installed a TCIP4. The bike starts and runs, but the thread is also a good warning: a programmable ignition does not remove the need to test pulse generators, fuel delivery, charging, and wiring.

First map rule:

- reproduce stock timing checkpoints first;
- confirm with a timing light;
- then tune one change at a time.

### Option E: Rae-San

Best current evidence:

- strong V65 forum support;
- several users report replacing two V65 boxes with a single Rae-San-style unit;
- the Rae-San PULSER TAI product is designed to use OEM inductive pickups and rotor on supported bikes.

Important limitation:

- V65 evidence is not automatic V45 VF750S plug-in evidence;
- contact the vendor and verify the exact VF750S application before buying.

### Option F: Generic capacitive CDI

Usually the wrong first move.

Reason:

- the stock VF750S system is transistorized / inductive;
- CDI coil requirements and wiring strategy differ;
- a cheap universal CDI can create a new fault instead of fixing the old one.

Treat capacitive CDI as a custom conversion only.

## Installation Checklist

Before fitting a replacement box:

- photograph every connector;
- label the two original boxes;
- record printed codes and connector colors;
- clean the harness connectors;
- verify coil resistance and plug caps;
- verify pulse generator resistance cold, and hot if possible;
- verify charging voltage;
- mount the new module away from heat and water;
- protect the harness from seat-pan and rear-fender rub;
- keep the original boxes until the bike has passed road testing.

## First-Start Checklist After Replacement

1. Battery fully charged.
2. Fuel system confirmed.
3. Kill switch on.
4. All connectors seated.
5. Spark checked on all four cylinders.
6. Engine started and warmed gently.
7. Timing checked with a strobe.
8. Charging voltage checked.
9. Short ride only.
10. Hot restart tested.
11. Module and connector temperature checked after the ride.

## If The Problem Remains

### Still no spark

Return to:

- main fuse;
- ignition switch;
- kill switch;
- coil feed;
- spark-unit power;
- pickup signal.

### One bank still dead

Return to:

- pickup pair;
- coil;
- plug caps and HT leads;
- spark-unit connector;
- box compatibility.

### Runs cold, fails hot

Return to:

- pulse generators hot;
- charging output hot;
- connector voltage drop hot;
- fuel delivery;
- tank venting;
- vacuum-operated fuel valve.

### Runs, but badly

Do not immediately change timing. Confirm:

- valve clearances;
- compression;
- carb cleanliness;
- carb synchronization;
- intake leaks;
- fuel flow.

## Best Sources

- [CDI / Spark Unit tech and timing](../Manuals/cdi-reference/01-cdi-tech-and-timing.md)
- [CDI / Spark Unit diagnostics](../Manuals/cdi-reference/02-cdi-diagnostics-and-setup.md)
- [CDI / Spark Unit replacement options](../Manuals/cdi-reference/03-cdi-replacement-options.md)
- [V4MuscleBike - Here we go again](https://v4musclebike.com/threads/here-we-go-again.46903/)
- [V4MuscleBike - V4spark.com](https://v4musclebike.com/forums/showthread.php?p=531158)
- [V4MuscleBike - V65 CDI box](https://v4musclebike.com/forums/showthread.php?t=47554)
- [V4MuscleBike - Ideal ignition setup on V65](https://v4musclebike.com/threads/ideal-ignition-setup-on-v65.45321/)
- [V4MuscleBike - no spark at front cylinders](https://v4musclebike.com/showthread.php?t=5602)
- [V4MuscleBike - 84 VF750 Sabre ignition problem](https://v4musclebike.com/threads/84-vf-750-sabre-ignition-problem.32922/)
