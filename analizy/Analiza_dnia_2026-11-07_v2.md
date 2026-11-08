# Analiza dnia 2026-11-07 (v2): noc NBA + NHL

Zakres: NBA 7 meczów, NHL 12 meczów (07.11 wieczór - 08.11 rano, czas PL). Źródła i ograniczenia danych w sekcjach poniżej.

## NBA
# NBA 07.11.2026 (daty PL: 07.11 23:00 - 08.11 04:00) - analiza 7 meczów

Źródła: ESPN (scoreboard, standings, injuries, news), stats.nba.com (leaguedashteamstats / leaguedashplayerstats, sezon 2026-27, 7-10 meczów na drużynę), Pinnacle (tylko DEN-IND: pełne rynki), FanDuel (CDN odds feed: ML i spread), DraftKings (ESPN odds: spread/total/ML), model `nba_model.py` / `nba_props.py`. Sprawdzono 07.11.2026 (przed meczami; injury report NBA z wieczoru nie był dostępny - statusy z ESPN z 06.11, część wpisów dotyczy meczów z 06.11).
BettingPros: nie użyto (brak klucza w sesji nieinteraktywnej) - pominięte źródło.
Early season (7-10 meczów): SD różnicy podniesione do 12-12,5 przy niejasnych statusach; stat. mieszane z oceną składów.

Uwaga ogólna dot. rynków zawodnika: nie mam linii bukmacherskich dla propów (tylko Pinnacle team totals w DEN-IND), więc linie propów są ORIENTACYJNE (blisko mojej średniej). Wszystkie propy = pewność niska/średnia, bez statusu "typ na kupon" dopóki nie ma realnej linii, kursu i potwierdzonego składu.

## Kontekst B2B (wyniki z 06.11)
ATL (WAS@ATL, w), CLE (PHI@CLE), OKC (@MEM), WAS (@ATL), SAS (@SAC), POR (@LAL, 118-124) - wszyscy grają drugi dzień z rzędu. Rywale BKN, NYK, GSW, ORL, HOU, PHX nie grali 06.11 (odpoczęci). DEN-IND: mecz w Meksyku (City, ok. 2240 m n.p.m., podobnie jak Denver) - brak realnej przewagi gospodarza dla IND, DEN zaaklimatyzowane.

## Statystyki drużyn (stats.nba.com, 2026-27)
| Drużyna | Bilans | Net | ORtg | DRtg | Pace |
|---|---|---|---|---|---|
| DEN | 4-3 | +0,1 | 115,1 | 115,0 | 98,5 |
| IND | 3-6 | -2,5 | 109,5 | 112,0 | 101,8 |
| BKN | 2-6 | -6,4 | 106,2 | 112,6 | 99,0 |
| ATL | 6-4 | +3,1 | 114,5 | 111,4 | 103,1 |
| NYK | 4-4 | +4,7 | 113,3 | 108,5 | 97,0 |
| CLE | 5-4 | +4,3 | 115,9 | 111,6 | 101,7 |
| WAS | 4-5 | -0,8 | 111,7 | 112,5 | 99,8 |
| OKC | 7-2 | +4,2 | 113,0 | 108,8 | 98,9 |
| ORL | 2-6 | -8,9 | 107,4 | 116,3 | 98,6 |
| GSW | 6-3 | +4,5 | 117,0 | 112,5 | 100,6 |
| HOU | 7-2 | +10,4 | 120,0 | 109,6 | 98,2 |
| PHX | 2-5 | -6,8 | 114,7 | 121,4 | 99,6 |
| SAS | 7-2 | +9,1 | 117,1 | 108,1 | 99,4 |
| POR | 6-2 | +8,6 | 120,0 | 111,4 | 101,0 |

---

## 1) Denver Nuggets @ Indiana Pacers (NBA Mexico City Game; 07.11 23:00 PL, 16:00 lok.)
**Typ:** DEN wygrywa | **p:** 73,6% (rynek bez marży Pinnacle 72,5%) | **fair:** 1,36 | **Pewność:** średnia
**Rynek:** Pinnacle IND +7 (+101) / DEN -7 (-112); ML IND +253 / DEN -294; total 230,5 (-107/-105); team total IND 111,5, DEN 118,5. DK: DEN -7,5, 229,5, ML -268/+220. FD: DEN -7,5 (1,95), ML 1,34/3,40.
**Oczekiwane punkty:** DEN 118,7 - IND 111,3 (spread DEN -7,4; total 230,0)
**Injury (ESPN 06.11):** IND bez Haliburtona (min. 2 tyg.), Sheppard out; McConnell questionable (hamstring), Oubre Jr. questionable (calf), Furphy out. DEN: Strawther out; DeRozan probable (back). Jokić, Murray w pełnym składzie.
**H2H:** niewiele waży; skład IND bez rozgrywającego numer 1.
**Statystyki:** DEN ORtg 115,1 / pace 98,5 (wolne), IND pace 101,8 (szybsze) -> total w okolicach linii. IND bez Haliburtona spada do ORtg ~108.
**Ryzyka:** spread -7,5 ~ p 50% (brak edge); mecz neutralny - model nie daje IND home +2,5. Blowout (DEN +12) skraca minuty Jokicia/Murraya. Zmiana statusu DeRozana, Oubre, McConnella.

| Rynek | Linia | p | fair | Pewność |
|---|---|---|---|---|
| Zwycięzca DEN | ML | 73,6% | 1,36 | średnia |
| Zwycięzca IND | ML | 26,4% | 3,79 | średnia |
| Spread DEN | -7,0 | 51,3% | 1,95 | niska (=rynek) |
| Spread IND | +7,5 | 50,3% | 1,99 | niska |
| Total | 230,5 | O 48,9% / U 51,1% | 2,05 / 1,96 | niska (=rynek) |
| Total | 229,5 | O 51,1% / U 48,9% | 1,96 / 2,05 | niska |
| Total IND | 111,5 | O 49,3% / U 50,7% | 2,03 / 1,97 | niska |
| Total DEN | 118,5 | O 50,7% / U 49,3% | 1,97 / 2,03 | niska |

Rynki zawodnika (linie orientacyjne, średnie sezonowe skorygowane):
| Zawodnik | Rynek / linia | p Over | fair O | Uwagi |
|---|---|---|---|---|
| Jokić | PRA 43,5 (śr. 42,4) | 43,1% (U 56,9% / 1,76) | 2,32 | spread -7,5: lekkie ryzyko blowoutu; niska |
| Murray | pkt 24,5 (śr. 24,8 skor.) | 48,4% | 2,07 | niska |
| Murray | 3PM 3,5 (śr. 3,9) | 54,2% | 1,84 | niska/średnia |
| Siakam | pkt 20,5 (śr. 21,8 bez Haliburtona) | 54,0% | 1,85 | wymaga potwierdzenia składu IND; niska |
| Nembhard | ast 6,5 (śr. 7,2, McConnell Q) | 56,1% | 1,78 | zależne od McConnella; niska |

---

## 2) Brooklyn Nets @ Atlanta Hawks (08.11 01:30 PL, 07.11 19:30 ET; ATL B2B)
**Typ:** ATL wygrywa | **p:** 69,4% (rynek DK bez marży ok. 70,1%) | **fair:** 1,44 | **Pewność:** średnia
**Rynek:** DK ATL -7,5 (-104), total 227,5, ML ATL -269 / BKN +221; FD ATL -7,5 (1,87), ML 1,385/3,15 (ATL).
**Oczekiwane punkty:** ATL 116,3 - BKN 109,7 (ATL -6,6; total 226,0; B2B ATL: -1 do -1,5 w różnicy i -1,5 w sumie względem rynku)
**Injury:** ATL: Jalen Johnson (ankle) out w piątek, status na sobotę niepotwierdzony - zakładam brak/ograniczony wymiar (jeden z top-2 w ATL; -3 w różnicy już w modelu), Landale, Gilbert, Newell out. BKN: Sharpe day-to-day, Bilodeau out; Porter Jr. i Randle zdrowi (wg ESPN).
**Statystyki:** ATL net +3,1 (3 wygrane z rzędu, pace 103,1); BKN net -6,4, DRtg 112,6, 2-6.
**H2H:** brak istotnego.
**Ryzyka:** ATL B2B + ewentualny brak Johnsona; wymuszone minuty dla ławki; spread -7,5 daje wyraźnie <50% na pokrycie.

