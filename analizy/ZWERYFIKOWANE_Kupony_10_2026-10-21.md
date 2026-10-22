# Kupony 10 na 21.10.2026 (dziś + noc 21/22.10), czas polski

## 1. Okres, źródła kursów, godzina pobrania
- Okres: środa 21.10.2026 oraz noc 21/22.10 (NBA, NHL). Pobranie kursów: 21.10 ok. 07:45-08:15 CEST.
- Kursy: **Betclic.pl** (piłka LM: 1X2, DC, gole, BTTS; NBA: zwycięzca; tenis ATP/WTA: zwycięzca). Betclic nie ma hokeja, więc nogi NHL mają kurs z **gg397.bet** (oznaczone w tabeli). Pozostałe nogi nie zostały potwierdzone na gg397.bet, więc rozbieżności > 0,10 nie są sprawdzone.
- Prawdopodobieństwa: piłka = λ z kursów Pinnacle (bez marży) i `poisson.py`, korekta tylko Aston Villa (rotacja); NBA = linie DraftKings bez marży (brak injury reportu); NHL = `nhl_model.py` (bramkarze niepotwierdzeni); **tenis = rynek Betclic po usunięciu marży, z limitem 75%** (brak statystyk serwisu/returnu i kontuzji), czyli bez niezależnej analizy.

## 2. Skrót terminarza
| Sport | Wydarzeń | Uwagi |
|---|---|---|
| Piłka | 9 | Liga Mistrzów, 3. kolejka (18:45 i 21:00); inne ligi: brak potwierdzenia |
| NBA | 11 | 01:00-04:30 (22.10); Kings-Clippers bez kursów na Betclic |
| NHL | 2 | 01:30 (22.10) |
| Tenis | 20 singli ATP/WTA | w kuponach tylko mecze od ok. 09:00 |
| MMA | 0 | brak gali UFC/KSW w oknie |
| E-sport | pominięty | ok. 50 meczów tier-2/3, brak tier-1 w oknie i brak danych |

## 3. Pula nóg (fair > 1.15, p > 50%); NBA i NHL osobno
| Mecz | Rynek | p | Kurs | Źródło kursu | Fair | EV | Pewność |
|---|---|---|---|---|---|---|---|
| Como - Man United | 12 (bez remisu) | 77,1% | 1,26 | Betclic | 1,30 | -2,9% | średnia/niska |
| Club Brugge - Lens | 12 | 78,7% | 1,23 | Betclic | 1,27 | -3,2% | średnia/niska |
| Real - Leipzig | Real wygrywa | 78,1% | 1,21 | Betclic | 1,28 | -5,5% | średnia |
| Inter - Shakhtar | Over 2.5 | 74,7% | 1,28 | Betclic | 1,34 | -4,4% | średnia |
| Rublev - Mannarino (Almaty) | Rublev | 74,8% | 1,23 | Betclic | 1,34 | -8,0% | niska (p = rynek) |
| Raptors - Bulls (NBA) | Raptors ML | 77,7% | 1,20 | Betclic | 1,29 | -6,8% | niska |
| Rockets - Mavericks (NBA) | Rockets ML | 75,1% | 1,24 | Betclic | 1,33 | -6,9% | niska |
| Lakers - Warriors (NBA) | Lakers ML | 65,7% | 1,39 | Betclic | 1,52 | -8,7% | niska |
| Ottawa - Florida (NHL) | **Ottawa +1,5 (z OT)** | 72,5% | 1,45 | **gg397.bet** | 1,38 | **+5,1%** | średnia, przewaga niepotwierdzona |
| Buffalo - Philadelphia (NHL) | Philadelphia +1,5 (z OT) | 61,3% | 1,55 | **gg397.bet** | 1,63 | -5,0% | średnia |

NHL: jedyna noga z dodatnim EV to Ottawa +1,5 po cenie gg397.bet. Ten EV wynika z ceny gg397 (1,45 wobec ok. 1,37 wyliczonego z DraftKings), a nie z mojego p ponad rynkiem. Dodatkowo gg397 ma w tym meczu 1X2 (Florida 1,76, Ottawa 3,16) sprzeczne z DraftKings (mecz wyrównany), więc kurs trzeba potwierdzić przed postawieniem.

## 4. Kupony

