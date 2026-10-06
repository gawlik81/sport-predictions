# TOP 100 predykcji i superkupon — wtorek, 06.10.2026 (piłka nożna, tenis, e-sport)

Użyte skille: football-predictor, tennis-predictor i esports-predictor. Analiza przygotowana o 07:50 CEST.

**Ograniczenia danych (ważne):**
- Proxy tego środowiska blokuje strony z kursami i statystykami: betclic.pl, flashscore, sofascore, HLTV, Liquipedia, Tennis Abstract, UEFA, Wikipedia. Wszystkie dane pochodzą z wyników wyszukiwarki (zapowiedzi, agregatory kursów, prediction markets).
- **Kursy Betclic nie są dostępne.** Kolumna „Kurs rynk.” zawiera kurs cytowany w zapowiedziach (oznaczony ✓) albo szacunek: kurs fair × 0,94, czyli typowa marża. Przed postawieniem kuponu sprawdź kursy u bukmachera.
- λ goli w piłce dopasowałem do kursów rynkowych 1X2, zgodnie z regułą 5 skilla dla meczów reprezentacji. Model nie twierdzi więc, że ma przewagę nad rynkiem. Ranking porządkuje typy według prawdopodobieństwa, a nie według value.
- Statystyk serwisu i returnu w tenisie nie dało się pobrać (Tennis Abstract jest zablokowany), więc p_serve oszacowałem z rankingu, formy i kursów. Zgodnie z regułą 4 tennis-predictor **total gemów i handicapy gemowe nie weszły do rankingu**. Są tylko w skrócie tenisowym.
- E-sport: brak statystyk map i stron (HLTV jest zablokowany), więc p_map wyprowadziłem z kursów. Zgodnie z regułą 7 nie ma totali rund. Od typów e-sportowych odjąłem 3 pp, bo reguły skilla e-sportowego nie są jeszcze zweryfikowane.

**Oferta dnia (godziny CEST):**
- **Piłka nożna, Liga Narodów, 4. kolejka:**
  - Anglia–Czechy, Chorwacja–Hiszpania, Szwajcaria–Macedonia Płn., Szkocja–Słowenia, Mołdawia–Słowacja, Albania–San Marino, Białoruś–Finlandia, Estonia–Islandia, Luksemburg–Bułgaria (wszystkie o 20:45);
  - Kazachstan–Wyspy Owcze (16:00).
- **Piłka nożna, mecze towarzyskie:** Korea Płd.–Uzbekistan (13:00), Chiny–Tadżykistan (ok. 13:35), Rosja–Nigeria (19:00), Algieria–Niger (21:30), Indie–Urugwaj, Jordania–Wenezuela (godziny niepotwierdzone), Argentyna–Benin (w nocy 6/7.10 czasu PL, pożegnanie Messiego).
- **Tenis:**
  - finał ATP 500 Tokio, Alcaraz–Lehecka (ok. 11:00);
  - finał ATP 500 Pekin, Djokovic–de Minaur (nie wcześniej niż 13:00);
  - WTA 1000 Pekin, 1/8 finału: Muchova–Osaka (ok. 09:00), Bartunkova–Kraus (ok. 10:10), Andreeva–Snigur (godzina niepotwierdzona).
  - Mecz Noskova–Alexandrova zaczął się o 06:10 i został pominięty. Mecze Świątek–Jovic, Zheng–Charaeva i Li–Svitolina grane są 7.10 o 05:00 czasu PL, więc nie należą do dzisiejszej oferty.
- **E-sport, CS2 ESL Pro League S24 (Katowice), faza szwajcarska, runda 4, BO3:**
  - pula 2-1 (zwycięzca awansuje do Spodka): Spirit–1win, FURIA–Aurora, Falcons–NAVI;
  - pula 1-2 (przegrany odpada): G2–PARIVISION, BetBoom–9z, Legacy–M80.
  - LoL Worlds startuje dopiero 15.10, a playoffy Dota 2 BLAST Slam VIII na LAN-ie od 8.10. Dziś nie ma w tych grach meczów tier-1.

**Zasady rankingu:**
- Uwzględnia tylko typy z kursem fair z modelu ≥1,15 (prawdopodobieństwo ≤ 87%).
- Najwyżej 6 rynków z jednego meczu. Typy z tego samego meczu są skorelowane.
- Kolejność według prawdopodobieństwa po korektach, czyli kolumny „Prawd.”.
- Korekty:
  - mecze towarzyskie: -2 pp (zmiany, eksperymenty w składach);
  - Under 3,5 przy łącznym λ > 2,3: -2 pp;
  - WTA: -3 pp dla faworytki;
  - Djokovic: -3 pp (39 lat, trzysetowy ćwierćfinał z Zverevem);
  - e-sport: -3 pp.

## TOP 100 predykcji

