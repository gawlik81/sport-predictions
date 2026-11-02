# Analiza tenis - piątek 30.10.2026 (godziny czasu polskiego)

Turnieje: ATP 500 Erste Bank Open Wiedeń (hala, twardy), ATP 500 Swiss Indoors Bazylea (hala, twardy), WTA 125 Queretaro (twardy), WTA 125 Curitiba (ziemia/outdoor).
Wszystkie mecze ćwierćfinałowe wg ESPN mają status "pre" (żaden nie rozpoczęty w chwili analizy), więc żaden nie jest pominięty jako rozegrany.

## Źródła i metoda
- Terminarz, wyniki rund wcześniejszych: ESPN scoreboard (MCP `espn_scoreboard`, atp/wta).
- Ranking, H2H, wyniki 2026 i point-by-point: `apitennis_standings`, `apitennis_h2h` (MCP). Z point-by-point policzyłem dla każdego zawodnika **hold% i break% z ostatnich ~10 meczów (głównie październik 2026, twarde/hala, Szanghaj-Tokio-Wiedeń-Bazylea-Bruksela)**, ze shrinkage do średniej tour (prior 40 gemów: hold 83%, break 17%), korektą o return rywala i przeliczeniem na p_serve (odwrócenie modelu gemu). To jest p_serve **z danych** (nie z rankingu), ale próba jest mała (10-12 meczów, mieszana jakość rywali), więc totale gemów mają pewność najwyżej średnią.
- Kursy: `theoddsapi_odds` (region EU, h2h; kurs odniesienia Pinnacle, marża usunięta proporcjonalnie). BettingPros nie użyty (brak klucza w tej sesji).
- Model: `tennis_model.py` (p_serve -> gem -> set -> mecz) + rozszerzenie własne (ten sam model gemów/setów) do handicapu gemowego i wyniku setowego. Końcowe p_serve skalibrowałem tak, by P(mecz) zgadzało się z moim p po korektach z SKILL.md (poniżej).
- Informacje: Rune (Achilles, 373 dni bez wygranej w ATP) potwierdzone w sieci (tennismajors, puntodebreak, tennisuptodate). Dla pozostałych zawodników wyszukiwanie kontuzji nie dało wiarygodnych wyników 2026 (wyszukiwarka zwracała stare lata), więc brak informacji o kontuzji traktuję jako "nie znaleziono", nie jako "brak kontuzji". Wzmianka o 3-godzinnym meczu Struff-Djokovic NIEPOTWIERDZONA w sieci (wynik 7-6/5-7/7-6 wg ESPN, czas nieznany).

Skróty: p = moje prawdopodobieństwo po korektach, fair = 1/p, rynek = Pinnacle po usunięciu marży (kursy dziesiętne w nawiasie).

---

## ATP Wiedeń (Erste Bank Open), ćwierćfinały

