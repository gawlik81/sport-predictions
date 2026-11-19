# Analiza piłkarska B - 12.11.2026 (godziny PL)

Zakres: 7 meczów (Liga Narodów UEFA 2026/27 x3, Liga Mistrzyń kobiet x2, towarzyskie x2). Skille: football-analyst (poisson.py, markets.py). Źródła: Superbet MCP (stats, H2H, nieobecni, kursy; kursy Superbet z 12.11), WebSearch (kontekst grup; składy oficjalne niedostępne przed meczem), własny model Poissona/NB.

Zastrzeżenia ogólne:
- Próby statystyczne z `superbet_stats` to 3-4 mecze bieżącej edycji (w tym San Marino jako rywal), więc λ kalibrowano głównie do formy, H2H i rynku bez marży; różnice vs rynek bez marży nie przekraczają ~5 pp (poza Maltą, patrz sekcja 7).
- Sędziowie znani tylko w 5 z 7 meczów, bez ich historii kartek (brak źródła) - kartki liczone ze średnich drużyn/rynku, pewność maks. średnia.
- Składy oficjalne nieopublikowane w momencie analizy; typy zawodnika pominięte.
- Kursy Superbet porównane z moim p: prawie wszędzie EV < 0 (rynek wycenia podobnie, marża zjada przewagę). Jedyne drobne dodatnie EV to rożne (Albania O8.5, Czarnogóra O8.5, Barcelona O8.5) - w granicach szumu.

---

## 1. Albania - Finlandia (Liga Narodów, liga C gr. 1, kol. 5, 20:45, Air Albania Stadium, Tirana)

Ranga: mecz o pierwsze miejsce w grupie (awans do ligi B); Albania prowadzi (9 pkt z 4 meczów), Finlandia ~7 pkt. Pełna motywacja obu stron, brak rotacji. Sędzia: Joao Pedro Pinheiro (POR).

**Parametry:** λ Albania 1.15, λ Finlandia 0.85 (xG 2.1 vs 1.4 w próbie, ale przeciwnicy to San Marino/Białoruś; Albania bez Kumbulli i Shehu: -0,05 λ; Finlandia bez absencji).

| Rynek | p | fair | Kurs Superbet | Pewność |
|---|---|---|---|---|
| 1 Albania | 42.6% | 2.35 | 2.12 | średnia |
| X | 30.4% | 3.29 | 2.95 | średnia |
| 2 Finlandia | 27.0% | 3.70 | 3.85 | średnia |
| 1X | 73.0% | 1.37 | 1.24 | średnia |
| X2 | 57.4% | 1.74 | 1.67 | średnia |
| 12 | 69.6% | 1.44 | 1.37 | średnia |
| Over 1.5 | 59.4% | 1.68 | 1.61 | średnia |
| Under 1.5 | 40.6% | 2.46 | 2.30 | niska |
| Over 2.5 | 32.3% | 3.09 | 2.87 | średnia |
| Under 2.5 | 67.7% | 1.48 | 1.41 | średnia |
| Over 3.5 | 14.3% | 7.00 | 5.85 | średnia |
| Under 3.5 | 85.7% | 1.17 | 1.13 | średnia (graniczny fair) |
| BTTS tak | 39.1% | 2.56 | n/d | niska |
| BTTS nie | 60.9% | 1.64 | n/d | niska |
| Rożne O8.5 (śr. 9.2) | 55.3% | 1.81 | 1.88 | niska/średnia |
| Rożne U9.5 | 56.4% | 1.77 | 1.51 | niska |
| Rożne O10.5 | 32.8% | 3.05 | 3.05 | niska |
| Kartki O3.5 (śr. 4.0) | 53.8% | 1.86 | 1.64 | niska |
| Kartki U4.5 | 63.0% | 1.59 | 1.49 | niska |
| Dokładny wynik | 1-0 15.6% (6.43), 0-0 13.5% (7.39), 1-1 13.2% (7.56) | | | niska |

