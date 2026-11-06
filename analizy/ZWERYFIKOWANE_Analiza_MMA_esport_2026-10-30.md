# Analiza MMA (UFC Fight Night: Moicano vs. Nolan) i e-sport (CS2 PGL Bucharest, LoL Worlds) - 30-31.10.2026

Dane z 30.10.2026. Czasy w czasie polskim (CET, UTC+1; od 25.10 w Europie czas zimowy, w USA nadal letni). Kursy referencyjne: Pinnacle (przez MCP `sportsdata`, kursy amerykańskie przeliczone na dziesiętne, marża zdjęta proporcjonalnie). Kursów Betclic/gg397.bet nie pobierano, więc EV względem polskiego bukmachera nie jest policzone. Fair odds = 1/p.

## CZĘŚĆ A. MMA: UFC Fight Night (UFC Vegas 123), Meta APEX, Las Vegas

### Weryfikacja karty
- Karta zgadza się z zapytaniem; potwierdzona przez Wikipedię, ufcalendar i listę Pinnacle (12 walk). Brak tytułu stawki; tylko main event ma 5 rund (ufcalendar), reszta 3 rundy (domyślnie, UFC nie podaje wprost).
- Zmiany: Brown - Smith (Leal wypadł, kontuzja; Smith z krótkim terminem), Marshall - Hope (Bolaños wypadł, rozcięcie oka; Hope zastępca), Osbourne - Durden i Reese - Gall dodane 23.10 (Osbourne wypadł wcześniej z UFC 329 z nieujawnioną kontuzją). Bekoev - Petroski usunięta (Bekoev: nagły przypadek medyczny); Petroski walczy 7.11.
- Godziny PL: prelims sob 31.10 22:00; main card nd 01.11 01:00; main event ok. 03:00 (Pinnacle szacuje start ME ok. 03:15 PL).
- Ważenie (pt 30.10 po południu czasu USA) jeszcze się nie odbyło w chwili researchu: brak komunikatu o przekroczeniu limitu. Przed obstawianiem sprawdzić oficjalne wyniki ważenia i ewentualne zmiany.
- Statystyki kariery: serwer `ufc_*` zwrócił stronę bot-challenge. Dane o zawodnikach tylko częściowe (AgentMMA, mmasucka, ufcalendar); brak SLpM/obalenia dla większości. Dlatego p dla większości walk opiera się na rynku (Pinnacle po zdjęciu marży) z korektami z dostępnych informacji, a pewność jest niska/średnia. Kalshi/Polymarket i BettingPros nie użyte.

### Wyniki modelu (`mma_model.py`) i p końcowe

Wejście do skryptu: fa, fb = P(finisz wygranej A/B), da = P(A na punkty | dystans). Parametr `--w 1.3,1,0.8` (więcej finiszów w R1).

| Walka (kategoria, rundy, godz. PL) | Typ / rynek | p | Fair | Rynek (Pinnacle, bez marży) | Pewność |
|---|---|---|---|---|---|
| Moicano - Nolan (LW, 5R, ~03:00 nd) | Moicano wygra | 51% | 1.96 | 54% (Nolan 46%); DK z 25.10 miał Nolana -115 | niska |
| | Nolan wygra | 48% | 2.08 | | niska |
| | Dystans (5R) | 60% | 1.67 | brak wiarygodnej linii | niska |
| | Over 1.5 rundy | 70% | 1.43 | 64% (linia 1.5 w walce 5R podejrzana) | niska |
| Brown - Smith (WW, 3R) | Smith wygra | 68% | 1.47 | 70% | średnia |
| | Smith KO/TKO | 31% | 3.25 | brak | niska |
| | Walka na dystans | 46% | 2.17 | ok. 50% | niska |
| Osbourne - Durden (FLW, 3R) | Durden wygra | 52% | 1.92 | 52% | niska (Osbourne po kontuzji) |
| Yana Santos - Luana Santos (WBW, 3R) | Luana Santos wygra | 71% | 1.41 | 73% | średnia |
| | Dystans | 76% | 1.32 | 74% (Over 2.5) | średnia |
| Lebosnoyani - Hasanov (WW, 3R) | Lebosnoyani wygra | 68% | 1.47 | 70% | niska (Hasanov 5-0, poziom nieznany) |
| | Dystans | 46% | 2.17 | 44% | niska |
| Hope - Marshall (FW, 3R, zastępca Hope) | Marshall wygra | 65% | 1.54 | 66% | niska |
| Berggren - Sezinando (WW, 3R) | Sezinando wygra | 61% | 1.64 | 62% | niska |
| Erosa - Lee (FW, 3R) | Lee wygra | 57% | 1.75 | 58% | niska |
| Gall - Reese (MW, 3R) | Reese wygra | 74% | 1.35 | 76% | niska-średnia |
| | Reese przez finisz | 44% | 2.27 | brak | niska |
| Kropschot - Klein (MW, 3R) | Kropschot wygra | 71% | 1.41 | 73% | niska |
| Rodriguez - Alencar (WSW, 3R) | Rodriguez wygra | 69% | 1.45 | 70% | niska |
| | Dystans | 75% | 1.33 | 71% (Over 2.5) | niska |
| Lisboa - Szabova (WFLW, 3R, debiut Szabovej) | Szabova wygra | 80% | 1.25 | 85% (obcięte do 80%: debiut w UFC, brak statystyk, reguła pułapu) | średnia |
| | Walka zakończona przed czasem | 52% | 1.92 | 54% | niska |
| | Szabova przez finisz | 46% | 2.17 | brak | niska |

