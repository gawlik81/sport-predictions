# Analiza piłkarska - reprezentacje UEFA, wtorek 17.11.2026, 20:45 (PL)

Ranga: wszystkie 8 meczów to **6. kolejka (ostatnia) fazy ligowej UEFA Nations League 2026/27** (mecze o punkty i awans/spadek, nie towarzyskie). Tabele wg Wikipedii (stan po 14.11) i wyników z Superbet H2H; błędy statusów na Wikipedii sprawdzone własnym rachunkiem (np. B2: Węgry mogą jeszcze wyprzedzić Irlandię Płn.). Format: zwycięzcy grup B awansują do A; 2. miejsca B grają baraże awansu; ostatnie miejsca B grają baraże utrzymania z 2. miejscami C; w A top 2 do ćwierćfinałów.
Źródła: Superbet MCP (kursy, statystyki, H2H, nieobecni - dane "manual", częściowo niepotwierdzone), Wikipedia (tabele), Sportsmole/Salzburg24/TV4/africasoccer (newsy), własny model Poissona (`poisson.py`) i NB (`markets.py`). BettingPros: nie używany (brak klucza w tej sesji). Składy: wszystkie nadal "przewidywane" lub brak (13:00 PL).

Zasady zastosowane: λ reprezentacji nie poniżej ~0,7; Under 2.5 przy łącznym λ ≤ 2,0 maksymalnie średnia pewność; rynki rożne/kartki oparte tylko na jednym źródle (Superbet, próbka 5 meczów) = niska pewność, bez rekomendacji. Rozbieżności z rynkiem >5 pp skorygowane w stronę rynku lub uzasadnione. Kursy Superbet podane tylko tam, gdzie pobrane.

---

## 1. Walia - Portugalia (UEFA Liga Narodów, grupa A4, 20:45 PL, Cardiff, Superbet 15339582)
**Stawka:** Portugalia 12 pkt, potrzebuje 1 pkt, by wygrać grupę (przy porażce i wygranej Danii Dania wyprzedza ją bilansem H2H 6:5 w golach). Walia 3 pkt, ostatnia, walczy o uniknięcie spadku/baraży. Portugalia 14.11 przegrała 1-4 z Danią.
**Model:** λ Walia 0,90 / Portugalia 2,00 (rynek ≈ 0,85/2,0).
| Rynek | p | fair | pewność | uwagi / kurs Superbet |
|---|---|---|---|---|
| Portugalia wygra | 63,0% | 1.59 | średnia | rynek 1.46 (no-vig 64,6%) |
| Podwójna szansa X2 | 83,9% | 1.19 | średnia | rynek 1.13 |
| Over 1.5 gola | 78,5% | 1.27 | średnia | rynek 1.15 |
| Over 2.5 gola | 55,4% | 1.80 | niska | rynek 1.48 (63,9%), mój p niżej o ~8 pp - brak Dias/Palhinha/B. Silva i Ronaldo na emeryturze ścina atak, ale osłabia też obronę |
| Under 3.5 | 67,0% | 1.49 | średnia | rynek 1.66 (nie ma przewagi) |
| BTTS tak | 51,3% | 1.95 | niska | |
| Rożne (średnia 9,2) O8.5 / O9.5 | 55% / 44% | 1.81 / 2.30 | niska | tylko 1 źródło; Portugalia 6,2 rożnych/mecz vs Walia 2,8 |
| Kartki (średnia 4,6; sędzia Jablonski, DE, nie ma jego statystyk) O3.5 / O4.5 | 64% / 47% | 1.57 / 2.13 | niska | brak danych sędziego |

