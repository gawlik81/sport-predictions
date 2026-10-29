# Analiza dnia 28.10.2026 (czas polski, CET)

Zbiorcze analizy skillami analitycznymi. Zakres: Serie A, ATP Wiedeń/Bazylea, e-sport (CS2/LoL/Dota 2, także niższe tiery). Bez MMA, NBA i NHL (brak wydarzeń w tym dniu polskim).

---

<!-- źródło: an_seriea_1 -->
# Serie A, 9. kolejka, sroda 28.10.2026 (CET): analiza 3 meczow o 18:30

Zrodla: MCP sportsdata (seriea_standings/matches/team_stats, pinnacle_league_matchups + pinnacle_matchup_markets), WebSearch/WebFetch (Sky Sport probabili formazioni 27.10, calciomercato.it, ilfattoquotidiano 24.10, AIA/Italpress/diretta.it - sedziowie, tuttoudinese, DAZN/bet365 - absencje). BettingPros: pominiete (brak klucza w sesji). Kursy: tylko Pinnacle (US -> dziesietne, marza usunieta), bez Betclic/gg397.bet. Sedziowie: Sacchi (Milan-Bologna), Massa (Parma-Udinese), Pairetto (Venezia-Inter). Skladu oficjalne nieznane (tylko "probabili") - rynki zawodnika bez typow.

Uwaga o godzinie: Sky Sport podaje Venezia-Inter na 20:45, ale terminarz Serie A (seriea_matches), Pinnacle (cutoff 17:30 UTC) i AIA/Italpress wskazuja 18:30. Przyjeto 18:30; zweryfikuj przed obstawieniem.

Tabela (sezon 2026/27): Lazio 25, Inter 22 (8 m.), Roma 21, Como 20, Milan 18 (8 m.), Bologna 13. miejsce (8 pkt), Udinese 17. (4), Parma 19. (4), Venezia 20. (3).
Srednie sezonowe na mecz (Opta, seriea_team_stats): xG Inter 3.14, Milan 1.94, Bologna 1.47, Venezia 1.57 (6 goli z 12.6 xG), Udinese 1.14, Parma 0.92. Zolte kartki wlasne/mecz: Venezia 2.5, Milan 1.9, Bologna 1.75, Udinese 1.75, Parma 1.5, Inter 1.4. Faule/mecz: Bologna 12.75, Udinese 11.0, Parma 10.4, Venezia 10.25, Milan 9.75, Inter 8.75. Rozne wykonywane/mecz wg Opta (prawdopodobnie zanizone): Inter 5.75, Venezia 4.5, Bologna 4.0, Udinese 4.0, Parma 3.4, Milan 3.1 - srednie rozne ustalono wazone z liniami Pinnacle.

---

## 1. Milan - Bologna (San Siro, 18:30)

**Typ:** brak mocnego typu na 1X2; najlepsze: DC 1X / Under 3.5 | pewnosc srednia

### Wycena (lambda Milan 1.50, Bologna 0.90 -> poisson.py; p skorygowane wzgledem rynku)
| Rynek | p | fair | Pinnacle (bez marzy) | pewnosc |
|---|---|---|---|---|
| Milan wygra (1) | 53% | 1.89 | 56.0% (1.79) | srednia |
| Remis | 26.5% | 3.77 | 25.9% | srednia |
| Bologna wygra (2) | 20.5% | 4.88 | 18.1% | srednia |
| DC 1X | 79.5% | 1.26 | ok. 82% | srednia |
| DC X2 | 47% | 2.13 | - | niska |
| DC 12 | 73.5% | 1.36 | - | srednia |
| Milan wygra 2+ golami | 25% | 4.00 | AH -1.5 ok. 32% | niska |
| Over 1.5 | 69% | 1.45 | ok. 73% | srednia |
| Over 2.5 | 44% | 2.27 | 46.1% | srednia |
| Under 2.5 | 56% | 1.79 | 53.9% | srednia |
| Over 3.5 | 22% | 4.55 | - | srednia |
| Under 3.5 | 78% | 1.28 | ok. 80% | srednia |
| BTTS tak | 46% | 2.17 | ok. 46% | srednia |
| BTTS nie | 54% | 1.85 | - | srednia |
| Rozne (srednia 8.6): Over 8.5 / Under 8.5 | 47% / 53% | 2.13 / 1.89 | O8.5 ok. 45.5% | niska/srednia |
| Rozne Under 9.5 | 63% | 1.59 | O9.5 ok. 38% | srednia |
| Rozne Over 7.5 | 60% | 1.67 | ok. 61% | srednia |
| Kartki zolte (srednia 3.9, Sacchi): Over 2.5 / 3.5 (4+) / 4.5 (5+) | 69% / 51% / 33% | 1.45 / 1.96 / 3.03 | Pinnacle Bookings: 70% / 52% / 33% | niska/srednia |
| Faule meczowe (srednia 24): Over 23.5 | 52% | 1.92 | brak linii | niska |

Najlepszy rynek meczu: Under 3.5 (78%, fair 1.28) lub DC 1X (79.5%, fair 1.26); wynik 1X2 Milanu (53%) to nie jest mocny typ.

### Dane
- **Milan (Amorim):** 5W-3D-0L, 16:7 w bramkach, bez porazki w sezonie. Ostatnie: 2-0 Venezia (d), 1-1 Juventus (w), 2-2 Lazio (w), 3-0 Lecce (d), 1-1 Sassuolo (w), 3-2 Atalanta (d), 2-0 Udinese (w). U siebie 3/3 wygrane, 8:2.
- **Bologna (Palladino):** 2W-2D-4L, 8:10. Ostatnie: 0-1 Atalanta (w), 2-2 Sassuolo (d), 0-1 Napoli (w), 1-1 Torino (d), 2-1 Lecce (w, wygrana Bologny), 1-3 Inter (d, porazka), 2-0 Cagliari (w, wygrana). Na wyjazdach 2W-0D-2L (4:3); xG 1.47 / mecz, ale tylko 8 goli z 11.7 xG.
- **H2H:** MCP zwraca tylko biezacy sezon, brak zweryfikowanych wynikow z 2025/26 - H2H nie wazono.
- **Informacje medialne:** Milan w emergency: brak Rabiota, Gila, Moreiry, Gabbii, Chukwueze, Saelemaekersa, Loftusa-Cheeka, P. Terracciano (ilfattoquotidiano, Sky 27.10). Probabilny sklad 4-4-1-1: Maignan; Tomori, De Winter, Pavlovic, Estupinan; Hutchinson, Musah, Jashari, Bartesaghi; Cisse; Ramos. Pulisic i Modric prawdopodobnie odpoczywaja (derby z Interem 31.10). Bologna 3-4-2-1: bez Holma, Orsoliniego, Piccoliego; Enem (achilles) watpliwy; Odgaard falszywa dziewiatka, Ferguson moze odpoczac. Brak zawieszonych.
- **Sedzia:** Sacchi (VAR Giua). Zrodla rozbiezne: 3.8 zoltej/mecz w 2025/26 (ValueStats) vs 5.1 kartki/mecz w 2026/27 (Virgilio, dane niespojne). Srednia kartek 3.9, zgodna z rynkiem.

### Kalibracja
- p Milanu obnizone z rynku (56% -> 53%, -3 pp) za konkretna informacje kadrowa: 8 nieobecnych (srodek pola: Rabiot; obrona: Gila, Gabbia), rotacja Pulisic/Modric. Nie schodzono >5 pp pod rynek. Bologna nie jest w kryzysie, wiec brak korekty kryzysowej.
- Ryzyko faworyta ma dwie twarze: remis 26.5% i wygrana Bologny 20.5% (Bologna 2 z 4 wyjazdow wygrane).
- Rynki zawodnika: brak potwierdzonych skladow, brak typow.

### Ryzyka
1. Milan w emergency (8 nieobecnych, w kadrze meczowej Camarda i Hutchinson) - mniej kontroli, ryzyko remisu lub wygranej Bologny.
2. Rotacja przed derbami (Pulisic/Modric/Cisse): mniej jakosci w ataku, mniej goli (Under).
3. Odgaard jako falszywa dziewiatka - BTTS ok. 46%, wynik 1-1 / 2-1 mozliwy.
4. Rozne/kartki: linie bliskie sredniej, niska pewnosc, statystyki sedziego niespojne.

**Rynek (Pinnacle):** 1X2 Milan 1.73 / X 3.73 / Bologna 5.35 (surowe); bez marzy 56.0 / 25.9 / 18.1. Total glowna 2.25 (O -118 / U +107), O2.5 +110, U2.5 -125. Team total Milan 1.5: -110/-110; Bologna 0.5 O -151. Rozne 8.0: O -118 / U -100. Kartki 3.5: O -119 / U -102.

---

## 2. Parma - Udinese (Tardini, 18:30)

**Typ:** brak mocnego typu (wyrownany mecz). Najlepsze rynki: Under 3.5, Over 1.5 | pewnosc niska/srednia

### Wycena (lambda Parma 1.15, Udinese 1.10)
| Rynek | p | fair | Pinnacle (bez marzy) | pewnosc |
|---|---|---|---|---|
| Parma wygra (1) | 36% | 2.78 | 35.2% | niska |
| Remis | 29.5% | 3.39 | 30.9% | niska |
| Udinese wygra (2) | 34.5% | 2.90 | 34.0% | niska |
| DC 1X | 65.5% | 1.53 | 66% | niska |
| DC X2 | 64% | 1.56 | 65% | niska |
| DC 12 | 70.5% | 1.42 | 69% | niska |
| Over 1.5 | 68% | 1.47 | ok. 72% | srednia |
| Over 2.5 | 43% | 2.33 | 45.7% | niska/srednia |
| Under 2.5 | 57% | 1.75 | 54.3% | niska/srednia |
| Over 3.5 | 19% | 5.26 | - | srednia |
| Under 3.5 | 81% | 1.23 | ok. 82% | srednia |
| BTTS tak | 48% | 2.08 | ok. 50% | niska |
| BTTS nie | 52% | 1.92 | - | niska |
| Rozne (srednia 9.2): Over 8.5 / Over 9.5 / Under 10.5 | 55% / 44% / 67% | 1.82 / 2.27 / 1.49 | linia 9.0: O -115 / U -102; O8.5 ok. 57% | niska/srednia |
| Kartki zolte (srednia 4.0, Massa): Over 2.5 / 3.5 (4+) / 4.5 (5+) | 71% / 55% / 37% | 1.41 / 1.82 / 2.70 | Pinnacle: O3.5 55.9%, O4.5 37.6% | niska/srednia |
| Faule meczowe (srednia 23): Over 21.5 / Over 23.5 | 60% / 44.5% | 1.67 / 2.25 | brak | niska |

Najlepszy rynek: Under 3.5 (81%, fair 1.23) lub Over 1.5 (68%, fair 1.47); kartki Over 3.5 (55%, fair 1.82) jako dodatkowy.

### Dane
- **Parma:** 1W-1D-6L, 5 goli strzelonych i 15 straconych w 8 meczach, xG 0.92 / mecz, 16.75 strzalow straconych / mecz. U siebie 1W-1D-2L (3:6). Ostatnie: 0-2 Juventus, 1-1 Monza, 1-2 Como, 2-1 Genoa (w), 0-3 Inter, 0-3 Torino (d), 1-2 Lazio.
- **Udinese (Runjaic, pod presja):** 1W-1D-6L w tabeli (4 pkt), 9:18, 6 porazek z rzedu (1-2 Lazio, 3-5 Inter, 0-1 Cagliari, 1-2 Torino, 0-3 Lecce, 0-2 Milan). Na wyjazdach 1W-0D-2L (7:9), jedyna wygrana 3-2 w Monzy. xG 1.14 / mecz.
- **H2H:** MCP bez danych z 2025/26 (spotkania 29.11.2025 i 18.04.2026 wystepuja w WebSearch bez potwierdzonych wynikow) - nie wazono.
- **Informacje medialne:** Parma bez Nicolussi Caviglii, Almqvista, Elphege; Drobnic niejasny (DAZN: gotowy, bet365: kontuzjowany). Probabilny 3-5-2: Corvi; Delprato, Troilo, Ndiaye; Britschgi, Fabbian, Bernabe, Keita, Valeri; Lontani, Romero. Udinese bez Alaby, Gueye, Bayo, Solet (nie wraca; wg DAZN rowniez Zanoli), 3-4-2-1: Okoye; Abankwah, Kabasele, Palma; Vojvoda, Karlstrom, Miller, Kamara; Ekkelenkamp, Zaniolo; Davis. Brak zawieszonych. Zrodla (Sky/Goal/bet365) nie zgadzaja sie co do skladow - traktowac jako probabilne.
- **Sedzia:** Massa (VAR Mazzoleni). Statystyk kartek 2026/27 nie znaleziono; srednia 4.0 oparta na druzynach (ok. 3.3 zoltej z danych sezonu) i podniesiona wg rynku Pinnacle (O3.5 56%) oraz stawki meczu (dolne miejsca tabeli).

### Kalibracja
- Under 2.5 z poissona 61% -> 57% (nie dalej niz ok. 5 pp od rynku 54%): absencje obronne Udinese (Solet, Alaba) nie uzasadniaja wiekszej korekty, bo obie druzyny traca >1.9 gola/mecz.
- Obie druzyny w kryzysie; korekta kryzysowa dotyczy tylko underdoga, a tu brak faworyta (rynek 35/31/34), wiec 1X2 = "brak mocnego typu".
- Rynki zawodnika: bez potwierdzonych skladow, brak typow.

### Ryzyka
1. Mecz "o sześć punktow" na dole tabeli: duza zmiennosc (karny, czerwona kartka).
2. Obie druzyny traca bardzo duzo (Parma 1.9, Udinese 2.25 / mecz) - Over 2.5 (43%) moze byc niedoszacowany przy wynikach typu 2-2, 3-1.
3. Presja na Runjaicu - mozliwa zmiana ukladu, nieprzewidywalna reakcja.
4. Pewnosc wszystkich rynkow wynikowych niska.

**Rynek (Pinnacle):** 1X2 Parma 2.77 / X 3.15 / Udinese 2.87 (surowe); bez marzy 35.2 / 30.9 / 34.0. Total glowna 2.25 (O -117 / U +106), O2.5 +113, U2.5 -127. Team total 0.5: Parma O -314, Udinese O -302 (oba ok. 72%). Rozne 9.0: O -115 / U -102. Kartki 4.0: O +108 / U -130.

---

## 3. Venezia - Inter (Penzo, 18:30)

**Typ:** Inter wygra / Over 2.5 | pewnosc srednia (rotacja Interu przed derbami)

### Wycena (lambda Venezia 1.00, Inter 2.30; Inter obnizony wzgledem rynku o ok. 3 pp)
| Rynek | p | fair | Pinnacle (bez marzy) | pewnosc |
|---|---|---|---|---|
| Venezia wygra (1) | 14.5% | 6.90 | 12.7% | srednia |
| Remis | 18.5% | 5.41 | 17.4% | srednia |
| Inter wygra (2) | 67% | 1.49 | 69.9% (1.43) | srednia |
| DC 1X | 33% | 3.03 | - | srednia |
| DC X2 | 85.5% | 1.17 (graniczny 1.15-1.20) | 87.3% | srednia |
| DC 12 | 81.5% | 1.23 | - | srednia |
| Inter wygra 2+ golami | 43% | 2.33 | AH -1.5 ok. 48% | niska/srednia |
| Over 1.5 | 84% | 1.19 (graniczny) | ok. 86% | srednia |
| Over 2.5 | 65% | 1.54 | 68.3% | srednia |
| Under 2.5 | 35% | 2.86 | 31.7% | srednia |
| Over 3.5 | 44% | 2.27 | 47.2% | srednia |
| Under 3.5 | 56% | 1.79 | 52.8% | srednia |
| BTTS tak | 57% | 1.75 | ok. 59% | srednia |
| BTTS nie | 43% | 2.33 | - | srednia |
| Inter strzeli 2+ | 69% | 1.45 | ok. 73% | srednia |
| Rozne (srednia 9.8): Over 8.5 / 9.5 / 10.5 | 60% / 50.6% / 39% | 1.67 / 1.98 / 2.54 | linia 9.5: O +103 / U -122; O8.5 ok. 58% | niska/srednia |
| Rozne Inter 5.5+ (team total) | ok. 52% | 1.92 | O5.5 -125 | niska |
| Kartki zolte (srednia 3.5, Pairetto): Over 2.5 / 3.5 (4+) / 4.5 (5+) | 62% / 43% / 29% | 1.61 / 2.33 / 3.45 | Pinnacle: O2.5 61.9%, O3.5 41.9% | niska/srednia |
| Faule meczowe (srednia 20): Over 18.5 / Over 20.5 | 60% / 44% | 1.65 / 2.27 | brak | niska |

Najlepszy rynek meczu: Over 2.5 (65%, fair 1.54) lub Inter wygra (67%, fair 1.49). DC X2 (fair 1.17) i Over 1.5 (fair 1.19) graniczne.

### Dane
- **Inter (Chivu):** 7W-1D-0L, 23:10, xG 3.14 / mecz (najlepszy atak ligi). Ostatnie: 1-0 Cagliari (w), 3-2 Napoli (d), 5-3 Udinese (d), 2-2 Roma (w), 3-0 Parma (d), 3-1 Bologna (w), 2-1 Fiorentina (d). Wyjazdy 2W-1D-0L (6:3).
- **Venezia (Nicola):** 1W-0D-7L, 6:17. Ostatnie: 0-2 Milan, 2-3 Frosinone, 2-4 Fiorentina, 0-2 Lazio, 1-3 Atalanta, 1-0 Napoli (jedyna wygrana), 0-1 Genoa. U siebie 1W-0D-3L (3:8), xG 1.57 / mecz (6 goli z 12.6 xG), najwiecej zoltych w lidze (2.5 / mecz), 15.75 strzalow straconych / mecz.
- **H2H:** MCP bez danych z 2025/26 - nie wazono.
- **Informacje medialne:** Inter bez Lautaro Martineza, Stonesa, Pavarda, Jonesa, Luis Henrique (calciomercato.it, Sky). Chivu rotuje przed derbami z Milanem (31.10): Bastoni, Barella, Calhanoglu moga odpoczac; Thuram prawdopodobnie na laweczce. Probabilny 3-5-2: Provedel; Bisseck, Akanji, Carlos Augusto; Spence/Diouf, Sucic, Zielinski, Barella/Mkhitaryan, Dimarco; Bonny, Esposito. Venezia 3-5-2: Stankovic; Halhal, Moreno, Juan Jesus; Hainaut, Kike Perez, Sohm, Basic, Mazzocchi; Yeboah, Adams. Bez Sverko, Adorante, Franjic, Correia. Brak zawieszonych.
- **Sedzia:** Pairetto (VAR Camplone). Statystyk kartek 2026/27 nie znaleziono; srednia 3.5 oparta na druzynach (Venezia 2.5 + Inter 1.4 = 3.9, obnizona, bo mecz bedzie jednostronny i Inter rzadko faluje) i rynku.

