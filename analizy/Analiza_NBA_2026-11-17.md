# Analiza NBA, noc 17->18.11.2026 (czas PL; data USA 17.11)

Krok 2 flow (skill nba-analyst). Sprawdzenie danych: 17.11.2026 ok. 13:10-14:00 CET.

**Zrodla:** ESPN (injuries z komentarzami z 16.11, scoreboard, standings), BettingPros (klucz ustawiony; linie/kursy DK, FanDuel, konsensus, projekcje; props), Superbet (superbet_event_odds), model `nba_model.py` (SD roznicy 12.5, SD sumy 18.5 - podniesione z powodu wczesnego sezonu, 12-14 meczow na druzyne i niepewnych statusow).

**Ograniczenia danych (wazne):**
- Oficjalny injury report NBA (PDF) zwraca 403, a WebSearch nie zwrocil raportu na 17.11.2026. Statusy pochodza z ESPN (komentarze do 16.11) i flag BettingPros (DTD). Statusy GTD/Questionable moga sie zmienic do ok. 90 min przed meczem; dla zadnego meczu nie ma potwierdzonego skladu.
- Brak szczegolowych statystyk minutowych graczy (drugie niezalezne zrodlo): rynki zawodnika wyceniam tylko orientacyjnie i NIE rekomenduje zadnego typu zawodnika (zob. sekcja props).
- Sezon jest na starcie (12-14 meczow): H2H i forma waza malo, bilans i net rating skonsultowane z rynkiem.

**Back-to-back / dzien wolny:** tylko MIN i POR graja drugi dzien z rzedu (16.11 POR @ MIN 98:106, ten sam parkiet). Pozostali: NYK i TOR graly 15.11 (TOR 108:112 NYK), SAS, UTA, LAC, CHA 15.11, LAL 15.11 - zadnych innych b2b. Dla DET nie ustalono daty ostatniego meczu (brak danych).

## Tabela zbiorcza (p = moje, po ewentualnym sciagnieciu do rynku; kursy Superbet z `superbet_event_odds` 17.11)

| Mecz | Rynek | p | fair | Superbet | EV Superbet | Pewnosc |
|---|---|---|---|---|---|---|
| NYK @ TOR | NYK wygra (z dogrywka) | 59% | 1.69 | 1.67 | -1.5% | srednia |
| NYK @ TOR | NYK +2.5 | 65% | 1.54 | 1.53 | -0.5% | srednia |
| NYK @ TOR | NYK +4.5 | 71% | 1.41 | 1.40 | -0.6% | srednia |
| NYK @ TOR | NYK -2.5 | 50% | 2.00 | 1.82 | -9% | niska |
| NYK @ TOR | total 217.5 | 50/50 | 2.00 | O 1.92 / U 1.87 | brak przewagi | niska |
| POR @ MIN | **Under 227.5** | 54.5% | 1.83 | 1.95 | **+6.3%** | niska-srednia |
| POR @ MIN | Under 226.5 | 53% | 1.89 | 2.02 | +7.1% | niska-srednia |
| POR @ MIN | Under 228.5 | 56% | 1.79 | 1.87 | +4.7% | niska-srednia |
| POR @ MIN | MIN wygra | 55% | 1.82 | 1.77 | -2.6% | niska |
| DET @ SAS | SAS wygra | 76% | 1.32 | 1.26 | -4.2% | wysoka-srednia |
| DET @ SAS | SAS -3.5 / -5.5 / -7.5 | 68% / 63% / 56% | 1.46 / 1.60 / 1.77 | nie pobrano | n/d | srednia |
| DET @ SAS | SAS -9.5, total 222.5 | 50/50 | 2.00 | spread DK -107 | brak przewagi | niska |
| UTA @ LAC | LAC wygra | 69.5% | 1.44 | 1.39 | -3.4% | srednia |
| UTA @ LAC | LAC -3.5 | 61% | 1.64 | nie pobrano | n/d | srednia |
| UTA @ LAC | LAC -6.5, total 225.5 | 51% / 50% | 1.96 / 2.00 | spread DK -107 | brak przewagi | niska |
| CHA @ LAL | LAL wygra | 74% | 1.35 | 1.31 | -3.1% | srednia |
| CHA @ LAL | LAL -3.5 / -5.5 | 66% / 61% | 1.52 / 1.64 | nie pobrano | n/d | srednia |
| CHA @ LAL | LAL -7.5 | 53% | 1.89 | DK -8.5 -103, FD -7.5 -114 | brak przewagi | niska |

