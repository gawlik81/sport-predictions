# Analiza piłkarska - mecze klubowe 13.11.2026 (czas polski)

Źródła: Superbet MCP (`superbet_stats`, `_h2h`, `_missing_players`, `_lineups`, `_event_odds`), WebSearch/WebFetch (Infobae, SALAMANCArtv, footballpredictions.ai, ran.joyn.de, cdleganes.com, fichajes.com). Modele: `poisson.py`, `markets.py`. Kursy: Superbet (marża zdjęta proporcjonalnie przy porównaniach "rynek bez marży"). BettingPros nie użyty (brak klucza w sesji). Wszystkie składy są niepotwierdzone (przed oficjalnymi). To oszacowania probabilistyczne, nie gwarancje.

Potwierdzenie rozgrywek: Znicz - Sokół = II liga (grupa wschodnia, 15. kolejka), Leganes - Burgos = LaLiga 2 (Segunda División), Salamanca UDS - Celta = Copa del Rey, jeden mecz (bez rewanżu, dogrywka/karne, rynek "Awans"; mecz przełożony z 28.10), Dijon - Orleans = Coupe de France, jeden mecz z dogrywką i karnymi (rynek "Awans"; źródło ran.joyn.de podaje 7. rundę).

---

## 1. Znicz Pruszków - Sokół Kleczew (II liga, 13.11, 18:00)

**Typ:** Znicz wygra lub zremisuje (1X) | **p:** 78,5% | **fair:** 1.27 | **Pewność:** średnia. Mecz bez wartości względem kursu Superbet (1X 1.16).
**λ:** 2,00 / 1,15 (łącznie 3,15; rynek bez marży implikuje ok. 3,1)

| Rynek | p | fair | Kurs Superbet | EV | Pewność |
|---|---|---|---|---|---|
| 1 / X / 2 | 57,1% / 21,5% / 21,5% | 1.75 / 4.65 / 4.66 | 1.59 / 4.25 / 4.55 | -9% / -9% / -2% | średnia |
| 1X / X2 / 12 | 78,5% / 42,9% / 78,5% | 1.27 / 2.33 / 1.27 | 1.16 / 2.20 / 1.18 | -9% / -6% / -7% | średnia |
| Over 1.5 | 82,2% | 1.22 | 1.12 | -8% | średnia |
| Over 2.5 / Under 2.5 | 61,0% / 39,0% | 1.64 / 2.56 | 1.43 / 2.60 | -13% / +1% | średnia |
| Over 3.5 | 38,6% | 2.59 | 2.07 | -20% | niska |
| BTTS tak / nie | 59,1% / 40,9% | 1.69 / 2.44 | 1.50 / 2.37 | -11% / -3% | średnia |
| Handicap Znicz -1.5 / Sokół +1.5 | 34,0% / 66,0% | 2.94 / 1.52 | 2.40 / 1.50 | -18% / -1% | średnia |
| Rożne (średnia 10,6) Over 10.5 / Under 10.5 | 48% / 52% | 2.07 / 1.94 | 1.72 / 1.97 | -17% / +2% | niska (brak sędziego) |
| Kartki | brak sędziego; średnie 2,0 + 2,2 | - | - | - | brak typu |

**Statystyki drużyn:** Znicz 1. w grupie, 33 pkt po 15 meczach (10W 3D 2L, bramki 29:17), u siebie 5W 3D 1L, 16:10 (footballpredictions.ai). Średnie sezonowe Superbet: Znicz 1,9 strzelone / 1,1 stracone; Sokół 1,4 / 2,0. Sokół 15., 18 pkt (4W 6D 5L, 21:30), na wyjeździe 1W 2D 3L, 6:16 (średnio 2,7 straconego). Forma Znicza: 2:2 Podhale, 0:3 w Łęcznej (Górnik), 0:1 Ruch, 2:0 Avia, 1:0 Rekord, 1:0 Zawisza; Sokół: 3:2 Sandecja, 2:1 Stal SW (wyjazd), 2:1 Podhale, 4:2 Śląsk II, 0:0 Resovia, 1:2 Hutnik. Uwaga: lista formy Superbet zawiera mecze w dniach powszednich (prawdopodobnie puchary lub zaległości), a pole xG Superbet (5,4/mecz dla Znicza) jest błędne i zostało zignorowane.
**H2H:** brak w bazie Superbet (bilans 0-0-0), brak danych.
**Informacje medialne:** brak raportu kontuzji (`missing_players` niedostępne dla II ligi), brak składów, brak sędziego. Znalazłem tylko zapowiedź algorytmiczną (nie wiarygodna). Pewność ograniczona brakiem tych danych.
**Ryzyka:** (1) remis (21,5%) i wygrana Sokoła (21,5%) mają podobną wagę; Sokół ma serię WWWWD/WWWDL i 11 goli w 5 meczach, ale to forma przeciwko słabszym rywalom; (2) Znicz strzelił w ostatnich 5 meczach tylko 5 goli, więc Over 2.5 i handicap -1.5 są droższe niż się wydaje; (3) kryzys dotyczy tylko underdoga, a Sokół nie jest w kryzysie wynikowo (brak obniżki p Znicza).
**Rynek:** model zgodny z rynkiem w 1X2 (57,1% vs 58,0% bez marży), Over 2.5 mniej niż rynek (61,0% vs 64,5%), BTTS tak 59,1% vs 61,2% - różnice < 5 pp, brak value. **Brak mocnego typu ani value; najbezpieczniejszy "wynikowy" rynek to Znicz 1X lub Over 1.5 (oba kursy poniżej fair).**

