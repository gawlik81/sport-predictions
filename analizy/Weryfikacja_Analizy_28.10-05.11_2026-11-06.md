# Weryfikacja zbiorcza analiz z 28.10-05.11.2026 (hipotetyczne rozliczenie głównych typów)

**Zakres:** pliki `Analiza_*` i `Linemate_*` z `analizy/` bez prefiksu `ZWERYFIKOWANE_` (kupony i listy z tych dni były rozliczone wcześniej). Dla każdego meczu rozliczono **jeden główny typ dokumentu** (linia "Typ:" albo rynek z najwyższym p przy fair > 1,15; przy "brak mocnego typu" rynek wskazany jako najlepszy, oznaczony w grupie). Pominięto rożne, kartki, faule; rynki zawodnika tylko z Linemate (p z dokumentu). To **nie są rekomendacje**: typy "bez mocnego typu" i picki Linemate nie wchodziły do kuponów. Kursów w większości brak, więc **bez rachunku zysku**. Zbierało 6 subagentów (po jednej grupie dat), liczenie `verify.py`, p z dokumentów nie poprawiano.
**Źródła wyników:** ESPN scoreboard i boxscore (piłka, NBA, NHL, ATP/WTA; jedno źródło), NHL API (krzyżowo), WebSearch/Wikipedia (MMA, e-sport, Puchar Polski; zwykle 2+ źródła), `Weryfikacja_Uzupelnienie_Ekstraklasa_LAC-MIA_2026-11-05.md` (Ekstraklasa 02.11).

## Bilans
| Dzień (czas PL) | Nogi rozliczone | Trafione | Oczekiwane |
|---|---|---|---|
| 28.10 | 89* | 57 | 57,05 |
| 29.10 (noc NBA/NHL = US 29.10) | 38 | 24 | 22,91 |
| 30-31.10 | 86 | 55 | 60,55 (-1,36 odch.) |
| 01.11 | 43 | 32 | 29,85 |
| 02-03.11 | 105 | 73 | 68,5 |
| 04-05.11 (poza kuponami i listami) | 138 | 93 | 93,28 |
| **Razem** | **499** | **334** | **332,1** |

*Osaka - Pohankova (p 72%) agent zostawił jako nierozliczoną ("przełożona"), ale ESPN pokazuje mecz z 29.10 (Pohankova 6-3 7-5, jedno źródło), więc doliczyłem go jako pudło; agent miał 57/88 przy 56,33.
Pasma p (wszystkie dni): **70-80%: 102/124 (82%) przy ok. 92,5 oczekiwanych (+1,9 odch.)**; 80-100%: 55/71 przy 59,6, ale ta różnica to prawie wyłącznie Linemate. 50-70%: zgodne z p. Kalibracja całości dobra, bez nadwyżki ponad wariancję.

Wyniki per grupa (najciekawsze, trafione/oczekiwane):
- **Piłka DC/wynik:** 28.10 DC 6/6 (4,6), 30.10 4/5, 01.11 5/5 (3,73), 02-03.11 4/5; 05.11 wybrana lista 13/13, ale **cały zbiór 05.11 (wynik/DC, 26 nóg): 16/26 przy 18,9 (-1,31 odch.)**.
- **Piłka gole (Over/Under):** 05.11 23/28 (20,5), 01.11 Over 3/4, 30.10 Over/Under 5/6, 28.10 Over 2/2, Under 1/1; bez zauważalnego odchylenia.
- **Tenis zwycięzca:** 28.10 **6/14 (9,25; -1,85)**, 30.10 5/5 (3,51), 02-03.11 24/34 (22,0), 04.11 3/8 (4,99), 05.11 4/7 (4,4). Razem ok. 42/68 przy ok. 44.
- **NBA ML:** 29.10 1/1+, 30.10 2/5 (3,25; pudła w jednym wieczorze), 01.11 3/4, 02-03.11 7/9, 04-05.11 w normie.
- **NHL ML/puck line/total:** puck line +1,5 05.11 14/16 (11,3), 04.11 trend nad p; ML i total bez przewagi; total 02-03.11 1/3.
- **MMA (30.10):** 8/10 (6,84).
- **E-sport:** serie z p ≥ 62%: 8/9 (02-03.11), 12/17 (28.10), LoL DK-BLG 4/8 (4,5), TES-BLG 0/1; **"bez mocnego typu": 3/9 (28.10), 2/8 (02-03.11), 1/4 (30.10)**, ale w tych meczach agent wybierał stronę po kolejności wymienienia, więc to nie jest ocena modelu.
- **Linemate (hit rate / p_adj):** 29.10 12/20 (12,0), **30.10 4/11 (9,93; -6,3 odch.)**, 01.11 11/15 (10,43). Razem **27/46 przy ok. 32,4**.

