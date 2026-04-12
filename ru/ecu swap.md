# Заметки по EFI swap для VF750

Здесь собраны реальные обсуждения и направления решения для EFI-конверсии VF750, найденные к текущему моменту.

## Источники обсуждений

1. [EFI swapping VF750 (GSXR throttle bodies)](https://forum.vf1000.com/t/efi-swapping-my-interceptor/5487)
   План: использовать throttle bodies от GSXR750 и разделить их в компоновку 2+2 для V4.

2. [Converting carbs to fuel injection (VF750 Sabre)](https://v4musclebike.com/threads/converting-carbs-to-fuel-injection.44405/)
   Полное обсуждение перехода с карбюраторов на EFI. Оно подтверждает, что такие проекты делали, но полностью задокументированных завершённых сборок очень мало.

3. [EFI conversion discussion for Honda V4 (Megasquirt)](https://forum.vf1000.com/t/efi-conversion/1856)
   Основные идеи из обсуждения:
   - individual throttle bodies
   - инжекторы GSXR
   - Megasquirt ECU
   - ожидаемый прирост примерно в диапазоне +5 to 15 hp

4. [VF750 EFI discussions (general list)](https://forum.vf1000.com/c/vf750/12)
   Общая категория VF750, где встречаются треды по EFI и swap-темам.

## Варианты компоновки EFI для VF750

### Вариант 1: Отдельные throttle bodies

Это самый серьёзный и типовой EFI-путь для V4.

#### Концепция
- 4 throttle bodies
- 4 injectors
- standalone ECU
- custom fuel rail

#### Типичные доноры
- GSXR600/750 throttle bodies
- CBR600 throttle bodies
- R6 throttle bodies
- VFR800 throttle bodies

#### Плюсы
- наиболее правильная схема для V4
- лучший отклик на газ
- проще хорошо настроить после упаковки в раму

#### Минусы
- трудно разместить
- требует кастомного впуска

### Вариант 2: Два throttle bodies (2+2 цилиндра)

#### Схема
- передний ряд -> 1 throttle body
- задний ряд -> 1 throttle body

#### Плюсы
- проще
- меньше проводки
- легче синхронизировать

#### Минусы
- хуже отклик на газ
- риск неравномерной подачи топлива

### Вариант 3: Один throttle body и plenum

#### Схема
- 1 большой throttle body
- plenum
- 4 runner-а

#### Плюсы
- самый простой вариант
- самый дешёвый

#### Минусы
- слабее отклик на газ
- хуже поведение на низких оборотах
- длинный впускной тракт

### Вариант 4: Scooter throttle bodies

Популярный DIY-путь, когда главная проблема — упаковка под бак.

#### Частые размеры
- 28 mm scooter throttle bodies
- 30 mm scooter throttle bodies
- 32 mm scooter throttle bodies

#### Схема
- 4 маленьких throttle bodies
- внешние injectors
- общий fuel pump

#### Плюсы
- компактно
- дешево
- легче разместить под баком

#### Минусы
- ограниченный поток воздуха
- перед финальным решением нужна реальная проверка

## ECU, которые чаще всего используют

- Megasquirt
- Microsquirt
- Speeduino
- Ecotrons
- Ignitech EFI

По форумам чаще всего всплывает именно Speeduino.

## Необходимые датчики

- TPS — обязателен
- MAP — один общий датчик или четыре отдельных сигнала
- CLT — температура двигателя
- IAT — температура впускного воздуха
- O2 — желательно

## Что потребуется по топливной системе

Нужно добавить:

- 3 bar fuel pump
- обратную магистраль
- fuel pressure regulator
- injectors примерно 180 to 240 cc

### Какие injectors чаще используют

- GSXR600
- CBR600
- R6
- SV650
- VFR800

Общий вывод из собранных заметок: 200 cc обычно достаточно.

## Основные проблемы EFI на VF750

1. Очень мало места под баком
2. Сложная V4-компоновка впуска
3. Синхронизация между рядами цилиндров
4. Слабый вакуумный сигнал на V4
5. Старая система зарядки сама по себе не очень сильная

## Наиболее перспективная конфигурация для VF750

### Лучший полный сетап

- 4 x 32 mm throttle bodies
- Speeduino
- shared MAP
- single TPS
- 4 x 220 cc injectors
- custom fuel rail

### Минимальный EFI swap

Самая простая возможная конфигурация:

- 2 throttle bodies
- 2 injectors
- batch fire
- Speeduino

### Самое интересное компактное решение

- 4 scooter throttle bodies
- внешние injectors
- маленький airbox
- Speeduino

Почему это выделяется:

- очень компактно
- выше шанс реально уложить всё под баком