**Statystyki:** Albania 3 W z 4 w LN (2-0 Białoruś, 3-0 i 2-1 San Marino, 1-2 w Finlandii); śr. 2.0 gola strzelonego, 0.8 straconego, 5.8 celnych, rożne 6.8. Finlandia: 7-0 San Marino, 2-1 Albania, 0-0 i 0-1 z Białorusią; śr. 2.3 strzelonego (zawyżone przez San Marino), 0.5 straconego. Jakość z lepszymi rywalami słabsza (0-4 Niemcy, 1-2 Węgry w czerwcu).
**H2H:** 03.10.2026 Finlandia - Albania 2:1 (czerwona kartka). Poprzednio brak w bazie.
**Informacje medialne:** Albania: Kumbulla i Shehu kontuzjowani (Superbet); Finlandia bez absencji. Trenerzy: Maran / Friis. Składy nieogłoszone.
**Ryzyka:** wyrównany mecz (żaden wynik >43%); remis ~30%, ale i wygrana Finlandii 27% (rewanż za 2-1). Gospodarz nie jest pewniakiem. Czerwona kartka (poprzedni mecz miał) rozbija Under.
**Rynek:** zgodny z modelem w granicach 2-3 pp; brak value. **Najlepszy rynek:** Under 2.5 (67.7%) lub 1X (73%) - brak mocnego typu na wynik.

---

## 2. Czarnogóra - Łotwa (Liga Narodów, liga C gr. 2, kol. 5, 20:45, Stadion Pod Goricom, Podgorica)

Ranga: Czarnogóra liderem grupy z 4 zespołów walczących o awans do ligi B; Łotwa w tej edycji bez wygranej (0-2 Armenia, 1-2 Czarnogóra, 1-2 Cypr). Pełna motywacja gospodarzy. Sędzia: Jerome Brisard (FRA).

**Parametry:** λ Czarnogóra 2.10, λ Łotwa 0.70 (reprezentacja: nie schodzimy poniżej 0.7; Łotwa strzeliła 0.5/mecz, xG 0.7). Czarnogóra bez Loncara (zawieszony; Superbet), korekta -0.05. Gospodarze xG 1.9.

| Rynek | p | fair | Kurs Superbet | Pewność |
|---|---|---|---|---|
| 1 Czarnogóra | 69.9% | 1.43 | 1.28 | średnia/wysoka |
| X | 18.9% | 5.29 | 5.30 | średnia |
| 2 Łotwa | 11.2% | 8.92 | 9.30 | średnia |
| 1X | 88.8% | 1.13 | 1.04 | średnia (graniczny fair) |
| X2 | 30.1% | 3.32 | 3.35 | średnia |
| 12 | 81.1% | 1.23 | 1.14 | średnia |
| Over 1.5 | 76.9% | 1.30 | 1.26 | średnia |
| Over 2.5 | 53.1% | 1.88 | 1.80 | niska |
| Under 2.5 | 46.9% | 2.13 | 2.00 | niska |
| Over 3.5 | 30.8% | 3.25 | 3.05 | niska |
| Under 3.5 | 69.2% | 1.45 | 1.38 | średnia |
| BTTS tak | 44.2% | 2.26 | n/d | niska |
| BTTS nie | 55.8% | 1.79 | n/d | niska |
| Rożne O8.5 (śr. 9.8) | 62.1% | 1.61 | 1.62 | niska/średnia |
| Rożne O9.5 | 50.6% | 1.98 | 1.95 | niska |
| Rożne O10.5 | 39.4% | 2.54 | 2.45 | niska |
| Kartki O3.5 (śr. 3.8) | 50.2% | 1.99 | 1.59 | niska |
| Kartki U4.5 | 66.4% | 1.51 | 1.53 | niska |
| Dokładny wynik | 2-0 13.4% (7.46), 1-0 12.8% (7.83), 3-0 9.4% (10.65) | | | niska |

