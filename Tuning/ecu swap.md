# VF750 EFI / ECU Swap Planning

Collected and verified notes.

Checked: 2026-04-29

## Scope

- project bike context: 1982 Honda VF750S / V45 Sabre
- stock system: four CV carburetors, no engine ECU, separate transistorized spark units
- focus: converting from carburetors to electronic fuel injection with a standalone ECU
- updated with V4MuscleBike EFI and ignition research

## Short Answer

There is no clean, finished, repeatable V45 Sabre EFI conversion recipe confirmed on V4MuscleBike.

The forum evidence says the swap is possible, but the practical consensus is conservative: clean, sealed, correctly tuned carbs are the best rider solution unless the project goal is experimentation, turbo work, altitude compensation, or long-term parts independence.

### Practical conclusion

- if the bike needs to run well this season, rebuild and tune the carb rack
- if the bike is a long-term custom project, EFI is possible but should be treated as a full fuel-system, intake, wiring, sensor, charging, and tuning project
- do not think of this as an "ECU swap"; the VF750S does not have a stock fuel ECU to swap
- an EFI conversion can keep the stock spark units at first, which reduces risk
- replacing both fuel and ignition control at once creates too many first-start variables

## Best Forum Evidence Found

### 1. V4MuscleBike: 1983 VF750S EFI question

Status: strongest direct V45 Sabre forum thread found.

#### What it shows

- the original question is from a `1983 Sabre VF750S` owner asking whether carb-to-EFI conversion is possible
- members point to prior attempts, but not a polished finished recipe
- Speeduino-style DIY EFI is treated as possible, not easy
- experienced members argue that a properly serviced V4 carb rack is usually the better normal-use path
- the V4 geometry, multiple banks, packaging, and tuning work make the project much larger than it first appears

#### Why this matters

This thread is useful mostly as a decision filter. It does not give a bolt-on shopping list for a VF750S; it says the project is in custom-fabrication territory.

#### Source

