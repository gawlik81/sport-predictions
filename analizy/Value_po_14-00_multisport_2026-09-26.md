# Value po 14:00 — sobota, 26.09.2026 (piłka, tenis i e-sport; kursy Betclic ok. 14:20)

Użyte skille: football-predictor, tennis-predictor i esports-predictor.

**EV** = p (konserwatywne) × kurs Betclic. Value oznacza EV > 1.

## 5 typów

| # | Dyscyplina | Mecz (godz.) | Typ | Model | Konserw. | Fair | Betclic | EV |
|---|---|---|---|---|---|---|---|---|
| 1 | Piłka (LN C4) | Islandia – Estonia (18:00) | **X2** | 44,9% | ~38% | 2,63 | 3,32 | 1,26 |
| 2 | Piłka (LN C4) | Islandia – Estonia (18:00) | **Under 2,5 gola** | 58,3% | ~53% | 1,89 | 2,15 | 1,14 |
| 3 | Tenis (Laver Cup) | Zverev – de Minaur (ok. 15:10) | **de Minaur +1,5 seta** | 64,1% | ~55% | 1,82 | 1,99 | 1,09 |
| 4 | Piłka (LN C1) | Albania – Białoruś (20:45) | **X2** | 52,9% | ~48% | 2,08 | 2,25 | 1,08 |
| 5 | Tenis (Laver Cup) | Alcaraz – Fritz (ok. 20:00) | **Fritz +1,5 seta** | 66,4% | ~55% | 1,82 | 1,93 | 1,06 |

**Korelacja:** typy #1 i #2 dotyczą tego samego meczu. Wyniki 0-0, 1-1 i 0-1 trafiają oba, a pewna wygrana Islandii przegrywa oba.

## Tenis — Laver Cup (O2 Londyn, hala, kort twardy)

**Format:** best-of-3, a zamiast trzeciego seta rozgrywa się super tie-break do 10 punktów. Skrypt modeluje pełny trzeci set, więc:
- typy na zwycięzcę i na handicap setowy są przybliżeniem;
- typ „+1,5 seta” wymaga tylko wygrania jednego z dwóch pierwszych setów, więc super tie-break go nie zmienia;
- total gemów pomijam, bo model go zawyża (super tie-break liczy się jako 1 gem).

**Dane:** Tennis Abstract, kort twardy od 09.2025. Wejście modelu: p_serve = SPW − (RPW rywala − 0,36).

| Mecz | SPW / RPW (A ; B) | p_serve A : B | Model: A wygrywa | Rynek | A 2-0 (model / rynek) |
|---|---|---|---|---|---|
| Zverev – de Minaur | 70,4/35,7 ; 63,9/39,1 | 0,673 : 0,642 | 64,7% | ~77% (1,25) | 35,9% / ~55% (1,73) |
| Alcaraz – Fritz | 69,5/42,6 ; 71,2/38,4 | 0,671 : 0,646 | 61,9% | ~76% (1,27) | 33,7% / ~53% (1,78) |

**Model a rynek:** rozjazd przekracza 10 pp, a model w ATP zwykle spłaszcza faworytów. Dlatego obcinam p underdoga o ~9-11 pp.

**Argumenty jakościowe:**
- **de Minaur.**
  - Za: w meczach drużynowych ma z Zverevem 3-0 (Laver Cup 2025, United Cup 2024, ATP Cup 2020) i dobrze czuje się w formacie drużynowym.
  - Przeciw: Zverev ma sezon życia (bilans 55-13, tytuły w Roland Garros i US Open) i prowadzi w H2H 8-3. Obaj grają pierwszy mecz po ok. 3 tygodniach przerwy.
- **Fritz.**
  - Za: Alcaraz wrócił po urazie nadgarstka z kwietnia i od tego czasu rozegrał tylko 5 meczów singlowych. Kapitan Noah przyznał, że obawiał się jego występu. Fritz pokonał Alcaraza w Laver Cup 2025 w dwóch setach, a hala sprzyja jego serwisowi.
  - Przeciw: Alcaraz prowadzi w H2H 5-1 i w piątek wygrał debla z Fritzem 6-4 6-4.

## Piłka — patrz `Value_po_14-00_2026-09-26.md`

- **Islandia – Estonia.** Islandia nie wygrała 6 meczów (0-2-4) i w 3 z 5 ostatnich nie strzeliła gola. Estonia gra W-W-L-D-W, a w H2H 3 z 4 meczów skończyły się remisem. Rynek daje Islandii 74%, a model 55%.
- **Albania – Białoruś.** Albania przegrała 5 meczów z rzędu, a Białoruś nie przegrała 5. Ryzyko: H2H 3-1-0 dla Albanii.

## E-sport — brak typów

- **Oferta Betclic dziś po 14:00:** tylko League of Legends. CS2 i Dota 2 nie mają dziś wydarzeń.
  - EMEA Masters Summer 2026, faza grupowa (18:00-21:00).
  - CBLOL: FURIA – RED Canids.
  - LCS: LYON – Shopify Rebellion (22:00, kurs 1,08).
- **Odrzucone z powodu reguł 7-8 skilla** (tier-2, brak statystyk, Liquipedia zwraca 403):
  - EMEA Masters: większość meczów to faworyci po kursie 1,01-1,15, które nie przechodzą filtra fair >1,15.
  - Wyrównane mecze EMEA Masters (Valerion – LODIS 1,75/1,92, Phantasma – SU 3,10/1,30) nie mają danych, na których dałoby się oprzeć wycenę.
  - LYON – Shopify: bez danych i poniżej filtra kursów.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