| # | Mecz | Godz. | Typ | Prawd. | Kurs fair |
|---|---|---|---|---|---|
| 1 | Albania – San Marino (LN C) | 20:45 | **BTTS – nie** | 86,9% | 1,15 |
| 2 | Kazachstan – Wyspy Owcze (LN C) | 16:00 | **Over 0,5 gola** | 86,5% | 1,16 |
| 3 | Mołdawia – Słowacja (LN C) | 20:45 | **X2 (Słowacja lub remis)** | 86,1% | 1,16 |
| 4 | Albania – San Marino (LN C) | 20:45 | **San Marino nie strzeli (czyste konto Albania)** | 86,1% | 1,16 |
| 5 | Chorwacja – Hiszpania (LN A) | 20:45 | **X2 (Hiszpania lub remis)** | 85,9% | 1,16 |
| 6 | Kazachstan – Wyspy Owcze (LN C) | 16:00 | **Under 3,5 gola** | 85,7% | 1,17 |
| 7 | Bartunkova – Kraus (WTA 1000 Pekin, 1/8) | ok. 10:10 | **Bartunkova +1,5 seta (wygra min. seta)** | 85,4% | 1,17 |
| 8 | Szwajcaria – Macedonia Płn. (LN B) | 20:45 | **Szwajcaria strzeli gola** | 85,0% | 1,18 |
| 9 | Luksemburg – Bułgaria (LN C) | 20:45 | **Under 3,5 gola** | 84,8% | 1,18 |
| 10 | Anglia – Czechy (LN A) | 20:45 | **1 (Anglia)** | 84,2% | 1,19 |
| 11 | Rosja – Nigeria (tow.) | 19:00 | **Rosja +1,5 (nie przegra 2+ golami)** | 83,7% | 1,19 |
| 12 | Kazachstan – Wyspy Owcze (LN C) | 16:00 | **Wyspy Owcze +1,5 (nie przegra 2+ golami)** | 83,7% | 1,20 |
| 13 | Algieria – Niger (tow.) | 21:30 | **Under 4,5 gola** | 83,5% | 1,20 |
| 14 | Indie – Urugwaj (tow.) | b.d. | **Under 4,5 gola** | 83,5% | 1,20 |
| 15 | Anglia – Czechy (LN A) | 20:45 | **Over 1,5 gola** | 83,5% | 1,20 |
| 16 | Indie – Urugwaj (tow.) | b.d. | **12 (bez remisu)** | 83,1% | 1,20 |
| 17 | Luksemburg – Bułgaria (LN C) | 20:45 | **Bułgaria +1,5 (nie przegra 2+ golami)** | 82,5% | 1,21 |
| 18 | Andreeva – Snigur (WTA 1000 Pekin, 1/8) | rano | **Andreeva wygrywa** | 82,4% | 1,21 |
| 19 | Albania – San Marino (LN C) | 20:45 | **Under 4,5 gola** | 82,4% | 1,21 |
| 20 | Djokovic – de Minaur (ATP 500 Pekin, finał) | od 13:00 | **Djokovic +1,5 seta (wygra min. seta)** | 82,2% | 1,22 |
| 21 | Rosja – Nigeria (tow.) | 19:00 | **Nigeria +1,5 (nie przegra 2+ golami)** | 82,2% | 1,22 |
| 22 | Szkocja – Słowenia (LN B) | 20:45 | **Under 3,5 gola** | 81,9% | 1,22 |
| 23 | Mołdawia – Słowacja (LN C) | 20:45 | **Słowacja strzeli gola** | 81,7% | 1,22 |
| 24 | Chorwacja – Hiszpania (LN A) | 20:45 | **Over 1,5 gola** | 81,5% | 1,23 |
| 25 | Algieria – Niger (tow.) | 21:30 | **1 (Algieria)** | 81,1% | 1,23 |
| 26 | Chorwacja – Hiszpania (LN A) | 20:45 | **12 (bez remisu)** | 81,1% | 1,23 |
| 27 | Chiny – Tadżykistan (tow.) | ok. 13:35 | **Under 3,5 gola** | 80,9% | 1,24 |
| 28 | Argentyna – Benin (tow.) | noc 6/7.10 | **Argentyna -1,5 (wygrywa 2+ golami)** | 79,9% | 1,25 |
| 29 | Jordania – Wenezuela (tow.) | b.d. | **Wenezuela +1,5 (nie przegra 2+ golami)** | 79,9% | 1,25 |
| 30 | Chorwacja – Hiszpania (LN A) | 20:45 | **Under 4,5 gola** | 79,8% | 1,25 |
| 31 | Szwajcaria – Macedonia Płn. (LN B) | 20:45 | **12 (bez remisu)** | 79,7% | 1,25 |
| 32 | Albania – San Marino (LN C) | 20:45 | **Over 1,5 gola** | 79,3% | 1,26 |
| 33 | Korea Płd. – Uzbekistan (tow.) | 13:00 | **1X (Korea lub remis)** | 79,3% | 1,26 |
| 34 | Korea Płd. – Uzbekistan (tow.) | 13:00 | **Under 3,5 gola** | 78,9% | 1,27 |
| 35 | Falcons – NAVI (CS2 EPL S24, BO3) | 19:00 | **Falcons +1,5 mapy** | 78,9% | 1,27 |
| 36 | Estonia – Islandia (LN C) | 20:45 | **Islandia strzeli gola** | 78,8% | 1,27 |
| 37 | Alcaraz – Lehecka (ATP 500 Tokio, finał) | 11:00 | **Alcaraz wygrywa** | 78,6% | 1,27 |
| 38 | FURIA – Aurora (CS2 EPL S24, BO3) | 16:30 | **FURIA +1,5 mapy** | 78,5% | 1,27 |
| 39 | Estonia – Islandia (LN C) | 20:45 | **X2 (Islandia lub remis)** | 78,1% | 1,28 |
| 40 | G2 – PARIVISION (CS2 EPL S24, BO3) | 14:00 | **G2 +1,5 mapy** | 78,1% | 1,28 |
| 41 | Jordania – Wenezuela (tow.) | b.d. | **Under 3,5 gola** | 77,9% | 1,28 |
| 42 | Indie – Urugwaj (tow.) | b.d. | **2 (Urugwaj)** | 77,4% | 1,29 |
| 43 | BetBoom – 9z (CS2 EPL S24, BO3) | 16:30 | **BetBoom +1,5 mapy** | 77,2% | 1,30 |
| 44 | Anglia – Czechy (LN A) | 20:45 | **Under 4,5 gola** | 77,2% | 1,30 |
| 45 | Mołdawia – Słowacja (LN C) | 20:45 | **Under 3,5 gola** | 76,9% | 1,30 |
| 46 | Albania – San Marino (LN C) | 20:45 | **Albania Over 1,5 gola** | 76,9% | 1,30 |
| 47 | Szkocja – Słowenia (LN B) | 20:45 | **Słowenia +1,5 (nie przegra 2+ golami)** | 76,9% | 1,30 |
| 48 | Mołdawia – Słowacja (LN C) | 20:45 | **12 (bez remisu)** | 76,6% | 1,30 |
| 49 | Białoruś – Finlandia (LN C) | 20:45 | **Białoruś +1,5 (nie przegra 2+ golami)** | 76,6% | 1,31 |
| 50 | Białoruś – Finlandia (LN C) | 20:45 | **Finlandia strzeli gola** | 76,5% | 1,31 |
| 51 | Szkocja – Słowenia (LN B) | 20:45 | **1X (Szkocja lub remis)** | 76,4% | 1,31 |
| 52 | Chiny – Tadżykistan (tow.) | ok. 13:35 | **Tadżykistan +1,5 (nie przegra 2+ golami)** | 76,1% | 1,31 |
| 53 | Anglia – Czechy (LN A) | 20:45 | **Anglia Over 1,5 gola** | 76,0% | 1,32 |
| 54 | Korea Płd. – Uzbekistan (tow.) | 13:00 | **Korea strzeli gola** | 75,7% | 1,32 |
| 55 | Spirit – 1win (CS2 EPL S24, BO3) | ok. 14:00 | **Spirit wygrywa serię** | 75,4% | 1,33 |
| 56 | Muchova – Osaka (WTA 1000 Pekin, 1/8) | ok. 09:00 | **Osaka +1,5 seta (wygra min. seta)** | 75,0% | 1,33 |
| 57 | Rosja – Nigeria (tow.) | 19:00 | **Under 3,5 gola** | 74,9% | 1,33 |
| 58 | Szwajcaria – Macedonia Płn. (LN B) | 20:45 | **Under 3,5 gola** | 74,8% | 1,34 |
| 59 | Estonia – Islandia (LN C) | 20:45 | **Under 3,5 gola** | 74,8% | 1,34 |
| 60 | Białoruś – Finlandia (LN C) | 20:45 | **Under 3,5 gola** | 74,8% | 1,34 |
| 61 | Estonia – Islandia (LN C) | 20:45 | **12 (bez remisu)** | 74,4% | 1,34 |
| 62 | Szkocja – Słowenia (LN B) | 20:45 | **Szkocja strzeli gola** | 74,1% | 1,35 |
| 63 | Indie – Urugwaj (tow.) | b.d. | **Over 1,5 gola** | 74,0% | 1,35 |
| 64 | Algieria – Niger (tow.) | 21:30 | **Over 1,5 gola** | 74,0% | 1,35 |
| 65 | Muchova – Osaka (WTA 1000 Pekin, 1/8) | ok. 09:00 | **Muchova +1,5 seta (wygra min. seta)** | 74,0% | 1,35 |
| 66 | Białoruś – Finlandia (LN C) | 20:45 | **X2 (Finlandia lub remis)** | 74,0% | 1,35 |
| 67 | Chiny – Tadżykistan (tow.) | ok. 13:35 | **1X (Chiny lub remis)** | 73,6% | 1,36 |
| 68 | Białoruś – Finlandia (LN C) | 20:45 | **12 (bez remisu)** | 73,5% | 1,36 |
| 69 | Albania – San Marino (LN C) | 20:45 | **Albania -1,5 (wygrywa 2+ golami)** | 73,3% | 1,36 |
| 70 | Argentyna – Benin (tow.) | noc 6/7.10 | **BTTS – nie** | 72,8% | 1,37 |
| 71 | Argentyna – Benin (tow.) | noc 6/7.10 | **Over 2,5 gola** | 72,7% | 1,38 |
| 72 | Estonia – Islandia (LN C) | 20:45 | **Estonia +1,5 (nie przegra 2+ golami)** | 72,6% | 1,38 |
| 73 | Argentyna – Benin (tow.) | noc 6/7.10 | **Benin nie strzeli (czyste konto Argentyna)** | 72,1% | 1,39 |
| 74 | Szkocja – Słowenia (LN B) | 20:45 | **12 (bez remisu)** | 72,1% | 1,39 |
| 75 | Korea Płd. – Uzbekistan (tow.) | 13:00 | **12 (bez remisu)** | 71,8% | 1,39 |
| 76 | Luksemburg – Bułgaria (LN C) | 20:45 | **1X (Luksemburg lub remis)** | 71,5% | 1,40 |
| 77 | Algieria – Niger (tow.) | 21:30 | **BTTS – nie** | 71,1% | 1,41 |
| 78 | Chiny – Tadżykistan (tow.) | ok. 13:35 | **Chiny strzeli gola** | 70,7% | 1,41 |
| 79 | Kazachstan – Wyspy Owcze (LN C) | 16:00 | **1X (Kazachstan lub remis)** | 70,5% | 1,42 |
| 80 | Białoruś – Finlandia (LN C) | 20:45 | **Over 1,5 gola** | 70,2% | 1,42 |
| 81 | Estonia – Islandia (LN C) | 20:45 | **Over 1,5 gola** | 70,2% | 1,42 |
| 82 | Szwajcaria – Macedonia Płn. (LN B) | 20:45 | **Over 1,5 gola** | 70,2% | 1,42 |
| 83 | Rosja – Nigeria (tow.) | 19:00 | **12 (bez remisu)** | 70,0% | 1,43 |
| 84 | Luksemburg – Bułgaria (LN C) | 20:45 | **12 (bez remisu)** | 69,9% | 1,43 |
| 85 | Szwajcaria – Macedonia Płn. (LN B) | 20:45 | **1 (Szwajcaria)** | 69,8% | 1,43 |
| 86 | Jordania – Wenezuela (tow.) | b.d. | **12 (bez remisu)** | 69,8% | 1,43 |
| 87 | Chiny – Tadżykistan (tow.) | ok. 13:35 | **12 (bez remisu)** | 69,5% | 1,44 |
| 88 | Korea Płd. – Uzbekistan (tow.) | 13:00 | **Uzbekistan +1,5 (nie przegra 2+ golami)** | 69,4% | 1,44 |
| 89 | Kazachstan – Wyspy Owcze (LN C) | 16:00 | **12 (bez remisu)** | 69,4% | 1,44 |
| 90 | Jordania – Wenezuela (tow.) | b.d. | **Jordania strzeli gola** | 69,3% | 1,44 |
| 91 | Legacy – M80 (CS2 EPL S24, BO3) | ok. 19:00 | **Legacy wygrywa serię** | 68,8% | 1,45 |
| 92 | Algieria – Niger (tow.) | 21:30 | **Niger nie strzeli (czyste konto Algieria)** | 68,5% | 1,46 |
| 93 | Luksemburg – Bułgaria (LN C) | 20:45 | **Luksemburg strzeli gola** | 68,3% | 1,46 |
| 94 | Mołdawia – Słowacja (LN C) | 20:45 | **Over 1,5 gola** | 68,1% | 1,47 |
| 95 | Rosja – Nigeria (tow.) | 19:00 | **Rosja strzeli gola** | 67,9% | 1,47 |
| 96 | Algieria – Niger (tow.) | 21:30 | **Algieria Over 1,5 gola** | 67,2% | 1,49 |
| 97 | Bartunkova – Kraus (WTA 1000 Pekin, 1/8) | ok. 10:10 | **Bartunkova wygrywa** | 67,1% | 1,49 |
| 98 | Jordania – Wenezuela (tow.) | b.d. | **1X (Jordania lub remis)** | 67,0% | 1,49 |
| 99 | Chorwacja – Hiszpania (LN A) | 20:45 | **2 (Hiszpania)** | 67,0% | 1,49 |
| 100 | Kazachstan – Wyspy Owcze (LN C) | 16:00 | **Kazachstan strzeli gola** | 66,7% | 1,50 |