**Statystyki:** Czarnogóra 4 mecze LN: 2-1 Cypr, 3-2 w Armenii, 2-1 Łotwa (wyjazd), mecz z Armenią 05.10 (wynik niedostępny, czerwona kartka); śr. 1.8 gola, 1.0 straconego. Łotwa: 0-2 Armenia, 1-2 Czarnogóra, 1-2 Cypr; śr. 0.5 strzelonego, 1.5 straconego. Czerwcowe wyniki Łotwy: 0-1 z Wyspami Owczymi.
**H2H:** 02.10.2026 Łotwa - Czarnogóra 1:2 (źródła podają też 0:2); 2021 0:0 i 1:2, 2020 1:1. Bilans Czarnogóry 3 W 2 R 0 P.
**Informacje medialne:** zawieszony Loncar; oficjalne składy brak. Trenerzy: Vucinic / Nicolato.
**Ryzyka:** remis (19%) i wygrana Łotwy (11%), przy czym Łotwa strzela rzadko; Czarnogóra konsekwentnie traci gole w LN (2 straty w 3 z 4 meczów), więc BTTS i Over nie są wykluczone. Dwa gole po 80' często przy obronie wyniku.
**Rynek:** model 4-5 pp niżej niż rynek bez marży na wygraną Czarnogóry (72.5%); zgodnie z regułą "nie schodź pod rynek bez konkretów" - tu różnica tylko λ (floor Łotwy 0.7). **Najlepszy rynek:** wygrana Czarnogóry / Over 1.5 (fair 1.30), bez EV.

---

## 3. San Marino - Białoruś (Liga Narodów, liga C gr. 1, kol. 5, 20:45, Serravalle)

Ranga: Białoruś walczy o 1. miejsce (7 pkt), San Marino bez zdobytego punktu w tej edycji (0-7, 0-3, 0-4, 1-2). Pełna motywacja Białorusi; rotacji nie oczekujemy. Sędzia: Goga Kikacheishvili (GEO).

**Parametry:** λ San Marino 0.33, λ Białoruś 2.45 (xG Białorusi 0.9 w próbie, ale wyniki 4-0 z San Marino i rywal klasy najsłabszej w UEFA; łączna średnia 1.3 gola i 0.5 straconego). Białoruś bez Shumanskiy'ego (zawieszony; skrzydłowy), -0.05.

| Rynek | p | fair | Kurs Superbet | Pewność |
|---|---|---|---|---|
| 1 San Marino | 3.5% | 28.7 | 18.0 | wysoka (że nie wygrają) |
| X | 12.3% | 8.11 | 7.70 | średnia |
| 2 Białoruś | 84.2% | 1.19 | 1.13 | wysoka |
| 1X | 15.8% | 6.33 | 5.20 | średnia |
| X2 | 96.5% | 1.04 | 1.007 | wysoka (fair poniżej 1.15) |
| 12 | 87.7% | 1.14 | 1.07 | wysoka (fair poniżej 1.15) |
| Over 1.5 | 76.5% | 1.31 | 1.21 | średnia/wysoka |
| Over 2.5 | 52.6% | 1.90 | 1.66 | niska |
| Under 2.5 | 47.4% | 2.11 | 2.20 | niska |
| Over 3.5 | 30.4% | 3.29 | 2.65 | niska |
| Under 3.5 | 69.6% | 1.44 | 1.47 | średnia |
| Under 4.5 | ~84% | ~1.19 | 1.18 | średnia |
| BTTS tak | 25.7% | 3.89 | n/d | średnia |
| BTTS nie | 74.3% | 1.35 | n/d | średnia |
| Rożne O8.5 (śr. 9.3) | 56.5% | 1.77 | 1.54 | niska |
| Rożne O9.5 | 44.7% | 2.24 | 1.85 | niska |
| Kartki O4.5 (śr. 5.0) | 53.4% | 1.87 | 1.49 | niska |
| Kartki U5.5 | 61.7% | 1.62 | 1.69 | niska |
| Kartki U6.5 | 74.3% | 1.35 | 1.35 | niska |
| Dokładny wynik | 0-2 18.6% (5.37), 0-1 15.2% (6.58), 0-3 15.2% (6.58) | | | niska |

**Statystyki:** San Marino: 0.3 gola strzelonego, 4.0 straconego na mecz; xG 0.5. Białoruś 1.3 strzelonego, 0.5 straconego (1-0 Finlandia, 0-0 Finlandia, 4-0 SM, 0-2 Albania). Obie drużyny faulują i dostają dużo kartek (3.0 i 3.3 na mecz) - przy dużej różnicy klas SM broni się faulami.
**H2H:** 03.10.2026 Białoruś - San Marino 4:0; 2018: 5:0 i 2:0 dla Białorusi.
**Informacje medialne:** zawieszony Shumanskiy; składy nieznane.
**Ryzyka:** niski wynik (Białoruś 1-0 po 0-0 z Finlandią; w 3 z 4 meczach do 1 gola z wyjątkiem SM), czerwona kartka dla San Marino. Fair wygranej Białorusi 1.19 jest powyżej progu 1.15 tylko nieznacznie.
**Rynek:** zgodny z modelem (84.2% vs 82.7% bez marży). **Najlepszy rynek:** Białoruś wygra (1.19), Over 1.5 (1.31), BTTS nie (1.35) - bez dodatniego EV.