**Najlepszy rynek nocy:** Under totalu w POR @ MIN (jedyny typ z dodatnim EV na Superbet, bo linia Superbet ok. 228 jest o 1-2 pkt wyzej niz konsensus USA 226.5-227.5; plus b2b obu druzyn). To jedyna przewaga; zapas EV jest niewielki, pewnosc niska-srednia.

Reszta nocy: ceny faworytow (SAS, LAC, LAL, NYK) sa blisko fair, bez przewagi. Mecz NYK @ TOR to prawie "brak mocnego typu" (spread ok. 3).

---

## 1. Toronto Raptors - New York Knicks (wt. 18.11, 01:30 PL; 17.11 USA) - Superbet 15767070
**Dom/wyjazd:** TOR u siebie, NYK na wyjezdzie. Brak b2b (oba graly 15.11, 1 dzien wolny); rewanz po 2 dniach, 15.11 NYK wygral 112:108 w Toronto.

**Typ:** NYK wygra | **p 59%** | **fair 1.69** | **Pewnosc: srednia**

**Rynki dodatkowe**
| Rynek | p | fair | Uwagi |
|---|---|---|---|
| NYK wygra (z dogr.) | 59% | 1.69 | rynek bez marzy 56.5-57.7%; model 60.7% sciagniety do rynku +2 pp |
| TOR wygra | 41% | 2.44 | |
| NYK +2.5 / +4.5 | 65% / 71% | 1.54 / 1.41 | Superbet 1.53 / 1.40: brak EV |
| NYK -2.5 / -3.5 | 50% / 46% | 2.00 / 2.17 | rynek: -2.5 DK, -3.5 FD |
| Total 216.5 / 217.5 / 218.5 | O 52 / 50 / 48% | | BettingPros proj 218.6; DK/FD 216.5 |
| Total druzyn | TOR 107.3, NYK 110.2 | | linie total druzyny nie pobrane, brak rekomendacji |

**Statystyki druzyn (ESPN standings 17.11):** NYK 7-6, srednio 109.9-104.0 (+5.9), ostatnie 10: 7-3, na wyjezdzie 3-3. TOR 5-8, 113.8-112.8 (+1.0), seria L4, ostatnie 10: 3-7, dom 2-4. Roznica net 4.9 pkt na korzysc NYK, minus przewaga parkietu ok. 2.5 daje spodziewane NYK ok. +2.9.
**H2H:** 15.11 NYK 112:108 w Toronto (Bittle out). Waga niska.
**Informacje medialne:** TOR: Kawhi Leonard out (kolano, powrot ok. 23.11), Nate Bittle out (stopa); Quickley, Murray-Boyles, Poeltl flagowani DTD w BettingPros (brak potwierdzenia ESPN; ESPN ich nie wymienia na liscie kontuzji). NYK: ESPN nie ma NYK na liscie kontuzji, Josh Hart DTD wg BettingPros. Do potwierdzenia po injury report 17.11 wieczorem.
**Oczekiwane punkty:** TOR 107.3 - NYK 110.2 (spread NYK -2.9, total 217.5).
**Ryzyka:** wlasnie srodkowa niepewnosc statusow DTD obu druzyn; seria L4 TOR (nie obnizam NYK; kryzys dotyczy tylko underdoga, i tak jest w cenie); wyrownany mecz.
**Rynek:** Superbet ML NYK 1.67 / TOR 2.17, total 217.5 (1.92 / 1.87), handicap NYK -2.5 1.82. Rynek ok. fair, brak przewagi.

## 2. Minnesota Timberwolves - Portland Trail Blazers (wt. 18.11, 02:00 PL; 17.11 USA) - Superbet 15767089
**Dom/wyjazd:** MIN u siebie, POR na wyjezdzie. **Back-to-back dla OBU druzyn** (16.11 ten sam rywal, ten sam parkiet, MIN 106:98).

**Typ:** Under 227.5 punktow | **p 54.5%** | **fair 1.83** | **Pewnosc: niska-srednia**