### 13:30 Medvedev - Mannarino
- Ranking: Medvedev 5., Mannarino 73. (Mannarino przeszedł kwalifikacje).
- Forma/zmęczenie: Medvedev po Almaty (do 25.10), w Wiedniu R1 2-0 Merida, R2 3 setów z Norriem (4-6 6-3 7-6) w czwartek. Mannarino: kwalifikacje (2 mecze) + R1 Buse w 3 setach + R2 Mensik 2-0, razem 5 meczów w 5 dni po Almaty; wiek 38. Brak dnia odpoczynku czwartkowego u obu (Mannarino grał w środę).
- Dane 2026 (hold/break, shrinkage): Medvedev 86,5/26,9, Mannarino 78,8/21,2. p_serve: Medvedev 0,640, Mannarino 0,585.
- H2H: Medvedev 4-1 (ostatnio 2-0 Den Bosch czerwiec 2025, 2-0 Pekin 2024 dla Medvedeva; Mannarino wygrał 2-1 Den Bosch 2023). Twarda, hala - Medvedev dominuje.
- Model: 80,4%; rynek 77,2% (1,26 / 4,27). Korekta: rywal przeszedł kwalifikacje (rytm meczowy, 5 meczów w 5 dni), Medvedev po trzysetowcu. Odjąłem 4 pp od modelu -> **p = 76%**.
- **Zwycięzca:** Medvedev 76% (fair 1,32). Rynek 1,26 - brak value, typ informacyjny.
- **Wynik setowy:** 2-0 46,4% (fair 2,16); 2-1 29,6% (3,38); 1-2 13,8%; 0-2 10,2%.
- **Zwycięzca 1. seta:** Medvedev 68% (fair 1,47).
- **Handicap gemowy:** Medvedev -1,5: 70,1% (1,43); -2,5: 63,6% (1,57); -3,5: 53,2% (1,88); Mannarino +4,5: 60,5% (1,65).
- **Total gemów:** E = 24,1; Over 21,5: 59% (1,69); Over 22,5: 52%; Over 23,5: 47%; Under 23,5: 53%. Pewność niska-średnia (p_serve z małej próby), nie do rankingu.
- **Pewność:** średnia. **Ryzyka:** Mannarino (leworęczny, slajsy, hala) wydłuża gemy; Medvedev po 3 setach w czwartek; bez informacji o kontuzjach.

### 15:00 Alcaraz - Paul
- Ranking: Alcaraz 3., Paul 14.
- Forma: Alcaraz w Wiedniu 2 mecze 2-0 (Khachanov, Basilashvili); wcześniej Tokio (3 wygrane, w tym Lehecka... mecz z Lehecką wg API jako porażka) i Szanghaj (porażka z Bergsem wg API, dane wymagają ostrożności). Paul: Rublev 2-0, Darderi 2-0 (6-1 6-2), lekki dojazd; przed turniejem kwalifikacje w Lyonie (przegrał z Fritzem).
- Dane 2026: Alcaraz 83,9/24,8 -> p_serve 0,621 (po korekcie na Paula), Paul 80,8/23,1 -> 0,597. Próbka Alcaraza (12 meczów) zaniża jego poziom (kilka meczów w slabszej dyspozycji w Szanghaju).
- H2H: Alcaraz 8-1 w 9 meczach (Paul wygrał tylko Toronto 2023); ostatnie: US Open 2026 3-0, AO 2026 3-0, RG 2025 3-0.
- Model: 62,1%; rynek 75,7% (1,28 / 3,99). Rozstęp 13,6 pp > 8 pp, więc p niepewne (zasada SKILL.md: nie uśredniam mechanicznie). Model zaniża Alcaraza (mała próba, shrinkage do średniej), H2H i rynek mówią co innego. Biorę wartość poniżej rynku, ale powyżej modelu: **p = 70%**, pewność niska.
- **Zwycięzca:** Alcaraz 70% (fair 1,43). Rynek 1,28 - brak value.
- **Wynik setowy:** 2-0 40,5% (2,47); 2-1 29,5% (3,39); 1-2 16,8%; 0-2 13,2%.
- **Zwycięzca 1. seta:** Alcaraz 63,7% (1,57).
- **Handicap gemowy:** Alcaraz -1,5: 63,5% (1,57); -2,5: 56,9% (1,76); Paul +4,5: 66,0% (1,52).
- **Total gemów:** E = 24,5; Over 21,5: 62%; Over 22,5: 55%; Over 23,5: 49,5%. Pewność niska.
- **Ryzyka:** niska pewność modelu (rozstęp), ewentualna zmienność formy Alcaraza, hala sprzyja serwisowi Paula.

