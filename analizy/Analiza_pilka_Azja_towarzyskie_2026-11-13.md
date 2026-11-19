# Analiza: mecze reprezentacji (towarzyskie) 13.11.2026

Czasy polskie (CET = UTC+1). Źródła: Superbet MCP (`superbet_h2h`, `superbet_event_odds`, `superbet_lineups`, `superbet_stats`), WebSearch (Korea Herald/Korea Times/SBS, Football Australia, africasoccer, infonegocios.com.py, latribuna.hn). Obliczenia: `poisson.py` + własny rozkład Poissona (handicap azjatycki). BettingPros: nie użyty.

**Ograniczenia danych (dotyczą wszystkich meczów):** `superbet_missing_players` zwraca brak danych dla każdego z 5 meczów, `superbet_stats` nie ma średnich (xG, rożne, kartki), składy: status "brak", sędziowie nieogłoszeni. Dlatego rynki rożne/kartki/faule/zawodnika NIE są wyceniane i nie ma typu na kupon (reguła "min. dwa źródła liczb"). Wszystkie mecze to towarzyskie, gdzie obowiązują rotacje (wiele zmian w trakcie meczu), a kluczowa niewiadoma to skład. Pewność ograniczona do niskiej/średniej.

**Kalibracja reprezentacji (SKILL.md):** λ drużyny nie niżej niż 0,7 dla zespołów ofensywnie realnych (Singapur 0,40 to świadomy wyjątek: słaby wynik 0-6 z Malezją, 0-2 z Indonezją, rynek Superbet daje Singapurowi ok. 0,4). Korekty kadrowe w dół <15%. Under 2.5 przy łącznym λ ≤ 2,0 najwyżej średnia pewność (nie dotyczy tu, bo sumy λ to 2,3-3,3). Nie schodzę pod rynek o >5 pp bez konkretów; różnice poniżej uzasadnione.

---

## 1. Singapur - Paragwaj (13.11, 13:00 PL; National Stadium, Singapur) | event 15780698

**Typ (najlepszy rynek):** Paragwaj wygra | **p:** 87,6% | **fair:** 1.14 (≤1.15, pomijać w rankingach) | **Pewność:** średnia

| Rynek | p | fair | Kurs Superbet | Uwagi |
|---|---|---|---|---|
| 1 / X / 2 | 3,0 / 9,4 / 87,6% | 33.3 / 10.7 / 1.14 | 24 / 11 / 1.06 | rynek no-vig 4,0 / 8,7 / 89,1% |
| DC 1X / X2 / 12 | 12,4 / 97,0 / 91,0% | 8.1 / 1.03 / 1.10 | 6.9 / - / 1.04 | skrajnie krótkie |
| Over 1.5 | 84,1% | 1.19 | 1.08 | rynek 90% |
| Over 2.5 | 64,0% | 1.56 | 1.31 | rynek ~73% |
| Over 3.5 | 42,0% | 2.38 | 1.82 | rynek ~50%; różnica 8 pp, mój model niższy za rotację Paragwaju |
| Under 3.5 | 58,0% | 1.72 | 1.87 | |
| BTTS tak | 31,2% | 3.21 | - | |
| AH Paragwaj -1.5 | 69,4% | 1.44 | - | brak kursu w próbce |
| AH Paragwaj -2.5 | ok. 49% | 2.0 | - | |
| AH Singapur +1.5 | 30,6% | 3.27 | - | |
| Paragwaj team Over 1.5 | ok. 78% | 1.28 | 1.13 | |

λ: Singapur 0,40 / Paragwaj 2,90. Najbardziej prawdopodobne wyniki: 0-3, 0-2, 0-4.

