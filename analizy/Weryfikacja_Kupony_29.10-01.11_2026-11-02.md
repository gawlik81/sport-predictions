# Weryfikacja kuponów z 29.10, 30-31.10 i 01.11.2026

**Zweryfikowane pliki (po zmianie nazwy z prefiksem `ZWERYFIKOWANE_`):** `Kupony_10_2026-10-29.md` (6 kuponów + tryb EV E1-E10), `Kupony_10_2026-10-30.md` (kupony 1-10), `Kupony_EV_NBA_NHL_2026-10-30.md` (-1/A-D, single NBA/NHL), `Kupony_10_2026-11-01.md` i `_v2.md`.
**Nie oznaczone:** pliki `Analiza_*`, `Kursy_*`, `Linemate_*`, `Terminarz_*` z tych dni. Sprawdzono tylko nogi, które weszły do kuponów, więc reszta rynków z analiz nie jest rozliczona.

**Źródła wyników:** ESPN scoreboard/summary (piłka, NBA, NHL, tenis, UFC; jedno źródło), boxscore ESPN (Towns, Tatum), WebSearch (Ekstraklasa: 3 portale zgodne; CS2 MOUZ-FURIA: HLTV i inne zgodne). Tenis z ESPN zwraca duplikaty całego turnieju, więc wyniki filtrowano po parze nazwisk.
**Uwaga o danych:** p nóg kuponów z 29.10 i kuponów v2 z 01.11 (poziomy 2-4) dokument podaje tylko łącznie, więc te kupony wchodzą do bilansu jako jednostki z p łącznym.

## Wyniki (nogi kuponów)
- **29.10:** ATL-CLE 114-111, NO-SAC 132-120, POR-MEM 103-124; NHL: CAR-CBJ 3-2, TBL-WPG 6-4, STL-BOS 4-1, LAK-OTT 6-5 po dogr., ANA-BUF 6-7, DAL-MTL 2-5, DET-CHI 4-1, MIN-NYI 3-4 po dogr., NSH-WSH 3-4; piłka: Atl.-MG 0-1 Cruzeiro, Vasco 1-4 Flamengo, Grêmio 2-0 Athletico.
- **30-31.10:** Lech 3-1 Wisła, GKS 3-2 Widzew, Górnik 0-0 Legia, Coventry 3-1 Sunderland, Bournemouth 2-0 Leeds, Brentford 2-0 Forest, Hull 2-2 Ipswich, Chelsea 2-0 MU, Villa 1-1 Fulham, Lille 1-0 Lens, Troyes 2-0 Le Mans, Rayo 3-0 Celta, Schalke 0-2 Leipzig, Leverkusen 2-4 Stuttgart, Milan 3-1 Inter; Struff - Borges 6-2 6-3, Fils - Fritz krecz (ESPN: 2-6, 0-2, krecz Filsa); MOUZ - FURIA 1-2; Rodriguez - Alencar i Y. Santos - L. Santos na dystans (3 rundy, pełny czas); NBA team totals: ORL 121, MIA 145, CHA 79, MIN 127, GSW 112, PHX 120; FLA 5-2 WPG; Towns PRA 37, Tatum PRA 40.
- **01.11:** Lecce 1-2 Genoa, Como 1-0 Venezia, Racing 0-3 Real, Juventus 2-0 Napoli, Elche 0-1 Valencia, Athletic 2-1 Real Sociedad, Getafe 3-1 Sevilla, Paris FC 3-1 Monaco, Liverpool 0-1 Arsenal, Frosinone 2-0 Torino, Marseille 2-0 Toulouse, Lazio 2-1 Cagliari, Lyon 2-0 Angers, Orlando 97-108 Boston, Carolina 7-0 Winnipeg, Alcaraz wygrał (jedno źródło), Basel: Vacherot pokonał Lehecka 2-1 w setach.

## Bilans (skrypt `verify.py`, 65 jednostek)
| | Trafione | Oczekiwane |
|---|---|---|
| Wszystkie jednostki | 40/65 | 36,9 (+0,84 odch.) |
| Kupony 29.10 (poziom 1-2, wszystkie EV<0) | 6/6 | 3,35 (+2,2 odch.) |
| Kupony 30.10 K1-K10 | 5/9 (K7 nierozliczony: krecz) | ok. 5,0 |
| Kupony 01.11 (v1+v2 pojedyncze, poziom 0-2, bez -1) | 2/2 skryptem + 4/8 ręcznie (v2 poziomy 2-4) | ok. 4,4 |
| Tryb EV 29.10 (E1-E10) | 3/10 | 2,84 |
| NBA/NHL -1 (30.10) | 1/4 | 1,24 |
| 01.11 -1/1-5 | 2/5 | 0,9 |

Kupony 30.10: K2 (poziom 0, EV +5,4%) trafiony, K1 (EV +6,5%) przegrał przez Struff O21,5. Hipotetyczny zysk skryptu (stawka 1 na kupon): +6,66, tylko informacyjnie.
Kupony v2 z 01.11 poziomy 2-4 rozliczone ręcznie: #2 Como+Lazio O1,5 trafiony, #3 Real+Athletic O1,5 trafiony, #4 Getafe/Sevilla X2 przegrany, #5 Elche O1,5 przegrany (0-1), #6 Liverpool 1X przegrany, #7 Alcaraz+Carolina trafiony, #8 Marseille O2,5 przegrany (2-0). Razem 3/7 z oczekiwanych ok. 3,9.

