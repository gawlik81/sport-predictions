# Najbardziej prawdopodobna predykcja dla każdego wydarzenia - 16.10.2026

Kryterium: z rynków Betclic (kurs > 1,05) wybrana predykcja o najwyższym p dla każdego wydarzenia. Kursy: betclic.pl (Chrome i dane ze strony, 16.10 rano, godziny CEST). Dotyczy wydarzeń od 12:00; poranne mecze tenisowe (Świtolina, Chwalińska - Sakkari, Jodar - Ruud) już trwają lub trwały.

## Skąd p

- **Piłka (8 meczów):** rozkład Poissona dopasowany do 1X2 i linii totali Pinnacle (po devigu), z którego policzyłem wszystkie rynki Betclic: gole, podwójną szansę, handicapy, BTTS. Błąd dopasowania modelu do rynku Pinnacle to 0,1-0,3 pp na liniach, ale p ogonowych rynków (handicap +3, Under 5,5) pochodzi z ekstrapolacji modelu: pewność średnia.
- **Tenis, LoL, CS2:** p wprost z linii Pinnacle (handicap setów / map) po devigu.
- Kupon liczę z limitem 75% dla tenisa (brak statystyk serwisu), choć rynek daje więcej.
- Brak własnych korekt kadrowych: składy i kontuzje nieogłoszone.

## Predykcje (po jednej na wydarzenie)

| Godz. | Wydarzenie | Predykcja | p | Kurs Betclic | Fair | EV |
|---|---|---|---|---|---|---|
| 12:00 | Medvedev - Paul | Medvedev wygra seta | 81,9% (limit 75%) | 1,16 | 1,22 | -5,0% |
| 13:00 | Li - Świątek | Świątek wygra seta | 89,7% (limit 75%) | 1,06 | 1,11 | -4,9% |
| 16:00 | Aurora - 9z | Aurora +1,5 mapy | 82,6% | 1,12 | 1,21 | -7,5% |
| 18:00 | Wieczysta - Raków | Under 5,5 gola | 87,7% | 1,09 | 1,14 | -4,4% |
| 18:00 | Warta - Unia | Unia (+3) handicap | 90,0% | 1,07 | 1,11 | -3,7% |
| 20:00 | Karmine Corp - MVK (Bo5) | KC +1,5 mapy | 86,2% | 1,06 | 1,16 | -8,6% |
| 20:30 | Frankfurt - Köln | Over 1,5 gola | 88,8% | 1,08 | 1,13 | -4,1% |
| 20:30 | Widzew - Wisła | Widzew (+2) handicap | 84,3% | 1,12 | 1,19 | -5,6% |
| 20:30 | Ruch - Odra | Odra (+3) handicap | 88,2% | 1,08 | 1,13 | -4,7% |
| 20:45 | Frosinone - Sassuolo | Sassuolo (+3) handicap | 91,8% | 1,06 | 1,09 | -2,7% |
| 20:45 | Le Mans - Toulouse | Under 5,5 gola | 91,6% | 1,06 | 1,09 | -2,9% |
| 21:00 | Deportivo - Levante | Levante (+3) handicap | 90,4% | 1,06 | 1,11 | -4,1% |

Handicap "(+3)" to handicap 3-drogowy Betclic: drużyna wygrywa zakład, jeśli nie przegra różnicą 3 lub więcej goli.

## Kupon (kurs 1,5-2,0, najwyższe p)

| Mecz | Predykcja | p | Kurs |
|---|---|---|---|
| Frankfurt - Köln | Over 1,5 gola | 88,8% | 1,08 |
| Frosinone - Sassuolo | Sassuolo (+3) | 91,8% | 1,06 |
| Wieczysta - Raków | Under 5,5 gola | 87,7% | 1,09 |
| Widzew - Wisła | Widzew (+2) | 84,3% | 1,12 |
| Ruch - Odra | Odra (+3) | 88,2% | 1,08 |

**Łączne p: 53,2% | fair 1,88 | kurs 1,51 | EV -19,8% | stawka 0% bankrolla.**

Dlaczego EV jest tak niskie: przy nogach po 1,06-1,12 trzeba złożyć 5-6 nóg, żeby przekroczyć kurs 1,5, a marża Betclic (3-5% na nodze) się kumuluje. Dla porównania, poprzednie 2-nogowe kupony o p 50-60% miały EV od -7% do -13%. Kolejne warianty o podobnym p (53,0-53,3%) to zamiany jednej nogi (np. Le Mans Under 5,5 zamiast Frankfurt Over 1,5), z EV około -20%.

Gdyby próg kursu zestawu obniżyć do 1,3: 4 nogi (Le Mans, Frosinone, Deportivo, Warta) dają p 68,4% przy kursie 1,27; 3 nogi p 76,0% przy 1,19.

## Ryzyka

- **Ekstrapolacja ogonów:** handicapy +2/+3 i Under 5,5 wyceniłem modelem Poissona, który zaniża skrajne wyniki (pogrom 4+ goli) przy meczach z podwyższonym tempem. Jeden mecz z dużą różnicą goli przekreśla cały kupon.
- **Korelacja nóg:** Over 1,5 i Under 5,5 nie są sprzeczne, ale w kuponie nie ma nóg, które się wykluczają; wszystkie są niezależne meczowo.
- **1. Liga:** limity Pinnacle 100-400 USD, więc p mniej wiarygodne.
- **Kursy** mogą się zmienić do czasu meczu. To oszacowania, nie gwarancje.