Kluczowe fakty:
- Moicano: 37 lat, 21-7-1, nr 12 w rankingu, pięć porażek przez finisz, ostatnio poddanie Duncana w R2 (kwiecień); wcześniej porażki z Makhachevem (sub R1) i Dariushem. SLpM 4.1, 1.68 obaleń/15 min. Nolan: 26 lat, 11-1, nr 14, SLpM 5.9, wyższy zasięg (źródła rozbieżne: 73 in vs 203 cm), ostatnio decyzja z Ziamem; Nolan dostał walkę we wrześniu po wycofaniu się Briana Ortegi (ok. 6 tygodni przed galą), więc krótki termin nie jest istotnym czynnikiem. Wiek 37 w 5 rundach to ryzyko ogonowe, ale rynek (Pinnacle) mimo to faworyzuje Moicano, więc p jest blisko 50/50.
- Smith: 13-0 (jedno źródło podaje sprzeczne dane o porażkach), 11 finiszów, ostatnio TKO w 1:32; Brown: 28 walk, 5 porażek przez finisz; Smith z krótkim terminem po Leal.
- Szabova: 12-0, 9 finiszów, była mistrzyni Oktagonu w dwóch wagach; Lisboa 7-4, przegrała dwie ostatnie walki przez finisz.

Uwaga do linii Over/Under w main evencie: Pinnacle wycenia Over 1.5 rundy tylko na 64% (ok. 36% walki kończy się w pierwszej połowie 2. rundy), co jest sprzeczne z modelem (84%) i z profilem obu zawodników. Odrzucono jako niewiarygodne źródło; typ O/U w main evencie nie trafia do rankingu.

## CZĘŚĆ B. E-sport 30-31.10.2026

Pary i godziny z Pinnacle (lista meczów z `pinnacle_sport_matchups`, sport E Sports) oraz Strafe (LoL). HLTV, Liquipedia i dotesports zwróciły 403. PandaScore bez klucza. Dota 2: brak turnieju tier-1 w liście Pinnacle na te dni (nie potwierdzono innym źródłem).

### CS2: PGL Masters Bucharest (24-31.10, playoffs bo3, finał bo5)
- Ćwierćfinały rozegrane 29.10: Vitality - NAVI 2-1 (awans), Nemiga - FUT 2-0 (awans). Para 2. półfinału: MOUZ - FURIA (z Pinnacle).
- Półfinał 1: Nemiga - Vitality, pt 30.10 13:00 PL (Pinnacle cutoff 12:00 UTC). W chwili research mógł być już w toku lub zakończony; nie zweryfikowano wyniku.
- Półfinał 2: MOUZ - FURIA, pt 30.10 16:00 PL.
- Mecz o 3. miejsce (bo3) i finał (bo5) w sob 31.10: pary zależą od półfinałów, godziny nieznane. Dla finału bo5 i 3. miejsca nie podano p. Nie wymyślano par.
- Brak mapowych statystyk veto dla półfinałów (wyszukiwanie dało tylko dane ogólne: MOUZ za 3 mies. Mirage/Inferno 86%, Ancient 25%, Anubis bez danych; Liquid pokonało MOUZ 2-1 w Swiss). Dlatego p mapy oparte o rynek, pewność niska-średnia.

| Mecz (bo3) | Rynek | p | Fair | Rynek (Pinnacle, bez marży) | Pewność |
|---|---|---|---|---|---|
| Nemiga - Vitality (p mapy Vit. 0.74) | Vitality wygra serię | 83% | 1.20 | 83% | średnia |
| | Vitality -1.5 map (2-0) | 55% | 1.83 | 58% | średnia |
| | Nemiga +1.5 map | 45% | 2.21 | 42% | średnia |
| | Under 2.5 map | 61% | 1.64 | 64% | średnia |
| MOUZ - FURIA (p mapy MOUZ 0.565) | MOUZ wygra serię | 59% | 1.69 | 60% | niska |
| | MOUZ +1.5 map | 81% | 1.23 | brak linii | niska |
| | FURIA +1.5 map | 68% | 1.47 | 68% | niska |
| | Total map | 49/51% | ok. 2.0 | 46% Over | niska (odrzucony) |

