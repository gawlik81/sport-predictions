# TOP 10 predykcji dnia — piątek, 02.10.2026 (wersja 2: gole, rożne i faule)

Użyte skille: football-predictor, tennis-predictor i esports-predictor.
**W piłce nożnej są tylko typy over/under** (gole, rożne, faule), zgodnie z prośbą.

**Zmiana względem wersji 1:** pierwsza wersja zawierała tylko gole, bo nie znalazłem wtedy danych o rożnych i faulach. Po dokładniejszym wyszukaniu (zapowiedzi bet builder: That's A Goal, Statz.ai, Sports Gambler, Sky Sports) mam statystyki rożnych dla 9 meczów i fauli dla 4 meczów. Ranking jest przebudowany.

**Źródła:** zapowiedzi meczowe i statystyki drużyn (linki na końcu) oraz wyniki 1. i 2. kolejki LN. Kursów bukmacherskich nie zbierałem. Przy typach jest kurs fair (1/p). Stan na ok. 09:00.

**Zasady rankingu:**
- Uwzględnia tylko typy z kursem fair powyżej 1,15. Najwyżej 2 typy z jednego meczu.
- **Gole, under:** liczba z wariantu z λ podniesionym o 0,15 na drużynę (reguła 5). **Gole, over:** model bazowy.
- **Rożne:** model Poissona z λ ze statystyk drużyn. Jedno źródło oznacza obcięcie o 5 pp i najwyżej średnią pewność (Krok 2b, pkt 4). Dwa źródła albo zgodna statystyka meczów oznaczają obcięcie o 3 pp.
- **Faule:** Poisson zaniża rozrzut liczby fauli (wariancja jest wyższa niż średnia), więc obcinam wynik o ok. 6 pp.

## Ranking

| # | Mecz | Godz. | Typ | Prawd. | Kurs (fair) | Pewność | Podstawa i ryzyko |
|---|------|-------|-----|--------|-------------|---------|-------------------|
| 1 | Węgry – Gruzja | 20:35 | **Under 3,5 gola** | 80,9% (bazowo 86,6%) | 1,24 | Średnia/Wysoka | Żadna z drużyn nie strzeliła gola w LN (obie 0-1 i 0-0). Węgry średnio 1,2 gola z 10,5 strzału. Ryzyko: obie muszą zdobyć punkty |
| 2 | Kazachstan – Mołdawia | 16:00 | **Under 3,5 gola** | 78,9% (bazowo 84,8%) | 1,27 | Średnia | Mołdawia nie wygrała 17 meczów i ma problemy ze strzelaniem. Kazachstan u siebie traci 0,33 gola na mecz. Zapowiedzi typują Under 2,5 |
| 3 | Wyspy Owcze – Słowacja | 20:45 | **Over 7,5 rzutu rożnego** | ~77% (model 82,2%) | 1,30 | Średnia | λ rożnych 4,5 : 6,0. Wyspy Owcze 4,6, Słowacja 5,3 rożnego na mecz. W 5 ostatnich meczach Wysp Owczych u siebie padało średnio **12,6 rożnego**. Ryzyko: jedno źródło dla Słowacji |
| 4 | Bośnia i H. – Szwecja | 20:45 | **Over 1,5 gola** | 74,2% | 1,35 | Średnia/Wysoka | Szwecja strzeliła gola w 11 meczach LN z rzędu. BiH u siebie traci gola w 12 z 13 meczów. Pożegnanie Džeko, brak Isaka. Ryzyko: 1-0 |
| 5 | Łotwa – Czarnogóra | 18:00 | **Over 7,5 rzutu rożnego** | ~74% (model 74,2%) | 1,35 | Średnia | λ 4,6 : 5,0. Ponad 8 rożnych padło w **7 z 8** ostatnich meczów Łotwy u siebie i w **10 z 11** meczów Czarnogóry na wyjeździe. Ta statystyka meczów potwierdza model, więc bez obcięcia |
| 6 | Belgia – Turcja | 20:45 | **Over 1,5 gola** | 73,3% | 1,36 | Średnia | Turcja straciła 5 goli w 2 meczach. Belgia średnio 2,4 gola w 10 meczach, ale gra bez Courtoisa i Doku. Ryzyko: Belgia nie strzeliła gola Francji |
| 7 | Belgia – Turcja | 20:45 | **Over 7,5 rzutu rożnego** | ~73% (model 76,1%) | 1,37 | Średnia | λ 5,5 : 4,3. Belgia 6,1 wywalczonego i 3,9 oddanego rożnego na mecz, Turcja 6,3 i 4,3, a w 5 ostatnich meczach Turcja średnio 6,6 rożnego. Dwa źródła. Skorelowane z #6 |
| 8 | Polska – Rumunia | 20:45 | **Over 21,5 faula** | ~72% (model 78,2%) | 1,39 | Średnia | λ fauli 12,5 : 13,0. Polska 12,29, Rumunia 13,35 faula na mecz. Marin (Rumunia) 2,22 faula na 90 min, a Zalewski często wymusza faule. Stawka meczu (obie drużyny bez wygranej) sprzyja walce. Ryzyko: rozrzut fauli i styl sędziego (nieznany) |
| 9 | Bośnia i H. – Szwecja | 20:45 | **Under 10,5 rzutu rożnego** | ~71% (model 74,1%) | 1,41 | Średnia | λ 4,4 : 4,3. W 10 ostatnich meczach BiH padało średnio 9,0 rożnego łącznie, Szwecji 8,7. Szwecja w 3 ostatnich meczach miała poniżej 4,5 rożnego, a BiH 3 razy z rzędu oddała poniżej 4,5. Zapowiedź typuje Under 9,5 |
| 10 | Francja – Włochy | 20:45 | **Over 7,5 rzutu rożnego** | ~70% (model 73,1%) | 1,43 | Średnia | λ 5,9 : 3,6. Francja 6,9 rożnego na mecz (20 meczów), Włochy 3,93 (14 meczów). Zapowiedź szacuje total na 9,8 i daje Over 8,5 60%. Ryzyko: Francja Zidane'a gra zachowawczo (dwa razy 1-0) |

**Oczekiwana liczba trafień: ok. 7,4 z 10.** Skorelowane są pary #4/#9 (BiH–Szwecja) i #6/#7 (Belgia–Turcja).

## Pozostałe typy powyżej 65% (poza TOP 10)

| Mecz | Typ | Prawd. | Kurs (fair) | Uwagi |
|---|---|---|---|---|
| Węgry – Gruzja | Under 10,5 rzutu rożnego | ~71% (model 75,2%) | 1,41 | Węgry 4,2, Gruzja 4,4 rożnego na mecz (jedno źródło). Wypadło, bo #1 to już typ z tego meczu |
| Francja – Włochy | Under 3,5 gola | 71,4% | 1,40 | Francja dwa razy wygrała 1-0 |
| Belgia – Turcja | Over 21,5 faula | ~70% (model 70,7%) | 1,43 | Belgia 12,3 faula na mecz, w jej meczach średnio 23,6 faula łącznie. W meczach Turcji średnio 25,2 faula, a **78% meczów** kończyło się powyżej 21,5. Statystyka meczów potwierdza model, więc bez obcięcia. Trzeci typ z meczu, dlatego poza TOP 10 |
| Polska – Rumunia | Over 1,5 gola | 71,3% | 1,40 | Wersja 1 rankingu |
| Cypr – Armenia | Over 7,5 rzutu rożnego | ~65% (model 69,9%) | 1,54 | Cypr 5,4, Armenia 2,9 rożnego na mecz. W meczu z Łotwą Cypr miał 11 rożnych |
| Bośnia i H. – Szwecja | Over 21,5 faula | ~67% (model 72,7%) | 1,49 | BiH 13,6 faula i 2,1 żółtej kartki na mecz (27 żółtych w 10 meczach) |
| Rumunia (drużynowo) | Under 3,5 rzutu rożnego | ~67% (model 69,2%) | 1,49 | Rumunia miała poniżej 3,5 rożnego w 5 kolejnych wyjazdach. Polska u siebie oddała poniżej 3,5 rożnego w 6 kolejnych meczach |
| Francja – Włochy | Under 23,5 faula | ~63% (model 67,7%) | 1,59 | Francja 9,15, Włochy 11,25 faula na mecz |

## Tenis i e-sport — dlaczego brak typów

- **Tenis.**
  - Pekin i Tokio grają dziś 2. rundę. Sesja wieczorna w Tokio zaczyna się o 09:00 CEST, a w Pekinie mecze zaczynają się od 07:00 CEST.
  - Najciekawszy mecz to **Djokovic – Bu Yunchaokete**: Djokovic ma w Pekinie bilans 30-0, a Bu to nr 114 z dziką kartą.
  - Godziny tego meczu nie potwierdziłem. Nie mam też rzeczywistych statystyk serwisu i returnu obu zawodników na twardej nawierzchni, więc zgodnie z regułą 4 total gemów nie wchodzi do rankingu.
  - Wygrana Djokovica dałaby kurs fair poniżej 1,15, więc odpada zgodnie z filtrem.
- **E-sport.**
  - W CS2 grają dziś tylko turnieje tier-3: ROG Journey Autumn (pula 20 tys. USD), Stake Ranked, ESN Fall Showdown.
  - Zgodnie z regułą 8 (ryzyko integralności i brak danych) nie typuję.
  - LoL na igrzyskach azjatyckich to reprezentacje bez danych.

## Skrót — modele

**Gole (Poisson):**

| Mecz | λ gole | O1,5 | U2,5 | U3,5 (baza / stres) |
|---|---|---|---|---|
| Francja – Włochy | 1,40 : 1,00 | 69,2% | 57,0% | 77,9% / 71,4% |
| Belgia – Turcja | 1,75 : 0,85 | 73,3% | 51,8% | 73,6% |
| Polska – Rumunia | 1,40 : 1,10 | 71,3% | 54,4% | 75,8% |
| Bośnia i H. – Szwecja | 1,30 : 1,35 | 74,2% | 50,6% | 72,5% |
| Węgry – Gruzja | 1,00 : 0,95 | 58,0% | 69,0% | 86,6% / 80,9% |
| Kazachstan – Mołdawia | 1,15 : 0,90 | 60,7% | 66,3% | 84,8% / 78,9% |
| Cypr – Armenia | 1,10 : 1,25 | 68,0% | 58,3% | 78,9% / ~72% |
| Łotwa – Czarnogóra | 0,95 : 1,35 | 66,9% | 59,6% | 79,9% / 73,6% |
| Wyspy Owcze – Słowacja | 0,70 : 1,60 | 66,9% | 59,6% | 79,9% / 73,6% |

**Rożne (Poisson):**

| Mecz | λ rożne | O7,5 | O8,5 | O9,5 | U10,5 | Dane wejściowe |
|---|---|---|---|---|---|---|
| Francja – Włochy | 5,9 : 3,6 | 73,1% | 60,8% | 47,8% | 64,5% | FRA 6,9, ITA 3,93 rożnego na mecz |
| Polska – Rumunia | 5,8 : 2,8 | 62,7% | 49,1% | 36,0% | 75,2% | POL 5,59, ROU 4,88; ROU <3,5 na 5 wyjazdach |
| Belgia – Turcja | 5,5 : 4,3 | 76,1% | 64,4% | 51,7% | 60,8% | BEL 6,1 / 3,9, TUR 6,3 / 4,3 (wywalczone / oddane) |
| Bośnia i H. – Szwecja | 4,4 : 4,3 | 64,0% | 50,4% | 37,3% | 74,1% | BiH 4,0 / 5,0, SWE 3,9 / 4,8 (10 meczów) |
| Węgry – Gruzja | 4,2 : 4,4 | 62,7% | 49,1% | 36,0% | 75,2% | HUN 4,2, GEO 4,4 |
| Łotwa – Czarnogóra | 4,6 : 5,0 | 74,2% | 62,0% | 49,1% | 63,3% | LVA 4,4, MNE 5,2; >8 rożnych w 7/8 i 10/11 meczów |
| Wyspy Owcze – Słowacja | 4,5 : 6,0 | 82,2% | 72,1% | 60,3% | 52,1% | FRO 4,6, SVK 5,3; mecze FRO u siebie średnio 12,6 |
| Cypr – Armenia | 5,8 : 3,4 | 69,9% | 57,0% | 43,9% | 68,2% | CYP 5,4, ARM 2,9 |
| Kazachstan – Mołdawia | 4,0 : 3,3 | O6,5 59,4% | O7,5 44,6% | O8,5 31,1% | U9,5 79,9% | zapowiedź: 6-8 rożnych |

**Faule (Poisson, bez korekty na rozrzut):**

| Mecz | λ faule | O20,5 | O21,5 | O22,5 | O23,5 | Dane |
|---|---|---|---|---|---|---|
| Polska – Rumunia | 12,5 : 13,0 | — | 78,2% | 71,7% | 64,3% | POL 12,29, ROU 13,35 faula na mecz |
| Belgia – Turcja | 12,3 : 12,0 | 77,6% | 70,7% | 63,1% | 55,1% | BEL 12,3; mecze TUR średnio 25,2 faula łącznie |
| Bośnia i H. – Szwecja | 13,6 : 11,0 | — | 72,7% | 65,4% | 57,5% | BiH 13,6 faula na mecz |
| Francja – Włochy | 10,0 : 11,5 | 57,2% | 48,6% | 40,1% | 32,3% | FRA 9,15, ITA 11,25 faula na mecz |

**Kartki (bez modelu, sygnały z danych):**
- Węgry–Gruzja sędziuje Srđan Jovanović, średnio 4,0-4,07 żółtej kartki na mecz.
- BiH zebrała 27 żółtych kartek w 10 meczach.

---
Źródła:
- [That's A Goal, Francja–Włochy (bet builder)](https://www.thatsagoal.com/predictions/nations-league/france-vs-italy-bet-builder-tips-02-10-26)
- [Statz.ai, rożne Francji](https://statz.ai/team/france/corners)
- [That's A Goal, Polska–Rumunia (bet builder)](https://www.thatsagoal.com/predictions/nations-league/poland-vs-romania-bet-builder-tips-02-10-26)
- [Statz.ai, Belgia–Turcja](https://statz.ai/h2h/belgium-vs-turkey/19676675)
- [Statz.ai, faule Belgii](https://statz.ai/team/belgium/fouls)
- [Sports Gambler, Belgia–Turcja](https://www.sportsgambler.com/betting-tips/football/belgium-vs-turkey-prediction-lineups-odds-2026-10-02/)
- [Statz.ai, Szwecja–BiH](https://statz.ai/h2h/sweden-vs-bosnia/19676704)
- [Sports Gambler, BiH–Szwecja](https://www.sportsgambler.com/betting-tips/football/bosnia-herzegovina-vs-sweden-prediction-lineups-odds-2026-10-02/)
- [Sky Sports, Węgry–Gruzja](https://www.skysports.com/football/hungary-vs-georgia/554046)
- [Sports Gambler, Węgry–Gruzja](https://www.sportsgambler.com/betting-tips/football/hungary-vs-georgia-prediction-lineups-odds-2026-10-02/)
- [Sports Gambler, Cypr–Armenia](https://www.sportsgambler.com/betting-tips/football/cyprus-vs-armenia-prediction-lineups-odds-2026-10-02/)
- [Sports Gambler, Łotwa–Czarnogóra](https://www.sportsgambler.com/betting-tips/football/latvia-vs-montenegro-prediction-lineups-odds-2026-10-02/)
- [Sports Gambler, Wyspy Owcze–Słowacja](https://www.sportsgambler.com/betting-tips/football/faroe-islands-vs-slovakia-prediction-lineups-odds-2026-10-02/)
- [The Pressing Zone, Kazachstan–Mołdawia](https://www.thepressingzone.com/kazakhstan-vs-moldova-prediction-2026/)
- [Sports Mole, Polska–Rumunia](https://www.sportsmole.co.uk/football/poland/uefa-nations-league/preview/poland-vs-romania-prediction-team-news-lineups_606004.html)
- [Sports Mole, Belgia–Turcja](https://www.sportsmole.co.uk/football/belgium/uefa-nations-league/preview/belgium-vs-turkey-prediction-team-news-lineups_606012.html)
- [Sports Mole, BiH–Szwecja](https://www.sportsmole.co.uk/football/sweden/uefa-nations-league/preview/bosnia-hvina-vs-sweden-prediction-team-news-lineups_606005.html)
- [Goal, Francja–Włochy](https://www.goal.com/en/news/france-italy-uefa-nations-league-preview/blt34db302c6b849447)
- [101 Great Goals, wyniki 28.09](https://www.101greatgoals.com/match-reports/nations-league-results-today-reports-results-scores-goals/)
- [Tennis Majors, Djokovic 30-0 w Pekinie](https://www.tennismajors.com/atp/djokovic-makes-it-30-0-in-beijing-beating-borges-despite-treatment-862205.html)
- [esports.gg, kalendarz CS2](https://esports.gg/news/counter-strike-2/schedule-cs2-events-2026/)

*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