**Oczekiwana liczba trafień: ok. 76 ze 100.** Typy z jednego meczu są silnie skorelowane, np. Over 0,5 i Under 3,5 w meczu Kazachstan–Wyspy Owcze. Rzeczywista wariancja jest więc dużo większa niż przy 100 niezależnych typach.

Podział: Piłka – 87, Tenis – 7, E-sport – 6

## SUPERKUPON: 18 zdarzeń, kurs ok. 106

**Jak powstał kupon:**
- Każde zdarzenie pochodzi z innego meczu. Wszystkie typy są z listy TOP 100.
- Z kuponu wyłączyłem:
  - mecze WTA z rana (mogą zacząć się przed postawieniem kuponu, a Andreeva–Snigur nie ma potwierdzonej godziny);
  - Argentynę–Benin (gra w nocy).
- Optymalizacja: maksymalne łączne prawdopodobieństwo przy łącznym kursie > 100 i liczbie zdarzeń ≤ 20.
- Porównałem warianty od 16 do 20 zdarzeń: 16 → 0,30%, 17 → 0,32%, 18 → 0,29%, 19 → 0,26%, 20 → 0,21%.
- **Wybrałem 18 zdarzeń**, bo dają zapas ok. 6% nad progiem kursu 100. Kursy są szacunkowe, a wariant 17-zdarzeniowy (100,8) mógłby u bukmachera spaść poniżej 100.

