# TOP 10 predykcji dnia — poniedziałek, 28.09.2026

Użyte skille: football-predictor, tennis-predictor i esports-predictor.

**Źródło kursów:** betclic.pl jest zablokowany przez proxy tego środowiska. Kursy Betclic biorę z polskich zapowiedzi, które je cytują (sportowefakty, mecze24, podkarpacielive). Tam, gdzie znalazłem tylko średnią z kilku bukmacherów, podaję ją jako „rynek”. Stan na ok. 15:45.

**Oferta dnia:**
- **Piłka nożna, 2. kolejka Ligi Narodów:**
  - A1: Belgia–Francja, Turcja–Włochy (obie 20:45);
  - B: Gruzja–Ukraina (18:00), Szwecja–Polska, Rumunia–Bośnia i Hercegowina, Irlandia Płn.–Węgry (wszystkie 20:45);
  - C: Armenia–Czarnogóra, Łotwa–Cypr (obie 18:00).
- **Tenis, poza rankingiem:**
  - półfinały w Hangzhou (Rublev–Jacquet, Miedwiediew–Safiullin) były rozgrywane w południe i już się skończyły albo trwają;
  - półfinał Hurkacz–Shapovalov w Chengdu (trzeci mecz od 13:00) prawdopodobnie trwa, a kurs przed meczem był 1,65 / 2,25;
  - Tokio ma dziś tylko kwalifikacje.
- **E-sport, poza rankingiem:** nie znalazłem dziś meczów tier-1. PGL Wallachia S9 już się skończył, a LCS gra dalej 3–4.10.

**Zasady rankingu:**
- Uwzględnia tylko typy z kursem uczciwym powyżej 1,15.
- Dla typów Under liczbę do rankingu biorę z wariantu z λ podniesionym o 0,15 na drużynę. To reguła 5 z Kroku 2b: model zaniżał gole w meczach reprezentacji o ok. 0,3 na mecz. Dla typów Over zostaje model bazowy.
- Dzień jest bardzo wyrównany: w żadnym meczu rynek nie daje faworytowi więcej niż ok. 50%. Dlatego w rankingu nie ma typów powyżej 77%.

## Ranking

