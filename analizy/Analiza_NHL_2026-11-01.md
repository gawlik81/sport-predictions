# Analiza NHL - dzień USA 01.11.2026 (niedziela)

Sprawdzone 01.11.2026 przed południem czasu PL. Źródła: NHL API (tabela, terminarz, liderzy), Daily Faceoff (bramkarze, godz. sprawdzenia: rano 01.11), Pinnacle (kursy i linie, kursy dziesiętne przeliczone z amerykańskich, marża usunięta), NHL.com/ESPN (kontekst). BettingPros: klucz API ustawiony, ale nie wywołany w tej analizie (pominięte, nie blokuje). Początek sezonu (12-15 meczów na drużynę), więc próba mała i λ mieszane z klasą drużyn oraz rynkiem. Brak back-to-back u żadnej z 10 drużyn w danych terminarza (dzień wcześniej 31.10 brak tych meczów w terminarzu NHL API; do potwierdzenia przy składach).

Uwaga o dogrywce: skrypt `nhl_model.py` (Poisson) zaniża remis po 60' (~15-16% vs rynek ~20-22%). W tabelach 60' podaję wartości z remisem skorygowanym do ~20%; moneyline (z OT/karnymi) i puck line to wprost wyniki skryptu. Rynek Pinnacle 60' 3-way ma remis 20-24%.

## Podsumowanie (zwięzła tabela)

| Mecz (czas PL) | Faworyt / ML z OT | Fair ML | 60' (1/X/2) | Puck line | Total (λ łączne) | Najlepszy rynek | Pewność |
|---|---|---|---|---|---|---|---|
| WPG @ CAR (19:00) | CAR 68% | 1.47 / WPG 3.14 | 57/20/23 | WPG +1.5 56% (1.77) | Under 6.5 57% (1.75), λ 3.6+2.45=6.05 | CAR ML (rynek 71% bez marży, brak value) | średnia (bramkarze niepotwierdzeni) |
| MIN @ WSH (21:30) | 50/50 | 2.00 / 2.00 | 40/20/40 | ±1.5 74% (1.36) | Under 6.5 59% (1.69), λ 2.95+2.95=5.9 | brak mocnego typu | niska-średnia |
| UTA @ PHI (22:00) | UTA 61% | 1.63 / PHI 2.59 | UTA 51 / X 20 / PHI 29 | PHI +1.5 64% (1.57) | Under 6.5 59% (1.69), λ 3.3+2.6=5.9 | UTA ML (rynek 59,6%) | niska-średnia (Cossa i Vladar niepotwierdzeni) |
| EDM @ NYR (00:00 02.11) | NYR 54% | 1.85 / EDM 2.17 | NYR 44 / X 20 / EDM 36 | EDM +1.5 69% (1.44) | Over 5.5 62% (1.60), λ 3.35+3.1=6.45 | brak mocnego typu | niska (bramkarz Oilers) |
| OTT @ ANA (02:00 02.11) | OTT 51% | 1.97 / ANA 2.03 | OTT 41 / X 20 / ANA 39 | ±1.5 ok. 72% (1.37-1.39) | Over 5.5 64% (1.57), λ 3.3+3.25=6.55 | brak mocnego typu | niska |

Ranking top (fair ≥ 1.15, p z mojego modelu, nie typy "pewne"):
1. WPG @ CAR - CAR ML 68% (fair 1.47; Pinnacle 1.36, EV ujemne), tylko jako noga kuponu.
2. UTA @ PHI - UTA ML 61% (fair 1.63; Pinnacle 1.63, EV ~0).
3. UTA @ PHI / MIN @ WSH - Under 6.5 po 59% (fair 1.69). Total tylko jeśli składy/bramkarze się potwierdzą.
4. WPG @ CAR - Under 6.5 57% (fair 1.75), Pinnacle zajmuje 6.0 (O -109/U -105), więc 6.5 jest alternatywą.
Żaden rynek nie ma EV > +5% wobec Pinnacle; rynek jest efektywny, a bramkarze niepotwierdzeni. Jedyne marginalne EV: OTT@ANA Under 6.5 (Pinnacle +113, model 48,6% pod... patrz mecz 5) ok. +3,5%.

---