| # | Godz. | Mecz | Typ | Prawd. | Kurs fair | Kurs rynk. | Nr w TOP 100 |
|---|---|---|---|---|---|---|---|
| 1 | 11:00 | Alcaraz – Lehecka (ATP 500 Tokio, finał) | **Alcaraz wygrywa** | 78,6% | 1,27 | 1,25 ✓ | 37 |
| 2 | 13:00 | Korea Płd. – Uzbekistan (tow.) | **Uzbekistan +1,5 (nie przegra 2+ golami)** | 69,4% | 1,44 | 1,32 | 88 |
| 3 | ok. 13:35 | Chiny – Tadżykistan (tow.) | **12 (bez remisu)** | 69,5% | 1,44 | 1,32 | 87 |
| 4 | 16:00 | Kazachstan – Wyspy Owcze (LN C) | **12 (bez remisu)** | 69,4% | 1,44 | 1,36 | 89 |
| 5 | ok. 19:00 | Legacy – M80 (CS2 EPL S24, BO3) | **Legacy wygrywa serię** | 68,8% | 1,45 | 1,34 ✓ | 91 |
| 6 | 19:00 | Rosja – Nigeria (tow.) | **Rosja strzeli gola** | 67,9% | 1,47 | 1,35 | 95 |
| 7 | 20:45 | Albania – San Marino (LN C) | **Over 1,5 gola** | 79,3% | 1,26 | 1,19 | 32 |
| 8 | 20:45 | Anglia – Czechy (LN A) | **1 (Anglia)** | 84,2% | 1,19 | 1,15 ✓ | 10 |
| 9 | 20:45 | Białoruś – Finlandia (LN C) | **Over 1,5 gola** | 70,2% | 1,42 | 1,34 | 80 |
| 10 | 20:45 | Chorwacja – Hiszpania (LN A) | **Under 4,5 gola** | 79,8% | 1,25 | 1,18 | 30 |
| 11 | 20:45 | Estonia – Islandia (LN C) | **Over 1,5 gola** | 70,2% | 1,42 | 1,34 | 81 |
| 12 | 20:45 | Luksemburg – Bułgaria (LN C) | **Luksemburg strzeli gola** | 68,3% | 1,46 | 1,38 | 93 |
| 13 | 20:45 | Mołdawia – Słowacja (LN C) | **Over 1,5 gola** | 68,1% | 1,47 | 1,38 | 94 |
| 14 | 20:45 | Szkocja – Słowenia (LN B) | **Szkocja strzeli gola** | 74,1% | 1,35 | 1,27 | 62 |
| 15 | 20:45 | Szwajcaria – Macedonia Płn. (LN B) | **Over 1,5 gola** | 70,2% | 1,42 | 1,34 | 82 |
| 16 | 21:30 | Algieria – Niger (tow.) | **BTTS – nie** | 71,1% | 1,41 | 1,29 | 77 |
| 17 | b.d. | Indie – Urugwaj (tow.) | **Over 1,5 gola** | 74,0% | 1,35 | 1,24 | 63 |
| 18 | b.d. | Jordania – Wenezuela (tow.) | **Jordania strzeli gola** | 69,3% | 1,44 | 1,32 | 90 |

**Łączny kurs (szacunkowy, rynkowy): ok. 106,32.** Łączny kurs fair z modelu: ok. 351.

**Szansa trafienia całego kuponu: ok. 0,3%, czyli mniej więcej 1 do 351.** Wartość oczekiwana: ok. 0,30 zł na każdy postawiony 1 zł.