| # | Mecz | Godz. | Typ | Prawd. | Kurs (fair) | Pewność | Kluczowe ryzyko |
|---|------|-------|-----|--------|-------------|---------|-----------------|
| 1 | Belgia – Francja | 20:45 | **Over 1,5 gola** | 76,9% | 1,30 | Średnia/Wysoka | Brak Mbappé (uraz kolana, ok. 2 tygodnie przerwy). Obie drużyny wygrały 1. kolejkę z czystym kontem: Belgia 2-0 z Włochami, Francja 1-0 z Turcją. Za typem: w 3 z 5 ostatnich meczów Belgii u siebie i Francji na wyjeździe padły co najmniej 3 gole. Rynek wycenia Over 2,5 na ok. 1,52, czyli wyżej niż model |
| 2 | Irlandia Płn. – Węgry | 20:45 | **Under 3,5 gola** | 76,8% (model 82,9%) | 1,30 | Średnia | Irlandia Płn. traciła u siebie średnio 0,2 gola w 10 meczach i wygrała w Gruzji 1-0 golem w 90+9'. Węgry przegrały 0-1 z Ukrainą. Ryzyko: Węgry na wyjazdach tracą średnio 2,1 gola |
| 3 | Łotwa – Cypr | 18:00 | **Under 3,5 gola** | 75,8% (model 81,9%) | 1,32 | Średnia | Obie przegrały 1. kolejkę (Łotwa 0-2 z Armenią, Cypr 1-2 z Czarnogórą). W ostatnim H2H padł remis 1-1. Ryzyko: mecz słabych obron w Lidze C |
| 4 | Turcja – Włochy | 20:45 | **Under 3,5 gola** | 74,7% (model 80,9%) | 1,34 | Średnia | Turcja gra bez Çalhanoğlu, Yıldıza i zawieszonego bramkarza Çakıra, a Kökçü jest wątpliwy. W 2026 strzeliła więcej niż 1 gola tylko w 1 z 6 meczów o punkty. Ostatnie H2H: 0-0. Ryzyko: obie drużyny muszą gonić wynik po porażce w 1. kolejce |
| 5 | Belgia – Francja | 20:45 | **X2** | 73,3% | 1,36 | Średnia | Francja wygrała 4 ostatnie mecze z Belgią. Zidane i van Bommel to nowi selekcjonerzy. **Wygrana Belgii ma w modelu 26,6%**, a rynek daje ok. 25%. Remis jest pokryty typem. Skorelowane z #1 |
| 6 | Szwecja – Polska | 20:45 | **1X** | 72,6% | 1,38 | Średnia | Szwecja gra bez Isaka (odesłany z urazem), Ekdala i Holma. Polska bez Kamińskiego, Lewandowski gra. Szwecja wygrała 2-1 z Rumunią, Polska zremisowała 0-0 z BiH. **Wygrana Polski: 27,4%** (rynek ok. 25%) |
| 7 | Rumunia – Bośnia i H. | 20:45 | **1X** | 72,2% | 1,39 | Średnia | **BiH wygrała 3 ostatnie mecze z Rumunią (dwa w 2025)**, a model daje jej 27,7%. Za typem: Rumunia wygrała 4 mecze z rzędu u siebie (średnio 2,1 gola w 10 meczach u siebie). BiH zremisowała 0-0 z Polską |
| 8 | Gruzja – Ukraina | 18:00 | **Under 3,5 gola** | 71,4% (model 77,9%) | 1,40 | Średnia | Ukraina bez Nazarenki (czerwona kartka z Węgrami). Ukraina wygrała 1-0 z Węgrami, Gruzja przegrała 0-1 z Irlandią Płn. (Kwaracchelia nie strzelił karnego). Jedyne H2H: 1-1. Ryzyko: Gruzja u siebie gra ofensywnie |
| 9 | Szwecja – Polska | 20:45 | **Over 1,5 gola** | 71,3% | 1,40 | Średnia | Brak Isaka obniża siłę ataku Szwecji. Polska ostatnio nie strzeliła gola z BiH. Obie drużyny mają jednak jakościowych napastników: Gyökeresa i Lewandowskiego |
| 10 | Irlandia Płn. – Węgry | 20:45 | **X2** | 70,9% | 1,41 | Średnia | Betclic ma na Węgry najniższy kurs w zestawieniu (2,05 wobec 2,33 w Betfan). Wygrana Irlandii Płn. ma w modelu 29,0%. Po zwycięstwie w Gruzji jest na fali. Skorelowane z #2 |

**Oczekiwana liczba trafień: ok. 7,3 z 10.** Pary #1/#5, #6/#9 i #2/#10 dotyczą tych samych meczów, więc wariancja jest wyższa niż przy typach niezależnych.

## Value względem Betclic (model a rynek)

**Nie znalazłem wyraźnego value, EV wszędzie ≤ 1,05.**

| Mecz | Typ | Model | Kurs | EV |
|---|---|---|---|---|
| Szwecja – Polska | 2 (Polska) | 27,4% | ok. 3,80 (Betclic, zakres 3,70-3,94) | ~1,04 |
| Gruzja – Ukraina | 1 (Gruzja) | 38,6% | ok. 2,66 (rynek) | ~1,03 |
| Turcja – Włochy | X | 28,6% | ok. 3,45 (rynek) | ~0,99 |
| Belgia – Francja | X2 | 73,3% | ok. 1,31 (z kursów Betclic 4,00 i 1,95) | ~0,96 |
| Irlandia Płn. – Węgry | 2 (Węgry) | 41,7% | 2,05 (Betclic) | ~0,85 |

Według reguły 7 z Kroku 2b value na underdoga w meczach reprezentacji typujemy jako X2. Dla Polski X2 wychodzi po kursie ok. 1,85, przy 53,7% w modelu. To EV ok. 0,99, więc bez value.

## Świadomie pominięte