| Rynek | Linia | p | fair | Pewność |
|---|---|---|---|---|
| Zwycięzca ATL | ML | 69,4% | 1,44 | średnia |
| Spread BKN | +7,5 | 53,0% | 1,89 | niska |
| Spread ATL | -6,5 | 50,3% | 1,99 | niska |
| Total | 227,5 | U 53,3% / O 46,7% | 1,88 / 2,14 | niska (Under = B2B ATL, bez konkretu poza tym) |
| Total ATL | 115,5 | O 52,9% | 1,89 | niska |
| Total BKN | 110,5 | U 52,9% | 1,89 | niska |

Rynki zawodnika (orientacyjne):
| Zawodnik | Rynek / linia | p Over | fair O | Uwagi |
|---|---|---|---|---|
| Alexander-Walker (ATL) | 3PM 3,5 (śr. 4,1) | 56,2% | 1,78 | B2B ryzyko minut; niska |
| Randle (BKN) | pkt 19,5 (śr. 21,0) | 55,3% | 1,81 | niska |
| Porter Jr. (BKN) | pkt 20,5 (śr. 21,4) | 51,7% | 1,93 | niska |
| Okongwu (ATL) | reb 7,5 (śr. 8,6) | 59,4% | 1,68 | status Johnsona wpływa na zbiórki (+); niska/średnia |

---

## 3) New York Knicks @ Cleveland Cavaliers (08.11 02:00 PL, 20:00 ET; CLE B2B)
**Typ:** NYK wygrywa | **p:** 63,5% (rynek DK bez marży 63,0%) | **fair:** 1,58 | **Pewność:** średnia
**Rynek:** DK NYK -4,5 (-110), total 224,5, ML NYK -191 / CLE +160; FD CLE +4,5 (1,96), ML CLE 2,72 / NYK 1,49.
**Oczekiwane punkty:** NYK 114,2 - CLE 110,4 (NYK -3,8; total 224,6)
**Injury:** NYK: Hart out (ankle) - rotacja i zbiórki; Towns, Brunson, Anunoby gotowi. CLE: Allen out (knee, 06.11), Tyson out, Merrill out (elbow) w piątek - zakładam, że status na sobotę ten sam (niepotwierdzone); Mitchell, Mobley, Harden zdrowi. CLE B2B (po PHI).
**Statystyki:** NYK DRtg 108,5, pace 97,0 (najwolniejsza liga), CLE ORtg 115,9. NYK odpoczęci.
**Ryzyka:** wolne tempo NYK (-); CLE bez Allena traci obronę obręczy; Hart out osłabia NYK. Pewność średnia, spread =~ rynek.

| Rynek | Linia | p | fair | Pewność |
|---|---|---|---|---|
| Zwycięzca NYK | ML | 63,5% | 1,58 | średnia |
| Spread CLE | +4,5 | 52,2% | 1,91 | niska |
| Spread NYK | -3,5 | 51,0% | 1,96 | niska |
| Total | 224,5 | O 50,2% / U 49,8% | 1,99 / 2,01 | niska |
| Total | 223,5 | O 52,4% / U 47,6% | 1,91 / 2,10 | niska |
| Total NYK | 113,5 | O 52,5% | 1,90 | niska |
| Total CLE | 110,5 | O 49,6% / U 50,4% | 2,01 / 1,99 | niska |

Rynki zawodnika (orientacyjne):
| Zawodnik | Rynek / linia | p Over | fair O | Uwagi |
|---|---|---|---|---|
| Brunson | pkt 25,5 (śr. 25,6; Hart out +) | 46,3% (z 25,4) | 2,16 | niska |
| Towns | reb 12,5 (śr. 13,6; CLE bez Allena) | 51,9% | 1,93 | niska/średnia |
| Mitchell | pkt 22,5 (śr. 22,6, użycie + bez Allena/Tysona) | 54,9% (śr. 24) | 1,82 | CLE B2B, niska |
| Harden | ast 5,5 (śr. 5,9) | 52,2% | 1,92 | niska |

---

## 4) Washington Wizards @ Oklahoma City Thunder (08.11 02:00 PL, 20:00 CT; obie B2B)
**Typ:** OKC wygrywa | **p:** 77,6% (rynek DK bez marży 81,2%) | **fair:** 1,29 | **Pewność:** średnia (fair <1,30 - typ na kupon tylko w kombinacji; ≤1,15 nie dotyczy)
**Rynek:** DK OKC -11,5 (-115), total 222,5, ML OKC -545 / WAS +411; FD OKC -11,5 (1,95).
**Oczekiwane punkty:** OKC 115,5 - WAS 105,5 (OKC -10,0; total 221,0). Schodzę 3,6 pp pod rynek ze względu na decymację składu OKC (J. Williams, Holmgren, Wallace, Topic, Sorber, Jaylin Williams out), WAS grał wczoraj (AD out w piątek, status niepotwierdzony).
**Injury:** OKC: SGA, Mitchell, McCain, Hartenstein zdrowi. WAS: Davis out (ankle) w piątek, Vukcevic out, Beekman out; Young, George, Dybantsa gotowi.
**Ryzyka:** blowout skraca minuty SGA; spread -11,5 to p ~45% (model), bez edge; B2B obu drużyn - Under lekko faworyzowany, ale konkretu brak.

| Rynek | Linia | p | fair | Pewność |
|---|---|---|---|---|
| Zwycięzca OKC | ML | 77,6% | 1,29 | średnia |
| Spread WAS | +11,5 | 54,8% | 1,83 | niska |
| Spread OKC | -9,5 | 51,6% | 1,94 | niska |
| Total | 222,5 | U 53,3% / O 46,7% | 1,88 / 2,14 | niska/średnia (b2b obu drużyn) |
| Total | 221,5 | O 48,9% / U 51,1% | 2,05 / 1,96 | niska |
| Total OKC | 114,5 | O 53,6% | 1,86 | niska |
| Total WAS | 107,5 | U 57,2% (rynek +3 pp: 55%) | 1,75 | niska |

Rynki zawodnika (orientacyjne; blowout!):
| Zawodnik | Rynek / linia | p | fair | Uwagi |
|---|---|---|---|---|
| SGA | pkt 29,5 (śr. 29,9; skor. 28,3 za blowout) | U 58,8% | 1,70 | ryzyko blowoutu obniża minuty; niska |
| T. Young | ast 9,5 (śr. 9,6, AD out +) | O 48,2% | 2,07 | niska |
| Hartenstein | reb 8,5 (śr. 9,7) | O 59,9% | 1,67 | OKC bez Holmgrena; niska/średnia |

---

## 5) Orlando Magic @ Golden State Warriors (08.11 02:30 PL, 17:30 PT)
**Typ:** GSW wygrywa | **p:** 69% (model 69,1%, rynek DK bez marży 65,7%) | **fair:** 1,45 | **Pewność:** średnia
**Rynek:** DK GSW -5,5 (-106), total 222,5, ML GSW -217 / ORL +180; FD ORL +5,5 (1,87).
**Oczekiwane punkty:** GSW 114,3 - ORL 107,8 (GSW -6,5; total 222,1)
**Injury:** ORL: Banchero out (high-ankle, 4-6 tyg.), Suggs out, Isaac out, Penda out - brak dwóch z trzech najlepszych graczy; Wagner, Bane, Carter Jr. grają. GSW: Curry zdrowy (29,9 pkt), Draymond questionable (elbow), Payton II questionable, Santos DTD; Butler III (ACL), Moody out, Porzingis wycofał się z gry.
**Statystyki:** GSW 6 wygranych z rzędu, ORtg 117,0, ORL DRtg 116,3 (25.), 3 porażki z rzędu. Rynek zaniża przewagę GSW, ale -5,5 jest zbliżone do mojej linii.
**Ryzyka:** Draymond Q (zbiórki/asysty, obrona); ORL rozegranie bez Suggsa; GSW rotacja na minutach Curry (28,7 min).

| Rynek | Linia | p | fair | Pewność |
|---|---|---|---|---|
| Zwycięzca GSW | ML | 69% | 1,45 | średnia |
| Spread GSW | -5,5 | 53,3% | 1,88 | niska/średnia |
| Spread GSW | -4,5 | 56,6% | 1,77 | niska |
| Total | 222,5 | O 49,1% / U 50,9% | 2,04 / 1,97 | niska |
| Total GSW | 113,5 | O 52,9% | 1,89 | niska |
| Total ORL | 108,5 | U 52,5% | 1,90 | niska |

