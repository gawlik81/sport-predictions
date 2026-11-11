# Real Madryt (K) - Paris FC (K), Liga Mistrzyń 26/27, 10.11.2026, 18:45 (Estadio Alfredo Di Stéfano)

Superbet event 15641500. Źródła: connector `superbet-mcp` (kursy, statystyki, H2H, sędzia); rezerwa: WebSearch (bez wyniku o tym meczu). Składy: **brak** (ani oficjalnych, ani przewidywanych). Nieobecni: **brak danych** (connector zwrócił błąd, web nic). Pierwszy raport z odczytu o 16:30 czasu polskiego.

**Typ:** Real wygra mecz | **p:** ok. 65% (zakres 62-70%) | **Fair odds:** 1,53 | **Pewność:** średnia (niższa przez brak składów i małą próbę sezonu)
Kurs Superbet 1,41 (p z rynku bez marży ok. 66%). **EV ok. -8%**, więc to nie jest value bet.

## Model
λ Real 2,3, λ Paris 1,05 (zakres 2,1/0,95 - 2,6/1,10), `poisson.py`. Mój pierwszy szacunek z samych średnich sezonu (1,95/1,0) dawał Real 59,5%, czyli ok. 6 pp poniżej rynku bez konkretnej informacji kadrowej; zgodnie z regułą "nie schodź pod rynek o >5 pp" przyjąłem λ zbliżone do rynku (rynek wycenia gola Realu na 93%, gola Paris na 63%).

| Rynek | p (zakres) | fair | kurs Superbet | EV | pewność |
|---|---|---|---|---|---|
| Real wygra | 65% (62-70) | 1,53 | 1,41 | -8% | średnia |
| Remis | 19% | 5,35 | 4,85 | | |
| Paris wygra | 16% | 6,28 | 5,65 | | |
| 1X | 84% | 1,19 | 1,10 | -8% | średnia |
| Powyżej 1,5 gola | 85% | 1,18 | 1,11 | | wysoka, ale fair ≤ 1,2 |
| Powyżej 2,5 gola | 65% (59-72) | 1,54 | 1,41 | -8% | średnia |
| Powyżej 3,5 gola | 43% (36-51) | 2,32 | 2,02 | -13% | niska |
| BTTS tak | 58% (54-62) | 1,71 | 1,60 | -6% | średnia |
| Real wygra i poniżej 5,5 gola | 56% (56-57) | 1,79 | 1,63 | -9% | średnia |
| Real wygra i powyżej 1,5 gola | 57% (54-63) | 1,74 | 1,56 | -11% | średnia |
| Real -1,5 (handicap) | 43% (40-48) | 2,34 | 2,00 | -15% | niska |
| Rożne (średnia ok. 10) | linia 9,5: ok. 50% | | O 1,95 / U 1,75 | | niska (brak danych o rożnych sezonu, składy nieznane) |
| Kartki | nie wyceniam | | linia 2,5: O 2,05 / U 1,63 | | niska (sędzia Emily Heaslip, brak jej statystyk w źródłach) |

Wszystkie typy mają EV < 0: przy λ zbliżonym do rynku strata to w praktyce marża Superbet (ok. 6-9%), a przy moim niższym λ jeszcze większa. **Nie ma tu mocnego typu z przewagą nad rynkiem.**

## Statystyki drużyn (connector, sezon LM 26/27; próba: Real 5 meczów, Paris 3)
- Real: 1,6 gola strzelonego, 1,0 straconego, 5,2 strzału celnego, rożne 5,8, żółte 1,2, faule 10,0, posiadanie 48%.
- Paris FC: 1,7 gola strzelonego, **2,7 straconego**, 3,7 strzału celnego, rożne 4,3, żółte 0,7, 1 czerwona w 3 meczach, posiadanie 41%.
- Forma Realu (wszystkie rozgrywki, od najnowszego): Bilbao 1:1 (wyjazd), Sevilla 3:1 (wyjazd, wygrana Realu), Bayern 2:2 (wyjazd), Tenerife 3:2 (dom), Espanyol 3:1 (dom), **Barcelona 0:7** (wyjazd, 04.10). Dużo straconych goli (16 w 6 meczach).
- Forma Paris FC: Montpellier 5:0, PSG 1:1, Hacken 1:1, Toulouse 4:0 (wyjazd), Lens 4:1, Arsenal 2:2. Mocna ofensywa i niezła forma, ale w LM traci dużo.

## H2H
Ostatnie mecze: luty 2026 (baraż o ćwierćfinał) Paris 2:3 Real, Real 2:0 Paris (z czerwoną kartką); listopad 2025 Real 1:1 Paris; 2023 Real 0:1 i 1:2 w Paryżu. Real wygrał oba ostatnie bezpośrednie mecze, ale Paris FC jest dziś wyraźnie mocniejszy niż w 2023 r., więc H2H waży nisko.

## Informacje medialne
Nie znalazłem zapowiedzi, składów ani komunikatów klubowych na ten mecz (WebSearch zwrócił tylko starsze mecze obu klubów). Nie wiem o absencjach; to główne źródło niepewności i powód, dla którego pewność to najwyżej "średnia". Składy pojawią się ok. 60-75 minut przed startem (po ok. 17:30).

## Ryzyka typu "Real wygra"
Remis (ok. 19%) i wygrana Paris (ok. 16%): Paris strzela w każdym meczu sezonu (1,7 gola) i jest w dobrej formie, a Real traci dużo (ostatnie 6 meczów: 16 goli, w tym 0:7). Brak składów.

## Rynek
1X2 1,41 / 4,85 / 5,65 (Superbet, marża ok. 9%), rynek wycenia Real na ok. 66%. Inne źródła kursów nie były sprawdzane (BettingPros bez klucza).

To oszacowania probabilistyczne, nie gwarancje.

## Kupon (Bet Builder, warunek: łączny kurs > 1,5 i < 2,5; stawka 5 zł)
Żaden kupon nie ma EV > 0. **Wariant awaryjny** (najwyższe p w kursie 1,5-2,5, pewność średnia): **Real wygra mecz + poniżej 5,5 gola**, kurs 1,63 (API), p ok. 56% (56-57%), fair 1,79, EV ok. -9%. Konkurent o zbliżonym p: 12 + poniżej 4,5 gola, kurs 1,51 (p 54-62%, EV -12%, kurs na granicy progu 1,5). Przewaga bukmachera jest po jego stronie. Kelly: 0% bankrolla (EV < 0); stawka 5 zł to świadomy zakład rozrywkowy.
