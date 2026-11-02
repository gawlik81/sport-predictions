# Kupony 30.10-31.10.2026 (10 kuponów, poziomy luzowania 0-2)

## 1. Okres i źródło kursów

- Okres: piątek 30.10 - sobota 31.10.2026 (+ noc 01.11 dla UFC); zakres zawężony za zgodą użytkownika (niedziela 01.11 pominięta).
- Kursy: **Betclic.pl** (źródło główne), kontrola **gg397.bet/pl** tylko dla nóg z EV > 0.
- Godzina pobrania: piłka, NBA, NHL ok. 07:00 CET; tenis, MMA, e-sport ok. 13:00-13:30 CET (30.10). Kursy mogą się zmienić do startu.
- Analizy: `Analiza_pilka_cz1/cz2`, `Analiza_NBA`, `Analiza_NHL`, `Analiza_tenis`, `Analiza_MMA_esport` (wszystkie `_2026-10-30.md`). Kursy: `Kursy_Betclic_*_2026-10-30.md`.

## 2. Skrót terminarza

Analizowano ok. 85 wydarzeń z 30-31.10: piłka 17 (cz1) + 16 (cz2, w tym 6 Ekstraklasy), NBA 12, NHL 9, tenis ATP/WTA (ćwierćfinały Wiedeń/Bazylea/Queretaro), UFC 12 walk, e-sport (CS2 PGL Bucharest, LoL Worlds).
Pominięte: Curitiba (ranga 100-600, dane tylko z ITF), mecz o 3. miejsce i finał CS2 oraz runda 5 Worlds (pary nieznane), półfinały tenisowe (pary zależne od piątku), Jazz-Blazers i Hornets-76ers (brak linii), Radomiak-Śląsk, Zagłębie-Korona, Raków-Pogoń (poniedziałek 02.11). Mecze już rozpoczęte w chwili składania (Medvedev-Mannarino, CS2 Nemiga-Vitality, Rune-Vacherot) nie weszły do kuponów.
Dyscyplin bez nóg na kuponach: **NHL** (Betclic wystawił 3 z 9 meczów, bez totali 5,5/6,5 i puck line, EV < 0), **NBA** (patrz niżej).

## 3. Pula nóg po filtrach

Odrzucono nogi z p ≤ 50% (GKS wygra 50%, Lisboa-Szabova dystans 48%, Mainz wygra 45,5%), fair ≤ 1,15, bez kursu Betclic, ze statusem "po ważeniu"/stand-in o niskiej pewności oraz Moicano-Nolan dystans 5R (kurs 3,63 to artefakt, analiza go odrzuciła).

**Nogi z EV > 0 na Betclic i p > 50%:**

| Mecz | Termin PL | Rynek | p | Fair | Betclic | gg397.bet | EV | Pewność / uwagi |
|---|---|---|---|---|---|---|---|---|
| Lech - Wisła Kraków | sob 17:30 | Lech lub remis | 84% | 1,19 | 1,22 | brak wiarygodnego | +2,5% | średnia |
| Lech - Wisła Kraków | sob 17:30 | Lech wygra | 64% | 1,56 | 1,73 | 1,84 | +10,7% | **przewaga niepotwierdzona** (rynek ok. 55%, p modelu +9 pp); nie wszedł do kuponu |
| Struff - Borges | pt 19:10 | Over 21,5 gemów | 77% | 1,30 | 1,35 | 1,40 | +3,5% | średnia; Over 22,5 (1,56, EV +4,5%) i Borges +3,5 (1,32, +5,6%) to ten sam mecz |
| Struff - Borges | pt 19:10 | Borges wygra | 53% | 1,89 | 2,12 | 1,70 | +12,4% | **przewaga niepotwierdzona**, niska pewność, rozbieżność 0,42; odrzucony |
| GKS Katowice - Widzew | sob 20:15 | GKS lub remis | 76% | 1,32 | 1,34 | brak wiarygodnego | +1,8% | średnia |
| Rodriguez - Alencar (UFC) | sob 22:20 | Walka na dystans | 75% | 1,33 | 1,38 | 1,19 | +3,5% | rozbieżność 0,19, feed gg397 niewiarygodny dla tej walki; "po ważeniu" |
| Coventry - Sunderland | sob 16:00 | Under 3,5 | 75,8% | 1,32 | 1,33 | 1,17 | +0,8% | rozbieżność 0,16; przewaga w granicy błędu |
| GSW - Lakers | sob 03:00 | GSW total drużyny Under 116,5 | 59% | 1,70 | 1,81 | brak | +6,8% | niska pewność; **żaden kupon nie spełnia p > 50%** z tą nogą |
| Suns - Nuggets | sob 03:00 | PHX total drużyny Under 113,5 | 55% | 1,82 | 1,84 | brak | +1,2% | niska pewność; j.w. |

