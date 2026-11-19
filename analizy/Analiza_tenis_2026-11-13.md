# Analiza tenis 13.11.2026 (czas polski)

Mecze: ATP Bybit Stockholm Open (ATP 250, hala/twarda) - półfinały; WTA Finals Indian Wells (hala/twarda, round robin, grupa 2) - ostatnia kolejka.
Źródła pary/godziny: ESPN scoreboard (sportsdata MCP) + Pinnacle (sportsdata MCP, kursy), potwierdzone ATP (raport QF), Tennis Uptodate, Tennis Majors, Sportskeeda/LWOS (WebSearch). Kursy: Pinnacle (po przeliczeniu z amerykańskich, bez marży w kolumnie "rynek no-vig"); BettingPros pominięty (brak klucza w sesji).

## Uwaga metodologiczna (ważna)
- Brak twardych statystyk sezonu (hold/break, % punktów przy serwisie) dla żadnego z ośmiu zawodników: WebSearch ich nie zwrócił, API Tennis wymaga klucza. **p_serve jest więc oszacowane** (kalibrowane tak, by p meczu odpowiadało mojej ocenie po korektach), model służy tylko do kształtu rozkładu wyniku setowego i handicapu gemów.
- Zgodnie z regułą SKILL.md: **total gemów nie jest podany jako typ** (p_serve z szacunku). W tabelach jest tylko jako linia rynku do orientacji.
- Dla żadnego meczu własne p nie odbiega od rynku no-vig o więcej niż 2 pp (celowo: brak twardych danych = nie schodzę/nie wchodzę ponad rynek). Wartość (EV) względem Pinnacle jest ~0 lub ujemna; to nie są typy "value", tylko wycena.
- Kontuzje: osobne wyszukiwania nie wykazały żadnej bieżącej kontuzji u ośmiorga zawodników (Rune wycofał się z QF z urazem uda/ścięgna, to nie dotyczy tych meczów). Niepotwierdzone w oficjalnych źródłach ATP/WTA, tylko brak doniesień.

---

## 1. Tabilo - Tirante (ATP Stockholm, SF, hala, 14:00)
**Typ:** zwycięzca Tabilo | **p:** 55% | **Fair:** 1.82 | **Pewność:** niska
Rynek Pinnacle: Tabilo 1.70 / Tirante 2.26 (no-vig 57,0% / 43,0%). Inne źródła: BetMGM -150/+115, Dimers model 55%.

**Sytuacja:** Tabilo (rozstawiony nr 4, top 35) po serii 1-7 przed Stockholmem wygrał w Sztokholmie m.in. z Sonego 7-6 6-7 7-5 (11.11) i Michelsenem 7-5 7-6(2) w 1h54 (12.11) (ESPN/ATP). Tirante: nierozstawiony, QF z Shevchenko 7-6 6-7 6-3 po 2h49 (tylko jedno przełamanie), R2 walkover. Tirante ma najkrótszy odpoczynek (QF skończony ok. 17:10 PL, SF o 14:00 następnego dnia), Tabilo kończył wcześniej (ok. 14:00 PL). Hala szybka, duży pierwszy serwis Tirante (źródło: LWOS/Tenngrand).
**H2H:** Tabilo 4-1 (wg Sportskeeda; Tenngrand podaje 3-1), wszystkie wygrane Tabilo na mączce; Tirante wygrał jedyne spotkanie na twardej (Challenger Cancun 2025, 6-2 6-4). Pierwszy mecz w hali. Waga niska (Challenger + inna nawierzchnia).
**Kalibracja:** forma Tabilo (1-7 -> 4 wygrane) i szybka hala = ryzyko, p obcięte o ~2 pp względem rynku; nie więcej, bo brak twardych statystyk serwisu Tirante.
**Model (p_serve Tabilo 0.650 / Tirante 0.640, szacowane):**
- Zwycięzca meczu: Tabilo 55% (1.82) / Tirante 45% (2.22).
- Wynik setowy: Tabilo 2-0 28% (3.5), 2-1 26,5% (3.8), Tirante 2-1 23% (4.3), 2-0 22% (4.6). Over 2.5 seta ~50% (rynek 44,6%: więcej 2-0 niż model; rynek sugeruje, że typy 2-1 są drogie).
- Zwycięzca 1. seta: Tabilo 53,5% (1.87) (Pinnacle no-vig 54,6%).
- Handicap gemów (symulacja, orientacyjnie): Tabilo -1.5 48,5% (2.06) / Tirante +1.5 51,5% (1.94); Tabilo -2.5 42%; Tabilo +2.5 71,6%.
- Total gemów: **brak typu** (p_serve szacowane). Linia Pinnacle 24.5 (-110/-104), model ~25,8 (nie używać).
**Ryzyka:** wzrost dyspozycji Tirante serwisem na szybkiej hali (tie-breaki), znużenie Tirante po 2h49 (działa w drugą stronę), niestabilna forma Tabilo.

