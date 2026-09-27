# TOP 10 predykcji dnia — niedziela, 27.09.2026

Użyte skille: football-predictor, tennis-predictor i esports-predictor.

**Źródło kursów:** betclic.pl jest zablokowany przez proxy tego środowiska (tak samo sportowefakty, mecze24, flashscore, betfan). Kursy Betclic pochodzą z polskich zapowiedzi bukmacherskich, które je cytują (stan na rano), oraz z porannego pliku `Value_multisport_2026-09-27.md`. Tam, gdzie znalazłem tylko średnią rynkową, oznaczam to jako „rynek”.

**Oferta dnia:**
- Piłka nożna: 8 meczów 2. kolejki Ligi Narodów:
  - A2: Serbia–Holandia, Niemcy–Grecja;
  - A4: Dania–Walia, Norwegia–Portugalia;
  - B: Austria–Kosowo, Izrael–Irlandia;
  - D: Litwa–Azerbejdżan, Gibraltar–Andora.
- Belgia–Francja i Turcja–Włochy grają 28.09, a Hiszpania–Chorwacja 29.09. Nie ma ich w dzisiejszej ofercie.
- Tenis:
  - ATP 250 Chengdu, ćwierćfinały (Hurkacz–Harris, Mannarino–Shapovalov, Muller–Davidovich Fokina, Basilashvili–Brooksby);
  - ATP 250 Hangzhou, ćwierćfinały (m.in. Miedwiediew–Wong);
  - Laver Cup, dzień 3 (Europa prowadzi 7-5; dziś każdy mecz jest za 3 pkt, gra się do 13 pkt).
- E-sport: LCS, Cloud9–Team Liquid (22:00, BO5, finał górnej drabinki). W CS2 i Dota 2 Betclic nie ma dziś meczów tier-1.

**Zasady rankingu:**
- Uwzględnia tylko typy z kursem uczciwym powyżej 1,15.
- Kolejność według prawdopodobieństwa po korektach, czyli liczby „do rankingu”.
- Stosuje reguły kalibracji z weryfikacji 24.09 i 26.09:
  - w meczach reprezentacji Over 1,5 to najpewniejszy rynek goli;
  - przy dużej różnicy klas rynek bywa trafniejszy niż model;
  - w tenisie underdog +1,5 seta, a total gemów tylko przy rzeczywistych statystykach serwisu i returnu.

## Ranking

