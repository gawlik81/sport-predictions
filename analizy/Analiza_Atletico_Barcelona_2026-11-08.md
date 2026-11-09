# Atletico Madryt - Barcelona (La Liga, 08.11.2026, 21:00)

Analiza skrócona (start za ok. 20 min od odczytu danych). Źródła: connector superbet-mcp (składy oficjalne, nieobecni, statystyki, H2H, kursy); brak researchu w sieci (newsy, konferencje), brak xG spoza serwisu.

**Typ:** Barcelona wygra mecz | **p:** 56% (zakres 47-64%) | **Fair odds:** 1.79 | **Kurs Superbet (API):** 1.90 | **EV:** ok. +6% (zakres od -10% do +21%) | **Pewność:** średnia

## Model
λ Atletico 1.35, λ Barcelona 2.15 (poisson.py). Sędzia: Javier Alberola Rojas.

| Rynek | p (λ 1.35/2.15) | fair | kurs Superbet | EV |
|---|---|---|---|---|
| 1 Atletico | 23.6% | 4.23 | 3.45 | -18% |
| X | 20.6% | 4.85 | 4.25 | -12% |
| 2 Barcelona | 55.7% | 1.79 | 1.90 | +6% |
| Over 1.5 | 86.4% | 1.16 | 1.09 | -6% |
| Over 2.5 | 67.9% | 1.47 | 1.34 | -9% |
| BTTS tak | 65.4% | 1.53 | 1.36 | -11% |
| Barcelona & powyżej 1.5 gola | 49% | 2.04 | 2.07 | +1% |
| Barcelona & BTTS | 33% | 3.05 | 2.80 | -8% |

Czułość (λ Atletico/Barcelona): 1.5/1.9 -> Barcelona 47%; 1.2/2.4 -> 64%.

## Dane
- Statystyki sezonu (Superbet): Atletico 2.0 gola strzelone, 0.7 stracone, xG 1.6; Barcelona 4.2 gola strzelone, 1.1 stracone, xG 3.5 (średnie Barcelony wyglądają na zawyżone po meczach z 6:1 i 5:2).
- Forma Atletico: 0:2 Bayern, 2:0 Levante, 1:0 Deportivo, 1:1 Stuttgart, 1:0 Espanyol. Forma Barcelony: 3:0 Aston Villa, 6:1 Alaves, 1:2 Real, 2:4 PSG, 5:2 Betis.
- H2H (ostatnie 5, 2026): Atletico 4:0, Barcelona 3:0, Atletico 1:2, 0:2 (Atletico wygrało), 1:2. Barcelona 3 z 5.
- Nieobecni: Atletico - Romero; Barcelona - Bardghji, Xavi Espart, Rodri, Kounde, D. Olmo (powody nieznane, źródło "manual").
- Składy oficjalne: Atletico bez Sorlotha, Lookmana i Davida w XI (Alvarez, Lee, Baena z przodu); Barcelona z Yamalem, Raphinhą i Gordonem, bez Kounde (Cubarsi, Cancelo w obronie).

## Ryzyka
Remis (ok. 21%) i wygrana Atletico (ok. 24%); wyjazd na Metropolitano, Atletico po meczu z Bayernem. Rozbieżność z rynkiem bez marży (Barcelona ok. 50%) wynosi +5-6 pp: rynek może wiedzieć coś o składzie lub stanie zdrowia, którego nie widać w danych.
