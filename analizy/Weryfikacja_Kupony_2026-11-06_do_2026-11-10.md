# Weryfikacja kuponów i list predykcji 06-10.11.2026

## Zakres i źródła
Zweryfikowane (typy z kuponów i list poziomu 7): `Kupony_10_2026-11-06`, `Kupony_10_2026-11-06_v2` (NBA/NHL), `Kupony_10_2026-11-07_v2` (NBA/NHL), `Kupony_10_2026-11-08`, `Kupony_10_2026-11-09`, `Kupony_10_2026-11-10`. Rozliczono tylko nogi, które weszły do kuponów i list (74/93 trafionych), nie wszystkie rynki z plików `Analiza_*`.

Wyniki: ESPN scoreboard (piłka top 5 lig, NBA, NHL, ATP Paryż), boxscore ESPN dla rynków zawodnika (Herro, P. George, Curry, Matthews, Keller, Stützle, J. Hughes). Wisła Kr - Cracovia 2:1 (WebSearch, kilka źródeł); Motor - Wisła Płock 3:2 (**jedno źródło**, beIN Sports).

**Nierozliczone:** Korona - Radomiak 1X i Śląsk - Piast 12 (07.11; brak wyniku w ESPN i WebSearch). Przez to `Kupony_10_2026-11-07.md` to weryfikacja częściowa (kupon 1 nierozliczony, kupon 5 przegrany niezależnie od Śląska) i **nie dostaje prefiksu**. Pozostałe `Analiza_*` (w tym `Analiza_dnia_*`, analizy pojedynczych meczów) nie były weryfikowane pełnie, więc też bez prefiksu.

## Bilans (verify.py)
| | Trafione | Oczekiwane |
|---|---|---|
| Nogi wszystkie | 74/93 | 67,1 (+1,6 σ) |
| Listy poziomu 7 (59 nóg) | 49/59 | 42,3 (+1,9 σ) |
| Kupony | 12/20 rozliczonych | 10,5 |

Grupy: NBA ML 18/20 (14,6), NBA total 6/8 (5,6), NBA prop 1/3 (1,9), NHL ML/puck line 20/24 (17,1), NHL prop 4/4 (2,8), NHL total/drużyna 3/3 (2,1), piłka DC/12 11/17 (12,6), piłka gole 8/11 (8,2), piłka 1X2 2/2, tenis 1/1.

Pasma p: 60-70% 25/32 (21,6), 70-80% 45/57 (42,5). Brier 0,167.

## Kupony
| Kupon | Nogi | Kurs | p | Wynik |
|---|---|---|---|---|
| 06.11 K1 | Wisła 1X + HSV O1.5 | 1,51 | 57,8% | trafiony |
| 06.11 K2 | Motor 12 + Toulouse 12 | 1,60 | 55,1% | trafiony (jedno źródło) |
| 06.11 K3 | Venezia 12 + Sevilla 12 | 1,68 | 53,6% | **pudło** Sevilla-Alavés 0:0 |
| 06.11v2 K1 | Celtics ML + Herro O2.5 3PM | 2,04 | 50,4% | **pudło** Herro 1/5 za 3 |
| 07.11 K2 | Fulham 12 + Roma O2.5 | 1,70 | 54,1% | pudło Fulham-Newcastle 1:1 |
| 07.11 K3 | Stuttgart O2.5 + Real | 1,69 | 52,4% | pudło Stuttgart 1:0 |
| 07.11 K4 | Shelton + Espanyol 1X | 1,70 | 51,7% | trafiony |
| 07.11 K5 | Śląsk 12 + Cagliari X2 | 1,75 | 51,0% | pudło (Cagliari wygrało) |
| 07.11 K6 | Leipzig O2.5 + Osasuna X2 | 1,57 | 50,2% | trafiony |
| 07.11 K7 | Torino 1X + Dortmund | 1,61 | 50,2% | trafiony |
| 07.11 K8 | Leeds O1.5 + Málaga 1X | 1,79 | 50,0% | pudło (Leeds 1:0, Málaga 1:2) |
| 07.11 K1 | Korona 1X + Mainz O2.5 | 1,51 | 59,8% | nierozliczony |
| 07.11v2 K1 | DEN + HOU ML | 1,64 | 54,5% | pudło PHX 102:99 HOU |
| 07.11v2 K2 | OKC + DAL po 60' | 1,72 | 46,2% | trafiony |
| 07.11v2 K3 | GSW + CAR po 60' | 1,89 | 46,2% | trafiony |
| 07.11v2 K4 | ATL + EDM po 60' | 1,85 | 45,9% | trafiony |
| 09.11 K1 | CLE ML + VAN +1.5 | 1,89 | 58,4% | pudło (CHA 124:112, VAN 1:3) |
| 09.11 K2 | SA ML + SJ +1.5 | 1,85 | 57,7% | trafiony (SJ po karnych) |
| 09.11 K3 | GS + DET ML | 1,52 | 58,0% | trafiony |
| 10.11 K1 | FLA +1.5 + TOR +1.5 | 2,24 | 50,6% | pudło (TOR 3:6) |
| 10.11 K2 | NSH +1.5 + MTL +1.5 | 2,06 | 50,5% | trafiony |
| 10.11 K3 | MIA ML + WSH +1.5 | 1,67 | 52,3% | trafiony |