**Statystyki:** Singapur ostatnie 5: 0-6 Malezja (wyjazd), 1-0 Bangladesz, 0-2 Indonezja, 2-1 Tajlandia (wyjazd), 1-3 Tajlandia; bramki 4 w 5 meczach z rywalami z Azji PD. Paragwaj: 1-0 Kolumbia, 2-0 Boliwia (wrzesień/październik), po MŚ 2026 (0-1 z Francją 04.07, przebieg turnieju niezweryfikowany). Przepaść klas ogromna (ranking FIFA).
**H2H:** brak.
**Informacje medialne:** Alfaro powołał 27 zawodników na azjatycką trasę (Singapur 13.11, Japonia 17.11, oba w Singapurze), m.in. Eduardo Delmas (Olimpia); pełna lista niepotwierdzona (infonegocios.com.py, latribuna.hn). Skład "brak". Zakończenie sezonu, dwa mecze w 5 dni, więc rotacja prawdopodobna, ale Paragwaj i tak o klasy lepszy.
**Ryzyka:** Paragwaj z rezerwami i niska intensywność (mało goli, wygrana 1-0/2-0 przy Over 1.5 ok.), gol Singapuru z kontry (BTTS 31%); remis lub wygrana Singapuru łącznie ok. 12%.
**Rynek vs fair:** rynek wyżej wycenia Paragwaj (89% vs 87,6%); brak value, typ do kuponu tylko jako element z innym rynkiem (fair 1.14 poniżej progu).

---

## 2. ZEA - Honduras (13.11, 15:10 PL; Mohammed Bin Zayed Stadium, Abu Zabi) | event 15685767

**Typ:** ZEA nie przegra (1X) | **p:** 74,5% | **fair:** 1.34 | **Pewność:** niska-średnia (mecz wyrównany; "brak mocnego typu" na wynik)

| Rynek | p | fair | Kurs Superbet | Uwagi |
|---|---|---|---|---|
| 1 / X / 2 | 47,4 / 27,1 / 25,5% | 2.11 / 3.69 / 3.92 | 2.12 / 3.30 / 3.30 | rynek no-vig 43,8 / 28,1 / 28,1% |
| DC 1X / X2 / 12 | 74,5 / 52,6 / 72,9% | 1.34 / 1.90 / 1.37 | 1.29 / 1.66 / 1.29 | brak value |
| Over 1.5 | 68,1% | 1.47 | 1.36 | rynek 72% |
| Over 2.5 / Under 2.5 | 41,7 / 58,3% | 2.40 / 1.72 | 2.10 / 1.64 | rynek 43,5 / 56,5% |
| Over 3.5 / Under 3.5 | 21,1 / 78,9% | 4.74 / 1.27 | 3.75 / 1.22 | |
| BTTS tak / nie | 46,2 / 53,8% | 2.16 / 1.86 | - | |
| AH ZEA -1 (zwrot przy 1) | win 22,9%, push 24,4% | - | - | |
| AH ZEA -1.5 | 22,9% | 4.37 | - | |
| AH ZEA +1.5 | 91,1% | 1.10 | - | zbyt krótkie |
| AH Honduras +1.5 | 77,1% | 1.30 | - | |

λ: ZEA 1,40 / Honduras 0,95. Wyniki: 1-0, 1-1, 0-1.

**Statystyki:** ZEA (nowy trener Zlatko Dalić od sierpnia 2026), forma: 0-2 z Arabią Saud. (06.10), 1-0 Oman, 1-1 Katar, 3-0 Bahrajn (wyjazd), 4-0 Jemen; 2 gole stracone w 5 meczach, 9 strzelone. Honduras: 1-1 Jamajka, 1-2 Martynika (!), 1-0 Jamajka, 2-3 Surinam, 0-2 Argentyna (VI); 7 straconych w 4 meczach z słabymi rywalami - obrona dziurawa, ale z kontynuowaną formą ofensywną (BTTS w 3/4).
**H2H:** jedno spotkanie, 1-1 (2018), bez znaczenia.
**Informacje medialne:** brak oficjalnego składu ZEA i Hondurasu; lista 26 zawodników ZEA w Abu Zabi/Al-Ain niepotwierdzona w treści (albayan.ae). Honduras po długiej podróży do Zatoki, mecz w klimacie gospodarza; Honduras często gra rezerwowym składem w towarzyskich (Molina). ZEA po sezonie krajowym i Pucharze Zatoki (finał przegrany 0-2 z Arabią).
**Ryzyka:** remis i wygrana Hondurasu razem 52,6%; Honduras z szybkimi skrzydłami w kontrach; dużo zmian w drugiej połowie = chaos, więcej bramek niż model.
**Rynek vs fair:** moje ZEA 47,4% vs rynek 43,8% (+3,6 pp, w tolerancji); Over 2.5 zgodny z rynkiem. Brak wyraźnego value.

