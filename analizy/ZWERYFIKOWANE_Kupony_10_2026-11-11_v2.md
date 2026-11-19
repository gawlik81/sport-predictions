# Kupony: dziś wieczór + noc 11→12.11.2026 (czas polski), wersja v2

**Okres:** od 21:20 PL 11.11 do rana 12.11.2026.
**Kursy:** Superbet (connector `superbet-mcp`), pobrane 11.11 ok. 21:30-22:30 PL. Wyjątek: nogi CS2 mają kursy BETBOOM (fallback, Superbet nie obsługuje e-sportu), oznaczone przy nodze.
**Poziomy luzowania:** dopuszczone tylko 0-2 (wybór użytkownika).
**Analizy:** `Analiza_dnia_NBA_NHL_2026-11-11.md` (10 NBA + 6 NHL), `Analiza_CS2_BLAST_Rivals_2026-11-11.md`, `Analiza_Londrina_Nautico_Petrolero_AlwaysReady_2026-11-11.md`. Wcześniejszy plik `Kupony_10_2026-11-11.md` (tylko NBA+NHL, kursy Betclic) nie zmieniony.

## Terminarz (skrót)
- NBA: 10 meczów (01:00-04:00 PL). NHL: 6 meczów (01:00-04:00 PL). Analizy z 11.11 wieczorem, składy i bramkarze w większości niepotwierdzone.
- CS2 BLAST Rivals (Hongkong, 12.11): Legacy-Falcons 03:00, FURIA-Vitality 05:30, FUT-MOUZ 08:00.
- Piłka (po 21:20 PL): Londrina-Nautico (Brazylia, 23:00), Independiente Petrolero-Always Ready (Boliwia, 23:00). Pominięte: Fuerte San Francisco-Alianza, Real Soacha-Cartagena, ligi stanowe PE, DC Power-Brooklyn (K) (niskie ligi bez danych). Reszta piłki z 11.11 już trwa lub rozegrana.
- Pominięte: Dota 2 Asgard (tier C), LoL LCP Promotion (tier D), brak kursów Superbet i wiarygodnych danych. Tenis: ATP Stockholm i WTA Finals grają dopiero w dzień 12.11 (poza oknem nocy); API tenisowe niedostępne (konto nieopłacone). MMA: brak gal (najbliższe 21.11).

## Pula nóg po filtrach (p > 50%, fair > 1.15, kurs Superbet; wybrane)
| Mecz | Rynek | p | Kurs | EV | Uwagi |
|---|---|---|---|---|---|
| SJS-PIT | SJS +1,5 (z OT) | 69,9% | 1,49 | +4,2% | przewaga niepotwierdzona (p > rynek o 6,8 pp), bramkarze niepotw. |
| Londrina-Nautico | Under 3,5 gola | 75,0% | 1,38 | +3,5% | przewaga niepotwierdzona (p > rynek o 8 pp); Nautico 6 nieobecnych ze źródła "manual" |
| CGY-NYR | CGY +1,5 (z OT) | 71,0% | 1,44 | +2,2% | Cooley potwierdzony |
| FURIA-Vitality | FURIA +1,5 map | 65,8% | 1,55 | +2,0% | BETBOOM (fallback) |
| BUF-TBL | TBL +1,5 (z OT) | 76,3% | 1,27 | -3,1% | TBL B2B 12.11 |
| BUF-TBL | Under 7,5 goli | 70,9% | 1,37 | -2,9% | |
| TOR-BOS | BOS ML | 67% | 1,43 | -4,2% | BOS B2B, George OUT |
| ANA-NSH | ANA +1,5 (z OT) | 75,4% | 1,25 | -5,8% | |
| EDM-PHI | EDM lub remis po 60' | 72% | 1,26 | -9,3% | Vladar niepotw. |

Pozostałe nogi (spready, totale NBA, ML) mają p ≈ rynek, więc EV ≈ marża (-2 do -13%). Najlepsze single z EV > 0 poniżej progu p > 50% (poziomy -1/-2, wymagają zgody): POR-OKC OKC ML (p 54,8%, 1,87, +2,5%), HOU-GSW Under 220,5 (54,3%, 1,88, +2,1%), CLE +3,5 (51,8%, 1,97, +2,0%), GSW ML (34,5%, 3,05, +5,2%), SJS-PIT Under 6,5 (55%, 2,12, "przewaga niepotwierdzona"). Nie wchodzą do kuponów (każda z nich ma p ≤ ~55%, więc 2 nogi dają p < 50%).