## 2. Musetti - Fritz (ATP Stockholm, SF, hala, 17:00)
(ESPN podaje Musetti-Fritz o 16:00Z = 17:00 PL; na Pinnacle gospodarzem jest Fritz.)
**Typ:** zwycięzca Fritz | **p:** 58% | **Fair:** 1.72 | **Pewność:** niska-średnia
Rynek Pinnacle: Fritz 1.64 / Musetti 2.39 (no-vig 59,4% / 40,6%).

**Sytuacja:** Fritz nr 1 turnieju, nr 10 rankingu (LWOS), pokonał Norrie 7-5 6-3 (11.11), QF walkover (Rune wycofany, uraz uda) - świeży; 7. półfinał sezonu, 3. w 4 tygodniach (forma vs zmęczenie, obie hipotezy; walkover zmniejsza zmęczenie). Musetti: Samuel 6-1 6-4, QF z Humbertem 7-6(5) 3-6 6-4 w 2h29, przełamany na początku 3. seta; mecz skończył ok. 22:00 PL, SF o 17:00 (ok. 19 h odpoczynku). Musetti 10-2 w hali w sezonie, wygrał finał w Lyonie z Fritzem 6-3 6-4 (25.10), Turyn mu się nie udał przez kontuzje (źródło LWOS; bieżącego urazu brak).
**H2H:** Musetti 5-3, Fritz wygrał 2 z 3 w hali, ostatnie (Lyon, hala) wygrał Musetti. Fritz serwis, Musetti return i bekhend; szybka hala sprzyja Fritzowi.
**Kalibracja:** p Fritza 58% (rynek 59,4%) z powodu ostatniego H2H (Lyon) i niższego p_serve na returnie Musettiego; walkover to niewielki plus kondycyjny, ale brak rytmu meczowego to też drobna korekta (-1 pp).
**Model (p_serve Fritz 0.671 / Musetti 0.654, szacowane):**
- Zwycięzca: Fritz 58% (1.72) / Musetti 42% (2.39).
- Wynik setowy: Fritz 2-0 31% (3.25), 2-1 27,5% (3.65); Musetti 2-1 22% (4.55), 2-0 20% (5.05). Over 2.5 seta ~50% (rynek ~41%).
- Zwycięzca 1. seta: Fritz 55% (1.82) (Pinnacle no-vig 57,6%).
- Handicap gemów (symulacja): Fritz -1.5 52% (1.92) / Musetti +1.5 48% (2.08); Fritz -2.5 44,5%; Musetti +2.5 55,5%.
- Total gemów: **brak typu**. Linia Pinnacle 23.0 (-113/-101).
**Ryzyka:** Musetti w pierwszym planie (return + Lyon 3 tyg. temu), zerwanie rytmu Fritza, wysoka liczba tie-breaków (serwis Fritza na szybkiej hali).

## 3. Muchova - Andreeva (WTA Finals, grupa 2, 3. kolejka, 21:00)
**Typ:** zwycięzczyni Andreeva | **p:** 70% | **Fair:** 1.43 | **Pewność:** średnia
Rynek Pinnacle: Andreeva 1.38 / Muchova 3.36 (no-vig 70,9% / 29,1%).

**Stawka grupowa:** Andreeva 2-0 w setach 4-0 (pokonała Sabalenkę 6-4 6-0 po 11 gemach z rzędu i Svitolinę 6-4 6-0), **awans i zwycięstwo w grupie już zapewnione**, gra o 200 pkt rankingowych (kontekst: bliskość nr 2) i o bilans 3-0. **Muchova 0-2 (1-4 w setach), wyeliminowana** (przegrała z Sabalenką 6-7(2) 5-7 i ze Svitolina 6-2 2-6 2-6). Gra o 200 pkt/prize money. Nie jest to czysty mecz bez stawki, ale motywacja Muchovej jest ograniczona; ryzyko dla Andreevy to oszczędzanie sił przed półfinałem (przeciwnik półfinałowy: druga z grupy 1) - bardziej prawdopodobne tylko po trudnym 1. secie.
**Stan zdrowia:** brak bieżących doniesień o urazach (Muchova ma historię kontuzji). Zmęczenie: Andreeva dwa krótkie mecze (ok. 70 min każdy), Muchova trzysetowy mecz 11.11 (2h+).
**H2H:** Andreeva 1-0 (Ningbo 2024, krecz Muchovej przy 2-6 0-1, nieaktualne).
**Kalibracja:** rynek zbyt silnie pewien 2-0 (Pinnacle ~49% 2-0 Andreevy); model flatten dla WTA, p 70% (rynek 70,9%).
**Model (p_serve Andreeva 0.610 / Muchova 0.570, szacowane):**
- Zwycięzca: Andreeva 70% (1.43) / Muchova 30% (3.33).
- Wynik setowy (spłaszczone): Andreeva 2-0 41% (2.44), 2-1 29% (3.45); Muchova 2-1 17% (5.9), 2-0 13% (7.7). Rynek: 2-0 Andreeva ~49% (wyższe niż moje).
- Zwycięzca 1. seta: Andreeva 64% (1.56) (Pinnacle no-vig 66%).
- Handicap gemów (symulacja): Andreeva -2.5 59,5% (1.68); -3.5 50% (2.0); -4.5 39% (2.55); Muchova +4.5 61%. Przy linii rynku -4.0 moje p wygranej ~44% (rynek ~52%): **brak value**, model może zaniżać ogon.
- Total gemów: **brak typu**. Linia Pinnacle 20.5 (-112/-100).
**Ryzyka:** Andreeva ulegająca spokojniejszej motywacji (stawka tylko punkty), Muchova ze swobodą (dead rubber lubi upset 15-20%), model nie wychwytuje zachowania "bez stawki".