---

## 2. Leganes - Burgos (LaLiga 2, 13.11, 20:30)

**Typ:** brak mocnego typu (mecz wyrównany) | najlepszy rynek: Under 3.5 gola (79,9%, fair 1.25) lub X2 (61,7%, fair 1.62), oba bez value | **Pewność:** niska-średnia
**λ:** 1,20 / 1,10 (łącznie 2,3, zgodne z rynkiem: O2.5 2.27 / U2.5 1.63)

| Rynek | p | fair | Kurs Superbet | EV | Pewność |
|---|---|---|---|---|---|
| 1 / X / 2 | 38,3% / 28,3% / 33,4% | 2.61 / 3.53 / 3.00 | 2.47 / 3.00 / 3.05 | -5% / -15% / +2% | niska |
| 1X / X2 / 12 | 66,6% / 61,7% / 71,7% | 1.50 / 1.62 / 1.39 | 1.35 / 1.51 / 1.36 | -10% / -7% / -2% | średnia |
| Over 1.5 / Under 1.5 | 66,9% / 33,1% | 1.49 / 3.02 | 1.40 / 2.92 | -6% / -3% | średnia |
| Over 2.5 / Under 2.5 | 40,4% / 59,6% | 2.48 / 1.68 | 2.27 / 1.63 | -8% / -3% | średnia |
| Under 3.5 | 79,9% | 1.25 | 1.23 | -2% | średnia |
| BTTS tak / nie | 46,6% / 53,4% | 2.15 / 1.87 | brak kursu osobnego rynku | - | niska |
| Handicap Leganes -1.5 / Burgos +1.5 | 16,4% / 83,6% | 6.10 / 1.20 | - | - | niska |
| Rożne (średnia 8,5; sezon 3,8 + 4,2) Under 9.5 / Over 7.5 | 64% / 60% | 1.56 / 1.65 | 1.67 / 1.41 | +7% / -15% | niska (jedno źródło) |
| Kartki (średnia 5,7; sędzia Romero Freixas) Over 4.5 / Over 5.5 | 64% / 49% | 1.56 / 2.04 | 1.29 / 1.60 | -17% / -22% | niska |