---

## 4. Barcelona (K) - Arsenal (K) (Liga Mistrzyń 2026/27, faza ligowa, 18:45, Spotify Camp Nou)

Ranga: faza ligowa UWCL, rewanż finału 2025 (Arsenal 1:0 w Lizbonie); obie drużyny walczą o czołówkę, bez rotacji. Sędzia: Ivana Martincic (CRO).

**Parametry:** λ Barcelona 3.00, λ Arsenal 1.00 (Barcelona w próbie 6.3 gola/mecz przeciw słabszym, rynek daje 75% 1; Arsenal 4 gole stracone w ostatnich 2 spotkaniach z City i drużynami ligi angielskiej: 2-4 City, 1-1 Aston Villa, 2-1 Liverpool, 3-0 Benfica).

| Rynek | p | fair | Kurs Superbet | Pewność |
|---|---|---|---|---|
| 1 Barcelona | 77.5% | 1.29 | 1.21 | średnia |
| X | 13.1% | 7.62 | 6.50 | średnia |
| 2 Arsenal | 9.4% | 10.65 | 8.30 | średnia |
| 1X | 90.6% | 1.10 | 1.03 | wysoka (fair poniżej 1.15) |
| X2 | 22.5% | 4.44 | 3.65 | średnia |
| 12 | 86.9% | 1.15 | 1.07 | wysoka (fair graniczny) |
| Over 1.5 | 90.8% | 1.10 | n/d | wysoka (fair poniżej 1.15) |
| Over 2.5 | 76.2% | 1.31 | 1.20 | średnia |
| Under 2.5 | 23.8% | 4.20 | 4.00 | średnia |
| Over 3.5 | 56.6% | 1.77 | 1.53 | niska/średnia |
| Under 3.5 | 43.4% | 2.31 | 2.30 | niska |
| BTTS tak | 60.1% | 1.66 | n/d | niska |
| BTTS nie | 39.9% | 2.50 | n/d | niska |
| Rożne O8.5 (śr. 10.3) | 67.3% | 1.49 | 1.49 | niska/średnia |
| Rożne O9.5 | 56.2% | 1.78 | 1.77 | niska |
| Rożne O10.5 | 45.0% | 2.22 | 2.17 | niska |
| Kartki O1.5 (śr. 2.6) | 68.5% | 1.46 | n/d | niska |
| Kartki O2.5 | 45.9% | 2.18 | n/d | niska |
| Dokładny wynik | 2-0, 3-0, 2-1, 3-1 po 8.2% (fair 12.13) | | | niska |

**Statystyki:** Barcelona ostatnio: 5-1 Madryt CCF, 4-0 Badalona, 8-0 HB Koge, 3-0 Granada, 1-2 Real Sociedad (jedyna porażka), 7-0 Real Madryt; średnio 6.3 gola. Arsenal: 2-1 Liverpool, 1-1 Villa, 3-0 Benfica (UWCL), 2-1 Tottenham, 1-1 Birmingham, 2-4 City. Kartek w kobiecej piłce mało (próba 0.3-0.7 na drużynę).
**H2H:** 24.05.2025 Arsenal 1:0 Barcelona (finał UWCL); 2021 Barcelona 4:1 i 4:0 (wyjazd Arsenalu 0:4).
**Informacje medialne:** brak danych kadrowych (Superbet nie obsługuje nieobecnych dla kobiet; wyszukiwanie nie zwróciło aktualnych newsów). We wrześniu Barcelona bez Paredes i van Asten (stare, nieaktualne). Trenerzy: Romeu / Slegers.
**Ryzyka:** Arsenal to zeszłoroczny triumfator potwierdzający klasę (1:0 w finale); Barcelona ma historię wpadek w meczach z drużynami ligi angielskiej; remis 13%, wygrana Arsenalu 9.4% - w sumie ~22%, przy kursie 8.30 Arsenal nieopłacalny.
**Rynek:** zgodny (75.1% bez marży vs 77.5%). **Najlepszy rynek:** Over 2.5 (fair 1.31, kurs 1.20 - EV -9%) lub rożne O8.5 (kurs 1.49, EV ~0) - brak value.

