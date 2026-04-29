# Проект Honda Sabre 1982 Cafe Racer

Русское зеркало: `README.md`

Этот репозиторий — техническая база для переделки `1982 Honda VF750S Sabre` в `cafe racer`.

Здесь собраны сервисные мануалы, каталоги деталей, исследовательские заметки, фото-референсы и практические инструкции по проекту.

## Цель проекта

- Подробно разобраться в штатной платформе V45 Sabre.
- Подготовить сервисную документацию в поисковом и структурированном виде.
- Исследовать ключевые зоны переделки: передняя подвеска, EFI, электрика и общий cafe-racer дизайн.
- Спланировать визуальную и техническую конверсию мотоцикла.

## Быстрый старт

Если начинаешь работу с репозиторием, иди в таком порядке:

1. Прочитай `README.md`, чтобы понять структуру репозитория.
2. Открой `HowTo/README.md` для основных работ по обслуживанию, диагностике и модификациям.
3. Посмотри `problems.md` — там собраны типовые слабые места VF750 / V45.
4. Для проводки и зарядки сначала используй `Manuals/electrical-reference/`.
5. Для spark units / CDI / TCI, углов зажигания и диагностики используй `Manuals/cdi-reference/`.
6. Для передней подвески и свапа вилки смотри `Tuning/fork swap.md`.
7. Для EFI / ECU конверсии смотри `Tuning/ecu swap.md`.
8. Для дизайна и реальных build threads смотри `Tuning/sabre-cafe-racer-projects.md` и `Images/`.
9. Для форумов, внешних источников и каталогов деталей смотри `resources.md`.

## Структура репозитория

```text
Manuals/
  source PDFs                 исходные PDF мануалов и каталогов деталей
  haynes-manual/              Haynes service manual: OCR, поиск, разбиение по разделам
  partslist-vf700s-sabre/     каталог VF700S: OCR, поиск, разбиение по разделам
  electrical-reference/       собранный пакет по электрике
  cdi-reference/              отдельный пакет по зажиганию / spark units
.scripts/                     Python-скрипты для обработки PDF
Images/                       референсы: stock, cafe racer, Pinterest, build process
Tuning/                       тюнинг, свапы и исследовательские статьи
HowTo/                        инструкции по обслуживанию, ремонту и модификациям
problems.md                   типовые проблемы VF750 и решения
resources.md                  форумы, каталоги деталей и внешняя документация
ru/                           русское зеркало основных статей
```

## Документация

### Исходные PDF

- [Honda VF700/750/1100 Haynes service manual](../Manuals/Honda%20VF700,750,1100%20v45,65%20Sabre%20And%20Magna%20V-Fours%2082-88%20Haynes%20Service%20Manual%20Eng%20By%20Mosue.pdf)
- [VF700S Sabre parts list 1984-1985](../Manuals/partslist-vf700s-sabre_84-85_en-11082016-0807.pdf)

### Обработанные материалы

PDF-файлы в `Manuals/` были превращены в searchable PDF с OCR-слоем и разбиты по разделам:

- **Haynes manual** — 10 разделов: от вводной части до электрики и таблиц пересчета.
- **Parts catalog** — 5 разделов: вводные страницы, двигатель, рама, индекс номеров деталей и индекс описаний.
- **Electrical reference** — единый пакет по системе зажигания, электросистеме, схемам проводки, каталогу электрических деталей и типовым неисправностям.
- **CDI reference** — отдельный пакет по spark units / TCI, контрольным точкам зажигания, диагностике и вариантам замены.

Каждый сгенерированный пакет содержит `manifest.json` с привязкой к исходникам и диапазонами страниц.

## Исследовательские статьи

