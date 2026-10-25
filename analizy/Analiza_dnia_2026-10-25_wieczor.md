# Analiza dnia 25.10.2026, wieczór (18:00 – 26.10 06:00, czas polski CET)

**Źródła danych:** WebSearch, ESPN API, BettingPros API (serwer `sportsdata` się nie połączył). Betclic.pl i gg397.bet odrzucają połączenia z tego serwera (CloudFront 403). Kursy do kuponów pochodzą z BettingPros (book podany przy nodze), nie z Betclic.
**Czas:** od 25.10 obowiązuje CET (UTC+1); USA jeszcze w EDT, więc 19:00 ET = 00:00 CET.
**Stan na:** 25.10, ok. 08:00. Składy, bramkarze NHL i injury reporty NBA trzeba potwierdzić przed startem.

## Terminarz (niedziela 25.10, czas polski)

**Piłka nożna**
- 18:00 Lecce – Juventus | Serie A, 8. kolejka
- 18:30 Real Sociedad – Levante | La Liga, 10. kolejka
- 20:45 Udinese – AC Milan | Serie A, 8. kolejka (dopisany po terminarzu BettingPros; gospodarz Udinese)
- ~~20:45 PSG – Olympique Lyon~~: **przełożony na pon. 26.10, 20:30** (zakaz prefektury); analiza w sekcji piłki, ale poza okresem kuponów
- 21:00 FC Barcelona – Real Madryt | La Liga, 10. kolejka (El Clásico)

**E-sport**
- LoL Worlds 2026, Swiss R3: 18:00 HLE – IG (Bo1, 1-1), 19:00 G2 – TES (Bo1, 1-1), 20:00 KOI – DK (Bo3, mecz o awans 2-0), 23:00 Gen.G – LYON (Bo3, mecz o awans 2-0)
- 18:00 CS2 PGL Masters Bucharest, Swiss R2 (bo3): FURIA – NAVI, Legacy – DENDELE

**NHL** (sezon zasadniczy)
- 20:00 Panthers @ Blackhawks (15:00 ET)
- 23:00 Islanders @ Stars (18:00 ET) (nie Rangers)
- 00:00 26.10 Canadiens @ Jets (19:00 ET 25.10), Heritage Classic na otwartym stadionie, Princess Auto Stadium
- 01:00 Avalanche @ Predators (20:00 ET)
- 03:00 Wild @ Canucks (22:00 ET)

**NBA** (sezon zasadniczy)
- 22:00 Lakers @ Jazz (17:00 ET)
- 23:00 Pacers @ Nets (18:00 ET)
- 00:00 26.10 Clippers @ Thunder, Magic @ Knicks, Raptors @ Timberwolves (19:00 ET 25.10)
- 00:30 Pistons @ 76ers (19:30 ET)
- 02:00 Grizzlies @ Kings (21:00 ET)

**Pominięte / brak:** tenis (finały w Lyonie, Brukseli, Ałmaty, Ningbo i Osace w dzień; turnieje w Wiedniu i Bazylei startują 26.10), MMA (brak gali UFC/KSW 25.10), piłka przed 18:00 (m.in. Legia – Lech 17:30, Liverpool – Brighton 15:00, Sunderland – Leeds 17:30, mecze Bundesligi), Dota 2 (brak tier-1 wieczorem).

