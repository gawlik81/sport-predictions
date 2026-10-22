# Analiza dnia 21.10.2026 (dziś + noc 21/22.10), czas polski

Stan: piłka, NBA i NHL gotowe. **Tenis: bez osobnej analizy statystycznej** (brak statystyk serwisu/returnu i kontuzji z sieci), p tenisowe w `ZWERYFIKOWANE_Kupony_10_2026-10-21.md` pochodzą z kursów Betclic po usunięciu marży (limit 75%). E-sport tier-2/3 pominięty (brak tier-1 w oknie).
Terminarz: Liga Mistrzów (9 meczów, 3. kolejka), NBA 11, NHL 2, tenis ATP/WTA (20 singli, jeszcze nierozegrane). MMA: brak gali UFC/KSW w oknie 21-22.10.

## Piłka nożna: Liga Mistrzów, 3. kolejka fazy ligowej

**Metoda i ograniczenia.** Wyszukiwarka nie zwróciła świeżych previewów (składy niepotwierdzone, większość wyników dotyczyła dawnych sezonów). Dlatego λ wyprowadzone z kursów Pinnacle (1X2 + totale, po usunięciu marży, dopasowanie Poissona), potem korekty tylko za konkretne informacje. Zgodnie z regułą "nie schodź pod rynek o >5 pp bez konkretów" prawie wszędzie p = rynek, więc przewaga może wynikać wyłącznie z cen Betclic. Rożne, kartki i faule nie są wyceniane: nie znamy sędziów ani składów (reguła skilla: brak typu).
Skrypt: `poisson.py` (λ gospodarze / λ goście).

| Mecz (godz.) | λ | 1 | X | 2 | O1.5 | O2.5 | O3.5 | U2.5 | U3.5 | BTTS tak | Pewność |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Como - Man United (18:45) | 1.76/1.54 | 43.2% (2.32) | 22.9% | 33.9% (2.95) | 84.1% (1.19) | 64.1% (1.56) | 42.0% | 35.9% | 58.0% | 65.0% (1.54) | niska |
| Lille - Galatasaray (18:45) | 1.64/1.40 | 43.3% (2.31) | 23.9% | 32.8% (3.05) | 80.7% (1.24) | 58.6% (1.71) | 36.2% | 41.4% | 63.8% (1.57) | 60.7% (1.65) | niska |
| Aston Villa - Viking (21:00) | 2.75/0.92 | 75.6% (1.32) | 14.4% | 9.9% | 88.1% (1.14) | 70.9% (1.41) | 49.9% | 29.1% | 50.1% | 56.3% (1.78) | średnia |
| Bayern - Arsenal (21:00) | 1.80/1.42 | 46.6% (2.15) | 22.9% | 30.5% (3.28) | 83.1% (1.20) | 62.4% (1.60) | 40.2% | 37.6% | 59.8% (1.67) | 63.3% (1.58) | niska |
| Club Brugge - Lens (21:00) | 2.06/1.54 | 49.8% (2.01) | 21.2% | 28.9% | 87.4% (1.14) | 69.7% (1.43) | 48.5% | 30.3% | 51.5% | 68.5% (1.46) | niska |
| Inter - Shakhtar (21:00) | 3.02/0.88 | 80.0% (1.25) | 12.2% | 7.7% | 90.1% (1.11) | 74.7% (1.34) | 54.7% | 25.3% | 45.3% | 55.7% (1.80) | średnia |
| Betis - Feyenoord (21:00) | 2.28/1.30 | 59.4% (1.68) | 19.6% | 20.9% | 87.2% (1.15) | 69.4% (1.44) | 48.1% | 30.6% | 51.9% | 65.3% (1.53) | niska |
| Real Madryt - Leipzig (21:00) | 3.22/1.12 | 78.1% (1.28) | 12.4% | 9.5% | 93.0% (1.07) | 80.8% (1.24) | 63.0% (1.59) | 19.2% | 37.0% | 64.7% (1.55) | średnia |
| Sporting - LASK (21:00) | 2.96/0.86 | 79.7% (1.26) | 12.5% | 7.8% | 89.4% (1.12) | 73.4% (1.36) | 53.0% | 26.6% | 47.0% | 54.7% (1.83) | średnia |

