# TOP 10 predykcji dnia — wtorek, 29.09.2026

Użyte skille: football-predictor, tennis-predictor i esports-predictor.
**W piłce nożnej są tylko typy „over”** (gole, rożne, faule), zgodnie z prośbą.

**Źródło kursów:** betclic.pl jest zablokowany przez proxy tego środowiska. Kursy 1X2 biorę z polskich i zagranicznych zapowiedzi (średnie rynkowe). Kursów Betclic na linie over (gole, rożne, faule) nie udało się znaleźć, więc przy typach podaję tylko kurs uczciwy (fair). **Typ ma value, jeśli kurs w Betclic jest wyższy od kursu fair.** Stan na ok. 07:30.

**Oferta dnia:**
- **Piłka nożna, 2. kolejka Ligi Narodów:**
  - 18:00: Mołdawia–Wyspy Owcze, Finlandia–Białoruś;
  - 20:45: Czechy–Anglia, Hiszpania–Chorwacja, Szkocja–Szwajcaria, Słowacja–Kazachstan, San Marino–Albania, Bułgaria–Estonia, Słowenia–Macedonia Płn., Luksemburg–Islandia.
- **Tenis, finały ATP 250 (kort twardy):**
  - Chengdu, ok. 13:00: Hurkacz [5]–Davidovich Fokina [2];
  - Hangzhou, ok. 13:30: Miedwiediew [1]–Rublow [2].
- **E-sport:** nie znalazłem dziś meczów tier-1. LCK i LEC skończyły sezon, PGL Wallachia S9 już się zakończył, a LCS gra 3–4.10.

**Zasady rankingu:**
- Uwzględnia tylko typy z kursem fair powyżej 1,15. Dlatego odpadają m.in. Over 0,5 gola: 88-94% w modelu, ale kurs fair 1,06-1,14.
- Dla Over goli biorę model bazowy. Weryfikacje z 24 i 26.09 pokazały, że model zaniża gole w meczach reprezentacji o ok. 0,3 na mecz, więc liczby są raczej zachowawcze.
- Rożne w meczach reprezentacji mam tylko z jednego źródła. Dlatego obcinam je o 7-8 pp i daję najwyżej średnią pewność (reguła 4 z Kroku 2b).
- W tenisie statystyki serwisu Hurkacza, Rublowa i Davidovicha są szacowane. Zgodnie z regułą 4 tenisowego Kroku 2b total gemów nie wchodzi do rankingu. W rankingu jest tylko +1,5 seta.

## Ranking