To uczciwa liczba, nie pesymizm. Każde z 18 zdarzeń jest obciążone marżą bukmachera (ok. 6%), a model ma λ dopasowane do rynku, więc nie zakłada przewagi nad kursami. Kurs > 100 z „pewniaków” po 1,15-1,40 wymaga wielu zdarzeń, a każde kolejne mnoży ryzyko. Kupon traktuj jako zabawę za symboliczną stawkę, nie jako inwestycję.

**Ryzyka kuponu:**
- 11 zdarzeń rozgrywa się o 20:45 w Lidze Narodów. Z weryfikacji 24 i 26.09:
  - Over 1,5 w meczach reprezentacji wszedł 15 razy na 18;
  - wyjątkiem były mecze dwóch defensywnych drużyn (Słowenia–Szkocja 0-0).
- Najsłabsze ogniwa (ok. 68%):
  - Mołdawia–Słowacja, Over 1,5: Słowacja zremisowała 1-1 na Wyspach Owczych, a w pierwszym meczu wygrała 2-0;
  - Luksemburg strzeli gola: obie drużyny mają liczne braki — Luksemburgowi brakuje m.in. Barreiro (zawieszony), Sinaniego i Martinsa;
  - Rosja strzeli gola.
- Anglia–Czechy, 1:
  - Tuchel zapowiada rotację, z kadry wypadli Scott i Konsa, a Kane może zacząć na ławce;
  - Czechy przegrały 4 mecze z rzędu.
  - Ryzyko remisu (11%) i wygranej Czech (4,5%) jest wliczone w prawdopodobieństwo.
- Chorwacja–Hiszpania, Under 4,5: Chorwacja straciła 7 goli z Anglią, ale Hiszpanii brakuje Ferrana Torresa, Nico Williamsa i Grimaldo.
- Legacy–M80, Legacy: p_map wyprowadziłem z kursu 1,34. Mecz o przetrwanie (pula 1-2), a składów nie potwierdziłem na Liquipedii, bo jest zablokowana.
- Alcaraz–Lehecka: Alcaraz odrabiał straty w półfinale z Munarem (5-7 6-3 6-1). Lehecka gra mocnym serwisem i wygrał pewnie 6-4 6-2 z Vacherotem.
- Indie–Urugwaj i Jordania–Wenezuela nie mają potwierdzonej godziny. Sprawdź, czy są w ofercie przed postawieniem kuponu.

**Wariant z wyższą szansą (poza TOP 100):**
- Optymalizator bez ograniczenia do TOP 100 wybrał 9 zdarzeń po ok. 52-59% z kursami 1,60-1,75 (m.in. BetBoom @1,72, Macedonia +1,5, Chorwacja +1,5).
- Szansa całego kuponu: ok. 0,48%, czyli 1 do ~210. Przy kursie > 100 mniej zdarzeń oznacza mniej marż, więc trafienie jest ok. 1,6 razy bardziej prawdopodobne.
- Te zdarzenia nie są jednak „najpewniejsze”, więc to tylko alternatywa.

## Skrót: piłka nożna (model Poissona, λ dopasowane do rynku)

| Mecz | Godz. | λ gole | 1X2 (%) | O1,5 | O2,5 | U3,5 | BTTS | Rynek |
|---|---|---|---|---|---|---|---|---|
| Anglia – Czechy (LN A) | 20:45 | 2,75 : 0,50 | 84,2 / 11,3 / 4,5 | 83,5% | 63,0% | 59,1% | 36,8% | 1,15 / 7,30 / 15,50 |
| Chorwacja – Hiszpania (LN A) | 20:45 | 0,90 : 2,20 | 14,1 / 18,9 / 67,0 | 81,5% | 59,9% | 62,5% | 52,8% | 9,20 / 5,00 / 1,28 |
| Szwajcaria – Macedonia Płn. (LN B) | 20:45 | 1,90 : 0,55 | 69,8 / 20,3 / 9,9 | 70,2% | 44,3% | 76,8% | 36,0% | Szwajcaria ~1,25-1,36 |
| Szkocja – Słowenia (LN B) | 20:45 | 1,35 : 0,85 | 48,5 / 27,9 / 23,6 | 64,5% | 37,7% | 81,9% | 42,4% | 1,80 / 3,40 / 4,55 |
| Mołdawia – Słowacja (LN C) | 20:45 | 0,65 : 1,70 | 13,9 / 23,4 / 62,8 | 68,1% | 41,7% | 78,9% | 39,1% | Słowacja 1,37-1,41 |
| Albania – San Marino (LN C) | 20:45 | 2,80 : 0,15 | 91,3 / 7,7 / 1,0 | 79,3% | 56,5% | 65,8% | 13,1% | Albania 1,01-1,02 |
| Białoruś – Finlandia (LN C) | 20:45 | 1,00 : 1,45 | 26,0 / 26,5 / 47,5 | 70,2% | 44,3% | 76,8% | 48,4% | Finlandia 1,75-2,00 |
| Estonia – Islandia (LN C) | 20:45 | 0,90 : 1,55 | 21,9 / 25,6 / 52,6 | 70,2% | 44,3% | 76,8% | 46,7% | Islandia ~1,67 |
| Luksemburg – Bułgaria (LN C) | 20:45 | 1,15 : 0,90 | 41,4 / 30,1 / 28,5 | 60,7% | 33,7% | 84,8% | 40,6% | 2,10 / 3,00 / 3,50 |
| Kazachstan – Wyspy Owcze (LN C) | 16:00 | 1,10 : 0,90 | 39,9 / 30,6 / 29,5 | 59,4% | 32,3% | 85,7% | 39,6% | 2,30-2,49 / 2,90-3,20 / 3,00-3,22 |
| Algieria – Niger (tow.) | 21:30 | 2,40 : 0,35 | 83,1 / 13,0 / 3,9 | 76,0% | 51,9% | 70,3% | 26,9% | 1,09 / 6,84 / 16,00 |
| Argentyna – Benin (tow.) | noc 6/7.10 | 3,60 : 0,30 | 93,9 / 4,9 / 1,2 | 90,0% | 74,7% | 45,4% | 25,2% | 1,01 / 43 / 75; O3,5 1,26 |
| Indie – Urugwaj (tow.) | b.d. | 0,45 : 2,30 | 5,7 / 14,9 / 79,4 | 76,0% | 51,9% | 70,3% | 32,6% | Urugwaj ~86% |
| Korea Płd. – Uzbekistan (tow.) | 13:00 | 1,50 : 0,75 | 55,1 / 26,2 / 18,7 | 65,7% | 39,1% | 80,9% | 41,0% | Korea ~1,65 |
| Rosja – Nigeria (tow.) | 19:00 | 1,20 : 1,15 | 37,2 / 28,0 / 34,8 | 68,1% | 41,7% | 78,9% | 47,8% | brak kursów (Rosja ~1,82 w 1 źródle) |
| Chiny – Tadżykistan (tow.) | ok. 13:35 | 1,30 : 0,85 | 47,1 / 28,5 / 24,4 | 63,3% | 36,4% | 82,9% | 41,7% | brak kursów |
| Jordania – Wenezuela (tow.) | b.d. | 1,25 : 1,05 | 40,8 / 28,2 / 31,0 | 66,9% | 40,4% | 79,9% | 46,4% | model zewn. 44/27/29 |