**Statystyki:** Walia 0,6 gola/mecz (xG 0,7), traci 1,6; w oknie: 0-1 z Portugalią, 0-2 i 0-1 z Danią, 2-1 z Norwegią, 1-3 z Norwegią. Portugalia 2,0 gola (xG 1,6), traci 1,6; w serii 4-2 i 1-4 z Danią, 2-1/2-1 z Norwegią.
**H2H:** Portugalia - Walia 1-0 (24.09.2026, gol Joao Felixa); poprzednio 2-0 w 2016.
**Informacje medialne:** Portugalia bez Rubena Diasa i Palhinhy (zawieszenie - limit kartek Ligi Narodów), Bernardo Silva wykluczony po badaniach; Ronaldo ogłosił koniec reprezentacji i nie ma go w kadrze (africasoccer, dailysports); wymieniany też Conceicao (zawieszony - tylko jedno źródło). Walia bez Ampadu (zawieszenie, jedno źródło), Neco Williams (uraz), wg 3addedminutes także Wilson i Rodon (niepotwierdzone, data artykułu niejasna).
**Ryzyka:** Portugalia potrzebuje tylko punktu, więc możliwe niskie tempo po objęciu prowadzenia (Under); porażka Portugalii 1-4 z Danią pokazuje obronną niestabilność bez Diasa; Walia u siebie z Bellamym motywowana.
**Najlepszy rynek meczu:** Portugalia wygra / X2 (ale fair 1.19 - granica 1.15-1.20), Over 1.5 (fair 1.27). **Pewność: średnia.**

---

## 2. Dania - Norwegia (UEFA Liga Narodów, grupa A4, 20:45 PL, Kopenhaga, Superbet 15339583)
**Stawka:** decydujący o 2. miejscu (ćwierćfinał). Dania 9 pkt, Norwegia 6 pkt. Dania potrzebuje remisu (10 pkt); Norwegia musi wygrać (9 pkt i wyższy bilans H2H po 3-2 u siebie, o ile nie przegra różnicą 3+ bramek). Sędzia: Meler (TUR).
**Model:** λ Dania 1,60 / Norwegia 1,55 (rynek total ≈ 3,1; stawka i H2H 3-2, 4-2 i 4-1 w pobliskich meczach wskazują wysokie tempo).
| Rynek | p | fair | pewność | uwagi / kurs |
|---|---|---|---|---|
| 1X2 | 39,3% / 23,6% / 37,1% | 2.55 / 4.23 / 2.69 | niska | rynek 2.57 / 3.90 / 2.45; brak mocnego typu na wynik |
| Dania lub Norwegia (12) | 76,4% | 1.31 | średnia | rynek 1.25 |
| Over 1.5 gola | 82,2% | 1.22 | średnia-wysoka | rynek 1.13 |
| Over 2.5 gola | 61,0% | 1.64 | średnia | rynek 1.45 (65,4% no-vig) |
| Under 3.5 | 61,4% | 1.63 | średnia | rynek 1.75 |
| Over 3.5 | 38,6% | 2.59 | niska | rynek 2.07 |
| BTTS tak | 62,9% | 1.59 | średnia | oba atakują, oba tracą ≥1,6 |
| Rożne (śr. 9,6) O8.5 / O9.5 / O10.5 | 60% / 48% / 37% | 1.67 / 2.07 / 2.69 | niska | 1 źródło |
| Kartki (śr. 3,6; Meler - turecki sędzia, przeciętnie surowy, brak danych) O2.5 / O3.5 | 66% / 47% | 1.53 / 2.15 | niska | |

**Statystyki:** Dania 2,2 gola/mecz (xG 1,5), traci 1,6; 4-1 z Portugalią (14.11), 2-4 u siebie z nią, 1-0 i 2-0 z Walią, 2-3 z Norwegią. Norwegia 1,8 gola (xG 1,6), traci 1,8; 3-1 z Walią (14.11), 1-2 z Walią, 1-2 i 1-2 z Portugalią, 3-2 z Danią.
**H2H:** Norwegia - Dania 3-2 (24.09.2026, dublet Haalanda; 1 czerwona kartka); Dania - Norwegia 3-1 (06.2024).
**Informacje medialne:** brak listopadowych składów i listy absencji (Superbet bez danych). Przewidywany: Dania z Hojlundem i Isaksenem (Sportsmole), Norwegia z Haalandem i Odegaardem (wrześniowe przewidywania - niepotwierdzone na listopad). W wrześniu Norwegia grała bez Sørlotha (uraz; status listopadowy nieznany).
**Ryzyka:** Dania zadowolona z remisu może grać ostrożniej w końcówce (Under); Norwegia musi atakować (wyższe tempo, kontry Danii); rynek strzałów Haalanda/Odegaarda - brak potwierdzonego składu.
**Najlepszy rynek meczu:** Over 1.5 (fair 1.22) / BTTS tak (1.59) / Over 2.5 (1.64). **Pewność: średnia.**