## Kupony: 4 (nie 10)
Przy progach 0-2 (jeden mecz = jedna noga, brak powtórzeń meczu między kuponami) powstaje 1 kupon poziomu 0, 1 poziomu 1 i 2 poziomu 2. Nie dobijam do 10 (zasada "nie fabrykuj typu"); poziomy 3-7 nie były dopuszczone.

### Kupon 1 (poziom 0, bazowy)
| Godz. PL | Mecz | Typ | p | Kurs | EV | Źródło |
|---|---|---|---|---|---|---|
| 23:00 (11.11) | Londrina-Nautico (Serie B) | Under 3,5 gola | 75,0% | 1,38 | +3,5% | Superbet |
| 04:00 (12.11; USA 11.11 19:00 PT) | Sharks-Penguins | SJS +1,5 (z OT) | 69,9% | 1,49 | +4,2% | Superbet |
Łączne p: 52,4% | Fair: 1,91 | Kurs: 2,06 | EV: +7,8%. Stawka wg modelu: 1,8% bankrolla (1/4 Kelly). **Obie nogi mają "przewagę niepotwierdzoną"** (p modelu o 7-8 pp wyżej niż rynek bez marży). Po korekcie p do rynku + 5 pp (68,1% i 71,7%): łączne p 48,8%, EV +0,4%, stawka 0,1% bankrolla. Traktuj jako stawkę minimalną. Ryzyko: Nautico ma xG 1,4 i nie jest słabeuszem; bramkarze SJS/PIT niepotwierdzeni.

### Kupon 2 (poziom 1: EV ≥ -5%)
| Godz. PL | Mecz | Typ | p | Kurs | EV | Źródło |
|---|---|---|---|---|---|---|
| 01:00 (11.11 19:00 ET) | Sabres-Lightning | TBL +1,5 (z OT) | 76,3% | 1,27 | -3,1% | Superbet |
| 05:30 (12.11) | FURIA-Vitality (CS2 bo3, winners match) | FURIA +1,5 map | 65,8% | 1,55 | +2,0% | BETBOOM (fallback) |
Łączne p: 50,2% | Fair: 1,99 | Kurs: 1,97 | EV: -1,2% | Stawka: 0%. Złamany próg: EV > 0 (poziom 1). Ryzyko: TBL na B2B, p CS2 szacowane bez map poola (HLTV 403).

### Kupon 3 (poziom 2: bez limitu EV, ranking po p)
| Godz. PL | Mecz | Typ | p | Kurs | EV | Źródło |
|---|---|---|---|---|---|---|
| 01:30 (11.11 19:30 MT) | Flames-Rangers | CGY +1,5 (z OT) | 71,0% | 1,44 | +2,2% | Superbet |
| 03:00 | Oilers-Flyers | EDM lub remis po 60' | 72,0% | 1,26 | -9,3% | Superbet |
Łączne p: 51,1% | Fair: 1,96 | Kurs: 1,81 | EV: -7,2% | Stawka: 0%. Ryzyko: Vladar (PHI) niepotwierdzony; rynek 60' liczony osobno od moneyline.

### Kupon 4 (poziom 2)
| Godz. PL | Mecz | Typ | p | Kurs | EV | Źródło |
|---|---|---|---|---|---|---|
| 01:00 (11.11 19:00 ET) | Raptors-Celtics | BOS ML (z dogr.) | 67,0% | 1,43 | -4,2% | Superbet |
| 04:00 | Ducks-Predators | ANA +1,5 (z OT) | 75,4% | 1,25 | -5,8% | Superbet |
Łączne p: 50,5% | Fair: 1,98 | Kurs: 1,79 | EV: -9,7% | Stawka: 0%. Ryzyko: BOS na B2B (4 mecze w 6 nocy), bramkarze NSH/ANA niepotwierdzeni.

## Ostrzeżenia
- Założenie niezależności meczów; kursy mogą się zmienić do startu; składy NBA (injury report ok. 90 min przed) i bramkarze NHL do potwierdzenia.
- Prawie wszystkie p to oszacowania zakotwiczone w rynku (brak przewagi); kupony 2-4 mają EV ujemne i stawkę 0%, kupon 1 ma przewagę niepotwierdzoną.
- Kurs CS2 jest z BETBOOM, nie z Superbet; HLTV/Liquipedia niedostępne (403), p per mapa szacowane. Wynik G2-MOUZ z 11.11 niepewny w źródłach.
- Rynków zawodnika nie wyceniano (brak potwierdzonych składów); zbiórki/asysty/trójki NBA nie pobrano z Superbet.
- To oszacowania probabilistyczne, nie gwarancje i nie porada finansowa.