Rynki zawodnika (orientacyjne):
| Zawodnik | Rynek / linia | p Over | fair O | Uwagi |
|---|---|---|---|---|
| Curry | pkt 28,5 (śr. 29,9; ~29 skor.) | 49,5% | 2,02 | niska (blowout niskie) |
| Curry | 3PM 4,5 (śr. 4,7) | 48,4% | 2,07 | niska |
| Curry | 3PM 3,5 | 66,8% | 1,50 | średnia (dobra podłoga); wymaga realnego kursu |
| Wagner (ORL) | pkt 20,5 (śr. 19,6 + użycie bez Banchero ~21) | 49,4% | 2,02 | niska |
| Bane (ORL) | 3PM 3,5 (śr. 3,5) | 46,1% | 2,17 | niska |

---

## 6) Houston Rockets @ Phoenix Suns (08.11 03:00 PL, 18:00 MT/PT)
**Typ:** HOU wygrywa | **p:** 74% (po korekcie; model 77,3%, rynek DK bez marży 71,0%) | **fair:** 1,35 | **Pewność:** średnia
**Rynek:** DK HOU -7,5 (-103), total 223,5, ML HOU -284 / PHX +231; FD HOU -7,5 (1,95).
**Oczekiwane punkty:** HOU 116,0 - PHX 107,5 (HOU -8,5; total 223,5)
**Injury:** HOU: Capela out (ankle), Adams out - brak centrów w rotacji, ale Sengun gra 35 min; Durant, Smith Jr., Thompson, VanVleet zdrowi. PHX: Mark Williams out, Goodwin doubtful, Fleming Q; Booker, Brooks, Bridges, Green zdrowi. Oba zespoły odpoczęte.
**Statystyki:** HOU net +10,4 (ORtg 120,0, DRtg 109,6, 7-2); PHX DRtg 121,4 (29. w lidze), rebounding najsłabszy (DREB 60,1%) -> przewaga HOU na zbiórkach nawet bez Capeli.
**Ryzyka:** model +6 pp nad rynkiem -> ściągnięte do +3 pp (zasada kalibracji); spread HOU -7,5 ~ 53% (słaby edge).

| Rynek | Linia | p | fair | Pewność |
|---|---|---|---|---|
| Zwycięzca HOU | ML | 74% (model 77,3%) | 1,35 | średnia |
| Spread HOU | -7,5 | 53,3% | 1,88 | niska/średnia |
| Spread HOU | -6,5 | 56,6% | 1,77 | niska/średnia |
| Total | 223,5 | O 50,0% / U 50,0% | 2,00 | niska |
| Total HOU | 115,5 | O 51,8% | 1,93 | niska |
| Total PHX | 108,5 | U 53,6% | 1,86 | niska |

Rynki zawodnika (orientacyjne):
| Zawodnik | Rynek / linia | p | fair | Uwagi |
|---|---|---|---|---|
| Booker | pkt 25,5 (śr. 25,4; HOU DRtg 109,6) | U 56,8% | 1,76 | niska; wynik wyrównany do blowoutu -> minuty OK |
| Sengun | PRA 37,5 (śr. 39,6; bez Capeli) | O 57,2% | 1,75 | niska/średnia |
| Durant | pkt 19,5 (śr. 20,8) | O 54,1% | 1,85 | niska |
| J. Smith Jr. | 3PM 2,5 (śr. 3,0) | O 57,1% | 1,75 | niska |

---

## 7) San Antonio Spurs @ Portland Trail Blazers (08.11 04:00 PL, 19:00 PT; obie B2B)
**Typ:** SAS wygrywa | **p:** 64,4% (rynek DK bez marży 65,7%) | **fair:** 1,55 | **Pewność:** niska/średnia
**Rynek:** DK SAS -5,5 (-112), total 226,5, ML SAS -217 / POR +180; FD POR +5,5 (1,91).
**Oczekiwane punkty:** SAS 114,3 - POR 110,2 (SAS -4,1; total 224,5; B2B obu: -2 do sumy względem rynku)
**Injury:** SAS: Wembanyama (52 pkt wczoraj w SAC, ESPN), Harper, Castle, Fox zdrowi; Tobias Harris out (calf), Quaintance out. POR: Morant out (hamstring, ok. 4 tyg.), Sharpe out (meniskus), Krejci out; Avdija, Lillard, Holiday, Clingan grają. Obie drużyny B2B; POR przegrała wczoraj z LAL 118-124 (Dončić 53).
**Statystyki:** SAS net +9,1 (DRtg 108,1, 7 z rzędu), POR net +8,6 (ORtg 120,0, 6-2).
**Ryzyka:** Wembanyama po 52 pkt/B2B (zmęczenie, minuty); wyrównane mecze (spread 4-5) = niska pewność; Under łączy B2B obu drużyn - jedyny konkret.

| Rynek | Linia | p | fair | Pewność |
|---|---|---|---|---|
| Zwycięzca SAS | ML | 64,4% | 1,55 | niska/średnia |
| Spread POR | +5,5 | 54,5% | 1,84 | niska |
| Spread SAS | -4,5 | 48,7% | 2,05 | niska |
| Total | 226,5 | U 54,4% -> (rynek +3 pp: 53%) | 1,84 | niska/średnia (B2B obu) |
| Total | 224,5 | O 50,0% / U 50,0% | 2,00 | niska |
| Total SAS | 114,5 | O 49,3% | 2,03 | niska |
| Total POR | 111,5 | U 54,7% | 1,83 | niska |

Rynki zawodnika (orientacyjne):
| Zawodnik | Rynek / linia | p | fair | Uwagi |
|---|---|---|---|---|
| Wembanyama | pkt 28,5 (śr. 29,1; B2B ~28,5) | O 49,5% | 2,02 | niska; wysoka wariancja |
| Wembanyama | reb 12,5 (śr. 12,6; B2B ~12,4) | O 46,2% | 2,17 | niska |
| Avdija | pkt 22,5 (śr. 23,3; Morant out + użycie) | O 48,3% | 2,07 | niska |
| Lillard | pkt 20,5 (śr. 20,4) | U 54,1% | 1,85 | niska |
| Clingan | reb 9,5 (śr. 10,6) | O 58,4% | 1,71 | POR bez Morantа zbiórek nie zmienia; niska/średnia |

---

## Ranking (wszystkie rynki, fair >1,15; kandydaci na kupon)
| Mecz | Rynek | p | fair | Pewność | Zależy od | Kurs rynku znany |
|---|---|---|---|---|---|---|
| HOU @ PHX | HOU wygrywa | 74% | 1,35 | średnia | Capela/Adams out (uwzględnione) | DK 1,35 (-284) - tak |
| DEN @ IND | DEN wygrywa | 73,6% | 1,36 | średnia | DeRozan, Oubre/McConnell | Pinnacle 1,34 / DK 1,37 |
| WAS @ OKC | OKC wygrywa | 77,6% | 1,29 | średnia | brak (blowout bez znaczenia dla ML) | DK 1,18 (-545) - EV ujemne |
| ATL vs BKN | ATL wygrywa | 69,4% | 1,44 | średnia | Jalen Johnson, B2B | DK 1,37 (-269) |
| GSW vs ORL | GSW wygrywa | 69% | 1,45 | średnia | Draymond Q | DK 1,46 (-217) |
| NYK @ CLE | NYK wygrywa | 63,5% | 1,58 | średnia | stan Allena/CLE rotacji | DK 1,52 (-191) |
| SAS @ POR | SAS wygrywa | 64,4% | 1,55 | niska/śr. | B2B obu | DK 1,46 (-217) |
| SAS @ POR | Under 226,5 | ~53% | 1,89 | niska | B2B obu | DK 1,89 |

EV: tylko HOU ML ~ -0 (fair = rynek), brak wyraźnej wartości; model mieści się w przedziale rynku (±4 pp) - NBA rynek efektywny. Mocnych edge nie ma; mecze 1, 3, 7 są w kategorii "brak mocnego typu" na spread i total.

## Podsumowanie rynków (zwięźle)
Statusy z ESPN z 06.11; injury report NBA z wieczoru 07.11 nie był dostępny. Zmiana statusu Jalena Johnsona (ATL), Anthony'ego Davisa (WAS), Allena/Tysona/Merrilla (CLE), Draymonda (GSW), DeRozana/Oubre/McConnella (DEN/IND) może zmienić linie o 1-4 pkt. To oszacowania probabilistyczne, nie gwarancje.

## NHL - część 1 (18:30-01:00)
# NHL 07.11.2026 - analiza (6 meczów, część 1) - plik roboczy

Sprawdzenie danych: 07.11.2026 ok. 15:15-16:00 UTC (kursy Pinnacle/DraftKings last_update 15:14-15:16Z, DailyFaceoff przed porannymi potwierdzeniami). **Żaden z 12 bramkarzy ważnych dla tych 6 meczów nie jest potwierdzony** (poza "Likely" Sorokin NYI), więc pewność każdego rynku meczu to najwyżej niska/średnia, a rynek obron bramkarza nie dostaje typu. Skład może się zmienić do rozpoczęcia meczu. BettingPros: pominięty (brak weryfikacji klucza API w tej sesji, nie blokowało analizy).

