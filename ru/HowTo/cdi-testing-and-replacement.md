
# CDI / TCI блок зажигания: диагностика и замена

Русская версия: `HowTo/cdi-testing-and-replacement.md`

Проверено: 29.04.2026

## Охват

- Мотоцикл: Honda VF750S / V45 Sabre 1982 года
- В мануале Honda: «spark unit» (блок зажигания)
- На форумах встречаются названия: CDI, igniter, «чёрный ящик», spark box
- Техническая заметка: штатная система VF750S — транзисторное индуктивное зажигание с питанием от аккумулятора, поэтому корректнее называть её TCI, а не классическим CDI

## Краткий вывод

Не начинайте с покупки случайного универсального CDI-блока.

Правильная последовательность действий:

1. Проверьте напряжение аккумулятора, массу, предохранители и питание зажигания.
2. Определите, проблема на всех цилиндрах или только на одной паре (wasted-spark).
3. Проверьте датчики импульсов, катушки зажигания, наконечники свечей, высоковольтные провода и питание блоков зажигания.
4. Только после этого меняйте блоки зажигания на оригинальные, проверенные аналоги или правильно настроенные программируемые TCI.

## Безопасность

- Держите пары топлива подальше от проверки искры.
- Используйте изолированный тестер искры или запасную свечу, надёжно заземлённую.
- Не прокручивайте стартер с отсоединёнными высоковольтными проводами рядом с баком или поплавковыми камерами.
- Не оставляйте зажигание включённым надолго при заглушённом двигателе.
- Снимайте клемму аккумулятора перед разборкой разъёмов или заменой блоков зажигания.

## Как устроена система

Раннее зажигание VF750S:

- два датчика импульсов;
- два блока зажигания;
- две катушки зажигания;
- цилиндры работают парами по принципу «wasted-spark» (искра на каждом обороте);
- штатная регулировка угла опережения отсутствует.

Контрольные точки зажигания:

- холостой ход: около 10° до ВМТ;
- опережение начинается примерно с 1500 об/мин;
- полный угол опережения: около 37° до ВМТ при 3300 об/мин.

Характеристики датчиков:

- номинальное сопротивление датчика импульсов: 480 Ом ±10%;
- по Haynes для 1982–1986: 450–550 Ом.

Перед разборкой разъёмов смотрите схему электропроводки:

- `../../Manuals/electrical-reference/manuals/04-wiring-diagram-1982-750-sabre.pdf`
- `../manuals/cdi-reference/01-cdi-tech-and-timing.md`

## Типовые неисправности

### Нет искры на всех четырёх цилиндрах

Проверьте:

- низкое напряжение аккумулятора при запуске;
- основной предохранитель или предохранитель стартера;
- замок зажигания или аварийный выключатель;
- отсутствие питания 12 В на блоках зажигания или катушках;
- плохой общий контакт массы;
- коррозию разъёмов.

### Не работает одна пара цилиндров

Проверьте:

- соответствующий блок зажигания;
- пару датчиков импульсов;
- одну катушку зажигания;
- цепь наконечника свечи/высоковольтного провода;
- повреждение разъёма или жгута конкретного ряда цилиндров.

Early 750 Sabre pairs:

- cylinders `1 and 3`;
- cylinders `2 and 4`.

### Misfire или shutdown хуже на горячую

Подозревать:

- pulse generator resistance drifting hot;
- spark unit breaking down with heat/vibration;
- connector resistance rising with heat;
- weak charging voltage warm;
- fuel starvation masquerading as ignition failure.

V4MuscleBike `Here we go again` — хороший warning example: owner поставил Ignitech TCIP4, но диагностика все равно вернулась к pulse generators, fuel delivery и model-specific fuel-system logic.

### Странное поведение tachometer

Форумные заметки связывают rear-bank ignition faults с tach behavior. Это clue, не proof. Все равно нужно проверять wiring, pickups, coils and spark units.

## Инструменты

- fully charged battery;
- multimeter;
- spark tester или spare known-good plug;
- timing light;
- wiring diagram;
- back-probe leads;
- contact cleaner;
- dielectric grease для reassembly, не как conductor;
- notebook для cold/hot resistance readings.

## Диагностический порядок

### 1. Battery and main power

- charge battery fully;
- measure voltage at rest;
- measure voltage while cranking;
- inspect main fuse and starter-solenoid area;
- inspect ignition switch and kill switch.

Weak cranking voltage can look like bad ignition.

### 2. Grounds and connectors

Проверить и почистить:

- battery negative to engine;
- battery negative to frame if present;
- coil grounds / mounting;
- spark-unit connectors;
- pulse-generator connectors;
- coil primary connectors;
- prior-owner splices.

### 3. Spark на всех цилиндрах

Одинаково проверить каждый цилиндр и записать:

- no spark on all four;
- weak spark on all four;
- no spark on one pair;
- intermittent spark after heat soak;
- spark present but engine still does not fire.

### 4. Dead pair

Если мертвы два цилиндра, сравнить:

- spark output bank to bank;
- coil primary feed;
- coil resistance;
- pulse generator resistance;
- connector condition.

### 5. Pulse generators cold

Measure both pulse generator circuits:

- `450 to 550 ohms` Haynes range;
- Honda reference около `480 ohms +/- 10%`.

Continuity alone is not enough.

### 6. Pulse generators hot

Если bike runs cold and dies hot:

- прогреть до появления fault;
- safely shut down;
- сразу измерить pulse generators;
- сравнить с cold values.

Pickup может быть нормальным cold и fail hot.

