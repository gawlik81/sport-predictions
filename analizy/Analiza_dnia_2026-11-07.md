# Analiza dnia 2026-11-07 (sobota, czas PL)

Źródło: skille *-analyst (subagenci), dane z MCP sportsdata i sieci. Kursy odniesienia w analizach to Pinnacle/inne, NIE Betclic.


---

# Premier League, sobota 07.11.2026 (GW10) - analiza football-analyst

Źródła: ESPN (tabela, terminarz), FPL API (status/newsy kontuzji, xG zawodników), Premier League API (sędziowie, terminarz), Pinnacle przez MCP (kursy odniesienia po usunięciu marży oraz linie rożnych i "bookings"; to jedyne źródło kursów, kursów Betclic nie sprawdzano). WebSearch nie zwrócił aktualnych zapowiedzi ani przewidywanych składów na ten tydzień, a H2H nie zostało pobrane (wagę H2H pominięto). Składy NIEPOTWIERDZONE (oficjalne ok. godz. przed meczem). Tabela po 9 kolejkach (W-R-P, bramki): Arsenal 8-0-1 14:5, Man City 7-0-2 20:10, Hull 2-5-2 11:10, Leeds 2-5-2 9:8, Spurs 3-3-3 10:10, Newcastle 3-2-4 12:15, Fulham 2-3-4 9:11, Forest 1-3-5 6:12.

Metoda: λ z Poissona (poisson.py), skalibrowane do rynku Pinnacle bez marży (nie schodzę pod rynek o >5 pp bez konkretów). Rożne i kartki: brak własnych statystyk drużyn i sędziów, średnia wyprowadzona wyłącznie z linii Pinnacle, więc pewność niska, bez rekomendacji na kupon.

---

## 1. Leeds United - Tottenham Hotspur (13:30, Elland Road)
Sędzia: John Brooks (statystyki kartek nieznane).
λ: Leeds 1.30, Spurs 1.35. Rynek bez marży 1X2: 34.6 / 28.6 / 36.9.

| Rynek | p | fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 35.8 / 26.1 / 38.1 | 2.79 / 3.83 / 2.62 | niska |
| 1X / X2 / 12 | 61.9 / 64.2 / 73.9 | 1.62 / 1.56 / 1.35 | niska/średnia |
| Over 1.5 | 74.2 | 1.35 | średnia |
| Over 2.5 / Under 2.5 | 49.4 / 50.6 | 2.02 / 1.98 | niska |
| Under 3.5 | 72.5 | 1.38 | średnia |
| BTTS tak / nie | 53.9 / 46.1 | 1.86 / 2.17 | niska |
| Rożne (linia ~10.0) O9.5 / U10.5 | 52.8 / 58.4 | 1.89 / 1.71 | niska |
| Kartki (średnia 4.8, linia Pinnacle 5.0) O3.5 / O4.5 | 66.5 / 50.2 | 1.50 / 1.99 | niska |

Brak mocnego typu (mecz wyrównany, 5 remisów Leeds w 9 meczach). Najbezpieczniej: 12 (bez remisu) ok. 74% lub Over 1.5.
Statystyki: Leeds 9 goli strzelonych, 8 straconych; Spurs 10:10; oba zespoły mało bramkowe (xG zawodników FPL ok. 11.5 i 11.7).
Kadry (FPL): Leeds - Calvert-Lewin 75%, Okafor 50%, Stach 50%, Mateo Joseph out; wg sportsmole Rodon out (hamstring), Elvedi 75% (niepotwierdzone). Spurs - out: Bergvall, Mudryk, Odobert, Sávio, Xavi; Richarlison poza kadrą.
Ryzyka: niepewne wejście Calvert-Lewina (główny strzelec Leeds); remis; mecz o niskiej liczbie okazji.

## 2. Arsenal - Hull City (16:00, Emirates)
Sędzia: Farai Hallam (VAR Oliver).
λ: Arsenal 2.70, Hull 0.55. Rynek: Arsenal 83.8 / X 11.4 / Hull 4.7; O2.5 ok. 63%.

| Rynek | p | fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 82.6 / 12.2 / 5.3 | 1.21 / 8.22 / 18.96 | wysoka (faworyt), średnia (rynki pochodne) |
| 1X | 94.8 | 1.05 | poniżej progu 1.15, pomijać |
| Over 1.5 | 83.5 | 1.20 | wysoka (graniczny 1.15-1.20) |
| Over 2.5 / Under 2.5 | 63.0 / 37.0 | 1.59 / 2.71 | średnia |
| Over 3.5 | 40.9 | 2.45 | niska |
| BTTS nie / tak | 60.5 / 39.5 | 1.65 / 2.53 | średnia |
| Arsenal AH -1.5 (rynek bez marży ok. 64%) | ok. 62-64 | ok. 1.58 | średnia |
| Rożne (średnia 10.4, linia 10.0) O9.5 / U10.5 | 57.3 / 53.9 | 1.75 / 1.86 | niska |
| Kartki (średnia 3.3, linia 3.0) U3.5 / O2.5 | 59.1 / 60.2 | 1.69 / 1.66 | niska |

Najlepszy rynek: Arsenal wygra (1.21) lub Over 2.5 / BTTS nie; AH -1.5 jako wariant.
Statystyki: Arsenal 14 goli, 5 straconych (lider, 24 pkt); Hull 11:10, 5 remisów.
Kadry (FPL): Arsenal - Saka out (udo, 3 gole), Dowman zawieszony; Hull - Crooks zawieszony, Hughes/Morita/Matazo/Ansah/Targett out, Gourna-Douath i Gyabi 75%. Hull okrojony w środku pola i ataku.
Ryzyka: wygrana Arsenalu przy rezygnacji z tempa po pucharach, remis (12%) i niska bramkowość (1-0), brak Saki zmniejsza liczbę zagrożeń; underdog nie jest w kryzysie (5 remisów, 11 pkt), więc bez korekty kryzysowej.

## 3. Fulham - Newcastle United (16:00, Craven Cottage)
Sędzia: Robert Jones.
λ: Fulham 1.65, Newcastle 1.20. Rynek bez marży: 47.0 / 26.4 / 26.6 (Fulham faworytem); O2.5 ok. 57%.

| Rynek | p | fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 47.9 / 24.3 / 27.8 | 2.09 / 4.11 / 3.60 | niska/średnia |
| 1X / X2 / 12 | 72.2 / 52.1 / 75.7 | 1.38 / 1.92 / 1.32 | średnia |
| Over 1.5 | 77.7 | 1.29 | średnia |
| Over 2.5 / Under 2.5 | 54.2 / 45.8 | 1.84 / 2.19 | niska/średnia |
| Under 3.5 | 68.1 | 1.47 | średnia |
| BTTS tak / nie | 56.5 / 43.5 | 1.77 / 2.30 | niska/średnia |
| Rożne (średnia 10.5, linia 10.5) O9.5 / O10.5 / U10.5 | 58.4 / 47.2 / 52.8 | 1.71 / 2.12 / 1.89 | niska |
| Kartki (średnia 3.6, linia 3.5) O2.5 / O3.5 | 65.5 / 46.5 | 1.53 / 2.15 | niska |

Najlepszy rynek: Over 1.5 / 12 (bez remisu) / BTTS tak; wynik 1X2 bez przewagi.
Statystyki: Fulham 9:11, 4 porażki, forma przeciętna (xG FPL ok. 13.9 vs 7-9 goli: niedokończenie); Newcastle 12:15 (najgorsza obrona z tej czwórki).
Kadry (FPL): Fulham - tylko Cairney out (kolano); Newcastle - out: Joelinton, Livramento, Jaouen, Ramsey zawieszony; wątpliwi: Miley 50%, Fernandez-Pardo 75%. Wg sportsmole wcześniej Newcastle mocno osłabiony (z kwietnia, nieaktualne).
Ryzyka: remis (24%) i wygrana gości po kontrach; przewaga kadrowa Fulham jest już w kursie rynkowym (moje p domu 47.9 vs 47.0).

## 4. Nottingham Forest - Manchester City (18:30, City Ground)
Sędzia: Samuel Barrott (VAR Tierney).
λ: Forest 1.00, City 1.95. Rynek bez marży: Forest 20.1 / X 24.4 / City 55.4; O2.5 ok. 57.7%.

| Rynek | p | fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 18.9 / 21.6 / 59.5 | 5.30 / 4.62 / 1.68 | średnia |
| X2 (City nie przegra) | 81.1 | 1.23 | średnia/wysoka |
| City DNB | 75.9 | 1.32 | średnia |
| Over 1.5 | 79.3 | 1.26 | średnia |
| Over 2.5 / Under 2.5 | 56.6 / 43.4 | 1.77 / 2.30 | średnia |
| Over 3.5 | 34.2 | 2.93 | niska |
| BTTS tak / nie | 54.2 / 45.8 | 1.84 / 2.18 | niska/średnia |
| Rożne (średnia 10.0, linia 10.0) O9.5 / U10.5 | 52.8 / 58.4 | 1.89 / 1.71 | niska |
| Kartki (średnia 3.6, linia 3.5) O3.5 / O2.5 | 46.5 / 65.5 | 2.15 / 1.53 | niska |

Najlepszy rynek: podwójna szansa X2 lub Over 1.5; wygrana City ok. 60% to nie "pewniak" (Forest broni się u siebie, ale ma tylko 6 goli w 9 meczach).
Statystyki: City 20:10 (Haaland 9 goli, xG 6.56); Forest 6:12, ostatnie miejsce w xG-niedoborze (xG zawodników ok. 14.9 vs 6 goli - wynik poniżej oczekiwań, potencjał regresji).
Kadry (FPL): City - Semenyo out (kolano); Forest - Dominguez out (do 30.12), Savona out, Igor Jesus 75% (łydka); Ndoye główny strzelec (2 gole).
Ryzyka dwustronne dla faworyta City: remis (21.6%) ORAZ wygrana Forest (18.9%); Forest u siebie w meczu wysokiej stawki (walka o utrzymanie, miejsce 19). Nie obniżano p faworyta za formę (reguła kalibracji).

---

## Kandydaci (uwaga dla bet-slip-buildera, kursów rynkowych Betclic brak)
| Mecz | Rynek | p | fair | Pewność | Zależy od |
|---|---|---|---|---|---|
| Arsenal - Hull | Arsenal wygra | 82.6 | 1.21 | wysoka | skład Arsenalu (brak Saki) |
| Arsenal - Hull | Over 2.5 | 63.0 | 1.59 | średnia | tempo, Saka/Havertz |
| Arsenal - Hull | Over 1.5 | 83.5 | 1.20 | wysoka (graniczny) | j.w. |
| Forest - City | X2 | 81.1 | 1.23 | średnia/wysoka | skład City |
| Forest - City | Over 1.5 | 79.3 | 1.26 | średnia | |
| Fulham - Newcastle | Over 1.5 | 77.7 | 1.29 | średnia | |
| Fulham - Newcastle | 12 | 75.7 | 1.32 | średnia | |
| Leeds - Spurs | Over 1.5 | 74.2 | 1.35 | średnia | Calvert-Lewin |

To oszacowania probabilistyczne, nie gwarancje.

---

# Analiza LaLiga (esp.1), 12. kolejka 2026/27, sobota 07.11.2026 (czas PL)

## Weryfikacja par i godzin (dwa niezależne źródła)
| Mecz | ESPN esp.1 (UTC -> PL) | oficjalny feed LaLiga (competition=primera-division) | Pinnacle (League "Spain - La Liga") | Wniosek |
|---|---|---|---|---|
| Málaga - Racing Santander | 13:00Z -> 14:00 | 13:00Z, La Rosaleda, PreMatch | 13:00Z | OK, Primera Division |
| Espanyol - Deportivo | 15:15Z -> 16:15 | 15:15Z, RCDE Stadium | 15:15Z | OK |
| Osasuna - Athletic Club | 17:30Z -> 18:30 | 17:30Z, El Sadar | 17:30Z | OK |
| Valencia - Real Madrid | 20:00Z -> 21:00 | 20:00Z, Mestalla | 20:00Z | OK |

Wszystkie 4 mecze istnieją w pierwszej lidze (nie Segunda). Uwaga: część stron WWW (comuniate, laliga.com ficha, footballdream) podaje dla niektórych meczów 08.11 20:00 lub 08.11 11:00, ale ESPN, API LaLiga i Pinnacle zgodnie dają 07.11 i podane godziny; strony WWW wyglądają na nieaktualne wpisy. Rekomendacja: przed kuponem sprawdzić godzinę na laliga.com.

Źródła: ESPN (scoreboard, standings, team_schedule), LaLiga API (laliga_matches), Pinnacle (matchup_markets, kursy amerykańskie przeliczone na dziesiętne, marża usunięta proporcjonalnie), WebSearch (kontuzje, słabe i częściowo sprzeczne).

## Tabela (po 10-11 meczach; punkty / bilans bramek GF-GA)
Real Madrid 3. 27 pkt 28-10 | Athletic 7. 15 pkt 14-10 (10 meczów) | Deportivo 8. 14 pkt 15-14 | Espanyol 14. 11 pkt 13-14 | Osasuna 15. 11 pkt 11-22 | Racing 16. 11 pkt 15-29 | Valencia 19. 9 pkt 8-17 | Málaga 20. 5 pkt 8-21 (0 zwycięstw, 5 remisów, 6 porażek).

## Brak danych (wpływa na pewność)
- Sędziowie: nie ogłoszeni / nie znalezieni dla żadnego meczu -> kartki i faule liczone ze średnią ligową, pewność niska.
- Statystyk rożnych/kartek drużyn z sezonu 2026/27 nie udało się pobrać z MCP ani z sieci -> rożne i kartki tylko jako szkic ze średnią ligową (rożne 9,8, kartki 5,4), BEZ rekomendacji na kupon.
- Kontuzje: tylko jedno słabe źródło (Asesorías Fantasy) dla Osasuna - Athletic; reszta brak. Składy niepotwierdzone (konferencje dopiero przed meczem). BettingPros: nie używany (brak klucza w tej sesji).
- λ ustawione na bazie goli/mecz z tabeli (próbka 10-11 meczów, duży szum), przycięte do rynku Pinnacle; zgodnie z kalibracją nie schodzę pod rynek o >5 pp bez konkretnych informacji (Racing i Real Madrid skorygowane z tego powodu).

---
## 1. Málaga - Racing Santander (14:00, La Rosaleda)
Typ: brak mocnego typu na wynik (wyrównane, lekka przewaga gospodarza). Najlepsze rynki: Over 1.5 (75,1%), 1X (67,5%).
λ: Málaga 1.45, Racing 1.25 (suma 2.7; rynek ok. 2.75).

| Rynek | p | fair | Pinnacle (bez marży) | Pewność |
|---|---|---|---|---|
| 1 Málaga | 41.8% | 2.39 | 39.6% (2.45) | niska |
| X | 25.7% | 3.90 | 28.0% | niska |
| 2 Racing | 32.6% | 3.07 | 32.3% (3.00) | niska |
| 1X | 67.5% | 1.48 | | niska/średnia |
| X2 | 58.3% | 1.72 | | niska |
| 12 | 74.4% | 1.34 | | średnia |
| Over 1.5 | 75.1% | 1.33 | | średnia |
| Over 2.5 | 50.6% | 1.97 | ok. 56% (O2.5 -136) | niska |
| Under 2.5 | 49.4% | 2.03 | | niska |
| Over 3.5 | 28.6% | 3.50 | | niska |
| BTTS tak | 54.6% | 1.83 | | niska/średnia |
| Rożne O9.5 | ok. 50% | ok. 2.0 | brak kursu | niska (średnia ligowa) |
| Kartki O4.5 | ok. 59% | 1.68 | | niska (sędzia nieznany) |