---

## 3. Ukraina - Gruzja (UEFA Liga Narodów, grupa B2, 20:45 PL, Koszyce (SVK), Superbet 15339602)
**Stawka:** Ukraina 4 pkt (nie awansuje), Gruzja 2 pkt (ostatnia). Przy wygranej Gruzji (5 pkt) to Ukraina zostaje ostatnia i gra baraż utrzymania; remis/wygrana Ukrainy zostawia Gruzję ostatnią. Sędzia: Matosa. Neutralny teren (Koszyce).
**Model:** λ Ukraina 1,20 / Gruzja 0,80.
| Rynek | p | fair | pewność | uwagi / kurs |
|---|---|---|---|---|
| Ukraina wygra | 45,4% | 2.20 | niska | rynek 2.12 (44,1%) |
| Ukraina lub remis (1X) | 75,4% | 1.33 | średnia | rynek 1.28 |
| Under 2.5 | 64% | 1.56 | średnia (max przy λ≤2) | rynek 1.62 (58,7% no-vig); mój model dawał 67,7%, skorygowałem w stronę rynku |
| Under 3.5 | 85,7% | 1.17 | średnia | granica 1.15-1.20; rynek 1.22 |
| BTTS nie | 61,5% | 1.63 | średnia | |
| Over 1.5 | 59,4% | 1.68 | niska | rynek 1.42 - mój p niżej (63% rynek); Gruzja 0 goli w 5 meczach |
| Rożne (śr. 8,6) O7.5 / O8.5 | 60% / 48% | 1.65 / 2.08 | niska | |
| Kartki (śr. 4,2) O3.5 / O4.5 | 57% / 40% | 1.75 / 2.48 | niska | Ukraina 3,0 kartki/mecz |

**Statystyki:** Ukraina 0,4 gola/mecz w bieżącej serii (xG 0,8), traci 1,2: 0-1 z Węgrami, 0-3 z Irlandią Płn. (dom), 1-2 z Węgrami, 0-0 z Gruzją, 0-1 z Irlandią Płn. (14.11). Gruzja 0 goli w 5 meczach (xG 0,8), traci 0,8: 0-1, 0-0, 0-1, 0-2 (z Węgrami 14.11), 0-0.
**H2H:** Gruzja - Ukraina 0-0 (28.09.2026); wcześniej 1-1 i 1-0 (2024).
**Informacje medialne:** Gruzja bez Tsitaishviliego (zawieszenie, Superbet), Ukraina bez zgłoszonych nieobecnych; trener Ukrainy Maldera (Superbet).
**Ryzyka:** bardzo niska skuteczność obu; w przypadku wcześniejszego gola Gruzja (potrzebuje wygranej) otworzy grę; wynik Under/BTTS nie wymaga zwycięzcy.
**Najlepszy rynek meczu:** Under 3.5 (1.17, granica) / BTTS nie (1.63) / Under 2.5 (1.56). **Pewność: niska-średnia.**

---

