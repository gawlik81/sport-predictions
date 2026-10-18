# Kupon z pewniaków (akumulator) - Betclic, 17.10.2026

Warunki użytkownika: pojedyncze typy z kursem > 1,1 i < 1,25, kurs kuponu > 2,0 i < 3,0.
Kursy: betclic.pl, odczyt 17.10.2026 ok. 12:30-13:00. Godziny: czas polski.

## Kupon

| # | Mecz | Typ | Kurs | p własne | Fair |
|---|------|-----|------|----------|------|
| 1 | Espanyol - Atlético (14:00) | Remis lub Atlético (podwójna szansa) | 1,18 | 79% | 1,27 |
| 2 | Strasbourg - PSG (17:15) | Remis lub PSG (podwójna szansa) | 1,12 | 84% | 1,19 |
| 3 | Bologna - Inter (18:00) | Remis lub Inter (podwójna szansa) | 1,15 | 83% | 1,20 |
| 4 | Betis - Barcelona (18:30) | Remis lub Barcelona (podwójna szansa) | 1,15 | 83% | 1,20 |
| 5 | Bayern - RB Leipzig (18:30) | Bayern wygra | 1,18 | 79% | 1,27 |

- Kurs łączny: 1,18 x 1,12 x 1,15 x 1,15 x 1,18 = 2,06
- Łączne p: ok. 36% (iloczyn, mecze niezależne); fair odds ok. 2,8
- EV: ok. -26%; Kelly: 0% bankrolla

## Źródła p

- Poisson (`football-analyst/scripts/poisson.py`, λ: Atlético 1,65 / Espanyol 0,95; PSG 1,9 / Strasbourg 1,0; Inter 1,9 / Bologna 0,85; Barcelona 2,5 / Betis 1,15; Bayern 3,2 / Leipzig 1,1) uśredniony z rynkiem po usunięciu marży z kursów 1X2 Betclic.
- Składy, kontuzje i sędziowie nieznani (brak newsów z 2026 w wyszukiwarce), pewność niska-średnia.

## Uwagi

- Każdy typ ma p ok. 79-84%, ale przy 5 nogach łączne p to ok. 36%. Żaden kupon z nóg 1,1-1,25 i kursem > 2,0 nie osiągnie p > 50% (wymagałoby nóg po ok. 87%, które mają kursy poniżej 1,15 po marży).
- Nogi mają ujemne EV (-5% do -7% każda), a w akumulatorze marże się mnożą.
- Odrzucone: Man City wygra (1,23, p 76%): remis i przegrana to dwa scenariusze porażki, a kurs jest przy górnej granicy; Over 2,5 Bayern (1,11) i Over 1,5 Atlético (1,20) zostają jako zamienniki.
- Atlético gra o 14:00: kupon trzeba zagrać wcześnie lub zamienić nogę 1.

Oszacowania probabilistyczne, nie gwarancje.