Hipotetyczny zysk przy stawce 1 na kupon: +0,55 (informacyjnie; większość kuponów miała zalecaną stawkę 0%, więc to nie dowód przewagi). Kursy w części dni pochodziły z Pinnacle/DraftKings (nie Betclic), więc zysk jest zawyżony.

## Analiza pomyłek
- **Piłka 12 / DC (6 pudeł z 17):** remisy Sevilla-Alavés 0:0, Fulham-Newcastle 1:1, Celta-Levante 0:0, Fiorentina-Juventus 2:2 (4 z 10 rozliczonych nóg "12" przy p 73-77%) oraz Cagliari X2 i Málaga 1X (wygrana drużyny, którą nie typowano). Wariancja: 4 remisy na 10 meczów przy oczekiwanych ok. 2,5 to -1,1 σ.
- **Herro Over 2.5 trójek (06.11v2):** noga o "niskiej-średniej" pewności z p 65% (rynek 61%), weszła do jedynego kuponu z dodatnim EV; trafił 1/5. P. George O2.5 (2/5) też pudło, Curry O3.5 trafił (5/10). Nie błąd definicji; wariancja rynku 3PM, ale to jedyna noga o niskiej pewności w kuponie, która zdecydowała o porażce.
- **VAN +1.5 (09.11) i TOR +1.5 (10.11):** obie flagowane "przewaga niepotwierdzona" (p modelu 6-11 pp nad rynkiem), obie przegrały różnicą 2-3 goli; w tym samym zestawie SJ, FLA, NSH, MTL +1.5 trafiły (4/6, 20/24 w całej grupie puck line/ML). Wariancja.
- **CLE ML 76% (Allen DTD):** przegrana w Charlotte; wariancja.
- **HOU ML (07.11v2):** 99:102 u PHX; wariancja (p 74% z poziomem 2, EV -4,5%).
- **Stuttgart-Werder O2.5 (1:0):** wariancja (p 69,7%).
- Żaden przypadek nie łamie istniejącej reguły ze skilla ani nie wskazuje błędu danych/rozliczenia.

## Co zadziałało
NBA moneyline faworytów (18/20 przy 14,6 oczekiwanych), NHL +1.5 (20/24 vs 17,1), rynki zawodnika NHL (4/4 po potwierdzonych składach), totale NBA Over (6/8), wszystkie trzy kupony poziomu 3+4 NBA/NHL z 07.11v2 (3 z 4 kuponów trafione).

## Kalibracja skilli
**Bez zmian.** Brak konkretnego błędu procesu: odchylenie nóg +1,6 σ jest w stronę trafień, a pudła to wariancja (remisy w 12, rynki 3PM, puck line z p modelu nad rynkiem). Jedna kolejka nie uzasadnia zmiany reguł; wpisy w "Do obserwacji".

## Do obserwacji
- **Piłka "12 (bez remisu)" przy p 73-77%:** 4 remisy w 10 nogach (Sevilla, Fulham, Celta, Fiorentina). Zmienić (np. p 12 o 2-3 pp w dół w meczach ligowych o wyrównanych λ), jeśli w kolejnych weryfikacjach ≥ 10 nóg da hit rate < 65%.
- **NBA Over trójek 2.5 przy p 60-65% i niskiej pewności:** 1/3 (Herro, George pudło; Curry trafił). Zmienić regułę (pułap p ok. 55% bez potwierdzonych minut/roli), jeśli po ≥ 8 nogach hit rate < 50%.
- **NBA ML i NHL +1.5 nad oczekiwaniem (+1,7 σ, +1,3 σ):** sprawdzić, czy p faworytów NBA 64-82% nie są zaniżone; próba za mała (20 i 24 nogi).
- **Dane:** Motor - Wisła Płock z jednego źródła; Korona - Radomiak i Śląsk - Piast nierozliczone; do uzupełnienia, wtedy oznaczyć `Kupony_10_2026-11-07.md`.

To oszacowania, nie gwarancje; mała próba.