### 17:30 Fery - Zverev
- Ranking: Zverev 2., Fery 35.
- Forma: Zverev R1 Landaluce 2-1, R2 Griekspoor 2-0; Szanghaj 1/8 przegrana z Davidovichem. Fery: R1 Fearnley (walkover/krótki), R2 Musetti 3 sety (czwartek, 16:05Z), kwalifikacje w Lyonie przegrane, Wimbledon 2026 półfinał (przegrana 0-3 z Zverevem 10.07), więc jest w wysokiej formie sezonowej. Fery ma tylko jeden dzień przerwy po trzysetowcu.
- Dane 2026: Zverev 90,4/16,4 -> p_serve 0,695 (po korekcie), Fery 81,1/18,7 -> 0,637.
- H2H: Zverev 1-0 (Wimbledon SF 2026, 3-0).
- Model: 71,2%; rynek 85,9% (1,13 / 6,88). Rozstęp 14,7 pp. Zverev nie 35+, bo bo3 - brak korekty wiekowej. Fery na fali (SF Wimbledonu), model zaniża Zvereva (słaby return, ale serwis dominuje w hali). **p = 76%** (poniżej rynku, powyżej modelu), pewność niska-średnia.
- **Zwycięzca:** Zverev 76% (fair 1,32). Rynek 1,13 - brak value; fair 1,32 jest jedyną nogą > 1,15 po mojej wycenie.
- **Wynik setowy:** 2-0 46,4% (2,16); 2-1 29,6% (3,38); 1-2 13,8%; 0-2 10,2%.
- **Zwycięzca 1. seta:** Zverev 68% (1,47).
- **Handicap gemowy:** Zverev -1,5: 68,9% (1,45); -2,5: 60,1% (1,66); Fery +4,5: 69,3% (1,44); +3,5: 53,6%.
- **Total gemów:** E = 25,3; Over 22,5: 57%; Over 23,5: 50%; Over 24,5: 49%. Serwis obu - tiebreaki możliwe. Pewność niska.
- **Ryzyka:** Zverev i słabszy dzień w secie (ostatnio przegrywa z rywalami z top 30), Fery z momentum.

### 20:00 De Minaur - Berrettini
- Ranking: De Minaur 10., Berrettini 48.
- Forma: De Minaur R1 Machac 3 sety, R2 Tien 2-0; wcześniej Szanghaj (przegrana z Zverevem). Berrettini R1 Etcheverry 2-0, R2 Cobolli (ESPN: wynik "5-2", sugeruje krótki mecz/krecz rywala - NIEPOTWIERDZONE), więc jest świeży. Przed turniejem kwalifikacje w Lyonie.
- Dane 2026: De Minaur 82,1/23,2 -> p_serve 0,667, Berrettini 87,5/13,5 -> 0,640 (silny serwis, słaby return).
- H2H: Berrettini 3-2 (5 meczów w bazie); ostatnie dwa rozdzielone: Miami 2025 wygrał Berrettini 2-0, ćwierćfinał Wiednia 2025 wygrał De Minaur 2-0.
- Model: 63,0%; rynek 67,0% (1,45 / 2,95). Różnica 4 pp - w normie. Berrettini świeższy po krótkiej R2 i z serwisem na hali. **p = 64%**.
- **Zwycięzca:** De Minaur 64% (fair 1,56). Rynek 1,45 - brak value.
- **Wynik setowy:** 2-0 35,3% (2,83); 2-1 28,7% (3,48); 1-2 19,6%; 0-2 16,4%.
- **Zwycięzca 1. seta:** De Minaur 59,4% (1,68).
- **Handicap gemowy:** De Minaur -1,5: 56,2% (1,78); -2,5: 48%; Berrettini +3,5: 63,7% (1,57); +4,5: 76,6%.
- **Total gemów:** E = 25,7; Over 22,5: 61%; Over 23,5: 54%; Over 24,5: 53%. Pewność niska-średnia (wysoka szansa na tiebreaki).
- **Ryzyka:** serwis Berrettiniego daje tiebreaki (wariancja); De Minaur kontruje returnem (break% 23%).

---