Statystyki (wyniki z ESPN, sprawdzone strona gospodarza-pierwsza): Málaga 0 zwycięstw (5 remisów, 6 porażek), 8 goli strzelonych / 21 straconych; u siebie 0W-3D-2L (1-1 Deportivo, 0-0 Levante, 1-3 Villarreal, 1-1 Espanyol, 2-5 Real Sociedad); ostatnio 1-1 w Alavés, 1-2 w Betis. Racing: u siebie świetnie (3W-2D-1L: 2-2 Villarreal, 3-2 Elche, 2-1 Alavés, 2-2 Valencia, 2-1 Espanyol, 0-3 z Real Madryt 01.11), ale na wyjeździe 0W-0D-5L, 4 gole strzelone i 18 straconych (0-1 Getafe, 2-3 Rayo, 2-7 Barcelona, 0-5 Celta, 0-2 Osasuna). Dlatego podniosłem λ Málagi (+) i obniżyłem λ Racingu względem średniej sezonowej.
H2H: brak spotkań w 2026/27; poprzednie sezony w Segunda - nie liczone.
Ryzyka: Málaga w kryzysie (0 wygranych), korektę kryzysową zastosowano tylko do jej remisu/wygranej: p 1 jest tylko 2 pp ponad rynkiem; remis (Málaga 5 remisów w 11); Racing może wygrać mimo słabych wyjazdów (strzela na każdym stadionie, gole po obu stronach). Składy/kontuzje i sędzia: brak danych.
Rynek: Pinnacle 2.45 / 3.46 / 3.00, total 2.75 (-109/-103), Over 2.5 -136.

## 2. Espanyol - Deportivo (16:15, RCDE Stadium)
Typ: Under 3.5 (79,9%, fair 1.25 - krótki, zakres 1.15-1.25) lub 1X (69,0%). Kierunkowo: Under 2.5 (59,6%).
λ: Espanyol 1.25, Deportivo 1.05 (suma 2.3).

| Rynek | p | fair | Pinnacle (bez marży) | Pewność |
|---|---|---|---|---|
| 1 Espanyol | 40.8% | 2.45 | 38.7% (2.51) | niska/średnia |
| X | 28.2% | 3.55 | 29.9% | niska |
| 2 Deportivo | 31.0% | 3.23 | 31.4% (3.09) | niska/średnia |
| 1X | 69.0% | 1.45 | | średnia |
| X2 | 59.2% | 1.69 | | niska |
| 12 | 71.8% | 1.39 | | średnia |
| Over 1.5 | 66.9% | 1.49 | | średnia |
| Over 2.5 | 40.4% | 2.48 | ok. 46% (O2.5 +112) | niska |
| Under 2.5 | 59.6% | 1.68 | ok. 54% | niska/średnia |
| Under 3.5 | 79.9% | 1.25 | | średnia |
| BTTS tak | 46.4% | 2.16 | | niska |
| BTTS nie | 53.6% | 1.87 | | niska |
| Rożne O9.5 | ok. 50% | ok. 2.0 | | niska |
| Kartki O4.5 | ok. 59% | 1.68 | | niska |

Statystyki: Espanyol 13 goli / 14 straconych; u siebie tylko 1W-1D-3L (3-0 Levante, 1-2 RM, 1-1 Sevilla, 1-3 Elche, 0-1 Atlético); ostatnio 1-2 w Racing (24.10) i 1-0 wygrana w Villarreal (30.10). Deportivo (8., 14 pkt, 5 remisów): 15 / 14; na wyjeździe 1W-2D-2L (1-1 Málaga, 3-2 w Villarreal, 1-1 Getafe, 2-3 Real Sociedad, 0-1 Atlético); ostatnio 1-0 przegrana w Atlético (24.10) i 2-1 wygrana z Osasuną (02.11).
H2H: brak spotkań w 2026/27 (Espanyol i Depor niedawno w różnych ligach) - nie liczone.
Ryzyka: remis (Depor remisuje często - p remisu może być zaniżone); Under 2.5 niepewne, Depor strzela u rywali. Składy/kontuzje, sędzia: nieznane.
Rynek: Pinnacle 2.51 / 3.25 / 3.09, total 2.5 (+112/-126).

## 3. Osasuna - Athletic Club (18:30, El Sadar)
Typ: X2 (ok. 69%, fair ok. 1.45) - Athletic nieco faworytem na wyjeździe; sam wynik 2 to ok. 41-45%, bez mocnego typu.
λ: Osasuna 1.00, Athletic 1.20 (suma 2.2; rynek ok. 2.25).

| Rynek | p | fair | Pinnacle (bez marży) | Pewność |
|---|---|---|---|---|
| 1 Osasuna | 30.5% | 3.28 | 24.9% (3.90) | niska |
| X | 28.9% | 3.46 | 28.3% | niska |
| 2 Athletic | 40.6% | 2.47 | 46.9% (2.07) | niska |
| 1X | 59.4% | 1.68 | | niska |
| X2 | 69.5% | 1.44 | | średnia |
| 12 | 71.1% | 1.41 | | średnia |
| Over 1.5 | 64.5% | 1.55 | | średnia |
| Over 2.5 | 37.7% | 2.65 | ok. 44% | niska |
| Under 2.5 | 62.3% | 1.61 | ok. 56% | niska/średnia |
| Under 3.5 | 81.9% | 1.22 | | średnia |
| BTTS tak | 44.2% | 2.26 | | niska |
| BTTS nie | 55.8% | 1.79 | | niska/średnia |
| Rożne O9.5 | ok. 50% | ok. 2.0 | | niska |
| Kartki O4.5 | ok. 59% | 1.68 | | niska |

Uwaga: mój p Athleticu (40,6%) jest 6,3 pp pod rynkiem; wynika z konkretów: Athletic na wyjeździe 1W-1D-2L (0-2 Barça, 2-0 Celta, 0-0 Valencia, 1-3 Levante), gole 3/6, a Osasuna u siebie broni dobrze (2W-2D-1L, tylko 3 gole stracone: 0-0 Levante, 1-0 Getafe, 0-2 Espanyol, 1-1 Rayo, 2-0 Racing). Rynek jednak bywa trafniejszy - traktować 2 Athletic jako 41-47%, niska pewność.
Statystyki: Osasuna 11 / 22 (wyjazdy fatalne: 5-2 Alavés, 4-0 Atlético, 5-2 Betis, 2-0 Sevilla, 2-1 Depor), ostatnio 1-2 w Deportivo (02.11). Athletic (10 meczów, zaległy) 14 / 10; ostatnio 4-0 Getafe i 2-1 Real Sociedad u siebie.
H2H: brak danych 2026/27.
Informacje medialne (jedno słabe źródło, Asesorías Fantasy, niepotwierdzone, możliwa nieaktualność): Osasuna bez Oroza, Del Castillo, Herrando; Athletic bez De Galarrety, Guruzeki. Nie zmieniałem λ z tego powodu (brak twardych danych).
Ryzyka: Athletic wygrywa lub remis (Osasuna gospodarz obrona 0.6 gola/mecz), Osasuna może wygrać u siebie. Sędzia nieznany.
Rynek: Pinnacle 3.90 / 3.43 / 2.07, total 2.25 (-110/-102), O2.5 +118.

## 4. Valencia - Real Madrid (21:00, Mestalla)
Typ: 2 Real Madryt 75,2% (fair 1.33); Over 1.5 (84,7%, fair 1.18, graniczny 1.15-1.20); Over 2.5 (65,0%).
λ: Valencia 0.80, Real Madryt 2.55 (suma 3.35).

| Rynek | p | fair | Pinnacle (bez marży) | Pewność |
|---|---|---|---|---|
| 1 Valencia | 9.5% | 10.50 | 8.3% (11.52) | wysoka, że nie typ |
| X | 15.3% | 6.55 | 14.9% | niska |
| 2 Real Madryt | 75.2% | 1.33 | 76.8% (1.25) | średnia |
| 1X | 24.8% | 4.03 | | niska |
| X2 | 90.5% | 1.10 | | pomijać (fair <= 1.15) |
| 12 | 84.7% | 1.18 | | graniczny |
| Over 1.5 | 84.7% | 1.18 | | średnia, graniczny |
| Over 2.5 | 65.0% | 1.54 | 65.8% (O2.5 -226) | średnia |
| Over 3.5 | 43.1% | 2.32 | ok. 45% | niska |
| Under 3.5 | 56.9% | 1.76 | | niska |
| BTTS tak | 50.8% | 1.97 | | niska |
| BTTS nie | 49.2% | 2.03 | | niska |
| Rożne O9.5 | ok. 50% | ok. 2.0 | | niska |
| Kartki O4.5 | ok. 59% | 1.68 | | niska (sędzia nieznany) |

Statystyki: Valencia 19., 9 pkt, 8 goli / 17 straconych; u siebie 0W-2D-4L, 3 gole strzelone, 11 straconych (0-0 Celta, 0-1 Betis, 0-5 Barça, 2-3 Real Sociedad, 0-0 Athletic, 1-2 Villarreal); ostatnio 1-0 wygrana w Elche (01.11). Real Madryt 3., 9W-0D-2L, 28-10; pięć wygranych z rzędu (m.in. 2-1 w Barcelonie 25.10, 3-0 w Racing 01.11, 4-1 Sevilla, 1-0 Villarreal); porażki tylko 0-1 w Betis i 1-2 w Atlético; na wyjazdach 4W-0D-2L.
Rozbieżność z rynkiem: pierwotny model dawał RM 71,7% (5,1 pp pod rynkiem); zgodnie z regułą kalibracji nie schodzę pod rynek >5 pp bez konkretów (forma RM świetna, kontuzje nieznane), więc λ_RM = 2.55, p = 75,2%.
H2H: brak danych 2026/27 (potrzebny ostatni sezon - nie sprawdzano).
Ryzyka dwustronne dla faworyta: remis (15%) ORAZ wygrana Valencii (9,5%) - razem ok. 25%; Valencia jest w kryzysie (korekta tylko po stronie underdoga - uwzględniona w niskim λ_V = 0.80, nie obniżam RM); RM może rotować po meczu LM w tygodniu (nie sprawdzano). Składy RM i kontuzje: do potwierdzenia.
Rynek: Pinnacle 11.52 / 6.47 / 1.25, total 3.25 (-106/-108), O2.5 -226, RM TT 2.5 -103/-118, Valencia TT 0.5 over -133.

---
## Ranking pomocniczy (wszystkie rynki, bez kuponów; fair > 1.15)
| # | Mecz | Rynek | p | fair | Pewność | Od czego zależy / kurs rynkowy |
|---|---|---|---|---|---|---|
| 1 | Valencia - RM | 2 (RM wygra) | 75.2% | 1.33 | średnia | składy RM; Pinnacle 1.25, mała przewaga nad rynkiem (brak value) |
| 2 | Valencia - RM | Over 1.5 | 84.7% | 1.18 | średnia (graniczny) | gole RM; kurs rynkowy nieznany, Over 2.5 -226 |
| 3 | Osasuna - Athletic | X2 | 69.5% | 1.44 | średnia | składy Athletic; kurs nieznany |
| 4 | Osasuna - Athletic | Under 3.5 | 81.9% | 1.22 | średnia | gole Osasuny (wariancja) |
| 5 | Espanyol - Deportivo | Under 3.5 | 79.9% | 1.25 | średnia | j.w. |
| 6 | Espanyol - Deportivo | 1X | 69.0% | 1.45 | średnia | remis u Depor |
| 7 | Málaga - Racing | Over 1.5 | 75.1% | 1.33 | średnia | Racing na wyjeździe traci 3.6/mecz; kurs nieznany |
| 8 | Málaga - Racing | BTTS tak | 54.6% | 1.83 | niska/średnia | Málaga słaby atak (0.73), Racing na wyjeździe 0.8 gola |
| 9 | Valencia - RM | Over 2.5 | 65.0% | 1.54 | średnia | zgodne z rynkiem 65.8% |

Wyniki wyrównane (brak mocnego typu na 1X2): Málaga - Racing, Espanyol - Deportivo, Osasuna - Athletic (najlepiej X2/2, ale p < 50% dla samego 2). Rożne i kartki: bez rekomendacji (brak statystyk drużyn i sędziów, tylko średnie ligowe).

Wszystkie liczby to oszacowania probabilistyczne, nie gwarancje.

---

# Serie A, 11. kolejka, sobota 07.11.2026 (czas PL): analiza 4 meczów

Metoda: λ z goli/mecz (tabela ESPN, 10 meczów, skurczone ~35% do średniej ligi 1,57 gola na drużynę) skorygowane o składy i zblendowane z linią Pinnacle po usunięciu marży. Rozkłady: `poisson.py`, `markets.py`. To oszacowania probabilistyczne, nie gwarancje.

## Potwierdzenie par i godzin (dwa źródła)
| Mecz | ESPN (UTC -> PL) | Pinnacle | Dodatkowo |
|---|---|---|---|
| Cagliari - Frosinone | 14:00Z = 15:00 | 14:00Z | Lega/Diretta/Fantacalcio: 15:00 |
| Torino - Lecce | 14:00Z = 15:00 | 14:00Z | Diretta, Eurosport: 15:00 (Sky podaje 18:00, błąd/odstępstwo) |
| Parma - Bologna | 17:00Z = 18:00 | 17:00Z | Diretta: 18:00 |
| AS Roma - Sassuolo | 19:45Z = 20:45 | 19:45Z | Diretta: 20:45 |

Pary i godziny zgodne z zapytaniem. Sędziowie (Diretta, Fantacalcio): Ayroldi, Feliciani, Zufferli, Di Bello.

## Kontekst tabeli (ESPN, po 10 kolejkach)
Roma 3. (24 pkt, 28-10, bez porażki), Frosinone 6. (20 pkt, 24-14), Bologna 9. (14 pkt), Torino 10. (13), Cagliari 12. (13 pkt, 9-15), Lecce 14. (9 pkt, 11-21), Parma 15. (8 pkt, 8-15), Sassuolo 17. (8 pkt, 16-26). Liga strzela ok. 3,15 gola/mecz (wysoko). Brak podziału dom/wyjazd i xG w źródłach, więc λ mają niższą precyzję.

## Rożne i kartki: ograniczenia danych
- Brak średnich rożnych per drużyna (PianetaFanta bez wartości w wyniku wyszukiwania). Wiadomo tylko, że po zmianie przepisów w sezonie 2026/27 rośnie liczba rożnych (więcej meczów >15). Średnie rożnych to szkic z poziomu ligi: **pewność niska, bez typu na kupon**.
- Kartki: średnia ligi 2026/27 ok. 3,7 żółtych/mecz (Pianetafanta: dom 1,5, wyjazd 2,2), mniej niż w poprzednich sezonach (nowa polityka Orsato). Statystyk kartek konkretnych sędziów (Ayroldi, Feliciani, Zufferli, Di Bello) nie znalazłem, więc liczę ze średnią ligową z drobną korektą stawki: **pewność niska**. Kartki liczone jako żółta = 1.
- Kursy bukmacherów (Betclic) niepobrane; jako odniesienie Pinnacle (bez marży), rożne i kartki bez linii rynkowych.

