# Kupony NBA + NHL, noc 05→06.11.2026 (v2)

Okres: noc NBA + NHL 05→06.11.2026 (czas PL, mecze 01:00-04:00 w piątek 06.11; data lokalna USA 05.11).
Kursy: Betclic.pl, pobrane 05.11 wieczorem, przed startem. gg397.bet: **niezweryfikowany** (nie udało się wyszukać meczów w interfejsie po 3 próbach). BettingPros pominięty (brak klucza).
Analizy: `analizy/Analiza_NBA_NHL_noc_2026-11-05.md`. Poziomy luzowania dozwolone przez użytkownika: 0-2 i 7.

## Skrót terminarza
13 wydarzeń: NBA 2 (PHX-ORL 03:00, GSW-MIA 04:00), NHL 11 (9 o 01:00, ANA@EDM 02:00, NSH@COL 03:30). Wszystkie analizowane, żaden nie pominięty. Inne sporty poza zakresem (decyzja użytkownika: tylko noc NBA + NHL).

## Pula nóg po wycenie z kursami Betclic (wybór)
Betclic nie oferuje puck line ani linii goli 6.5+; zwycięzca meczu i total liczą dogrywkę.
| Mecz | Rynek | p | Kurs | Fair | EV | Pewność |
|---|---|---|---|---|---|---|
| GSW-MIA | GSW ML | 70,5% | 1.52 | 1.42 | +7,2% | średnia |
| ANA@EDM | Over 5.5 | 74,0% | 1.38 | 1.35 | +2,1% | średnia (Tomkins, Brossoit) |
| GSW-MIA | GSW Over 118.5 pkt | 59% | 1.72 | 1.70 | +1,5% | niska (korelacja z GSW ML) |
| GSW-MIA | Lendeborg pkt O19.5 | ok. 54% | 1.90 | 1.85 | ok. +3% | niska (debiutant, jedno źródło) |
| WPG-VAN | Over 4.5 | 81,9% | 1.19 | 1.22 | -2,5% | średnia |
| MTL-UTA | Over 5.5 | 65,2% | 1.49 | 1.53 | -2,9% | średnia |
| NYR-PHI | Over 4.5 | 77,1% | 1.24 | 1.30 | -4,4% | średnia |
| TBL-CHI | Over 4.5 / Over 5.5 | 79% / 61,6% | 1.17 / 1.50 | 1.27 / 1.62 | -7,6% | średnia |
| NSH@COL | Over 4.5 | 78,7% | 1.18 | 1.27 | -7,1% | średnia |
| DAL-CBJ | Over 4.5 | 73,4% | 1.26 | 1.36 | -7,5% | niska-średnia |
| NJD-STL | Over 4.5 | 73,2% | 1.25 | 1.37 | -8,5% | średnia |
| CAR-NYI | Over 4.5 | 74,6% | 1.22 | 1.34 | -9,0% | średnia |
| VGK-DET | Over 4.5 | 70,6% | 1.23 | 1.42 | -13,2% | niska-średnia |
Pozostałe (moneyline faworytów, punkty zawodników 1+) mają EV od -5% do -20%: Betclic wycenia je niżej niż moje fair. Rynki zawodnika mają jedno źródło liczb i nie weszły do kuponów. P dla Over 4.5 (WPG, NYR, DAL, NSH, CAR, NJD) z `nhl_model.py` na λ z analiz.

## Kupony

### Kupon 1, poziom 0 (bazowy)
| Godz. PL | Mecz | Typ | p | Kurs Betclic | EV nogi |
|---|---|---|---|---|---|
| 04:00 (US 05.11 22:00 ET) | GSW-MIA | GSW ML (z OT) | 70,5% | 1.52 | +7,2% |
| 02:00 (US 05.11 20:00 ET) | ANA@EDM | Over 5.5 goli | 74,0% | 1.38 | +2,1% |
Łączne p 52,2% | fair 1.92 | kurs 2.10 | **EV +9,4%** | stawka Kelly 1/4: **2,1%** bankrolla (1/2: 4,3%).
Spełnia wszystkie progi bazowe. Ryzyka: Giannis (nadgarstek, niepotwierdzony): OUT podnosi p GSW (do ok. 80%), ale kurs Betclic 1.52 jest wyraźnie wyższy niż u innych (1.36-1.385), więc cena wymaga weryfikacji na gg397.bet przed grą; w ANA@EDM gra czwarty bramkarz EDM (Tomkins), Brossoit niepotwierdzony. Obie nogi mają p zbliżone do rynku, a przewaga wynika głównie z wyższej ceny Betclic, więc EV jest wrażliwe na zmianę kursu (przy GSW 1.45 i EDM 1.35 EV spada do ok. +2%).

### Kupon 2, poziom 2 (bez limitu EV, ranking po p; złamany próg EV > 0)
| Godz. PL | Mecz | Typ | p | Kurs | EV nogi |
|---|---|---|---|---|---|
| 01:00 | NYR-PHI | Over 4.5 goli | 77,1% | 1.24 | -4,4% |
| 01:00 | MTL-UTA | Over 5.5 goli | 65,2% | 1.49 | -2,9% |
p 50,3% | kurs 1.85 | **EV -7,1%** | stawka 0%.

