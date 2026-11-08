# Napoli - Lazio (Serie A 26/27, 08.11.2026, 12:30 czasu polskiego)

Źródła: connector `superbet-mcp` (kursy, składy, nieobecni, statystyki sezonu, H2H, sędzia); model Poissona (`poisson.py`, `markets.py`). Rezerwa (WebSearch, MCP `sportsdata`) nie użyta: czas do startu ok. 85 min, a connector dał komplet danych poza statystykami sędziego. Analiza z godz. ok. 11:05; skład oficjalny jeszcze nieznany.

## Dane

- **Sędzia:** Luca Pairetto (VAR: Aureliano). Brak jego średnich kartek/fauli w źródłach connectora, więc rynki kartek i fauli bez typu.
- **Składy (przewidywane, niepotwierdzone):** Napoli 3-5-1-1 (Meret; Rrahmani, Marin, Beukema; Politano, Anguissa, Gilmour, McTominay, Lang; De Bruyne; Hojlund). Lazio 4-3-3 (Mandas; Floriani Mussolini, Sutalo, Provstgaard, Pellegrini; Frattesi, Belahyane, Taylor; Isaksen, Pinamonti, Noslin).
- **Nieobecni Napoli (10):** Lobotka, Olivera, Spinazzola, Di Lorenzo, Neres, Favasuli, Mukinayi, Alisson Santos, Buongiorno (kontuzje, źródło "manual", powody nieznane), Marianucci (zawieszenie). To głównie obrona i boki: realne osłabienie defensywy.
- **Nieobecni Lazio (3):** Zaccagni, Gudmundsson, Tavares (kontuzje).
- **Sezon (10 meczów):** Napoli 1.7 gola strzelone / 1.3 stracone, xG 1.7, strzały 15.6, rożne 5.3, żółte 1.0, faule 8.6. Lazio 2.4 / 0.8, xG 1.6, strzały 13.8, rożne 4.7, żółte 1.6, faule 11.1. Gole Lazio zawyża 6-2 w Sassuolo (xG 1.6 mówi o mniejszej sile ataku).
- **Forma Napoli (5 meczów):** 1-4 (Porto, wyjazd), 0-2 Juventus, 4-1 Monza, 3-3 Roma, 4-3 Bodo: 13 straconych goli w 5 meczach.
- **Forma Lazio:** 2-1 Cagliari, 6-2 Sassuolo (wyjazd), 2-1 Parma, 3-0 Juventus (wyjazd), 3-1 Monza.
- **H2H (ostatnie 5):** 0-2, 0-2 (Lazio wygrywało w Neapolu i u siebie w sezonie 25/26), 2-2, 0-1, 3-1 dla Lazio. Ostatnie 5 bezpośrednich meczów to 4 wygrane/remisy Lazio (waga niska: inne składy i trenerzy).
- **Kursy Superbet (API):** 1 = 2.30, X = 3.60, 2 = 2.92; po usunięciu marży ok. 41.2% / 26.3% / 32.4%. Over 2.5 = 1.59 (ok. 59% bez marży), BTTS tak = 1.51 (ok. 62%).

## Model

λ Napoli 1.50, λ Lazio 1.35 (łącznie 2.85). Podstawa: średnie ligowe dom/wyjazd, ataki 1.7 / 2.4 z korektą w dół dla Lazio (skrzywienie przez 6-2) i w górę dla straconych goli Napoli (nieobecni obrońcy, 13 straconych w 5). Wariant niski 1.35/1.20 i wysoki 1.65/1.50 pokazują czułość.

| Rynek | p (centralne) | zakres p (3 warianty λ) | fair | Superbet | Pewność |
|---|---|---|---|---|---|
| Napoli wygra | 40.9% | 40.2-41.4% | 2.45 | 2.30 | średnia |
| Remis | 24.9% | 23.6-26.6% | 4.01 | 3.60 | średnia |
| Lazio wygra | 34.2% | 33.2-35.0% | 2.93 | 2.92 | średnia |
| 1X (Napoli nie przegra) | 65.8% | 65.0-66.8% | 1.52 | 1.40 | średnia |
| X2 (Lazio nie przegra) | 59.1% | 58.6-59.8% | 1.69 | 1.61 | średnia |
| Over 1.5 gola | 77.7% | 72.3-82.2% | 1.29 | 1.18 | średnia |
| Over 2.5 gola | 54.2% | 46.9-61.0% | 1.84 | 1.59 | średnia |
| Under 3.5 | 68.1% | 61.4-74.7% | 1.47 | 1.55 | średnia |
| Under 4.5 | 88-92% | - | ok. 1.1 | 1.21 | średnia (poniżej progu fair 1.15) |
| BTTS tak | 57.5% | 51.8-62.8% | 1.74 | 1.51 | średnia |
| Rożne (średnia 10.0, O 9.5) | 52.8% | zależy od średniej 9.5-10.6 | 1.89 | 2.00 | niska (jedno źródło średnich, brak danych sędziego) |
| Kartki, faule | - | - | - | - | niska: sędzia Pairetto bez statystyk w źródłach, rynek kartek Superbet wycenia ok. 4.5 kartki, a średnia sezonu obu drużyn to ok. 2.7 żółtych (różnica >1: prawdopodobnie inna definicja kartek) |

Rozbieżność z rynkiem: Over 2.5 mam o ok. 5 pp niżej niż rynek (54% vs 59%), BTTS o ok. 5 pp niżej (57.5% vs 62%). Rynek prawdopodobnie bardziej waży defensywę Napoli (10 nieobecnych, 13 straconych w 5 meczach) i skuteczność Lazio niż moje średnie sezonowe. Nie schodzę pod rynek bez konkretu, więc zakres p wyżej sięga do wariantu wysokiego (Over 2.5 = 61%), a nie do jednej liczby.

## Ryzyka

- Skład nieoficjalny: przy braku kilku zawodników Napoli podstawowej jedenastki (status "manual", powody nieznane) przewaga obrony Lazio / ataku Lazio może być większa.
- Wynik zależny od defensywy Napoli: ryzyko wysokiej wygranej Lazio (zakład X2/Under łączy się z rynkiem, który może być źle wyceniony w górę).
- Rynki Under przy 10 nieobecnych w jednej drużynie bywają niedoszacowane przez takie dane (źródło "manual").

*To oszacowania probabilistyczne, nie gwarancje.*
