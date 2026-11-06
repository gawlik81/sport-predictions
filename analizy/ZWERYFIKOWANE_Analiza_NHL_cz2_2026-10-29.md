# Analiza NHL cz. 2 - noc 29/30.10.2026 (czas polski)

Skill: nhl-analyst. Źródła: NHL API (tabela, terminarz, goalie leaders), DailyFaceoff (bramkarze, sprawdzono 29.10 rano/po południu czasu PL), TheOddsAPI (średnia ~20-29 książek, US/EU; oznaczone "rynek"). BettingPros: nie użyto (brak sprawdzenia klucza w tej sesji). Próba sezonu mała (11-14 meczów), więc λ mieszane z ubiegłym sezonem. Skład może zmienić się do rozpoczęcia meczu.

Back-to-back: żadna z 10 drużyn nie gra drugiego dnia z rzędu (ostatnie mecze 26-27.10, LAK 27.10 - 2 dni przerwy). Brak korekty B2B.

Rynek "ML" w tabelach = moneyline z dogrywką/karnymi. "60'" = 3-way po regulaminowym czasie.

---

### Montreal Canadiens - Dallas Stars (30.10, 01:00; 29.10 USA)
**Typ:** Dallas ML | **p:** 56,6% | **Fair:** 1,77 | **Pewność:** średnia (obaj bramkarze potwierdzeni)

| Rynek | p | fair | pewność |
|---|---|---|---|
| ML Dallas (z OT) | 56,6% | 1,77 | średnia |
| ML Montreal | 43,4% | 2,30 | niska |
| 60': Dallas / remis / MTL | 48,1% / 16,6% / 35,3% | 2,08 / 6,02 / 2,83 | niska |
| Puck line Dallas -1.5 | 31,9% | 3,13 | niska |
| Puck line MTL +1.5 | 68,1% | 1,47 | średnia |
| Total 5.5: Over / Under | 53,8% / 46,2% | 1,86 / 2,17 | niska |
| Total 6.5: Under | 59,1% | 1,69 | niska-średnia |
| Oettinger obrony Under 25.5 (śr. 25,5) | 51,9% | 1,93 | niska (brak linii rynkowej) |

**Statystyki:** DAL 7-4-1, gole 33:25 (2,75:2,08), L10 7 wygranych, ale porażka 1:5 z NJD 27.10. MTL 7-3-2, 38:36, seria 3 wygranych (2:0 z STL 27.10).
**H2H:** niska waga; nie sprawdzano aktualnego sezonu.
**Bramkarze (DailyFaceoff):** Oettinger potwierdzony (.929, GAA 1,43 - regresja do ~.912); Dobes potwierdzony (.847, GAA 4,46 - mała próba, zakładam realnie ~.895, czyli +0,1 gola dla DAL). Fowler (MTL, .942) nie startuje.
**Informacje medialne:** brak znalezionych kontuzji kluczowych graczy (wyszukiwanie nie zwróciło aktualnych źródeł - luka w danych).
**Oczekiwane gole:** DAL 3,15 - MTL 2,75 (łącznie 5,9).
**Ryzyka:** wysoka losowość; słaby Dobes może być przesadzony na małej próbie; Dallas po wysokiej porażce, regresja Oettingera.
**Rynek:** DAL 1,74 / MTL 2,73 (średnia), total 5.5 O 1,76 / U 2,09, 6.0 O 1,92 / U 1,91, DAL -1.5 2,50, MTL +1.5 1,55. Moje p DAL zbliżone do rynku (~58%), brak wyraźnego value. Over 5.5 przy 1,76 daje EV około -5% (53,8% x 1,76 = 0,95).

---

### New York Islanders - Minnesota Wild (30.10, 01:00)
**Typ:** Minnesota ML | **p:** 60,1% | **Fair:** 1,66 | **Pewność:** średnia (Wallstedt niepotwierdzony, ale to oczywisty startowy)