Źródła: NHL.com API (tabela, statystyki drużyn, bramkarzy), ESPN (injuries), DailyFaceoff (bramkarze, składy WSH), Pinnacle i DraftKings przez theoddsapi/pinnacle MCP (kursy dziesiętne; Pinnacle = "rynek"), NHL.com skater leaders (props). Brak dostępu do MoneyPuck/NaturalStatTrick (403/404), więc **xG/CF%/GSAx nie zostały pobrane**: λ opiera się na GF/GA na mecz, strzałach za/przeciw, PP%/PK%, SV% bramkarzy i kursie rynkowym. To obniża pewność (jedno źródło liczb dla rynków zawodnika).

Rozliczenie: moneyline, puck line i total (6.0 / 6.5 / 5.5) liczone **z dogrywką i karnymi (gol w OT liczy się do totalu, gol z karnych nie)**; "60'" = 3-way po regulaminie. Wszystkie 12 drużyn miało co najmniej 1 dzień przerwy (żadnej drugiej nogi back-to-back; 6.11 grały tylko CBJ-BUF, SJS-MIN, ANA-CGY; 5.11 STL, NJD, NYI, UTA, MTL, NYR, NSH grały, więc odpoczynek 1 dzień).

Średnia ligi ~3,0 gola/drużynę. Pierwsze ~15-17 meczów sezonu: próby małe, wagi ostrożne.

---

## 1) Florida Panthers @ Washington Capitals (07.11, 18:30 PL; 12:30 ET)

**Typ:** brak mocnego typu na zwycięzcę (WSH ML 54,9%). Najlepszy rynek: FLA +1.5 (z OT) | **p 69,4%** | fair 1,44 | pewność niska-średnia
**Statystyki:** WSH 14 m., GF 3,50 / GA 3,43, PP 21,6%, PK 76,1% (słaby), strzały 27,6/27,6; FLA 16 m., GF 3,25 / GA 2,94, PP 24,0%, PK 84,6%, strzały 28,8 za / 24,2 przeciw (dobry udział w strzałach). Tabela: WSH 8-6-0 (16 pkt), FLA 9-5-2 (20 pkt).
**Kontuzje (ESPN):** FLA bez Barkova (IR do 27.11) i Marchanda (IR do 21.11), Gadjovich IR; WSH bez Sandina i Desharnais (obrońcy). Skład WSH (DailyFaceoff, 6.11): Ovechkin, Strome-Kyrou-Tuch, Wilson, Chychrun/Roy.
**Bramkarze:** WSH Logan Thompson (.887, GAA 3,22; niepotwierdzony, prawie pewny); FLA Akira Schmid (.889, 2,86; 7 z 8 startów, DailyFaceoff: niepotwierdzony) vs Markstrom (.885, 8 GS). Obaj bramkarze FLA poniżej średniej, więc różnica Schmid/Markstrom mała (≈0,05 gola).
**H2H:** niska waga (skład i bramkarze zmienione); nie pobrano szczegółów.
**Oczekiwane gole:** WSH 3,15 - FLA 2,85 (razem 6,0). Korekty: dom +0,1, brak Barkova/Marchanda -0,25 dla FLA (przy bazowej sile ataku 3,25 GF), słaby PK WSH +0,1 dla FLA, słabi bramkarze obu stron +0,1 dla obu.
**Rynek (Pinnacle):** ML WSH 1,83 / FLA 2,08 (no-vig WSH 53,2%, FLA 46,8%); PL FLA +1.5 1,45 / WSH -1.5 2,92; total 6.0 (O 1,84 / U 2,06; DK 6.5 O 2,00/U 1,83). Różnica modelu vs rynek: WSH +1,7 pp (w normie).