## ATP Bazylea (Swiss Indoors), ćwierćfinały

### 14:00 Vacherot - Rune
- Ranking: Vacherot 31., Rune 1202. w rankingu API (rzeczywisty: powrót z ochronionym rankingiem po zerwaniu Achillesa w Sztokholmie, październik 2025; źródła: tennismajors, puntodebreak, tennisuptodate). Brak wygranej w ATP przez 373 dni do 26.10.
- Forma: Rune wygrał R1 z Halysem 3 sety (6-4 6-7 7-6), R2 z Hurkaczem 3 sety (3-6 6-3 7-6?) - dwa trzysetowce w 3 dni; wcześniej porażki w Tokio i Szanghaju; pojawia się wzmianka o wycofaniu z Brukseli z nową dolegliwością (niedokładnie datowane, niepotwierdzone). Vacherot: R1 Navone 2-0, R2 Jodar 3 sety (7-6 2-6 7-6), czwartkowy mecz.
- Dane 2026: Rune (6 meczów od powrotu) 85,9/15,1 -> p_serve 0,686 po korekcie; Vacherot 81,9/14,5 -> 0,655. Próba Rune'a to tylko 6 meczów po kontuzji.
- H2H: Vacherot 1-0 (Szanghaj QF 2025, 2-1).
- Model: Rune 64,6%; rynek Rune 57,8% (1,68 / 2,30). Rozstęp 7 pp, ale informacja twarda: powrót po 11-miesięcznej kontuzji (zasada SKILL.md: wyraźnie obniż pewność) oraz dwa trzysetowce z rzędu. **p Rune = 54%**, Vacherot 46%.
- **Zwycięzca:** Rune 54% (fair 1,85) - brak typu, pewność niska.
- **Wynik setowy:** 2-0 Rune 22,4%; 2-1 23,6%; 1-2 26,3%; 0-2 27,7% (przy p Vacherot 46%: spłaszczone).
- **Zwycięzca 1. seta:** Rune 52,7% (brak przewagi).
- **Handicap gemowy:** Rune -1,5: 45,4%; Vacherot -1,5: 37,6%; Vacherot +3,5: 74,0%; Rune +3,5: 79,5%.
- **Total gemów:** E = 26,4; Over 21,5: 74,6% (fair 1,34); Over 22,5: 65% (1,53); Over 23,5: 57%; Over 24,5: 56,5%. Dwóch serwerów i wyrównany mecz - wysoka szansa na 3 sety lub tiebreaki. Pewność średnia dla niskich linii (Over 21,5).
- **Ryzyka:** Rune - uraz/wycieńczenie (3-setowe mecze), Vacherot tego samego dnia grał w czwartek; wysoka wariancja.

### 15:30 Fils - Fritz
- Ranking: Fils 8., Fritz 13.
- Forma: Fils po Brukseli (półfinał, przegrana ze Struffem 1-2), w Bazylei R1 2-0, R2 3 sety z Michelsenem (czwartek). Fritz: R1 Hijikata 2-0, R2 Shapovalov 2-0 (czwartek), szybkie mecze; w Lyonie wcześniej.
- Dane 2026: Fils 86,8/18,5 -> p_serve 0,683, Fritz 87,7/15,9 -> 0,671 (po korekcie).
- H2H: Fils 1-0 (Tokio 2024, 2-1).
- Model: Fils 55,7%; rynek Fils 50,6% (1,92 / 1,97). Fils: trzysetowiec w czwartek + tydzień w Brukseli (zmęczenie) -> odjąłem ~4,7 pp od modelu: **p Fils = 51%**. Fritz 49%. Brak typu.
- **Zwycięzca:** Fils 51% (fair 1,96) - brak przewagi.
- **Wynik setowy:** 2-0 Fils 25,7%; 2-1 25,3%; 1-2 24,7%; 0-2 24,3%.
- **Zwycięzca 1. seta:** 50,7%.
- **Handicap gemowy:** Fils -1,5: 42,3%; Fritz -1,5: 40,3%; Fils +3,5: 78%; Fritz +3,5: 77%.
- **Total gemów:** E = 26,6; Over 21,5: 76% (1,32); Over 22,5: 66,6% (1,50); Over 23,5: 58%; Over 24,5: 57%; Over 25,5: 54%. Dwaj top-serwisanci hala: wiele tiebreaków. Pewność średnia dla Over 21,5-22,5.
- **Ryzyka:** wariancja tiebreaków; zmęczenie Filsa; brak H2H poza 2024.