### Zestawienie
| Kupon | Nogi | Kurs | Łączne p | EV | Poziom luzowania | Co złamano | Stawka |
|---|---|---|---|---|---|---|---|
| **1 (TOP 3)** | Como - MU 12 + **Ottawa +1,5 (NHL)** | 1,83 | 55,9% | **+2,1%** | **0 (bazowy)** | nic; przewaga niepotwierdzona, kurs gg397 | 0,6% (1/4 Kelly) tylko po potwierdzeniu kursu 1,45, inaczej 0% |
| 2 | Brugge - Lens 12 + **Philadelphia +1,5 (NHL)** | 1,91 | 48,2% | -8,0% | **3** | EV < 0; p zestawu < 50% (noga p ≥ 55% zachowana) | 0% |
| **3 (TOP 3)** | Lille - Galatasaray 12 + **Rockets ML (NBA)** | 1,57 | 57,2% | -10,0% | **2** | EV < 0 | 0% |
| 4 | Inter - Shakhtar Over 2.5 + Rublev | 1,57 | 55,9% | -12,0% | **2** | EV < 0 | 0% |
| **5 (TOP 3)** | Bayern - Arsenal 12 + **Raptors ML (NBA)** | 1,51 | 59,9% | -9,4% | **2** | EV < 0 | 0% |
| 6 | Sporting - LASK Over 2.5 + Musetti | 1,59 | 54,4% | -13,7% | **2** | EV < 0 | 0% |
| 7 | Struff + Paul (tenis) | 1,56 | 53,8% | -16,0% | **2** | EV < 0 | 0% |
| 8 | Real wygrywa + **Lakers ML (NBA)** | 1,68 | 51,3% | -13,7% | **2** | EV < 0 | 0% |
| 9 | Aston Villa Over 2.5 + Betis - Feyenoord 12 | 1,52 | 56,9% | -13,2% | **4** | EV < 0; tylko 1 noga > 1,20 (Betis 1,20) | 0% |
| 10 | Bayern - Arsenal Over 1.5 + Cirstea | 1,58 | 55,4% | -12,7% | **4 + 6** | EV < 0; tylko 1 noga > 1,20; Bayern - Arsenal w kuponach 5 i 10 (różne rodziny: wynik / gole) | 0% |

Poziom 5 (kurs zestawu > 1,4) nie był potrzebny. Poziomy 1-6 stosowane po kolei i tylko do najniższego, który dawał 10 zestawów.

### Szczegóły kuponów
**Kupon 1 (poziom 0)** | Łączne p 55,9% | Fair 1,79 | Kurs 1,83 | EV +2,1%
| Mecz | Typ | Godz. | p | Kurs | Fair | Źródło |
|---|---|---|---|---|---|---|
| Como - Man United | 12 (bez remisu) | 18:45 | 77,1% | 1,26 | 1,30 | Betclic |
| Ottawa - Florida (NHL) | Ottawa +1,5 puck line | 01:30 (22.10; USA śr. 21.10 19:30 ET) | 72,5% | 1,45 | 1,38 | gg397.bet |
Ryzyko: bramkarze niepotwierdzeni (Ullmark / Schmid), kurs gg397 do potwierdzenia, remis w meczu Como.

**Kupon 2 (poziom 3)** | p 48,2% | Fair 2,07 | Kurs 1,91 | EV -8,0%
Brugge - Lens 12 (21:00, 78,7%, 1,23 Betclic) + Philadelphia +1,5 (NHL, 01:30 22.10, 61,3%, 1,55 gg397.bet). Ryzyko: remis Brugge - Lens, Buffalo wygrywa 2+ golami (bramkarze niepotwierdzeni).

**Kupon 3 (poziom 2)** | p 57,2% | Fair 1,75 | Kurs 1,57 | EV -10,0%
Lille - Galatasaray 12 (18:45, 76,1%, 1,27) + Rockets wygrywają z Mavericks (NBA, 02:30 22.10; USA śr. 21.10 20:30 ET; 75,1%, 1,24). Ryzyko: remis w Lille, niepotwierdzony injury report NBA, spread -9,5 (blowout).

**Kupon 4 (poziom 2)** | p 55,9% | Fair 1,79 | Kurs 1,57 | EV -12,0%
Inter - Shakhtar Over 2.5 (21:00, 74,7%, 1,28) + Rublev wygrywa z Mannarino (Almaty, 10:50, 74,8%, 1,23). Ryzyko: tenis bez statystyk (p = rynek).

**Kupon 5 (poziom 2)** | p 59,9% | Fair 1,67 | Kurs 1,51 | EV -9,4%
Bayern - Arsenal 12 (21:00, 77,1%, 1,26) + Raptors wygrywają z Bulls (NBA, 01:30 22.10; USA śr. 21.10 19:30 ET; 77,7%, 1,20). Ryzyko: remis na Allianz, injury report NBA, spread -9,5.

