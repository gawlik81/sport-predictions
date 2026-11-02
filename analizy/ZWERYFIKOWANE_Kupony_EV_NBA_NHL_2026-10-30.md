# NBA i NHL, 30-31.10.2026: poziomy -1 (tryb EV) i -2 (single EV)

Powtórny przegląd na prośbę użytkownika (zgoda na poziomy -1 i -2 udzielona w zapytaniu). Kursy: **Betclic.pl, pobrane 30.10 ok. 07:00**; gg397.bet nie dał weryfikacji (brak kursów NBA na stronie turnieju, brak totali drużyn). **Linemate nie został użyty:** `linemate-picks` wymaga Chrome z zalogowaną sesją, a połączenie z przeglądarką było rozłączone.

## Co zmieniło się po przeglądzie

Betclic nie ma totali meczu NBA na liniach z analizy, ale ma **totale drużyn**. Przeliczyłem p dla linii Betclic (rozkład normalny wokół mojej średniej wyniku drużyny z `Analiza_NBA_2026-10-30.md`, odchylenie 11,2 pkt, wyprowadzone z p w analizie; to przybliżenie, nie wynik skryptu `nba_model.py`).

| Noga (Betclic) | Termin PL | Średnia modelu | p modelu | p rynku bez marży | Różnica | Kurs | EV (p modelu) | p po korekcie (rynek +5 pp) | EV po korekcie |
|---|---|---|---|---|---|---|---|---|---|
| Orlando total drużyny Under 110,5 (TOR-ORL) | sob 00:30 | 108 | 58,8% | 49,6% | +9,2 pp | 1,85 | +8,8% | 54,6% | +1,0% |
| Miami total drużyny Under 122,5 (MIA-IND) | sob 01:00 | 119,5 | 60,6% | 51,2% | +9,3 pp | 1,79 | +8,4% | 56,2% | +0,6% |
| Charlotte total drużyny Under 110,5 (WAS-CHA) | sob 00:00 | 107,5 | 60,6% | 51,5% | +9,1 pp | 1,78 | +7,9% | 56,5% | +0,6% |
| Minnesota total drużyny Under 114,5 (MIN-LAC) | sob 01:00 | 112,5 | 57,1% | 49,0% | +8,0 pp | 1,87 | +6,8% | 54,0% | +1,0% |
| Golden State total drużyny Under 116,5 (GSW-LAL) | sob 03:00 | 114 | 58,8% | 50,7% | +8,2 pp | 1,81 | +6,4% | 55,7% | +0,8% |
| Phoenix total drużyny Under 113,5 (PHX-DEN) | sob 03:00 | 112 | 55,3% | 49,9% | +5,5 pp | 1,84 | +1,8% | 54,9% | +0,9% |
| Winnipeg wygra po 60' (FLA-WPG) | sob 00:00 | - | 29,5% | ok. 26% | +3,5 pp | 3,63 | +7,1% | 29,5% | +7,1% |

Pominięte: LAC U108,5 i DEN U117,5 (ten sam mecz co MIN i PHX, jeden mecz = jedna noga), CHI U109,5 i TOR U115,5 (EV ≈ +0,2%), Under totali meczu (Betclic ma tylko okno niższych linii, p dla niego nie jest przeliczone), BOS-CHI Under 6,5 (Betclic nie wystawił meczu; kurs BettingPros 1,82 nie jest kursem Betclic, a gg397.bet nie było sprawdzone), rynki zawodnika (Betclic ich nie ma).

**Wszystkie nogi NBA to "przewaga niepotwierdzona":** moje p jest o 5-9 pp wyższe od rynku, a każda ze średnich jest 2-3,5 pkt poniżej linii rynku. To systematyczne przesunięcie modelu (próba 3-6 meczów na drużynę), nie osobne sygnały. Po ściągnięciu p do rynku +5 pp (zasada skilla) EV spada z +6...+9% do ok. **+1%**, czyli praktycznie zera. Stawki liczę z p po korekcie.