---

## 3. Arabia Saudyjska - Korea Płd. (13.11, 15:30 PL; Jassim Bin Hamad Stadium, Doha) | event 15645119

**Typ:** Korea Płd. nie przegra (X2) | **p:** 78,7% | **fair:** 1.27 | **Pewność:** średnia (wynik), niska (dokładny)

| Rynek | p | fair | Kurs Superbet | Uwagi |
|---|---|---|---|---|
| 1 / X / 2 | 21,3 / 26,2 / 52,5% | 4.69 / 3.82 / 1.90 | 4.20 / 3.55 / 1.80 | rynek no-vig 22,1 / 26,2 / 51,7% |
| DC 1X / X2 / 12 | 47,5 / 78,7 / 73,8% | 2.11 / 1.27 / 1.35 | 1.92 / 1.19 / 1.26 | |
| Over 1.5 | 68,1% | 1.47 | 1.36 | |
| Over 2.5 / Under 2.5 | 41,7 / 58,3% | 2.40 / 1.72 | 2.10 / 1.64 | zgodne z rynkiem |
| Over 3.5 / Under 3.5 | 21,1 / 78,9% | 4.74 / 1.27 | 3.75 / 1.22 | |
| BTTS tak / nie | 44,5 / 55,5% | 2.25 / 1.80 | - | |
| AH Korea -1 | win 26,9%, push 25,6% | - | - | |
| AH Korea -1.5 | 26,9% | 3.72 | - | |
| AH Arabia +1.5 | 73,1% | 1.37 | - | |
| AH Korea +1.5 | 93,2% | 1.07 | - | pomijać |

λ: Arabia 0,85 / Korea 1,50. Wyniki: 0-1, 1-1, 0-2.

**Statystyki:** Arabia (Georgios Donis): 2-0 ZEA, 2-0 Irak, 3-0 Oman (wyjazd), 1-0 Kuwejt - 4 mecze bez straty, 8-0; solidna defensywa. Korea (tymczasowy trener Robert Moreno): 2-0 Uzbekistan, 3-0 Ekwador, 1-4 Urugwaj, mecz z Wenezuelą bez wyniku w danych, 0-1 z RPA (czerwiec, MŚ). Zmienne rezultaty, ale mocniejsza kadra.
**H2H:** 2023-09-12 Korea 1-0 Arabia; ogólnie 0-1-2 dla Korei od 2018 (stare, niska waga).
**Informacje medialne:** mecz przeniesiony z Arabii Saudyjskiej do Dohy (zagrożenie ze strony Huti; africasoccer.com, Korea Times). Korea: 26 zawodników powołanych 29.10 w Cheonan, Son Heung-min w kadrze i kapitanem (Al Jazeera, Korea Times); kontekst: spór o atmosferę w drużynie, kontrakt Morena wygasa po dwóch meczach (Doha 13.11, Katar 17.11) przed Pucharem Azji (styczeń, Arabia Saudyjska). Arabia: 30-osobowa lista Donisa, długotrwała kontuzja Hassana Kadesha (obrona; africasoccer.com). Skład brak.
**Ryzyka:** mecz neutralny pod kątem terenu, Arabia w dobrej formie i przed własnym Pucharem Azji (motywacja do testu); Korea z tymczasowym trenerem i turbulencjami (rotacje, brak automatyzmów); wygrana Arabii 21%, remis 26%.
**Rynek vs fair:** moje 52,5% vs rynek 51,7% (zgodne). Brak value.

---

## 4. Katar - Australia (13.11, 15:45 PL; Jassim Bin Hamad Stadium, Doha) | event 15315992

