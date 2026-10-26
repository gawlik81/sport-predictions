# Analiza dnia 25.10.2026, piłka nożna: Top 5 lig + Ekstraklasa (czas polski CET)

**Zakres:** 21 meczów od 12:15 do 17:30. Cztery mecze wieczorne (Lecce – Juventus, Real Sociedad – Levante, Udinese – Milan, Barcelona – Real) są w `analizy/Analiza_dnia_2026-10-25_wieczor.md`.
**Źródła:** ESPN API (tabele, H2H, boxscore'y: strzały, rożne, faule, kartki; kursy DraftKings), WebSearch (newsy, składy, sędziowie), BettingPros API (kursy). Serwer `sportsdata` się nie połączył. Betclic.pl i gg397.bet odrzucają połączenia z tego serwera (CloudFront 403). Brak xG we wszystkich meczach. Ekstraklasy nie ma w ESPN ani BettingPros, więc analizy bez kursów (decyzja użytkownika).
**Stan na:** 25.10, ok. 08:30-09:30. Składy do potwierdzenia ok. 1 h przed meczem.

## Terminarz (niedziela 25.10, CET)
- 12:15 Śląsk Wrocław – Wieczysta Kraków (Ekstraklasa)
- 12:30 Inter – Fiorentina (Serie A)
- 14:00 Athletic Club – Getafe (La Liga)
- 14:45 Jagiellonia – Wisła Płock (Ekstraklasa)
- 15:00 Atalanta – Frosinone, Genoa – Venezia (Serie A); Liverpool – Brighton, Manchester United – Bournemouth, Crystal Palace – Newcastle, Hull – Brentford (Premier League); Monaco – Lille (Ligue 1)
- 15:30 Hoffenheim – Leverkusen (Bundesliga)
- 16:15 Celta – Betis (La Liga)
- 17:15 Marseille – Le Havre, Rennes – Strasbourg, Auxerre – Le Mans, Angers – Lorient, Toulouse – Troyes (Ligue 1)
- 17:30 Sunderland – Leeds (Premier League), Freiburg – Bayern (Bundesliga), Legia – Lech (Ekstraklasa)

Źródła terminarza: ESPN scoreboard (eng.1, esp.1, ita.1, ger.1, fra.1), [ekstraklasa.org](https://ekstraklasa.org/terminarz), [sport1.pl](https://sport1.pl/terminarz/ekstraklasa), BettingPros events.

## Analiza meczów piłkarskich – niedziela 25.10.2026 (część A, czas CET)

Metoda: skill `football-analyst` (4 filary → λ → `poisson.py`, rynki dodatkowe `markets.py`, krok "Skalibruj"). Źródła: ESPN API (summary: lastFiveGames, standings, seasonseries, pickcenter DraftKings; boxscore 5 ostatnich meczów każdej drużyny – rożne, faule, kartki, strzały), WebSearch (zapowiedzi, składy, sędziowie). MCP `sportsdata` nie działa; strony bukmacherów/zapowiedzi niedostępne przez WebFetch/curl (DNS/403) – korzystano ze streszczeń wyników wyszukiwania. Betclic niedostępny; kursy DraftKings (ESPN) i polskich bukmacherów (z zapowiedzi) tylko jako kontrola rynku.

---

### 12:15 Śląsk Wrocław – Wieczysta Kraków (Ekstraklasa, 12. kolejka, Tarczyński Arena)

**Kluczowe dane**
- Tabela: Śląsk 17. miejsce, 6 pkt w 11 meczach, bramki 14–22 (śr. 1,27 / 2,00) – tabela klubowa via WebSearch (slasknet/sportowefakty; inny wyliczony bilans 12–19 w 10 meczach – rozbieżność). Seria 4–5 porażek z rzędu (ostatnio m.in. 1–4 z Lechem u siebie 10.10, porażki z Jagiellonią, Koroną, Wisłą) – sportowefakty, zapowiedzi bukmacherskie. 1 wygrana w sezonie.
- Wieczysta (beniaminek): 8 pkt w 11 meczach, bramki 16–21 (śr. 1,45 / 1,91), 15.–16. miejsce; 16.10 przegrana 1–2 z Rakowem (TVP Sport, Interia); wcześniej 4–3 z Puszczą, 2–2 z Widzewem.
- Obie drużyny tracą ok. 2 gole/mecz → profil meczu otwartego.
- H2H (I liga 2025/26): 1–1 we Wrocławiu (karny w doliczonym czasie dla Wieczystej), 3–3 w Krakowie (30.11.2025) – soccerway/FotMob via WebSearch. Waga średnia (inne ligi, częściowo inne składy).
- Sędzia: Mateusz Piszczelok (Katowice), VAR Wojciech Myć (gol24, sportowefakty). Średnia kartek sędziego – brak danych → liczona średnia ligowa.
- Statystyki rożnych/kartek/fauli drużyn: **brak danych** (ESPN nie obsługuje Ekstraklasy, strony statystyczne zablokowane) – rynki dodatkowe ze średnich ligowych, niska pewność.

**Newsy**
- Śląsk: zawieszony Marc Llinares; poza grą Michał Mokrzycki (więzadło krzyżowe, do końca sezonu), Irodotos Christodoulou, Jorge Yriarte; Damian Warchoł niepewny; nowy nabytek kontuzjowany (transfery.info – nagłówek) – FotMob, gol24.
- Wieczysta: Stefan Feiertag (kolano, do końca grudnia) – FotMob.
- Kontekst: "mecz o posadę" obu trenerów – Ante Šimundža (Śląsk) i Željko Kopić (Wieczysta) (slasknet, Dziennik Polski). Mecz bezpośredni o utrzymanie.

**Rynek (polscy bukmacherzy z zapowiedzi, WebSearch):** 1 ≈ 2,67–3,00, X ≈ 3,31–3,79, 2 ≈ 2,10–2,22; BTTS tak ≈ 1,44–1,49; Over 2.5 ≈ 1,55. Po usunięciu marży (1 2,80 / X 3,55 / 2 2,15): 1 32%, X 26%, 2 42%. Kursów DraftKings brak.

**λ:** Śląsk 1,40, Wieczysta 1,60 (bazowo ok. 1,6/1,55 ze średnich ataku i obrony z regresją do średniej ligi; korekta Śląska w dół za kryzys underdoga – seria porażek, presja na trenera, zawieszenie Llinaresa i 3–4 absencje).

| Rynek | p | fair | pewność |
|---|---|---|---|
| 1 Śląsk | 33,5% | 2,98 | średnia |
| X | 24,2% | 4,14 | średnia |
| 2 Wieczysta | 42,3% | 2,36 | średnia |
| 1X | 57,7% | 1,73 | niska–średnia |
| X2 | 66,5% | 1,50 | średnia |
| 12 | 75,8% | 1,32 | średnia |
| Over 1.5 | 80,1% | 1,25 | średnia |
| Over 2.5 | 57,7% | 1,73 | średnia |
| Under 2.5 | 42,3% | 2,36 | średnia |
| Over 3.5 | 35,3% | 2,83 | niska |
| Under 3.5 | 64,7% | 1,55 | średnia |
| BTTS tak | 60,1% | 1,66 | średnia |
| BTTS nie | 39,9% | 2,51 | średnia |
| Śląsk strzeli ≥1 | 75,3% | 1,33 | średnia |
| Śląsk ≥2 gole | 40,8% | 2,45 | niska |
| Wieczysta strzeli ≥1 | 79,8% | 1,25 | średnia |
| Wieczysta ≥2 gole | 47,5% | 2,11 | niska |
| Rożne Over 8.5 (śr. 9,6 – średnia ligowa, brak danych drużyn) | 59,9% | 1,67 | niska |
| Rożne Over/Under 9.5 | 48,2% / 51,8% | 2,07 / 1,93 | niska |
| Kartki Over 3.5 (śr. 4,6 – ligowa + stawka meczu o utrzymanie; sędzia bez danych) | 63,5% | 1,57 | niska |
| Kartki Over/Under 4.5 | 47,0% / 53,0% | 2,13 / 1,89 | niska |
| Faule/strzały | brak danych | – | – |

**Ryzyka:** (a) wygrana Śląska – efekt "nowego impulsu"/mecz o posadę u siebie, Wieczysta też w słabej formie i traci 1,9 gola/mecz; (b) remis 24% – mecz dwóch drużyn walczących o utrzymanie może być zachowawczy; (c) dla Over/BTTS – nerwowy mecz o "6 punktów" z mało stworzonymi sytuacjami. Dane bramkowe Śląska rozbieżne między źródłami; brak xG.

**Typy z p>50% i fair>1.15:** X2 66,5% (1,50), Over 1.5 80,1% (1,25), Under 3.5 64,7% (1,55), BTTS tak 60,1% (1,66), Over 2.5 57,7% (1,73), 12 75,8% (1,32), Wieczysta ≥1 79,8% (1,25), Śląsk ≥1 75,3% (1,33), 1X 57,7% (1,73, niska). Rożne O8.5 i kartki O3.5 – niska pewność (średnie ligowe), nie rekomendować na kupon. Najlepszy rynek meczu: BTTS tak / Over 1.5 (rynek BTTS ≈1,46 implikuje ok. 65% – mój model 60% jest poniżej rynku, więc BTTS bez value po kursie rynkowym). Wynik 1X2: brak mocnego typu.

---

### 12:30 Inter – Fiorentina (Serie A, 8. kolejka, San Siro)

**Kluczowe dane (ESPN 401875036)**
- Tabela: Inter 2. miejsce, 19 pkt w 7 meczach (6-1-0), bramki 21–9 (3,0 / 1,29 na mecz). Fiorentina 18. miejsce, 4 pkt (1-1-5), bramki 8–17 (1,14 / 2,43).
- Forma Inter: 3–0 Parma (d), 3:4 Club Brugge (d, LM), 3–1 w Bologni, 1–0 Szachtar (d, LM, 21.10, czerwona kartka Bastoniego). Fiorentina: 1–1 Napoli (d), 1:2 w Genui, 1:3 Como (d), 3–0 Pisa (Coppa).
- Boxscore 4 ost. meczów o stawkę (ESPN): Inter rożne 4,75 zdobyte / 2,75 oddane, strzały 19,8 (celne 7,8), faule 9,8, żółte 1,75. Fiorentina rożne 5,5 / 3,25 (zawyżone przez 11 rożnych z Como), strzały 15,5, faule 12,5, żółte 2,5.
- H2H (ESPN): 1–1 (03.2026, Florencja), 3–0 (10.2025, Mediolan), 2–1 (02.2025, Mediolan), 0–3 (02.2025, Florencja), 1–0 dla Interu (01.2024). U siebie Inter wygrał ostatnie 2.
- Sędzia: Maurizio Mariani (Aprilia), VAR Fabbri – ok. 3,5–4 kartek/mecz (Viola News, Mondopengwin).

**Newsy (Tuttosport, QS, Firenze Post, Sportitalia; 23–25.10)**
- Inter (Chivu), przewidywany 3-5-2: Provedel; Bisseck, Akanji, Bastoni; Diouf, Barella, Calhanoglu, Zieliński, Carlos Augusto; Pio Esposito, Thuram. Bastoni dostępny (zawieszenie tylko w UEFA). Kontuzja Luis Henrique. Część źródeł pisze o rotacji po środowym meczu LM – umiarkowana. Inter goni prowadzące Lazio (22 pkt).
- Fiorentina (Vanoli): bez Parisiego (więzadło krzyżowe), Arthura Atty; Ranieri wątpliwy; De Gea w bramce, Pongračić–Dragusin; Vanoli znów zmienia ustawienie (4-3-3/4-2-3-1). Drużyna w kryzysie (3 porażki ligowe z rzędu, strefa spadkowa).

**Rynek DraftKings (ESPN pickcenter):** 1 1,34 / X 5,25 / 2 7,00 → bez marży 1 69,2%, X 17,6%, 2 13,2%; total 3.5: Over 2,00 / Under 1,77 → Over 3.5 ≈ 47%. Rynek widzi ok. 3,3–3,4 gola.

**λ:** Inter 2,30, Fiorentina 1,00. Inter strzela 3,0/mecz, Fiorentina traci 2,43 – surowy model daje dużo więcej, regresja do średniej. Krok "Skalibruj": underdog w kryzysie (zmiany ustawienia, desperacja) → faworyt nie wyżej niż rynek; zejście pod rynek o 2,7 pp (dopuszczalne <5 pp) za lekką rotację po LM i kontuzję Luisa Henrique. Fiorentina strzelała w każdym z 4 ost. meczów o stawkę → λ gości 1,0.

| Rynek | p | fair | pewność |
|---|---|---|---|
| 1 Inter | 66,5% | 1,50 | średnia–wysoka |
| X | 18,5% | 5,41 | średnia |
| 2 Fiorentina | 15,0% | 6,67 | średnia |
| 1X | 85,0% | 1,18 (graniczny 1,15–1,20) | wysoka |
| X2 | 33,5% | 2,98 | średnia |
| 12 | 81,5% | 1,23 | średnia |
| Over 1.5 | 84,1% | 1,19 (graniczny) | wysoka |
| Over 2.5 | 64,1% | 1,56 | średnia |
| Under 2.5 | 35,9% | 2,78 | średnia |
| Over 3.5 | 42,0% | 2,38 | średnia (rynek 47%) |
| Under 3.5 | 58,0% | 1,72 | średnia |
| BTTS tak | 56,9% | 1,76 | średnia |
| BTTS nie | 43,1% | 2,32 | średnia |
| Inter ≥1 gol | 90,0% | 1,11 (≤1,15 – pominąć) | wysoka |
| Inter ≥2 gole | 66,9% | 1,49 | średnia |
| Inter ≥3 gole | 40,4% | 2,48 | niska–średnia |
| Fiorentina ≥1 gol | 63,2% | 1,58 | średnia |
| Fiorentina ≥2 gole | 26,4% | 3,79 | niska |
| Rożne Over 8.5 (śr. 9,3: Inter ok. 5,8, Fio ok. 3,5) | 56,5% | 1,77 | niska–średnia |
| Rożne Under 9.5 | 55,3% | 1,81 | niska–średnia |
| Rożne Under 10.5 | 66,1% | 1,51 | średnia |
| Kartki Over 2.5 (śr. 3,9: Mariani 3,5–4 + Fio 2,5 żółtej/mecz, Inter mało kartek) | 70,2% | 1,42 | średnia |
| Kartki Over/Under 3.5 | 52,0% / 48,0% | 1,92 / 2,08 | niska |
| Kartki Under 4.5 | 64,7% | 1,55 | średnia |
| Faule Over 20.5 (śr. 22,5) | 63,9% | 1,56 | niska |
| Faule Under 24.5 | 66,6% | 1,50 | niska |
| Strzały Over 24.5 (śr. 27: Inter ok. 18, Fio ok. 9–10) | 65,4% | 1,53 | niska |

**Ryzyka:** (a) remis (18,5%) – Inter po LM w środę, zmęczenie, Fiorentina z De Geą i zagęszczoną defensywą; (b) wygrana Fiorentiny (15%) – Inter tracił gole (4 z Brugge, 1 z Bologną), drużyna w kryzysie gra "o życie" i ma kontry. Dla Over 2.5/BTTS: Inter zagrał 1–0 z Szachtarem i 3–0 z Parmą – mecze "do zera" się zdarzają. Rożne: mała próbka (4 mecze).

**Typy z p>50% i fair>1.15:** 1 Inter 66,5% (1,50), Inter ≥2 gole 66,9% (1,49), Over 2.5 64,1% (1,56), Fiorentina ≥1 63,2% (1,58), Under 3.5 58,0% (1,72), BTTS tak 56,9% (1,76), 12 81,5% (1,23), 1X 85,0% (1,18 – graniczny), Over 1.5 84,1% (1,19 – graniczny), kartki Over 2.5 70,2% (1,42), kartki Under 4.5 64,7% (1,55), rożne Under 10.5 66,1% (1,51), rożne O8.5 56,5% / U9.5 55,3% (niska), faule O20.5 63,9% (niska), strzały O24.5 65,4% (niska). Najlepsze rynki meczu: 1 Inter i kartki Over 2.5.

---

### 14:00 Athletic Club – Getafe (La Liga, 10. kolejka, San Mamés)

**Kluczowe dane (ESPN 401882835)**
- Tabela: Athletic 15. miejsce, 9 pkt w 8 meczach (2-3-3), bramki 8–9 (1,0 / 1,13). Getafe 16., 9 pkt w 9 (2-3-4), bramki 5–11 (0,56 / 1,22). Obie drużyny bardzo słabo strzelają.
- Forma Athletic: 3–0 Atlético (d), 1–1 Elche (d), 0–0 Alavés (d), 0–0 w Walencji, 1:3 w Levante (śr. 21.10, czerwona kartka Laporte). Bez wygranej od 4 meczów.
- Forma Getafe: 1–0 Málaga (d), 0:3 w Barcelonie, 1–1 w Craiovej (LK), 1–1 Rayo (d, czerwona Djené), 2:5 z Lugano (d, LK, czwartek 22.10) → 3 dni odpoczynku, Athletic 4 dni.
- Boxscore 5 ost. meczów (ESPN): Athletic rożne 6,0 zdobyte / 3,0 oddane, strzały 16,8 (oddane 9,6), faule 11,6, żółte 1,8 (+1 czerwona). Getafe rożne 7,0 / 6,4 (zawyżone przez 15 z Lugano), strzały oddane rywalom 15,4, faule 11,6, żółte 3,2 (+1 czerwona) – styl Bordalása.
- H2H (ESPN): 2–0 Getafe (04.2026), 0–1 Athletic u siebie (10.2025), 2–0 dla Athletic w Getafe (05.2025), 1–1 (08.2024), 2–0 Athletic (05.2024). Wszystkie 5 meczów ≤ 2 gole; Getafe nie przegrał 2 ostatnich.
- Sędzia: Francisco Hernández Maeso (Extremadura) – EFE/Infobae. Średnia kartek sędziego – brak danych → liczona ze stylu drużyn i średniej La Ligi.

**Newsy (EFE/Infobae 24.10, RFEF, Radio Nervión, Asesorías Fantasy)**
- Athletic (trener Edin Terzić): zawieszony Aymeric Laporte (czerwona z Levante); kontuzje: Oihan Sancet (mięsień), Gorka Guruzeta (kolano, do końca sezonu); Álvaro Djaló wątpliwy (infekcja). Po rotacji w środę ma wrócić podstawowy skład.
- Getafe (Bordalás): zawieszony Djené; kontuzje długotrwałe Juanmi, Christantus Uche; Enes Ünal wątpliwy (kostka); Mangala i Zaid Romero blisko powrotu. Przewidywany atak Satriano + Ünal, w bramce Soria. Klub "en plena marejada" (kryzys, EFE).

**Rynek DraftKings (ESPN pickcenter):** 1 1,56 / X 4,00 / 2 7,50 → bez marży 1 61,4%, X 23,9%, 2 14,7%; total 2.5: Over 2,25 / Under 1,65 → Under 2.5 ≈ 57,8%.

**λ:** Athletic 1,55, Getafe 0,70. Athletic ma dominację (62–69% posiadania, 17 strzałów) ale niską skuteczność (1 gol/mecz) i brak Sancet/Guruzety; brak Laporte osłabia obronę (+ dla Getafe), Getafe zmęczony po czwartku i z najsłabszym atakiem ligi (0,56). Model 57,8% vs rynek 61,4% (−3,6 pp, w limicie 5 pp; uzasadnienie: absencje Sancet/Guruzeta/Laporte). Kryzys Getafe (underdog) nie podnosi jego szans powyżej modelu.

| Rynek | p | fair | pewność |
|---|---|---|---|
| 1 Athletic | 57,8% | 1,73 | średnia |
| X | 25,5% | 3,92 | średnia |
| 2 Getafe | 16,8% | 5,97 | średnia |
| 1X | 83,3% | 1,20 (graniczny) | wysoka |
| X2 | 42,3% | 2,36 | średnia |
| 12 | 74,6% | 1,34 | średnia |
| Over 1.5 | 65,7% | 1,52 | średnia |
| Under 1.5 | 34,3% | 2,92 | średnia |
| Over 2.5 | 39,1% | 2,56 | średnia |
| Under 2.5 | 60,9% | 1,64 | średnia–wysoka |
| Over 3.5 | 19,1% | 5,25 | średnia |
| Under 3.5 | 80,9% | 1,24 | wysoka |
| BTTS tak | 39,7% | 2,52 | średnia |
| BTTS nie | 60,3% | 1,66 | średnia–wysoka |
| Athletic ≥1 gol | 78,8% | 1,27 | średnia |
| Athletic ≥2 gole | 45,9% | 2,18 | niska–średnia |
| Getafe ≥1 gol | 50,3% | 1,99 | średnia |
| Getafe Under 1.5 gola | 84,4% | 1,18 (graniczny) | wysoka |
| Rożne Over 8.5 (śr. 10,0: Athletic ok. 6,5, Getafe ok. 3,5) | 64,2% | 1,56 | średnia |
| Rożne Over/Under 9.5 | 52,8% / 47,2% | 1,89 / 2,12 | niska |
| Kartki Over 3.5 (śr. 5,0: Getafe 3,2 + Athletic 1,8; sędzia bez danych) | 69,3% | 1,44 | średnia |
| Kartki Over 4.5 | 53,4% | 1,87 | niska |
| Faule Over 21.5 (śr. 24) | 67,1% | 1,49 | niska–średnia |
| Strzały Over 22.5 (śr. 25: Athletic ok. 17, Getafe ok. 8) | 65,9% | 1,52 | niska |

**Ryzyka:** (a) remis 25,5% – Athletic 3 remisy (0–0 ×2) w 5 meczach, nie umie zamieniać przewagi na gole, brak Sancet i Guruzety; Getafe Bordalása gra na 0–0; (b) wygrana Getafe 16,8% – osłabiona obrona bez Laporte, stałe fragmenty, H2H: Getafe wygrał 1–0 na San Mamés rok temu. Dla Under 2.5: wynik 2–1/3–0 przy wczesnym golu Athletic (Getafe stracił 5 goli w czwartek ze zmęczeniem). Kartki: sędzia bez średniej.

**Typy z p>50% i fair>1.15:** Under 3.5 80,9% (1,24), Athletic ≥1 78,8% (1,27), 12 74,6% (1,34), kartki Over 3.5 69,3% (1,44), faule Over 21.5 67,1% (1,49), strzały O22.5 65,9% (niska), Over 1.5 65,7% (1,52), rożne Over 8.5 64,2% (1,56), Under 2.5 60,9% (1,64), BTTS nie 60,3% (1,66), 1 Athletic 57,8% (1,73), kartki O4.5 53,4% (niska), rożne O9.5 52,8% (niska), Getafe ≥1 50,3% (1,99, na granicy), 1X 83,3% (1,20 – graniczny), Getafe U1.5 84,4% (1,18 – graniczny). Najlepsze rynki: Under 2.5 / BTTS nie, kartki Over 3.5, rożne Over 8.5.

---

## Tabela kandydatów (dla bet-slip-builder)

| Mecz | Rynek | p | fair | pewność | od czego zależy | kurs rynkowy |
|---|---|---|---|---|---|---|
| Inter – Fiorentina | 1 Inter | 66,5% | 1,50 | średnia–wysoka | skład po LM | DK 1,34 (fair rynku 1,45) |
| Inter – Fiorentina | Inter ≥2 gole | 66,9% | 1,49 | średnia | Thuram/Esposito w XI | brak |
| Inter – Fiorentina | Over 2.5 | 64,1% | 1,56 | średnia | – | ok. 1,40 (QSC) |
| Inter – Fiorentina | Kartki Over 2.5 | 70,2% | 1,42 | średnia | sędzia Mariani (znany) | ok. 1,45 combo (Mondopengwin) |
| Athletic – Getafe | Under 3.5 | 80,9% | 1,24 | wysoka | – | brak |
| Athletic – Getafe | Under 2.5 | 60,9% | 1,64 | średnia–wysoka | – | DK 1,65 |
| Athletic – Getafe | BTTS nie | 60,3% | 1,66 | średnia–wysoka | Ünal (wątpliwy) | brak |
| Athletic – Getafe | Kartki Over 3.5 | 69,3% | 1,44 | średnia | sędzia bez średniej | brak |
| Athletic – Getafe | Rożne Over 8.5 | 64,2% | 1,56 | średnia | dominacja Athletic | brak |
| Athletic – Getafe | 1 Athletic | 57,8% | 1,73 | średnia | absencje ofensywne | DK 1,56 |
| Śląsk – Wieczysta | X2 | 66,5% | 1,50 | średnia | – | ok. 1,40–1,45 (wyliczone z 1X2) |
| Śląsk – Wieczysta | Over 1.5 | 80,1% | 1,25 | średnia | – | brak |
| Śląsk – Wieczysta | BTTS tak | 60,1% | 1,66 | średnia | – | 1,44–1,49 (bez value) |
| Śląsk – Wieczysta | Under 3.5 | 64,7% | 1,55 | średnia | – | brak |

Oszacowania probabilistyczne, nie gwarancje; przed meczem potwierdź oficjalne składy (ok. 60 min przed startem).

Źródła (WebSearch): fotmob.com (Śląsk–Wieczysta), gol24.pl (absencje i sędziowie 12. kolejki), sportowefakty.wp.pl, slasknet.com, dziennikpolski24.pl, sport.tvp.pl, sport.interia.pl, zapowiedzi bukmacherskie (mecze24, etoto, lvbet, betfan – nagłówki/streszczenia); tuttosport.com, sport.quotidiano.net, firenzepost.it, napolimagazine.com (Sportitalia), violanews.com, mondopengwin.it, quotescommessecalcio.com; infobae.com (EFE), elgoldigital.com, radionervion.com, asesoriasfantasy.com; ESPN API (dane liczbowe Inter/Athletic).

## Analiza meczów 25.10.2026 (część B) – football-analyst

Źródła wspólne: ESPN API (`ita.1` summary/scoreboard/schedule – tabela, lastFiveGames, H2H, boxscore wszystkich 75 rozegranych meczów Serie A 2026/27, kursy DraftKings z pickcenter), WebSearch (newsy, sędziowie, absencje). Ekstraklasy nie ma w ESPN (`pol.1` → 404), Sofascore/FotMob/ekstraklasa.org niedostępne z sesji – dla meczu 1 dane tylko z wyników WebSearch (mniej liczb, niższa pewność). Brak xG w dostępnych źródłach (wszystkie trzy mecze) – λ oparte na golach/strzałach, nie na xG.

Średnie Serie A 2026/27 (ESPN, 75 meczów): gole 3,00 (dom 1,59 / wyjazd 1,41), rożne 9,5, faule 21,8, żółte kartki 3,28 (uwaga: ESPN prawdopodobnie zaniża kartki względem oficjalnych protokołów – stąd niska pewność rynków kartkowych w Serie A), strzały 29,0.

---

### 14:45 Jagiellonia Białystok – Wisła Płock (Ekstraklasa, 12. kolejka)

**Kluczowe dane**
- Jagiellonia: 4 porażki z rzędu w lidze (m.in. 1:3 z Górnikiem Zabrze 10.10, 0:1 w Lubinie z Zagłębiem 18.10), 13. miejsce, 12 pkt (WebSearch: sportowefakty/polskapilka/jagiellonia.pl). W czwartek 22.10 Liga Europy (faza ligowa, 3. kolejka): **0:3 u siebie z Anderlechtem** (weszlo.com, gol24.pl, sportowefakty) – wcześniej 1:2 z Olympiakosem i 3:1 z Ararat-Armenia. Trener Adrian Siemieniec. Mecz 3 dni po pucharach.
- Wisła Płock: 10. miejsce (wg Eurosport tabela 14 pkt/10 meczów, 4-2-4; po 11. kolejce prawdopodobnie 17 pkt), w 11. kolejce 1:0 z Radomiakiem (gol 15', strzelec zapisany w źródle jako „Jurica Prszir”, weszlo.com „Jaki to był zły mecz”, Interia) – drużyna raczej defensywna, mecze niskobramkowe.
- Statystyk goli/strzałów/rożnych sezonu 2026/27 obu drużyn **nie udało się pobrać** (brak dostępu do Flashscore/Sofascore) – rożne liczone ze średniej ligowej (~9,6), niska pewność.
- Sędzia: **Damian Kos** (jagiellonia.pl, wisla-plock.pl, sportowefakty) – w sezonie 2026/27: 5 meczów, 26 żółtych, 0 czerwonych (≈5,2 ŻK/mecz) → surowy; średnia kartek podniesiona do 4,9 (z ~4,5 ligowej, ściągnięta ku średniej przy małej próbie).
- H2H (ostatnie 2 sezony): 19.09.2025 Wisła – Jagiellonia 0:1 (Pululu), 21.03.2026 Jagiellonia – Wisła 1:2 (dublet Deni Jurić) (weszlo, Interia, goal.pl).
- Absencje: Jagiellonia – Norbert Wojtuszek (kontuzja); Wisła – lista ucięta w źródle (Jorge Jiménez i in., niepełna) (gol24 „Kto nie zagra w 12. kolejce”). Przewidywane składy na 25.10 niedostępne.
- Rynek (mecze24.pl, średnia kursów PL): 1 = 1.92, X = 3.65, 2 ≈ 3.9 (szacowane) → bez marży ok. 49,6% / 26,1% / 24,4%. DraftKings/ESPN – brak.

**λ:** Jagiellonia 1,55 – Wisła 1,05 (łącznie 2,60). Forma Jagi jest już w kursie (zasada: nie obniżam faworyta za serię porażek); zmęczenie po czwartkowym meczu europejskim uwzględnione lekko (λ gospodarzy niżej niż typowe dla Jagi u siebie). Wisła nie jest w kryzysie (wygrała ostatni mecz) – brak korekty kryzysowej.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 Jagiellonia | 48,9% | 2.05 | niska |
| X | 25,4% | 3.93 | niska |
| 2 Wisła | 25,7% | 3.89 | niska |
| 1X | 74,3% | 1.35 | średnia/niska |
| X2 | 51,1% | 1.96 | niska |
| 12 | 74,6% | 1.34 | niska |
| Over 1.5 | 73,3% | 1.36 | średnia/niska |
| Under 1.5 | 26,7% | 3.74 | niska |
| Over 2.5 | 48,2% | 2.08 | niska |
| Under 2.5 | 51,8% | 1.93 | niska |
| Over 3.5 | 26,4% | 3.79 | niska |
| Under 3.5 | 73,6% | 1.36 | średnia/niska |
| BTTS tak | 51,2% | 1.95 | niska |
| BTTS nie | 48,8% | 2.05 | niska |
| Jagiellonia Over 0.5 gola | 78,8% | 1.27 | średnia/niska |
| Jagiellonia Over 1.5 gola | 45,9% | 2.18 | niska |
| Wisła Over 0.5 gola | 65,0% | 1.54 | niska |
| Wisła Over 1.5 gola | 28,3% | 3.53 | niska |
| Rożne Over 8.5 (śr. 9,6 – średnia ligowa) | 59,9% | 1.67 | niska (brak danych drużyn) |
| Rożne Over 9.5 | 48,2% | 2.07 | niska |
| Rożne Under 10.5 | 62,8% | 1.59 | niska |
| Kartki Over 3.5 (śr. 4,9, sędzia Kos) | 67,9% | 1.47 | średnia/niska |
| Kartki Over 4.5 | 51,8% | 1.93 | niska |
| Kartki Under 5.5 | 63,2% | 1.58 | niska |
| Faule / strzały | – | – | brak danych, bez wyceny |

Najczęstsze wyniki: 1-1 12,1%, 1-0 11,5%, 2-1 9,4%.

**Ryzyka:** (a) remis – Jaga w serii 4 porażek, 3 dni po 0:3 z Anderlechtem, możliwa rotacja i spadek intensywności; Wisła gra niskie tempo; (b) wygrana Wisły – Wisła wygrała ostatnie H2H w Białymstoku 2:1, Jaga traci gole seryjnie. Brak składów i danych statystycznych drużyn; kartki zależą od jednego źródła o sędzi (5 meczów).

**Kalibracja:** 1X2 bez mocnego typu (~49% gospodarzy, zgodnie z rynkiem, różnica −0,7 pp). Rynki dodatkowe bez rekomendacji „wysoka” (brak dwóch źródeł średnich).

**Typy z p>50% i fair>1.15:** Jagiellonia Over 0.5 gola 78,8% (1.27); 1X 74,3% (1.35); Under 3.5 73,6% (1.36); Over 1.5 73,3% (1.36); kartki Over 3.5 67,9% (1.47); Wisła Over 0.5 gola 65,0% (1.54); kartki Under 5.5 63,2% (1.58); rożne Under 10.5 62,8% / Over 8.5 59,9% (niska – tylko średnia ligowa, nie na kupon); granicznie ~50%: Under 2.5 51,8%, kartki Over 4.5 51,8%, BTTS tak 51,2%, X2 51,1%.

---

### 15:00 Atalanta – Frosinone (Serie A, 8. kolejka)

**Kluczowe dane (ESPN)**
- Tabela: Atalanta 11. (7 m., 3-0-4, 9 pkt, gole 10:11), Frosinone 6. (7 m., 4-1-2, 13 pkt, gole 13:9 – „rewelacja”, bergamonews.it).
- Atalanta u siebie: 3:1 Venezia, 1:2 Cagliari, 1:0 Bologna, 2:1 Sassuolo (7:4 w 4 meczach); ostatnio 2:3 w Mediolanie z Milanem (18.10) i **0:2 z Ajaxem w Amsterdamie w czwartek 22.10** (Liga Konferencji) – 3 dni przerwy, 3 porażki wyjazdowe z rzędu.
- Frosinone na wyjeździe: 1:1 Genoa, 3:0 w Florencji, 0:3 w Neapolu; ostatnio 4:2 z Sassuolo. Raimondo 7 goli (24 strzały), Kvernadze 3 gole.
- Statystyki meczowe (ESPN boxscore, średnie na mecz): Atalanta rożne 3,6 za / 4,9 przeciw, faule 10,3, strzały 13,3 za / 18,0 przeciw; Frosinone rożne 5,4 / 6,9, faule 16,0 (najwięcej w tej czwórce), strzały 17,4 / 19,6. Średnia sum w meczach: strzały 31,3 (ATA) i 37,0 (FRO), gole 3,0 i 3,1.
- Absencje (bergamonews.it 25.10, Sky Sport 20.10): Atalanta bez **Hiena, Kolašinaca, Scalviniego** (trzech środkowych obrońców), Kessiégo, Kamaldeena, Raspadoriego, Pompeia; Frosinone bez Grillitscha (inne listy: Birligea out, Raimondo „do oceny” – kluczowe dla typów na Frosinone; jeśli Raimondo nie zagra, λ Frosinone −0,15).
- Sędzia: **Livio Marinelli** (Tivoli), VAR Dionisi (sport.sky.it, tuttoatalanta, tuttofrosinone). W danych ESPN tylko 1 mecz (Inter–Monza: 4 ŻK, 19 fauli) – za mała próba, kartki ze średniej ligowej skorygowanej o faulującą Frosinone.
- H2H (ESPN): 01.2024 5:0, 08.2023 1:2 (Frosinone), 2019 5:0, 2018 4:0, 2016 0:0 – stare, niska waga.
- Rynek DraftKings (ESPN pickcenter): 1 = 1.83 (-120; otwarcie -170!), X = 3.95, 2 = 3.50 (otwarcie +350) → bez marży 50,3% / 23,4% / 26,4%; Over 3.5 = 1.83 / Under 3.5 = 1.95 (otwarcie Over +110) → Over 3.5 ok. 51,6%. Silny ruch rynku przeciw Atalancie i w stronę goli – zgodny z kryzysem kadrowym w obronie i meczem w czwartek.

**λ:** Atalanta 1,95 – Frosinone 1,50 (łącznie 3,45). Podstawa: atak ATA u siebie ~1,75/m, obrona FRO na wyjeździe średnia; λ Frosinone podniesione za brak trzech środkowych obrońców Atalanty (konkretna informacja kadrowa po stronie obrony; korekta jednostronna).

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 Atalanta | 48,3% | 2.07 | niska |
| X | 21,9% | 4.56 | niska |
| 2 Frosinone | 29,8% | 3.35 | niska |
| 1X | 70,2% | 1.42 | średnia/niska |
| X2 | 51,7% | 1.93 | niska |
| 12 | 78,1% | 1.28 | średnia |
| Over 1.5 | 85,9% | 1.16 | średnia (granica 1.15-1.20) |
| Over 2.5 | 67,0% | 1.49 | średnia |
| Under 2.5 | 33,0% | 3.03 | niska |
| Over 3.5 | 45,3% | 2.21 | niska (rynek 51,6%) |
| Under 3.5 | 54,7% | 1.83 | niska – przeciw rynkowi, nie rekomenduję |
| BTTS tak | 66,6% | 1.50 | średnia |
| BTTS nie | 33,4% | 3.00 | niska |
| Atalanta Over 0.5 gola | 85,8% | 1.17 | średnia (granica) |
| Atalanta Over 1.5 gola | 58,0% | 1.72 | niska/średnia |
| Frosinone Over 0.5 gola | 77,7% | 1.29 | średnia |
| Frosinone Over 1.5 gola | 44,2% | 2.26 | niska |
| Rożne Over 8.5 (śr. 10,2) | 66,3% | 1.51 | niska/średnia |
| Rożne Over 9.5 | 55,1% | 1.82 | niska |
| Rożne Under 11.5 | 66,5% | 1.50 | niska |
| Kartki (ŻK) Over 2.5 (śr. 3,8) | 68,7% | 1.46 | niska (ESPN zaniża ŻK, sędzia bez próby) |
| Kartki Over 3.5 | 50,2% | 1.99 | niska |
| Kartki Under 4.5 | 66,4% | 1.51 | niska |
| Faule Over 22.5 (śr. 25,5) | 70,1% | 1.43 | niska |
| Faule Over 24.5 | 55,8% | 1.79 | niska |
| Strzały łącznie Over 28.5 (śr. 33, definicja ESPN z zablokowanymi) | 75,2% | 1.33 | niska |
| Strzały Over 30.5 | 63,9% | 1.56 | niska |

Najczęstsze wyniki: 1-1 9,3%, 2-1 9,1%, 1-2 7,0%, 2-2 6,8%.

**Ryzyka:** (a) remis – zmęczona, osłabiona Atalanta po Amsterdamie, Frosinone w formie; (b) wygrana Frosinone – trzy porażki wyjazdowe Atalanty z rzędu, improwizowana linia obrony, Raimondo (7 goli) groźny na kontrach; dla Overów: niski scenariusz, jeśli Atalanta zagra ostrożnie, a Raimondo nie wystąpi.

**Kalibracja:** p Atalanty 48,3% vs rynek 50,3% (−2 pp, w granicy 5 pp). Total: moje Over 3.5 45% vs rynek 51,6% – rozbieżność 6 pp bez dodatkowej wiedzy → rynek bywa trafniejszy; nie gram Under 3.5 przeciw ruchowi rynku. Over 2.5 i BTTS spójne z formą obu (oba tracą w ≥ 60% meczów: ATA 6/7, FRO 5/7).

**Typy z p>50% i fair>1.15:** Over 1.5 85,9% (1.16, graniczny); Atalanta Over 0.5 85,8% (1.17, graniczny); 12 78,1% (1.28); Frosinone Over 0.5 77,7% (1.29); strzały Over 28.5 75,2% (1.33, niska); 1X 70,2% (1.42); faule Over 22.5 70,1% (1.43, niska); kartki Over 2.5 68,7% (1.46, niska); **Over 2.5 67,0% (1.49)**; **BTTS tak 66,6% (1.50)**; rożne Under 11.5 66,5% / Over 8.5 66,3% (1.51); kartki Under 4.5 66,4%; strzały Over 30.5 63,9%; Atalanta Over 1.5 58,0%; faule Over 24.5 55,8%; rożne Over 9.5 55,1%; Under 3.5 54,7% (nie rekomenduję – przeciw rynkowi); X2 51,7%; kartki Over 3.5 50,2%. Najlepszy rynek meczu: Over 2.5 / BTTS tak.

---

### 15:00 Genoa – Venezia (Serie A, 8. kolejka)

**Kluczowe dane (ESPN)**
- Tabela: Genoa 17. (7 m., 1-1-5, 4 pkt, gole 5:13), Venezia 20. (7 m., 1-0-6, 3 pkt, gole 6:16) – mecz o utrzymanie.
- Genoa u siebie: 1:1 Frosinone, 1:4 Como, 0:2 Napoli, 2:1 Fiorentina (4:8); ostatnio 0:2 w Rzymie. Brak gry w pucharach w tygodniu.
- Venezia na wyjeździe: 2:3 Frosinone, 1:3 Atalanta, 0:2 Milan (3:8); ostatnio sensacyjne 1:0 z Napoli (przy 9-29 strzałach i 0-12 rożnych – wynik ponad grę).
- Średnie meczowe (ESPN boxscore): Genoa rożne 4,4 za / 4,7 przeciw, faule 9,4, ŻK 2,6 własnych (4,4 w meczu); Venezia rożne 4,1 / 4,7, faule 10,7, ŻK 2,9 (3,9 w meczu). Sumy w meczach: faule 21,4 / 20,4; strzały 26,4 / 31,6.
- Absencje (eurosport.it, Sky Sport, trivenetogoal.it 24.10, bet365 news): Genoa bez Colombo (lider asyst), Venturino, Meichtry'ego, Havela, Sowa, Nuredini; Baldanzi wątpliwy, Ehizibue do oceny. Venezia bez Franjicia, Adorante, Correii, Sverko; Busio i Bella-Kotchap wrócili do kadry (trener Nicola). Brak zawieszeń.
- Przewidywane składy: Genoa (3-4-2-1) Bijlow; Marcandalli, Østigård, Vásquez; Ellertsson, Frendrup, Traoré, Puczka/Ehizibue; Messias, El Shaarawy; Osmajić. Venezia (3-5-2) Stanković; Moreno/Schingtienne, Juan Jesus, Halhal; Hainaut, Kike Pérez, Basić, Sohm, Haps; Yeboah, Akor Adams.
- Sędzia: **Simone Sozza**, VAR Di Paolo (tuttofrosinone, calvar, quotidiano.net). W ESPN 2 mecze: Inter–Napoli 3 ŻK, Venezia–Lazio 6 ŻK.
- H2H (ESPN): 2025 2:0, 2024 0:2, 2023 1:0 (Serie B), 2022 1:2, 2022 1:1 – śr. 2,0 gola, 2/5 BTTS.
- Rynek DraftKings: 1 = 2.10 (+110), X = 3.20, 2 = 3.35 → bez marży 43,8% / 28,7% / 27,5%; Over 2.5 = 2.00 / Under 2.5 = 1.80 → Under ok. 52,6%.

**λ:** Genoa 1,40 – Venezia 1,05 (łącznie 2,45). Oba ataki najsłabsze w lidze (0,71 i 0,86 gola/m.), obie obrony słabe (1,86 i 2,29 straconych/m.) – wartości ściągnięte ku średniej ze względu na małą próbę. Brak Colombo: niewielka korekta ataku Genoi (≤3 pp, zgodnie z zasadą). Brak przepaści klas → reguła kryzysu underdoga nie ma zastosowania.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 Genoa | 45,0% | 2.22 | niska |
| X | 26,8% | 3.73 | niska |
| 2 Venezia | 28,2% | 3.54 | niska |
| 1X | 71,8% | 1.39 | średnia/niska |
| X2 | 55,0% | 1.82 | niska |
| 12 | 73,2% | 1.37 | niska |
| Over 1.5 | 70,2% | 1.42 | średnia/niska |
| Under 1.5 | 29,8% | 3.36 | niska |
| Over 2.5 | 44,3% | 2.26 | niska |
| Under 2.5 | 55,7% | 1.80 | niska/średnia (rynek 52,6%) |
| Over 3.5 | 23,2% | 4.31 | niska |
| Under 3.5 | 76,8% | 1.30 | średnia |
| BTTS tak | 49,0% | 2.04 | niska |
| BTTS nie | 51,0% | 1.96 | niska |
| Genoa Over 0.5 gola | 75,3% | 1.33 | średnia/niska |
| Genoa Over 1.5 gola | 40,8% | 2.45 | niska |
| Venezia Over 0.5 gola | 65,0% | 1.54 | niska |
| Venezia Under 1.5 gola | 71,7% | 1.39 | niska/średnia |
| Rożne Over 7.5 (śr. 9,0) | 65,0% | 1.54 | niska/średnia |
| Rożne Over 8.5 | 53,0% | 1.89 | niska |
| Rożne Under 10.5 | 69,4% | 1.44 | niska/średnia |
| Kartki (ŻK) Over 3.5 (śr. 4,3, stawka „o utrzymanie”) | 58,8% | 1.70 | niska |
| Kartki Under 5.5 | 72,2% | 1.39 | niska |
| Faule Over 19.5 (śr. 21) | 60,4% | 1.65 | niska |
| Faule Under 23.5 | 70,6% | 1.42 | niska |
| Strzały łącznie Over 24.5 (śr. 28) | 71,4% | 1.40 | niska |
| Strzały Over 26.5 | 58,5% | 1.71 | niska |

Najczęstsze wyniki: 1-1 12,8%, 1-0 11,6%, 0-1 9,5%, 0-0 8,6%.

**Ryzyka:** (a) remis – dwie najsłabsze ofensywy, mecz nerwowy, 1-1 najczęstszym wynikiem; (b) wygrana Venezii – świeża wygrana z Napoli, powrót Busio, słaba Genoa u siebie (1 wygrana w 4). Dla Under 2.5: obie obrony tracą dużo (Venezia 2,3/m.), więc Over 2.5 realny mimo słabych ataków.

**Kalibracja:** Genoa 45,0% vs rynek 43,8% (+1,2 pp) – wyrównany mecz, **brak mocnego typu w 1X2**. Under 2.5 +3 pp nad rynek – w granicy, bez wyciągania przewagi z absencji.

**Typy z p>50% i fair>1.15:** Under 3.5 76,8% (1.30); Genoa Over 0.5 75,3% (1.33); 12 73,2% (1.37); Under 5.5 kartek 72,2% (1.39); 1X 71,8% (1.39); Venezia Under 1.5 71,7% (1.39); strzały Over 24.5 71,4% (1.40, niska); faule Under 23.5 70,6% (1.42, niska); Over 1.5 70,2% (1.42); rożne Under 10.5 69,4% (1.44); Venezia Over 0.5 65,0%; rożne Over 7.5 65,0% (1.54); faule Over 19.5 60,4%; kartki Over 3.5 58,8%; strzały Over 26.5 58,5%; **Under 2.5 55,7% (1.80)**; X2 55,0%; rożne Over 8.5 53,0%; BTTS nie 51,0%. Najlepszy rynek meczu: Under 3.5 / 1X.

### Ranking TOP (wszystkie rynki, fair > 1.15, p > 50%) i kandydaci na kupon

| # | Mecz | Rynek | p | fair | pewność | zależy od | kurs rynkowy |
|---|---|---|---|---|---|---|---|
| 1 | Atalanta – Frosinone | 12 | 78,1% | 1.28 | średnia | – | brak (DK tylko 1X2/O3.5) |
| 2 | Genoa – Venezia | Under 3.5 | 76,8% | 1.30 | średnia | skład Genoi (Colombo out) | brak |
| 3 | Jagiellonia – Wisła | 1X | 74,3% | 1.35 | średnia/niska | rotacja Jagi po LE | ~1.3 (szac. z 1.92/3.65) |
| 4 | Jagiellonia – Wisła | Under 3.5 | 73,6% | 1.36 | średnia/niska | brak statystyk drużyn | brak |
| 5 | Genoa – Venezia | 1X | 71,8% | 1.39 | średnia/niska | – | brak (DK 1 = 2.10, X = 3.20) |
| 6 | Atalanta – Frosinone | 1X | 70,2% | 1.42 | średnia/niska | 3 CB Atalanty out | brak |
| 7 | Jagiellonia – Wisła | Kartki Over 3.5 | 67,9% | 1.47 | średnia/niska | sędzia Kos (5,2 ŻK/m., 5 meczów) | brak |
| 8 | Atalanta – Frosinone | Over 2.5 | 67,0% | 1.49 | średnia | Raimondo (do oceny) | brak (DK O3.5 1.83) |
| 9 | Atalanta – Frosinone | BTTS tak | 66,6% | 1.50 | średnia | Raimondo (do oceny) | brak |
| 10 | Atalanta – Frosinone | Rożne Over 8.5 | 66,3% | 1.51 | niska/średnia | jedno źródło (ESPN) | brak |
| 11 | Genoa – Venezia | Under 2.5 | 55,7% | 1.80 | niska/średnia | – | DK Under 1.80 (EV ≈ 0) |

Graniczne 1.15-1.20: Atalanta – Frosinone Over 1.5 (1.16) i Atalanta Over 0.5 (1.17). Rynki kartek/fauli/strzałów w Serie A i rożnych w Ekstraklasie mają tylko jedno źródło (albo średnią ligową), więc wg zasady skilla nie powinny iść do kuponu jako nogi główne. 1X2 we wszystkich trzech meczach: brak mocnego typu (43-49%).

---

*To oszacowania probabilistyczne oparte na niepełnych danych (brak xG, w Ekstraklasie brak statystyk drużynowych), nie gwarancje.*

## Premier League, niedziela 25.10.2026, analiza skillem football-analyst (część C)

**Źródła ogólne:** ESPN API (summary dla 401878765 / 401879252 / 401879254: tabela, lastFiveGames, seasonseries, pickcenter DraftKings), ESPN boxscore wszystkich 7 meczów ligowych każdej drużyny w sezonie 2026/27 (strzały, celne, rożne, faule, kartki, posiadanie, sędziowie), WebSearch (NBC Sports, Sports Mole, Dave.sport, This Is Anfield, Liverpool.com, SI, WhoScored preview, Last Word on Sports, Football Faithful).
**Braki:** brak xG (MCP sportsdata nie działa, FBref/Understat nie sprawdzone), dlatego jako proxy xG użyto strzałów i strzałów celnych. Statystyki rożnych/kartek/fauli pochodzą z jednego źródła (ESPN boxscore, 7 meczów), więc wszystkie rynki dodatkowe mają najwyżej **niską** pewność i zgodnie ze skillem nie są rekomendowane jako typ główny. Sędziowie MU–BOU i CRY–NEW nieznani (średnia ligowa). Uwaga: jeden serwis wspominał o sztormie "Boelo" nad UK; nie potwierdzono przełożenia ani wpływu (wiatr może obniżać jakość gry i podnosić losowość).
**Kursy DraftKings** (ESPN pickcenter, amerykańskie → dziesiętne, p bez marży proporcjonalnie) służą jako kontrola rynku.

Średnie sezonowe z boxscore ESPN (7 meczów PL, za / przeciw):

| Drużyna | Gole | Strzały | Celne | Rożne | Faule | Żółte |
|---|---|---|---|---|---|---|
| Liverpool (5., 12 pkt) | 1.29 / 1.14 | 15.7 / 11.9 | 5.0 / 3.4 | 4.9 / 4.4 | 13.9 / 10.3 | 2.4 / 2.0 |
| Brighton (3., 16 pkt, GD +18) | 3.29 / 0.71 | 17.9 / 10.7 | 6.0 / 3.3 | 5.7 / 5.0 | 12.9 / 10.0 | 2.1 / 1.3 |
| Man United (15., 7 pkt) | 1.43 / 1.43 | 19.7 / 11.0 | 5.0 / 4.4 | 6.1 / 3.6 | 9.6 / 11.4 | 1.7 / 2.6 |
| Bournemouth (17., 6 pkt) | 1.29 / 1.86 | 15.1 / 9.6 | 5.1 / 3.7 | 4.7 / 3.9 | 13.0 / 12.0 | 3.0 / 1.4 |
| Crystal Palace (16., 7 pkt) | 1.29 / 2.43 | 10.1 / 17.9 | 3.7 / 6.1 | 3.1 / 5.7 | 10.0 / 10.0 | 1.3 / 1.6 |
| Newcastle (14., 8 pkt) | 1.43 / 2.00 | 12.3 / 17.3 | 3.6 / 5.3 | 4.6 / 5.3 | 12.1 / 11.3 | 2.7 / 2.1 |

---

### 15:00 Liverpool – Brighton (Premier League)

**Kluczowe dane**
- Tabela (ESPN): Brighton 3. (5-1-1, 19:5 bramek, w tym 5-0 z Palace, 3-0 z Arsenalem, 5-0 w Coventry), Liverpool 5. (3-3-1, 9:8). Liverpool w lidze strzela mało jak na liczbę strzałów (15.7 strzału / 1.29 gola; 27 strzałów w 2-2 z Newcastle), za to w LM 6-3 z LASK i 4-3 z Villarrealem.
- Kalendarz: Liverpool grał we wtorek 20.10 (LM, dom, 4-3), Brighton w czwartek 22.10 (LKE w Jabloncu, 0-0, podróż do Czech) - Brighton ma 3 dni odpoczynku, Liverpool 5 (ESPN lastFiveGames). Lekki plus Liverpoolu.
- H2H (ESPN seasonseries): 2-1 dla BHA (03.2026), 3-0 LIV (02.2026), 2-0 LIV (12.2025), 3-2 BHA (05.2025), 2-1 LIV (11.2024). Liverpool 3-2 w 5 meczach, w Anfield bez straty gola w dwóch ostatnich.
- Sędzia: **Sam Barrott**, VAR Michael Oliver (SI, Liverpool.com, Brit Brief). W tym sezonie u Barrotta: LIV–NFO 2-2 (6 żółtych), FUL–CRY (0 żółtych) - za mała próba, kartki liczone ze stylu drużyn.

**Newsy**
- Liverpool bez: Szoboszlai (udo), Ekitiké (Achilles), Frimpong (mięsień), Bradley, Leoni, Jaros; Muñoz pod znakiem zapytania, Barcola zdrowy (Dave.sport, This Is Anfield). Brak dwóch ważnych ofensywnych ogniw (Szoboszlai, Ekitiké) - λ LIV obniżona o ok. 0.1.
- Brighton bez: Mitoma, Ferguson, Tzimas, Azeez; Struijk (udo) oceniany; Minteh i Wieffer "może opcja", start mało prawdopodobny (Hürzeler na konferencji, This Is Anfield / Yahoo).

**λ:** Liverpool 1.70, Brighton 1.40 (suma 3.10). Atak BHA bardzo mocny (6.0 celnych/mecz), obrona LIV przeciętna; obrona BHA najlepsza w statystyce strzałów przeciw, ale LIV u siebie z przewagą posiadania. Suma bliska rynkowi (DK O3.5 = 40% bez marży, co odpowiada sumie ok. 3.2).

**Rynek (DraftKings):** LIV 2.15 / X 3.80 / BHA 3.20 → bez marży 44.7% / 25.3% / 30.0%. O3.5 2.35 / U3.5 1.59 → U3.5 59.7%. Model zgodny z rynkiem w 1X2 (różnica < 2 pp).

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 Liverpool | 44.7% | 2.24 | niska |
| X | 23.6% | 4.24 | niska |
| 2 Brighton | 31.7% | 3.15 | niska |
| 1X | 68.3% | 1.46 | średnia |
| X2 | 55.3% | 1.81 | niska |
| 12 | 76.4% | 1.31 | średnia |
| Over 1.5 | 81.5% | 1.23 | średnia |
| Over 2.5 / Under 2.5 | 59.9% / 40.1% | 1.67 / 2.49 | średnia |
| Over 3.5 / Under 3.5 | 37.5% / 62.5% | 2.67 / 1.60 | średnia |
| BTTS tak / nie | 61.6% / 38.4% | 1.62 / 2.60 | średnia |
| Liverpool Over 0.5 / 1.5 | 81.7% / 50.7% | 1.22 / 1.97 | średnia / niska |
| Brighton Over 0.5 / 1.5 | 75.3% / 40.8% | 1.33 / 2.45 | średnia / niska |
| Rożne (śr. 10.0) O8.5 / O9.5 / U10.5 / U11.5 | 64.2% / 52.8% / 58.4% / 68.5% | 1.56 / 1.89 / 1.71 / 1.46 | niska |
| Kartki żółte (śr. 4.0, Barrott) O3.5 / U4.5 / U5.5 | 53.8% / 63.0% / 76.5% | 1.86 / 1.59 / 1.31 | niska |
| Faule (śr. 23.5) O21.5 / O22.5 / U24.5 | 63.6% / 56.0% / 59.2% | 1.57 / 1.78 / 1.69 | niska |
| Strzały (śr. 28.1) O24.5 / O26.5 | 71.9% / 59.1% | 1.39 / 1.69 | niska |
| Strzały celne (śr. 8.9) O7.5 / O8.5 | 64.9% / 52.3% | 1.54 / 1.91 | niska |

Najczęstsze wyniki: 1-1 10.7%, 2-1 9.1%, 1-0 7.7%, 1-2 7.5%.

**Ryzyka:** (a) remis (23.6%) - dwie drużyny ofensywne, ale LIV ma 3 remisy w 7 meczach; (b) wygrana Brighton (31.7%) - najlepszy bilans bramkowy ligi, wygrana 2-1 z LIV w marcu; (c) dla totali: przy braku Szoboszlaia/Ekitiké LIV może znów marnować strzały (Under), a sztorm/wiatr zwiększa losowość. Brighton po czwartkowym meczu w Czechach może być zmęczony - to plus dla LIV, ale nie liczbowo duży (rotacja w LKE prawdopodobna).

**Typy z p>50% i fair>1.15:** Over 1.5 (81.5%, 1.23), Over 0.5 Liverpool (81.7%, 1.22), 12 (76.4%, 1.31), Over 0.5 Brighton (75.3%, 1.33), 1X (68.3%, 1.46), Under 3.5 (62.5%, 1.60), BTTS tak (61.6%, 1.62), Over 2.5 (59.9%, 1.67), X2 (55.3%, 1.81), Liverpool Over 1.5 (50.7%, 1.97 - na granicy); rynki dodatkowe (niska pewność, jedno źródło): strzały O24.5 (71.9%), U11.5 rożnych (68.5%), O8.5 rożnych (64.2%), O21.5 fauli (63.6%), U4.5 kartek (63.0%). **Najlepszy rynek meczu: BTTS tak / Over 1.5** (brak mocnego typu na wynik - mecz wyrównany).

---

### 15:00 Manchester United – Bournemouth (Premier League)

**Kluczowe dane**
- Tabela (ESPN): MU 15. (1-4-2, 10:10), Bournemouth 17. (1-3-3, 9:13). MU dominuje w strzałach (19.7 vs 11.0, 6.1 rożnych), ale tylko 1 wygrana w lidze; ostatnie 3 mecze ligowe to remisy 1-1 (FUL, TOT, LEE), w LM porażki 0-2 z Atlético i 1-4 z Como.
- Bournemouth: 0-1 LIV, 1-5 CHE, potem 3-0 Sturm, 2-0 SUN (29 strzałów vs 3), 3-0 AC Milan (LE, czwartek 22.10, dom) - forma rośnie, ale tylko 1 wygrana w lidze.
- Kalendarz: MU grał w środę 21.10 w Como (podróż), BOU w czwartek 22.10 u siebie - podobny odpoczynek (3-4 dni).
- H2H (ESPN): 2-2 (03.2026), 4-4 (12.2025), 4-1 MU (07.2025, sparing), 1-1 (04.2025), 0-3 BOU (12.2024). Ostatnie mecze ligowe bardzo bramkowe i bez wygranej MU od dawna w lidze.
- Sędzia: nieznany (brak w wynikach wyszukiwania) → średnia ze stylu drużyn, pewność kartek obniżona.

**Newsy**
- MU: Carrick pod presją po 1-4 w Como, zapowiada "inny zespół" (ESPN, Last Word on Sports). Wracają Yoro (po zawieszeniu) i Heaven (choroba); Lisandro Martínez i Rashford wątpliwi; część źródeł podaje też Shaw i Mainoo jako kontuzjowanych (NBC Sports, Football Faithful - sprzeczne, niepotwierdzone).
- BOU: wraca Kroupi; Alex Scott i Alex Toth nie zagrają; Evanilson po urazie w środku tygodnia - niepewny (NBC Sports).
- Typy prasowe rozbieżne: 1-1 (jeden serwis), 1-2 (inny) (Sports Mole/Khel Now).

**λ:** MU 1.55, BOU 1.30 (suma 2.85). MU u siebie z przewagą strzałów, ale nieskuteczne i z przeciętną obroną (4.4 celnych przeciw); BOU traci 1.86/mecz, ale u siebie i w pucharach ostatnio szczelny. Korekta: −0.05 dla BOU za Scotta i niepewnego Evanilsona.

**Rynek (DraftKings):** MU 2.30 / X 3.60 / BOU 3.00 → bez marży 41.6% / 26.5% / 31.9%. O2.5 1.65 / U2.5 2.25 → O2.5 57.8%. Model: 43.2% / 24.8% / 32.0%, O2.5 54.2% - w granicach 4 pp od rynku.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 Man United | 43.2% | 2.31 | niska |
| X | 24.8% | 4.03 | niska |
| 2 Bournemouth | 32.0% | 3.13 | niska |
| 1X | 68.0% | 1.47 | średnia |
| X2 | 56.8% | 1.76 | niska |
| 12 | 75.2% | 1.33 | średnia |
| Over 1.5 | 77.7% | 1.29 | średnia |
| Over 2.5 / Under 2.5 | 54.2% / 45.8% | 1.84 / 2.19 | niska |
| Over 3.5 / Under 3.5 | 31.9% / 68.1% | 3.13 / 1.47 | średnia |
| BTTS tak / nie | 57.3% / 42.7% | 1.75 / 2.34 | średnia |
| MU Over 0.5 / 1.5 | 78.8% / 45.9% | 1.27 / 2.18 | średnia / niska |
| BOU Over 0.5 / 1.5 | 72.7% / 37.3% | 1.38 / 2.68 | średnia / niska |
| Rożne (śr. 9.2) O8.5 / U9.5 / U10.5 | 55.3% / 56.4% / 67.2% | 1.81 / 1.77 / 1.49 | niska |
| Kartki żółte (śr. 4.3, sędzia nieznany) O3.5 / U4.5 / U5.5 | 58.8% / 58.0% / 72.2% | 1.70 / 1.72 / 1.39 | niska |
| Faule (śr. 23.0) O21.5 / O22.5 / U24.5 | 60.0% / 52.2% / 62.9% | 1.67 / 1.92 / 1.59 | niska |
| Strzały (śr. 27.7) O24.5 / O26.5 | 69.6% / 56.5% | 1.44 / 1.77 | niska |
| Strzały celne (śr. 9.1) O7.5 / O8.5 | 67.1% / 54.8% | 1.49 / 1.83 | niska |

Najczęstsze wyniki: 1-1 11.7%, 2-1 9.0%, 1-0 9.0%, 1-2 7.6%.

**Ryzyka:** dla MU: (a) remis (24.8%) - 3 remisy 1-1 z rzędu w lidze; (b) wygrana Bournemouth (32.0%) - BOU w formie (3 wygrane do zera z rzędu), MU w kryzysie trenerskim. Korekty kryzysowej nie stosuję do faworyta (zasada skilla), a MU nie jest wyraźnym faworytem. Dla Over/BTTS: BOU nie stracił gola w 3 ostatnich meczach, MU nieskuteczny (realny scenariusz Under 2.5 i BTTS nie). Kontuzje MU niepotwierdzone (Martínez, Rashford, Shaw, Mainoo).

**Typy z p>50% i fair>1.15:** MU Over 0.5 (78.8%, 1.27), Over 1.5 (77.7%, 1.29), 12 (75.2%, 1.33), BOU Over 0.5 (72.7%, 1.38), Under 3.5 (68.1%, 1.47), 1X (68.0%, 1.47), BTTS tak (57.3%, 1.75), X2 (56.8%, 1.76), Over 2.5 (54.2%, 1.84 - rynek 57.8%); rynki dodatkowe (niska pewność): strzały O24.5 (69.6%), U10.5 rożnych (67.2%), O7.5 celnych (67.1%), U24.5 fauli (62.9%), O3.5 kartek (58.8%). **Brak mocnego typu na wynik; najlepsze rynki: Under 3.5 i 1X.**

---

### 15:00 Crystal Palace – Newcastle (Premier League)

**Kluczowe dane**
- Tabela (ESPN): Palace 16. (2-1-4, 9:17), Newcastle 14. (2-2-3, 10:14). Palace oddaje rywalom 17.9 strzału i 6.1 celnych na mecz (najgorsza obrona z trzech analizowanych), sam 10.1 strzału i 3.1 rożnego; Newcastle też dziurawy (17.3 strzału przeciw, 1-4 w Coventry, 1-4 w Leeds, 0-1 z Villą).
- Kalendarz: Palace grał w czwartek 22.10 w Stambule (Beşiktaş 2-2, LE) - długa podróż, 3 dni odpoczynku; wcześniej 0-5 w Brighton i 2-3 w Lyonie. Newcastle bez pucharów, ostatni mecz 17.10 - pełny tydzień odpoczynku (ESPN). Przewaga świeżości dla Newcastle.
- H2H (ESPN): 2-1 CRY (04.2026), 2-0 NEW (01.2026), 5-0 NEW (04.2025), 1-1 (11.2024), 2-0 CRY (04.2024).
- Sędzia: nieznany → średnia stylu drużyn.

**Newsy**
- Palace: trener Pierre Sage pod dużą presją po 0-5 (Yahoo, Dave.sport, Sports Mole). Nie zagrają: Tomiyasu (łydka), Riad (kolano), Timber (udo); Henderson (stopa) niepewny - prawdopodobnie Benítez w bramce; Strand Larsen (uraz) wykluczony wg Sports Mole / mocno wątpliwy wg Football Faithful; wraca Disasi po zawieszeniu.
- Newcastle (trener Matthias Jaissle, 3 porażki w 4 meczach): bez Livramento (kolano) i Jaouena; wątpliwi Fernández-Pardo (choroba), Elanga (udo, nie na 90'), Ramsey; Burn - sprzeczne informacje (Dave vs WhoScored). Przewidywany XI m.in. Hall, Botman, Thiaw, Joelinton, Barnes, Wissa, Osula (Sports Mole).

**λ:** Palace 1.40, Newcastle 1.60 (suma 3.00). Obie obrony słabe w strzałach przeciw; Palace bez Strand Larsena traci jedną opcję w ataku (−0.05), zmęczenie po Stambule podnosi λ Newcastle (+0.05). Korekta kryzysowa (Palace = underdog w kryzysie: trener Sage pod presją, 0-5 w Brighton, 1 wygrana w 5 ostatnich meczach) - przesunięcie ok. 2 pp na korzyść NEW wliczone w λ.

**Rynek (DraftKings):** CRY 2.80 / X 3.65 / NEW 2.40 → bez marży 34.1% / 26.1% / 39.8%. O3.5 2.35 / U3.5 1.59 → U3.5 59.7%. Model: 33.5% / 24.2% / 42.3% (+2.5 pp dla NEW, uzasadnione odpoczynkiem i absencjami Palace).

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 Crystal Palace | 33.5% | 2.98 | niska |
| X | 24.2% | 4.14 | niska |
| 2 Newcastle | 42.3% | 2.36 | niska |
| 1X | 57.7% | 1.73 | niska |
| X2 | 66.5% | 1.50 | średnia |
| 12 | 75.8% | 1.32 | średnia |
| Over 1.5 | 80.1% | 1.25 | średnia |
| Over 2.5 / Under 2.5 | 57.7% / 42.3% | 1.73 / 2.36 | średnia |
| Over 3.5 / Under 3.5 | 35.3% / 64.7% | 2.83 / 1.55 | średnia |
| BTTS tak / nie | 60.1% / 39.9% | 1.66 / 2.51 | średnia |
| Palace Over 0.5 / 1.5 | 75.3% / 40.8% | 1.33 / 2.45 | średnia / niska |
| Newcastle Over 0.5 / 1.5 | 79.8% / 47.5% | 1.25 / 2.11 | średnia / niska |
| Rożne (śr. 9.4) O8.5 / U9.5 / U10.5 | 57.7% / 54.1% / 65.0% | 1.73 / 1.85 / 1.54 | niska |
| Kartki żółte (śr. 3.9, sędzia nieznany) O3.5 / U4.5 / U5.5 | 52.0% / 64.7% / 77.8% | 1.92 / 1.55 / 1.28 | niska |
| Faule (śr. 21.7) O20.5 / U22.5 | 57.9% / 58.0% | 1.73 / 1.72 | niska |
| Strzały (śr. 28.8) O24.5 / O26.5 | 75.7% / 63.6% | 1.32 / 1.57 | niska |
| Strzały celne (śr. 9.3) O7.5 / O8.5 | 69.3% / 57.2% | 1.44 / 1.75 | niska |

Najczęstsze wyniki: 1-1 11.2%, 1-2 8.9%, 0-1 8.0%, 2-1 7.8%.

**Ryzyka:** dla Newcastle (X2/2): (a) remis (24.2%) - obie drużyny bez formy; (b) wygrana Palace (33.5%) - u siebie, Palace wygrało ostatni mecz u siebie (3-1 z Forest) i ostatnie H2H w Selhurst (2-1), efekt "reakcji" po 0-5 i walki trenera o posadę; Newcastle przegrało 3 z 4 i ma problem z golami. Totale: obie obrony słabe → Over, ale Palace bez Strand Larsena i Newcastle z niską skutecznością (3.6 celnych/mecz) → Under 3.5 bliższy rynkowi.

**Typy z p>50% i fair>1.15:** Over 1.5 (80.1%, 1.25), Newcastle Over 0.5 (79.8%, 1.25), 12 (75.8%, 1.32), Palace Over 0.5 (75.3%, 1.33), X2 (66.5%, 1.50), Under 3.5 (64.7%, 1.55), BTTS tak (60.1%, 1.66), Over 2.5 (57.7%, 1.73), 1X (57.7%, 1.73); rynki dodatkowe (niska pewność): strzały O24.5 (75.7%), O7.5 celnych (69.3%), U10.5 rożnych (65.0%), U4.5 kartek (64.7%). **Najlepszy rynek meczu: BTTS tak / Over 1.5; z wyników X2 (pewność średnia, ale bez przewagi nad rynkiem 65.9%).**

---

### Uwagi kalibracyjne (krok "Skalibruj")
- Wszystkie trzy mecze są wyrównane (faworyt 42-45%) → **brak mocnego typu na 1X2**; podwójne szanse i rynki goli są uczciwszym wejściem.
- Model nie schodzi pod rynek o >5 pp w żadnym rynku 1X2/totalu (największa różnica: Newcastle +2.5 pp, MU O2.5 −3.6 pp).
- Korekta kryzysowa zastosowana tylko wobec underdoga (Palace); MU i Liverpool bez obniżek za formę, jedynie za konkretne absencje (Szoboszlai, Ekitiké).
- Rynki dodatkowe: jedno źródło (ESPN boxscore), dwóch sędziów nieznanych, brak potwierdzonych składów → pewność niska, nie na wariant główny kuponu; brak rynków zawodnika (składy niepotwierdzone).
- Kursy z DraftKings (ESPN) to kontrola rynku; kursów Betclic brak.

To oszacowania probabilistyczne, nie gwarancje.

## Analiza: niedziela 25.10.2026, część D (football-analyst)

Źródła: ESPN API (summary: lastFiveGames, standings, seasonseries, leaders, pickcenter DraftKings; boxscore każdego meczu ligowego sezonu 2026/27 z teams/<id>/schedule) oraz WebSearch (12 zapytań). MCP `sportsdata` nie działa. Średnie (strzały, rożne, faule, kartki) policzyłem sam z boxscore'ów ESPN ze wszystkich meczów ligowych sezonu (6-7 na drużynę). Kartki liczone jako żółta = 1, czerwona = 2. **Nigdzie nie znalazłem sędziów** (ESPN `officials` = null, wyszukiwania bez wyniku), więc kartki i faule mają średnią ligową/drużynową i niską pewność. **Nie ma xG**: ESPN go nie podaje, a w wyszukiwaniu nie było danych z sezonu 2026/27. Zastępczo użyłem strzałów i strzałów celnych. Kursy DraftKings (ESPN pickcenter) pokazuję bez marży, jako kontrolę rynku.

---

### 15:00 Hull City – Brentford (Premier League)

**Kluczowe dane (ESPN):**
- Tabela: Hull 11. (7 meczów, 9 pkt, bramki 8-7), Brentford 7. (7 meczów, 10 pkt, 13-8).
- Hull, liga: 1.14 gola strzelonego i 1.00 straconego na mecz, 10.4 strzału (3.4 celnego), rywale oddają 14.6 strzału. Rożne 3.7 wywalczone i 6.7 oddane rywalom, posiadanie 23-35%. Wyniki u siebie: 0-0 z AVL, 2-0 z MUN, 2-2 z EVE. Seria 4 meczów ligowych bez wygranej (D, L, D, L), ostatnio 0-1 z Fulham przy 5 strzałach i 0 celnych. Jakirović nazwał ten mecz najgorszym, odkąd prowadzi zespół (podgląd footballdream/thestatszone).
- Brentford, liga: 1.86 gola strzelonego i 1.14 straconego, 15.0 strzału (4.1 celnego). Rożne 3.9 wywalczone i 5.1 oddane, faule 14.7 na mecz (najwięcej z 6 analizowanych drużyn), kartki 3.14 na mecz. Na wyjeździe: 2-2 z BOU, 1-1 z LEE, 2-2 z AVL (bramki 5-5, rożne w meczach 3, 11, 4).
- Over 2.5 padł w 3/7 meczów Hull i 4/7 meczów Brentford. BTTS: Hull 3/7, Brentford 5/7.

**H2H:** ostatnie mecze z lat 2018-2020 w Championship (np. 1-5 w 02.2020). To historia sprzed lat, więc waga zerowa.

**Newsy:**
- Brentford: w meczu z Liverpoolem (1-2) dostał dwie czerwone kartki (ESPN keyEvents). Yarmoliuk za brutalny faul ma zawieszenie do 08.11. Janelt wyleciał za drugą żółtą i pauzuje do 31.10; to lider drużyny w podaniach (243) i strzelec 2 goli. Wypada więc **dwóch środkowych pomocników**. Furo jest kontuzjowany, Schuster ma kostkę (ok. 75%). Źródło: podgląd FPL z 21.10, przytoczony w wynikach WebSearch (footballdream.in, thestatszone).
- Hull: nie zagrają Matazo, Targett, Ansah, Gyabi i C. Hughes. Butland jest poza grą po operacji łokcia/ramienia. Wszystkie 7 meczów bronił Tzolakis (26 obron), więc to już jest w bazie. W ataku Belloumi (3 gole, 18 strzałów) i McBurnie.
- Brentford gra w środę 28.10 w Carabao Cup z Sunderlandem: w tym meczu rotacja raczej nie grozi. Hull grał ostatnio w sobotę, więc obie drużyny są wypoczęte. Mecz przełożono na niedzielę (brentfordfc.com, Sky).
- Sędzia: nieznany.

**λ:** Hull 1.10, Brentford 1.75 (suma 2.85). Uzasadnienie: atak Hull jest słaby (3.4 celnego strzału na mecz), Brentford strzela 1.67 gola na wyjeździe. Sam model dawał Brentford ok. 50%. Absencje środka pola Brentford obniżyły mu λ tylko lekko, bo rynek (DK) ustawiono już po zawieszeniach.

**Rynek (DraftKings, bez marży):** 1 19.6% / X 23.5% / 2 56.9%; Over 2.5 57.8%. Mój wynik 2 = 52.6%, czyli -4.3 pp względem rynku. To w granicy 5 pp, a uzasadnieniem jest konkretna informacja kadrowa (dwóch zawieszonych pomocników).

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 Hull | 23.8% | 4.20 | średnia |
| X | 23.6% | 4.24 | średnia |
| 2 Brentford | 52.6% | 1.90 | średnia |
| 1X | 47.4% | 2.11 | średnia |
| X2 Brentford lub remis | **76.2%** | 1.31 | średnia |
| 12 | 76.4% | 1.31 | niska |
| DNB Brentford | 68.8% | 1.45 | średnia |
| Over 1.5 | **77.7%** | 1.29 | średnia |
| Over 2.5 / Under 2.5 | 54.2% / 45.8% | 1.84 / 2.19 | niska (rynek: 57.8% Over) |
| Over 3.5 / Under 3.5 | 31.9% / **68.1%** | 3.13 / 1.47 | średnia |
| BTTS tak / nie | 55.1% / 44.9% | 1.81 / 2.23 | niska |
| Hull Over 0.5 gola | 66.7% | 1.50 | niska-średnia |
| Brentford Over 0.5 gola | **82.6%** | 1.21 | średnia |
| Brentford Over 1.5 gola | 52.2% | 1.92 | niska |
| Rożne (średnia 8.5) Over 7.5 / Under 9.5 / Under 10.5 | 59.3% / **64.7%** / 74.6% | 1.69 / 1.55 / 1.34 | niska-średnia (próba 3-4 meczów dom/wyjazd, PL ok. 10, zawężono do średniej) |
| Kartki (średnia 4.4, sędzia nieznany) Over 3.5 / Under 5.5 | 60.4% / 70.7% | 1.65 / 1.41 | niska |
| Faule (średnia 23.5) Over 21.5 | 63.6% | 1.57 | niska |
| Strzały meczowe (26.5) Over 23.5 | 68.8% | 1.45 | niska |

**Ryzyka:**
- Typ na Brentford przegrywa na dwa sposoby, o podobnej wadze. Remis (23.6%): Hull u siebie stracił tylko 2 gole w 3 meczach i nastawia się na obronę. Wygrana Hull (23.8%): Brentford ma osłabiony środek pola bez Janelta i Yarmoliuka, a w 3 meczach wyjazdowych stracił 5 goli.
- Over 1.5 przegrywa przy 0-0 lub 1-0 (Hull zremisował 0-0 z AVL i przegrał 0-1 z FUL).
- Rożne: w meczach Brentford na wyjeździe zdarzyło się 11 rożnych (LEE), a próba jest mała. Rynek rożnych jest nieznany.

**Typy z p>50% i fair>1.15:** X2 76.2% (1.31), Over 1.5 77.7% (1.29), DNB Brentford 68.8% (1.45), Under 3.5 68.1% (1.47), Brentford Over 0.5 gola 82.6% (1.21, granicznie), Under 9.5 rożnych 64.7% (1.55, niska), Kartki Over 3.5 60.4% (1.65, niska), Over 2.5 54.2% (1.84, niska), BTTS tak 55.1% (1.81, niska), 2 Brentford 52.6% (1.90).
**Najlepszy rynek meczu:** X2 albo Over 1.5 (średnia pewność). Typ wynikowy na samo „2” jest blisko 50/50.

---

### 15:00 AS Monaco – Lille (Ligue 1)

**Kluczowe dane (ESPN):**
- Tabela: Lille 3., Monaco 5. Obie drużyny po 7 meczach mają 14 pkt (Monaco bramki 10-6, Lille 10-5).
- Monaco, liga: 1.43 gola strzelonego i 0.86 straconego, 11.7 strzału (4.4 celnego). Rożne 3.7 wywalczone i 5.3 oddane, kartki 2.14 na mecz. U siebie bramki 6-3: 2-0 z OLM, 2-1 z RCL, 2-2 z TOU. Ostatnio przegrało 0-1 w Lorient. W Lidze Konferencji wygrało 2-1 z CSKA i 3-0 z Freiburgiem (czwartek 22.10, czyli **3 dni przerwy**).
- Lille, liga: 1.43 gola strzelonego i 0.71 straconego, 12.3 strzału (5.4 celnego). Rożne 3.3 wywalczone i 4.9 oddane, kartki 1.29 na mecz (bardzo mało). Na wyjeździe stracił tylko 2 gole w 3 meczach. W Lidze Mistrzów: 0-3 z Arsenalem i 2-4 z Galatasarayem (środa 21.10, Lille ma 0 pkt w LM; sudradio/AFP).
- Over 2.5 padł w 3/7 meczów Monaco i 2/7 meczów Lille.

**H2H (ESPN, 2024-2026):** 1-0 dla Monaco, 0-0, 1-2, 0-1, 0-1 (Lille wygrał trzy ostatnie mecze). W 5 meczach padło łącznie 6 goli, Under 2.5 w 4/5.

**Newsy:**
- Lille nie ma Igamane, który według telquel.ma (09.2026) wypadł na całą fazę ligową LM. Pozostałych absencji z października nie znalazłem.
- Monaco: brak aktualnej listy kontuzji (wyszukiwania dały tylko materiały z poprzednich sezonów). Najlepszy strzelec to Brunner (4 gole), asystent Golovin (3).
- Sędzia: nieznany.
- **Braki: newsy kadrowe obu drużyn są niepełne, więc obniżam pewność.** Obie drużyny grały w tygodniu w pucharach, Monaco ma o dzień krótszą przerwę.

**λ:** Monaco 1.40, Lille 1.10 (suma 2.50).

**Rynek (DK, bez marży):** 1 47.9% / X 27.8% / 2 24.3%; Over 2.5 52.0%. Mój wynik 1 = 43.8% (-4.1 pp). Over 2.5 wychodzi mi 45.6%, czyli **6.4 pp poniżej rynku**. Uzasadnienie to forma obu defensyw (straty 0.86 i 0.71 gola na mecz), H2H z Under 2.5 w 4/5 i zmęczenie pucharami. Nie wynika to z korekty kadrowej, ale różnicę z rynkiem i tak zaznaczam: rynek może wiedzieć więcej.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 Monaco | 43.8% | 2.28 | niska-średnia |
| X | 26.6% | 3.75 | niska |
| 2 Lille | 29.6% | 3.38 | niska |
| 1X | **70.4%** | 1.42 | średnia |
| X2 | 56.2% | 1.78 | niska |
| 12 | 73.4% | 1.36 | niska |
| DNB Monaco | 59.7% | 1.68 | niska-średnia |
| Over 1.5 | **71.3%** | 1.40 | średnia |
| Over 2.5 / Under 2.5 | 45.6% / 54.4% | 2.19 / 1.84 | niska (rynek: 52% Over) |
| Under 3.5 | **75.8%** | 1.32 | średnia |
| BTTS tak / nie | 50.3% / 49.7% | 1.99 / 2.01 | brak typu |
| Monaco Over 0.5 gola | 75.3% | 1.33 | średnia |
| Lille Over 0.5 gola | 66.7% | 1.50 | niska-średnia |
| Rożne (średnia 9.0) Over 7.5 / Over 8.5 / Under 10.5 | 65.0% / 53.0% / 69.4% | 1.54 / 1.89 / 1.44 | niska |
| Kartki (średnia 3.6, sędzia nieznany) Over 2.5 / Under 4.5 | 65.5% / 69.7% | 1.53 / 1.43 | niska |
| Faule (średnia 24) Over 21.5 | 67.1% | 1.49 | niska |
| Strzały meczowe (26) Over 23.5 | 65.6% | 1.52 | niska |

**Ryzyka:**
- 1X przegrywa przy wygranej Lille (29.6%): Lille wygrał trzy ostatnie H2H po 1 golu i ma najlepszą defensywę z tej czwórki.
- Typ na Monaco to też ryzyko remisu (26.6%; 0-0 i 1-1 to łącznie ok. 21%).
- Under 3.5 przegrywa przy otwartym meczu po pucharach. Monaco zremisowało 2-2 z TOU, a Lille stracił 4 gole z GAL.
- Rynek wycenia Over 2.5 wyżej niż ja, więc w Under 2.5 nie upatruję value z wysoką pewnością.

**Typy z p>50% i fair>1.15:** Under 3.5 75.8% (1.32), Over 1.5 71.3% (1.40), 1X 70.4% (1.42), DNB Monaco 59.7% (1.68), Under 2.5 54.4% (1.84, niska, sprzeczne z rynkiem), kartki Over 2.5 65.5% (1.53, niska), rożne Over 7.5 65.0% (1.54, niska).
**Najlepszy rynek meczu:** Under 3.5 lub 1X (średnia pewność). 1X2 jest wyrównane, więc brak mocnego typu wynikowego.

---

### 15:30 TSG Hoffenheim – Bayer Leverkusen (Bundesliga)

**Kluczowe dane (ESPN):**
- Tabela: Hoffenheim 14. (6 meczów, 6 pkt, bramki 11-14), Leverkusen 4. (6 meczów, 13 pkt, 16-9).
- Hoffenheim, liga: 1.83 gola strzelonego i 2.33 straconego, 17.8 strzału (5.3 celnego), rożne 6.7 wywalczone i 4.7 oddane. Wszystkie mecze ligowe z ≥3 golami: 2-3 z HSV, 1-3 z SCP, 2-1 z VFB, 2-3 z DOR, 2-3 z KOE, 2-1 z BMG. W Lidze Europy: 2-3 z Besiktasem i **3-0 z Lyonem (czwartek 22.10)**.
- Leverkusen, liga: 2.67 gola strzelonego i 1.50 straconego, 19.7 strzału (6.2 celnego), rożne 7.3 wywalczone i 3.3 oddane. Na wyjeździe bramki 8-8: 2-3 z ELV, 2-2 z FCA, 4-3 z M05. Seria 5 wygranych z rzędu (wliczając LE 4-0 z Lechem i 2-0 z OFI w czwartek 22.10, 33 strzały). Schick: 6 goli i 23 strzały (ESPN leaders).
- Over 2.5 padł w 6/6 meczów Hoffenheim i 4/6 meczów Leverkusen. Over 3.5: Hoffenheim 4/6, Leverkusen 3/6.

**H2H (ESPN):** 1-0 dla Hoffenheim (01.2026), 2-1 dla Hoffenheim na wyjeździe (08.2025), wygrane B04 3-1 (02.2025), 4-1 (09.2024) i 2-1. Hoffenheim wygrał dwa ostatnie mecze.

**Newsy:**
- Brak aktualnej listy kontuzji obu drużyn. Wyszukiwania dały tylko stare materiały: Flekken i Tella z sezonu 2025/26, Hlozek i Machida ze stycznia 2026. Nie przenoszę ich na ten mecz.
- Obie drużyny grały w czwartek w LE, więc mają równe 3 dni przerwy. Daghim, Conté i Hlozek mają po 2 gole.
- Sędzia: nieznany. **Pewność obniżona za brak newsów.**

**λ:** Hoffenheim 1.60, Leverkusen 2.05 (suma 3.65).

**Rynek (DK, bez marży):** 1 31.7% / X 23.3% / 2 44.9%; linia 3.5 z Over 54.1%. Mój wynik 2 = 48.4% (+3.5 pp), Over 3.5 = 49.5% (-4.6 pp). W granicy 5 pp.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 Hoffenheim | 30.4% | 3.29 | niska |
| X | 21.3% | 4.70 | niska |
| 2 Leverkusen | 48.4% | 2.07 | niska-średnia |
| 1X | 51.6% | 1.94 | niska |
| X2 | **69.6%** | 1.44 | średnia |
| 12 | 78.7% | 1.27 | średnia |
| DNB Leverkusen | 61.4% | 1.63 | średnia |
| Over 1.5 | 87.9% | 1.14 | poniżej progu 1.15 |
| Over 2.5 | **70.6%** | 1.42 | średnia-wysoka (Hoffenheim 6/6, rynek ~zgodny) |
| Over 3.5 / Under 3.5 | 49.5% / 50.5% | 2.02 / 1.98 | brak typu |
| BTTS tak | **69.5%** | 1.44 | średnia |
| Hoffenheim Over 0.5 gola | 79.8% | 1.25 | średnia |
| Hoffenheim Over 1.5 gola | 47.5% | 2.11 | niska |
| Leverkusen Over 0.5 gola | 87.1% | 1.15 | granicznie (≤1.15, pominąć) |
| Leverkusen Over 1.5 gola | **60.7%** | 1.65 | średnia |
| Rożne (średnia 10.5) Over 8.5 / Over 9.5 | 69.3% / 58.4% | 1.44 / 1.71 | niska-średnia |
| Kartki (średnia 3.7, sędzia nieznany) Over 2.5 / Under 4.5 | 67.1% / 68.1% | 1.49 / 1.47 | niska |
| Faule (średnia 24) Over 21.5 | 67.1% | 1.49 | niska |
| Strzały meczowe (30) Over 27.5 | 64.6% | 1.55 | niska |

**Ryzyka:**
- X2 przegrywa przy wygranej Hoffenheim (30.4%): TSG wygrał dwa ostatnie H2H i w czwartek rozbił Lyon 3-0.
- Leverkusen „2” przegrywa przy remisie (21.3%) albo przy porażce (30.4%), bo w tym sezonie traci 2.67 gola na mecz na wyjeździe.
- Over 2.5 i BTTS przegrywają w meczu zamkniętym po czwartkowym wysiłku obu drużyn. H2H 1-0 ze stycznia 2026 pokazuje, że taki scenariusz jest możliwy.
- Brak newsów kadrowych: nieobecność Schicka lub bramkarza zmieniłaby liczby.

**Typy z p>50% i fair>1.15:** Over 2.5 70.6% (1.42), BTTS tak 69.5% (1.44), X2 69.6% (1.44), DNB Leverkusen 61.4% (1.63), Leverkusen Over 1.5 gola 60.7% (1.65), Hoffenheim Over 0.5 gola 79.8% (1.25), 12 78.7% (1.27), rożne Over 8.5 69.3% (1.44, niska-średnia), kartki Over 2.5 67.1% (1.49, niska), 1X 51.6% (1.94, niska).
**Najlepszy rynek meczu:** Over 2.5 / BTTS tak.

---

## Kandydaci na kupon (dla bet-slip-builder)

| Mecz | Rynek | p | fair | pewność | zależy od | kurs rynkowy |
|---|---|---|---|---|---|---|
| Hoffenheim – Leverkusen | Over 2.5 | 70.6% | 1.42 | średnia-wysoka | składy (brak newsów) | DK: linia 3.5 (Over 3.5 -135); O2.5 nieznany |
| Hoffenheim – Leverkusen | BTTS tak | 69.5% | 1.44 | średnia | składy | nieznany |
| Hull – Brentford | X2 | 76.2% | 1.31 | średnia | potwierdzenie zawieszeń Brentford | DK 2: 1.69 |
| Hull – Brentford | Over 1.5 | 77.7% | 1.29 | średnia | – | nieznany (DK O2.5 1.645) |
| Monaco – Lille | Under 3.5 | 75.8% | 1.32 | średnia | – | nieznany |
| Monaco – Lille | 1X | 70.4% | 1.42 | średnia | składy (brak newsów) | DK 1: 2.00, X: 3.45 |
| Hoffenheim – Leverkusen | X2 | 69.6% | 1.44 | średnia | składy | DK 2: 2.05 |
| Monaco – Lille | Over 1.5 | 71.3% | 1.40 | średnia | – | nieznany |
| Hull – Brentford | Under 3.5 | 68.1% | 1.47 | średnia | – | nieznany |
| Hull – Brentford | DNB Brentford | 68.8% | 1.45 | średnia | zawieszenia | nieznany |

Typy rożnych, kartek i fauli mają niską pewność: sędziowie są nieznani, a średnie pochodzą z 6-7 meczów z jednego źródła (ESPN). Nie rekomenduję ich do wariantu głównego.

Sprzeczności do uniknięcia w jednym kuponie: Monaco Under 2.5 z Over 2.5 tego meczu. Hull–Brentford Over 2.5 łączyć z Under 3.5 tylko świadomie (wtedy typem jest „dokładnie 3 gole”).

To są oszacowania probabilistyczne, nie gwarancje.

## Analizy piłkarskie, niedziela 25.10.2026 (część E): La Liga + Ligue 1

Skill: `football-analyst`, wywołany osobno dla każdego meczu. Skrypty: `poisson.py`, `markets.py`.

**Źródła i ograniczenia (dotyczą wszystkich trzech meczów):**
- ESPN API: `summary` (lastFiveGames, seasonseries/H2H, pickcenter DraftKings, leaders, news), `standings`, `teams/<id>/schedule` oraz boxscore'y wszystkich rozegranych w tym sezonie meczów ligowych sześciu drużyn (Celta i Betis po 9, francuskie drużyny po 7). Z boxscore'ów: strzały, celne, rożne, faule, żółte i czerwone kartki. Z `rosters` meczów pucharowych z 21-22.10: wyjściowe XI, czyli realna rotacja.
- Z ESPN nie ma xG. WebSearch (9 zapytań) nie znalazł żadnych zapowiedzi, przewidywanych składów, list kontuzji ani obsady sędziowskiej na 25.10.2026, bo wyniki dotyczyły wcześniejszych sezonów. Dla wszystkich trzech meczów **sędzia jest nieznany**, a **składy niepotwierdzone**. Kartki i faule liczę więc ze średnich drużyn z ESPN (jedno źródło), z niską pewnością. To nie są typy na kupon.
- Kartki liczone jako liczba (żółta = 1, czerwona = 2). Średnie ESPN dotyczą żółtych, a czerwone dodaję według ich częstości.
- Kursy DraftKings (ESPN pickcenter) służą jako kontrola rynku, po usunięciu marży metodą proporcjonalną.
- Średnia ligowa z tabel ESPN: La Liga 1,52 gola na drużynę na mecz (286 goli w 188 meczach drużyn), Ligue 1 1,52 (198 goli w 130).

---

### 16:15 Celta Vigo – Real Betis (La Liga, 10. kolejka, Balaídos)

**Kluczowe dane (ESPN):**
- Tabela: Celta 9. miejsce (9 meczów, 2-5-2, bramki 10:7, 11 pkt), Betis 4. miejsce (9 meczów, 6-1-2, bramki 16:14, 19 pkt).
- Celta u siebie (5 meczów): gole 1,80:1,20 (z czego 5-0 z Racingiem), strzały 9,6 vs 14,6 rywala, rożne 2,6 vs 4,4. Ogólnie 9,4 strzału, 3,2 celnego i 2,8 rożnego na mecz, więc atak jest bardzo słaby wolumenowo. Obrona mocna: 4 czyste konta w 9 meczach, na wyjeździe tylko 0,25 straconego gola na mecz.
- Ostatnie mecze Celty: 0-0 w Elche, 2-1 z Alavés (6 strzałów Celty przy 20 Alavés), w Lidze Europy 1-2 z Juventusem i 2-1 na Celtic Park w czwartek 22.10.
- Betis na wyjeździe (4 mecze): gole 1,50:1,75, strzały 18,0 vs 18,2, rożne 4,8 vs 8,0. Ogólnie 16,4 strzału i 6,3 celnego na mecz. Ostatnio 5-2 z Osasuną, 2-5 z Barceloną, a w Lidze Mistrzów 3-2 z Porto i 1-0 z Feyenoordem (środa 21.10).
- Over 2.5 padło w 4/9 meczów Celty i 4/9 meczów Betisu. BTTS: 4/9 u Celty, 5/9 u Betisu.
- Kartki (żółte, obie drużyny łącznie): mecze Celty średnio 3,8, mecze Betisu 4,1. Faule: Celta 12,2 vs 14,4 rywala, Betis 9,9 vs 11,7.
- H2H (ESPN, 5 meczów od 2024): 1-1, 1-1, 3-2 dla Celty, 2-2, 2-1 dla Betisu. BTTS 5/5, Over 2.5 3/5. Zdecydowanie remisowe i bramkowe.

**Newsy / skład:**
- Facundo Bernal (Betis) dostał czerwoną kartkę za brutalne zachowanie 17.10 z Barceloną (ESPN keyEvents). W lidze najpewniej jest zawieszony, choć długość kary nie została potwierdzona.
- Betis mocno rotował z Feyenoordem: grali Natan, Bartra, Isco, Roca, Parrott, Antony, a odpoczywali Lo Celso, Cucho, Ceballos, Llorente i V. Gómez. Podstawowa jedenastka jest więc świeża.
- Celta grała w czwartek w Glasgow, czyli ma o dzień krócej na regenerację i za sobą podróż. Rotowała częściowo: Aspas, Febas, Rueda i M. Alonso grali w LE, a Moriba, Swedberg, Driouech i Lago w lidze.
- Z Celtic grał Miguel Román (asysty w lidze, lider ESPN). O kontuzjach z bieżącego tygodnia brak danych w sieci (Comuniate wspomina Llorente i Ruibala we wrześniu, ale to nieaktualne).

**λ:** Celta 1,20, Betis 1,40, łącznie 2,60.
- Wyliczenie: atak Celty 0,73 × obrona Betisu 1,03 × 1,65 (gospodarze) ≈ 1,24, a po zmęczeniu po czwartku 1,20. Atak Betisu 1,17 × obrona Celty (0,51 surowo, zbiegnięte do 0,75, bo Celta oddaje rywalom 13,3 strzału na mecz) × 1,40 (goście) ≈ 1,23. Do tego +0,17 za świeży skład podstawowy Betisu i H2H 5/5 BTTS, a −Bernal neutralnie.
- Rynek DK: 1 +220, X +255, 2 +125, czyli bez marży 30,1% / 27,1% / 42,8%. O/U 2.5: −135/+110, czyli Over 54,7%. Model daje 1X2 w granicach 2 pp od rynku. Over 2.5 z modelu wynosi 48,2%, a z formy obu drużyn 44%. Kalibruję do 50%, czyli nie schodzę >5 pp pod rynek.

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 Celta | 32,2% | 3.11 | średnia |
| X | 26,2% | 3.81 | średnia |
| 2 Betis | 41,6% | 2.41 | średnia |
| 1X | 58,4% | 1.71 | średnia |
| X2 | 67,8% | 1.47 | średnia |
| 12 | 73,8% | 1.36 | niska |
| DNB Betis | 56,4% | 1.77 | niska-średnia |
| Over 1.5 | 73,3% | 1.36 | średnia |
| Over 2.5 / Under 2.5 (po kalibracji) | 50% / 50% | 2.00 / 2.00 | niska (brak typu) |
| Over 3.5 / Under 3.5 | 26,4% / 73,6% | 3.79 / 1.36 | średnia |
| BTTS tak / nie (po korekcie formy, H2H 5/5) | 52% / 48% | 1.92 / 2.08 | niska |
| Celta Over 0.5 gola | 69,9% | 1.43 | średnia |
| Betis Over 0.5 gola | 75,3% | 1.33 | średnia |
| Betis Over 1.5 gola | 40,8% | 2.45 | niska |
| Rożne (śr. 9,0): Over 8.5 / Under 9.5 / Under 10.5 | 53,0% / 58,8% / 69,4% | 1.89 / 1.70 / 1.44 | niska |
| Kartki (śr. 4,4, sędzia nieznany): Over 3.5 / Under 4.5 / Under 5.5 | 60,4% / 56,3% / 70,7% | 1.65 / 1.78 / 1.41 | niska |
| Faule (śr. 24): Over 22.5 / Under 24.5 | 59,8% / 55,4% | 1.67 / 1.80 | niska |
| Strzały (śr. 26): Over 23.5 | 65,6% | 1.52 | niska |
| Celne (śr. 9,7): Over 8.5 | 61,8% | 1.62 | niska |

- Najczęstsze wyniki: 1-1 (12,5%), 0-1 (10,4%), 1-0 (8,9%).
- Rożne: Celta ok. 4,4 (najsłabsza produkcja rożnych, ale Betis na wyjeździe oddaje 8,0 na mecz), Betis ok. 4,6.

**Ryzyka:**
- Betis jako lekki faworyt: remis jest bardzo prawdopodobny (H2H 3 remisy w 5 meczach, 1-1 to najczęstszy wynik), a Celta wygrywa u siebie (obrona 4 czyste konta, Betis traci 1,75 gola na wyjeździe).
- Zmęczenie Celty działa w obie strony. Brak Bernala osłabia środek pola Betisu.

**Typy z p > 50% i fair > 1.15:**
- X2 67,8% (1.47, średnia).
- Over 1.5 73,3% (1.36, średnia).
- Under 3.5 73,6% (1.36, średnia).
- Betis Over 0.5 75,3% (1.33) i Celta Over 0.5 69,9% (1.43).
- 1X 58,4% (1.71).
- DNB Betis 56,4% (1.77).
- Kandydaci z rynków dodatkowych, wyłącznie z niską pewnością i bez rekomendacji na kupon (jedno źródło, sędzia nieznany): strzały Over 23.5 65,6%, celne Over 8.5 61,8%, kartki Over 3.5 60,4%, faule Over 22.5 59,8%, rożne Under 9.5 58,8%.
- Mecz wyrównany, **brak mocnego typu na wynik**. Najlepszy rynek: X2 albo Under 3.5.

---

### 17:15 Olympique Marseille – Le Havre (Ligue 1, Stade Vélodrome)

**Kluczowe dane (ESPN):**
- Tabela: OM 10. miejsce (7 meczów, 3-0-4, bramki 14:10, 9 pkt), Le Havre 18., czyli ostatnie (7 meczów, 0-2-5, bramki 5:11, 2 pkt, **bez wygranej w sezonie**, 3 porażki z rzędu: 2-3 w Tuluzie, 0-1 w Lille, 1-3 z Auxerre).
- OM u siebie: 4-0 ze Strasbourgiem, 2-3 z Paris FC, 1-2 z PSG, czyli gole 2,33:1,67. Ogólnie 13,1 strzału, 4,9 celnego, 4,4 rożnego, rywale 15,9 strzału i 4,4 rożnego. Ostatnio w lidze 2-0 w Troyes i 5-2 w Angers. W Lidze Europy porażki 0-1 z Olympiakosem i 0-1 w Grazu (22.10).
- Le Havre: 15,7 strzału, ale tylko 4,7 celnego i 0,71 gola na mecz. Traci 1,57 gola, wykonuje 5,7 rożnego i oddaje rywalom 4,9. Popełnia dużo fauli: 14,6 na mecz (rywale 15,1).
- Over 2.5: 4/7 w meczach OM, 3/7 w meczach HAC. BTTS: 3/7 OM, 4/7 HAC. Kartki łącznie: mecze OM 3,4 żółtej, HAC 3,2, a OM ma 0,29 czerwonej na mecz.
- H2H (ESPN): OM wygrał 5 ostatnich meczów (2-1, 5-1, 3-1, 6-2, 1-0). Le Havre zdobył gola w 4 z nich.

**Newsy / skład:**
- OM w Grazu wystawił niemal całkowicie rezerwowy skład: Aguerd, Meïté, U. Garcia, Bezahaf, A. Gomes, Maupay, Abdallah (ESPN rosters). Podstawowi z Angers odpoczywali: Gouiri (5 goli w lidze), Paixão, Harit, Weah, Emerson, Egan-Riley, Abdelli, Nnadi. Spodziewam się świeżej pierwszej jedenastki, a jedynym obciążeniem jest czwartkowa podróż sztabu.
- Le Havre (Digard, kontrakt przedłużony w 06.2026 według sports.orange.fr) nie gra w pucharach i ma pełny tydzień. Seko dostał czerwoną kartkę 10.10 w Lille, a z Auxerre już nie grał, więc kara jest odbyta.
- Kontuzji z bieżącego tygodnia w sieci nie znaleziono, więc pewność jest obniżona.

**λ:** OM 2,05, HAC 0,95, łącznie 3,00.
- Surowo: 1,32 × 1,03 × 1,65 ≈ 2,24 dla OM, a dla HAC (atak 0,47 zbiegnięty do 0,6, bo 15,7 strzału na mecz) × 0,94 × 1,40 ≈ 0,80.
- Model surowy (2,2/0,9) daje OM 67,0%. **Krok "Skalibruj":** Le Havre jest underdogiem w kryzysie (0 wygranych, ostatnie miejsce, desperacja), więc odejmuję ok. 4 pp. λ 2,05/0,95 daje 62,8% przy rynku 63,6%, czyli w granicy ±5 pp.
- Rynek DK: 1 −200, X +380, 2 +475, czyli bez marży 63,6% / 19,8% / 16,6%. O/U 3.5: +125/−155, czyli Over 3.5 42,2%. Model daje 35,3%, a forma (średnio 2,9 gola w meczach obu drużyn) wspiera model. Kalibruję do Over 3.5 38% / Under 3.5 62%, bo rynek bywa trafniejszy przy dużej różnicy klas.

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 OM | 62,8% | 1.59 | średnia |
| X | 20,6% | 4.87 | średnia |
| 2 Le Havre | 16,6% | 6.01 | średnia |
| 1X | 83,4% | 1.20 (graniczne 1.15-1.20) | średnia |
| 12 | 79,4% | 1.26 | średnia |
| X2 | 37,2% | 2.69 | średnia |
| DNB OM | 79,1% | 1.26 | średnia |
| Over 1.5 | 80,1% | 1.25 | średnia |
| Over 2.5 (kalibr.) | 59% | 1.69 | średnia-niska |
| Under 3.5 (kalibr.) | 62% | 1.61 | niska-średnia |
| BTTS tak / nie (po korekcie formy) | 50% / 50% | 2.00 | niska (brak typu) |
| OM Over 1.5 gola | 60,7% | 1.65 | średnia |
| OM Over 0.5 gola | 87,1% | 1.15 (odpada) | – |
| Le Havre Over 0.5 gola | 61,3% | 1.63 | niska-średnia |
| Rożne (śr. 9,7): Over 8.5 / Over 9.5 / Under 10.5 | 61,0% / 49,4% / 61,7% | 1.64 / 2.02 / 1.62 | niska |
| Kartki (śr. 3,8, sędzia nieznany): Over 2.5 / Under 4.5 | 68,7% / 66,4% | 1.46 / 1.51 | niska |
| Faule (śr. 25,5): Over 23.5 | 63,1% | 1.58 | niska |
| Strzały (śr. 27): Over 24.5 | 65,4% | 1.53 | niska |
| Celne (śr. 9,9): Over 8.5 | 64,1% | 1.56 | niska |

- Najczęstsze wyniki: 2-0, 1-0, 2-1, 1-1.
- Rożne: OM ok. 5,2 (dominacja), HAC ok. 4,5. Le Havre wykonuje dużo rożnych, więc linie Under na rożne są ryzykowne.

**Ryzyka:**
- OM jako faworyt: remis (20,6%), gdyby OM zwolnił po dwóch porażkach w LE i podróży z Austrii. Wygrana Le Havre (16,6%) przy desperacji ostatniej drużyny, 15,7 strzału na mecz i stałych fragmentach.
- OM w tym sezonie przegrał 2 z 3 meczów domowych (z PSG i Paris FC, czyli z silniejszymi rywalami niż HAC).
- Under 3.5 przegrywa przy scenariuszu 5-2 z Angers. Mecze OM średnio dają 3,43 gola.

**Typy z p > 50% i fair > 1.15:**
- Wynik i bramki: 1X 83,4% (1.20, graniczne), 12 79,4% (1.26), DNB OM 79,1% (1.26), Over 1.5 80,1% (1.25), OM wygra 62,8% (1.59), OM Over 1.5 gola 60,7% (1.65), Under 3.5 62% (1.61), Over 2.5 59% (1.69), Le Havre Over 0.5 61,3% (1.63).
- Kandydaci z rynków dodatkowych, wyłącznie z niską pewnością i bez rekomendacji na kupon (jedno źródło, sędzia nieznany): kartki Over 2.5 68,7%, strzały Over 24.5 65,4%, celne Over 8.5 64,1%, faule Over 23.5 63,1%, rożne Over 8.5 61%.
- **Najlepszy rynek meczu:** zwycięstwo OM / DNB OM (zgodne z rynkiem, świeży podstawowy skład).

---

### 17:15 Stade Rennais – Strasbourg (Ligue 1, Roazhon Park)

**Kluczowe dane (ESPN):**
- Tabela: Rennes 7. miejsce (7 meczów, 4-1-2, bramki 15:14, 13 pkt), Strasbourg 14. (7 meczów, 2-1-4, bramki 12:15, 7 pkt, **4 porażki ligowe z rzędu**: 1-2 z Paris FC, 1-2 w Nicei, 1-3 z PSG, wcześniej 1-1 z Monaco).
- Rennes u siebie: 2-2 z PSG, 3-2 z Le Mans, 1-0 z OM, 4-1 z Auxerre, czyli gole 2,50:1,25, strzały 18,0 vs 14,0, rożne 5,8 vs 6,5. Ostatnio 3-4 w Paris FC, a w LE 2-1 z OFI i 2-2 w Turynie z Juventusem (czwartek 22.10).
- Strasbourg na wyjeździe: gole 2,00:2,50 (w tym 6-2 w Troyes). Ogólnie 12,1 strzału vs 16,6 rywala, tylko 2,1 rożnego na mecz vs 5,4 rywala.
- Over 2.5: **6/7 w meczach Rennes i 6/7 w meczach Strasbourga**. BTTS: 5/7 Rennes, 6/7 Strasbourg. Obie drużyny tracą gola w 6/7 meczów.
- Kartki łącznie: mecze Rennes 4,7 żółtej (Rennes 2,4 na mecz), Strasbourg 2,9. Faule: Rennes 13,4, rywale Strasbourga tylko 8,4.
- Lepaul (Rennes) ma 7 goli w 7 meczach, Yassine i Reyna (Strasbourg) po 2.
- H2H (ESPN): 3-0, 4-1 i 1-0 dla Rennes (trzy ostatnie), wcześniej 3-1 i 2-0 dla Strasbourga.

**Newsy / skład:**
- Rennes w Turynie zagrał rotowanym składem: Aït Boudlal, Nagida, Rongier, Camara, Al-Tamari, Dia (ESPN rosters). Lepaul, Blas, Szymanski, Frankowski, Cissé i Soumaré nie zaczynali, więc podstawowy skład z ligi jest relatywnie świeży, ale klub ma za sobą podróż z Włoch w czwartek wieczorem.
- Strasbourg nie gra w pucharach i ma pełny tydzień odpoczynku.
- Brak doniesień o kontuzjach i zmianie trenera z bieżącego tygodnia (WebSearch dawał tylko materiały z 2025), więc pewność jest obniżona.

**λ:** Rennes 1,95, Strasbourg 1,35, łącznie 3,30.
- Surowo: 1,41 × 1,41 × 1,65 ≈ 3,3 dla Rennes, a po zbiegnięciu do średniej (mała próba) ok. 2,0, minus −0,05 za podróż z Turynu. Strasbourg: 1,12 × 1,32 × 1,40, po zbiegnięciu 1,35.
- Seria porażek Strasbourga nie daje korekty kryzysowej: to nie jest przepaść klas, a Strasbourg nie zmienił trenera według dostępnych danych.
- Rynek DK: 1 −125, X +330, 2 +290, czyli bez marży 53,2% / 22,3% / 24,5%. O/U 3.5: +105/−135, czyli Over 3.5 45,9%. Model daje 51,5% / 22,0% / 26,5% oraz Over 3.5 42,0%, czyli zgodnie z rynkiem.
- Over 2.5 i BTTS podnoszę o ok. 2 pp z modelu ze względu na formę (6/7 Over i ≥ 60% meczów ze straconym golem po obu stronach).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 Rennes | 51,5% | 1.94 | średnia |
| X | 22,0% | 4.55 | średnia |
| 2 Strasbourg | 26,5% | 3.77 | średnia |
| 1X | 73,5% | 1.36 | średnia |
| X2 | 48,5% | 2.06 | średnia |
| 12 | 78,0% | 1.28 | średnia |
| DNB Rennes | 66,0% | 1.52 | średnia |
| Over 1.5 | 84,1% | 1.19 (graniczne) | średnia-wysoka |
| Over 2.5 (kalibr.) | 66% | 1.52 | średnia |
| Over 3.5 / Under 3.5 | 42,0% / 58,0% | 2.38 / 1.72 | niska |
| BTTS tak (kalibr.) | 66% | 1.52 | średnia |
| Rennes Over 0.5 gola | 85,8% | 1.17 (graniczne) | średnia |
| Rennes Over 1.5 gola | 58,0% | 1.72 | średnia-niska |
| Strasbourg Over 0.5 gola | 74,1% | 1.35 | średnia |
| Strasbourg Over 1.5 gola | 39,1% | 2.56 | niska |
| Rożne (śr. 9,0): Over 8.5 / Under 9.5 / Under 10.5 | 53,0% / 58,8% / 69,4% | 1.89 / 1.70 / 1.44 | niska |
| Kartki (śr. 4,0, sędzia nieznany): Over 3.5 / Under 4.5 | 53,8% / 63,0% | 1.86 / 1.59 | niska |
| Faule (śr. 22,5): Over 21.5 / Under 23.5 | 56,2% / 59,4% | 1.78 / 1.68 | niska |
| Strzały (śr. 29): Over 26.5 | 64,8% | 1.54 | niska |
| Celne (śr. 11): Over 9.5 | 64,4% | 1.55 | niska |

- Najczęstsze wyniki: 1-1 (9,7%), 2-1 (9,5%), 1-0, 2-0.
- Rożne: Rennes ok. 5,3, Strasbourg ok. 3,7 (tylko 2,1 rożnego na mecz w sezonie).

**Ryzyka:**
- Rennes jako faworyt: remis (22%), np. 2-2 jak z PSG, gdy Rennes słabnie po czwartku w Turynie. Wygrana Strasbourga (26,5%): wypoczęty Strasbourg z 2,0 gola na mecz na wyjeździe, a Rennes stracił 3,0 gola na mecz na wyjeździe i 4 gole w Paris FC.
- Over 2.5 i BTTS przegrywają przy meczu "zamkniętym" 1-0, jak trzy z ostatnich H2H (1-0, 3-0, 2-0 bez BTTS).

**Typy z p > 50% i fair > 1.15:**
- Wynik i bramki: Over 1.5 84,1% (1.19, graniczne), Rennes Over 0.5 85,8% (1.17, graniczne), 12 78,0% (1.28), Strasbourg Over 0.5 74,1% (1.35), 1X 73,5% (1.36), Over 2.5 66% (1.52), BTTS tak 66% (1.52), DNB Rennes 66,0% (1.52), Rennes Over 1.5 gola 58,0% (1.72), Under 3.5 58,0% (1.72), Rennes wygra 51,5% (1.94).
- Kandydaci z rynków dodatkowych, wyłącznie z niską pewnością i bez rekomendacji na kupon (jedno źródło, sędzia nieznany): strzały Over 26.5 64,8%, celne Over 9.5 64,4%, kartki Under 4.5 63,0%, faule Under 23.5 59,4%, rożne Under 9.5 58,8%.
- **Najlepszy rynek meczu:** Over 2.5 / BTTS tak (forma 6/7 po obu stronach, zgodne z wysokim totalem rynku). Wynik 1 jest bliski 50%, więc brak mocnego typu na zwycięzcę.

---

## Tabela kandydatów (wejście dla bet-slip-builder)

| Mecz | Rynek | p | Fair | Pewność | Zależy od | Kurs rynkowy |
|---|---|---|---|---|---|---|
| OM – Le Havre | DNB OM | 79,1% | 1.26 | średnia | skład OM (świeży po rotacji) | brak (DK tylko 1X2) |
| OM – Le Havre | OM wygra | 62,8% | 1.59 | średnia | jw. | DK −200 (1.50) |
| OM – Le Havre | Over 1.5 | 80,1% | 1.25 | średnia | – | brak |
| OM – Le Havre | OM Over 1.5 gola | 60,7% | 1.65 | średnia | Gouiri w składzie | brak |
| OM – Le Havre | Under 3.5 | 62% | 1.61 | niska-średnia | rynek wyżej na Over | DK −155 (1.65) |
| Rennes – Strasbourg | Over 2.5 | 66% | 1.52 | średnia | – | brak (DK tylko 3.5) |
| Rennes – Strasbourg | BTTS tak | 66% | 1.52 | średnia | – | brak |
| Rennes – Strasbourg | DNB Rennes | 66,0% | 1.52 | średnia | skład po Turynie | brak |
| Rennes – Strasbourg | 1X | 73,5% | 1.36 | średnia | – | brak |
| Rennes – Strasbourg | Strasbourg Over 0.5 | 74,1% | 1.35 | średnia | – | brak |
| Celta – Betis | X2 | 67,8% | 1.47 | średnia | skład Betisu (Bernal zawieszony?) | brak (DK 2 +125) |
| Celta – Betis | Under 3.5 | 73,6% | 1.36 | średnia | – | brak |
| Celta – Betis | Over 1.5 | 73,3% | 1.36 | średnia | – | brak |

Rynki dodatkowe (rożne, kartki, faule, strzały) zostały wycenione dla wszystkich meczów, ale z niską pewnością (jedno źródło ESPN, sędziowie nieznani). Nie powinny trafiać do głównych wariantów kuponów.

To oszacowania probabilistyczne oparte na niepełnych danych (brak xG, składów i sędziów), a nie gwarancje.

## Ligue 1, niedziela 25.10.2026 (17:15 CET) - analizy football-analyst

Skill `football-analyst` wywołany osobno dla każdego meczu. Godzina z ESPN: 2026-10-25T16:15Z, czyli 17:15 CET (zmiana czasu tego dnia). Uwaga: część serwisów (Sports Mole, Kickoff, Starting11, Rotowire) podaje 24.10. Obowiązuje ESPN, ale przed meczem warto potwierdzić termin.

**Źródła i ograniczenia (wspólne):**
- ESPN API (`fra.1` summary/schedule): wyniki, tabela, boxscore każdego meczu ligowego 2026/27, czyli 7 meczów na drużynę (strzały, celne, rożne, faule, kartki, posiadanie), H2H, kursy DraftKings (pickcenter).
- WebSearch (11 zapytań). Strony z zapowiedziami (Sports Mole, Stats Zone) zablokowane przez proxy (403/ENOTFOUND), więc mam z nich tylko streszczenia wyników wyszukiwania.
- **Brak xG**: jako proxy służą strzały i celne z ESPN.
- **Sędziowie nieznani**: nie znalazłem obsady 9. kolejki (ligue1.com nie odpowiada), więc kartki i faule liczę ze średnich drużyn i ligi. Pewność tych rynków jest najwyżej niska-średnia.
- **Składy niepotwierdzone**: rynków zawodnika nie wyceniam.
- Średnie z próbki 36 meczów ESPN z udziałem tych 6 drużyn: gole 3,19, rożne 10,2, kartki 3,4 (żółta = 1, czerwona = 1, liczone wg ESPN; u bukmacherów czerwona często liczy się za 2), faule 25,4.
- Kursy DK po usunięciu marży (proporcjonalnie) służą jako kontrola rynku.

---

### 17:15 AJ Auxerre – Le Mans (Ligue 1)

**Kluczowe dane (ESPN):**
- Tabela: Auxerre 13. (9 pkt, 3-0-4, bilans bramek -6), Le Mans 16. (6 pkt, 1-3-3, -5, beniaminek).
- Auxerre: w 7 meczach śr. 1,57 gola strzelonego i 2,43 straconego. Strzały 12,1 do 14,9, celne 5,1 do 6,4, rożne 5,6 do 7,6, faule 15,1. U siebie (3 mecze): 1-0 z Nice, 2-1 z Brest, 1-3 z Angers. Gole 1,33:1,33, strzały 14,0:11,7, rożne 6,0:7,0. Ostatnio 3-1 w Le Havre i 1-4 w Rennes.
- Le Mans: śr. 1,43 gola strzelonego i 2,14 straconego. Strzały 10,6 do 16,6, rożne tylko 2,7 do 5,9, faule 14,9, kartki 2,57 na mecz (najwięcej z tych 6 drużyn). Na wyjeździe: 1-1 w Nice, 2-3 w Rennes, 1-3 w PSG. Trzy porażki z rzędu (ostatnio 0-3 u siebie z Toulouse), 1 wygrana w 7 meczach.
- Mecze obu drużyn są bramkowe: średnio 4,0 gola w meczach Auxerre i 3,57 w meczach Le Mans.
- Strzelcy (ESPN): Archer 4 gole w 5 meczach, Namaso 3 (AUX); Mafouta 4, Bourabaa 3 (LM).

**H2H (ESPN):** ostatnie mecze w latach 2010-2020, głównie w Ligue 2 (AUX 1-0, 2-0; 1-1; 1-3; 2-1). Za stare, waga zerowa.

**Newsy:** Stats Zone (streszczenie z wyszukiwania): Auxerre pod wodzą Willa Stilla po słabym starcie wygrało 3 z 4 ostatnich meczów, w Le Havre dublet zdobył Danny Loader. Trener Le Mans to Patrick Videira (Kickoff). Nie znalazłem raportu kontuzji ani przewidywanych składów (Rotowire: "lineup not reported"). Modele zewnętrzne: Kickoff 44/24/32, Sportiko 49/28/24.

**Rynek (DraftKings, ESPN):** 1 = 2.10, X = 3.60, 2 = 3.40, czyli bez marży 45,4/26,5/28,1. O2.5 = 1.69 / U2.5 = 2.15, czyli Over 56%.

**λ:** Auxerre 1,65, Le Mans 1,30 (łącznie 2,95). Obie obrony przepuszczają ponad 2 gole na mecz, więc regresja do średniej ligi jest umiarkowana.

**Skalibruj:** Auxerre ma p < 50%, więc nie jest wyraźnym faworytem. Korekty kryzysowej za serię Le Mans (3 porażki) nie stosuję, bo reguła dotyczy faworyta z p 50-85%. Model jest zgodny z rynkiem (±1 pp na 1X2 i Over 2.5). To mecz wyrównany: **brak mocnego typu wynikowego**.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 (Auxerre) | 45,7% | 2.19 | niska |
| X | 24,1% | 4.14 | niska |
| 2 (Le Mans) | 30,2% | 3.31 | niska |
| 1X | 69,8% | 1.43 | średnia |
| X2 | 54,3% | 1.84 | niska |
| 12 | 75,9% | 1.32 | średnia |
| Auxerre DNB | 60,2% | 1.66 | niska |
| Over 1.5 | 79,3% | 1.26 | średnia |
| Under 1.5 | 20,7% | 4.84 | niska |
| Over 2.5 | 56,6% | 1.77 | średnia |
| Under 2.5 | 43,4% | 2.30 | niska |
| Over 3.5 | 34,2% | 2.93 | niska |
| Under 3.5 | 65,8% | 1.52 | niska-średnia |
| BTTS tak | 58,8% | 1.70 | średnia |
| BTTS nie | 41,2% | 2.43 | niska |
| Auxerre Over 0.5 | 80,8% | 1.24 | średnia |
| Auxerre Over 1.5 | 49,1% | 2.04 | niska |
| Le Mans Over 0.5 | 72,7% | 1.38 | średnia |
| Le Mans Over 1.5 | 37,3% | 2.68 | niska |
| Rożne (śr. 10,5) Over 8.5 | 69,3% | 1.44 | niska-średnia |
| Rożne Over 9.5 | 58,4% | 1.71 | niska |
| Rożne Under 10.5 | 52,8% | 1.89 | niska |
| Kartki (śr. 3,9; sędzia nieznany) Over 2.5 | 70,2% | 1.42 | niska-średnia |
| Kartki Over 3.5 | 52,0% | 1.92 | niska |
| Kartki Under 4.5 | 64,7% | 1.55 | niska |
| Faule (śr. 26) Over 23.5 | 66,5% | 1.50 | niska |
| Faule Over 25.5 | 52,1% | 1.92 | niska |
| Strzały (śr. 26,5) Over 23.5 | 68,8% | 1.45 | niska |
| Strzały celne (śr. 9,5) Over 7.5 | 71,3% | 1.40 | niska |
| Strzały celne Over 8.5 | 59,5% | 1.68 | niska |

Średnie rynków dodatkowych:
- Rożne: AUX u siebie 6,0 / LM na wyjeździe przepuszcza 5,7; LM na wyjeździe 4,0 / AUX u siebie przepuszcza 7,0.
- Kartki: obie drużyny faulują po ok. 15 razy na mecz; Le Mans ma 2,57 kartki na mecz.

**Ryzyka:**
- Typ Over/BTTS przegrywa, jeśli Le Mans zamknie mecz (u siebie z Toulouse oddał 1 celny strzał) albo Auxerre wygra 1-0 jak z Nice, przy 30% posiadania.
- Typ 1X przegrywa przy wygranej Le Mans (30%), która przy dziurawej obronie Auxerre (6,4 celnego strzału rywala na mecz) jest realna.
- Brak składów i sędziego.

**Typy z p > 50% i fair > 1.15:**
- Over 1.5 (79,3%, 1.26)
- 1X (69,8%, 1.43)
- Rożne Over 8.5 (69,3%, 1.44)
- Kartki Over 2.5 (70,2%, 1.42)
- Celne Over 7.5 (71,3%, 1.40)
- Strzały Over 23.5 (68,8%, 1.45)
- Faule Over 23.5 (66,5%, 1.50)
- Under 3.5 (65,8%, 1.52)
- Auxerre DNB (60,2%, 1.66)
- BTTS tak (58,8%, 1.70)
- Rożne Over 9.5 (58,4%, 1.71)
- Over 2.5 (56,6%, 1.77)
- X2 (54,3%, 1.84)
- Kartki Over 3.5 (52,0%, 1.92)

Najlepszy rynek meczu: **BTTS tak / Over 1.5** (oba ataki strzelają, obie obrony słabe). Wynik 1X2 bez mocnego typu.

---

### 17:15 Angers – Lorient (Ligue 1)

**Kluczowe dane (ESPN):**
- Tabela: Angers 15. (7 pkt, 2-1-4, bilans bramek -6), Lorient 8. (11 pkt, 3-2-2, +1).
- Angers: śr. 1,29 gola strzelonego i 2,14 straconego. W dwóch ostatnich meczach stracił 10 goli (1-5 w Brest, 2-5 z Marseille). Strzały 13,6 do 17,6, ale celne tylko 3,0 do 6,6. U siebie: 0-2 z Lille, 1-2 z Rennes, 2-0 z Troyes, 2-5 z OM. Rożne u siebie 6,0:6,25, faule 10,9 (mało).
- Lorient: śr. 1,00 gola strzelonego i 0,86 straconego. Trzy wygrane 1-0 lub podobne z rzędu, w tym 1-0 z Monaco i 1-0 z Paris FC, oba u siebie. Na wyjeździe: 0-0 w Nice, 1-0 w Lens, 1-2 w Le Mans (gole 0,67:0,67). Mecze Lorient średnio 1,86 gola.
- Lorient jest wyraźnie przegrzany względem gry: oddaje 9,9 strzału przy 13,9 rywala i 2,6 rożnego przy 5,6 rywala. Bilans 0,86 straconego przy 3,9 celnego strzału rywala na mecz to ponadprzeciętna skuteczność bramkarza (Mvogo, 21 obron).

**H2H (ESPN):** Lorient 1-2 Angers (08.2026, sparing lub inna data), Lorient 2-0 Angers (02.2026), Angers 2-0 Lorient (10.2025), 0-0 i 1-2 (2023). Bez wyraźnego wzorca, niskie wyniki.

**Newsy:** Ground News: Himad Abdelli nie znalazł się w kadrze na Marseille (powód potwierdził Dujeux, ale fragment tekstu się urwał; wygasający kontrakt). Jego status na niedzielę jest **niepotwierdzony**. Poza tym nie znalazłem raportów kontuzji ani składów. Trener Angers: Alexandre Dujeux.

**Rynek (DraftKings):** 1 = 2.95, X = 3.30, 2 = 2.50, czyli bez marży 32,5/29,1/38,4. O2.5 = 2.00 / U2.5 = 1.80, czyli Over 47,4%.

**λ:** Angers 1,15 (lekko w dół za możliwy brak Abdellego, bez dalszych korekt), Lorient 1,30. Defensywa Angers jest słaba, ale atak Lorient na wyjeździe nieskuteczny.

**Skalibruj:** model jest zgodny z rynkiem (±2 pp). Lorient jest faworytem z p tylko 40%, więc nie ma mocnego typu wynikowego. Under 2.5 jest 3 pp powyżej rynku, co mieści się w progu, ale forma Angers (10 straconych goli w 2 meczach) przemawia za golami, więc pewność dla Under daję tylko średnią.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 (Angers) | 32,8% | 3.05 | niska |
| X | 27,2% | 3.67 | niska |
| 2 (Lorient) | 40,0% | 2.50 | niska |
| 1X | 60,0% | 1.67 | niska |
| X2 | 67,2% | 1.49 | średnia |
| 12 | 72,8% | 1.37 | niska-średnia |
| Lorient DNB | 54,9% | 1.82 | niska |
| Over 1.5 | 70,2% | 1.42 | średnia |
| Under 1.5 | 29,8% | 3.36 | niska |
| Over 2.5 | 44,3% | 2.26 | niska |
| Under 2.5 | 55,7% | 1.80 | średnia |
| Over 3.5 | 23,2% | 4.31 | niska |
| Under 3.5 | 76,8% | 1.30 | średnia |
| BTTS tak | 49,7% | 2.01 | niska |
| BTTS nie | 50,3% | 1.99 | niska |
| Angers Over 0.5 | 68,3% | 1.46 | niska-średnia |
| Angers Over 1.5 | 31,9% | 3.13 | niska |
| Lorient Over 0.5 | 72,7% | 1.38 | niska-średnia |
| Lorient Over 1.5 | 37,3% | 2.68 | niska |
| Rożne (śr. 9,8) Over 8.5 | 62,1% | 1.61 | niska |
| Rożne Over 9.5 | 50,6% | 1.98 | niska |
| Rożne Under 10.5 | 60,6% | 1.65 | niska |
| Kartki (śr. 3,2; sędzia nieznany) Over 2.5 | 58,3% | 1.72 | niska |
| Kartki Under 3.5 | 61,0% | 1.64 | niska |
| Kartki Under 4.5 | 76,2% | 1.31 | niska-średnia |
| Faule (śr. 24,2) Over 21.5 | 68,5% | 1.46 | niska |
| Faule Under 25.5 | 61,2% | 1.63 | niska |
| Strzały (śr. 27,5) Over 23.5 | 74,5% | 1.34 | niska |
| Strzały Over 25.5 | 61,9% | 1.62 | niska |
| Strzały celne (śr. 7,9) Over 6.5 | 65,8% | 1.52 | niska |

Średnie rynków dodatkowych:
- Rożne: ANG u siebie 6,0 / LOR na wyjeździe przepuszcza 6,0; LOR na wyjeździe zdobywa tylko 2,0 rożnego.
- Kartki i faule: obie drużyny faulują mało (ANG 10,9, LOR 9,3 fauli na mecz) i rzadko dostają kartki (1,7 i 1,1 na mecz).

**Ryzyka:**
- Under 3.5 / Under 2.5 przegrywa, jeśli powtórzy się defensywna zapaść Angers (1-5, 2-5). W tym scenariuszu Lorient strzela 3 lub więcej.
- X2 przegrywa przy wygranej Angers (33%), np. przez regres skuteczności Lorient: przy 13,9 strzału rywala na mecz bilans 0,86 straconego gola jest nie do utrzymania.
- Abdelli niepotwierdzony, sędzia nieznany.

**Typy z p > 50% i fair > 1.15:**
- Under 3.5 (76,8%, 1.30)
- Kartki Under 4.5 (76,2%, 1.31)
- Strzały Over 23.5 (74,5%, 1.34)
- 12 (72,8%, 1.37)
- Lorient Over 0.5 (72,7%, 1.38)
- Over 1.5 (70,2%, 1.42)
- Faule Over 21.5 (68,5%, 1.46)
- Angers Over 0.5 (68,3%, 1.46)
- X2 (67,2%, 1.49)
- Celne Over 6.5 (65,8%, 1.52)
- Rożne Over 8.5 (62,1%, 1.61)
- Strzały Over 25.5 (61,9%, 1.62)
- Faule Under 25.5 (61,2%, 1.63)
- Kartki Under 3.5 (61,0%, 1.64)
- Rożne Under 10.5 (60,6%, 1.65)
- 1X (60,0%, 1.67)
- Kartki Over 2.5 (58,3%, 1.72)
- Under 2.5 (55,7%, 1.80)
- Lorient DNB (54,9%, 1.82)
- Rożne Over 9.5 (50,6%, 1.98)
- BTTS nie (50,3%, 1.99)

Najlepszy rynek meczu: **Under 3.5** oraz **X2** (średnia pewność). 1X2 bez mocnego typu.

---

### 17:15 Toulouse – Troyes (Ligue 1)

**Kluczowe dane (ESPN):**
- Tabela: Toulouse 12. (9 pkt, 2-3-2, bilans bramek +1), Troyes 17. (4 pkt, 1-1-5, -11, beniaminek).
- Toulouse: śr. 1,71 gola strzelonego i 1,57 straconego. U siebie gole tylko 1,0:1,67 (0-2 z Lyonem, 0-1 z Lille, 3-2 z Le Havre), ale pod względem strzałów dominuje: 18,3 do 13,0 i 5,7 celnego. Z Lille oddał 24 strzały, z czego 10 celnych, i przegrał 0-1, więc wyniki u siebie są poniżej poziomu gry. Na wyjeździe 2,25 gola na mecz, ostatnio 3-0 w Le Mans.
- Troyes: śr. 0,71 gola strzelonego i 2,29 straconego. Cztery porażki z rzędu: 2-6 ze Strasbourgiem, 0-2 w Lille, 0-2 w Angers, 0-2 z OM, 1-3 z Lens. Na wyjeździe celne tylko 2,0 na mecz.
- Ciekawostka: Troyes wywalcza dużo rożnych (7,1 do 2,1). Gra dośrodkowaniami i pada wiele bloków.
- Strzelcy: Tengstedt 5 goli w 5 meczach, Cásseres 5 asyst (ESPN).

**H2H (ESPN):** 4-1, 3-0, 1-1, 0-0, 1-0 dla Toulouse (2018-2023). Stare, waga niska. Brak porażki Toulouse.

**Newsy:** Sports Mole i Stats Zone (streszczenie z wyszukiwania): Ilyas Azizi ma wrócić po chorobie, Troyes bez nowych absencji. Toulouse jest bez porażki w 4 meczach. Flashscore: Tengstedt ma 6 udziałów przy golach w drugich połowach w 4 meczach. Modele zewnętrzne (Flashscore, Kickoff) wskazują wygraną Toulouse.

**Rynek (DraftKings):** 1 = 1.53, X = 4.50, 2 = 5.75, czyli bez marży 62,3/21,1/16,6. O2.5 = 1.59 / U2.5 = 2.35, czyli Over 59,7%.

**λ:** Toulouse 2,10, Troyes 0,90 (łącznie 3,0, zgodnie z rynkiem totalu). Surowy Poisson daje 65,0/19,9/15,1.

**Skalibruj:**
- Underdog jest w kryzysie (4 porażki z rzędu, desperacja w walce o utrzymanie), więc odejmuję 5 pp od faworyta: **1 = 60%**, X 22,5%, 2 17,5%.
- To 2,3 pp pod rynkiem, czyli w granicy dozwolonej.
- Rynki goli zostawiam bez zmian; tylko Toulouse Over 1.5 obniżam do 59% (spójnie z korektą).
- Troyes trafiło do siatki tylko w 3 z 7 meczów, więc Troyes Over 0.5 obniżam do 55%, a BTTS tak do 49%.

| Rynek | p | fair odds | pewność |
|---|---|---|---|
| 1 (Toulouse) | 60,0% | 1.67 | średnia |
| X | 22,5% | 4.44 | niska |
| 2 (Troyes) | 17,5% | 5.71 | niska |
| 1X | 82,5% | 1.21 | średnia-wysoka |
| X2 | 40,0% | 2.50 | niska |
| 12 | 77,5% | 1.29 | średnia |
| Toulouse DNB | 77,4% | 1.29 | średnia |
| Over 1.5 | 80,1% | 1.25 | średnia |
| Under 1.5 | 19,9% | 5.02 | niska |
| Over 2.5 | 57,7% | 1.73 | średnia |
| Under 2.5 | 42,3% | 2.36 | niska |
| Over 3.5 | 35,3% | 2.83 | niska |
| Under 3.5 | 64,7% | 1.55 | niska-średnia |
| BTTS tak | 49% | 2.04 | niska |
| BTTS nie | 51% | 1.96 | niska |
| Toulouse Over 0.5 | 87,8% | 1.14 (≤ 1.15, odpada) | średnia |
| Toulouse Over 1.5 | 59% | 1.69 | średnia |
| Toulouse Over 2.5 | 35% | 2.86 | niska |
| Troyes Over 0.5 | 55% | 1.82 | niska |
| Troyes Under 0.5 (Toulouse czyste konto) | 45% | 2.22 | niska |
| Rożne (śr. 10,0) Over 8.5 | 64,2% | 1.56 | niska |
| Rożne Over 9.5 | 52,8% | 1.89 | niska |
| Rożne Under 10.5 | 58,4% | 1.71 | niska |
| Kartki (śr. 3,3; sędzia nieznany) Over 2.5 | 60,2% | 1.66 | niska |
| Kartki Under 3.5 | 59,1% | 1.69 | niska |
| Kartki Under 4.5 | 74,6% | 1.34 | niska-średnia |
| Faule (śr. 26,9) Over 23.5 | 72,1% | 1.39 | niska |
| Faule Over 25.5 | 58,5% | 1.71 | niska |
| Strzały (śr. 28,6) Over 25.5 | 68,7% | 1.46 | niska |
| Strzały Over 27.5 | 55,7% | 1.80 | niska |
| Strzały celne (śr. 9,0) Over 7.5 | 66,0% | 1.52 | niska |
| Strzały celne Over 8.5 | 53,5% | 1.87 | niska |

Średnie rynków dodatkowych:
- Rożne: TOU u siebie 6,0 / TRO na wyjeździe przepuszcza 2,0; TRO na wyjeździe zdobywa 7,0 / TOU u siebie przepuszcza 4,7. Sprzeczne sygnały, więc pewność niska.
- Faule: Toulouse 15,6 fauli na mecz (dużo).

**Ryzyka:**
- Remis (22,5%): Toulouse u siebie wygrał tylko 1 z 3 meczów mimo przewagi w strzałach, a nieskuteczność może się powtórzyć.
- Wygrana Troyes (17,5%): drużyna desperacko gra o utrzymanie i wywalcza dużo rożnych, więc gol ze stałego fragmentu i obrona wyniku to realny scenariusz.
- Over 2.5 przegrywa przy 1-0 lub 2-0, co jest typowym wynikiem przy słabym ataku Troyes.

**Typy z p > 50% i fair > 1.15:**
- 1X (82,5%, 1.21, przypadek graniczny 1.15-1.20+)
- Over 1.5 (80,1%, 1.25)
- 12 (77,5%, 1.29)
- Toulouse DNB (77,4%, 1.29)
- Kartki Under 4.5 (74,6%, 1.34)
- Faule Over 23.5 (72,1%, 1.39)
- Strzały Over 25.5 (68,7%, 1.46)
- Celne Over 7.5 (66,0%, 1.52)
- Under 3.5 (64,7%, 1.55)
- Rożne Over 8.5 (64,2%, 1.56)
- Kartki Over 2.5 (60,2%, 1.66)
- 1 Toulouse (60,0%, 1.67)
- Kartki Under 3.5 (59,1%, 1.69)
- Toulouse Over 1.5 (59%, 1.69)
- Faule Over 25.5 (58,5%, 1.71)
- Rożne Under 10.5 (58,4%, 1.71)
- Over 2.5 (57,7%, 1.73)
- Strzały Over 27.5 (55,7%, 1.80)
- Troyes Over 0.5 (55%, 1.82)
- Celne Over 8.5 (53,5%, 1.87)
- Rożne Over 9.5 (52,8%, 1.89)
- BTTS nie (51%, 1.96)

Toulouse Over 0.5 (fair 1.14) odpada z rankingu. Najlepszy rynek meczu: **Toulouse DNB / 1X oraz Over 1.5** (średnia pewność, zgodność z rynkiem).

---

## Kandydaci na kupon (dla bet-slip-builder)

| Mecz | Rynek | p | fair | pewność | od czego zależy | kurs rynkowy |
|---|---|---|---|---|---|---|
| Toulouse – Troyes | Toulouse DNB | 77,4% | 1.29 | średnia | skład TOU (Tengstedt) | brak |
| Toulouse – Troyes | Over 1.5 | 80,1% | 1.25 | średnia | - | brak (O2.5 DK 1.59) |
| Toulouse – Troyes | 1 Toulouse | 60,0% | 1.67 | średnia | po korekcie kryzysowej -5 pp | DK 1.53 (EV < 0) |
| Toulouse – Troyes | Over 2.5 | 57,7% | 1.73 | średnia | - | DK 1.59 (EV < 0) |
| Auxerre – Le Mans | Over 1.5 | 79,3% | 1.26 | średnia | - | brak |
| Auxerre – Le Mans | BTTS tak | 58,8% | 1.70 | średnia | składy | brak |
| Auxerre – Le Mans | Over 2.5 | 56,6% | 1.77 | średnia | - | DK 1.69 (EV < 0) |
| Auxerre – Le Mans | 1X | 69,8% | 1.43 | średnia | - | brak |
| Angers – Lorient | Under 3.5 | 76,8% | 1.30 | średnia | forma obrony Angers | brak |
| Angers – Lorient | X2 | 67,2% | 1.49 | średnia | Abdelli (ANG) | brak |
| Angers – Lorient | Under 2.5 | 55,7% | 1.80 | średnia | - | DK 1.80 (EV około 0) |
| Wszystkie | kartki, faule, rożne, strzały | patrz tabele | - | niska | sędzia nieznany, brak drugiego źródła | brak |

Zgodnie z regułą skilla (brak dwóch niezależnych źródeł średnich i nieznany sędzia) rynków kartek, fauli, rożnych i strzałów nie rekomenduję do wariantu głównego kuponu.

To są oszacowania probabilistyczne, nie gwarancje.

## Analiza piłkarska – niedziela 25.10.2026 (grupa G, 17:30 CET)

Skill: `football-analyst` (osobno na każdy mecz). Źródła: ESPN API (summary, schedule, boxscore 7/6 ostatnich meczów ligowych każdej drużyny, pickcenter DraftKings), WebSearch (newsy, sędziowie, Ekstraklasa). MCP `sportsdata` nie działa, WebFetch nie rozwiązywał domen (ENOTFOUND), więc treść artykułów znam tylko ze streszczeń wyszukiwarki. Skrypty: `poisson.py`, `markets.py`. Statystyki "własne/rywala" to średnie z boxscore'ów ESPN z sezonu 2026/27.

---

### 17:30 Sunderland – Leeds United (Premier League)

**Kluczowe dane**
- Tabela (ESPN): Sunderland 20. (1-1-5, 4 pkt, bramki 6:14), Leeds 8. (2-4-1, 10 pkt, 9:6).
- Sunderland u siebie: 1-0 Fulham, 0-2 Arsenal, 0-2 Brighton (1:4). 4 porażki ligowe z rzędu (Ipswich 1-2, Brentford 1-1, Man City 3-5, Arsenal 0-2, Brighton 0-2, Bournemouth 0-2). W 7 meczach 3 czerwone kartki (Arsenal, Brighton – czerwona dla rywala, Bournemouth) (ESPN boxscore).
- Leeds na wyjeździe: 1-0 Forest, 1-1 Brighton, 1-2 Arsenal (3:3). Ostatnio 1-1 z Man Utd, 0-0 z Palace, 4-1 z Newcastle.
- Średnie na mecz (własne/rywala): Sunderland strzały 11,6/14,6, celne 4,0/3,7, rożne 4,3/4,3, faule 11,4/14,1, żółte 1,7/1,6. Leeds strzały 12,0/14,1, celne 4,0/4,3, rożne 4,0/4,3, faule 12,7/11,9, żółte 1,9/2,4 (ESPN, 7 meczów). Brak xG w dostępnych źródłach.
- Puchary: Sunderland grał w czwartek 22.10 w Poznaniu (LE, 1-1 z Lechem, 25 strzałów, 6 rożnych) + podróż; Leeds bez meczu w tygodniu (ostatni mecz 18.10).
- H2H (ESPN, 5 meczów): 0-1, 1-0 (Sunderland w Leeds), 1-1, 1-2, 2-2 – wyrównane, niskobramkowe (śr. 2,2 gola).

**Newsy**
- Sunderland: Danso zawieszony (do 31.10), Ballard kontuzja (ścięgno), Isidor 50%, Brobbey 75%, Meunier 75% (lista FPL z 21.10 wg footballdream.in – jedno źródło, niepotwierdzone). Trener Régis Le Bris pod presją zarządu (footballinsider247, football365 – plotkarskie źródła).
- Leeds: Rodon kontuzja (powrót ok. 21.11).
- Sędzia: **Stuart Attwell** (VAR Pawson) – potwierdzone przez leedsunited.com, Sunderland Echo. Kariera: 3,4–4,3 żółtych/mecz (Statshub / ValueStats), w tym sezonie 2 mecze, 11 żółtych (mała próba). Prowadził w tym sezonie Brighton–Leeds (29 fauli, 6 żółtych wg ESPN).
- Przewidywane ustawienia: Sunderland 4-5-1, Leeds 5-4-1 (footballdream.in) – zapowiada zamknięty mecz.

**λ:** Sunderland 1,10 / Leeds 1,25 (słaby atak SUN u siebie, mocna obrona LEE 0,86 straconych/mecz; korekta w dół za brak Danso/Ballarda zrównoważona słabą skutecznością Leeds na wyjeździe). Korekta kryzysowa: Sunderland nie jest wyraźnym underdogiem (rynek ~32/30/38), więc nie stosuję pełnych –5–10 pp; zmęczenie po czwartku uwzględnione w λ.

**Rynek (DraftKings przez ESPN):** 1 +195 (2.95), X +220 (3.20), 2 +150 (2.50) → bez marży 32,2 / 29,7 / 38,0%. O2.5 +115 / U2.5 –140 → Over 44,4%. Mój model w granicach ±3 pp od rynku.

| Rynek | p | fair | pewność |
|---|---|---|---|
| 1 Sunderland | 32,4% | 3.09 | średnia |
| X | 27,9% | 3.58 | średnia |
| 2 Leeds | 39,7% | 2.52 | średnia |
| 1X | 60,3% | 1.66 | średnia |
| X2 | 67,6% | 1.48 | średnia |
| 12 | 72,1% | 1.39 | niska |
| Leeds DNB | 55,1% | 1.82 | niska |
| Over 1.5 | 68,1% | 1.47 | średnia |
| Over 2.5 / Under 2.5 | 41,7% / 58,3% | 2.40 / 1.72 | średnia |
| Under 3.5 | 78,9% | 1.27 | średnia |
| BTTS tak / nie | 47,6% / 52,4% | 2.10 / 1.91 | niska |
| Sunderland strzeli ≥1 | 66,7% | 1.50 | średnia |
| Leeds strzeli ≥1 | 71,3% | 1.40 | średnia |
| Sunderland Under 1.5 goli | 69,9% | 1.43 | średnia |
| Leeds Under 1.5 goli | 64,5% | 1.55 | średnia |
| Rożne (śr. 8,6): O7.5 / U9.5 / U10.5 | 60,5% / 63,5% / 73,6% | 1.65 / 1.57 / 1.36 | średnia |
| Rożne O8.5 / U8.5 | 48,1% / 51,9% | 2.08 / 1.93 | niska |
| Kartki (żółte=1, śr. 4,1, Attwell): O3.5 / U4.5 / U5.5 | 55,5% / 61,3% / 75,1% | 1.80 / 1.63 / 1.33 | średnia |
| Faule (śr. 24,5): O21.5 / O23.5 / U25.5 | 70,4% / 55,9% / 59,0% | 1.42 / 1.79 / 1.69 | niska |
| Strzały (śr. 24,5): O22.5 / U24.5 | 62,6% / 51,8% | 1.60 / 1.93 | niska |
| Strzały celne (śr. 8,0): O7.5 / U8.5 | 53,7% / 59,3% | 1.86 / 1.69 | niska |

**Ryzyka:** (a) dla X2/Leeds: wygrana Sunderlandu (32%) – efekt "nowego bodźca"/zmiany trenera, gospodarze dominowali w Poznaniu; remis (28%) – oba zespoły grają defensywnie, Leeds 4 remisy w 7. (b) Under 2.5/rożne Under: wczesny gol otwiera mecz; Sunderland traci dużo w meczach z czołówką (5 z City). (c) Kartki: Sunderland ma 3 czerwone w 7 meczach, a Attwell w tym sezonie pokazuje dużo – Over kartek realny; Under kartek tylko niska/średnia pewność. (d) Składy niepotwierdzone (lista FPL z 21.10).

**Typy z p>50% i fair>1.15:** X2 67,6% (1.48); Under 2.5 58,3% (1.72); Under 3.5 78,9% (1.27); Over 1.5 68,1% (1.47); Leeds ≥1 gol 71,3% (1.40); Sunderland Under 1.5 goli 69,9% (1.43); rożne Under 10.5 73,6% (1.36) / Under 9.5 63,5% (1.57); rożne Over 7.5 60,5% (1.65); kartki Under 5.5 75,1% (1.33); faule Over 21.5 70,4% (1.42, niska); strzały Over 22.5 62,6% (1.60, niska). Najlepszy rynek meczu: **Under 3.5 / Under 2.5** i **rożne Under 10.5** (oba zespoły ~4 rożne/mecz). Brak mocnego typu wynikowego (1X2 wyrównane).

---

### 17:30 SC Freiburg – Bayern Monachium (Bundesliga)

**Kluczowe dane**
- Tabela (ESPN): Bayern 2. (4-2-0, 14 pkt, 22:5), Freiburg 3. (4-1-1, 13 pkt, 15:6).
- Freiburg u siebie 3/3: 4-1 Werder, 5-0 Gladbach, 2-1 Schalke (11:2). Wyjazdy: 1-0 Paderborn, 2-2 Frankfurt, 1-2 Leverkusen. W tygodniu: 3-2 Jablonec (LKE), **0-3 w Monako (czwartek 22.10)** – 3 dni odpoczynku.
- Bayern: 5-1 Stuttgart, 0-0 Schalke, 2-1 Elversberg, 7-0 Union, 2-2 Augsburg, 6-1 Leipzig; LM: 3-3 Viking, **2-2 Arsenal (środa 21.10)**.
- Średnie (własne/rywala): Freiburg strzały 16,2/9,2, celne 5,3/2,5, rożne 5,2/3,5, faule 9,5/14,2, żółte 1,5/1,5. Bayern strzały 24,3/7,8, celne 10,3/2,8, rożne 9,7/2,7, faule 10,5/9,3, żółte 0,8/2,2 (ESPN, 6 meczów). Brak xG.
- H2H (ESPN, 5 ostatnich): Freiburg–Bayern 2-3 (04.2026), Bayern–Freiburg 6-2, Freiburg–Bayern 1-2, Bayern–Freiburg 2-0, Freiburg–Bayern 2-2 → Bayern 4W 1R 0P, średnio 4,4 gola, BTTS w 4/5.

**Newsy**
- **Vincent Kompany zasłabł na treningu w piątek, jest w szpitalu (stan stabilny), nieobecny tygodnie; drużynę poprowadzi asystent Aaron Danks** (ESPN news 23–24.10; Goal, Sportsgambler/khelnow – zgodne).
- Bayern – absencje: Neuer (ścięgno stopy, w bramce Urbig), Pavlović (łydka, wg Sky/Bild), Musiala (mięsień uda), Luis Díaz (naderwanie ścięgna), Kim Min-jae (uraz z meczu z Arsenalem, wątpliwy/out), Kimmich (sprawy rodzinne) (Goal "6 players and a manager"; status Kima i Kimmicha różni się między źródłami). Brak doniesień o absencji Kane'a.
- Freiburg: Muslija out (więzadła, do końca grudnia), Engelhardt wątpliwy (zszedł w 15' w Monako, zastępca Osterhage), Lienhart niepewny, Suzuki wraca po pauzie (preview khelnow/Sportsgambler).
- Sędzia: FotMob podaje Felixa Zwayera, inne źródło – jeszcze nie wyznaczony → **niepotwierdzony**, kartki liczone ze średniej drużyn (Bayern i Freiburg po ~3,0 żółtych/mecz łącznie).

**λ:** Freiburg 1,25 / Bayern 2,40. Bayern bazowo ~2,7 na wyjeździe (3,67 gola/mecz), –~12% za brak Musiali, Díaza, Kimmicha, Pavlovicia i trenera; Freiburg bazowo ~1,0 przeciw obronie Bayernu, +0,25 za osłabioną obronę (Neuer, Kim) i 2-2/3-3 Bayernu w LM; Freiburg zmęczony po czwartku (bez dodatkowej korekty totalu >3 pp zgodnie z regułą).

**Rynek (DraftKings):** 1 +500 (6.00), X +425 (5.25), 2 –255 (1.39) → bez marży 15,5 / 17,7 / 66,8%. Sportsgambler: Bayern ~72% implied (–263). O3.5 –130 / U3.5 +105 → Over 3.5 53,7%. Mój Bayern 62,8% = –4 pp od rynku (uzasadnione konkretnymi absencjami 6 graczy + trenera; rynek mógł je już częściowo wycenić – przy dużej różnicy klas rynek bywa trafniejszy). Over 3.5: mój 49,5% vs rynek 53,7% – nie gram przeciwko rynkowi.

| Rynek | p | fair | pewność |
|---|---|---|---|
| 1 Freiburg | 18,6% | 5.38 | średnia |
| X | 18,6% | 5.37 | średnia |
| 2 Bayern | 62,8% | 1.59 | średnia |
| 1X | 37,2% | 2.69 | średnia |
| X2 | 81,4% | 1.23 | średnia |
| 12 | 81,4% | 1.23 | niska |
| Bayern DNB | 77,1% | 1.30 | średnia |
| Over 1.5 | 87,9% | 1.14 (≤1.15 – pomijać) | wysoka |
| Over 2.5 | 70,6% | 1.42 | średnia |
| Over 3.5 / Under 3.5 | 49,5% / 50,5% | 2.02 / 1.98 | niska |
| BTTS tak | 64,9% | 1.54 | średnia |
| Freiburg strzeli ≥1 | 71,3% | 1.40 | średnia |
| Bayern strzeli ≥1 / ≥2 (O1.5) / ≥3 | 90,9% / 69,2% / 43,0% | 1.10 / 1.45 / 2.33 | średnia |
| Rożne (śr. 10,0): O8.5 / O9.5 / U11.5 | 64,2% / 52,8% / 68,5% | 1.56 / 1.89 / 1.46 | średnia |
| Rożne Bayernu (śr. 6,8): O4.5 / O5.5 | 77,6% / 64,6% | 1.29 / 1.55 | średnia |
| Kartki (żółte=1, śr. 3,4, sędzia niepotw.): O2.5 / U4.5 | 62,0% / 73,0% | 1.61 / 1.37 | niska |
| Faule (śr. 22,0): O19.5 / U23.5 | 67,9% / 63,2% | 1.47 / 1.58 | niska |
| Strzały (śr. 28): O24.5 / O26.5 | 71,4% / 58,5% | 1.40 / 1.71 | niska |
| Strzały celne (śr. 10): O8.5 / O9.5 | 65,2% / 53,3% | 1.53 / 1.87 | niska |

**Ryzyka:** (a) Bayern: remis (19%) i wygrana Freiburga (19%) – Freiburg 3/3 u siebie, 11:2; Bayern bez trenera, bez Kimmicha/Pavlovicia w środku i z rezerwowym bramkarzem, po 2-2 z Arsenalem; 3-3 z Vikingiem pokazuje dziury w obronie. (b) Over 2.5/BTTS: Freiburg zmęczony po Monako i bez Engelhardta może się zamknąć – możliwe 0-2. (c) Rożne Bayernu: przy szybkim prowadzeniu Bayern zwalnia; brak Musiali/Díaza = mniej dryblingu na skrzydłach. (d) Kartki i faule: sędzia niepotwierdzony – pewność niska.

**Typy z p>50% i fair>1.15:** Bayern 62,8% (1.59); Bayern DNB 77,1% (1.30); X2 81,4% (1.23); Over 2.5 70,6% (1.42); BTTS tak 64,9% (1.54); Freiburg ≥1 gol 71,3% (1.40); Bayern O1.5 goli 69,2% (1.45); rożne O8.5 64,2% (1.56) / U11.5 68,5% (1.46); rożne Bayernu O4.5 77,6% (1.29) / O5.5 64,6% (1.55); kartki O2.5 62,0% (1.61, niska); kartki U4.5 73,0% (1.37, niska); strzały O24.5 71,4% (1.40, niska); celne O8.5 65,2% (1.53, niska). Over 1.5 (1.14) – pominąć. Najlepszy rynek meczu: **Over 2.5** i **rożne Bayernu Over 4.5** (Bayern 9,7 rożnego/mecz, Freiburg pozwala 3,5 – ale przeciw słabszym rywalom).

---

### 17:30 Legia Warszawa – Lech Poznań (Ekstraklasa, Stadion Wojska Polskiego)

**Kluczowe dane** (brak Ekstraklasy w ESPN – dane wyłącznie z WebSearch, pewność niższa)
- Tabela: Lech 2. (10 meczów, 25 pkt, bramki **27:9**), Legia 3. (11 meczów, 23 pkt, bez porażki w lidze), lider Górnik 27 pkt (ekstraklasa.org, TNT Sports, gol24; źródła częściowo sprzeczne). Bramki Legii: snapshot po 9 kolejkach 19:8 (astar.czest.pl), potem 2-0 Wisła i 1-1 Cracovia → ok. 22:9 w 11 (szacunek).
- Legia: 2-0 Wisła Kraków (11.10, gole Zjawiński, Adamski), 1-1 Cracovia (17.10, Sevcik); wcześniej dwa domowe remisy z rzędu; odpadła z Pucharu Polski z Motorem (0-3). **Bez meczu w tygodniu** – 8 dni odpoczynku.
- Lech: 6-1 Korona (18.10), LE: 4-0 z Leverkusen (15.10, wg ESPN), **1-1 z Sunderlandem w czwartek 22.10** (ESPN: Sunderland 25 strzałów, Lech 16; 3 rożne Lecha, 0 żółtych) – 3 dni odpoczynku, grał podstawowy skład (Lis, Yegbe, Skrzypczak, Gurgul, Pereira, Rodriguez, Murawski, Kozubal, Ishak, Håkans, Walemark).
- Strzelcy: Legia – Adamski, Zjawiński, Augustyniak po 4; Lech – Rodriguez 6.
- H2H: "Lech w ostatnich 10 meczach z Legią wygrał tylko 3 razy" (etoto/najlepsibukmacherzy); ostatni mecz w Poznaniu Lech–Legia 4-0 (sezon nieprecyzowany). Szczegóły niepotwierdzone.
- Brak danych o xG, strzałach, rożnych i faulach obu drużyn.

**Newsy**
- Legia: wraca Vinagre; kontuzjowany Jakub Żewłakow; wątpliwy Bichakhchyan; Adamski z 3 żółtymi (zagrożony). Przewidywany skład 3-4-3: Hindrich – Piątkowski, Augustyniak, Deziel – Wszołek, Kapustka, Urbański, Vinagre – Sevcik, Adamski, Zjawiński (etoto/najlepsibukmacherzy).
- Lech (trener Niels Frederiksen): out Gholizadeh, Douglas, João Moutinho, Sayyadmanesh, Mońka; Gumny wątpliwy. Skład 4-2-3-1: Lis – Pereira, Skrzypczak, Yegbe, Gurgul – Murawski, Kozubal – Walemark, Rodriguez, Bengtsson – Ishak.
- Sędzia: **Szymon Marciniak** (PZPN; legia.net, meczyki, transfery.info). W sezonie 2026/27: 9 meczów, 23 żółte (≈2,6/mecz) – łagodny w lidze, ale to klasyk o 2. miejsce → średnia kartek 3,8 (2,6 + korekta za stawkę/derby i Ekstraklasową średnią wyższą niż u Marciniaka).

**λ:** Legia 1,35 / Lech 1,30. Lech ma najlepszy atak (2,7/mecz), ale: wyjazd, 3 dni po LE, 5 absencji w ofensywie/pomocy; Legia wypoczęta, niepokonana, mocna obrona (~0,8 straconych). Rynek prawie równy.

**Rynek:** średnie kursy 1X2 2.70 / 3.50 / 2.60 (gol24/etoto/najlepsibukmacherzy – zagregowane, nie Betclic) → bez marży 35,6 / 27,4 / 37,0%. Kursów DraftKings brak (mecz poza ESPN). Mój model: 38,1 / 26,1 / 35,8 – w granicach ±3 pp.

| Rynek | p | fair | pewność |
|---|---|---|---|
| 1 Legia | 38,1% | 2.62 | niska |
| X | 26,1% | 3.83 | niska |
| 2 Lech | 35,8% | 2.79 | niska |
| 1X | 64,2% | 1.56 | średnia |
| X2 | 61,9% | 1.62 | średnia |
| 12 | 73,9% | 1.35 | niska |
| Over 1.5 | 74,2% | 1.35 | średnia |
| Over 2.5 / Under 2.5 | 49,4% / 50,6% | 2.02 / 1.98 | niska |
| Under 3.5 | 72,5% | 1.38 | średnia |
| BTTS tak / nie | 53,9% / 46,1% | 1.86 / 2.17 | niska |
| Legia strzeli ≥1 | 74,1% | 1.35 | średnia |
| Lech strzeli ≥1 | 72,7% | 1.38 | średnia |
| Legia Under 1.5 / Lech Under 1.5 goli | 60,9% / 62,7% | 1.64 / 1.59 | niska |
| Rożne (śr. 9,5 – średnia ligowa, BRAK danych drużyn): O8.5 | 58,8% | 1.70 | niska – nie rekomendować |
| Kartki (żółte=1, śr. 3,8, Marciniak): O2.5 / O3.5 / U4.5 / U5.5 | 68,7% / 50,2% / 66,4% / 79,2% | 1.46 / 1.99 / 1.51 / 1.26 | niska |
| Faule / strzały | – | – | brak danych |

**Ryzyka:** (a) 1X: wygrana Lecha (36%) – najlepszy atak ligi, Rodriguez/Ishak/Walemark w formie (6-1 z Koroną); (b) X2: wygrana Legii (38%) – Lech zmęczony po czwartku i bez 5 graczy, Legia wypoczęta i u siebie niepokonana; (c) kartki: klasyk o dużej stawce może przebić łagodną średnią Marciniaka (O4.5 33,6%), ale też Marciniak trzyma mecze krótko – obie strony; (d) dane Ekstraklasy pochodzą ze streszczeń wyszukiwarki, częściowo sprzecznych (tabela) – pewność obniżona o jeden poziom.

**Typy z p>50% i fair>1.15:** 1X 64,2% (1.56); X2 61,9% (1.62); Over 1.5 74,2% (1.35); Under 3.5 72,5% (1.38); Legia ≥1 gol 74,1% (1.35); Lech ≥1 gol 72,7% (1.38); BTTS tak 53,9% (1.86, niska); kartki O2.5 68,7% (1.46, niska); kartki U5.5 79,2% (1.26, niska) / U4.5 66,4% (1.51, niska). **Brak mocnego typu wynikowego** (mecz wyrównany). Najlepszy rynek meczu: **Under 3.5** i **Legia strzeli gola** (Legia u siebie, wypoczęta; Lech gra 3 dni po LE).

---

## Tabela kandydatów (wejście dla bet-slip-builder)

| Mecz | Rynek | p | fair | pewność | zależy od | kurs rynkowy |
|---|---|---|---|---|---|---|
| SUN–LEE | Under 3.5 | 78,9% | 1.27 | średnia | składy | brak (DK tylko 2.5) |
| SUN–LEE | Under 2.5 | 58,3% | 1.72 | średnia | – | DK 1.71 (≈fair, brak EV) |
| SUN–LEE | X2 | 67,6% | 1.48 | średnia | Danso/Ballard out | brak |
| SUN–LEE | Rożne Under 10.5 | 73,6% | 1.36 | średnia | styl 4-5-1/5-4-1 | brak |
| SUN–LEE | Kartki Under 5.5 | 75,1% | 1.33 | średnia | Attwell (potw.) | brak |
| SCF–FCB | Bayern DNB | 77,1% | 1.30 | średnia | skład Bayernu | brak |
| SCF–FCB | Over 2.5 | 70,6% | 1.42 | średnia | – | brak (DK O3.5 1.77) |
| SCF–FCB | BTTS tak | 64,9% | 1.54 | średnia | Engelhardt, Neuer out | brak |
| SCF–FCB | Rożne Bayernu Over 4.5 | 77,6% | 1.29 | średnia | skład skrzydeł | brak |
| SCF–FCB | Bayern wygra | 62,8% | 1.59 | średnia | trener Danks, 6 absencji | DK 1.39 (poniżej fair – brak EV) |
| LEG–LPO | Under 3.5 | 72,5% | 1.38 | średnia | – | brak |
| LEG–LPO | Legia ≥1 gol | 74,1% | 1.35 | średnia | – | brak |
| LEG–LPO | 1X | 64,2% | 1.56 | średnia | zmęczenie Lecha | ~1.5 (z 2.70/3.50) |

To oszacowania probabilistyczne oparte na niepełnych danych, nie gwarancje.

Źródła: ESPN API (site.api.espn.com, summary 401878764 / 401884759 i boxscore'y), footballdream.in (Sunderland–Leeds GW8), leedsunited.com / sunderlandecho.com / leedsallover.com (sędzia Attwell), statshub.com, valuestats.com (Attwell), footballinsider247.com, football365.com (Le Bris), goal.com (absencje Bayernu), khelnow.com, sportsgambler.com, fotmob.com (Freiburg–Bayern), ekstraklasa.org, tntsports.co.uk, astar.czest.pl (tabela Ekstraklasy), gol24.pl, etoto.pl, najlepsibukmacherzy.pl, weszlo.com (Legia–Lech), legia.net, meczyki.pl, transfery.info, igol.pl (sędzia Marciniak), legia.net/meczyki.pl (forma Legii).

