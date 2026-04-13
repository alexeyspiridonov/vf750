# VF750 EFI Swap Notes

These are the real VF750 EFI swap discussions and solution directions collected so far.

## Source Threads

1. [EFI swapping VF750 (GSXR throttle bodies)](https://forum.vf1000.com/t/efi-swapping-my-interceptor/5487)
   Plan: use GSXR750 throttle bodies and split them into a 2+2 layout for the V4.

2. [Converting carbs to fuel injection (VF750 Sabre)](https://v4musclebike.com/threads/converting-carbs-to-fuel-injection.44405/)
   Full carb-to-EFI conversion discussion. It confirms that people have done it, but there are very few fully documented finished projects.

3. [EFI conversion discussion for Honda V4 (Megasquirt)](https://forum.vf1000.com/t/efi-conversion/1856)
   Main idea discussed:
   - individual throttle bodies
   - GSXR injectors
   - Megasquirt ECU
   - expected gain in the +5 to 15 hp range

4. [VF750 EFI discussions (general list)](https://forum.vf1000.com/c/vf750/12)
   Broader VF750 category that includes EFI and swap-related threads.

## EFI Layout Options for the VF750

### Option 1: Individual throttle bodies

This is the most common serious EFI direction for a V4.

#### Concept
- 4 throttle bodies
- 4 injectors
- standalone ECU
- custom fuel rail

#### Typical donor parts
- GSXR600/750 throttle bodies
- CBR600 throttle bodies
- R6 throttle bodies
- VFR800 throttle bodies

#### Pros
- most correct approach for a V4
- best throttle response
- easier to tune properly once packaged

#### Cons
- hard to package
- requires custom intake fabrication

### Option 2: Two throttle bodies (2+2 cylinders)

#### Layout
- front bank -> 1 throttle body
- rear bank -> 1 throttle body

#### Pros
- simpler
- less wiring
- easier synchronization

#### Cons
- worse throttle response
- uneven fueling risk

### Option 3: Single throttle body plus plenum

#### Layout
- 1 large throttle body
- plenum
- 4 runners

#### Pros
- simplest
- cheapest

#### Cons
- worse throttle response
- weak low-RPM behavior
- long intake path

### Option 4: Scooter throttle bodies

Popular DIY route when packaging under the tank is the main concern.

#### Common choices
- 28 mm scooter throttle bodies
- 30 mm scooter throttle bodies
- 32 mm scooter throttle bodies

#### Layout
- 4 small throttle bodies
- external injectors
- shared fuel pump

#### Pros
- compact
- cheap
- easier to fit under the tank

#### Cons
- limited flow
- needs real testing before committing

## ECUs Commonly Used

- Megasquirt
- Microsquirt
- Speeduino
- Ecotrons
- Ignitech EFI

Most common in forum discussions: Speeduino.

## Required Sensors

- TPS — mandatory
- MAP — one shared sensor or four individual signals
- CLT — engine temperature
- IAT — intake air temperature
- O2 — recommended

## Fuel System Requirements

You need to add:

- 3 bar fuel pump
- return line
- fuel pressure regulator
- 180 to 240 cc injectors

### Injectors commonly used

- GSXR600
- CBR600
- R6
- SV650
- VFR800

Typical conclusion from the collected notes: 200 cc is usually enough.

## Main EFI Problems on the VF750

1. Very little room under the tank
2. Difficult V4 intake packaging
3. Bank-to-bank synchronization
4. Weak vacuum signal on a V4
5. The old charging system is not very strong

## Most Promising VF750 Setup

### Best full setup

- 4 x 32 mm throttle bodies
- Speeduino
- shared MAP
- single TPS
- 4 x 220 cc injectors
- custom fuel rail

### Minimum EFI swap

Simplest possible setup:

- 2 throttle bodies
- 2 injectors
- batch fire
- Speeduino

### Most interesting compact solution

- 4 scooter throttle bodies
- external injectors
- small airbox
- Speeduino

Why it stands out:

- very compact
- more likely to fit under the tank
