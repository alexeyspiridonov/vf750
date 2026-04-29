# CDI / Spark Unit: диагностика и setup

Русское зеркало: `manuals/cdi-reference/02-cdi-diagnostics-and-setup.md`

## 1. Главное правило

Не начинай с обвинения spark units.

На этой платформе симптомы "bad CDI" часто вызывают:

- low battery voltage during cranking;
- poor ground paths;
- corroded connectors;
- weak pulse generator output;
- bad coil or HT path;
- old kill-switch or ignition-switch contacts.

## 2. Common failure patterns

### Падает один bank / одна пара

Смотреть:

- one spark unit;
- pickup pair feeding that spark unit;
- coil serving that bank;
- bank-specific connector or harness damage.

### Misfire worse hot

Смотреть:

- spark unit breaking down with temperature;
- pickup coil resistance drifting hot;
- connector resistance rising with heat;
- weak charging system causing low running voltage.

### Tachometer ведет себя странно

Локальные forum references связывают tach behavior с rear-bank ignition faults. Это полезная clue, но не proof.

## 3. Practical diagnostic order

Перед покупкой parts:

1. Confirm battery condition and cranking voltage.
2. Confirm clean grounds from battery, frame, engine.
3. Confirm switched ignition power reaches both spark units during cranking and running.
4. Measure both pulse generators against spec.
5. Check coil primary and secondary resistance.
6. Inspect plug caps, HT leads and connectors.
7. Check ignition timing with strobe.
8. Only then condemn spark unit.

## 4. Fast isolation logic

Если bike runs on only one bank:

- identify whether `1-3` or `2-4` is dead;
- compare pickup resistance bank-to-bank;
- compare coil feed and spark output bank-to-bank;
- if two spark units are same part number and connector format, swap them and see whether fault follows box.

Если fault moves with box, box is prime suspect.

## 5. Timing-light check

Для stock-style system timing-light check — это реальный setup procedure.

Target checkpoints:

- `10° BTDC` at idle;
- full advance at `37° BTDC` by `3,300 rpm`.

Если timing unstable, late или asymmetric:

- pulse generators;
- spark units;
- rotor / trigger condition;
- harness voltage drop;
- grounds.

## 6. Что означает setup

Для stock spark units setup — это не editing map. Это:

- clean power and ground;
- healthy pickups;
- healthy coils;
- correct static wiring;
- timing marks verified with strobe.

Это baseline перед modern ignition conversion.

## 7. Перед любой replacement ignition

Сначала:

- fix charging issues;
- clean all ignition connectors;
- verify pickup resistance cold and hot if possible;
- verify correct coils and plug caps;
- get carbs and valve clearances right.

Если engine mechanically или fuel-system sick, ignition box не исправит это tuning magic.