NBA: pozostałe Under totali drużyn (MIN, ORL, MIA) mają na Betclic inne linie niż analiza (p do przeliczenia), więc nie weszły. Rynki zawodnika (Tatum, Towns) nie istnieją na Betclic. Moneyline i spready NBA/NHL mają EV < 0.

## 4. Kupony

Łączne p, kurs i EV liczone skryptem `bet-slip-builder/scripts/slip.py` (założenie niezależności meczów). Stawka = 1/4 Kelly'ego dla całego zestawu. Zasady: jedna noga na mecz w kuponie, żadna noga nie powtarza się w innym kuponie, brak sprzeczności, fair każdej nogi > 1,15.

### Poziom 0 (progi bazowe: EV > 0, p > 50%, kurs 1,5-2,5, dwie nogi > 1,2)

**Kupon 1** | EV **+6,5%** | p **64,7%** | kurs **1,65** | fair 1,55 | stawka **2,5% bankrolla**
| Noga | Termin PL | Rynek | p | Kurs Betclic | gg397.bet | EV |
|---|---|---|---|---|---|---|
| Lech - Wisła Kraków | sob 17:30 | Lech lub remis | 84% | 1,22 | brak wiarygodnego | +2,5% |
| Struff - Borges | pt 19:10 | Over 21,5 gemów | 77% | 1,35 | 1,40 | +4,0% |
Ryzyko: Lech 1X ma kurs tuż nad 1,2 (marża pochłania przewagę), a total gemów opiera się na p_serve z 10-12 ostatnich meczów (Betclic ma niższe linie główne, 18,5-22,5). Struff grał trzy sety z Djokoviciem, czas meczu niepotwierdzony.

**Kupon 2** | EV **+5,4%** | p **57,0%** | kurs **1,85** | fair 1,75 | stawka **1,6% bankrolla**
| Noga | Termin PL | Rynek | p | Kurs Betclic | gg397.bet | EV |
|---|---|---|---|---|---|---|
| GKS Katowice - Widzew | sob 20:15 | GKS lub remis | 76% | 1,34 | brak wiarygodnego | +1,8% |
| Rodriguez - Alencar (UFC) | sob 22:20 | Walka na dystans | 75% | 1,38 | 1,19 (niewiarygodny) | +3,5% |
Ryzyko: noga MMA "po ważeniu" (zastępstwa w karcie, ważenie jeszcze się nie odbyło); GKS 1X bez składów i bez kursu referencyjnego z gg397.bet, a na gg397.bet "GKS wygra" jest niżej (1,80).

### Poziom 1 (EV zestawu ≥ -5%; stawka 0%, nie do gry bez zgody; poniżej bazowych progów EV)

**Kupon 3** | EV -0,9% | p 59,1% | kurs 1,68 | fair 1,69 | stawka 0%
Coventry - Sunderland (sob 16:00) Under 3,5 (p 75,8%, 1,33; gg397.bet 1,17, rozbieżność 0,16) + Schalke - Leipzig (sob 15:30) Leipzig lub remis (p 78%, 1,26). Ryzyko: Under 3,5 praktycznie bez przewagi; Leipzig tylko w rynku Betclic.

**Kupon 4** | EV -2,8% | p 52,6% | kurs 1,85 | fair 1,90 | stawka 0%
Lille - Lens (pt 21:05) Under 3,5 (p 72,5%, 1,36) + Bournemouth - Leeds (sob 16:00) Under 3,5 (p 72,5%, 1,36). Ryzyko: obie nogi z tej samej rodziny rynków; mecz Lille-Lens jest wyrównany.

