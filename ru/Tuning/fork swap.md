# Honda Sabre: свап современной вилки

Русское зеркало: `Tuning/fork swap.md`

Собранные и проверенные заметки.

Проверено: 2026-04-29

## Scope

- проект: 1982 Honda VF750S Sabre;
- близкий локальный parts catalog: 1984-1985 VF700S Sabre;
- фокус: замена штатного передка на более современный fork / triple / wheel / brake package;
- обновлено с учетом V4MuscleBike fork-swap тем и build thread Sugarkryptonite V65 Sabre.

## Короткий вывод

Подтвержденного bolt-on modern fork kit для VF750S / VF700S Sabre не найдено.

Самое важное: front end — это система, а не две трубы вилки. При реальном свапе почти всегда затрагиваются stem, triples, bearings, wheel, axle, brakes, brake master cylinder, controls, cables, headlight, gauges, steering stops и wiring.

### Практический вывод

- если нужен настоящий modern USD conversion, планируй complete donor front end plus custom stem/triples/bearings/wheel/brake/cable work;
- если цель — хорошо едущий мотоцикл без machining project, rebuilt stock front end или close-era Honda conventional front end ниже по риску;
- V65/R1 swaps доказывают feasibility на уровне Sabre family, но не bolt-on compatibility для VF750S/V45;
- улучшение штатной вилки через springs, emulators, seals, bushings, sag и brake service может быть разумнее, чем донорская sportbike вилка.

## Главные подтвержденные проекты

### 1. Perry / 1984 VF700S Sabre Cafe

Статус: самый сильный прямой proof of concept для modern front-end conversion на Sabre.

#### Подтвержденные решения

- 2008 Suzuki GSX-R750 USD front end;
- GSX-R750 Tokico front brakes;
- GSX-R750 hand controls;
- custom-machined CognitoMoto steering stem;
- custom CognitoMoto triple trees;
- custom CognitoMoto front hub;
- 17x3.5 front wheel;
- 120/70-17 front tire;
- custom throttle cables;
- custom stainless braided brake lines.

#### Почему важно

- это не "forks only" swap;
- пример показывает полный пакет: stem + triples + wheel/hub + brakes + controls + cables;
- это типовой old-bike custom pattern: donor front end плюс custom parts, чтобы все реально встало и работало.

#### Источники