Noga NHL (WPG 60') zależy od niepotwierdzonego bramkarza, a Winnipeg gra drugi dzień z rzędu na Florydzie. Pozostałe mecze NHL: Betclic ma tylko VGK-NJ, FLA-WPG i CGY-SEA, wszystkie ML/spread/60' z EV < 0 poza WPG 60' (WPG ML z dogrywką: 2,60, EV +1,4%, ten sam mecz).

## Poziom -1 (EV zestawu > 0 i każdej nogi; bez progów p i kursu; stawka 1/4 Kelly z p po korekcie)

| Kupon | Nogi | Łączne p (model / po korekcie) | Kurs | EV (model / po korekcie) | Stawka |
|---|---|---|---|---|---|
| -1/A | Orlando U110,5 (1,85) + Miami U122,5 (1,79) | 35,6% / 30,7% | 3,31 | +18,0% / +1,6% | 0,2% |
| -1/B | Charlotte U110,5 (1,78) + Minnesota U114,5 (1,87) | 34,6% / 30,5% | 3,33 | +15,2% / +1,6% | 0,2% |
| -1/C | Golden State U116,5 (1,81) + Winnipeg 60' (3,63) | 17,3% / 16,4% | 6,57 | +14,0% / +8,0% | 0,4% |

Łączne p wszystkich trzech jest **poniżej 50%** (wariancja wysoka), a nogi A i B pochodzą z tego samego przesunięcia modelu, więc nie są niezależnymi dowodami. Phoenix U113,5 zostaje bez pary (wejdzie tylko jako single).

## Poziom -2 (single EV; ten sam zestaw nóg co powyżej, nie do gry razem z kuponami -1)

Ranking po EV; stawka 1/4 Kelly z p po korekcie.

| # | Noga | Kurs | p (model / po korekcie) | EV (model / po korekcie) | Stawka |
|---|---|---|---|---|---|
| 1 | Orlando total drużyny Under 110,5 | 1,85 | 58,8% / 54,6% | +8,8% / +1,0% | 0,3% |
| 2 | Miami total drużyny Under 122,5 | 1,79 | 60,6% / 56,2% | +8,4% / +0,6% | 0,2% |
| 3 | Charlotte total drużyny Under 110,5 | 1,78 | 60,6% / 56,5% | +7,9% / +0,6% | 0,2% |
| 4 | Winnipeg wygra po 60' (FLA-WPG, po bramkarzu) | 3,63 | 29,5% / 29,5% | +7,1% / +7,1% | 0,7% |
| 5 | Minnesota total drużyny Under 114,5 | 1,87 | 57,1% / 54,0% | +6,8% / +1,0% | 0,3% |
| 6 | Golden State total drużyny Under 116,5 | 1,81 | 58,8% / 55,7% | +6,4% / +0,8% | 0,3% |
| 7 | Phoenix total drużyny Under 113,5 | 1,84 | 55,3% / 54,9% | +1,8% / +0,9% | 0,3% |

## Ostrzeżenia

- Tryb EV nie podnosi jakości: EV +6...+9% bierze się z tego, że moje średnie leżą poniżej linii Betclic w każdym meczu. Po korekcie wszystkie nogi NBA mają EV ≈ +1%, w granicy błędu. Weryfikacja 26-28.10: 17 nóg "przewaga niepotwierdzona" trafiło 9 (53%) przy średnim p modelu ok. 65%.
- Statusy NBA (DTD) pochodzą z ESPN/Rotowire, nie z oficjalnego raportu; kluczowe: Minnesota bez Edwardsa i Clippers bez Beala, Ingrama i Strusa (rynek już to wycenił), Hornets bez Knueppela, White'a, G. Williamsa, Boswella (Schröder DTD). Przed meczem sprawdź injury report; zmiana składu zmienia total drużyny najbardziej.
- Kursy z godz. 07:00 mogą się zmienić; dodatkowa linia z innymi kursami zmienia EV.
- Nie sprawdzono na gg397.bet; kursów z DK/Pinnacle/BettingPros nie użyto jako kursów Betclic.
- Oszacowania probabilistyczne, nie gwarancje; stawki to sugestia wielkości, nie porada finansowa.

## Dodatek po sprawdzeniu Linemate (30.10)

Linemate (patrz `Linemate_NBA_NHL_2026-10-30.md`) nie dodał żadnej nogi z kursem Betclic ani gg397.bet i bez własnego p. Zestawy -1/A-C i single -2 powyżej pozostają bez zmian.

Jedyne dodatkowe nogi to dwa rynki zawodnika z analizy NBA z linią **BettingPros** (kurs -115 = 1,87, książka nieustalona, **nie Betclic**; Betclic nie ma rynków zawodnika, gg397.bet niesprawdzony). Wchodzą tylko do poziomu -1/-2, "po składach", niska pewność, "przewaga niepotwierdzona" (p modelu o ok. 10 pp wyższe od rynku 50%):

| Noga | Termin PL | p modelu | p po korekcie (rynek +5 pp) | Kurs | EV (model / po korekcie) | Stawka (¼ Kelly, p po korekcie) |
|---|---|---|---|---|---|---|
| Towns (NYK) PRA Over 34,5 | sob 00:30 | 61% | 55% | 1,87 (BettingPros) | +14,1% / +2,9% | 0,8% |
| Tatum (BOS) PRA Under 43,5 | sob 00:30 | 60% | 55% | 1,87 (BettingPros) | +12,2% / +2,9% | 0,8% |
| Kupon -1/D: obie nogi | | 36,6% / 30,3% | | 3,50 | +28,0% / +5,8% | 0,6% |

Ryzyka: Tatum Under zależy od blowoutu przy spreadzie 15,5 (jeśli mecz jest wyrównany do 3. kwarty, odpada); Towns bez ryzyka blowoutu, ale 76ers mają Browna DTD (zmiana spreadu o 2-3 pkt). Rynki zawodnika wymagają potwierdzonego składu i injury reportu przed meczem.