## 4. Węgry - Irlandia Północna (UEFA Liga Narodów, grupa B2, 20:45 PL, Budapeszt, Superbet 15339603)
**Stawka:** decydujący o 1. miejscu (awans do A): Irlandia Płn. 11 pkt, Węgry 10 pkt. Węgry muszą wygrać; NI wystarczy remis. (Wikipedia oznacza NI jako awansującą - błąd, Węgry z wygraną mają 13 pkt.) Sędzia: Guida (ITA).
**Model:** λ Węgry 1,20 / Irlandia Płn. 0,75.
| Rynek | p | fair | pewność | uwagi / kurs |
|---|---|---|---|---|
| Węgry wygrają | 46,7% | 2.14 | niska | rynek 1.95 (48,0%) |
| Węgry lub remis (1X) | 76,9% | 1.30 | średnia | rynek 1.21 |
| Under 2.5 | 65% | 1.54 | średnia | rynek 1.60 (59,2% no-vig); model 69%, skorygowane w stronę rynku |
| Under 3.5 | 86,6% | 1.15 | średnia | granica, rynek 1.21 |
| BTTS nie | 63% | 1.59 | średnia | NI nie straciła gola w 5 meczach |
| Over 1.5 | 58,0% | 1.72 | niska | rynek 1.43 |
| Rożne (śr. 8,4) O7.5 / O8.5 | 58% / 46% | 1.72 / 2.19 | niska | |
| Kartki (śr. 4,0) O3.5 / O4.5 | 54% / 37% | 1.86 / 2.70 | niska | Węgry 2,6 kartki/mecz |

**Statystyki:** Węgry 1,0 gola/mecz (xG 1,6), tracą 0,4: 0-0 NI (wyjazd), 1-0 Gruzja, 2-1 Ukraina (wyjazd), 0-1 Ukraina (dom), 2-0 Gruzja (14.11). NI 1,0 gola (xG 1,4), 0 straconych w 5 meczach (3 W, 2 R): 1-0 z Ukrainą (14.11, gol Devlina z dystansu), 3-0 z Ukrainą, 0-0 z Węgrami, wygrane i remis z Gruzją.
**H2H:** NI - Węgry 0-0 (28.09.2026); wcześniej NI 0-1 Węgry (03.2022).
**Informacje medialne:** Węgry bez Orbana i Vitalisa (zawieszenia, Superbet), Szoboszlai wg Superbet kontuzjowany ("manual"), ale Sportsmole i inne zapowiedzi opisują go jako zdrowego - **niepotwierdzone**; przewidywany skład Superbet bez niego; Varga wymieniany jako wątpliwy. NI bez zgłoszonych absencji (5-4-1). Uwzględniono -5% do λ Węgier za nieobecności.
**Ryzyka:** Węgry potrzebują wygranej i będą atakować (mogą stracić w kontrze); NI broni 5-4-1 i ma 0 straconych; rywalizacja o awans zwiększa kartki.
**Najlepszy rynek meczu:** Under 3.5 (fair 1.15, granica - pomijać w rankingu) / BTTS nie (1.59) / Under 2.5 (1.54) / Węgry lub remis (1.30). **Pewność: średnia.**

---

## 5. Irlandia - Kosowo (UEFA Liga Narodów, grupa B3, 20:45 PL, Dublin, Superbet 15339606)
**Stawka:** Irlandia 5 pkt, Kosowo 6 pkt (2. miejsce = baraż awansu). Irlandia z wygraną (8 pkt) wyprzedza Kosowo; Kosowo z punktem ma co najmniej 7. Ostatnie miejsce: Izrael (3 pkt) może wyprzedzić Irlandię, jeśli ta przegra, a Izrael wygra z Austrią. Sędzia: Malcevs (LAT).
**Model:** λ Irlandia 1,20 / Kosowo 0,85.
| Rynek | p | fair | pewność | uwagi / kurs |
|---|---|---|---|---|
| Irlandia wygra | 44,1% | 2.27 | niska | rynek 2.10 (44,5%) |
| Irlandia lub remis (1X) | 73,9% | 1.35 | średnia | |
| Under 2.5 | 63% | 1.59 | średnia | rynek 1.56 (60,6% no-vig); model 66,3% |
| Under 3.5 | 84,8% | 1.18 | średnia | granica; rynek 1.20 |
| BTTS nie | 60,0% | 1.67 | średnia | |
| Over 1.5 | 60,7% | 1.65 | niska | rynek 1.45 |
| Rożne (śr. 8,0) O7.5 / O8.5 | 53% / 41% | 1.88 / 2.46 | niska | |
| Kartki (śr. 3,2; Malcevs) O2.5 / O3.5 | 58% / 39% | 1.72 / 2.57 | niska | Irlandia 1,8 kartki/mecz, Kosowo 1,2 |

