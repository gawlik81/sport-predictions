# Analiza NBA - noc 12/13.11.2026 (4 mecze)

Metoda: skill `nba-analyst` (model rozkładu normalnego `nba_model.py`, rynki zawodnika `nba_props.py`).
Źródła: ESPN (scoreboard, game summary: bilans, injury report, ostatnie 5 meczów, linie DraftKings), Superbet (`superbet-mcp`, kursy z dogrywką), własne p z modelu. Injury report sprawdzony 12.11.2026 ok. 16:30 (czas PL); statusy mogą się zmienić do tip-offu.
Nie pozyskano: BettingPros (brak klucza, pominięte), Pinnacle/stats.nba.com (timeouty), net rating/pace (brak danych z dostępnych źródeł - korekty oparte na linii rynkowej, bilansie i absencjach, więc pewność jest obniżona). Back-to-back: nie zweryfikowane (źródło nie daje daty ostatniego meczu w użytecznej formie).
Sezon dopiero się rozkręca (10-12 meczów na drużynę): próbka mała, SD podniesione tam, gdzie statusy gwiazd niejasne.

## Tabela zbiorcza: mecz | rynek | linia | p | fair | pewność

Kurs Superbet podany tylko tam, gdzie go pobrano (z dogrywką). EV = p x kurs - 1.