## 4. Svitolina - Sabalenka (WTA Finals, grupa 2, 3. kolejka, 22:30)
(ESPN 21:30Z = 22:30 PL; Pinnacle podaje 22:00Z = 23:00 PL; kolejność po meczu Muchova-Andreeva, start "nie przed". Gospodarzem w Pinnacle jest Sabalenka.)
**Typ:** zwycięzczyni Sabalenka | **p:** 64% | **Fair:** 1.56 | **Pewność:** średnia
Rynek Pinnacle: Sabalenka 1.53 / Svitolina 2.68 (no-vig 63,6% / 36,4%).

**Stawka grupowa:** obie 1-1, **zwycięzczyni awansuje do półfinału** (z 2. miejsca w grupie 2, rywalka Noskova, zwyciężczyni grupy 1), przegrana odpada. Wszystko do wygrania.
**Forma:** Sabalenka: 7-6(2) 7-5 z Muchovą, potem 4-6 0-6 z Andreevą (prowadziła 4-1, straciła 11 gemów z rzędu; spadek poziomu, ale w głównym źródle bez informacji o kontuzji). Svitolina: 4-6 0-6 z Andreevą, 3-6 6-2 6-2 z Muchovą (wygrana po przegranym 1. secie); 32 lata, bilans setów 2-3 w tegorocznych Finals.
**H2H:** Sabalenka 6-1 (5 z rzędu, w tym 6-2 6-3 w półfinale AO 2026), wszystkie na twardej. Dla Svitoliny jedyna wygrana: Strasbourg 2020 (mączka).
**Kalibracja:** brak własnych statystyk, p z H2H i rynku; nie przekraczam rynku o >1 pp; sygnał: wyraźny spadek Sabalenki w 2. secie z Andreevą (nerwy/forma) obniża p o ~2 pp względem czystej H2H (model bazowy dawałby 67%).
**Model (p_serve Sabalenka 0.620 / Svitolina 0.592, szacowane):**
- Zwycięzca: Sabalenka 64% (1.56) / Svitolina 36% (2.78).
- Wynik setowy (spłaszczone): Sabalenka 2-0 34% (2.9), 2-1 29% (3.45); Svitolina 2-1 20% (5.0), 2-0 17% (5.9). Rynek: Sabalenka 2-0 (-1.5 setu, Pinnacle +138) ~41% vs moje 34%: rynek bardziej "czysty" niż model.
- Zwycięzca 1. seta: Sabalenka 59% (1.69) (Pinnacle no-vig 60,5%).
- Handicap gemów (symulacja): Sabalenka -2.5 52,7% (1.90); -3.5 43% (2.33); Svitolina +3.5 57% (1.75). Linia rynku -3.0: moje ok. 48% (po wyłączeniu pusha), na poziomie rynku: **brak value**.
- Total gemów: **brak typu**. Linia Pinnacle 22.0 (-105/-107).
**Ryzyka:** wynik meczu o wszystko (Sabalenka ma problem z presją - z Andreevą oddała 11 gemów z rzędu), 32-letnia Svitolina szybko neutralizuje serwis, ryzyko trzeciego seta (rynek over 2.5 seta ~42%).

---

## Zestawienie (p vs rynek no-vig)
| Rynek | p | fair | Pinnacle (dec.) | Pewność |
|---|---|---|---|---|
| Tabilo wygra | 55% | 1.82 | 1.70 | niska |
| Fritz wygra | 58% | 1.72 | 1.64 | niska-średnia |
| Andreeva wygra | 70% | 1.43 | 1.38 | średnia |
| Sabalenka wygra | 64% | 1.56 | 1.53 | średnia |

Najpewniejszy typ dnia: Andreeva (70%); ale kurs Pinnacle 1.38 daje EV ok. -3% i p niewiele odbiega od rynku, więc brak value. Żaden mecz nie spełnia kryterium "przewaga nad rynkiem >2 pp z twardą informacją"; wszystkie to wyceny kalibrowane do rynku, nie value bety. Wszystkie wyliczenia to oszacowania, nie gwarancje.