---

## 5. Benfica (K) - Austria Wiedeń (K) (Liga Mistrzyń 2026/27, faza ligowa, 21:00, Estadio do Sport Lisboa e Benfica)

Ranga: faza ligowa UWCL; obie drużyny w dolnej/środkowej części tabeli. Benfica gra u siebie, bez rotacji. Sędzia: Caroline Lanssens (BEL). Uwaga: wyszukiwarka podała część źródeł z datą 11.11; Superbet i terminarz wskazują 12.11, godz. 21:00 PL (20:00 UTC).

**Parametry:** λ Benfica 1.90, λ Austria 0.90. Benfica w UWCL: 0-3 Bayern, 0-3 Arsenal, ligowo 4-1 Sporting, 6-0 Braga; Austria: 1-1 Inter, 1-4 Juventus, ale 6-0 Rapid. Rynek (63.4% Benfica) sugeruje przewagę wyższą niż moja; trzymam się różnicy <5 pp.

| Rynek | p | fair | Kurs Superbet | Pewność |
|---|---|---|---|---|
| 1 Benfica | 60.8% | 1.64 | 1.44 | średnia |
| X | 21.9% | 4.57 | 4.35 | średnia |
| 2 Austria | 17.3% | 5.78 | 5.85 | średnia |
| 1X | 82.7% | 1.21 | 1.09 | średnia |
| X2 | 39.2% | 2.55 | 2.50 | niska |
| 12 | 78.1% | 1.28 | 1.16 | średnia |
| Over 1.5 | 76.9% | 1.30 | 1.20 | średnia |
| Over 2.5 | 53.1% | 1.88 | 1.66 | niska |
| Under 2.5 | 46.9% | 2.13 | 2.07 | niska |
| Over 3.5 | 30.8% | 3.25 | 2.65 | niska |
| Under 3.5 | 69.2% | 1.45 | 1.41 | średnia |
| BTTS tak | 50.5% | 1.98 | n/d | niska |
| BTTS nie | 49.5% | 2.02 | n/d | niska |
| Rożne O8.5 (śr. 9.4) | 57.7% | 1.73 | 1.54 | niska |
| Rożne O9.5 | 45.9% | 2.18 | 1.85 | niska |
| Kartki O1.5 (śr. 2.8) | 72.1% | 1.39 | n/d | niska |
| Kartki O2.5 | 50.2% | 1.99 | n/d | niska |
| Dokładny wynik | 1-0 11.6% (8.66), 2-0 11.0% (9.11), 1-1 10.4% (9.62) | | | niska |

**Statystyki:** Superbet nie zwraca średnich meczowych (puste); forma: Benfica 1-0 z Torreense (wąsko), 0-3 z Arsenalem, 4-1 Sporting, 4-0 Maritimo, 6-0 Braga, 0-3 Bayern. Austria: 3-0 LASK, 1-4 Juventus, 1-1 Altach, 3-0 St. Polten, 6-0 Rapid, 1-1 Inter.
**H2H:** brak spotkań.
**Informacje medialne:** brak danych kadrowych i składów (kobiety nie objęte endpointem). Trenerzy: Baptista / Kenesei.
**Ryzyka:** Benfica bezradna w UWCL z silniejszymi (0-3 x2), Austria potrafi zremisować z Interem; mecz bliżej do 55-60% niż 63%; remis 22%, wygrana Austrii 17%.
**Rynek:** różnica do rynku 2.6 pp (60.8% vs 63.4%), brak value. **Najlepszy rynek:** 1X (fair 1.21) lub Over 1.5 (1.30) - bez EV.

---

## 6. Litwa - Surinam (towarzyski, 18:00, Dariaus ir Girenas, Kowno)

Ranga: towarzyski (nie liczy się do rankingu w sposób znaczący); Litwa gra za 4 dni Ligę Narodów z Liechtensteinem (16.11) - rotacja prawdopodobna; Surinam w trakcie przerwy, dużo grających za granicą (Holandia), skład Henka Frasera może się znacznie różnić od ostatnich zgrupowań. Wysoka niepewność składów. Sędzia: nieznany.