### 7. Coils, plug caps, HT leads

По manual проверить primary/secondary resistance.

Осмотреть:

- cracked plug caps;
- loose HT leads;
- corrosion at coil terminals;
- wrong resistance caps;
- old plugs masking spark quality.

### 8. Power to spark units

По wiring diagram проверить switched ignition power на spark units and coils during cranking and running.

Проверять voltage drop, а не только open-circuit voltage.

### 9. Swap spark units only if compatible

Если две stock boxes одинаковые по connector format and compatible:

- mark both boxes;
- swap them;
- проверить, follows fault the box.

Если fault moves with box, box becomes prime suspect.

Не считать все year/model boxes interchangeable.

### 10. Timing light

После запуска проверить:

- около `10 degrees BTDC` at idle;
- smooth advance;
- около `37 degrees BTDC` by `3,300 rpm`.

Если timing unstable or wrong, диагностировать components. Stock system has no normal timing adjustment.

## Варианты замены

### Option A: exact-code OEM or NOS spark units

Лучше, если bike stays stock и можно match exact printed code and connector layout.

Плюсы: stock curve, проще manual-based troubleshooting, минимум setup.  
Минусы: used parts могут быть heat-damaged; listings часто смешивают VF years/models.

### Option B: verified plug-and-play replacement modules

Лучше, если нужен stock-style operation with newer electronics без map tuning.

CDI reference package отслеживает Carmo как current stock-style replacement path. Но нужно проверить exact box codes.

См.: [CDI replacement options](../manuals/cdi-reference/03-cdi-replacement-options.md)

### Option C: Ignitech SPARKER TCI

Хорошо, если нужен modern inductive replacement и system family должен совпадать со stock Honda TCI-style architecture.

Ignitech describes SPARKER TCI as inductive battery/transistor ignition for multi-cylinder carbureted motorcycles. Это правильнее, чем random capacitive CDI box.

### Option D: Ignitech TCIP4

Хорошо, если нужен programmable timing и есть готовность к wiring/laptop setup.

V4MuscleBike имеет прямой V45 Sabre пример: 1982 VF750S owner installed TCIP4. Bike starts and runs, но thread предупреждает: programmable ignition не отменяет диагностику pulse generators, fuel delivery, charging and wiring.

First map rule:

- reproduce stock timing checkpoints;
- confirm with timing light;
- tune one change at a time.

### Option E: Rae-San

Best current evidence:

- strong V65 forum support;
- several users replace two V65 boxes with one Rae-San-style unit;
- Rae-San PULSER TAI uses OEM inductive pickups and rotor on supported bikes.

Ограничение:

- V65 evidence не значит V45 VF750S plug-in;
- contact vendor and verify exact VF750S application.

### Option F: generic capacitive CDI

Обычно плохой первый ход.

Причина:

- stock VF750S is transistorized / inductive;
- CDI coil requirements and wiring differ;
- cheap universal CDI can create a new fault.

Capacitive CDI — только как full custom conversion.

## Installation checklist

Перед заменой:

- photograph every connector;
- label original boxes;
- record printed codes and connector colors;
- clean harness connectors;
- verify coil resistance and plug caps;
- verify pulse generator resistance cold/hot;
- verify charging voltage;
- mount new module away from heat and water;
- protect harness from seat-pan/rear-fender rub;
- keep original boxes until road testing passed.

## First-start checklist

1. Battery fully charged.
2. Fuel system confirmed.
3. Kill switch on.
4. Connectors seated.
5. Spark checked on all four cylinders.
6. Engine started and warmed gently.
7. Timing checked with strobe.
8. Charging voltage checked.
9. Short ride only.
10. Hot restart tested.
11. Module/connector temperature checked after ride.

## Если проблема осталась

### Still no spark

Вернуться к:

- main fuse;
- ignition switch;
- kill switch;
- coil feed;
- spark-unit power;
- pickup signal.

### One bank still dead

Вернуться к:

- pickup pair;
- coil;
- plug caps and HT leads;
- spark-unit connector;
- box compatibility.

### Runs cold, fails hot

Вернуться к:

- pulse generators hot;
- charging output hot;
- connector voltage drop hot;
- fuel delivery;
- tank venting;
- vacuum-operated fuel valve.

### Runs, but badly

Не менять timing сразу. Проверить:

- valve clearances;
- compression;
- carb cleanliness;
- carb synchronization;
- intake leaks;
- fuel flow.

## Лучшие источники

- [CDI / Spark Unit tech and timing](../manuals/cdi-reference/01-cdi-tech-and-timing.md)
- [CDI / Spark Unit diagnostics](../manuals/cdi-reference/02-cdi-diagnostics-and-setup.md)
- [CDI / Spark Unit replacement options](../manuals/cdi-reference/03-cdi-replacement-options.md)
- [V4MuscleBike - Here we go again](https://v4musclebike.com/threads/here-we-go-again.46903/)
- [V4MuscleBike - V4spark.com](https://v4musclebike.com/forums/showthread.php?p=531158)
- [V4MuscleBike - V65 CDI box](https://v4musclebike.com/forums/showthread.php?t=47554)
- [V4MuscleBike - Ideal ignition setup on V65](https://v4musclebike.com/threads/ideal-ignition-setup-on-v65.45321/)
- [V4MuscleBike - no spark at front cylinders](https://v4musclebike.com/showthread.php?t=5602)
- [V4MuscleBike - 84 VF750 Sabre ignition problem](https://v4musclebike.com/threads/84-vf-750-sabre-ignition-problem.32922/)