| Mecz | Rynek | Linia | p | fair | Superbet (EV) | pewność |
|---|---|---|---|---|---|---|
| TOR @ PHI | Zwycięzca PHI | ML | 71.8% | 1.39 | 1.28 (-8%) | średnia |
| TOR @ PHI | Zwycięzca TOR | ML | 28.2% | 3.55 | 3.50 (-1%) | średnia |
| TOR @ PHI | Spread PHI | -8.5 | 48.5% | 2.06 | 1.87 (-9%) | średnia |
| TOR @ PHI | Spread TOR | +8.5 | 51.5% | 1.94 | 1.92 (-1%) | średnia |
| TOR @ PHI | Spread TOR | +10.5 | 57.6% | 1.74 | 1.68 (-3%) | średnia |
| TOR @ PHI | Spread PHI | -6.5 | 54.6% | 1.83 | 1.62 (-12%) | średnia |
| TOR @ PHI | Total Under | 222.5 | 52.2% | 1.92 | 1.87 (-2%) | niska-średnia |
| TOR @ PHI | Total Over | 222.5 | 47.8% | 2.09 | 1.92 (-8%) | niska-średnia |
| TOR @ PHI | Total Under | 224.5 | 56.6% | 1.77 | 1.74 (-1%) | niska-średnia |
| TOR @ PHI | Total drużyny PHI / TOR (linia szac. 115.5 / 107.5) | O/U | ~47% O / ~53% U | ~1.90 U | brak kursu | niska |
| TOR @ PHI | Maxey punkty Over | 24.5 (śr. 26.0) | 54.7% | 1.83 | 1.97 (25+) (+8%) | niska (Embiid/LeBron DTD, blowout) |
| TOR @ PHI | Maxey punkty Over | 29.5 | 30.3% | 3.30 | brak | niska |
| TOR @ PHI | Embiid punkty 20+ | - | brak p (status DTD) | - | 1.80 | bez typu |
| DET @ WSH | Zwycięzca DET | ML | 80.9% | 1.24 | 1.20 (-3%) | średnia |
| DET @ WSH | Zwycięzca WSH | ML | 19.1% | 5.24 | 4.25 (-19%) | średnia |
| DET @ WSH | Spread DET | -10.5 | 48.3% | 2.07 | ok. 1.93 (-7%) (DK) | średnia |
| DET @ WSH | Spread WSH | +10.5 | 51.7% | 1.94 | ok. 1.93 (0%) (DK) | średnia |
| DET @ WSH | Spread DET | -8.5 | 55.0% | 1.82 | brak | średnia |
| DET @ WSH | Spread WSH | +12.5 | 58.3% | 1.72 | brak | średnia |
| DET @ WSH | Total | 220.5 | 50.0 / 50.0% | 2.00 | brak | niska ("brak mocnego typu") |
| DET @ WSH | Total drużyny DET / WSH (szac. 115.5 / 105) | O/U | ~49% / ~51% | ~2.0 | brak kursu | niska |
| DET @ WSH | Cunningham punkty Under | 24.5 (śr. 22.5, blowout) | 63.9% | 1.57 | brak | niska |
| DET @ WSH | Cunningham asysty Over | 6.5 (śr. 7.2) | 56.1% | 1.78 | brak | niska |
| DET @ WSH | A. Davis punkty Over | 24.5 (śr. 25.0) | 49.5% | 2.02 | brak | niska |
| DET @ WSH | A. Davis zbiórki Over | 9.5 (śr. 10.0) | 52.1% | 1.92 | brak | niska |
| DAL @ MIN | Zwycięzca MIN | ML | 64.1% | 1.56 | 1.45 (-7%) | średnia |
| DAL @ MIN | Zwycięzca DAL | ML | 35.9% | 2.78 | 2.70 (-3%) | średnia |
| DAL @ MIN | Spread MIN | -5.5 | 48.4% | 2.07 | ok. 1.88 (DK -114) (-9%) | średnia |
| DAL @ MIN | Spread DAL | +5.5 | 51.6% | 1.94 | ok. 1.95 (DK) (+1%) | średnia |
| DAL @ MIN | Spread DAL | +7.5 | 57.9% | 1.73 | brak | średnia |
| DAL @ MIN | Total Under | 225.5 | 51.1% | 1.96 | brak (DK 225.5; Superbet kombinacje używają 230.5, nie zweryfikowano) | niska |
| DAL @ MIN | Total Over | 225.5 | 48.9% | 2.05 | j.w. | niska |
| DAL @ MIN | Total drużyny MIN / DAL (szac. 115.75 / 109.75) | O/U | ~49% / ~52% O DAL | ~1.95 | brak kursu | niska |
| DAL @ MIN | Flagg punkty Over | 24.5 (śr. 25.5) | 52.1% | 1.92 | brak | niska |
| DAL @ MIN | Flagg asysty Over | 6.5 (śr. 6.9) | 52.0% | 1.92 | brak | niska |
| DAL @ MIN | Gobert zbiórki Over | 10.5 (linia szac., śr. 11.8) | 60.0% | 1.67 | brak linii | niska |
| CHA @ PHX | Zwycięzca PHX | ML | 68.4% | 1.46 | 1.39 (-5%) | średnia |
| CHA @ PHX | Zwycięzca CHA | ML | 31.6% | 3.17 | 2.92 (-8%) | średnia |
| CHA @ PHX | Spread PHX | -6.5 | 50.0% | 2.00 | 1.90 (-5%) | średnia |
| CHA @ PHX | Spread CHA | +6.5 | 50.0% | 2.00 | 1.88 (-6%) | średnia |
| CHA @ PHX | Spread CHA | +8.5 | 56.4% | 1.77 | 1.63 (-8%) | średnia |
| CHA @ PHX | Total Under | 214.5 | 53.3% | 1.88 | 1.88 (0%) | niska-średnia |
| CHA @ PHX | Total Under | 216.5 | 57.7% | 1.73 | 1.74 (+0.4%) | niska-średnia |
| CHA @ PHX | Total Over | 214.5 | 46.7% | 2.14 | 1.90 (-11%) | niska-średnia |
| CHA @ PHX | Total drużyny PHX / CHA (szac. 110.5 / 104) | O/U | ~47% O / ~53% U CHA | ~1.90 | brak kursu | niska |
| CHA @ PHX | Booker punkty Over | 24.5 (śr. 25.0) | 49.5% | 2.02 | 1.82 (25+) (-10%) | niska |
| CHA @ PHX | Naz Reid punkty Over | 19.5 (śr. 19.5 po absencjach) | 46.4% | 2.15 | 1.57 (20+) (-27%) | niska |

Wniosek ogólny: rynek NBA jest tu efektywny, a model (oparty na linii rynkowej i absencjach) nie znajduje przewagi powyżej ~1-3 pp. Z kursów Superbet dodatnie EV mają tylko: Maxey 25+ (+8%, ale pewność niska i zależny od statusów Embiida/LeBrona oraz blowoutu) oraz Under 216.5 w CHA @ PHX (+0.4%, praktycznie zero). Żaden mecz nie daje mocnego typu; do kuponów to kandydaci co najwyżej warunkowi.

---