**Rynki dodatkowe**
| Rynek | p | fair | Superbet |
|---|---|---|---|
| Under 226.5 / 227.5 / 228.5 / 229.5 | 53 / 54.5 / 56 / 58% | 1.89 / 1.83 / 1.79 / 1.72 | 2.02 / 1.95 / 1.87 / 1.80 (EV +7.1 / +6.3 / +4.7 / +4.4%) |
| MIN wygra | 55% | 1.82 | 1.77 (EV -2.6%) |
| POR wygra | 45% | 2.22 | 2.02 (EV -9%) |
| MIN -1.5 / -2.5 | 52% / 50% | 1.92 / 2.00 | rynek -2.5 |
| Total druzyn | MIN 113.5, POR 111.0 | | brak linii, brak rekomendacji |

**Statystyki druzyn:** MIN 10-4, 117.4-106.1 (+11.3), dom 6-2, ostatnie 10: 7-3 (bez Edwardsa od 29.10). POR 9-4 (ESPN: 9-4), 117.9-111.4 (+6.5), wyjazd 6-2, ostatnie 10: 6-4 (bez Moranta od 7.11). Wczoraj lacznie tylko 204 pkt.
**H2H:** 16.11 MIN 106:98.
**Informacje medialne:** MIN: Anthony Edwards out (kolano, do ok. 21.12), DiVincenzo out, Jaylen Clark out; Jonathan Kuminga DTD (bark, zjechal w 4. kwarcie wczoraj; ESPN: powrot 17.11); Shannon Jr. DTD (BettingPros). POR: Morant out (hamstring), Sharpe out, Krejci out, Youngblood out. Drugi mecz w 24 h z tym samym rywalem: obnizam total o ok. 2.5 pkt wzgledem srednich druzyn (b2b obu druzyn).
**Oczekiwane punkty:** MIN 113.5 - POR 111.0 (spread MIN -2.5, total 224.5; konsensus USA 226.5-227.5, BettingPros proj 224.7).
**Ryzyka:** Under sciagniety do rynku +3 pp (regula ze skilla); Kuminga i Shannon moga zagrac wiecej (Over); rewanz na tym samym parkiecie moze miec wyzsze tempo; wczoraj total 204 (zachecajaca anegdota, nie podstawa). Pewnosc niska-srednia, bo przewaga wynika z roznicy linii Superbet vs USA i b2b.
**Rynek:** Superbet total glowny ok. 228 (O 228.5 1.92 / U 228.5 1.87), ML MIN 1.77 / POR 2.02.

## 3. Detroit Pistons - San Antonio Spurs (wt. 18.11, 02:00 PL; 17.11 USA) - Superbet 15767090
**Dom/wyjazd:** SAS u siebie, DET na wyjezdzie. Brak b2b (SAS ostatni mecz 15.11 w Utah, 110:102; DET nieznany).

**Typ:** SAS wygra | **p 76%** | **fair 1.32** | **Pewnosc: wysoka-srednia** (nie jest kandydatem na kupon: fair blisko 1.15, Superbet 1.26 przy EV -4%)

**Rynki dodatkowe**
| Rynek | p | fair | Uwagi |
|---|---|---|---|
| SAS wygra | 76% | 1.32 | rynek bez marzy 74.6-76.5% |
| SAS -3.5 / -5.5 / -7.5 | 68% / 63% / 56% | 1.46 / 1.60 / 1.77 | Superbet nie pobrany |
| SAS -9.5 | 50% | 2.00 | DK/FD -9.5 (-105/-108); BettingPros proj -6.9 |
| DET +9.5 | 50% | 2.00 | |
| Total 221.5 / 222.5 | O 52 / 50% | | DK 222.5, FD 221.5, proj BettingPros 225.3 |
| Total druzyn | SAS 116.0, DET 106.5 | | |