### Kalibracja
- p Interu 67% vs rynek 69.9% (-3 pp): rotacja i brak Lautaro to konkretna informacja. Venezia w kryzysie (7 porazek) - korekta kryzysowa dotyczy underdoga, wiec p Venezii nie podnoszono za "desperacje"; 14.5% vs 12.7% wynika z rotacji.
- Ryzyko faworyta - dwie twarze: remis 18.5% i wygrana Venezii 14.5%.
- Rynki zawodnika (Bonny/Esposito, Dimarco, Adams/Yeboah): sklady niepotwierdzone, brak typow.

### Ryzyka
1. Rotacja Interu przed derbami (Thuram, Bastoni, Calhanoglu, Barella): mniej jakosci, ryzyko wyniku typu 1-0, 2-0 i kontrolowania meczu.
2. Debiut pary Bonny-Esposito, brak Lautaro - xG 3.14 moze nie przelozyc sie na wynik.
3. Venezia u siebie traci 2 gole / mecz, ale tez strzela (BTTS 57%).
4. Remis lub wygrana Venezii lacznie 33%; Venezia ma jedna wygrana w sezonie (1-0 z Napoli u siebie).
5. Rozbieznosc godziny (Sky 20:45 vs 18:30).

**Rynek (Pinnacle):** 1X2 Venezia 7.58 / X 5.55 / Inter 1.38 (surowe); bez marzy 12.7 / 17.4 / 69.9. Total glowna 3.5 (O +107 / U -118), O2.5 -242, U2.5 +204. Inter team total 2.5: O +108 / U -131; Venezia team total 0.5: O -201 (64%). Rozne 9.5: O +103 / U -122. Kartki: O2.5 -189 / U +149; O3.5 +126 / U -158.

---

## Tabela rynkow (skrot)

| Mecz | Rynek | p | fair | pewnosc |
|---|---|---|---|---|
| Milan - Bologna | Milan wygra | 53% | 1.89 | srednia |
| Milan - Bologna | DC 1X | 79.5% | 1.26 | srednia |
| Milan - Bologna | Under 3.5 | 78% | 1.28 | srednia |
| Milan - Bologna | Over 1.5 | 69% | 1.45 | srednia |
| Milan - Bologna | Under 2.5 | 56% | 1.79 | srednia |
| Milan - Bologna | BTTS nie | 54% | 1.85 | srednia |
| Milan - Bologna | Rozne Under 9.5 | 63% | 1.59 | srednia |
| Milan - Bologna | Kartki Over 2.5 (zolte) | 69% | 1.45 | niska/srednia |
| Parma - Udinese | 1 / X / 2 | 36 / 29.5 / 34.5% | 2.78 / 3.39 / 2.90 | niska (brak typu) |
| Parma - Udinese | DC 12 | 70.5% | 1.42 | niska |
| Parma - Udinese | Under 3.5 | 81% | 1.23 | srednia |
| Parma - Udinese | Over 1.5 | 68% | 1.47 | srednia |
| Parma - Udinese | Under 2.5 | 57% | 1.75 | niska/srednia |
| Parma - Udinese | Rozne Over 8.5 | 55% | 1.82 | niska/srednia |
| Parma - Udinese | Kartki Over 3.5 (4+) | 55% | 1.82 | niska/srednia |
| Venezia - Inter | Inter wygra | 67% | 1.49 | srednia |
| Venezia - Inter | DC X2 | 85.5% | 1.17 (graniczny) | srednia |
| Venezia - Inter | Over 1.5 | 84% | 1.19 (graniczny) | srednia |
| Venezia - Inter | Over 2.5 | 65% | 1.54 | srednia |
| Venezia - Inter | BTTS tak | 57% | 1.75 | srednia |
| Venezia - Inter | Inter 2+ gole | 69% | 1.45 | srednia |
| Venezia - Inter | Rozne Over 8.5 | 60% | 1.67 | niska/srednia |
| Venezia - Inter | Kartki Over 2.5 (zolte) | 62% | 1.61 | niska/srednia |

Typy z fair odds <= 1.15 pominieto. To sa oszacowania probabilistyczne, nie gwarancje.

---

<!-- źródło: an_seriea_2 -->
# Serie A, 9. kolejka, 28.10.2026 (środa) - analiza: Genoa-Juventus, Monza-Napoli

Źródła: MCP sportsdata (seriea_matches/standings/team_stats - Opta, pinnacle_matchup_markets), Sky Sport, Tuttosport, Eurosport, NapoliMagazine, Corriere dello Sport (przez WebSearch), Virgilio/Valuestats/Fichajes (sędziowie). BettingPros: nie użyty (brak klucza w sesji - pominięty). Kursy: Pinnacle (po usunięciu marży), kursów Betclic/gg397 nie sprawdzano.
Godzina: oba mecze 20:45 CET (19:45 UTC) - potwierdzone w seriea_matches (MCP), Tuttosport, Sky, Eurosport, Pinnacle.

Liga 2026/27 po 8 kolejkach: Juventus 7. (14 pkt, 11-8), Napoli 10. (11 pkt, 13-10), Monza 15. (7 pkt, 15-18), Genoa 16. (7 pkt, 6-13).

---

## 1) Genoa - Juventus (Stadio Ferraris, sędzia: Doveri)

**Typ główny:** Under 2.5 gola (60.9%, fair 1.64) / alternatywnie X2 (podwójna szansa, 77%) | **Pewność:** średnia (Under), niska-średnia (wynik)

### Parametry
λ Genoa 0.85, λ Juventus 1.40 (suma 2.25; rynek Pinnacle: Over 2.5 38.8% po de-vig, czyli podobnie).

Statystyki sezonu (Opta, 8 meczów): 
- Genoa: GF 6 (xG 8.0 = 1.00/m), GA 13 (xGA 10.9 = 1.36/m). U siebie 2W-1D-2L, 5-8. Ostatnio: 1-0 Venezia (dom), 2-0 przegrana z Romą, 2-1 Fiorentina. Rożne za 4.1/m, przeciw 5.4/m. Żółte kartki 19+1 czerwona (2.4/m), faule 10.0/m.
- Juventus: GF 11 (xG 12.0 = 1.50/m), GA 8 (xGA 4.5 = 0.56/m - świetna defensywa jakościowo). Na wyjeździe 2W-1D-1L, 6-4. Ostatnio: 2-0 Lecce (wyjazd), 1-1 Cagliari (wyjazd), 0-3 Lazio (dom), 2-0 Atalanta. Rożne za 7.5/m, przeciw 3.4/m. Żółte 9 (1.1/m), faule 12.9/m.

**H2H:** ostatni mecz 06.04.2026 Juventus-Genoa (Spalletti vs De Rossi) - wynik nie potwierdzony w źródłach, więc nie ważony. Stare H2H (sprzed 2023) nieistotne. Brak twardych danych H2H = ignoruję filar.

### Informacje medialne
- Genoa (De Rossi, 3-5-2, Sky/Tuttosport/GenovaToday): niedostępni Venturino, Havel, Sow, Wiafe (Corriere dello Sport wymienia też Ehizibue, Nuredini - niespójność źródeł, Tuttosport miał Wiafe w składzie, Sky pisze o jego urazie). Przewidywany skład: Bijlow; Marcandalli, Ostigard, Vasquez; Ellertsson, Baldanzi, Frendrup, Traore, El Shaarawy; Vitinha, Osmajic. Dyskwalifikacji brak.
- Juventus (Spalletti, 3-5-1-1): niedostępni wg Sky: Yildiz, Ekhator, Thuram, Locatelli, Grabara, Conceicao, Celik, Nico Gonzalez (osiem nazwisk, w tym główne opcje ofensywne i środek pola). Przewidywany skład: Vicario; Gatti, Bremer, Lucumi; Kalulu, McKennie, Douglas Luiz, Koopmeiners, Cambiaso; Alajbegovic; Woltemade (Kolo Muani vs Alajbegovic w ballottaggio). Ograniczone rotacje po 2-0 w Lecce. Dyskwalifikacji brak.
- Sędzia: Daniele Doveri (Rzym). 2025/26 Serie A: 3.42 żółtej/mecz, 0.13 czerwonej/mecz; kariera 3.90. Sezon 26/27 tylko 2 mecze (próba za mała).
- Mecz środkowotygodniowy dla obu (bez pucharów w tym tygodniu wg dostępnych źródeł).

### Rynek (Pinnacle, de-vig)
1X2: Genoa 18.2% (5.32) / remis 28.0% (3.46) / Juventus 53.8% (1.80). Total 2.0 (O -117/U +106); O2.5 2.48 / U2.5 1.575 -> Under 61.2%. Rożne: linia 9.0 (O -109/U -107), Genoa 3.5, Juve 5.5. Kartki (bookings): linia 3.0 (O -123/U +102).
Moje Juve 49.9% vs rynek 53.8% (-3.9 pp, w granicy 5 pp): różnica wynika z 8 absencji Juve; rynek już je ma w cenie, więc nie schodzę niżej.

### Tabela rynków (model: poisson.py λ 0.85/1.40; markets.py)
| Rynek | p | Fair | Pewność | Uwagi |
|---|---|---|---|---|
| 1 Genoa | 22.8% | 4.39 | niska | |
| X remis | 27.3% | 3.66 | niska | remis ≈ rynek 28% |
| 2 Juventus | 49.9% | 2.01 | niska-średnia | rynek 53.8% |
| 1X | 50.1% | 2.00 | niska | |
| X2 (remis lub Juve) | 77.2% | 1.30 | średnia | |
| 12 (bez remisu) | 72.7% | 1.38 | średnia | |
| Over 1.5 | 65.7% | 1.52 | średnia | |
| Under 1.5 | 34.3% | 2.92 | niska | |
| Over 2.5 | 39.1% | 2.56 | średnia | rynek 38.8% |
| Under 2.5 | 60.9% | 1.64 | średnia | rynek 61.2% |
| Over 3.5 | 19.1% | 5.25 | średnia | |
| Under 3.5 | 80.9% | 1.24 | średnia-wysoka | |
| BTTS tak | 43.1% | 2.32 | średnia | |
| BTTS nie | 56.9% | 1.76 | średnia | Genoa GF 0.75/m |
| Rożne (średnia 9.6) Over 8.5 | 59.9% | 1.67 | niska-średnia | |
| Rożne Over 9.5 | 48.2% | 2.07 | niska | linia rynku 9.0 |
| Rożne Under 10.5 | 62.8% | 1.59 | niska-średnia | |
| Rożne Under 11.5 | 72.6% | 1.38 | średnia | |
| Kartki (żółta=1; średnia 3.4) Over 2.5 | 62.0% | 1.61 | niska-średnia | Doveri |
| Kartki Over 3.5 | 42.8% | 2.34 | niska | |
| Kartki Under 4.5 | 73.0% | 1.37 | średnia | |
| Faule meczowe (średnia 22.9) Over 21.5 | 59.2% | 1.69 | niska | |
| Faule Under 24.5 | 63.7% | 1.57 | niska | |
| Rynki zawodnika | - | - | brak typu | składy niepotwierdzone, brak dwóch źródeł średnich |

Wyniki najbardziej prawdopodobne: 0-1 14.8%, 1-1 12.5%, 0-0 10.5%, 0-2 10.3%, 1-0 9.0%.

Uzasadnienie średnich: rożne - Genoa (4.1 za, 3.4 przepuszczone przez Juve -> 3.75), Juventus (7.5 za, 5.4 przepuszcza Genoa -> 6.4) = 10.1; skorygowane w dół do 9.6 (Juve bez Yildiza/Conceicao, mniej wrzutek; rynek 9.0, różnica 0.6 < 1.5). Kartki - Doveri 3.4-3.9 żółtej/m, drużyny razem ~3.5 (Genoa ostra 2.4, Juve 1.1) -> 3.4; rynek linia 3.0 (różnica 0.4 < 1).

### Ryzyka
- Pod Under 2.5: Juve ma doświadczonych atakujących poza grą, ale Genoa traci 1.6/m - jeden gol straconego przez Genoa i rzut karny/stały fragment dają 3 gole; Juve przegrywało z Lazio 0-3 i Sassuolo 2-3 (dwie wpadki w ostatnich 8).
- Pod Juve (wynik): zdziesiątkowany atak (Yildiz, Thuram, Gonzalez poza), Genoa wygrała dwa ostatnie mecze u siebie? (2-1 Fiorentina, 1-0 Venezia) - gospodarz w formie i De Rossi znaczy Spalletti-style intensywność; ryzyko dwustronne: remis (28%) ORAZ wygrana Genoa (23%).
- Kartki/faule: sędzia Doveri znany ale próba 26/27 minimalna; "pewność wysoka" niedostępna bez potwierdzonych składów.

**Rekomendacja:** brak mocnego typu na wynik (Juve ~50% = wyrównane). Najlepszy rynek meczu: Under 3.5 (80.9%, fair 1.24) i Under 2.5 (60.9%, 1.64, zgodne z rynkiem - brak przewagi nad rynkiem, ale solidna baza do kuponu).

---

## 2) Monza - Napoli (U-Power Stadium / Brianteo, sędzia: Ayroldi)

**Typ główny:** Napoli lub remis (X2) 74.5% / Over 1.5 80.1% / Over 2.5 57.7% | **Pewność:** średnia (gole), niska-średnia (wynik)

### Parametry
λ Monza 1.20, λ Napoli 1.80 (suma 3.0; rynek: linia 2.75, O2.5 58.0% po de-vig - zgodnie).

Statystyki sezonu (Opta, 8 meczów):
- Monza: GF 15 (xG 13.9 = 1.74/m), GA 18 (xGA 12.8 = 1.60/m; 6 goli z dystansu - najwięcej w lidze). U siebie 2W-0D-1L, 8-4 (wygrane 2-1 Sassuolo, 4-0 Cagliari; ostatnio 2-3 z Torino na wyjeździe). Rożne za 4.25/m, przeciw 4.75/m. Żółte 11+1 (1.5/m), faule 11.1/m. Varela: gol w każdym z 7 występów.
- Napoli: GF 13 (xG 16.3 = 2.03/m), GA 10 (xGA 11.2 = 1.40/m; 16.6 strzałów na bramkę rywala/m wobec 10.2 rok temu). Na wyjeździe 1W-1D-2L, 5-5. Ostatnio: 3-3 Roma (dom), 0-1 Venezia (wyjazd), 3-0 Frosinone. Rożne za 5.9/m, przeciw 5.1/m. Żółte 7 (0.9/m), faule 8.5/m.

**H2H (Eurosport/Opta):** Napoli wygrało 4 z ostatnich 6 meczów Serie A z Monzą (1 remis, 1 porażka); ostatnie trzy 7-2 łącznie; 4 czyste konta Napoli vs Monza. Skład Monzy 2026/27 inny niż w H2H sprzed lat, waga niska.

### Informacje medialne
- Napoli (trener formalnie Allegri - zawieszony na 2 mecze, Napoli zrezygnowało z odwołania wg Il Napolionline, na ławce Landucci; wpływ na wynik minimalny): niedostępni Buongiorno, Neres, Alisson Santos, Badiashile, Spinazzola (część "do oceny"), Favasuli (wraca ok. 12. kolejki). Di Lorenzo obolały po meczu z Bodo (zastąpi go Marianucci). De Bruyne prawdopodobnie odpoczywa (Lobotka w środku). Typowy skład: Milinkovic-Savic (wg Sky; Tuttosport/Eurosport podają Meret - niepotwierdzony bramkarz); Marianucci, Rrahmani, Marin, Olivera; Anguissa, Lobotka, McTominay; Politano, Hojlund, Giovane. Pewne: ofensywa z Hojlundem i McTominayem (31 goli we wszystkich rozgrywkach od debiutu), słabsza obrona (Rrahmani wraca).
- Monza (Juric, 3-4-2-1): niedostępni Pessina, Ziolkowski, Maye, Folorunsho (nie powołany wg Sky; Eurosport/NapoliMagazine mają go w składzie - niespójność). Skład: Tornqvist; Goglichidze, Lucchesi, Carboni; Birindelli, Foe Ondoa, Akinsanmiro, Mangas; Robinson, Mota; Varela. Dyskwalifikacji brak.
- Sędzia: Giovanni Ayroldi (Molfetta). 2025/26 (Fichajes): 10 meczów, 44 żółte = 4.4/m, 1 czerwona; sezon 26/27 brak danych. Napoli pod Ayroldim: 3W, 2R, 1P w 6 meczach.
- Napoli grało niedawno w Lidze Mistrzów z Bodo (data nie potwierdzona w źródłach; Sky pisze o stłuczeniu Di Lorenzo w tym meczu) i 24.10 zremisowało 3-3 z Romą; kalendarz gęsty, zmęczenie to ryzyko, ale forma Napoli jest już w kursie.

### Rynek (Pinnacle, de-vig)
1X2: Monza 21.5% (4.51) / remis 24.1% (4.02) / Napoli 54.4% (1.78). Total 2.75 (O -118/U +107); O2.5 -148 -> 58.0%, U2.5 42.0%; O3.5 +165 (36%). Rożne: linia 9.5 (O -102/U -116), Monza 3.5, Napoli 5.5. Kartki: linia 3.5 (O -134/U +111).
Moje Napoli 51.4% vs rynek 54.4% (-3.0 pp): korekta za absencje (5 graczy + Di Lorenzo + De Bruyne odpoczywa) zmieściła się w limicie 5 pp.

### Tabela rynków (poisson.py λ 1.20/1.80; markets.py)
| Rynek | p | Fair | Pewność | Uwagi |
|---|---|---|---|---|
| 1 Monza | 25.4% | 3.93 | niska | rynek 21.5% |
| X remis | 23.1% | 4.32 | niska | rynek 24.1% |
| 2 Napoli | 51.4% | 1.94 | niska-średnia | rynek 54.4% |
| 1X | 48.5% | 2.06 | niska | |
| X2 (remis lub Napoli) | 74.5% | 1.34 | średnia | |
| 12 (bez remisu) | 76.9% | 1.30 | średnia | |
| Over 1.5 | 80.1% | 1.25 | średnia-wysoka | |
| Under 1.5 | 19.9% | 5.02 | średnia | |
| Over 2.5 | 57.7% | 1.73 | średnia | rynek 58.0% |
| Under 2.5 | 42.3% | 2.36 | średnia | |
| Over 3.5 | 35.3% | 2.83 | średnia | rynek ~36% |
| Under 3.5 | 64.7% | 1.55 | średnia | |
| BTTS tak | 58.3% | 1.71 | średnia | Monza strzela u siebie 2.7/m, Napoli traci 1.25/m |
| BTTS nie | 41.7% | 2.40 | średnia | |
| Rożne (średnia 9.8) Over 8.5 | 62.1% | 1.61 | niska-średnia | |
| Rożne Over 9.5 | 50.6% | 1.98 | niska | linia rynku 9.5 |
| Rożne Over 10.5 | 39.4% | 2.54 | niska | |
| Rożne Under 11.5 | 70.6% | 1.42 | średnia | |
| Kartki (żółta=1; średnia 3.8) Over 2.5 | 68.7% | 1.46 | niska-średnia | Ayroldi |
| Kartki Over 3.5 | 50.2% | 1.99 | niska | rynek 3.5 O -134 (~54%) |
| Kartki Under 4.5 | 66.4% | 1.51 | niska-średnia | |
| Faule meczowe (średnia 19.8) Over 18.5 | 59.1% | 1.69 | niska | Napoli 8.5/m, Monza 11.1/m |
| Faule Under 21.5 | 65.4% | 1.53 | niska | |
| Rynki zawodnika | - | - | brak typu | składy niepotwierdzone; Varela (gol w 7/7 meczów) - seria, bez danych o strzałach nie wyceniam strzelca |