### Philadelphia 76ers - Toronto Raptors (13.11, 01:00 PL; 12.11 19:00 ET)
**Typ:** brak mocnego typu; najbliższy wartości: Toronto +10.5 | **p:** 57.6% | **fair:** 1.74 | **Pewność:** średnia (EV vs Superbet 1.68 = -3%)
**Statystyki drużyn:** PHI 9-3 (dom 4-2, wyjazd 5-1), ostatnie 5: W 126-107 CHI, W 112-106 DET, L 95-119 CLE, W 127-121 CHI, L 101-123 BOS (mieszana forma, 2 przegrane z 5). TOR 5-6 (wyjazd 3-3), ostatnie 5: W 125-118 LAC, L 109-128 DEN, W 121-107 MIL, L 102-118 MEM, L 93-98 BOS. Liderzy: Maxey 26.7 pkt, Embiid 9.3 zb., Barrett 20.5, Shead 6.9 ast. Net rating/pace: brak danych z dostępnych źródeł.
**H2H:** pierwsze spotkanie sezonu (kolejne 10.01, 15.03, 06.04.2027); waga niska.
**Informacje medialne (ESPN, 12.11 ok. 16:30):** PHI: Embiid Day-To-Day (stopa), LeBron James Day-To-Day (plecy), Bona Out (plecy), Barlow Out (złamanie pleców), Hukporti Out (Achilles). TOR: Kawhi Leonard Out (kolano), Scottie Barnes Out (pachwina), Bittle Out, Jackson-Davis DTD (choroba). Linia otwarcia ML PHI -410 przesunęła się do -344 (rynek lekko cofnął się z powodu niepewności DTD).
**Oczekiwane punkty:** PHI 114.75 - TOR 106.75 (spread -8.0, total 221.5). Korekta: absencja Kawhiego i Barnesa po stronie TOR już w linii (-8.5); DTD Embiida/LeBrona obniżają mnie o ok. 0.5 pkt i podnoszą SD różnicy do 13.
**Rynek:** DK: PHI -8.5, total 222.5, ML -344/+276 (no-vig ok. 73.5%/26.5%). Superbet: PHI 1.28 / TOR 3.50, handicap -8.5 1.87/1.92, total 222.5 1.87 (U) / 1.92 (O). Moje p zgodne z rynkiem w granicach 2 pp.
**Ryzyka:** gdy Embiid i LeBron zagrają i obaj w pełnej rotacji, PHI pokryje -8.5 częściej (blowout, ale wtedy gwiazdy tracą minuty: Over punktów zawodnika zagrożony); gdy obaj wypadną, spread powinien zmaleć o 4-6 pkt (Under/TOR+ zyskuje). Rynki zawodnika PHI nie dostają typu głównego do czasu potwierdzenia składu (Maxey Over 24.5 tylko warunkowo).

### Detroit Pistons @ Washington Wizards (13.11, 01:00 PL; 12.11 19:00 ET)
**Typ:** Detroit wygra | **p:** 80.9% | **fair:** 1.24 | **Pewność:** średnia (Superbet 1.20, EV -3%: brak value; fair > 1.15)
**Statystyki drużyn:** DET 7-3 (wyjazd 4-1), ostatnie 5: W 110-94 BKN, W 124-91 CHA, W 112-106 PHI, W 121-116 LAL, W 122-111 WSH. WSH 4-8 (dom 2-2, wyjazd 2-6), ostatnie 5 same porażki: 105-120 ATL, 132-139 ATL, 75-114 OKC, 111-122 DET, 101-114 IND (słaba obrona, ok. 120+ puszczanych). Liderzy: Cunningham 22.3 pkt / 7.6 ast, A. Thompson 8.4 zb., A. Davis 25.2 pkt / 10.0 zb., Young 8.3 ast.
**H2H:** DET 1-0 w sezonie (10.11: DET 122-111 w tej samej hali; kolejne spotkania 13.11 i 11.04.2027). Dwa mecze w 3 dni: Wizards znają rywala, ale to nie zmienia różnicy klas.
**Informacje medialne:** DET: Jalen Duren Out (hamstring), Isaiah Joe Out (biodro), Onyenso DTD. WSH: Vukcevic Out, Beekman Out, Champagnie Out, Watkins Out (kolano; to rotacja, nie gwiazdy). Cunningham, Young, Davis w pełnej dyspozycji wg listy ESPN. Duren out (podkosz DET) już wliczone w linię -10.5.
**Oczekiwane punkty:** WSH 105.25 - DET 115.25 (spread DET -10.0, total 220.5). Duren out: -1 do -2 pkt w różnicy względem składu pełnego; pozostawiam linię rynku, bo WSH ma jeszcze więcej braków.
**Rynek:** DK: DET -10.5, total 220.5, ML DET -467 / WSH +360 (no-vig ok. 79%/21%), WSH +10.5 -108. Superbet: DET 1.20 / WSH 4.25. Moje p ML 80.9% vs rynek ok. 79%: zgodnie.
**Ryzyka:** blowout (DET +10.5/+12.5) obniża minuty Cunninghama i Thompsona (Under punktów Cunninghama 63.9% przy śr. 22.5 skorygowanej o blowout; niska pewność); gdy Cunningham pauzuje (ostatnio mecze z plecami), spread kurczy się o 4-6 pkt. WSH przy dużym wyniku po drugiej stronie Over zawodników WSH nieco ryzykowny przy garbage time, ale Davis (25.2) ma sufit.