## Analiza pomyłek
- **NHL Under 4,5 (29.10), 0/8 przy p 26-35%:** padło w sumie 5, 5, 5, 7, 7, 7, 7 i 13 goli. Wcześniejsze nogi "przewagi niepotwierdzonej" 53% przy p 65%. Jeden wieczór daje szanse ok. 0,3-2% na taki wynik przy niezależności, ale jest to też druga seria w tej samej grupie z p wyraźnie nad rynkiem. **Błąd procesu (p > rynek o >5 pp bez konkretnej informacji, Poisson z krótką próbą).** Zmiana w `nhl-analyst`.
- **NBA total drużyny Under (30.10), 2/6 przy p 55-61%:** MIA 145, ORL 121, MIN 127, PHX 120 pkt. Wszystkie p były o 5-9 pp nad rynkiem, średnie modelu 2-3,5 pkt pod linią (próba 3-6 meczów). Dokument sam ostrzegał o przesunięciu modelu. **Błąd procesu (to samo przesunięcie w 6 nogach).** Zmiana w `nba-analyst`; stawki po ściągnięciu p (0,2-0,3%) ograniczyły skutki.
- **Struff - Borges O21,5 gemów (p 77%, kupon 1, stawka 2,5%):** 6-2 6-3 = 17 gemów. p 77% na Over przy dwóch zawodnikach z silnym serwisem wygląda na zawyżone (Over 21,5 w bo3 zwykle ok. 55-65%, wymaga 3 setów lub tiebreaków), a p_serve wzięto z 10-12 meczów. **Podejrzenie błędu procesu, ale jedna noga; do obserwacji** (reguła "bez total gemów przy p_serve z rankingu" już istnieje).
- **Fils - Fritz (krecz):** noga O21,5 nierozliczona (kupon 7). Fils w analizie był oznaczony jako zmęczony; ryzyko kreczu wpisane.
- **Leverkusen 1X (73%) i Milan - Inter, Inter X2 (72,5%) w kuponie 10, Górnik - Legia O1,5 (73%), Coventry U3,5 (75,8%), Lecce U2,5, Getafe-Sevilla X2, Liverpool 1X, Marseille O2,5, Elche O1,5:** **wariancja** (p 60-78%, pojedyncze rozjazdy; 1X/DC 5/7 przy 5,3).
- **Kupony 29.10 6/6 przy EV<0:** wariancja w drugą stronę (p łączne 51-64%, szanse 6/6 ok. 1,5%). Nie jest to dowód, że poziom 2 ma przewagę; stawka 0%.
- **Błąd budowy kuponu:** brak nowych. Kupon 1 z 30.10 ustawiono zgodnie z regułami; przegrał jedną nogą.

## Co zadziałało
- Tryb EV z korektą p ściągniętym do rynku + 5 pp zmniejszył stawki dokładnie w grupach, które padły (NHL Under, NBA team totals).
- Piłka BTTS nie / Under 2,5 w trybie EV 01.11 trafiły 9/13 (oczekiwane 6,5): przeciwny kierunek niż NHL/NBA, więc nie ma podstaw do globalnej korekty "under" w piłce.
- Rynki MMA "na dystans" 2/2, Towns PRA i Tatum PRA 2/2, 1X2 piłka (Como, Real, Lech) 3/3, piłka p 80%+ 2/2.

## Kalibracja skilli
- **`nhl-analyst`:** dopisano regułę, że Under 4,5 z Poissona bez konkretu nie schodzi pod rynek o >3 pp (29-30.10: 0/8).
- **`nba-analyst`:** dopisano regułę dla totali drużyny Under: p do rynku + 3 pp, gdy linia jest >2 pkt nad średnią modelu bez konkretu (2/6).
- Pozostałe skille bez zmian: pudła w piłce, tenisie i MMA to wariancja lub pojedyncze przypadki.

## Do obserwacji
- **Total gemów w tenisie przy p>70%:** Struff-Borges 0/1 (+ Fils-Fritz krecz). Warunek zmiany: kolejne 2-3 pudła Over z p>70% → obniżyć sufit p dla Over gemów w bo3 do ok. 65%.
- **Piłka 1X/DC p ≈ 73%:** 5/7; razem z poprzednimi weryfikacjami bez sygnału.
- **NHL Under 4,5 / NBA Under:** po kolejnej weryfikacji sprawdzić, czy ściągnięte p daje ok. oczekiwaną trafność.
- **Jakość danych:** wszystko z jednego źródła (ESPN), Ekstraklasa i CS2 z WebSearch; Alcaraz (finał Wiedeń) z ESPN bez drugiego źródła; nie rozliczono nóg spoza kuponów w analizach.

Hipotetyczny zysk tylko informacyjny (stawki w dokumentach to 0% lub ułamek %). To oszacowania, nie gwarancje; próba jest mała.
