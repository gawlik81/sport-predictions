# TOP 10 predykcji dnia — środa, 30.09.2026

Użyte skille: football-predictor, tennis-predictor i esports-predictor.
**W piłce nożnej są tylko typy „over”** (gole, rożne, faule), zgodnie z prośbą.

**Źródło kursów:** betclic.pl jest zablokowany przez proxy tego środowiska. Kursy 1X2 biorę z zapowiedzi, które je cytują, na przykład STS dla Polska U21–Szwecja U21 (1,65 / 4,00 / 4,75). Kursów Betclic na linie over nie znalazłem, więc podaję kurs fair. **Typ ma value, jeśli kurs w Betclic jest wyższy od kursu fair.** Stan na ok. 06:45.

**Oferta dnia:**
- **Piłka nożna.** Liga Narodów ma dziś przerwę (3. kolejka od 1.10), a ligi klubowe stoją z powodu przerwy reprezentacyjnej. W ofercie są:
  - kwalifikacje ME U21: Polska–Szwecja i Malta–Niemcy (oba o 18:00);
  - Liga Mistrzyń, 2. kolejka: Roma–Barcelona, Häcken–Juventus, Paris FC–Arsenal (wszystkie 18:45), OL Lyonnes–Chelsea i Benfica–Bayern (oba 21:00).
- **Tenis.** Pierwsza runda ATP 500 w Pekinie i Tokio oraz WTA 1000 w Pekinie. Sesje dzienne zaczęły się o 04:00 i 05:00 CEST, więc większość meczów już trwa. Kolejność gier sesji wieczornych nie była jeszcze opublikowana. Mecz Alcaraz–Michelsen jest 1.10 o 04:00 CEST, czyli nie dziś.
- **E-sport.** Jedyne większe rozgrywki to igrzyska azjatyckie (LoL, reprezentacje narodowe, 29.09–2.10). To nie jest tier-1 klubowy i nie mam danych o składach ani formie. Zgodnie z regułami 7-8 esports-predictor nie typuję.

**Dlatego cała dzisiejsza dziesiątka to piłkarskie typy over na gole.**
- **Rożne:** dla meczów U21 i kobiet nie znalazłem żadnych danych.
- **Faule:** też brak danych.

Model z samej średniej byłby fałszywą precyzją, więc typów na rożne i faule nie ma.

**Zasady rankingu:**
- Uwzględnia tylko typy z kursem fair powyżej 1,15. Dlatego odpadają Over 0,5 gola (91-97%) i Over 1,5 w meczu Malta–Niemcy U21 (86,9%, kurs fair 1,151, na granicy progu).
- **Kalibracja:** reguły kalibracji skilla piłkarskiego pochodzą z meczów seniorów. Piłka kobieca i U21 mają większe różnice klas i więcej goli, ale model nie był na nich weryfikowany. Pewność najwyżej średnia/wysoka.

## Ranking