**Statystyki drużyn (sezon, 13 meczów):** Leganes 11 goli strzelonych (0,8/mecz), 1,8 straconego, 156 strzałów (12,0), 4,2 celnych, ale 23 zmarnowane "big chances" - niska skuteczność, więc λ ataku podniosłem powyżej gołej średniej bramkowej, ale nie powyżej rynku. Burgos 19 goli (1,5), 1,1 straconego, strzały 12,1 (4,1 celnych), 3 czyste konta po obu stronach. Forma Leganes (6): 1:0 Alcorcón (wt. 10.11, prawdopodobnie puchar), 1:3 Albacete, 3:4 Valladolid, 1:1 Mallorca, 0:1 Cordoba, 0:3 Almeria (bilans 1W 1D 4L, 6:12). Forma Burgos: 2:1 Celta B, 1:1 Castellon, 4:2 Laredo, 3:2 Andorra, 1:0 Sabadell, 0:1 Granada (mieszane ligi/puchar).
**H2H:** Burgos wygrał ostatnie dwa (2:1 sty 2026, 2:1 na wyjeździe w Leganes 1.11.2025); wcześniej Leganes 2:0 (2024). Bilans od 2001: 2W Leganes, 4D, 4W Burgos. Tylko 2 mecze z ostatnich ~3 lat, waga niska.
**Informacje medialne:** nieobecni (Superbet): Leganes - Francisco Montero (zawieszenie, nr 3, lewa obrona); Burgos - David Gonzalez Ballesteros i Saul Del Cerro (kontuzje, powód nieznany). Przewidywany skład Leganes 4-4-2 z Morata i Soko z przodu; Burgos 4-2-3-1 z Fores i Curro (status "przewidywany", niepotwierdzony). Sędzia: Gonzalo Romero Freixas, brak danych z Segunda 26/27; proxy z Primera RFEF ok. 5,2-5,4 żółtych/mecz (fichajes.com), więc dla kartek brak twardego sygnału. Leganes ma 3,5 kartek/mecz (3 czerwone w sezonie), co jest wkładem do średniej 5,7. Uwaga: zawodnika rynku (Morata strzały) nie typuję - skład niepotwierdzony.
**Ryzyka:** remis (28,3%) i wygrana któregokolwiek z zespołów mają podobne p; Burgos ma lepszy atak i defensywę w liczbach (wartościowy gość), ale gra na wyjeździe z gospodarzem w niskim bilansie bramkowym; Leganes może wykorzystać przymus punktowania po serii 1W w 6 meczach.
**Rynek:** model = rynek (1X2 bez marży 38,0/31,3/30,8% vs model 38,3/28,3/33,4%). Różnice na remisie 3 pp (rynek wyżej). Brak value, brak typu rekomendowanego do kuponu. Jedyny dodatni EV (Burgos win +2%, Under 9.5 rożnych +7%) leży w granicach błędu lub opiera się na jednym źródle średniej.

---

## 3. Salamanca UDS - Celta Vigo (Copa del Rey, 13.11, 21:00)

**Format:** jeden mecz (bez rewanżu), przy remisie po 90 min dogrywka i karne; Superbet ma rynek "Awans" (Celta 1.09, Salamanca 5.85). Salamanca gra w Segunda Federación (4. poziom), trener Iker Muniain; Celta (Primera + Liga Europy) z trenerem Claudio Giraldezem. Rewanż nie istnieje, mecz był przełożony z 28.10 (źródło: SALAMANCArtv, Infobae).
**Typ:** Celta awansuje | **p:** 83% | **fair:** 1.20 (przypadek graniczny 1.15-1.20) | **Pewność:** średnia (pułap obniżony o rotacje i puchar)
**λ:** Celta 2,40 / Salamanca 0,70 (łącznie 3,1; rynek ok. 3,3-3,5). Wynik w 90': Celta 74%, remis 16,5%, Salamanca 9,5%.

| Rynek | p | fair | Kurs Superbet | EV | Pewność |
|---|---|---|---|---|---|
| Celta awansuje / Salamanca awansuje | 83% / 17% | 1.20 / 5.9 | 1.09 / 5.85 | -9% / 0% | średnia |
| 1 / X / 2 (90 min) | 9,5% / 16,5% / 74,0% | 10.5 / 6.1 / 1.35 | 8.70 / 5.90 / 1.23 | - / -3% / -9% | średnia |
| Podwójna szansa X2 (Celta lub remis) | 90,5% | 1.10 | 1.03 | -7% | średnia (poniżej progu fair 1.15) |
| Over 1.5 | 82% | 1.22 | 1.12 | -8% | średnia |
| Over 2.5 / Under 2.5 | 60% / 40% | 1.67 / 2.50 | 1.40 / 2.70 | -16% / +8% | niska-średnia |
| Over 3.5 / Under 3.5 | 37% / 63% | 2.70 / 1.59 | 2.00 / 1.70 | -26% / +7% | niska |
| BTTS tak / nie | 46% / 54% | 2.17 / 1.85 | 1.82 / 1.87 | -16% / +1% | niska |
| Handicap Celta -1.5 / -2.5 | 51% / 31% | 1.96 / 3.2 | 1.64 / 2.55 | -16% / -21% | niska |
| Rożne, kartki | brak danych statystycznych Salamanki (4. liga), sędzia nieznany | - | - | - | brak typu |