| Rynek | p | fair | pewność |
|---|---|---|---|
| ML Wild (z OT) | 60,1% | 1,66 | średnia |
| ML NYI | 39,9% | 2,50 | niska |
| 60': MIN / remis / NYI | 51,4% / 16,8% / 31,8% | 1,95 / 5,96 / 3,14 | niska |
| Puck line MIN -1.5 | 34,5% | 2,90 | niska |
| Puck line NYI +1.5 | 65,5% | 1,53 | średnia |
| Total 5.5: Over / Under | 48,8% / 51,2% | 2,05 / 1,95 | brak mocnego typu |
| Total 6.5: Under | 64,1% | 1,56 | niska-średnia |
| Sorokin obrony Under 24.5 (śr. 25,0) | 48,4% | 2,07 | niska |

**Statystyki:** MIN 9-3-2 (20 pkt), gole 44:31 (3,14:2,21), seria 3 W, L10 7 W. NYI 6-4-2, 36:32, 4:3 z NSH 27.10.
**Bramkarze:** Sorokin potwierdzony (.919, GAA 2,26). Wallstedt "unconfirmed" w DailyFaceoff (.922, GAA 1,99) - brak informacji o rotacji; jeśli zagra rezerwowy, p Wild spada o 3-4 pp.
**Informacje medialne:** brak aktualnych źródeł o kontuzjach (luka).
**Oczekiwane gole:** MIN 3,10 - NYI 2,50 (łącznie 5,6). Kalibracja: pierwszy szkic 3,0:2,6 dawał 56,7%, czyli ponad 5 pp pod rynkiem (rynek ~63% po usunięciu marży), podniosłem λ Wild do 3,1 (dom + forma obrony 2,21 GA).
**Ryzyka:** niepotwierdzony Wallstedt, świetny Sorokin, niski total (oba zespoły dobrze bronią), dogrywka.
**Rynek:** MIN 1,66 / NYI 2,96; total 5.5 O 1,81 / U 2,03; MIN -1.5 2,35, NYI +1.5 1,62. Under 5.5 przy 2,03 daje EV ok. +4% (51,2% x 2,03 = 1,04), ale pewność niska. Moneyline MIN przy 1,66 EV ~0%.

---

### Buffalo Sabres - Anaheim Ducks (30.10, 03:00; 29.10 USA)
**Typ:** brak mocnego typu (mecz wyrównany) | lekki faworyt Buffalo | **p:** 52,4% | **Fair:** 1,91 | **Pewność:** niska

| Rynek | p | fair | pewność |
|---|---|---|---|
| ML Buffalo (z OT) | 52,4% | 1,91 | niska |
| ML Anaheim | 47,6% | 2,10 | niska |
| 60': ANA / remis / BUF | 39,4% / 16,4% / 44,1% | 2,54 / 6,09 / 2,27 | niska |
| Puck line BUF -1.5 | 28,8% | 3,48 | niska |
| Puck line ANA +1.5 | 71,2% | 1,40 | niska |
| Total 5.5: Over | 57,8% | 1,73 | niska |
| Total 6.5: Over / Under | 45,0% / 55,0% | 2,22 / 1,82 | niska |

**Statystyki:** BUF 5-4-3, 33:41 (2,75:3,42), 2:0 u SJS 27.10. ANA 5-6-1, 37:43 (3,08:3,58), seria OT porażki, 5:6 z VAN 27.10. Obie drużyny tracą dużo.
**Bramkarze:** Ellis (BUF) "likely" (.902, GAA 2,27); Husso (ANA) niepotwierdzony (.888, GAA 3,09) - słaby. Lyon (BUF) poza grą do końca sezonu (DailyFaceoff).
**Oczekiwane gole:** ANA 3,00 - BUF 3,15 (łącznie 6,15).
**Ryzyka:** niepotwierdzeni obaj bramkarze, ANA zmiana na rezerwowego możliwa, mecz coin flip.
**Rynek:** BUF 1,87 / ANA 2,45 (rynek ~52% BUF - zgodne); total 6.5 O 1,85 / U 1,99. Under 6.5 przy 1,99 daje EV ok. +9% (55% x 1,99 = 1,09), ale pewność niska, bo oba bramkarze niepotwierdzeni, obie obrony słabe (przechylenie ku Over). Traktować ostrożnie.