**Kontekst i korekty λ:**
- **Anglia–Czechy.**
  - Anglia wygrała 7-0 w Chorwacji, a Czechy przegrały 4 mecze z rzędu (1-3 z Hiszpanią).
  - Tuchel zapowiedział rotację: Scott i Konsa są kontuzjowani, a Guehi, Bellingham i Gordon mogą odpocząć.
  - λ Anglii 2,75 jest nieco poniżej wyceny rynku (O2,5 @1,36), właśnie przez rotację.
- **Chorwacja–Hiszpania.**
  - Chorwacja przegrała 0-7 z Anglią, najwyżej w historii. Według zapowiedzi kadrę prowadzi Bilić.
  - Hiszpanii brakuje Ferrana Torresa, Nico Williamsa i Grimaldo. Cubarsí wraca do składu.
  - Rynek daje Hiszpanii ok. 75%, model po korekcie za braki 67%. X2 ma 85,9%.
- **Szwajcaria–Macedonia Płn.**
  - Szwajcarii brakuje Xhaki (wykluczony), Embolo (zawieszony) i Zakarii (kontuzja). Tydzień temu wygrała jednak 3-0 w Skopje.
  - Macedonia nie wygrała 8 meczów z rzędu.
- **Szkocja–Słowenia.**
  - Szkocję prowadzi nowy trener, Pocognoli. Brakuje McTominaya, Adamsa i Shanklanda.
  - Słowenii brakuje Šeška. Szkocja wygrała 2-0 w Macedonii.
  - Niski łączny λ (2,2): Under 3,5 ma 81,9%.
- **Mołdawia–Słowacja.** Słowacja wygrała 2-0 u siebie (gole przed przerwą), ale zremisowała 1-1 na Wyspach Owczych. Mołdawia ma bilans 0-2-3 w ostatnich meczach.
- **Albania–San Marino.**
  - San Marino nie strzeliło gola od 18 meczów i przegrało 0-7 z Finlandią oraz 0-4 z Białorusią.
  - Albania wygrała z San Marino 5 razy z rzędu, z bilansem bramek 16-0.
  - Zgodnie z regułą 5 (duża różnica klas) nie stosuję podłogi λ 0,7 dla San Marino. Typy z kursem fair < 1,15 (np. wygrana Albanii, ok. 91%) odpadają przez filtr.
- **Luksemburg–Bułgaria.**
  - Duże braki po obu stronach. Luksemburg: Korac, Sinani, Jans i Martins (kontuzje), Mahmutović i Barreiro (zawieszenia).
  - Bułgaria: L. Petkov i Velkovski (zawieszenia), M. Petkov i T. Ivanov (wycofani).
  - Zgodnie z regułą 7 korekta dla każdej drużyny wynosi najwyżej -5%. Najpewniejszy jest Under 3,5 (84,8%).
- **Kazachstan–Wyspy Owcze.**
  - Wyspy Owcze zremisowały 1-1 ze Słowacją, a Kazachstan ma 1 punkt.
  - Kazachstanowi brakuje Satpayeva i Zaynutdinova.
  - Mecz bez faworyta, więc najpewniejsze są Over 0,5 i Under 3,5.
- **Mecze towarzyskie.** Każdy typ obciąłem o 2 pp, bo w takich meczach zdarzają się zmiany i eksperymenty w składach. Dla Rosji–Nigerii, Chin–Tadżykistanu i Jordanii–Wenezueli λ to luźne szacunki z rankingu FIFA i jednego modelu zewnętrznego. Nigeria przegrała 0-3 z Gwineą Bissau, a 1. mecz z Rosją skończył się 1-1.
- **Rożne:** nie modelowałem ich. Dla reprezentacji nie ma dwóch niezależnych źródeł rozbicia rożnych (Krok 2b, pkt 4), a większość serwisów jest zablokowana.

## Skrót: tenis (model punkt → gem → set → mecz, p_serve szacowane)

| Mecz | Godz. | p_serve A : B | Wygrana A | 2-0 A | 0-2 A | Oczek. gemy | Rynek |
|---|---|---|---|---|---|---|---|
| Alcaraz – Lehecka (ATP 500 Tokio, finał) | 11:00 | 0,69 : 0,62 | 78,6% | 49,3% | 8,9% | 24,5 | Alcaraz 1,25 (-400), O/U 21,5 |
| Djokovic – de Minaur (ATP 500 Pekin, finał) | od 13:00 | 0,67 : 0,64 | 64,3% | 35,6% | 16,2% | 25,5 | Djokovic 1,50-1,53 |
| Andreeva – Snigur (WTA 1000 Pekin, 1/8) | rano | 0,60 : 0,53 | 85,4% | 57,7% | 5,8% | 22,3 | Andreeva -5,5 gema @1,81 |
| Bartunkova – Kraus (WTA 1000 Pekin, 1/8) | ok. 10:10 | 0,58 : 0,55 | 70,1% | 40,7% | 13,1% | 23,8 | brak |
| Muchova – Osaka (WTA 1000 Pekin, 1/8) | ok. 09:00 | 0,58 : 0,58 | 50,0% | 25,0% | 25,0% | 24,7 | brak (~50/50) |

