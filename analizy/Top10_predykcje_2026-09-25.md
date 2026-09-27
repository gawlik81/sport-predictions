# TOP 10 predykcji dnia — piątek, 25.09.2026

**Zakres analizy:**
- Piłka nożna: 8 meczów 1. kolejki Ligi Narodów UEFA 2026/27, dywizje A1, B2, B4 i C2.
- Tenis: ćwierćfinały WTA 500 w Singapurze i WTA 250 w Seulu oraz 1/8 finału ATP 250 w Chengdu i Hangzhou. Wszystkie turnieje na kortach twardych.

**Zasady rankingu:**
- Uwzględnia tylko typy z kursem uczciwym powyżej 1,15.
- Stosuje reguły kalibracji po weryfikacji z 24.09 (patrz `Weryfikacja_predykcji_2026-09-24.md`):
  - λ w piłce nie schodzi poniżej ~0,7, a korekty kadrowe łącznie nie przekraczają ~15%;
  - typy Under traktuję ostrożnie;
  - w tenisie obniżam szansę faworyta w pierwszym meczu po wolnym losie;
  - total gemów trafia do rankingu tylko przy rzeczywistych statystykach serwisu i returnu.

**Poprawa jakości danych w tenisie:** tym razem mamy rzeczywiste SPW/RPW z Tennis Abstract (kort twardy, 2026 lub ostatnie 52 tygodnie). Wejście modelu liczę jako p_serve(A) = SPW(A) − (RPW(B) − średnie RPW touru). Średnie RPW touru to 0,44 w WTA i 0,36 w ATP.

## Ranking

| # | Mecz | Rozgrywki | Typ | Prawd. | Kurs (fair) | Pewność | Kluczowe ryzyko |
|---|------|-----------|-----|--------|-------------|---------|-----------------|
| 1 | Szwecja – Rumunia (20:45) | LN B4 | **1X** | 82,0% | 1,22 | Średnia/Wysoka | Szwecja wygrała 1 z 6 ostatnich meczów i ma liczne urazy (Elanga, Hien). Rumunia nie wygrała 6 wyjazdów z rzędu; Hagi debiutuje w meczu o punkty. Rynek: Szwecja 1,48–1,51 |
| 2 | Polska – Bośnia i H. (20:45) | LN B4 | **1X** | 80,1% | 1,25 | Średnia/Wysoka | Braki u obu (Polska: Grabara, Benedyczak, Frankowski; BiH: Vasilj, Dedić). BiH często remisuje (6 remisów w 10 meczach). Model zgodny z rynkiem (55/25/20) |
| 3 | Andreeva [1] – Fernandez [6] (ok. 12:30) | WTA 500 Singapur, QF | **Andreeva wygrywa** | ~80% (surowo 87,9%) | 1,25 | Średnia | H2H na twardej 0-2 (ostatnio Toronto 2026, 1-6 4-6), dlatego odjąłem 8 pp. Andreeva ma już za sobą mecz w turnieju, więc nie gra pierwszego meczu po wolnym losie. Rynek: 1,30 |
| 4 | Turcja – Francja (20:45) | LN A1 | **X2** | 81,0% | 1,23 | Średnia | Debiut Zidane'a i długa lista braków Francji (Saliba, Tchouaméni, Konaté, Zaïre-Emery). Turcja bez Çalhanoğlu i Yıldıza, ale u siebie groźna |
| 5 | Gruzja – Irlandia Płn. (18:00) | LN B2 | **1X** | 78,0% | 1,28 | Średnia | Irlandia Płn. przegrała 6 z 8 ostatnich wyjazdów; Kwaracchelia gra. Ryzyko: Gruzja przegrała 5 z 10 meczów od 09.2025 |
| 6 | Turcja – Francja (20:45) | LN A1 | **Over 1,5 gola** | 76,9% | 1,30 | Średnia | Rynek wycenia Over 2,5 na 1,43, więc idzie dalej niż model. Uwaga: to ten sam mecz co typ #4, wyniki obu typów są skorelowane |
| 7 | Etcheverry [3] – Jacquet (od 13:30) | ATP 250 Hangzhou, R16 | **Over 21,5 gema** | 74,8% | 1,34 | Średnia | Obaj utrzymują serwis w ok. 84% gemów, oczekiwane 26,4 gema. Ryzyko: próba Jacqueta na poziomie ATP to tylko 8 meczów |
| 8 | Włochy – Belgia (20:45) | LN A1 | **Over 8,5 rożnych** | 75,0% | 1,33 | Średnia/Niska | λ rożnych 4,95 : 5,85. Podział na wywalczone i oddane pochodzi z jednego źródła (Sportsgambler), ale sumy z APWin (11,0 i 12,9 rożnego na mecz) go potwierdzają. Obaj trenerzy nowi (Mancini, van Bommel) |
| 9 | Volynets – Birrell [2] (ok. 05:10) | WTA 250 Seul, QF | **Volynets wygrywa** | 73,0% | 1,37 | Średnia | Model zgodny z rynkiem (1,30). Volynets wygrała oba mecze w Seulu po 6-0 w drugim secie; Birrell wygrała 1 z 6 meczów przed Seulem. H2H 2-2 |
| 10 | Tabilo [3] – Mannarino (od 13:00) | ATP 250 Chengdu, R2 | **Over 21,5 gema** | 72,7% | 1,37 | Średnia | Obaj mocno serwują (hold 83,6% i 77,7%), oczekiwane 26,1 gema. Tabilo gra pierwszy mecz po Pucharze Davisa na mączce, co działa raczej za wyrównanym meczem |