---

### Ottawa Senators - Los Angeles Kings (30.10, 03:00)
**Typ:** brak mocnego typu | lekki faworyt Ottawa | **p:** 52,4% | **Fair:** 1,91 | **Pewność:** niska

| Rynek | p | fair | pewność |
|---|---|---|---|
| ML Ottawa (z OT) | 52,4% | 1,91 | niska |
| ML Kings | 47,6% | 2,10 | niska |
| 60': LAK / remis / OTT | 39,3% / 16,6% / 44,1% | 2,54 / 6,04 / 2,27 | niska |
| Puck line OTT -1.5 | 28,6% | 3,50 | niska |
| Puck line LAK +1.5 | 71,4% | 1,40 | średnia |
| Total 5.5: Over / Under | 56,2% / 43,8% | 1,78 / 2,28 | niska |
| Total 6.5: Under | 56,6% | 1,77 | niska |
| Johansson obrony Over 24.5 (śr. 25,0) | 51,6% | 1,94 | niska |

**Statystyki:** OTT 8-5-0, 39:38, przegrane 1:4 z VGK 27.10. LAK 3-6-2, 28:37 (2,55:3,36) - najsłabsza ofensywa z tej piątki, 1:2 z CHI 27.10.
**Bramkarze:** Johansson (OTT) potwierdzony (.891) - Ullmark (.945) kontuzja (lower body), poza grą jeszcze ok. tydzień; Kuemper (LAK) potwierdzony (.888, GAA 3,46). Obaj bramkarze poniżej średniej, dlatego λ obu ~3,0.
**Oczekiwane gole:** LAK 2,95 - OTT 3,10 (łącznie 6,05).
**Ryzyka:** mecz wyrównany, słabi bramkarze podnoszą wariancję, LAK ma problem ze strzelaniem (2,55), ale gra u siebie.
**Rynek:** OTT 2,03 / LAK 2,24 (rynek ~52% OTT - zgodne); total 5.5 O 1,79 / U 2,05, 6.0 O 2,00 / U 1,84; LAK +1.5 1,39 (EV około -1%).

---

### Vancouver Canucks - San Jose Sharks (30.10, 03:00)
**Typ:** San Jose ML | **p:** 53,1% | **Fair:** 1,88 | **Pewność:** niska-średnia

| Rynek | p | fair | pewność |
|---|---|---|---|
| ML Sharks (z OT) | 53,1% | 1,88 | niska-średnia |
| ML Vancouver | 46,9% | 2,13 | niska |
| 60': SJS / remis / VAN | 45,1% / 15,9% / 39,0% | 2,22 / 6,28 / 2,57 | niska |
| Puck line SJS -1.5 | 30,0% | 3,33 | niska |
| Puck line VAN +1.5 | 70,0% | 1,43 | średnia |
| Total 5.5: Over | 63,1% | 1,58 | średnia |
| Total 6.5: Over / Under | 50,6% / 49,4% | 1,98 / 2,02 | brak mocnego typu |
| Askarov obrony Over 25.5 (śr. 26,0) | 51,6% | 1,94 | niska |