**Statystyki:** Irlandia 1,2 gola (xG 1,3), traci 1,0: 0-1 z Kosowem, 3-0 z Izraelem, 2-2 z Austrią, 1-1 z Izraelem, 0-1 z Austrią (14.11). Kosowo 0,6 gola (xG 1,4), traci 0,8: 1-0 z Irlandią, 3-1 i 1-1 z Austrią, 0-0 z Izraelem x2 (w tym 14.11, czerwona kartka).
**H2H:** Kosowo - Irlandia 1-0 (24.09.2026).
**Informacje medialne:** Kosowo bez Hodzy (zawieszenie) i Dellovy (uraz, Superbet "manual"); Irlandia bez zgłoszonych absencji; trener Irlandii Hallgrimsson.
**Ryzyka:** Kosowo rzadko traci (4 w 5 meczach), ale też mało strzela; Irlandia zmotywowana (2. miejsce) może wygrać 1-0.
**Najlepszy rynek meczu:** Under 3.5 (1.18, granica) / BTTS nie (1.67) / Under 2.5 (1.59). **Pewność: niska-średnia.**

---

## 6. Izrael - Austria (UEFA Liga Narodów, grupa B3, 20:45 PL, Debreczyn (HUN), Superbet 15339607)
**Stawka:** Austria 11 pkt - **awans do A już zapewniony** rachunkiem (Kosowo max 9), więc ryzyko rotacji (Rangnick po awansie wcześniej zmienił 6 zawodników; Sportsmole: możliwa rotacja). Izrael 3 pkt (ostatni): potrzebuje wygranej i porażki Irlandii, by uniknąć ostatniego miejsca. Sędzia: Massa (ITA). Mecz na neutralnym terenie.
**Model:** λ Izrael 0,85 / Austria 1,70 (rotacja -10% w λ Austrii; rynek total ≈ 2,9).
| Rynek | p | fair | pewność | uwagi / kurs |
|---|---|---|---|---|
| Austria wygra | 55% | 1.82 | średnia | rynek 1.85 (50,5% no-vig), brak przewagi |
| Austria lub remis (X2) | 79,0% | 1.27 | średnia | |
| Over 1.5 | 72,3% | 1.38 | średnia | rynek 1.17 (ok. 82%) - mój p niższy o ~10 pp (rotacja, Izrael 0,4 gola/mecz) |
| Over 2.5 | 46,9% | 2.13 | niska | rynek 1.56 (60,8%); rozbieżność ~14 pp, rynek może mieć rację (Austria 3,0 gola/mecz w tej fazie) |
| Under 3.5 | 74,7% | 1.34 | średnia | |
| BTTS tak | 46,8% | 2.14 | niska | |
| Rożne (śr. 8,8) O7.5 / O8.5 | 63% / 51% | 1.59 / 1.98 | niska | Austria 5,2 rożnych/mecz |
| Kartki (śr. 3,6) O2.5 / O3.5 | 65% / 47% | 1.53 / 2.15 | niska | Izrael 2,4, Austria 1,8 |

**Statystyki:** Austria 2,0 gola/mecz (xG 1,7), traci 1,0: 3-1 z Izraelem, 3-1 z Kosowem, 2-2 z Irlandią, 1-1 z Kosowem, 1-0 z Irlandią (14.11). Izrael 0,4 gola (xG 0,5), traci 1,4: 1-3, 0-3 z Irlandią, 1-1, 0-0 (x2).
**H2H:** Austria - Izrael 3-1 (24.09.2026); ostatnie 5 H2H wysokie (4-2, 5-2, 3-1, 4-2).
**Informacje medialne:** Izrael bez Raza Shlomo (zawieszenie); Austria bez zgłoszonych nieobecnych, skład niepotwierdzony; wątek rotacji.
**Ryzyka:** rotacja i brak motywacji Austrii; Izrael motywowany; remis lub niskie gole.
**Najlepszy rynek meczu:** Austria lub remis (1.27) / Over 1.5 (1.38). **Pewność: niska-średnia (rotacja).**

---