## Analiza pomyłek
**Błąd procesu (konkretny, nie wariancja):**
- **Linemate: p z hit rate wyższe od rynku o +13 do +25 pp.** Sabonis double-double (p 85%, rynek 62%, 5/5 na 4 meczach, dokument sam napisał "kurs podejrzanie wysoki, zweryfikować"), Fehervary Over 1,5 bloków (68% vs 55%), Nembhard Under 19,5 (69% vs 51%), Fox Over 0,5 pkt (82% vs 58%), z 30.10 Coronato, Hischier, B. Tkachuk, Connor, Diabate, Hart (hit rate 5/5-9/12, wszystkie pudła). Reguła 1a w `linemate-picks` już mówi, że p_adj zawyża (efekt selekcji), ale nie podawała liczby, a dokumenty trzymały p_adj blisko 100%. Picki Linemate nie wchodziły do kuponów (reguła "bez pełnej analizy nie wchodzi"), więc skutek to tylko zaniżony bilans hipotetyczny.
- **Terminarz: pary spoza rzeczywistości.** 02-03.11 cztery pary tenisowe nie odbyły się (Merida-Blockx, Kouamé-Davidovich Fokina, Tien-Tsitsipas, Eala-Parks; w ESPN inni rywale), Osaka-Pohankova przełożona, pary 13. kolejki Ekstraklasy z 30.10 niezgodne z soccerway, CS2 NAVI-Falcons podane na 04.11, a wg esports.ru grane 02.11; Zenith-Direborn (Dota) bez śladu. Pięć niezależnych przypadków z różnych dni, źródło: kursy Pinnacle/agregatory bez drugiego potwierdzenia.
- **Borges-Struff Over 21,5 gemów (76,7%, 17 gemów):** p z p_serve z 10 meczów bez linii rynku, ale agent oceniał to jako umiarkowany błąd; jednostkowy przypadek (tenis total bez rynku już ma regułę), bez zmiany.
- **Hope-Marshall (30.10):** zawodnik nie zrobił wagi (catchweight 148), informacja dostępna przed walką; wpływ na p nieustalony, jednostkowe.
- **Medvedev 81% po wolnym losie (04.11):** zgodnie z wzorcem z 05.11; reguła 6-8 pp jest nowsza niż ten mecz.
**Wariancja:** pozostałe pudła z p ≥ 65% (Mensik, Hurkacz, Nakashima, Yastremska, Atalanta 1X, Milan 1X, Leverkusen, Sturm, Sunderland, Getafe U3,5, TOR/DAL ML 30.10, DAL ML 02.11, MEM ML 02.11, FLA +1,5, STL +1,5, Liquid/Vitality w e-sporcie i inne): p ≈ rynek lub poniżej, bez pominiętego sygnału. Agenci wskazali jedynie luki w zakresie reguł (Yastremska: reguła kwalifikanta dotyczy tylko WTA 1000/R2 i p ≥ 75%) - jednostkowe.

## Co zadziałało
- Piłka DC/gole: łącznie ok. 85-90% trafień przy p 70-80% w typach głównych, mimo pudeł faworytów u siebie 05.11.
- MMA 8/10, NHL puck line +1,5 (14/16 05.11), tenis p ≥ 70% zgodny z p.
- Wykluczenia z kuponów rynków zawodnika i Linemate (bez pełnej analizy) były słuszne: to dokładnie te nogi, które zaniżają bilans.
- Dokumenty same oznaczały ryzyko (np. Sabonis, Nembhard "ryzyko wyższych minut", p_adj "zawyża o kilkanaście pp").