**Kupon 6 (poziom 2)** | p 54,4% | Fair 1,84 | Kurs 1,59 | EV -13,7%
Sporting - LASK Over 2.5 (21:00, 73,4%, 1,28) + Musetti wygrywa z Kouamé (Lyon, 19:00, 74,1%, 1,24). Ryzyko: tenis p = rynek.

**Kupon 7 (poziom 2)** | p 53,8% | Fair 1,86 | Kurs 1,56 | EV -16,0%
Struff wygrywa z Onclin (Bruksela, 19:10, 74,5%, 1,23) + Paul wygrywa z Bonzi (Lyon, 20:10, 72,2%, 1,27). Ryzyko: dwa mecze z p = rynek, brak sprawdzonych kontuzji.

**Kupon 8 (poziom 2)** | p 51,3% | Fair 1,95 | Kurs 1,68 | EV -13,7%
Real wygrywa z Leipzig (21:00, 78,1%, 1,21) + Lakers wygrywają z Warriors (NBA, 04:00 22.10; USA śr. 21.10 22:00 ET; 65,7%, 1,39). Ryzyko: noga NBA niska pewność, brak injury reportu.

**Kupon 9 (poziom 4)** | p 56,9% | Fair 1,76 | Kurs 1,52 | EV -13,2%
Aston Villa - Viking Over 2.5 (21:00, 70,9%, 1,27) + Betis - Feyenoord 12 (21:00, 80,3%, 1,20). Ryzyko: rotacja Villi przed City.

**Kupon 10 (poziom 4 + 6)** | p 55,4% | Fair 1,80 | Kurs 1,58 | EV -12,7%
Bayern - Arsenal Over 1.5 (21:00, 83,1%, 1,15) + Cirstea wygrywa z Bejlek (Ningbo, 09:20, 66,7%, 1,37). **Mecz tenisowy startuje za ok. godzinę.** Ryzyko: noga Over 1.5 z kursem 1,15 (fair 1,20, graniczna).

### Kupon 11 (dodatkowy, tylko NBA, na prośbę, kurs > 1,5)
Kursy Betclic z stron meczów (21.10 ok. 08:15). p handicapów = rozkład normalny (SD 13) wokół linii DraftKings, bez injury reportu, pewność niska.
| Mecz | Typ | Godz. (22.10) | p | Kurs | Fair | EV |
|---|---|---|---|---|---|---|
| Brooklyn - Charlotte | Hornets +7,5 | 01:30 | 67,8% | 1,43 | 1,48 | -3,1% |
| Memphis - Utah | Jazz +6,5 | 02:00 | 65,0% | 1,44 | 1,54 | -6,4% |
Łączne p 44,1% | Fair 2,27 | Kurs 2,06 | EV -9,3% | Stawka 0%. Poziom: 3+ (EV < 0, p zestawu 44,1% < 45%). Nogi nie powtarzają się z kuponów 1-10.
Alternatywa z wyższym p (powtarza nogi z kuponów 5 i 8, więc łamie regułę "bez powtórzeń"): Raptors ML 1,20 + Lakers ML 1,39, kurs 1,67, p 51,0%, EV -14,9%.
Najlepszy pojedynczy zakład NBA: Wizards ML 1,57 (p 61,6%, EV -3,3%).

## 5. Ostrzeżenia
- **Tylko kupon 1 ma dodatni EV, i to dzięki cenie gg397.bet na NHL, której nie potwierdziłem na Betclic.** Pozostałe 9 ma ujemne EV (-8% do -16%) i stawkę 0%: własne p pochodzi z rynku, a marża Betclic wynosi 3-10%.
- NHL: gg397.bet pokazuje dla Buffalo - Philadelphia 1X2 2,30 / 4,39 / 2,24 oraz Florida - Ottawa 1,76 / 4,49 / 3,16, czyli niespójnie z DraftKings (Buffalo -185). 1X2 z gg397 nie jest użyty; użyłem tylko puck line +1,5, ale jego wiarygodność jest niższa. Bramkarze startowi niepotwierdzeni.
- Tenis: bez statystyk serwisu/returnu i bez potwierdzonych kontuzji; p to rynek. Betclic podaje inne godziny niż Flashscore dla części meczów.
- NBA: początek sezonu, brak injury reportu; statusy gwiazd do sprawdzenia przed meczem.
- Rożne, kartki, faule i rynki zawodnika nie zostały wycenione (brak sędziów i składów).
- Założenie niezależności meczów; kursy mogą się zmienić do startu; składy do potwierdzenia ok. 1 h przed meczem.
- To oszacowania probabilistyczne, nie gwarancje. Sugerowana stawka nie jest poradą finansową.