**Statystyki:** SJS 6-6-1, 37:45 (2,85:3,46), L10 4 W, 0:2 z BUF 27.10. VAN 3-10-1, 43:65 (3,07:4,64) - najgorsza defensywa ligi (regresja do ~3,6, ale nadal bardzo słaba), 6:5 w ANA 27.10.
**Bramkarze:** Askarov (SJS) potwierdzony (.898, GAA 3,13); Merilainen (VAN) potwierdzony (.900, GAA 3,44).
**Oczekiwane gole:** SJS 3,35 - VAN 3,15 (łącznie 6,5).
**Ryzyka:** małe próbki, Vancouver strzela dużo mimo bilansu (wysokie tempo), więc Under jest ryzykowny; faworyt SJS niewielki.
**Rynek:** SJS 1,72 / VAN 2,75 (rynek ~58% SJS, ja 53%: -5 pp, zgodnie z regułą nie schodzę niżej bez konkretu); total 6.5 O 1,82 / U 2,03; SJS -1.5 2,37; VAN +1.5 1,61 (EV ok. +13%: 70% x 1,61 = 1,13, pewność średnia). Over 5.5 (fair 1,58) - linia 5.5 u bukmacherów nie była dostępna w zebranych danych; sprawdzić kurs przed użyciem.

---

## Ranking kandydatów (fair odds > 1,15)

| # | Mecz | Rynek | p | Fair | Pewność | Kurs rynku | Uwagi |
|---|---|---|---|---|---|---|---|
| 1 | VAN @ SJS | VAN +1.5 (puck line) | 70,0% | 1,43 | średnia | 1,61 | EV ok. +13%, oba bramkarze potwierdzeni |
| 2 | MTL @ DAL | MTL +1.5 | 68,1% | 1,47 | średnia | 1,55 | EV ok. +5% |
| 3 | NYI @ MIN | NYI +1.5 | 65,5% | 1,53 | średnia | 1,62 | EV ok. +6%; zależne od Wallstedta |
| 4 | OTT @ LAK | LAK +1.5 | 71,4% | 1,40 | średnia | 1,39 | EV ok. -1% |
| 5 | NYI @ MIN | Wild ML | 60,1% | 1,66 | średnia | 1,66 | EV ok. 0%; Wallstedt niepotwierdzony |
| 6 | NYI @ MIN | Under 6.5 | 64,1% | 1,56 | niska-średnia | brak w danych | sprawdzić kurs |
| 7 | MTL @ DAL | Dallas ML | 56,6% | 1,77 | średnia | 1,74 | EV ok. -2% |
| 8 | BUF @ ANA | Under 6.5 | 55,0% | 1,82 | niska | 1,99 | EV ok. +9%, ale bramkarze niepotwierdzeni |

Pasuje do kuponu (p > 50%, kurs > 1,2): puck line +1.5 (VAN, MTL, NYI) i Dallas/Minnesota ML. Typy z fair odds <= 1,15 pominięto (BTTS tak 88-92%, fair 1,08-1,14). Dodatkowe uwagi: +1.5 to wysoka powtarzalność, ale krótki kurs (1,55-1,62); łączenie nóg ML i puck line tego samego meczu jest skorelowane.

## Luki w danych
- Brak aktualnych previewów i raportów kontuzji dla większości zespołów (wyszukiwarka zwróciła głównie ubiegłe sezony). Kontuzje poza Ullmarkiem (OTT) i Lyonem (BUF) nieznane.
- Brak xG/CF% (MoneyPuck/NST) - λ opierają się na golach, bramkarzach i regresji do średniej.
- Rynki zawodnika (strzały, punkty, strzelec gola): nie wyceniono, bo brak drugiego niezależnego źródła średnich i potwierdzonych linii/PP; zgodnie ze skillem nie rekomenduję ich na kupon. Wyceniono tylko obrony bramkarzy (szkice, bez linii rynkowych, niska pewność, nie do kuponu).
- Bramkarze sprawdzeni w dniu meczu (DailyFaceoff); niepotwierdzeni: Wallstedt (MIN), Husso (ANA), Ellis (BUF - likely). Sprawdzić ponownie po porannym skate.

To oszacowania probabilistyczne, nie gwarancje.
