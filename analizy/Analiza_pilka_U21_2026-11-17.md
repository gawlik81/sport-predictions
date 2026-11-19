# Analiza piłka młodzieżowa (U21/U20) - 17.11.2026

Źródła: Superbet MCP (statystyki sezonu, H2H/forma, kursy), WebSearch (powołania PL/DE, terminarz play-offów). Godziny w czasie polskim (CET). Modele: Poisson (`poisson.py`), rożne/kartki (`markets.py`).

**Zasady wspólne dla młodzieżówek:** składy bardzo niepewne (powołania, awanse do seniorów, rotacja w towarzyskich), próbki statystyk małe (2-6 meczów, część średnich Superbet z 1-3 spotkań), sędziowie nieznani (poza Czechy-Turcja), brak potwierdzonych składów (oficjalne ~1 h przed startem). Wszystkie pewności obniżone o jeden poziom względem analiz seniorskich; maksymalna pewność to "średnia". Rynki rożne/kartki/zawodnika: brak linii i sędziów, więc brak rekomendacji.

**Ranga meczów:**
- Eliminacje ME U21 2027 (play-off, rewanże; pierwsze mecze 13.11): Czechy-Turcja (1-0 dla CZE w pierwszym), Holandia-Dania (3-0 dla NED), Irlandia-Finlandia (0-1). Kursy dotyczą 90 minut rewanżu.
- Towarzyskie: Egipt-Japonia, Chorwacja-Niemcy, Serbia-Polska (mecz w Hiszpanii, San Pedro del Pinatar, więc neutralny teren mimo statusu gospodarza), Polska U20-Rumunia U20 (U20, Superbet: Rumunia jako gospodarz), Portugalia-Norwegia, Albania-Hiszpania.

---

## 1. Czechy U21 - Turcja U21 (17:00 PL, ID 15547912) - rewanż play-off ME U21
Superbet pisze "Czechy - Turcja"; sędzia główny: Granit Maqedonci (poziom: brak danych o jego średniej kartek).
**Dane:** Czechy: gole 1.6/0.5 stracone (sezon), rożne 5.6, kartki 1.5; Turcja: 1.0/1.0, rożne 3.6, kartki 2.9. Forma CZE: W 1-0 w Turcji (13.11), P 0-2 z Portugalią, W 1-0 Bułgaria, R 1-1 Azerbejdżan, W 5-0 Gibraltar. Turcja: R 2-2 Ukraina, wcześniej W 1-0 Kosowo, P 0-3 Chorwacja.
**H2H:** 13.11.2026 Turcja 0-1 Czechy (pierwszy mecz play-off); wcześniejsze z 2013/2017 bez znaczenia.
**Kontekst:** Czechy prowadzą 1-0 w dwumeczu, Turcja musi gonić (otwarcie gry), Czechy mogą się cofnąć. λ: CZE 1.3, TUR 1.0 (zaokrąglone, rynek: CZE 45%, O2.5 ok. 44%).
| Rynek | p | fair | kurs Superbet | EV | pewność |
|---|---|---|---|---|---|
| 1 | 43.4% | 2.30 | 2.02 | -12% | niska |
| X | 28.0% | 3.58 | 3.20 | | |
| 2 | 28.6% | 3.49 | 3.50 | | |
| 1X | 71.4% | 1.40 | 1.24 | -11% | niska-średnia |
| Under 3.5 | 79.9% | 1.25 | 1.23 | -2% | średnia |
| Under 2.5 | 59.6% | 1.68 | 1.64 | -2% | niska-średnia |
| Over 1.5 | 66.9% | 1.49 | 1.35 | -10% | niska |
| BTTS nie | 54.0% | 1.85 | 1.80 | -3% | niska |
Rożne: średnia ok. 9.2 (CZE 5.6 + TUR 3.6 z krzyżowaniem), Over 9.5 = 43.6%, Under 9.5 = 56.4% (brak linii bukmachera i drugiego źródła, tylko szkic).
**Ryzyka:** rotacja/awanse do seniorów, Turcja odrabia stratę i może się otworzyć (rośnie Over/BTTS), dogrywka po remisie w dwumeczu nie wchodzi do rynków 90'.
**Brak wyraźnej przewagi nad rynkiem.**