### Winnipeg Jets @ Carolina Hurricanes (01.11, 19:00 PL; 13:00 ET)
**Typ:** Carolina ML (z dogrywką) | **p:** 68% | **Fair odds:** 1.47 | **Pewność:** średnia
**Statystyki drużyn:** CAR 11-2-2, GF/GA 56/36 (3,7 / 2,4 na mecz), seria 3 W, 8-2 w ostatnich 10. WPG 4-7-3 (14 meczów), GF/GA 34/47 (2,4 / 3,4), 1-9 w ostatnich 10, seria 4 porażek (NHL API). Pinnacle: CAR -276 / WPG +235 (71,1 / 28,9% bez marży); 60' CAR 58 / X 20 / WPG 22%; puck line CAR -1,5 -103 (49,5%); total 6.0 (O -109, U -105); team total CAR 3.5 (O -133).
**H2H:** niska waga; Hellebuyck nie gra już w Winnipeg (wymieniony do Devils, Daws przyszedł w pakiecie), skład inny niż w poprzednich latach.
**Bramkarze (Daily Faceoff, rano 01.11):** CAR Kochetkov (SV% .919) - niepotwierdzony; WPG Daws (SV% .886) - niepotwierdzony, alternatywa Skinner (.899).
**Informacje medialne:** brak kontuzji w danych DFO; brak back-to-back; WPG w serii 1-9, ale zgodnie z zasadami nie karzę faworyta/nie premiuję underdoga za formę, tylko za bramkarza (Daws ok. +0,2 gola dla CAR).
**Oczekiwane gole:** CAR 3.6 - WPG 2.45 (łącznie 6.05). Pułap 68% mieści się w limicie ~65-68%; do rynku 71% brakuje 3 pp (bramkarz niepotwierdzony, więc nie podnoszę).
**Rynki dodatkowe (p / fair, wynik skryptu 3.6 vs 2.45):**

| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML CAR (z OT) | 68,2% | 1.47 | średnia |
| ML WPG (z OT) | 31,8% | 3.14 | niska |
| 60' CAR / X / WPG | 57 / 20 / 23% | 1.75 / 5.0 / 4.3 | średnia |
| Puck line CAR -1.5 | 43,6% | 2.29 | niska |
| Puck line WPG +1.5 | 56,4% | 1.77 | średnia |
| Total Over 5.5 / Under 5.5 | ok. 56% / 44% | 1.78 / 2.27 | niska |
| Total Over 6.5 / Under 6.5 | ok. 43% / 57% | 2.33 / 1.75 | niska |
| Anytime goal: Kyle Connor (11 goli w sezonie; NHL API) | ok. 30% | 3.3 | niska, jedno źródło |

**Ryzyka:** Skinner zamiast Dawsa (CAR słabiej), Kochetkov rotacja, gole w pustą bramkę (puck line), CAR zbyt luźno po serii 3 W. Rynek: CAR ML 1.36 (fair 1.47) bez value; WPG ML 3.35 (EV ok. +6% teoretycznie, ale ze słabym Dawsem to pułapka).

### Minnesota Wild @ Washington Capitals (01.11, 21:30 PL; 15:30 ET)
**Typ:** brak mocnego typu (ML 50/50). Najlepszy rynek: Under 6.5 (59%) | **Fair:** 1.69 | **Pewność:** niska-średnia
**Statystyki drużyn:** MIN 9-3-3 (15 m.), GF/GA 47/35 (3,1 / 2,3), 6-? w ostatnich 10, ostatni mecz po dogrywce (OT). WSH 8-4-0 (12 m.), GF/GA 43/37 (3,6 / 3,1), seria 3 W, 7 W w ostatnich 10 (NHL API). Lider strzelców ligi: Kaprizov 14 goli (MIN); Tuch 10 (WSH). Pinnacle: ML -106 / -106 (50/50); 60' WSH 38,6 / X 22,7 / MIN 38,7; total 6.0 (O -115, U +101); puck line WSH +1.5 -276; team totals 3.5 po 139.
**H2H:** niska waga.
**Bramkarze:** MIN Wallstedt (SV% .916) POTWIERDZONY (DFO); WSH Thompson (.903) niepotwierdzony, zapasowy Lindgren (.888) - ryzyko.
**Informacje medialne:** brak zgłoszonych kontuzji w DFO; brak back-to-back; Wild lepsza obrona (2,3 GA), Caps lepszy atak: efekt się równoważy, przewaga własnego lodu +0,1.
**Oczekiwane gole:** WSH 2.95 - MIN 2.95 (łącznie 5.9).
**Rynki dodatkowe (skrypt 2.95 vs 2.95):**

| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML WSH / MIN (z OT) | 50,0% / 50,0% | 2.00 / 2.00 | niska (brak mocnego typu) |
| 60' WSH / X / MIN | 40 / 20 / 40% | 2.50 / 5.0 / 2.50 | niska |
| Puck line ±1.5 (faworyta brak) | -1.5: 26,3% / +1.5: 73,7% | 3.81 / 1.36 | niska (fair ≤ 1.36, +1.5 blisko progu, ale > 1.15) |
| Total Over 5.5 / Under 5.5 | 53,8% / 46,2% | 1.86 / 2.17 | niska |
| Total Over 6.5 / Under 6.5 | 40,9% / 59,1% | 2.44 / 1.69 | średnia |
| Anytime goal: Kaprizov (14 goli) | ok. 33% | 3.0 | niska, jedno źródło |
| Wallstedt obrony (śr. ok. 25.5 przy 27-28 strzałach, SV% .905-.916) | Over 25.5: 48%; Under 25.5: 52% | 2.08 / 1.93 | niska (brak linii rynkowej) |

**Ryzyka:** Lindgren zamiast Thompsona zmienia λ MIN o ok. +0,2; mecz o niskiej dyspersji (remis po 60' ~20% = rozstrzygnięcie w OT, ML to rzut monetą).
**Rynek:** Pinnacle 50/50 = zgodne; Under 6.5 przy linii 6.0 oznacza, że rynek ma Under 6.0 po 101 (~48%), więc mój Under 6.5 nie jest value ponad rynek, tylko wyceną alternatywną linii.

### Utah Mammoth @ Philadelphia Flyers (01.11, 22:00 PL; 16:00 ET)
**Typ:** Utah ML (z dogrywką) | **p:** 61% | **Fair odds:** 1.63 | **Pewność:** niska-średnia
**Statystyki drużyn:** UTA 9-5-0, GF/GA 51/46 (3,6 / 3,3), 6 W w ostatnich 10. PHI 3-8-4 (15 m.), GF/GA 29/51 (1,9 / 3,4), najgorszy atak w próbce, 3 W w ostatnich 10. Michkov 9 goli (PHI), Cooley i Schmaltz po 7 (UTA) (NHL API). Pinnacle: ML PHI +140 / UTA -159 (40,4 / 59,6% bez marży); 60' UTA 47,1 / X 22,3 / PHI 30,6; total 6.0 (O -105, U -110); team totals PHI 2.5 (O -122), UTA 3.5 (O +111).
**H2H:** niska waga; Flyers przeszli zmianę składu w lecie.
**Bramkarze:** UTA Cossa (niepotwierdzony, brak statystyk sezonu w danych); PHI Vladar (SV% .888, niepotwierdzony; Woll .899 alternatywa).
**Informacje medialne:** brak kontuzji w DFO; PHI w kryzysie (3-8-4), ale rynek już to uwzględnia (PHI tylko 40%): nie schodzę poniżej rynku bez konkretów, korekta kryzysu nie stosuje się do faworyta. Wątpliwość: Cossa rzadko startował w NHL, pewność niska.
**Oczekiwane gole:** UTA 3.3 - PHI 2.6 (łącznie 5.9).
**Rynki dodatkowe (skrypt gospodarze=PHI 2.6, goście=UTA 3.3):**

| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML UTA (z OT) | 61,4% | 1.63 | niska-średnia |
| ML PHI (z OT) | 38,6% | 2.59 | niska |
| 60' UTA / X / PHI | 51 / 20 / 29% | 1.96 / 5.0 / 3.45 | niska-średnia |
| Puck line UTA -1.5 | 36,4% | 2.75 | niska |
| Puck line PHI +1.5 | 63,6% | 1.57 | średnia |
| Puck line PHI -1.5 / UTA +1.5 | 17,7% / 82,3% | 5.65 / 1.22 | średnia |
| Total Over 5.5 / Under 5.5 | 53,8% / 46,2% | 1.86 / 2.17 | niska |
| Total Over 6.5 / Under 6.5 | 40,8% / 59,2% | 2.45 / 1.69 | średnia |
| Anytime goal: Michkov (9 goli) | ok. 28% | 3.6 | niska, jedno źródło |

**Ryzyka:** niepewny Cossa (debiut/pierwsze starty), PHI w domu bywa lepsza od wyniku (xG nie sprawdzone), gole w pustą bramkę.
**Rynek:** UTA 1.63 vs fair 1.63 = brak value.

### Edmonton Oilers @ New York Rangers (02.11, 00:00 PL; 19:00 ET)
**Typ:** brak mocnego typu; lekko Rangers ML | **p:** 54% | **Fair odds:** 1.85 | **Pewność:** niska
**Statystyki drużyn:** EDM 10-2-2 (14 m.), GF/GA 60/43 (4,3 / 3,1), 7 W w ostatnich 10, najlepszy atak w próbce (Draisaitl 12 goli, McDavid 8, Podkolzin 9, Bouchard 7 jako obrońca; NHL API). NYR 7-6-1 (14 m.), GF/GA 44/42 (3,1 / 3,0), seria 3 porażek, 4-? w ostatnich 10, Lafrenière 9 goli. Pinnacle (mecz Rangers v Oilers, gospodarz NYR): ML NYR -126 / EDM +112 (54,2 / 45,8%); 60' NYR 42,2 / X 22,3 / EDM 35,5; puck line NYR -1,5 +190, EDM +1,5 -224; total 6.5 (O -112, U -102); team totals NYR 3.5 (O +109), EDM 2.5 (O -170).
**H2H:** niska waga.
**Bramkarze:** EDM Matt Tomkins - "confirmed" w Daily Faceoff, ale notatka strony jest sprzeczna (przypisanie do Oilers vs blurb "starts in NYR"); to prawdopodobnie awaryjne wezwanie z AHL po tym, jak Levi trafił na IR (23.10, The Hockey News), a Jarry (SV% .901) jest zapewne niedostępny/odpoczywa. Brak statystyk NHL = traktuję jako gorszego od średniej: +0,3 gola dla NYR. NYR Garand (SV% .899) niepotwierdzony; Shesterkin (.927) alternatywa i wtedy λ EDM spada o ok. 0,3.
**Informacje medialne:** EDM bez pewnego bramkarza to główne ryzyko; brak innych kontuzji w DFO.
**Oczekiwane gole:** NYR 3.35 - EDM 3.1 (łącznie 6.45).
**Rynki dodatkowe (skrypt NYR 3.35, EDM 3.1):**

| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML NYR (z OT) | 53,9% | 1.85 | niska |
| ML EDM (z OT) | 46,1% | 2.17 | niska |
| 60' NYR / X / EDM | 44 / 20 / 36% | 2.27 / 5.0 / 2.78 | niska |
| Puck line NYR -1.5 / EDM +1.5 | 30,6% / 69,4% | 3.27 / 1.44 | niska / średnia |
| Puck line EDM -1.5 / NYR +1.5 | 24,1% / 75,9% | 4.16 / 1.32 | niska / średnia |
| Total Over 5.5 / Under 5.5 | 62,4% / 37,6% | 1.60 / 2.66 | niska-średnia |
| Total Over 6.5 / Under 6.5 | 49,8% / 50,2% | 2.01 / 1.99 | niska |
| Total Over 7.5 / Under 7.5 | 32,0% / 68,0% | 3.13 / 1.47 | niska |
| Anytime goal: Draisaitl (12 goli) | ok. 34% | 2.9 | niska, jedno źródło i niepotwierdzony skład |

**Ryzyka:** niepotwierdzony bramkarz Oilers (jeśli jednak Jarry, ML NYR spada do ok. 49%); Shesterkin zamiast Garanda; wysoka wariancja (obie ofensywy w formie). Rynek: NYR -126 (fair 1.85 vs kurs 1.79): bez value.

### Ottawa Senators @ Anaheim Ducks (02.11, 02:00 PL; 18:00 PT)
**Typ:** brak mocnego typu (OTT 51%) | **Najlepszy rynek:** Over 5.5 gola 64% (fair 1.57) | **Pewność:** niska
**Statystyki drużyn:** OTT 9-5-1, GF/GA 49/45 (3,3 / 3,0), 5 W w ostatnich 10. ANA 5-7-1 (13 m.), GF/GA 43/50 (3,3 / 3,8), seria 1 porażki, 3 W w ostatnich 10. Stützle i Batherson po 9 goli (OTT), Sennecke 8 (ANA). Pinnacle: ML ANA +105 / OTT -118 (47,4 / 52,6%); 60' OTT 41,2 / X 22,1 / ANA 36,7; total 6.5 (O -130, U +113); puck line OTT -1,5 +238 / ANA +1,5 -305.
**H2H:** niska waga.
**Bramkarze:** OTT Samuel Ersson (niepotwierdzony; w ligowym rankingu SV% tabeli nie ma go w top, wejście na miejsce Ullmarka, SV% .945 w tym sezonie; powód nieznany - back-to-back lub odpoczynek; DFO nie opisuje). ANA Brossoit POTWIERDZONY (DFO), brak SV% w danych.
**Informacje medialne:** brak zgłoszonych kontuzji w DFO; zmiana bramkarza Ottawy względem Ullmarka daje +0,25 gola dla ANA względem scenariusza Ullmarka (uwzględnione).
**Oczekiwane gole:** ANA 3.25 - OTT 3.3 (łącznie 6.55).
**Rynki dodatkowe (skrypt ANA 3.25, OTT 3.3):**

| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML OTT (z OT) | 50,8% | 1.97 | niska (brak mocnego typu) |
| ML ANA (z OT) | 49,2% | 2.03 | niska |
| 60' OTT / X / ANA | 41 / 20 / 39% | 2.44 / 5.0 / 2.56 | niska |
| Puck line ANA -1.5 / OTT +1.5 | 26,7% / 73,3% | 3.74 / 1.37 | niska / średnia |
| Puck line OTT -1.5 / ANA +1.5 | 28,1% / 71,9% | 3.56 / 1.39 | niska / średnia |
| Total Over 5.5 / Under 5.5 | 63,8% / 36,2% | 1.57 / 2.76 | niska-średnia |
| Total Over 6.5 / Under 6.5 | 51,4% / 48,6% | 1.95 / 2.06 | niska |
| Total Over 7.5 / Under 7.5 | 33,5% / 66,5% | 2.99 / 1.50 | niska |
| Anytime goal: Stützle (9 goli) | ok. 31% | 3.2 | niska, jedno źródło |
| Brossoit obrony (ok. 26.5 przy 29 strzałach OTT, SV% ok. .895) | Over 26.5: 48%; Under 26.5: 52% | 2.08 / 1.93 | niska (brak linii rynkowej, brak SV%) |

**Ryzyka:** zmiana bramkarza OTT, Ducks tracą 3,8 gola na mecz (Over wspierane), a Pinnacle O 6.5 -130 (54,6%) sugeruje, że rynek jest bardziej "Over" niż mój (51,4%). Under 6.5 po +113 (kurs 2.13) daje EV ok. +3,5% wg modelu, marginalnie i bez potwierdzonych składów.

---

## Tabela kandydatów na kupon (dla bet-slip-builder)

| Mecz | Rynek | p | fair | Pewność | Zależy od | Kurs rynkowy (Pinnacle) |
|---|---|---|---|---|---|---|
| CAR - WPG | CAR ML (z OT) | 68% | 1.47 | średnia | Daws/Kochetkov | 1.36 (EV ujemne) |
| CAR - WPG | WPG +1.5 | 56% | 1.77 | średnia | j.w. | 1.90 (-111): EV ok. +6% |
| UTA - PHI | UTA ML | 61% | 1.63 | niska-średnia | Cossa, Vladar | 1.63 (EV ~0) |
| UTA - PHI | Under 6.5 | 59% | 1.69 | średnia | bramkarze | brak 6.5 w pobranych (linia 6.0) |
| WSH - MIN | Under 6.5 | 59% | 1.69 | średnia | Thompson | brak 6.5 (linia 6.0: U 1.99) |
| EDM - NYR | NYR +1.5 | 76% | 1.32 | niska-średnia | bramkarz EDM | NYR +1.5 -342 (1.29) |
| OTT - ANA | Over 5.5 | 64% | 1.57 | niska-średnia | Ersson/Ullmark | 1.48 (-208): EV ujemne |

Żadne typy rynku zawodnika nie nadają się na kupon: średnie oparte na jednym źródle (NHL API), składy i linie PP niepotwierdzone, brak linii bukmacherskich propsów. Nie rekomenduję ich.

Skład może się zmienić do rozpoczęcia meczu; bramkarze sprawdzeni w Daily Faceoff rano 01.11, tylko Wallstedt (MIN), Brossoit (ANA) i Tomkins (EDM, z zastrzeżeniem) oznaczeni jako potwierdzeni. To oszacowania probabilistyczne, nie gwarancje.