### Dallas Mavericks @ Minnesota Timberwolves (13.11, 02:00 PL; 12.11 20:00 ET)
**Typ:** brak mocnego typu; Dallas +5.5 | **p:** 51.6% | **fair:** 1.94 | **Pewność:** niska-średnia
**Statystyki drużyn:** MIN 8-3 (dom 4-1), ostatnie 5: L 111-121 SA, W 112-100 MIL, W 117-107 HOU, W 115-109 NO, W 115-100 UTA (ok. 114 pkt, stabilna obrona). DAL 7-4 (wyjazd 2-2), ostatnie 5: L 100-115 SAC, L 111-112 SA, W 112-100 UTA, W 130-93 BKN, W 125-122 IND. Liderzy: Flagg 25.9 pkt / 6.9 ast, Washington 7.5 zb.; Ball 18.3 pkt / 6.0 ast, Gobert 12.1 zb., Dosunmu 18.1 pkt.
**H2H:** pierwsze spotkanie sezonu (kolejne 25.03 i 04.04.2027).
**Informacje medialne:** MIN: Anthony Edwards Out (operacja kolana), DiVincenzo Out (Achilles). DAL: Lively II Out (stopa), Biberovic Out, de Larrea Out, Morez Johnson Jr. DTD. Brak Edwardsa (top-1 MIN) to -3 do -7 pkt w różnicy meczu i został już wliczony w linię -5.5 (MIN 8-3 mimo to).
**Oczekiwane punkty:** MIN 115.0 - DAL 110.0 (spread MIN -5.0, total 225.0; SD różnicy 12.5). Linia rynku MIN -5.5.
**Rynek:** DK: MIN -5.5 (-114), total 225.5, ML -223/+185 (no-vig 66%/34%). Superbet: MIN 1.45 / DAL 2.70. UWAGA: kombinacje Superbet używają totalu 230.5 (DK 225.5); nie udało się pobrać głównej linii totalu Superbet, więc nie wyceniam EV totalu Superbet. Moje p MIN 64.1% vs rynek ok. 66%: różnica 2 pp.
**Ryzyka:** Flagg (stan ok; brak na liście kontuzji) - zwiększone użycie piłki bez Lively'ego; zbiórki DAL cienkie przy braku Lively'ego (Gobert Over zbiórek zyskuje, ale linia szacowana, bez kursu). Irving występuje w rynkach Superbet - jego status nie jest w injury report ESPN, ale to wymaga potwierdzenia przed typami z jego udziałem. Mała próba (11 meczów).