- [Converting carbs to fuel injection](https://v4musclebike.com/threads/converting-carbs-to-fuel-injection.44405/)

### 2. VF / VFR community EFI experiments

Status: useful concept references, not direct Sabre proof.

#### Common ideas

- split GSXR throttle bodies into a V4-friendly layout
- run individual throttle bodies
- use Megasquirt / MicroSquirt / Speeduino-style standalone control
- start with batch or bank injection before chasing sequential injection

#### Important limitation

Most of these examples are VF/VFR-adjacent or Interceptor-focused. They help with architecture, but they do not prove that a donor throttle body set fits under a Sabre tank.

#### Sources

- [EFI swapping VF750](https://forum.vf1000.com/t/efi-swapping-my-interceptor/5487)
- [EFI conversion discussion for Honda V4](https://forum.vf1000.com/t/efi-conversion/1856)

## What The Stock Bike Gives You

The VF750S is a carbureted motorcycle with a separate ignition system:

- four carburetors in a tight V4 intake package
- vacuum-operated fuel valve on the Sabre fuel system
- no high-pressure pump, return line, or fuel rail
- two pulse generator coils
- two spark units
- two ignition coils
- wasted-spark operation
- ignition timing checked by strobe, not adjusted mechanically

This is why an EFI conversion has two possible directions:

- fuel-only EFI while keeping the stock spark units
- full fuel-and-ignition control using the standalone ECU or a separate programmable ignition

Fuel-only is the better first prototype.

## Architecture Options

### Option 1: Fuel-only EFI, stock ignition retained

This is the lowest-risk experimental path.

#### Concept

- standalone ECU controls injectors and fuel pump relay
- stock Honda spark units continue to control ignition timing
- ECU receives a clean rpm signal for fueling only
- wideband oxygen sensor is used for tuning feedback

#### Pros

- fewer first-start variables
- stock ignition curve remains known
- easier to revert to carbs
- easier to diagnose if the bike will not start

#### Cons

- no ignition timing control
- rpm signal conditioning still has to be done correctly
- any weak stock ignition component remains in the system

### Option 2: EFI plus programmable ignition

This is a deeper custom path.

#### Concept

- ECU or programmable ignition controls spark timing
- stock spark units are removed or bypassed
- pickup signals, coil drivers, dwell, tach output, and kill logic must all be handled correctly

#### Pros

- full control of fuel and ignition
- better future path for turbo, high compression, or heavy engine changes
- one calibration can coordinate fuel and spark

#### Cons

- much higher wiring and setup risk
- wrong dwell or coil strategy can damage parts
- base timing must be locked and verified before tuning
- failure diagnosis becomes harder

If ignition control is the main goal, use the CDI / TCI notes first:

- [CDI testing and replacement](../HowTo/cdi-testing-and-replacement.md)
- [CDI replacement options](../Manuals/cdi-reference/03-cdi-replacement-options.md)

## Throttle Body Layouts

### 1. Four individual throttle bodies

Best technical direction for a V4.

Typical donor ideas:

- GSXR600 / GSXR750 throttle bodies
- CBR600 throttle bodies
- R6 throttle bodies
- VFR800 throttle bodies
- compact scooter throttle bodies in the `28 to 32 mm` range

Pros:

- best cylinder-to-cylinder control
- closest to a modern motorcycle EFI layout
- easiest to tune accurately once mechanically packaged

Cons:

- hard packaging under the tank
- custom intake boots or manifolds
- custom fuel rail work
- throttle linkage and cable routing become fabrication jobs

### 2. Split inline sportbike throttle bodies into a 2+2 layout

This is the common VF/VFR experiment idea.

Pros:

- donor parts are easy to find
- injectors, TPS, and rails may come as a package
- bank-by-bank packaging can be more realistic than one rigid inline rack

Cons:

- spacing rarely matches the Honda V4 intake directly
- rails and throttle linkage usually need modification
- bank synchronization still matters

### 3. Two throttle bodies

Possible, but less attractive.

Pros:

- simpler fabrication
- fewer injectors and less wiring
- easier fuel rail layout

Cons:

- weaker throttle response
- uneven mixture risk
- harder to make the engine feel like a clean V4

### 4. Single throttle body plus plenum

This is the simplest layout, but not the best motorcycle solution.

Pros:

- one throttle body
- one TPS
- simpler cable routing

Cons:

- plenum volume and runner length become hard to get right
- low-rpm response can suffer
- packaging may still be worse than expected

## ECU Choices

### Speeduino

Best use case:

- DIY-friendly experimental build
- owner is comfortable with open-source hardware, wiring, firmware, and tuning
- project can tolerate iteration

Why it fits the research:

- V4MuscleBike mentions Speeduino-style DIY EFI as a plausible path
- Speeduino is an open-source engine-management project with hardware, firmware, and software components

Watch-outs:

- board quality and enclosure quality vary
- input protection, grounds, and noise control matter a lot on a motorcycle
- support depends on the exact board and firmware path chosen

Source:

- [Speeduino GitHub](https://github.com/speeduino/speeduino)

### MicroSquirt / MegaSquirt

Best use case:

- more mature standalone path
- weather-resistant motorcycle-sized ECU is preferred
- batch or bank injection is acceptable

Why it fits:

- MicroSquirt is commonly used on small engines and powersports projects
- MicroSquirt targets batch-fire or semi-sequential fueling and wasted-spark ignition, which matches a conservative V4 first build better than chasing full sequential injection immediately

Watch-outs:

- still needs proper trigger setup and wiring
- not a plug-and-play VF750S kit
- tuning discipline matters more than the brand name

Sources:

- [MicroSquirt product information](https://www.msextra.com/product-range/microsquirt/)
- [MegaSquirt fuel-injection modes](https://www.megamanual.com/v22manual/mfuel.htm)

### Ignitech EFI / ignition-adjacent paths

Ignitech is more relevant in this repo for programmable ignition than for a proven VF750S EFI conversion.

Use Ignitech notes when the goal is spark control:

- [Ignitech SPARKER TCI](https://www.ignitech.cz/en/vyrobky/tci/tci.htm)
- [Ignitech SPARKER TCIP4](https://www.ignitech.cz/en/vyrobky/tcip/tcip.htm)

## Required Sensors And Signals

### Minimum for a practical EFI build

- TPS
- MAP or alpha-N strategy
- CLT / engine temperature
- IAT
- wideband O2 for tuning
- crank or rpm signal
- battery voltage input

### Strongly recommended

- barometric correction if altitude use matters
- fuel pressure gauge during setup
- ECU-controlled fuel-pump relay
- fused ECU and injector power
- clean sensor ground strategy

### MAP signal warning

A V4 with individual throttles can produce a pulsing MAP signal. Plan for:

- a small vacuum manifold
- restrictors if needed
- alpha-N or blended alpha-N / speed-density tuning if MAP is unstable

## Fuel System Requirements

EFI requires a high-pressure fuel system. The stock carb fuel path is not enough.

Plan for:

- EFI-rated fuel hose
- high-pressure fuel pump
- pre-filter and post-filter as required by the pump
- fuel pressure regulator
- return line or returnless regulator strategy
- injector bungs or throttle bodies with injectors
- leak-free fuel rails
- pump relay and fuse
- safe routing away from heat and sharp edges

### Injector sizing

The old note range of `180 to 240 cc/min` is a reasonable starting research band, but do not buy injectors from that number alone.

Calculate from:

- real horsepower target
- brake specific fuel consumption assumption
- number of injectors
- target duty cycle
- fuel pressure

For a near-stock VF750S, small sportbike injectors may be enough. For turbo or major engine work, recalculate.

## Electrical And Charging Constraints

The ECU will only be as reliable as the old Honda electrical system feeding it.

Do this before EFI:

- test the charging system
- repair the stator connector / three-yellow-wire path
- verify regulator/rectifier output
- clean battery, frame, and engine grounds
- remove sketchy prior-owner accessory wiring
- build a fused relay-fed ECU/injector/pump power path

Related local notes:

- [Charging system test](../HowTo/charging-system-test.md)
- [Stator connector repair](../HowTo/stator-connector-repair.md)
- [Regulator/rectifier upgrade](../HowTo/regulator-rectifier-upgrade.md)
- [Ground wire upgrade](../HowTo/ground-wire-upgrade.md)

## Packaging Constraints

Measure before buying parts.

Critical measurements:

- carb throat diameter and spacing
- intake boot angle
- distance from intake mouth to tank underside
- available airbox volume
- throttle cable route
- choke/enrichment removal strategy
- injector angle and rail clearance
- fuel-line entry and exit routes
- battery and electronics tray space
- heat exposure near rear cylinders

Mock the throttle bodies in cardboard, plastic, or scrap plate before cutting manifolds.

## Recommended Build Order

1. Make the engine run correctly on carbs first.
2. Set valves, compression-check if needed, and confirm spark on all four cylinders.
3. Repair charging and grounds.
4. Decide fuel-only EFI or full fuel-and-ignition control.
5. Choose throttle body layout and mock it under the tank.
6. Build the high-pressure fuel system outside the bike and pressure-test it.
7. Build the ECU harness on the bench with fuses and relays.
8. Confirm TPS, temperature sensors, O2, and rpm signal in software before first start.
9. Start on conservative fuel-only settings if possible.
10. Tune idle, warmup, low throttle, and cruise before wide-open throttle.
11. Add ignition control only after the fuel side is repeatable.

## Decision Matrix

### Best rider decision

Rebuild and tune the carb rack.

Use:

- [Carburetor cleaning](../HowTo/carburetor-cleaning.md)
- [Carburetor installation](../HowTo/carburetor-installation.md)
- [Carburetor synchronization](../HowTo/carburetor-synchronization.md)

### Best experimental EFI decision

Fuel-only EFI first, stock ignition retained, wideband O2 installed, complete carb rack kept on the shelf.

### Best high-modification decision

Full standalone fuel and ignition only if the bike is already getting major intake, exhaust, turbo, compression, or wiring changes.

### Highest mistake risk

Buying an ECU first, then trying to make random throttle bodies fit later.

## 2026-04-29 V4MuscleBike Update Summary

- The direct V45 Sabre EFI thread does not show a finished plug-and-play conversion.
- Forum advice strongly favors proper carb service for normal road use.
- Speeduino / Megasquirt-style EFI is plausible, but the V4 packaging and tuning workload are the real project.
- Do not combine EFI troubleshooting with unknown ignition, charging, and carb problems. Baseline the motorcycle first.

## Best Sources

- [V4MuscleBike - Converting carbs to fuel injection](https://v4musclebike.com/threads/converting-carbs-to-fuel-injection.44405/)
- [VF1000 - EFI swapping VF750](https://forum.vf1000.com/t/efi-swapping-my-interceptor/5487)
- [VF1000 - EFI conversion discussion](https://forum.vf1000.com/t/efi-conversion/1856)
- [Speeduino official repository](https://github.com/speeduino/speeduino)
- [MicroSquirt product information](https://www.msextra.com/product-range/microsquirt/)
- [MegaSquirt injection mode reference](https://www.megamanual.com/v22manual/mfuel.htm)
- [V4MuscleBike upgrade research map](v4musclebike-upgrade-research.md)
- [CDI / Spark Unit reference package](../Manuals/cdi-reference/README.md)