| # | Mecz | Godz. | Typ | Prawd. | Kurs (fair) | Betclic | Pewność | Kluczowe ryzyko |
|---|------|-------|-----|--------|-------------|---------|---------|-----------------|
| 1 | Jodar – Fritz (Laver Cup) | ok. 16:30 | **Fritz +1,5 seta** | ~84% (model 90,0%) | 1,19 | 1,27 | Średnia/Wysoka | **Zakład może zostać zwrócony:** jeśli Europa wygra debla i mecz Zverev–Tien, osiągnie 13 pkt i mecz się nie odbędzie. Fritz gra dziś wcześniej debla, a wczoraj przegrał super tie-break do 13-11 z Alcarazem. p_serve 0,676 : 0,618 (Tennis Abstract, twarda) |
| 2 | Austria – Kosowo | 18:00 | **1X** | 82% (model 83,6%) | 1,22 | ~1,10 (1X2: ~1,50 / 4,20 / 5,25) | Średnia/Wysoka | Kosowo pokonało Irlandię 1-0 (xG 2,22:0,28), a Austria wygrała 3-1 z Izraelem. Ryzyko remisu 22,7% jest pokryte typem. Wygrana Kosowa ma w modelu 16,2%, a rynek wycenia ją na 15-16%. Austria nie przegrała 10 meczów u siebie |
| 3 | Dania – Walia | 18:00 | **1X** | 81,8% | 1,22 | ~1,19 (1X2: 1,62 / 3,75 / 5,00) | Średnia/Wysoka | Dania przegrała 2-3 w Norwegii. Walia była w Lizbonie bezradna (strzały 5-22), ale przegrała tylko 0-1. Wygrana Walii ma w modelu 18%. Dania nie przegrała 8 meczów u siebie (średnio 2,2 : 0,7 w bramkach) |
| 4 | Serbia – Holandia | 18:00 | **X2** | 80,0% | 1,25 | ~1,17 (1X2 rynek: ~5,25 / 4,00 / 1,60) | Średnia | Serbia bez Vlahovicia i Mitrovicia przegrała u siebie 1-2 z Grecją. Holandii brakuje Brobbeya, a Timber jest niepewny. Wygrana Serbii ma w modelu 19,8%, a remis jest pokryty typem |
| 5 | Niemcy – Grecja | 20:45 | **Over 1,5 gola** | 79,3% | 1,26 | — | Średnia/Wysoka | Grecja wygrała 2-1 w Belgradzie i może bronić się nisko. Model daje Niemcom 69,8% na zwycięstwo, rynek ok. 69%, więc wyceny są zgodne |
| 6 | Norwegia – Portugalia | 20:45 | **Over 1,5 gola** | 79,3% | 1,26 | — | Średnia/Wysoka | Mecz na szczycie grupy może być taktycznie zamknięty. Za typem: Norwegia–Dania skończyło się 3-2, a Haaland i Ronaldo są w przewidywanych składach. BTTS w modelu 59,3% (Betclic 1,54, EV 0,91, bez value) |
| 7 | Litwa – Azerbejdżan | 15:00 | **Under 3,5 gola** | ~79% (model 84,8%) | 1,27 | — | Średnia | Model zaniżał gole w meczach reprezentacji o ok. 0,3 na mecz, więc liczbę do rankingu wziąłem z wariantu z λ podniesionym do 1,25 : 1,10 (78,9%). Litwa strzela średnio 0,6 gola, Azerbejdżan przegrał 5 meczów z rzędu. Betclic 1X2: 2,40 / 3,10 / 2,90 |
| 8 | Cloud9 – Team Liquid (LCS) | 22:00 | **Liquid +1,5 mapy** | ~76% (model 79,7%) | 1,32 | — | Średnia | p_map C9 0,42 wyprowadziłem z rynku (pojedyncza mapa dla C9 @2,15). Liquid wygrał 5-0 w mapach w dwóch ostatnich seriach. Nie znalazłem doniesień o zmianach w składach, ale nie potwierdziłem ich na Liquipedii. Obciąłem 3-4 pp, bo reguły e-sportowe nie są jeszcze zweryfikowane |
| 9 | Dania – Walia | 18:00 | **Over 1,5 gola** | 73,3% | 1,36 | — | Średnia | Wynik skorelowany z typem #3. Ryzyko: Dania wygrywa skromnie 1-0 przeciw nisko ustawionej Walii (tak jak Portugalia 24.09) |
| 10 | Serbia – Holandia | 18:00 | **Over 1,5 gola** | 73,3% | 1,36 | — | Średnia | Wynik skorelowany z typem #4. Serbia straciła 12 goli w 5 meczach, Holandia strzeliła 13 w 5 meczach. Ryzyko: zamknięty mecz na 0-1 |

**Oczekiwana liczba trafień: ok. 7,9 z 10.** Typy #3/#9 i #4/#10 są skorelowane, więc wariancja jest wyższa niż przy niezależnych typach.

## Value względem kursów Betclic