## 2. Egipt U21 (U23) - Japonia U21 (17:00 PL, ID 15975278) - towarzyski
Superbet podaje gospodarza jako "Egipt U23" (nie U21); brak jakichkolwiek statystyk Egiptu, brak H2H. Japonia U21: 1.5 gola/mecz, 1.0 stracony; P 0-2 z Hiszpanią (13.11), W 3-0 Ukraina (czerwiec).
**Pewność: niska (brak danych o jednej drużynie).** λ: EGY 1.2, JPN 1.4 (głównie z rynku: 1 = 28%, X2 = 78%).
| Rynek | p | fair | kurs | EV | pewność |
|---|---|---|---|---|---|
| X2 | 67.8% | 1.47 | 1.28 | -13% | niska |
| Japonia wygra | 41.6% | 2.41 | 2.07 | | niska |
| Over 1.5 | 73.3% | 1.36 | 1.27 | -7% | niska |
| Under 3.5 | 73.6% | 1.36 | 1.31 | -4% | niska |
| BTTS tak | 52.6% | 1.90 | 1.72 | -10% | niska |
**Ryzyka:** nieznany skład Egiptu (U23 = mocniejsza kadra), rotacja Japonii po tournée w Europie. **Brak podstaw do typu.**

## 3. Chorwacja U21 - Niemcy U21 (18:00 PL, ID 15861872) - towarzyski, Rijeka
Trenerzy: Olić / Di Salvo. Powołania Niemiec: nowi Behrens, Hülsmann; wg Volksstimme brakuje bramkarza Backhausa i kapitana Tresoldiego (niepotwierdzone w pełnym składzie). Chorwacja: 1.7 gola/1.0 straconego; forma: P 0-1 Ukraina, W 1-0 Litwa, W 3-1 Węgry, R 2-2 Irlandia. Niemcy: P 1-2 Belgia (13.11), W 2-0 Gruzja, W 4-1 Malta, W 4-0 Łotwa; stracone 2.0/mecz (Superbet), strzały celne 7.0.
**H2H:** brak. λ: CRO 1.2, GER 1.8 (rynek: GER 51%, O2.5 ok. 58%).
| Rynek | p | fair | kurs | EV | pewność |
|---|---|---|---|---|---|
| Niemcy wygrają | 51.4% | 1.94 | 1.80 | -7% | niska-średnia |
| X2 | 74.6% | 1.34 | 1.21 | -10% | średnia |
| Over 1.5 | 80.1% | 1.25 | 1.17 | -7% | średnia |
| Over 2.5 | 57.7% | 1.73 | 1.58 | -9% | niska-średnia |
| BTTS tak | 58.3% | 1.71 | 1.56 | -9% | niska |
| Under 3.5 | 64.7% | 1.55 | 1.49 | -4% | niska |
**Ryzyka:** towarzyski, masowe zmiany po 60. minucie, Niemcy z brakami kadrowymi, Chorwacja u siebie z Olić (mocna motywacja). **Brak value.**

## 4. Serbia U21 - Polska U21 (18:00 PL, ID 15880647) - towarzyski (Hiszpania, teren neutralny)
Trenerzy: Mirković / Brzęczek. Polska: W 2-0 Norwegia (13.11, tournée w San Pedro del Pinatar), P 2-6 Włochy, W 3-0 Szwecja, W 4-1 Armenia. Brak w kadrze: Mazurek, Reguła, Abramowicz (powołani do seniorów), źródło flashscore/soccerway. Serbia (współgospodarz ME U21 2027, więc bez eliminacji): W 2-0 Macedonia Pn. (12.11), W 2-1/P 1-3 Rosja, W 3-0 Irak U23.
**H2H:** 2019-20 Serbia 1-0 Polska, Polska 1-0 Serbia (dawne, mała waga).
λ: SRB 1.3, POL 1.6. Rynek: POL 49%, O2.5 58%, BTTS 60%.
| Rynek | p | fair | kurs | EV | pewność |
|---|---|---|---|---|---|
| Polska wygra | 44.4% | 2.25 | 1.97 | -12% | niska |
| X2 | 68.9% | 1.45 | 1.27 | -12% | niska-średnia |
| Over 1.5 | 78.5% | 1.27 | 1.17 | -8% | średnia |
| Over 2.5 | 55.4% | 1.80 | 1.59 | -12% | niska-średnia |
| BTTS tak | 58.1% | 1.72 | 1.53 | -11% | niska |
| Under 3.5 | 67.0% | 1.49 | 1.48 | -1% | niska |
**Ryzyka:** to drugi mecz w 4 dni (rotacja), Serbia z własną presją "domowego" meczu, tournée w Hiszpanii. **Brak value; Under 3.5 i X2 to najbliższe rynkowi.**