| # | Mecz | Godz. | Typ | Prawd. | Kurs (fair) | Pewność | Kluczowe ryzyko |
|---|------|-------|-----|--------|-------------|---------|-----------------|
| 1 | Benfica – Bayern (LM kobiet) | 21:00 | **Over 1,5 gola** | 85,3% | 1,17 | Średnia/Wysoka | Bayern (kurs ok. 1,29) zremisował 2-2 z Man City, tracąc prowadzenie 2-0. Benfica wygrała wszystkie mecze w sezonie (5-1 z Porto, 2-1 w Turynie). Zapowiedź typuje Over 3 gole po 1,84, czyli rynek też oczekuje otwartego meczu. Ryzyko: Bayern kontroluje mecz i wygrywa 1-0 |
| 2 | Malta U21 – Niemcy U21 | 18:00 | **Niemcy U21 powyżej 1,5 gola** | 84,1% | 1,19 | Średnia/Wysoka | Malta przegrała wszystkie 8 meczów kwalifikacji i traci średnio 4 gole na mecz. Niemcy muszą wygrać, bo w walce o 1. miejsce z Grecją liczy się bilans bramek. Ryzyko: rotacja w składzie Niemiec i mur Malty na własnym boisku |
| 3 | Roma – Barcelona (LM kobiet) | 18:45 | **Over 1,5 gola** | 80,8% | 1,24 | Średnia/Wysoka | Barcelona (kurs 1,02-1,11) wygrała wszystkie 3 mecze z Romą przy bilansie 10-1 i 6 kolejnych meczów w sezonie. Roma zaczęła od 0-0 z Leuven. Ryzyko: Roma broni się nisko, a Barcelona wygrywa 1-0 lub 2-0 (w ostatnim meczu 2-0 z Logroño) |
| 4 | OL Lyonnes – Chelsea (LM kobiet) | 21:00 | **Over 1,5 gola** | 76,9% | 1,30 | Średnia | Hit kolejki: Bompastor wraca do Lyonu. Kurs 1,55 / 4,00 / 5,50. Zapowiedzi typują 2-1 w obu kierunkach. Ryzyko: zamknięty, taktyczny mecz dwóch faworytów |
| 5 | Polska U21 – Szwecja U21 | 18:00 | **Over 1,5 gola** | 75,1% | 1,33 | Średnia | Polska wygrała 8 z 8 meczów, w tym 6-0 w Szwecji. Kurs 1,65 / 4,00 / 4,75 (STS). Ryzyko: Polska jest blisko awansu i może kontrolować wynik, a Szwecja zagra ostrożniej po 0-6 |
| 6 | Paris FC – Arsenal (LM kobiet) | 18:45 | **Over 1,5 gola** | 75,1% | 1,33 | Średnia | Zapowiedź typuje 1-1. Arsenal wygrał 3 z 16 meczów z francuskimi drużynami, a Paris FC przegrał 5 z 6 meczów z angielskimi. Ryzyko: wyrównany mecz na 1-0 |
| 7 | Häcken – Juventus (LM kobiet) | 18:45 | **Over 1,5 gola** | 71,3% | 1,40 | Średnia | Häcken przegrał 0-1 z Interem, mając 39% posiadania piłki, a Juventus przegrał 1-2 z Benficą. Obie drużyny muszą zdobyć punkty. Zapowiedź typuje BTTS. **Kursów 1X2 nie znalazłem**, więc λ jest luźniejsze |
| 8 | Malta U21 – Niemcy U21 | 18:00 | **Over 2,5 gola** | 68,8% | 1,45 | Średnia | Skorelowane z #2. Wchodzi dopiero, gdy Niemcy strzelą 3 gole albo gdy Malta strzeli honorowego (Malta ma 1 gola w 8 meczach) |
| 9 | Benfica – Bayern (LM kobiet) | 21:00 | **Over 2,5 gola** | 66,0% | 1,52 | Średnia/Niska | Skorelowane z #1. Rynek: Over 3 @1,84 |
| 10 | Roma – Barcelona (LM kobiet) | 18:45 | **Barcelona powyżej 1,5 gola** | 75,1% | 1,33 | Średnia | Skorelowane z #3. Umieszczone na końcu, bo typ #3 wchodzi też przy wyniku 1-1 |