- **Armenia – Czarnogóra.** Model 36,1 / 27,7 / 36,1, rynek tak samo wyrównany. Under 3,5 ma po stresie λ tylko 71,4%. Obie drużyny wygrały 1. kolejkę (Armenia 2-0 z Łotwą, Czarnogóra 2-1 z Cyprem), a w ostatnim H2H było 2-2.
- **Under 2,5.** W 4 meczach ma w modelu 57-64%, ale po stresie λ spada poniżej 60%. Zgodnie z regułą 5 najwyżej średnia pewność, więc do rankingu nie wszedł.
- **Tenis.** W momencie analizy nie zostały mecze przed rozpoczęciem. Rozliczenie z wczoraj: Hurkacz pokonał Harrisa 7-6(10) 6-4. Były 23 gemy, więc Over 21,5 z modelu wszedłby, a Harris +1,5 seta nie. Model mylnie wskazał Harrisa jako faworyta (60,9%).
- **Rożne.** Nie modelowałem ich, bo dla reprezentacji nie mam dwóch niezależnych źródeł rozbicia na rożne wywalczone i oddane (Krok 2b pkt 4).
- **E-sport.** Brak meczów tier-1. Tier-2 pominąłem zgodnie z regułami 7-8.

## Skrót — piłka nożna (model Poissona)

| Mecz | λ gole | 1X2 (%) | O1,5 | O2,5 | U3,5 (bazowy / po stresie) | BTTS | Kursy 1X2 |
|---|---|---|---|---|---|---|---|
| Gruzja – Ukraina (18:00) | 1,25 : 1,15 | 38,6 / 27,6 / 33,8 | 69,2% | 43,0% | 77,9% / 71,4% | 48,7% | rynek 2,66 / 3,27 / 2,71 |
| Armenia – Czarnogóra (18:00) | 1,20 : 1,20 | 36,1 / 27,7 / 36,1 | 69,2% | 43,0% | 77,9% / 71,4% | 48,8% | rynek 2,70 / 3,15 / 2,67 |
| Łotwa – Cypr (18:00) | 1,15 : 1,05 | 38,0 / 29,1 / 32,9 | 64,5% | 37,7% | 81,9% / 75,8% | 44,4% | rynek 2,56 / 3,18 / 2,74 |
| Belgia – Francja | 1,15 : 1,65 | 26,6 / 24,4 / 48,9 | 76,9% | 53,0% | 69,2% / 62,5% | 55,1% | Betclic ok. 3,70 / 4,00 / 1,95 |
| Turcja – Włochy | 1,05 : 1,20 | 31,9 / 28,6 / 39,4 | 65,8% | 39,1% | 80,9% / 74,7% | 45,4% | rynek 2,70-2,84 / 3,20-3,54 / 2,40-2,52 |
| Szwecja – Polska | 1,45 : 1,05 | 46,2 / 26,4 / 27,4 | 71,3% | 45,6% | 75,8% / 69,2% | 49,7% | Betclic w zakresie 1,85-1,98 / 3,40-3,72 / 3,70-3,94 |
| Rumunia – Bośnia i H. | 1,35 : 1,00 | 44,7 / 27,5 / 27,7 | 68,0% | 41,7% | 78,9% / 72,5% | 46,8% | Betclic w zakresie 2,05-2,12 / 3,20-3,58 / 3,30-3,58 |
| Irlandia Płn. – Węgry | 0,95 : 1,20 | 29,0 / 29,2 / 41,7 | 63,3% | 36,4% | 82,9% / 76,8% | 42,8% | Węgry 2,05 (Betclic), rynek ok. 3,25 / 3,18 / 2,29 |

**Korekty λ:**
- **Francja:** -10% za brak Mbappé. Olise, Dembélé i Doué to głębokie zaplecze, więc nie więcej.
- **Szwecja:** -8% za brak Isaka.
- **Turcja:** -10% za brak dwóch kreatorów (Çalhanoğlu, Yıldız).
- **Ukraina:** -3% za brak Nazarenki.
- **Polska:** bez korekty za Kamińskiego. Zgodnie z regułą 7 słabsza drużyna dostaje najwyżej -5%, a to jeden gracz.
- **Irlandia Płn.:** λ obrony niskie z powodu 0,2 straconego gola na mecz u siebie. Przy wyjazdowej średniej Węgier (2,1 straconego gola) λ ataku Irlandii zostaje jednak na 0,95, a nie niżej (podłoga ~0,7 nie jest tu potrzebna).