**Kontekst:**
- **Alcaraz–Lehecka.** Alcaraz odrobił straty z Munarem i wygrał 5-7 6-3 6-1. Lehecka pokonał Vacherota 6-4 6-2. Model (78,6%) jest zgodny z rynkiem (ok. 78%).
- **Djokovic–de Minaur.**
  - Djokovic ma w Pekinie bilans 33-0 i prowadzi w H2H 3-1. W ćwierćfinale wygrał z Zverevem po trzech setach, a półfinał skończył się po 1,5 seta przez dyskwalifikację Miedwiediewa (piłka trafiła widza).
  - de Minaur awansował po kreczu Hurkacza.
  - Djokovic ma 39 lat, więc odjąłem 3 pp. Dlatego wybrałem **Djokovic +1,5 seta (82,2%)** zamiast jego zwycięstwa.
  - Według weryfikacji z 26.09 underdog +1,5 seta to najlepszy rynek (4/5). Wariant de Minaur +1,5 seta ma w modelu 64,4%, kurs fair 1,55.
- **Andreeva–Snigur.**
  - Snigur przeszła Kawę (z 0-3 w decydującym secie) i Paolini po comebacku, więc jest zmęczona, ale ma rytm meczowy (reguła 2).
  - Andreeva odrobiła stratę seta z Yuan (3-6 6-0 6-0).
  - Typ: Andreeva wygrywa, 82,4% po -3 pp. Godziny meczu nie potwierdziłem.
- **Bartunkova–Kraus.**
  - Bartunkova pokonała Sabalenkę 6-4 6-3. To jej drugi wynik powyżej oczekiwań w turnieju, więc zgodnie z regułą 10 oceniam ją wyżej niż wynika z rankingu.
  - Typ w rankingu to bezpieczniejszy wariant: Bartunkova +1,5 seta (85,4%).
  - Ryzyko: pierwszy mecz po największym zwycięstwie w karierze.
- **Muchova–Osaka.**
  - Muchova wygrała oba tegoroczne mecze, ale Osaka wygrała trzy wcześniejsze mecze na twardej nawierzchni. Model: 50/50.
  - W rankingu tylko +1,5 seta dla obu zawodniczek. Typy wzajemnie się nie wykluczają: obie wchodzą przy wyniku 2-1.

## Skrót: e-sport (CS2 EPL S24, BO3, p_map z kursów)

| Seria | Godz. | p_map A | A wygrywa | A -1,5 (2-0) | B +1,5 | Over 2,5 mapy | Rynek |
|---|---|---|---|---|---|---|---|
| Spirit – 1win (CS2 EPL S24, BO3) | ok. 14:00 | 0,70 | 78,4% | 49,0% | 51,0% | 42,0% | brak kursów; parę podaje HLTV |
| G2 – PARIVISION (CS2 EPL S24, BO3) | 14:00 | 0,56 | 59,7% | 31,9% | 68,1% | 49,2% | Polymarket G2 59% |
| FURIA – Aurora (CS2 EPL S24, BO3) | 16:30 | 0,57 | 60,4% | 32,5% | 67,5% | 49,0% | FURIA 1,61 / Aurora 2,16 |
| BetBoom – 9z (CS2 EPL S24, BO3) | 16:30 | 0,56 | 58,2% | 30,8% | 69,2% | 49,4% | BetBoom ~1,72 |
| Falcons – NAVI (CS2 EPL S24, BO3) | 19:00 | 0,57 | 61,2% | 33,1% | 66,9% | 48,9% | Polymarket Falcons 61% |
| Legacy – M80 (CS2 EPL S24, BO3) | ok. 19:00 | 0,65 | 71,8% | 42,2% | 57,8% | 45,5% | Legacy 1,34 / M80 3,21 |

**Kontekst:**
- Po dwóch dniach MOUZ (2:0 ze Spiritem) i Vitality (2:1 z Falconsami) awansowały do play-offów z bilansem 3-0.
- Spirit (1. rozstawienie) przegrał z MOUZ i gra o awans z 1win. 1win wcześniej pokonał G2. Kursów na ten mecz nie znalazłem, więc p_map 0,70 to szacunek z różnicy klas.
- FURIA wygrała wszystkie mecze H2H z Aurorą w ostatnich 6 miesiącach.
- G2 gra o przetrwanie i o kwalifikację na Major w Singapurze.
- Składów nie zweryfikowałem na Liquipedii (reguła 9), bo jest zablokowana. W zapowiedziach nie znalazłem informacji o stand-inach.
- W rankingu są tylko typy +1,5 mapy i zwycięstwo Spirit oraz Legacy. Typy +1,5 dla faworytów wchodzą przy 2-0 i 2-1.

## Świadomie pominięte

- **Typy z kursem fair < 1,15**, np. wygrane Albanii (91%), Argentyny (94%) i Algierii (83%), wchodzą tylko w wersjach z handicapem lub w innych rynkach.
- **Total gemów i handicapy gemowe w tenisie:** reguła 4 (p_serve szacowane). Orientacyjnie:
  - Alcaraz–Lehecka: oczekiwane ok. 24,5 gema, O21,5 w modelu ok. 70% (rynek ~57%);
  - Djokovic–de Minaur: oczekiwane ok. 25,5 gema.
- **Noskova–Alexandrova** (start 06:10, przed analizą).
- **Mecze Świątek–Jovic, Zheng–Charaeva i Li–Svitolina** grane są 7.10 o 05:00 czasu PL. Świątek ma na rynku ok. 66%.
- **Eliminacje ATP Szanghaj, U21 (m.in. Irlandia–Anglia U21), EFL Trophy, Dota 2 tier-2 (PARI Universe Qualifier, EPL World SEA):** brak danych, które pozwalają na model.
- **Rożne i kartki:** brak dwóch niezależnych źródeł danych.