**Oczekiwana liczba trafień: ok. 7,6 z 10.** Na liście są trzy pary skorelowanych typów (#1 z #9, #2 z #8, #3 z #10), więc wariancja jest wyraźnie wyższa niż przy typach niezależnych. Najbardziej niezależna wersja to #1-#7.

## Skrót — piłka nożna (model Poissona)

| Mecz | λ gole | 1X2 (%) | O1,5 | O2,5 | O3,5 | BTTS | Kurs 1X2 |
|---|---|---|---|---|---|---|---|
| Malta U21 – Niemcy U21 | 0,25 : 3,30 | 1,2 / 5,8 / 87,9 | 86,9% | 68,8% | 47,4% | 20,2% | brak |
| Polska U21 – Szwecja U21 | 1,80 : 0,90 | 58,4 / 22,9 / 18,5 | 75,1% | 50,6% | 28,6% | 49,4% | 1,65 / 4,00 / 4,75 (STS) |
| Roma – Barcelona (W) | 0,35 : 2,70 | 3,0 / 10,4 / 84,5 | 80,8% | 58,8% | 36,4% | 26,9% | Barcelona 1,02-1,11 |
| Häcken – Juventus (W) | 1,20 : 1,30 | 34,1 / 27,0 / 38,9 | 71,3% | 45,6% | 24,2% | 50,8% | brak |
| Paris FC – Arsenal (W) | 1,10 : 1,60 | 26,1 / 24,9 / 48,8 | 75,1% | 50,6% | 28,6% | 53,1% | brak |
| OL Lyonnes – Chelsea (W) | 1,80 : 1,00 | 55,9 / 23,1 / 20,8 | 76,9% | 53,0% | 30,8% | 52,6% | 1,55 / 4,00 / 5,50 |
| Benfica – Bayern (W) | 1,20 : 2,20 | 19,9 / 20,0 / 59,3 | 85,3% | 66,0% | 44,2% | 61,6% | Bayern ok. 1,29 |

**Uwagi do modelu:**
- **Brak danych sezonowych.** Nie było danych ligowych w formacie „siła ataku/obrony”, więc λ szacowałem z formy, H2H i rynku (Krok 2, „luźniejsze oszacowanie”).
- **Benfica – Bayern:** 1X2 z modelu (Bayern 59%) jest poniżej rynku (ok. 75%). Dla typów over to nieistotne. Przy λ Bayernu podniesionym do dopasowania z rynkiem Over 1,5 tylko rośnie, więc liczba z modelu jest zachowawcza.
- **Rożne i faule:** dla żadnego z 7 meczów nie znalazłem średnich rożnych ani fauli (ani jednego źródła). Zgodnie z Krokiem 1 zaznaczam to wprost i nie podaję linii.

## Tenis i e-sport — dlaczego brak typów

- **Pekin (ATP 500 i WTA 1000) i Tokio (ATP 500), 1. runda:**
  - dzienne sesje trwały już w chwili analizy, a pierwszy na korcie centralnym w Pekinie był Chaczanow–Auger-Aliassime;
  - kolejność gier sesji wieczornych nie była opublikowana;
  - dla zawodników pierwszej rundy nie zebrałem statystyk serwisu i returnu, więc total gemów i tak nie mógłby wejść do rankingu (reguła 4).
- **Alcaraz – Michelsen** gra 1.10 o 04:00 CEST. Rynek daje Alcarazowi ok. 1,19-1,20, a zapowiedzi typują Over 21,5 gema. Mogę to przeanalizować jutro.
- **LoL na igrzyskach azjatyckich:** reprezentacje narodowe bez historii i statystyk, więc zgodnie z regułami 7 i 8 esports-predictor bez typów.

---
Źródła:
- [matchday.pl, program 30.09](https://matchday.pl/2026/09/29/30-09-26-sroda-pilka-nozna-w-tv/)
- [Yahoo/Bulinews, Malta U21–Niemcy U21](https://bulinews.com/malta-u21-germany-u21-preview-team-news-and-predicted-lineups)
- [Meczyki, Polska U21–Szwecja U21](https://www.meczyki.pl/typy-bukmacherskie/polska-u21-szwecja-u21/6029408)
- [TVP Sport, Polska U21–Szwecja U21](https://sport.tvp.pl/95584062/polska-u21-szwecja-u21-na-zywo-transmisja-meczu-el-me-u21-online-live-stream-30092026-gdzie-ogladac)
- [Tips.GG, Roma–Barcelona](https://tips.gg/article/roma-w-vs-barcelona-w-30-09-2026/)
- [Everything Barca, Roma–Barcelona](https://everythingbarca.com/roma-vs-barca-femeni-womens-champions-league-preview-predictions-team-news-and-tv-info)
- [Dailysports, Häcken–Juventus](https://dailysports.net/predictions/hcken-w-vs-juventus-w-prediction-who-will-claim-the-first-points/)
- [Yahoo, Paris FC–Arsenal](https://sports.yahoo.com/articles/paris-fc-vs-arsenal-womens-215036614.html)
- [The Pride of London, OL Lyonnes–Chelsea](https://theprideoflondon.com/ol-lyonnes-vs-chelsea-women-s-champions-league-preview-predictions-team-news-and-tv-info)
- [Dailysports, Benfica–Bayern](https://dailysports.net/predictions/benfica-have-won-every-match-this-season-but-historically-struggle-against-bayern-prediction-for-benfica-w-bayern-w/)
- [FC Bayern, zapowiedź](https://fcbayern.com/frauen/en/news/previews/2026/09/preview-benfica-vs.-fc-bayern-women-uwcl-md-2)
- [UEFA, 2. kolejka LM kobiet](https://www.uefa.com/womenschampionsleague/news/02a9-21acecc8532e-02077a71aac9-1000--uefa-women-s-champions-league-matchday-2-preview-ol-lyonn/)
- [Bleacher Nation, Pekin 30.09](https://www.bleachernation.com/how-to-watch/2026/09/29/china-open-schedule-wednesday-september-30-matchups-tv-live-stream-info/)
- [ATP, drabinka Tokio](https://www.atptour.com/en/news/tokyo-2026-draw-preview)
- [Dimers, Alcaraz–Michelsen](https://www.dimers.com/tennis/news/carlos-alcaraz-vs-alex-michelsen-tennis-prediction-atp-japan-open-2026-ac)
- [Sheep Esports, igrzyska azjatyckie](https://www.sheepesports.com/en/articles/asian-games-2026-esports-schedule-and-participants/en)

*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
