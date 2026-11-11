# Atletico Madryt (K) - FC Badalona (K) (Primera Division Kobiet 26/27, 09.11.2026, 19:00 PL, Superbet 15627207)

Analiza skrócona (start za ok. 25 min). Źródła: connector superbet (składy oficjalne, sędzia, średnie sezonu, H2H, forma, kursy) i własny model Poissona (`poisson.py`). Nieobecni: connector zwrócił "Brak danych" (rezerwa nie użyta). Sędzia: Paola Cebollada Lopez (brak jej statystyk).

## Dane
- Średnie sezonu (gosp. / goście): gole 2.1 / 1.0, stracone 1.3 / 1.9, strzały celne 6.6 / 3.9, rożne 4.6 / 4.7, kartki 1.1 / 1.3. Brak xG.
- Forma Atletico (6): R 1-1 Granada, W 4-0 Valencia, W 4-0 Madryt CCF, W 2-1 Deportivo, P 2-3 Athletic, W 1-0 Logrono (4 W, 1 R, 1 P).
- Forma Badalona (6): P 0-4 Barcelona, P 0-1 Logrono, P 0-4 Tenerife, R 3-3 Sevilla, P 0-1 Granada, R 0-0 Real Sociedad (0 W, 2 R, 4 P, 3 mecze bez gola).
- H2H: Atletico 4-2 w Badalonie (04.2026), 2-0, 5-0, 1-1, 1-0, 3-1; bilans od 2012: 10 W, 2 R, 1 P Atletico.
- Składy oficjalne, Hermoso na ławce u Atletico.

## Model i rynek
- Rynek bez marży: 1 / X / 2 = 75 / 15 / 10%. Model (λ 2.0 / 1.0): 60.6 / 21.2 / 18.3%, czyli 14 pp pod rynkiem. Rozbieżność > 10 pp bez konkretnej informacji, więc liczy się rynek (reguła skilla).
- Under 3.5 @1.60: model 63-65%, rynek bez marży ok. 57%. Over 2.5: rynek ok. 63%.
- Wszystkie kombinacje (12/1X z golami, handicap, gole drużyny) mają EV < 0 przy λ 1.9-2.2 / 0.9-1.1.
- Jedyny typ z EV bliskim zera (Under 3.5 @1.60, EV od 0 do +3.6% wg modelu) opiera się na przewadze 7-8 pp nad rynkiem bez konkretnej informacji, więc pewność niska.

## Wniosek
Brak kuponu: pewność niska (duża rozbieżność z rynkiem bez konkretów, brak danych o nieobecnych, nieznany sędzia), EV < 0 dla pozostałych kombinacji. Typ wynikowy Atletico @1.20 poniżej progu kursu.

Oszacowania probabilistyczne, nie gwarancje.