**Typy 1X2 w przedziale 50-85%:**
- #5, #6, #7 i #10 to podwójne szanse, więc remis jest w nich pokryty.
- Scenariusz odwrotnego wyniku to 26,6-29,0% i jest opisany przy każdym typie.
- Rozjazdy model–rynek w żadnym meczu nie przekraczają 10 pp.

---
Źródła:
- [TVP Sport, terminarz 28.09](https://sport.tvp.pl/95626415/liga-narodow-uefa-terminarz-meczow-w-poniedzialek-28-wrzesnia-2026)
- [sportowefakty, Belgia–Francja](https://sportowefakty.wp.pl/bukmacherzy/1276279/poniedzialkowy-hit-w-lidze-narodow-belgia-francja-typy-i-kursy)
- [Al Jazeera, Belgia–Francja](https://www.aljazeera.com/sports/2026/9/28/belgium-france-uefa-nations-league-mbappe-injury-olise-de-bruyne)
- [mecze24, Turcja–Włochy](https://www.mecze24.pl/aktualnosci/turcja-wlochy-typy-statystyki-kursy-analiza-28-09-2026)
- [Sports Mole, Turcja–Włochy](https://www.sportsmole.co.uk/football/turkey/uefa-nations-league/preview/turkey-vs-italy-prediction-team-news-lineups_605813.html)
- [sportowefakty, Szwecja–Polska](https://sportowefakty.wp.pl/bukmacherzy/1276256/tego-meczu-przegrac-nie-wolno-typy-i-kursy-na-mecz-szwecja-polska)
- [Sport1, składy Szwecja–Polska](https://sport1.pl/szwecja-polska-przewidywane-sklady-na-mecz-28-09-2026)
- [Polskie Radio, Szwecja–Rumunia](https://polskieradio24.pl/sport/wynik-meczu-szwecja-rumunia-kto-wygral-w-polskiej-grupie-w-lidze-narodow)
- [sportowefakty, Rumunia–BiH](https://sportowefakty.wp.pl/bukmacherzy/1276260/graja-nasi-grupowi-rywale-rumunia-bosnia-typy-i-kursy)
- [mecze24, Irlandia Płn.–Węgry](https://www.mecze24.pl/aktualnosci/irlandia-polnocna-wegry-typy-statystyki-kursy-analiza-28-09-2026)
- [RTÉ, Gruzja–Irlandia Płn.](https://www.rte.ie/sport/soccer/2026/0925/1592957-nations-league-n-ireland-strike-late-to-win-in-georgia/)
- [ESPN, Węgry–Ukraina](https://www.espn.com/soccer/match/_/gameId/401861054/ukraine-hungary)
- [mecze24, Gruzja–Ukraina](https://www.mecze24.pl/aktualnosci/gruzja-ukraina-typy-kursy-statystyki-prognozy-28-09-2026)
- [mecze24, Armenia–Czarnogóra](https://www.mecze24.pl/aktualnosci/armenia-czarnogora-typy-statystyki-kursy-analiza-28-09-2026)
- [mecze24, Łotwa–Cypr](https://www.mecze24.pl/aktualnosci/lotwa-cypr-typy-statystyki-kursy-zapowiedz-meczu-28-09-2026)
- [sportowefakty, Hurkacz–Shapovalov](https://sportowefakty.wp.pl/bukmacherzy/1276241/bedzie-pierwszy-final-w-sezonie-hubert-hurkacz-denis-shapovalov-typy-i-kursy)
- [ATP, Chengdu QF](https://www.atptour.com/en/news/chengdu-2026-sunday-report)
- [Tennis Tonic, Hangzhou SF](https://tennistonic.com/tennis-news/1058689/andrey-rublev-victorious-over-jacquet-in-the-semifinal-at-the-hangzhou-open-hangzhou-results-highlights/)
- [PGL Wallachia S9](https://www.pglesports.com/dota2/wallachia-s9-2026/)

*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
