# VF750 EFI / ECU Swap Planning

Русское зеркало: `Tuning/ecu swap.md`

Собранные и проверенные заметки.

Проверено: 2026-04-29

## Scope

- проект: 1982 Honda VF750S / V45 Sabre;
- штатная система: четыре CV carbs, нет engine ECU, отдельные transistorized spark units;
- фокус: переход с карбюраторов на electronic fuel injection со standalone ECU;
- обновлено с учетом V4MuscleBike EFI и ignition research.

## Короткий вывод

На V4MuscleBike не найден чистый, законченный и повторяемый рецепт EFI conversion для V45 Sabre.

Форумные данные говорят: swap возможен, но практический consensus осторожный. Для обычного rider build лучше clean, sealed, correctly tuned carbs. EFI имеет смысл, если проект изначально экспериментальный: turbo, altitude compensation, long-term parts independence или глубокая кастомизация.

### Практический вывод

- если bike должен хорошо ехать в этом сезоне, rebuild and tune the carb rack;
- если bike — long-term custom project, EFI возможен, но это full fuel-system, intake, wiring, sensor, charging and tuning project;
- не думай об этом как об "ECU swap": у VF750S нет штатного fuel ECU;
- первый prototype лучше делать fuel-only EFI со stock spark units;
- менять fuel и ignition control одновременно — слишком много переменных для first start.

## Лучшие найденные forum evidence

### 1. V4MuscleBike: 1983 VF750S EFI question

Статус: strongest direct V45 Sabre forum thread.

Что показывает:

- вопрос от владельца `1983 Sabre VF750S` о carb-to-EFI conversion;
- участники указывают на прошлые attempts, но не на polished finished recipe;
- Speeduino-style DIY EFI считается возможным, но не простым;
- опытные участники советуют properly serviced V4 carb rack как лучший normal-use path;
- V4 geometry, banks, packaging и tuning делают проект намного больше, чем кажется.

Источник:

- [Converting carbs to fuel injection](https://v4musclebike.com/threads/converting-carbs-to-fuel-injection.44405/)

### 2. VF / VFR community EFI experiments

Статус: useful concept references, not direct Sabre proof.

Общие идеи:

- split GSXR throttle bodies into a V4-friendly layout;
- individual throttle bodies;
- Megasquirt / MicroSquirt / Speeduino-style standalone control;
- начать с batch или bank injection перед sequential injection.

Ограничение: эти примеры чаще VF/VFR-adjacent или Interceptor-focused. Они помогают с architecture, но не доказывают fit под Sabre tank.

Источники:

- [EFI swapping VF750](https://forum.vf1000.com/t/efi-swapping-my-interceptor/5487)
- [EFI conversion discussion for Honda V4](https://forum.vf1000.com/t/efi-conversion/1856)

## Что есть в штатном мотоцикле

VF750S — карбюраторный мотоцикл с отдельной системой зажигания:

- четыре карбюратора в тесной V4 intake package;
- vacuum-operated fuel valve на Sabre fuel system;
- нет high-pressure pump, return line или fuel rail;
- two pulse generator coils;
- two spark units;
- two ignition coils;
- wasted-spark operation;
- ignition timing проверяется strobe, не регулируется механически.

Отсюда два пути:

- fuel-only EFI while keeping stock spark units;
- full fuel-and-ignition control через standalone ECU или отдельный programmable ignition.

Fuel-only — лучший первый prototype.

## Architecture options

### Option 1: Fuel-only EFI, stock ignition retained

Самый низкий риск для experiment path.

Concept:

- standalone ECU controls injectors and fuel pump relay;
- stock Honda spark units continue ignition timing;
- ECU получает clean rpm signal только для fueling;
- wideband O2 используется для tuning feedback.

Плюсы:

- меньше first-start variables;
- stock ignition curve остается известной;
- проще вернуться на carbs;
- проще диагностировать no-start.

Минусы:

- нет ignition timing control;
- rpm signal conditioning все равно должен быть правильным;
- слабые stock ignition parts остаются в системе.

### Option 2: EFI plus programmable ignition

Более глубокий custom path.

Concept:

- ECU или programmable ignition controls spark timing;
- stock spark units удаляются или bypassed;
- pickup signals, coil drivers, dwell, tach output и kill logic должны быть решены правильно.

Плюсы:

- полный контроль fuel and ignition;
- лучший путь для turbo, high compression или больших engine changes;
- одна calibration связывает fuel and spark.

Минусы:

- гораздо выше wiring/setup risk;
- wrong dwell или coil strategy могут повредить детали;
- base timing must be locked and verified before tuning;
- failure diagnosis сложнее.

Если цель именно ignition control, сначала смотри:

- [CDI testing and replacement](../HowTo/cdi-testing-and-replacement.md)
- [CDI replacement options](../manuals/cdi-reference/03-cdi-replacement-options.md)

## Throttle body layouts

### 1. Four individual throttle bodies

Лучшее техническое направление для V4.

Donor ideas:

- GSXR600 / GSXR750 throttle bodies;
- CBR600 throttle bodies;
- R6 throttle bodies;
- VFR800 throttle bodies;
- compact scooter throttle bodies `28 to 32 mm`.

Плюсы:

- лучший cylinder-to-cylinder control;
- ближе всего к modern motorcycle EFI layout;
- легче тонко tune после packaging.

Минусы:

- сложно упаковать под tank;
- custom intake boots or manifolds;
- custom fuel rail work;
- throttle linkage and cable routing становятся fabrication jobs.

### 2. Split inline sportbike throttle bodies into 2+2

Common VF/VFR experiment idea.

Плюсы:

- donor parts легко найти;
- injectors, TPS и rails могут идти комплектом;
- bank-by-bank packaging может быть реалистичнее жесткой inline rack.

Минусы:

- spacing редко совпадает с Honda V4 intake;
- rails and throttle linkage обычно требуют modification;
- bank synchronization still matters.

### 3. Two throttle bodies

Возможно, но менее привлекательно.

Плюсы:

- проще fabrication;
- меньше injectors and wiring;
- проще fuel rail layout.

Минусы:

- хуже throttle response;
- риск uneven mixture;
- тяжелее сохранить clean V4 feel.

### 4. Single throttle body plus plenum

Самый простой layout, но не лучший motorcycle solution.

Плюсы:

- один throttle body;
- один TPS;
- simpler cable routing.

Минусы:

- plenum volume and runner length сложно сделать правильно;
- low-rpm response может пострадать;
- packaging все равно может быть хуже ожидаемого.

## ECU choices

### Speeduino

Best use:

- DIY-friendly experimental build;
- владелец готов к open-source hardware, wiring, firmware and tuning;
- проект может пережить iteration.

Почему подходит:

- V4MuscleBike упоминает Speeduino-style DIY EFI как plausible path;
- Speeduino — open-source engine-management project с hardware, firmware and software.

Watch-outs:

- board quality and enclosure quality vary;
- input protection, grounds и noise control критичны на motorcycle;
- support зависит от выбранной board/firmware path.

Источник:

- [Speeduino GitHub](https://github.com/speeduino/speeduino)

### MicroSquirt / MegaSquirt

Best use:

- более mature standalone path;
- нужен weather-resistant motorcycle-sized ECU;
- batch или bank injection acceptable.

Почему подходит:

- MicroSquirt часто используется в small engines и powersports projects;
- batch-fire / semi-sequential fueling и wasted-spark ignition хорошо подходят консервативному V4 first build.

Источники:

- [MicroSquirt product information](https://www.msextra.com/product-range/microsquirt/)
- [MegaSquirt fuel-injection modes](https://www.megamanual.com/v22manual/mfuel.htm)

### Ignitech EFI / ignition-adjacent paths

В этом repo Ignitech важнее как programmable ignition, чем как proven VF750S EFI conversion.

Смотри Ignitech notes, если цель spark control:

- [Ignitech SPARKER TCI](https://www.ignitech.cz/en/vyrobky/tci/tci.htm)
- [Ignitech SPARKER TCIP4](https://www.ignitech.cz/en/vyrobky/tcip/tcip.htm)

## Required sensors and signals

Минимум:

- TPS;
- MAP или alpha-N strategy;
- CLT / engine temperature;
- IAT;
- wideband O2 for tuning;
- crank or rpm signal;
- battery voltage input.

Желательно:

- barometric correction для altitude use;
- fuel pressure gauge during setup;
- ECU-controlled fuel-pump relay;
- fused ECU and injector power;
- clean sensor ground strategy.

MAP warning:

V4 с individual throttles может давать pulsing MAP signal. Планируй:

- small vacuum manifold;
- restrictors if needed;
- alpha-N или blended alpha-N / speed-density, если MAP unstable.

## Fuel system requirements

EFI требует high-pressure fuel system. Stock carb fuel path не подходит.

Нужно планировать:

- EFI-rated fuel hose;
- high-pressure fuel pump;
- pre-filter and post-filter;
- fuel pressure regulator;
- return line или returnless regulator strategy;
- injector bungs или throttle bodies with injectors;
- leak-free fuel rails;
- pump relay and fuse;
- safe routing away from heat and sharp edges.

### Injector sizing

Диапазон `180 to 240 cc/min` можно использовать как стартовую research zone, но не как готовое решение.

Считать нужно от:

- реальной horsepower target;
- BSFC assumption;
- number of injectors;
- target duty cycle;
- fuel pressure.

Для near-stock VF750S small sportbike injectors могут быть достаточны. Для turbo или major engine work считать заново.

## Electrical and charging constraints

ECU будет надежным настолько, насколько надежна старая Honda electrical system.

До EFI:

- test charging system;
- отремонтировать разъём генератора и цепь трёх жёлтых проводов;
- проверить выходное напряжение регулятора/выпрямителя;
- очистить массы аккумулятора, рамы и двигателя;
- убрать сомнительную дополнительную проводку от прошлых владельцев;
- собрать питание ЭБУ, форсунок и насоса через предохранители и реле.

Локальные ссылки:

- [Проверка системы зарядки](../HowTo/charging-system-test.md)
- [Ремонт разъёма генератора](../HowTo/stator-connector-repair.md)
- [Улучшение регулятора/выпрямителя](../HowTo/regulator-rectifier-upgrade.md)
- [Улучшение массы](../HowTo/ground-wire-upgrade.md)

## Ограничения по компоновке

Измерить до покупки:

- диаметр и расстояние между горловинами карбюраторов;
- угол впускных патрубков;
- расстояние от входа впуска до нижней стороны бака;
- доступный объём корпуса воздушного фильтра;
- маршрут троса газа;
- план удаления подсоса/обогатителя;
- угол форсунок и зазор под топливную рампу;
- вход и выход топливных шлангов;
- место под аккумулятор и площадку электроники;
- нагрев возле задних цилиндров.

Сначала сделать макет дроссельных узлов из картона, пластика или обрезков листового материала, и только потом резать коллекторы.

## Рекомендуемый порядок сборки

1. Сначала добиться правильной работы на карбюраторах.
2. Отрегулировать клапаны, при необходимости проверить компрессию, подтвердить искру на всех четырёх цилиндрах.
3. Починить зарядку и массы.
4. Решить: только впрыск топлива или полный контроль топлива и зажигания.
5. Выбрать компоновку дроссельных узлов и сделать макет под баком.
6. Собрать топливную систему высокого давления вне мотоцикла и проверить давлением.
7. Собрать жгут ЭБУ на столе с предохранителями и реле.
8. До первого запуска проверить в программе TPS, датчики температуры, кислородный датчик и сигнал оборотов.
9. Если возможно, начинать с консервативных настроек только по топливу.
10. Настроить холостой ход, прогрев, малый газ и крейсерский режим до проверки полного газа.
11. Добавлять управление зажиганием только после стабильной работы топливной части.

## Матрица решений

### Лучшее решение для обычной езды

Перебрать и настроить блок карбюраторов.

См.:

- [Чистка карбюраторов](../HowTo/carburetor-cleaning.md)
- [Установка карбюраторов](../HowTo/carburetor-installation.md)
- [Синхронизация карбюраторов](../HowTo/carburetor-synchronization.md)

### Best experimental EFI decision

Fuel-only EFI first, stock ignition retained, wideband O2 installed, complete carb rack kept on shelf.

### Best high-modification decision

Full standalone fuel and ignition только если bike уже получает major intake, exhaust, turbo, compression или wiring changes.

### Highest mistake risk

Сначала купить ECU, а потом пытаться впихнуть random throttle bodies.

## 2026-04-29 V4MuscleBike update summary

- Direct V45 Sabre EFI thread не показывает finished plug-and-play conversion.
- Forum advice strongly favors proper carb service for normal road use.
- Speeduino / Megasquirt-style EFI plausible, но V4 packaging and tuning workload — это реальный проект.
- Не смешивай EFI troubleshooting с неизвестными ignition, charging and carb problems. Сначала baseline motorcycle.

## Лучшие источники

- [V4MuscleBike - Converting carbs to fuel injection](https://v4musclebike.com/threads/converting-carbs-to-fuel-injection.44405/)
- [VF1000 - EFI swapping VF750](https://forum.vf1000.com/t/efi-swapping-my-interceptor/5487)
- [VF1000 - EFI conversion discussion](https://forum.vf1000.com/t/efi-conversion/1856)
- [Speeduino official repository](https://github.com/speeduino/speeduino)
- [MicroSquirt product information](https://www.msextra.com/product-range/microsquirt/)
- [MegaSquirt injection mode reference](https://www.megamanual.com/v22manual/mfuel.htm)
- [V4MuscleBike upgrade research map](v4musclebike-upgrade-research.md)
- [CDI / Spark Unit reference package](../manuals/cdi-reference/README.md)