### 18:00 Lehecka - Kym
- Ranking: Lehecka 21., Kym 222. (Szwajcar, dzika karta/lokalny).
- Forma: Lehecka R1 Wawrinka 2-0, R2 Altmaier 2-0 (łatwe), wcześniej Bruksela (przegrana z Griekspoorem), Szanghaj. Kym: R1 Rinderknech 2-0 (tiebreak), R2 Shelton 3 sety (7-6 w ostatnim) - mecz z czwartkowej nocy (21:15Z); w stanie euforii domowej publiczności.
- Dane 2026: Lehecka 91,0/18,3 -> p_serve 0,674; Kym 85,0/23,3 -> 0,642 (statystyki Kyma głównie z Challengerów i dwóch meczów ATP - NIE liczą się jak poziom ATP, SKILL.md).
- H2H: brak.
- Model: Lehecka 52,9% (zaniżone przez statystyki Kyma z Challengerów); rynek 70,6% (1,38 / 3,31). Rozstęp 17,7 pp. Zasada: bilans z Challengerów nie liczy się jak ATP, więc nie zakładam, że Kym jest 47%; ranking 222. vs 21. i dwa mecze Lehecki w 2-0. Odejmuję efekt publiczności i formy Kyma: **p Lehecka = 65%**, pewność niska.
- **Zwycięzca:** Lehecka 65% (fair 1,54). Rynek 1,38 - brak value.
- **Wynik setowy:** 2-0 36,2% (2,76); 2-1 28,8% (3,47); 1-2 19,1%; 0-2 15,9%.
- **Zwycięzca 1. seta:** Lehecka 60,1% (1,66).
- **Handicap gemowy:** Lehecka -1,5: 57,1% (1,75); -2,5: 48,7%; Kym +3,5: 63,4% (1,58); Kym +4,5: 76,6% (fair 1,31).
- **Total gemów:** E = 25,8; Over 21,5: 70%; Over 22,5: 61,5%; Over 23,5: 54%. Pewność niska (p_serve Kyma z Challengerów) - bez wpisywania do rankingu.
- **Ryzyka:** Lehecka po ostatnich porażkach z rywalami niżej notowanymi (Jodar, Griekspoor), domowy wpływ publiczności.