- [CafeRacer.net thread](https://www.caferacer.net/threads/1984-honda-honda-vf700s-sabre-cafe.28714/)
- [Inazuma Cafe](https://www.inazumacafe.com/2016/10/vf750-sabre-cafe.html)

### 2. Sugarkryptonite / V65 Sabre appendix

Статус: полезный family-level proof, но не прямой V45 аналог.

#### Подтвержденные решения

- Yamaha R1 front end conversion;
- new head bearings;
- custom steering stem / bearing work;
- custom lock nuts and triple-clamp work;
- fork disassembly, seal service и spacer/extender planning;
- custom headlight lower brackets;
- clip-ons and sportbike-style controls;
- brake master cylinder / lever troubleshooting after bore-size mismatch.

#### Почему важно

- показывает, что custom sportbike front-end swaps на Sabre family возможны;
- подтверждает мысль: надо думать complete donor package, а не isolated fork tubes;
- показывает hidden work после физической установки передка: headlight mounts, controls, brake hydraulics, fork sealing, bearing settling и road-test correction;
- дает предупреждение по cheap levers и cheap headlight hardware.

#### Ограничение

Это V65 Sabre, не VF750S project bike.

#### Источники

- [V4MuscleBike full build thread](https://v4musclebike.com/threads/newbies-84-v65-sabre.25947/)
- [V4MuscleBike sale/build thread](https://v4musclebike.com/threads/custom-cafe-racer-honda-v65-sabre.35922/#post-404196)
- [Локальные build notes](newbies-84-v65-sabre-build.md)
- [Локальный image archive](../../Images/build-process/newbies-84-v65-sabre/README.md)

### 3. K-Speed / Sabre Racer

Статус: сильный design reference, но не modern USD conversion.

Подтвержденное решение:

- штатные 37 mm telescopic TRAC forks были lowered, а не заменены на modern donor front end.

Почему важно:

- Sabre можно визуально опустить и сделать агрессивным без полного modern fork swap;
- полезно, если цель — stance, а не donor front-end conversion.

Источник:

- [Pipeburn feature](https://pipeburn.com/sabre-racer-honda-vf750s-k-speed-customs/)

### 4. Balkan Moto / V45 Sabre

Статус: главный warning example.

Что произошло:

- автор сначала укоротил front end через cut fork springs;
- позже признал, что setup был unsafe и оставил около 1.5 inches travel;
- на следующем, более хорошем donor bike вилки были rebuilt properly: progressive springs, fresh seals, preload caps, sag setup.

Почему важно:

- это самый понятный warning найденный в research;
- не режь пружины как замену нормальному lowering / fork work;
- ride height changes без geometry и damping/spring work быстро делают плохой мотоцикл.

Источники:

- [Balkan Moto build page](https://www.balkanmoto.com/builds/1982-83-honda-sabre-v45-cafe-racer.php)
- [Balkan Moto suspension geometry tool](https://www.balkanmoto.com/tools/suspension-geometry.php)

## Что есть в штатном мотоцикле

Локальные факты:

- parts data показывает dual-disc front brake setup и 110/90-18 front tire;
- Haynes содержит разделы по forks, steering stem, steering head bearings, TRAC/anti-dive, front wheel и front brakes;
- ранний 750 использует stock air-assisted fork arrangement.

Почему это важно:

- современные sportbike forks часто короче;
- modern swaps часто переводят переднее колесо с 18-inch на 17-inch;
- вместе эти изменения могут сильно изменить rake, trail и общий stance.

Локальные источники:

- `../../Manuals/haynes-manual/sections/06-frame-suspension-and-final-drive.pdf`
- `../../Manuals/haynes-manual/sections/07-brakes-wheels-and-tires.pdf`
- `../../Manuals/partslist-vf700s-sabre/partslist-vf700s-sabre-searchable.txt`

## Жесткие ограничения

### 1. Forks-only swap — неправильная модель

Реальный package обычно включает:

- fork tubes / fork legs;
- upper and lower triple clamps;
- steering stem;
- steering bearings;
- axle;
- wheel;
- brake rotors;
- calipers;
- brake master cylinder;
- brake lines;
- controls and switchgear;
- speedometer / sensor;
- headlight and gauge mounts;
- ignition switch mount;
- steering stops;
- cable and harness routing.

### 2. Stem and bearing work решают проект

Если donor triples не подходят к Sabre frame:

- нужен custom stem;
- или machining / press work;
- или bearing stack solution;
- или custom triples.

Нельзя покупать вилку только по tube diameter.

### 3. Brakes and controls являются частью свапа

После donor front end нужно проверить:

- master cylinder bore;
- caliper piston area;
- lever travel and feel;
- brake-light switch;
- hose routing;
- reservoir clearance;
- throttle and switchgear routing.

V65/R1 пример показывает: mismatched master cylinder / lever может сделать тормоза плохими даже если вилка физически стоит.

### 4. Headlight, gauges and ignition становятся fabrication work

На cafe/streetfighter Sabre после свапа почти всегда нужно заново решать:

- headlight brackets;
- gauge mount;
- ignition switch location;
- wire routing around steering stops;
- brake hose and throttle cable clearance;
- lock-to-lock interference.

Дешевые universal headlights/brackets — частый weak point.

## Варианты направления

### Вариант A: full modern USD front end

Лучше всего, если цель — радикальный modern cafe/streetfighter build.

Плюсы:

- современная жесткость и тормоза;
- широкий выбор donor parts;
- сильный визуальный эффект.

Минусы:

- custom stem/triples почти неизбежны;
- wheel/brake/speedo/headlight/controls превращаются в один большой проект;
- легко испортить geometry;
- дорого и долго.

Рабочие reference paths:

- GSX-R route через Perry;
- R1 route как V65 family-level reference.

### Вариант B: close-era Honda conventional front end

Лучше всего, если нужна lower-risk Honda-family логика.

Что смотреть:

- near-era VFR front end;
- fork length;
- tube diameter;
- axle and wheel fit;
- brake caliper and rotor compatibility;
- steering stem and bearing stack.

V4MuscleBike V45/VFR thread полезен именно как reminder: даже если fork diameter близок, Sabre calipers may not swap, и весь VFR wheel/brake/front-end package может быть проще.

Источник:

- [Fork swap?](https://v4musclebike.com/forums/showthread.php?t=34228)

### Вариант C: rebuild and upgrade stock front end

Лучше всего, если цель — ride quality, а не show-piece swap.

Что делать:

- fresh fork seals;
- bushings;
- proper fork oil;
- correct sag;
- fork springs;
- Race Tech / Gold Valve Emulator-style direction;
- brake rebuild;
- fresh lines and pads;
- steering head bearing adjustment.

V4MuscleBike suspension discussions часто относятся к springs, emulators, seals, bushings, sag и brake service как к серьезной альтернативе donor-fork swaps.

## Что измерить до покупки деталей

- stock fork length axle-to-top;
- donor fork length axle-to-top;
- fork tube diameter at triples;
- triple clamp offset;
- steering stem length;
- bearing inner/outer diameters;
- axle diameter;
- wheel diameter and tire size;
- brake rotor diameter and offset;
- caliper mounting style;
- master cylinder bore;
- lock-to-lock clearance;
- headlight/gauge/ignition clearance;
- available height above lower triple;
- brake hose, throttle cable and harness path;
- full compression tire-to-frame clearance.

## Бюджет, который легко забыть

Кроме fork legs и triples почти всегда нужны:

- bearings and seals;
- stem machining or custom stem;
- wheel bearings/spacers;
- brake lines;
- master cylinder;
- brake pads and fluid;
- fork seal/bushing service;
- possible fork spacer/extender work;
- headlight brackets;
- gauge mount;
- ignition switch mount;
- steering stops;
- throttle cables;
- switchgear wiring;
- brake-light wiring;
- bearing retorque and post-ride fastener shakedown.

## 2026-04-29 V4MuscleBike update summary

- V4MuscleBike не дал bolt-on VF750S modern-fork recipe.
- Самый близкий V45 direction — near-era VFR package, но с обязательными измерениями.
- V65 R1 build полезен как process reference: кастомный передок тянет за собой brakes, controls, headlight, gauges и bearing shakedown.
- Если цель — ездить лучше, сначала рассмотреть rebuilt stock fork + springs/emulators + brake service.

## Лучшие источники

- [Perry VF700S / Inazuma Cafe](https://www.inazumacafe.com/2016/10/vf750-sabre-cafe.html)
- [Perry VF700S / CafeRacer.net](https://www.caferacer.net/threads/1984-honda-honda-vf700s-sabre-cafe.28714/)
- [V4MuscleBike fork discussion](https://v4musclebike.com/forums/showthread.php?t=34228)
- [V4MuscleBike V65 fork swap discussion](https://v4musclebike.com/forums/showthread.php?t=13645)
- [V4MuscleBike Magna fork upgrades discussion](https://v4musclebike.com/forums/showthread.php?t=43709)
- [V4MuscleBike Progressive Springs discussion](https://v4musclebike.com/forums/showthread.php?t=32994)
- [K-Speed / Pipeburn](https://pipeburn.com/sabre-racer-honda-vf750s-k-speed-customs/)
- [Balkan Moto build](https://www.balkanmoto.com/builds/1982-83-honda-sabre-v45-cafe-racer.php)
- [V4MuscleBike Newbie's 1984 V65 Sabre](https://v4musclebike.com/threads/newbies-84-v65-sabre.25947/)
- [V4MuscleBike V65 Sabre build/sale thread](https://v4musclebike.com/threads/custom-cafe-racer-honda-v65-sabre.35922/#post-404196)