## Świadomie pominięte

- **Tararudee [3] – Joint (Seul).** Model daje Tararudee 82,7%, a rynek ok. 50%, przy czym źródła kursów są sprzeczne. Jej bilans 40-14 na twardej to w dużej mierze mecze ITF i WTA 125, więc statystyki są zawyżone. Tak dużej rozbieżności nie przekładam na typ.
- **Mertens [4] – Chwalińska [5] (Singapur).** Model daje 50,5% na 49,5%, a rynek Mertens 1,35 (ok. 72%). Mertens gra pierwszy mecz od US Open, bo miała wolny los i walkower. Chwalińska prowadzi w H2H 1-0 (6-4 6-0, mączka). **Chwalińska ma tu wartość, ale to rzut monetą, więc nie trafia do TOP 10.**
- **Rublev [2] – Hijikata.** Rublev ma 71,2%, ale gra pierwszy mecz po wolnym losie, a od sierpnia ma na twardej bilans 2-3, w tym porażkę z nr 281. Pominięty zgodnie z regułami 1 i 3 tenisowego Kroku 2b.
- **Preston – Korneeva (Seul).** Korneeva ma 71,8%, zgodnie z rynkiem, ale ma historię kontuzji (mięsień brzucha w sierpniu), a Preston jest rozpędzona po wygranej z Ostapenko.
- **Czarnogóra – Cypr i Armenia – Łotwa: Under 2,5.** Model daje 63,6% i 60,9%, rynek też skłania się ku Under. Po wczorajszych dwóch porażkach Under w meczach reprezentacji (reguła 5 piłkarskiego Kroku 2b) nie wstawiam tych typów do rankingu.
- **Bondar [6] – Ruse [4].** Ruse ma 56,7% w modelu i ok. 62% na rynku. Bondar grała wczoraj 3 h 15 min. Mecz bez wyraźnego faworyta.

## Skrót — piłka nożna (Liga Narodów, 1. kolejka, 25.09)

| Mecz | 1X2 (%) | O1,5 | O2,5 | BTTS | λ gole | Rożne |
|---|---|---|---|---|---|---|
| Gruzja – Irlandia Płn. (18:00) | 51,2 / 26,8 / 22,0 | 66,9% | 40,4% | 43,8% | 1,45 : 0,85 | ok. 4,9 : 4,1 (2 źródła, łącznie ok. 9) |
| Armenia – Łotwa (18:00) | 47,2 / 27,8 / 25,0 | 65,8% | 39,1% | 44,0% | 1,35 : 0,90 | brak wiarygodnych danych |
| Włochy – Belgia | 41,3 / 26,8 / 31,8 | 71,3% | 45,6% | 50,6% | 1,35 : 1,15 | λ 4,95 : 5,85; O8,5 75%, O9,5 64% |
| Turcja – Francja | 19,0 / 22,5 / 58,5 | 76,9% | 53,1% | 51,7% | 0,95 : 1,85 | λ 4,6 : 5,65; O8,5 69% |
| Węgry – Ukraina | 40,8 / 28,2 / 31,0 | 66,9% | 40,4% | 46,4% | 1,25 : 1,05 | źródła rozbieżne |
| Polska – Bośnia i H. | 55,1 / 25,0 / 19,9 | 70,2% | 44,3% | 45,7% | 1,60 : 0,85 | λ 5,5 : 4,1; O7,5 74%, O8,5 62% |
| Szwecja – Rumunia | 58,7 / 23,3 / 18,0 | 73,3% | 48,2% | 47,3% | 1,75 : 0,85 | źródła sprzeczne (Szwecja 3,4 vs 5,15 wywalczonego) |
| Czarnogóra – Cypr | 49,8 / 28,1 / 22,2 | 63,3% | 36,4% | 40,8% | 1,35 : 0,80 | brak drugiego źródła |