**Źródła terminarza (WebSearch):** [cope.es](https://www.cope.es/programas/tiempo-de-juego/noticias/laliga-confirma-horarios-10a-jornada-clasico-domingo-25-octubre-21-00h-20260921_3440773.html), [elimparcial.es](https://www.elimparcial.es/noticia/300249/deportes/laliga.-fechas-horarios-y-donde-ver-la-decima-jornada.html), [programmi.sky.it](https://programmi.sky.it/sport/calcio/serie-a/dove-vedere-lecce-juventus), [lephoceen.fr](https://www.lephoceen.fr/calendrier/ligue-1), [fr.firstsport.tv](https://fr.firstsport.tv/programme/2026-10-25), [footballwebpages.co.uk](https://www.footballwebpages.co.uk/premier-league/20261025), [starting11.com](https://starting11.com/fixtures/legia-warszawa-vs-lech-poznan), [Yahoo Sports](https://sports.yahoo.com/articles/sundays-time-schedule-022923357.html), [DirecTV](https://www.directv.com/insider/nba-games-on-tv-today/), [dailyfaceoff.com](https://www.dailyfaceoff.com/nhl-daily-schedule/2026-10-25), [ESPN NHL](https://www.espn.com/nhl/schedule), [Liquipedia LoL](https://liquipedia.net/leagueoflegends/World_Championship/2026/Swiss_Stage), [sheepesports.com](https://www.sheepesports.com/en/articles/worlds-2026-swiss-stage-round-3-draw/en), [esports.ru](https://esports.ru/counter-strike-2/tournaments/pgl-masters-bucharest-2026/).

## Analiza piłkarska B – niedziela 25.10.2026 (CET)

Skill: `football-analyst` (pełny przebieg: research → `poisson.py` / `markets.py` → Skalibruj).
Źródła: wyłącznie WebSearch (WebFetch/curl zablokowane, MCP `sportsdata` niedostępny, BettingPros pominięty zgodnie z poleceniem). Składy przewidywane, nie potwierdzone (wyjściowe składy ogłaszane ok. 1 h przed meczem).

---

### 18:00 Lecce – Juventus (Serie A, 8. kolejka)

**Kluczowe dane**
- Tabela: Lecce 11-12. miejsce, 9 pkt (3-0-4), gole 9:12 (Virgilio, Corriere dello Sport). U siebie 1-0-2: 0-4 Roma, 3-2 Monza, 1-2 Bologna (FootyStats, Sky) → 4:8 w 3 meczach domowych. Ostatnio 3-0 w Udine 18.10 (ANSA, ESPN).
- Juventus: 8-9. miejsce, 11 pkt po 7 meczach (3-2-2), gole 9:8 (Corriere dello Sport, Tuttosport). 18.10 przegrana 0-3 u siebie z Lazio (Sky, Corriere dello Sport); w czwartek 22.10 w LE 2-2 z Rennes (tuttojuve, calciolecce) – "jedno zwycięstwo w 5 meczach" (Statz). xG Juve 1,92/mecz, na wyjeździe 2,38, 17 strzałów/mecz (FootyStats, mała próba). 3 czyste konta w 7 meczach ligowych (Squawka). Lecce: niskie xG i ok. 2,6 celnych strzałów/mecz (FotMob).
- Rożne: Juventus lider ligi – 8,14 wykonywanych/mecz (Footiqo; statz.ai 8,1); Lecce 4,43 wykonywanych (Footiqo/statz.ai 4,4), u siebie 5,33 wykonywanych i 3,33 oddanych (Footiqo, 3 mecze).
- Kartki/faule: Lecce 2,0 kartki i 12,4 faulu/mecz (gambling.com, mała próba). Sędzia **Fabio Maresca** (Sky Sport, designacje 21.10): kariera ok. 2,4 + 2,5 żółtych/mecz (gospodarze/goście, 146 meczów, Pianetafanta – "fischietto facile"), 5,46 kartki/mecz (Valuestats, 25/26). Brak danych Juve o kartkach/faulach w tym sezonie.
- H2H (ostatnie ~2 lata): 09.05.2026 Lecce 0-1 Juventus (ESPN, Vlahović 1'), 03.01.2026 Juventus 1-1 Lecce (ESPN), 12.2024 Lecce 1-1 Juventus (TMW, Rebić 90+3'). Historycznie Juve dominuje (23-8-4, juventus.com), ale ostatnie mecze niskobramkowe i wyrównane.

**Newsy**
- Juventus – plaga kontuzji: poza grą Yildiz (powrót ok. końca XI), Thuram i Locatelli (raczej 2027), Ekhator, Grabara, Conceição, a po meczu z Rennes nowe urazy mięśniowe Nico Gonzáleza (~1 mies.) i Çelika (~3 tyg.) (Virgilio, calciolecce, DirettaFanta). Spalletti odwołał konferencję przedmeczową (tuttojuve, tribuna). Przewidywany skład 3-4-1-2: Vicario; Kalulu, Bremer, Lucumí; McKennie, Douglas Luiz, Sarr, Cambiaso; Alajbegović; Woltemade, Kolo Muani (Sky, SOS Fanta, DirettaFanta).
- Lecce (4-3-3): Falcone; Veiga, Gaspar, Tiago Gabriel, Gallo; Kaba, Ngom, Maleh; N'Dri, Geubbels, Fatah. Nieobecni: Coulibaly, Ilić, Berisha, Pierotti (calciolecce, DirettaFanta).
- Juve grała w czwartek (u siebie, bez podróży), Lecce miało pełny tydzień.

**Rynek (kontrola, przed meczem)**: 1X2 1.48 (Ladbrokes) / 4.33 (Coral) / 8.00 (bet365) wg Statz → po usunięciu marży ok. 12% / 22% / 65,5%. Over 2.5 1.80 i BTTS tak 2.00 (bet365 wg Statz); Over 2.5 1.87 (Footballwhispers). Juve wygra do zera 13/10 = 2.30 (William Hill wg Squawka).

**λ i kalibracja**: bazowo z formy wychodziło λ 0,85 / 1,65 (Juve 56%, −9,5 pp pod rynek). Reguła "nie schodź pod rynek > 5 pp bez konkretnej informacji": konkretna informacja jest (8 absencji, 2 nowe urazy, mecz w czwartek), ale rynek ją zna, więc podniesiono do **λ Lecce 0,80 / Juventus 1,80** → Juve 61,1% (−4,4 pp pod rynek). Forma Juve (1 wygrana w 5) nie obniża p faworyta (reguła z TOP5 09.10). Lecce nie jest w kryzysie (wygrana 3-0 tydzień temu) – bez korekty kryzysowej. Łączne λ 2,6, Over 2.5 48% vs rynek ok. 52% (bez marży z 1.80 przy nieznanym Under) – różnica w granicach 5 pp.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 Lecce | 16,2% | 6.17 | średnia |
| X | 22,6% | 4.42 | średnia |
| 2 Juventus | 61,1% | 1.64 | średnia |
| 1X | 38,9% | 2.57 | średnia |
| X2 | 83,8% | 1.19 (graniczny 1.15-1.20) | średnia |
| 12 | 77,3% | 1.29 | niska |
| Over 1.5 | 73,3% | 1.36 | średnia |
| Under 1.5 | 26,7% | 3.74 | średnia |
| Over 2.5 | 48,2% | 2.08 | średnia |
| Under 2.5 | 51,8% | 1.93 | niska (≈ rynek, wyrównane) |
| Over 3.5 | 26,4% | 3.79 | średnia |
| Under 3.5 | 73,6% | 1.36 | średnia |
| BTTS tak | 46,0% | 2.18 | średnia |
| BTTS nie | 54,0% | 1.85 | niska/średnia |
| Juventus Over 0.5 gola | 83,5% | 1.20 (graniczny) | średnia |
| Juventus Over 1.5 gola | 53,7% | 1.86 | niska |
| Lecce Over 0.5 gola | 55,1% | 1.81 | niska |
| Lecce Under 1.5 gola | 80,9% | 1.24 | średnia |
| Juventus wygra do zera | 37,5% | 2.67 | niska (rynek 2.30) |
| Wynik 0-1 / 0-2 / 1-1 | 13,4% / 12,0% / 10,7% | 7.48 / 8.31 / 9.35 | niska |
| Rożne Over 8.5 (śr. 9,8) | 62,1% | 1.61 | niska |
| Rożne Over 9.5 | 50,6% | 1.98 | niska |
| Rożne Under 10.5 | 60,6% | 1.65 | niska |
| Juventus rożne Over 4.5 (śr. 6,0) | 68,5% | 1.46 | niska/średnia |
| Juventus rożne Over 5.5 | 53,7% | 1.86 | niska |
| Kartki (żółte=1) Over 3.5 (śr. 4,8, Maresca) | 66,5% | 1.50 | niska/średnia |
| Kartki Over 4.5 | 50,2% | 1.99 | niska |
| Kartki Under 5.5 | 64,8% | 1.54 | niska |
| Faule Over 21.5 (śr. 24,5) | 70,4% | 1.42 | niska (brak danych Juve) |
| Faule Over 23.5 | 55,9% | 1.79 | niska |

Średnie dodatkowe: rożne Juve 6,0 (8,1 wykonywanych vs 3,33 oddanych przez Lecce u siebie, korekta w górę za przewagę) + Lecce 3,8 = 9,8; kartki 4,8 (Maresca ok. 4,9 żółtych/mecz w karierze, Lecce 2,0/mecz, liga ok. 4,3 → podbite za surowego sędziego, ale dane sezonu 26/27 sprzeczne); faule z Lecce 12,4 + szacunek Juve ok. 12. Rynki zawodnika: brak (składy niepotwierdzone, brak średnich per 90 z dwóch źródeł) – nie wyceniam.

**Ryzyka**
- Remis (22,6%): Juve osłabiona, mało kreatywna bez Yildiza/Conceição, 2 z 3 ostatnich H2H to 1-1; zmęczenie po czwartku.
- Wygrana Lecce (16,2%): Lecce w dobrym momencie (3-0 w Udine), N'Dri/Geubbels szybcy w kontrze, Juve po 0-3 z Lazio psychicznie chwiejna.
- Under 3.5 przegrywa przy rozbitej obronie Lecce u siebie (0-4 z Romą, 8 straconych w 3 meczach domowych).
- Kartki: dane Maresci w sezonie 26/27 sprzeczne (1 mecz, 8 kartek vs średnie kariery) – pewność ograniczona.

**Typy z p>50% i fair>1.15**
- Under 3.5 – 73,6% / 1.36 (średnia)
- Over 1.5 – 73,3% / 1.36 (średnia)
- Lecce Under 1.5 gola – 80,9% / 1.24 (średnia)
- Juventus (2) – 61,1% / 1.64 (średnia)
- X2 – 83,8% / 1.19 (graniczny), Juventus Over 0.5 gola – 83,5% / 1.20 (graniczny)
- Juventus rożne Over 4.5 – 68,5% / 1.46 (niska/średnia)
- Kartki Over 3.5 – 66,5% / 1.50 (niska/średnia; zależy od Maresci)
- Faule Over 21.5 – 70,4% / 1.42 (niska – nie na kupon główny)
- Rożne Over 8.5 – 62,1% / 1.61 (niska), Under 10.5 – 60,6% / 1.65 (niska)
- BTTS nie – 54,0% / 1.85 (niska/średnia), Juventus Over 1.5 gola – 53,7% / 1.86 (niska), Under 2.5 – 51,8% / 1.93 (niska, brak mocnego typu na total 2.5)
- **Najlepszy rynek meczu:** Under 3.5 / Lecce Under 1.5 gola (spójne z niskobramkowymi H2H i niskim xG Lecce); wynikowo Juventus 1.64 fair vs rynek ok. 1.48 – brak value po kursie.

---

### 18:30 Real Sociedad – Levante (La Liga, 10. kolejka)

**Kluczowe dane**
- Tabela: Real Sociedad 5. miejsce, 16 pkt (5-1-3), gole 17:17 (Wikipedia, Fox Sports, LaLiga.com). U siebie 2-1-1: 2-1 Espanyol, 0-0 Celta, 0-3 Atlético, 3-2 Deportivo (Fox, LaLiga.com) → 7:6. Ostatnio 5-2 w Maladze 18.10; 18 goli w ostatnich 5 meczach (Infobae/EFE). W czwartek 22.10 w LE 6-0 na wyjeździe z Lillestrøm (Infobae; mecz w Norwegii o 21:00 – podróż), wcześniej 1-1 z Union SG.
- Levante: 11. miejsce, 10 pkt po 9 meczach (2-4-3), gole 15:17 (Fichajes; inne tabele 7 pkt – sprzeczność, przyjęto 10 pkt jako zgodne z wynikami). Ostatnio 3-1 z Athletic 21.10 (LaLiga.com), wcześniej 3-3 z Sevillą, 1-1 z Deportivo; 5-2 z Betisem w sierpniu. **Bez zwycięstwa na wyjeździe w tym sezonie** (casasdeapuestas/legalbet). Mecze Levante bramkostrzelne (3,6 gola/mecz).
- Rożne: Real Sociedad 7,0 wykonywanych / 4,89 oddanych (Footiqo, 9 meczów), u siebie 8,5 wykonywanych (Betaminic, 4 mecze); mecze RS śr. 12,25 rożnych (Apwin). Levante 3,29 wykonywanych / 5,29 oddanych (Betaminic), mecze Levante śr. 8,58 rożnych (Apwin).
- Kartki/faule: RS ok. 1,9-2,0 żółtych i 12,2-12,4 faulu/mecz (LaLiga.com, 2 snapshoty). Levante – brak wiarygodnych danych. Sędzia **Javier Alberola Rojas**, VAR Guillermo Cuadra (OneFootball, 25.10; brak potwierdzenia w komunikacie CTA): 4,14 żółtych i 0,24 czerwonych/mecz w 25/26 (Fichajes, 21 meczów); 3,25 żółtych (Valuestats, 60 meczów) – źródła sprzeczne.
- H2H: RS wygrała 3 ostatnie mecze ligowe z Levante na Anoecie bez straty gola (casasdeapuestas/legalbet), m.in. 2-0 w IV 2026 (Statmuse); bilans 38 meczów 14-12 dla RS (Infobae).

**Newsy**
- Real Sociedad (Pellegrino Matarazzo): niemal pełna kadra; poza grą Odriozola (więzadło krzyżowe), wg innego źródła także Luken Beitia; Yangel Herrera wątpliwy/trenował z grupą (Comuniate, Infobae). Przewidywany skład: Remiro; Fort, Jon Martín, Sarr, Sergio Gómez; Gorrotxategi, Soler, Sučić; Barrenetxea, Oyarzabal, Guedes – alternatywnie Kubo w składzie, Óskarsson obok Oyarzabala (Comuniate, OneFootball). Sučić najlepszy strzelec ligowy RS (3 gole, Squawka). Możliwa częściowa rotacja po czwartku w Norwegii.
- Levante (Luis Castro): bez Enzo Bardelliego (uraz mięśniowy) i stopera Deli. Ryan w bramce, w ataku Brugué i Iván Romero, możliwy Nacho Pérez na prawej (Infobae, Comuniate).

**Rynek (kontrola)**: 1X2 1.65 / 4.30 / 4.80 (Legalbet) → bez marży ok. 58% / 22% / 20%; RS 1.57-1.80 w różnych źródłach, 4/6 = 1.67 (William Hill wg Squawka). Over 2.5 1.57 (bet365 wg Statz), 1.72 (EaglePredict), 1.75 (Eurosport). Modele: Statz 57/22/21, Dimers 56-58% RS, Forebet 40% RS.

**λ i kalibracja**: RS w domu 1,75 gola/mecz, Levante traci 1,89/mecz i nie wygrywa na wyjeździe; Levante strzela 1,67/mecz, RS traci 1,89. Bazowo λ 1,75 / 1,15 (RS 51%, −7 pp pod rynek) → reguła ">5 pp pod rynek tylko z konkretem": jedynym konkretem jest czwartkowy mecz w Norwegii i forma Levante (oba częściowo w kursie), więc **λ Real Sociedad 1,85 / Levante 1,10** → RS 54,9% (−3 pp pod rynek). Levante nie jest w kryzysie (wygrana 3-1 z Athletic) – bez korekty kryzysowej. Over 2.5 56,6% vs rynek ok. 58-61% (bez marży) – w granicach; nie podnoszę.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 Real Sociedad | 54,9% | 1.82 | średnia |
| X | 22,7% | 4.41 | średnia |
| 2 Levante | 22,4% | 4.47 | średnia |
| 1X | 77,6% | 1.29 | średnia |
| X2 | 45,1% | 2.22 | średnia |
| 12 | 77,3% | 1.29 | średnia |
| Over 1.5 | 79,3% | 1.26 | średnia/wysoka |
| Under 1.5 | 20,7% | 4.84 | średnia |
| Over 2.5 | 56,6% | 1.77 | średnia |
| Under 2.5 | 43,4% | 2.30 | średnia |
| Over 3.5 | 34,2% | 2.93 | średnia |
| Under 3.5 | 65,8% | 1.52 | średnia/niska (Levante 3,6 gola/mecz) |
| BTTS tak | 56,2% | 1.78 | średnia |
| BTTS nie | 43,8% | 2.28 | średnia |
| Real Sociedad Over 0.5 gola | 84,3% | 1.19 (graniczny) | średnia |
| Real Sociedad Over 1.5 gola | 55,2% | 1.81 | średnia/niska |
| Levante Over 0.5 gola | 66,7% | 1.50 | średnia |
| Levante Over 1.5 gola | 30,1% | 3.32 | niska |
| Wynik 1-1 / 2-1 / 1-0 / 2-0 | 10,7% / 9,9% / 9,7% / 9,0% | 9.39 / 10.15 / 10.33 / 11.16 | niska |
| Rożne Over 8.5 (śr. 10,6) | 70,2% | 1.42 | niska/średnia |
| Rożne Over 9.5 | 59,4% | 1.68 | niska |
| Rożne Over 10.5 | 48,3% | 2.07 | niska |
| Real Sociedad rożne Over 4.5 (śr. 6,6) | 75,6% | 1.32 | średnia/niska |
| Real Sociedad rożne Over 5.5 | 62,0% | 1.61 | niska |
| Kartki (żółte=1) Over 3.5 (śr. 4,3, Alberola) | 58,8% | 1.70 | niska |
| Kartki Under 4.5 | 58,0% | 1.72 | niska |
| Kartki Under 5.5 | 72,2% | 1.39 | niska |
| Faule Over 21.5 (śr. 24,0) | 67,1% | 1.49 | niska (brak danych Levante) |
| Faule Over 23.5 | 52,2% | 1.92 | niska |

Średnie dodatkowe: rożne RS 6,6 (8,5 u siebie wykonywanych vs 5,29 oddawanych przez Levante, zbite za możliwą rotację) + Levante 4,0 = 10,6; kartki 4,3 (Alberola 3,25-4,14 żółtych, RS 1,9-2,0, La Liga ok. 4,5-5 – mecz bez stawki derbowej); faule RS 12,2 + szacunek Levante 12. Rynki zawodnika: brak wyceny (składy przewidywane z rozbieżnościami Kubo/Óskarsson/Sučić; kontrola rynku: Sučić gol lub asysta 21/20 = 2.05 Betfred wg Squawka, Barrenetxea gol +260 = 3.60 wg SportsGambler).

**Ryzyka**
- Remis (22,7%): Levante w formie (3-1 z Athletic, 3-3 z Sevillą), RS straciła 17 goli w 9 meczach; 1-1 to najczęstszy wynik modelu (i wg Dimers).
- Wygrana Levante (22,4%): zmęczenie RS po czwartku w Norwegii i możliwa rotacja, szybkie kontry Brugué/Romero na wysoko grającą obronę RS.
- Over 1.5 przegrywa przy zamkniętym meczu po rotacji (RS 0-0 z Celtą u siebie).
- Kartki: sędzia potwierdzony tylko przez jedno źródło medialne, średnie sprzeczne – wyłącznie niska pewność.

**Typy z p>50% i fair>1.15**
- Over 1.5 – 79,3% / 1.26 (średnia/wysoka)
- 1X – 77,6% / 1.29 (średnia); 12 – 77,3% / 1.29 (średnia)
- Real Sociedad rożne Over 4.5 – 75,6% / 1.32 (średnia/niska)
- Rożne Over 8.5 – 70,2% / 1.42 (niska/średnia)
- Levante Over 0.5 gola – 66,7% / 1.50 (średnia)
- Under 3.5 – 65,8% / 1.52 (średnia/niska)
- Faule Over 21.5 – 67,1% / 1.49 (niska – nie na kupon główny)
- Real Sociedad rożne Over 5.5 – 62,0% / 1.61 (niska); Rożne Over 9.5 – 59,4% / 1.68 (niska)
- Kartki Over 3.5 – 58,8% / 1.70 (niska); Kartki Under 5.5 – 72,2% / 1.39 (niska)
- Over 2.5 – 56,6% / 1.77 (średnia); BTTS tak – 56,2% / 1.78 (średnia)
- Real Sociedad Over 1.5 gola – 55,2% / 1.81; Real Sociedad (1) – 54,9% / 1.82 (średnia; vs rynek 1.65 – brak value)
- Real Sociedad Over 0.5 gola – 84,3% / 1.19 (graniczny)
- **Najlepszy rynek meczu:** Over 1.5 oraz Levante strzeli (66,7%) – oba zespoły tracą i strzelają regularnie; wynik 1 bez wartości względem kursu rynkowego.

---

## Tabela kandydatów (dla bet-slip-builder)

| Mecz | Rynek | p | fair | pewność | zależy od | kurs rynkowy znany |
|---|---|---|---|---|---|---|
| Lecce – Juventus | Under 3.5 | 73,6% | 1.36 | średnia | brak | nie |
| Lecce – Juventus | Lecce Under 1.5 gola | 80,9% | 1.24 | średnia | skład Lecce | nie |
| Lecce – Juventus | Over 1.5 | 73,3% | 1.36 | średnia | – | nie |
| Lecce – Juventus | Juventus (2) | 61,1% | 1.64 | średnia | skład Juve | tak: 1.48 (Ladbrokes, Statz) – EV < 0 |
| Lecce – Juventus | Juventus rożne Over 4.5 | 68,5% | 1.46 | niska/średnia | skład, styl Spallettiego | nie |
| Lecce – Juventus | Kartki Over 3.5 | 66,5% | 1.50 | niska/średnia | Maresca | nie |
| Real Sociedad – Levante | Over 1.5 | 79,3% | 1.26 | średnia/wysoka | rotacja RS | nie |
| Real Sociedad – Levante | 1X | 77,6% | 1.29 | średnia | rotacja RS | nie |
| Real Sociedad – Levante | Real Sociedad rożne Over 4.5 | 75,6% | 1.32 | średnia/niska | skład RS | nie |
| Real Sociedad – Levante | Levante Over 0.5 gola | 66,7% | 1.50 | średnia | – | nie |
| Real Sociedad – Levante | Over 2.5 | 56,6% | 1.77 | średnia | – | tak: 1.57 (bet365, Statz) / 1.75 (Eurosport) |
| Real Sociedad – Levante | Real Sociedad (1) | 54,9% | 1.82 | średnia | rotacja RS | tak: 1.65 (Legalbet) – EV < 0 |

Ograniczenia: brak MCP i WebFetch – statystyki rożnych/kartek/fauli z pojedynczych agregatorów (Footiqo, Betaminic, Apwin, gambling.com, LaLiga.com), często sprzecznych i z małych prób; rynki dodatkowe maksymalnie niska/średnia pewność. Składy nie potwierdzone. To oszacowania probabilistyczne, nie gwarancje.
### 20:45 Udinese – AC Milan (Serie A, 8. kolejka; gospodarz Udinese)

> **UWAGA – gospodarz:** wg ESPN (event 401874779, "AC Milan at Udinese", Stadio Friuli/Bluenergy Stadium, Udine) oraz Agimeg/Eurosport/pianetamilan/trivenetogoal mecz to **Udinese – AC Milan**, gospodarzem jest **Udinese**. Wszystkie liczby poniżej liczone dla Udinese u siebie, Milan na wyjeździe. Przy rozliczaniu typów "1"/"2" u bukmachera: 1 = Udinese, 2 = Milan.

**Typ główny:** Milan lub remis (X2) | **p:** 76.6% | **Fair:** 1.31 | **Pewność:** średnia
**Najlepsze rynki meczu:** X2, Over 1.5 gola, Udinese Under 1.5 gola, Under 3.5; wynik wprost (Milan 52.6%) – brak mocnego typu.

#### Kluczowe dane (źródła)
- **Tabela (ESPN standings):** Milan 5. – 7 meczów 4-3-0, gole 14:7, 15 pkt (forma DWWDW w lidze/Europie). Udinese 16. – 7 meczów 1-1-5, 9:16, 4 pkt; **4 porażki ligowe z rzędu** (Inter 3-5, Cagliari 0-1, Torino 1-2, Lecce 0-3 u siebie). Udinese u siebie 2:7 w 4 meczach.
- **Liga 2026/27 (ESPN):** 225 goli w 75 meczach = 3.0 gola/mecz (sezon bramkostrzelny).
- **Statystyki meczowe (ESPN boxscore, 7 meczów ligowych każdej drużyny):**
  - Milan: strzały 12.3 za / 9.6 przeciw, celne ok. 4.7 za; rożne 3.0 za / 3.1 przeciw (niskie); faule 9.3 własne / 12.0 rywala; żółte 1.86 własne / 1.43 rywala. Na wyjeździe: gole 6:5 w 4 meczach, rożne 3.75 za / 3.5 przeciw.
  - Udinese: strzały 14.3 za / 16.4 przeciw; rożne 3.9 za (1 mecz z 16, mediana ~2) / 5.7 przeciw; faule 11.0 / 8.9; żółte 1.86 / 0.43. U siebie: dużo strzałów (17, 10, 26, 14), ale mało celnych i goli; rożne przeciw 5.75.
  - Łącznie w meczach: Milan – rożne 6.1, faule 21.3, żółte 3.3, celne 8.3; Udinese – rożne 9.6, faule 19.9, żółte 2.3, celne 10.4.
- **xG:** brak dostępnych danych (FBref/Understat niedostępne w tej sesji) – obniżona pewność λ.
- **Sędzia:** Matteo Marcenaro (Genua), VAR Pezzuto (trivenetogoal, radiorossonera, Corriere dello Sport). Średnia kartek: KeplerQuant 4.96/mecz (50 meczów od 2021, +0.58 vs średnia), faule 24.2/mecz; FotMob 2026/27: 4.3 żółtej/mecz (2 mecze). Średnia ligi 2026/27: 3.61 kartek, 21.6 fauli (KeplerQuant). Sędziował w tym sezonie Lazio–Milan 2-2 (5 żółtych, ESPN).
- **H2H (ESPN, 5 ostatnich):** Milan–Udinese 0-3 (11.04.2026), Udinese–Milan 0-3 (20.09.2025), Udinese–Milan 0-4 (04.2025), Milan–Udinese 1-0 (10.2024), Udinese–Milan 2-3 (01.2024). Milan 4-1; w Udine Milan 3/3 wygranych. Waga niska–średnia (inni trenerzy: Amorim w Milanie od 2026/27).
- **Rynek (do kontroli, nie do kuponu):** DraftKings via ESPN: Udinese 4.20 / X 3.50 / Milan 1.80, O/U 2.5: 1.87/1.91. Włoscy bukmacherzy (Agimeg, quotescommessecalcio): Milan 1.67–1.70, X ~3.90, Udinese 5.00–5.50; Over 2.5 1.81–1.87, Under 1.86–1.92; Over 1.5 ~1.25; Goal 1.80 / NoGoal 1.95. Bez marży: Milan ok. 51.5% (DK) – 57% (IT), średnio ~54–55%; Over 2.5 ~50%.

#### Newsy (kontuzje, składy, kontekst)
- **Milan (trener Rúben Amorim):** w czwartek 22.10 porażka 0-3 w Bournemouth (LE), czerwona kartka Maignana (~27') – w Serie A dostępny (zawieszenie tylko w LE). 3 dni odpoczynku + podróż z Anglii vs 7 dni Udinese (Agimeg). Nieobecni pewni: Saelemaekers, Gabbia, Chukwueze, Terracciano (pianetamilan, DAZN, radiorossonera). **Sprzeczne doniesienia:** Rabiot, Gila, Moreira – wg MilanNews/allmilan/radiorossonera poza kadrą, wg calciomercato/TMW w składzie. Gonçalo Ramos: rezonans bez urazu łydki, wrócił do treningów, kandydat do składu (gianlucadimarzio, milanisti channel), ale wg części źródeł może odpocząć. Brak konferencji Amorima przed meczem (MilanPress). Przewidywane ustawienie 3-4-2-1 lub 4-2-3-1: Maignan; De Winter, Pavlović, (Gila/Tomori); Musah, Modrić; Pulisic, Loftus-Cheek/Rabiot, Cissé; Ramos/Camarda. Liczba nieobecnych ~7 (radiorossonera).
- **Udinese (Kosta Runjaić):** Alaba (uraz z meczu z Lecce), Gueye, Bayo, Zanoli (nawrót urazu) – out; Solet niepewny (problem mięśniowy); Zaniolo wraca, ale na ławkę (konferencja Runjaicia 24.10, fantacalcio/diariofvg/sosfanta). Brak zawieszeń. 3-4-2-1: Okoye; …; Ekkelenkamp, Chakvetadze/Zaniolo; Davis. Runjaić: mecz z Lecce "najgorszy w trzy lata", klub potwierdził zaufanie do trenera – presja/kryzys (5 porażek z rzędu we wszystkich rozgrywkach wg części źródeł).
- Niepotwierdzone składy – oficjalne ~1h przed meczem.

#### λ i model
- Baza: liga 3.0 gola/mecz (ok. 1.6 dom / 1.4 wyjazd). Siły z 7 meczów regresowane o 50% do średniej (mała próba): Milan atak ~1.17, Udinese obrona ~1.26 → ~2.06; korekta za zmęczenie po LE (czwartek, wyjazd do Anglii) i absencje (Saelemaekers, Gabbia, możliwi Rabiot/Gila, Ramos niepewny) ok. −10%, dociągnięcie do rynku (total ~2.6–2.7) → **λ Milan = 1.70**.
- Udinese: atak u siebie słaby (2 gole w 4 meczach mimo wielu strzałów), Milan traci 1.0/mecz; brak Alaby dotyczy obrony. → **λ Udinese = 1.05**. Łącznie 2.75.
- `poisson.py 1.05 1.70`; `markets.py` dla rożnych 8.3, kartek 3.7, fauli 22.5, strzałów 26, celnych 9.0, gole drużyn.

#### Tabela wszystkich rynków

| Rynek | p | Fair odds | Pewność |
|---|---|---|---|
| 1 (Udinese) | 23.4% | 4.28 | średnia |
| X | 24.0% | 4.16 | średnia |
| 2 (Milan) | 52.6% | 1.90 | średnia-niska (brak mocnego typu) |
| 1X (Udinese lub remis) | 47.4% | 2.11 | średnia |
| X2 (Milan lub remis) | 76.6% | 1.31 | średnia |
| 12 (bez remisu) | 76.0% | 1.32 | średnia-niska |
| Milan DNB (zakład bez remisu) | 69.2% | 1.45 | średnia |
| Over 1.5 gola | 76.0% | 1.32 | średnia |
| Under 1.5 gola | 24.0% | 4.17 | średnia |
| Over 2.5 gola | 51.9% | 1.93 | niska (≈ rynek) |
| Under 2.5 gola | 48.1% | 2.08 | niska |
| Over 3.5 gola | 29.7% | 3.37 | średnia |
| Under 3.5 gola | 70.3% | 1.42 | średnia |
| BTTS tak | 53.1% | 1.88 | niska |
| BTTS nie | 46.9% | 2.13 | niska |
| Milan Over 0.5 gola | 81.7% | 1.22 | średnia |
| Milan Over 1.5 gola | 50.7% | 1.97 | niska |
| Milan Under 2.5 gola | 75.7% | 1.32 | średnia-niska |
| Udinese Over 0.5 gola | 65.0% | 1.54 | średnia-niska |
| Udinese Under 1.5 gola | 71.7% | 1.39 | średnia |
| Wynik 1-1 / 0-1 / 1-2 / 0-2 | 11.4% / 10.9% / 9.7% / 9.2% | 8.76 / 9.20 / 10.31 / 10.83 | niska |
| Rożne Over 7.5 (śr. 8.3) | 56.9% | 1.76 | niska |
| Rożne Over 8.5 | 44.4% | 2.25 | niska |
| Rożne Under 9.5 | 67.0% | 1.49 | niska |
| Rożne Under 10.5 | 76.6% | 1.31 | niska |
| Kartki Over 2.5 (śr. 3.7, ż=1) | 67.1% | 1.49 | niska-średnia |
| Kartki Over 3.5 | 48.4% | 2.07 | niska |
| Kartki Under 4.5 | 68.1% | 1.47 | niska |
| Kartki Under 5.5 | 80.5% | 1.24 | niska |
| Faule Over 20.5 (śr. 22.5) | 63.9% | 1.56 | niska |
| Faule Over 21.5 | 56.2% | 1.78 | niska |
| Faule Under 23.5 | 59.4% | 1.68 | niska |
| Strzały Over 22.5 (śr. 26) | 72.1% | 1.39 | niska |
| Strzały Over 24.5 | 58.8% | 1.70 | niska |
| Strzały celne Over 7.5 (śr. 9.0) | 66.0% | 1.52 | niska |
| Strzały celne Over 8.5 | 53.5% | 1.87 | niska |

Uwagi do rynków dodatkowych: rożne, faule, strzały i kartki tylko z jednego źródła statystyk meczowych (ESPN boxscore, 7 meczów), więc pewność niska. Kartki liczone jako żółte = 1 (czerwona to dodatkowo ok. +0.1 do średniej przy rozliczeniu "czerwona = 2"). Średnia kartek 3.7 łączy niską bazę drużyn (2.3–3.3 żółtych/mecz) z surowym sędzią (Marcenaro ~4.3–5.0 vs liga 3.6) i stawką: Milan po porażce i czerwonej kartce w LE, Udinese w desperacji. Rożne 8.3 są poniżej typowej średniej ligi, bo Milan bierze mało rożnych (3.0/mecz) i mało ich oddaje; z drugiej strony Udinese u siebie traci 5.75 rożnego.

#### Skalibruj (zastosowane reguły)
- **Ryzyko ma dwie twarze:** dla Milanu (52.6%) remis 24.0% i wygrana Udinese 23.4%, podobna waga.
- **Kryzys underdoga:** Udinese ma 4 porażki ligowe z rzędu i trener jest pod presją (desperacja i reakcja "pokażemy, że jesteśmy inną drużyną"). Różnica klas jest umiarkowana, więc nie ma "przepaści klas". Korektę ujęto w obniżeniu p Milanu do 52.6%, czyli ok. 2–3 pp poniżej średniej rynkowej (~55%).
- **Nie schodź pod rynek >5 pp bez konkretów:** −2–3 pp ma konkretne podstawy: mecz w czwartek w Anglii, 3 dni odpoczynku, 4 pewne absencje i 3 sporne (Rabiot, Gila, Moreira), Ramos niepewny. Nie obniżam więcej.
- **Total:** absencje Milanu dotyczą obu stron boiska, a sezon jest bramkostrzelny (3.0/mecz), więc nie wyciągam przewagi Under/Over nad rynkiem. Over 2.5 i BTTS ≈ 50–53%: brak typu.
- **Rynki dodatkowe:** sędzia znany, ale składy niepotwierdzone, więc pułap pewności to niska/średnia, bez "wysokiej". Surowy sędzia podniósł średnią kartek (z ~2.9 do 3.7), czyli zmienił liczbę, a nie tylko opis.
- **Rynki zawodnika:** pominięte, bo składy są niepotwierdzone (Ramos, Rabiot, Zaniolo z ławki).

#### Ryzyka
- **Milan nie wygrywa (47%):** (a) remis (24%), bo zmęczenie po LE, rotacja, Udinese gra zamknięty 3-4-2-1 i Milan ma niskie liczby rożnych i strzałów na wyjazdach (3 strzały z Juventusem); (b) wygrana Udinese (23%), bo reakcja po klęsce z Lecce, wynik 0-3 z ostatniego H2H na San Siro, a Milan po 0-3 w LE może być mentalnie rozbity.
- **X2 przegrywa** tylko przy wygranej Udinese: najważniejsze ryzyko to czerwona kartka lub rzut karny (Marcenaro często dyktuje karne: 22 w 66 meczach, StatsHub).
- **Over 1.5 przegrywa** przy 0-0, 1-0 lub 0-1 (24%): oba zespoły zmęczone lub ostrożne, Udinese słabe w ataku u siebie.
- **Udinese Under 1.5** przegrywa, jeśli Milan znów będzie tracił (Atalanta 3-2, Lazio 2-2), a defensywa Milanu bez Gabbii/Gili jest osłabiona.
- **Kartki:** wysokie p Over 2.5 i Under 4.5 na raz wynikają ze średniej 3.7 przy dużej wariancji. Surowy sędzia przemawia za Over, niska baza drużyn za Under.

#### Typy z p > 50% i fair > 1.15
| Rynek | p | Fair | Pewność | Od czego zależy |
|---|---|---|---|---|
| X2 (Milan lub remis) | 76.6% | 1.31 | średnia | skład Milanu (Rabiot/Ramos) |
| Over 1.5 gola | 76.0% | 1.32 | średnia | rynek ~1.25 (fair 1.32 > kurs, brak value) |
| 12 | 76.0% | 1.32 | średnia-niska | – |
| Under 10.5 rożnych | 76.6% | 1.31 | niska | jedno źródło statystyk |
| Udinese Under 1.5 gola | 71.7% | 1.39 | średnia | Zaniolo z ławki, Davis |
| Milan Under 2.5 gola | 75.7% | 1.32 | średnia-niska | – |
| Strzały Over 22.5 | 72.1% | 1.39 | niska | jedno źródło |
| Under 3.5 gola | 70.3% | 1.42 | średnia | – |
| Milan DNB | 69.2% | 1.45 | średnia | skład |
| Kartki Under 4.5 | 68.1% | 1.47 | niska | sędzia surowy (ryzyko) |
| Kartki Over 2.5 | 67.1% | 1.49 | niska-średnia | sędzia Marcenaro |
| Rożne Under 9.5 | 67.0% | 1.49 | niska | jedno źródło |
| Strzały celne Over 7.5 | 66.0% | 1.52 | niska | – |
| Udinese Over 0.5 gola | 65.0% | 1.54 | średnia-niska | – |
| Faule Over 20.5 | 63.9% | 1.56 | niska | sędzia 24.2 fauli/mecz |
| Rożne Over 7.5 | 56.9% | 1.76 | niska | – |
| BTTS tak | 53.1% | 1.88 | niska | blisko rynku, brak mocnego typu |
| Milan wygrana (2) | 52.6% | 1.90 | średnia-niska | rynek 1.67–1.80, brak value |
| Over 2.5 gola | 51.9% | 1.93 | niska | ≈ rynek |
| Milan Over 0.5 gola | 81.7% | 1.22 | średnia | przypadek graniczny (1.15–1.25) |

Najlepsze kandydatury na kupon: X2, Over 1.5 (sprawdzić, czy kurs > 1.32), Udinese Under 1.5, Under 3.5. Kursy na rynki dodatkowe nieznane; kursy do EV podaje orkiestrator.

Źródła: ESPN API (scoreboard, standings, summary/boxscore, odds DraftKings), trivenetogoal.it / radiorossonera.it / corrieredellosport.it (sędzia), KeplerQuant, FotMob, StatsHub (statystyki sędziego), pianetamilan.it, DAZN, radiorossonera.it, calciomercato.com, tuttomercatoweb.com, gianlucadimarzio.com, milanistichannel.com, MilanPress (Milan), fantacalcio.it, diariofvg.it, sosfanta.com, mondoudinese.it (Udinese), sportmediaset / Sky / Corriere dello Sport (Bournemouth–Milan 3-0), Agimeg, quotescommessecalcio.com (kursy IT).

*To oszacowania probabilistyczne, nie gwarancje.*
## Piłka nożna, część A: analiza meczów z 25.10.2026 (CET)

Skill: `football-analyst` (4 filary + `poisson.py`/`markets.py` + krok "Skalibruj"). Źródła: wyłącznie WebSearch (31 zapytań). MCP `sportsdata` nie połączył się (ENOENT), a WebFetch jest zablokowany, więc nie było pełnych statystyk xG, rożnych ani kartek z bieżącego sezonu. Wszędzie, gdzie brakuje danych, obniżam pewność. BettingPros nie był używany (zgodnie z poleceniem).

> **UWAGA: PSG – OL PRZENIESIONY.** Prefektura policji w Paryżu zakazała rozegrania meczu w niedzielę, a LFP 23.10 przełożyła go na **poniedziałek 26.10.2026, 20:30** na Parc des Princes (beIN Sports FR, Foot Mercato, Orange Sports). Mecz NIE odbędzie się 25.10. Analiza poniżej obowiązuje dla nowego terminu.

---

### 20:45 (przeniesiony na pon. 26.10, 20:30) PSG – Olympique Lyon (Ligue 1, 8. kolejka)

**Kluczowe dane**
- **Tabela po 7. kolejce:** Lyon 1. miejsce, 14 pkt (4-2-1, bramki 13-5, +8); PSG 2. miejsce, 14 pkt (+5). Pięć klubów ma po 14 pkt (Foot Mercato, Lensois, Mercatolive). PSG ma serię 4 zwycięstw (4 W i 1 P w ostatnich 5), ostatnio wygrał 3-1 w Strasburgu (Soccerway). Na początku sezonu PSG był słaby: po 4 meczach 5 pkt i bramki 6-6 (Foot Mercato, stats).
- **Puchary:** PSG pokonał Barcelonę 4-2 we wtorek 20.10 w LM (Al Jazeera, Fanatik; bramki: Doué, L. Hernández, Vitinha, Ruiz). Lyon grał w czwartek 22.10 w LE w Hoffenheim; przed tym meczem miał 100% bilans w fazie ligowej (Sports Mole), a wyniku nie znalazłem. PSG ma więc 2 dni więcej odpoczynku, a przełożenie meczu na poniedziałek daje obu drużynom dodatkowy dzień.
- **xG, strzały, rożne, kartki 2026/27:** brak danych w wynikach wyszukiwania. Jedyne liczby rożnych są historyczne (Lyon 6,0 rożnego na mecz w 2025, sportsgambler) i nie nadają się do kalibracji. Pewność rynków dodatkowych: niska.
- **H2H (ostatnie ~1 rok):** PSG – Lyon 1-2 (19.04.2026, Endrick, Afonso Moreira; Kvaratskhelia), Lyon – PSG 2-3 (09.11.2025) (sportytrader, ESPN, psg.fr). W obu meczach padło co najmniej 3 gole i obie drużyny strzeliły.
- **Sędzia:** nie znaleziono nominacji.

**Newsy (kadry)**
- PSG: **Kvaratskhelia** wypada na kilka miesięcy (zerwane więzadło krzyżowe), **Dembélé** ma uraz uda i nie zagra, **Marquinhos** ma uraz mięśnia uda, **Nuno Mendes** jest niedostępny (Foot-sur7, Maxifoot, VIPSG). Przewidywany skład: Safonov – Hakimi, Zabarnyi, Pacho, L. Hernández (lub Digne) – Zaïre-Emery, Vitinha, Ruiz – Akliouche, (G.) Ramos/Torres, Doué (Canal Supporters, VIPSG, But! FC). Atak jest uszczuplony, ale w tym samym składzie PSG strzelił Barcelonie 4 gole.
- Lyon (trener Paulo Fonseca): **Keito Nakamura** pauzuje za kartki, **Openda** jest kontuzjowany, a **Šulc** gra pod znakiem zapytania (źródła francuskie zebrane przez WebSearch; niepotwierdzone na konferencji).

**λ:** PSG 2,10 | Lyon 1,00. Baza to siła ofensywna PSG (seria wygranych, 4 gole z Barceloną) minus brak dwóch najlepszych skrzydłowych (ok. -0,15) i najlepsza obrona Lyonu (0,71 straconego gola na mecz). Lyon dostaje 1,0, bo w obronie PSG brakuje Marquinhosa i Mendesa, a w H2H Lyon strzelał 2 gole w każdym meczu.

**Rynek (kontrola):** PSG 1,41-1,47, remis 5,00-5,30, Lyon 6,25 (Rue des Joueurs, Africafoot). Bez marży daje to ok. 66/18,5/15,5%. Over 2.5: 1,40 (1xbet, za Wincomparator), czyli ok. 68% bez marży. PSG + Over 2.5: 1,69 (Betclic, za Rue des Joueurs).
- Mój 1: 62,6%, czyli -3,4 pp względem rynku. To mieści się w limicie 5 pp i jest uzasadnione konkretnymi absencjami (Kvara, Dembélé, Marquinhos, Mendes).
- Mój Over 2.5: 59,9% wobec ok. 68% na rynku. Różnica przekracza 5 pp, a nie mam twardej informacji, która by ją wyjaśniała. **Over 2.5 nie rekomenduję jako value**. Rynek może trafniej wyceniać tempo PSG (rynek bywa trafniejszy).

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 (PSG) | 62,6% | 1.60 | średnia |
| X | 20,3% | 4.94 | niska |
| 2 (Lyon) | 17,1% | 5.85 | niska |
| 1X | 82,9% | 1.21 | średnia (blisko progu 1.20) |
| 12 | 79,7% | 1.25 | średnia |
| X2 | 37,4% | 2.67 | niska |
| Over 1.5 | 81,5% | 1.23 | średnia |
| Over 2.5 / Under 2.5 | 59,9% / 40,1% | 1.67 / 2.49 | niska-średnia (rynek wyżej, ok. 68%) |
| Over 3.5 / Under 3.5 | 37,5% / 62,5% | 2.67 / 1.60 | niska-średnia |
| BTTS tak / nie | 55,5% / 44,5% | 1.80 / 2.25 | niska-średnia (H2H 2/2 BTTS) |
| PSG Over 0.5 gola | 87,8% | 1.14 | wykluczony (fair ≤ 1.15) |
| PSG Over 1.5 gola | 62,0% | 1.61 | średnia |
| PSG Over 2.5 gola | 35,0% | 2.85 | niska |
| Lyon Over 0.5 gola | 63,2% | 1.58 | niska-średnia |
| Lyon Under 1.5 gola | 73,6% | 1.36 | średnia |
| Rożne Over 8.5 / 9.5 / 10.5 (średnia 9,8) | 62,1% / 50,6% / 39,4% | 1.61 / 1.98 / 2.54 | niska (brak danych 2026/27) |
| Kartki Over 3.5 / Under 4.5 (średnia 4,0, sędzia nieznany) | 53,8% / 63,0% | 1.86 / 1.59 | niska |
| Faule, strzały | brak danych | – | brak typu |
| Rynki zawodnika | brak średnich na 90 min | – | brak typu (np. Doué strzały: składy niepotwierdzone) |

Najczęstsze wyniki: 2-1 i 2-0 (po 9,9%), 1-1 i 1-0 (po 9,5%).

**Ryzyka (oba scenariusze porażki faworyta):**
- **Remis (20%):** Lyon ma najlepszą obronę ligi (5 straconych w 7 meczach), a PSG bez Kvary i Dembélé ma mniej indywidualnych rozwiązań. Możliwe zmęczenie po Barcelonie, choć PSG ma więcej odpoczynku.
- **Wygrana Lyonu (17%):** Lyon wygrał 2-1 na Parc des Princes w kwietniu 2026, jest liderem i nie przechodzi kryzysu (korekta kryzysowa nie dotyczy). Kontra przeciwko przebudowanej obronie PSG (brak Marquinhosa i Mendesa).
- Data meczu się zmieniła, a ostateczne składy będą znane dopiero w poniedziałek.

**Typy z p > 50% i fair > 1.15:**
- 1X PSG: 82,9% @ 1.21 (średnia)
- 12: 79,7% @ 1.25 (średnia)
- Over 1.5: 81,5% @ 1.23 (średnia)
- Lyon Under 1.5 gola: 73,6% @ 1.36 (średnia)
- 1 PSG: 62,6% @ 1.60 (średnia; rynek ok. 1,44 bez value)
- PSG Over 1.5 gola: 62,0% @ 1.61 (średnia)
- Under 3.5: 62,5% @ 1.60 (niska-średnia)
- Lyon Over 0.5 gola: 63,2% @ 1.58 (niska-średnia)
- Over 2.5: 59,9% @ 1.67 (niska-średnia; rynek ok. 68%)
- BTTS tak: 55,5% @ 1.80 (niska-średnia)
- Rożne Over 8.5: 62,1% @ 1.61 (niska, nie na kupon)
- Kartki Under 4.5: 63,0% @ 1.59 (niska, sędzia nieznany, nie na kupon)
- Kartki Over 3.5: 53,8% @ 1.86 (niska, nie na kupon)

**Najlepszy rynek meczu:** 1X / Over 1.5 jako mocna noga, a 1 PSG jako typ wynikowy (brak value względem kursu ok. 1,44).

---

### 21:00 FC Barcelona – Real Madryt (La Liga, 10. kolejka, Camp Nou)

**Kluczowe dane**
- **Tabela po 9. kolejce:** Barcelona 27 pkt (9/9 zwycięstw, bramki 39-9), Atlético 22, Real 21 (7 W, 2 P) (VOV). Football Web Pages podaje inne liczby (Barça 24 pkt z 8 meczów, Real 18), co jest rozbieżnością źródeł. Squawka pisze o "perfect start" Barcelony, co potwierdza bilans 100%.
- **Puchary:** Barcelona przegrała z PSG 2-4 we wtorek 20.10 (pierwsza porażka sezonu, koniec serii 11 zwycięstw; Al Jazeera, Reuters/The Star). Real pokonał Leipzig 4-1 w środę 21.10 (Bernardo Silva, Güler, Mbappé, Diomande; Shafaq), ma komplet 3/3 w LM, a 10.10 wygrał 1-0 z Villarrealem w lidze. Trener Realu według części źródeł 2026: José Mourinho (bdnews24); źródła są niespójne.
- **Statystyki (Forebet, Statz, sportsgambler, ostatnie 10 meczów):**
  - Barcelona: 7,3-7,4 rożnego na mecz (1. w lidze), posiadanie 70,6%, 9,8 faula, 1,2 żółtej kartki, 1,0 straconego gola na mecz (Statz).
  - Real: 6,0 rożnego dla siebie i 3,5 przeciw, posiadanie 55,4%, 1,1 straconego gola i 4,1 celnego strzału rywali na mecz, 8,6-9,0 faula (najmniej w lidze), 1,75 żółtej kartki.
  - Linie Forebet: rożne 9.5, kartki 4.5.
- **H2H:** Barça – Real 2-0 (10.05.2026, Rashford, F. Torres), finał Superpucharu 3-2 dla Barcelony (01.2026, Dżudda) (sportytrader, Wikipedia, Morocco World News). Wyniku Clásico z 10.2025 nie zweryfikowałem w tym researchu.
- **Sędzia:** nominacji nie znaleziono (CTA zwykle ogłasza 2 dni przed meczem; wynik nie wrócił w wyszukiwaniu).

**Newsy (kadry)**
- Barcelona (Flick): poza grą **Dani Olmo** (przywodziciel, ok. 4 tyg., uraz z meczu z PSG; ESPN, Reuters), **Jules Koundé** (skręcona kostka, Flick 24.10: "nie zaryzykujemy"), **Eric García**, **Andreas Christensen**, **Roony Bardghji** (zerwane ACL) (thefalse9, Goal). Linia obrony mocno przetrzebiona, czyli rośnie λ Realu. Lamine Yamal strzelił gola PSG, a o jego kontuzji nic nie znalazłem.
- Real: **Vinícius Júnior zawieszony** (4 mecze w lidze za czerwoną kartkę z Villarrealem 10.10; thefalse9, legalbet), poza grą **Rodrygo** (kolano), **Raúl Asencio** (złamanie zmęczeniowe), **Ferland Mendy**, możliwy też **Marco Asensio** (Goal). Mbappé w przewidywanym XI, bez problemów zdrowotnych (Al Jazeera). Real traci dwóch skrzydłowych, ale ma w formie Güler, Bernardo Silvę i Diomande.

**λ:** Barcelona 2,45 | Real 1,50. Barça strzela w lidze średnio 4,3 gola u siebie i na wyjeździe, ale Real traci tylko 1,1 gola na mecz, więc łącznie ok. 2,45. Real dostaje 1,50, bo obrona Barcelony jest bez Koundé, Christensena i E. Garcíi, a Barça straciła 4 gole z PSG. Za brak Viníciusa i Rodrygo odejmuję ok. 0,15.

**Rynek (kontrola):** 1: 1,57-1,65, X: 4,33-5,80, 2: 3,75-7,00 (mediana ok. 1,61/5,0/3,9; legalbet, Doradobet, William Hill, Retabet, 1xBet za Bolavip/Redgol/RPP), czyli bez marży ok. 58/19/24%. Over 2.5: 1,17-1,18 (Legalbet, Meridianbet/Retabet), czyli ok. 81-82% bez marży. BTTS tak: 1,27 (Retabet), czyli ok. 75%.
- Mój 1: 58,5%, zgodny z rynkiem.
- Mój Over 2.5: 75,4% wobec ok. 81% na rynku (ok. -6 pp), BTTS 71% wobec ok. 75%. Krok "Skalibruj" mówi, żeby nie schodzić pod rynek o >5 pp bez konkretnej informacji, a moje informacje kadrowe (osłabiona obrona Barcelony) działają raczej na Over. Dlatego realne p dla Over 2.5 przyjmuję w przedziale 75-80% i NIE wyciągam z tego żadnego Under. Rynek bywa trafniejszy.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 (Barcelona) | 58,5% | 1.71 | średnia |
| X | 18,9% | 5.30 | niska |
| 2 (Real) | 22,7% | 4.41 | niska |
| 1X | 77,4% | 1.29 | średnia |
| 12 | 81,2% | 1.23 | średnia |
| X2 | 41,6% | 2.40 | niska |
| Over 1.5 | 90,5% | 1.11 | wykluczony (fair ≤ 1.15) |
| Over 2.5 / Under 2.5 | 75,4% / 24,6% | 1.33 / 4.07 | średnia (rynek wyżej) |
| Over 3.5 / Under 3.5 | 55,7% / 44,3% | 1.80 / 2.26 | niska-średnia |
| BTTS tak / nie | 71,0% / 29,0% | 1.41 / 3.45 | średnia |
| Barcelona Over 0.5 gola | 91,4% | 1.09 | wykluczony (fair ≤ 1.15) |
| Barcelona Over 1.5 gola | 70,2% | 1.42 | średnia |
| Barcelona Over 2.5 gola | 44,3% | 2.26 | niska |
| Real Over 0.5 gola | 77,7% | 1.29 | średnia |
| Real Under 2.5 gola | 80,9% | 1.24 | średnia |
| Real Over 1.5 gola | 44,2% | 2.26 | niska |
| Rożne Over 8.5 / 9.5 / 10.5 / 11.5 (średnia 10,2) | 66,3% / 55,1% / 43,9% / 33,5% | 1.51 / 1.82 / 2.28 / 2.98 | niska-średnia (2 źródła średnich, linia Forebet 9.5) |
| Kartki Over 3.5 / 4.5 / 5.5 (średnia 4,8, Clásico, sędzia nieznany) | 66,5% / 50,2% / 35,2% | 1.50 / 1.99 / 2.84 | niska |
| Faule Over 19.5 / 21.5 (średnia 21,5) | 64,3% / 48,3% | 1.56 / 2.07 | niska (obie drużyny faulują mało, wyższa stawka meczu) |
| Mbappé strzeli gola | ok. 49% (λ 1,5 × udział ok. 45%) | ok. 2.05 | niska, poniżej 50% |
| Inne rynki zawodnika (strzały Yamala, Mbappé) | brak średnich na 90 min z bieżącego sezonu | – | brak typu |

Najczęstsze wyniki: 2-1 (8,7%), 3-1 i 1-1 (po 7,1%), 2-2 (6,5%).

**Ryzyka (oba scenariusze porażki faworyta):**
- **Remis (19%):** przetrzebiona obrona Barcelony daje miejsce na mecz typu 2-2, a Real ma lepszą formę pucharową (4-1 vs 2-4 Barcelony).
- **Wygrana Realu (23%):** kontry Mbappé przeciwko improwizowanej linii obrony (brak 3 środkowych/bocznych obrońców), pierwsza porażka Barcelony może wybić ją z rytmu, a w razie Mourinho Real zagra pragmatycznie, z kontry. Real nie jest w kryzysie, więc korekta kryzysowa nie dotyczy.
- Brak sędziego i potwierdzonych składów, co mocno dotyczy rynków dodatkowych.
- Rozbieżność źródeł tabeli (27 vs 24 pkt Barcelony).

**Typy z p > 50% i fair > 1.15:**
- 12: 81,2% @ 1.23 (średnia)
- Real Under 2.5 gola: 80,9% @ 1.24 (średnia)
- Real Over 0.5 gola: 77,7% @ 1.29 (średnia)
- 1X: 77,4% @ 1.29 (średnia)
- Over 2.5: 75,4% @ 1.33 (średnia; kurs rynkowy 1,17 poniżej fair, bez value)
- BTTS tak: 71,0% @ 1.41 (średnia; rynek 1,27 bez value)
- Barcelona Over 1.5 gola: 70,2% @ 1.42 (średnia)
- Rożne Over 8.5: 66,3% @ 1.51 (niska-średnia)
- Kartki Over 3.5: 66,5% @ 1.50 (niska, sędzia nieznany)
- Faule Over 19.5: 64,3% @ 1.56 (niska)
- 1 Barcelona: 58,5% @ 1.71 (średnia; rynek ok. 1,61, bez value)
- Over 3.5: 55,7% @ 1.80 (niska-średnia)
- Rożne Over 9.5: 55,1% @ 1.82 (niska-średnia)
- Kartki Over 4.5: 50,2% @ 1.99 (niska, graniczny)

**Najlepszy rynek meczu:** BTTS tak / Real Over 0.5 gola (obrona Barcelony bez 3 obrońców plus Mbappé w formie). Mecz nie daje mocnego typu na wynik (58,5%).

---

### Tabela kandydatów na kupon (wejście dla `bet-slip-builder`)

| Mecz | Rynek | p | fair | pewność | zależy od | kurs rynkowy znany? |
|---|---|---|---|---|---|---|
| PSG – OL (pon. 26.10) | 1X | 82,9% | 1.21 | średnia | składy (Doué/Ramos) | nie (pochodny z 1X2) |
| PSG – OL | Over 1.5 | 81,5% | 1.23 | średnia | – | nie |
| PSG – OL | Lyon Under 1.5 | 73,6% | 1.36 | średnia | – | nie |
| PSG – OL | 1 PSG | 62,6% | 1.60 | średnia | absencje PSG | tak, 1,41-1,47 (brak value) |
| PSG – OL | PSG Over 1.5 gola | 62,0% | 1.61 | średnia | – | nie |
| PSG – OL | Over 2.5 | 59,9% | 1.67 | niska-średnia | – | tak, 1,40 (rynek wyżej niż model) |
| Barça – Real | 12 | 81,2% | 1.23 | średnia | – | nie |
| Barça – Real | Real Under 2.5 gola | 80,9% | 1.24 | średnia | – | nie |
| Barça – Real | Real Over 0.5 gola | 77,7% | 1.29 | średnia | Mbappé w XI | nie |
| Barça – Real | 1X | 77,4% | 1.29 | średnia | – | nie |
| Barça – Real | Over 2.5 | 75,4% | 1.33 | średnia | – | tak, 1,17-1,18 (brak value) |
| Barça – Real | BTTS tak | 71,0% | 1.41 | średnia | – | tak, 1,27 (brak value) |
| Barça – Real | Barcelona Over 1.5 gola | 70,2% | 1.42 | średnia | – | nie |
| Barça – Real | Rożne Over 8.5 | 66,3% | 1.51 | niska-średnia | sędzia, przebieg | nie (linia Forebet 9.5) |

Uwaga dla kuponu: PSG – OL odbędzie się **26.10**, nie 25.10, co zmienia okno rozliczenia kuponu.

To są oszacowania probabilistyczne oparte na niepełnych danych z wyszukiwarki, a nie gwarancje.
## E-sport: niedziela 25.10.2026, 18:00 – 06:00 CET (LoL Worlds Swiss R3 + CS2 PGL Masters Bucharest Swiss R2)

> Metodyka: skill `esports-analyst` (cztery filary, `scripts/series.py`, krok „Skalibruj”). Dane pochodzą wyłącznie z WebSearch (31 zapytań). WebFetch/curl były zablokowane, a serwer MCP `sportsdata` nie połączył się (ENOENT). BettingPros nie był używany. **Ważny brak:** dla żadnego z czterech meczów LoL nie znalazłem kursu na konkretny mecz, więc p w LoL opierają się na sile drużyn, wynikach R1–R2, kursach outright i modelu awansu (outdrafted przez Everything Edinburgh), a nie na rynku meczowym. Dla CS2 znalazłem kursy meczowe, ale z pojedynczych serwisów. Nie znam veta, więc map i total rund CS2 nie wyceniam per mapa. Total killi i czasu gry w LoL też nie wyceniam, bo nie mam danych. Kuponów tu nie składam.
> Uwaga: 25.10 o 03:00 Polska wraca na czas zimowy (CET = UTC+1). Wszystkie godziny poniżej są w CET. W Teksasie (CDT = UTC−5) obowiązuje jeszcze czas letni, więc CET = CDT + 6 h. Rumunia przeszła na czas zimowy EET = UTC+2 = CET + 1 h.

### Zweryfikowany terminarz (CET)

| Godz. CET | Gra | Mecz | Format | Stan | Weryfikacja |
|---|---|---|---|---|---|
| 18:00 | CS2 | FURIA – Natus Vincere | bo3 | 1-0 vs 1-0 | HLTV (slot 18:00), vprognoze 19:55–20:00 MSK = 18:00 CET, EGW/stavka 17:00 UTC = 18:00 CET |
| 18:00 | CS2 | Legacy – DENDELE CS | bo3 | 0-1 vs 0-1 | HLTV (slot 18:00), EGW 17:00 UTC; vprognoze podaje 20:00 MSK |
| 18:00 | LoL | Hanwha Life – Invictus Gaming | Bo1 | 1-1 vs 1-1 | Liquipedia 12:00 CDT; Sheepesports: 1. mecz dnia |
| 19:00 | LoL | G2 Esports – Top Esports | Bo1 | 1-1 vs 1-1 | Liquipedia 13:00 CDT; Sheepesports: 2. mecz. **Rozbieżność:** Polymarket podaje „1:00 PM ET” (= 18:00 CET) |
| 20:00 | LoL | Movistar KOI – Dplus KIA | Bo3 (Fearless) | 2-0 vs 2-0, o awans | Liquipedia/Sheepesports 14:00 CDT |
| 23:00 | LoL | Gen.G – LYON | Bo3 (Fearless) | 2-0 vs 2-0, o awans | Liquipedia/Sheepesports 17:00 CDT |

Pary podane w zleceniu się zgadzają. Pozostałe mecze R3 LoL, czyli Bo1 1-1 KC–BLG i CFO–T1 oraz Bo3 0-2 TL–AL i LØS–TSW, są według Sheepesports i egamersworld rozgrywane 26.10, więc wypadają poza oknem. Wcześniejsze mecze CS2 R2 (FUT–Liquid 09:00; Vitality–MongolZ i BetBoom–Nemiga 12:00; G2–Aurora i MOUZ–9z 15:00; Spirit–TYLOO w ciągu dnia) zaczynają się przed 18:00 i je pominąłem. Godziny CS2 wyliczyłem tak: sloty esports.ru 11/14/17/20 są w czasie MSK (UTC+3), co daje 09/12/15/18 CET, a to zgadza się z HLTV. Liquipedia ma etykietę „EEST” przesuniętą o 2 h, prawdopodobnie błędną. Przed meczem warto potwierdzić godzinę, bo PGL bywa opóźniony po długich seriach.

### Wyniki z 24.10 (aktualizacja względem Analiza_dnia_2026-10-24_wieczor.md)

**LoL Worlds R2 (Bo1)** – źródła: GosuGamers, Dotesports, Hotspawn, Liquipedia (opisy w wynikach wyszukiwania):
- Grupa 1-0: **DK 1-0 T1** (41 min; drugi comeback DK z rzędu, „Elder flip” w ostatniej minucie), **Gen.G 1-0 HLE** (29 min, dominacja), **MKOI 1-0 CFO**, **LYON 1-0 KC**.
- Grupa 0-1: **TES 1-0 AL**, **G2 1-0 LØS** („jedna z najbardziej niechlujnych wygranych w historii Worlds”), **IG 1-0 TSW** (z nerwami, dobry TheShy na K'Sante), **BLG 1-0 TL** (Bin na Camille).
- Bilans typów z 24.10: G2 ✓, BLG ✓, IG ✓, AL ✗, T1 ✗ (DK wygrało), KOI ✓, KC ✗ (LYON wygrało), HLE–Gen.G bez typu.
- Tabela: 2-0 DK, Gen.G, MKOI, LYON; 1-1 T1, HLE, CFO, KC, TES, G2, IG, BLG; 0-2 AL, LØS, TSW, TL.

**CS2 PGL Masters Bucharest R1 (bo3)**:
- **NAVI 2-0 G2**: Nuke 13-11, Dust2 22-19 po dogrywkach (HLTV „NAVI scrape narrow win”). Typ NAVI +1.5 ✓, G2 +1.5 ✗.
- **FURIA 2-0 DENDELE**: Ancient (pick DENDELE) 13-8, Inferno (pick FURIA) 13-11 po 6-6 do przerwy. W vecie DENDELE zbanowało Dust2 i Mirage, FURIA Anubis i Cache, decyderem był Nuke (HLTV, Dust2.com.br, Cybersport). Typy FURIA wygra ✓, Under 2.5 ✓, FURIA −1.5 ✓.
- **Nemiga 2-0 Legacy**: niespodzianka, Legacy było nr 7 VRS. Na Dust2 Legacy doszło do piłki meczowej, ale przegrało w 21. rundzie, a na Ancient syph0 zdobył 47 fragów (HLTV „Nemiga move past Legacy”).
- Pozostałe: Liquid 2-1 MOUZ, BetBoom 2-1 Spirit, MongolZ 2-1 Aurora, FUT 2-0 TYLOO, Vitality – 9z (Vitality w grupie 1-0).

---

### LoL: Hanwha Life – Invictus Gaming (Worlds 2026, Swiss R3, 1-1, Bo1, 25.10 18:00 CET)
**Dane:**
- HLE: LCK #2, mistrz MSI 2026 (3-2 z BLG; Korea JoongAng Daily), skład Zeus, Kanavi, Zeka, Gumayusi, Delight. W R1 rozbiło TES, w R2 przegrało z Gen.G w 29 min. Przed R2 tips.gg: Gen.G 1.65 / HLE 2.25. Outright: Polymarket/Kalshi 17–20%, BC.Game 4.5.
- IG: LPL #4. W R1 przegrało z Gen.G (rynek R1 Gen.G 76–78%), w R2 wygrało z TSW „mimo kilku nerwowych momentów” (TheShy na K'Sante). W finale regionalnym LPL przegrało 1-3 z TES (Strafe). Outright: BC.Game 19.0, Polymarket ~3%.
- H2H w obecnych składach: brak danych.
- Rynek meczowy: nie znalazłem kursu (Polymarket/egamersworld nie były zindeksowane).

**p:** HLE 66%. Punkt wyjścia ~70% (LCK #2 vs LPL #4, różnica outright 4.5 vs 19). Obniżyłem go za Bo1 i brak rynku. Porażka HLE z Gen.G to porażka z faworytem turnieju, czyli szum, nie sygnał. `series.py 0.66 --bo 1`.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| HLE wygra | 66.0% | 1.52 | niska-średnia |
| IG wygra | 34.0% | 2.94 | niska |
| (Bo1: handicap i total map nie istnieją; total killi i czas gry bez danych) | – | – | – |

**Ryzyka:** Bo1 to jeden draft. IG ma TheShy w formie, a LPL po słabym R1 wygrało 4/4 mecze w R2 (forma regionu rośnie). Strona mapy jest nieznana. Brak rynku: jeśli kurs na HLE wyniesie poniżej 1.40, rynek widzi ponad 70% i moja liczba jest konserwatywna.
**Typy z p>50% i fair>1.15:** HLE wygra (66.0%, fair 1.52), niska-średnia pewność.

### LoL: G2 Esports – Top Esports (Worlds 2026, Swiss R3, 1-1, Bo1, 25.10 19:00 CET; Polymarket podaje 18:00)
**Dane:**
- G2: LEC #1. W R1 przegrało z DK po dominującym early game (prowadziło 7:0 w killach), w R2 ograło LØS, ale bardzo niechlujnie (Hotspawn/Dotesports). Na MSI 2026 przegrało 0-3 z LYON (tips.gg). Outright BC.Game 17.0.
- TES: LPL #3, wciąż bez top-lanera ZUIAN-a (odmowy wizy, gra 369; Insider Gaming/Dotesports, 24.10). W R1 przegrało z HLE, w R2 wygrało derby LPL z AL. W 2026 słaba forma: 7.-8. na MSI i 7.-8. w LPL Split 3 (Strafe). Outright BC.Game 34.0.
- H2H: TES wygrało z G2 3-1 na Worlds 2025 i w maratonie bo5 na MSI 2026 (lipiec; kursy wtedy TES 1.74 / G2 2.04, GG.BET przez win.gg). To było jeszcze z ZUIAN-em, więc daję tej informacji niską wagę.
- Rynek meczowy: Polymarket ma rynek (~61 tys. $ obrotu), ale cena nie trafiła do wyników wyszukiwania.

**p:** G2 55%. Kursy outright (17 vs 34) i brak ZUIAN-a przemawiają za G2. H2H z 2025–26 i niechlujna gra G2 ciągną w stronę 50%. Bo1. `series.py 0.55 --bo 1`.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| G2 wygra | 55.0% | 1.82 | niska |
| TES wygra | 45.0% | 2.22 | niska |

**Ryzyka:** TES miało w H2H przewagę przez ostatnie dwa lata. G2 dwa razy z rzędu grało słabo w mid-game. 369 rozgrywa się z każdym meczem. Kolejność i godzina meczu są niepewne.
**Typy z p>50% i fair>1.15:** G2 wygra (55%, fair 1.82). **Brak mocnego typu.**

### LoL: Movistar KOI – Dplus KIA (Worlds 2026, Swiss R3, 2-0, Bo3 Fearless, o awans do fazy pucharowej, 25.10 20:00 CET)
**Dane:**
- DK: LCK #4, mistrz EWC 2026 (pierwszy międzynarodowy tytuł; GosuGamers). W R1 wygrało z G2 po odrobieniu 0:7 w killach, w R2 z T1 w 41 min po drugim „cudownym” comebacku z rzędu, Elder flip w ostatniej minucie (GosuGamers, Dotesports). Słabe early game DK powtarza się, a wygrywa ono teamfightami w late game.
- MKOI: LEC #2-3. W R1 wygrało z BLG mimo kursu 5.55 (39 min; pierwsza w historii wygrana KOI w meczu otwarcia Worlds), w R2 z CFO. Przed Worlds przegrało 0-3 z G2 w finale LEC.
- Modele i rynek przed turniejem: awans DK 71% vs KOI 18% (outdrafted przez Everything Edinburgh). Outright BC.Game DK 13.0, KOI 51.0, Polymarket DK 10%. Kursu na ten mecz nie znalazłem.
- H2H w obecnych składach: brak danych.

**p gry (DK):** 0.64, ta sama na każdą grę (strona i draft nieznane, Fearless). Punkt wyjścia ~0.67 (LCK vs LEC, różnica outright). Obniżyłem go o 3 pp, bo DK ma powtarzalnie słabe early game, a KOI jest w dobrej formie (2 wygrane, w tym upset na BLG). `series.py 0.64 --bo 3`.
**p meczu:** DK 70.5% / KOI 29.5%.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| DK wygra serię | 70.5% | 1.42 | niska-średnia |
| KOI wygra serię | 29.5% | 3.38 | niska |
| DK −1.5 (2-0) | 41.0% | 2.44 | niska |
| KOI +1.5 map | 59.0% | 1.69 | niska-średnia |
| DK +1.5 map | 87.0% | 1.15 | – (fair ≤ 1.15, pominąć) |
| KOI −1.5 (2-0 KOI) | 13.0% | 7.72 | niska |
| Over 2.5 map | 46.1% | 2.17 | niska |
| Under 2.5 map | 53.9% | 1.85 | niska |
| Dokładny wynik 2-0 DK / 2-1 DK / 1-2 / 0-2 | 41.0 / 29.5 / 16.6 / 13.0% | 2.44 / 3.39 / 6.03 / 7.72 | niska |

**Ryzyka:** DK oddaje early game. W Bo3 KOI może zbudować przewagę, której DK nie odrobi drugi i trzeci raz, a każda gra z comebackiem kończy się blisko 50/50. Fearless wymaga głębokiej puli championów od obu drużyn. Brak rynku: przy kursie DK w okolicach 1.30 rynek widzi ~75%, co w Bo3 jest blisko mojej liczby, ale bez punktu odniesienia pewność pozostaje niska.
**Typy z p>50% i fair>1.15:** DK wygra (70.5%, fair 1.42), KOI +1.5 map (59.0%, fair 1.69), Under 2.5 map (53.9%, fair 1.85, słaby). DK wygra i KOI +1.5 to scenariusz 2-1 DK. Oba typy się nie wykluczają, ale są ze sobą powiązane.

### LoL: Gen.G – LYON (Worlds 2026, Swiss R3, 2-0, Bo3 Fearless, o awans, 25.10 23:00 CET)
**Dane:**
- Gen.G: LCK #1, mistrz LCK (dwa tytuły z rzędu). W R1 pokonało IG, w R2 HLE w 29 min. Faworyt turnieju: Kalshi 35%, Polymarket ~33%, kurs 3.10–3.25 (win.gg, smartbettingguide). Model awansu 91%.
- LYON: LCS #2. W R1 pokonało TSW (kurs 1.54), w R2 KC. Na MSI 2026 rozbiło G2 3-0 (tips.gg). Outright 35–41. Model awansu 29%. GosuGamers pisze, że po MSI LYON „może wejść do top 8”.
- H2H w 2026: brak danych w wynikach wyszukiwania.
- Rynek meczowy: nie znalazłem kursu. Gen.G ma pierwszy wybór strony jako wyższy seed (Sheepesports).

**p gry (Gen.G):** 0.75. Różnica klas LCK #1 vs LCS #2 dawałaby ~0.80, ale ściągnąłem do 0.75, bo LYON jest w realnie dobrej formie (2-0 i 3-0 z G2 na MSI) i brakuje rynku. `series.py 0.75 --bo 3`.
**p meczu:** Gen.G 84.4% / LYON 15.6%.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| Gen.G wygra serię | 84.4% | 1.19 | średnia (graniczny 1.15–1.20) |
| LYON wygra serię | 15.6% | 6.40 | niska |
| Gen.G −1.5 (2-0) | 56.2% | 1.78 | średnia-niska |
| LYON +1.5 map | 43.8% | 2.29 | niska |
| Gen.G +1.5 map | 93.8% | 1.07 | – (pominąć) |
| Under 2.5 map | 62.5% | 1.60 | średnia-niska |
| Over 2.5 map | 37.5% | 2.67 | niska |
| Dokładny wynik 2-0 / 2-1 / 1-2 / 0-2 | 56.2 / 28.1 / 9.4 / 6.2% | 1.78 / 3.56 / 10.67 / 16.00 | niska |

**Ryzyka:** LYON potrafi zaskoczyć w drafcie (pokazało to na MSI przeciw G2). W Fearless gra 2 i 3 wymuszają nietypowe postacie. Gen.G jest już pewne miejsca w Swiss i w razie porażki ma dwie kolejne szanse, ale to nie powód, by grało na pół gwizdka. Gen.G −1.5 i Under 2.5 to ten sam scenariusz (2-0), więc są silnie skorelowane.
**Typy z p>50% i fair>1.15:** Gen.G wygra (84.4%, fair 1.19, graniczny), Under 2.5 map (62.5%, fair 1.60), Gen.G −1.5 (56.2%, fair 1.78). Under 2.5 i Gen.G −1.5 nie łączyć.

---

### CS2: FURIA – Natus Vincere (PGL Masters Bucharest 2026, Swiss R2, 1-0 vs 1-0, bo3, 25.10 18:00 CET)
**Dane:**
- Rynek: stavka.tv FURIA 1.60 / NAVI 2.35, FURIA 2-0 ok. 2.90. Vprognoze FURIA 1.60 / NAVI 2.34. EGamersWorld w jednej migawce FURIA 1.37 (pojedyncza, odstająca). Strona meczu na HLTV daje według wyniku wyszukiwania NAVI 53.8% / FURIA 46.2%, ale tekst był nieczytelny i może to być ankieta fanów, nie model. Bez marży (1.60/2.35): **FURIA ~59.5%**.
- Forma: FURIA jest #3 HLTV i #4 VRS, finalista IEM Cologne Major 2026, z serią 4 wygranych. W R1 pokonała DENDELE 2-0 (Ancient 13-8, Inferno 13-11). Kluczowy gracz według Skin.Club to molodoy (najlepszy rating na Ancient). NAVI w R1 wygrało z G2 2-0, ale na styk (Nuke 13-11, Dust2 22-19 po dogrywkach). Wcześniej NAVI miało słabszą serię (24.10) i przegrało 0-2 z Legacy na EWC 2026 (cryptobriefing).
- Składy: FURIA yuurih, KSCERATO, FalleN, molodoy, YEKINDAR; NAVI b1t, Aleksib, iM, w0nderful, makazze (Dotesports). Brak informacji o stand-inach.
- H2H w 2026: **FURIA 2-1 dwa razy** – IEM Kraków (II; Mirage/Inferno/Dust2, Inferno pick FURIA wygrany) i IEM Rio (IV; Mirage pick NAVI, Dust2 pick FURIA, decyder Nuke dla FURIA) (navi.gg, HLTV). Bilans historyczny NAVI 11-7, Mirage 10-4 i Nuke 8-5 dla NAVI (egamersworld; zawiera stare składy, niska waga).
- Mapy: FURIA ma Inferno 78% (9 map; vprognoze) i dobry Nuke (pick w EWC). NAVI regularnie wybiera Mirage przeciw FURIA i właśnie wygrało Nuke i Dust2 z G2. Veto nieznane.

**p map (FURIA):** [mapa NAVI, np. Mirage: 0.48; mapa FURIA, np. Inferno: 0.65; decyder Nuke/Dust2: 0.57] → `series.py 0.48 0.65 0.57 --bo 3`.
**p meczu:** FURIA 60.0% / NAVI 40.0%, zgodnie z rynkiem bez marży (~59.5%). Nie mam informacji uzasadniającej odejście od rynku.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| FURIA wygra | 60.0% | 1.67 | średnia |
| NAVI wygra | 40.0% | 2.50 | niska |
| FURIA −1.5 (2-0) | 31.2% | 3.21 | niska (rynek ~2.90) |
| NAVI +1.5 map | 68.8% | 1.45 | średnia |
| FURIA +1.5 map | 81.8% | 1.22 | średnia |
| NAVI −1.5 (2-0 NAVI) | 18.2% | 5.49 | niska |
| Over 2.5 map | 50.6% | 1.98 | niska (brak typu) |
| Under 2.5 map | 49.4% | 2.02 | niska |
| Dokładny wynik 2-0 / 2-1 / 1-2 / 0-2 (FURIA) | 31.2 / 28.8 / 21.8 / 18.2% | 3.21 / 3.47 / 4.60 / 5.49 | niska |

Total rund: veto nieznane, nie wyceniam. Orientacyjnie wyrównany mecz to 21–24 rundy na mapę, a NAVI grało w R1 mapy na styk (24 i 41 rund).
**Ryzyka:** pick NAVI na Mirage (historycznie 10-4 NAVI) i forma NAVI na Nuke mogą odwrócić decydera. FURIA nie zawsze dowozi przewagę jako faworyt. Kursy pochodzą z dwóch serwisów, a migawka EGW 1.37 odstaje, więc jeśli rynek w rzeczywistości jest bliżej 1.40, moje 60% jest za nisko.
**Typy z p>50% i fair>1.15:** FURIA +1.5 map (81.8%, fair 1.22), NAVI +1.5 map (68.8%, fair 1.45), FURIA wygra (60.0%, fair 1.67; rynek 1.60 – brak value). FURIA +1.5 i NAVI +1.5 przegrywają w przeciwnych scenariuszach 2-0, więc nie łączyć.

### CS2: Legacy – DENDELE CS (PGL Masters Bucharest 2026, Swiss R2, 0-1 vs 0-1, bo3, 25.10 18:00 CET)
**Dane:**
- Rynek: vprognoze Legacy 1.33 / DENDELE 3.30, czyli bez marży **Legacy ~71%**. Model HLTV daje Legacy ~89% (VRS #8 vs #42). Stavka.tv „kef 1.78” to prawdopodobnie kurs typu (np. 2-0), a nie zwycięzcy. EGW „~1.8 dla obu” to błędna lub pusta migawka.
- Forma: Legacy to #7-8 VRS, 3. miejsce na EWC 2026 (2-0 z NAVI i Falcons, 2-1 z FURIA, 0-2 ze Spirit). W R1 niespodziewanie przegrało 0-2 z Nemigą: na Dust2 doszło do piłki meczowej, ale przegrało w 21. rundzie, a na Ancient syph0 zdobył 47 fragów. Skin.Club i vprognoze piszą o „poważnych obawach co do formy” Legacy. DENDELE (ex-Sharks, #40-42) przegrało z FURIA 0-2, ale stawiało opór (8 i 11 rund). W kwalifikacjach SA wygrywało pewnie (2-0 z Imperial).
- Skład Legacy: nie potwierdziłem składu z X 2026 (ostatnio znany: latto, n1ssim, arT, saadzin, dumau – HLTV IV 2026). Ta niepewność obniża pewność.
- H2H: nie znalazłem bezpośrednich spotkań w 2026. Brazylijskie derby, drużyny się znają.
- Mapy DENDELE (z veta z FURIA): banuje Dust2 i Mirage, wybiera Ancient. Map Legacy nie znam.

**p map (Legacy):** [0.67 (pick DENDELE, prawdopodobnie Ancient), 0.70 (pick Legacy), 0.68 (decyder)] → `series.py 0.67 0.70 0.68 --bo 3`.
**p meczu:** Legacy 76.3% / DENDELE 23.7%. To +5 pp nad rynkiem bez marży (71%) i dużo poniżej modelu HLTV (89%), czyli środek widełek. Porażkę z Nemigą traktuję jako sygnał słabszej formy i ściągnąłem nią p z ~80%. Nie schodzę niżej, bo Nemiga to zwycięzca LAN-u CIS w formie, więc porażka z nią nie była kompromitacją.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| Legacy wygra | 76.3% | 1.31 | średnia (rynek 1.33 – brak value) |
| DENDELE wygra | 23.7% | 4.22 | niska |
| Legacy −1.5 (2-0) | 46.9% | 2.13 | niska |
| DENDELE +1.5 map | 53.1% | 1.88 | niska |
| Legacy +1.5 map | 90.1% | 1.11 | – (pominąć) |
| DENDELE −1.5 (2-0 DENDELE) | 9.9% | 10.10 | niska |
| Under 2.5 map | 56.8% | 1.76 | niska-średnia |
| Over 2.5 map | 43.2% | 2.31 | niska |
| Dokładny wynik 2-0 / 2-1 / 1-2 / 0-2 (Legacy) | 46.9 / 29.4 / 13.8 / 9.9% | 2.13 / 3.40 / 7.23 / 10.10 | niska |

Total rund: veto nieznane, nie wyceniam. Przy dużej różnicy klas spodziewam się 19–22 rund na mapę, ale DENDELE grało z FURIA na Inferno 24 rundy.
**Ryzyka:** forma Legacy po 0-2 z Nemigą, presja meczu na 0-2 (porażka oznacza mecz o przetrwanie), derby brazylijskie, nieznane veto. Pick DENDELE na Ancient może dać mapę ~50/50, co uderza w Under 2.5 i w Legacy −1.5. Sprzeczne kursy (1.33 vs 1.78) dodają niepewności.
**Typy z p>50% i fair>1.15:** Legacy wygra (76.3%, fair 1.31), Under 2.5 map (56.8%, fair 1.76), DENDELE +1.5 map (53.1%, fair 1.88, słaby, rzut monetą). Under 2.5 i DENDELE +1.5 przy 2-0 Legacy się wykluczają.

---

### Podsumowanie typów e-sport 25.10 (p>50%, fair>1.15)

| Godz. CET | Mecz | Typ | p | fair | pewność |
|---|---|---|---|---|---|
| 23:00 | Gen.G – LYON | Gen.G wygra | 84.4% | 1.19 | średnia (graniczny) |
| 18:00 | FURIA – NAVI | FURIA +1.5 map | 81.8% | 1.22 | średnia |
| 18:00 | Legacy – DENDELE | Legacy wygra | 76.3% | 1.31 | średnia (rynek 1.33) |
| 20:00 | KOI – DK | DK wygra | 70.5% | 1.42 | niska-średnia |
| 18:00 | FURIA – NAVI | NAVI +1.5 map | 68.8% | 1.45 | średnia |
| 18:00 | HLE – IG | HLE wygra | 66.0% | 1.52 | niska-średnia |
| 23:00 | Gen.G – LYON | Under 2.5 map | 62.5% | 1.60 | średnia-niska |
| 18:00 | FURIA – NAVI | FURIA wygra | 60.0% | 1.67 | średnia (rynek 1.60) |
| 20:00 | KOI – DK | KOI +1.5 map | 59.0% | 1.69 | niska-średnia |
| 18:00 | Legacy – DENDELE | Under 2.5 map | 56.8% | 1.76 | niska-średnia |
| 23:00 | Gen.G – LYON | Gen.G −1.5 | 56.2% | 1.78 | średnia-niska |
| 19:00 | G2 – TES | G2 wygra | 55.0% | 1.82 | niska (brak mocnego typu) |
| 20:00 | KOI – DK | Under 2.5 map | 53.9% | 1.85 | niska |
| 18:00 | Legacy – DENDELE | DENDELE +1.5 | 53.1% | 1.88 | niska |

Pominięte (fair ≤ 1.15): DK +1.5 (1.15), Gen.G +1.5 (1.07), Legacy +1.5 (1.11). Korelacje: w każdym meczu typy „−1.5” i „Under 2.5” to ten sam scenariusz 2-0. W FURIA – NAVI nie łączyć +1.5 dla obu drużyn. Przed kuponem trzeba pobrać kursy meczowe LoL (żaden nie był dostępny) i sprawdzić, czy p nie odbiega od rynku bez marży o > 5 pp bez konkretnej informacji.

**Źródła (WebSearch):** [Liquipedia LoL Swiss Stage](https://liquipedia.net/leagueoflegends/World_Championship/2026/Swiss_Stage), [Sheepesports R3 draw](https://www.sheepesports.com/en/articles/worlds-2026-swiss-stage-round-3-draw/en), [GosuGamers Day 2](https://www.gosugamers.net/lol/news/79411-gen-g-dplus-kia-lyon-and-mkoi-improve-to-2-0-records-in-worlds-2026-swiss-stage-day-2), [GosuGamers DK–T1](https://www.gosugamers.net/lol/news/79410-dplus-kia-pull-off-another-miracle-comeback-at-lol-worlds-2026-swiss-stage), [Dotesports Day 2](https://dotesports.com/league-of-legends/news/dk-beats-t1-as-lpl-picks-up-its-first-wins-on-day-2-of-worlds-2026-swiss-stage), [Hotspawn Day 2](https://www.hotspawn.com/league-of-legends/news/worlds-2026-swiss-stage-day-2), [egamersworld R3](https://egamersworld.com/lol/news/38028/worlds-2026-swiss-round-3-geng-chase-playoffs-as-l-ZMXa4b7Jt), [Polymarket TES–G2](https://polymarket.com/esports/league-of-legends/worlds/lol-tes-g2-2026-10-25), [win.gg](https://win.gg/lol-worlds-betting-preview-odds/), [Everything Edinburgh](https://everythingedinburgh.com/games/gaming/worlds-2026-swiss-stage/), [tips.gg R2](https://tips.gg/article/worlds-championship-2026-swiss-stage-round-1-recap-round-2-betting-predictions-tournament-winner-event-story/), [win.gg G2–TES MSI](https://win.gg/g2-esports-vs-top-esports-best-betting-odds-and-picks-for-msi-2026/), [Strafe TES–IG](https://www.strafe.com/news/read/top-esports-defeats-invictus-gaming-to-qualify-for-worlds-2026/), [HLTV day 2 preview](https://www.hltv.org/news/45794/furia-vs-navi-aurora-vs-g2-headline-pgl-masters-bucharest-day-2), [HLTV NAVI–G2](https://hltv.org/news/45793/navi-scrape-narrow-win-over-g2-to-secure-massive-vrs-payout), [HLTV Nemiga–Legacy](https://www.hltv.org/news/45792/nemiga-move-past-legacy-in-bucharest), [HLTV FURIA–DENDELE](https://www.hltv.org/matches/2399726/furia-vs-dendele-pgl-masters-bucharest-2026), [Dust2.com.br](https://www.dust2.com.br/noticias/79230/furia-bate-dendele-na-estreia-da-pgl-masters-bucharest), [HLTV FURIA–NAVI](https://www.hltv.org/matches/2399733/furia-vs-natus-vincere-pgl-masters-bucharest-2026), [stavka.tv FURIA–NAVI](https://stavka.tv/matches/csgo/25-10-2026-furia-natus-vincere), [vprognoze FURIA–NAVI](https://vprognoze.ru/topforecast/8208513-furia-natus-vincere-2026-10-25.html), [navi.gg IEM Rio](https://navi.gg/en/tournaments/iem-rio-2026/match/13518), [navi.gg IEM Kraków](https://navi.gg/en/tournaments/iem-krakw-2026/match/13026), [egamersworld H2H](https://egamersworld.com/counterstrike/history/navi-vs-furia-4yHyZHdnB-), [HLTV Legacy–DENDELE](https://www.hltv.org/matches/2399734/legacy-vs-dendele-pgl-masters-bucharest-2026), [vprognoze Legacy–DENDELE](https://vprognoze.ru/topforecast/8208519-legacy-dendele-2026-10-25.html), [stavka.tv Legacy–DENDELE](https://stavka.tv/matches/csgo/25-10-2026-legacy-dendele-cs), [cryptobriefing EWC](https://cryptobriefing.com/legacy-third-place-esports-world-cup/), [Dotesports PGL](https://dotesports.com/counter-strike/news/pgl-masters-bucharest-2026-schedule-results).

To oszacowania, nie gwarancje.
## NHL: niedziela 25.10.2026, analiza skillem `nhl-analyst`

**Stan na:** 25.10, rano/przedpołudnie CET. Dane pochodzą wyłącznie z WebSearch (ok. 32 zapytania), czyli ze streszczeń wyników wyszukiwania. WebFetch/curl są zablokowane, MCP `sportsdata` się nie połączył (ENOENT), a BettingPros nie był używany. **Brak xG/CF% ze stron analitycznych** (MoneyPuck/NST nie zwróciły danych), więc λ budowałem z GF/GA, special teams, bramkarzy i newsów, a potem zakotwiczyłem na rynku bez marży. Początek sezonu (10-12 meczów), więc próba jest mała.

**Czas:** od 25.10 Polska ma CET (UTC+1), USA EDT, więc ET + 5 h = CET.

## Weryfikacja par, godzin i back-to-back (B2B)

| # | Mecz (gospodarz drugi) | ET | CET | Uwagi |
|---|---|---|---|---|
| 1 | Panthers @ Blackhawks | 15:00 | 20:00 | United Center (Inside The Rink, iHeart) |
| 2 | **Islanders** @ Stars (**nie Rangers**) | 18:00 | 23:00 | NHL.com „Islanders at Stars projected lineups”, Bleacher Nation, DocSports. NYR grali 24.10 w Ottawie i w niedzielę nie grają. |
| 3 | Canadiens @ Jets, Heritage Classic | **19:00** (18:00 czasu Winnipeg) | **00:00 (26.10)** | Princess Auto Stadium (Squawka, CBS/AP, ABC News). DAZN podał 18:00 ET, ale to prawdopodobnie czas lokalny (CT). |
| 4 | Avalanche @ Predators | 20:00 | 01:00 (26.10) | Bridgestone Arena (ESPN, NHL.com Avalanche) |
| 5 | Wild @ Canucks | 22:00 (19:00 PT) | 03:00 (26.10) | Rogers Arena (NHL.com Canucks, Inside The Rink) |

**Wyniki z 24.10 (uzupełnienie):**
- **PIT 3-2 NSH po dogrywce:** Saros obronił 34 strzały, strzały 26-37, Malkin nie zagrał (choroba). Źródła: NHL.com, ESPN, AP/ABC.
- **MIN 5-1 SEA:** Kaprizov strzelił gola w 26. sekundzie, Coleman zdobył 2 gole (jeden do pustej), Wallstedt obronił 22 strzały, MIN ma bilans 7-3-2. Źródła: AP/ABC, ESPN, Fox13.
- **OTT - NYR:** wyniku nie sprawdzałem, bo NYR nie grają 25.10.

**B2B:**
- **NSH** gra drugi dzień z rzędu i wraca z Pittsburgha.
- **MIN** gra drugi dzień z rzędu (lot Seattle → Vancouver), to 4. mecz z 5 na wyjeździe (NHL.com Canucks).
- **FLA:** ostatni mecz 22.10 w PIT (0-4), więc nie ma B2B.
- **CHI:** grał 23.10 (1-4 z MTL), nie ma B2B.
- **MTL:** grał 23.10 w CHI (4-1), nie ma B2B.
- **WPG:** ostatnio 2-3 po dogrywce w DAL (22.10), nie ma B2B.
- **DAL:** ostatnio wygrana po dogrywce z WPG, nie ma B2B.
- **NYI:** nie było ich w terminarzu 24.10, więc zakładam brak B2B (niepotwierdzone wprost).
- **COL:** grał 23.10 (6-3 z TBL; NHL.com Avalanche recap), nie ma B2B.
- **VAN:** grał 22/23.10 (2-5 z DET), nie ma B2B.

**Bramkarze (DailyFaceoff 25.10: potwierdzonych 2 z 10):**
- Potwierdzeni: **Schmid (FLA)** i **Pickard (MIN)** (DFO, THN/Yahoo „Wild announce goalie plan”).
- Pozostali są przewidywani i niepotwierdzeni.

---

## 1. Chicago Blackhawks - Florida Panthers (25.10, 20:00 CET; 15:00 ET)

**Dane:**
- **Bilans:** FLA 5-4-2, CHI 3-7(-1), według Inside The Rink.
- **Gole na mecz:** FLA strzela 2,82 (20.-21.) i traci 3,09 (14.). CHI strzela 2,20 (30.) i traci **4,00 (30.)**. Źródła: Inside The Rink, Pick Dawgz.
- **PP:** FLA 19,2% (23.), CHI 10,3% (31.). Źródło: iHeart.
- **Forma:** FLA przegrali 0-4 w PIT i 1-5 w OTT, nie wygrali jeszcze na tym wyjeździe (NHL.com Panthers preview). CHI przegrali 1-4 z MTL.
- **Absencje FLA:** Barkov (dolna część ciała, powrót ok. 27.10), Marchand (noga), Markstrom (górna część ciała), Forsling day-to-day. Źródła: iHeart, ESPN.
- **Absencje CHI:** **Bedard na IR (powrót ok. 7.11)**, Byram day-to-day, Ellis poza sezonem. Źródła: ESPN, iHeart.
- **H2H:** ostatni mecz 25.01.2026: FLA 5-1.
- **Trendy:** Under w 6 z 7 ostatnich meczów FLA z drużynami z ujemnym bilansem (Covers). Over w 8 z 9 dziennych meczów CHI w United Center (Pick Dawgz).
- **Rynek:**
  - Moneyline: FLA -180/-182, CHI +150/+171 (iHeart, Inside The Rink). Bez marży FLA ok. 62-63%.
  - Total jest niejasny: jedno źródło podaje U5.5 -105, Pick Dawgz linię 6.5 (O +102 / U -122).

**Bramkarze:**
- FLA: **Akira Schmid, POTWIERDZONY** (DFO), bilans 2-2-1, 3,62 GAA, .867 (Pick Dawgz).
- CHI: Spencer Knight (5 ostatnich startów, 3-5-0, .888) albo Arvid Söderblom (0-2-0). Niepotwierdzony.
- Obaj są poniżej średniej ligi, co podnosi λ obu stron.

**λ (60'):** CHI 2,55 - FLA 3,25 (łącznie 5,8).
- Słaba defensywa CHI i brak Bedarda: -0,15 dla CHI.
- Absencje FLA (Barkov, Marchand): -0,2 dla FLA.
- Słaby Schmid: +0,2 dla CHI.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 60' CHI / X / FLA | 30,6% / 16,3% / 53,0% | 3.26 / 6.13 / 1.89 | niska-średnia |
| Moneyline FLA (z OT) | 61,5% | 1.63 | średnia |
| Moneyline CHI | 38,5% | 2.60 | – |
| FLA -1.5 / CHI +1.5 | 36,3% / 63,7% | 2.75 / 1.57 | niska |
| FLA +1.5 | 82,5% | 1.21 | średnia (krótki kurs) |
| Over / Under 5.5 | 52,2% / 47,8% | 1.92 / 2.09 | niska |
| Over / Under 6.5 | 39,1% / 60,9% | 2.56 / 1.64 | niska-średnia |
| Total FLA Over 2.5 | 63,0% | 1.59 | niska-średnia |
| Total CHI Under 3.5 | 74,7% | 1.34 | średnia |
| Total CHI Over 1.5 | 72,3% | 1.38 | niska-średnia |

**Kalibracja:** FLA 61,5% to ok. 1 pp pod rynkiem, mieści się w limicie. Formy FLA nie obniżałem, bo jest już w kursie. Na pułapie p obniżono FLA za konkretne absencje.

**Ryzyka:**
- Schmid (.867) może oddać mecz.
- Bez Barkova i Marchanda atak FLA jest przeciętny.
- CHI gra u siebie po dniu przerwy.
- Total jest niepewny, bo linia może wynosić 5.5 albo 6.5 zależnie od bukmachera.

**Typy z p>50% i fair>1.15:**
- **FLA ML 61,5% (1.63)**
- CHI U3.5 74,7% (1.34)
- FLA TT O2.5 63,0% (1.59)
- U6.5 60,9% (1.64)
- FLA +1.5 82,5% (1.21)

---

## 2. Dallas Stars - New York Islanders (25.10, 23:00 CET; 18:00 ET)

**Dane:**
- **Bilans:** DAL 6-3-1 (ostatnio 3-2 po dogrywce z WPG; Fox Sports), NYI 5-3-2.
- **Gole:**
  - NYI: 29 strzelonych (20. w lidze), 22 stracone, czyli ok. 2,9 / 2,2 na mecz.
  - DAL: 25 strzelonych, ok. 2,5 na mecz.
  - **Żaden z 10 meczów DAL nie przekroczył 5,5 gola** (Bleacher Nation).
- **PP:** NYI 20,0% (6/30), DAL 4 gole (27. w lidze). Źródło: NHL.com / Fox preview.
- **Absencje NYI:** Barzal (kolano), Romanov (ACL), Maccelli, Ritchie.
- **Absencje DAL:** Steel, Bäck, Duchene, Lindell out; Faksa możliwy; C. Hughes według Fox. Źródła: NHL.com, Fox.
- **H2H:** brak danych z tego sezonu.
- **Rynek:**
  - Moneyline: DAL -198/-200, NYI +164 (DraftKings, VegasInsider, Bleacher Nation). Bez marży DAL 63,7% (ScoresAndStats).
  - **Total 5.5.** Bleacher Nation daje Under 5.5 z projekcją 4,8 gola.

**Bramkarze (przewidywani, niepotwierdzeni według DFO):**
- DAL: **Oettinger** (8 z 10 startów, 1,23 GAA, .939).
- NYI: **Sorokin** (7 z 10 startów, 1,72 GAA, .934).
- Dwóch elitarnych bramkarzy w formie obniża λ obu stron. Gdyby zagrał Varlamov albo DeSmith: +0,15-0,25 dla rywala.

**λ:** DAL 2,85 - NYI 2,05 (łącznie 4,9).
- Atut własnego lodu i lepszy bilans DAL.
- Absencje NYI (Barzal, Romanov): -0,15 dla NYI.
- Absencje DAL (Duchene, Lindell): -0,1 dla DAL.
- Obaj bramkarze: około -0,2 dla każdej strony.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 60' DAL / X / NYI | 55,0% / 17,5% / 27,5% | 1.82 / 5.71 / 3.64 | niska-średnia |
| Moneyline DAL | 64,2% | 1.56 | średnia |
| DAL -1.5 / NYI +1.5 | 36,7% / 63,3% | 2.73 / 1.58 | niska |
| DAL +1.5 | 85,7% | 1.17 | (blisko progu 1.15-1.20) |
| **Under 5.5** | **63,4%** | **1.58** | **średnia** (warunek: Oettinger + Sorokin) |
| Under 6.5 | 75,4% | 1.33 | średnia |
| Over 4.5 | 57,7% | 1.73 | niska |
| Total NYI Under 2.5 | 66,3% | 1.51 | średnia |
| Total DAL Over 1.5 | 77,7% | 1.29 | średnia |
| Total DAL Over 2.5 | 54,2% | 1.85 | niska |

**Kalibracja:**
- DAL 64,2% vs rynek 63,7%: zgodność.
- Under 5.5 opiera się na konkretach: dwóch bramkarzy z SV% > .930, słabe PP DAL, absencje ofensywne NYI, 10/10 meczów DAL na Under 5.5. Nie jest to więc sama forma.
- Pewność najwyżej średnia, bo bramkarze są niepotwierdzeni.

**Ryzyka:**
- Zmiana bramkarza (np. DeSmith) mocno uderza w Under.
- Gole do pustej bramki.
- Regresja SV% (.939 i .934 są nie do utrzymania).

**Typy z p>50% i fair>1.15:**
- **Under 5.5 63,4% (1.58)**
- **DAL ML 64,2% (1.56)**
- NYI TT U2.5 66,3% (1.51)
- U6.5 75,4% (1.33)
- DAL TT O1.5 77,7% (1.29)
- DAL +1.5 85,7% (1.17, oznaczone)

---

## 3. Winnipeg Jets - Montréal Canadiens, Heritage Classic (26.10, 00:00 CET; 25.10, 19:00 ET)

**Dane:**
- **Bilans:** WPG 4-3-3, **4 porażki z rzędu** (ostatnia 2-3 po dogrywce w DAL; AP/ABC). MTL 5-3-2 po wygranej 4-1 w CHI.
- **Gole:** MTL strzela 3,20 i traci 3,50, WPG strzela 2,60 i traci 2,90. Źródło: ESPN.
- **PK:** MTL 81,0%, WPG 80,8% (ESPN).
- **Hellebuyck oddany do NJ 23.10** (za Mercera, Bjugstada, Dawsa i picki; NHL.com, Global News). Jets wchodzą w „nową erę” właśnie na Heritage Classic. Mercer i Bjugstad mogą zadebiutować, ich status jest niepotwierdzony.
- **Absencje MTL:** **Suzuki out 2-4 tyg.** (górna część ciała; Squawka, AP), Montembeault na liście kontuzji.
- **Absencje WPG:** Namestnikov, G. Brown.
- **Warunki:** otwarty stadion. Prognoza Environment Canada: słonecznie, ok. 5°C w dzień i **ok. -4°C w nocy, bezchmurnie** (Squawka). Mróz sprzyja jakości lodu, ale gra na zewnątrz zwykle jest mniej płynna (wiatr, oświetlenie, gorsze odbicia).
- **H2H:** brak danych z tego sezonu.
- **Rynek:**
  - Moneyline: MTL -115/-118, WPG -102 (Bleacher Nation, SportsLine), czyli MTL ok. 52-53% bez marży.
  - Total 5.5: Bleacher Nation daje Over (projekcja 6,2), a Hockeynomist i Pick Dawgz Under.
  - Kyle Connor gol +135 (ats.io; 9 G w 10 meczach).

**Bramkarze (niepotwierdzeni):**
- MTL: **Jacob Fowler** (DFO „unconfirmed”; 4-1, 1,94 GAA, .910 według ESPN), alternatywa Dobeš.
- WPG: **Stuart Skinner** (3-1-3, 2,67 GAA, .912), praktycznie jedyny realny starter po odejściu Hellebuyecka. Zmiennik Clay Stevenson (z waivers) albo Daws (z NJ).
- Brak Hellebuyecka jest już w liczbach Skinnera i w kursie.

**λ:** WPG 2,70 - MTL 2,80 (łącznie 5,5).
- Brak Suzukiego: -0,15 dla MTL.
- Atut domu WPG jest mniejszy na neutralnym, otwartym obiekcie (+0,05 zamiast +0,1).
- Gra na zewnątrz: -0,05 dla każdej strony.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 60' WPG / X / MTL | 39,6% / 17,4% / 42,9% | 2.52 / 5.74 / 2.33 | niska |
| Moneyline MTL | 51,7% | 1.93 | niska (**brak mocnego typu**) |
| Moneyline WPG | 48,3% | 2.07 | niska |
| MTL +1.5 / WPG +1.5 | 75,9% / 73,1% | 1.32 / 1.37 | niska-średnia |
| Over / Under 5.5 | 47,1% / 52,9% | 2.12 / 1.89 | niska |
| Under 6.5 | 65,7% | 1.52 | średnia-niska |
| Total WPG Under 3.5 | 71,4% | 1.40 | niska-średnia |
| Total MTL Under 3.5 | 69,2% | 1.45 | niska-średnia |
| K. Connor gol (λ 0,45) | 36,2% | 2.76 | niska (rynek +135 = 42,6%; brak typu) |

**Ryzyka:**
- Mecz jest wyrównany, a dogrywka padnie w ok. 17-23% przypadków.
- Na otwartym stadionie możliwy wiatr albo opóźnienie.
- Debiut nowych zawodników WPG.
- Bramkarz MTL jest niepotwierdzony.

**Typy z p>50% i fair>1.15:**
- Under 6.5 65,7% (1.52)
- WPG TT U3.5 71,4% (1.40)
- MTL TT U3.5 69,2% (1.45)
- MTL +1.5 75,9% (1.32)
- MTL ML 51,7% (1.93) to brak mocnego typu.

---

## 4. Nashville Predators - Colorado Avalanche (26.10, 01:00 CET; 25.10, 20:00 ET)

**Dane:**
- **Bilans:** COL 5-4-1 (Picks and Parlays), po wygranej 6-3 z TBL 23.10 (MacKinnon 4 pkt; NHL.com). Wcześniej MacKinnon był bez punktów w porażkach z PHI i NJ. Ma 6 meczów wielopunktowych i 4 bez punktu (ats.io).
- **NSH:** 3-3-4 po 2-3 po dogrywce w PIT 24.10 i 0-6 w BOS 22.10.
- **Statystyki (źródła sprzeczne):**
  - Fox Sports: COL 3,6 strzelonych / 2,4 straconych, NSH 3,0 / 3,3.
  - ESPN (prawdopodobnie nieaktualne): COL 4,43 GF, PP 20%, PK 82,4%; NSH 2,57 GF, **PP 26,9%**, PK 86,4%.
  - Wcześniejsze dane (Inside The Rink): NSH 2,56 GF, PP 28,6% (3.).
- **B2B NSH:** drugi dzień, lot PIT → NSH. Saros obronił wczoraj 34 strzały.
- **H2H:** brak danych z tego sezonu.
- **Rynek:**
  - Moneyline: COL -203, NSH +178 (Picks and Parlays). Kalshi/Polymarket 67-71% dla COL, czyli bez marży ok. 65-68%.
  - Total 5.5: Picks and Parlays proponuje Over 5.5 przy -120 lub lepiej. Linii z kursem nie potwierdziłem.

**Bramkarze (niepotwierdzeni):**
- COL: **Mackenzie Blackwood** (DFO, przewidywany).
- NSH: według Kalshi/CBS najpewniej **Justus Annunen** (.806 według Kalshi), bo w drugim dniu B2B zwykle gra rezerwowy. Starsza notatka mówi jednak, że Annunen był na IR, a z AHL ściągnięto Murraya, więc **tożsamość rezerwowego jest niepewna**. Saros jest możliwy, ale mało prawdopodobny po 34 obronach.

**λ:** NSH 2,45 - COL 3,50 (łącznie 5,95).
- Słaby rezerwowy NSH: +0,3 dla COL.
- B2B NSH: -0,1 dla NSH i gorsza obrona.
- Mocne PP NSH: +0,05.
- COL obniżone z 3,6 do 3,5, żeby nie wyjść ponad rynek i pułap ok. 67%.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 60' NSH / X / COL | 25,9% / 15,4% / 58,7% | 3.85 / 6.50 / 1.70 | średnia |
| **Moneyline COL** | **66,8%** | **1.50** | **średnia** (bramkarz NSH niepotwierdzony) |
| COL -1.5 / NSH +1.5 | 42,0% / 58,0% | 2.38 / 1.72 | niska |
| COL +1.5 | 85,8% | 1.17 | (oznaczone 1.15-1.20) |
| Over / Under 5.5 | 54,6% / 45,4% | 1.83 / 2.20 | niska-średnia |
| Over / Under 6.5 | 41,4% / 58,6% | 2.41 / 1.71 | niska |
| Total COL Over 2.5 | 67,9% | 1.47 | średnia |
| Total NSH Under 3.5 | 76,8% | 1.30 | średnia |
| MacKinnon 2+ pkt | brak średniej z dwóch źródeł | – | brak typu |

**Ryzyka:**
- Jeśli zagra jednak Saros, λ COL spada o ok. 0,3, a p COL do ok. 62%.
- Mocne PP NSH.
- Forma COL jest niestabilna (porażki z PHI i NJ).

**Typy z p>50% i fair>1.15:**
- **COL ML 66,8% (1.50)**
- COL TT O2.5 67,9% (1.47)
- NSH TT U3.5 76,8% (1.30)
- 60' COL 58,7% (1.70)
- Over 5.5 54,6% (1.83, niska pewność)
- U6.5 58,6% (1.71, niska)
- COL +1.5 85,8% (1.17, oznaczone)

---

## 5. Vancouver Canucks - Minnesota Wild (26.10, 03:00 CET; 25.10, 22:00 ET / 19:00 PT)

**Dane:**
- **Bilans:** MIN 7-3-2 po 5-1 w SEA 24.10. **VAN 2-9-1, 9 porażek z rzędu**, ostatnio 2-5 z DET (Inside The Rink, Yahoo, NHL.com Canucks).
- **Kaprizov:** 12 G w 12 meczach (11 G w 11 meczach przed 24.10 według NHL.com, plus gol 24.10).
- **Quinn Hughes** wraca do Vancouver jako zawodnik MIN. Asystował przy golu Kaprizova (ESPN).
- **Wcześniej (z analizy 24.10):** MIN tracił 2,45 gola (5.), PP 25,7%, PK 78,4%. Gustavsson out (biodro), Foligno out.
- **Statystyki VAN (GF/GA, PK):** nie znalazłem. Według ats.io PK VAN jest słabe.
- **B2B MIN:** drugi dzień, 4. mecz z 5 na wyjeździe. Lot z Seattle jest krótki.
- **H2H:** pierwszy mecz w sezonie.
- **Rynek:**
  - Moneyline: MIN -194, VAN +170 (Picks and Parlays). Kalshi/Polymarket ok. 66%, czyli bez marży MIN ok. 64-65%.
  - SGP (Sports Gambling Podcast): MIN ML -177.
  - Total: linia z kursem niepotwierdzona. Picks and Parlays proponuje Over 5.5 -120, Hockeynomist Under 5.5 +115.
  - Covers: Kaprizov gol -120.

**Bramkarze:**
- MIN: **Calvin Pickard, POTWIERDZONY** (THN/Yahoo, DFO). To jego drugi start w sezonie. W karierze z VAN ma 2-2-2, 2,48 GAA, .909.
- VAN: **niepotwierdzony.** CBS podaje Meriläinena przed Lankinenem, Demko na IR (biodro, do ok. 21.12).

**λ:** VAN 2,50 - MIN 3,30 (łącznie 5,8).
- Słaby VAN i rezerwowy bramkarz VAN: +0,2 dla MIN.
- B2B: -0,1 dla MIN.
- Pickard zamiast Wallstedta: +0,15 dla VAN.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 60' VAN / X / MIN | 29,2% / 16,1% / 54,7% | 3.43 / 6.20 / 1.83 | niska-średnia |
| **Moneyline MIN** | **63,1%** | **1.58** | **średnia** |
| MIN -1.5 / VAN +1.5 | 37,9% / 62,1% | 2.64 / 1.61 | niska |
| MIN +1.5 | 83,6% | 1.20 | (oznaczone 1.15-1.20) |
| Over / Under 5.5 | 52,2% / 47,8% | 1.92 / 2.09 | niska |
| Under 6.5 | 60,9% | 1.64 | niska-średnia |
| Total MIN Over 2.5 | 64,1% | 1.56 | średnia-niska |
| Total VAN Under 3.5 | 75,8% | 1.32 | średnia |
| Kaprizov gol (λ 0,52 po regresji) | 40,5% | 2.47 | niska (rynek -120 = 54,5% wygląda na przeszacowany, brak typu) |

**Kalibracja:**
- MIN 63,1% to ok. 1-2 pp pod rynkiem, z konkretnych powodów: B2B i Pickard.
- Serii porażek VAN nie dokładałem jako „kryzysu” ponad rynek, bo jest już w kursie.

**Ryzyka:**
- Zmęczenie MIN w trzeciej tercji.
- Pickard to słabszy bramkarz.
- Efekt powrotu Hughesa (motywacja VAN).
- Seria VAN statystycznie musi się kiedyś skończyć.

**Typy z p>50% i fair>1.15:**
- **MIN ML 63,1% (1.58)**
- MIN TT O2.5 64,1% (1.56)
- VAN TT U3.5 75,8% (1.32)
- 60' MIN 54,7% (1.83)
- U6.5 60,9% (1.64)
- MIN +1.5 83,6% (1.20, oznaczone)

---

## Ranking (wszystkie rynki, fair > 1.15; przypadki 1.15-1.20 oznaczone)

| # | Mecz | Rynek | p | fair | pewność | zależy od |
|---|---|---|---|---|---|---|
| 1 | NSH-COL | NSH total Under 3.5 | 76,8% | 1.30 | średnia | bramkarz NSH (bez znaczenia, jeśli Saros) |
| 2 | VAN-MIN | VAN total Under 3.5 | 75,8% | 1.32 | średnia | bramkarz VAN |
| 3 | DAL-NYI | Under 6.5 | 75,4% | 1.33 | średnia | Oettinger/Sorokin |
| 4 | CHI-FLA | CHI total Under 3.5 | 74,7% | 1.34 | średnia | Schmid potwierdzony |
| 5 | NSH-COL | COL Over 2.5 | 67,9% | 1.47 | średnia | rezerwowy NSH |
| 6 | NSH-COL | COL ML | 66,8% | 1.50 | średnia | rezerwowy NSH |
| 7 | DAL-NYI | NYI total Under 2.5 | 66,3% | 1.51 | średnia | Oettinger |
| 8 | WPG-MTL | Under 6.5 | 65,7% | 1.52 | średnia-niska | bramkarze, warunki |
| 9 | DAL-NYI | DAL ML | 64,2% | 1.56 | średnia | bramkarze |
| 10 | DAL-NYI | Under 5.5 | 63,4% | 1.58 | średnia | Oettinger + Sorokin |
| 11 | VAN-MIN | MIN ML | 63,1% | 1.58 | średnia | Pickard (potwierdzony) |
| 12 | CHI-FLA | FLA ML | 61,5% | 1.63 | średnia | Schmid (potwierdzony), bramkarz CHI |
| – | oznaczone 1.15-1.20 | DAL +1.5 (1.17), COL +1.5 (1.17), MIN +1.5 (1.20) | | | | |

**Tabela kandydatów na kupon (dla `bet-slip-builder`):**

| Mecz | Rynek | p | fair | pewność | od czego zależy | kurs rynkowy znany? |
|---|---|---|---|---|---|---|
| COL@NSH | COL ML | 66,8% | 1.50 | średnia | bramkarz NSH (Annunen/Murray vs Saros) | tak: -203 ≈ 1.49 (Picks and Parlays), brak value |
| MIN@VAN | MIN ML | 63,1% | 1.58 | średnia | B2B, bramkarz VAN | tak: -194 ≈ 1.52, -177 ≈ 1.56 (SGP) |
| NYI@DAL | DAL ML | 64,2% | 1.56 | średnia | bramkarze | tak: -198 ≈ 1.51 |
| NYI@DAL | Under 5.5 | 63,4% | 1.58 | średnia | Oettinger + Sorokin | linia 5.5 tak, kurs Under nieznany |
| FLA@CHI | FLA ML | 61,5% | 1.63 | średnia | Knight/Söderblom | tak: -181 ≈ 1.55 |
| MTL@WPG | Under 6.5 | 65,7% | 1.52 | średnia-niska | Fowler, wiatr | nie (rynek główny 5.5) |
| totale drużyn (CHI U3.5, VAN U3.5, NSH U3.5, NYI U2.5, COL O2.5, MIN O2.5) | patrz tabele | | | | | nie |

**Uwagi końcowe:**
- Moneyline faworytów w kursach (ok. 1.49-1.56) są bliskie albo poniżej moich fair odds, więc value w ML jest marginalne albo ujemne. Ewentualnego value trzeba szukać w totalach drużyn i w Under 5.5 DAL-NYI, ale te kursy trzeba pobrać z Betclic.
- Bramkarzy sprawdziłem około przedpołudnia CET 25.10. Składy mogą się zmienić do rozpoczęcia meczu, więc przed kuponem potwierdź startujących (DFO/NHL.com).
- To oszacowania probabilistyczne, nie gwarancje.

**Źródła (WebSearch):**
- Terminarz, previews i statystyki: [Inside The Rink FLA@CHI](https://insidetherink.com/stats/nhl/games/2026-10-25-panthers-at-blackhawks-2026020180/), [NHL.com Panthers preview](https://www.nhl.com/panthers/news/preview-panthers-try-to-pick-up-first-win-of-road-trip-in-chicago), [iHeart FLA-CHI](https://foxsports940.iheart.com/content/2026-10-24-panthers-vs-blackhawks-prediction-picks-oct-25/), [Pick Dawgz FLA-CHI](https://pickdawgz.com/nhl-picks/panthers-vs-blackhawks-prediction-10-25-2026-todays-nhl-picks/), [ESPN FLA-CHI](https://www.espn.com/nhl/game/_/gameId/401892578/panthers-blackhawks), [Covers FLA-CHI](https://www.covers.com/sport/hockey/nhl/matchup/382456), [Bleacher Nation DAL-NYI](https://www.bleachernation.com/picks/2026/10/25/stars-vs-islanders-nhl-best-bets-odds-prediction-and-pick-oct-25/), [NHL.com NYI@DAL](https://www.nhl.com/news/new-york-islanders-dallas-stars-game-preview-october-25-2026), [Fox DAL-NYI](https://www.foxsports.com/articles/nhl/stars-host-the-islanders-after-overtime-win), [ScoresAndStats NYI-DAL](https://www.scoresandstats.com/predictions/hockey/nhl/new-york-islanders-vs-dallas-stars-odds-picks/2026-10-25/), [DocSports](https://www.docsports.com/free-picks/nhl-hockey/2026/new-york-islanders-vs-dallas-stars-prediction-10-25-2026-nhl-picks-best-bets-odds.html), [Squawka Heritage Classic](https://www.squawka.com/ca/news/nhl/heritage-classic-2026/), [AP/ABC Jets-Canadiens](https://abcnews.com/Sports/wireStory/jets-bring-4-game-losing-streak-matchup-canadiens-137533449), [Bleacher Nation MTL-WPG](https://www.bleachernation.com/picks/2026/10/25/canadiens-vs-jets-nhl-best-bets-odds-prediction-and-pick-oct-25/), [SportsLine MTL-WPG](https://www.sportsline.com/insiders/canadiens-vs-jets-odds-line-2026-nhl-heritage-classic-best-bets-from-proven-model/), [ESPN MTL-WPG](https://www.espn.com/nhl/game/_/gameId/401891807/canadiens-jets), [NHL.com Hellebuyck trade](https://www.nhl.com/news/topic/trade-coverage/connor-hellebuyck-traded-to-new-jersey-devils-from-winnipeg-jets), [NHL.com Jets reset](https://www.nhl.com/news/winnipeg-jets-will-reset-after-connor-hellebuyck-traded-to-new-jersey-devils), [ats.io MTL-WPG props](https://ats.io/nhl/props/montreal-canadiens-winnipeg-jets-10-25-2026/), [Picks and Parlays COL-NSH](https://picksandparlays.net/free-picks/nhl/colorado-avalanche-vs-nashville-predators-picks-and-predictions-for-sunday-october-25-2026), [Polymarket COL-NSH](https://polymarket.com/sports/nhl/nhl-col-nsh-2026-10-25), [NHL.com Avalanche recap 23.10](https://www.nhl.com/avalanche/news/game-recap-10-23-26), [NHL.com Avalanche preview](https://www.nhl.com/avalanche/news/game-preview-avalanche-at-predators-339126618), [Fox COL-NSH](https://www.foxsports.com/nhl/colorado-avalanche-vs-nashville-predators-oct-25-2026-game-boxscore-44738?tab=boxscore), [ats.io COL-NSH](https://ats.io/nhl/props/colorado-avalanche-nashville-predators-10-25-2026/), [Kalshi starting goalies](https://kalshi.com/nhl/starting-goalies), [CBS NSH depth chart](https://www.cbssports.com/nhl/teams/NSH/nashville-predators/depth-chart/), [NHL.com Canucks preview](https://www.nhl.com/canucks/news/canucks-host-wild-to-close-out-homestand-on-sunday-night), [Inside The Rink MIN@VAN](https://insidetherink.com/stats/nhl/games/2026-10-25-wild-at-canucks-2026020184/), [THN Wild goalie plan](https://thehockeynews.com/nhl/minnesota-wild/game-day/wild-announce-goalie-plan-for-saturday-sundays-back-to-back), [Picks and Parlays MIN-VAN](https://picksandparlays.net/free-picks/nhl/minnesota-wild-vs-vancouver-canucks-picks-and-predictions-for-sunday-october-25-2026), [SGP best bet](https://www.sportsgamblingpodcast.com/2026/10/24/best-bet-for-sunday-oct-25th-nhl-predictions/), [Polymarket MIN-VAN](https://polymarket.com/sports/nhl/nhl-min-van-2026-10-25), [CBS VAN depth chart](https://www.cbssports.com/nhl/teams/van/vancouver-canucks/depth-chart/), [Hockeynomist 25.10](https://hockeconomics.substack.com/p/nhl-picks-sunday-october-25-2026), [DFO starting goalies 25.10](https://www.dailyfaceoff.com/starting-goalies/2026-10-25).
- Wyniki z 24.10: [NHL.com PIT-NSH](https://nhl.com/news/nashville-predators-pittsburgh-penguins-game-recap-october-24-2026), [AP/ABC PIT-NSH](https://abcnews.com/Sports/wireStory/ville-koivunen-scores-ot-penguins-rally-3-2-137546064), [AP/ABC MIN-SEA](https://abcnews.com/Sports/wireStory/kaprizov-scores-early-wild-defeat-kraken-5-1-137548327), [ESPN MIN-SEA](https://www.espn.com/nhl/boxscore/_/gameId/401892577).
## NBA, niedziela 25.10.2026 (USA), czas polski CET

Skill: `nba-analyst` (kroki 1-4 dla każdego meczu), skrypty `nba_model.py` i `nba_props.py team_points`. Stan danych: 25.10 rano/w ciągu dnia (CET), wyłącznie WebSearch (ok. 29 zapytań). **Statusy zawodników mogą się zmienić do ok. 90 min przed tip-offem.**

## Ograniczenia danych (obniżają pewność wszystkich typów)
- MCP `sportsdata` nie połączył się (ENOENT), WebFetch/curl zablokowane, BettingPros nieużywany (zgodnie z zadaniem). Jedyne źródło: snippety WebSearch. **Linie z portali typerskich (CappersPicks, Pick Dawgz, Covers, iHeart/Fox, Dimers, Polymarket)**, nie z Betclic. Część z nich się nie zgadza (zaznaczam).
- Bieżące net rating / pace / ORtg / DRtg 2026-27 to próba 2-3 meczów (NBAstuffer ma tabelę, ale snippet pokazuje po 1 meczu) i nie mają wartości. **Rating drużyny = win total (przeliczony (W-41)/2,7 pkt) i zakotwiczenie w linii rynku**; tempo z totalu rynku. Total i spread przy linii rynku wychodzą blisko 50/50 z założenia.
- **Rynków zawodnika nie wyceniam**: średnie z 2 meczów z jednego źródła (ESPN; Sportsmole je powiela), linie propsów sprzeczne (Dončić Over 24,5 wg Sportsmole vs 32,5 w meczu 23.10 wg FanDuel). Wymóg skilla (2 niezależne źródła + potwierdzone minuty) niespełniony.
- SD podniesione: różnica 13,5 (DET@PHI 14,5), suma 19,5 (DET@PHI 20).

## Terminarz (zweryfikowany) i back-to-back
Wszystkie 7 par potwierdzone w źródłach z 24-25.10 (ESPN gameId, CappersPicks, iHeart, Covers, Heavy, NBA TV PR). Inne pary z Sports Media Watch nie znalazły potwierdzenia.

| # | Mecz | ET | CET |
|---|---|---|---|
| 1 | Lakers @ Jazz | 17:00 | 22:00 (25.10) |
| 2 | Pacers @ Nets | 18:00 | 23:00 |
| 3 | Clippers @ Thunder | 19:00 | 00:00 (26.10) |
| 4 | Magic @ Knicks | 19:00 | 00:00 |
| 5 | Raptors @ Timberwolves | 19:00 | 00:00 |
| 6 | Pistons @ 76ers | 19:30 | 00:30 |
| 7 | Grizzlies @ Kings | 21:00 | 02:00 |

**Back-to-back (drugi dzień, mecze 24.10):** **BKN** (przegrali 121-125 @CLE 24.10 wieczorem, lot do NY, mecz o 18:00 ET - Yahoo/Field Level Media) i **PHI** (wygrali 127-116 z MIL 24.10 u siebie - ESPN/NBC Sports Philadelphia). Reszta grała 23.10 (1 dzień przerwy), OKC od 22.10 (2 dni).

Wyniki sezonu (ESPN, z plików weryfikacji 20-23.10 + 24.10 z WebSearch): LAL 2-0 (127-105 GSW, 125-117 LAC); UTA 1-1 (103-123 @MEM, 120-119 NOP); IND 1-1 (123-120 @NOP, 105-121 DAL); BKN 0-2 (103-110 CHA, 121-125 @CLE); OKC 2-0 (116-104 @SA, 96-84 DEN); LAC 1-1 (121-96 SAC, 117-125 @LAL, 26 strat); ORL 0-2 (125-132 ATL, 93-115 MIN); NYK 0-2 (100-106 PHI, 103-107 @BOS); TOR 2-0 (135-92 CHI, 112-102 @WAS); MIN 2-0 (131-106 @MIA, 115-93 @ORL); DET 2-0 (121-113 BOS, 128-111 @MIA); PHI 3-0; MEM 2-0 (123-103 UTA, 111-108 @GSW); SAC 0-2 (96-121 @LAC, 120-128 POR).

Win totals 2026-27 (SportsBettingDime/BetMGM/Betfanatics/Complex, rozbieżności ±1-2): OKC 60,5 | NYK 52,5 | PHI 50,5 | DET 49,5 | MIN 48,5 | LAL 46,5 | TOR 45,5 | IND 44,5 | ORL 43,5 | UTA 35,5 | LAC 27,5-30,5 | MEM 28,5-29,5 | BKN 24,5 | SAC 20,5-21,5.

---

### 1. Utah Jazz - Los Angeles Lakers (25.10, 22:00 CET; 17:00 ET)
**Dane:** LAL 2-0, Dončić 25,5 pkt i 7 as. na mecz (ESPN/Sportsmole, 2 mecze), w składzie Reaves i Kessler; Out: Adou Thiero, Cameron Carr; LaRavia wraca po skręceniu kostki (Lakers Daily). UTA 1-1, Keyonte George 20,5 pkt / 7,5 as. (ESPN), Markkanen i Jaren Jackson Jr. w rdzeniu (NBA.com preview); **Nurkić Out** (stopa), Trey Alexander Out/DTD (ESPN vs Pick Dawgz). Obie drużyny odpoczęte 1 dzień, LAL podróż + wysokość SLC.
**Rynek:** LAL -6,5, total 235,5 (ESPN) / 236,5 (Pick Dawgz: O -105 / U -115), ML LAL -238 / UTA +196 (CappersPicks) → bez marży LAL 67,6%. Outlier: Sportsmole LAL -11,5 / 228,5 (odrzucam). Dimers: LAL 63,3%, projekcja 119-115.
**H2H:** LAL wygrali 3 ostatnie mecze ze średnią +11,3 (Pick Dawgz), ale z innymi składami; waga mała.
**Wejścia modelu:** win totals dają tylko LAL -1,5 (LAL +2,0, UTA -2,0, HCA +2,5); rynek -6,5 uwzględnia słabe UTA i absencję Nurkicia. Nie schodzę pod rynek o > 5 pp bez informacji: **UTA 115,25 - LAL 120,75** (LAL -5,5; total 236), SD 13,5/19,5.

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| LAL ML | 67,2% | 1,49 | niska/średnia |
| UTA ML | 32,8% | 3,05 | niska |
| LAL -6,5 (linia rynku) | 47,0% | 2,13 | brak typu |
| UTA +6,5 | 53,0% | 1,89 | niska |
| UTA +8,5 | 58,8% | 1,70 | niska |
| LAL -4,5 | 53,0% | 1,89 | niska |
| Total 235,5 Over / Under | 51,0 / 49,0% | 1,96 / 2,04 | brak typu |
| Total LAL Over 116,5 | 64,4% | 1,55 | niska |
| Total UTA Over 111,5 | 62,8% | 1,59 | niska |

**Ryzyka:** mecz o 17:00 ET (wczesny) w Salt Lake City; jeśli rynek ma rację co do -6,5, UTA +6,5 to rzut monetą; LaRavia bez limitu minut niepotwierdzony.
**Typy z p>50% i fair>1.15:** LAL ML 67,2% / 1,49 (niska/średnia, zgodne z rynkiem); UTA +8,5 58,8% / 1,70 (niska, alt-linia); total LAL Over 116,5 64,4% / 1,55 (niska, linia drużyny rynkowa nieznana).

### 2. Brooklyn Nets - Indiana Pacers (25.10, 23:00 CET; 18:00 ET)
**Dane:** IND 1-1 (L 105-121 z DAL 23.10). Out: T.J. McConnell, Johnny Furphy, Ben Sheppard (kolano); Aaron Nesmith Probable (ścięgno, NBC Sports 24.10) (CappersPicks, Pick Dawgz). BKN 0-2, **drugi dzień B2B** po 121-125 w Clevelandzie (Michael Porter Jr. 28 pkt, Randle 23, Demin 22 - Yahoo), wczesny tip-off 18:00 ET. Tyler Bilodeau Q/Out (bark).
**Rynek:** IND -7,5 (-105) / BKN +7,5 (-115), total 231,5, ML IND -278 / BKN +223/+225 (Pick Dawgz, CappersPicks) → bez marży IND 70,4%. Wcześniejsza linia IND -2,5 / 232,5 (Picks and Parlays) przestarzała. CappersPicks AI: 118-110.
**H2H:** poprzedni sezon, składy zmienione, waga ~0.
**Wejścia modelu:** IND +1,3, BKN -6,1, HCA +2,5, B2B BKN -1,5 → IND -6,4; z rynkiem -7,5 przyjmuję **BKN 112 - IND 119** (IND -7; total 231, B2B -1 pkt sumy), SD 13,5/19,5.

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| IND ML | 71,1% | 1,41 | niska/średnia |
| BKN ML | 28,9% | 3,46 | niska |
| IND -7,5 (linia rynku) | 48,5% | 2,06 | brak typu |
| BKN +7,5 | 51,5% | 1,94 | brak typu |
| IND -3,5 | 60,2% | 1,66 | niska |
| IND -2,5 | 63,1% | 1,59 | niska |
| Total 231,5 Over / Under | 49,0 / 51,0% | 2,04 / 1,96 | brak typu |
| Under 232,5 | 53,1% | 1,88 | niska |
| Total IND Over 115,5 | 62,0% | 1,61 | niska |
| Total BKN Over 108,5 | 62,0% | 1,61 | niska |

**Ryzyka:** IND przegrał u siebie z osłabionym DAL (forma faworyta w kursie, bez korekty); BKN pokazał ofensywę w CLE (121 pkt). Trzy absencje rotacyjne IND.
**Typy z p>50% i fair>1.15:** IND ML 71,1% / 1,41 (niska/średnia); IND -3,5 60,2% / 1,66 (niska, alt-linia).

### 3. Oklahoma City Thunder - LA Clippers (26.10, 00:00 CET; 19:00 ET)
**Dane:** OKC 2-0 (96-84 z DEN; seria SGA 141 meczów z 20+ pkt przerwana - Yardbarker/JOX), 2 dni odpoczynku. Out: Otega Oweh (sezon, Achilles); Topić i Sorber DTD/Out (iHeart vs ESPN). Statusy Holmgrena i J. Williamsa niepotwierdzone (brak na raportach). LAC 1-1, 26 strat w 117-125 @LAL 23.10, dzień przerwy + lot. **Out: Beal, Ingram, Strus, Konan Niederhäuser, Miller** (ESPN; iHeart podaje Beala/Ingrama/Niederhäusera jako DTD). Statusy Leonarda i Garlanda: brak informacji.
**Rynek:** OKC -14,5, total 221,5 (CappersPicks; VegasInsider - otwarcie), ML OKC ok. -1200 (Bovada wg BettingNews, raczej zawyżone), LAC +700 (VegasInsider), Polymarket OKC 85%. Dimers: 85,4%, projekcja 116-104.
**H2H:** poprzedni sezon, waga ~0.
**Wejścia modelu:** OKC +7,2, LAC -4,6, HCA +2,5 → -14,3; odpoczynek OKC vs dzień przerwy + podróż LAC +0,7 → **OKC 118 - LAC 103** (OKC -15; total 221), SD 13,5/19,5.

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| OKC ML | 85,9% | 1,16 | średnia (fair 1,15-1,20: oznaczone) |
| LAC ML | 14,1% | 7,07 | niska |
| OKC -14,5 (linia rynku) | 51,5% | 1,94 | brak typu |
| OKC -10,5 | 63,1% | 1,59 | niska/średnia |
| OKC -8,5 | 68,5% | 1,46 | niska/średnia |
| Total 221,5 Over / Under | 49,0 / 51,0% | 2,04 / 1,96 | brak typu |
| Total OKC Over 114,5 | 62,0% | 1,61 | niska |
| Total LAC Under 101,5 | 44,8% | 2,23 | brak typu |

**Ryzyka:** spread ≥ 10 = blowout, rezerwy OKC w 4. kwarcie (zagraża -14,5 i Over drużyny OKC, nie ML); Leonard zagra pełne minuty → LAC lepszy niż -15; Holmgren/Williams poza grą (nieznane).
**Typy z p>50% i fair>1.15:** OKC ML 85,9% / 1,16 (formalnie powyżej 1,15, przypadek 1,15-1,20, wartość w kuponie znikoma); OKC -8,5 68,5% / 1,46 (niska/średnia, alt-linia); OKC -10,5 63,1% / 1,59.

### 4. New York Knicks - Orlando Magic (26.10, 00:00 CET; 19:00 ET)
**Dane:** NYK 0-2 (porażki 6 i 4 pkt), injury report pusty (iHeart, Field Level Media; jedno źródło: Alvarado Q, kostka). ORL 0-2 (93-115 z MIN). **Paolo Banchero Out** (niski stopień high ankle sprain, kilka tygodni - ESPN, CBS, Yahoo). Out też Jonathan Isaac, Noah Penda, Izaiyah Nelson; **Anthony Black Q** (kostka, HotTakes/iHeart). Franz Wagner zdrowy. Oba zespoły odpoczęte 1 dzień (ORL grał 23.10 u siebie, NYK w Bostonie).
**Rynek:** NYK -7,5, total 224,5, ML NYK -320 / ORL +255 (CappersPicks; Sportsmole NYK -333) → bez marży NYK 73,0%. Starsze SI -6,5 / 220,5 odrzucam (inny mecz).
**H2H:** seria play-off 2025 i sezon 2025-26, inne składy; waga mała.
**Wejścia modelu:** NYK +4,3, ORL +0,9, HCA +2,5 → -5,9; Banchero Out -3 (gwiazda, część już w linii), Black Q -0,5 → **NYK 116,25 - ORL 107,75** (NYK -8,5; total 224), SD 13,5/19,5. Różnica z rynkiem 1 pkt (< 3, OK).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| NYK ML | 72,3% | 1,38 | średnia |
| ORL ML | 27,7% | 3,61 | niska |
| NYK -7,5 (linia rynku) | 53,0% | 1,89 | niska |
| NYK -5,5 | 58,8% | 1,70 | niska/średnia |
| NYK -3,5 | 64,4% | 1,55 | niska/średnia |
| Total 224,5 Over / Under | 49,0 / 51,0% | 2,04 / 1,96 | brak typu |
| Total NYK Over 112,5 | 62,8% | 1,59 | niska |
| Total ORL Under 106,5 | 45,7% | 2,19 | brak typu |

**Ryzyka:** NYK 0-2 (forma faworyta w kursie, nie obniżam); Black zagra → ORL ok. +0,5; reakcja drużyny po urazie lidera bywa krótkotrwale pozytywna.
**Typy z p>50% i fair>1.15:** NYK ML 72,3% / 1,38 (średnia); NYK -5,5 58,8% / 1,70 (niska/średnia); NYK -7,5 53,0% / 1,89 (niska, minimalna przewaga).

### 5. Minnesota Timberwolves - Toronto Raptors (26.10, 00:00 CET; 19:00 ET)
**Dane:** oba 2-0. MIN: Edwards 30 pkt/mecz, LaMelo Ball 16,5 (Deadspin), debiut Balla w Target Center (NBA TV PR); **DiVincenzo Out** (Achilles). TOR: Barnes 25,5 pkt / 10 zb. (Deadspin), Leonard w zapowiedzi Fox Sports jako grający (brak na raporcie iHeart, niepotwierdzone oficjalnie); **Nate Bittle Out** (stopa). Oba odpoczęte 1 dzień (TOR z Waszyngtonu, MIN z Orlando).
**Rynek:** MIN -1,5 (DraftKings via Covers; Caesars -1, BetRivers TOR +0,5), total 231,5 (Covers); ML TOR -111 / MIN -109 (CappersPicks) vs inne źródło MIN -2,5. Bez marży ok. 50-54% MIN.
**H2H:** poprzedni sezon (bez Leonarda i Balla), waga ~0.
**Wejścia modelu:** MIN +2,8, TOR +1,7, HCA +2,5 → MIN -3,6; rynek -1,5 → **MIN 116,75 - TOR 114,75** (MIN -2; total 231,5), SD 13,5/19,5.

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| MIN ML | 54,4% | 1,84 | brak typu (wyrównany) |
| TOR ML | 45,6% | 2,19 | brak typu |
| MIN -1,5 (linia rynku) | 51,5% | 1,94 | brak typu |
| MIN +1,5 | 60,2% | 1,66 | niska |
| MIN +3,5 | 65,8% | 1,52 | niska |
| TOR +3,5 | 54,4% | 1,84 | niska |
| Total 231,5 Over / Under | 50 / 50% | 2,00 | brak typu |

**Ryzyka:** Leonard (load management, historia urazów) i nowe zgranie Ball-Edwards; mecz wyrównany.
**Typy z p>50% i fair>1.15:** **brak mocnego typu** (p 45-55%). Formalnie MIN +1,5 60,2% / 1,66 i TOR +3,5 54,4% / 1,84 (niska, alt-linie).

### 6. Philadelphia 76ers - Detroit Pistons (26.10, 00:30 CET; 19:30 ET) - **PHI na B2B**
**Dane:** PHI 3-0, 127-116 z MIL 24.10: Embiid triple-double 28/11/10, Brown 27, Maxey 26, Edgecombe 17 (ESPN, NBC Sports Philadelphia). **LeBron James nie grał 24.10** (dolna część pleców/rwa kulszowa - Inquirer); w raportach na 25.10 Q (CappersPicks) lub Out (Yahoo). **Embiid zapowiadał, że zagra tylko w jednym meczu weekendowego B2B** (Liberty Ballers/PhillyVoice) - zagrał w sobotę, więc najpewniej pauzuje w niedzielę (niepotwierdzone). Out: Hukporti (Achilles), Barlow (kręgosłup); Dean Wade Q (kostka). DET 2-0 (128-111 @MIA 23.10), 1 dzień przerwy. **Jalen Duren Out** (ścięgno udowe, Heavy), **Ausar Thompson Q** (kostka, HotTakes).
**Rynek (sprzeczny):** PHI -2,5, total 226,5, ML PHI -144 / DET +118 (CappersPicks; linia 24.10 w logu SportsEdge PHI -2,5) → bez marży PHI 56,3%; Polymarket PHI 56%. Outlier TheRx: PHI -7,5, ML -310/+255, total 221,5 - niespójny z Polymarket, odrzucam (być może przy założeniu gry Embiida). 79% publiki na PHI.
**H2H:** sezon 2025-26, PHI bez LeBrona/Browna, waga ~0.
**Wejścia modelu:** PHI +3,5, DET +3,15, HCA +2,5 → PHI -2,9; B2B -1,5; prawdopodobny brak Embiida -3 (pół korekty -1,5 przy niepewności, część w linii), Duren Out DET -1,5 (wliczony w PHI +1,5) → **PHI 112,75 - DET 111,25** (PHI -1,5; total 224), SD 14,5/20 (2+ kluczowe statusy niejasne). Różnica z rynkiem 3,6 pp (B2B + Embiid; < 5 pp).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| PHI ML | 52,7% | 1,90 | brak typu |
| DET ML | 47,3% | 2,12 | brak typu |
| PHI -2,5 (linia rynku) | 47,3% | 2,12 | brak typu |
| DET +2,5 | 52,7% | 1,90 | niska |
| DET +7,5 (gdyby linia TheRx) | 66,0% | 1,51 | niska (linia niepewna) |
| PHI +2,5 | 60,9% | 1,64 | niska |
| Total 224,5 Over / Under | 49 / 51% | 2,04 / 1,96 | brak typu |
| Under 226,5 | 55,0% | 1,82 | niska |
| Over 221,5 | 55,0% | 1,82 | niska |

**Ryzyka:** status Embiida i LeBrona decyduje o wszystkim: gra Embiid i LeBron → PHI ok. -5/-6 (p ~66%); obaj Out → DET ok. -1 (p DET ~53%). Totale zależą od tej samej informacji (bez Embiida niższe tempo PHI?). Do potwierdzenia ok. 90 min przed meczem.
**Typy z p>50% i fair>1.15:** **brak mocnego typu**. Formalnie DET +2,5 52,7% / 1,90 (niska, warunkowo: Embiid Out). Typ warunkowy nie może być wariantem głównym kuponu.

### 7. Sacramento Kings - Memphis Grizzlies (26.10, 02:00 CET; 21:00 ET)
**Dane:** MEM 2-0 (123-103 z UTA u siebie, 111-108 @GSW 23.10, krótki lot); **Cedric Coward DTD** (nadgarstek). SAC 0-2: **Ben Simmons Out (sezon, Achilles), Maxime Raynaud Out (kolano), Dylan Cardwell Out (łydka)** (iHeart/Fox Sports AM 1280); Malik Monk wrócił jako Probable 23.10 po kostce (NBC Sports, Yahoo), status na 25.10 nieznany. Oba odpoczęte 1 dzień.
**Rynek:** MEM -4,5, total 236,5, ML MEM -180 / SAC +150 (CappersPicks; Fox Sports AM 1280 ML -175) → bez marży MEM 61,6%. Dimers: MEM 62,9%. Projekcje: 120-112 (CappersPicks), 118-109 (iHeart).
**H2H:** poprzedni sezon, waga ~0.
**Wejścia modelu:** win totals dają tylko MEM -0,3 (MEM -4,6, SAC -7,4, HCA +2,5); rynek -4,5 wycenia słaby skład SAC (brak 3 wysokich) i start MEM. Kompromis bliżej rynku: **SAC 116,25 - MEM 119,75** (MEM -3,5; total 236), SD 13,5/19,5.

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| MEM ML | 61,6% | 1,62 | niska |
| SAC ML | 38,4% | 2,61 | niska |
| MEM -4,5 (linia rynku) | 47,0% | 2,13 | brak typu |
| SAC +4,5 | 53,0% | 1,89 | niska |
| SAC +6,5 | 58,8% | 1,70 | niska |
| MEM -2,5 | 53,0% | 1,89 | niska |
| Total 236,5 Over / Under | 49 / 51% | 2,04 / 1,96 | brak typu |
| Total MEM Over 115,5 | 64,4% | 1,55 | niska |
| Total SAC Over 112,5 | 62,8% | 1,59 | niska |

**Ryzyka:** rozjazd win totals vs rynek (MEM przed sezonem ok. 29 W, teraz faworyt na wyjeździe) - wysoka niepewność ratingów; SAC bez wysokich (zbiórki), mecz późno (02:00 CET).
**Typy z p>50% i fair>1.15:** MEM ML 61,6% / 1,62 (niska, = rynek); SAC +6,5 58,8% / 1,70 (niska, alt-linia).

---

## Podsumowanie: kandydaci (wejście do `bet-slip-builder`; kursy = portale typerskie, nie Betclic)

| Mecz | Rynek | p | Fair | Pewność | Od czego zależy | Kurs rynku znany? |
|---|---|---|---|---|---|---|
| LAC @ OKC | OKC ML | 85,9% | 1,16 | średnia | fair 1,15-1,20 (oznaczone), blowout bez wpływu | tak (ok. -800 do -1200) |
| ORL @ NYK | NYK ML | 72,3% | 1,38 | średnia | Banchero Out potwierdzony; Black Q | tak (-320/-333) |
| IND @ BKN | IND ML | 71,1% | 1,41 | niska/średnia | BKN B2B, absencje IND | tak (-278) |
| LAC @ OKC | OKC -8,5 | 68,5% | 1,46 | niska/średnia | Leonard, rezerwy w 4Q | alt-linia |
| LAL @ UTA | LAL ML | 67,2% | 1,49 | niska/średnia | LaRavia, wczesny tip | tak (-238) |
| ORL @ NYK | NYK -5,5 | 58,8% | 1,70 | niska/średnia | Black Q | alt-linia |
| MEM @ SAC | MEM ML | 61,6% | 1,62 | niska | rating MEM niepewny, Coward DTD | tak (-180) |
| IND @ BKN | IND -3,5 | 60,2% | 1,66 | niska | j.w. | alt-linia |
| LAL @ UTA | UTA +8,5 | 58,8% | 1,70 | niska | linia rynku -6,5 | alt-linia |
| MEM @ SAC | SAC +6,5 | 58,8% | 1,70 | niska | j.w. | alt-linia |
| TOR @ MIN | brak typu (pick'em) | - | - | - | Leonard | - |
| DET @ PHI | brak typu (Embiid/LeBron) | - | - | - | statusy po raporcie | - |

Typy z fair ≤ 1,15: brak (OKC ML 1,16 na granicy). Totale: brak typu (model zakotwiczony w linii rynku, brak konkretnej informacji na Under/Over). Rynki zawodnika: brak (jedno źródło średnich, sprzeczne linie). Przed kuponem: kursy Betclic i injury report ok. 90 min przed tip-offem (szczególnie Embiid/LeBron, Black, Leonard, Holmgren/J. Williams, Monk).

**Źródła (WebSearch, 25.10):** ESPN (game pages 401909861, 401909865; injuries; recap PHI-MIL), CappersPicks (AI picks 10/25/26: LAL@UTA, IND@BKN, LAC@OKC, ORL@NYK, TOR@MIN, DET@PHI, MEM@SAC), Pick Dawgz (LAL-UTA, IND-BKN), Covers (TOR-MIN odds 388602), Dimers (predictions, best bets 10/25), Polymarket (LAC-OKC; PHI 56¢ via SportsEdge GitHub log), BettingNews, VegasInsider, TheRx (DET-PHI, outlier), iHeart/Fox Sports (injury reports i predictions: LAC-OKC, ORL-NYK, TOR-MIN, MEM-SAC), Sportsmole, Lakers Daily, NBC Sports (Nesmith; Monk), Picks and Parlays, Yahoo/Field Level Media (CLE 125-121 BKN), NBC Sports Philadelphia, Inquirer, Liberty Ballers, Heavy (Duren), HotTakes (A. Thompson, A. Black), ESPN/CBS/Yahoo (Banchero), Deadspin, Fox Sports (Leonard), Yardbarker/JOX (SGA), NBA TV PR, SportsBettingDime/BetMGM/Betfanatics/Complex (win totals), pliki `analizy/Weryfikacja_Kupony_i_analiza_dnia_2026-10-2[0-3].md` (wyniki 20-23.10).

To oszacowania probabilistyczne przy ograniczonych danych (wczesny sezon, linie z portali, statusy niepotwierdzone), nie gwarancje.