Fair odds w nawiasach tylko tam, gdzie ≤ 3.3 (reszta nieistotna dla kuponów). Typy z fair ≤ 1.15 nie wchodzą do rankingów (np. O1.5 w większości meczów).
Dodatkowe rynki z linii Pinnacle: Over 3.5 Real - Leipzig wyceniony przez rynek ok. 61% (alt. 3.5: O -197), zgodnie z modelem 63%.

### Informacje medialne (ze źródłem, stan na 21.10 rano)
- **Aston Villa - Viking:** Emery ma rotować, bo za 3 dni City w Premier League (Sports Mole / Roundtable, preview z 21.10). Ruggeri (ścięgno) poza grą > miesiąc, Maatsen blisko powrotu, Manzambi prawdopodobnie zdrowy. Korekta: λ gospodarzy 2.98 → 2.75 (rotacja), 1: 78.8% → 75.6%.
- **Lille - Galatasaray:** Squawka: brak nowych problemów kadrowych po obu stronach. Obie drużyny po 0 pkt po dwóch kolejkach (Lille bilans bramek -4, Galatasaray -5).
- **Club Brugge - Lens:** brak absencji po obu stronach (starting11, Squawka); Tresoldi 4 gole w 173 min, atak Lens oparty na Thauvinie.
- **Betis - Feyenoord:** Squawka: brak świeżych absencji; Feyenoord z problemami w obronie (7 straconych w 2 meczach). Givairo Read w przewidywanym składzie, wcześniej raportowany jako kontuzjowany: do potwierdzenia.
- **Sporting - LASK:** brak Debasta, Santosa i Zalazara (starting11, bez szczegółów); LASK 0 pkt, bilans -4.
- **Bayern - Arsenal, Inter - Shakhtar, Real - Leipzig, Como - Man United:** brak wiarygodnych aktualnych previewów (wyniki wyszukiwania dotyczyły poprzednich sezonów). Składy niepotwierdzone, pewność niska/średnia.
- Inter ma 0 pkt po dwóch kolejkach: to kryzys faworyta, więc zgodnie z kalibracją nie obniżamy p (forma jest w kursie).

### Ryzyka
- Faworyci 75-80% (Villa, Inter, Real, Sporting): remis ~12-14% oraz niespodzianka 8-10% (łącznie ok. 20-25% na brak wygranej). Rotacja Villi to dodatkowe ryzyko.
- Mecze wyrównane (Como, Lille, Bayern, Brugge): brak mocnego typu na wynik; ewentualnie BTTS/Over, ale tylko jeśli kurs Betclic jest wyraźnie wyższy niż fair.
- Kursy Pinnacle na ten dzień są wysokie dla totali (np. Real - Leipzig 4.0); Betclic może mieć inne linie.

### Kandydaci na kupon z piłki (tylko wejście do `bet-slip-builder`, kursy Betclic do pobrania)
| Mecz | Rynek | p | Fair | Pewność |
|---|---|---|---|---|
| Inter - Shakhtar | 1 | 80.0% | 1.25 | średnia |
| Sporting - LASK | 1 | 79.7% | 1.26 | średnia |
| Real - Leipzig | 1 | 78.1% | 1.28 | średnia |
| Aston Villa - Viking | 1 | 75.6% | 1.32 | średnia (rotacja) |
| Inter - Shakhtar | Over 2.5 | 74.7% | 1.34 | średnia |
| Sporting - LASK | Over 2.5 | 73.4% | 1.36 | średnia |
| Real - Leipzig | Over 2.5 | 80.8% | 1.24 | średnia |
| Aston Villa - Viking | Over 2.5 | 70.9% | 1.41 | średnia |
| Betis - Feyenoord | 1 | 59.4% | 1.68 | niska |
| Club Brugge - Lens | BTTS tak | 68.5% | 1.46 | niska |
| Club Brugge - Lens | Over 2.5 | 69.7% | 1.43 | niska |
| Betis - Feyenoord | Over 2.5 | 69.4% | 1.44 | niska |

To oszacowania probabilistyczne, nie gwarancje.

## NBA, noc 21/22.10 (początek sezonu 2026/27)