**Korekty λ:**
- Francja: -10% za braki w środku pola i obronie.
- Polska i Bośnia: po -5% za braki.
- Ukraina: -8% (bez Dowbyka, nowy trener).
- Włochy i Belgia: λ przybliżone do średniej, bo obaj trenerzy debiutują.
- Nigdzie nie zszedłem poniżej 0,8. Na podstawie weryfikacji z 24.09 unikam agresywnego obniżania.

**Typy 1X2 w przedziale 50-85%.** Dla każdego istnieją oba scenariusze zagrożenia: remis i wygrana słabszej drużyny. Dlatego w rankingu wybrałem podwójne szanse.

## Skrót — tenis

### WTA (średnie RPW touru 0,44)

| Mecz | SPW / RPW (A ; B) | p_serve A : B | Faworyt | Wygrana | Oczek. gemy |
|---|---|---|---|---|---|
| Volynets – Birrell [2] | 57,3/47,0 ; 55,5/44,2 | 0,571 : 0,525 | Volynets | 73,0% | 23,5 |
| Bondar [6] – Ruse [4] | 59,5/41,5 ; 57,8/43,4 | 0,590* : 0,603 | Ruse | 56,7% | 24,9 |
| Preston – Korneeva | 56,7/47,3 ; 57,5/50,8 | 0,499 : 0,542 | Korneeva | 71,8% | 23,5 |
| Tararudee [3] – Joint [5] | 59,4/47,0 ; 54,6/44,7 | 0,587 : 0,516 | Tararudee | 82,7% (!) | 22,6 |
| Mertens [4] – Chwalińska [5] | 60,2/45,3 ; 57,9/47,5 | 0,567 : 0,566 | — | 50,5% | 24,5 |
| Wang – Prozorova | 59,6/42,8 ; 61,1/45,1 | 0,585 : 0,570** | Wang | 57,8% | 24,5 |
| Andreeva [1] – Fernandez [6] | 61,1/47,8 ; 59,4/40,4 | 0,647 : 0,556 | Andreeva | 87,9% (w rankingu ~80%) | 22,3 |
| Sakkari [7] – Gibson | 59,9/45,4 ; 61,5/43,5 | 0,604 : 0,571** | Sakkari | 66,6% | 24,3 |

\* Bondar: -0,01 za zmęczenie po meczu 3 h 15 min.
\*\* Korekta w dół za statystyki zawyżone meczami ITF i WTA 125. Prozorova dostała dodatkowo korektę za ok. 6 h gry w dwóch meczach.

### ATP (średnie RPW touru 0,36)

| Mecz | p_serve A : B | Faworyt | Wygrana | Oczek. gemy | O21,5 |
|---|---|---|---|---|---|
| Tabilo [3] – Mannarino | 0,667 : 0,656 | Tabilo | 55,3% | 26,1 | 72,7% |
| van de Zandschulp [4] – Basilashvili | 0,637 : 0,618 | vdZ | 59,4% | 25,2 | 67,1% |
| Shapovalov [7] – Kopriva | 0,626 : 0,589 | Shapovalov | 68,2% | 24,5 | 62,2% |
| Sonego – Brooksby | 0,656 : 0,622 | Sonego | 66,4% | 25,2 | 66,5% |
| Etcheverry [3] – Jacquet | 0,685 : 0,667 | Etcheverry | 58,4% | 26,4 | 74,8% |
| Marozsán [6] – Daniel | 0,645 : 0,620 | Marozsán | 62,3% | 25,2 | 67,0% |
| Rublev [2] – Hijikata | 0,660 : 0,615 | Rublev | 71,2% | 24,8 | 64,1% |
| Faria [7] – Gaston | 0,667 : 0,623 | Faria | 70,6% | 25,0 | 65,4% |

**Model a rynek w ATP.** Model wyraźnie mniej niż rynek faworyzuje Shapovalova (68% wobec kursu 1,25) i van de Zandschulpa (59% wobec 1,50). W ATP 250, przy zbliżonych statystykach serwisu, model skłania się ku wyrównanym meczom. Dlatego typy na zwycięzców z ATP nie weszły do rankingu, a lepszą propozycją są wysokie totale gemów.

**Poza analizą:** Miedwiediew – Royer, Vacherot, Davidovich Fokina i Hurkacz grają dopiero 26.09.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