**Typ:** brak mocnego typu na wynik; najlepszy rynek: Under 3.5 (78,9%, fair 1.27) lub Australia nie przegra (X2) 69,9%, fair 1.43 | **Pewność:** niska

| Rynek | p | fair | Kurs Superbet | Uwagi |
|---|---|---|---|---|
| 1 / X / 2 | 30,0 / 27,7 / 42,2% | 3.33 / 3.61 / 2.37 | 3.40 / 3.35 / 2.07 | rynek no-vig 27,4 / 27,8 / 44,9% |
| DC 1X / X2 / 12 | 57,7 / 69,9 / 72,2% | 1.73 / 1.43 / 1.39 | - | |
| Over 1.5 | 68,1% | 1.47 | 1.36 | |
| Over 2.5 / Under 2.5 | 41,7 / 58,3% | 2.40 / 1.72 | 2.12 / 1.63 | rynek 43,5 / 56,5% |
| Over 3.5 / Under 3.5 | 21,1 / 78,9% | 4.74 / 1.27 | 3.75 / 1.22 | |
| BTTS tak / nie | 47,3 / 52,7% | 2.11 / 1.90 | - | |
| AH Australia -1 | win 19,2%, push 23,0% | - | - | |
| AH Australia -1.5 | 19,2% | 5.21 | - | |
| AH Katar +1.5 | 80,8% | 1.24 | - | |
| AH Australia +1.5 | 88,6% | 1.13 | - | pomijać |

λ: Katar 1,05 / Australia 1,30. Wyniki: 1-1, 1-0 Australia, 0-1.

**Statystyki:** Katar (Julen Lopetegui): 2-0 Bahrajn (wyjazd; 2 czerwone), 1-0 Jemen (wyjazd), 1-1 ZEA; w czerwcu 0-6 Kanada, 1-3 Bośnia (poziom MŚ). Słaba ofensywa (4 gole w 3 meczach). Australia (Popovic): 1-1 i 2-4 z Brazylią (wrzesień), w czerwcu 0-2 USA, 2-0 Turcja (MŚ); traci dużo (4 gole z Brazylią).
**H2H:** brak od 2018.
**Informacje medialne:** Australia przywozi 25-osobowy skład z ośmioma zmianami względem września, bez Mathew Ryana, Jacksona Irvine'a, Milosa Degeneka i Aidena O'Neilla (Football Australia, Newcastle Herald); duża rotacja, debiutanci (Diesel Herrington). Skład Kataru nieznany. Mecz o 15:45 PL w Doha (u Kataru na stadionie Jassim bin Hamad). Przed Pucharem Azji (Arabia Saudyjska, styczeń-luty); Australia dalej jedzie do Jordanii.
**Ryzyka:** osłabiona Australia + gospodarze w znanym środowisku = Katar blisko równych szans; Lopetegui testuje skład; obie obrony zawodne, Over 2.5 realny (41,7% w modelu).
**Rynek vs fair:** Australia 42,2% (mój) vs 44,9% (rynek): schodzę o 2,7 pp za osiem zmian i brak liderów, w tolerancji 5 pp.

---

## 5. Kuwejt - Syria (13.11, 17:30 PL; Stadion Al-Sadaqua Walsalam, Kuwejt) | event 15716922

**Typ:** brak mocnego typu na wynik (wyrównane, ok. 40% maks); najlepszy rynek: Under 3.5 (76,8%, fair 1.30) | **Pewność:** niska

| Rynek | p | fair | Kurs Superbet | Uwagi |
|---|---|---|---|---|
| 1 / X / 2 | 32,8 / 27,2 / 40,0% | 3.05 / 3.67 / 2.50 | 3.15 / 3.30 / 2.17 | rynek no-vig 29,4 / 28,0 / 42,6% |
| DC 1X / X2 / 12 | 60,0 / 67,2 / 72,8% | 1.67 / 1.49 / 1.37 | - | |
| Over 1.5 | 70,2% | 1.42 | 1.28 | rynek 74% |
| Over 2.5 / Under 2.5 | 44,3 / 55,7% | 2.26 / 1.80 | 1.90 / 1.78 | rynek 48 / 52%; różnica 3,7 pp |
| Over 3.5 / Under 3.5 | 23,2 / 76,8% | 4.31 / 1.30 | 3.20 / 1.29 | |
| BTTS tak / nie | 49,7 / 50,3% | 2.01 / 1.99 | - | |
| AH Syria -1 | win 18,0%, push 22,0% | - | - | |
| AH Kuwejt +1.5 | 82,0% | 1.22 | - | |
| AH Syria +1.5 | 86,7% | 1.15 | - | graniczne |
| AH Syria -1.5 | 18,0% | 5.56 | - | |

