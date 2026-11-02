# Linemate: NBA i NHL, 30-31.10.2026

Pobrano 30.10.2026 (sesja zalogowana, plan bez Linemate+: brak danych o wpływie kontuzji na kolegów z drużyny). Źródło: linemate.io/nba, /nba/trends, /nhl, /nhl/trends.

**Pokrycie:** NBA 9 meczów nocy 30/31.10 (CHA-WAS, NYK-PHI, CHI-BOS, ORL-TOR, DET-BKN, HOU-DAL, IND-MIA, LAC-MIN, LAL-GSW), bez PHX-DEN w widoku głównym (picki Bookera i Brooksa dotyczą go). NHL tylko 3 mecze dnia: NJD-VGK, WPG-FLA, SEA-CGY (mecze z 31.10 Linemate jeszcze nie ma). Kursy na Linemate pochodzą z nieokreślonej książki, **to nie Betclic**; Betclic nie ma rynków zawodnika NBA/NHL, a gg397.bet nie był sprawdzony (przeglądarka była rozłączona). Hit rate to historia, nie p; p_adj = (k + 10·p_kurs)/(n + 10) to tylko ranking kandydatów (efekt selekcji zawyża o kilkanaście pp).

## Ranking (sort po p_adj - p_kurs; max 2 picki na mecz)

| # | Mecz (PL) | Pick, linia | Kurs Linemate | Hit rate | p_adj | p_kurs | Różnica | Zgodność z własną analizą / flagi |
|---|---|---|---|---|---|---|---|---|
| 1 | FLA-WPG (sob 00:00) | Niederreiter Under 0,5 pkt | 1,33 | 18/18 | 91,1% | 75,2% | +15,9 pp | brak własnego p; kurs tuż nad progiem |
| 2 | SEA-CGY (sob 01:00) | Coronato Under 0,5 gola | 1,31 | 5/5 | 84,2% | 76,3% | +7,9 pp | mała próba |
| 3 | FLA-WPG | Perfetti Over 1,5 strzałów | 1,50 | 8/8 | 81,5% | 66,7% | +14,8 pp | brak własnego p; bramkarz niepotwierdzony |
| 4 | FLA-WPG | Rosen Under 0,5 pkt | 1,28 | 12/14 | 82,5% | 78,1% | +4,4 pp | słaba przewaga |
| 5 | NJD-VGK (pt 23:00) | Hischier Over 1,5 strzałów | 1,56 | 6/6 | 77,6% | 64,1% | +13,5 pp | mała próba |
| 6 | FLA-WPG | B. Tkachuk Over 0,5 pkt | 1,73 | 7/8 (w tym 7/8 bez Marchanda) | 71,0% | 57,8% | +13,2 pp | **zgodne z analizą NHL: Marchand, Barkov, Markstrom na IR**; brak własnego p |
| 7 | FLA-WPG | K. Connor Over 2,5 strzałów | 1,82 | 5/5 | 69,9% | 54,9% | +15,0 pp | mała próba, mecz FLA vs WPG b2b |
| 8 | CHA-WAS (sob 00:00) | brak mocnego typu: Diabate Over 1,5 ast 1,78 (z parlaya) | 1,78 | 5 z ostatnich 6 | ok. 66% | 56,2% | ok. +10 pp | analiza NBA: Schröder DTD |
| 9 | PHX-DEN (sob 03:00) | Booker Over 5,5 asyst | 1,91 | 4/5 (4/4 vs DEN) | 61,6% | 52,4% | +9,2 pp | analiza: "brak typu" (średnia 5,3, mała próba 3 meczów) |
| 10 | NYK-PHI (sob 00:30) | J. Hart Over 7,5 zbiórek | 1,95 | 9/12 | 64,3% | 51,3% | +13,0 pp | Alvarado Out (analiza), brak własnego p |
| 11 | DET-BKN (sob 00:30) | P. Reed Under 9,5 zbiórek | 1,88 | 19/20 | 81,1% | 53,2% | +27,9 pp | **flaga:** Duren Out (analiza), więcej zbiórek dla Reeda; trend z innej roli |
| 12 | LAC-MIN (sob 01:00) | D. Jones Under 1,5 strat | 1,44 | 18/20 | 83,1% | 69,4% | +13,7 pp | Edwards Out, przewaga rynku |
| 13 | CHI-BOS (sob 00:30) | brak: Tatum/George Under (analiza) nie ma w trendach Linemate | - | - | - | - | - | blowout 15,5 pkt |

Odrzucone: Giddey O1,5 zb. 1Q, Barnes O1,5 zb. 1Q, Brooks O3,5 pkt 1Q (rynki kwartałowe, małe próby), Sengun O14,5 REB+AST (DTD), Siakam/Murray/Carter O0,5 przechwyt (1,72-1,85, 3/4-11/14), Anunoby U2,5 trójek (5/6, brak własnego p), parlaye Linemate (korelacja, nie na kupon).

## Wnioski dla poziomów -1 i -2

- Linemate **nie dodaje nóg do kuponów**: żaden pick nie ma kursu Betclic ani gg397.bet, a własnego p mamy tylko dla totali drużyn NBA i dwóch rynków zawodnika z linią BettingPros (Tatum PRA U43,5, Towns PRA O34,5). W Linemate nie ma żadnego z tych trzech rynków (totale drużyn NBA, Tatum, Towns).
- Zgodność sygnałów: Linemate potwierdza kierunek analizy NHL dla FLA (bez Marchanda Tkachuk-owie mają wyższy udział w punktach), ale to nie jest p; przed użyciem trzeba wycenić w `nhl-analyst` i potwierdzić składy/bramkarzy.
- Flaga: Reed Under 9,5 zbiórek (19/20) kłóci się z faktem, że Duren jest Out, więc hit rate pochodzi z innej roli.