## Kalibracja skilli
- **`sports-fixtures-finder`:** dopisano regułę: parę tenisową i mecz ligi krajowej potwierdzić w drugim źródle w dniu meczu (ESPN scoreboard/order of play, strona ligi wg daty); para tylko z kursów lub jednego agregatora to "do potwierdzenia" (5 przypadków 28.10-04.11).
- **`linemate-picks` (pkt 1a):** własne p oparte wyłącznie na hit rate nie wyżej niż `p_kurs + 10 pp`; w nawiasie liczby (27/46 przy ok. 32, 30.10 4/11) i przykłady.
- Pozostałe skille: **bez zmian**, bo odchylenia poza Linemate mieszczą się w wariancji lub mają tylko jednostkowy przypadek.

## Do obserwacji
- **Piłka DC/1X2 faworyta:** hipoteza "reguły zbyt ostrożne" (DC 13/13 z listy 05.11) **wycofana**: pełny zbiór 05.11 wypadł 16/26 przy 18,9; dla samych wybranych list i typów głównych 28.10-02.11 wynik wyższy, więc razem w normie. Warunek: ocenić po następnej pełnej kolejce pucharowej bez selekcji.
- **Tenis 28.10 (6/14) i faworyt z mniejszym obciążeniem:** pudła, w których wygrywał zawodnik z większą liczbą meczów w tygodniu (Mannarino, Rune, Joint, Dart, Borges); razem z wzorcem R2 po wolnym losie. Warunek: kolejne 4+ takich pudeł → reguła "zmęczenie vs forma" do korekty.
- **E-sport "seria bez mocnego typu" (CCT tier D, p 53-62%):** 1/6 w CCT 28.10, 2/8 w 02-03.11; próba nie mierzy modelu (losowa strona), ale p 53-62% na cienkich danych nie ma przewagi - w analizach e-sportowych unikać typu przy braku kursu i danych.
- **Terminarz:** po zmianie reguły sprawdzić, czy liczba nieistniejących par spada.
- **Dane:** wyniki z jednego źródła (ESPN); nierozliczone: 6 meczów Ekstraklasy z 30.10 (Cracovia-Motor, Górnik-Legia, Płock-Piast, Wieczysta-Jagiellonia, Lech-Wisła, GKS-Widzew; brak źródła), 5 meczów CS2 z 04.11 (MongolZ-FURIA, NAVI-Falcons, Yellow Submarine-NAVI, OG-GL, Zenith-Cloud Dawning), TES-IG (LoL QF, 03.11), Zenith-Direborn, ESEA Morrow-VIT.A (walkower), D. White Under 1,5 ast w 1. kwarcie (brak podziału kwart). Brak potwierdzenia dla pojedynczych nóg nie wpływa na bilans.

## Pliki
Oznaczone `ZWERYFIKOWANE_` (wszystkie mecze rozstrzygnięte lub nierozliczone z udokumentowanej przyczyny: nieistniejąca para, krecz, nie grał): analizy z 28.10, 29.10, 30.10 (poza `Analiza_pilka_cz2_2026-10-30.md`), 01.11, 02.11, `Analiza_pilka_LM_2026-11-03.md`, `Analiza_NHL_2026-11-03.md`, tenis 03.11, `Analiza_dnia_2026-11-04_v2.md`, `Analiza_dnia_2026-11-05.md`, `Analiza_NBA_NHL_noc_2026-11-05.md` i pliki `Linemate_*` / `Analiza_Linemate_*`. **Nie oznaczone** (brakuje wyników): `Analiza_pilka_cz2_2026-10-30.md` (Ekstraklasa), `Analiza_dnia_2026-11-04.md` (CS2 04.11), `Analiza_esport_2026-11-03.md` i `Analiza_esport_Dota_LoL_2026-11-03.md` (TES-IG). `Terminarz_*` i `Kursy_Betclic_*` to dane wejściowe, bez prefiksu.

To oszacowania, nie gwarancje; próba jest mała, a wybór "głównego typu" to interpretacja agentów.