**Parametry:** λ Litwa 1.05, λ Surinam 1.20 (Litwa defensywna: 3 stracone w 4 meczach LN, ale też 0 strzelonych w Azerbejdżanie; Surinam: 2-1 Martynika, 3-2 Honduras, 0-1 Gwatemala w CONCACAF).

| Rynek | p | fair | Kurs Superbet | Pewność |
|---|---|---|---|---|
| 1 Litwa | 31.9% | 3.13 | 2.82 | niska |
| X | 28.6% | 3.49 | 3.05 | niska |
| 2 Surinam | 39.4% | 2.54 | 2.50 | niska |
| 1X | 60.5% | 1.65 | 1.47 | niska |
| X2 | 68.0% | 1.47 | 1.38 | niska |
| 12 | 71.3% | 1.40 | 1.33 | niska |
| Over 1.5 | 65.7% | 1.52 | 1.44 | niska |
| Over 2.5 | 39.1% | 2.56 | 2.35 | niska |
| Under 2.5 | 60.9% | 1.64 | 1.51 | niska |
| Over 3.5 | 19.1% | 5.25 | 4.35 | niska |
| Under 3.5 | 80.9% | 1.24 | 1.17 | niska |
| BTTS tak | 45.4% | 2.20 | n/d | niska |
| BTTS nie | 54.6% | 1.83 | n/d | niska |
| Rożne O7.5 (śr. 8.6) | 60.5% | 1.65 | 1.47 | niska |
| Rożne O8.5 | 48.1% | 2.08 | 1.77 | niska |
| Rożne O9.5 | 36.5% | 2.74 | 2.20 | niska |
| Kartki O3.5 (śr. 3.8, szacunek) | 50.2% | 1.99 | brak rynku | bardzo niska |
| Dokładny wynik | 1-1 13.3% (7.53), 0-1 12.6% (7.91), 1-0 11.1% (9.04) | | | niska |

**Statystyki:** Litwa: 0-1 Azerbejdżan (wyjazd), 3-0 Andora, 1-1 Azerbejdżan, 2-0 Liechtenstein; wiosną 0-2 Gruzja, 2-0 Mołdawia. Surinam: 1-0 przegrana z Gwatemalą, 2-1 Martynika, 3-2 Honduras, 1-2 Boliwia (marzec). Wyniki z wyższą szczytowością - Surinam średnio strzela 1.5+.
**H2H:** brak.
**Informacje medialne:** LRT ogłosił skład na mecze z Surinamem i Liechtensteinem (nazwiska nie odczytane); brak nieobecnych w bazie.
**Ryzyka:** towarzyski - zmiany po 60'; wyrównane trzy wyniki (32/29/39). Brak mocnego typu.
**Rynek:** zgodny w granicach 2 pp. **Najlepszy rynek:** brak (X2 fair 1.47 / Under 3.5 1.24), bez EV.

---

## 7. Malta - Eswatini (towarzyski, 18:30, Ta' Qali)

Ranga: towarzyski; Malta ma 5 meczów bez porażki (2-0 Liechtenstein, 2-1 Andora wyjazd, 1-1 Gibraltar, 1-0 Andora, 0-2 Azerbejdżan w czerwcu); Eswatini bez meczu od marca 2026 (0-2 i 1-2 z Erytreą), podróż do Europy, brak zgrania. Sędzia: nieznany. Skład Malty (trener De Leo) nieznany.

**Parametry:** λ Malta 1.70, λ Eswatini 0.85. Rynek (63.7% dla Malty) jest wyżej niż mój model wyjściowy 1.55/0.90 (52.6%); podniosłem λ gospodarza do 1.7 z powodu długiej przerwy i podróży Eswatini, bez nowych informacji kadrowych. Różnica do rynku wciąż ~6 pp (57.5% vs 63.7%) - zgodnie z regułą nie schodzę niżej bez konkretów, ale pewność niska.