| Rynek | Linia | p | fair | Rynek (kurs) | Pewność |
|---|---|---|---|---|---|
| Moneyline (z OT) | WSH | 54,9% | 1,82 | 1,83 | niska (bramkarze niepotw.) |
| Moneyline (z OT) | FLA | 45,1% | 2,22 | 2,08 | niska |
| 60' 3-way | WSH / X / FLA | 46,5 / 16,6 / 37,0% | 2,15 / 6,04 / 2,71 | 60' WSH 2,28 / X 4,38 / FLA 2,60 (Pinnacle 3-way) | niska |
| Puck line | FLA +1.5 | 69,4% | 1,44 | 1,45 (EV +0,6%) | niska-średnia |
| Puck line | WSH -1.5 | 30,6% | 3,27 | 2,92 | niska |
| Total (z OT) | Over 5.5 / Under 5.5 | 55,4% / 44,6% | 1,80 / 2,24 | O 5.5 1,66 (Pinn. alt.) | niska |
| Total (z OT) | Over 6.5 / Under 6.5 | 42,5% / 57,5% | 2,35 / 1,74 | O 6.5 2,05 (Pinn. alt.) | niska |
| BTTS (60') | tak | 90,2% | 1,11 | - | pomijać (fair ≤ 1,15) |

Rynki zawodnika: Tkachuk (FLA, 22 pkt w 16 m.) punkty: średnia na mecz 1,3 (po odjęciu Barkova większa rola, WSH PK słaby): Over 0,5 pkt 71,9% fair 1,39; Over 1,5 37,1% fair 2,70. **Pewność niska** (jedno źródło, rola PP niepotwierdzona). Brak typu na obrony bramkarzy (niepotwierdzeni).
**Ryzyka:** zmiana bramkarza (Schmid/Markstrom, Lindgren za Thompsona), dogrywka (16-17% meczów) rozstrzyga ML i PL, pusta bramka zawyża różnice, nowa gwiazda wraca w FLA = λ FLA +0,2. Kursy z godz. 15:16Z, mecz startuje 17:30Z.

---

## 2) St. Louis Blues @ Nashville Predators (07.11, 19:00 PL; 13:00 ET)

**Typ:** brak mocnego typu (STL 51,7% vs NSH 48,3%). Najlepszy: NSH +1.5 | **p 72,5%** | fair 1,38 | pewność niska
**Statystyki:** NSH 16 m. (7-4-5, 19 pkt), GF 3,00 / GA 2,94, PP 29,6% (świetny), PK 90,0%, strzały 25,8 za / 29,2 przeciw (gra na bramkarzu, bilans strzałów słaby); STL 16 m. (7-7-2, 16 pkt), GF 3,06 / GA 3,13, PP 21,3%, PK 85,7%, strzały 27,2 / 28,8. STL po dogrywce z NJD (4-5 OT, 5.11).
**Kontuzje (ESPN):** NSH: Marchessault Day-to-Day (planowany powrót 7.11, niepotwierdzony); STL: Dube (IR), Krug, Tucker, Mailloux (D, IR do 25.11).
**Bramkarze:** NSH Juuse Saros (.908, 2,77; niepotwierdzony); STL Joel Hofer (.918, 2,39, 11 z 11 startów; niepotwierdzony). Hofer wyraźnie ponad średnią (SV% regresja możliwa); w λ STL zmniejszone o 0,1 vs sama GF.
**H2H:** niska waga, brak danych.
**Oczekiwane gole:** NSH 2,85 - STL 2,95 (razem 5,8). Dom +0,1, PP NSH silne +0,05, Hofer -0,1 dla NSH, STL bez dwóch obrońców +0,05 dla NSH.
**Rynek (Pinnacle):** ML NSH 2,02 / STL 1,88 (no-vig NSH 48,2%, STL 51,8%); PL NSH +1.5 1,39 / STL -1.5 3,17; total 6.0 (O 1,98 / U 1,90; DK 5.5 O 1,77/U 2,10). Zgodność z rynkiem bardzo dobra.

| Rynek | Linia | p | fair | Rynek (kurs) | Pewność |
|---|---|---|---|---|---|
| Moneyline (z OT) | NSH | 48,3% | 2,07 | 2,02 | niska |
| Moneyline (z OT) | STL | 51,7% | 1,94 | 1,88 | niska |
| 60' 3-way | NSH / X / STL | 39,9 / 17,0 / 43,1% | 2,51 / 5,90 / 2,32 | - | niska |
| Puck line | NSH +1.5 | 72,5% | 1,38 | 1,39 (EV +0,8%) | niska |
| Puck line | STL +1.5 | 75,2% | 1,33 | brak w feedzie | niska |
| Puck line | NSH -1.5 / STL -1.5 | 24,8% / 27,5% | 4,04 / 3,64 | STL -1.5 3,17 | niska |
| Total (z OT) | Over 5.5 / Under 5.5 | 52,2% / 47,8% | 1,92 / 2,09 | DK O 1,77 / U 2,10 | niska |
| Total (z OT) | Over 6.5 / Under 6.5 | 39,3% / 60,7% | 1,65 / ... (fair O 2,55 / U 1,65) | ok. O 2,3 (alt.) | niska |

Rynki zawodnika: Forsberg (NSH, 19 pkt) i Josi (D, 18 pkt) wysokie punkty, ale brak drugiego źródła/roli PP w tej sesji: **nie rekomendowane**. Obrony: Hofer (średnia 25,0 obron: Over 24,5 51,6% fair 1,94; Over 25,5 44,7%) i Saros: niepotwierdzeni = **bez typu**.
**Ryzyka:** niepotwierdzeni bramkarze (Saros/Hofer rotują), Marchessault, dogrywka (17%), duża zmienność SV% Hofera.

---

## 3) New York Rangers @ Seattle Kraken (07.11, 23:00 PL; 17:00 ET)

**Typ:** NYR ML (z OT) | **p 54,9%** | fair 1,82 | pewność niska (rynek 1,78, EV -2,3%). Mecz wyrównany/brak mocnego typu.
**Statystyki:** SEA 15 m. (9-5-1, 19 pkt), GF 3,47 / GA 3,53 (najsłabsza obrona z 12), PK 65,0% (bardzo słabe), PP 21,6%, strzały 25,5 za / 30,5 przeciw; NYR 17 m. (9-7-1, 19 pkt), GF 3,00 / GA 2,88, PK 90,6%, PP 20,0%, strzały 25,5 / 26,5, FO 54,0%.
**Kontuzje (ESPN):** NYR: Shesterkin (G) out do końca sezonu (kolano), Durzi (D) wraca 9.11, Veleno IR; SEA: McCann (LW, IR do 2.01), Lindgren (D, IR do 19.11), Melanson, Douglas.
**Bramkarze:** NYR Dylan Garand (.906, 2,52, 11 GS; niepotwierdzony); SEA Joey Daccord (.889, 3,53, 7 GS; niepotwierdzony).
**H2H:** niska waga, bez danych.
**Oczekiwane gole:** SEA 2,9 - NYR 3,2 (razem 6,1). Dom +0,1; SEA obrona/PK słabe +0,15 dla NYR; brak McCanna -0,15 dla SEA; Garand ponad średnią -0,1 dla SEA.
**Rynek (Pinnacle):** ML NYR 1,78 / SEA 2,16 (no-vig NYR 54,8%, SEA 45,2%) - identyczne z modelem; PL NYR -1.5 2,99 / SEA +1.5 1,43; total 6.5 (O 2,04 / U 1,85).

| Rynek | Linia | p | fair | Rynek (kurs) | Pewność |
|---|---|---|---|---|---|
| Moneyline (z OT) | NYR | 54,9% | 1,82 | 1,78 | niska-średnia |
| Moneyline (z OT) | SEA | 45,1% | 2,22 | 2,16 | niska |
| 60' 3-way | SEA / X / NYR | 37,1 / 16,4 / 46,5% | 2,70 / 6,09 / 2,15 | - | niska |
| Puck line | SEA +1.5 | 69,2% | 1,44 | 1,43 (EV -1,0%) | niska |
| Puck line | NYR -1.5 | 30,8% | 3,25 | 2,99 | niska |
| Total (z OT) | Over 5.5 / Under 5.5 | 57,0% / 43,0% | 1,75 / 2,33 | - | niska |
| Total (z OT) | Over 6.5 / Under 6.5 | 44,2% / 55,8% | 2,26 / 1,79 | O 2,04 / U 1,85 (no-vig O 47,5%) | niska |

Rynki zawodnika: Fox (NYR, D, 21 pkt) - brak roli PP/drugiego źródła: bez typu. Obrony Daccord (Over 24,5: 53,0% fair 1,89, średnia 25,2) - niepotwierdzony, bez typu.
**Ryzyka:** Garand/ewentualna rotacja w bramce NYR (jedyny pewny bramkarz po kontuzji Shesterkina, ale 2 GS bez startu w 13 m.), słaby PK SEA może podbić gole, mecz po podróży NYR na zachód (dwa dni przerwy, nieokreślony efekt stref czasowych).

---

## 4) Montreal Canadiens @ Toronto Maple Leafs (08.11, 01:00 PL; 19:00 ET)

**Typ:** brak mocnego typu (MTL 51,6% vs TOR 48,4%). Najlepszy: TOR +1.5 | **p 71,7%** | fair 1,39-1,40 | pewność niska (rynek 1,42, EV +1,8%)
**Statystyki:** TOR 17 m. (8-7-2, 18 pkt), GF 3,65 / GA 3,24, PP 28,8%, PK 88,1%, strzały 28,2 / 29,7; MTL 16 m. (10-3-3, 23 pkt, najlepszy bilans z 12), GF 3,44 / GA 3,19, PP 14,0% (słabe), PK 78,5%, strzały 27,6 / 28,3. MTL wygrała 5-4 w OT z UTA 5.11.
**Kontuzje (ESPN):** TOR: Tavares (powrót 7.11, niepotwierdzony), Marchenko (do 17.11), Blankenburg, Rifai (8.11), Merzlikins (G, długo); MTL: Demidov (RW, do 14.11), Matheson (D, do 14.11), Montembeault (G, Day-to-Day).
**Bramkarze:** MTL Jacob Fowler (.925, 2,17, 9 GS; niepotwierdzony; Montembeault DTD, więc Fowler prawdopodobny); TOR Sergei Bobrovsky (.889, 3,27, 11 GS; niepotwierdzony) lub Stolarz (.910, 2,66, 6 GS). Rozstrzygnięcie Bobrovsky/Stolarz = ≈0,3 gola; w λ przyjęto Bobrovsky (ostrożnie).
**H2H:** niska waga, bez danych.
**Oczekiwane gole:** TOR 3,1 - MTL 3,2 (razem 6,3). Dom +0,1; Fowler (SV% .925 - regresja ×0,5) -0,15 dla TOR; Bobrovsky +0,15 dla MTL; brak Demidova -0,1 dla MTL; PP TOR vs PK MTL 78,5% +0,05.
**Rynek (Pinnacle):** ML MTL 1,84 / TOR 2,08 (no-vig MTL 53,0%, TOR 47,0%); PL MTL -1.5 3,05 / TOR +1.5 1,42; total 6.5 (O 1,88 / U 2,00; DK O 1,87/U 1,95).

| Rynek | Linia | p | fair | Rynek (kurs) | Pewność |
|---|---|---|---|---|---|
| Moneyline (z OT) | MTL | 51,6% | 1,94 | 1,84 | niska |
| Moneyline (z OT) | TOR | 48,4% | 2,07 | 2,08 | niska |
| 60' 3-way | TOR / X / MTL | 40,3 / 16,2 / 43,4% | 2,48 / 6,16 / 2,30 | - | niska |
| Puck line | TOR +1.5 | 71,7% | 1,40 | 1,42 (EV +1,8%) | niska |
| Puck line | MTL +1.5 | 74,3% | 1,35 | brak w feedzie | niska |
| Puck line | MTL -1.5 / TOR -1.5 | 28,3% / 25,7% | 3,53 / 3,89 | MTL -1.5 3,05 | niska |
| Total (z OT) | Over 5.5 / Under 5.5 | 60,1% / 39,9% | 1,66 / 2,51 | - | niska |
| Total (z OT) | Over 6.5 / Under 6.5 | 47,4% / 52,6% | 2,11 / 1,90 | O 1,88 / U 2,00 (no-vig O 51,5%) | niska |

Rynki zawodnika (niska pewność, jedno źródło NHL.com, rola PP niepotwierdzona): Matthews (TOR, 26 pkt w 17 m., lider) punkty Over 0,5 średnia 1,3: p 71,9% fair 1,39; Over 1,5: 37,1% fair 2,70. Strzały Matthewsa przy średniej 3,6: Over 2,5 67,1% fair 1,49, Over 3,5 47,3% fair 2,11 (średnia strzałów z szacunku, nie z logu). Strzelec gola (0,42/mecz): 34,3% fair 2,92. Wszystko skorelowane z wynikiem TOR; bez typu na kupon do czasu potwierdzenia składu i linii.
**Ryzyka:** niepotwierdzeni bramkarze obu stron (Bobrovsky/Stolarz, Fowler/Montembeault), powrót Tavaresa, regresja SV% Fowlera, derby = wysoka zmienność.

---

## 5) Utah Mammoth @ Ottawa Senators (08.11, 01:00 PL; 19:00 ET)

**Typ:** UTA ML (z OT) | **p 53,2%** | fair 1,88 | pewność niska (rynek UTA 1,86, EV -1,0%). Brak mocnego typu.
**Statystyki:** UTA 17 m. (10-6-1, 21 pkt), GF 3,59 / GA 3,47, **PP 38,3%**, PK 70,4% (słaby), strzały 29,7 / 25,4 (dobry bilans strzałów); OTT 17 m. (10-6-1, 21 pkt), GF 3,06 / GA 3,06, PP 12,1% (bardzo słabe), PK 73,8%, strzały 25,9 / 27,1.
**Kontuzje (ESPN):** OTT: Ullmark (G, IR do 10.11, nie gra), Greig (C, out), Foegele, Burakovsky, Eklund (IR); UTA: Yamamoto (RW, do 11.11), Marino (D, do 14.11), Nate Schmidt (D, Day-to-Day, 7.11).
**Bramkarze:** OTT Samuel Ersson (.880, 3,33, 5 GS; niepotwierdzony) - alternatywa Johansson (.848, 4,60); UTA Karel Vejmelka (.872, 3,31, 11 GS; niepotwierdzony). Oba duety słabe; na OTT gorszy bramkarz rezerwowy = wrażliwość λ ±0,2.
**H2H:** niska waga, bez danych.
**Oczekiwane gole:** OTT 3,0 - UTA 3,2 (razem 6,2). Dom +0,1; Ersson/Vejmelka obaj poniżej średniej (+0,15 dla każdej strony); PP UTA 38,3% vs PK OTT 73,8% +0,1 dla UTA; PP OTT 12,1% -0,05; brak Greiga/kontuzje ataku OTT -0,1.
**Rynek (Pinnacle):** ML OTT 2,05 / UTA 1,86 (no-vig OTT 47,6%, UTA 52,4%); PL OTT +1.5 1,41 / UTA -1.5 3,10; total 6.5 (O 1,93 / U 1,96; DK O 1,89/U 1,93).

| Rynek | Linia | p | fair | Rynek (kurs) | Pewność |
|---|---|---|---|---|---|
| Moneyline (z OT) | UTA | 53,2% | 1,88 | 1,86 | niska |
| Moneyline (z OT) | OTT | 46,8% | 2,14 | 2,05 | niska |
| 60' 3-way | OTT / X / UTA | 38,7 / 16,3 / 45,0% | 2,58 / 6,12 / 2,22 | - | niska |
| Puck line | OTT +1.5 | 70,5% | 1,42 | 1,41 (EV -0,6%) | niska |
| Puck line | UTA +1.5 | 75,8% | 1,32 | brak w feedzie | niska |
| Puck line | UTA -1.5 / OTT -1.5 | 29,5% / 24,2% | 3,39 / 4,13 | UTA -1.5 3,10 | niska |
| Total (z OT) | Over 5.5 / Under 5.5 | 58,6% / 41,4% | 1,71 / 2,41 | - | niska |
| Total (z OT) | Over 6.5 / Under 6.5 | 45,8% / 54,2% | 2,18 / 1,84 | O 1,93 / U 1,96 (no-vig O 50,4%) | niska |

Uwaga do totalu: model (45,8% Over 6.5) jest 4,6 pp poniżej rynku mimo słabych bramkarzy i PP UTA 38%. Zgodnie z kalibracją nie schodzimy pod rynek o >5 pp bez konkretu; ewentualny Over wymagałby potwierdzenia Ersson/Johansson i gry UTA bez zmian. Rozsądny zakres Over 6.5: 46-50%.
Rynki zawodnika: Keller (UTA, 22 pkt w 17 m.) punkty średnia 1,2: Over 0,5 69,0% fair 1,45; Over 1,5 33,6% fair 2,98. Stützle (OTT, 22 pkt) punkty 1,2 (wsparcie: słaby Vejmelka): te same wartości. **Niska pewność**, brak potwierdzenia linii/PP; bez typu.
**Ryzyka:** Ersson vs Johansson (Ullmark out), Vejmelka najsłabszy SV%, dogrywka (UTA grała ostatnio dwie dogrywki), nietypowo wysoka zmienność PP.

---

## 6) New Jersey Devils @ New York Islanders (08.11, 01:00 PL; 19:00 ET)

**Typ:** NJD ML (z OT) | **p 55,9%** | fair 1,79 | pewność niska-średnia (rynek 1,68 = NJD 58,1% bez marży; model 2,2 pp niżej). Najlepszy EV: NYI +1.5 | **p 69,2%** | fair 1,44 | rynek 1,50 (Pinnacle) / 1,49 (DK), **EV +3,8%** | pewność niska-średnia.
**Statystyki:** NJD 16 m. (11-5-0, 22 pkt, seria 3 W), GF 3,50 / GA 2,94, strzały **32,9 za** / 25,0 przeciw (najlepszy bilans), PP 18,0%, PK 67,6% (słaby); NYI 15 m. (7-6-2, 16 pkt, seria 2 L), GF 2,80 / GA 2,87, PP 14,6%, PK 86,5%, strzały 25,6 / 27,1, FO 55,5%. NJD 5-4 OT z STL 5.11; NYI 3-5 z CAR 5.11.
**Kontuzje (ESPN):** NYI: Barzal (C, IR do 14.11, kolano), Pulock (D), Maccelli (LW), Ritchie, Romanov; NJD: Casey (D, do 21.11). NYI mocno osłabiona w ataku.
**Bramkarze:** NYI Ilya Sorokin (.911, 2,41, 10 GS; **Likely**, Stefen Rosner / DailyFaceoff); NJD Jake Allen (.887, 3,11, 8 GS; niepotwierdzony; DailyFaceoff typuje Allena, drugi bramkarz NJD nie został zidentyfikowany w danych, więc ryzyko rotacji). Przewaga bramkowa NYI w bramce ≈ +0,25 gola.
**H2H:** niska waga, bez danych.
**Oczekiwane gole:** NYI 2,65 - NJD 3,0 (razem 5,65). Dom +0,1; Barzal out -0,15 dla NYI; Sorokin (.911) -0,15 dla NJD; Allen (.887) +0,1 dla NYI; dominacja strzałów NJD +0,1.
**Rynek (Pinnacle):** ML NJD 1,68 / NYI 2,33 (no-vig NJD 58,1%, NYI 41,9%); PL NJD -1.5 2,74 / NYI +1.5 1,50; total 6.0 (O 2,00 / U 1,88); DK 5.5 O 1,77 / U 2,10.

| Rynek | Linia | p | fair | Rynek (kurs) | Pewność |
|---|---|---|---|---|---|
| Moneyline (z OT) | NJD | 55,9% | 1,79 | 1,68 (EV -6,1%) | niska-średnia |
| Moneyline (z OT) | NYI | 44,1% | 2,27 | 2,33 (EV +2,8%) | niska |
| 60' 3-way | NYI / X / NJD | 35,8 / 17,0 / 47,2% | 2,80 / 5,87 / 2,12 | - | niska-średnia |
| Puck line | NYI +1.5 | 69,2% | 1,44 | 1,50 (EV +3,8%) | niska-średnia |
| Puck line | NJD +1.5 | 78,7% | 1,27 | brak w feedzie | niska-średnia |
| Puck line | NJD -1.5 / NYI -1.5 | 30,8% / 21,3% | 3,25 / 4,71 | NJD -1.5 2,74 | niska |
| Total (z OT) | Over 5.5 / Under 5.5 | 49,7% / 50,3% | 2,01 / 1,99 | DK O 1,77 / U 2,10 | niska |
| Total (z OT) | Over 6.5 / Under 6.5 | 36,8% / 63,2% | 2,72 / 1,58 | alt. | niska |
| Total (z OT) | Over 6.0 (push na 6) | ok. 44% bez push (model 5,65) | - | O 2,00 / U 1,88 | niska |

Wniosek totalu: model 5,65 vs rynek 6,0; lekki skłon do Under 6.0/6.5 (Sorokin + słaby atak NYI), ale rynek podobny (U 1,88-2,10) i brak konkretu poza bramkarzem, więc pewność niska. Under 6.5 (63,2%) wymagałby ostrożności: Poisson zaniża ogon wysokich wyników (kalibracja 29-30.10).
Rynki zawodnika: **Sorokin obrony** (jedyny bramkarz "Likely"): oczekiwane strzały NJD ≈ 30 (NJD SF 32,9 vs NYI SA 27,1 uśrednione) × SV% .915 ≈ 27,4 obron. Over 25,5: 60,9% fair 1,64; Over 26,5: 54,3% fair 1,84; Over 27,5: 47,5% fair 2,10; Under 28,5: 59,0% fair 1,70. **Niska pewność** (Likely, nie confirmed; tylko jedno źródło liczb). Jack Hughes (NJD, 21 pkt w 16 m.) punkty średnia 1,2: Over 0,5 69,0% fair 1,45, Over 1,5 33,6% fair 2,98 - niska pewność, bez typu (brak drugiego źródła/roli PP).
**Ryzyka:** Allen może rotować, Sorokin nie potwierdzony oficjalnie, NYI bez Barzala, ewentualna dogrywka (NJD i NYI grają dużo OT), NJD ma PK 67,6%, a NYI PP 14,6% (neutralizuje).

---

## Ranking kandydatów (wszystkie rynki, fair > 1,15, wszystkie z niską/niską-średnią pewnością - bramkarze niepotwierdzeni)

| # | Mecz | Rynek | p | fair | Kurs rynku | EV | Zależy od |
|---|---|---|---|---|---|---|---|
| 1 | NJD @ NYI | NYI +1.5 (z OT) | 69,2% | 1,44 | 1,50 | +3,8% | Sorokin (Likely), Allen |
| 2 | MTL @ TOR | TOR +1.5 (z OT) | 71,7% | 1,40 | 1,42 | +1,8% | Bobrovsky/Stolarz, Fowler |
| 3 | STL @ NSH | NSH +1.5 (z OT) | 72,5% | 1,38 | 1,39 | +0,8% | Saros/Hofer |
| 4 | FLA @ WSH | FLA +1.5 (z OT) | 69,4% | 1,44 | 1,45 | +0,6% | Schmid/Markstrom, Thompson |
| 5 | NJD @ NYI | Sorokin Over 25,5 obron | 60,9% | 1,64 | brak | n/d | Sorokin start (Likely), linia nieznana |
| 6 | NJD @ NYI | NYI ML | 44,1% | 2,27 | 2,33 | +2,8% | model niżej od rynku o 2,2 pp (NJD), niska pewność |
| 7 | UTA @ OTT | UTA ML | 53,2% | 1,88 | 1,86 | -1,0% | Ersson/Johansson |
| 8 | NYR @ SEA | NYR ML | 54,9% | 1,82 | 1,78 | -2,3% | Garand, Daccord |

Nie wchodzi do rankingu: ML faworytów (EV ujemne lub ≈0), BTTS (fair ≈1,10, ≤ 1,15), rynki zawodnika bez potwierdzenia składu/roli PP, obrony bramkarzy poza Sorokinem. Puck line +1.5 to wyłącznie "bezpieczniejsza" opcja o krótkich kursach 1,39-1,50; wygrywa także przy porażce 1 golem w OT i w regulaminie, przegrywa tylko przy porażce 2+ golami.

**Tabela kandydatów na kupon (dla bet-slip-builder):** powyższe pozycje 1-4 (puck line +1.5) mają fair 1,38-1,44 (powyżej 1,15, ale blisko dolnej granicy kursu 1,2 dla nóg), p 69-72,5%. Kursy Pinnacle/DraftKings (brak Betclic w tej analizie, trzeba sprawdzić). Wszystkie niepotwierdzone co do bramkarzy: sprawdzić poranne skate (DailyFaceoff) przed złożeniem kuponu.

*To są oszacowania probabilistyczne, nie gwarancje; skład, bramkarze i kursy mogą zmienić się do rozpoczęcia meczu.*

## NHL - część 2 (02:00-04:00)
# NHL - analiza 6 meczów, noc 07/08.11.2026 (godziny PL) - plik tymczasowy

Źródła: NHL standings (MCP nhl_standings), ESPN (scoreboard, injuries, team stats), DailyFaceoff (bramkarze, sprawdzone 07.11 przed meczami), kursy US (theoddsapi: DraftKings/FanDuel/BetMGM, dziesiętne). BettingPros: pominięte (nie sprawdzano klucza). Pinnacle: mecze nie w liście highlighted. Kursy to rynek US (z dogrywką; total/ML z OT).
Ograniczenia: xG/CF%/GSAx i średnie zawodników (strzały, punkty) NIE zostały pobrane z drugiego niezależnego źródła -> rynki zawodnika tylko orientacyjne, bez rekomendacji. Bramkarze startowi niepotwierdzeni poza Pickardem (MIN). Sezon: 14-18 meczów, próba mała, λ z regresją do średniej ligi (~3,0).

Tabela (GP, W-L-OT, GF/GA na mecz): CAR 18, 13-3-2, 3.83/2.39 | CHI 17, 4-12-1, 2.18/3.94 | DAL 16, 9-5-2, 2.81/2.38 | SJ 18, 7-10-1, 2.50/3.61 | MIN 18, 12-3-3, 3.33/2.17 | TBL 15, 10-3-2, 3.73/3.07 | COL 17, 9-6-2, 4.00/3.29 | DET 17, 7-7-3, 2.88/3.06 | LAK 14, 5-7-2, 3.07/3.36 | PIT 16, 5-9-2, 3.19/3.63 | EDM 17, 11-3-3, 4.18/3.12 | VAN 18, 3-14-1, 2.94/4.61.

---
## 1) Chicago Blackhawks @ Carolina Hurricanes (08.11, 02:00; 07.11 20:00 ET)
Bramkarze (DailyFaceoff, niepotw.): CHI Knight (4-9, .891, GAA 3.34); CAR Kochetkov (10-1, .922, GAA 1.64). Kontuzje: CHI Byram (IR), Kane (out); CAR Staal (IR), Nikishin (out). CAR 7-3 w ost. 10 (W1), CHI 2 wygrane w 10 (L3).
λ: CAR 3.9 - CHI 2.3 (suma 6.2). Rynek: CAR ML 1.21-1.23 (~78% bez marży), total 6.5 (O 2.05/U 1.80), CAR -1.5 1.57.
Rynek / p / fair / pewność:
- Moneyline (z OT): CAR 74% (fair 1.35) | CHI 26% (3.89) - pewność średnia (kurs 1.22 = brak EV)
- 60' 3-way: CAR 66.9% (1.49) | X 13.5% (7.40) | CHI 19.5% (5.12)
- Puck line: CAR -1.5 50.9% (1.97) / CHI +1.5 49.1% (2.04); CAR +1.5 89.9% (1.11, pomijać)
- Total (z OT): Over 6.5 45.2% (2.21) / Under 6.5 54.8% (1.82); Over 5.5 58.6% (1.71) - pewność niska
- BTTS (60') 88.2% - fair 1.13 (pomijać)
Ryzyka: Kochetkov niepotw. (zmiana = CAR -0.3 gola), CHI wyjazd 3. porażka z rzędu ale underdog; gole w pustą bramkę.

## 2) San Jose Sharks @ Dallas Stars (08.11, 02:00; SJ back-to-back po MIN 06.11)
Bramkarze (niepotw.): SJ Nedeljkovic (3-2-1, .899; Keyser na IR, więc to realny startowy mimo B2B); DAL Oettinger (8-3-1, .909, GAA 1.90). Kontuzje: DAL Heiskanen (out), Duchene, Back, Krys, Capobianco (IR), Steel DTD; SJ Wennberg, Chernyshov, Musty, Keyser (IR). SJ L4.
λ: DAL 3.5 - SJ 2.4 (SJ: baza 2.5 -0.1 B2B; DAL: Heiskanen -0.1, obrona nadal top). Suma 5.9. Rynek: DAL ML 1.33 (~71% bez marży), -1.5 ~1.85, total 6.5 (O 2.05/U 1.80).
- Moneyline (z OT): DAL 67.6% (1.48) | SJ 32.4% (3.09) - pewność średnia. Model podciągnięty do ~rynku (-3 pp), bo wyjściowo 64.6% było >5 pp pod rynkiem bez konkretu.
- 60' 3-way: DAL 59.5% (1.68) | X 15.3% (6.53) | SJ 25.2% (3.97)
- Puck line: DAL -1.5 42.7% (2.34) / SJ +1.5 57.3% (1.75); DAL +1.5 86.3% (1.16)
- Total: Over 6.5 ~40% / Under 6.5 ~57% (fair ~1.75; model 59%, zcapowane do rynku +3 pp wg reguły); Over 5.5 ~54%
Ryzyka: B2B SJ może oznaczać rezerwowego (jeśli nie Nedeljkovic = po prostu zmiana); Oettinger niepotw.; DAL tylko 2.81 GF/g.

## 3) Tampa Bay Lightning @ Minnesota Wild (08.11, 02:00; MIN back-to-back)
Bramkarze: MIN Pickard POTWIERDZONY (1-1, .833, GAA 3.50; Wallstedt odpoczywa na B2B, Gustavsson IR); TBL Vasilevskiy niepotw. (8-3-1, .886 - słabo jak na niego). Kontuzje: MIN Spurgeon, Faber, M. i N. Foligno (IR), McCarron DTD; TBL Gourde (IR). MIN W3, TBL W2 (10-3-2).
λ: MIN 3.1 - TBL 3.5 (MIN -0.1 B2B, -0.15 brak 2 obrońców, Pickard +0.3 dla TBL; Vasilevskiy .886 +0.1 dla MIN). Suma 6.6. Rynek: TBL ML ~1.70 (57%), TBL -1.5 2.8, total 6.5 (O 2.0/U 1.83).
- Moneyline (z OT): TBL 56.2% (1.78) | MIN 43.8% (2.28) - pewność niska/średnia (kurs TBL 1.70 -> EV ~-4%; MIN 2.16-2.20 ~EV -5%)
- 60' 3-way: TBL 48.2% (2.07) | X 15.7% (6.38) | MIN 36.1% (2.77)
- Puck line: TBL -1.5 32.9% (3.04) / MIN +1.5 67.1% (1.49); TBL +1.5 77.5% (1.29)
- Total: Over 6.5 52.1% -> po korekcie do rynku 49-50% (fair ~2.0), Over 5.5 ~64% (1.58) - niska
Ryzyka: Pickard to rezerwowy z .833 (mała próba), ale MIN to drużyna z GA 2.17; Vasilevskiy niepotw.; wysoka wariancja.

## 4) Detroit Red Wings @ Colorado Avalanche (08.11, 03:00)
Bramkarze (niepotw.): COL Blackwood (8-3-1, .892, GAA 2.80); DET Tarasov (2-2-1, .938, GAA 1.57, mała próba; Gibson DTD). Kontuzje: DET Larkin, Kasper, Appleton, Edvinsson, Johansson (IR), Gibson DTD; COL Manson (out), L'Heureux. COL: 2 OT-porażki ostatnio, GF 4.00/g; DET 5 W w 10, L2.
λ: COL 3.7 - DET 2.8 (suma 6.5). Rynek: COL ML 1.43-1.44 (~66%), -1.5 2.05-2.2, total 6.5 (1.98/1.85).
- Moneyline (z OT): COL 63.9% (1.56) | DET 36.1% (2.77) - pewność średnia (kurs COL 1.43: brak EV; DET 2.85-2.88 EV ~ +3% przy 36%, niska pewność)
- 60' 3-way: COL 56.0% (1.79) | X 15.1% (6.63) | DET 28.9% (3.46)
- Puck line: COL -1.5 40.1% (2.49) / DET +1.5 59.9% (1.67); COL +1.5 83.2% (1.20)
- Total: Over 6.5 50.4% (1.98) / Under 49.6% (2.02); Over 5.5 63.1% (1.58) - niska
Ryzyka: Tarasov z .938 to szum małej próby; brak Larkina u DET obniża atak; Blackwood słaby SV%.

## 5) Pittsburgh Penguins @ Los Angeles Kings (08.11, 03:00)
Bramkarze (niepotw.): PIT Murashov (0-4-1, .868, GAA 3.83); LAK Kuemper (5-3-1, .884, GAA 3.45). Obaj słabi. Kontuzje: PIT Rust, Soderblom, van Riemsdyk, Graves (IR); LAK Zuccarello, Fiala, Turcotte, Dvorak, Jenik (IR). PIT L3 (5-9-2), LAK W1 (14 meczów).
λ: LAK 3.4 - PIT 3.1 (suma 6.5; słabi bramkarze podbijają obie strony, ale bez ataku obu). Rynek: LAK ML 1.77-1.83 (~53%), -1.5 2.8-2.94, total 6.5 (2.0/1.83).
- Moneyline (z OT): LAK 54.7% (1.83) | PIT 45.3% (2.21) - BRAK mocnego typu (wyrównany), pewność niska
- 60' 3-way: LAK 46.7% (2.14) | X 15.9% (6.30) | PIT 37.5% (2.67)
- Puck line: LAK -1.5 31.4% (3.19) / PIT +1.5 68.6% (1.46); LAK +1.5 76.5% (1.31)
- Total: Over 6.5 50.6% (1.98) / Under 49.4% (2.02); Over 5.5 63.1% (1.58) - niska/średnia; Over wspierany słabymi bramkarzami, ale bramkarz niepotw.
Ryzyka: zmiana bramkarza (PIT backup Jarry? nie sprawdzono), duża losowość.

## 6) Vancouver Canucks @ Edmonton Oilers (08.11, 04:00)
Bramkarze (niepotw.): VAN Lankinen (1-8, .804, GAA 6.03 - katastrofa; Demko IR); EDM Jarry (4-1-3, .898, GAA 2.56) - Jarry w ESPN DTD, Andersen i Levi na IR -> RYZYKO: gdy Jarry nie zagra, EDM ma poważny problem z bramką. Kontuzje: EDM Hyman, Howard, Savoie, Janmark, Regula, Leppanen (IR); VAN Chytil, Thomas, MacEachern (IR), Willander DTD. VAN 3-14-1 (L4, GA 4.61/g), EDM 11-3-3 (GF 4.18/g).
λ: EDM 4.2 - VAN 2.6 (suma 6.8; Lankinen .804 + defensywa VAN dają EDM wysokie λ; Hyman -0.1). Rynek: EDM ML 1.29-1.32 (~75-77%), -1.5 1.67-1.69, total 6.5-7.0 (6.5 O 1.66/U 2.24 DK; BetMGM 7.0 O 2.05).
- Moneyline (z OT): EDM 73.3% (1.36) | VAN 26.7% (3.74) - pewność średnia (kurs 1.29-1.32 -> EV ujemne)
- 60' 3-way: EDM 66.2% (1.51) | X 13.1% (7.64) | VAN 20.7% (4.83)
- Puck line: EDM -1.5 50.9% (1.96) / VAN +1.5 49.1% (2.04); EDM +1.5 88.8% (1.13, pomijać). Kurs EDM -1.5 1.68 vs fair 1.96: EV ujemne wg modelu (rynek wycenia ~58-59%)
- Total: Over 6.5 ~55% (fair ~1.82; wcześniejsze 4.0/2.7 dawało 53.4%), Over 7.5 ~37% (2.7), Over 5.5 ~67% (1.50) - średnia/niska. Rynek 6.5 O 1.66 = ~57-58%
Ryzyka: status Jarry'ego (DTD), wysoka wariancja Lankinena; blowout/pusta bramka; EDM po wolnych wygranych.

---
## Rynki zawodnika (orientacyjnie, BEZ rekomendacji)
Nie pobrano średnich zawodników z dwóch niezależnych źródeł ani składów/linii/PP, więc zgodnie z SKILL.md brak typów. Wzorce z nhl_props.py (do użycia po uzupełnieniu danych):
- Strzały gwiazdy ze średnią 3.6: Over 2.5 67%, Over 3.5 47%.
- Strzelec gola przy średniej 0.45/mecz: 36% (fair 2.76); przy 0.40: 33%. Pułap ~45% nawet dla najlepszych.
- Obrony bramkarza przy oczekiwanych 26 strzałach: Over 24.5 58.5%; kontekst: CAR (Kochetkov) i DAL (Oettinger) bronią mniej strzałów (silne drużyny), CHI/SJ/VAN oddają więcej strzałów rywalowi (Knight/Nedeljkovic/Lankinen - obrony Over bardziej prawdopodobne), ale bez potwierdzonego bramkarza i bez danych o strzałach -> pewność niska, nie na kupon.
- Potwierdzone: tylko Pickard (MIN) - ale brak linii obron i danych o strzałach TBL.

## Podsumowanie i kandydaci
Brak mocnych typów (p>70%) z dodatnim EV: faworyci (CAR, EDM, DAL, COL) mają kursy 1.22-1.44 zbliżone do lub krótsze niż fair modelu. Najmocniejsze: CAR ML 75%, EDM ML 73%, DAL ML 68% (wszystko z OT, bramkarze niepotw., kursy 1.22/1.29/1.33). Najbardziej wyrównane (brak typu): PIT@LAK, TBL@MIN, DET@COL (z lekkim COL). Totale: wszystkie ok. 50% przy linii 6.5 (EDM ~55%).
To oszacowania probabilistyczne, nie gwarancje; bramkarze sprawdzeni 07.11 przed meczami, skład może się zmienić do rozpoczęcia.