| # | Mecz | Godz. | Typ | Prawd. | Kurs (fair) | Pewność | Kluczowe ryzyko |
|---|------|-------|-----|--------|-------------|---------|-----------------|
| 1 | Hiszpania – Chorwacja | 20:45 | **Over 1,5 gola** | 77,7% | 1,29 | Średnia/Wysoka | Hiszpania wygrała MŚ bez straty gola w 5 meczach, więc możliwe jest 1-0. Za typem: w 5 z 6 ostatnich meczów H2H padły co najmniej 3 gole, a Hiszpania wygrała 3-2 z Anglią. Hiszpanii brakuje Erica Garcii, Porro i Gaviego, Chorwacji Baturiny i Erlicia |
| 2 | San Marino – Albania | 20:45 | **Over 1,5 gola** | 76,9% | 1,30 | Średnia/Wysoka | Albania (kurs ok. 1,05) wygrała 4 mecze H2H z bilansem 13-0. Ryzyko: skromne 0-1, bo Albania wygrywa zwykle niewysoko (2-0 z Białorusią). λ dopasowane do rynku, bez podłogi 0,7 dla San Marino (reguła 5) |
| 3 | Czechy – Anglia | 20:45 | **Over 1,5 gola** | 76,0% | 1,32 | Średnia/Wysoka | Czechy mają 7 wycofanych z kadry (m.in. Chorý, Provod, Jurásek) i nie grają Schick ani Souček. Anglia na wyjazdach strzela średnio 3,1 gola. Kane nie strzelił karnego z Hiszpanią (2-3). Ryzyko: Anglia wygrywa 1-0 |
| 4 | Czechy – Anglia | 20:45 | **Over 6,5 rzutu rożnego** | ~75% (model 83,5%) | 1,33 | Średnia | λ rożnych 3,6 : 5,9. Czechy 5,9 i Anglia 5,1 rożnego wywalczonego na mecz (**jedno źródło**, bez rozbicia na dom i wyjazd), korekta za dominację Anglii. Wynik skorelowany z #3 |
| 5 | Hiszpania – Chorwacja | 20:45 | **Over 6,5 rzutu rożnego** | ~74% (model 81,9%) | 1,35 | Średnia | λ rożnych 6,3 : 3,0. Hiszpania średnio 8,6 rożnego łącznie w meczu w 10 ostatnich meczach (TotalCorner, jedno źródło). Superbet proponuje w bet builderze Under 10,5, co zgadza się z oczekiwanym totalem ~9,3 |
| 6 | Hurkacz – Davidovich Fokina | ok. 13:00 | **Hurkacz +1,5 seta** | ~72% (model 77,8%) | 1,39 | Średnia | Mecz bliski remisu: model 54,3% dla Hurkacza, rynek 52-57%. H2H 4-2 dla Davidovicha. Hurkacz grał 3 sety w półfinale (6-7 6-3 6-3) i to jego pierwszy finał od maja 2025. Nowych kontuzji nie znalazłem (reguła 8). p_serve szacowane, więc obciąłem 6 pp |
| 7 | Finlandia – Białoruś | 18:00 | **Over 1,5 gola** | 71,3% | 1,40 | Średnia | Białoruś nie przegrała 7 meczów i 4 wyjazdów, ale seria ma małą moc predykcyjną (reguła 7). Finlandia w 10 meczach strzelała i traciła średnio po 1,7 gola, a na San Marino wygrała 7-0. Ryzyko: Białoruś broni się nisko (0-2 z Albanią) |
| 8 | Luksemburg – Islandia | 20:45 | **Over 1,5 gola** | 70,2% | 1,42 | Średnia | Ostatnie 2 mecze H2H: 3-1 i 1-1. Luksemburg wygrał 2-1 w Bułgarii, Islandia zremisowała 1-1 z Estonią. Ryzyko: Islandia w 3 z 5 meczów przed LN nie strzeliła gola |
| 9 | Szkocja – Szwajcaria | 20:45 | **Over 1,5 gola** | 66,9% | 1,49 | Średnia/Niska | Szkocja nie strzeliła gola w Słowenii (0-0) i ma nowego trenera Pocognoliego oraz 7 debiutantów. Szwajcaria gra bez Xhaki, Sommera, Akanjiego i Schära, a to raczej osłabia obronę niż atak |
| 10 | Miedwiediew – Rublow | ok. 13:30 | **Rublow +1,5 seta** | ~65% (model 76,3%) | 1,54 | Średnia/Niska | **Model 48% dla Miedwiediewa, rynek ok. 65%**. Zgodnie z regułą 1 (faworyt z top-20, model ≥10 pp poniżej rynku) nie typuję Rublowa na zwycięstwo, tylko +1,5 seta, i obcinam go do blendu z rynkiem. H2H 7-2 dla Miedwiediewa |

**Oczekiwana liczba trafień: ok. 7,3 z 10.** Pary #1 i #5 oraz #3 i #4 dotyczą tych samych meczów.

## Faule — dlaczego nie ma typu

Jedyne znalezione dane o faulach (Czechy–Anglia: „Anglia 11, Czechy 6 fauli na mecz”) pochodzą z jednej zapowiedzi, bez rozbicia na faule popełnione i wymuszone. Dla reprezentacji nie ma dostępu do FBref (403). Nie da się więc zbudować modelu z Kroku 6a na takiej podstawie, a strzelanie linii „na oko” byłoby fałszywą precyzją. **Typ na faule: brak.** Oczekiwana liczba kartek w Czechy–Anglia to 3-5, z zastrzeżeniem, że sędzia nie jest znany.

## Świadomie pominięte (tylko rynki over)

- **Słowacja – Kazachstan: Over 1,5** ma w modelu 63,3%. Under 2,5 padł w 14 z 16 ostatnich meczów obu drużyn w tych rozgrywkach, a Kazachstan zremisował 1-1 z Wyspami Owczymi. Za nisko do rankingu.
- **Bułgaria – Estonia: Over 1,5** 64,5% oraz **Słowenia – Macedonia Płn.: Over 1,5** 62,0%. Rynek też skłania się ku Under 2,5 (Bułgaria–Estonia: Under @1,65). Słowenia zremisowała 0-0 ze Szkocją.
- **Mołdawia – Wyspy Owcze: Over 1,5** 62,0% (λ 1,15 : 0,95). W 5 ostatnich meczach obu drużyn padało średnio 2,6 gola, ale Mołdawia nie strzeliła gola w Słowacji.
- **Szkocja – Szwajcaria, rożne:** nie mam danych o rożnych dla żadnej z drużyn. Model z samej średniej ligowej daje O6,5 81%, ale to czysty szacunek, więc do rankingu nie wchodzi.
- **Over 2,5 gola:** najwyżej 54% (Hiszpania–Chorwacja), więc poniżej progu.
- **Tenis, total gemów:** Hurkacz–Davidovich Over 21,5 ma w modelu 73,4% (oczekiwane 26,2 gema), Miedwiediew–Rublow Over 21,5 69,1% (oczekiwane 25,6). Oba pominięte zgodnie z regułą 4, bo p_serve jest szacowane. Rynek ustawia linię Miedwiediew–Rublow na 23,5, a Dimers daje Under 24,5 59%.

