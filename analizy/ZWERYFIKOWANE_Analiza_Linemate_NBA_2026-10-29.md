# Analiza pickow Linemate NBA - 29/30.10.2026

Sprawdzenie: 29.10.2026 wieczorem (stats.nba.com leaguedashplayerstats / leaguegamelog 2026-27, istniejaca analiza Analiza_NBA_2026-10-29.md, kursy Betclic z Kursy_Betclic_2026-10-29.md). Model: nba_props.py (rozklad NB / normalny). BettingPros: klucz ustawiony, ale nie odpytywany ponownie (limit 429 z poprzedniej analizy); linie z pliku Betclic/Linemate. Oficjalny injury report niepotwierdzony - statusy moga sie zmienic do tip-offu.

Wszystkie probki sezonu 2026-27 to 3-4 mecze. Hit rate Linemate (np. 8/9, 13/14) obejmuje wiec w duzej mierze zeszly sezon i inne role/sklady. "p_adj Linemate" = hit rate skurczony do 50% (prior Beta(2,2): (h+2)/(n+4)). Moje p laczy srednia sezonu (regresja), minuty, status i kontekst meczu.

## Wyniki sezonu 2026-27 (stats.nba.com)

| Zawodnik | Mecze | Min | Ostatnie mecze (pkt/zb/ast) | Srednia |
|---|---|---|---|---|
| J. Fears (NO) | 4 | 22,9 | 8/3/1, 7/0/1, 10/6/2, 11/4/3 | 9,0 / 3,3 / 1,8 |
| T. Murphy III (NO) | 4 | 32,6 | 11/4/1, 9/6/3, 26/6/4, 6/1/3 | 13,0 / 4,3 / 2,8 |
| D. Sabonis (SAC) | 4 | 36,0 | 14/18/8, 27/19/10, 15/15/3, 20/14/8 | 19,0 / 16,5 / 7,3 (4/4 double-double) |
| D. Lillard (POR) | 3 | 29,4 | 25/3/6, 19/5/2, 21/5/4 | 21,7 / 4,3 / 4,0 |
| T. Jerome (MEM) | 4 | 31,3 | 45/7/6, 28/2/5, 31/4/7, 15/1/8 | 29,8 / 3,5 / 6,5 (spadek: 45-28-31-15) |