**Statystyki druzyn:** SAS 12-2, seria W12, 118.8-105.9 (+12.9), 10-0 w ostatnich 10, dom 5-2. DET 8-4, 115.7-110.3 (+5.4), ostatnie 10: 6-4, wyjazd 5-2.
**H2H:** brak istotnych danych w tym sezonie. Waga niska.
**Informacje medialne (ESPN, 16.11):** DET: Jalen Duren out (hamstring, ok. 24.11), Duncan Robinson out, Taurean Prince out, Ronald Holland II out, Isaiah Joe doubtful; Ausar Thompson DTD (BettingPros). To piec zawodnikow rotacji, najpewniej wiekszosc juz w linii (spread -9.5). SAS: Tobias Harris out (lydka), Quaintance out; Wembanyama nie jest na liscie kontuzji i ma linie props (28 pkt), wiec zakladamy gre.
**Oczekiwane punkty:** SAS 116.0 - DET 106.5 (spread SAS -9.5, total 222.5).
**Ryzyka:** blowout skraca minuty gwiazd (Wembanyama, Cunningham); status Wembanyamy nie potwierdzony oficjalnym raportem; SAS gra 12 meczow z rzedu wygrane, rynek juz to wycenia.
**Rynek:** Superbet ML SAS 1.26 / DET 3.70. Brak EV.

## 4. Utah Jazz - LA Clippers (wt. 18.11, 04:30 PL; 17.11 USA) - Superbet 15767191
**Dom/wyjazd:** LAC u siebie, UTA na wyjezdzie. Brak b2b (oba graly 15.11).

**Typ:** LAC wygra | **p 69.5%** | **fair 1.44** | **Pewnosc: srednia**

**Rynki dodatkowe**
| Rynek | p | fair | Uwagi |
|---|---|---|---|
| LAC wygra | 69.5% | 1.44 | rynek bez marzy 67.5%; model 71.2%; Superbet 1.39 (EV -3.4%) |
| UTA wygra | 30.5% | 3.28 | Superbet 2.90 |
| LAC -3.5 | 61% | 1.64 | Superbet nie pobrany |
| LAC -6.5 | 51% | 1.96 | DK/FD -6.5 (-107/-106) |
| Total 224.5 / 225.5 / 226.5 | O 52 / 50 / 48% | | BettingPros proj 222.3 (lekko Under) |
| Total druzyn | LAC 116.5, UTA 109.0 | | |

**Statystyki druzyn:** UTA 1-13, seria L12, 107.1-118.0 (-10.9), 0-10 w ostatnich 10, wyjazd 0-6. LAC 4-8 wg ESPN (wins 4, losses 8), 112.3-116.5 (-4.2), dom 4-3, wyjazd 0-5, seria W2.
**H2H:** brak istotnych danych.
**Informacje medialne (ESPN):** UTA: Markkanen out (zlamanie reki, do 4.01), Jaren Jackson Jr. out (MCL), Nurkic out, Jaxson Hayes out; LAC: Brandon Ingram out (Achilles, do ok. 19.11), Beal out, Niederhauser out, Jordan Miller out; Hachimura i Derrick Jones Jr. DTD (BettingPros). Kryzys dotyczy tylko underdoga (UTA): liczby sa juz skorygowane o brak graczy.
**Oczekiwane punkty:** LAC 116.5 - UTA 109.0 (spread LAC -7.5, total 225.5).
**Ryzyka:** LAC jest 0-5 na wyjezdzie i slabo na papierze (net -4.2), ale u siebie 4-3; Jazz zle bronia (118 pkt/mecz), co podbija total; status Hachimury/Jonesa.
**Rynek:** Superbet ML LAC 1.39 / UTA 2.90. Brak EV.

## 5. Charlotte Hornets - Los Angeles Lakers (wt. 18.11, 05:00 PL; 17.11 USA) - Superbet 15767174
**Dom/wyjazd:** LAL u siebie, CHA na wyjezdzie. Brak b2b (oba graly 15.11, CHA w LA).

**Typ:** LAL wygra | **p 74%** | **fair 1.35** | **Pewnosc: srednia**

**Rynki dodatkowe**
| Rynek | p | fair | Uwagi |
|---|---|---|---|
| LAL wygra | 74% | 1.35 | rynek bez marzy 71.6-73.4%; Superbet 1.31 (EV -3.1%) |
| CHA wygra | 26% | 3.85 | Superbet 3.30 |
| LAL -3.5 / -5.5 | 66% / 61% | 1.52 / 1.64 | Superbet nie pobrany |
| LAL -7.5 / -8.5 | 53% / 50% | 1.89 / 2.00 | DK -8.5 (-103), FD -7.5 (-114) |
| Total 219.5 / 220.5 | O 51 / 49% | | BettingPros proj 221.7 |
| Total druzyn | LAL 114.5, CHA 105.5 | | |

