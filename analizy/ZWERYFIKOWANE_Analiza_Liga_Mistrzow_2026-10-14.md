# Liga Mistrzów, 2. kolejka fazy ligowej, 14.10.2026 (czas polski)

**Zakres:** tylko piłka nożna (9 meczów LM). Tenis (Szanghaj, Wuhan), e-sport i MMA nie weszły: nie udało się zweryfikować dzisiejszych par/kart (źródła mieszały dane z 2025 i 2026, UFC zwraca bot-challenge).

**Terminarz (ESPN + UEFA, zgodne):** 18:45 Feyenoord - Como, LASK - Liverpool; 21:00 Shakhtar - AEK, Bodo/Glimt - Dortmund, Betis - Porto, Aston Villa - Fenerbahce, Man City - PSG, Roma - Real Madryt, Slovan Bratislava - Stuttgart.

## Metoda i jej granice (ważne)

- Kursy: Pinnacle (`pinnacle_matchup_markets`), 1X2 i linie goli, marża usunięta proporcjonalnie. To kursy zagraniczne, nie krajowego bukmachera.
- λ obu drużyn dopasowane do rynku (1X2 + główny total), potem `poisson.py`. **Oznacza to, że moje p jest praktycznie rynkowe, bez własnej przewagi.** Powód: research newsowy nie dał twardych informacji (brak potwierdzonych składów i sędziów, tylko ogólne "brak nowych absencji"), a reguła kalibracji zabrania schodzić pod/nad rynek bez konkretów.
- Rożne, kartki, faule, rynki zawodnika: **niewycenione**. Brak sędziów i drugiego źródła statystyk, więc zgodnie ze skillem nie ma typu.
- Doniesienia o Kamarze/McGinnie (Villa) wyglądają na stare i niespójne (Squawka stawia ich w XI), więc nie korygowałem λ.
- Venue w źródłach bywa błędne (np. Shakhtar - AEK "na Stamford Bridge" w jednym ze źródeł); nie wpływa na wycenę.

## Wyceny (p modelu = rynek bez marży)

| Mecz | λ dom/gość | 1 | X | 2 | O2.5 | O3.5 | BTTS | Pewność |
|---|---|---|---|---|---|---|---|---|
| Feyenoord - Como | 1.48 / 2.04 | 28.0% | 21.4% | 50.6% | 68.3% | 46.8% | 67.2% | niska-średnia |
| LASK - Liverpool | 0.98 / 2.54 | 12.5% | 16.4% | 71.1% | 68.3% | 46.8% | 57.5% | średnia |
| Shakhtar - AEK | 1.38 / 1.40 | 36.9% | 25.4% | 37.8% | 52.6% | 30.4% | 56.4% | brak mocnego typu |
| Bodo/Glimt - Dortmund | 1.68 / 2.04 | 32.2% | 21.2% | 46.5% | 71.8% | 51.0% | 70.8% | średnia |
| Betis - Porto | 1.68 / 1.26 | 47.3% | 24.0% | 28.7% | 56.3% | 33.9% | 58.3% | brak mocnego typu |
| Aston Villa - Fenerbahce | 2.06 / 1.10 | 59.5% | 20.9% | 19.6% | 61.2% | 38.9% | 58.2% | średnia |
| Man City - PSG | 1.88 / 1.52 | 46.3% | 22.3% | 31.4% | 66.0% | 44.2% | 66.2% | niska-średnia |
| Roma - Real Madryt | 1.44 / 1.98 | 28.0% | 21.8% | 50.2% | 66.4% | 44.6% | 65.8% | niska-średnia |
| Slovan - Stuttgart | 0.98 / 2.76 | 10.7% | 14.7% | 74.6% | 72.1% | 51.4% | 58.5% | średnia |

## Kursy Pinnacle użyte do EV (dziesiętne)

| Rynek | Kurs |
|---|---|
| Stuttgart wygra (Slovan) | 1.292 |
| Liverpool wygra (LASK) | 1.356 |
| Over 2.5 Slovan - Stuttgart | 1.334 |
| Over 2.5 Bodo - Dortmund | 1.348 |
| Over 2.5 LASK - Liverpool | 1.403 |
| Over 2.5 Feyenoord - Como | 1.405 |
| Over 2.5 Roma - Real | 1.444 |
| Over 2.5 City - PSG | 1.459 |
| Villa wygra | 1.633 |

BTTS: Pinnacle nie zwrócił ceny, więc kurs nieznany.

## Ryzyka ogólne

- Ryzyko faworytów (Liverpool, Stuttgart): remis i wygrana underdoga (LASK i Slovan łącznie ok. 29% i 25%); mecze po pierwszej kolejce, rotacja przed ligą w weekend (Dortmund, Betis mają ligę za 3 dni).
- Over 2.5 opiera się na wysokich liniach Pinnacle (3.25-3.5); Poisson przy tak wysokim λ może zawyżać Over/BTTS względem realnej wariancji.
- To oszacowania probabilistyczne, nie gwarancje.