### LoL: Worlds 2026, faza szwajcarska (Allen, Teksas), runda 4 bo3, pt 30.10 (1-2, mecz o przetrwanie)
- Liquid - LOS: pt 30.10 ok. 21:00 PL (16:00 ET; Pinnacle 20:15 UTC = 21:15). Liquid wygrało 2-0 z Anyone's Legend (1. rozstawiony LPL), LOS 2-0 z Team Secret Whales. Rynek faworyzuje Liquid wyraźnie.
- HLE - G2: sob 31.10 ok. 00:00 PL (19:00 ET, Pinnacle 23:15 UTC = 00:15). Brak szczegółowej analizy formy.
- Runda 5 (sob 31.10, ok. 18:00 PL wg zapytania): pary nieznane, zależą od wyników rund 4. Według Strafe grają trzy przegrane 2-1 z rundy 4 i trzej zwycięzcy meczów eliminacyjnych; ustalą się dopiero po 30.10.
- Wyniki rundy 4 z 28-29.10: T1 i Invictus Gaming (3 wygrane) oraz Top Esports awansowali; Karmine Corp pokonało CTBC 2-0.

| Mecz (bo3) | Rynek | p | Fair | Rynek (Pinnacle, bez marży) | Pewność |
|---|---|---|---|---|---|
| Liquid - LOS (p mapy 0.70) | Liquid wygra serię | 78% | 1.28 | 80% | średnia |
| | Liquid -1.5 map | 49% | 2.04 | 53% | niska |
| | Liquid +1.5 map | 91% | 1.10 | brak | odrzucony (fair <= 1.15) |
| | Under 2.5 map | 58% | 1.72 | 61% | niska |
| HLE - G2 (p mapy 0.69) | HLE wygra serię | 77% | 1.30 | 77% | średnia |
| | HLE -1.5 map | 48% | 2.10 | 51% | niska |
| | Under 2.5 map | 57% | 1.75 | 59% | niska |

Pinnacle ma też handicap HLE -1.5 po -112 i Liquid -1.5 po -125, co przy EV z naszym p jest ujemne.

## Najlepsze rynki (fair > 1.15, p wysokie, pewność nie niska preferowana)

| Wydarzenie | Rynek | p | Fair |
|---|---|---|---|
| Lisboa - Szabova | Szabova wygra | 80% | 1.25 |
| Gall - Reese | Reese wygra | 74% | 1.35 |
| Kropschot - Klein | Kropschot wygra | 71% | 1.41 |
| Yana Santos - Luana Santos | Luana Santos wygra | 71% | 1.41 |
| Yana Santos - Luana Santos | Dystans | 76% | 1.32 |
| Rodriguez - Alencar | Rodriguez wygra | 69% | 1.45 |
| Rodriguez - Alencar | Dystans | 75% | 1.33 |
| Brown - Smith | Smith wygra | 68% | 1.47 |
| Lebosnoyani - Hasanov | Lebosnoyani wygra | 68% | 1.47 |
| Nemiga - Vitality | Vitality wygra serię | 83% | 1.20 |
| Nemiga - Vitality | Under 2.5 map | 61% | 1.64 |
| Liquid - LOS | Liquid wygra serię | 78% | 1.28 |
| HLE - G2 | HLE wygra serię | 77% | 1.30 |
| MOUZ - FURIA | FURIA +1.5 map | 68% | 1.47 |

Uwaga: p wynikają głównie z rynku, więc przewaga nad Pinnacle (EV) jest zerowa lub ujemna. Zasadność kuponów zależy od kursów Betclic/gg397.bet, których tu brak. Liczba zastępców i krótkie terminy zwiększają niepewność MMA.

## Odrzucone

- Moicano - Nolan: dystans i Over/Under rund w main evencie (rozbieżność model vs linia Pinnacle 84% vs 64%, nie do wyjaśnienia bez danych); zwycięzca 51/48% to praktycznie moneta, bez przewagi.
- Osbourne - Durden: 52/48%, Osbourne po niewyjaśnionej kontuzji, nie ma sygnału.
- Marshall - Hope, Berggren - Sezinando, Erosa - Lee: p 57-65%, zastępca lub brak statystyk, za niska pewność.
- Kropschot - Klein Over/Under: rynek 50/50.
- Szabova w sposobie wygranej (KO/TKO): brak statystyk uderzeń, debiut w UFC, tylko niska pewność.
- MOUZ - FURIA zwycięzca/total map: p blisko 50-60%, rynek 60/40, bez sygnału; total 49% bez przewagi.
- Liquid +1.5 map (fair 1.10) i inne typy z fair <= 1.15 odrzucone według zasady.
- Mecz o 3. miejsce i finał CS2 bo5 (31.10), runda 5 Worlds (31.10): pary nieznane lub zależne od wyników, nie typowano.
- Dota 2: brak tier-1 w dniach 30-31.10 według źródeł; nie potwierdzono poza Pinnacle.

To są oszacowania, nie gwarancje.
