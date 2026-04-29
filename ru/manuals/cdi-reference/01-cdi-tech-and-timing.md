# CDI / Spark Unit: техника и углы зажигания

Русское зеркало: `manuals/cdi-reference/01-cdi-tech-and-timing.md`

## 1. Что реально стоит на мотоцикле

Для раннего V45 Sabre локальные мануалы описывают battery-fed transistorized ignition system:

- two pulse generator coils;
- two spark units;
- two ignition HT coils;
- wasted-spark operation.

Два spark units обслуживают пары цилиндров:

- cylinders `1 and 3`;
- cylinders `2 and 4`.

На ранних 700/750 Sabre spark units стоят сзади под сиденьем / в зоне rear fender.

## 2. Stock timing data

Для `1982-1983 750 Sabre` локальные мануалы дают такие практические checkpoints:

| Параметр | Значение |
| --- | --- |
| Idle timing | `10° BTDC` at idle |
| Advance starts | около `1,500 rpm` |
| Full advance | `37° BTDC` at `3,300 rpm` |

Эти числа совпадают между local factory-maintenance OCR и Haynes ignition section.

## 3. Что известно о stock advance curve

Factory and Haynes material дают inspection checkpoints, а не полный internal map spark units.

Практическая интерпретация:

- bike сидит около `10° BTDC` at idle;
- timing остается близко к base timing до примерно `1,500 rpm`;
- spark units then ramp advance electronically;
- by `3,300 rpm`, system should be at `37° BTDC`.

То есть service literature дает надежные `start point` and `full-advance point`, но не всю hidden OEM curve между ними.

## 4. Важные specs для диагностики

| Параметр | Значение |
| --- | --- |
| Pulse generator nominal resistance | `480 ohms +/- 10%` |
| Haynes check range for 1982-1986 | `450 to 550 ohms` |
| System type | `12 V transistorized ignition` |
| Timing adjustment | `none` |

Wire pairs для pulse generators в Haynes OCR:

- `white/yellow` and `yellow` для одной pickup pair;
- `white/blue` and `blue` для второй pickup pair.

OCR может ошибаться, поэтому перед depinning/repinning сверяться с wiring diagram.

## 5. Что не регулируется

Мануалы прямо говорят:

- normal ignition timing adjustment отсутствует;
- system only checked with timing light;
- if timing is wrong, component is faulty and should be tested or replaced.

Это важно: на этой платформе "timing drift" обычно не adjustment-related. Чаще причины:

- bad spark unit;
- weak pulse generator signal;
- poor voltage supply;
- poor grounds;
- coil or connector problems.

## 6. Stock-curve summary

Рабочая цель для stock-running VF750S:

- healthy 12 V supply;
- both spark units firing cleanly;
- base timing около `10° BTDC`;
- clean advance progression to `37° BTDC` by `3,300 rpm`.

Все, что за пределами этого, сначала считать fault, а не tuning opportunity.