| Rynek | p | fair | Kurs Superbet | Pewność |
|---|---|---|---|---|
| 1 Malta | 57.5% | 1.74 | 1.45 | niska |
| X | 23.9% | 4.19 | 4.10 | niska |
| 2 Eswatini | 18.6% | 5.38 | 6.70 | niska |
| 1X | 81.4% | 1.23 | 1.08 | niska |
| X2 | 42.5% | 2.35 | 2.55 | niska |
| 12 | 76.1% | 1.31 | 1.20 | niska |
| Over 1.5 | 72.3% | 1.38 | 1.37 | niska |
| Over 2.5 | 46.9% | 2.13 | 2.15 | niska |
| Under 2.5 | 53.1% | 1.88 | 1.62 | niska |
| Over 3.5 | 25.3% | 3.95 | 3.85 | niska |
| Under 3.5 | 74.7% | 1.34 | 1.21 | niska |
| BTTS tak | 46.8% | 2.14 | n/d | niska |
| BTTS nie | 53.2% | 1.88 | n/d | niska |
| Rożne O7.5 (śr. 8.6) | 60.5% | 1.65 | 1.49 | niska |
| Rożne O8.5 | 48.1% | 2.08 | 1.80 | niska |
| Rożne O9.5 | 36.5% | 2.74 | 2.22 | niska |
| Kartki O3.5 (śr. 3.5, szacunek) | 44.7% | 2.24 | brak rynku | bardzo niska |
| Dokładny wynik | 1-0 13.3% (7.53), 1-1 11.3% (8.86), 2-0 11.3% (8.86) | | | niska |

**Statystyki:** Malta: 4 mecze LN bez porażki (3W 1R), 6 goli strzelonych, 2 stracone (1.5 / 0.5 na mecz). Eswatini: 6 ostatnich meczów bez wygranej (0-3 Zielony Przylądek, 2-2 Angola, 0-2 Libia, 0-3 Kamerun, 0-2 i 1-2 Erytrea) - średnio 0.8 strzelonego, 2.0 straconego.
**H2H:** brak.
**Informacje medialne:** tylko listing meczu; brak nieobecnych. Trenerzy: De Leo / Ntibane.
**Ryzyka:** towarzyski z wieloma zmianami; Malta gra zachowawczo i mało goli (Under 2.5 realne); faworytem jest Malta, ale kurs 1.45 na wygraną nie ma value (EV -17%).
**Rynek:** różnica 6 pp na wygranej Malty, bez nowych informacji; **Najlepszy rynek:** brak (1X fair 1.23, Over 1.5 1.38), bez EV.

---

## Tabela zbiorcza: mecz | rynek | p | fair | pewność