---

## 1. Cagliari - Frosinone (15:00, Sardegna Arena), sędzia Ayroldi
λ: 1,45 / 1,80 (model własny 1,14/1,90, rynek ok. 1,55/1,75; zblendowane, bo rynek zna braki lepiej niż 10 meczów).

| Rynek | p | fair | Rynek Pinnacle (bez marży) | Pewność |
|---|---|---|---|---|
| 1 / X / 2 | 31,2 / 22,9 / 46,0% | 3,21 / 4,37 / 2,18 | 31,4 / 25,3 / 43,3% | niska (wyrównany, brak mocnego typu) |
| 1X | 54,1% | 1,85 | | niska |
| X2 | 68,9% | 1,45 | | średnia |
| Over 1,5 | 83,5% | 1,20 | | średnia (graniczny fair 1,15-1,20) |
| Over 2,5 / Under 2,5 | 63,0 / 37,0% | 1,59 / 2,71 | O2,5 ok. 65% | średnia |
| Over 3,5 | 40,9% | 2,45 | linia główna 3,25 | niska |
| BTTS tak / nie | 63,9 / 36,1% | 1,57 / 2,77 | | średnia |
| Rożne (śr. 10,3) | O9,5 56% / O10,5 45% / U11,5 65% | 1,78 / 2,22 / 1,53 | brak linii | niska |
| Kartki (śr. 4,0) | O3,5 54% / O4,5 37% | 1,86 / 2,70 | brak linii | niska |

Najlepszy rynek: Over 2,5 lub BTTS tak (oba ~63-64%), Frosinone nie ma przewagi na tyle dużej, by pewnie typować 1X2.

Składy / do potwierdzenia (Sky, Eurosport, 06.11): Cagliari: zawieszony Obert; kontuzje Idrissi, Felici, Nzola (uraz mięśnia), Fadera; Aurelio zagrożony (przemęczenie). Ofensywa Cagliari osłabiona (Mendy/Maldini z przodu), 4-3-2-1. Frosinone: kontuzje Grillitsch i Raimondo (napastnik; gra Birligea), 4-2-3-1, wybór środkowego obrońcy (Monterisi/Cittadini).
Statystyki: Cagliari 0,9 gola strzela i 1,5 traci na mecz (słaby atak), Frosinone 2,4 strzela, 1,4 traci. Frosinone to beniaminek na 6. miejscu, więc forma jest już w kursie.
Ryzyka: Cagliari u siebie po braku napastników bez goli (Under/0-1), Frosinone gubi punkty w trasie przy remisie; BTTS nie, jeśli Cagliari nie trafi (λ gosp. bez Nzoli i Fadery może być bliżej 1,1). H2H: brak świeżych danych (kluby długo w różnych ligach), nie ważone.

## 2. Torino - Lecce (15:00), sędzia Feliciani
λ: 1,65 / 1,10 (model własny 1,92/1,19 vs rynek 1,5/1,05; zblendowane).

| Rynek | p | fair | Rynek Pinnacle (bez marży) | Pewność |
|---|---|---|---|---|
| 1 / X / 2 | 50,2 / 24,5 / 25,4% | 1,99 / 4,09 / 3,94 | 52,5 / 26,6 / 21,0% | średnia (Torino fav, Lecce +4 pp vs rynek) |
| 1X | 74,7% | 1,34 | | średnia |
| X2 | 49,9% | 2,00 | | niska |
| Over 1,5 | 76,0% | 1,32 | | średnia |
| Over 2,5 / Under 2,5 | 51,9 / 48,1% | 1,93 / 2,08 | ok. 50 / 50% | brak mocnego typu |
| Under 3,5 | 70,3% | 1,42 | | średnia |
| BTTS tak / nie | 53,9 / 46,1% | 1,86 / 2,17 | | niska |
| Rożne (śr. 10,0) | O9,5 53% / O10,5 42% | 1,89 / 2,40 | brak linii | niska |
| Kartki (śr. 3,8) | O3,5 50% / O4,5 34% | 1,99 / 2,98 | brak linii | niska |

Najlepszy rynek: 1X (74,7%, fair 1,34) lub Under 3,5.

Składy: Torino 3-5-2: kontuzje Fortini, Rodriguez; Mandragora wątpliwy, Cacciamani prawdopodobnie wraca (Patterson faworytem na lewą stronę), Adams/Simeone z przodu. Lecce 4-3-3: kontuzje Ilic, Berisha, Pierotti, Geubbels, Monteiro (5 absencji, w tym w ataku); Gorter z kontuzją, ale ma grać; Coulibaly wraca; Stulic vs Esteban w ataku.
Statystyki: Torino 1,4 strzela/1,6 traci, Lecce 1,1/2,1 (najgorsza obrona obok Sassuolo i Venezii; 7 porażek w 10).
Ryzyka: remis (Lecce w kursie rynku dostaje mniej niż u mnie, ale Torino ma słabą ofensywę), wygrana Lecce po kontrze. Dla Torino nie podnosiłem p za formę (ujęta w kursie), tylko za braki Lecce.

## 3. Parma - Bologna (18:00), sędzia Zufferli
λ: 0,88 / 1,50 (model własny 1,03/1,32, rynek ok. 0,9/1,5; zblendowane, nie schodzę pod rynek).

| Rynek | p | fair | Rynek Pinnacle (bez marży) | Pewność |
|---|---|---|---|---|
| 1 / X / 2 | 22,1 / 26,1 / 51,8% | 4,53 / 3,82 / 1,93 | 18,5 / 26,1 / 55,4% | średnia (Bologna fav, -3,6 pp vs rynek) |
| 1X | 48,2% | 2,07 | | niska |
| X2 | 77,9% | 1,28 | | średnia-wysoka |
| Over 1,5 | 68,7% | 1,46 | | średnia |
| Under 2,5 | 55,0% (O2,5 45,0%) | 1,82 / 2,22 | rynek O2,5 ok. 48,5% | niska (dopasowano do rynku, bez przewagi) |
| Under 3,5 | 78,3% | 1,28 | | średnia |
| BTTS tak / nie | 45,5 / 54,5% | 2,20 / 1,83 | | niska |
| Rożne (śr. 10,3) | O9,5 56% / O10,5 45% | 1,78 / 2,22 | brak linii | niska |
| Kartki (śr. 3,8) | O3,5 50% / O4,5 34% | 1,99 / 2,98 | brak linii | niska |

Najlepszy rynek: X2 (Bologna lub remis), ew. Under 3,5; zwycięstwo Bologny ~52% to za mało na mocny typ.

Składy: Parma 3-4-2-1: kontuzje Bernabé, Drobnic; Romero ma zaczynać z ławki; Lontani/Touré z przodu (słaby atak: 0,8 gola/mecz). Bologna 3-4-2-1: kontuzje Holm, De Silvestri, Enem; Piccoli wraca po urazie (konkuruje z Odgaardem), Skorupski w bramce. Statystyki: Parma 8 pkt, 8-15 w bramkach; Bologna 14 pkt, 14-13.
Ryzyka: Parma w kryzysie/walce o utrzymanie nie ma "korekty kryzysowej" na faworyta (dotyczy tylko underdoga, tu Parma ma 4 mecze bez dużej liczby goli); remis (26%) i wygrana Parmy (22%) to podobne scenariusze porażki typu na Bolognę.

## 4. AS Roma - Sassuolo (20:45, Olimpico), sędzia Di Bello
λ: 2,65 / 1,05 (model własny 3,65/1,13 ucięty do rynku ok. 2,55/1,0; absencje Roma i Berardi po stronie gości).

| Rynek | p | fair | Rynek Pinnacle (bez marży) | Pewność |
|---|---|---|---|---|
| 1 / X / 2 | 71,4 / 15,9 / 12,7% | 1,40 / 6,29 / 7,89 | 74,4 / 15,5 / 10,2% | wysoka-średnia |
| 1X | 87,3% | 1,15 | | wysoka (fair graniczny 1,15) |
| 12 | 84,1% | 1,19 | | wysoka (graniczny 1,15-1,20) |
| Over 1,5 | 88,4% | 1,13 | | wysoka, ale fair <1,15 (do pominięcia w rankingu) |
| Over 2,5 / Under 2,5 | 71,5 / 28,5% | 1,40 / 3,50 | ok. 69% | średnia-wysoka |
| Over 3,5 | 50,6% | 1,98 | linia główna 3,5, ok. 50% | brak mocnego typu |
| BTTS tak / nie | 60,4 / 39,6% | 1,66 / 2,53 | | średnia |
| Roma Over 1,5 gola | ok. 79% | ok. 1,27 | rynek ok. 76% | średnia-wysoka |
| Rożne (śr. 11,5; Roma dominuje) | O10,5 58% / O11,5 47% | 1,72 / 2,11 | brak linii | niska |
| Kartki (śr. 3,6) | O3,5 46% / U3,5 54% | 2,15 / 1,87 | brak linii | niska |

Najlepszy rynek: Roma wygra (fair 1,40) lub Over 2,5 (fair 1,40); opcja zachowawcza 1X (fair 1,15).

Składy: Roma 3-4-2-1 (Gasperini): kontuzje Svilar, Pellegrini, Dybala (niewyleczony), Koné, Rensch (ok. 20 dni); bramkarz niepewny: Vasquez vs Gollini (Gasperini: "Non lo so, vediamo"); Malen sam z przodu, Soulé i Mora za nim. Sassuolo 3-4-2-1: kontuzje Koné (wg Sky; prawdopodobnie błąd źródła, pojawia się też przy Romie), Leysen, Boloca; Berardi ma wypaść (Eurosport: out, Sky: silne ryzyko); Thorstvedt wraca; Esposito przed Bowiem.
Statystyki: Roma 2,8 gola/mecz, traci 1,0, 10 meczów bez porażki; Sassuolo traci 2,6 (najgorsza obrona w lidze), strzela 1,6.
Ryzyka: remis i wygrana Sassuolo (łącznie ~28%): rezerwowy bramkarz Romy, brak Dybali i Koné, rotacja; Berardi poza grą obniża λ gości do ok. 1,05 (zmiana liczby, nie tylko opis). Duża różnica klas: rynek bywa trafniejszy, więc nie schodzę poniżej rynku.

---

## Kandydaci (bez budowania kuponów)
| Mecz | Rynek | p | fair | Pewność | Zależy od |
|---|---|---|---|---|---|
| Roma - Sassuolo | Roma wygra | 71,4% | 1,40 | wysoka-średnia | bramkarz Romy, Berardi |
| Roma - Sassuolo | Over 2,5 | 71,5% | 1,40 | średnia-wysoka | j.w. |
| Roma - Sassuolo | 1X | 87,3% | 1,15 | wysoka | graniczny fair |
| Parma - Bologna | X2 | 77,9% | 1,28 | średnia-wysoka | skład Bologny (Piccoli/Odgaard) |
| Torino - Lecce | 1X | 74,7% | 1,34 | średnia | Mandragora/Cacciamani |
| Torino - Lecce | Under 3,5 | 70,3% | 1,42 | średnia | |
| Cagliari - Frosinone | Over 2,5 | 63,0% | 1,59 | średnia | ofensywa Cagliari bez Nzoli/Fadery |
| Cagliari - Frosinone | BTTS tak | 63,9% | 1,57 | średnia | |

Rożne i kartki: brak linii i słabe dane, nie rekomenduję. Przed kuponem sprawdzić oficjalne składy ok. 1 h przed meczem (zwłaszcza bramkarz Romy, Berardi, Mandragora, Aurelio) oraz kursy Betclic.

---

# Analiza Bundesliga, 9. kolejka, sobota 07.11.2026 (czas PL)

Bez kuponów. Oszacowania probabilistyczne, nie gwarancje. Skrypty: `poisson.py` (1X2, O/U, BTTS), `markets.py` (kartki, rożne).

## Potwierdzenie par i godzin (3 źródła)
| Mecz | OpenLigaDB | Pinnacle (UTC) | bundesliga.com / t-online |
|---|---|---|---|
| Dortmund - Elversberg | 07.11 15:30 | 14:30Z = 15:30 | 14:30 UTC / 15:30, Signal Iduna Park |
| Mainz - Bayern | 07.11 15:30 | 14:30Z | 15:30 |
| Leipzig - Augsburg | 07.11 15:30 | 14:30Z | 15:30 |
| Paderborn - Frankfurt | 07.11 15:30 | 14:30Z | 15:30 |
| Stuttgart - Werder | 07.11 18:30 | 17:30Z = 18:30 | 18:30 |

Wszystkie pary i godziny zgodne. Uwaga: rekordy OpenLigaDB mają stary `lastUpdate` (lipiec/wrzesień), ale zgadzają się z Pinnacle i bundesliga.com.

## Metoda i dane
- Wyniki 73 rozegranych meczów sezonu 2026/27 (OpenLigaDB): średnio 3,51 gola/mecz (gospodarze 2,14, goście 1,37). To liga bardzo bramkowa, rynek (Pinnacle) wycenia totaly 3,3-4,0.
- λ = mieszanka modelu statystycznego (siła ataku/obrony z 8 kolejek, shrinkage 55%) i λ dopasowanych do kursów Pinnacle bez marży (zgodnie z regułą: nie schodzić pod rynek o >5 pp bez konkretów). Rynek ma większą wagę, bo 8 meczów to mała próba.
- Kursy: Pinnacle (MCP), przeliczone na dziesiętne; marża 1X2 ok. 3-4%. Betclic/gg397 nie sprawdzano. BettingPros pominięty (brak klucza w tej sesji).
- **Sędziowie: nie ogłoszeni/nieznalezieni dla żadnego meczu** (bundesliga.com, t-online, DFB bez obsady; kicker 403). Kartki liczone ze średnich drużyn i ligi (łącznie 270 kartek / 144 mecze drużynowe = 3,75/mecz), pewność niska.
- **Rożne: brak danych drużynowych** (bundesliga.com nie pokazuje, Pinnacle bez rynku rożnych). Średnie to priory ligowe (~10) skorygowane o układ sił, pewność niska, nie rekomenduję.
- Kartki własne na mecz (8 kolejek, żółte+czerwone, bundesliga.com): Dortmund 2,1; Elversberg 1,75; Mainz 2,5; Bayern 1,0; Leipzig 0,9; Augsburg 1,5; Paderborn 1,5; Frankfurt 2,25; Stuttgart 1,5; Werder 1,4.

---
## 1. Borussia Dortmund - SV Elversberg (15:30)
λ 2,40 / 1,05 (rynek: 2,57 / 0,98; model stat.: 2,16 / 1,11). Typ: **wygrana Dortmundu 67%, pewność średnia**.

