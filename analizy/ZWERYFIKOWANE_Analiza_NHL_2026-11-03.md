# Analiza NHL, noc 03→04.11.2026 (11 meczów)

Źródła: NHL API, ESPN, Daily Faceoff, Pinnacle (kontrola p). Skill nhl-analyst, skrypty nhl_model.py / nhl_props.py. Stan bramkarzy z 03.11 rano USA — do potwierdzenia przed meczem.

# NHL 03.11.2026 (wtorek USA, noc na 04.11 PL) - analiza wg skilla nhl-analyst, mecze 1-3

Źródła: NHL API (nhl_schedule/standings/game_landing/boxscore), ESPN (game_summary: kontuzje, statystyki drużyn), DailyFaceoff (bramkarze, sprawdzone w dniu meczu, przed 7 PM ET), Pinnacle (kursy 60', ML, puck line, total; do porównania z moim p), skrypty nhl_model.py / nhl_props.py.
Braki: brak xG/CF%/GSAx (MoneyPuck/Natural Stat Trick niedostępne) - próbki 13-16 meczów, λ mieszane z ligą (shrink ok. 50%); BettingPros pominięty (brak klucza, nie pytano); H2H sezonu 2026-27 brak (0 spotkań w tym sezonie, waga niska); rynki zawodnika nie mają linii bukmachera - to wyceny rozkładów z ostatnich meczów, tylko 1 źródło liczb (NHL.com/ESPN) = pewność niska, bez rekomendacji na kupon. Godziny: 01:00 PL = 19:00 ET (czas PL = UTC+1 po zmianie czasu 01.11). Skład może się zmienić do rozpoczęcia meczu.

Konwencja: p to moje końcowe oszacowanie. λ z nhl_model.py (Poisson) to 60 minut; remis po 60' i dogrywkę Poissona traktuję jako szkic - wartości 3-way i puck line skorygowałem do rynku (remis ok. 21-22% zamiast 16%; gole w pustą bramkę podnoszą szanse -1.5). Ceny rynkowe poniżej to Pinnacle po usunięciu marży (oznaczone "rynek").

---

## 1. Toronto Maple Leafs - Utah Mammoth (04.11, 01:00 PL; 03.11 19:00 ET, Scotiabank Arena)

**Kontekst**
- Bramkarze (DailyFaceoff, sprawdzone 03.11 przed meczem): Utah Sebastian Cossa - POTWIERDZONY (.855 SV%, 3.20 GAA, 5 GP; Vejmelka .872 odpoczywa); Toronto Sergei Bobrovsky - POTWIERDZONY (.885, 3.29 GAA, 10 GP; Stolarz .910 gra mniej - "outplayed" przez Stolarza).
- B2B / podróż: oba zespoły bez B2B. Utah grał 01.11 w Filadelfii (1 dzień przerwy, przelot do Toronto); Toronto ostatnio 31.10 (Vancouver W 4-2) - 3 dni przerwy. Lekka przewaga TOR w odpoczynku.
- Kontuzje (ESPN): TOR bez Tavaresa (Out, ok. 07.11), Marchenko (IR, 17.11 - 6 G), Wood, Blankenburg, Rifai; UTA Yamamoto Day-To-Day (upper body, 03.11 - status niepotwierdzony), Marino (IR), Lamoureux (IR).
- Forma: TOR 8-6-2, GF 3.75 / GA 3.25, PP 30.0%, PK 91.1%, SOG 28.1 / SA 29.3. UTA 9-6-0, GF 3.60 / GA 3.47, PP 34.6%, PK 68.8%, SOG 29.9 / SA 24.5. Ostatnie 5: TOR W-W-L-L-W; UTA L-W-L-W-L (porażka 3-6 w PHI 01.11). Bardzo wysokie PP obu stron i słaby PK UTA (68.8%) przy dużej liczbie kar UTA (169 PIM) = wysoki wynik.
- H2H: brak meczów w tym sezonie; poprzednie lata nie mają wagi (skład, bramkarze).

**Przyjęte λ (60')**: TOR 3.10 - UTA 3.30 (razem 6.4). Uzasadnienie: obie obrony i obaj bramkarze poniżej średniej; TOR bez Tavaresa/Marchenki (-0.2) i z przewagą własnego lodu (+0.1), UTA lepsze PP. Kontrola rynku: razem ok. 6.4-6.5 w 60' (Pinnacle total 6.5 reg. over 49%); ML rynek TOR 43.6% / UTA 56.4% (UTA faworytem na wyjeździe z Cossą .855 - dziwne, ale to rynek i brak xG, więc nie schodzę poniżej o >5 pp).

**Rynki (p, fair)**
| Rynek | p | fair | Rynek Pinnacle (bez marży) |
|---|---|---|---|
| Moneyline (z OT/SO): TOR | 45% | 2.22 | 43.6% |
| Moneyline: UTA | 55% | 1.82 | 56.4% |
| 60' 3-way: TOR / remis / UTA | 36% / 21% / 43% | 2.78 / 4.76 / 2.33 | 33.6 / 21.9 / 44.5 |
| Puck line UTA -1.5 | 33% | 3.03 | 35.5% |
| Puck line TOR +1.5 | 67% | 1.49 | |
| Puck line TOR -1.5 | 25% | 4.00 | 25.4% |
| Puck line UTA +1.5 | 75% | 1.33 | |
| Total goli (z OT) Over 5.5 / Under 5.5 | 63% / 37% | 1.59 / 2.70 | Over 5.5 ok. 64% |
| Over 6.5 / Under 6.5 | 51% / 49% | 1.96 / 2.04 | Over 55% |
| Over 7.5 / Under 7.5 | 31% / 69% | 3.23 / 1.45 | |
| Obie strzelą (60') | 91% | 1.10 | (fair <=1.15, pomijać) |

Rynki zawodnika (średnie z ostatnich 16 meczów, wyceny bez linii bukmachera, pewność niska; skład niepotwierdzony; rynki tego samego zawodnika skorelowane):
- Matthews (TOR, 46 strzałów/16, 20:36 TOI): SOG Over 2.5 53% (fair 1.87), Over 3.5 33%; strzelec gola ok. 33% (fair 3.0; 11 G przy sh% 23.9% - regresja uwzględniona); punkty Over 0.5 ok. 64%.
- Nylander (TOR, 46/16): SOG Over 2.5 53%; gol ok. 31%.
- Cooley (UTA, 8 G, ale sh% 34.8% - nie do utrzymania, 1.5 strzału/mecz): gol ok. 24%, bez typu. Keller (UTA, 1.2 pkt/mecz, PP): punkty Over 0.5 ok. 58%.
- Obrony: Cossa (potw.) oczekiwane SA ok. 27.5 (TOR SOG 28.1 vs UTA SA 24.5), SV% regresowane ok. .880 -> średnia 24.2: Over 23.5 ok. 55%, Over 24.5 ok. 47%, Over 25.5 ok. 40%. Bobrovsky (potw.): SA ok. 29.5 (UTA SOG 29.9 vs TOR SA 29.3), SV% ok. .885 -> średnia 26.0: Over 25.5 52%, Over 26.5 45%.

**Typ główny:** Total Over 5.5 goli (z OT) | p 63% | fair 1.59 | pewność średnia (obaj bramkarze potwierdzeni i słabi, słaby PK UTA, wysokie PP; ryzyko: seria udanych obron, rozkład ogona). Najlepszy rynek meczu = total (zwycięzca to prawie rzut monetą: brak mocnego typu w ML, p 45-55%). Alternatywnie UTA +1.5 75% (fair 1.33), niska wartość.

**Ryzyka:** Cossa .855 na małej próbie (5 GP) może się okazać lepszy; Yamamoto DTD; gol w dogrywce wlicza się do totalu z OT, ale nie gol z karnych; Bobrovsky bywa zmieniany w trakcie meczu. Poisson z λ z kilku meczów zaniża ogon wysokich wyników (nie schodzę poniżej rynku w Over/Under >3 pp - nie schodzę).

---

## 2. Montreal Canadiens - Winnipeg Jets (04.11, 01:00 PL; 03.11 19:00 ET, Centre Bell)

**Kontekst**
- Bramkarze: Montreal Jacob Fowler - POTWIERDZONY (DailyFaceoff; .931-.932 SV%, 1.84-1.97 GAA, 7-1-0, 8 GP, 2 SO - próbka mała, regresuję do ok. .915); Winnipeg Stuart Skinner - PRZEWIDYWANY (niepotwierdzony; .887, 3.36 GAA, 10 GP; alternatywy Daws .886, Stevenson .870). Hellebuyck poza klubem (spór/transfer, sezon 2026-27 Skinner jest numerem 1). Montembeault (MTL) IR do 05.11.
- B2B / podróż: oba bez B2B. WPG grał 01.11 w Raleigh (0-7 z CAR), a 30.10 na Florydzie (1-5 FLA) - przegrywa 5 z rzędu (GF 2.27/mecz, SOG 26.3); w MTL 1 dzień przerwy po przelocie. MTL ostatnio 31.10 (W 5-4 z PIT), 3 dni odpoczynku, 5 wygranych z rzędu (L10: 8 W).
- Kontuzje (ESPN): MTL bez Suzukiego (Out, ok. 18.11 - 5 G, 12 pkt w 9 meczach), Demidova (IR), Dacha (Out, choroba, ok. 05.11), Mathesona (Out), Montembeaulta (IR). WPG: Morrissey (IR, wrist, ok. 08.11), Namestnikov, Bjugstad, Brown (IR).
- Forma: MTL 9-3-2 (rekord 14 GP), GF 3.29 / GA 3.00, PP 9.5%, PK 81.8%, SOG 27.5 / SA 27.6, PDO podwyższone przez Fowlera. WPG 4-8-3, GF 2.27 / GA 3.60, PP 16.7%, PK 70.5%, SOG 26.3 / SA 29.7; Connor 11 G (60 strzałów), Scheifele 12 pkt.
- H2H: w 2026-27 brak; MTL wygrał 2-1 w WPG (poprzednio, wymienione w ostatnich 5 WPG jako L 2-1 vs MTL), niska waga.

**Przyjęte λ (60')**: MTL 3.15 - WPG 2.55 (razem 5.7). Uzasadnienie: WPG najsłabszy atak ligi i najgorsza obrona/PK, Fowler (regresowany ok. .915) obniża λ WPG o ok. 0.15; MTL osłabiony brakiem Suzukiego/Demidova (-0.15..-0.2) i najgorszym PP (9.5%). Rynek 60': MTL 48.5 / remis 21.6 / WPG 29.9; total ok. 5.9-6.0.

**Rynki (p, fair)**
| Rynek | p | fair | Rynek Pinnacle (bez marży) |
|---|---|---|---|
| Moneyline (z OT/SO): MTL | 60% | 1.67 | 60.4% |
| Moneyline: WPG | 40% | 2.50 | 39.6% |
| 60' 3-way: MTL / remis / WPG | 48% / 21% / 31% | 2.08 / 4.76 / 3.23 | 48.5 / 21.6 / 29.9 |
| Puck line MTL -1.5 | 37% | 2.70 | 39.5% |
| Puck line WPG +1.5 | 63% | 1.59 | |
| Puck line WPG -1.5 | 20% | 5.00 | |
| Puck line MTL +1.5 | 80% | 1.25 | |
| Total goli (z OT) Over 5.5 / Under 5.5 | 52% / 48% | 1.92 / 2.08 | Over 5.5 ok. 55% |
| Over 6.5 / Under 6.5 | 40% / 60% | 2.50 / 1.67 | Over 6.5 ok. 44% |
| Obie strzelą (60') | 88% | 1.14 | (fair <=1.15, pomijać) |

Rynki zawodnika (niska pewność, wyceny bez linii bukmachera, skład niepotwierdzony):
- Kyle Connor (WPG; 60 strzałów/15 = 4.0/mecz, 11 G, 5 PPG, 21:02 TOI): SOG Over 3.5 ok. 51%, Over 4.5 ok. 34%; strzelec gola ok. 34% (fair 2.9; sh% 18% regresowane, Fowler .915).
- Caufield (MTL; 44/14 = 3.1/mecz, 8 G; po wypadnięciu Suzukiego PP1): SOG Over 2.5 ok. 58% (fair 1.72), gol ok. 33%.
- Hutson (MTL, 0.93 pkt/mecz, 24:54 TOI): punkty Over 0.5 ok. 55%.
- Obrony: Fowler (potw.) oczekiwane SA ok. 27 (WPG SOG 26.3 vs MTL SA 27.6), SV% ok. .915 -> średnia 24.7: Over 23.5 ok. 56%, Over 24.5 ok. 50%, Over 25.5 ok. 42%. Skinner (niepotwierdzony - bez typu): SA ok. 28.6, SV% ok. .888 -> średnia 25.4: Over 24.5 ok. 55%, Over 25.5 ok. 48%, Over 26.5 ok. 41%.

**Typ główny:** MTL ML (z OT) | p 60% | fair 1.67 | pewność średnia (Fowler potw., WPG w kryzysie, ale model zgodny z rynkiem, nie ma przewagi wartości). Najpewniejszy rynek: MTL +1.5 80% (fair 1.25; wyższy kurs od progu 1.15, ale niski zysk). Total: brak mocnego typu (p 48-52%).

**Ryzyka:** Fowler regresuje do średniej (.931 na 220 strzałach); Skinner niepotwierdzony (jeśli Stevenson/Daws - zmiana λ WPG o ±0.1); najgorsze PP ligi MTL (9.5%) ogranicza gole; WPG ma najniższy GF, ale PK 70.5% przy 151 PIM MTL; gol w pustą bramkę skraca margines.

---

## 3. Tampa Bay Lightning - Detroit Red Wings (04.11, 01:00 PL; 03.11 19:00 ET, Benchmark International Arena)

**Kontekst**
- Bramkarze: Detroit John Gibson - PRZEWIDYWANY (niepotwierdzony; .860 SV%, 3.37 GAA, 4-5-1, 10 GP; rezerwowy Tarasov .927/1.75 GAA grał pełne 60' wczoraj w Sunrise (W 5-3 z FLA) - dlatego Gibson jest logicznym startowym); Tampa Andrei Vasilevskiy - PRZEWIDYWANY (niepotwierdzony; .877, 3.00 GAA, 10 GP; Hildeby .885 na wypadek rotacji). Oba niepotwierdzone (0 z 22 na DailyFaceoff o czasie sprawdzenia) - pewność najwyżej średnia/niska.
- B2B / podróż: DET w DRUGIM DNIU BACK-TO-BACK (02.11 W 5-3 w Sunrise, FLA; 03.11 w Tampie; przelot krótki, ale zmęczenie i brak odpoczynku). TBL ostatnio 31.10 (L 4-5 SO w NSH), 2 dni przerwy.
- Kontuzje (ESPN): DET bez Larkina (IR - zawieszenie, do 14.11), Kaspera (IR 14.11), Appletona (IR 10.11), Edvinssona (IR, spór kontraktowy), Johanssona D (Out, 05.11) - bez 3 centrów; TBL bez Girgensonsa (Out, 05.11) i Gourde'a (IR, 02.12).
- Forma: TBL 8-3-2 (13 GP), GF 3.69 / GA 3.23, PP 15.2%, PK 77.1%, SOG 30.1 / SA 24.9; Kucherov 18 pkt (14 A), Guentzel 8 G, Hagel 8 G/58 strzałów. DET 7-5-3, GF 2.93 / GA 2.93 (Tarasov!), PP 23.5%, PK 70.2%, SOG 29.6 / SA 24.5; Arvidsson 8 G, DeBrincat 7 G, Raymond 15 pkt, 6 z 8 ostatnich meczów wygranych. Ostatnie 5: TBL W-L-L-W-L (OT/SO porażki); DET L-W-W-L-W.
- H2H: brak meczów w 2026-27; w przeszłości Gibson 17-5-2 z DET przeciwko Tampie (kariera, mała waga). 

**Przyjęte λ (60')**: TBL 3.50 - DET 2.55 (razem 6.05). Uzasadnienie: DET bez trzech centrów (-0.15), B2B (-0.15), Gibson .860 (+0.1..0.15 dla TBL po regresji do ok. .890); TBL z dobrym atakiem (3.69) i przewagą lodu (+0.1). Rynek 60': TBL 57.5 / remis 19.9 / DET 22.6; ML rynku TBL 70.1% - wyższe niż mój model (65%): różnica 5 pp, w granicy "nie schodzę pod rynek o >5 pp" - ustawiam 66% (niższe zaznaczone jako ostrożność, bo żaden bramkarz niepotwierdzony i Poisson nie liczy lepiej remisów).

**Rynki (p, fair)**
| Rynek | p | fair | Rynek Pinnacle (bez marży) |
|---|---|---|---|
| Moneyline (z OT/SO): TBL | 66% | 1.52 | 70.1% |
| Moneyline: DET | 34% | 2.94 | 29.9% |
| 60' 3-way: TBL / remis / DET | 56% / 20% / 24% | 1.79 / 5.00 / 4.17 | 57.5 / 19.9 / 22.6 |
| Puck line TBL -1.5 | 44% | 2.27 | ok. 48-50% |
| Puck line DET +1.5 | 56% | 1.79 | |
| Puck line TBL +1.5 | 86% | 1.16 | (fair 1.16 - na granicy 1.15, oznaczyć) |
| Puck line DET -1.5 | 14% | 7.14 | |
| Total goli (z OT) Over 5.5 / Under 5.5 | 57% / 43% | 1.75 / 2.33 | Over 5.5 ok. 57% |
| Over 6.5 / Under 6.5 | 45% / 55% | 2.22 / 1.82 | Over 6.5 ok. 47.6% |
| Obie strzelą (60') | 90% | 1.11 | (pomijać) |

Rynki zawodnika (niska pewność; skład i bramkarze niepotwierdzeni; zawodnik DET na B2B):
- Hagel (TBL; 58 strzałów/13 = 4.5/mecz, 8 G, 21:29 TOI): SOG Over 3.5 ok. 57% (fair 1.76), Over 4.5 ok. 39%; gol ok. 36% (fair 2.8).
- Guentzel (TBL; 38/13 = 2.9/mecz, 8 G): SOG Over 2.5 ok. 52%; gol ok. 34%. Kucherov (TBL, 1.38 pkt/mecz): punkty Over 0.5 ok. 66% (fair 1.52).
- DeBrincat (DET; 55/15 = 3.7/mecz, 7 G): SOG Over 2.5 ok. 66%, Over 3.5 ok. 46%. Arvidsson (DET; 2.9 strzału, 8 G, PP): gol ok. 28%; punkty Over 0.5 ok. 54%. Raymond (DET): punkty Over 0.5 ok. 56%.
- Obrony: Gibson (przew.): SA ok. 28 (TBL SOG 30.1 vs DET SA 24.5), SV% ok. .885 -> średnia 24.8: Over 24.5 ok. 52%, Over 25.5 ok. 45%. Vasilevskiy (przew.): SA ok. 27.2 (DET SOG 29.6 vs TBL SA 24.9), SV% ok. .905 -> średnia 24.6: Over 23.5 ok. 55%, Over 25.5 ok. 41%. Bez typu do potwierdzenia startujących.

**Typ główny:** TBL ML (z OT) | p 66% | fair 1.52 | pewność średnia-niska (przewaga DET w braku centrów, B2B, ale oba bramkarze niepotwierdzeni; rynek jeszcze wyżej wycenia TBL 70%). Alternatywa: TBL +1.5 86% (fair 1.16, krótki kurs, oznaczone). Total: Over 5.5 57% (fair 1.75) bez przewagi względem rynku.

**Ryzyka:** Gibson/Vasilevskiy niepotwierdzeni (zmiana na Hildeby/Tarasov przesuwa λ o ok. 0.2-0.3); DET z dobrym PP 23.5% i Arvidssonem; Tampa 3 z 5 ostatnich meczów przegrane/OT; po dogrywce karnych rozstrzyga loteria; pusta bramka podnosi wyniki -1.5.

---

## Podsumowanie top rynków (mecze 1-3)
| Mecz | Rynek | p | fair | Pewność |
|---|---|---|---|---|
| TOR - UTA | Over 5.5 goli (z OT) | 63% | 1.59 | średnia |
| TOR - UTA | UTA +1.5 / UTA ML | 75% / 55% | 1.33 / 1.82 | niska (ML = brak mocnego typu) |
| MTL - WPG | MTL ML (z OT) | 60% | 1.67 | średnia |
| MTL - WPG | MTL +1.5 | 80% | 1.25 | średnia |
| TBL - DET | TBL ML (z OT) | 66% | 1.52 | średnia-niska (bramkarze niepotw.) |
| TBL - DET | TBL +1.5 | 86% | 1.16 | niska (fair na granicy 1.15) |

Bramkarze sprawdzeni 03.11 przed meczem (DailyFaceoff): potwierdzeni: Cossa, Bobrovsky, Fowler; niepotwierdzeni: Skinner, Gibson, Vasilevskiy. To oszacowania probabilistyczne, nie gwarancje.

# NHL wtorek 03.11.2026 (USA), noc na 04.11 PL - mecze 4-6 (skill nhl-analyst)

Godzina sprawdzenia bramkarzy: 03.11.2026 (Daily Faceoff, przez WebFetch; start 00:07 UTC = 01:07 PL). Sklad moze sie zmienic do rozpoczecia meczu.
Zrodla: NHL.com API (nhl_standings, nhl_club_schedule, nhl_goalie_leaders, nhl_skater_leaders; stan 03.11), Pinnacle (kursy zamkniete na moment sprawdzenia, przeliczone na p bez marzy), Daily Faceoff (bramkarze). BettingPros: pominiety (brak klucza/nie uzyty). xG/CF%/GSAx i liczba strzalow na mecz: NIE znalezione (brak drugiego zrodla) - rynki strzalow zawodnika i obron bramkarza maja niska pewnosc i nie wchodza do kuponu.
Poczatek sezonu (14-16 meczow) - proba mala, wiec p mocno zakotwiczone w rynku Pinnacle.
Uwaga o remisie: model Poissona zaniza remis po 60' (16% vs rynek ~22-23%), wiec p 3-way podaje wg rynku/blendu, a Poissona jako szkic. Dogrywka/karne dla ML i totalu liczone zgodnie z nhl_model.py.

---

## 4. St. Louis Blues @ New York Rangers (01:00 PL, wt 03.11 19:00 ET, MSG)

**Kontekst**
- Bramkarze: STL Joel Hofer - POTWIERDZONY (DailyFaceoff); sezon .916 SV%, 2.42 GAA, 6 W. NYR Dylan Garand - POTWIERDZONY; .896 SV%, 2.73 GAA, 4 W. Daily Faceoff wspomina, ze Shesterkin ma kontuzje do konca sezonu (zrodlo tylko ta strona, nie zweryfikowane drugim zrodlem; Shesterkin ma w statystykach .927/1.79 w 3 wygranych, wiec absencja jest istotna - obniza jakosc bramki NYR).
- B2B/podroze: STL ostatni mecz 31.10 (W 5-4 w DET), 2 dni odpoczynku; NYR ostatni 01.11 (L 1-4 z EDM), 1 dzien przerwy. Brak B2B po zadnej stronie.
- Forma: STL 7-6-1, GF 44 / GA 42 w 14 m (3.14 / 3.00), seria W2, L10 6-4-0 (35:29). NYR 7-7-1, GF 45 / GA 46 w 15 m (3.00 / 3.07), seria 4 porazek, L10 3-6-1 (29:38). W domu NYR 8 meczow, wyjazd STL bilans bramkowy ok. 25:26 w 7 m.
- Kluczowi: NYR Lafreniere 9 G / 16 pkt, Fox (D) 17 pkt; STL Snuggerud 8 G, McTavish 6 G.
- H2H: brak danych z biezacego sezonu (nie szukano glebiej; waga niska).

**Rynek (Pinnacle, bez marzy):** ML z OT: NYR 52.4% / STL 47.6%. 60': NYR 40.6% / X 22.9% / STL 36.5%. Total 6.0 (-104/-108); O5.5 54.8%, O6.5 44.4%. Team totals ok. 3.0 / 3.0. NYR -1.5 (60') +214.

**Przyjete lambda (60'):** NYR 2.90 - STL 3.00 (razem 5.90). Uzasadnienie: baza ligi 3.0; dom NYR +0.1; Garand (.896) slabszy niz sredni -> STL +0.1; Hofer (.916) lepszy niz sredni -> NYR -0.1; NYR kryzys (4 porazki) nie koryguje (zasada skilla: kryzys dotyczy tylko underdoga, a tu forma jest juz w kursie).

**Rynki (model Poissona; blend z rynkiem w kolumnie "p przyjete")**
| Rynek | Model | p przyjete | fair | Pewnosc |
|---|---|---|---|---|
| ML (z OT) NYR | 48.3% | 50.5% | 1.98 | niska |
| ML (z OT) STL | 51.7% | 49.5% | 2.02 | niska |
| 60' NYR (1) | 40.0% | 39.5% | 2.53 | niska |
| 60' remis (X) | 16.8% (zanizony) | 22% | 4.55 | niska |
| 60' STL (2) | 43.2% | 38.5% | 2.60 | niska |
| Puck line STL +1.5 | 75.1% | 74% | 1.35 | srednia (fair >1.15, ale kurs krotki) |
| Puck line NYR +1.5 | 72.4% | 71% | 1.41 | srednia |
| Puck line NYR -1.5 | 24.9% | 27% | 3.70 | niska |
| Puck line STL -1.5 | 27.6% | 28% | 3.57 | niska |
| Total Over 5.5 | 53.8% | 54% | 1.85 | niska-srednia |
| Total Under 5.5 | 46.2% | 46% | 2.17 | niska |
| Total Over 6.5 | 40.9% | 42% | 2.38 | niska |
| Total Under 6.5 | 59.1% | 58% | 1.72 | niska-srednia |
| Obie strzela (60') | 89.8% | 89% | 1.12 (<=1.15, pomijac) | - |

**Rynki zawodnika (srednia = rate sezonowy NHL.com, regresowany; JEDNO zrodlo, bez linii/PP, wiec pewnosc niska, nie do kuponu)**
| Rynek | p | fair |
|---|---|---|
| Lafreniere (NYR) strzelec gola (sr. 0.38) | 31.6% | 3.16 |
| Snuggerud (STL) strzelec gola (sr. 0.32) | 27.4% | 3.65 |
| Fox (NYR) pkt O0.5 (sr. 0.90) | 58% | 1.72 |
| Lafreniere pkt O0.5 (sr. 0.85) | 56.4% | 1.77 |
| Hofer obrony (sr. 25.5): O24.5 / O26.5 | 55.1% / 41.3% | 1.81 / 2.42 |
| Garand obrony (sr. 26.0): O24.5 / O26.5 | 58.5% / 44.8% | 1.71 / 2.23 |
Srednie obron to szacunek (strzaly rywala ~27-28 x SV%), bez drugiego zrodla strzalow.

**Pewnosc:** niska (mecz wyrownany, p 45-55% = brak mocnego typu na zwyciezce). Najlepsze rynki: puck line +1.5 (STL 75% / NYR 71%, krotkie kursy ~1.35-1.41), Under 6.5 (58%).
**Ryzyka:** Garand bardzo zmienny (.896); informacja o Shesterkinie niepotwierdzona drugim zrodlem; gole do pustej bramki w koncowce; dogrywka (ok. 22% meczow idzie do OT).
**Rynek vs model:** model STL 51.7% vs rynek 47.6% (4 pp, ponizej progu 5 pp - nie kwalifikuje sie jako value bez konkretu); total zgodny z rynkiem.

---

## 5. Minnesota Wild @ Philadelphia Flyers (01:00 PL, wt 03.11 19:00 ET)

**Kontekst**
- Bramkarze: MIN Jesper Wallstedt - POTWIERDZONY; .920 SV%, 2.06 GAA, 9 W (2. w lidze pod wzgledem wygranych). Filip Gustavsson kontuzjowany (biodro, wg DailyFaceoff). PHI Dan Vladar - POTWIERDZONY; .885 SV%, 3.23 GAA, 3 W (slaby); Joseph Woll .899/3.13 jako alternatywa.
- B2B/podroze: MIN ostatni mecz 01.11 (W 5-1 w WSH), 2 dni przerwy, krotka podroz DC-Filadelfia; PHI ostatni 01.11 (W 6-3 z UTA). Brak B2B.
- Forma: MIN 10-3-3 (23 pkt), GF 52 / GA 36 w 16 m (3.25 / 2.25), L10 6-2-2 (33:25), seria W1; na wyjazdach 6 m. PHI 4-8-4 (12 pkt), GF 35 / GA 54 (2.19 / 3.38) - najslabsza ofensywa i jedna z najslabszych defensyw; L10 4-4-2 (28:30). Dom PHI 7 m: 11:22 w bramkach.
- Kluczowi: Kaprizov 15 G / 25 pkt w 16 m (0.94 G/m - zawyzony shooting%), Quinn Hughes (D) 21 pkt, Boldy 14 pkt, Eriksson Ek 14 pkt; PHI Michkov 10 G.
- H2H: brak danych biezacego sezonu (waga niska).

**Rynek (Pinnacle, bez marzy):** ML z OT: MIN 61.9% / PHI 38.1%. 60': MIN 49.6% / X 21.4% / PHI 28.9%. Puck line MIN -1.5 ok. 40%, PHI +1.5 ok. 60%. Total 6.0 (+105/-118); O5.5 53.1%, O6.5 42.4%. Team total MIN 3.5 O +113, PHI 2.5 O -107.

**Przyjete lambda (60'):** PHI 2.55 - MIN 3.35 (razem 5.90). Uzasadnienie: PHI GF 2.19 + dom +0.1 + Wallstedt (.920) -> okolo 2.5; MIN GF 3.25 + zla defensywa PHI (GA 3.38) + Vladar (.885) +0.2 -> 3.35.

**Rynki (model Poissona; blend z rynkiem)**
| Rynek | Model | p przyjete | fair | Pewnosc |
|---|---|---|---|---|
| **ML (z OT) MIN** | 63.0% | 62% | 1.61 | **srednia** (bramkarze potwierdzeni, model zgodny z rynkiem) |
| ML (z OT) PHI | 37.0% | 38% | 2.63 | srednia |
| 60' MIN (1X2 gosc) | 54.7% | 50% | 2.00 | srednia |
| 60' remis | 16.0% (zanizony) | 21% | 4.76 | niska |
| 60' PHI | 29.3% | 29% | 3.45 | niska |
| Puck line MIN -1.5 | 38.0% | 39% | 2.56 | niska |
| Puck line PHI +1.5 | 62.0% | 61% | 1.64 | srednia |
| Puck line MIN +1.5 | 83.4% | 82% | 1.22 (przypadek 1.15-1.20+; krotki kurs) | srednia |
| Puck line PHI -1.5 | 16.6% | 18% | 5.56 | niska |
| Total Over 5.5 | 53.8% | 53.5% | 1.87 | niska-srednia |
| Total Under 5.5 | 46.2% | 46.5% | 2.15 | niska |
| Total Over 6.5 | 40.7% | 41.5% | 2.41 | niska |
| Total Under 6.5 | 59.3% | 58.5% | 1.71 | niska-srednia |
| Obie strzela (60') | 89% | 88% | 1.14 (<=1.15, pomijac) | - |

**Rynki zawodnika (jedno zrodlo, bez linii/PP - pewnosc niska, nie do kuponu)**
| Rynek | p | fair |
|---|---|---|
| Kaprizov strzelec gola (sr. 0.52, regresowane z 0.94) | 40.5% | 2.47 |
| Kaprizov pkt O0.5 (sr. 1.25) / O1.5 | 70.5% / 35.3% | 1.42 / 2.83 |
| Q. Hughes (D) pkt O0.5 (sr. 0.95) | 60.4% | 1.65 |
| Michkov (PHI) strzelec gola (sr. 0.40) | 33.0% | 3.03 |
| Wallstedt obrony (sr. 25.5): O24.5 / O26.5 | 55.1% / 41.3% | 1.81 / 2.42 |
| Vladar obrony (sr. 27.5, MIN strzela duzo): O25.5 / O27.5 | 61.6% / 48.2% | 1.62 / 2.07 |

**Pewnosc:** srednia dla MIN ML (62%); ale kurs fair 1.61 i rynek ok. 1.62 -> brak przewagi nad rynkiem. Najlepsze rynki: MIN ML 62%, MIN +1.5 82% (fair 1.22), Under 6.5 58.5%. Wallstedt vs Vladar to najwieksza roznica jakosci bramkarzy w tej trojce meczow.
**Ryzyka:** Kaprizov i MIN w serii z wysokim shooting% (regres), PHI ostatnio 6 goli z UTA; Wallstedt mlody (maly sample, .920 moze spasc); remis/OT ok. 21%; gole do pustej bramki psuja puck line -1.5.
**Rynek vs model:** zgodne (63.0% vs 61.9%).

---

## 6. Vegas Golden Knights @ Pittsburgh Penguins (01:00 PL, wt 03.11 19:00 ET)

**Kontekst**
- Bramkarze: PIT Arturs Silovs - POTWIERDZONY; .889 SV%, 2.98 GAA, 5 W, 2 shutouty. VGK Adin Hill - NIEPOTWIERDZONY (DailyFaceoff, snapshot: lista Carter Hart wg wyszukiwarki, strona-fetch: Hill); Hill .891 / 2.84 GAA / 5 W; Hart .893 / 2.65 / 4 W. Obaj prawie rownorzedni, wiec niepewnosc dotyczy glownie pewnosci, nie lambdy.
- B2B: **VGK w 2. dniu B2B** (02.11 przegrana w SO 2-3 w Bostonie, 03.11 w Pittsburghu po podrozy) - korekta -0.1 gola ataku i gorsza obrona; PIT ostatni mecz 31.10 (L 4-5 w MTL), 3 dni przerwy.
- Forma: VGK 9-5-2 (20 pkt), GF 55 / GA 47 w 16 m (3.44 / 2.94), L10 4-4-2 (32:33), ostatnie OT/SO. PIT 5-7-2 (12 pkt), GF 47 / GA 49 w 14 m (3.36 / 3.50), seria L1, L10 3-5-2 (29:36). Dom PIT 6 m: 15:... (slaba defensywa).
- Kluczowi: VGK Stone 10 G / 18 pkt, Eichel 20 pkt (7 G), Marner 17 pkt; PIT Malkin 6 G, E. Karlsson (D) 16 pkt.
- H2H: brak danych biezacego sezonu.

**Rynek (Pinnacle, bez marzy):** ML z OT: PIT 52.0% / VGK 48.0%. 60': PIT 40.7% / X 22.2% / VGK 37.1%. Total 6.5 (-116/+103): O6.5 52.2%; O5.5 62.5%. Team totals 3.5 / 3.5 (O ok. 47%). PIT -1.5 +218.

**Przyjete lambda (60'):** PIT 3.30 - VGK 3.20 (razem 6.50). Uzasadnienie: obie ofensywy ~3.4, obie defensywy slabe (GA 2.9-3.5), obaj bramkarze ~.89; dom PIT +0.1; VGK B2B -0.1; slaby Silovs podbija VGK. Zgodne z linia rynkowa 6.5.

**Rynki (model Poissona; blend z rynkiem)**
| Rynek | Model | p przyjete | fair | Pewnosc |
|---|---|---|---|---|
| ML (z OT) PIT | 51.6% | 51.5% | 1.94 | niska (Hill niepotwierdzony) |
| ML (z OT) VGK | 48.4% | 48.5% | 2.06 | niska |
| 60' PIT | 43.5% | 41% | 2.44 | niska |
| 60' remis | 16.0% (zanizony) | 21.5% | 4.65 | niska |
| 60' VGK | 40.5% | 37.5% | 2.67 | niska |
| Puck line VGK +1.5 | 71.4% | 72% | 1.39 | srednia |
| Puck line PIT +1.5 | 74.0% | 73% | 1.37 | srednia |
| Puck line PIT -1.5 | 28.6% | 27.5% | 3.64 | niska |
| Puck line VGK -1.5 | 26.0% | 27% | 3.70 | niska |
| **Total Over 5.5** | 63.1% | 62.5% | 1.60 | **niska-srednia (najlepszy rynek meczu)** |
| Total Under 5.5 | 36.9% | 37.5% | 2.67 | niska |
| Total Over 6.5 | 50.6% | 51% | 1.96 | niska |
| Total Under 6.5 | 49.4% | 49% | 2.04 | niska |
| Obie strzela (60') | 92.4% | 91% | 1.10 (<=1.15, pomijac) | - |

**Rynki zawodnika (jedno zrodlo, bez linii/PP - pewnosc niska, nie do kuponu)**
| Rynek | p | fair |
|---|---|---|
| Stone (VGK) strzelec gola (sr. 0.42, regresowane z 0.62) | 34% | 2.94 |
| Eichel (VGK) pkt O0.5 (sr. 1.05) | 64.1% | 1.56 |
| Marner (VGK) pkt O0.5 (sr. 0.90) | 58.5% | 1.71 |
| Malkin (PIT) strzelec gola (sr. 0.30) | 25.9% | 3.86 |
| E. Karlsson (D, PIT) pkt O0.5 (sr. 0.90) | 58.5% | 1.71 |
| Silovs obrony (sr. 26.5): O24.5 / O26.5 | 61% / 48.5% | 1.64 / 2.06 |
| Hill obrony (sr. 26.5, po B2B moze grac Hart): O24.5 / O26.5 | 61% / 48.5% | 1.64 / 2.06 |
Typ na obrony VGK tylko po potwierdzeniu bramkarza (niepotwierdzony = nie wchodzi do kuponu).

**Pewnosc:** niska dla zwyciezcy (50/50), niska-srednia dla Over 5.5. Mecz wyrownany = brak mocnego typu na zwyciezce. Najlepsze rynki: Over 5.5 (62.5%, fair 1.60, rynek ok. 1.54 - zgodne z rynkiem), puck line +1.5 (73%).
**Ryzyka:** niepotwierdzony bramkarz VGK (Hill vs Hart, w 2. dniu B2B moze zagrac rezerwowy); wysoka wariancja (obie bramki ~.89 SV%, ale sezon krotki, mozliwy regres w kierunku nizszych wynikow); wzmianki o VGK ostatnio OT/SO; Under 5.5 historycznie nie jest przewaga (patrz lekcje z 29-30.10). Over 5.5 padnie w razie szybkiego bramkarskiego wieczoru (pojedyncze 2-1/3-2).
**Rynek vs model:** zgodne (Over 5.5 63.1% vs 62.5%; PIT ML 51.6% vs 52.0%).

---

## Podsumowanie top rynkow (3 mecze)
| Mecz | Rynek | p | fair | Pewnosc | Zalezne od |
|---|---|---|---|---|---|
| MIN @ PHI | MIN ML (z OT) | 62% | 1.61 | srednia | Wallstedt vs Vladar potwierdzeni (kurs rynkowy ok. 1.62 - brak przewagi) |
| MIN @ PHI | MIN +1.5 | 82% | 1.22 | srednia | OT/pusta bramka |
| MIN @ PHI | Under 6.5 | 58.5% | 1.71 | niska-srednia | brak konkretu; Poisson zanizony ogon |
| VGK @ PIT | Over 5.5 | 62.5% | 1.60 | niska-srednia | Hill niepotwierdzony, B2B VGK |
| VGK @ PIT | puck line +1.5 (VGK/PIT) | 72-73% | 1.37-1.39 | srednia | krotki kurs |
| STL @ NYR | STL +1.5 | 74% | 1.35 | srednia | Garand .896, Hofer .916 potwierdzeni |
| STL @ NYR | Under 6.5 | 58% | 1.72 | niska-srednia | - |
Zwyciezca: ZADEN z 3 meczow nie przekracza 62% - STL@NYR i VGK@PIT to mecze 50/50 (brak mocnego typu); MIN@PHI jedyny z wyrazna przewaga (MIN 62%).
Kursy bukmacherow (Betclic/gg397) nie byly sprawdzane - w kolumnie "rynek" sa kursy Pinnacle przeliczone na p bez marzy.

To sa oszacowania probabilistyczne, nie gwarancje.

# NHL 03.11.2026 (wtorek USA, noc na 04.11 PL) - grupa 3: mecze 7-9

Skill: nhl-analyst (kroki 1-4 wg SKILL.md). Sprawdzenie bramkarzy: Daily Faceoff (strona 2026-11-03), 03.11 przed meczami; wszyscy sześciu startowi oznaczeni jako CONFIRMED przez DF. Skład może się zmienić do rozpoczęcia meczu.
Źródła: NHL API (nhl_standings, nhl_goalie_leaders, nhl_scores 02.11, nhl_player), Pinnacle (pinnacle_matchup_markets, kursy amerykańskie przeliczone na dziesiętne; Pinnacle jako rynek, marża ok. 2.5-3% zdjęta), Daily Faceoff / Squawka (WebSearch). BettingPros: nie użyty (brak klucza w sesji - pominięty). xG/CF%/GSAx: niedostępne w MCP, nie pobrane (to ogranicza pewność; λ oparte o gole/mecz, regresję do średniej ligi ~3.0 i rynek).
Początek sezonu (12-15 meczów): próba mała, liczby regresowane do średniej.
Poisson zaniża remisy po 60' (model 16-17%, rynek Pinnacle ok. 23%): w tabelach 60' podaję wartości skorygowane do ok. 22-23% remisu (oznaczone "korekta"), ML i totale z modelu skorygowane o rynek.

Skrót ligowy NHL (standings na 03.11): EDM 11-2-2 (64 GF/44 GA, 15 GP), COL 9-5-1 (64/46), NJD 9-5-0 (48/40, 14 GP), DAL 8-5-1 (38/31, 14 GP), WSH 8-5-0 (44/42, 13 GP), CBJ 5-7-0 (29/39, 12 GP).

---------------------------------------------------------------------

## 7. Dallas Stars @ Washington Capitals (04.11, 01:00 PL; wt. 03.11 19:00 ET, Capital One Arena)

**Kontekst**
- Bramkarze (DF, confirmed): DAL Jake Oettinger (7-3-1, 1.62 GAA, .921 SV%, 3 shutouty; L10 7-2-1, 1.58 GAA); WSH Logan Thompson (5-4-0, 2.92 GAA, .898 SV%; 3+ puszczone gole w 5 z ostatnich 8 meczów).
- B2B: brak informacji o B2B po żadnej stronie (żadna z drużyn nie grała 02.11 wg nhl_scores). Kontuzje: DF nie listuje istotnych; nie weryfikowałem pełnych list IR (luka).
- Forma: DAL L10 6-3-1 (seria W1), 38 GF/31 GA w 14 meczach (2.7/2.2; atak słaby, obrona i bramkarz świetne); WSH L10 6-4-0 (przegrał ostatni mecz), 44/42 w 13 (3.4/3.2; dom 6-3-0, 32 GF/30 GA u siebie). Rynek: Pinnacle ML WSH -106 / DAL -104 (praktycznie 50/50); DF: WSH -108.
- H2H: niska waga (zmiany składów), nie analizowany szczegółowo.

**Przyjęte λ (60')**: WSH 2.85, DAL 2.75 (łącznie 5.6). Uzasadnienie: DAL atak regresowany do ~2.8, ale Thompson (.898) lekko ponad średnią ligi w słabą stronę (+0.1); WSH atak 3.4 regresowany do ~3.1 vs bramkarz Oettinger (elitarny, mała próbka, regresja) i obrona DAL = -0.35, +0.1 dom. Skorygowane do rynku (total 5.5).

**Wycena (skrypt nhl_model.py 2.85 / 2.75; korekta remisu):**

| Rynek | p | fair | Rynek Pinnacle (dziesiętne) | Pewność |
|---|---|---|---|---|
| 60' 3-way: WSH / X / DAL (korekta) | 39% / 22.5% / 38.5% | 2.56 / 4.44 / 2.60 | 2.46 / 4.13 / 2.49 | średnia (3-way), niska co do typu |
| Moneyline z dogrywką: WSH / DAL | 50% / 50% | 2.00 / 2.00 | 1.94 / 1.96 | niska - brak mocnego typu |
| Puck line WSH -1.5 / DAL +1.5 | 28% / 72% | 3.57 / 1.39 | 3.36 / 1.36 | średnia dla DAL +1.5 |
| Puck line DAL -1.5 / WSH +1.5 | 25% / 75% | 4.00 / 1.33 | b/d | średnia |
| Total goli O/U 5.5 | 49% / 51% | 2.04 / 1.96 | 1.86 / 2.03 | niska |
| Total goli O/U 6.5 | 36% / 62% (cap pod rynek) | 2.78 / 1.61 | O 2.33 / U 1.65 (alt) | średnia |
| Obie strzelą (60') | ok. 86% | 1.16 | b/d | średnia, fair>1.15 granicznie |

**Rynki zawodnika/bramkarza (nie rekomendowane):**
- Obrony Oettingera: oczekiwane strzały DAL (bardzo szczelna obrona, 2.2 GA/mecz) ok. 24-27, SV% .921 regresowane do ~.912; średnia ok. 24.5-25 obron; brak 2 niezależnych źródeł liczby strzałów (tylko standings), więc tylko szkic: O 24.5 ok. 50%. Niska pewność, bez typu.
- Obrony Thompsona: oczekiwane strzały na WSH ok. 27-29 (DAL strzela dużo, ale gole słabe); O 26.5 ok. 55% szkic, niska pewność, bez typu.
- Strzelec gola/punkty/strzały: brak zweryfikowanych statystyk zawodników i składu PP z dwóch źródeł (Rantanen 17 pkt po 14 mecz, Robertson 14 pkt - tylko lista liderów NHL); bez typu.

**Typ:** brak mocnego typu na wynik (mecz wyrównany, p 50/50). Relatywnie najlepsze: **Under 6.5 gola (z dogrywką) 62%, fair 1.61, pewność średnia**; DAL +1.5 72%, fair 1.39 (pewność średnia; kurs rynkowy ok. 1.36 = brak przewagi). Oba bramkarze potwierdzeni.

**Ryzyka:** Thompson słaby (.898) - rozbicie WSH (+0.3 gola) przesuwa DAL; mała próbka Oettingera (regresja do .915); wynik 60' remis 22-23% (ryzyko dogrywki w PL +1.5 i ML); gol w pustą bramkę zawyża różnice (PL +1.5 DAL i Over). Pewność ogólna: niska-średnia.

---------------------------------------------------------------------

## 8. Colorado Avalanche @ Columbus Blue Jackets (04.11, 01:00 PL; wt. 03.11 19:00 ET, Nationwide Arena)

**Kontekst**
- Bramkarze (DF, confirmed): COL Scott Wedgewood (1-2-1, 3.47 GAA, .889 SV%, zagrał tylko 4 z 15 meczów; Blackwood grał 02.11 w Chicago); CBJ Cam Talbot (3-2-0, 2.83 GAA, .894 SV%; Greaves .883 słaby, Talbot gra dużo).
- **B2B: COL grał 02.11 (wygrana 5-2 w Chicago, Blackwood w bramce) - drugi dzień z rzędu, podróż CHI-CBJ.** CBJ nie grał 02.11 (wypoczęty). Kontuzje: DF "none listed" dla bramkarzy; pełnych list IR nie weryfikowałem.
- Forma: COL 15 meczów, 64 GF/46 GA (4.3/3.1), seria W3 (15-6 w 3 meczach), L10 6-3-1, na wyjeździe 3-4-0 (24 GF/23 GA - znacznie słabiej niż u siebie 40/23); CBJ 5-7-0, 29 GF/39 GA w 12 meczach (2.4/3.25), L10 4-6, seria L2, u siebie 4-3 (18 GF/23 GA). MacKinnon 25 pkt, Necas 18, Lehkonen 17, Makar 16 (liderzy NHL).
- H2H: niska waga, brak analizy szczegółowej.
- Rynek Pinnacle: ML COL -118 / CBJ +107 (novig ok. 52.8 / 47.2%); total 6.5 (O 2.04 / U 1.855); 3-way CBJ 2.63 / X 4.19 / COL 2.32; DF: COL -118.

**Przyjęte λ (60')**: COL 3.2, CBJ 2.9 (łącznie 6.1). Uzasadnienie: COL atak 4.3 regresowany do ~3.5, wyjazd i B2B -0.15, Wedgewood w bramce nie wpływa na własny atak; CBJ atak 2.4 regresowany do 2.7, obrona COL przy B2B +0.1, Wedgewood (.889, rezerwowy, drugi dzień B2B) +0.2 dla CBJ, dom +0.1. Wynik: COL lekki faworyt, mniejszy niż w rynku.

**Wycena (nhl_model.py 2.9 CBJ / 3.2 COL; korekta remisu):**

| Rynek | p | fair | Rynek Pinnacle | Pewność |
|---|---|---|---|---|
| 60' 3-way: COL / X / CBJ (korekta) | 42% / 23% / 35% | 2.38 / 4.35 / 2.86 | 2.32 / 4.19 / 2.63 | niska |
| Moneyline z dogrywką: COL / CBJ | 53% / 47% | 1.89 / 2.13 | 1.85 / 2.07 | niska - brak mocnego typu |
| Puck line COL -1.5 / CBJ +1.5 | 31% / 69% | 3.23 / 1.45 | 3.04 / 1.42 | średnia dla CBJ +1.5 |
| Puck line CBJ -1.5 / COL +1.5 | 22% / 78% | 4.55 / 1.28 | b/d | średnia |
| Total goli O/U 5.5 | 57% / 43% | 1.75 / 2.33 | 1.67 / 2.28 | średnia |
| Total goli O/U 6.5 | 45% / 55% | 2.22 / 1.82 | 2.04 / 1.855 | niska |
| Total goli O/U 7.5 | ok. 27% / 73% | 3.70 / 1.37 | O 3.46 / U 1.33 | niska |
| Obie strzelą (60') | ok. 90% | 1.11 | b/d | pomijać (fair <= 1.15) |

**Rynki zawodnika/bramkarza (nie rekomendowane):**
- Obrony Wedgewooda (potwierdzony, ale rezerwowy .889): strzały COL-CBJ - brak wiarygodnych danych o strzałach z dwóch źródeł; szkic ok. 27-28 strzałów na CBJ (CBJ gra defensywnie słabo, COL strzela dużo), O 25.5 obron ok. 55%, niska pewność.
- Obrony Talbota: szkic ok. 27-28 strzałów (COL B2B może strzelać mniej), SV% .894 regres. ok. .903; O 24.5 ok. 60%, niska pewność, bez typu.
- Zawodnicy: MacKinnon (25 pkt po 15 meczach) - brak zweryfikowanego gamelogu strzałów/linii PP z 2 źródeł; bez typu. Strzelec gola dla gwiazd rzadko >45%.

**Typ:** brak mocnego typu na zwycięzcę (p 53/47, rynek 52.8/47.2). Najlepszy relatywnie rynek: **Over 5.5 gola 57%, fair 1.75 (pewność średnia; rynek 1.67 - przewaga niewielka, o ok. 1pp)**; CBJ +1.5 69% (fair 1.45, kurs rynkowy 1.42). Dwaj słabi bramkarze (SV% .889 / .894) potwierdzeni - sprzyja Over; ryzyko: B2B COL = niższe tempo/strzały.

**Ryzyka:** B2B COL (słabsza obrona, ale niższa liczba strzałów); mała próbka Wedgewooda (4 mecze); CBJ najsłabszy atak ligi (29 GF w 12) - szansa na Under; remis 60' 22-23%; gol w pustą bramkę (Over/PL).

---------------------------------------------------------------------

## 9. Edmonton Oilers @ New Jersey Devils (04.11, 01:30 PL; wt. 03.11 19:30 ET, Prudential Center)

**Kontekst**
- Bramkarze (DF, confirmed): EDM Tristan Jarry (4-1-2, 2.53 GAA, .895 SV% DF / .901 NHL.com, 2 shutouty z rzędu, 42 obronione strzały z rzędu; Levi kontuzjowany na kilka tygodni - Jarry numer jeden); NJD **Connor Hellebuyck** (2-0, 1.50 GAA, .923 SV%; dołączył do NJD po 3 tygodniach sezonu - tylko 2 mecze w NJD, próbka minimalna; elitarny bramkarz w karierze). Uwaga: NHL goalie leaders pokazuje Jake'a Allena (NJD) 5 W, .887 SV% - Allen NIE startuje wg DF, więc Hellebuyck lekko podnosi NJD.
- B2B: EDM grał 31.10 (NYI) i 01.11 (NYR) - 03.11 po dniu przerwy (02.11 wolne), więc bez B2B; trzeci mecz wyjazdowy (NYI, NYR, NJD) i seria wyjazdowa, ale 7-0 na wyjeździe w sezonie. NJD nie grał 02.11. Kontuzje: Levi (EDM, multi-week); innych istotnych nie potwierdziłem (luka).
- Forma: EDM 11-2-2, 64 GF/44 GA w 15 (4.3/2.9), seria W3 (12-1 w 3 meczach), na wyjeździe 7-0, 35 GF/14 GA; McDavid 39 pkt/15 meczów (9 G, 30 A, 21% sh%), Draisaitl 28, Bouchard 26. NJD 9-5-0, 48/40 w 14 (3.4/2.9), L10 7-3, dom 6-2 (29 GF/18 GA); Jack Hughes 16 pkt.
- H2H: niska waga, nie analizowany.
- Rynek Pinnacle: ML NJD -154 / EDM +138 (novig ok. 59 / 41%); total 6.0 (O 1.917 / U 1.971; 5.5 O 1.72; 6.5 O 2.13); PL NJD -1.5 +163 / EDM +1.5 -186; 3-way NJD 2.04 / X 4.30 / EDM 3.05; DF: NJD -150.

**Przyjęte λ (60')**: NJD 3.15, EDM 2.85 (łącznie 6.0). Uzasadnienie: NJD atak 3.4 regresowany do 3.1, Jarry (.895-.901) lekko poniżej średniej +0.1, dom +0.1 -> 3.15; EDM atak 4.3 (wyniki wyjazdowe 5.0 GF/mecz zawyżone) regresowany do 3.3, Hellebuyck (elitarny, ale 2 mecze próbki; regresja) -0.25 -> ok. 3.05, wyjazd -0.1... Finalnie 2.85 po korekcie o rynek; różnica między modelem (ML NJD 54.9%) i rynkiem (59%) to ok. 4pp - akceptowalna, ML ustawiam 56.5%.

**Wycena (nhl_model.py 3.15 NJD / 2.85 EDM; korekta remisu i rynku):**

| Rynek | p | fair | Rynek Pinnacle | Pewność |
|---|---|---|---|---|
| 60' 3-way: NJD / X / EDM (korekta) | 45% / 22.5% / 32.5% | 2.22 / 4.44 / 3.08 | 2.04 / 4.30 / 3.05 | niska-średnia |
| Moneyline z dogrywką: NJD / EDM | 56.5% / 43.5% | 1.77 / 2.30 | 1.649 / 2.38 | niska-średnia |
| Puck line NJD -1.5 / EDM +1.5 | 32% / 68% | 3.13 / 1.47 | 2.63 / 1.54 | średnia dla EDM +1.5 |
| Puck line EDM -1.5 / NJD +1.5 | 24% / 76% | 4.17 / 1.32 | b/d (alt: 3.25 / 1.31 PL +/-1.5 alt) | średnia |
| Total goli O/U 5.5 | 56% / 44% | 1.79 / 2.27 | 1.72 / 2.19 | średnia |
| Total goli O/U 6.0 (push) | ok. 49% / 51% (bez zwrotu) | ok. 2.04 / 1.96 | 1.917 / 1.971 | niska |
| Total goli O/U 6.5 | 44% / 56% | 2.27 / 1.79 | 2.13 / 1.76 | niska |
| Obie strzelą (60') | ok. 90% | 1.11 | b/d | pomijać (fair <= 1.15) |

**Rynki zawodnika/bramkarza (dane tylko z NHL API; brak 2. niezależnego źródła -> bez typu):**
- McDavid (EDM, C): sezon 42 strzały/15 meczów = 2.8/mecz, ostatnie 5: 6, 3, 3, 2, 3 strzałów (średnia 3.4), TOI 19-26 min, PPP 15 pkt. Szkic: strzały średnia ok. 3.0 -> Over 2.5 55.6% (fair 1.80), Over 3.5 35% (fair 2.84); punkty: średnia ok. 1.4 (regresja z 2.6/mecz) -> Over 0.5 pkt 74.5% (fair 1.34), Over 1.5 40.5% (fair 2.47); strzelec gola ok. 31-34% (sh% 21% to szczęście, vs Hellebuyck -). Pewność niska (jedno źródło, Hellebuyck elitarny). Kolejne rynki McDavida są skorelowane.
- Obrony Hellebuycka: oczekiwane strzały EDM ok. 27-29; SV% .923 regres. ok. .912 -> ok. 26 obron; O 25.5 ok. 55%; niska pewność, bez typu.
- Obrony Jarry'ego: strzały NJD ok. 26-28 (szkic), SV% regres. ok. .902 -> ok. 25; O 24.5 ok. 55%; niska pewność, bez typu.

**Typ:** brak mocnego typu. Rynek wycenia NJD wyżej (59%) niż mój model (56.5%) - różnica 2.5pp, w tolerancji. Najlepsze relatywnie: **Over 5.5 gola 56%, fair 1.79 (pewność średnia)**, EDM +1.5 68%, fair 1.47 (kurs 1.54 -> EV +4.7% przy p 68%, ale przewaga zależy od Hellebuycka i Jarry'ego; pewność średnia, wymaga ostrożności - p wyższe niż rynek tylko o ok. 3-4pp).

**Ryzyka:** Hellebuyck - tylko 2 mecze w NJD, rotacja/forma nieznana, jedna rozbita partia zmienia total; Jarry z serią shutoutów (regresja); EDM trzeci mecz wyjazdowy z rzędu (zmęczenie podróżą: -0.1 gola już wliczone), ale 7-0 na wyjeździe; gole w pustą bramkę (Over, PL); remis 60' 22-23%.

---------------------------------------------------------------------

## Podsumowanie i kandydaci (bez fair <= 1.15)

| Mecz | Rynek | p | fair | Pewność | Zależy od | Kurs rynkowy (Pinnacle) |
|---|---|---|---|---|---|---|
| 7 DAL@WSH | Under 6.5 (z dog.) | 62% | 1.61 | średnia | bramkarze potwierdzeni (Oettinger/Thompson) | U 6.5 alt ok. 1.65 |
| 7 DAL@WSH | DAL +1.5 | 72% | 1.39 | średnia | brak rozbicia WSH, Oettinger | 1.36 |
| 8 COL@CBJ | Over 5.5 | 57% | 1.75 | średnia | Wedgewood/Talbot potwierdzeni, B2B COL | O 1.67 |
| 8 COL@CBJ | CBJ +1.5 | 69% | 1.45 | średnia | brak rozbicia COL (B2B) | 1.42 |
| 9 EDM@NJD | Over 5.5 | 56% | 1.79 | średnia | Hellebuyck/Jarry potwierdzeni | O 1.72 |
| 9 EDM@NJD | EDM +1.5 | 68% | 1.47 | średnia | Hellebuyck próbka 2 mecze | 1.54 |
| 9 EDM@NJD | NJD ML | 56.5% | 1.77 | niska-średnia | Hellebuyck | 1.649 |
| 9 EDM@NJD | McDavid O 0.5 pkt | 74.5% | 1.34 | niska | 1 źródło, brak kursu | b/d |

Wszystkie ML mieszczą się w 45-57% (hokej, wyrównane, sezon początkowy): oznaczone "brak mocnego typu". Przewagi vs rynek są małe (<=5pp) i mieszczą się w błędzie modelu; Under 4.5 nie wyceniałem (lekcja z 29-30.10).
Przypomnienie: to oszacowania probabilistyczne, nie gwarancje; bramkarze potwierdzeni na rano dnia meczu (DF), skład może się zmienić do rozpoczęcia meczu.

# NHL 03.11.2026 (wtorek USA, noc na 04.11 PL) - analiza meczów 10-11 (skill nhl-analyst)

Sprawdzenie bramkarzy i składów: 03.11.2026 rano czasu USA (Inside the Rink, Fox Sports/AP, WebSearch/DailyFaceoff-agregatory); **żaden bramkarz nie jest oficjalnie potwierdzony** - skład może się zmienić do rozpoczęcia meczu. Kursy: Pinnacle (MCP `pinnacle_matchup_markets`, przeliczone z amerykańskich, fair = po usunięciu marży) i DraftKings (Inside the Rink / Fox, 03.11 ok. 10:20 CET). Źródło statystyk: NHL.com (MCP: nhl_standings, nhl_club_schedule, nhl_goalie_leaders, nhl_skater_leaders). BettingPros: nie użyty (brak potwierdzonego klucza w sesji). xG/GSAx/PDO: brak dostępu (tylko podstawy NHL.com), obniża pewność.

---

## 10. Carolina Hurricanes @ Nashville Predators (04.11, 02:00 PL; wt. 03.11, 20:00 ET / 19:00 CT, Bridgestone Arena)

### Kontekst
- **Bramkarze (niepotwierdzeni, projekcja):** CAR Pyotr Kochetkov (SV% .929, najlepszy w czołówce ligi; rezerwa Bussi .865); NSH Juuse Saros (SV% .902, słabo; rezerwa Annunen). Oba zespoły mają 2 dni przerwy (CAR gra 01.11, NSH 31.10), więc nie ma powodu do rezerwowego; Saros wg zapowiedzi "go-to" po 2 dniach wolnego. Pewność startu: Kochetkov wysoka, Saros średnia.
- **B2B / podróż:** żaden z zespołów nie gra drugiego dnia z rzędu. CAR: 4 wygrane z rzędu (ostatnio 7-0 z WPG 01.11), seria wyjazdowa 7-? ; NSH: 5-4-5, 3 z ostatnich 10 wygranych, 3 mecze po dogrywce/karnych w 5 ostatnich.
- **Kontuzje:** CAR: Taylor Hall (LW) day-to-day, oczekiwany powrót dziś (niepewny), Jordan Staal (C) IR do 3.12, Nikishin (D) poza do 7.11. NSH: brak raportu (Nashville pozyskało Shane'a Wrighta 01.11; w pierwszych liniach Stamkos-O'Reilly-Bourque).
- **Statystyki (NHL.com):** CAR 12-2-2, 26 pkt, GF 63 (3,94/m), GA 36 (2,25/m), L10 8 W. NSH 5-4-5, GF 42 (3,00/m), GA 47 (3,36/m). Próba mała (14-16 meczów): wartości zregresowane ok. 50% do średniej ligi.
- **H2H:** brak danych z tego sezonu; waga niska.
- **Liderzy:** CAR Aho 21 pkt/16 m, Blake 16, Stankoven 15, Svechnikov 14; NSH Forsberg 17/14 m, Stamkos 16, O'Reilly 15, Josi 15.
- **Rynek (Pinnacle):** ML (z OT) CAR -196 / NSH +175 (fair CAR 64,5%); 60' 3-way CAR -121 / X +358 / NSH +252 (fair 52,1 / 20,8 / 27,1%); total 6,5 over +105 / under -118 (fair over 47,4%); puck line CAR -1,5 +127. DraftKings ML CAR -192 / NSH +160.

### Przyjęte λ (60 min)
**NSH 2,75 - CAR 3,50 (suma 6,25).** Uzasadnienie: atak CAR (zregresowany 1,15 średniej) vs obrona NSH (Saros .902, 1,07) = ok. 3,7, minus dobry Kochetkov i wyjazd = 3,5; atak NSH ~ średnia vs defensywa CAR (0,87) + własny lód = 2,65-2,75. Model (3,5 vs 2,75) dał CAR 61,9% ML, rynek 64,5%: różnica 2,6 pp (<5), więc końcowe p to uśrednienie. Zawsze zmienia liczbę: bramkarze (Kochetkov +, Saros -) zawarte w λ; Hall niepewny (-0,05 gola CAR, nie zmieniam λ, jeśli zagra).

### Wyceny (końcowe = średnia model/rynek; rynek wskazany)

| Rynek | p | fair | Pewność | Uwagi |
|---|---|---|---|---|
| **Moneyline (z OT/karnymi) CAR** | 63% | 1,59 | średnia | model 61,9%, rynek fair 64,5%; zależy od Kochetkova |
| Moneyline NSH | 37% | 2,70 | średnia | |
| **60' 3-way: CAR (1)** | 52% | 1,92 | średnia | model 53,7% / rynek 52,1% |
| 60' X (remis) | 20% | 5,00 | niska | Poisson zaniża remis (model 15,7%), użyto rynku 20,8% |
| 60' NSH (2) | 28% | 3,57 | niska | |
| Puck line CAR -1,5 (z OT) | 40% | 2,50 | niska | model 37,6%, rynek fair 42,8%; nie "bezpieczniejsze" |
| Puck line NSH +1,5 | 60% | 1,67 | średnia | |
| Puck line CAR +1,5 | 81% | 1,23 | wysoka p, krótki kurs | fair >1,15, ale blisko progu |
| Total Over 5,5 (z OT) | 59% | 1,69 | niska | rynek over 5,5 -153 => fair 58%; zgodne |
| Total Under 5,5 | 41% | 2,44 | niska | |
| Total Over 6,5 | 47% | 2,13 | niska | rynek fair 47,4% - brak przewagi |
| **Total Under 6,5** | 53% | 1,89 | niska | rynek fair 52,6%; "bez konkretu", pewność niska |
| Total Over 7,5 | 29% | 3,45 | niska | |
| Total Under 7,5 | 71% | 1,41 | niska | |
| Obie strzelą (60') | 91% | 1,10 | - | fair <1,15, pomijać |
| Total drużyny CAR Over 2,5 | 69% | 1,45 | średnia | rynek (alt) Over 2,5 -289 => fair ~72%; fair ok. 1,40-1,45 |
| Total drużyny NSH Over 1,5 | 76% | 1,32 | średnia | rynek -328 => fair ~75% |

**Rynki zawodnika (niska pewność, nie na kupon):** liczby tylko z jednego źródła (NHL.com sumy sezonu) + skład z Inside the Rink; bez drugiego niezależnego źródła i bez linii bukmachera.
- Aho punkty Over 0,5: ŚREDNIA 1,1 (zregresowane z 1,31) -> 66% (fair 1,52); Over 1,5: 30% (3,33). Strzelec gola Aho (λ 0,42): 34% (2,92).
- Stamkos/Forsberg/O'Reilly (NSH) punkty Over 0,5: średnia ok. 1,0 -> ok. 62% (1,60); NSH z λ 2,75, ale CAR to jedna z lepszych obron ligi. Strzelec gola dla gwiazd: 31-34%, nie przekracza 45%.
- Obrony bramkarza: Kochetkov (oczekiwane strzały NSH ok. 28, SV% ~.915-.92 po regresji) średnia ~26: Over 24,5 58,5% / Over 25,5 51,6% / Over 26,5 44,8%. Saros (CAR strzałowy atak ok. 30+ strzałów): średnia ~27,5: Over 25,5 61,6% / Over 26,5 54,9% / Over 27,5 48,2%. Typ możliwy dopiero po potwierdzeniu bramkarzy i linii bukmachera; rozrzut duży (sd ~6).

### Pewność i ryzyka
- **Pewność meczu: średnia.** Najlepszy rynek: **CAR ML (z OT) 63% fair 1,59** oraz **CAR 60' (1) 52% fair 1,92**; to faworyt z najlepszym bilansem w lidze (12-2-2) przeciw rywalowi z bramkarzem .902. Pułap hokejowy 65-68% - p jest poniżej.
- Ryzyka: (a) Saros "gorący" (Nashville wygrało 3 z ostatnich 10, ale 3 dogrywki - mecze wyrównane); (b) rezerwowy Bussi (.865) w bramce CAR zmieniłby p o ok. -6 pp; (c) Taylor Hall niepewny; (d) regresja CAR: bilans 12-2-2 przy GA 2,25 i serii 4 wygranych, PDO nieznane (prawdopodobnie >102 - seria częściowo szczęście, ale forma faworyta jest już w kursie); (e) dogrywka 3v3 (ok. 20% meczów) - ML i total liczone z OT, 3-way po 60'; (f) pusta bramka zawyża różnice (puck line -1,5).
- Pewność typów: ML CAR średnia; total niska (bez przewagi nad rynkiem); props niska.

---

## 11. Anaheim Ducks @ Vancouver Canucks (04.11, 03:00 PL; wt. 03.11, 21:00 ET / 18:00 PT, Rogers Arena)

### Kontekst
- **Bramkarze (niepotwierdzeni):** ANA: Lukas Dostal (SV% .872, 4-4-1, GAA 3,56; 60% projekcji FantasyHockeyLab), alternatywy Brossoit (grał w niedzielę 01.11 vs OTT - mało prawdopodobny) i Husso (SV% .857). VAN: **Thatcher Demko na IR (biodro, powrót ok. 21.12)**; projekcja Leevi Merilainen (SV% .897, lepszy z dwójki) przy Kevinie Lankinenie (SV% .812, fatalny). Pewność startu: ANA średnia, VAN średnia (Merilainen), ryzyko Lankinena = Over/ANA w górę.
- **B2B / podróż:** brak B2B u obu (ANA grał 01.11 w domu z OTT, 6-3 W; VAN 31.10 z TOR 2-4 L). ANA lecący z Kalifornii do Vancouver (1 strefa, lekka podróż); VAN gra 3. mecz w 6 dniach (wolne 01-02.11).
- **Kontuzje:** ANA: Troy Terry (RW, biodro, wraca ok. 6.11), Ian Moore (D), Poehling (C, do 25.11), Greer (LW, IR do 11.11). VAN: Demko (G), Chytil (C, ok. 7.11), Akil Thomas, MacEachern. VAN wrócił Quillan z AHL.
- **Statystyki:** ANA 6-7-1, GF 49 (3,50/m), GA 53 (3,79/m); L10 3-6-1, strzela 3,5, traci 4,0. VAN 3-12-1, GF 47 (2,94/m), GA 72 (4,50/m, najgorsza obrona ligi); L10 1-8-1, strzela 2,5, traci 4,1. Liderzy: ANA Carlsson 21 pkt/14 m (4 g + 17 a), Gauthier (5 g + 3 a w L10, hat-trick wcześniej), LaCombe 15 pkt (D); VAN E. Pettersson 16 pkt/16 m, Boeser 4 g + 5 a w L10.
- **H2H:** 27.10.2026 VAN 6-5 OT w Anaheim (Lekkerimäki 2 g). Wcześniej CAR 6-3 w Vancouver (20.10) pokazuje słabość VAN; waga H2H niska.
- **Rynek (Pinnacle):** ML (z OT) ANA -153 / VAN +138 (fair ANA 59,0%); 60' 3-way ANA +103 / X +337 / VAN +203 (fair 46,8 / 21,8 / 31,4%); total 7,0 over +120 / under -135 (fair over 44,2%); 6,5 over -138; puck line ANA -1,5 +158 / VAN +1,5 -180; team total ANA 3,5, VAN 2,5. DraftKings ANA -155 / VAN +130. Wysoki total (7,0) odzwierciedla dwóch słabych bramkarzy.

### Przyjęte λ (60 min)
**VAN 3,30 - ANA 3,55 (suma 6,85).** Uzasadnienie: obrona VAN 4,5 GA/m (zregresowane 1,25 średniej) i Merilainen .897/Lankinen .812 podnoszą ANA do ok. 3,7; atak VAN zregresowany ~0,99 x obrona ANA (3,79 GA, Dostal .872) = 3,36 + własny lód = 3,45; kompromis do rynku (suma 7,0). Bramkarz startowy zmienia λ: Lankinen w bramce VAN = +0,3 gola dla ANA; Brossoit/Husso zamiast Dostala ~ +0,1-0,2 dla VAN. Brak Terry'ego (ANA) -0,1 uwzględniony. Model dał ANA ML 53,8%, rynek 59,0%: różnica 5,2 pp - zgodnie z regułą "nie schodź pod rynek >5 pp bez konkretu", użyto 56% (konkret: oba zespoły w kryzysie L10, VAN ma lepszego bramkarza w Merilainenie niż rynek zakłada, ANA gra na wyjeździe, a Dostal .872 jest tak samo słaby).

### Wyceny

| Rynek | p | fair | Pewność | Uwagi |
|---|---|---|---|---|
| **Moneyline ANA (z OT/karnymi)** | 56% | 1,79 | niska | model 53,8%, rynek fair 59,0%; faworyt tylko z nazwy, brak mocnego typu (p 45-55% w sensie wyrównania) |
| Moneyline VAN | 44% | 2,27 | niska | |
| 60' 3-way ANA (1X2 "2") | 45% | 2,22 | niska | model 46,0%, rynek 46,8% |
| 60' X | 20% | 5,00 | niska | Poisson zaniża remis (15,5%), użyto rynku 21,8% |
| 60' VAN | 35% | 2,86 | niska | |
| Puck line ANA -1,5 | 34% | 2,94 | niska | model 31,2%, rynek 37,6% |
| Puck line VAN +1,5 | 66% | 1,52 | niska | |
| Puck line ANA +1,5 | 76% | 1,32 | średnia | |
| Puck line VAN -1,5 | 24% | 4,17 | niska | |
| Total Over 5,5 (z OT) | 68% | 1,47 | średnia | |
| Total Under 5,5 | 32% | 3,12 | niska | |
| **Total Over 6,5** | 56% | 1,79 | średnia | model 56,0%; rynek 6,5 over -138 => fair ~56%; zgodne |
| Total Under 6,5 | 44% | 2,27 | niska | |
| Total Over 7,0 (zwrot przy 7) | 44% (bez zwrotu, nie liczone) | 2,27 | niska | rynek fair 44,2% |
| Total Over 7,5 | 36% | 2,78 | niska | model 37,9%, rynek 35,2% |
| Total Under 7,5 | 64% | 1,56 | niska | |
| Total drużyny ANA Over 2,5 | 69% | 1,45 | średnia | |
| Total drużyny VAN Over 2,5 | 64% | 1,56 | niska | rynek 2,5 under -119 przy VAN o 2,5 ~ over -102 w domu? (alt: over fair ~58-60%) |
| Obie strzelą (60') | 93% | 1,07 | - | fair <1,15, pomijać |

**Rynki zawodnika (niska pewność, nie na kupon):** jedno źródło liczb (NHL.com + zapowiedzi), brak linii bukmachera i potwierdzenia bramkarzy.
- Leo Carlsson (ANA, C, PP1) punkty Over 0,5: 21 pkt w 14 m (1,5/m), średnia po regresji 1,3 -> 72% (fair 1,39); Over 1,5: 37% (2,70). Przeciwnik: najgorsza obrona ligi.
- Gauthier (ANA, PP1) strzelec gola: ~0,45 gola/m w L10 (5 g w 10) po regresji 0,40 -> 33% (3,03); LaCombe (D) punkty Over 0,5: 15 pkt w 14, ale obrońca: ~55%.
- E. Pettersson (VAN) punkty Over 0,5: 1,0/m -> 62% (1,60); Boeser strzelec ok. 30%; brak Chytila.
- Obrony: Dostal (VAN strzela ok. 27-28 strzałów) średnia ~25: Over 23,5 58,7% / Over 24,5 51,6% / Over 25,5 44,7%. Merilainen (ANA ok. 28-30 strzałów) średnia ~24,5: Over 22,5 62,3% / Over 23,5 55,2% / Over 24,5 48,1%. Tylko po potwierdzeniu startujących; rozrzut sd ~5,7.

### Pewność i ryzyka
- **Pewność meczu: niska.** Mecz dwóch drużyn w kryzysie (VAN 1-8-1 L10, ANA 3-6-1 L10) z fatalnymi bramkarzami; wynik bardziej zależy od bramkarza niż od siły. Najlepsze rynki: **Total Over 6,5 56% fair 1,79 (średnia)** i **Total Over 5,5 68% fair 1,47** (zgodne z rynkiem, bez przewagi); ML ANA 56% = brak mocnego typu.
- Ryzyka: (a) Lankinen w bramce VAN (SV% .812) - ANA ML/Over rosną (ok. +4 pp / +0,3 gola); (b) Merilainen w formie (.897 to najlepszy z dwójki) - zmniejsza total; (c) Dostal/Husso na wahnięciu; (d) powrót Terry'ego 06.11 - dziś go nie ma; (e) VAN u siebie ma 1-? bilans domowy (1 wygrana w domu), ale ANA 2-? na wyjeździe w sumie; (f) dogrywka (ostatnie spotkanie 6-5 OT) - total i ML liczone z OT; (g) pusta bramka zawyża różnice. Under 6,5/5,5 bez konkretu nie rekomendowany (Poisson zaniża ogon wysokich wyników, lekcja z 29-30.10).

---

## Skrót topów (z p, fair; fair <=1,15 pominięte)
1. Mecz 10: CAR ML (z OT) 63% / 1,59 (średnia); CAR 60' (1) 52% / 1,92 (średnia); CAR +1,5 81% / 1,23 (krótki); CAR team total Over 2,5 69% / 1,45 (średnia).
2. Mecz 11: Over 5,5 68% / 1,47 (średnia); Over 6,5 56% / 1,79 (średnia); ANA ML 56% / 1,79 (niska, brak mocnego typu); Carlsson punkty Over 0,5 72% / 1,39 (niska; warunek: Carlsson gra, linia).
Wszystko to oszacowania probabilistyczne, nie gwarancje; bramkarze mogą się zmienić do rozpoczęcia meczu.