| Mecz | Typ | Model / konserw. | Fair | Betclic | EV | Uwaga |
|---|---|---|---|---|---|---|
| Gibraltar – Andora (18:00) | 1 (Gibraltar) | 41,1% / ~35% | 2,86 | 3,55 | 1,24 | Rynek daje Andorze ok. 39-40%, a model 28%. Rozjazd przekracza 10 pp, więc typ tylko na małą stawkę. Bezpieczniejsza wersja: 1X @1,53 (model 72,1%) |
| Jodar – Fritz | Fritz +1,5 seta | 90,0% / ~84% | 1,19 | 1,27 | 1,07 | Typ #1 z rankingu |
| Serbia – Holandia | 1X | 43,7% / ~38% | 2,63 | 2,75 | 1,05 | Przeciw rankingowemu X2 (#4). To zakład na rozjazd model–rynek, nie na przewidywany wynik |
| Zverev – Tien (ok. 14:10) | Tien +1,5 seta | 64,0% / ~58% | 1,72 | 1,79 | 1,04 | Poniżej progu 60% do rankingu |
| Hurkacz – Harris | Harris +1,5 seta | 81,8% / ~67% | ~1,50 | brak kursu Betclic | ? | Value od kursu ~1,55. Patrz sekcja o tenisie |

## Świadomie pominięte

- **Hurkacz [5] – Harris (Q), ATP Chengdu QF.** Godzina rozpoczęcia jest niepewna: według różnych źródeł od ok. 10:30 do 14:30 CEST.
  - Kursy rynkowe: Hurkacz 1,54, Harris 2,43 (ok. 62-65% dla Hurkacza). Dimers daje Hurkaczowi 59%.
  - Model odwraca faworyta: Harris 60,9%, bo ma p_serve 0,704 wobec 0,680 Hurkacza.
  - Statystyki Harrisa pochodzą z Tennis Abstract (69,4% SPW, 37,9% RPW), po obcięciu o 1 pp za Challengery zgodnie z regułą 11. Harris ma bilans 31-7 na twardej, 62 asy w Chengdu i ani razu nie stracił serwisu w turnieju głównym.
  - Statystyki Hurkacza są szacowane: 61,2% pierwszego serwisu z sezonu i ok. 34% RPW.
  - Oczekiwane 27 gemów, Over 21,5 ma w modelu 78,3%. **Nie wstawiam go do rankingu (reguła 4)**, bo p_serve Hurkacza jest szacowane. Kurs rynkowy 1,23 (ok. 81%) i tak nie daje value.
  - Rozsądny typ to **Harris +1,5 seta**, jeśli Betclic da co najmniej ok. 1,55. Świeżych kontuzji Hurkacza nie znalazłem (sprawdzone zgodnie z regułą 8).
- **Izrael – Irlandia (20:45, Debreczyn).** Mecz bez faworyta: model 37,5 / 27,3 / 35,1, rynek 36 / 29 / 35. 1X ma 64,8% przy kursie ok. 1,46, a X2 62,4% przy ok. 1,45. Oba typy bez value.
- **Niemcy – Grecja, 1 (Niemcy).** Model 69,8%, rynek ok. 69%, kurs ok. 1,35 (EV 0,94). Dlatego wybrałem Over 1,5.
- **Norwegia – Portugalia, 1X2.** Model 38,8 / 24,5 / 36,6, rynek ok. 35 / 28 / 37. To rzut monetą.
- **Austria – Kosowo, Kosowo.** Model 16,2%, kurs 5,25-6,00, EV ok. 0,85-0,97.
- **Mannarino – Shapovalov (Chengdu).** Rano był w value (Over 20,5 @1,57), ale mecz prawdopodobnie już się zaczął.
- **Alcaraz – de Minaur (Laver Cup).** de Minaur +1,5 seta: ok. 33% po korekcie, kurs 3,20. Niskie p i zmęczenie de Minaura po meczu z super tie-breakiem 11-9.
- **Rożne.** Nie modelowałem ich, bo dla reprezentacji nie mam dwóch niezależnych źródeł rozbicia na rożne wywalczone i oddane. Zgodnie z Krokiem 2b pkt 4 typ na rożne mógłby mieć najwyżej średnią pewność i nie przeszedłby do TOP 10.
- **E-sport tier-2 (CBLOL, EMEA Masters, akademie).** Bez danych, pominięte zgodnie z regułami 7-8.

## Skrót — piłka nożna (model Poissona)

| Mecz | λ gole | 1X2 (%) | O1,5 | O2,5 | U3,5 | BTTS | Betclic / rynek 1X2 |
|---|---|---|---|---|---|---|---|
| Litwa – Azerbejdżan (15:00) | 1,10 : 0,95 | 38,7 / 30,3 / 31,0 | 60,7% | 33,7% | 84,8% | 40,9% | 2,40 / 3,10 / 2,90 |
| Gibraltar – Andora (18:00) | 1,10 : 0,85 | 41,1 / 31,0 / 27,9 | 58,0% | 31,0% | 86,6% | 38,2% | Gibraltar 3,55 (rynek ~3,3 / 2,8 / 2,4) |
| Serbia – Holandia (18:00) | 0,90 : 1,70 | 19,8 / 23,9 / 56,1 | 73,3% | 48,2% | 73,6% | 48,4% | ~5,25 / 4,00 / 1,60 |
| Dania – Walia (18:00) | 1,75 : 0,85 | 58,5 / 23,3 / 18,0 | 73,3% | 48,2% | 73,6% | 47,2% | 1,62 / 3,75 / 5,00 |
| Austria – Kosowo (18:00) | 1,80 : 0,80 | 60,9 / 22,7 / 16,2 | 73,3% | 48,2% | 73,6% | 45,8% | ~1,50 / 4,20 / 5,25 |
| Niemcy – Grecja (20:45) | 2,20 : 0,75 | 69,8 / 18,2 / 11,3 | 79,3% | 56,6% | 65,8% | 46,5% | rynek 1,33-1,38 / 4,80-5,36 / 7,00-8,45 |
| Norwegia – Portugalia (20:45) | 1,50 : 1,45 | 38,8 / 24,5 / 36,6 | 79,3% | 56,6% | — | 59,3% | rynek ~2,55 / 3,55 / 2,60 |
| Izrael – Irlandia (20:45) | 1,25 : 1,20 | 37,5 / 27,3 / 35,1 | 70,2% | 44,3% | 76,8% | 49,8% | rynek 2,69 / 3,30 / 2,65 |

**Korekty λ:**
- Serbia: -10% za brak Vlahovicia i Mitrovicia. Po weryfikacji z 24.09 nie więcej: wtedy przy -20% Serbia strzeliła w 4. minucie.
- Holandia: bez korekty za Brobbeya, bo ma głęboką kadrę ofensywną.
- Andora: λ 0,85, a nie niżej. To mecz dwóch słabych drużyn, więc obowiązuje podłoga ~0,7 (reguła 5).
- Kosowo i Walia: słabsze drużyny dostały najwyżej -5% (reguła 7).
- Niemcy: λ dobrane tak, by 1X2 zgadzało się z rynkiem (ok. 69%), zgodnie z regułą 5 dla meczów o dużej różnicy klas.

**Typy 1X2 w przedziale 50-85%.** Przy #2, #3 i #4 remis jest pokryty podwójną szansą. Pozostaje scenariusz „odwrotnego wyniku”: 16-20% w modelu, zgodnie z rynkiem.

**Rozjazdy model–rynek powyżej 10 pp:** tylko Gibraltar–Andora (Andora: model 28%, rynek ~40%).

## Skrót — tenis (model punkt→gem→set→mecz)

| Mecz | p_serve A : B | Wygrana (model) | Rynek | Oczek. gemy | Uwagi |
|---|---|---|---|---|---|
| Jodar – Fritz (Laver Cup, 3. set to super tie-break do 10) | 0,618 : 0,676 | Fritz 76,4% | ok. 70% | — | Fritz 2-0: 46,6%, Fritz +1,5 seta: 90,0% |
| Zverev – Tien (Laver Cup) | 0,665 : 0,634 | Zverev 64,8% | 2-0 @1,92 | — | Tien +1,5 seta: 64% |
| Hurkacz – Harris (Chengdu QF) | 0,680 : 0,704* | Harris 60,9% | Hurkacz ~62% | 27,0 | Harris +1,5 seta: 81,8%; O21,5: 78,3%; O22,5: 69,3%. *p_serve Hurkacza szacowane |

## Skrót — e-sport

| Seria | Format | p_map (C9) | C9 wygrywa | Dokładny wynik (top 3) | Handicap / total map |
|---|---|---|---|---|---|
| Cloud9 – Team Liquid (LCS, UB final) | BO5 | 0,42 | 35,3% | 1-3: 24,6%, 2-3: 20,7%, 0-3: 19,5% | Liquid +1,5: 79,7%; C9 +1,5: 55,9% (Betclic 1,65, EV 0,92); Over 3,5 mapy: 73,1% |

Zwycięzca awansuje do wielkiego finału 4.10, a przegrany spada do finału dolnej drabinki 3.10. Obie drużyny mają więc drugą szansę, co nieco obniża stawkę.

---
Źródła:
- [mecze24 / podkarpacielive, Litwa–Azerbejdżan (Betclic 2,40/3,10/2,90)](https://www.mecze24.pl/aktualnosci/litwa-azerbejdzan-typy-kursy-statystyki-27-09-2026)
- [mecze24, Dania–Walia](https://www.mecze24.pl/aktualnosci/dania-walia-typy-kursy-na-mecz-27-09-2026)
- [mecze24, Serbia–Holandia](https://www.mecze24.pl/aktualnosci/serbia-holandia-typy-kursy-27-09-2026)
- [sportowefakty, Niemcy–Grecja](https://sportowefakty.wp.pl/bukmacherzy/1276098/niemcy-grecja-w-lidze-narodow-typy-kursy-sklady)
- [sportowefakty, Norwegia–Portugalia](https://sportowefakty.wp.pl/bukmacherzy/1276104/haaland-kontra-ronaldo-norwegia-portugalia-typy-kursy-sklady)
- [mecze24, Austria–Kosowo](https://www.mecze24.pl/aktualnosci/austria-kosowo-typy-kursy-statystyki-27-09-2026)
- [mecze24, Izrael–Irlandia](https://www.mecze24.pl/aktualnosci/izrael-irlandia-typy-kursy-na-mecz-27-09-2026)
- [sport1.pl, Gibraltar–Andora](https://sport1.pl/typy/gibraltar-andorra-27-09-2026-4111818)
- [scores24, Belgia–Francja 28.09](https://scores24.live/pl/soccer/m-28-09-2026-belgium-france-prediction)
- [sportowefakty, Hurkacz–Harris](https://sportowefakty.wp.pl/bukmacherzy/1276047/hurkacz-gra-o-polfinal-w-chengdu-bedzie-faworytem-meczu-typy-i-kursy-na-mecz)
- [Sportskeeda, Hurkacz–Harris](https://www.sportskeeda.com/tennis/hubert-hurkacz-vs-lloyd-harris-preview-head-to-head-odds-prediction-betting-tips-chengdu-open-2026)
- [Dimers, Hurkacz–Harris](https://www.dimers.com/tennis/news/lloyd-harris-vs-hubert-hurkacz-tennis-prediction-atp-chengdu-open-2026-ac)
- [ATP, harmonogram Chengdu](https://www.atptour.com/en/scores/current/chengdu/7581/daily-schedule)
- [Yahoo, Laver Cup 7-5](https://sports.yahoo.com/articles/team-europe-leads-team-world-000223636.html)
- [Field Level Media, LCS](https://fieldlevelmedia.com/esports/team-liquid-to-face-cloud9-in-upper-bracket-final-at-lcs-summer-playoffs/)
- [tennis.com, Miedwiediew–Wong](https://www.tennis.com/tournaments/hangzhou-open/matches/d-medvedev-vs-c-wong-2026-09-27)

*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