| Rynek | p | fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 67,2 / 17,9 / 14,9% | 1,49 / 5,60 / 6,70 | średnia |
| DC 1X / X2 / 12 | 85,1 / 32,8 / 82,1% | 1,18 / 3,05 / 1,22 | średnia |
| Over / Under 1,5 | 85,9 / 14,1% | 1,16 / 7,08 | średnia (graniczne 1,15-1,20) |
| Over / Under 2,5 | 67,0 / 33,0% | 1,49 / 3,03 | średnia |
| Over / Under 3,5 | 45,3 / 54,7% | 2,21 / 1,83 | niska |
| BTTS tak / nie | 59,1 / 40,9% | 1,69 / 2,45 | średnia |
| Rożne (śr. 10,5) O/U 9,5 | 58,4 / 41,6% | 1,71 / 2,40 | niska |
| Rożne O/U 10,5 | 47,2 / 52,8% | 2,12 / 1,89 | niska |
| Kartki (śr. 3,7) O/U 3,5 | 48,4 / 51,6% | 2,07 / 1,94 | niska |
| Kartki O/U 4,5 | 31,9 / 68,1% | 3,13 / 1,47 | niska |

- Rynek Pinnacle: 1 / X / 2 = 1,35 / 5,82 / 8,22 (bez marży 71,6 / 16,6 / 11,8%). Moje 67,2% jest 4,4 pp pod rynkiem (różnica za Guirassy'ego, patrz niżej). Total 3,5 ok. 50/50, O2,5 alt. 1,37.
- Statystyki: BVB 5W 3R 0P, 14:6 (najlepsza obrona ligi), ostatnio 2:2 z Bayernem, 1:0 z Frankfurtem, 0:0 z Unionem. Elversberg 4W 1R 3P, 16:16, ostatnio 4:1 z Mainz, 0:4 w Lipsku, 4:3 z Augsburgiem; mecze Elversberg średnio 4 gole.
- H2H: brak meczów ligowych (jedyny: Puchar 1981, BVB 4:1). Weight zerowy.
- Media: **Guirassy nie zagra** (udo, uraz w CL z Betis; bundesliga.com, getfootballnewsgermany). Przewidywany skład BVB 3-4-2-1: Kobel; Schlotterbeck, Anton, Gadou; Beier, Nmecha, J. Bellingham, Ryerson; Chukwuemeka, Karetsas; Silva (niepotwierdzony; skład ok. 60 min przed meczem). Elversberg bez zgłoszonych absencji. Mecz po meczu CL (zmęczenie/rotacja), do 8 tys. kibiców gości.
- Ryzyka: remis (ok. 18%) i niespodzianka Elversberg (ok. 15%; drużyna strzela dużo i dobrze gra na wyjeździe). Rotacja po CL, brak Guirassy'ego obniża p wygranej o ok. 3 pp wobec rynku. Elversberg ofensywnie zagraża, więc BTTS ok. 59%.
- Do potwierdzenia: skład BVB (Guirassy out, Can/Nmecha), sędzia.

---
## 2. Mainz - Bayern Monachium (15:30)
λ 1,15 / 2,85 (rynek: 1,11 / 2,94; model stat.: 1,71 / 2,53). Typ: **wygrana Bayernu 72,5%, pewność średnia**.

| Rynek | p | fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 12,6 / 15,0 / 72,5% | 7,95 / 6,68 / 1,38 | średnia |
| DC 1X / X2 / 12 | 27,6 / 87,5 / 85,0% | 3,62 / 1,14 / 1,18 | średnia (X2 poniżej 1,15, pomijać) |
| Over / Under 1,5 | 90,8 / 9,2% | 1,10 / 10,9 | wysoka, ale fair <1,15 |
| Over / Under 2,5 | 76,2 / 23,8% | 1,31 / 4,20 | średnia |
| Over / Under 3,5 | 56,6 / 43,4% | 1,77 / 2,31 | niska-średnia |
| BTTS tak / nie | 64,4 / 35,6% | 1,55 / 2,81 | średnia |
| Rożne (śr. 10,8) O/U 10,5 | 50,5 / 49,5% | 1,98 / 2,02 | niska |
| Rożne O/U 9,5 | 61,5 / 38,5% | 1,63 / 2,60 | niska |
| Kartki (śr. 3,6) O/U 3,5 | 46,5 / 53,5% | 2,15 / 1,87 | niska |
| Kartki O/U 4,5 | 30,3 / 69,7% | 3,30 / 1,43 | niska |

- Rynek Pinnacle: 8,61 / 6,70 / 1,29 (bez marży 11,2 / 14,3 / 74,5%). Total główny 4,0 (O/U ok. 50/50), O3,5 = 1,59, O2,5 przy linii 3,0 = 1,29. Zgodne z modelem w granicach 2-3 pp.
- Statystyki: Bayern 5W 3R, 27:8 (6:1 z Lipskiem, 7:0 z Unionem), ostatnio 2:2 z BVB. Mainz 3W 1R 4P, 17:17, wygrał tylko 1 z ostatnich 5 (wg Yahoo przegrał 4 z 5, nie wygrał u siebie w sezonie), ostatnio 1:4 w Elversberg, 2:3 z Werderem.
- H2H: brak świeżych danych w researchu, waga niska.
- Media (Yahoo Sports, artykuł z niespójną datą w treści, potraktować jako umiarkowanie pewne): **Mainz bez Posha (czerwona) i Mwene (kartki), kontuzje Kohr, Silas**; Ruoppi wraca. **Bayern bez Musiali, Diaza, Gnabry'ego, Saibariego, Ndiaye (5 graczy ofensywy), Kompany chory, prowadzi asystent Danks**; Neuer zdrowy; Pavlović pod znakiem zapytania, Davies z ograniczonymi minutami. Prognozowany skład Bayernu: Neuer; Laimer, Upamecano, Kim, Brown; Kimmich, Pavlović; Olise, Karl, Davies; Kane.
- Ryzyka (oba kierunki): remis (15%) i wygrana Mainz (12,6%): Mainz w osłabionej obronie, ale Bayern bez 5 ofensywnych graczy i z trenerem pod chorobą; mecz wyjazdowy po CL. Absencje w obu drużynach częściowo się znoszą, dlatego trzymam się rynku.
- Do potwierdzenia: Kane/Pavlović/Davies, skład Mainz (Posch/Mwene out), sędzia.

---
## 3. RB Leipzig - FC Augsburg (15:30)
λ 2,55 / 1,20 (rynek: 2,60 / 1,25; model stat.: 2,73 / 1,53). Typ: **wygrana Lipska 66,6%, pewność średnia**.

| Rynek | p | fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 66,6 / 17,3 / 16,1% | 1,50 / 5,77 / 6,22 | średnia |
| DC 1X / X2 / 12 | 83,9 / 33,4 / 82,7% | 1,19 / 2,99 / 1,21 | średnia |
| Over / Under 1,5 | 88,8 / 11,2% | 1,13 / 8,95 | wysoka, fair <1,15 |
| Over / Under 2,5 | 72,3 / 27,7% | 1,38 / 3,61 | średnia |
| Over / Under 3,5 | 51,6 / 48,4% | 1,94 / 2,07 | niska |
| BTTS tak / nie | 64,4 / 35,6% | 1,55 / 2,81 | niska-średnia |
| Rożne (śr. 10,6) O/U 9,5 | 59,4 / 40,6% | 1,68 / 2,46 | niska |
| Rożne O/U 10,5 | 48,3 / 51,7% | 2,07 / 1,94 | niska |
| Kartki (śr. 3,2) O/U 2,5 | 58,3 / 41,7% | 1,72 / 2,40 | niska |
| Kartki O/U 3,5 | 39,0 / 61,0% | 2,57 / 1,64 | niska |

- Rynek Pinnacle: 1,46 / 5,37 / 6,07 (bez marży 66,1 / 18,0 / 15,9%) - moje p praktycznie równe. Total 3,75; O2,75 = 1,29.
- Statystyki: Leipzig 5W 3P, 22:11, **u siebie 4/4 wygranych, bilans bramek 18:0**; ostatnio 4:0 Elversberg, 2:0 Schalke (wyjazd), 3:2 przegrany z City w CL (wtorek/środa). Augsburg 2W 3R 3P, 18:15, bez wygranej w 6 meczach, ostatnio 1:2 z Freiburgiem; Gregoritsch 5 goli (rekord klubowy po 8 meczach), Augsburg strzela dużo (4:3 w Elversberg), ale traci 1,9/mecz.
- H2H: poprzedni sezon, 25. kolejka Leipzig 2:1 (samobój w doliczonym czasie); bbez dłuższej serii.
- Media: przewidywane składy (bundesliga.com) - Leipzig 4-2-3-1 z Nkunku, Baumgartner, Gomis; Augsburg 3-4-2-1 z Gregoritschem. Brak znalezionych informacji o absencjach obu drużyn (nie znaczy, że ich nie ma). Trener Leipzigu: Demichelis.
- Ryzyka: Augsburg bardzo wysoki sprint-pressing i skuteczny Gregoritsch (wygrana Augsburga 16%); remis 17%. Leipzig po meczu CL (rotacja/zmęczenie). BTTS niższe niż model, jeśli Leipzig dalej nie traci u siebie (0 straconych w 4 domowych), ale próba mała; dlatego pewność niska-średnia.
- Do potwierdzenia: skład Leipzigu po CL, absencje, sędzia.

---
## 4. SC Paderborn - Eintracht Frankfurt (15:30)
λ 1,40 / 1,60 (rynek: 1,55 / 1,75; model stat.: 1,59 / 1,16). **Mecz wyrównany, brak mocnego typu w wyniku.**

| Rynek | p | fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 33,5 / 24,2 / 42,3% | 2,98 / 4,14 / 2,36 | niska |
| DC 1X / X2 / 12 | 57,7 / 66,5 / 75,8% | 1,73 / 1,50 / 1,32 | niska-średnia |
| Over / Under 1,5 | 80,1 / 19,9% | 1,25 / 5,02 | średnia |
| Over / Under 2,5 | 57,7 / 42,3% | 1,73 / 2,36 | niska |
| Over / Under 3,5 | 35,3 / 64,7% | 2,83 / 1,55 | niska-średnia |
| BTTS tak / nie | 60,1 / 39,9% | 1,66 / 2,51 | niska |
| Rożne (śr. 10,0) O/U 9,5 | 52,8 / 47,2% | 1,89 / 2,12 | niska |
| Kartki (śr. 3,7) O/U 3,5 | 48,4 / 51,6% | 2,07 / 1,94 | niska |
| Kartki O/U 4,5 | 31,9 / 68,1% | 3,13 / 1,47 | niska |

- Rynek Pinnacle: 2,92 / 3,88 / 2,33 (bez marży 33,3 / 25,0 / 41,7%) - 1X2 zgodne z moim modelem. **Rozbieżność na totalu**: Pinnacle total 3,25 (O2,5 = 1,47, ok. 65% bez marży) vs moje O2,5 57,7%: różnica ok. 7 pp. Przyczyna po mojej stronie: Paderborn strzelił 6 goli w 8 meczach (mecze Paderborn średnio 1,6 gola, najniższe w lidze), więc zszedłem z totalem poniżej rynku, ale nie więcej niż to uzasadnia próba. Traktować Over 2,5 / Under 2,5 jako brak przewagi.
- Statystyki: Paderborn 2W 3R 3P, 6:9, 3 mecze bez porażki (0:0 z Gladbach, 1:0 HSV, 2:2 Werder); najsłabszy atak ligi. Frankfurt 3W 2R 3P, 13:18 (6:0 w Lipsku, 4:1 w Augsburgu, 1:0 Köln, 3:1 HSV); Ebnoutalib 6 goli w lidze.
- H2H: ostatnie 2019/20, Frankfurt 3:2 (po 3:0). Waga zerowa.
- Media: przewidywane składy (bundesliga.com): Paderborn (Hütter wspomniał o 5-3-2 z Tigges), Frankfurt 4-4-2 z Burkardtem i Ebnoutalibem; Paderborn nieprzegrywający u siebie. Brak informacji o absencjach. Frankfurt 3-1 z HSV w lidze/Pucharze (artykuł niejednoznaczny).
- Ryzyka: wszystkie trzy wyniki realne; Paderborn zamyka mecze, przy golu Frankfurtu wynik się rozstrzyga. Podwójna szansa X2 (1,50 fair) bez przewagi nad rynkiem.
- Do potwierdzenia: składy, sędzia (Frankfurt 2,25 kartki/mecz, Onyedika 3 żółte).

---
## 5. VfB Stuttgart - Werder Brema (18:30)
λ 2,05 / 1,55 (rynek: 2,09 / 1,46; model stat.: 2,00 / 1,74). **Wyrównany, brak mocnego typu na wynik; najlepszy rynek: Over 2,5 / BTTS.**

| Rynek | p | fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 49,4 / 21,3 / 29,3% | 2,02 / 4,70 / 3,41 | niska |
| DC 1X / X2 / 12 | 70,7 / 50,6 / 78,7% | 1,41 / 1,98 / 1,27 | niska-średnia |
| Over / Under 1,5 | 87,4 / 12,6% | 1,14 / 7,96 | średnia, fair <1,15 |
| Over / Under 2,5 | 69,7 / 30,3% | 1,43 / 3,30 | średnia |
| Over / Under 3,5 | 48,5 / 51,5% | 2,06 / 1,94 | niska |
| BTTS tak / nie | 68,6 / 31,4% | 1,46 / 3,19 | średnia |
| Rożne (śr. 10,2) O/U 9,5 | 55,1 / 44,9% | 1,82 / 2,23 | niska |
| Kartki (śr. 3,4) O/U 3,5 | 42,8 / 57,2% | 2,34 / 1,75 | niska |
| Kartki O/U 4,5 | 27,0 / 73,0% | 3,71 / 1,37 | niska |

- Rynek Pinnacle: 1,885 / 4,21 / 3,78 (bez marży 51,4 / 23,0 / 25,6%), total 3,5 (50/50), O2,5 = 1,37 (ok. 70% bez marży). Moje p w granicach 2-4 pp rynku. Gospodarz u mnie 49,4% (rynek 51,4%) po uwzględnieniu formy Werderu (7 meczów bez porażki).
- Statystyki: Stuttgart 3W 5P, 14:15, ostatnio 4:2 w Leverkusen, ale przegrane 0:1 z HSV i 2:3 z Gladbach; porażka 0:2 z Galatasaray w CL. Werder 4W 3R 1P, 17:14, 7 meczów bez porażki (2:0 Hoffenheim, 3:2 w Mainz, 2:2 z Paderbornem, 2:2 z BVB); Füllkrug strzela w 7 meczach z rzędu (rekord klubowy do wyrównania/poprawienia).
- H2H: poprzednie spotkanie 1:1 (Demirović wyrównał po golu Werderu). Mało danych.
- Media: przewidywane składy (bundesliga.com): Stuttgart 3-4-2-1 (Seimen; Mittelstädt, Chabot, Jaquez; El Khannouss, Undav, Demirović), Werder 4-2-3-1 (Hein; Friedl, Pieper; Füllkrug). Brak informacji o absencjach. Hoeneß: „potrzebny top performance”; Thioune: stawia na zwarte bronienie i stabilność. Stuttgart po meczu CL (zmęczenie), Werder tydzień przerwy.
- Ryzyka: oba mecze dwóch drużyn z dobrym atakiem i dziurawą obroną (Stuttgart traci 1,9/mecz), więc Under 2,5 tylko 30%; porażka u Over przy ostrożnej taktyce Werderu i zwycięstwie 1:0 / 2:0.
- Do potwierdzenia: składy (Undav/Demirović), sędzia.

---
## Podsumowanie rynków z najwyższym p (fair >1,15), do dalszego użycia przez bet-slip-builder
| Mecz | Rynek | p | fair | Pewność | Rynek Pinnacle | Zależy od |
|---|---|---|---|---|---|---|
| Mainz - Bayern | Bayern wygra | 72,5% | 1,38 | średnia | 1,29 (bez marży 74,5%) | skład Bayernu (Kane/Pavlović) |
| Mainz - Bayern | Over 2,5 | 76,2% | 1,31 | średnia | O3,0 = 1,29 | Kane gra; ofensywa Bayernu osłabiona |
| Leipzig - Augsburg | Over 2,5 | 72,3% | 1,38 | średnia | O2,75 = 1,29 | skład Leipzigu po CL |
| Stuttgart - Werder | Over 2,5 | 69,7% | 1,43 | średnia | O2,5 = 1,37 | składy |
| Stuttgart - Werder | BTTS tak | 68,6% | 1,46 | średnia | brak | składy |
| Dortmund - Elversberg | Dortmund wygra | 67,2% | 1,49 | średnia | 1,35 | rotacja po CL, brak Guirassy'ego |
| Dortmund - Elversberg | Over 2,5 | 67,0% | 1,49 | średnia | O2,5 = 1,37 | j.w. |
| Leipzig - Augsburg | Leipzig wygra | 66,6% | 1,50 | średnia | 1,46 | Leipzig po CL |
| Paderborn - Frankfurt | brak mocnego typu | - | - | niska | - | - |

Pominięte (fair ≤1,15): Over 1,5 w kilku meczach (1,10-1,16), X2 Mainz - Bayern (1,14). Granicznie 1,15-1,20: DC 1X Dortmund (1,18), 12 Mainz - Bayern (1,18), Over 1,5 Dortmund (1,16), 1X Leipzig (1,19).

Kartki i rożne: bez sędziów i bez statystyk rożnych (pewność niska), nie rekomenduję do kuponów. Kursy bukmacherów PL (Betclic) nie sprawdzano, tylko Pinnacle.

To są oszacowania probabilistyczne, nie gwarancje.

---

# Analiza: Ligue 1 + Ekstraklasa, sobota 07.11.2026 (czas PL)

Stan wiedzy: sobota 07.11.2026, ok. 08:30 PL. Mecz Korona - Radomiak (12:15) jeszcze się NIE zaczął.

## Potwierdzenie par i godzin (drugie źródło)
| Mecz | Godzina PL | Źródło 1 | Źródło 2 | Status |
|---|---|---|---|---|
| Korona Kielce - Radomiak Radom | 12:15 (EXBUD Arena) | ekstraklasa.org (terminarz 14. kol.) | pilkarskiswiat/gol24 (12:15, Canal+ Sport 3) | potwierdzone |
| Śląsk Wrocław - Piast Gliwice | 14:45 | ekstraklasa.org | mecze24, slasknet | potwierdzone |
| Górnik Zabrze - Wieczysta Kraków | 17:30 | ekstraklasa.org | slasknet, flashscore (para) | potwierdzone |
| Widzew Łódź - Pogoń Szczecin | 20:15 | ekstraklasa.org | weszlo (20:15) | potwierdzone |
| AJ Auxerre - Paris FC | 19:00 (18:00Z) | ESPN (MCP) | brak drugiego; starting11 podaje 17:15 (niespójne, ESPN i zlecenie = 19:00) | para potwierdzona, godzina wg ESPN |
| Paris Saint-Germain - Troyes | 21:05 (20:05Z) | ESPN (MCP) | zgodne ze zleceniem | potwierdzone |

## Metodologia i ograniczenia
- λ z rozkładu Poissona (`poisson.py`), korekty o absencje i rynek (kursy bez marży), kalibracja wg SKILL.md (nie schodzę pod rynek o >5 pp bez konkretów).
- Kursy: Ekstraklasa - przeglądy polskich bukmacherów (Fortuna/STS/LVBET/Betfan/forBET, bez Betclic); Ligue 1 - DraftKings przez ESPN (MCP), przeliczone na dziesiętne. To nie są kursy Betclic.
- BRAK: obsady sędziowskiej (poza Korona - Radomiak: Tomasz Kwiatkowski), potwierdzonych składów, statystyk rożnych/kartek drużyn i sędziów. Rożne i kartki liczone ze średnich ligowych/szkicowych -> pewność NISKA, bez rekomendacji typu na kupon.
- BettingPros: nie używano (brak klucza w sesji).
- Absencje (ekstraklasa.org "Pauzujący i zagrożeni", polskiezf.pl; stan 4-6.11): Korona - Rubezić (kartki); Radomiak - Tapsoba (kartki), Camara (dyskwalifikacja), Szcześniak (ACL, długa); Górnik - Janicki (kartki); Piast - Lewicki (kartki); Pogoń - Cojocaru (czerwona kartka, bramkarz) + kontuzje Mendy, Juwara, Wahlqvist, Ndiaye, Ali; Widzew - Fornalczyk (mięśnie), Czyż, Lerager poza; Wieczysta - Feiertag poza; Śląsk - brak pauzujących.
- Brak informacji o jednej kluczowej rzeczy: mecz 12:15 - składy ogłoszone ok. 11:15, sprawdzić przed meczem.

---

## 1. Korona Kielce - Radomiak Radom (Ekstraklasa 14. kol., 12:15, sędzia: T. Kwiatkowski)
Tabela: Korona 10./11. (18 pkt, bilans 14:19), Radomiak 15. (11 pkt, 15:29). Forma: Korona 1W-4P w 5 (0:1 w Lubinie, pierwsza porażka pod Kolendowiczem), ale tylko 1 porażka u siebie w 12 meczach; ostatnio u siebie traci 0,8, strzela 1,1. Radomiak (trener Carver) pierwsza wygrana 3:1 ze Śląskiem, wcześniej 5 porażek; w 5 meczach 23 gole (4,6/mecz); wyjazd: strzela ~1, traci ~2. H2H: ostatnio 0:2 (02.2026), Korona wygrała 5 z 8. Brak Tapsoby i Camary (obrona) u gości, brak Rubezicia u gospodarzy.
Model: λ 1,65 / 0,95. Rynek 1X2 (Fortuna/STS) 1,65-1,75 / 3,6-3,97 / 4,4-4,66 (bez marży ok. 56/24/20).

| Rynek | p | fair | Pewność | Uwagi |
|---|---|---|---|---|
| 1 Korona | 54% | 1.85 | średnia | rynek 56% |
| X | 24,5% | 4.08 | | |
| 2 Radomiak | 21,5% | 4.65 | | |
| 1X | 78,5% | 1.27 | średnia | główny typ meczu |
| X2 | 46% | 2.17 | niska | |
| Over 1.5 | 73% | 1.37 | średnia | |
| Over 2.5 | 51% | 1.96 | niska | model 48%, rynek ~55% (Fortuna 1.73); średnia z uwagi na gole Radomiaka |
| Under 2.5 | 49% | 2.04 | niska | |
| Under 3.5 | 74% | 1.35 | średnia | |
| BTTS tak | 50% | 2.00 | niska | |
| Rożne O/U 9.5 (śr. 9,8) | 51/49% | 1.98/2.02 | niska | brak danych rożnych |
| Kartki O/U 4.5 (śr. 4,6, sędzia Kwiatkowski bez statystyk) | 47/53% | 2.13/1.89 | niska | |

Ryzyka: remis (24%) i wygrana Radomiaka po odbiciu pod nowym trenerem (21%); skład Korony po porażce; Radomiak strzela dużo, ale też traci. Do potwierdzenia: składy ~11:15, sędzia i jego średnia kartek.

## 2. Śląsk Wrocław - Piast Gliwice (14:45)
Tabela: Śląsk 16. (9 pkt, 17:25), wygrał 1 z 11 ostatnich, traci 2+ gole w 3 z 5; strzela 1,7 u siebie, gola w 12/13 meczów. Piast 8. (21 pkt, 24:20), 17 pkt w 8 meczach, gol w 10 meczach z rzędu, 4 mecze bez porażki na wyjeździe, najwięcej goli po 75' (10). H2H: w ostatnich 5 Piast 2, Śląsk 1, 2 remisy, 2,6 gola/mecz; gol w 25 kolejnych H2H. Brak Lewickiego (kartki) u Piasta; Shabani zagrożony. Rynek 1X2: 2,40-2,51 / 3,3-3,6 / 2,55-2,70 (ok. 38/26/36).
Model λ 1,35 / 1,30 (z korektą na BTTS 1,4/1,35).

| Rynek | p | fair | Pewność | Uwagi |
|---|---|---|---|---|
| 1 Śląsk | 38% | 2.63 | niska | wyrównany |
| X | 26% | 3.85 | | |
| 2 Piast | 36% | 2.78 | niska | |
| 1X | 64% | 1.56 | niska | |
| X2 | 62% | 1.61 | niska | rynek 1.47 (Superbet) = 68%, nie schodzę pod rynek >5pp |
| 12 | 74% | 1.35 | średnia | |
| Over 1.5 | 74% | 1.35 | średnia | |
| Over 2.5 | 50% | 2.00 | niska | |
| BTTS tak | 57% | 1.75 | niska-średnia | rynek STS 1.52 (66%); model 54%, podniesione o formę (Piast gol 10 z rz., Śląsk gol 12/13, obaj tracą) |
| Rożne O/U 9.5 (śr. 9,8) | 51/49% | | niska | brak danych |
| Kartki O/U 4.5 (śr. 4,6) | 47/53% | 2.13/1.89 | niska | sędzia nieznany |

Brak mocnego typu wynikowego. Ryzyka: Śląsk po "nowym otwarciu" (trener/porażka 1:3 z Radomiakiem) vs Piast w formie; skład Piasta bez Lewickiego. Do potwierdzenia: składy, sędzia.

## 3. Górnik Zabrze - Wieczysta Kraków (17:30)
Tabela: Górnik 2. (28 pkt w 13, 21:11, najmniej straconych 0,85/mecz), ale 4 remisy w 5 ostatnich (2W-3R, bez porażki w 5); u siebie ostatnie 10: strzela 1,3, traci 1,4. Wieczysta 18. (8 pkt, 17:26), 4 porażki z rzędu; wyjazd ostatnie 10: strzela 1,6, traci 2,2; dominuje w posiadaniu, 5 ostatnich goli z ławki. Brak Janickiego (kartki, stoper) u Górnika; Szcześniak (kontuzja) według przeglądu - Szcześniak Radomiak/Górnik rozbieżność źródeł, niepotwierdzone. Rynek 1X2: 1,53-1,59 / 4,0-4,4 / 5,0-5,4 (bez marży ok. 61/22/17), O2.5 ~1,58-1,62, BTTS ~1,62-1,67.
Model λ 1,75 / 1,0 (55/23,5/21,5), moje p podniesione do 58% (model był o 6 pp pod rynkiem, a konkretów obniżających Górnika jest mało; Janicki to jeden stoper).

| Rynek | p | fair | Pewność | Uwagi |
|---|---|---|---|---|
| 1 Górnik | 58% | 1.72 | średnia | rynek 61% (1.56) |
| X | 23% | 4.35 | | |
| 2 Wieczysta | 19% | 5.26 | | |
| 1X | 81% | 1.23 | średnia | |
| Handicap Górnik -1.5 | 31% | 3.2 | niska | |
| Over 1.5 | 76% | 1.32 | średnia | |
| Over 2.5 | 54% | 1.85 | niska | rynek ~60% |
| Under 3.5 | 71% | 1.41 | średnia | rynek 1.52 = 62% |
| BTTS tak | 53% | 1.89 | niska | rynek ~58% |
| Rożne O/U 9.5 (śr. 10,2, Górnik dominuje) | 55/45% | | niska | brak danych |
| Kartki O/U 4.5 (śr. 4,4) | 44/56% | 2.29/1.78 | niska | |

Ryzyka: remis (Górnik remisuje - 4 z ostatnich 5), wygrana Wieczystej mało prawdopodobna (19%); wysoka dominancja gospodarzy nie gwarantuje wyniku (Gąsparik, remisy).

## 4. Widzew Łódź - Pogoń Szczecin (20:15)
Tabela: Widzew 14. (11 pkt, 1W-8R-4P; bez zwycięstwa w 10, 4 ostatnie domowe remisy, żadnej wygranej u siebie; stracił w 10 z 12 meczów; 2:3 w Katowicach). Pogoń 4. (24 pkt w 12, 20:12), przegrała 1:3 z Rakowem po 7 meczach bez porażki, gol w 9 meczach z rz. H2H: Pogoń 25 pkt z 27 w 9 meczach (ostatnie 6 wygrane, 0:4 i 1:0 w 2025/26); bez wagi pełnej (inne składy/trenerzy). Pogoń bez Cojocaru (czerwona kartka, bramkarz) i z listą kontuzji (Mendy, Juwara, Wahlqvist, Ndiaye, Ali). Widzew: Fornalczyk wątpliwy, Czyż, Lerager poza; 5 zagrożonych kartką. Rynek (LVBET): 2,20 / 3,85 / 3,05 (bez marży 44/25/31); O2.5 1,77; BTTS 1,67.
Model λ 1,2 / 1,25 (35/27/38); moje p skompromitowane z rynkiem: gospodarz nie niżej niż -4 pp (H2H to silny sygnał, ale stare składy; konkret: zmiana bramkarza Pogoni i kontuzje).

| Rynek | p | fair | Pewność | Uwagi |
|---|---|---|---|---|
| 1 Widzew | 40% | 2.50 | niska | rynek 44% |
| X | 27% | 3.70 | niska | Widzew remisuje najczęściej w lidze |
| 2 Pogoń | 33% | 3.03 | niska | rynek 31% |
| 1X | 67% | 1.49 | niska-średnia | |
| X2 | 60% | 1.67 | niska | |
| Over 1.5 | 71% | 1.41 | średnia | |
| Over 2.5 | 47% | 2.13 | niska | rynek 1.77 (~54%) |
| Under 3.5 | 76% | 1.32 | średnia | |
| BTTS tak | 56% | 1.79 | niska-średnia | rynek 1.62-1.67; Widzew traci w 10/12, Pogoń trafia 9 z rz. |
| Rożne O/U 9.5 (śr. 9,8) | 51/49% | | niska | brak danych |
| Kartki O/U 4.5 (śr. 4,8, 5 zagrożonych Widzewa) | 49/51% | | niska | sędzia nieznany |

Brak mocnego typu: mecz wyrównany (blisko 40/27/33). Najbezpieczniejszy kierunek: BTTS / Over 1.5. Ryzyka: Widzew bez wygranej u siebie vs Pogoń osłabiona w bramce i obronie.

## 5. AJ Auxerre - Paris FC (Ligue 1, 19:00, Stade de l'Abbé-Deschamps)
Tabela (ESPN): Paris FC 4. (17 pkt, 16:10; forma WLWLW, 5-2-2), Auxerre 14. (10 pkt, 13:23 - najgorsza obrona poza top 4 od końca, 2,56 straconego/mecz; forma LDWLW, 3-1-5). Strzelcy: Sinayoko (PFC) 8, Archer (AUX) 6. Rynek (DraftKings): Auxerre 4.60 / X 4.10 / Paris FC 1.71 (bez marży ok. 21/23/56), O2.5 1.69 / U2.5 2.15; handicap Paris FC -0,5 1.65.
Model (Auxerre 1,1 / Paris FC 1,65): 25/24,5/50, rynek 56%; biorę 53% (obniżam o 3 pp wyłącznie za mały domowy atut Auxerre; brak konkretów kadrowych, więc nie schodzę dalej).
Brak informacji o składach, kontuzjach i sędzi (nie znaleziono) - pewność maks. średnia.

| Rynek | p | fair | Pewność | Uwagi |
|---|---|---|---|---|
| 1 Auxerre | 23% | 4.35 | | |
| X | 24% | 4.17 | | |
| 2 Paris FC | 53% | 1.89 | średnia | rynek 1.71 |
| 1X | 47% | 2.13 | niska | |
| X2 | 77% | 1.30 | średnia | |
| Over 1.5 | 77% | 1.30 | średnia | |
| Over 2.5 | 54% | 1.85 | niska-średnia | rynek 1.69 (56-59%) |
| BTTS tak | 55% | 1.82 | niska-średnia | Auxerre traci 2,56/mecz, ale strzela tylko 1,4 |
| Rożne O/U 9.5 (śr. 10,4) | 57/43% | 1.75/2.34 | niska | |
| Kartki O/U 3.5 (śr. 4,0) | 54/46% | 1.86/2.16 | niska | |

Ryzyka: remis (24%) i wygrana Auxerre (23%) - gospodarze nie przegrali we wszystkich meczach; bez składów. Uwaga: różnica godzin w starting11 (17:15) to najpewniej błąd, godzinę trzymam wg ESPN (19:00).

## 6. Paris Saint-Germain - Troyes (Ligue 1, 21:05, Parc des Princes)
Tabela (ESPN): PSG 1. (20 pkt, 21:10; forma WWWWW), Troyes 16. (8 pkt, 7:16; forma WDLLL, 2-2-5; strzela 0,78/mecz). Rynek (DraftKings): PSG 1.14 / X 9.00 / Troyes 17.0 (bez marży 84/11/6), handicap PSG -2,5 ~2.00, O3.5 1.83 / U3.5 1.95.
Absencje PSG: wg konferencji z 29.10 (Le Havre) poza Dembélé, Kvaratskhelia, Mendes, Marquinhos - stan na 07.11 niepotwierdzony (nie znaleziono konferencji przedmeczowej). Rotacja możliwa przed LM.
Model λ 2,6 / 0,6: 80/13/6; biorę 82/12/6 (rynek 84%; konkretna korekta za listę kontuzji, -2 pp).

| Rynek | p | fair | Pewność | Uwagi |
|---|---|---|---|---|
| 1 PSG | 82% | 1.22 | średnia-wysoka | graniczny fair 1.15-1.25 (rynek 1.14) |
| X | 12% | 8.3 | | |
| 2 Troyes | 6% | 16.7 | | |
| 1X | 94% | 1.06 | wysoka | poniżej progu 1.15, pominąć |
| Over 1.5 | 83% | 1.20 | średnia | graniczny 1.15-1.20 |
| Over 2.5 | 62% | 1.61 | średnia | |
| Over 3.5 | 40% | 2.50 | niska | rynek 1.83 (~52%) - moje p niższe, brak value |
| Under 3.5 | 60% | 1.66 | niska | |
| Handicap PSG -1.5 | 59% | 1.70 | niska-średnia | |
| Handicap PSG -2.5 | 36% | 2.75 | niska | |
| BTTS nie | 58% | 1.72 | niska | Troyes strzela mało (7 goli w 9) |
| Rożne O/U 10.5 (śr. 11,0, PSG dominuje) | 53/47% | 1.90/2.11 | niska | brak danych |
| Kartki O/U 3.5 (śr. 3,2) | 39% Over | 2.57 | niska | PSG mało kart, sędzia nieznany |

Ryzyka: rotacja i kontuzje PSG (Dembélé, Kvaratskhelia, Marquinhos - niepotwierdzone), Troyes broniący się nisko = mały margines; remis 12%, wygrana Troyes 6%.

---

## Podsumowanie rynków (najlepszy rynek w meczu, bez kuponów)
| Mecz | Najlepszy rynek | p | fair | Pewność |
|---|---|---|---|---|
| Korona - Radomiak | 1X | 78,5% | 1.27 | średnia |
| Śląsk - Piast | 12 (brak remisu) / Over 1.5 | 74% | 1.35 | średnia (brak mocnego typu wynikowego) |
| Górnik - Wieczysta | 1X / Over 1.5 / Under 3.5 | 81% / 76% / 71% | 1.23 / 1.32 / 1.41 | średnia |
| Widzew - Pogoń | Over 1.5 / Under 3.5 | 71% / 76% | 1.41 / 1.32 | średnia (wynik: brak mocnego typu) |
| Auxerre - Paris FC | X2 / Over 1.5 | 77% | 1.30 | średnia |
| PSG - Troyes | PSG wygra / PSG -1.5 / Over 2.5 | 82% / 59% / 62% | 1.22 / 1.70 / 1.61 | średnia-wysoka |

To są oszacowania probabilistyczne, nie gwarancje.

---

# Analiza tenisowa - sobota 07.11.2026 (czas PL)

Metoda: research w sieci (WebSearch/WebFetch; klucze API_TENNIS i The Odds API niedostepne, więc bez MCP tenisowego), model `tennis_model.py` + własna symulacja Monte Carlo (ten sam model punkt->gem->set->mecz) dla handicapu gemowego. Kursy z jednego źródła (Kalshi przez SportsBettingDime, BetMGM/Sportskeeda, 1xbet) - to NIE Betclic; do weryfikacji w bukmacherze.

## Potwierdzenie par (drugie źródło)
| Mecz | Źródło 1 | Źródło 2 | Status |
|---|---|---|---|
| Shelton - Van Assche (Paris SF) | Al Jazeera / tennismajors (strona meczu SF) | TennisTemple, SportsBettingDime, Dimers; sortiraparis: SF 14:30 i nie przed 17:00 | POTWIERDZONE |
| Alcaraz - Ruud (Paris SF) | Al Jazeera (Alcaraz d. Fritz, Ruud d. Borges) | tennismajors (strona SF), Sportskeeda, LastWordOnSports | POTWIERDZONE |
| Eala - Sakkari (Hong Kong SF) | tennis.com (draw: SF Sakkari(4) - Eala(2)) | ESPN, GMA, TennisUpToDate | POTWIERDZONE; godzina niepewna (źródła: ok. 16:00 lokalnie = ok. 09:00 PL, jedno podaje 07:10 GMT = 08:10 PL) |

Status meczów: nie mogę sprawdzić wyniku live (brak klucza livescore); w źródłach brak informacji o rozpoczęciu/zakończeniu - zakładam, że przed meczem. Sprawdź tuż przed.
Sprzeczność źródeł: godzina/kort Shelton - Van Assche (14:30 Court 2 vs 13:30 UTC Central) - godzina zgodna z sortiraparis (14:30 PL).

---

## 1. Ben Shelton (3, USA, ATP 4) - Luca Van Assche (FRA, ATP 47) | Paris Masters SF, hala, twarda | ok. 14:30
**Dane (SportsBettingDime / Tennis Abstract, 52 tyg.):** gemy serwisowe wygrane Shelton 89,9% vs Van Assche 77,2%; punkty przy 1. serwisie 76,6% vs 69,0%; asy/gem 0,73 vs 0,35; gemy returnowe 14,4% vs 29,2%; konwersja break pointów 36,7% vs 47,4%; Elo hard 1925 vs 1716.
**Droga w Paryżu:** Shelton: Norrie 6-3 6-4, Rinderknech 3-6 6-4 7-6(5) (z 2-4 w tie-breaku), Paul 6-4 4-6 6-3. Van Assche: Navone, Tien 7-6 6-4, Musetti 7-5 3-6 6-4, Hijikata 6-4 6-7 7-5 (2h44) - pierwszy SF Masters 1000. Van Assche wygrał w tym roku ATP 250 Estoril.
**H2H:** 0-0.
**Media:** Shelton przegrał tydzień wcześniej w Bazylei z nr 222 Jerome Kymem (forma/zmienność). Brak doniesień o kontuzjach. Van Assche ma zaliczone 2 trzysetówki z rzędu (zmęczenie) i 175 cm vs serwis Sheltona.
**Rynek (Kalshi):** Shelton -334 (bez marży ok. 76%), Van Assche +316; spread gemowy Shelton -3,5 ok. 49%; total 23,5 (Over +122).

p_serve (ze statystyk 52 tyg., skorygowane o return rywala): Shelton 0,69, Van Assche 0,63 (źródło p_serve: statystyki, nie ranking). Model: Shelton 76,8%.
Korekty: minus ok. 2 pp (porażka z nr 222 tydzień temu, 3 sety z rzędu z wąskimi końcówkami; wysoka zmienność Sheltona), wynik 75% (rynek 76%, zgodność).

| Rynek | p | Fair odds | Pewność | Uwagi |
|---|---|---|---|---|
| Zwycięzca: Shelton | 75% | 1,33 | średnia | Van Assche 25% / 4,00 |
| Wynik setowy 2-0 Shelton | 45% | 2,22 | niska | 2-1 Shelton 30% (3,33); 1-2: 14,5% (6,9); 0-2: 10,5% (9,5) |
| Handicap gemowy Shelton -2,5 | 60% | 1,67 | niska | -1,5: 69% (1,45) |
| Handicap gemowy Shelton -3,5 | 48% | 2,08 | niska | = rynek; brak przewagi |
| Handicap gemowy Van Assche +3,5 | 52% | 1,92 | niska | |
| Total gemów | - | - | - | Model 24,5-25,1; Over 23,5 ok. 48%, Under ok. 52% - Kalshi wyżej wycenia Under (ok. 56%), brak value; p_serve ze statystyk, więc dane OK, ale nie typować (brak przewagi) |

**Ryzyka:** tie-breaki (Shelton serwis wygrywa, ale Van Assche return 29% i konwersja BP 47%); gorszy dzień Sheltona (Basel); zmęczenie Van Assche zmniejsza jego szanse w 3. secie.

---

## 2. Carlos Alcaraz (2, ESP) - Casper Ruud (NOR) | Paris Masters SF, hala | nie przed 17:00
**Droga:** Alcaraz: Michelsen 7-6(4) 6-3, walkower (Berrettini wycofany) w R16, Fritz 6-7(10) 7-5 6-3 (2h43, obroniony 2 mecz-bole) w piątek wieczorem; tylko 2 mecze rozegrane w turnieju. Ruud: Cerundolo 6-3 6-2, Jodar 6-3 6-4, Struff 6-3 6-3, Borges 7-6(5) 6-4 - bez straconego seta, 4 mecze.
**H2H:** Alcaraz 6-1 (w tym Indian Wells 2026); jedyna wygrana Ruuda: ATP Finals Turyn 2024, hala twarda.
**Media:** brak doniesień o kontuzji Alcaraza (Al Jazeera); serwis wahał się przy 5-5 z Fritzem. Przerwa dla Alcaraza: ok. 18 h od końca 3-godzinnego meczu. Ruud poza top 8 w sezonie, bez motywacji ATP Finals, ale rytm.
**Rynek:** BetMGM Alcaraz -550 / Ruud +400 (bez marży ok. 81/19%); Tennistonic 1,17 / 5,0 (ok. 83%).
**Statystyki serwisu/returnu 2026 nie znalezione** - p_serve oszacowane z profilu (Alcaraz 0,67, Ruud 0,61, korekta na halę i H2H) -> total gemów nie typowany.
Model: Alcaraz 77,3%. Własne p: 78% (poniżej rynku o ok. 3 pp: zmęczenie po 2h43 i obronionych MP, Ruud w rytmie i wygrał z nim na hali; H2H 6-1 wspiera Alcaraza).

| Rynek | p | Fair odds | Pewność | Uwagi |
|---|---|---|---|---|
| Zwycięzca: Alcaraz | 78% | 1,28 | średnia | Ruud 22% / 4,55 |
| Wynik setowy 2-0 Alcaraz | 46% | 2,17 | niska | 2-1: 32% (3,13); 1-2 Ruud: 13% (7,7); 0-2: 9% (11) |
| Handicap gemowy Alcaraz -2,5 | 63% | 1,59 | niska | |
| Handicap gemowy Alcaraz -3,5 | 52% | 1,92 | niska | -4,5: 38% (2,63); Ruud +3,5: 48%, +4,5: 62% |
| Total gemów | - | - | - | p_serve oszacowane - nie podawać |

**Ryzyka:** zmęczenie Alcaraza/niski poziom serwisu, hala (Turyn 2024) sprzyja Ruudowi, gorszy dzień (wahnięcia z Fritzem); Alcaraz jest krótkim faworytem (fair 1,28 > 1,15, ale rynek ok. 1,17 - brak value).

---

## 3. Alexandra Eala (2, FIL, live ok. 16) - Maria Sakkari (4, GRE, ok. 30) | WTA Hong Kong SF, twarda | ok. 09:00
**Droga:** Eala: Jones 6-4 6-3, Valentova 6-4 7-6(7), Ruzic 7-6(7) 7-5 (ok. 2h30, przerwa na deszcz, obroniła 11 BP). Sakkari: Young 6-1 6-4, Joint 4-6 6-3 6-3, Sasnovich 6-2 6-3 (krótki, ok. wygodny).
**H2H:** 0-0.
**Kontekst:** Eala 4. SF WTA sezonu, tytuł WTA 500 w 2026; wygrana da jej top 15. Sakkari wraca do top 30 po słabszych sezonach (kontuzja barku 2024); w 2026 drugi finał w zasięgu; tytuły: 2 z 11 finałów, ostatni 2023. Typerzy podzieleni (Sportskeeda i Best Bets: Eala; LastWordOnSports i Freetips: Sakkari; zwracają uwagę na wrażliwy serwis Eali).
**Rynek:** Sportskeeda: Eala -135 / Sakkari +105 (bez marży ok. 54/46%); 1xbet Eala 1,73 (ok. 58% z marżą).
**Brak statystyk serwisu i returnu** - p_serve oszacowane; total gemów nie typowany.
Model (p_serve 0,64/0,62, tylko ranking): Eala 60% - odrzucony; rozstęp od rynku i źródeł >5 pp bez twardych danych. Własne p: 53% (poniżej rynku: dłuższy i trudniejszy QF Eali, serwis wrażliwy, doświadczenie Sakkari na turniejach; plus: forma Eali, 4. SF sezonu, rozstawienie).

| Rynek | p | Fair odds | Pewność | Uwagi |
|---|---|---|---|---|
| Zwycięzca: Eala | 53% | 1,89 | niska | Sakkari 47% / 2,13 |
| Wynik setowy | Eala 2-0 28% (3,57); Eala 2-1 25% (4,00); Sakkari 2-1 24% (4,17); Sakkari 2-0 23% (4,35) | | niska | rozkład spłaszczony (zasada WTA) |
| Handicap gemowy Eala -1,5 | 43% | 2,33 | niska | Sakkari +1,5: 57% (1,75) |
| Handicap gemowy Eala -2,5 | 36% | 2,78 | niska | Sakkari +2,5: 64% (1,56) |
| Total gemów | - | - | - | p_serve oszacowane - nie podawać; informacyjnie ok. 21-23 (tylko poglądowo; Statszone tipuje Over 19,5) |

**Ryzyka:** niski stopień pewności; przy równych szansach wynik zależy od serwisu Eali (11 obronionych BP w QF) i regeneracji; faworyt nie wyraźny; godzina meczu niepewna.

---

## Podsumowanie
- Pary potwierdzone; mecze zakładam jako niezaczęte (sprawdzić tuż przed).
- Najwyższe p: Alcaraz 78% (fair 1,28) i Shelton 75% (fair 1,33) - obaj w okolicy rynku (brak value), pewność średnia.
- Eala - Sakkari: mecz równy, nie do TOP; pewność niska.
- Total gemów: żaden nie jest typowany (Shelton - VA: brak przewagi nad rynkiem; pozostałe p_serve szacowane).
- To oszacowania, nie gwarancje.

---

# Analiza e-sport, sobota 07.11.2026 (czas PL), stan na 08:27 PL (07:27 UTC)

Oba mecze jeszcze się nie rozpoczęły ani nie zakończyły (Pinnacle: status "pending", cutoff = start). Kursy: Pinnacle (MCP sportsdata), marża usunięta proporcjonalnie (~4-5%). Źródła HLTV/Liquipedia/Leaguepedia/blast.tv zwracały 403, więc potwierdzenia pochodzą z agregatorów, Pinnacle i mediów (linki w tekście).

---

## 1. CS2, IEM Beijing 2026, półfinał (bo3): MOUZ - BetBoom Team, ok. 10:45 PL

**Potwierdzenie pary i rangi rundy (drugie źródło):** to NIE jest runda otwarcia playoffów, tylko PÓŁFINAŁ (SF2). MOUZ wygrali Grupę B bez straty mapy i weszli prosto do półfinału (bye). BetBoom wygrali ćwierćfinał z FURIA 2-1 w piątek 06.11 (Ancient 13-5, Dust2 przegrane 10-13, Nuke 16-14 po dogrywce), pierwsza wygrana BetBoom z FURIA po pięciu porażkach z rzędu. Źródła: HLTV (news), timesaver.gg, TalkEsport, rg.org, skin.club, Strafe (bracket: MOUZ vs zwycięzca FURIA/BetBoom).
**Godzina:** 17:45 CST = 09:45 UTC = **10:45 PL** (HLTV/timesaver.gg, Pinnacle start 09:45Z, Strafe 10:45 CET). Navi.gg pokazuje inną godzinę (11:45, prawdopodobnie inna strefa/slot); poprzedni mecz (MongolZ vs NAVI, SF1, 07:30 PL) już trwa, więc możliwe opóźnienie startu.
**Stawka:** zwycięzca gra finał (bo5, niedziela 08.11) z MongolZ/NAVI. Przegrany gra mecz o 3. miejsce.

**Składy (bez stand-inów w żadnym źródle):**
- MOUZ: torzsi, Spinx, xertioN, PR, xelex (HLTV; skład z Cologne Major z Brollanem i Jimpphatem jest już nieaktualny).
- BetBoom: Boombl4, zorte, S1ren, d1Ledez, Magnojez; trener Fierce.

**Statystyki / forma:**
- MOUZ: nr 1 VRS (1964 pkt), 2-0 TYLOO, 2-0 BetBoom (Ancient 13-6, Mirage 16-14), 2-0 PARIVISION (Ancient 13-2, Mirage 13-9), 0 straconych map na turnieju. Spinx rating 1.17 (3 mies.), 1.94 w meczu z TYLOO. Uwaga: korzystny los, zdecydowanie słabsi rywale w grupie (Insider Gaming). Odpoczęci (bye).
- BetBoom: nr 6 VRS (1801 pkt) / ~4. wg Strafe; droga przez dolną drabinkę (Aurora 2-0, Liquid 2-1, FURIA 2-1), gra 3 serie w 4 dni. Magnojez 1.14, zorte 1.05 (rośnie), Boombl4 0.96. Magnojez sam mówi, że w grupie "nie mieli szans", ale zespół jest w formie i z pewnością siebie po pierwszej wygranej z FURIA.
- Win rate map, 3 mies. (BetBoom | MOUZ), skin.club: Mirage 62% (13) | 81% (16); Dust2 29% (7) | 58% (12); Inferno 0 | 78% (9); Nuke 71% (7) | 69% (13); Ancient 57% (7) | 43% (7); Anubis 50% (10) | 0 map; Cache 40% | 44%.
- Symulacja vetów HLTV: Mirage 93%, Nuke 69%, Ancient 62%, Dust2 46% (jako mapy rozegrane). Przewidywany veto: BB ban Mirage, MOUZ ban Ancient, BB pick Anubis, MOUZ pick Dust2, decider Nuke. Realny veto nieznany (mecz nie wystartował).
**H2H:** 03.11 grupa B MOUZ 2-0 (Mirage 16-14, Ancient 13-6). Inne spotkania w obecnych składach nie ustalone.

**Kalibracja:** p per mapa (a nie jedna wartość): mapa BetBoom (Anubis/Ancient/Nuke) 0.57 dla MOUZ, mapa MOUZ (Dust2/Inferno/Mirage) 0.68, decider (Nuke) 0.60. Model wyszedł 67.2% (bez korekt 64.9%), rynek Pinnacle bez marży 70.5%: różnica 3 pp, bez podstaw do schodzenia pod rynek (brak stand-inów, kontuzji), więc jestem blisko rynku, lekko niżej z powodu świeżo wygranej przez BB z FURIA i słabszej mapy MOUZ na Anubis. Sygnał ryzyka "MOUZ losowy los/słabsi rywale" uwzględniony przez obniżenie z 70.5% do 67.2%.

`series.py 0.57 0.68 0.60 --bo 3`

| Rynek | Typ | p | Fair odds | Pinnacle (dec.) / p rynku bez marży | Pewność |
|---|---|---|---|---|---|
| Zwycięzca serii | MOUZ | 67.2% | 1.49 | 1.37 / 70.5% | średnia |
| Zwycięzca serii | BetBoom | 32.8% | 3.05 | 3.26 / 29.5% | średnia |
| Dokładny wynik | MOUZ 2-0 | 38.8% | 2.58 | 2.24 (hcap -1.5) / 43.0% | niska |
| Dokładny wynik | MOUZ 2-1 | 28.5% | 3.51 | n/d | niska |
| Dokładny wynik | BetBoom 2-1 | 19.0% | 5.26 | n/d | niska |
| Dokładny wynik | BetBoom 2-0 | 13.8% | 7.25 | n/d | niska |
| Handicap map | MOUZ -1.5 | 38.8% | 2.58 | 2.24 / 43.0% | niska |
| Handicap map | BetBoom +1.5 | 61.2% | 1.63 | 1.69 / 59.0% | średnia |
| Handicap map | MOUZ +1.5 | 86.2% | 1.16 (graniczny) | 1.13 | średnia |
| Handicap map | BetBoom -1.5 | 13.8% | 7.25 | 6.28 | niska |
| Total map | Over 2.5 (3 mapy) | 47.5% | 2.11 | 2.21 / 43.6% | niska |
| Total map | Under 2.5 (2-0 któregoś) | 52.5% | 1.90 | 1.71 / 56.4% | niska |
| Zwycięzca mapy 1 | MOUZ | 57% | 1.75 | 1.64 / 61.3% | niska (zależy od vetów) |
| Zwycięzca mapy 1 | BetBoom | 43% | 2.33 | 2.49 | niska |
| Zwycięzca mapy 2 | MOUZ | 68% | 1.47 | 1.43 / 67.5% | niska (zależy od vetów) |
| Zwycięzca mapy 2 | BetBoom | 32% | 3.13 | 3.00 | niska |

Rynkowe kursy Pinnacle: MOUZ -273 (1.37), BB +226 (3.26); hcap MOUZ -1.5 +124, BB +1.5 -144; total 2.5 O +121 / U -141; mapa 1 MOUZ -175 / BB +149; mapa 2 MOUZ -235 / BB +197.

**Ocena:** wyrównana seria z umiarkowanym faworytem; brak mocnego typu na zwycięzcę (fair 1.49 vs rynek 1.37: brak wartości w MOUZ). Jedyne marginalne value: BetBoom +1.5 mapy (EV ok. +3-4% względem 1.69) i Over 2.5 (EV ok. +5% względem 2.21), oba w granicach błędu modelu.
**Ryzyka:**
- Veto: nieznany, mapy 1 i 2 zależą od tego, kto pickuje; MOUZ mają przewagę na Dust2/Inferno/Mirage, BB na Anubis (MOUZ 0 map) i Ancient/Nuke.
- Dokładna historia: BB dwa razy w 4 dniach na dogrywkowej mapie (Nuke 16-14), zmęczenie zmniejsza p BB, forma i pewność siebie je zwiększają.
- Opóźnienie startu przez SF1 (MongolZ - NAVI).
- Rozbieżność godzinowa w niektórych źródłach (11:45 w navi.gg).

---

## 2. LoL, Worlds 2026, półfinał (bo5): Invictus Gaming - Gen.G, sob. 07.11 ok. 23:00 PL

**Potwierdzenie pary i godziny:** to Gen.G, które wygrało ćwierćfinał z LYON 3-0 (04.11; zabójstwa 19-8, 22-6, 16-10) i mają zagrać z IG w SF1 (esports.gg, Yahoo Sports, riftdaily, ESTNN). Godzina: **17:00 ET = 22:00 UTC = 23:00 PL** (Lolumen, Senseos 22:00 UTC, eScharts 22:00 GMT, ESTNN "11 PM Paris", Pinnacle start 22:00Z). eScharts ma w jednym miejscu 21:40 GMT, uznaję to za błąd; lines.com podał ostatecznie to samo 17:00 ET (zgodne). Półfinał 2 (BLG - T1) w niedzielę o tej samej porze. Lokalizacja: Allen, Teksas. Możliwy poślizg na Worlds jest typowo kilkuminutowy.
**Status:** nie rozpoczęty ani zakończony.

**Składy:**
- Gen.G: Kiin (top), Canyon (jungle), Chovy (mid), Ruler (ADC), Duro (support). Bez zmian/stand-inów.
- IG: TheShy (top, wrócił do składu po 15.06.2026), Wei (jungle), Rookie (mid), JiaQi (ADC), Meiko (support). Skład ustalony od lipca. Bez informacji o stand-inach (stand-in w TES, nie w IG, w ćwierćfinale).

**Forma:**
- Gen.G: obrońcy tytułu (turniej 2025), Swiss 3-0 (jedyna stracona gra: LYON, 2-1; łącznie 3 serie bez porażki serii), ćwierćfinał 3-0 w 91 minut (57-24 w killach). Wysoki rating (Polymarket 1552, najwyższy z ósemki; IG 1398, najniższy). Obrońcy tytułu wg Invena. Picki z QF: Kiin Olaf/Aurora, Canyon Qiyana/JarvanIV/Pantheon, Chovy Taliyah/Galio/Viktor, Ruler Ashe, Duro Seraphine. Patch 26.22 od 04.11 (niepotwierdzony jako patch tych gier).
- IG: Swiss 3-1 (porażka w R1 z Gen.G, wygrane z Secret Whales, HLE, LYON 2-1), ćwierćfinał 3-1 z TES (TES grał z 369 jako stand-inem za ZUIAN, brak wizy). Gry: 27-12, 17-20 (TES, 47 min), 16-9, 16-10. Wei (Jayce, Naafiri) MVP; styl: agresywne skirmishe w dżungli i picki nieszablonowe. W LPL 2026 przegrali Grand Final z Anyone's Legend (12.09), na Worlds jako ostatni reprezentant LPL (pokonali JDG).
**H2H:** Swiss R1 (23.10) Gen.G 1-0, gra 26 min; IG prowadziło wczesne (first blood, ok. +2k w 10 min), Gen.G przejęło smoki/Soul/Barona i wygrało. Dla bo5 to jedna gra, ale pokazuje, że IG potrafi wygrać early, a Gen.G skaluje w mid/late.
**Brak danych:** pełne drafty i win rate stron (blue/red), gol.gg/Oracle's Elixir niedostępne (403/brak w wynikach), więc nie rozdzielałem p po stronach (rozstrzygnięcie stron w grze 1 nieznane).

**Kalibracja:** p Gen.G na grę 0.67 (rynek, Pinnacle moneyline gry: 69.4% bez marży). Serię liczy się ze stałą p. Rynek serii 80.6% vs mój 79.5%: zgodne (<2 pp). Rozkład wyników rynku jest bardziej "wygrywowy 3-0" (Gen.G -2.5 36.8%, Over 3.5 59.9%) niż czysty model niezależnych gier (Gen.G 3-0 30.1%, Over 3.5 66.3%); korzystam z mieszanki, bo siła Gen.G jest zmienna i korelowana między grami (jeśli Gen.G w formie, rozkład przechyla się do sweepów; TheShy/Wei dają IG wysoką wariancję).

`series.py 0.67 --bo 5` + korekta rozkładu wyniku w stronę rynku

| Rynek | Typ | p | Fair odds | Pinnacle (dec.) / p rynku bez marży | Pewność |
|---|---|---|---|---|---|
| Zwycięzca serii | Gen.G | 79.5% | 1.26 | 1.18 / 80.6% | średnia-wysoka |
| Zwycięzca serii | IG | 20.5% | 4.88 | 4.89 / 19.4% | średnia-wysoka |
| Dokładny wynik | Gen.G 3-0 | 33% | 3.03 | n/d (-2.5: 2.61 / 36.8%) | niska |
| Dokładny wynik | Gen.G 3-1 | 29.5% | 3.39 | n/d | niska |
| Dokładny wynik | Gen.G 3-2 | 17% | 5.88 | n/d | niska |
| Dokładny wynik | IG 3-2 | 10% | 10.0 | n/d | niska |
| Dokładny wynik | IG 3-1 | 7% | 14.3 | n/d | niska |
| Dokładny wynik | IG 3-0 | 3.5% | 28.6 | n/d | niska |
| Handicap map | Gen.G -1.5 (3-0 lub 3-1) | 62.5% | 1.60 | 1.45 / 65.4% | średnia |
| Handicap map | Gen.G -2.5 (3-0) | 33% | 3.03 | 2.61 / 36.8% | niska |
| Handicap map | IG +1.5 | 37.5% | 2.67 | 2.73 / 34.6% | średnia |
| Handicap map | IG +2.5 | 67% | 1.49 | 1.52 / 63.2% | średnia |
| Handicap map | Gen.G +1.5 | 89.5% | 1.12 (poniżej 1.15) | 1.07 | średnia |
| Handicap map | IG -1.5 | 10.5% | 9.5 | 7.48 | niska |
| Total map | Over 3.5 (4-5 gier) | 63.5% | 1.57 | 1.57 / 59.9% | średnia |
| Total map | Under 3.5 (sweep) | 36.5% | 2.74 | 2.34 / 40.1% | średnia |
| Total map | Over 4.5 (5 gier) | 27% | 3.70 | 3.33 / 26% (Polymarket) | niska |
| Total map | Under 4.5 | 73% | 1.37 | 1.27 | średnia |
| Zwycięzca gry 1 | Gen.G | 67% (+/-2 pp w zależności od strony) | 1.49 | 1.38 / 69.4% | niska-średnia |
| Zwycięzca gry 1 | IG | 33% | 3.03 | 3.13 / 30.6% | niska-średnia |
| Zwycięzca gry 2 | Gen.G | 67% | 1.49 | 1.37 / 69.4% | niska-średnia |
| Zwycięzca gry 3 | Gen.G | 67% | 1.49 | 1.37 / 69.4% | niska-średnia |

(Uwaga: Pinnacle gra 1-3 Gen.G -264 = 1.38, IG +213 = 3.13; bez marży 69.4% / 30.6%; gry 4 i 5: oferta -110/-110 placeholder bez realnego p.)

Kursy Pinnacle serii: Gen.G -550 (1.18), IG +389 (4.89); hcap Gen.G -2.5 +161 (2.61) / IG +2.5 -192 (1.52); Gen.G -1.5 -224 (1.45) / IG +1.5 +173 (2.73); total 3.5 O -176 (1.57) / U +134 (2.34); 4.5 O +233 / U -383.

**Ocena:** faworyt wyraźny (ok. 80%), ale kurs zwycięzcy serii (1.18) jest poniżej fair 1.26: brak wartości; ponadto próg 1.15-1.20 to graniczne. Sensowniejsze rynki to IG +2.5 mapy (p 67%, kurs 1.52, EV w granicach błędu) i Gen.G -1.5 (fair 1.60 vs 1.45, brak wartości). Brak mocnego typu z wartością.
**Ryzyka:**
- Gen.G: przeciążenie/zmęczenie (3 serie w 8 dni, pierwsza seria 04.11), choć ćwierćfinał był szybki (91 min); Gen.G nie przegrali serii na Worlds.
- IG: agresywne picki (Jayce, Naafiri, Gnar) mogą zaskoczyć, TheShy i Rookie w formie turniejowej, doświadczenie (3 byłych mistrzów); IG miało wczesną przewagę w Swiss R1.
- Brak pewnych danych o stronach i draftach; patch 26.22 (04.11) może zmienić meta.
- Opóźnienia startu na Worlds są rzadkie, ale możliwe; godzina 23:00 PL potwierdzona 5 źródłami.

---
Szacunki, nie gwarancje. Bez budowania kuponów. Uwaga warsztatowa: korekty i p ustalone ręcznie na podstawie skryptu `series.py`; źródła rangowe (HLTV, Liquipedia, gol.gg) niedostępne (403), więc część statystyk (map pool BB/MOUZ) pochodzi z skin.club (3 mies.) i HLTV (przez cytaty), a statystyki stron LoL są niedostępne.

---

# Analiza NBA + NHL, sobota 07.11.2026 (czasy polskie)

Sprawdzone: 07.11.2026 (rano/przedpołudnie). Status składów i bramkarzy może się zmienić do startu. Brak klucza BettingPros / MySportsFeeds / TheOddsAPI, więc kursy tylko z feedu `nba_odds_today` (Novibet, FanDuel) i Pick Dawgz. Kursów NHL nie udało się znaleźć (brak rynku odniesienia, pewność obniżona). Oszacowania probabilistyczne, nie gwarancje.

## NBA: Denver Nuggets @ Indiana Pacers (23:00 PL, 17:00 ET), mecz w Mexico City (Arena CDMX, ok. 2240 m n.p.m.)

Uwaga: Pacers są formalnym gospodarzem, ale mecz jest w Meksyku (neutralny parkiet, brak przewagi własnego parkietu; wysokość nad poziomem morza służy raczej Denver).

**Dane**
- Net rating (NBA.com Advanced, 7-9 meczów): DEN +0,1 (ORtg 115,1 / DRtg 115,0, pace 98,5, bilans 4-3); IND -2,5 (ORtg 109,5 / DRtg 112,0, pace 101,8, bilans 3-6). Próba bardzo mała, zmieszana z oczekiwaniami rynku.
- Forma: DEN 128-109 z TOR (Jokić triple-double 32/10/11), 3 z 4 wygrane. IND 107-103 w Memphis, koniec serii 5 porażek. H2H: DEN 4 z 5 ostatnich (niska waga).
- Injury report (ESPN, Pick Dawgz, Indy Cornrows, aktualizacja 06.11): DEN: Strawther OUT, S. Jones OUT (hamstring), DeRozan back, probable/questionable (źródła rozbieżne). Jokić, Murray, Gordon, Johnson, Braun bez statusu. IND: Haliburton OUT (do ok. 13.11), McConnell OUT/questionable (rozbieżne), Oubre questionable (łydka), Furphy i Sheppard OUT. Zubac wrócił z kontuzji kostki (19 min, 1 pkt).
- Back-to-back: brak po żadnej stronie (IND ma dwa dni przerwy, DEN grał w środę). Drugi przystanek 3-meczowej wyprawy zagranicznej Pacers (zmęczenie, rotacja 12 graczy).
- `nba_daily_lineups` zwrócił 404 (brak potwierdzonych składów). Przewidywane starty: IND Nembhard, Nesmith, Oubre, Siakam, Zubac; DEN Murray, Braun, Gordon, C. Johnson, Jokić.

**Rynek:** ML DEN 1,37 (-268) / IND 3,20 (+220), bez marży DEN ok. 70%. Spread DEN -7,5 (Novibet 1,94; Pick Dawgz -106), FanDuel DEN -6,5 (1,83). Total 229,5 (Over -106 / Under -114, Pick Dawgz).

**Model:** surowe ORtg/DRtg dawały total ok. 223 i różnicę ok. 6. Z reguły SKILL.md (nie schodzić pod rynek bez konkretu) skorygowano do: DEN 117,75 - IND 110,75 (różnica 7,0, total 228,5). `nba_model.py 110.75 117.75`.

| Rynek | Typ | p | fair | Pewność |
|---|---|---|---|---|
| Zwycięzca | DEN | 73,4% | 1,36 | średnia (rynek ok. 70%; fair ≤ 1,36, kurs 1,37 bez EV) |
| Zwycięzca | IND | 26,6% | 3,76 | niska (rynek ok. 31%) |
| Spread DEN -6,5 | DEN pokrywa | 51,7% | 1,94 | niska |
| Spread DEN -7,5 | DEN pokrywa | 48,3% | 2,07 | niska |
| Spread IND +7,5 | IND pokrywa | 51,7% | 1,94 | niska |
| Total 229,5 | Under | 52,2% | 1,92 | niska (brak przewagi) |
| Total 229,5 | Over | 47,8% | 2,09 | niska |
| Jokić punkty 27,5 (linia ze źródła Pick Dawgz, niepotwierdzona) | Over 26,5 przy średniej 27,5 | 52% | 1,92 | niska (brak 2. źródła średniej, brak linii bukmachera) |
| Jokić PRA (średnia 47 założona) | Over 44,5 | 58% | 1,72 | niska, nie rekomendować (brak danych o linii) |

**Najlepszy rynek meczu:** brak mocnego typu. Zwycięzca DEN to jedyny typ z sensownym p (73%), ale kurs rynkowy 1,37 jest w okolicy fair (1,36), czyli EV ok. 0. Spread i total bez przewagi nad rynkiem.

**Ryzyka:** Haliburton OUT jest już w linii; DeRozan/Oubre/McConnell niepotwierdzeni (zmiana +-1 pkt w różnicy); nietypowa lokalizacja (wysokość, podróż, możliwy wolniejszy/szybszy tempo i wyższa wariancja: SD podniesione nie zostało, warto użyć 12,5/19); ryzyko blowoutu przy spreadzie 7,5 obniża minuty Jokicia i Siakama (rynki zawodnika tylko po potwierdzeniu); rozbieżność źródeł co do linii (-6,5 vs -7,5).

---

## NHL (bramkarze: Daily Faceoff 07.11, wszyscy 6 UNCONFIRMED; kursów NHL brak)

Back-to-back: żadna z 6 drużyn nie grała 06.11 (ostatnie mecze: FLA 04.11, WSH 03.11, STL i NSH 05.11, NYR 05.11, SEA 04.11), więc brak korekty b2b. Początek sezonu (14-17 meczów): λ zmieszane z lig. średnią 3,0 (waga ok. 50%). Typy z dogrywką (moneyline/total) chyba że napisano "60'".

### Washington Capitals - Florida Panthers (18:30 PL; 07.11 12:30 ET)
- Statystyki: FLA 9-5-2, GF 3,25 / GA 2,94, wygrane 4 z 5 ostatnich (m.in. 5-3 vs CHI 04.11). WSH 8-6-0, GF 3,5 / GA 3,43, trzy porażki z rzędu u siebie/na wyjeździe w ostatnich meczach (L2; 3-6 z DAL 03.11).
- Bramkarze (niepotwierdzeni): FLA Markstrom .886 / 2,57 GAA; WSH Thompson .887 / 3,22 (Lindgren rezerwowy). Obaj poniżej normy, wzajemnie się znoszą w λ.
- Kontuzje: WSH Sandin OUT, Desharnais IR (osłabiona obrona). FLA brak informacji w źródłach.
- λ: WSH 3,05 - FLA 3,20 (łącznie 6,25). `nhl_model.py 3.05 3.2`.

| Rynek | Typ | p | fair | Pewność |
|---|---|---|---|---|
| Moneyline | FLA | 52,4% | 1,91 | niska ("brak mocnego typu") |
| Moneyline | WSH | 47,6% | 2,10 | niska |
| 60' 3-way | 1 / X / 2 | 39,5 / 16,3 / 44,2% | 2,53 / 6,14 / 2,26 | niska |
| Puck line | FLA +... (FLA -1,5) | 28,9% | 3,46 | niska |
| Puck line | WSH +1,5 | 71,1% | 1,41 | niska |
| Puck line | WSH -1,5 | 24,9% | 4,01 | niska |
| Total 5,5 | Over | 59,4% | 1,68 | niska |
| Total 6,5 | Over / Under | 46,6% / 53,4% | 2,15 / 1,87 | niska |

Ryzyka: obaj bramkarze słabi, więc zmiana na Lindgrena lub drugiego bramkarza FLA zmienia λ o 0,3 gola; wysoki total modelu (6,25) może być wyższy niż rynek (nieznany): wg zasady skilla nie traktować Over jako przewagi bez konkretu.

### Nashville Predators - St. Louis Blues (19:00 PL; 07.11 13:00 ET)
- Statystyki: NSH 7-4-5, GF 3,06 / GA 3,13, 3 mecze z rzędu bez regulaminowej porażki (OT 3-2 z COL 05.11), dużo meczów do dogrywki. STL 7-7-2, GF 3,06 / GA 3,13, przegrane 1-3 NYR i 4-5 NJD (OT).
- Bramkarze (niepotwierdzeni): STL Hofer .918 / 2,39 (mocny punkt STL); NSH Saros .908 / 2,76.
- Kontuzje: brak informacji w źródłach. Obie drużyny po 1 dniu przerwy (brak b2b).
- λ: NSH 2,90 - STL 2,80 (łącznie 5,7; Hofer obniża λ NSH). `nhl_model.py 2.9 2.8`.

| Rynek | Typ | p | fair | Pewność |
|---|---|---|---|---|
| Moneyline | NSH | 51,7% | 1,94 | niska ("brak mocnego typu") |
| Moneyline | STL | 48,3% | 2,07 | niska |
| 60' 3-way | 1 / X / 2 | 43,1 / 17,1 / 39,8% | 2,32 / 5,85 / 2,51 | niska |
| Puck line | STL +1,5 | 72,7% | 1,38 | niska |
| Puck line | NSH +1,5 | 75,4% | 1,33 | niska |
| Total 5,5 | Under / Over | 49,5% / 50,5% | 2,02 / 1,98 | niska |
| Total 6,5 | Under | 62,4% | 1,60 | niska-średnia (typ najbardziej "wartościowy" w meczu, ale rynku nie znamy; wg SKILL.md Under nie schodzić poniżej rynku o >3 pp) |
| Saros obrony (założona średnia 26,5) | Over 24,5 / Under 26,5 | 61,8% / 51,8% | 1,62 / 1,93 | niska (nie rekomendować, brak średniej i linii) |

Ryzyka: Hofer lub Saros zastąpiony rezerwowym; nieznane kontuzje; duży odsetek OT (17%+) zaburza rynki 60'.

### Seattle Kraken - New York Rangers (23:00 PL; 07.11 17:00 ET)
- Statystyki: SEA 9-5-1, GF 3,6 / GA 3,53 (otwarte mecze), wygrane 2-1 OT z CGY 04.11 (poprzednio 2-6 w CGY). NYR 9-7-1, GF 3,0 / GA 2,88, dwie wygrane z rzędu (3-1 STL, 3-2 PHI). NYR po podróży na zachodnie wybrzeże (ostatni mecz 05.11).
- Bramkarze (niepotwierdzeni): SEA Daccord .889 / 3,53 GAA (słaby); NYR: Daily Faceoff (page) pokazuje Garand .906 / 2,51 (6-6-1), a wynik wyszukiwarki wymieniał Shesterkina. Rozbieżność, bramkarz NYR do potwierdzenia.
- Kontuzje: brak informacji w źródłach.
- λ: SEA 3,10 - NYR 3,05 (łącznie 6,15). `nhl_model.py 3.1 3.05`.

| Rynek | Typ | p | fair | Pewność |
|---|---|---|---|---|
| Moneyline | SEA | 50,8% | 1,97 | niska ("brak mocnego typu") |
| Moneyline | NYR | 49,2% | 2,03 | niska |
| 60' 3-way | 1 / X / 2 | 42,6 / 16,4 / 41,0% | 2,35 / 6,08 / 2,44 | niska |
| Puck line | NYR +1,5 | 72,6% | 1,38 | niska |
| Puck line | SEA +1,5 | 73,9% | 1,35 | niska |
| Total 5,5 | Over | 57,8% | 1,73 | niska |
| Total 6,5 | Over / Under | 45,0% / 55,0% | 2,22 / 1,82 | niska |

Ryzyka: niepewny bramkarz NYR (Shesterkin vs Garand zmienia λ SEA o 0,2-0,3); Daccord słaby, ale próba mała (7 meczów); podróż NYR.

### Uwagi NHL
- Skrypt `nhl_model.py` dla linii całkowitej 6,0 nie obsługuje zwrotu stawki (wynik identyczny jak dla 6,5), więc linię 6 pomijano.
- Wszystkie trzy mecze to "brak mocnego typu" (p zwycięzcy 47-52%); żaden rynek nie przekracza progu pewności średniej. Brak rynków zawodnika z danych (brak potwierdzonych składów i linii).

## Ranking (bez fair ≤ 1,15; wszystko niskiej pewności, brak kursów NHL)
1. DEN ML (NBA) p 73,4%, fair 1,36 (kurs 1,37, EV ok. 0)
2. NSH-STL Under 6,5 p 62,4%, fair 1,60 (bez rynku)
3. WSH-FLA Over 5,5 p 59,4%, fair 1,68 (bez rynku)
4. SEA-NYR Under 6,5 p 55,0%, fair 1,82 (bez rynku)
5. DEN -6,5 / IND +7,5 p ok. 52%, fair 1,94 (brak przewagi)
