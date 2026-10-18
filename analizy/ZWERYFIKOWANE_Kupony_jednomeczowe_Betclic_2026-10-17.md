# Kupony jednomeczowe (MyCombi) - Betclic, 17.10.2026

Warunki użytkownika: 5 kuponów, każdy tylko z typami z jednego wydarzenia, kurs kuponu > 1,5 i < 2,5, własne p > 50%.
Kursy: betclic.pl, odczyt 17.10.2026 ok. 12:30 (czas polski). Godziny: czas polski.

## Werdykt

Żaden kupon nie ma EV > 0. Przy marży Betclic na MyCombi i kursach zbliżonych do rynku wszystkie typy spełniające p > 50% i kurs 1,5-2,5 mają EV od -9% do -14%. Przy EV < 0 ułamek Kelly'ego wynosi 0% bankrolla. Wszystkie pięć kuponów spełnia warunki użytkownika (kurs 1,5-2,5, p > 50%). Pierwotny kupon 5 (City wygra + Over 2,5, kurs 1,48) był poniżej progu i został zastąpiony.

## Dane wejściowe (filary)

- Tabele ESPN 17.10 (mecze, gole strzelone-stracone): Man City 6M, 16-5; Ipswich 6M, 9-12; Barcelona 8M, 34-7; Betis 8M, 14-9; Atlético 8M, 18-8; Espanyol 8M, 11-11.
- Man City: 6 wygranych w 6 meczach, Foden zawieszony (Khel Now, 15.10.2026). Haaland: brak potwierdzenia statusu, więc żaden kupon nie opiera się na nim.
- Barcelona, Betis, Atlético, Espanyol: wyszukiwarka nie zwróciła przedmeczowych newsów z 2026 (składy, kontuzje, sędzia). Pewność wszystkich typów: niska-średnia, składy niepotwierdzone.
- Model: Poisson (`football-analyst/scripts/poisson.py`) z λ: City 2,7 / Ipswich 0,8; Barcelona 2,5 / Betis 1,15; Atlético 1,65 / Espanyol 0,95. Prawdopodobieństwa łączne liczone z siatki wyników.

## Kupony

| # | Mecz | Typ (MyCombi) | Kurs | p własne | Fair | EV | Kelly | Pewność |
|---|------|---------------|------|----------|------|----|-------|---------|
| 1 | Betis - Barcelona (18:30) | Barcelona wygra + Powyżej 1,5 gola Barcelony | 1,51 | 60% | 1,66 | -9% | 0% | średnia |
| 2 | Espanyol - Atlético (14:00) | Atlético wygra | 1,63 | 55% | 1,82 | -10% | 0% | niska |
| 3 | Man City - Ipswich (16:00) | Powyżej 2,5 gola Man City | 1,69 | 52% | 1,92 | -12% | 0% | średnia |
| 4 | Bologna - Inter (18:00) | Powyżej 1,5 gola Interu | 1,52 | 58% | 1,72 | -12% | 0% | średnia |
| 5 | Roma - Genoa (20:45) | Roma wygra | 1,57 | 58% | 1,72 | -9% | 0% | niska |

Uwagi:
- Każdy kupon dotyczy innego meczu (Barcelona, Atlético, Man City, Inter, Roma).
- p w kuponach 2 i 3 to średnia modelu i rynku po usunięciu marży (model 53,8% / 50,6%, rynek ok. 57% / 55%).
- Kupon 4: λ Inter 1,9 / Bologna 0,85, model 56,6%, rynek po usunięciu marży ok. 61%. Kurs z Betclic 17.10 ok. 13:00.
- Kupon 5: λ Roma 1,8 / Genoa 0,9, model 58,6%, rynek ok. 59,5%. Kurs 1,57 z listy popularnych na stronie głównej Betclic (strony meczu Roma - Genoa nie otwierałem). Składy i sędzia nieznane.
- Zastąpione kupony: Barcelona wygra + Over 2,5 (1,64) i Man City wygra 1. połowę (1,56) były z meczów już użytych w kuponach 1-3.

## Odrzucone mecze i rynki

- Bayern - Leipzig: Bayern wygra + BTTS (1,72) ma p 46%; kupony z p > 50% mają kurs poniżej 1,5 (np. wygrana + Over 2,5 = 1,26).
- Strasbourg - PSG: PSG wygra + Over 1,5 (1,47) ma p 48%; wygrana PSG samodzielnie 1,38 jest poniżej progu kursu.
- Atlético: Under 2,5 (2,17) i BTTS Nie (2,10) wychodzą na plus (EV +12% i +6%) tylko dlatego, że λ modelu (łącznie 2,6) jest niższa niż implikowana przez rynek (ok. 2,95); brak konkretnej informacji, więc nie rekomenduję (zasada: nie schodź pod rynek bez konkretów).
- Typy ze strzelcem (Haaland, Kane, Raphinha, Torres): brak potwierdzonych składów.

## Jak zrelaksować warunki

1. Zejść z p > 50% na rynki z EV > 0 wymaga własnej przewagi informacyjnej; po potwierdzeniu składów (ok. godzinę przed meczem) warto przeliczyć Bayern i PSG.
2. Dodać mecze (Liverpool - Brentford, Lille - Brest, Everton - Chelsea), których kursów Betclic nie pobrano.

Oszacowania probabilistyczne, nie gwarancje.