| Mecz | Rynek | p | fair | Pewność |
|---|---|---|---|---|
| Albania - Finlandia | Under 2.5 | 67.7% | 1.48 | średnia |
| Albania - Finlandia | 1X | 73.0% | 1.37 | średnia |
| Albania - Finlandia | 1 / X / 2 | 42.6 / 30.4 / 27.0% | 2.35 / 3.29 / 3.70 | średnia (brak mocnego typu) |
| Albania - Finlandia | Over 2.5 / BTTS tak | 32.3% / 39.1% | 3.09 / 2.56 | niska |
| Albania - Finlandia | Rożne O8.5 (śr. 9.2) / Kartki O3.5 (śr. 4.0) | 55.3% / 53.8% | 1.81 / 1.86 | niska |
| Albania - Finlandia | Wynik: 1-0 / 0-0 / 1-1 | 15.6 / 13.5 / 13.2% | 6.43 / 7.39 / 7.56 | niska |
| Czarnogóra - Łotwa | 1 | 69.9% | 1.43 | średnia/wysoka |
| Czarnogóra - Łotwa | 1X / 12 | 88.8% / 81.1% | 1.13 / 1.23 | średnia |
| Czarnogóra - Łotwa | Over 1.5 / Under 3.5 | 76.9% / 69.2% | 1.30 / 1.45 | średnia |
| Czarnogóra - Łotwa | Over 2.5 / BTTS tak | 53.1% / 44.2% | 1.88 / 2.26 | niska |
| Czarnogóra - Łotwa | Rożne O9.5 (śr. 9.8) / Kartki O3.5 (śr. 3.8) | 50.6% / 50.2% | 1.98 / 1.99 | niska |
| Czarnogóra - Łotwa | Wynik: 2-0 / 1-0 / 3-0 | 13.4 / 12.8 / 9.4% | 7.46 / 7.83 / 10.65 | niska |
| San Marino - Białoruś | 2 Białoruś | 84.2% | 1.19 | wysoka |
| San Marino - Białoruś | Over 1.5 / BTTS nie | 76.5% / 74.3% | 1.31 / 1.35 | średnia/wysoka |
| San Marino - Białoruś | Over 2.5 / Under 3.5 | 52.6% / 69.6% | 1.90 / 1.44 | niska/średnia |
| San Marino - Białoruś | X2 / 12 (fair poniżej 1.15) | 96.5% / 87.7% | 1.04 / 1.14 | wysoka |
| San Marino - Białoruś | Rożne O8.5 (śr. 9.3) / Kartki O4.5 (śr. 5.0) | 56.5% / 53.4% | 1.77 / 1.87 | niska |
| San Marino - Białoruś | Wynik: 0-2 / 0-1 / 0-3 | 18.6 / 15.2 / 15.2% | 5.37 / 6.58 / 6.58 | niska |
| Barcelona (K) - Arsenal (K) | 1 Barcelona | 77.5% | 1.29 | średnia |
| Barcelona (K) - Arsenal (K) | Over 2.5 / Over 3.5 | 76.2% / 56.6% | 1.31 / 1.77 | średnia / niska |
| Barcelona (K) - Arsenal (K) | BTTS tak / 12 | 60.1% / 86.9% | 1.66 / 1.15 | niska / wysoka |
| Barcelona (K) - Arsenal (K) | Rożne O9.5 (śr. 10.3) / Kartki O1.5 (śr. 2.6) | 56.2% / 68.5% | 1.78 / 1.46 | niska |
| Barcelona (K) - Arsenal (K) | Wynik: 2-0, 3-0, 2-1, 3-1 | po 8.2% | 12.13 | niska |
| Benfica (K) - Austria (K) | 1 Benfica | 60.8% | 1.64 | średnia |
| Benfica (K) - Austria (K) | 1X / Over 1.5 | 82.7% / 76.9% | 1.21 / 1.30 | średnia |
| Benfica (K) - Austria (K) | Over 2.5 / BTTS tak | 53.1% / 50.5% | 1.88 / 1.98 | niska |
| Benfica (K) - Austria (K) | Rożne O9.5 (śr. 9.4) / Kartki O2.5 (śr. 2.8) | 45.9% / 50.2% | 2.18 / 1.99 | niska |
| Benfica (K) - Austria (K) | Wynik: 1-0 / 2-0 / 1-1 | 11.6 / 11.0 / 10.4% | 8.66 / 9.11 / 9.62 | niska |
| Litwa - Surinam | 2 Surinam / X2 | 39.4% / 68.0% | 2.54 / 1.47 | niska |
| Litwa - Surinam | Under 2.5 / Over 1.5 | 60.9% / 65.7% | 1.64 / 1.52 | niska |
| Litwa - Surinam | BTTS tak / nie | 45.4% / 54.6% | 2.20 / 1.83 | niska |
| Litwa - Surinam | Rożne O8.5 (śr. 8.6) | 48.1% | 2.08 | niska |
| Litwa - Surinam | Wynik: 1-1 / 0-1 / 1-0 | 13.3 / 12.6 / 11.1% | 7.53 / 7.91 / 9.04 | niska |
| Malta - Eswatini | 1 Malta | 57.5% | 1.74 | niska |
| Malta - Eswatini | 1X / Over 1.5 | 81.4% / 72.3% | 1.23 / 1.38 | niska |
| Malta - Eswatini | Under 2.5 / BTTS nie | 53.1% / 53.2% | 1.88 / 1.88 | niska |
| Malta - Eswatini | Rożne O8.5 (śr. 8.6) | 48.1% | 2.08 | niska |
| Malta - Eswatini | Wynik: 1-0 / 1-1 / 2-0 | 13.3 / 11.3 / 11.3% | 7.53 / 8.86 / 8.86 | niska |

Dla bet-slip-buildera: najwięcej wartości w zakresie progów (fair > 1.15, p > 50%) mają: Białoruś wygra (84.2%), Czarnogóra wygra (69.9%), Barcelona Over 2.5 (76.2%), Barcelona wygra (77.5%), Czarnogóra Over 1.5 (76.9%), Białoruś Over 1.5 (76.5%), Benfica 1X (82.7%). Kursy Superbet na te typy dają EV < 0 (patrz sekcje), więc zestawy będą wymagać poluzowanych poziomów lub trybu EV.

To oszacowania probabilistyczne, nie gwarancje.