## 7. Polska - Szwecja (UEFA Liga Narodów, grupa B4, 20:45 PL, Wrocław, Superbet 15339610)
**Stawka:** Szwecja 13 pkt - **awans do A już zapewniony** (Bośnia max 11), czyli mecz bez stawki dla gości (ryzyko rotacji, trzeci mecz w oknie po 3-2 z Bośnią 14.11). Polska 4 pkt: remis/wygrana walczy o uniknięcie ostatniego miejsca (Rumunia 3 pkt; Rumunia z wygraną 6 pkt, więc Polsce potrzebna wygrana (7), by pewnie uciec). Sędzia: Zwayer (DE).
**Model:** λ Polska 1,50 / Szwecja 1,30 (rynek total ≈ 2,8).
| Rynek | p | fair | pewność | uwagi / kurs |
|---|---|---|---|---|
| Polska wygra | 42,0% | 2.38 | niska | rynek 2.15 (44,3%) |
| Polska lub remis (1X) | 67,1% | 1.49 | niska-średnia | |
| Over 1.5 | 76,9% | 1.30 | średnia | rynek 1.16 |
| Over 2.5 | 53,1% | 1.88 | niska | rynek 1.54 (61,6%); mój p niższy o ~8 pp |
| Under 3.5 | 69,2% | 1.45 | średnia | rynek 1.61 |
| BTTS tak | 56,5% | 1.77 | niska-średnia | |
| Rożne (śr. 9,0) O8.5 / O9.5 | 53% / 41% | 1.89 / 2.43 | niska | Polska 5,8 rożnych/mecz |
| Kartki (śr. 3,4; Zwayer) O2.5 / O3.5 | 62% / 43% | 1.61 / 2.34 | niska | Polska 2,6 kartki, Szwecja 0,8 |

**Statystyki:** Polska 1,6 gola (xG 1,7), traci 1,2: 0-0 z Bośnią, 1-3 ze Szwecją, 6-0 z Rumunią, 0-1 z Bośnią, 1-2 z Rumunią (14.11, Bukareszt). Szwecja 2,0 gola (xG 1,8), traci 1,0: 2-1 Rumunia, 3-1 Polska, 1-1 Bośnia, 1-0 Rumunia, 3-2 Bośnia (14.11).
**H2H:** Szwecja - Polska 3-1 (28.09.2026), 3-2 (03.2026, baraż MŚ), Polska 2-0 (03.2022), Szwecja 3-2 (2021). Szwecja wygrała 8 z 10 historycznych.
**Informacje medialne:** Polska bez Kiwiora (zawieszenie, Superbet) i Casha (kontuzja, "manual"; media polskie potwierdzają jego absencję); Szwecja bez Holma (uraz), w kadrze Isak, Gyokeres, Kulusevski (wraca po 2 latach) i Lindelof (TV4); skład niepotwierdzony.
**Ryzyka:** wygrana Polski jest wrażliwa na rotację Szwecji (jeśli duża, podnoszę p Polski o ok. 3-4 pp - nie uwzględniono, brak potwierdzenia); Szwecja 3 wygrane z 3 meczów z Polską 2026; brak Kiwiora osłabia obronę.
**Najlepszy rynek meczu:** Over 1.5 (1.30) / Polska lub remis (1.49). **Pewność: niska-średnia.**

---

