# Kupony 01.11.2026 (niedziela), wersja 2: poziomy 0-4, -1 i -2

Zastępuje `ZWERYFIKOWANE_Kupony_10_2026-11-01.md`. **Korekta wersji 1:** pominąłem w niej część rynków "BTTS nie" i "Under 2.5", które mają dodatnie EV (m.in. Como - Venezia BTTS nie, Racing - Real BTTS nie, Frosinone Under 2.5, Marseille BTTS nie, Athletic Under 2.5). Wersja 2 liczy pełną pulę 105 nóg ze wszystkich pobranych kursów Betclic (skrypt w scratchpadzie sesji, kupony sprawdzone wzorem ze `slip.py`). Wniosek bazowy się nie zmienia: poziom 0 nadal 0 kuponów.

## 1. Okres i źródło kursów
- 01.11.2026, godziny polskie. Kursy Betclic.pl pobrane ok. 11:50-12:45, **bez weryfikacji na gg397.bet**. Kursy mogą się zmienić do startu.
- Analizy: `Analiza_pilka_cz1|cz2|cz3`, `Analiza_tenis_esport`, `Analiza_NBA`, `Analiza_NHL` z 01.11.2026. Terminarz: `Terminarz_2026-11-01.md` (32 wydarzenia).
- Brak kursów Betclic (nogi odpadły): Dota 2, total i puck line NHL, total 3.5, rożne, kartki, rynki zawodnika.

## 2. Zestawienie wszystkich kuponów

### A. Ścieżka poziomów 0-4 (kupon wielonogowy, stawka 0%)
Zasady: jeden mecz tylko w jednym kuponie, brak powtórzonych nóg, fair każdej nogi > 1,15, kurs zestawu 1,5-2,5, 2-3 nogi. Poziom 4 = poziom 3 (p kuponu > 45%, nogi pojedyncze p ≥ 55%) + kurs > 1,2 wystarczy dla jednej nogi.

| # | Poziom | Nogi (godz.) | Kursy | Łączne p | Kurs | EV | Stawka |
|---|---|---|---|---|---|---|---|
| 1 | 1 | Lecce - Genoa Under 2.5 (18:00) + Boston +4.5 hcp, NBA (21:30) | 1,57 / 1,22 | 51,5% | 1,92 | -1,3% | 0% |
| 2 | 2 | Como wygra (12:30) + Lazio - Cagliari Over 1.5 (15:00) | 1,28 / 1,25 | 56,4% | 1,60 | -9,8% | 0% |
| 3 | 2 | Real Madryt wygra (16:15) + Athletic - Real Sociedad Over 1.5 (21:00) | 1,23 / 1,24 | 55,6% | 1,53 | -15,2% | 0% |
| 4 | 2 | Getafe - Sevilla X2 (14:00) + Paris FC - Monaco Over 1.5 (17:15) | 1,33 / 1,22 | 54,2% | 1,62 | -12,0% | 0% |
| 5 | 4 | Elche - Valencia Over 1.5 (18:30) + Lehecka +1.5 seta, Basel (15:30) | 1,28 / 1,19 | 58,5% | 1,52 | -10,9% | 0% |
| 6 | 4 | Lyon 1X (17:15) + Liverpool 1X (17:30) | 1,11 / 1,50 | 55,8% | 1,67 | -7,1% | 0% |
| 7 | 4 | Alcaraz wygra, Vienna (14:10) + Carolina wygra ML, NHL (19:00) | 1,16 / 1,31 | 54,4% | 1,52 | -17,3% | 0% |
| 8 | 4 | Frosinone - Torino Over 1.5 (15:00) + Marseille - Toulouse Over 2.5 (20:45) | 1,10 / 1,48 | 51,8% | 1,63 | -15,7% | 0% |

Poziom 0: 0 kuponów. Poziom 1: 1. Poziom 2: 3 dodatkowe. Poziom 4: 4 dodatkowe (z puli zostały nogi, ale mecze są już zajęte, więc do 10 nie dobijam). Wszystkie kupony mają EV ujemne: rynek wycenia faworytów krócej niż fair. Kupon 1 jest najbliżej zera; p handicapu Boston +4.5 (81%) jest moim wyliczeniem z modelu NBA, nie z analizy.

### B. Poziom -1 (tryb EV): 5 kuponów po 2 nogi, wszystkie nogi EV > 0
Każda noga ma p wyższe od rynku po devigu, więc są oznaczone **"przewaga niepotwierdzona"** (modele analityków systematycznie dają mniej goli niż Betclic). Stawka Kelly 1/4 liczona z p ściągniętym do rynku + 5 pp. Łączne p niskie, wariancja wysoka.