**Statystyki druzyn:** LAL 12-2, seria W8, 122.8-114.9 (+7.9), 9-1 w ostatnich 10, dom 5-1. CHA 4-9, seria L2, 99.1-109.8 (-10.7), 2-8 w ostatnich 10, wyjazd 1-5.
**H2H:** brak istotnych danych w tym sezonie.
**Informacje medialne (ESPN, 16.11):** LAL: Austin Reaves out (piety), Walker Kessler out; Doncic nie jest na liscie kontuzji ESPN (BettingPros flaguje DTD, linia props 36.5 pkt wskazuje, ze zagra). CHA: Kon Knueppel out (hamstring, do ok. 12.12), Dennis Schroder out (do ok. 25.11); Brandon Miller gra (prop 18.5 pkt), Moussa Diabate DTD. Zmniejszam p LAL o ok. 2 pp wzgledem modelu (76%) przez brak Reavesa/Kesslera i ryzyko z Doncicem.
**Oczekiwane punkty:** LAL 114.5 - CHA 105.5 (spread LAL -9.0, total 220.0).
**Ryzyka:** status Doncica (jesli nie zagra, margines spada o 5-7 pkt i p LAL do ok. 62%); blowout skraca minuty gwiazd; slaba ofensywa CHA (99 pkt) ciagnie total w dol.
**Rynek:** Superbet ML LAL 1.31 / CHA 3.30. Brak EV.

---

## Rynki zawodnika (punkty, zbiorki, asysty, trojki, PRA)
Linie Superbet pokrywaja sie z konsensusem BettingPros (rozne o 0-1 pkt), a projekcje BettingPros (zaokraglone) leza w granicach 0.5-1 od linii. Nie mam drugiego niezaleznego zrodla srednich minutowych i potwierdzonych statusow (oficjalny raport NBA niedostepny), wiec zgodnie ze skillem **nie rekomenduje zadnego typu zawodnika** ("brak podstaw", pewnosc niska). Linie glownych graczy dla bet-slip-buildera:
- NYK-TOR: Brunson 25.5 pkt / 35.5 PRA; Towns 21.5 pkt / 37.5 PRA; Barnes 21.5 pkt; Barrett 19.5 pkt; Anunoby 16.5; Quickley 15.5 (DTD wg BettingPros).
- Konsensus BettingPros: Doncic 36.5 pkt, Wembanyama 27.5 pkt / 12.5 zb / 43.5 PRA, Cunningham 24.5 pkt / 8.5 ast, Avdija 23.5 pkt, Lillard 20.5 pkt, LaMelo Ball 21.5 pkt, Garland 22.5 pkt, Brandon Miller 18.5 pkt, Keyonte George 21.5 pkt, Darryn Peterson 20.5 pkt.
- Ryzyko blowoutu: SAS -9.5 i LAL ok. -8 (obnizenie minut gwiazd obu stron), wiec Over zbiorek/punktow gwiazd tych meczow jest ryzykowny.

## Kandydaci na kupon (wejscie dla bet-slip-builder)
| Mecz | Rynek | p | fair | Superbet | Pewnosc | Zaleznosc |
|---|---|---|---|---|---|---|
| POR @ MIN | Under 227.5 (lub 226.5 @2.02) | 54.5% | 1.83 | 1.95 | niska-srednia | Kuminga/Shannon, tempo rewanzu, b2b obu |
| NYK @ TOR | NYK +4.5 | 71% | 1.41 | 1.40 | srednia | statusy DTD TOR (Quickley, Poeltl, Murray-Boyles) |
| DET @ SAS | SAS wygra | 76% | 1.32 | 1.26 | wysoka-srednia | Wembanyama; EV ujemne |
| CHA @ LAL | LAL wygra | 74% | 1.35 | 1.31 | srednia | Doncic; EV ujemne |
| UTA @ LAC | LAC wygra | 69.5% | 1.44 | 1.39 | srednia | Hachimura, Jones Jr.; EV ujemne |

Jedyny typ z EV > 0 wg moich p to Under w POR @ MIN. Typy z fair <= 1.15 pominieto.

Przypomnienie: to oszacowania probabilistyczne, nie gwarancje; statusy graczy (injury report) moga zmienic sie do rozpoczecia meczu.