Wyniki najbardziej prawdopodobne: 1-1 10.8%, 1-2 9.7%, 0-1 9.0%, 0-2 8.1%, 2-1 6.5%.

Uzasadnienie średnich: rożne - Monza (4.25 za, 5.1 przepuszcza Napoli -> 4.7), Napoli (5.9 za, 4.75 przepuszcza Monza -> 5.3) = 10.0; w dół do 9.8 (Napoli bez Neresa i De Bruyne gorzej wrzuca; rynek 9.5). Kartki - Ayroldi 4.4 żółtej/m (próba 10 meczów), drużyny razem ~2.4 (Napoli bardzo czyste) -> 3.8; rynek 3.5 (różnica 0.3 < 1). Faule: 11.1 + 8.5 = 19.6 -> 19.8.

### Ryzyka
- Napoli (wynik): ryzyko dwustronne - remis (23%) ORAZ wygrana Monzy (25%); Monza w formie domowej (8-4 w 3 meczach u siebie), ale "nigdy nie wygrała 3 meczów domowych z rzędu"; Napoli 1W-1D-2L na wyjazdach, osłabione 5 absencjami i trzecim meczem w ciągu tygodnia.
- Over 2.5: scenariusz 1-0 lub 1-1 przy kontrolowanej grze Napoli bez De Bruyne; ale defensywy obu drużyn tracą > 1.25/m (Monza 2.25, Napoli 1.25 bramki/m).
- Under 1.5 małe ryzyko (19.9%).
- Niepewność składu (bramkarz Meret/Milinkovic-Savic, De Bruyne, Folorunsho) zmienia dokładne p o ~1-2 pp.
- Kartki: Ayroldi - próba 10 meczów, sezonu 26/27 brak.

**Rekomendacja:** najlepszy rynek meczu: Over 1.5 (80.1%, fair 1.25, krótki ale > 1.15); dalej Over 2.5 (57.7%, 1.73, zgodne z rynkiem - brak przewagi) i X2 (74.5%, 1.34). Wynik 1X2 - brak mocnego typu.

---

## Podsumowanie TOP (fair > 1.15)
1. Monza-Napoli Over 1.5 - 80.1%, fair 1.25, średnia-wysoka
2. Genoa-Juventus Under 3.5 - 80.9%, fair 1.24, średnia-wysoka
3. Monza-Napoli X2 - 74.5%, fair 1.34, średnia
4. Genoa-Juventus X2 - 77.2%, fair 1.30, średnia
5. Genoa-Juventus Under 2.5 - 60.9%, fair 1.64, średnia (zgodne z rynkiem)
6. Monza-Napoli BTTS tak - 58.3%, fair 1.71, średnia
7. Monza-Napoli Over 2.5 - 57.7%, fair 1.73, średnia

To oszacowania probabilistyczne, nie gwarancje.

---

<!-- źródło: an_atp_vienna -->
# ATP Wiedeń (Erste Bank Open, ATP 500, hala, twardy kort) - środa 28.10.2026 - analiza tennis-analyst

Źródła: apitennis (terminarz, ranking, H2H, statystyki meczowe SPW/RPW z ostatnich ~5 tygodni), Pinnacle (kursy, bez marży), WebSearch (kontuzje: Tiafoe, De Minaur; H2H Tien-De Minaur przez stringtension). BettingPros: nie użyty (brak klucza w sesji). Order of play NIEZWERYFIKOWANY - nie znaleziono oficjalnego planu na 28.10.2026.

## Godziny (rozbieżność źródeł)
| Mecz | apitennis (API) | Pinnacle (UTC -> CET, UTC+1) |
|---|---|---|
| Musetti - Tiafoe | 15:15 (druga wersja 15:30) | 14:00Z = 15:00 |
| Mensik - Mannarino | 17:00 (17:10) | 15:30Z = 16:30 |
| Rodionov - Basilashvili | 17:45 (18:00) | 16:30Z = 17:30 |
| Tien - De Minaur | 20:15 (20:30) | 19:00Z = 20:00 |
Wszystkie 4 mecze "nierozegrane" (status pusty). Godziny do potwierdzenia na erstebank-open.com / atptour.com.

## Uwaga metodologiczna o total gemów
Model punkt->gem->set daje ~25 gemów dla wyrównanego meczu, a Pinnacle wycenia 22.0-22.5 (po ~50/50). Model zawyża total o ~2.5 gema, a p_serve pochodzi z małych prób (4-13 meczów, różna jakość rywali). TOTAL GEMÓW: BRAK TYPU dla wszystkich 4 meczów. P_serve skalibrowano poziomem (~0.58-0.64) tak, by różnica między zawodnikami odpowiadała mojemu p zwycięstwa; to stosowane do rozkładu setów i handicapu gemowego (mniej wrażliwe niż total, ale nadal orientacyjne).

Statystyki sezonu/ostatnich tygodni (apitennis, mecze od 25.09; SPW = % pkt wygranych przy własnym serwisie, RPW = przy returnie): Musetti 70.8/36.5 (Lyon, 6 meczów, słabszy poziom), Tiafoe 68.7/30.1 (4 mecze), Mensik 70.3/34.9, Mannarino 64.7/36.6, Basilashvili 69.5/36.9 (13 meczów), Tien 65.1/34.9, De Minaur 66.6/37.2. Rodionov: 1 mecz w ostatnich 5 tygodniach (porażka w kwalifikacjach Lyon z Herbertem 7-6 5-7 0-6; SPW 58%, RPW 27%), brak próby.

---

### 1. Musetti (ATP 26) - Tiafoe (ATP 9 wg API) | R1 (1/16), hala, ~15:00 CET
**Typ:** Tiafoe wygra | **p:** 57% | **Fair:** 1.75 | **Pewność:** niska
- Zwycięzca: Tiafoe 57% (1.75) / Musetti 43% (2.33). Rynek Pinnacle bez marży: Tiafoe 56.0% / Musetti 44.0%.
- Wynik setowy: Tiafoe 2-0 30% (3.33), Tiafoe 2-1 27% (3.70), Musetti 2-1 22% (4.55), Musetti 2-0 21% (4.76).
- Zwycięzca 1. seta: Tiafoe 54.5% (1.83) / Musetti 45.5% (2.20).
- Handicap gemowy: Tiafoe -1.5 49.6% (2.02) | Musetti +1.5 50.4% (1.98); Tiafoe -2.5 43% (2.33); Tiafoe -3.5 34% (2.94). Pinnacle: Tiafoe -1.5 ~ 49/51 (zgodne).
- Total gemów: brak typu (patrz uwaga; Pinnacle 22.5 ~50/50).
- H2H: 3-3 wg API (Cincinnati 22.08.2026 Tiafoe 2-0, 7-6 7-5; RG 2025 Musetti 3-1; Cincinnati 2024 Tiafoe; Stuttgart 2023 Tiafoe; Rzym 2023 Musetti; Parma 2020 Tiafoe). Źródła zewnętrzne podają 4-4/3-3 (rozbieżność, nie liczy się bezpośrednio). Ostatnie spotkanie wygrał Tiafoe, na twardym.
- Kontuzje/zmęczenie: Tiafoe - operacja torbieli prawej dłoni po wycofaniu w Montrealu (sierpień 2026, puntodebreak 08.08.2026), od tego czasu grał (Cincinnati, Tokio R2 przegrana z Fils, Szanghaj R2 przegrana z Davidovichem 3 sety w tiebreakach); od 11.10 przerwa 17 dni bez meczu, brak informacji o nowym urazie; próba po powrocie mała. Musetti - wygrał turniej w Lyonie (finał w niedzielę 25.10 z Fritzem 6-3 6-4, wcześniej trzy mecze 3-setowe/tiebreakowe w QF-SF), czyli finał 3 dni przed meczem plus podróż: zgodnie z kalibracją -3 do -5 pp (zastosowane, ok. -3 pp od bazy ~46%).
- Ryzyka: Tiafoe po 17 dniach bez meczu i po operacji dłoni (wahania formy, serwis/forehand); Musetti w rytmie meczowym i z tytułem; małe próby statystyk.
- Rynek: Pinnacle Tiafoe 56.0% - moje p = rynek +1 pp, brak przewagi.