| # | Nogi (godz.) | Kursy | p (model) | Kurs | EV (model) | EV po ściągnięciu p | Stawka |
|---|---|---|---|---|---|---|---|
| -1/1 | Como - Venezia BTTS nie (12:30) + Racing - Real BTTS nie (16:15) | 2,12 / 2,42 | 25,5% | 5,13 | +30,7% | +9,7% | 0,6% |
| -1/2 | Frosinone - Torino Under 2.5 (15:00) + Marseille - Toulouse BTTS nie (20:45) | 2,97 / 2,55 | 15,5% | 7,57 | +17,7% | +14,6% | 0,6% |
| -1/3 | Juventus - Napoli BTTS nie (20:45) + Getafe - Sevilla, Sevilla wygra (14:00) | 2,00 / 2,35 | 23,7% | 4,70 | +11,4% | +8,1% | 0,55% |
| -1/4 | Paris FC - Monaco BTTS nie (17:15) + Liverpool wygra (17:30) | 2,22 / 2,73 | 17,8% | 6,06 | +8,0% | +8,0% | 0,4% |
| -1/5 | Lecce - Genoa BTTS nie (18:00) + Elche - Valencia BTTS nie (18:30) | 1,79 / 2,05 | 28,1% | 3,67 | +3,0% | +3,0% | 0,3% |

Pozostała noga: Athletic - Real Sociedad Under 2.5 (@2,00, p 50,6%, EV +1,2%), bez pary.

### C. Poziom -2 (pojedyncze, EV > 0): 10 kuponów, po najlepszej nodze z meczu
Stawka Kelly 1/4 z p ściągniętym do rynku + 5 pp.

| # | Mecz, rynek (godz.) | p | Kurs | EV | p po ściągnięciu | EV po ściągnięciu | Stawka |
|---|---|---|---|---|---|---|---|
| -2/1 | Como - Venezia BTTS nie (12:30) | 54,2% | 2,12 | +14,9% | 49,1% | +4,0% | 0,9% |
| -2/2 | Racing - Real BTTS nie (16:15) | 47,0% | 2,42 | +13,7% | 43,6% | +5,5% | 0,95% |
| -2/3 | Frosinone - Torino Under 2.5 (15:00) | 37,0% | 2,97 | +9,9% | 36,4% | +8,1% | 1,0% |
| -2/4 | Marseille - Toulouse BTTS nie (20:45) | 42,0% | 2,55 | +7,1% | 41,6% | +6,0% | 1,0% |
| -2/5 | Juventus - Napoli BTTS nie (20:45) | 53,4% | 2,00 | +6,8% | 51,8% | +3,6% | 0,9% |
| -2/6 | Getafe - Sevilla, Sevilla wygra (14:00) | 44,4% | 2,35 | +4,3% | 44,4% | +4,3% | 0,8% |
| -2/7 | Paris FC - Monaco BTTS nie (17:15) | 47,0% | 2,22 | +4,3% | 47,0% | +4,3% | 0,9% |
| -2/8 | Liverpool wygra (17:30) | 37,9% | 2,73 | +3,5% | 37,9% | +3,5% | 0,5% |
| -2/9 | Lecce - Genoa BTTS nie (18:00) | 56,8% | 1,79 | +1,7% | 56,8% | +1,7% | 0,5% |
| -2/10 | Elche - Valencia BTTS nie (18:30) | 49,4% | 2,05 | +1,3% | 49,4% | +1,3% | 0,3% |

## 3. Uwagi
- **Wspólny wzorzec:** niemal wszystkie dodatnie EV to rynki "mniej goli" (BTTS nie, Under 2.5), gdzie model jest o 4-8 pp bardziej "under" niż rynek, bez twardej informacji. Jeśli ten błąd jest systematyczny (analizy opierały się na mało świeżych składach), całe ścieżki -1 i -2 mogą mieć EV w rzeczywistości ujemne. Weryfikacja 26-28.10: nogi z niepotwierdzoną przewagą trafiły 53% przy modelowym p ok. 65%.
- Nogi z jednego rynku (BTTS nie) są skorelowane stylem, nawet w różnych meczach: seria 0-0/1-0 lub wysokie wyniki uderzy w kilka kuponów naraz.
- Stawki dla poziomów 0-4 to 0%, bo EV ≤ 0. Stawki -1/-2 to sugestia wielkości, nie porada finansowa.
- Como - Venezia startuje o 12:30; Getafe - Sevilla o 14:00, Alcaraz o 14:10. Kursy i składy sprawdź tuż przed meczem; NHL: bramkarze niepotwierdzeni.
- Założenie niezależności meczów; to oszacowania probabilistyczne, nie gwarancje.