Statusy: NO na back-to-back po porazce 91-104 z DEN (-1,5 w roznicy; ryzyko skrocenia minut mlodych), Missi OUT (nieobecny centrum: ok. +1 zbiorka do rozdzielenia na Jordana, Ziona, Murphy'ego, Fearsa), SAC bez K. Murraya, Simmonsa, Raynauda, Cardwella (Sabonis w pelni obciazony). Spready: NO -5 (nie blowout), POR -6 (lekki blowout, Lillard moze stracic 2-3 min). Wszyscy w oczekiwanych skladach.

## Wycena

### 1) J. Fears (NO) vs SAC
- Over 2,5 zb (Linemate 8/9, 1,74): sezon 3,3 zb w 23 min (3 z 4 meczow >= 3). Model dla sredniej 3,4: 61,5%. Missi OUT daje male plus, B2B minus w minutach (rookie, 21-24 min zawsze). Moje p 62%, fair 1,61, EV przy 1,74 ok. +8%. Pewnosc niska-srednia.
- Over 9,5 pkt: srednia 9,0, 2/4 (10, 11). Model 43%, fair 2,32. Brak kursu w danych; rynek zapewne ok. 50% - nie typowac. Pewnosc niska.

### 2) D. Sabonis (SAC) @ NO
- Over 0,5 double-double (5/5, 1,61): sezon 4/4 DD, 16,5 zb (min 14), 19 pkt (min 14), 36 min. P(zb >= 10) ok. 89%, P(pkt >= 10) ok. 95% - DD ok. 85%. Ryzyka: blowout SAC (NO -5, nie duzy), uraz/spoczynek, Sabonis zwykle 36+ min bo SAC bez rozgrywajacych. Moje p 85%, fair 1,18. Kurs 1,61 = 62% rynkowo, co jest podejrzanie wysokie dla gracza z 85% - FLAGA: zweryfikowac, czy to na pewno rynek double-double 0,5 (a nie np. triple-double / inna linia); jesli prawdziwy, EV ok. +37%. Fair 1,18 jest na granicy filtra 1,15.
- Betclic PRA Over 34,5 (1,32): sezon srednia 42,8; po regresji ok. 40; model 76-78%, fair ok. 1,30. EV ok. 0 do +3%. Skorelowane z DD - nie lacz.

### 3) T. Murphy III (NO)
- Sezon: 4,3 zb (4, 6, 6, 1) w 32,6 min. Hit rate Linemate (13/14 i 11/14) sugeruje wyzsza srednia z zeszlego sezonu (ok. 4,5-5); mieszam: srednia 4,5, Missi OUT +0,3, B2B -0,2.
- Over 3,5 (1,37): moje p 66%, fair 1,52; rynek 73% -> EV ok. -10%. Brak value.
- Over 4,5 (1,98): moje p 47%, fair 2,13; rynek 50,5% -> EV ok. -7%. Brak value. Pewnosc niska. Kierunek zgodny z Linemate (hit rate), ale cena zjada przewage.

### 4) D. Lillard (POR) vs MEM
- Under 19,5 pkt (6/8, 1,79): sezon 21,7 (25, 19, 21) w 29 min, 1 z 3 poniżej 19,5. Sharpe OUT zwieksza uzycie pilki, MEM ma 2. obrone (DRtg 105,9), lekki blowout (-1 do -2 min). Mean 20,5 -> Under 19,5 ok. 47%. Moje p 47%, fair 2,13, EV przy 1,79 ok. -16%. Hit rate Linemate 6/8 niepotwierdzony biezacym sezonem.
- Betclic pkt 20,5 Under (1,82): p 53%, fair 1,87, EV ok. -3%. Brak value.
- Betclic PRA 24,5 Over (1,39): sezon 30,0 (regresja ok. 28,5), model ok. 65-68%, fair ok. 1,50; rynek 72% -> EV ok. -7%. Lekko ponizej ceny. Pewnosc niska (3 mecze).

### 5) T. Jerome (MEM) @ POR
- Under 6,5 ast (4/5, 1,67): sezon 6,5 ast (6, 5, 7, 8: Under w 2 z 4), ale rola rozgrywajacego bez Morantu to nowosc; regresja do ok. 5,8-6,0. Model 60,7%; moje p 61%, fair 1,64, EV przy 1,67 ok. +2%. Pewnosc niska.
- Betclic PRA Over 34,5 (1,97): surowa srednia 39,8, spadek formy (45-28-31-15), regresja do ok. 33,5; moje p Over 46%, fair 2,17, EV ok. -9%. To jest sprzeczne z wczesniejszym Under PRA 34,5 (62% w Analiza_NBA); uzgodnione: Under PRA ok. 54%, Over 46%. Nie typowac Over PRA.

## Tabela

| Pick | Kurs | Wlasne p | p_adj Linemate | p rynku (z kursu) | Fair | Pewnosc | Flagi |
|---|---|---|---|---|---|---|---|
| Fears Over 2,5 zb | 1,74 | 62% | 77% (8/9) | 57,5% | 1,61 | niska-srednia | EV ok. +8%; B2B, minuty rookie 21-24; Missi OUT na plus; probka 4 mecze |
| Fears Over 9,5 pkt | - | 43% | brak | brak kursu | 2,32 | niska | bez kursu, nie typowac |
| Sabonis Over 0,5 DD | 1,61 | 85% | 78% (5/5) | 62% | 1,18 | srednia | kurs podejrzanie wysoki - zweryfikowac rynek; fair przy filtrze 1,15; EV ok. +37% jesli prawdziwy; ryzyko minut/blowout |
| Sabonis PRA Over 34,5 (Betclic) | 1,32 | 77% | - | 75,8% | 1,30 | srednia | EV ok. 0; skorelowane z DD |
| Murphy Over 3,5 zb | 1,37 | 66% | 83% (13/14) | 73% | 1,52 | niska | EV ok. -10%; hit rate vs biezacy sezon (4,3); B2B |
| Murphy Over 4,5 zb | 1,98 | 47% | 72% (11/14) | 50,5% | 2,13 | niska | EV ok. -7% |
| Lillard Under 19,5 pkt | 1,79 | 47% | 67% (6/8) | 56% | 2,13 | niska | EV ok. -16%; biezacy sezon 21,7; Sharpe OUT; probka 3 mecze |
| Lillard Under 20,5 (Betclic) | 1,82 | 53% | - | 55% | 1,87 | niska | EV ok. -3% |
| Lillard PRA Over 24,5 (Betclic) | 1,39 | 66% | - | 72% | 1,50 | niska | EV ok. -7% |
| Jerome Under 6,5 ast | 1,67 | 61% | 67% (4/5) | 60% | 1,64 | niska | EV ok. +2%; nowa rola, 4 mecze |
| Jerome PRA Over 34,5 (Betclic) | 1,97 | 46% | - | 50,8% | 2,17 | niska | EV ok. -9%; sprzeczne z Under PRA z analizy |

## Wnioski
- Jedyne typy z dodatnim EV wg moich p: Sabonis DD (jesli kurs 1,61 prawdziwy; ale to wymaga weryfikacji), Fears Over 2,5 zb (~+8%, pewnosc niska-srednia), Jerome Under 6,5 ast (marginalnie +2%, pewnosc niska).
- Murphy i Lillard: hit rate Linemate wyglada dobrze, ale nie potwierdza go biezacy sezon 3-4 meczow i kurs jest juz uwzgledniony - brak value.
- Wszystkie pewnosci co najwyzej srednie z powodu probek 3-4 meczow i niepotwierdzonych statusow; typy Fears i Jerome sa oparte na zalozeniu, ze zagraja normalna liczbe minut. Fears i Murphy sa na B2B (NO), wiec nie lacz ich na jednym kuponie z NO ML.

To oszacowania probabilistyczne, nie gwarancje; statusy graczy moga zmienic sie do rozpoczecia meczu.