### 19:30 Borges - Struff
- Ranking: Borges 53., Struff 47.
- Forma/zmęczenie: Struff przeszedł Brukselę (7 meczów w ~10 dni: finał z Griekspoorem przegrany 1-2), w Bazylei R1 Hanfmann 2-0, R2 Djokovic w 3 setach (7-6 5-7 7-6; trwał prawdopodobnie ponad 2,5 h, godzina 21:15Z czwartek - NIEPOTWIERDZONE co do czasu). Wiek 36. Borges: R1 Brunold 2-0, R2 Ruud 3 sety (środa), czwartek wolny. Przewaga świeżości po stronie Borgesa.
- Dane 2026: Borges 85,6/18,9 -> p_serve 0,691, Struff 88,2/13,6 -> 0,671 (silny serwis, słaby return).
- H2H: Borges 2-0 (Mallorca 2026 w 2 setach, Phoenix Challenger 2023).
- Model: Borges 59,4%; rynek Struff 54,6% (1,78 / 2,14), czyli Borges 45,4%. Różnica 14 pp NA KORZYŚĆ MOJEGO TYPU. Twarda informacja: H2H 2-0, zmęczenie Struffa (siedem meczów w 10 dni + wczorajsza noc), więc nie jest to czysty "własny błąd", ale SKILL.md każe być ostrożnym przy przewadze > 5 pp nad rynkiem: biorę dolną część rozstępu. **p Borges = 53%**, pewność niska.
- **Zwycięzca:** Borges 53% (fair 1,89). Rynek Borges 2,14 (Pinnacle) - formalnie EV ~ +13%, ale oznaczam jako **niepewne**, niska pewność, nie do TOP-N.
- **Wynik setowy:** 2-0 Borges 27%; 2-1 26%; 1-2 24%; 0-2 23%.
- **Zwycięzca 1. seta:** Borges 52%.
- **Handicap gemowy:** Borges -1,5: 44,1%; Struff -1,5: 38,3%; Borges +3,5: 80%; Struff +3,5: 76,1%.
- **Total gemów:** E = 26,7; Over 21,5: 76,7% (1,30); Over 22,5: 67% (1,49); Over 23,5: 58%; Over 24,5: 57,7%. Pewność średnia dla Over 21,5-22,5.
- **Ryzyka:** serwis Struffa na hali potrafi rozstrzygać mecz mimo zmęczenia; zmęczenie Struffa może być przeszacowane, bo wygrał oba tiebreaki wczoraj.

---

## WTA (orientacyjnie; ranking i hold/break z małej próby, w dużej części ITF W50/W100 i kwalifikacje - brak statystyk poziomu WTA 500+)

Queretaro (WTA 125) - mecze od 21:00. Statystyki gemów obejmują mecze ITF i WTA 125 z rywalami niskiej jakości, więc **nie podaję totali gemów ani handicapów** (zasada: p_serve nie z jakościowych danych). Tylko zwycięzca, pewność niska, nie do rankingu.

| Mecz (czas PL) | Ranking | Dane (hold/break, 10 meczów) | H2H | Zwycięzca p (fair) | Pewność |
|---|---|---|---|---|---|
| 21:00 Strakhova - Maria | 487. vs 70. | Strakhova 55,0/45,0; Maria 80,6/52,9 | brak | Maria 72% (1,39) | niska; Strakhova z kwalifikacji, 4 mecze w tygodniu (3-setowiec z Hercog w czwartek); Maria 38 lat, ale rytm |
| 22:30 Monnet - Podoroska | 243. vs 201. | Monnet 47,4/52,9; Podoroska 63,6/45,9 | Podoroska 1-0 (2023) | Podoroska 56% (1,79) | niska, brak typu |
| sob 01:00 Mandlik - Ferro | 210. vs 99. | Mandlik 53,8/42,2; Ferro 61,7/57,9 | Ferro 1-0 (2019) | Ferro 64% (1,56) | niska |
| sob 02:30 Andreescu - Herrero Linana | 129. vs 227. | Andreescu 78,7/49,5; Herrero 66,7/42,3 | brak | Andreescu 62% (1,61) | niska; obie zagrały R2 w nocy z czwartku na piątek (01:05 i 02:50 PL), mała przerwa; Andreescu - historia kontuzji |

Curitiba (WTA 125, ćwierćfinały 16:00-19:00): wszystkie cztery pary mają rywali ranking 100-600 i statystyki głównie z kwalifikacji i ITF (dwa mecze w tygodniu na miejscu), więc **odrzucone** z powodu braku danych poziomu WTA (szczegóły poniżej).