---
Źródła (przez wyszukiwarkę; strony były niedostępne do bezpośredniego pobrania):
- [weszlo: Anglia–Czechy (kursy 1,15/7,3/15,5)](https://weszlo.com/bukmacherzy/typy/anglia-czechy-zapowiedz-i-typy-na-lige-narodow-6-10-2026/)
- [weszlo: Chorwacja–Hiszpania](https://weszlo.com/bukmacherzy/typy/chorwacja-hiszpania-zapowiedz-i-typy-na-lige-narodow-6-10-2026/)
- [mecze24: Kazachstan–Wyspy Owcze](https://www.mecze24.pl/aktualnosci/kazachstan-wyspy-owcze-typy-kursy-statystyki-prognozy-06-10-2026)
- [betfan: Szkocja–Słowenia](https://sport.betfan.pl/szkocja-slowenia-typy-kursy-gdzie-ogladac-06-10-ln/)
- [Wyniki LN 3.10 (vietnam.vn)](https://www.vietnam.vn/en/ket-qua-bong-da-hom-nay-3-10-kich-tinh-uefa-nations-league)
- [soccervital: Mołdawia–Słowacja (kursy)](https://www.soccervital.com/moldova-vs-slovakia-soccer-prediction-jggaj5499.html)
- [easyodds: Albania–San Marino](https://easyodds.com/albania-vs-san-marino-betting-odds-tips-predictions-preview-6th-october-2026)
- [footballwhispers: Białoruś–Finlandia](https://footballwhispers.com/blog/belarus-vs-finland-prediction-06-10-2026/)
- [footballwhispers: Estonia–Islandia](https://footballwhispers.com/blog/estonia-vs-iceland-prediction-06-10-26/)
- [sportskeeda: Luksemburg–Bułgaria (składy)](https://www.sportskeeda.com/football/luxembourg-vs-bulgaria-prediction-betting-tips-october-6th-2026)
- [Sports Mole: Kazachstan–Wyspy Owcze](https://www.sportsmole.co.uk/football/nations-league/kazakhstan-vs-faroe-islands_game_259449.html)
- [Sports Mole: Chorwacja–Hiszpania (składy)](https://www.sportsmole.co.uk/football/spain/uefa-nations-league/preview/croatia-vs-spain-prediction-team-news-lineups_606200.html)
- [Racing Post: Anglia–Czechy](https://www.racingpost.com/sport/football-tips/nations-league/england-vs-czech-republic-betting-tips-predictions-team-news-odds-bet-builder-aczvz7H4hfHR/)
- [thepressingzone: Szwajcaria–Macedonia](https://www.thepressingzone.com/switzerland-vs-north-macedonia-prediction-2026/)
- [flashscore: Słowenia–Szkocja (składy)](https://www.flashscore.co.uk/news/football-uefa-nations-league-slovenia-v-scotland-where-to-watch-preview-lineups-and-odds/xOUuW7Rs/)
- [nostrabet: Argentyna–Benin](https://nostrabet.com/en/tips/argentina-benin/)
- [sportskeeda: Indie–Urugwaj](https://www.sportskeeda.com/football/india-vs-uruguay-prediction-betting-tips-october-6th-2026)
- [africasoccer: Algieria–Niger](https://africasoccer.com/?p=608479)
- [afrik-foot: Rosja–Nigeria](https://www.afrik-foot.com/en-ng/super-eagles-vs-russia-kick-off-time-venue)
- [starting11: Korea–Uzbekistan](https://starting11.com/fixtures/south-korea-vs-uzbekistan)
- [dailysports: Jordania–Wenezuela](https://dailysports.net/stat/football/jordan-vs-venezuela/)
- [Olympics.com: finał Pekin (Djokovic–de Minaur)](https://www.olympics.com/en/news/china-open-2026-novak-djokovic-reaches-beijing-final)
- [sportsbettingdime: Djokovic–de Minaur](https://www.sportsbettingdime.com/news/tennis/novak-djokovic-alex-de-minaur-picks-odds-predictions-atp-beijing-final/)
- [sportsbettingdime: Alcaraz–Lehecka](https://www.sportsbettingdime.com/news/tennis/alcaraz-vs-lehecka-expert-picks-props-odds-for-japan-open-final/)
- [ATP: wyniki Tokio](https://www.atptour.com/en/news/tokyo-2026-results)
- [Bleacher Nation: plan WTA Pekin 6.10](https://www.bleachernation.com/how-to-watch/2026/10/05/china-open-schedule-tuesday-october-6-matchups-tv-live-stream-info/)
- [WTA: Bartunkova–Sabalenka](https://www.wtatennis.com/news/4586336/bartunkova-stuns-sabalenka-in-beijing-third-round)
- [liontips: Snigur–Andreeva](https://www.liontips.com/tips/2026/10/05/snigur-andreeva-betting-tip-cf-1-81-and-bets-on-the-wta-beijing-match-october-6-2026)
- [dimers: Jovic–Świątek](https://www.dimers.com/tennis/news/iva-jovic-vs-iga-swiatek-tennis-prediction-wta-china-open-2026-ac)
- [HLTV: pary dnia 3 EPL S24](https://www.hltv.org/news/45649/navi-to-play-falcons-on-epl-s24-day-three)
- [Hotspawn: MOUZ i Vitality w play-offach](https://www.hotspawn.com/counter-strike/news/mouz-and-vitality-first-through-to-playoffs-at-esl-pro-league-season-24)
- [Polymarket: Falcons–NAVI](https://polymarket.com/esports/cs2/esl-pro-league/cs2-fal2-navi-2026-10-06)
- [Polymarket: G2–PARIVISION](https://polymarket.com/esports/cs2/esl-pro-league/cs2-g2-prv-2026-10-06)
- [stavka.tv: FURIA–Aurora](https://stavka.tv/matches/csgo/06-10-2026-furia-aurora-gaming)
- [stavka.tv: Legacy–M80](https://stavka.tv/matches/csgo/06-10-2026-legacy-m80)
- [stavka.tv: 9z–BetBoom](https://stavka.tv/matches/csgo/06-10-2026-9z-betboom-team)

*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