**Statystyki drużyn:** Superbet nie ma średnich ani nieobecnych dla Salamanki (liga niskiego szczebla). Forma Salamanki: 3:1 Real Avila (wyjazd), 1:0 Gimnastica Segoviana (2 czerwone kartki), 1:2 Talavera, 1:1 Navalcarnero, 1:3 Sestao, 3:2 San Sebastian Reyes (zmienna forma). Celta: ostatnio 1:2 Union SG (LE), 0:3 Rayo, 0:0 Levante w lidze (wynik 8.11 wg Infobae), 2:1 w Celticu - dobre wyniki w LE, słabsza liga.
**H2H:** jedyny mecz - Copa del Rey 3.12.2024, Celta wygrała 7:0 w Salamance (stare, inny skład, waga niska).
**Informacje medialne:** Celta bez Sebastiána Cáceresa; Altay Bayindir ma zadebiutować w bramce; spodziewane rotacje: Faye (45 min w sezonie), Ribes i Germain Milla z rezerw (problemy kadrowe w pierwszym zespole), Driouech i Hugo Burcio w składzie, Radu zachowany na Ligę Europy (Infobae 12.11). Salamanca bez Asiera Domíngueza (złamana stopa). Ponad 8 500 sprzedanych biletów, boisko w dobrym stanie. Mecz odbywa się w piątek, kilka dni po meczu LE i ligowym; Celta ma kolejny mecz ligowy w weekend (rotacja prawdopodobna).
**Ryzyka:** (1) Puchary bez rewanżu z rotacją: obniżony pułap pewności o kilka pp (zastosowano -2 pp na awans i -2 pp na wygranej w 90'); (2) zmienna jakość dublerów Celty - mecz może być dłużej "otwarty", a Salamanka (Muniain: "musi być noc idealna") ma atut własnego stadionu; (3) wysoka liczba goli typowa przy takiej różnicy klas, ale rezerwy Celty mogą zakończyć mecz po 1-0.
**Rynek:** model w 90' zgodny z rynkiem (74,0% vs 74,1% bez marży); awans 83% vs rynek 84,3% bez marży (zbieżne). Model niższy na Over 2.5 (60% vs 65,9%) i total (3,1 vs ok. 3,4): różnica 6 pp wynika z rotacji (rezerwy), bez twardych danych kadrowych o brakach w ataku, więc nie schodzę dalej poniżej rynku. Brak value po stronie Celty (kursy krótkie, fair ≤1.20).

---

## 4. Dijon - Orleans (Coupe de France, 13.11, 20:00)

**Format:** jeden mecz, przy remisie dogrywka/karne; rynek "Awans" (Dijon 1.27, Orleans 3.35). Rozgrywki potwierdzone ogólnie przez Superbet ("Puchar Francji 26/27") i ran.joyn.de (7. runda); szczebel: Dijon gra obecnie z klubami Ligue 2 (Metz, Reims, Troyes, Rodez, Grenoble, Red Star), Orleans z klubami National (Bastia, Amiens, Valenciennes, Villefranche, Quevilly, Cannes) - to wniosek z listy przeciwników, nie potwierdzony tabelą.
**Typ:** Dijon awansuje | **p:** 72% | **fair:** 1.39 | **Pewność:** średnia (puchar, rotacja nieznana). Kurs 1.27 poniżej fair (EV -8,5%), bez value.
**λ:** Dijon 1,85 / Orleans 1,00 (łącznie 2,85; rynek ok. 2,75). Wynik w 90': Dijon 57,3%, remis 22,6%, Orleans 20,1%.

| Rynek | p | fair | Kurs Superbet | EV | Pewność |
|---|---|---|---|---|---|
| Dijon awansuje / Orleans awansuje | 72% / 28% | 1.39 / 3.57 | 1.27 / 3.35 | -8% / -6% | średnia |
| 1 / X / 2 (90 min) | 57,3% / 22,6% / 20,1% | 1.75 / 4.43 / 4.97 | 1.48 / 4.20 / 5.20 | -15% / -5% / +4% | średnia |
| 1X / X2 / 12 | 79,9% / 42,7% / 77,4% | 1.25 / 2.34 / 1.29 | 1.10 / 2.32 / 1.16 | -12% / -1% / -10% | średnia |
| Over 1.5 | 77,7% | 1.29 | 1.15 | -11% | średnia |
| Over 2.5 / Under 2.5 | 54,2% / 45,8% | 1.84 / 2.19 | 1.58 / 2.17 | -14% / -1% | średnia |
| Over 3.5 / Under 3.5 | 31,9% / 68,1% | 3.13 / 1.47 | 2.42 / 1.45 | -23% / -1% | niska |
| BTTS tak / nie | 53,3% / 46,7% | 1.88 / 2.14 | 1.70 / 2.02 | -9% / -6% | średnia |
| Handicap Dijon -1.5 / Orleans +1.5 | 33,1% / 66,9% | 3.02 / 1.49 | - | - | niska |
| Rożne (linia 9.5) | brak danych statystycznych | - | Over 9.5 1.65 / Under 2.07 | - | brak typu |
| Kartki | brak danych, sędzia nieznany | - | - | - | brak typu |

**Statystyki drużyn (Superbet, ostatnie 6):** Dijon: 1:0 Red Star, 3:1 Grenoble (wyjazd), 1:2 Rodez, 2:4 Reims (wyjazd), 4:2 Metz, 2:2 Troyes - 13 goli strzelonych, 11 straconych (2,2 / 1,8), wiele goli w obu kierunkach. Orleans: 2:2 Valenciennes (wyjazd), 1:1 Villefranche, 2:3 Quevilly (wyjazd), 1:1 Bastia (wyjazd), 0:0 Cannes, 0:2 Amiens (wyjazd) - 6 strzelonych, 9 straconych (1,0 / 1,5), bilans 0W 4D 2L (bez zwycięstwa).
**H2H:** Dijon dominuje: bilans od 2018 4W 2D 0L; ostatnie: 3:2 (15.05.2026), 2:1 wyjazd (08.2025), 2:2, 1:1, 1:0, 2:1 wyjazd; wszystkie ostatnie spotkania były bramkowe (średnio 3,0 gola na mecz). Orleans nigdy nie wygrał w tym zestawieniu.
**Informacje medialne:** brak danych o nieobecnych i składach (niedostępne dla Pucharu Francji w Superbet); w sieci nie znalazłem zapowiedzi przedmeczowej. Trenerzy: Baptiste Ridira (Dijon), Jocelyn Precheur (Orleans). Brak informacji o rotacji w Dijon (Ligue 2 w trakcie ligi).
**Ryzyka:** (1) w pucharze gospodarz z wyższej ligi może rotować, a Orleans ma nieprzegraną serię 4 remisów w 6 meczach; (2) zawodnicy Dijon tracą dużo goli (1,8/mecz), co daje Orleans szansę na gola (BTTS 53%); (3) dogrywka i karne ocieniają awans bardziej niż wynik 90' (rozstrzygnięcie remisu ok. 60/40 dla Dijon).
**Rynek:** model nieco niższy od rynku na 1 (57,3% vs 61,1% bez marży) i Over 2.5 (54,2% vs 57,9%): różnica < 5 pp, bez dodatkowej informacji nie schodzę niżej. Awans Dijon 72% vs 72,5% rynku. Brak value w głównych rynkach; jedyny dodatni EV (Orleans wygra w 90' +4%) mieści się w błędzie modelu i nie jest rekomendacją.

---

## Podsumowanie - kandydaci do kuponu (po filtrze fair > 1.15)

| Mecz | Rynek | p | fair | Kurs Superbet | Pewność | Zależy od |
|---|---|---|---|---|---|---|
| Znicz - Sokół | 1X | 78,5% | 1.27 | 1.16 | średnia | składu, brak sędziego |
| Znicz - Sokół | Over 1.5 | 82,2% | 1.22 | 1.12 | średnia | formy ataku Znicza |
| Leganes - Burgos | Under 3.5 | 79,9% | 1.25 | 1.23 | średnia | składów (Morata), sędziego |
| Salamanca - Celta | Celta awansuje | 83% | 1.20 (graniczny) | 1.09 | średnia | rotacji Celty |
| Dijon - Orleans | Dijon awansuje | 72% | 1.39 | 1.27 | średnia | rotacji, dogrywki |
| Dijon - Orleans | Dijon 1X | 79,9% | 1.25 | 1.10 | średnia | składu |

Żaden z kursów Superbet nie ma dodatniego EV przy własnym p (poniżej fair we wszystkich głównych rynkach); najbliżej zera: Leganes Under 3.5 (EV -2%), Leganes Under 2.5 (-3%), Burgos win (+2%, niska pewność), Salamanca-Celta Under 3.5 (+7%, niska pewność, rynek 10 pp niżej od modelu z powodu rotacji). Rynki rożnych i kartek: tylko Leganes - Burgos ma jakiekolwiek dane (jedno źródło średnich + proxy sędziego), więc bez rekomendacji.

To są oszacowania probabilistyczne, nie gwarancje.