### Kupon 3, poziom 2
| 01:00 | DAL@CBJ | Over 4.5 | 73,4% | 1.26 | -7,5% |
| 01:00 | NJD-STL | Over 4.5 | 73,2% | 1.25 | -8,5% |
p 53,7% | kurs 1.57 | **EV -15,4%** | stawka 0%. Dallas gra rezerwowym DeSmithem (Oettinger nieobecny z nieznanego powodu).

### Kupon 4, poziom 2
| 01:00 | CAR@NYI | Over 4.5 | 74,6% | 1.22 | -9,0% |
| 01:00 | VGK@DET | Over 4.5 | 70,6% | 1.23 | -13,2% |
p 52,7% | kurs 1.50 | **EV -21,0%** | stawka 0%. Niepotwierdzeni Bussi i Hart; Tarasov (.938) na małej próbie.

Więcej niż 4 kuponów nie powstaje: poziom 1 (EV ≥ -5%) nie daje żadnego (najlepsza para ma -5,2%), a przy zasadzie "jedna noga raz, jeden mecz raz" po wyczerpaniu nóg z kursem > 1.2 i p > 70% brakuje kolejnych par z p > 50% i dwiema nogami > 1.2. Poziomy 3-6 oraz tryby -1/-2 poza zgodą użytkownika.

## Poziom 7: lista 20 predykcji (kurs Betclic > 1.14, p > 60%, ranking po p; to NIE kupony, stawka 0%)
Wszystkie rynki drużynowe (rynki zawodnika odpadły: jedno źródło liczb). Pewność niska-średnia, EV poniżej zera poza oznaczonymi.
| # | Mecz | Typ | p | Kurs | EV |
|---|---|---|---|---|---|
| 1 | WPG-VAN | Over 4.5 | 81,9% | 1.19 | -2,5% |
| 2 | MTL-UTA | Over 4.5 | 81,9% | 1.16 | -5,0% |
| 3 | TBL-CHI | Over 4.5 | 79,0% | 1.17 | -7,6% |
| 4 | NSH@COL | Over 4.5 | 78,7% | 1.18 | -7,1% |
| 5 | NYR-PHI | Over 4.5 | 77,1% | 1.24 | -4,4% |
| 6 | TBL-CHI | TBL ML | 76,0% | 1.18 | -10,3% |
| 7 | CAR-NYI | Over 4.5 | 74,6% | 1.22 | -9,0% |
| 8 | ANA@EDM | Over 5.5 | 74,0% | 1.38 | +2,1% |
| 9 | DAL-CBJ | Over 4.5 | 73,4% | 1.26 | -7,5% |
| 10 | NJD-STL | Over 4.5 | 73,2% | 1.25 | -8,5% |
| 11 | VGK-DET | Over 4.5 | 70,6% | 1.23 | -13,2% |
| 12 | GSW-MIA | GSW ML | 70,5% | 1.52 | +7,2% |
| 13 | MTL-UTA | Over 5.5 | 65,2% | 1.49 | -2,9% |
| 14 | NJD-STL | NJD ML | 63,0% | 1.43 | -9,9% |
| 15 | CAR-NYI | CAR ML | 62,0% | 1.48 | -8,2% |
| 16 | NSH@COL | COL ML | 62,0% | 1.43 | -11,3% |
| 17 | WPG-VAN | WPG ML | 62,0% | 1.42 | -12,0% |
| 18 | BOS@PIT | Over 5.5 | 62,0% | 1.51 | -6,4% |
| 19 | ANA@EDM | EDM ML | 61,0% | 1.48 | -9,7% |
| 20 | TBL-CHI | Over 5.5 | 61,6% | 1.50 | -7,6% |
Na jednym wydarzeniu kilka predykcji z różnych rynków (bez sprzeczności).

## Ostrzeżenia
- Założenie niezależności meczów; nogi z jednego wieczoru NHL mają wspólny czynnik (tempo ligi, gole w pustą bramkę), p kuponów może być zawyżone.
- Nogi z niepotwierdzoną przewagą: obie nogi kuponu 1 mają p bliskie rynkowi, a EV pochodzi z ceny Betclic; **gg397.bet nie zweryfikowany**.
- Kursy mogą zmienić się do startu. Bramkarze niepotwierdzeni: Cossa, Hart/Hill, Söderblom, Hellebuyck, Merilainen, Brossoit, Saros, Bussi, Swayman. Status Giannisa i Bookera (NBA) do sprawdzenia tuż przed meczem; kontuzje skaterów NHL w większości niezweryfikowane.
- Betclic nie oferuje puck line ani totali 6.5+, więc część p z analiz (puck line, Under) nie miała jak wejść do kuponów.
- To oszacowania probabilistyczne, nie gwarancje i nie porada finansowa.