**Kupon 5** | EV -1,9% | p 54,3% | kurs 1,81 | fair 1,84 | stawka 0%
Troyes - Le Mans (sob 20:45) Under 3,5 (p 71,4%, 1,38) + Y. Santos - L. Santos (UFC, nd 01:20) walka na dystans (p 76%, 1,31). Ryzyko: noga MMA "po ważeniu"; beniaminkowie Ligue 1 bez danych kadrowych.

**Kupon 6** | EV -4,6% | p 52,2% | kurs 1,83 | fair 1,91 | stawka 0%
Rayo - Celta (sob 16:15) Under 3,5 (p 76,8%, 1,26) + MOUZ - FURIA (CS2, pt 16:00) FURIA +1,5 mapy (p 68%, 1,45). Ryzyko: rynek wycenia Rayo - Celta Under wyżej niż model; noga CS2 zależna od przebiegu półfinału.

### Poziom 2 (bez limitu EV, ranking po p; stawka 0%, tylko poglądowo)

**Kupon 7** | EV -10,0% | p 59,1% | kurs 1,52 | fair 1,69 | stawka 0%
Brentford - Forest (sob 16:00) Over 1,5 (p 77,7%, 1,21) + Fils - Fritz (pt 15:10) Over 21,5 gemów (p 76%, 1,26; Fils zmęczony).

**Kupon 8** | EV -13,3% | p 55,9% | kurs 1,55 | fair 1,79 | stawka 0%
Hull - Ipswich (sob 16:00) Over 1,5 (p 75,1%, 1,26) + Chelsea - Man United (sob 13:30) 1X (p 74,5%, 1,23).

**Kupon 9** | EV -11,7% | p 53,9% | kurs 1,64 | fair 1,86 | stawka 0%
Aston Villa - Fulham (sob 21:00) 1X (p 73,8%, 1,27) + Górnik - Legia (pt 20:30) Over 1,5 (p 73%, 1,29).

**Kupon 10** | EV -13,3% | p 52,9% | kurs 1,64 | fair 1,89 | stawka 0%
Leverkusen - Stuttgart (sob 15:30) Leverkusen lub remis (p 73%, 1,27) + Milan - Inter (sob 20:45) Inter lub remis (p 72,5%, 1,29).

Poziomy 3-6 (zgoda użytkownika) nie były potrzebne: poziom 2 dał 10 kuponów. Poziom 3 dopuściłby nogi NBA (GSW U116,5 z p 59% w parze z Lech 1X dałby p 49,6%, więc nawet tam wymagałby p > 45%).

## 5. Ostrzeżenia

- **Tylko kupony 1 i 2 mają EV > 0 (stawka > 0).** Kupony 3-10 mają EV ujemne lub zerowe: pokazane zgodnie z poziomami luzowania, stawka 0%. Nie są rekomendacją do gry.
- Ten dzień ma wąską pulę: Betclic wycenia gole i wyniki ściślej niż modele (większość nóg z analiz ma EV od -1% do -17%). Wszystkie nogi z EV > 0 mają niską lub średnią pewność, a EV bierze się z różnicy 2-4 pp nad rynkiem, czyli w granicy błędu modelu.
- Założenie niezależności meczów; kupony 1, 2, 5 łączą mecze z różnych dni/dyscyplin, ale wynik jednej nogi nie wpływa na drugą.
- Nogi niepotwierdzone na gg397.bet lub rozbieżne > 0,10: Coventry U3,5 (1,17), Rodriguez-Alencar dystans (1,19), Lech wygra (1,84), Borges (1,70), GKS wygra (1,80). Feed gg397.bet bywa niespójny (anomalie w 1X2, kursy sprzeczne ze stroną meczu).
- Składy i kontuzje niepotwierdzone w LaLiga/Ligue 1/Ekstraklasie; bramkarze NHL niepotwierdzeni; statusy NBA z ESPN/Rotowire, nie z oficjalnego raportu.
- Kursy mogą się zmienić do startu; mecze z 30.10 (Struff-Borges 19:10, Lille-Lens 21:05, Górnik-Legia 20:30) wymagają odświeżenia tuż przed meczem.
- Oszacowania probabilistyczne, nie gwarancje; stawka to sugestia wielkości, nie porada finansowa.
