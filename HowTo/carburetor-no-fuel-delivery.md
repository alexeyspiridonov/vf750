# Carburetor no-fuel delivery troubleshooting

Models covered: VF750S / V45 Sabre first, with notes for V45 Magna and V65 bikes that use an electric fuel pump.

Source notes: Honda V45 fuel-system manual, Haynes fuel-system notes, and V4MuscleBike threads [Fuel Pump Operation](https://v4musclebike.com/threads/fuel-pump-operation.46998/), [Fuel Pump Troubleshooting](https://v4musclebike.com/threads/fuel-pump-troubleshooting.47087/), [Fuel Relay/Pump/Electrical Trouble](https://v4musclebike.com/threads/fuel-relay-pump-electrical-trouble-running-out-of-patience.29916/), and [1983 Magna V45 fuel pump removal](https://v4musclebike.com/threads/1983-magna-v45-fuel-pump-removal.42919/).

## Core idea

"The carb does not feed fuel" can mean three different things:

- no fuel reaches the carb rack;
- fuel reaches the rack, but one or more float bowls stay dry;
- bowls are full, but the pilot/enrichment circuits are clogged so the engine acts fuel-starved.

Do not start with jets or mixture screws. First prove where the fuel stops.

## Safety

- Work outside or with strong ventilation.
- Keep fuel away from sparks, heaters, cigarettes, and hot exhaust.
- Use a catch bottle or fuel-safe container whenever a hose is disconnected.
- Keep a fire extinguisher nearby.
- Do not leave an electric fuel pump hardwired while you walk away.
- Wipe spills before cranking.

## Step 1: check the float bowls

This is the fastest split between an upstream fuel problem and an internal carb problem.

1. Put the bike upright and stable.
2. Attach a short drain hose to one float-bowl drain if possible.
3. Open that bowl drain screw into a container.
4. Repeat for all four bowls.

Results:

- Fuel drains from all four bowls: the carb rack is receiving fuel. Look at pilot jets, starter/enrichment jets, air leaks, ignition, and sync.
- No fuel drains from any bowl: troubleshoot tank, petcock, vacuum fuel valve, fuel pump, relay, filter, and lines.
- Only some bowls are dry: fuel is reaching the rack, but there may be a blocked rail/T-joint, stuck float valve, blocked float-valve seat filter, or blocked bowl vent.

If the bowls are full but one pipe turns blue, the plug is white, and that cylinder is clearly hotter than the others, this is no longer a fuel-delivery-to-the-rack problem. Look for a cylinder-specific lean condition: a partly plugged pilot circuit, intake leak, incorrect pilot screw setting, diaphragm/slide fault, or incorrect carb assembly.

## Step 2: easy upstream checks

Do these before removing the carburetors:

- Enough fuel in the tank.
- Manual petcock/fuel valve set to `ON` or `RES`, not `OFF`.
- Fuel cap vent not blocked. As a quick test, open the cap and see whether flow improves.
- Fuel line not kinked under the tank or carb rack.
- Fuel filter not backwards, plugged, too small, or stacked with another restrictive filter.
- Tank outlet and internal screen not plugged with rust or tank sealer.
- Vacuum line to the automatic fuel valve connected and not cracked.
- Bowl drain screws closed after testing.

One common field failure is very simple: the petcock was left off after tank or carb work.

## If fuel is present but one cylinder runs lean

Fresh V4MuscleBike field example on a `1984 V30`: the bike started easily, idled well, and pulled with good power, but after a ride the front-right pipe turned blue and the plug looked whitish. The forum response was: if cylinder synchronization is valid, an idle-drop mixture adjustment can be tried on the affected cylinder, but that adjustment only has a small correction range.

Practical takeaways:

- A blue pipe is a heat warning; do not leave it for later.
- A white plug on one cylinder points to a lean condition or overheating on that cylinder.
- An IR thermometer helps confirm which cylinder is hotter and whether the adjustment helped.
- If idle-drop adjustment does not correct it, clean/rebuild the carb instead of chasing jet sizes.
- A common cause is partly plugged carb passages, especially the pilot/low-throttle circuit.

For the cleaning procedure, see [how to clear a plugged pilot circuit](carburetor-cleaning.md#how-to-clear-a-plugged-pilot-circuit).

If the symptom appears more under load than at idle, check the [CV piston, needle, and diaphragm](carburetor-cleaning.md#checking-cv-pistons-needles-and-diaphragms).

Source: [V4MuscleBike - Carb tuning](https://v4musclebike.com/threads/carb-tuning.48630/)

## V45 Sabre: automatic fuel valve check

The V45 Sabre uses a manual fuel valve plus an automatic vacuum-operated fuel valve. If the automatic valve does not see vacuum, fuel may not flow to the carburetors even when the manual valve is `ON`.

Manual-style check:

1. Turn the manual fuel valve `ON`.
2. Put a container under the fuel line going to the carburetors.
3. Disconnect the fuel tube from the carburetor side.
4. Expect only a small amount of residual fuel to drain without vacuum.
5. Disconnect the vacuum tube from the intake port.
6. Apply vacuum with a hand vacuum pump.
7. Fuel should flow while vacuum is applied.
8. Fuel should stop when vacuum is removed.

If it fails:

- clean the automatic fuel valve;
- check the valve diaphragm;
- check the vacuum hose;
- check that the hose is routed to the correct intake port;
- check for a blocked fuel valve, tank outlet, or fuel line.

If this hose was disconnected during carb sync or carb removal, the bike can have two problems at once: no fuel-valve vacuum and a major intake leak.

## Electric pump bikes: V45 Magna / V65 notes

Many Magna/V65 discussions do not apply directly to a V45 Sabre, but they are useful if your bike has an electric pump.

Important behavior:

- The pump is not supposed to run continuously just because the key is on.
- The relay is triggered by the ignition/spark-box signal, so the pump normally runs when the engine is cranking or running.
- The pump may click once or a few times when the key/kill switch is cycled, then stop if the line and bowls are already pressurized.
- At idle, a healthy pump may only click occasionally.
- A full carb rack can make a good pump appear silent because back-pressure stalls the pump.

Basic pump split:

1. Disconnect the fuel hose at the carb end and aim it into a fuel-safe container.
2. Crank the engine or use the manual's fuel-pump test procedure.
3. If needed, test the pump through the relay connector only long enough to measure flow.

Forum field note: several first-gen threads discuss jumping the relay output to run the pump for testing. Wire colors differ by model/year, so verify the wiring diagram before doing this. The V4MuscleBike V65 examples commonly discuss the white pump feed and black/green switched power at the relay, with a blue signal wire from the spark box.

Results:

- Pump runs and delivers fuel when jumped: pump and fuel path are probably OK; suspect fuel-cut relay, spark-box trigger, pulse-generator/coil signal, wiring, or grounds.
- Pump does not run when jumped: suspect pump, pump ground, connector, fuse/power feed, or a seized pump.
- Pump runs but delivers weak flow: suspect clogged tank outlet, petcock, reserve/aux tank outlet, filter, kinked hose, air leak on pump inlet, or failing pump valves/diaphragm.
- Pump clicks constantly and fuel floods: suspect float valves, float height, dirty seats, or an aftermarket pump with too much pressure.

Do not permanently bypass the fuel-cut relay on a street bike. The relay exists so the pump stops when the engine stops.

## If fuel reaches the carb inlet but bowls stay dry

Likely causes:

- stuck-closed float needles after storage;
- blocked float-valve seat filters;
- varnish in the carb inlet rail or T-joints;
- float height set too low;
- float installed wrong or binding on the bowl;
- blocked bowl vents or air vent tube;
- drain screws left open during testing;
- fuel hose connected to the wrong fitting after rack installation.

What to do:

1. Confirm fuel actually reaches the carb rack inlet.
2. Open each bowl drain while applying normal fuel supply.
3. Tap the bowl lightly only as a temporary diagnostic.
4. If a bowl stays dry, remove the rack and inspect the float valve, seat, and small filter.
5. Verify V45 Sabre float height: `8.3 mm`.

## If bowls are full but the engine acts starved

This is not a no-fuel-supply problem anymore. It is usually carb metering.

Likely causes:

- clogged pilot jets;
- clogged starter/enrichment jets;
- blocked pilot passages;
- air leaks at intake boots or vacuum caps;
- choke/enrichment cable not moving the plungers;
- slides/pistons stuck closed;
- diaphragm tabs not seated correctly;
- wrong jet/needle/spring positions after carb rebuild.

Symptoms:

- runs only on choke;
- starts on fuel sprayed into the intake but dies;
- idle will not respond to pilot screw changes;
- one or two cylinders stay cold;
- throttle response is delayed or flat.

At that point, clean the rack again and prove the pilot/enrichment circuits with compressed air and carb cleaner flow paths before changing jet sizes.

## Quick diagnostic shortcuts

### Temporary gravity feed

A small fuel-safe auxiliary tank feeding the carb inlet can separate upstream fuel delivery from carb-internal problems.

- If it runs from a temporary tank, the issue is upstream of the rack.
- If it still will not run with full bowls, the issue is inside the carbs or outside the fuel system.

Keep the temporary tank low-pressure and secure. Do not hang an open container over a hot engine.

### Clear filter observation

On pump-equipped bikes, a clear filter can show whether fuel is moving. Do not over-interpret bubbles, but use it to spot an empty line, plugged filter, or pump that clicks without moving fuel.

### Bowl drain refill test

Drain one bowl, close the screw, then apply normal fuel supply. Open the screw again after a few seconds:

- fuel returns: that bowl refilled;
- still dry: that carb's float valve/inlet path is blocked or fuel never reached the rack.

## Most likely causes by symptom

| Symptom | First suspects |
|---|---|
| All bowls dry | petcock off, blocked tank outlet, blocked filter, disconnected vacuum valve line, failed automatic fuel valve, failed pump/relay on pump bikes |
| One bowl dry | stuck float needle, blocked seat filter, blocked T-joint/rail, float binding |
| Bowls full, no start | clogged pilot/starter jets, no spark, no compression, intake leak |
| Runs only on choke | clogged pilot circuits, air leak, low bowl level |
| Pump silent with key on | may be normal if bowls are full; test during cranking or by the manual procedure |
| Pump runs when jumped, not normally | fuel-cut relay, spark-box signal, wiring, grounds |
| Pump clicks rapidly but no fuel | empty tank, blocked inlet, bad filter, air leak on inlet, weak pump |
| Fuel pours into airbox | float valves not sealing, float height too high, excessive pump pressure |

## Related

- [Carburetor cleaning](carburetor-cleaning.md)
- [Carburetor installation](carburetor-installation.md)
- [Carburetor synchronization](carburetor-synchronization.md)
- [Intake boot replacement](intake-boot-replacement.md)
- [V4MuscleBike forum field notes](v4musclebike-forum-field-notes.md)
- [Carburetor reference package](../Manuals/carburetor-reference/README.md)