**Ograniczenia danych (ważne).** Sezon dopiero wystartował (otwarcie 20.10), więc bieżące statystyki drużyn nie istnieją, a injury report na dziś był nieosiągalny (wyszukiwarka zwróciła wyłącznie dawne sezony, `nba_daily_lineups` HTTP 404). Z previewów: Timberwolves bez DiVincenzo (Achilles, długa przerwa), Wizards bez Watkinsa (dwustronny, bez znaczenia). Brak informacji o statusach gwiazd w pozostałych meczach.
Zgodnie ze skillem: SD podniesione (różnica 13, suma 19), pewność niska, **brak typów na rynki zawodnika**, brak własnej przewagi nad rynkiem. Model (`nba_model.py`) zasilono liniami DraftKings (spread i total z ESPN), więc spread i total wychodzą 50/50 z założenia: to uczciwe "brak edge". Zwycięzcę liczę z moneyline po usunięciu marży (ok. 4,3%).

| Mecz (godz. PL) | Linia (spread / total) | Gospodarz wygrywa | Fair gosp. | Gość wygrywa | Fair gość | Pewność |
|---|---|---|---|---|---|---|
| Hawks @ Magic (01:00) | ORL -3.5 / 235.5 | 57.2% | 1.75 | 42.8% | 2.34 | niska |
| Bucks @ Wizards (01:00) | WSH -4.5 / 239.5 | 61.6% | 1.62 | 38.4% | 2.61 | niska |
| Timberwolves @ Heat (01:30) | MIA -1.5 / 242.5 | 52.2% | 1.92 | 47.8% | 2.09 | brak typu |
| Hornets @ Nets (01:30) | BKN -1.5 / 218.5 | 54.3% | 1.84 | 45.7% | 2.19 | brak typu |
| Bulls @ Raptors (01:30) | TOR -9.5 / 236.5 | 77.7% | 1.29 | 22.3% | 4.48 | niska/średnia |
| Jazz @ Grizzlies (02:00) | MEM -1.5 / 239.5 | 52.2% | 1.92 | 47.8% | 2.09 | brak typu |
| Pacers @ Pelicans (02:00) | IND -3.5 / 239.5 | 41.7% | 2.40 | 58.3% (IND) | 1.72 | niska |
| Mavericks @ Rockets (02:30) | HOU -9.5 / 229.5 | 75.1% | 1.33 | 24.9% | 4.01 | niska/średnia |
| Warriors @ Lakers (04:00) | LAL -6.5 / 235.5 | 65.7% | 1.52 | 34.3% | 2.92 | niska |
| Suns @ Trail Blazers (04:00) | POR -2.5 / 231.5 | 56.3% | 1.77 | 43.7% | 2.29 | brak typu |
| Kings @ Clippers (04:30) | LAC -4.5 / 228.5 | 63.7% | 1.57 | 36.3% | 2.75 | niska |

Spread i total każdego meczu: 50% po obu stronach (fair ~2.00 przed marżą rynku); żadnego sygnału, który uzasadniałby przesunięcie. Kursy spreadu/totalu DraftKings: ok. -105/-115, czyli marża ~4%, więc bez własnej przewagi EV ujemne.

**Ryzyka:** niepotwierdzone statusy gwiazd (decyzje tuż przed meczem), pierwsze mecze sezonu (nowe rotacje, wysoka wariancja), przy spreadach ≥ 9.5 (Raptors, Rockets) blowout. Wygrana faworyta to nie pokrycie spreadu.

**Kandydaci na kupon z NBA (wejście do `bet-slip-builder`; kursy Betclic do pobrania, bez własnej przewagi nad rynkiem):**
| Mecz | Rynek | p | Fair | Pewność |
|---|---|---|---|---|
| Raptors - Bulls | Raptors wygrywają | 77.7% | 1.29 | niska/średnia |
| Rockets - Mavericks | Rockets wygrywają | 75.1% | 1.33 | niska/średnia |
| Lakers - Warriors | Lakers wygrywają | 65.7% | 1.52 | niska |
| Clippers - Kings | Clippers wygrywają | 63.7% | 1.57 | niska |
| Wizards - Bucks | Wizards wygrywają | 61.6% | 1.62 | niska |

Godzina sprawdzenia danych: 21.10 ok. 08:00 CEST; injury report i składy do sprawdzenia przed meczem.

## NHL, noc 21/22.10 (godz. 01:30 PL = 19:30 ET, śr. 21.10 USA)