### Charlotte Hornets @ Phoenix Suns (13.11, 03:00 PL; 12.11 21:00 ET)
**Typ:** brak mocnego typu; najbliższy wartości: Under 216.5 | **p:** 57.7% | **fair:** 1.73 | **Pewność:** niska-średnia (Superbet 1.74, EV +0.4%)
**Statystyki drużyn:** PHX 4-6 (dom 4-3, wyjazd 0-3), ostatnie 5: L 119-132 POR, W 117-104 ORL, W 102-99 HOU, L 96-122 SA, W 133-110 LAC. CHA 4-7 (wyjazd 1-3), ostatnie 5: L 104-109 PHI, L 91-124 DET, W 114-104 BKN, L 80-119 BOS, W 124-112 CLE. Liderzy: Booker 25.1 pkt, Bridges 7.4 zb.; Reid 17.4 pkt / 8.5 zb., Diabate 9.1 zb., Allen 3.0 ast.
**H2H:** pierwsze spotkanie sezonu (kolejne 13.03.2027).
**Informacje medialne:** CHA: Brandon Miller Out (pachwina), Kon Knueppel Out (hamstring), Dennis Schroder Out (hamstring), Grant Williams Out, Moussa Diabate DTD (czworogłowy). PHX: Mark Williams Out (operacja barku). Hornets bez trzech czołowych graczy (Miller, Knueppel, Schroder), to największa absencja tej nocy; rynek ją już wlicza (PHX -6.5 mimo bilansu 4-6).
**Oczekiwane punkty:** PHX 109.75 - CHA 103.25 (spread PHX -6.5, total 213.0). Korekta total -1.5 względem rynku 214.5 (osłabiony atak CHA; maksymalnie to przesunięcie, nie przewaga, wg reguły SKILL).
**Rynek:** DK: PHX -6.5, total 214.5, ML -244/+201 (no-vig ok. 68%/32%). Superbet: PHX 1.39 / CHA 2.92; handicap -6.5 1.90/1.88; Under 214.5 1.88. Moje p PHX 68.4% = rynek.
**Ryzyka:** wyjazdowy bilans PHX 0-3 (to domowy mecz, 4-3); Diabate status DTD zmienia zbiórki CHA; Naz Reid przy 3 brakujących strzelcach ma wyższe użycie (mean 19.5, ale Superbet 20+ @1.57 = EV -27%, nie typ); blowout PHX obniża minuty Bookera (Over 24.5 przy śr. 25.0 to 49.5%).

---

## Ranking kandydatów (wszystkie rynki, bez fair <= 1.15; fair 1.15-1.20 oznaczone)

| # | Mecz | Typ | p | fair | pewność | od czego zależy | kurs znany |
|---|---|---|---|---|---|---|---|
| 1 | DET @ WSH | DET wygra (ML) | 80.9% | 1.24 | średnia | Cunningham zdrowy | Superbet 1.20 (EV -3%) |
| 2 | DET @ WSH | WSH +12.5 | 58.3% | 1.72 | średnia | Cunningham/Thompson minuty | brak |
| 3 | TOR @ PHI | TOR +10.5 | 57.6% | 1.74 | średnia | status Embiid/LeBron | Superbet 1.68 (EV -3%) |
| 4 | CHA @ PHX | Under 216.5 | 57.7% | 1.73 | niska-średnia | Diabate, tempo bez Millera/Knueppela | Superbet 1.74 (EV +0.4%) |
| 5 | TOR @ PHI | Under 224.5 | 56.6% | 1.77 | niska-średnia | Embiid/LeBron DTD | Superbet 1.74 (EV -1%) |
| 6 | DET @ WSH | Cunningham asysty Over 6.5 | 56.1% | 1.78 | niska | minuty (blowout) | brak |
| 7 | TOR @ PHI | Maxey punkty Over 24.5 | 54.7% | 1.83 | niska | status Embiid/LeBron, blowout | Superbet 25+ @1.97 (EV +8%) |
| 8 | DAL @ MIN | MIN wygra (ML) | 64.1% | 1.56 | średnia | Edwards Out (już w linii) | Superbet 1.45 (EV -7%) |
| 9 | CHA @ PHX | PHX wygra (ML) | 68.4% | 1.46 | średnia | - | Superbet 1.39 (EV -5%) |
| 10 | DAL @ MIN | Gobert zbiórki Over 10.5 | 60.0% | 1.67 | niska (linia szac.) | dostępna linia rynkowa | brak |

## Tabela kandydatów na kupon dla bet-slip-buildera

Tylko typy z kursem znanym i EV >= 0 lub marginalnie ujemnym; żaden nie spełnia progu p > 50% + EV > 0 + kurs > 1.2 jednocześnie z wysoką pewnością.

| Mecz | Rynek | p | fair | pewność | warunek | kurs |
|---|---|---|---|---|---|---|
| CHA @ PHX | Under 216.5 | 57.7% | 1.73 | niska-średnia | Diabate/Booker w składzie | Superbet 1.74 |
| TOR @ PHI | Maxey Over 24.5 (25+) | 54.7% | 1.83 | niska | potwierdzony skład PHI, Embiid/LeBron | Superbet 1.97 |
| TOR @ PHI | TOR +8.5 | 51.5% | 1.94 | średnia | - | Superbet 1.92 (EV -1%) |
| DAL @ MIN | DAL +5.5 | 51.6% | 1.94 | średnia | - | DK ok. 1.95, Superbet nieznany |

Wszystkie powyższe to szacunki probabilistyczne, nie gwarancje; status zawodników (Embiid, LeBron, Diabate, Irving) sprawdzić ponownie ok. 90 min przed meczem.
