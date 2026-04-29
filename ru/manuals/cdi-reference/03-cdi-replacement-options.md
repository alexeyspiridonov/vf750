# CDI / Spark Unit: варианты замены

Русское зеркало: `manuals/cdi-reference/03-cdi-replacement-options.md`

Проверено: 2026-04-29

## 0. V4MuscleBike update summary

Проход по V4MuscleBike от 2026-04-29 усиливает три мысли:

- forum users often say `CDI`, но stock VF750S ignition лучше считать inductive / TCI-style system;
- Ignitech TCIP4 — самый понятный programmable path для V45 Sabre, но он не отменяет диагностику pulse generators, fuel delivery, charging and wiring;
- Rae-San имеет strong V65 support, но V65 success не доказывает VF750S plug-in.

## 1. Сначала правильно сопоставить систему

Перед заказом считать код на существующем box/boxes и сравнить:

- Honda part number;
- supplier code on box;
- connector style and pin count;
- bike year and market.

Early V4 Honda ignition boxes легко купить неправильно, потому что sellers часто смешивают VF models.

## 2. Option A: used OEM or NOS spark units

Лучше, если:

- bike остается electrically stock;
- хочется minimum wiring work;
- нужно restore normal running.

Плюсы:

- lowest wiring risk;
- stock curve;
- easiest troubleshooting with factory manual.

Минусы:

- age-related reliability unknown;
- used boxes may already be heat-damaged;
- listings mix different VF years/codes.

Использовать только если exact box code совпадает.

## 3. Option B: Carmo plug-and-play replacement boxes

Current strong off-the-shelf option:

- Carmo lists `VF750S / VF750 / VF700F / VF700C V45 Sabre` category and broader `VF700 / VF750 / V40 / V45 Magna / Sabre / Interceptor` modules in single-box and `2x` formats.

Практический смысл:

- stock was visible on `2026-04-12`;
- listing marketed as `plug and play`;
- Carmo publishes compatibility markings like `AKBZ`, `MB0`, `MB1`.

Вывод:

- это low-friction modern replacement path for stock-style architecture;
- still verify exact existing box code.

## 4. Option C: Ignitech SPARKER TCI

Лучше, если:

- stock boxes dead or unreliable;
- нужен modern inductive ignition;
- full map tuning не нужен.

Почему правильная family:

- Ignitech describes `SPARKER TCI` as inductive `battery, transistor, TCI` ignition for multi-cylinder carbureted bikes;
- это ближе к stock VF750S principle, чем generic universal CDI.

Плюсы:

- modern electronics;
- designed for multi-cylinder carbureted motorcycles;
- lower conceptual mismatch than forcing generic CDI.

Минусы:

- pickup compatibility and harness strategy still need confirmation.

## 5. Option D: Ignitech TCIP4

Лучше, если:

- нужен programmable advance control;
- есть готовность к wiring and laptop-based setup;
- bike получает major changes: carb, exhaust, compression.

Ignitech states `TCIP4` is:

- inductive programmable ignition;
- intended for multi-cylinder carbureted bikes;
- fully programmable for ignition timing;
- configurable for different pickup systems and coils.

Практические предупреждения:

- first map should match stock checkpoints;
- do not use timing changes to hide carburetion or charging faults;
- keep changes conservative without repeatable road/dyno feedback.

## 6. Option E: Rae-San PULSER TAI / VF-style ignition modules

Лучше, если:

- исследуется modern single-box replacement;
- работа идет с V65 или другой explicitly supported VF application;
- нужен vendor-supported module using OEM pickup strategy.

Почему tracked:

- V4MuscleBike V65 owners часто упоминают Rae-San;
- `V65 CDI box` thread говорит, что несколько users switched;
- Rae-San PULSER TAI description says it uses OEM inductive pickups and rotor on supported bikes.

Ограничение для проекта:

- do not assume V65 module is V45 VF750S module;
- confirm exact VF750S / V45 Sabre application, connector strategy, coil compatibility, timing curve.

## 7. Option F: capacitive aftermarket CDI

Обычно wrong first move.

Причина:

- stock VF750S ignition is transistorized inductive;
- Ignitech documentation separates `TCI` from `CDI`;
- cheap universal CDI из-за названия может не подходить.

Treat capacitive CDI as full custom conversion.

## 8. Decision tree

### Lowest risk

- exact-code OEM replacement or verified modern plug-and-play replacement.

### Best stock-plus solution

- Carmo replacement modules.

### Best custom solution

- Ignitech `TCIP4`, starting from stock-equivalent curve.

### Best vendor-contact custom path

- Rae-San, only after confirming VF750S / V45 Sabre-specific solution.

### Highest mistake risk

- generic unverified "CDI" boxes with no model-specific pickup and coil strategy.

## 9. Safe tuning starting point

Если переходишь на programmable inductive ignition, сначала повтори stock service-manual checkpoints:

- idle около `10° BTDC`;
- no meaningful advance before roughly `1,500 rpm`;
- full advance около `37° BTDC` by `3,300 rpm`.

Потом менять только одну вещь за раз и логировать:

- rpm;
- load / throttle;
- detonation behavior;
- hot restart behavior;
- plug reading;
- coolant temperature trend.

Без дисциплины programmable box становится дорогим способом создать вторую неисправность.

## 10. V4MuscleBike threads before ordering

- [Here we go again](https://v4musclebike.com/threads/here-we-go-again.46903/) — direct V45 Sabre Ignitech TCIP4 install and diagnostic caution thread.
- [V65 CDI box](https://v4musclebike.com/forums/showthread.php?t=47554) — Rae-San V65 discussion and fuel-pump-control clarification.
- [Ideal ignition setup on V65](https://v4musclebike.com/threads/ideal-ignition-setup-on-v65.45321/) — coil power, COP, Rae-San, OEM-style coils and TCI/CDI vocabulary.
- [Ignitech replacement for Dyna 3000](https://v4musclebike.com/threads/ignitech-replacement-for-dyna-3000.40044/) — TCIP4 programming workflow, but later Magna, not first-gen Sabre.