Źródła: ESPN (statystyki sezonowe, oczekiwani bramkarze, kursy DraftKings). Początek sezonu (9-11 meczów na drużynę), próba mała. Bramkarze oznaczeni przez ESPN jako "Expected", **niepotwierdzeni** (potwierdzenie zwykle rano po skate): pewność najwyżej średnia. Skrypt `nhl_model.py`; rynki z dogrywką (moneyline, total) vs 60 minut podane osobno.

### Buffalo Sabres - Philadelphia Flyers
- Bilanse: BUF 4-3-2 (27 GF, 75 pkt łącznie w skali ESPN, SV% drużyny .861, 30. miejsce), PHI 2-6-3 (17 GF w 11 meczach = 1,55/mecz, 29. w lidze, SV% .904; 0-4-1 na wyjeździe).
- Bramkarze (oczekiwani): Luukkonen (BUF), Vladar (PHI).
- λ: BUF 3.35, PHI 2.50 (łącznie 5.85). Atak Flyers słaby, ale słaba skuteczność bramkarska Buffalo podbija PHI do 2.5.
- Rynek DraftKings: BUF -185 / PHI +154 (no-vig 62.2% / 37.8%), total 5.5 (Over 55.1% po usunięciu marży).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| Moneyline (z OT) BUF | 63.8% | 1.57 | średnia |
| Moneyline PHI | 36.2% | 2.77 | niska |
| 60' BUF / remis / PHI | 55.5% / 16.0% / 28.5% | 1.80 / 6.26 / 3.50 | średnia |
| Puck line BUF -1.5 | 38.7% | 2.58 | niska |
| Puck line PHI +1.5 | 61.3% | 1.63 | średnia |
| Puck line BUF +1.5 | 84.0% | 1.19 | średnia (kurs krótki) |
| Over 5.5 (z OT) | 53.0% | 1.89 | niska |
| Under 5.5 | 47.0% | 2.13 | niska |
| Over 6.5 / Under 6.5 | 39.9% / 60.1% | 2.51 / 1.66 | niska |

**Ryzyka:** niepotwierdzeni bramkarze, mała próba, gole w pustą bramkę zawyżają różnice, dogrywka (16%).

### Ottawa Senators - Florida Panthers
- Bilanse: OTT 6-3-0 (22 GF, SV% .910, 5. w lidze), FLA 5-2-2 (30 GF, SV% .888; 3-1-2 na wyjeździe).
- Bramkarze (oczekiwani): Ullmark (OTT), Schmid (FLA). Schmid to dla Florydy bramkarz poniżej średniej SV%, więc korekta lekko na korzyść Ottawy.
- λ: OTT 2.85, FLA 2.95 (łącznie 5.8).
- Rynek DraftKings: OTT -108 / FLA -112 (no-vig 49.6% / 50.4%), total 5.5 (Over 53.2%).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| Moneyline (z OT) FLA | 51.7% | 1.94 | niska (brak mocnego typu) |
| Moneyline OTT | 48.3% | 2.07 | niska |
| 60' OTT / remis / FLA | 39.9% / 17.0% / 43.1% | 2.51 / 5.90 / 2.32 | niska |
| Puck line FLA +1.5 | 75.2% | 1.33 | średnia |
| Puck line OTT +1.5 | 72.5% | 1.38 | średnia |
| Over 5.5 (z OT) | 52.2% | 1.92 | niska |
| Under 5.5 | 47.8% | 2.09 | niska |
| Over 6.5 / Under 6.5 | 39.3% / 60.7% | 2.55 / 1.65 | niska |

**Ryzyka:** mecz wyrównany, dwóch bramkarzy do potwierdzenia, drużyny różnią się skutecznością bramkarzy.

### Kandydaci na kupon z NHL (kursy Betclic do pobrania)
| Mecz | Rynek | p | Fair | Pewność | Zależy od |
|---|---|---|---|---|---|
| BUF - PHI | BUF moneyline | 63.8% | 1.57 | średnia | Luukkonen / Vladar |
| BUF - PHI | PHI +1.5 | 61.3% | 1.63 | średnia | bramkarze |
| FLA @ OTT | FLA +1.5 | 75.2% | 1.33 | średnia | Schmid, Ullmark |
| FLA @ OTT | OTT +1.5 | 72.5% | 1.38 | średnia | Schmid, Ullmark |

Godzina sprawdzenia: 21.10 ok. 08:30 CEST; bramkarze i skład do potwierdzenia przed meczem. To oszacowania probabilistyczne, nie gwarancje.
