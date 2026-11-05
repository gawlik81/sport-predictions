# Weryfikacja kuponów z 02.11 i 03.11.2026 (piłka, NBA, NHL, tenis, CS2)

**Zweryfikowane pliki:** `ZWERYFIKOWANE_Kupony_10_2026-11-02.md` (kupony A-F z pkt 7, pula EV z pkt 3 i kupon trybu -1; **częściowo**), `Kupony_10_2026-11-03.md` (lista 20 predykcji poziomu 7; **częściowo**), `Kupony_10_2026-11-03_v2.md` (NHL, noc 03→04.11: kupony 1-6 i lista 17 pojedynczych; **w całości**, po zmianie nazwy `ZWERYFIKOWANE_`).
**Nie oznaczone:** `ZWERYFIKOWANE_Kupony_10_2026-11-02.md` (brak wyników Ekstraklasy: Zagłębie - Korona, Radomiak - Śląsk, Raków - Pogoń; flashscore/sofascore nie zwracają listy meczów, WebSearch bez wyników) i `Kupony_10_2026-11-03.md` (brak noga #19 Kouamé - Davidovich Fokina; uzupełnione 05.11: mecz nie istnieje, plik oznaczony `ZWERYFIKOWANE_`). Pliki `Analiza_*` z 02-03.11 nie były rozliczane (tylko nogi kuponów).
**Źródła wyników:** ESPN scoreboard (piłka LM/PL/LaLiga/Serie A/Ligue 1, NBA, NHL, tenis; jedno źródło), CS2 IEM Beijing z esports.ru (jedno źródło; HLTV i Liquipedia 403). Piłka po 90 minutach, NHL moneyline i puck line z dogrywką/karnymi, total NHL bez karnych.
**Uwaga o danych:** w ESPN (ATP Paryż 03.11) Kouamé zagrał z Borgesem (0-2, 3-6 1-6), a nie z Davidovichem Fokiną. Możliwy błąd danych wejściowych w analizie tenisowej (zły rywal lub runda); nogi nie rozliczono, ale należy sprawdzić źródło terminarza.

## Wyniki
- **02.11:** Newcastle 0-1 Everton, Deportivo 2-1 Osasuna, Sassuolo 2-4 Fiorentina, Atalanta 0-3 Parma, Lorient 0-2 Brest; NBA: Mavericks 100-115 Kings, Timberwolves 112-100 Bucks, 76ers 126-107 Bulls, Magic 94-103 Wizards, Grizzlies 134-135 Pelicans (dogr.); NHL: Blackhawks 2-5 Avalanche.
- **03.11 (LM):** Galatasaray 2-0 Stuttgart, Szachtar 0-1 Sporting, Atlético 0-2 Bayern, Barcelona 3-0 Villa, Bodø/Glimt 0-0 Lille, Feyenoord 0-3 Inter, LASK 4-0 Slovan, Man Utd 3-2 Roma, Villarreal 0-6 PSG. Tenis: Fritz - Bonzi 3-6 6-3 6-4, Valentova - Sakatsume 6-3 7-5, Joint - Inglis 7-5 6-2. CS2: B8 2-1 Legacy, MongolZ 2-0 HEROIC, FURIA 2-1 NAVI (3 mapy), Falcons 2-1 FaZe.
- **NHL 03.11:** Rangers 3-1 Blues, Devils 4-3 Oilers (karne), Canucks 4-5 Ducks, Capitals 5-6 Stars, Predators 4-1 Hurricanes, Penguins 2-3 Golden Knights, Flyers 2-4 Wild, Blue Jackets 7-2 Avalanche, Canadiens 4-5 Jets (dogr.), Maple Leafs 2-3 Utah, Lightning 4-2 Red Wings.

## Bilans (skrypt `verify.py`, 47 jednostek, 2 nierozliczone)
| | Trafione | Oczekiwane |
|---|---|---|
| Wszystkie jednostki | 31/47 | 31,4 (-0,12 odch.) |
| Lista 03.11 (poziom 7), 19 rozliczonych | 17/19 | 13,8 |
| NHL v2, kupony 1-6 | 3/6 | 3,04 |
| NHL v2, 17 pojedynczych | 10/17 | 11,7 |
| 02.11 kupony A-F (C nierozliczony) | 1/5 | 2,69 |
| 02.11 pula EV (singles + kupon -1) | 3/6 | 2,97 |

**Lista 03.11:** pudła tylko #5 HEROIC +1.5 (MongolZ 2-0) i #14 Szachtar - Sporting Over 1.5 (0-1). Piłka DC 8/8 (oczekiwane 5,9), tenis 3/3.
**NHL v2:** kupon 1 (jedyny z EV +9,3%, stawka 2,0%) przegrał nogą STL +1.5 (Blues 1-3, różnica 2); kupony 2-4 trafione (puck line +1.5), kupony 5-6 przegrane przez Carolinę. Hipotetyczny zysk skryptu (stawka 1 na kupon NHL): -0,41; tylko informacja.
**02.11:** A Atalanta 1X (Parma 3-0) i Newcastle 1X (0-1) przegrane, B Mavericks (p 77%) przegrane, D Mavericks przegrane, E Sassuolo O1.5 + Avalanche trafiony, F Grizzlies przegrani (134-135 po dogr.). Kupon C (Radomiak 1X + 76ers ML trafiony) czeka na wynik Radomiak - Śląsk. Pula EV: Newcastle U2.5, Lorient U2.5, Magic U113.5 trafione; 76ers U125.5 (126 pkt) i Deportivo U2.5 (3 gole) przegrane; kupon -1 (4 nogi) przegrany przez 76ers.

## Analiza pomyłek
- **Mavericks ML p 77% (02.11), 100-115:** dokument wskazywał ryzyko Irvinga (Q) i wycenił p wyżej niż kurs sugerował (fair 1.30 vs rynek 1.22). Jedna noga, ryzyko opisane, ale p nie zostało obniżone. **Obserwacja, nie podstawa do zmiany.**
- **Carolina w NHL v2 (CAR +1.5, CAR ML, CAR team total Over 2.5, 1-4 w Nashville):** trzy nogi z jednego meczu p 63-81%; ostrzeżenie "Kochetkov niepotwierdzony" było w dokumencie, ale p nie zostało skorygowane; dodatkowo kupony 5 i 6 powtarzały mecz (kupon 6 poziomu 6 celowo). Skorelowane nogi to jedno zdarzenie. **Wariancja z elementem korelacji (kupon 6 zgodny z regułami poziomu 6).**
- **NHL Over/Under/ML/TT ("NHL inne"), 2/7 przy p 56-69%:** UTA O5.5 (5 goli), VGK O5.5 (5), DAL U6.5 (11), CAR TT, CAR ML (trafione: TBL ML, MIN ML). Przy próbie 7 nóg i zgodnym z poprzednią weryfikacją trendzie (Under 4,5 0/8 z 29-30.10) to **kolejna obserwacja p modelu wyżej niż rynek w NHL totals**, ale kierunki są mieszane (Over i Under), więc nie sygnał jednostronny.
- **Szachtar - Sporting Over 1.5 (p 70,2%), 0-1:** wariancja (kurs 1.20; fair 1.42, mecz zamknięty).
- **HEROIC +1.5 (p 76%), 0-2:** wariancja w bo3 przy niskiej pewności (analiza oznaczona "niska"; p wynikało z priora 50/50, dokument sam to ostrzegał przy Dota 2/LoL). Pojedyncze pudło.
- **STL +1.5 (p 74%, kupon 1 NHL), 1-3:** wariancja; dokument oznaczał "przewaga niepotwierdzona +5,2 pp nad rynkiem", a stawka 2,0% (1/4 Kelly) była liczona z p modelu, nie z p rynku + 5 pp. **Do obserwacji: wcześniejsza weryfikacja (01.11) wprowadziła ściąganie p do rynku +5 pp w trybie EV, w kuponach poziomu 0 NHL tego nie zastosowano.**
- **Kupony 02.11 A, D, F:** nogi niskiej pewności lub ryzyka (Mavs, Grizzlies Pippen doubtful) w zestawach z EV < 0 i stawką 0%; skutki zerowe.
- **Wykluczenia:** NHL Over 5.5 (COL@CBJ 9 goli, ANA@VAN Over 6.5, 9 goli) trafiały z puli EV < 0; Barcelona O2.5 trafiona; brak sygnału błędnych wykluczeń.

## Co zadziałało
- Piłka DC na LM 8/8 (p 68-78%), piłka 1X2 2/2, tenis zwycięzca 3/3 (p 69-71%).
- Puck line +1.5 w NHL: 8/10 (oczekiwane 7,4); kupony 2-4 NHL trafione.
- Pula EV 02.11: 3/6, zgodnie z oczekiwanym 2,97 (nogi "przewaga niepotwierdzona" nie odstawały od p).

## Kalibracja skilli
**Bez zmian.** Pudła to wariancja lub pojedyncze przypadki; jedyna ewentualna luka procesowa (stawka kuponu 1 NHL z p modelu mimo "przewagi niepotwierdzonej") jest pojedynczym przypadkiem i dotyczy reguły wprowadzonej dopiero 02.11 dla trybu EV.

## Do obserwacji
- **Kupon NHL poziomu 0 ze stawką liczoną z p modelu przy przewadze nad rynkiem > 5 pp:** 1 przypadek (kupon 1, stawka 2,0%, przegrany). Warunek zmiany: drugi taki przypadek → `bet-slip-builder`: stawka z p rynku + 5 pp także na poziomie 0.
- **NHL totals (Over/Under) przy p > rynek:** 29-30.10 Under 4,5 0/8, 03.11 Over/Under 0/3 (UTA O5.5, VGK O5.5, DAL U6.5). Warunek: kolejna seria < 40% przy ~10 nogach → zwiększyć ściągnięcie p do rynku w `nhl-analyst` także dla Over.
- **Nogi z jednego meczu w wielu kuponach (CAR):** korelacja, nie zmieniać reguł poziomów.
- **Dane:** wyniki z jednego źródła (ESPN; CS2 esports.ru); Ekstraklasa 02.11 i Kouamé - Davidovich Fokina do uzupełnienia; sprawdzić poprawność rywala Kouamé w terminarzu.

Hipotetyczny zysk tylko informacyjny (stawki 0% lub ułamek %). To oszacowania, nie gwarancje; próba jest mała.