## 5. Rumunia U20 - Polska U20 (18:00 PL, ID 15936553) - towarzyski U20
Superbet: Rumunia gospodarzem. Trenerzy: Curelea / Stępiński. Rumunia U20: 0.7 gola/2.3 straconego (3 mecze), P 1-3 Szwajcaria (13.11 i 31.03), P 0-1 Polska (03.2026), P 0-6 Niemcy (11.2025). Polska U20: P 1-2 Niemcy (13.11), W 2-0 Czechy, W 3-1 Portugalia, P 0-1 Niemcy, W 1-0 Rumunia.
**H2H:** Polska wygrała dwa ostatnie (1-0, 1-0), 2024 remis 1-1. λ: ROM 1.05, POL 1.5.
| Rynek | p | fair | kurs | EV | pewność |
|---|---|---|---|---|---|
| Polska wygra | 47.6% | 2.10 | 2.00 | -5% | niska |
| X2 | 73.5% | 1.36 | 1.25 | -8% | niska-średnia |
| Over 1.5 | 72.3% | 1.38 | 1.27 | -8% | niska |
| Under 3.5 | 74.7% | 1.34 | 1.31 | -2% | niska |
**Ryzyka:** U20, kadry bardzo zmienne, minimum danych. **Brak value.**

## 6. Holandia U21 - Dania U21 (18:30 PL, ID 15752261) - rewanż play-off ME U21
Pierwszy mecz: Dania 0-3 Holandia (13.11). Holandia: 2.0 gola/1.1 straconego, 6.6 strz. celnych; W 4-0 BiH, W 4-2 Słowenia, W 2-1 Belgia. Dania: 1.7/1.0, W 2-0 Białoruś, R 1-1 Austria, W 4-0 Walia.
**Kontekst:** NED prowadzi 3-0, więc motywacja i rotacja po stronie NED osłabione, Dania musi atakować (mecz otwarty, rośnie BTTS/gole). λ: NED 1.9, DEN 1.2; wg modelu NED 54%, po korekcie do rynku (59%) przyjmuję ok. 56%.
| Rynek | p | fair | kurs | EV | pewność |
|---|---|---|---|---|---|
| Holandia wygra (90') | ok. 56% | 1.79 | 1.54 | -14% | niska-średnia |
| 1X | ok. 78% | 1.28 | 1.14 | -11% | średnia |
| Over 1.5 | 81.5% | 1.23 | 1.13 | -8% | średnia |
| Over 2.5 | 59.9% | 1.67 | 1.48 | -11% | niska-średnia |
| BTTS tak | 59.4% | 1.68 | 1.57 | -7% | niska |
| Under 3.5 | 62.5% | 1.60 | 1.59 | -1% | niska |
Rożne: średnia ok. 10.6 (NED 6.0, DEN 5.6), Over 10.5 = 48.3% (szkic, brak linii).
**Ryzyka:** wysoka przewaga w dwumeczu = ryzyko rotacji i "wolnego" tempa NED. **Brak value.**

## 7. Portugalia U21 - Norwegia U21 (18:30 PL, ID 15804851) - towarzyski
Portugalia: W 1-0 Anglia (13.11), W 2-0 Czechy, W 4-0 Gibraltar, P 1-2 Bułgaria. Norwegia: P 0-2 Polska (13.11), R 1-1 Izrael, W 6-1 BiH. H2H: Portugalia 6 wygranych, 1 remis w historii (ostatnio 3-0 w 2023, 4-1 w 2020).
λ: POR 2.0, NOR 1.1 (rynek: POR 58%, O2.5 60%).
| Rynek | p | fair | kurs | EV | pewność |
|---|---|---|---|---|---|
| Portugalia wygra | 58.2% | 1.72 | 1.57 | -9% | średnia |
| 1X | 79.6% | 1.26 | 1.14 | -9% | średnia |
| Over 1.5 | 81.5% | 1.23 | 1.15 | -6% | średnia |
| Over 2.5 | 59.9% | 1.67 | 1.52 | -9% | niska-średnia |
| BTTS tak | 57.7% | 1.73 | 1.58 | -9% | niska |
| Under 3.5 | 62.5% | 1.60 | 1.54 | -4% | niska |
**Ryzyka:** rotacja, krótkie odległości. **Brak value (rynek wycenia podobnie).**

## 8. Irlandia U21 - Finlandia U21 (18:45 PL, ID 15752262) - rewanż play-off ME U21
Pierwszy mecz: Finlandia 1-0 Irlandia (13.11). Irlandia: 1.5/1.4, W 3-1 Anglia, W 4-3 Kazachstan, W 2-0 Słowacja, R 2-2 Chorwacja. Finlandia: 3.2 gola/0.6 straconego (silnie zawyżone słabymi grupami), R 4-4 Kosowo, W 2-0 Rumunia, W 2-1 Hiszpania, W 2-0 Norwegia.
**Kontekst:** Irlandia u siebie musi odrobić 0-1, Finlandia może grać z kontry; rynek daje Finlandii minimalną przewagę (38% vs 33%). λ: IRL 1.3, FIN 1.4.
| Rynek | p | fair | kurs | EV | pewność |
|---|---|---|---|---|---|
| 1 / X / 2 | 34.8 / 25.8 / 39.4% | 2.87 / 3.88 / 2.54 | 2.75 / 3.20 / 2.42 | -4% / | niska |
| X2 | 65.2% | 1.53 | 1.38 | -10% | niska |
| Over 1.5 | 75.1% | 1.33 | 1.29 | -3% | średnia |
| Over 2.5 | 50.6% | 1.98 | 1.92 | -3% | niska |
| BTTS tak | 54.8% | 1.82 | 1.73 | -5% | niska |
| Under 3.5 | 71.4% | 1.40 | 1.29 | -8% | niska |
**Ryzyka:** wyrównany mecz (brak mocnego typu), dogrywka i karne nie wchodzą w rynek 90'. **Brak mocnego typu.**

## 9. Albania U21 - Hiszpania U21 (19:00 PL, ID 15861871) - towarzyski
Albania (współgospodarz ME U21 2027): W 3-1 Luksemburg (13.11), R 2-2 Ukraina, P 0-1 Włochy. Hiszpania: W 2-0 Japonia (13.11), W 7-1 Rumunia, W 13-0 San Marino, P 1-2 Finlandia (25.09). H2H: 4 wygrane Hiszpanii, ostatnie 2018.
λ: ALB 0.7, ESP 2.4 (rynek: ESP 74%, Albania 10%).
| Rynek | p | fair | kurs | EV | pewność |
|---|---|---|---|---|---|
| Hiszpania wygra | 75.1% | 1.33 | 1.23 | -8% | średnia |
| X2 | 91.0% | 1.10 | 1.03 | pominąć (fair <1.15) | |
| Over 1.5 | 81.5% | 1.23 | 1.18 | -4% | średnia |
| Over 2.5 | 59.9% | 1.67 | 1.59 | -5% | niska-średnia |
| BTTS nie | 54.2% | 1.84 | 1.60 | -13% | niska |
| Under 3.5 | 62.5% | 1.60 | 1.46 | -9% | niska |
**Ryzyka:** rotacja Hiszpanii po sezonie klubowym, domowa publiczność Albanii. **Brak value.**

---

## Podsumowanie
Żaden rynek młodzieżowy nie ma EV > 0 względem kursów Superbet przy moich p (rynki bliskie fair: Under 3.5 w CZE-TUR, NED-DEN, SRB-POL, ROM-POL U20; Over 1.5 w IRL-FIN), a pewność ograniczona przez składy, próbki i brak sędziów. Rekomendacja: do kuponów nie używać nóg wynikowych z tej puli, ewentualnie traktować Under 3.5 / Over 1.5 jako wypełnienie przy EV zbliżonym do 0 (poziom -1, tylko za zgodą użytkownika).

To oszacowania probabilistyczne, nie gwarancje.
