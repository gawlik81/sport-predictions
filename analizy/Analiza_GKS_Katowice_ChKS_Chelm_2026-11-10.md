# GKS Katowice - ChKS Chełm (TAURON Liga / PlusLiga, bo5, 10.11.2026, 17:30)

Superbet event_id 15641466. Skill: volleyball-analyst. Pewność całej analizy: **niska**.

## Typ
**Brak mocnego typu** (mecz wyrównany, p Katowic ok. 46%, bez przewagi nad rynkiem). Żaden rynek nie ma EV > 0 przy kursach Superbet.

## Model
Źródło p: kursy Superbet "Zwycięzca" (Katowice 2.02, Chełm 1.75), po usunięciu marży (przelicznik 1.066) P(Katowice) = 46,4%, p seta Katowic = 48,1% (`volleyball_model.py --from-match 0.464 --bo 5`).
Korekt własnych nie wprowadzono: brak potwierdzonych składów i informacji o kontuzjach, a forma jest niejednoznaczna i zawarta w kursie.

| Rynek | p | fair | kurs Superbet | EV |
|---|---|---|---|---|
| Katowice wygra | 46,4% | 2.16 | 2.02 | -6,3% |
| Chełm wygra | 53,6% | 1.87 | 1.75 | -6,2% |
| Chełm +1.5 seta | 71,6% | 1.40 | 1.38 | -1,2% |
| Katowice +1.5 seta | 65,8% | 1.52 | 1.43 | -5,9% |
| Katowice +2.5 seta | 86,0% | 1.16 | 1.13 | -2,8% |
| Chełm +2.5 seta | 88,9% | 1.13 | 1.07 | -4,9% |
| Poniżej 4.5 seta (nie będzie 5. seta) | 62,6% | 1.60 | 1.57 | -1,7% |
| Będzie 4. set (powyżej 3.5) | 74,9% | 1.34 | 1.22 | -8,6% |
| Będzie 5. set | 37,4% | 2.67 | 2.22 | -16,9% |
| Dokładnie 4 sety | 37,5% | 2.67 | 2.45 | -8,1% |

## Statystyki i forma (wyniki, bez atak/blok/zagrywka: brak danych)
- Katowice (sezon 2026/27): 3:0 Zawiercie (16.10), 3:2 w Suwałkach (23.10), 0:3 Skra (27.10), 0:3 Lublin (31.10). Bilans 2-2.
- Chełm: 2:3 Stilon Gorzów (19.10), 0:3 Resovia (25.10), 2:3 Barkom (1.11, wyjazd), 3:2 Norwid Częstochowa (7.11, dom). Bilans 1-3, trzy z czterech meczów po 5 setów. Sezon 2025/26 zakończył na 13. miejscu (7 zwycięstw).
- Obie drużyny często grają długie mecze, co wspiera Over setów, ale kurs na to jest zbyt niski.

## H2H
Nie znaleziono wiarygodnych, świeżych wyników bezpośrednich meczów (brak danych).

## Informacje medialne
- Katowice pozyskały ukraińskiego przyjmującego Jewhenija Kisiliuka (Flashscore); brak informacji, czy gra.
- Składy, status rozgrywającego (Batak w kadrze Katowic) i kontuzje: **niepotwierdzone**, nie znaleziono źródeł.
- Rozbieżność: rynek faworyzuje Chełm (1.75), choć forma Chełma jest słabsza (bilans 1-3) i Katowice grają u siebie. Nie wiem, co za tym stoi (skład, absencje); zgodnie z zasadą nie schodzę pod rynek bez konkretów.

## Ryzyka
Niepotwierdzony skład i rozgrywający, niewyjaśniona rozbieżność z formą, nowy skill bez zweryfikowanych typów.

## Źródła
Kursy: connector superbet (rynki). Wyniki: globalsportsarchive.com (profil GKS Katowice), betexplorer.com (wyniki ChKS Chełm). Składy, statystyki, H2H: rezerwa (WebSearch), nic nie znaleziono. BettingPros: nie sprawdzano (brak pokrycia siatkówki).

## Wniosek dla kuponu
Pewność niska, wszystkie rynki z EV < 0: kuponu nie przygotowano (reguła superbet-coupon).

To oszacowania, nie gwarancje.