| Файл | Тема |
| --- | --- |
| `Tuning/fork swap.md` | Варианты современной передней подвески для VF750S / VF700S Sabre, подтвержденные сборки, доноры и предупреждения. |
| `Tuning/ecu swap.md` | EFI-конверсия: throttle bodies, ECU, Speeduino, Megasquirt, датчики и топливная система. |
| `Tuning/sabre-cafe-racer-projects.md` | Подборка реальных Sabre cafe racer проектов: Perry, HackAWeek, Balkan Moto, K-Speed, V4MuscleBike. |
| `Tuning/newbies-84-v65-sabre-build.md` | Подробные заметки по V4MuscleBike build thread Sugarkryptonite с локальным фотоархивом. |
| `Tuning/v4musclebike-upgrade-research.md` | Карта V4MuscleBike по CDI/TCI, EFI, вилкам, cafe racer проектам и настройке карбюраторов. |
| `resources.md` | Форумы, wiki, источники деталей, Facebook, Reddit и YouTube по платформе VF750. |
| `problems.md` | Типовые проблемы VF750 / V45 с симптомами, причинами и практическими решениями. |
| `HowTo/README.md` | Индекс отдельных how-to инструкций. |
| `HowTo/v4musclebike-forum-field-notes.md` | Практическая карта повторяющихся тем V4MuscleBike 1st Gen Magna/Sabre. |
| `Tuning/top-end-oiling.md` | Отдельная заметка по улучшению подачи масла к головам цилиндров. |

## Практические инструкции

`HowTo/README.md` разбивает работы по задачам: регулировка клапанов, инспекция распредвалов, top-end oil mod, снятие и установка карбюраторов, поиск проблем с подачей топлива, чистка и синхронизация карбов, зарядка, охлаждение, сцепление, подвеска, кардан, тормоза, тюнинг и fabrication для cafe racer.

`problems.md` сводит основные повторяющиеся проблемы VF750: износ распредвалов, смазка верхней части двигателя, натяжители цепей ГРМ, зарядка, карбюраторы, CDI/TCI, Pro-Link и связанные диагностические цепочки.

## Фото-референсы

Папка `Images/` содержит несколько групп:

- `Images/stock/` — стоковые фото Sabre.
- `Images/cafe-racer/` — собранные фото Sabre cafe racer.
- `Images/pinterest/` — скачанные изображения с Pinterest-доски `saber`.
- `Images/build-process/` — фото процесса сборки Perry / Inazuma, Balkan Moto, видео-референсов и архив V4MuscleBike `Newbie's '84 V65 Sabre`.
- `Images/repair-service/` — ремонтные мини-референсы по карбам и настройке.
- `Images/README.md` — индекс источников для папок с изображениями.

## Главные внешние источники

- **[V4MuscleBike](https://v4musclebike.com/forums/)** — главный форум по V45/V65 Sabre и Magna.
- **[VF1000 Forum / VF750 section](https://forum.vf1000.com/c/vf750/12)** — технические обсуждения, включая EFI и свапы.
- **[V4 Honda BBS](https://www.v4hondabbs.com)** — общий форум по Honda V4.
- **[CMSNL](https://www.cmsnl.com)** — схемы деталей и Honda microfiche.
- **[Partzilla](https://www.partzilla.com)** — поиск OEM-деталей.
- **Perry / 1984 VF700S Sabre Cafe** ([Inazuma Cafe](https://www.inazumacafe.com/2016/10/vf750-sabre-cafe.html), [CafeRacer.net](https://www.caferacer.net/threads/1984-honda-honda-vf700s-sabre-cafe.28714/)) — самый подробно задокументированный современный front-end conversion на Sabre.
- **HackAWeek / 1985 VF700S** ([site](https://hackaweek.com/hacks/the-1985-honda-vf700s-sabre-cafe-racer-conversion-begins/), [YouTube](https://www.youtube.com/watch?v=-bHv8hUwE5k)) — лучшая длинная видео-серия по Sabre cafe racer.
- **[Balkan Moto / V45 Sabre](https://www.balkanmoto.com/builds/1982-83-honda-sabre-v45-cafe-racer.php)** — честный DIY build с ошибками и исправлениями.

## Текущее состояние

Репозиторий активно используется для проекта `1982 Honda Sabre cafe racer`.

Сейчас:

- исходные мануалы обработаны в searchable и sectioned outputs;
- есть исследование по EFI, свапу вилки, cafe racer проектам и ресурсам сообщества;
- практические инструкции вынесены в `HowTo/`;
- типовые проблемы VF750 собраны в `problems.md`;
- есть отдельная статья по улучшению подачи масла к головам;
- фото-референсы разложены по stock, custom, Pinterest и build-process;
- в `ru/` начато русское зеркало ключевых статей.

Примечание: некоторые внешние сайты, особенно Reddit и Balkan Moto, могут отдавать антибот-ответы автоматическим проверкам, хотя нормально открываются в браузере.