## Skrót — piłka nożna (model Poissona)

| Mecz | λ gole | 1X2 (%) | O1,5 | O2,5 | O3,5 | Rynek 1X2 |
|---|---|---|---|---|---|---|
| Mołdawia – Wyspy Owcze (18:00) | 1,15 : 0,95 | 40,2 / 29,8 / 30,0 | 62,0% | 35,0% | 16,1% | 2,37 / 3,05 / 3,20 |
| Finlandia – Białoruś (18:00) | 1,55 : 0,95 | 51,2 / — / — | 71,3% | 45,6% | — | Finlandia ok. 1,70 |
| Czechy – Anglia | 0,85 : 1,90 | 16,2 / 21,7 / 61,7 | 76,0% | 51,8% | 29,7% | 6,33 / 4,60 / 1,47 |
| Hiszpania – Chorwacja | 2,10 : 0,75 | 68,1 / 19,2 / 12,2 | 77,7% | 54,2% | 31,9% | ok. 1,25-1,30 |
| Szkocja – Szwajcaria | 0,95 : 1,35 | 26,4 / 27,6 / 45,9 | 66,9% | 40,4% | 20,1% | Szwajcaria ok. 1,90 |
| Słowacja – Kazachstan | 1,70 : 0,45 | 68,1 / 22,4 / 9,3 | 63,3% | 36,4% | 17,1% | Słowacja wyraźnym faworytem |
| San Marino – Albania | 0,20 : 2,60 | 1,7 / 9,7 / 86,9 | 76,9% | 53,0% | 30,8% | 60 / 12 / 1,05 |
| Bułgaria – Estonia | 1,50 : 0,70 | 56,4 / 26,2 / 17,4 | 64,5% | 37,7% | 18,1% | 1,58 / 3,60 / 6,60 |
| Słowenia – Macedonia Płn. | 1,40 : 0,70 | 53,7 / 27,5 / 18,7 | 62,0% | 35,0% | 16,1% | 1,72 / 3,68 / 5,00 |
| Luksemburg – Islandia | 1,10 : 1,35 | 30,5 / 27,1 / 42,4 | 70,2% | 44,3% | 23,2% | brak kursów |

**Rożne (model, jedno źródło danych):**

| Mecz | λ rożne | O6,5 | O7,5 | O8,5 | O9,5 |
|---|---|---|---|---|---|
| Czechy – Anglia | 3,6 : 5,9 | 83,5% | 73,1% | 60,8% | 47,8% |
| Hiszpania – Chorwacja | 6,3 : 3,0 | 81,9% | 71,0% | 58,3% | 45,2% |
| Szkocja – Szwajcaria | 4,3 : 4,9 (szacunek) | 81,1% | 69,9% | 57,0% | 43,9% |

**Korekty λ goli:**
- Czechy: -10%, bo brakuje wielu graczy (7 wycofanych, Schick i Souček).
- Anglia: bez korekty.
- Hiszpania: bez korekty. Braki w obronie (Eric Garcia, Porro) nie osłabiają ataku.
- Szkocja: λ 0,95, nie niżej. To mecz podobnego poziomu, więc obowiązuje podłoga ~0,7, a 0-0 w Słowenii to jeden mecz.
- San Marino i Kazachstan: λ poniżej 0,7, dopasowane do rynku (reguła 5, mecze dużej różnicy klas).

## Skrót — tenis (model punkt→gem→set→mecz, p_serve szacowane)

| Mecz | p_serve A : B | Wygrana A (model) | Rynek | A +1,5 seta | B +1,5 seta | Oczek. gemy | O21,5 / O22,5 / O23,5 |
|---|---|---|---|---|---|---|---|
| Hurkacz – Davidovich Fokina | 0,669 : 0,660 | 54,3% | Hurkacz 1,68-1,75 | 77,8% | 72,0% | 26,2 | 73,4% / 64,1% / 56,7% |
| Miedwiediew – Rublow | 0,632 : 0,636 | 48,0% | Miedwiediew ok. 1,45-1,51 | 73,6% | 76,3% | 25,6 | 69,1% / 61,2% / 54,8% |

