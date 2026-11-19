# Vissel Kobe - Machida Zelvia (Puchar J. League, 11.11.2026, 11:00 czasu PL)

Event Superbet 15721391. Analiza szybka (start za ok. 35 min), bez wariantów kadrowych. Źródła: connector superbet (kursy, składy oficjalne, H2H, forma, sędzia); rezerwa nie była używana. Brak danych w connectorze: nieobecni (błąd "Brak danych"), średnie przedmeczowe gospodarzy (puste), xG.

## Dane
- **Składy oficjalne** (connector). Kobe 4-3-3 (Skibbe): Maekawa; Iino, Iwanami, Thuler, Nagato; Watanabe, Kuwasaki, Goke; Kawabata, Komatsu, Jean Patric. Na ławce Osako, Muto, Erik, Sasaki, Ideguchi, Sakai, czyli wyraźna rotacja w ataku. Machida 3-4-2-1 (Kuroda): Tani; Mochizuki, Kim Min-Tae, Dresevic; Nakamura, Mae, Shimoda, Akimoto; Shirasaki, Sento; Duke.
- **Sędzia:** Koichiro Fukushima (statystyki kartek nie sprawdzone, więc rynków kartek i fauli nie wyceniam).
- **H2H** (od 2024, connector): 0:0 (24.10.2026), 3:1 dla Machidy, 2:0 dla Machidy, 1:0 dla Kobe, 0:0, 1:2. Średnio 1,3 gola na mecz, 3 z 6 meczów z jednym lub zerem goli.
- **Forma Kobe:** 2:2 Urawa, 3:2 Ratchaburi, 3:1 Nagoya, 1:0 Daejeon, 0:0 Machida, 1:2 Kawasaki. Średnio 2,2 gola strzelone, 1,3 stracone, mecze otwarte.
- **Forma Machidy:** 2:1 Shanghai Shenhua, 1:0 Shanghai, 0:0 Kobe, 5:0 porażka w Shimizu (21.10, czerwona kartka); dwa mecze (Hiroshima, Gamba) bez wyniku w danych.

## Wycena (poisson.py)
λ Kobe 1,15, λ Machida 1,05 (suma 2,2; rynek bez marży ok. 2,2-2,3). Rotacja ataku Kobe i niski H2H ciągną w dół, otwarta forma Kobe w górę, więc zostaję przy rynku. Czułość: λ 1,05/0,95 oraz 1,25/1,15.

| Rynek | p (zakres) | fair | kurs Superbet | EV (środek) |
|---|---|---|---|---|
| 1 / X / 2 | 38% / 29% / 33% | 2.63 / 3.44 / 3.04 | 2.57 / 3.05 / 2.75 | ujemne |
| Under 2.5 | 62% (57-68%) | 1.61 | 1.56 | -3% |
| BTTS nie | 56% (51-60%) | 1.80 | 1.74 | -3% |
| Under 3.5 & BTTS nie | 54% (49-59%) | 1.86 | 1.80 | -3% |
| 12 & Under 3.5 | 58% (56-59%) | 1.74 | 1.57 | -10% |
| 1X & Under 3.5 | 55% (52-58%) | 1.82 | 1.62 | -11% |
| Over 2.5 | 38% | 2.65 | 2.25 | ujemne |

**Pewność:** średnia dla rynków goli (składy oficjalne, rynek i H2H zgodne), niska dla rynków wyniku (wyrównany mecz, brak mocnego typu) i dla kartek/fauli (brak danych o sędzi). Rożne pomijam (brak własnych średnich, średnia Machidy w danych to jeden mecz).

## Ryzyka
Mecz otwarty, bo Kobe strzela i traci, Machida po 5:0 mogła być w kryzysie; rotacja Kobe nie musi obniżyć goli. Puchar: możliwe zmiany składu w trakcie. Rynek wycenia ten mecz wyżej niż mój model tylko minimalnie, więc nie ma przewagi nad bukmacherem.

## Wniosek
Brak kuponu z EV > 0. Wariant awaryjny: **Under 2.5 gola** (najwyższe p w zakresie kursu 1.5-2.5, pewność średnia), p ok. 62%, kurs 1.56, EV ok. -3% (zakres -11% do +6%). Przewaga bukmachera jest po jego stronie. To oszacowania probabilistyczne, nie gwarancje.
