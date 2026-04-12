# VF750 Top-End Oiling Guide

Practical notes on improving oil delivery to the cylinder heads on the
Honda VF750 / V45 family.

This topic matters because cam and rocker wear on early VF engines is often
made worse by marginal oil delivery to the top end, especially at hot idle.

## What Problem This Addresses

Typical pattern:

- camshaft lobes and rocker surfaces wear early;
- top-end ticking gets worse as the engine warms up;
- rear bank often suffers more than the front;
- damage accelerates if idle speed is too low or oil changes are neglected.

In this repository, the problem is already summarized in:

- `problems.md`
- `howto.md`

## First Improve The Baseline Before Modifying Anything

Do these checks first, because an oiling mod does not fix an already worn or
neglected engine by itself:

1. Set idle correctly.
   Keep hot idle around `1100-1200 RPM`. Low idle reduces oil pressure where
   these engines already struggle.
2. Use the right oil and change it often.
   A motorcycle-safe `10W40` or `15W50` is the usual practical range already
   referenced elsewhere in this repo. Avoid automotive oils with wet-clutch
   friction modifiers.
3. Inspect cams and rockers.
   If the lobes or rocker pads are already damaged, improve oiling and repair
   the worn parts together.
4. Keep valve clearance in spec.
   Tight valves add heat and load to an already vulnerable top end.
5. Check the rest of the lubrication system.
   A weak oil pump, sludge, blocked passages, a bad filter installation, or
   heavy debris in the engine will make any head-oiling upgrade less useful.

## Most Common Improvement: External Top-End Oil Feed

The common VF fix is an external oil line kit that feeds the cylinder heads
more directly instead of relying only on the stock path.

Typical approach:

- take pressurized oil from the oil filter housing area;
- split or route that feed to the front and rear heads;
- connect at the head using banjo fittings or the chosen kit hardware;
- secure the lines away from exhaust heat and sharp edges;
- use new sealing washers at banjo or union connections.

The practical goal is simple:
- reduce pressure drop to the cam and rocker area;
- get oil to the heads faster and more consistently;
- reduce the chance of repeat camshaft wear after repair.

## Installation Notes That Matter

- Do not route the lines where they can touch headers or chafe on the frame.
- Do not leave unsupported line weight hanging from the fittings.
- Prime the system and check for leaks immediately after first start.
- Recheck all fittings after the first heat cycle.
- If you are using a drill-and-tap style kit, treat cleanliness as critical.
  Metal chips in the oiling system are unacceptable.

The local Haynes text is useful here because it explicitly notes the external
oil pipe hardware and the need for new sealing washers during reassembly:

- `manuals/haynes-manual/sections/02-engine-clutch-and-transmission.txt`

## Other Ways To Help Top-End Lubrication

These are not substitutes for direct oil-feed improvement, but they help:

- keep idle speed out of the too-low range;
- avoid long periods of hot idling;
- use a healthy oil pump during rebuilds;
- inspect oil passages any time the top end is apart;
- replace worn rocker arms and shafts together with damaged cams;
- do frequent oil and filter changes on an engine with unknown history.

## What This Mod Will Not Fix

- destroyed cams or rocker pads;
- incorrect valve timing;
- bad cam-chain tensioners;
- debris circulating through the engine;
- chronic overheating or fuel dilution of the oil.

If the valve train is already damaged, the correct path is:

1. inspect and measure;
2. repair or replace worn hard parts;
3. improve oil delivery;
4. set idle and valve clearance correctly;
5. monitor noise and oil condition after restart.

## Practical Recommendation For This Repository

For the `1982 VF750S Sabre` project, the lowest-risk order is:

1. inspect cam and rocker condition under the covers;
2. correct idle speed and valve clearance;
3. service oil and filter;
4. install or plan an external top-end oil feed;
5. only then judge whether the remaining noise is wear, tensioner, or oiling.

## Related Files

- `howto.md`
- `problems.md`
- `resources.md`
- `manuals/haynes-manual/sections/02-engine-clutch-and-transmission.txt`