## 8. Bośnia i Hercegowina - Rumunia (UEFA Liga Narodów, grupa B4, 20:45 PL, Zenica, Superbet 15339611)
**Stawka:** Bośnia 8 pkt - 2. miejsce zapewnione rachunkiem (Polska max 7, Szwecja 13), baraż awansu; niewielka motywacja (Tabaković kontuzjowany). Rumunia 3 pkt: potrzebuje wygranej (6 pkt) i niewygranej Polski, by uniknąć ostatniego miejsca (baraż utrzymania) - większa motywacja. Sędzia: Sanchez Martinez (ESP).
**Model:** λ Bośnia 1,50 / Rumunia 1,20 (Rumunia traci 2,8 gola/mecz, ale ma xG 0,7; łączny total ≈ 2,7).
| Rynek | p | fair | pewność | uwagi / kurs |
|---|---|---|---|---|
| Bośnia wygra | 44,1% | 2.27 | niska | rynek 2.17 (43,7%) |
| Bośnia lub remis (1X) | 69,6% | 1.44 | niska-średnia | |
| Over 1.5 | 75,1% | 1.33 | średnia | rynek 1.23 |
| Over 2.5 | 50,6% | 1.98 | niska | rynek 1.73 (54,8%) |
| Under 3.5 | 71,4% | 1.40 | średnia | rynek 1.43 |
| BTTS tak | 54,3% | 1.84 | niska-średnia | Rumunia traci prawie zawsze (14 goli w 5) |
| Rożne (śr. 8,0) O7.5 / O8.5 | 53% / 41% | 1.88 / 2.46 | niska | Bośnia 3,8, Rumunia 2,8 rożnych/mecz |
| Kartki (śr. 4,4; Sanchez Martinez) O3.5 / O4.5 | 60% / 44% | 1.65 / 2.29 | niska | Rumunia 3,4 żółtej kartki/mecz |

**Statystyki:** Bośnia 1,6 gola (xG 1,1), traci 1,2: 0-0 z Polską, 4-2 z Rumunią, 1-1 ze Szwecją, 1-0 z Polską, 2-3 ze Szwecją (14.11). Rumunia 1,0 gola (xG 0,7), traci 2,8: 1-2 ze Szwecją, 2-4 z Bośnią, 0-6 z Polską, 0-1 ze Szwecją, 2-1 z Polską (14.11).
**H2H:** Rumunia - Bośnia 2-4 (28.09.2026); Bośnia 3-1 (11.2025), Rumunia 0-1 (03.2025); Rumunia 4-1 (2022).
**Informacje medialne:** Bośnia bez Tabakovicia (uraz), Rumunia bez Baluty (zawieszenie); trenerzy Barbarez i Hagi (Superbet); składy niepotwierdzone.
**Ryzyka:** motywacja po stronie Rumunii (potrzebuje wygranej), Bośnia po 3-2 ze Szwecją w 3 dni; w przypadku remisu 2-2 itp. wysoki BTTS.
**Najlepszy rynek meczu:** Over 1.5 (1.33) / Under 3.5 (1.40) / Bośnia lub remis (1.44). **Pewność: niska-średnia.**

---

## Podsumowanie - najmocniejsze rynki (p >= 50% lub fair <= 2.0)
| Mecz | Rynek | p | fair | pewność |
|---|---|---|---|---|
| Dania - Norwegia | Over 1.5 | 82,2% | 1.22 | średnia-wysoka |
| Walia - Portugalia | Portugalia wygra | 63,0% | 1.59 | średnia |
| Walia - Portugalia | Over 1.5 | 78,5% | 1.27 | średnia |
| Walia - Portugalia | X2 | 83,9% | 1.19 | średnia (granica 1.15-1.20) |
| Dania - Norwegia | BTTS tak | 62,9% | 1.59 | średnia |
| Dania - Norwegia | Over 2.5 | 61,0% | 1.64 | średnia |
| Izrael - Austria | Austria lub remis (X2) | 79,0% | 1.27 | niska-średnia |
| Polska - Szwecja | Over 1.5 | 76,9% | 1.30 | średnia |
| Bośnia - Rumunia | Over 1.5 | 75,1% | 1.33 | średnia |
| Węgry - NI | Under 2.5 | 65% | 1.54 | średnia |
| Węgry - NI | BTTS nie | 63% | 1.59 | średnia |
| Ukraina - Gruzja | Under 2.5 | 64% | 1.56 | średnia |
| Irlandia - Kosowo | Under 2.5 | 63% | 1.59 | średnia |

Pominięte (fair <= 1.15): Under 3.5 w Hungary-NI (1.15), wszystkie Over 0.5.
Kursy Superbet dla rożnych, kartek i BTTS nie pobrane (tylko 1X2, podwójna szansa i gole).

Wszystkie wartości to oszacowania probabilistyczne, nie gwarancje.