λ: Kuwejt 1,15 / Syria 1,30. Wyniki: 1-1, 1-0 i 0-1.

**Statystyki:** Kuwejt (Helio Sousa): 1-3 Oman (wyjazd), 2-3 Irak (czerwona), 0-1 Arabia Saud., 2-2 Tajlandia (czerwiec), 1-3 ZEA (grudzień 2025): 2 punkty z ostatnich 5, defensywa słaba (10 straconych w 5). Syria (Jose Maria Lana): 1-4 Uzbekistan, 1-1 Jordania, 1-4 Białoruś, 5-1 Afganistan, 0-1 Maroko: ofensywa OK, obrona bardzo dziurawa (10 straconych w 4 meczach z silniejszymi).
**H2H:** 2-2 (09.2025 towarzyski, pierwszy mecz Sousy), Kuwejt 2-1 Syria (2023), ogółem 1-1-1. Niska waga.
**Informacje medialne:** brak opublikowanego składu na 13.11.2026 (Arab Times: brak świeżej listy). Kuwejt gra w domu. Syria po słabej serii wyników, ale w kwalifikacjach rywale to Uzbekistan/Jordania/Białoruś (klasa wyżej).
**Ryzyka:** wyrównany mecz, remis 27%; dużo kartek i zmian (Kuwejt miał czerwone w ostatnich meczach), BTTS prawie 50/50; ławka Syrii słaba.
**Rynek vs fair:** Syria 40,0% (mój) vs 42,6% rynek: schodzę 2,6 pp, bo Syria na wyjeździe z gorszą formą defensywną; w tolerancji.

---

## Podsumowanie i ranking (po filtrze fair > 1.15)

| # | Mecz | Rynek | p | fair | Pewność | Kurs rynkowy | Uwagi |
|---|---|---|---|---|---|---|---|
| 1 | Arabia Saud. - Korea | Korea nie przegra (X2) | 78,7% | 1.27 | średnia | 1.19 | kurs poniżej fair = brak value |
| 2 | Katar - Australia | Under 3.5 gola | 78,9% | 1.27 | niska-średnia | 1.22 | brak value |
| 3 | Kuwejt - Syria | Under 3.5 gola | 76,8% | 1.30 | niska-średnia | 1.29 | zgodne z rynkiem |
| 4 | ZEA - Honduras | ZEA nie przegra (1X) | 74,5% | 1.34 | niska-średnia | 1.29 | brak value |
| 5 | Singapur - Paragwaj | Paragwaj -1.5 AH | 69,4% | 1.44 | średnia | brak | zależy od rotacji; kursu AH brak |

Pominięte (fair ≤ 1.15): Paragwaj wygra (1.14), DC X2 i 12 w meczu Singapuru. Przypadki graniczne 1.15-1.20: Over 1.5 Singapur-Paragwaj (1.19), AH Syria +1.5 (1.15).

**Wniosek:** Kursy Superbet na te mecze są zgodne z moimi p w granicach 1-4 pp, więc brak wyraźnego value; największa niepewność to skład (rotacje w towarzyskich) i brak danych o rożnych/kartkach/sędziach, więc rynków dodatkowych nie rekomenduję. Najbardziej wiarygodne p: zwycięstwo Paragwaju w Singapurze i Korea nie przegra (zgodne z klasą i rynkiem). Najbardziej wyrównane (brak mocnego typu): Katar-Australia, Kuwejt-Syria, ZEA-Honduras.

Oszacowania probabilistyczne, nie gwarancje.