## Soboty 31.10 - półfinały (pary)
- **ATP Wiedeń SF1/SF2:** do ustalenia (zależą od ćwierćfinałów: Medvedev/Mannarino vs Alcaraz/Paul, Fery/Zverev vs De Minaur/Berrettini - ESPN pokazuje TBD vs TBD).
- **ATP Bazylea SF1/SF2:** do ustalenia (ESPN: TBD vs TBD).
- **WTA Pan Pacific Open (Tokio, nie Miami):** SF1 Rakhimova (wygrała QF z Joint) vs do ustalenia; SF2 do ustalenia (zależy od QF Parks-Pohankova, Fernandez-Rybakina, Shnaider-Eala, rozgrywanych rano 30.10; stan niepotwierdzony w tej analizie). Nie wymyślam par.
- **WTA Guangzhou, Queretaro, Curitiba:** SF do ustalenia.

## Odrzucone (z powodem)
- **Alcaraz - Paul, Zverev - Fery, Lehecka - Kym** jako wyższe typy: p niższe od rynku o 5-15 pp bez twardego powodu (poza korektami), niska pewność.
- **Vacherot - Rune:** Rune po 11-miesięcznej kontuzji, dwa trzysetowce; brak typu na zwycięzcę (54/46).
- **Fils - Fritz:** wyrównany (51/49), brak przewagi.
- **Borges - Struff:** typ Borgesa 53% (2,14 rynek) nie wchodzi do rankingu: przewaga nad rynkiem >5 pp, p oparte na zmęczeniu Struffa (czas meczu z Djokovicem niepotwierdzony), niska pewność.
- **Totale gemów w Wiedniu/Bazylei:** podane tylko informacyjnie (p_serve z danych 10 meczów); nie do rankingu top-N.
- **Queretaro Strakhova-Maria, Monnet-Podoroska, Mandlik-Ferro, Andreescu-Herrero Linana:** statystyki z ITF/kwalifikacji, rywale niskiej jakości, brak H2H poza starymi pojedynczymi meczami; podano tylko orientacyjnego zwycięzcę, bez totalu/handicapu, nie do rankingu.
- **Curitiba Grabher-Romero Gormaz (122. vs 131., H2H Romero 2-1 w 2024/25), Sierra-Riera (101. vs 140., ostatnie H2H sprzed 2023), Leme da Silva-F. Jones (609. vs 98.), Ortenzi-Tubello (173. vs 207., H2H ITF 2024 Tubello 4-0):** wyniki z kwalifikacji i ITF W35, brak statystyk WTA, rywale po 2 meczach kwalifikacyjnych w tygodniu; p byłoby szacunkiem z rankingu - odrzucone.

## Podsumowanie najlepszych rynków (po kalibracji)

| Mecz | Rynek | p | Fair | Uwagi |
|---|---|---|---|---|
| Medvedev - Mannarino | Medvedev wygra | 76% | 1,32 | rynek 1,26, brak value, pewność średnia |
| Zverev - Fery | Zverev wygra | 76% | 1,32 | rynek 1,13, brak value, pewność niska-średnia |
| Medvedev - Mannarino | Medvedev -1,5 gema | 70% | 1,43 | |
| Zverev - Fery | Zverev -1,5 gema | 69% | 1,45 | |
| Zverev - Fery | Fery +4,5 gema | 69% | 1,44 | |
| Lehecka - Kym | Kym +4,5 gema | 77% | 1,31 | p_serve Kyma z Challengerów, pewność niska |
| Alcaraz - Paul | Alcaraz wygra | 70% | 1,43 | rynek 1,28, pewność niska |
| Lehecka - Kym | Lehecka wygra | 65% | 1,54 | rynek 1,38 |
| De Minaur - Berrettini | De Minaur wygra | 64% | 1,56 | rynek 1,45 |
| Fils - Fritz | Over 21,5 gemów | 76% | 1,32 | pewność średnia, linia niska |
| Borges - Struff | Over 21,5 gemów | 77% | 1,30 | pewność średnia |
| Vacherot - Rune | Over 21,5 gemów | 75% | 1,34 | pewność średnia |

Są to oszacowania, nie gwarancje.