**Dane wejściowe:**
- Miedwiediew: SPW 65,2%, RPW 38,4% (Tennis Abstract, twarda, z raportu 26.09).
- Rublow, Hurkacz i Davidovich: szacunki z rankingu i fragmentarycznych statystyk sezonu (m.in. hold Rublowa 85,7% z top-50, 1. serwis Davidovicha 68,5%, 1. serwis Hurkacza 61,2%).

**Rozliczenie wczoraj:**
- Hurkacz pokonał Shapovalova 6-7(8) 6-3 6-3.
- Rublow pokonał Jacqueta 7-6(0) 6-1, co dało mu 400. zwycięstwo w karierze.
- Miedwiediew pokonał Safiullina.

---
Źródła:
- [matchday.pl, terminarz 29.09](https://matchday.pl/2026/09/28/29-09-26-wtorek-pilka-nozna-w-tv/)
- [mecze24, Czechy–Anglia](https://www.mecze24.pl/typy-bukmacherskie/anglia-czechy/3650163)
- [Football365, Czechy–Anglia](https://www.football365.com/match-preview/czech-republic-v-england-prediction-preview)
- [Sports Gambler, Czechy–Anglia](https://www.sportsgambler.com/betting-tips/football/czech-republic-vs-england-prediction-lineups-odds-2026-09-29/)
- [Al Jazeera, Hiszpania–Chorwacja](https://www.aljazeera.com/sports/2026/9/28/spain-croatia-uefa-nations-league-yamal-modric-teams-form)
- [bet.pl, Hiszpania–Chorwacja](https://bet.pl/hiszpania-chorwacja-kto-wygra-faworyt-meczu-sprawdz-kursy-i-typy-bukmacherskie-29-09-2026)
- [TotalCorner, Hiszpania](https://www.totalcorner.com/team/view/1416)
- [Racing Post, Szkocja–Szwajcaria](https://www.racingpost.com/sport/football-tips/nations-league/scotland-vs-switzerland-predictions-team-news-odds-betting-tips-bet-builder-a6KtJ2p4oPzm/)
- [Sportytrader, Szkocja–Szwajcaria](https://www.sportytrader.com/en/betting-tips/scotland-switzerland-375652/)
- [Gram Grubo, Słowacja–Kazachstan](https://gramgrubo.pl/slowacja-kazachstan-typy-bukmacherskie-i-analiza-29-9/)
- [podkarpacielive, San Marino–Albania](https://www.podkarpacielive.pl/pl/wydarzenia/57718,san-marino---albania-typy-kursy-bukmacherskie-zapowiedz-29092026)
- [podkarpacielive, Bułgaria–Estonia](https://www.podkarpacielive.pl/pl/wydarzenia/57729,bulgaria---estonia-typy-kursy-bukmacherskie-zapowiedz-29092026)
- [podkarpacielive, Słowenia–Macedonia](https://www.podkarpacielive.pl/pl/wydarzenia/57706,slowenia---macedonia-polnocna-typy-kursy-bukmacherskie-zapowiedz-29092026)
- [Sportskeeda, Luksemburg–Islandia](https://www.sportskeeda.com/football/luxembourg-vs-iceland-prediction-betting-tips-29th-september-2026)
- [mecze24, Mołdawia–Wyspy Owcze](https://www.mecze24.pl/aktualnosci/moldawia-wyspy-owcze-typy-kursy-bukmacherskie-29-09-2026)
- [betfan, Finlandia–Białoruś](https://sport.betfan.pl/finlandia-bialorus-typy-kursy-gdzie-ogladac-29-09/)
- [ATP, półfinały Chengdu](https://www.atptour.com/en/news/chengdu-2026-semi-final-report)
- [SportsBettingDime, Hurkacz–Davidovich](https://www.sportsbettingdime.com/news/tennis/hurkacz-vs-davidovich-fokina-picks-predictions-chengdu-final/)
- [ATP, półfinały Hangzhou](https://www.atptour.com/en/news/hangzhou-2026-semi-final-report)
- [SportsBettingDime, Miedwiediew–Rublow](https://www.sportsbettingdime.com/news/tennis/medvedev-rublev-best-bets-picks-odds-hangzhou-final/)
- [Dimers, Miedwiediew–Rublow](https://www.dimers.com/tennis/news/daniil-medvedev-vs-andrey-rublev-tennis-prediction-atp-hangzhou-open-2026-ac)
- [LWOS, statystyki twardej nawierzchni](https://lastwordonsports.com/tennis/2026/04/19/hard-court-jekyll-hydes/)

*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