### 2. Mensik (ATP 16) - Mannarino (ATP 73) | R1/R2 (1/8 wg API), hala, ~16:30 CET
**Typ:** Mensik wygra | **p:** 78% | **Fair:** 1.28 | **Pewność:** średnia
- Zwycięzca: Mensik 78% (1.28) / Mannarino 22% (4.55). Rynek Pinnacle bez marży: Mensik 82.1% / Mannarino 17.9%.
- Wynik setowy: Mensik 2-0 48% (2.08), Mensik 2-1 30% (3.33), Mannarino 2-1 13% (7.69), Mannarino 2-0 9% (11.1).
- Zwycięzca 1. seta: Mensik 70% (1.43) / Mannarino 30% (3.33).
- Handicap gemowy: Mensik -1.5 72.6% (1.38); -2.5 66% (1.52); -3.5 55.7% (1.80); -4.5 41% (2.44). Mannarino +4.5 ~ 59% (1.70). Pinnacle: Mensik -3.5 ~ -162 (59% bez marży ~57%), zgodne.
- Total gemów: brak typu (Pinnacle 22.0 ~50/50).
- H2H: Mannarino 1-0 (Queen's, czerwiec 2026, 5-7 7-6(3) 7-6(5) - trawa, wg API 2-1 dla Mannarino). Jedyna próba, inna nawierzchnia.
- Statystyki/zmęczenie: Mensik wygrał R1 w poniedziałek 6-2 6-2 z Neumayerem (łatwo, 32/39 punktów przy serwisie wygranych), pełny odpoczynek; Mannarino przeszedł kwalifikacje (SF + finał w sobotę/niedzielę: Tirante 6-4 7-6, Molcan 7-5 6-2) i we wtorek wygrał R1 z Buse 0-6 7-5 6-4 (3 sety, 90 pkt serwisowych) - to jego 3. mecz w 4 dniach i 4. w 5 dniach. Mensik przegrał z Mannarino w Queen's w 3 setach z 2 tiebreakami (według API; własne obserwacje o stylu Mannarino - leworęczny, niewygodny - spoza danych, niepotwierdzone). Kontuzje: nie znaleziono doniesień o urazach (wyszukiwanie ogólne, nie specyficzne - pewność ograniczona).
- Dlaczego 78% a nie 82%: porażka z Mannarino w czerwcu (tiebreaki, mały margines), styl Mannarino; przeciwwaga: jego zmęczenie nie jest wystarczającym argumentem za faworytem (kalibracja) - stąd bez dodatkowej korekty w górę.
- Ryzyka: tiebreaki (oba mecze Queen's rozstrzygnęły się w tiebreakach), niewygodny styl Mannarino, możliwy luźniejszy serwis Mensika.
- Rynek: Pinnacle 82.1%; moje p ~4 pp niżej.

### 3. Rodionov (ATP 137, WC, Austria) - Basilashvili (ATP 95) | R1, hala, ~17:30 CET
**Typ:** Basilashvili wygra | **p:** 55% | **Fair:** 1.82 | **Pewność:** niska
- Zwycięzca: Basilashvili 55% (1.82) / Rodionov 45% (2.22). Rynek Pinnacle bez marży: Basilashvili 57.9% / Rodionov 42.1%.
- Wynik setowy: Basilashvili 2-0 28% (3.57), 2-1 26% (3.85), Rodionov 2-1 23.5% (4.26), Rodionov 2-0 22% (4.55).
- Zwycięzca 1. seta: Basilashvili 53% (1.89) / Rodionov 47% (2.13).
- Handicap gemowy: Basilashvili -1.5 47.6% (2.10); Rodionov +1.5 52.4% (1.91); Basilashvili -2.5 41% (2.43). Pinnacle: Rodionov +2.0 / Basilashvili -2.0 po -107 (50/50; zgodne w sensie braku przewagi).
- Total gemów: brak typu (Pinnacle 22.5 ~50/50; SPW Rodionova brak próby).
- H2H: Basilashvili 1-0 (Bukareszt, marzec 2026, 6-4 0-6 6-3; w Rodionov kwalifikacje Bukareszt). Inne źródło też pokazuje 1-0.
- Forma/zmęczenie: Basilashvili - finalista Almaty (niedziela 25.10, finał z Miedwiediewem 7-6 1-6 3-6), 6 meczów w tygodniu (w tym 3-setowy SF z Tsitsipasem), 3 dni odpoczynku plus przelot Almaty-Wiedeń; w ostatnich 5 tygodniach 13 meczów, SPW 69.5%, RPW 36.9% (dobre liczby na poziomie ATP, Szanghaj/Almaty/Chengdu). Zasada kalibracji "finał <=3 dni przed pierwszym meczem": -3 do -5 pp (zastosowane: baza ~59% -> 55%). Rodionov - gospodarz (WC), przegrał kwalifikacje w Lyonie 18.10, tylko 1 mecz od 25.09 (brak rytmu), ranking 137, publiczność, ale brak statystyk ATP z ostatnich tygodni.
- Ryzyka: Basilashvili po wyczerpującym tygodniu i podróży; Rodionov grający w domu, wysoki serwis, ale słaby return w ostatnim meczu (27%).
- Rynek: Pinnacle 57.9%; moje p 3 pp niżej wynika z konkretnego sygnału (finał 3 dni temu). Pewność niska, nie typ do TOP.

### 4. Tien (ATP 18) - De Minaur (ATP 10) | 1/8 (R2 wg API), hala, ~20:00 CET
**Typ:** brak typu (równy mecz) | **p:** Tien 50% / De Minaur 50% | **Fair:** 2.00 / 2.00 | **Pewność:** niska
- Zwycięzca: Tien 50% (2.00) / De Minaur 50% (2.00). Rynek Pinnacle bez marży: Tien 48.8% / De Minaur 51.2%.
- Wynik setowy: każdy z czterech wyników ~25% (fair 4.00): Tien 2-0 25%, Tien 2-1 25%, De Minaur 2-1 25%, De Minaur 2-0 25%.
- Zwycięzca 1. seta: Tien 50% / De Minaur 50% (2.00 każdy). Pinnacle: ~50/50.
- Handicap gemowy: każdy -1.5: 43% (2.33); +1.5: 57% (1.75); -2.5: 36.7% (2.72). Pinnacle: Tien +0.5 -111 / De Minaur -0.5 -101 (~50/50).
- Total gemów: brak typu (Pinnacle 22.5 ~50/50).
- H2H: brak meczów (pierwsze spotkanie, stringtension).
- Forma/zmęczenie/kontuzje: De Minaur - wycofał się z finału w Pekinie 6.10 (kontuzja pachwiny/przywodziciela, skany), potem zagrał Szanghaj (ćwierćfinał, przegrał z Zverevem), Wiedeń R1 w poniedziałek 26.10 wygrał z Machacem 1-6 6-4 6-3 (3 sety, po przegranym 1. secie 1-6, SPW 56% w meczu) - sygnał ryzyka fizycznego, nie potwierdzony nowym urazem. Tien - R1 w poniedziałek 26.10 wygrał z Van Assche 6-3 6-1 (bez wysiłku), debiut w Wiedniu, w tym sezonie wygrał Genewę (maj), ranking 18, ostatnie wyniki słabsze (Szanghaj R2 Ruud, Pekin Hurkacz 3 sety).
- Przesłanki: De Minaur jest wyżej w rankingu i ma lepszy return (RPW 37.2 vs 34.9), ale ma niepewne zdrowie i trudniejszy R1; Tien odpoczęty. Rynek 51/49 dla De Minaura - zgodny z moją oceną.
- Ryzyka: stan zdrowia De Minaura (Tien bardziej odpoczęty = lekka przewaga), a doświadczenie/obrona De Minaura na hali; obie strony ~równe.

---

## Tabela zbiorcza
| Mecz | Rynek | p | Fair | Pewność |
|---|---|---|---|---|
| Musetti - Tiafoe | Tiafoe wygra | 57% | 1.75 | niska |
| Musetti - Tiafoe | Tiafoe 2-0 / 2-1 | 30% / 27% | 3.33 / 3.70 | niska |
| Musetti - Tiafoe | Tiafoe wygra 1. set | 54.5% | 1.83 | niska |
| Musetti - Tiafoe | Tiafoe -1.5 gema | 49.6% | 2.02 | niska |
| Mensik - Mannarino | Mensik wygra | 78% | 1.28 | średnia |
| Mensik - Mannarino | Mensik 2-0 / 2-1 | 48% / 30% | 2.08 / 3.33 | średnia |
| Mensik - Mannarino | Mensik wygra 1. set | 70% | 1.43 | średnia |
| Mensik - Mannarino | Mensik -1.5 / -3.5 gema | 72.6% / 55.7% | 1.38 / 1.80 | średnia |
| Rodionov - Basilashvili | Basilashvili wygra | 55% | 1.82 | niska |
| Rodionov - Basilashvili | Basilashvili 2-0 / 2-1 | 28% / 26% | 3.57 / 3.85 | niska |
| Rodionov - Basilashvili | Basilashvili wygra 1. set | 53% | 1.89 | niska |
| Rodionov - Basilashvili | Basilashvili -1.5 gema | 47.6% | 2.10 | niska |
| Tien - De Minaur | Tien / De Minaur wygra | 50% / 50% | 2.00 | niska |
| Tien - De Minaur | każdy wynik setowy | 25% | 4.00 | niska |
| Tien - De Minaur | każdy -1.5 gema | 43% | 2.33 | niska |

Total gemów: nie podajemy w żadnym meczu (model +2.5 gema ponad linię rynku; p_serve z małych prób).

To oszacowania, nie gwarancje.

---

<!-- źródło: an_atp_basel -->
# ATP Bazylea (Swiss Indoors, ATP 500, hala, twarda), sroda 28.10.2026 - analiza (tennis-analyst)

## Order of play i tozsamosc
- Center Court (tennistourcalendar.com, godziny CET): 14:00 Borges-Ruud (R16), po nim Djokovic (4) - Humbert (R32), nie przed 18:00 Fritz (6) - Hijikata (R32, lucky loser), po nim Hurkacz (10) - Rune (R16).
- API (apitennis): Djokovic-Humbert 15:40, Fritz-Hijikata 18:00, Hurkacz-Rune 19:30. Borges-Ruud w API ruszyl o 14:10 i byl w 2. secie o ~15:00, wiec Djokovic realnie ok. 15:45-16:15; Fritz "not before 18:00"; Hurkacz po Fritzu (prawdopodobnie 19:30-20:30). Godziny niepotwierdzone przez organizatora (ATP/Swiss Indoors), tylko agregator + API.
- "N. Djokovic" = Novak Djokovic (apitennis player_key 1905; ten sam klucz co w Shanghai z Hurkaczem 09.10, Wimbledon z Sinnerem; ATP: 39 lat, bilans 2026 19-8, 11. w Race to Turin, pierwszy start w Bazylei od 2011). Potwierdzone.
- Uwaga: ATP nazywa ten Basel "1/16" = 1. runda (draw 32). Dla Djokovica i Fritza to pierwszy mecz turnieju.

## Zrodla (kluczowe)
apitennis (fixtures, H2H, ostatnie wyniki), tennistourcalendar.com (order of play + wyniki pon/wt), ATP Tour (preview Djokovic Basel), Sportskeeda/Dimers/Kalshi/Matchstat/Bleacher Nation (kursy, hold%), Tennis Tonic, Last Word on Sports. BettingPros: nie uzyte (brak klucza/tenis poza zakresem). Tennis Abstract: dane w JS nieaktualne (brak 2026), niewykorzystane. Kursy Pinnacle/TheOddsAPI nie sprawdzane (brak czasu/kluczy) - kursy tylko z publikacji tipsterow (US odds), niepewne.

## Brak twardych statystyk serwisu/returnu
Mamy: Djokovic 2026 SPW ok. 67-68%, hold ok. 85,5-86%, RPW ok. 35,6% (Dropshot/TennisStats/ATP - rozne okna), Hurkacz hold 89,9% 2026 (Sportskeeda), Fritz 14,2 asa/mecz, Hijikata 4,8 (Bleacher Nation). Brak porownywalnych hold/SPW dla Humberta, Hijikaty, Rune'a. Wniosek: p_serve = oszacowane czesciowo z danych, czesciowo z rankingu -> TOTAL GEMOW NIE PODAJEMY dla zadnego meczu (zasada SKILL.md). Handicap gemowy i wynik setowy wyliczone symulacja Monte Carlo (40k) z tych samych p_serve - orientacyjne.

---
## 1. Djokovic (N.) - Humbert (R32, 15:40 API / ok. 16:00 realnie)
Model (p_serve D 0.685 / H 0.66, po korekcie): zwyciezca Djokovic 62%.
- Ranking/forma: Djokovic 39 l., 19-8 w 2026, ostatnio Shanghai R32 przegrana z Hurkaczem 4-6 3-6 (09.10); przed tym Beijing QF (przegrana Zverev). 2026 return wyraznie slabszy niz kariera (RPW ok. 35,6% vs ok. 40%). Humbert: leworeczny, halowy (4 z 7 tytulow w hali), ale forma slaba: Lyon R1 (kwalifikacje/20.10) przegrana z Moutet 6-2 6-7 6-7 po 3h21, Shanghai R1 przegrana z Gea, Tokio R16 z Lehecka; ok. 1 wygrana na 7 meczow. Wczesniej w 2025 w Bazylei skreczyl w polfinale (plecy).
- H2H: Djokovic 1-0 (Wimbledon 2019 R16, 3 sety); nigdy na hali.
- Kontuzje (osobne zapytania): brak doniesien o kontuzji obu (wyszukiwanie nie znalazlo nic z 10.2026). Djokovic bez meczu od 09.10 (19 dni) = ryzyko rdzy; Humbert ma rytm (Lyon 20.10, 8 dni temu).
- Korekta: model ok. 66% -> -3 pp za przerwe >=2 tyg. vs rywal z rytmem (zasada SKILL.md) = 62-63%. Rynek: Sportskeeda -250/+190 (bez marzy ok. 67,5%), Kalshi 71%, Dimers 74%. Rozstep model/rynek ok. 5-12 pp -> bierzemy dolna czesc, pewnosc NISKA-SREDNIA.
- Rynki:
  - Zwyciezca: Djokovic 62% (fair 1.61), Humbert 38% (2.63)
  - Wynik setowy: 2-0 D 34% (2.94); 2-1 D 28% (3.57); 1-2 H 20% (5.0); 0-2 H 17.5% (5.7)
  - Zwyciezca 1. seta: Djokovic 58% (1.72), Humbert 42% (2.38)
  - Handicap gemowy: D -1.5 53.5% (1.87) / H +1.5 46.5% (2.15); D -2.5 44% (2.27); H +2.5 56% (1.78); H +3.5 68% (1.47)
  - Total gemow: BRAK (p_serve z rankingu/czesciowo)
- Ryzyka: Djokovic rdza i slaby return 2026, hala/szybki kort = wiecej tie-breakow (zmienna), Humbert serwis lewej reki; scenariusz 2-1 i tie-break; wiek 39.

## 2. Fritz (6) - Hijikata (LL) (R32, 18:00, nie przed)
Model (0.72 / 0.65): Fritz 79.5% -> przyjmuje 80%.
- Fritz: 13. ATP, 14,2 asa/mecz, dobry halowo. Przed Basel: finalista Lyon (przegrana z Musetti 3-6 4-6 w niedziele 25.10), bez straty seta do finalu; wczesniej Shanghai R32 (Arnaldi) i R16 (Tsitsipas), Tokio R16 (Munar). Historia kolana/obliczy 2026 (AO), brak nowej kontuzji po Lyon.
- Hijikata: ok. 85. ATP, lucky loser (przegral finał kwalifikacji z Hanfmannem 6-4 1-6 3-6 w niedziele; wygral wczesniej z Kecmanovicem 7-6 6-3 - 8 asow). Czyli 3 mecze w Bazylei w nogach, ma rytm i aklimatyzacje, ale slaby serwis (4,8 asa/mecz).
- H2H: Fritz 1-0 (Delray 2024, 2-0). 
- Korekty: Fritz gral Lyon final w niedziele (podroz Lyon-Bazylea, 2 dni odpoczynku, 5 meczow tydzien) -> -2 pp; rytm Hijikaty/LL kwalifikant (zasada kwalifikant dotyczy faworyta spoza top 30 - Fritz jest 13., wiec nie stosuje pelnej -4/-6, tylko -2/-3 za zmeczenie). Rynek: -800/+500 (bez marzy ok. 84%), Matchstat 84%. Moje 80% = lekko ponizej rynku (-4 pp), spojne z reguly "nie schodz pod rynek bez konkretow": konkret = zmeczenie Lyon + rytm LL. Pewnosc SREDNIA-WYSOKA dla zwyciezcy.
- Rynki:
  - Zwyciezca: Fritz 80% (1.25), Hijikata 20% (5.0)
  - Wynik setowy: 2-0 F 50% (2.0); 2-1 F 29% (3.4); 1-2 H 12% (8.3); 0-2 H 8.5% (11.8)
  - Zwyciezca 1. seta: Fritz 71% (1.41)
  - Handicap gemowy: F -1.5 72.5% (1.38); F -2.5 62.5% (1.60); F -3.5 47% (2.13); H +4.5 69% (1.45)
  - Total gemow: BRAK
- Ryzyka: zmeczenie po Lyon/podroz, kolano, rytm i swiezosc Hijikaty (serwis-wolej slice, 3 mecze w Basel), ryzyko tie-breakow (Fritz mocny serwis -> tie-break w kazdym secie).

## 3. Hurkacz (10) - Rune (R16, po Fritzu, ok. 19:30-20:30)
Model (0.715 / 0.68): Hurkacz 65.7% -> przyjmuje 65%.
- Hurkacz: hold 89,9% w 2026 (Sportskeeda), mocny na hali; finalista Chengdu (przegr. Davidovich Fokina), Beijing QF, Shanghai R16; Basel R32 wygrana wtorek 3-6 6-3 6-4 z Bergs (wiec 1 dzien przerwy, 3 sety). Historia: dwie operacje kolana, skret w Wimbledonie 2026 R16 vs Struff z bolem plecow/brzucha (ret. przy prowadzeniu 2-0), wycofanie z Libema (plecy) - ryzyko fizyczne ogonowe.
- Rune: comeback po zerwanej Achillesie (pazdziernik 2025), pierwszy start Davis Cup 09.2026; wyniki: Tokio R32 przegrana z Jacquet 3-6 1-6, Shanghai R64 przegr. Altmaier; Basel R32 wygral w pon. z Halys 6-4 6-7 7-6 (3 sety, ok. 3h). Nieznane Rune'a hold/SPW 2026 (probka za mala), brak ciaglosci meczowej -> duza niepewnosc, ale 2 dni odpoczynku vs 1 dzien u Hurkacza.
- H2H: Rune 1-0 (Paris 2022, 7-5 6-1 wg Matchstat; API pokazuje 2-0 Rune), bez znaczenia dla hali 2026.
- Rynek: Sportskeeda -200/+155 (bez marzy ok. 63%), Matchstat 59%. Model 74-81% (przy roznych p_serve) vs rynek 59-63% = rozstep >8 pp -> dolna czesc, 64-65%, pewnosc NISKA-SREDNIA. Bez twardych statystyk Rune'a i z ryzykiem zdrowotnym Hurkacza nie podnosimy p.
- Rynki:
  - Zwyciezca: Hurkacz 65% (1.54), Rune 35% (2.86)
  - Wynik setowy: 2-0 H 37% (2.70); 2-1 H 29% (3.45); 1-2 R 19% (5.3); 0-2 R 15.5% (6.5)
  - Zwyciezca 1. seta: Hurkacz 60% (1.67), Rune 40% (2.50)
  - Handicap gemowy: H -1.5 56.5% (1.77) / R +1.5 43.5% (2.30); H -2.5 45% (2.22); R +2.5 55% (1.82); R +3.5 69%? (H -3.5 31% -> R +3.5 69%, 1.45)
  - Total gemow: BRAK (SPW Rune'a nieznane)
- Ryzyka: Hurkacz zmeczenie/ciala (plecy, 3 sety wczoraj), duzo tie-breakow (2 serwisy), Rune zmienny/niezmeczony po Achillesie; Rune lepszy return i druga seria.

## Podsumowanie
| Mecz | Rynek | p | fair | pewnosc |
|---|---|---|---|---|
| Djokovic - Humbert | Djokovic wygra | 62% | 1.61 | niska-srednia |
| | Djokovic wygra 1. set | 58% | 1.72 | niska |
| | Handicap D -1.5 gem | 53.5% | 1.87 | niska |
| | Wynik 2-0 D | 34% | 2.94 | niska |
| Fritz - Hijikata | Fritz wygra | 80% | 1.25 | srednia-wysoka |
| | Fritz 2-0 | 50% | 2.00 | srednia |
| | Handicap F -2.5 gem | 62.5% | 1.60 | srednia |
| | Fritz wygra 1. set | 71% | 1.41 | srednia |
| Hurkacz - Rune | Hurkacz wygra | 65% | 1.54 | niska-srednia |
| | Hurkacz wygra 1. set | 60% | 1.67 | niska |
| | Handicap H -1.5 gem | 56.5% | 1.77 | niska |
| | Wynik 2-0 H | 37% | 2.70 | niska |

Total gemow: nie podajemy (p_serve oszacowane). To oszacowania, nie gwarancje.

---

<!-- źródło: an_esports_top -->
# Analiza e-sport, sroda 28.10.2026 (czas PL, CET = UTC+1)

Zrodla: Pinnacle (MCP sportsdata, kursy z marza usunieta proporcjonalnie, snapshot ok. 15:00 CET), WebSearch (esports.gg, strafe, dotesports, rg.org, estnn, Liquipedia - czesc stron 403), series.py. Brak PandaScore (brak tokena), brak kursow Dota 2 (Pinnacle ich nie listuje). Dane o mapach/draftach/skladach w sieci byly bardzo skape - pewnosc obnizona, p mocno zakotwiczone w rynku Pinnacle (zgodnie z regula "nie schodz pod rynek >5 pp bez konkretow").

Korekty do zalozen zlecenia:
- Liquid - FURIA: wedlug strafe mecz juz LIVE (start 15:00 CET, rynek serii i mapy 1 zamkniete na Pinnacle o 14:43 CET). Dane sprzed meczu.
- Spirit - NAVI jest runda 5 Swiss (2-2 o awans potwierdzone: Spirit przegral z MOUZ 1-2 po OT na Mirage 14:16, wczesniej 2-13 na Nuke; NAVI przegralo 0-2 z Vitality; Liquid przegral 1-2 z Aurora; FURIA wygrala 2-0 z TYLOO).
- LoL: KOI jest 2-1 (nie 2-2), T1 tez 2-1. Wygrana = awans do cwiercfinalow (T1 po R2 przegranej z Dplus KIA bo1, KOI po R3 0-2 z Dplus KIA). Start 21:15 CET (nie 21:00), bo3.
- Dota 2: Spirit - OG (16:00 CET) to upper bracket R1 playoff bo3 (nie faza grupowa). GamerLegion - LEGION: nie znalazlem potwierdzenia w zrodlach; w grupach byli osobno (GL grupa A: 3-1, mapy 6-3; LEGION grupa B: 1-3, mapy 2-7). Zakladam UB R1 bo3 (4. para obok Spirit-OG, Yandex-Astra, PARIVISION-Liquid) - NIEPOTWIERDZONE. Spirit to aktualny mistrz TI 2026, grupa 4-0 (8-1 mapy); OG 2-2 (5-5), wyeliminowani z TI 2026 przez GL 0-2.

## Wyniki (p = prawdopodobienstwo, fair = 1/p)

### CS2 Liquid - FURIA (PGL Masters Bucharest, Swiss R5, bo3, 15:00, LIVE)
p mapy FURIA: 0.60 / 0.61 / 0.63 (rynek no-vig: mapa2 60.9%, mapa3 64.1%, mapa1 ~61-62%; mapa1 i seria juz zamkniete). Model: FURIA 66.7%.
- Zwyciezca serii: FURIA 66.7% (fair 1.50) | Liquid 33.3% (3.00)
- Dokladny wynik: FURIA 2-0 36.6% (2.73), FURIA 2-1 30.1% (3.32), Liquid 2-1 17.7% (5.65), Liquid 2-0 15.6% (6.41)
- Handicap map: FURIA -1.5 36.6% (2.73); Liquid +1.5 63.4% (1.58); FURIA +1.5 84.4% (1.18, graniczny); Liquid -1.5 15.6% (6.41)
- Total map: Under 2.5 52.2% (1.92), Over 2.5 47.8% (2.09). Rynek: line 21.5 rund na mape (over -107/under -118 amer.) = ok. 22 rund; widelki 20-24.
- Zwyciezca mapy 2 FURIA 60.9% (rynek), mapa 3 FURIA 64.1% (rynek).
- Pewnosc: srednia-niska (brak map pool/veto, mecz live, wyrownany 2-2 decider). Typ wiodacy: FURIA do wygrania serii, bez mocnego typu na handicap.
- Ryzyka: Liquid ma doswiadczenie, pokonal MOUZ w R1; FURIA bywala niestabilna; rozstrzygnac mogly pierwsze mapy (juz grane). Sprawdz wynik live przed obstawieniem.

### CS2 Spirit - NAVI (PGL Masters Bucharest, Swiss R5, bo3, 18:00)
p mapy Spirit: 0.60 / 0.64 / 0.62 (rynek no-vig: mapa1 61.0%, mapa2 67.0%, seria 69.9%). Model: Spirit 67.7% (2 pp pod rynkiem: Nuke 2-13 z MOUZ + OT = brak sygnalu zmiany skladu, tylko lekki hair-cut).
- Zwyciezca serii: Spirit 67.7% (fair 1.48) | NAVI 32.3% (3.09)
- Dokladny wynik: Spirit 2-0 38.4% (2.60), Spirit 2-1 29.3% (3.42), NAVI 2-1 17.9% (5.58), NAVI 2-0 14.4% (6.94)
- Handicap map: Spirit -1.5 38.4% (2.60); NAVI +1.5 85.6% (1.17, graniczny); Spirit +1.5 ~93%+ (poza zakresem fair >1.15); NAVI -1.5 14.4% (6.94). Rynek: Spirit -1.5 42.7% no-vig.
- Total map: Under 2.5 52.8% (1.89), Over 2.5 47.2% (2.12). Rynek Over 43.8%.
- Zwyciezca mapy: Spirit 61-67% (mapa1 61%, mapa2 67%).
- Pewnosc: srednia. H2H historycznie Spirit przeciw NAVI bo3 (w 2024 NAVI nie wygralo bo3 z Spirit), ale dane sprzed zmian skladow - niska waga.
- Ryzyka: Spirit zawiodl na Nuke (2-13), presja 2-2, NAVI rozpedzone? (przegrali 0-2 z Vitality, wiec raczej nie); wyrownane jesli veto odda NAVI mocna mape.

### LoL Worlds 2026, Swiss R4: Movistar KOI - T1 (bo3, 21:15 CET, Allen TX)
Rynek (Pinnacle no-vig): T1 81.1%; mapa 1 T1 73.2%; 2-0 T1 56.8%; Under 2.5 62.8%. Moj p gry T1: 0.72 (2 pp pod rynkiem: T1 przegral z Dplus KIA w R2, ale to szum; KOI 0-2 z DK w R3 - slaba forma). Model: T1 80.9%.
- Zwyciezca serii: T1 80.9% (fair 1.24) | KOI 19.1% (5.23)
- Dokladny wynik: T1 2-0 51.8% (1.93), T1 2-1 29.0% (3.44), KOI 2-1 11.3% (8.86), KOI 2-0 7.8% (12.76)
- Handicap map: T1 -1.5 51.8% (1.93); KOI +1.5 92.2% (1.09, <1.15 - pomijac); KOI -1.5 7.8%; T1 +1.5 ~96%+ (pomijac)
- Total map: Under 2.5 59.7% (1.68), Over 2.5 40.3% (2.48)
- Zwyciezca gry: T1 72% (gra 1, rynek 73%); KOI ~28%.
- Pewnosc: srednia. T1 3-krotny obecny mistrz, KOI wygrali z BLG i CTBC (R1 pierwsze w historii udane otwarcie), ale 0-2 z Dplus KIA. Brak danych o patchu/draftach/skladzie T1.
- Ryzyka: bo3 z presja awansu dla obu (obie 2-1); KOI przeciwko T1 w EWC 2025 przegralo; stage fright u T1 w Swiss; sprawdzic side selection.

### Dota 2 PARI Universe (tier A), UB R1 bo3: Team Spirit - OG (16:00 CET)
Brak kursow. p gry Spirit 0.66 (forma: TI 2026 mistrz, grupa 4-0 8-1 mapy, pokonali PARIVISION 2-1; OG 2-2, mapy 5-5, przegrane z Yandex 0-2). Model: Spirit 73.2%.
- Zwyciezca serii: Spirit 73.2% (fair 1.37) | OG 26.8% (3.73)
- Dokladny wynik: Spirit 2-0 43.6% (2.30), Spirit 2-1 29.6% (3.38), OG 2-1 15.3% (6.55), OG 2-0 11.6% (8.65)
- Handicap map: Spirit -1.5 43.6% (2.30); OG +1.5 88.4% (1.13, <1.15 - pomijac); OG -1.5 11.6% (8.65)
- Total map: Under 2.5 55.1% (1.81), Over 2.5 44.9% (2.23)
- Zwyciezca gry: Spirit ~66% (gra 1).
- Pewnosc: srednia-niska (brak kursow i draftow; OG historycznie wyrownywali Spirit, ale w obecnej formie Spirit wyraznie lepszy). Ryzyka: OG ma doswiadczenie bo3, mozliwa roznica mety i draftu, patch.

### Dota 2 PARI Universe: GamerLegion - LEGION (19:00 CET, pair niepotwierdzona; zakladam UB R1 bo3)
Brak kursow. p gry GL 0.60 (GL 3-1 w grupie, 6-3 mapy, pokonali OG na TI 2026; LEGION 1-3, mapy 2-7, ale awansowali przez kwalifikacje i grali slabo vs Spirit/PARIVISION). Model: GL 64.8%.
- Zwyciezca serii: GamerLegion 64.8% (fair 1.54) | LEGION 35.2% (2.84)
- Dokladny wynik: GL 2-0 36.0% (2.78)... (z perspektywy LEGION=A: LEGION 0-2 36.0%), GL 2-1 28.8% (3.47), LEGION 2-1 19.2% (5.21), LEGION 2-0 16.0% (6.25)
- Handicap map: GL -1.5 36.0% (2.78); LEGION +1.5 84.0% (1.19, graniczny); LEGION -1.5 16.0% (6.25)
- Total map: Under 2.5 52.0% (1.92), Over 2.5 48.0% (2.08)
- Zwyciezca gry: GL ~60%.
- Pewnosc: NISKA (para nie zweryfikowana w zrodlach, brak kursow, malo danych o LEGION poza grupa).
- Ryzyka: pomylka co do pary/formatu; LEGION to najslabsza ekipa grupy B, lecz Dota jest losowa; stand-iny nieznane.

## Ogolnie
To oszacowania, nie gwarancje. Mocne typy sa tylko dla T1 (dokladny wynik 2-0 ~52% to jedyna wyraznie plusowa pozycja w stosunku do rynku? nie: fair 1.93 vs rynek ok. 1.76 - brak value) i serie zwyciezcow Spirit w CS2/Dota; Liquid-FURIA wyrownany i LIVE.

---

<!-- źródło: an_cs2_a -->
# CS2 niższe tiery, środa 28.10.2026 (czas PL CET, wszystkie bo3)

Źródła: PandaScore MCP (terminarz, wyniki; kursów brak - match_odds 404), Strafe, esports.ru, csdb.gg. HLTV/Liquipedia/bo3.gg niedostępne (403 / bot-check, którego nie obchodziłem). Brak: składów/stand-inów, map poolu, veta, H2H, kursów. Wszystkie p to oszacowania z formy i rankingu, pewność niska. Wszystkie mecze według PandaScore "not_started" (sprawdzone ok. 14:00 PL), więc żadnego nie pominięto jako rozpoczętego. Uwaga: NEM-EF startuje 15:00 PL, może już trwać w chwili czytania.

| Mecz (PL) | Rynek | p | fair | Pewność |
|---|---|---|---|---|
| 15:00 NEM - EF (Stake Ranked, LB R1) | EF wygra serię | 60% | 1.65 | niska-średnia |
| | EF +1.5 map | 81% | 1.23 | niska-średnia |
| | Total map Over 2.5 | 49% | 2.04 | niska |
| 17:00 FNC - BIG (Stake Ranked, UB semi) | FNC wygra serię | 56% | 1.79 | niska |
| | FNC +1.5 map | 79% | 1.27 | niska |
| | Total map Over 2.5 | 50% | 2.01 | niska |
| 19:30 ICE - MIBR (Stake Ranked, UB semi) | MIBR wygra serię | 55% | 1.81 | niska |
| | MIBR +1.5 map | 78% | 1.28 | niska |
| | Total map Over 2.5 | 50% | 2.01 | niska |
| 15:30 HOTU - GL (Tesla Cup B, winners') | GL wygra serię | 52% | 1.91 | bardzo niska (brak typu) |
| | GL +1.5 map | 76.5% | 1.31 | bardzo niska |
| 18:00 LG - ENVY (Tesla Cup B, elimination) | LG wygra serię | 59% | 1.70 | niska |
| | LG +1.5 map | 81% | 1.24 | niska |
| | LG -1.5 map (2-0) | 31% | 3.19 | niska |
| 21:00 decider (Tesla Cup B) | para niewyłoniona: przegrany HOTU-GL vs zwycięzca LG-ENVY. Bez wyceny. | - | - | - |
| 18:00 BLUEJAYS.de - LEI (DACH CS Masters S6) | BLUEJAYS wygra serię | 54.5% | 1.84 | bardzo niska |
| | BLUEJAYS +1.5 map | 78% | 1.28 | bardzo niska |
| 19:00 Rush - HR (GC Liga A, Group D, winners') | Rush wygra serię | 51.5% | 1.94 | bardzo niska (brak typu) |

Godziny zweryfikowane z PandaScore (UTC+1). Mecz Rush - HR był pierwotnie 26.10, przełożony na 28.10.

## Szczegóły

### NEM (Team Nemesis) - EF (Eternal Fire), Stake Ranked Ep.5, LB R1
- Forma NEM: 0-2 z ICE (27.10, mapy Nuke 13-5, Mirage 13-4), 0-2 z Brute (NODWIN Clutch, 27.10), 2-0 INOX, 2-0 mellren, 2-3 z Virtus.pro (finał CIS LAN, 23.10). Forma EF: 1-2 z MIBR (27.10), 2-1 Sinners (finał DraculaN, 23.10, EF wygrał turniej), 2-1 JiJieHao, 2-1 BC.Game. Mapy p_EF = 0.57. NEM przegrał dwa mecze z rzędu 0-2 (po zmęczeniu dnia przedtem), EF przegrał 1-2 po 3 mapach z MIBR - bez przewagi świeżości po żadnej stronie. NEM i EF wywalczyli miejsca w closed qualifier (wg skin.club pokonali Fnatic, który wszedł potem za B8). Składy niepotwierdzone (cs2news: "roster not formed", rdy.gg datowanie niepewne). H2H: brak w źródłach.
- Ryzyka: NEM urwał VP mapy na LAN; nieznane składy/stand-iny; Wariancja bo3.

### FNC - BIG (UB semi, bo3)
- FNC 2-0 Astralis (27.10), BIG 2-1 magic (27.10). Rankingi stycznia (nieaktualne): FNC ok. 18-23 miejsce, BIG ok. 35 (VRS regional); BIG wcześniej niespójny i słaby na Dust2. W Ep.4 obie drużyny odpadły w LB (FNC przegrał z Astralis, BIG z Luminosity i Astralis). p_mapa_FNC 0.54. Składy aktualne niezweryfikowane (zmiany: Maden w FNC, blameF w BIG według stycznia).
- Ryzyka: brak danych map poolu, BIG po 3-mapowym meczu dzień wcześniej (FNC 2-0, więc lekko świeższy: uwzględnione w 0.54 zamiast 0.52).

### ICE - MIBR (UB semi)
- MIBR: 2-1 EF, 1-2 NIP, 2-0 100 Thieves, 2-1 Astralis, 2-1 BC.Game (4W-1L). ICE: 2-0 NEM, 0-2 Sangal, 0-2 NIP, 2-0 Sangal, 1-2 3DMAX (2W-3L). Wspólny przeciwnik NIP: obie przegrały. MIBR p_mapa 0.535. Brak rankingów/składów w źródłach (esports.ru: bez nazwisk).
- Ryzyka: MIBR grał 3 mapy dzień wcześniej, ICE 2-0; wolno 50/50 - brak mocnego typu.

### Tesla Cup Group B (Belgrad, LAN, tier C)
- HOTU 2-0 LG (Mirage 13-11, Ancient 13-4), rank Strafe: HOTU #33, LG #57 (forma 6/10 vs 4/10). GL 2-1 ENVY (Dust2 13-6, Ancient 3-13, Nuke 13-10), rank GL #28-30 (forma 7/10), ENVY #96-102 (1/10). H2H HOTU-GL: 2-0 HOTU w 2025 (nieaktualne); HOTU wyeliminował GL w BLAST Bounty Summer closed qual 2026 (nagłówek bo3.gg). Rankingowo GL > HOTU, formą i H2H HOTU, więc 52/48 dla GL = brak typu.
- LG-ENVY: LG wyżej w rankingu (różnica ok. 40 miejsc) i lepsza forma; ENVY wygrał jedną mapę z GL 13-3. Mapa p_LG 0.56. Decider: zależnie od wyniku dwóch meczów wyżej.

### BLUEJAYS.de - LEI (DACH CS Masters S6, online, tier D)
- BJ 3W-3L (2-0 BIG Academy, 1-2 Regnum4Games, 0-2 Ducks, 2-0 SSP, 2-0 Huskies, 1-2 Entropy); LEI 2W-3L (2-0 Pandaric, 0-2 Entropy, 0-2 BIG Academy, 0-2 Ducks, 2-1 Regnum4Games). Wspólni rywale lekko na korzyść BJ. Brak H2H, składów, kursów. Bardzo cienkie dane.

### Rush - HR (Gamers Club Liga Série A, Group D, online, tier D)
- Brak jakichkolwiek wiarygodnych danych o formie w Group D październik (csdb niedostępny). HR (Hunters Rising) w czerwcu-lipcu: 1-2 z MIBR Academy, 0-1 z Borracheiros. Rush to nie ma o czym pisać. Brak typu, p 51.5% to praktycznie moneta.

Wszystkie to oszacowania, nie gwarancje. Wartość tych liczb jest niska: dla meczów tier D nie znalazłem żadnych kursów do porównania, więc nie wolno ich traktować jako EV.

---

<!-- źródło: an_cs2_b -->
# CS2 CCT Europe - bo3, 28.10.2026 (CET) - analiza

Dane CIENKIE (tier D, online, brak HLTV/Liquipedia/bo3.gg: 403). Źródła: esports.ru (strony drużyn i turnieju), strafe.com, wyniki z 18-27.10. Brak kursów, brak map poolu i veto, brak potwierdzonych składów. Wszystkie p oparte na formie i wspólnych przeciwnikach, p mapy 0.42-0.53 (bez przewagi). Brak mocnego typu w żadnym meczu.
SKR = Sökerorg; DXE = DimoniX Esports; HEC = Hermine Esports Club; AUR.YB = Aurora Young Blood.

| Mecz | Zwycięzca serii (p / fair) | Handicap map ±1.5 | Total map O2.5 | Pewność |
|---|---|---|---|---|
| 6yuBoJlbl - SKR (16:00) | 6yu 53% / 1.89; SKR 47% / 2.13 | 6yu +1.5 77% (1.30); SKR +1.5 73% (1.37) | 50% / 2.00 | niska |
| ex-RUSTEC - ILLYR (19:00) | RUSTEC 54.5% / 1.84; ILLYR 45.5% / 2.20 | RUSTEC +1.5 78% (1.28); ILLYR +1.5 72% (1.39) | 50% / 2.01 | niska |
| AUR.YB - DXE (17:30) | AUR 54.5% / 1.84; DXE 45.5% / 2.20 | AUR +1.5 78% (1.28); DXE +1.5 72% (1.39) | 50% / 2.01 | niska |
| Winx - X-CITY (17:30) | X-CITY 57.5% / 1.74; Winx 42.5% / 2.35 | X-CITY -1.5 30% (3.31); Winx +1.5 70% (1.43) | 49.5% / 2.02 | niska |
| SPARX - Nemesis Academy (20:15) | Nemesis 62% / 1.62; SPARX 38% / 2.62 | Nemesis -1.5 33.6% (2.97); SPARX +1.5 66% (1.51) | 48.7% / 2.05 | niska-średnia |
| HEC - TTG (20:15) | HEC 53% / 1.89; TTG 47% / 2.13 | HEC +1.5 77% (1.30); TTG +1.5 73% (1.37) | 50% / 2.00 | niska |

Wszystkie typy poniżej progu "mocnego typu"; handicap +1.5 dla faworyta ma fair 1.28-1.30 (powyżej 1.15, ale to wynik wyrównania, nie przewagi).

## Szczegóły

### 6yuBoJlbl - Sökerorg (Series #12, Swiss runda 5, 16:00)
p mapy 6yu 0.52. 6yuBoJlbl (KZ; tasman, stratefly, bluewh1te, Pump, neaLaN, ICY): 1-2 ILLYR (20.10), 2-1 ex-6666, 1-2 Saint Sinners, 2-0 mellren (26.10). Strafe: bez rankingu, 6/10 ostatnich. SKR (Sökerorg): w Series #12 W BakS 2-1, L FORZE 0-2, L Spirit Academy 0-2, W ex-6666 2-0; 4-6 w ostatnich 10. Wspólny przeciwnik ex-6666: 6yu 2-1, SKR 2-0 (neutralne). H2H brak. Ryzyka: SKR lista 9 nazwisk (niejasny skład/stand-iny), brak map poolu.

### ex-RUSTEC - ILLYRIANS (19:00)
p mapy RUSTEC 0.53. H2H: ex-RUSTEC 2-0 (18.10, Series #11). RUSTEC (Brilliance, bl1x1, youka, yiksrezo, relaxxie): w S#12 W mellren 2-0, W Saint Sinners 2-1, L FORZE 1-2, L Spirit Academy 0-2; 4-6 w ost. 10. ILLYR (ok. 7 nazwisk, niestabilny): W 6yu 2-1, L ACES 0-2, L BakS 1-2, W HAVU 2-0; 5-5. Sygnał: dwie ostatnie porażki RUSTEC to szum (słabsi/silniejsi rywale z Swiss), bez korekty; H2H 2-0 daje +1 pp. Ryzyka: motywacja w Swiss (stawka kwalifikacji nieznana), wahliwy skład ILLYR.

### AUR.YB - DXE (Contenders #10, LB R2, 17:30)
p mapy AUR 0.53. AUR: L 0-2 HEC (UB 1/8), W 2-0 Four Magic (LB R1). DXE: W 2-0 DINERO, L 0-2 Monte (UB 1/4, spadek do LB). Marka Aurora Young Blood ma dłuższą historię w CCT, stąd lekka przewaga; to sygnał słaby. Format w LB: bo3 wg zlecenia (qualifier miał bo1; format playoffów niezweryfikowany).

### Winx - X-CITY (17:30)
p mapy Winx 0.45. X-CITY: W SPARX 2-0, L 1-2 prodigy (UB 1/4, wyrównane), słabe wyniki poza turniejem (4-6 w ost. 10, brak info o składzie). Winx: L 1-2 Spirit Academy Black (UB 1/8, wyrównane), W 2-1 eSuba (LB R1). Różnica niewielka; X-CITY przewaga za jakość rywali (prodigy to finalista UB). Ryzyka: brak składów i statystyk.

### SPARX - Team Nemesis Academy (20:15)
p mapy SPARX 0.42. SPARX: L 0-2 X-CITY; awans do LB R2 oznacza wygraną z ZOTIX (esports.ru pokazuje 0-0, dane niespójne). Nemesis: W 2-0 eSuba, L 1-2 Spirit Academy Black w ćwierćfinale UB (blisko z czołówką). Najwyraźniejszy faworyt dnia, ale nadal tier D i brak danych o mapach.

### HEC - TTG Esports (20:15)
p mapy HEC 0.52. HEC: W 2-0 AUR, L 0-2 Ducks (UB 1/4, finalista). TTG: L 1-2 Monte, W 2-0 DINERO (LB R1). HEC lepsze wyniki z silniejszymi rywalami, ale TTG był blisko Monte. Wyrównane.

## Uwagi
- Odpadły/zmienione w zleceniu: mecz DXE to DimoniX Esports (esports.ru). Godziny: esports.ru podaje czas MSK/GMT+3 (CET = -2h). ex-RUSTEC - ILLYR 21:00 MSK = 19:00 CET, 6yu - SKR 18:00 MSK = 16:00 CET.
- Format Contenders #10 bo3 (bracket w zleceniu); qualifier miał bo1, więc zweryfikować przed użyciem handicapu/total.
- Brak kursów (pandascore wymaga tokenu, nie próbowano); brak kontroli rynku.
- To oszacowania, nie gwarancje.

---

<!-- źródło: an_cs2_esea -->
# CS2 ESEA Advanced Europe S59, bo1, sr. 28.10.2026 (CET)
Zrodla: PandaScore MCP (terminarz, bo1), profilerr.net (tabela, ranking tabeli). Brak HLTV/map pool/H2H/skladow/kursow. WSZYSTKIE p to szacunki bez solidnej podstawy (rank w tabeli ESEA + bilans W/L z 1-6 meczow), bo1 => p serii = p mapy.
| Mecz (CET) | Typ | p | fair | Pewnosc |
|---|---|---|---|---|
| 18:30 wnT - PG | PG | 65% | 1.54 | niska |
| 19:00 ENRAGE - Diamant | brak typu (ENRAGE 50%) | 50% | 2.00 | bardzo niska |
| 19:00 GamersLab - BJNG | GamersLab | 60% | 1.67 | niska |
| 19:00 Morrow - VIT.A | Morrow | 55% | 1.82 | niska |
| 19:00 SINQU - FOR | SINQU | 65% | 1.54 | niska |
| 19:30 wnT - NoTime | NoTime | 57% | 1.75 | niska |
| 20:30 aimers - Ryvex | brak typu (aimers 48%) | 48% | 2.08 | bardzo niska |
| 20:30 Diamant - FAL.F | FAL.F | 65% | 1.54 | niska |
| 20:30 FOR - BJNG | FOR | 58% | 1.72 | niska |
Podstawa: pozycje/bilans: FAL.F #16 2-0; SINQU #9 3-1; PG #19 2-4; GamersLab #21 2-3; Morrow #26 1-4; FOR #28 1-2; Ryvex #30 1-5; aimers #33 1-4; BJNG #41 0-1; NoTime #38 1-1; VIT.A #44 0-2; wnT #46 0-3. ENRAGE i Diamant brak w tabeli (S58: ENRAGE wygral z WBT; Diamant przegral z KUUSAMO.gg).
Ryzyka: bo1 wysoka loteria (p sciagniete do 50%), mozliwe stand-iny/rezerwy w drugorzednych skladach, FAL.F/VIT.A to akademie (zmienne sklady), nieznany map pool/veto, brak H2H i kursow. Mecze 18:30-19:00 CET moga juz trwac - nie zweryfikowano startu.
To oszacowania, nie gwarancje.

---

<!-- źródło: an_dota_low -->
# Dota 2 niższe tiery, bo3, środa 28.10.2026 (czas polski CET)

Źródła: PandaScore MCP (terminarz, wyniki 14-27.10), web (rdy.gg/Liquipedia zwracają 403, brak danych o składach, drafcie, patchu). Kursy: brak (pandascore_match_odds 404, brak kursów Betclic). Wszystkie mecze not_started w momencie analizy.
Ogólne: dane bardzo cienkie, większość drużyn to świeże wpisy (ID utworzone 26-27.10) bez historii. Brak H2H, brak danych o draftach/herosach/win rate per patch. P mapy to oszacowanie z ostatnich wyników i ściągnięcie do 50%; pewność wszędzie niska.

| Mecz | Rynek | p | Fair | Pewność |
|---|---|---|---|---|
| 16:00 SOLID - Team Synapse (Nexus S2 UB QF1) | Synapse wygra serię | 60,4% | 1.65 | niska |
| | Synapse -1.5 map (2-0) | 32,5% | 3.08 | niska |
| | Synapse +1.5 / SOLID +1.5 | 81,5% / 67,5% | 1.23 / 1.48 | niska |
| | Total map Over 2.5 / Under 2.5 | 49,0% / 51,0% | 2.04 / 1.96 | niska |
| 19:00 Zero Tenacity - Team Revenant (Nexus S2 UB QF2) | Zero Tenacity wygra serię | 60,4% | 1.65 | niska |
| | Z10 -1.5 | 32,5% | 3.08 | niska |
| | Z10 +1.5 / Revenant +1.5 | 81,5% / 67,5% | 1.23 / 1.48 | niska |
| | Over 2.5 / Under 2.5 | 49,0% / 51,0% | 2.04 / 1.96 | niska |
| 22:00 Chandogs - rebeldes (Nexus S2 UB QF3) | Chandogs wygra serię | 57,5% | 1.74 | niska |
| | Chandogs -1.5 | 30,3% | 3.31 | niska |
| | Chandogs +1.5 / rebeldes +1.5 | 79,8% / 69,7% | 1.25 / 1.43 | niska |
| | Over 2.5 / Under 2.5 | 49,5% / 50,5% | 2.02 / 1.98 | niska |
| 16:00 angry birds - Roshan Hunters (EPC S3 Gr. B) | angry birds wygra serię | 57,5% | 1.74 | niska |
| | angry birds -1.5 | 30,3% | 3.31 | niska |
| | angry birds +1.5 / RH +1.5 | 79,8% / 69,7% | 1.25 / 1.43 | niska |
| | Over 2.5 / Under 2.5 | 49,5% / 50,5% | 2.02 / 1.98 | niska |
| 19:00 Rottweilas Latam - Level Up Academy (EPC S3 Gr. B) | Rottweilas wygra serię | 53,0% | 1.89 | niska (brak mocnego typu) |
| | Rottweilas -1.5 | 27,0% | 3.70 | niska |
| | Rottweilas +1.5 / LUA +1.5 | 77,0% / 73,0% | 1.30 / 1.37 | niska |
| | Over 2.5 / Under 2.5 | 49,9% / 50,1% | 2.00 / 2.00 | niska |

Wejścia series.py (bo3, stałe p mapy dla pierwszej drużyny): Synapse 0.57, Z10 0.57, Chandogs 0.55, angry birds 0.55, Rottweilas 0.52.
Total map i handicapy przy p ~0.5-0.6 to praktycznie moneta (Over ~49-50%): bez przewagi. Typy z fair <= 1.15 brak; +1.5 dla faworytów (fair 1.23-1.25) jedyny rynek "bezpieczniejszy", ale bez kursów nie wiadomo, czy ma wartość.

## Szczegóły

### SOLID - Team Synapse (Nexus Series S2 playoffs, UB QF, bo3, 16:00)
- Synapse (id 139124): znany bilans z PandaScore: EPL Masters Gr. B 4 wygrane serie (Dawn Bulls 2-1, Zero Tenacity 2-1, TheBot$ 2-0, i inne) vs porażki z CyberHero 1-2 i Yellow Submarine 0-2; DreamLeague playoffs (kwalifikacje): 2-0 White Sails, 0-2 OG, 1-2 Dawn Bulls. Regularny, grający od tygodni mid/low-tier.
- SOLID (PE, id 139457, profil z 26.10): brak jakichkolwiek wyników w bazie. Nieznany skład i forma.
- H2H brak. Draft/meta: brak danych. Synapse gra równolegle EPL Masters (zmęczenie, możliwa zamiana składów/priorytetów) - ryzyko.
- p map Synapse 0.57 (przewaga doświadczenia, nieznany przeciwnik, cap w stronę 50%).
- Ryzyka: SOLID może być pełnoprawnym zespołem z SA, który zna ping/meta regionu; Synapse spoza SA (ping online).

### Zero Tenacity - Team Revenant (Nexus S2 UB QF, bo3, 19:00)
- Z10 (RS, id 135854): bardzo aktywny, ale zmienna forma. Ostatnie 7 dni: EPC S3 Gr. A wygrane 2-1 Mena Warriors, 2-1 No Hoodwink, 2-0 oveA, 2-0 Pibbles Corp (26-27.10); EPL Masters: wygrane 2-0 TheBot$ (22.10), 2-1 Dawn Bulls (21.10), 2-1 Inner Circle x Insanity, 2-0 PuckChamp; porażki 1-2 Synapse (24.10), 0-2 CyberHero (x2), 0-2 Yellow Submarine, 1-2 Mena Warriors. Szeroki rozrzut, zwykle słabszy w EPL Masters (silniejszy poziom), mocny w EPC (słabszy poziom).
- Team Revenant (PE, id 139458): brak danych.
- Zmęczenie: Z10 grał 4 serie bo3 w 2 dni; w tym samym czasie ma mecze w EPC S3 - harmonogram nakładania się nieznany (ryzyko opóźnień/zamian). Uwzględnione obniżeniem p z ~0.60 do 0.57.
- Ryzyka: stand-in, kolizja terminów z EPC, nieznany Revenant.

### Chandogs - rebeldes (Nexus S2 UB QF, bo3, 22:00)
- Chandogs (PE, id 133237): DreamLeague kwalifikacje (14-15.10) 2-0 Hokori, 0-2 Skyreavers (czyli ocena ~średnia, region SA, gra u siebie w tej strefie czasowej/pingu). Najstarszy, znany zespół SA w tej parze.
- rebeldes (BR, id 139459, profil z 26.10): brak wyników.
- H2H brak. Ping/region: oba z Ameryki Południowej, brak przewagi pingu.
- p map Chandogs 0.55.
- Ryzyka: rebeldes może być sformowany pod turniej z mocnymi graczami (rebrand); Chandogs może mieć zmianę składu.

### angry birds - Roshan Hunters (EPC S3 Gr. B, bo3, 16:00)
- angry birds (id 139462): wczoraj 2-0 z Rottweilas Latam (27.10). Jedna seria = bardzo mała próba.
- Roshan Hunters (id 139461): brak danych.
- p map angry birds 0.55 (jedyny sygnał: wygrana 2-0 nad Rottweilas, który ma twardszą historię; ściągnięte do 50%).
- Ryzyka: tryb grupowy tier D, motywacja, możliwe stand-iny.

### Rottweilas Latam - Level Up Academy (EPC S3 Gr. B, bo3, 19:00)
- Rottweilas (PE, id 137808): DL kwalifikacje 1-2 Skyreavers (14.10), wczoraj 0-2 z angry birds (27.10). Nie wygrali ostatnio żadnej serii w naszych danych.
- Level Up Academy (id 139385): akademia organizacji Level UP (ogłoszona 3.10.2026 wg esports.ru), brak wyników; młody skład, często ambitna młodzież, lecz bez doświadczenia.
- Rottweilas dostają symboliczne 0.52 wynikające z historii, ale ich forma jest zła. Brak mocnego typu.
- Ryzyka: wszystkie.

## Uwagi końcowe
- Nie znaleziono kursów rynkowych (PandaScore odds 404), więc brak porównania z rynkiem. Gdy bukmacher da wyraźnie inny kurs (>10 pp różnicy), zakładaj, że rynek zna skład/stand-in, którego tu nie znamy, i nie dyskontuj marży.
- Oszacowania, nie gwarancje; pewność niska we wszystkich 5 meczach, więc jeśli trafią do kuponu, nie powinny mieć wysokiej stawki.

---

<!-- źródło: an_carabao_1 -->
# Carabao Cup R4, 28.10.2026 - analiza (football-analyst)
p = po 90 min (rynki gol/BTTS/rożne/kartki bez dogrywki), awans osobno. Fair = 1/p. Sędziowie nieznani (brak w źródłach), brak statystyk rożnych/kartek z 2 niezależnych źródeł, więc rożne/kartki = szkic, pewność niska. Pinnacle przez MCP nie zadziałał (serwer rozłączył się); kursy tylko z przeglądów (TNT Sports, toffeeweb).

## Man City - Brighton (20:30 CET, Etihad)
Wiadomości: City (Maresca) odpoczywają Haaland, Dias, Gvardiol, Anderson, Donnarumma po porażce 1-2 w Villa; w bramce Rulli, atak Samba/McAidoo; Semenyo kontuzja, Nunes wątpliwy (TNT, Yahoo/AOL, readmancity). Brighton: brak Mitomy, Azeeza, Fergusona, Tzimasa, Steele w bramce; 0 goli w 2 ostatnich ligowych meczach, 16 pkt (3. miejsce). H2H: City 21 z 36, Brighton nigdy nie wygrał na Etihad. City straciło w 4 ostatnich meczach (9 goli). λ 1.95 / 1.10 (rotacja obniża λ City z ~2.3 o ok. 15%).
| Rynek | p | fair | pewność |
|---|---|---|---|
| 1 | 57% | 1.75 | średnia |
| X | 22% | 4.58 | |
| 2 | 21% | 4.75 | |
| 1X | 79% | 1.27 | średnia |
| X2 | 43% | 2.33 | |
| 12 | 78% | 1.28 | |
| Over 1.5 | 81% | 1.24 | średnia |
| Over 2.5 | 59% | 1.70 | średnia |
| Under 2.5 | 41% | 2.43 | |
| Over 3.5 | 36% | 2.75 | niska |
| BTTS Tak | 57% | 1.75 | niska-średnia |
| Rożne (śr. 10.2) O 9.5 / U 10.5 | 55% / 56% | 1.82 / 1.78 | niska |
| Kartki (śr. 3.8) O 3.5 / U 4.5 | 50% / 66% | 1.99 / 1.51 | niska |
| AWANS City | 71% | 1.41 | średnia |
| AWANS Brighton | 29% | 3.45 | |
Rynek (TNT): City -1.5 @2.50 (imp. 40%), O3.5 @2.10, City+BTTS @2.70 (37%; moje ~35%: zgodne). Ryzyka: rotacja i młody atak (Samba), kontuzje Brighton ograniczają ich siłę, derby-puchar. Najlepszy rynek: Over 1.5 (fair 1.24, graniczny) lub awans City; Under 4.5 kartek niski kurs.

## Liverpool - Chelsea (21:00 CET, Anfield)
Wiadomości (livescore/Rush the Kop; Yahoo): Liverpool (Iraola wg źródeł) mocna rotacja: przew. Mamardashvili; Araujo, Gomez, Endo, Tsimikas; Gravenberch, Nyoni, Wirtz; Chiesa, Koumas, Ngumoha; Szoboszlai out, Wirtz po urazie wątpliwy. Chelsea (Alonso): brak Palmera (zawieszony), Joao Pedro, Reece'a Jamesa, E. Martineza, Chavarrii; przew. Penders; Fofana, Lacroix, Colwill; Neto, Henderson, Caicedo, Hato; Estevao, Rogers, Welbeck. Forma: Liverpool 2 wygrane ligowe z rzędu (2-0 Brighton), Chelsea 6-3 Leeds w pucharze, ale 0-2 u siebie z Tottenhamem. Skład Chelsea silniejszy niż Liverpoolu (młodzież), gospodarz +dom, razem niemal wyrównanie. H2H nie zebrane (źródła niespójne); waga niska. λ 1.25 / 1.35.
| Rynek | p | fair | pewność |
|---|---|---|---|
| 1 | 35% | 2.90 | niska |
| X | 26% | 3.79 | |
| 2 | 39% | 2.55 | |
| 1X | 61% | 1.64 | niska |
| X2 | 66% | 1.52 | niska |
| 12 | 74% | 1.36 | |
| Over 1.5 | 73% | 1.36 | średnia |
| Over 2.5 | 48% | 2.08 | |
| Under 2.5 | 52% | 1.93 | |
| Under 3.5 | 74% | 1.36 | średnia |
| BTTS Tak | 53% | 1.89 | niska |
| Rożne (śr. 10.6) O 9.5 / O 10.5 | 59% / 48% | 1.68 / 2.07 | niska |
| Kartki (śr. 4.2) O 3.5 / U 4.5 | 57% / 60% | 1.75 / 1.68 | niska |
| AWANS Liverpool | 47% | 2.12 | niska |
| AWANS Chelsea | 53% | 1.89 | niska |
Brak kursów w źródłach, brak porównania z rynkiem. Mecz wyrównany: brak mocnego typu wynikowego. Ryzyka: niepotwierdzone składy (rotacja obu), niepewny status Wirtza, Chelsea w kryzysie po porażce z Spurs (dotyczy faworyta/nie korygowane). Najlepszy rynek: Over 1.5 / Under 3.5 (niskie fair, ok. 1.36).

## Bournemouth - Aston Villa (20:45 CET, Vitality)
Wiadomości: Villa (Emery) mocna rotacja (Suzuki, Lindelof, Cash, Kamara, J. Gomes, McGinn, Manzambi, Jackson na ławce; w składzie Goretzka, Madjo), brak Wan-Bissaki, Ruggeriego, Onany; Bournemouth bez Araujo, Toth, Scotta (Kroupi wraca), forma: 4 wygrane z rzędu, 3-0 na Man Utd, ale 10 straconych w 5 meczach. Villa bez porażki w 7 ostatnich H2H (5W 2D), 4 ligi bez porażki (m.in. 2-1 z City). Kursy 1X2 (toffeeweb, 5 bukm.): ok. 2.2-2.6 / 2.4-3.5 / 2.8-3.2, po usunięciu marży ok. 41/28/31; Under 2.5 @2.1-2.2, BTTS Tak 1.50-1.57 (~62%), Over 2.5 @1.65. λ 1.40 / 1.30 (rotacja Villi vs. kondycja Bournemouth, dom).
| Rynek | p | fair | pewność |
|---|---|---|---|
| 1 | 39% | 2.54 | niska-średnia |
| X | 26% | 3.88 | |
| 2 | 35% | 2.87 | |
| 1X | 65% | 1.53 | niska-średnia |
| X2 | 61% | 1.64 | |
| 12 | 74% | 1.35 | |
| Over 1.5 | 75% | 1.33 | średnia |
| Over 2.5 | 51% | 1.97 | niska |
| Under 2.5 | 49% | 2.03 | |
| Under 3.5 | 71% | 1.40 | średnia |
| BTTS Tak | 57% | 1.75 | niska-średnia (podniesiono z 55% do 57%, rynek ~62%) |
| Rożne (śr. 10.0) O 9.5 / U 10.5 | 53% / 58% | 1.89 / 1.71 | niska |
| Kartki (śr. 4.0) O 3.5 / U 4.5 | 54% / 63% | 1.86 / 1.59 | niska |
| AWANS Bournemouth | 52% | 1.92 | niska |
| AWANS Villa | 48% | 2.08 | niska |
Moje 1X2 w granicach 2 pp od rynku. Mecz wyrównany, brak mocnego typu. Ryzyka: sprzeczne źródła o trenerze Bournemouth; dwa źródła o wyniku sprzeczne co do goli (Under 2.5 @2.1 vs BTTS 1.5: niespójne, rynek sam nie zdecydowany); rotacja Villi może dać mecz otwarty. Najlepszy rynek: Over 1.5 / Under 3.5.

Dogrywka/karne: przy remisie po 90 min zakładam 64% awans dla City, ~48-50% dla pozostałych (rozkład 50/50 w karnych, lekka przewaga lepszego składu).
To są oszacowania probabilistyczne, nie gwarancje.

---

<!-- źródło: an_carabao_2 -->
# Carabao Cup, 4. runda, 28.10.2026 (20:45 CET): Fulham - Crystal Palace, Sunderland - Brentford

Uwaga o danych: MCP sportsdata rozłączył się w trakcie (udało się tylko ESPN terminarz i lista Pinnacle; markets Pinnacle niedostępne). Reszta z sieci (readcrystalpalace, VAVEL, Betfred, SportsGambler, LiveScore, 365Scores, Wincomparator). Sędziowie nieogłoszeni/nieznalezieni. Brak danych o rożnych/kartkach drużyn, więc średnie to szacunki ligowe (pewność niska). BettingPros: nie używany (brak klucza/zapytania).
Skład "p po 90 min" to wynik regulaminowy; "awans" uwzględnia dogrywkę i karne (remis po 90' ≈ 50/50, lekka przewaga gospodarza na karnych).

## 1. Fulham - Crystal Palace (Craven Cottage)
**Dane:** Fulham (trener Arbeloa) wygrał 1-0 z Hull i 1-0 z Coventry (wyszedł ze strefy spadkowej), w poprzedniej rundzie 3-2 z West Ham; ostatnie 5: 3W, 1,4 gola, xG 1,64 (365Scores). Arbeloa zapowiada mocny skład mimo Aston Villi w sobotę. Nieobecny Sessegnon (zawieszenie), wątpliwy Smith Rowe. Palace (trener Sage, pod presją): 17. miejsce, 2 wygrane w 8 meczach PL, najwięcej straconych goli w lidze, porażki z Lyon, Brighton, Newcastle 0-2, remis 2-2 z Besiktas; w poprzedniej rundzie 3-0 z Middlesbrough. Absencje Palace: Riad, Tomiyasu, Timber (kontuzje), Sarr (pachwina, prawdopodobnie nie zagra), Strand Larsen i Henderson wątpliwi; odeszli Lacroix, Johnson, Munoz, Devenny. Przewidywany skład Palace 5-4-1 (365Scores), ostatnie 5: 1W, xG 1,35.
**H2H:** Palace bez porażki w 9 ostatnich wizytach na Craven Cottage (6W, 3R), 4W+1R w ostatnich 5 meczach, w tym 3-2 wyjazdowa wygrana w tym sezonie; Fulham nie wygrał z Palace od 2005. Waga niska (inni trenerzy/składy), ale lekko ściąga p Fulham.
**Rynek (niepewne, Bet365 przez Wincomparator, nieodświeżone):** 2,25 / 3,40 / 3,00; po usunięciu marży 41,5 / 27,4 / 31,1%; Under 2,5 1,95 / Over 2,5 1,85.
**Model:** λ Fulham 1,45, Palace 1,15 (poisson.py dla 1,5/1,15 dał 45,3/25,6/29,1; zmniejszone o rotację pucharową i H2H na Cottage; do rynku różnica <5 pp, brak konkretu poniżej rynku).
Korekty pucharowe: obniżony pułap pewności o kilka pp (rotacja obu stron, Palace z głęboką ławką problemów kadrowych, ale Fulham rotuje też przed Villą). Kryzys dotyczy underdoga (Palace), ale kadrowy i formą już wliczony w kurs i λ.

| Rynek (po 90') | p | fair | pewność |
|---|---|---|---|
| 1 Fulham | 44% | 2.27 | niska-średnia |
| X | 26% | 3.85 | niska |
| 2 Palace | 30% | 3.33 | niska |
| DC 1X | 70% | 1.43 | średnia |
| DC X2 | 56% | 1.79 | niska |
| DC 12 | 74% | 1.35 | średnia |
| Over 1.5 | 74% | 1.35 | średnia |
| Over 2.5 | 49% | 2.04 | niska (brak typu) |
| Under 2.5 | 51% | 1.96 | niska (brak typu) |
| Over 3.5 | 27% | 3.70 | niska |
| BTTS tak | 53% | 1.89 | niska-średnia |
| BTTS nie | 47% | 2.13 | niska |
| Rożne, średnia ~10,2 (VMR 1,25): O 9.5 | 55% | 1.82 | niska |
| Rożne U 10.5 | 56% | 1.78 | niska |
| Rożne O 10.5 | 44% | 2.28 | niska |
| Kartki, średnia ~3,6 (sędzia nieznany): O 3.5 | 46% | 2.15 | niska |
| Kartki U 3.5 | 54% | 1.87 | niska |
| Kartki O 2.5 | 65% | 1.53 | niska |
| **Awans Fulham (dogr.+karne)** | 57% | 1.75 | niska-średnia |
| Awans Palace | 43% | 2.33 | niska-średnia |

**Najlepszy rynek meczu:** Over 1.5 gola (74%, fair 1.35) lub DC 1X; wynik 1X2 bez mocnego typu (Fulham ~44% przy rynku ~42%).
**Ryzyka:** Palace wygrywa dzięki H2H i przewadze jakości w ataku (Mateta, Pino); rotacja Fulham przed Villą; niski poziom pewności bez sędziego i potwierdzonych składów; remis i karne (~26% remis po 90').

## 2. Sunderland - Brentford (Stadium of Light)
**Dane:** Sunderland (trener Le Bris) ostatnio słaby: jedna wygrana w 6 meczach, ostatnia w 3. rundzie tego pucharu, 20. miejsce w PL (5 pkt; wg Betfred nawet dół tabeli), tylko 3 gole w 6 meczach u siebie, ostatnie 5: 0,6 gola, xG 1,24 (365Scores/Betfred/SportsGambler). Brak Ballarda (hamstring), Mundle (kolano), Danso (zawieszony); Isidor test, Meunier może wrócić. Brentford: 6. miejsce (11 pkt), niepokonany na wyjazdach w 6 meczach, 2-1 w Reading w pucharze, 1-1 z Hull; ostatnie 5: 1,8 gola, xG 1,95, BTTS w 4/5. Brak Dasilvy, Furo, Milambo, Yarmolyuk zawieszony, Janelt wraca; Wilson strzelił pierwszy w obu pucharowych meczach. Przewidywane składy z rotacją po obu stronach (365Scores).
**H2H:** Brentford 3-0 (sty. 2026), 1-1 (wrz. 2026), Sunderland 2-1 (sie. 2025). Waga niska.
**Rynek (SportsGambler, 27.10):** 3,45 / 3,50 / 2,02; bez marży 27,1 / 26,7 / 46,2%. BTTS tak 1,64 (~57%), Over 2.5 1,79 (~52%). Awans bet365: Brentford 8/15 (~61% po marży), Sunderland 11/8. Brentford Under 5,5 rożnych 1,65.
**Model:** λ Sunderland 1,05, Brentford 1,50 (poisson 26,5/25,9/47,6); wycena zgodna z rynkiem w 1X2. BTTS i Over świadomie ~4-5 pp pod rynkiem: konkret to 0,6 gola/mecz i 3 gole w 6 domowych meczach Sunderlandu (nie sama nieobecność graczy).
Korekty pucharowe: obniżony pułap pewności; rotacja po obu stronach; faworyt wyjazdowy to Brentford (underdog Sunderland w kryzysie formy: odjęte ~2 pp od wygranej gospodarza względem formy ligowej, bez ruszania p faworyta).

| Rynek (po 90') | p | fair | pewność |
|---|---|---|---|
| 1 Sunderland | 27% | 3.70 | niska |
| X | 26.5% | 3.77 | niska |
| 2 Brentford | 46.5% | 2.15 | niska-średnia |
| DC 1X | 53.5% | 1.87 | niska |
| DC X2 | 73% | 1.37 | średnia |
| DC 12 | 73.5% | 1.36 | średnia |
| Over 1.5 | 72% | 1.39 | średnia |
| Over 2.5 | 48% | 2.08 | niska (brak typu) |
| Under 2.5 | 52% | 1.92 | niska (brak typu) |
| Over 3.5 | 25% | 4.00 | niska |
| BTTS tak | 52% | 1.92 | niska |
| BTTS nie | 48% | 2.08 | niska |
| Rożne, średnia ~10,0: O 9.5 | 53% | 1.89 | niska |
| Rożne U 10.5 | 58% | 1.71 | niska |
| Rożne O 10.5 | 42% | 2.40 | niska |
| Kartki, średnia ~3,4 (sędzia nieznany): O 3.5 | 43% | 2.34 | niska |
| Kartki U 3.5 | 57% | 1.75 | niska |
| Kartki O 2.5 | 62% | 1.61 | niska |
| **Awans Brentford (dogr.+karne)** | 60% | 1.67 | średnia-niska |
| Awans Sunderland | 40% | 2.50 | niska-średnia |

**Najlepszy rynek meczu:** awans Brentford (~60%, fair 1.67) lub DC X2 (73%, fair 1.37); Over 1.5 (72%) jako alternatywa. Rynek awansu bet365 (~61%) zgodny z modelem, brak value.
**Ryzyka:** rotacja Brentfordu (brak Yarmolyuka, Dasilvy, Milambo); Sunderland u siebie w pucharze z motywacją na poprawę serii; mecz zamknięty (Sunderland strzela mało) kończący się 0-0/1-0 i karnymi; niski poziom wiedzy o sędzi i składach.

## Tabela zbiorcza (najmocniejsze, wszystkie pewność niska-średnia, ranking z fair > 1.15)
| Mecz | Rynek | p | fair | pewność |
|---|---|---|---|---|
| Fulham - Palace | Over 1.5 gola | 74% | 1.35 | średnia |
| Fulham - Palace | DC 1X | 70% | 1.43 | średnia |
| Fulham - Palace | Awans Fulham | 57% | 1.75 | niska-średnia |
| Fulham - Palace | BTTS tak | 53% | 1.89 | niska-średnia |
| Sunderland - Brentford | DC X2 | 73% | 1.37 | średnia |
| Sunderland - Brentford | Over 1.5 gola | 72% | 1.39 | średnia |
| Sunderland - Brentford | Awans Brentford | 60% | 1.67 | średnia-niska |
| Sunderland - Brentford | Brentford wygra po 90' | 46.5% | 2.15 | niska-średnia |

Kursy Fulham - Palace są niepotwierdzone (Wincomparator/Bet365, być może nieaktualne); sprawdzić live przed kuponem. To oszacowania probabilistyczne, nie gwarancje.

---

<!-- źródło: an_dfb_1 -->
# DFB-Pokal 2. runda, śr. 28.10.2026, 20:45 CET (19:45Z) - analiza 4 meczów

Źródła: ESPN (scoreboard, summary, standings, lastFiveGames, H2H), DraftKings przez ESPN (kursy odniesienia, bez marży); MCP sportsdata padł w trakcie (Pinnacle niedostępny), WebSearch nie dał składów/kontuzji/sędziów. Brak: potwierdzonych składów, sędziów, xG, statystyk rożnych/kartek (średnie rożnych/kartek to szkice ze średnich ligowych, pewność niska). BettingPros: nie użyty. Gospodarz Kiel - Hoffenheim: potwierdzono Holstein Kiel (Holstein-Stadion), Hoffenheim gość. "p 90 min" = po 90 min (bez dogrywki); awans osobno (dogrywka/karne: faworyt ok. 50-55% w karnych, w dogrywce lekka przewaga).
Uwaga: mecz Kompany/Bayern - ESPN News: Kompany po hospitalizacji "improving day by day", Danks (asystent) mówi; Musiala - problem neurologiczny (niepewny). Niepotwierdzone, wpływ kadrowy nieznany.

## Leverkusen - Nürnberg (BayArena)
Forma: Lev. 4. w BL (7 m: 16-12), W/W/W/W i porażka 0-3 z Hoffenheim w niedzielę (25.10), czwartek 22.10 EL (OFI) = zmęczenie/rotacja. Nürnberg 2. w 2.BL (9 m: 21-12), ostatnio 4-4 Wolfsburg, 1-1 Cottbus, 0-1 z Kaiserslautern (24.10). H2H: Lev. 4-1-0 w ostatnich 5 (stare, 2019). Rynek (DK, fair bez marży): 1 74,9 / X 14,6 / 2 10,5; O/U 3,5: Over ok. 55%. Moje p ok. 3 pp poniżej rynku (rotacja po EL + niedzielna porażka).
Model λ 2.7 / 1.05.

| Rynek | p | fair | pewność |
|---|---|---|---|
| 1 (90') | 72,2% | 1.38 | średnia |
| X | 15,5% | 6.44 | |
| 2 | 12,3% | 8.16 | |
| 1X | 87,7% | 1.14 | średnia |
| X2 | 27,8% | 3.60 | |
| 12 | 84,5% | 1.18 | |
| Awans Lev. | 83,5% | 1.20 | średnia (cup, rotacja) |
| Awans Nürnberg | 16,5% | 6.06 | |
| Over 1.5 / Under 1.5 | 88,8% / 11,2% | 1.13 / 8.95 | średnia |
| Over 2.5 / Under 2.5 | 72,3% / 27,7% | 1.38 / 3.61 | średnia |
| Over 3.5 / Under 3.5 | 51,6% / 48,4% | 1.94 / 2.07 | niska (blisko 50%) |
| BTTS tak / nie | 60,6% / 39,4% | 1.65 / 2.54 | średnia |
| Rożne śr. 10.4: Over 9.5 / Over 10.5 | 57,3% / 46,1% | 1.75 / 2.17 | niska (brak danych) |
| Kartki śr. 3.8 (sędzia nieznany): Over 3.5 / Over 4.5 | 50,2% / 33,6% | 1.99 / 2.98 | niska |
Ryzyka: Lev. po EL i porażce 0-3 (rotacja, wolniejsza defensywa 12 straconych w 7), Nürnberg silny ofensywnie (2,3 gola/m) - remis i niespodzianka równie realne; gol po 80'.

## Bayern - Magdeburg (Allianz Arena)
Forma: Bayern 1. w BL (25-6 w 7 m), 6-1 z Lipskiem, 3-1 Freiburg; w LM 2-2 z Arsenalem 21.10. W 1. rundzie 4-1 z Osnabrück (po stracie gola). Magdeburg 5. w 2.BL (20-12), 6-1 z KSC w sobotę, ale 0-2 Drezno. H2H nieznane. Rynek: 1 90,5 / X 6,3 / 2 3,2; O/U 4,5: Over ok. 56% (DK ma Bayern -2500). Mój total niżej o ok. 4 pp (rotacja przy 3 meczach w tygodniu, niepewność Kompany/Musiala).
Model λ 3.9 / 0.8 (dla Over 4.5 łączne λ 4.7).

| Rynek | p | fair | pewność |
|---|---|---|---|
| 1 (90') | 89,5% | 1.12 | wysoka (fair ≤1.15 - nie do rankingu) |
| X | 6,9% | 14.5 | |
| 2 | 3,6% | 28.0 | |
| 1X | 96,4% | 1.04 | |
| 12 | 93,1% | 1.07 | |
| Awans Bayernu | 95,5% | 1.05 | wysoka |
| Awans Magdeburg | 4,5% | 22.2 | |
| Over 1.5 | 94,8% | 1.05 | wysoka |
| Over 2.5 / Under 2.5 | 84,7% / 15,3% | 1.18 / 6.55 | wysoka/średnia |
| Over 3.5 / Under 3.5 | 69,0% / 31,0% | 1.45 / 3.22 | średnia |
| Over 4.5 | 51% (rynek ok. 56%) | 1.96 | niska |
| BTTS tak / nie | 53,9% / 46,1% | 1.85 / 2.17 | niska (Magdeburg strzela 2,2/m, ale Bayern dominuje) |
| Rożne śr. 11.5: Over 10.5 / Over 11.5 | 58,0% / 47,3% | 1.72 / 2.11 | niska |
| Kartki śr. 2.9: Over 2.5 / Over 3.5 | 52,3% / 33,2% | 1.91 / 3.01 | niska (mecz jednostronny, sędzia nieznany) |
Ryzyka: rotacja Bayernu między LM a ligą, wczesna strata gola (jak z Osnabrück), niepewność kadrowa (Kompany w szpitalu, Musiala); wygrana Bayernu pewna, ale kursy ultra krótkie - wartość tylko na totalach/rożnych.

## Hannover 96 - Kaiserslautern (HDI Arena)
Forma: Hannover 16. w 2.BL (8-15 w 9 m), 0-3 z Magdeburgiem, 1-1 St. Pauli, 0-2 z Braunschweig (25.10). Kaiserslautern 3. (9-4 w 9 m), 4 m. bez porażki, 1-0 z Nürnberg (24.10), 0-0 Heidenheim. H2H: seria 2-2-1 (ostatni mecz 18.01.2026: FCK wygrał u siebie). Rynek: H 42,0 / X 25,5 / A 32,6; Over 2,5 ok. 60% (podejrzanie wysoko przy 2,5 gola/m w obu - to miękka linia, nie schodzę do rynku). Kryzys dotyczy underdoga: Hannover (gospodarz) po 3 słabych meczach, ale rynek i tak daje mu faworyta; moje 1X2 blisko rynku (+2 pp dla H).
Model λ 1.45 / 1.15.

| Rynek | p | fair | pewność |
|---|---|---|---|
| 1 (90') | 44,0% | 2.27 | niska (brak mocnego typu) |
| X | 26,0% | 3.84 | |
| 2 | 30,0% | 3.34 | |
| 1X | 70,0% | 1.43 | niska/średnia |
| X2 | 56,0% | 1.79 | |
| 12 | 74,0% | 1.35 | |
| Awans Hannover | 57,5% | 1.74 | niska |
| Awans Kaiserslautern | 42,5% | 2.35 | |
| Over 1.5 / Under 1.5 | 73,3% / 26,7% | 1.36 / 3.74 | średnia |
| Over 2.5 / Under 2.5 | 48,2% / 51,8% | 2.08 / 1.93 | niska (rynek: Over ok. 60%) |
| Over 3.5 / Under 3.5 | 26,4% / 73,6% | 3.79 / 1.36 | średnia |
| BTTS tak / nie | 52,3% / 47,7% | 1.91 / 2.10 | niska |
| Rożne śr. 9.6: Over 8.5 / Over 9.5 / Over 10.5 | 59,9% / 48,2% / 37,2% | 1.67 / 2.07 / 2.69 | niska |
| Kartki śr. 4.2 (zacięty mecz 2.BL, sędzia nieznany): Over 3.5 / Over 4.5 | 57,2% / 40,3% | 1.75 / 2.48 | niska/średnia |
Ryzyka: wyrównany mecz; Hannover w słabej formie (3 mecze bez wygranej, ale rynek faworyzuje), FCK defensywnie solidny (4 stracone w 9), dogrywka/karne ok. 28% (remis).

## Holstein Kiel - Hoffenheim (Holstein-Stadion; gospodarz potwierdzony: Kiel)
Forma: Kiel 13. w 2.BL (10-11 w 9 m), 3-0 z Dresden (25.10), 0-0 Hertha. Hoffenheim 10. w BL (14-14 w 7 m), 3-0 z Leverkusen (25.10), 3-0 Lyon (EL, 22.10), ale 2-3 z Besiktas i HSV - mecz zawsze otwarty. Dużo meczów (3 w tygodniu) - rotacja po EL. H2H: Hoffenheim 3-0 (m.in. 5-1 w Pokalu 2021; stare). Rynek: Kiel 17,2 / X 18,9 / Hoff. 63,9; O/U 3,5: Over ok. 49%. Moje p Hoffenheim ok. 3 pp poniżej rynku (rotacja, kryzys nie dotyczy faworyta).
Model λ 1.0 / 2.0.

| Rynek | p | fair | pewność |
|---|---|---|---|
| 1 Kiel (90') | 18,3% | 5.48 | średnia |
| X | 21,2% | 4.72 | |
| 2 Hoffenheim | 60,6% | 1.65 | średnia |
| 1X | 39,5% | 2.53 | |
| X2 | 81,8% | 1.22 | średnia |
| 12 | 78,8% | 1.27 | |
| Awans Hoffenheim | 72,0% | 1.39 | średnia (cup, rotacja) |
| Awans Kiel | 28,0% | 3.57 | |
| Over 1.5 / Under 1.5 | 80,1% / 19,9% | 1.25 / 5.02 | średnia |
| Over 2.5 / Under 2.5 | 57,7% / 42,3% | 1.73 / 2.36 | średnia/niska |
| Over 3.5 / Under 3.5 | 35,3% / 64,7% | 2.83 / 1.55 | niska |
| BTTS tak / nie | 54,7% / 45,3% | 1.83 / 2.20 | niska |
| Rożne śr. 10.4: Over 9.5 / Over 10.5 | 57,3% / 46,1% | 1.75 / 2.17 | niska |
| Kartki śr. 3.6: Over 3.5 / Over 4.5 | 46,5% / 30,3% | 2.15 / 3.30 | niska |
Ryzyka: Hoffenheim po 3 meczach w 8 dniach (rotacja, spadek intensywności), Kiel u siebie bez porażki w ostatnich 2 i skuteczny w kontrach; wygrana Kiel 18% + remis 21% = główne ryzyka faworyta.

Oszacowania probabilistyczne, nie gwarancje. Wszystkie rożne/kartki i składy bez potwierdzenia - przed kuponem sprawdź składy (60 min przed) i sędziów.

---

<!-- źródło: an_dfb_2 -->
# DFB-Pokal, 2. runda, sroda 28.10.2026, 18:00 CET (17:00 UTC) - analiza football-analyst

Weryfikacja: ESPN scoreboard (stan 14:13 UTC) - wszystkie 4 mecze "Scheduled", start 17:00 UTC, zaden nie ruszyl. Gospodarze potwierdzeni (ESPN + kluby): Dynamo Dresden (Rudolf-Harbig), SC Freiburg (Europa-Park), SC Paderborn (Home Deluxe Arena), SSV Jeddeloh II (Marschweg). Czesc serwisow podaje blednie 27.10 - klub Freiburga i ESPN: 28.10 18:00.
Zrodla: ESPN (terminarz, tabele, kursy DraftKings), Eurosport.de, Sports Mole, kicker (via WebSearch), Wincomparator (model, 403 przy pobraniu). Brak: sedziow, xG, rozne/kartki (brak danych -> bez rynkow rozne/kartki). Kursy DraftKings w formacie US, bez marzy w "rynek no-vig".
Wszystkie p dotycza 90 minut (1X2, DC, gole, BTTS); "Awans" osobno (dogrywka+karne, ok. 55-60% dla lepszego w remisie).

## 1. Dynamo Dresden - Schalke 04
Lambda 1.15 / 1.50. Rynek no-vig (DK): 29.0 / 25.1 / 45.9; O2.5 58.7% (DK 2.5: -170/+125).
Statystyki: Dresden (2. BL, 15., 11 GF/18 GA w 9) - 0-3 w Kilonii, 1 wygrana w 7; Schalke (BL 16., 4 GF/7 GA w 7) - bez wygranej od 11.09, 0-0 z Koln, ale 5-2 w R1. Schalke strzela rzadko (2 z 5 meczow z golem), Dresden traci ok. 2/mecz.
Kadra: Schalke bez Karamana, Wobera, Hojlunda, Schallenberga, Sylli; Gosens i El-Faouzi (rany/nos) pod znakiem zapytania, Ljubicic watpliwy (Sports Mole: out). Dresden: Schmidt (ACL), Bunning out, Keller watpliwy. H2H: jedyny puchar 2014 Dresden 2-1.
Moje O2.5 (49%) jest 9 pp pod rynkiem - brak xG/konkretow, wiec nie schodze nizej; slabe ataki Schalke vs najgorsza obrona. Kryzys Schalke (underdog? nie - faworyt): bez korekty na p faworyta wg reguly.

| Rynek | p | fair | pewnosc |
|---|---|---|---|
| 1 Dresden (90') | 29.1% | 3.44 | niska |
| X | 25.6% | 3.90 | niska |
| 2 Schalke (90') | 45.3% | 2.21 | niska |
| 1X | 54.7% | 1.83 | niska |
| X2 | 70.9% | 1.41 | srednia |
| 12 | 74.4% | 1.34 | srednia |
| Over 1.5 | 74.2% | 1.35 | srednia |
| Over 2.5 / Under 2.5 | 49.4% / 50.6% | 2.02 / 1.98 | niska (brak mocnego typu) |
| Over 3.5 / Under 3.5 | 27.5% / 72.5% | 3.64 / 1.38 | srednia |
| BTTS tak / nie | 53.1% / 46.9% | 1.88 / 2.13 | niska |
| Awans Schalke / Dresden | 59% / 41% | 1.69 / 2.44 | niska-srednia |

Ryzyka: Schalke zdziesiatkowany, bez wygranej 6 meczow, w pucharze 5 odpadniec z rzedu w R2; Dresden u siebie z motywacja; remis -> dogrywka/karne (26%). Najlepszy rynek: X2 / Over 1.5 (srednio), brak mocnego typu na wynik.

## 2. SC Freiburg - VfL Wolfsburg (2. BL)
Lambda 1.80 / 1.05. Rynek no-vig: 57.5 / 21.5 / 21.0; DK total 3.5 (O -105 / U -130, O3.5 ok. 47%).
Statystyki: Freiburg (BL 3., 16 GF/9 GA w 7); Wolfsburg (2. BL 4., 4W 4D 1L, 23 GF/14 GA w 9 - strzela i traci). Wolfsburg spadkowicz, klasa nizej, ale ofensywny.
Kadra: nie znaleziono potwierdzonych sklady/absencji (Wincomparator, niepotwierdzone: Eriksen, Vranckx, Rogerio out). Pewnosc obnizona za brak newsow. H2H: 2 mecze pucharowe, oba wygral Wolfsburg (stare, niska waga). Rotacja Freiburga w pucharze: -1 pp na gospodarza.

| Rynek | p | fair | pewnosc |
|---|---|---|---|
| 1 Freiburg (90') | 54.9% | 1.82 | srednia |
| X | 23.1% | 4.33 | srednia |
| 2 Wolfsburg (90') | 21.9% | 4.56 | srednia |
| 1X | 78.0% | 1.28 | srednia |
| X2 | 45.0% | 2.22 | niska |
| 12 | 76.9% | 1.30 | srednia |
| Over 1.5 | 77.7% | 1.29 | srednia |
| Over 2.5 / Under 2.5 | 54.2% / 45.8% | 1.84 / 2.19 | niska |
| Over 3.5 / Under 3.5 | 31.9% / 68.1% | 3.13 / 1.47 | niska-srednia (rynek bardziej na Over) |
| BTTS tak / nie | 54.3% / 45.7% | 1.84 / 2.19 | niska |
| Awans Freiburg / Wolfsburg | 69% / 31% | 1.45 / 3.23 | srednia |

Ryzyka: remis (23%) i wygrana Wolfsburga (22%) rownowazne; rotacja Freiburga, Wolfsburg w dobrej formie 2. BL (niepokonany w 4 ostatnich ligowych? nie potwierdzone). Najlepszy rynek: awans Freiburga / 1X.

## 3. SC Paderborn - VfB Stuttgart
Lambda 0.95 / 1.65 (po korekcie w kierunku rynku). Rynek no-vig: 18.0 / 20.5 / 61.5; DK total 3.5 (O +110 / U -145, O3.5 ok. 45%).
Statystyki: Paderborn (BL 13., 6 GF/9 GA w 7), Stuttgart (BL 15., 2W 5L, 10 GF/13 GA w 7 - słaba forma). Moje wyjsciowe lambdy dawaly Stuttgart 48.8%; rynek 61.5% -> podnioslem do 53.8% (nie schodze >5 pp pod rynek bez konkretow; forma faworyta nie obniza jego p). Nadal 7.7 pp pod rynkiem - bez danych o skladach nie zakladam przewagi.
H2H: 3 puchary, 3 wygrane Stuttgartu (2023: 2-1 po odrabianiu). Kadra/sedzia: brak aktualnych danych (wyszukiwanie zwrocilo tylko 2023) -> pewnosc niska.

| Rynek | p | fair | pewnosc |
|---|---|---|---|
| 1 Paderborn (90') | 21.7% | 4.61 | niska |
| X | 24.5% | 4.08 | niska |
| 2 Stuttgart (90') | 53.8% | 1.86 | niska |
| 1X | 46.2% | 2.16 | niska |
| X2 | 78.3% | 1.28 | srednia |
| 12 | 75.5% | 1.32 | srednia |
| Over 1.5 | 73.3% | 1.36 | srednia |
| Over 2.5 / Under 2.5 | 48.2% / 51.8% | 2.08 / 1.93 | niska |
| Over 3.5 / Under 3.5 | 26.4% / 73.6% | 3.79 / 1.36 | niska-srednia |
| BTTS tak / nie | 49.5% / 50.5% | 2.02 / 1.98 | niska |
| Awans Stuttgart / Paderborn | 69% / 31% | 1.45 / 3.23 | niska-srednia |

Ryzyka: Stuttgart w kryzysie ligowym (zero korekty p), Paderborn u siebie bronił sie dobrze; remis 24.5% -> karne loteria. Najlepszy rynek: awans Stuttgartu / X2.

## 4. SSV Jeddeloh II (Regionalliga, 4. liga) - Hertha Berlin (2. BL, lider)
Lambda 0.55 / 2.90. Rynek no-vig: 4.1 / 6.3 / 89.6; DK total 4.5 (O -130 / U +100, O4.5 ok. 53%).
Statystyki: Hertha - 1. w 2. BL, 8W 1D 0L, 20 GF/8 GA w 9. Jeddeloh II - w R1 wygral 5-2 z Heidenheim (sensacja); brak twardych danych o formie ligowej i skladzie (rezerwy klubu, mozliwe wzmocnienia z pierwszej druzyny) -> PEWNOSC NISKA, rynki wyznaczone z lambdy i rynku, nie z danych o Jeddeloh.
Rynek wyzej niz ja (89.6% vs 84.8%): zostawiam 85% (nie schodze >5 pp pod rynek). Puchar + czwartoligowiec u siebie: wiecej niespodzianek niz liga, ale 5-2 z Heidenheim pokazuje tez, ze gospodarze strzelaja (BTTS ryzyko).

| Rynek | p | fair | pewnosc |
|---|---|---|---|
| 1 Jeddeloh (90') | 4.5% | 22.2 | niska |
| X | 10.7% | 9.39 | niska |
| 2 Hertha (90') | 84.8% | 1.18 | niska (graniczne fair 1.15-1.20) |
| 1X | 15.2% | 6.58 | niska |
| X2 | 95.5% | 1.05 | niska (fair <=1.15, pomijac) |
| 12 | 89.3% | 1.12 | niska (fair <=1.15, pomijac) |
| Over 1.5 | 85.9% | 1.16 | niska (graniczne) |
| Over 2.5 / Under 2.5 | 67.0% / 33.0% | 1.49 / 3.03 | niska |
| Over 3.5 / Under 3.5 | 45.2% / 54.8% | 2.21 / 1.83 | niska |
| BTTS tak / nie | 40.0% / 60.0% | 2.50 / 1.67 | niska |
| Awans Hertha / Jeddeloh | 94% / 6% | 1.06 / 16.7 | niska (fair <=1.15) |

Ryzyka: wygrana/dogrywka Jeddeloh (15% remis+gospodarz po 90'), rotacja Herthy, mało danych o gospodarzu. Najlepszy rynek: Hertha 90' (1.18) / Over 2.5 (1.49).

## Podsumowanie
Brak mocnych typow (wszystko niska/srednia pewnosc). Zawsze: to oszacowania probabilistyczne, nie gwarancje. Brak rynkow rozne/kartki/faule: brak sedziow i statystyk.

---

<!-- źródło: an_pp -->
# Puchar Polski 1/16 - środa 28.10.2026 (analiza stan na ok. 15:30)

Kolejność: dane z sieci (MCP sportsdata rozłączony - brak Pinnacle/xG/składów oficjalnych). Kursy: Betclic/Fortuna/STS/Superbet z serwisów typerskich (meczyki.pl, weszlo.com, pilkarskiswiat.com, mecze24.pl, igamingpolska.pl), nie z własnego pobrania. p "po 90 min" liczone poisson.py; awans = p90 + remis x (dogrywka + karne 50/50); dogrywka λ x 0,36.

## Lista meczów 28.10 (czas PL)
Rozpoczęte, pominięte: Siarka Tarnobrzeg - Lech Poznań 12:30, Sokół Kleczew - Podhale Nowy Targ 12:30.
Analizowane (Ekstraklasa / 1. liga):
1. Puszcza Niepołomice (1L) - Wisła Płock (E) 17:30
2. Znicz Pruszków (2L) - Ruch Chorzów (1L) 17:30
3. GKS Tychy (2L) - Pogoń Siedlce (1L) 18:30
4. Lechia Gdańsk (1L) - Jagiellonia Białystok (E) 20:30, Polsat Plus Arena, TVP Sport
Pominięte: Polonia Środa Wlkp. - Śląsk II Wrocław 19:00 (bez drużyny E/1L, brak danych).
Uwaga: ligi drużyn (Lechia, Ruch, Puszcza = 1L; Znicz, Tychy = 2L) ustalone pośrednio (tabela 1L bez Znicza/Tychów, zasada gospodarza "niższa liga"); 2L niepotwierdzona wprost.

---
## 1. Puszcza Niepołomice - Wisła Płock (17:30)
λ 1,00 / 1,50 (Puszcza dom 1,3 str./0,7 strac.; Wisła 1,1 str./1,5 strac. w 10 ost.; 11. w Ekstraklasie, 14 pkt, bilans -6). Rynek (Betclic 3,60/3,50/1,80, bez marży 24,8/25,5/49,7).
| Rynek | p | fair |
|---|---|---|
| 1 / X / 2 (90') | 25,2 / 26,0 / 48,8 | 3,96 / 3,85 / 2,05 |
| 1X / X2 / 12 | 51,2 / 74,8 / 74,0 | 1,95 / 1,34 / 1,35 |
| Over 1,5 / 2,5 / 3,5 | 71,3 / 45,6 / 24,2 | 1,40 / 2,19 / 4,13 |
| Under 2,5 | 54,4 | 1,84 |
| BTTS tak / nie | 49,1 / 50,9 | 2,04 / 1,96 |
| Awans Wisła / Puszcza | 63,4 / 36,6 | 1,58 / 2,73 |
Pewność: średnia-niska (brak składów, kontuzji; zgodne z rynkiem w 1pp). Ryzyka: rotacja Wisły (liga 31.10 z Piastem), Puszcza grała 24.10 z Lechią (2:1 w lidze), puchar = więcej niespodzianek; remis ok. 26% + wygrana gospodarzy ok. 25%. Górny pułap awansu obniżony o kilka pp (puchar z rotacją).

## 2. Znicz Pruszków - Ruch Chorzów (17:30)
λ 1,00 / 1,25. Znicz (2L): 5 wygranych z rzędu (11:4), 10 meczów bez porażki, dom dobry; Ruch (1L, 13.): 3W-1R-1P, 8:3, 4 czyste konta (2:0 Pogoń Grodzisk, 3:0 Odra, 2:0 ŁKS). H2H: Znicz 3:2 (V.26), 2:1 (XI.25) - ale to było w 1L. Rynek (Betclic 3,10/3,40/2,00, bez marży 28,9/26,3/44,8).
| Rynek | p | fair |
|---|---|---|
| 1 / X / 2 (90') | 29,6 / 28,5 / 42,0 | 3,38 / 3,51 / 2,38 |
| 1X / X2 / 12 | 58,1 / 70,5 / 71,6 | 1,72 / 1,42 / 1,40 |
| Over 1,5 / 2,5 / 3,5 | 65,7 / 39,1 / 19,1 | 1,52 / 2,56 / 5,25 |
| Under 2,5 | 60,9 | 1,64 |
| BTTS tak / nie | 45,1 / 54,9 | 2,22 / 1,82 |
| Awans Ruch / Znicz | 57,1 / 42,9 | 1,75 / 2,33 |
Pewność: niska (brak składów/kontuzji, forma 2L trudna do skalibrowania). Ryzyka: Znicz w serii, ostatnie H2H dla Znicza; Ruch może rotować po ligowym 2:0 (25.10). Brak mocnego typu.

## 3. GKS Tychy - Pogoń Siedlce (18:30, Tychy)
λ 1,20 / 0,95. Tychy (2L): 10 meczów bez porażki (też 10 domowych), dom 1,3 str./0,3 strac., 3 z 5 ost. bez straty (2x 0:0); Siedlce (1L, 8. wg stanu z 2.09): 2W-3P w 5 (3:4 Stal Rzeszów, 1:3 Puszcza, 0:1 Podbeskidzie), strata dużo. H2H: Tychy 3 z 4 (ost. 1:0 12.04.26, gdy oba w 1L). Rynek: Tychy ok. 2,01-2,20, remis 3,34, Siedlce 3,21 (bez marży ok. 44/27/29).
| Rynek | p | fair |
|---|---|---|
| 1 / X / 2 (90') | 41,7 / 29,2 / 29,1 | 2,40 / 3,42 / 3,44 |
| 1X / X2 / 12 | 70,9 / 58,3 / 70,8 | 1,41 / 1,72 / 1,41 |
| Over 1,5 / 2,5 / 3,5 | 63,3 / 36,4 / 17,1 | 1,58 / 2,75 / 5,85 |
| Under 2,5 | 63,6 | 1,57 |
| BTTS tak / nie | 42,9 / 57,1 | 2,33 / 1,75 |
| Awans Tychy / Siedlce | 57,3 / 42,7 | 1,75 / 2,34 |
Pewność: niska (brak składów, tylko przeglądy typerskie). Ryzyka: Siedlce klasą wyżej (1L) i średnia 3,2 gola w ost. 5; dogrywka/karne ok. 15%. Under 2,5 i 1X to najlepsze rynki, ale p < 65%.

## 4. Lechia Gdańsk - Jagiellonia Białystok (20:30)
λ 1,05 / 1,60. Lechia (1L): 4W-1P w 5, bilans 15:6 (7:1 Mielec, 2:1 Arka, 2:1 Stal Rz., 3:1 Ruch; 1:2 Puszcza 24.10), 4 domowe wygrane z rzędu, traci w 9 meczach z rzędu, strzela pierwsza w 5/6; Jagiellonia (E, 10., -13 do lidera): 2W-3P, 5:8 (1:0 Wisła Płock 25.10, 0:3 Anderlecht 22.10 LE/LK, 0:1 Zagłębie, 3:1 Ararat, 1:3 Górnik), traci pierwsza w 5/6; liga 31.10 Wieczysta. H2H: Lechia 3:0 (III.26), Jagiellonia 2:0 (VIII.25), Lechia 1:0 (III.25), Jag 3:2 (IX.24). Predykcja Weszło: Lechia Holewiński - Kopasek, Łopata, Beskorowajnyj, Małow - Mena, Wójtowicz, Neugebauer, Dodaj - Blanuta, Szach; Jagiellonia Abramowicz - Conceicao, Vital, Kobayashi, Montoia - Romanczuk, Klynge - Jóźwiak, Imaz, Szmyt - Prelec (nieoficjalne; kontuzje brak danych). Rynek (Betclic 4,65/4,00/1,65, bez marży 20,1/23,3/56,6; Superbet O2,5 1,68, BTTS 1,69, 1X 2,02, X2 1,16).
Korekta: mój pierwotny model 1,0/1,5 dawał Jagiellonię 48,8% (8 pp pod rynkiem) - podniesiony do 50,1% (λ 1,6) bo bez konkretnej informacji kadrowej nie schodzę >5 pp pod rynek; zostaje ok. 6 pp pod rynkiem z powodu pucharu z rotacją po meczu Europy (22.10) i niższego pułapu faworyta.
| Rynek | p | fair |
|---|---|---|
| 1 / X / 2 (90') | 24,9 / 25,0 / 50,1 | 4,02 / 4,01 / 1,99 |
| 1X / X2 / 12 | 49,9 / 75,1 / 75,0 | 2,00 / 1,33 / 1,33 |
| Over 1,5 / 2,5 / 3,5 | 74,2 / 49,4 / 27,5 | 1,35 / 2,02 / 3,64 |
| Under 2,5 | 50,6 | 1,98 |
| BTTS tak / nie | 51,9 / 48,1 | 1,93 / 2,08 |
| Awans Jagiellonia / Lechia | 64,3 / 35,7 | 1,56 / 2,80 |
Pewność: średnia. Ryzyka (oba): remis 25% (dogrywka ok. 12% meczów po 90') oraz wygrana Lechii 25%; Jagiellonia w kiepskiej formie (nie jest underdogiem - bez korekty kryzysowej), traci pierwsza; Lechia z kolei traci w każdym meczu (BTTS sprzyja). Najlepszy rynek: Over 1,5 (74%, fair 1,35) i X2 (75%, fair 1,33), BTTS/O2,5 ok. 50-52% (rynek 1,68-1,69 = brak value).

---
## Zestawienie
| Mecz | Rynek | p | fair | Pewność |
|---|---|---|---|---|
| Puszcza - Wisła | Awans Wisła | 63,4 | 1,58 | średnia-niska |
| Puszcza - Wisła | Over 1,5 | 71,3 | 1,40 | niska |
| Znicz - Ruch | Under 2,5 | 60,9 | 1,64 | niska |
| Tychy - Siedlce | 1X | 70,9 | 1,41 | niska |
| Tychy - Siedlce | Under 2,5 | 63,6 | 1,57 | niska |
| Lechia - Jagiellonia | X2 | 75,1 | 1,33 | średnia |
| Lechia - Jagiellonia | Over 1,5 | 74,2 | 1,35 | średnia |
| Lechia - Jagiellonia | Awans Jagiellonia | 64,3 | 1,56 | średnia |

Brak mocnego typu: Znicz - Ruch (wyrównane). Oszacowania probabilistyczne, nie gwarancje.
