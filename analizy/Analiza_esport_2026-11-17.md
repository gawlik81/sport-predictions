# Analiza e-sport - wtorek 17.11.2026 (czas PL, CET)

Skill: esports-analyst. Źródła: Pinnacle (mcp__sportsdata__pinnacle_*, kursy USA przeliczone na dziesiętne, marża usunięta proporcjonalnie), PandaScore (terminarz, bez odds - brak klucza do odds), tips.gg (kursy nieznanego bukmachera, tylko Dota Asgard), csdb.gg (VRS, forma 120 dni, mapy 90 dni), Strafe, HLTV (tylko wyniki wyszukiwania; strona 403), WebSearch. Liquipedia/HLTV/rdy.gg blokują pobieranie (403), więc statystyki map i H2H są ubogie. Kursów Superbet na e-sport brak. Modele: `esports-analyst/scripts/series.py`.

## Potwierdzenie par i godzin

| Mecz | Pełne nazwy | Godzina PL | Źródło 1 | Źródło 2 | Status |
|---|---|---|---|---|---|
| NIP - UNiTY | Ninjas in Pyjamas - UNiTY Esports, Stake Ranked Ep.6, UB ćwierćfinał, bo3 | 17:00 | Strafe (16:00 UTC, bo3) | WebSearch/StarLadder (Ep.6 17-20.11) | potwierdzone (godzina wg Strafe "4:00 PM" = 16:00 UTC) |
| GL - LG | GamerLegion - Luminosity Gaming, Stake Ranked Ep.6, playoff, bo3 | 19:30 | Pinnacle (18:30Z, ID 1640493749) | csdb.gg (18:30 UTC, bo3) | potwierdzone |
| NXS - WAL | Nexus Gaming - Walczaki, CCT Europe 2026 Series #14, bo3 | 19:00 | HLTV (wynik wyszukiwania: 19:00) | brak drugiego | do potwierdzenia (jedno źródło, a pełne nazwy z wnioskowania) |
| HT - TLR | Hype Tech - The Last Resort, CCT Europe 2026 Series #14, bo3 | 16:00 | HLTV (16:00, bo3) | dust2.us (para; godzina rozbieżna: 10:00 AM UTC - prawdopodobnie strefa USA) | para potwierdzona, godzina 16:00 PL wg HLTV |
| Team Spirit - Aurora | Team Spirit - Aurora Gaming, 1win Essence III, UB final, bo3 | 17:00 | Pinnacle (16:00Z, ID 1640570302) | Team Smurf/Hotspawn (UB final 17.11) | potwierdzone |
| angry birds - TS.A | angry birds - Team Spirit Academy, Asgard Championship S2, bo3 | 17:00 | PandaScore (16:00Z, ID 1815857) | tips.gg (17:00) | potwierdzone |
| XE - CH | Xipto Esports - CyberHero, Asgard Championship S2, bo3 | 20:00 | Pinnacle (19:00Z, ID 1640570311) | tips.gg (20:00) | potwierdzone |

Uwaga: Pinnacle ma też "Hype Tech vs ex-INOX" (NODWIN Clutch, 13:00 PL) - to inny mecz niż HT - TLR.

---

## CS2

### Ninjas in Pyjamas - UNiTY Esports (Stake Ranked Ep.6, UB ćwierćfinał, bo3, 17:00)
**Typ:** zwycięzca serii NIP | **p:** 69% | **Fair:** 1.45 | **Pewność:** średnio-niska
**Statystyki:** NIP VRS #15 (1564 pkt), 120 dni 28-18 (maps 59-41), ostatnie 10: 7-3, seria 3 W, LAN 21-11 (65,6%), mapy: Mirage 75% (9-3), Nuke 72,7% (8-3), Inferno 62,5%, Ancient 58%, Dust2 33% (2-4), Cache 47% (csdb.gg). Skład: stavn, adamb, Krimbo, sjuush, xKacpersky (niepotwierdzony transferem; część źródeł podaje n0te/Snappi). UNiTY VRS #64 (1220 pkt), 41-17 w 120 dni, 9-1 w ostatnich 10 (6 W z rzędu), ale średni rywal #134 (słaby grafik), LAN 9-2; skład Dytor, KWERTZZ, Sn0w, M1key, 2high (skład zmieniany często, wcześniej problem z wystawieniem składu w CCT S7). Brak map UNiTY.
**H2H:** raz, 27.01.2025 CCT, NIP 2-0 (nieistotne - inny skład).
**Rynek:** brak kursów (nie ma na Pinnacle). Strafe: ~91-95% głosów na NIP (nie kurs).
**Liczby:** p mapy NIP 0.63 (NIP lepiej na LAN, wyższy VRS, ale UNiTY w serii 6 W i słaba próba) -> seria 69.1%.
| Rynek | p | Fair |
|---|---|---|
| NIP wygra | 69.1% | 1.45 |
| NIP -1.5 (2-0) | 39.7% | 2.52 |
| UNiTY +1.5 | 60.3% | 1.66 |
| NIP +1.5 | 86.3% | 1.16 (graniczne) |
| Under 2.5 map | 53.4% | 1.87 |
| Over 2.5 map | 46.6% | 2.15 |
| 2-0 NIP / 2-1 NIP | 39.7% / 29.4% | 2.52 / 3.40 |
**Ryzyka:** niepewny skład NIP, UNiTY gra serią zwycięstw przeciw słabszym, ale z ostatnich meczów nie widać ich map; wynik na 3. mapie (decider) to loteria. Bez kursu nie da się policzyć EV.

### GamerLegion - Luminosity Gaming (Stake Ranked Ep.6, playoff, bo3, 19:30)
**Typ:** brak mocnego typu (GL 56.6%) | **Fair GL:** 1.77 | **Pewność:** niska
**Statystyki (csdb.gg):** GL VRS #37 (1392), 13-15 w 120 dni, ostatnie 10: 4-6; LAN 11-10 (52%), online 2-5; mapy: Cache 88,9% (8-1), Nuke 63,6%, Dust2 55,6%, Ancient 50%, Mirage 20% (2-8). Skład: Snax, REZ, shalfey, Tauson, hypex, FL4MUS. Luminosity VRS #40 (1371), 10-12, seria 6 porażek (ostatnie 10: 3-7); mapy: Mirage 75% (6-2), Ancient 55,6%, Inferno 50%, Nuke 42,9%, Dust2 30%, Cache 20%. Skład: Rainwaker, afro, lux, Yxngstxr, AZUWU. Przewidywany veto (csdb): GL ban Mirage, LG ban Cache, GL pick Dust2, LG pick Inferno, ban Ancient, decider Nuke.
**H2H:** brak danych.
**Liczby:** mapy GL: Dust2 0.60, Inferno 0.45, Nuke 0.58 (decider przy rzadkich Nuke/Ancient). Seria GL 56.6%.
**Rynek (Pinnacle, devig):** GL 55.8% / LG 44.2% (kursy 1.725 / 2.18). Różnica 0.8 pp - zgodne. -1.5 GL 3.02, +1.5 LG 1.415, Over 2.5 map 2.07, Under 2.5 1.80.
| Rynek | p | Fair | Pinnacle | EV |
|---|---|---|---|---|
| GL wygra | 56.6% | 1.77 | 1.725 | -2% |
| LG wygra | 43.4% | 2.30 | 2.18 | -5% |
| LG +1.5 | 73.0% | 1.37 | 1.415 | +3% (graniczne) |
| GL -1.5 | 27.0% | 3.70 | 3.02 | ujemne |
| Over 2.5 map | 51.0% | 1.96 | 2.07 | +5.6% (graniczne) |
**Ryzyka:** wyrównana seria; GL online słabo, jeśli turniej online; LG po 6 porażkach z rzędu (kryzys underdoga obniżył jego p na mapach: Inferno 0.55 dla LG zamiast 0.60+). Brak mocnego typu.

### Nexus Gaming (NXS) - Walczaki (WAL) (CCT Europe #14, bo3, 19:00) - do potwierdzenia
**Typ:** zwycięzca serii NXS | **p:** 72% | **Fair:** 1.39 | **Pewność:** niska
**Statystyki:** Nexus VRS #65 (1187), 19-15 w 120 dni (maps 45-36), ostatnie 10: 5-5; LAN 8-5, online 11-10; mapy: Mirage 83% (5-1), Ancient 62,5%, Cache 58%, Anubis 50%, Dust2 47%, Inferno 44%. Skład niespójny w źródłach (shield, fNk, s0und, Nexius, HOLY vs SBT, XELLOW). Walczaki VRS #184 (741), 7-12, maps 18-28, wszystkie mecze online, ostatnie 10: 4-6 (2 porażki z rzędu); mapy: Nuke 66,7% (4-2), Anubis 60% (3-2), Inferno 0-3, Mirage 0-3. Skład: reiko, OLIMP, sNx, bajmi, mrouz.
**H2H:** brak.
**Rynek:** brak kursów (Pinnacle nie ma meczu).
**Liczby:** p mapy NXS 0.65 (różnica VRS 119 miejsc, ale niepewny skład i niska jakość próby) -> 71.8%.
| Rynek | p | Fair |
|---|---|---|
| NXS wygra | 71.8% | 1.39 |
| NXS -1.5 (2-0) | 42.3% | 2.37 |
| WAL +1.5 | 57.7% | 1.73 |
| Under 2.5 | 54.5% | 1.83 |
| 2-0 NXS | 42.3% | 2.37 |
**Ryzyka:** niepewny skład Nexusa (rozbieżne listy), brak kursu, jedno źródło godziny/pary, bo3 online.

### Hype Tech (HT) - The Last Resort (TLR) (CCT Europe #14, bo3, 16:00)
**Typ:** brak mocnego typu (TLR 56%) | **Fair TLR:** 1.79 | **Pewność:** niska
**Statystyki:** TLR VRS #114 (986), 15-21 w 120 dni, ostatnie 10: 5-5, online 13-19 (40,6%), mapy: Nuke 66,7% (6-3), Ancient 53,8%, Inferno 41,7%, Cache 33%, Dust2 29%, Mirage 0-3. Skład: Girafffe, arTisT, Extinct, Dutchy, Vacancy, bevve. HT: skład Dragon, Kind0, VLDN, brutmonster, Cjoffo (RS/BA/ME); brak rankingu/statystyk w źródłach; ostatnie mecze: 14.11 W 2-0 WW Team, L 1-2 Phantom; 15.11 L 0-2 Butterfly, L 0-2 Virtus.pro (1-3).
**H2H:** brak. **Rynek:** brak kursów.
**Liczby:** p mapy HT 0.46 (TLR wyższy VRS, ale słaba forma online; HT bez danych -> blisko 50%) -> TLR 56.0%.
| Rynek | p | Fair |
|---|---|---|
| TLR wygra | 56.0% | 1.79 |
| HT wygra | 44.0% | 2.27 |
| TLR +1.5 | 78.8% | 1.27 |
| Under 2.5 / Over 2.5 | 50.3% / 49.7% | 1.99 / 2.01 |
**Ryzyka:** brak wiarygodnych danych o HT ("brak podstaw" do mocnego typu); wyrównana seria.

---

## Dota 2

### Team Spirit - Aurora Gaming (1win Essence III, UB final, bo3, 17:00)
**Typ:** Spirit wygra (z handicap-ową alternatywą: Aurora +1.5) | **p Spirit:** 72% | **Fair:** 1.39 | **Pewność:** średnia
**Kontekst:** Spirit w playoffie: 2-0 LGD (ćwierćfinał), 2-0 PARIVISION (półfinał, 16.11). Aurora: 2-0 w otwarciu, 2-1 LEGION (16.11, po przegranej pierwszej grze); w fazie grupowej 2-1 GamerLegion. H2H: Aurora wygrała FISSURE Universe Ep.8 (finał, 3-2, luty 2026). UB final: przegrany spada do LB finału (mniejsza stawka -> więcej wariancji).
**Rynek (Pinnacle, devig):** seria Spirit 75.6% / Aurora 24.4% (1.262 / 3.90); mapa 1: 68.2% / 31.8%; Spirit -1.5 1.97 / Aurora +1.5 1.885; Over 2.5 mapy 2.22, Under 1.633 (57.6%).
**Liczby:** p mapy Spirit 0.65 (rynek ~0.68; ściągnięte o ok. 3 pp przez ostatni ostry mecz Aurory z H2H z lutego i mniejszą stawkę UB finału). Różnica do rynku 3.8 pp (< 5 pp).
| Rynek | p | Fair | Pinnacle | EV |
|---|---|---|---|---|
| Spirit wygra | 71.8% | 1.39 | 1.262 | ujemne |
| Aurora wygra | 28.2% | 3.55 | 3.90 | +10% (graniczne, niskie p) |
| Spirit 2-0 / -1.5 | 42.3% | 2.37 | 1.97 | ujemne |
| Aurora +1.5 | 57.7% | 1.73 | 1.885 | +8.8% (kandydat, niska-średnia pewność) |
| Under 2.5 map | 54.5% | 1.83 | 1.633 | ujemne |
| Over 2.5 map | 45.5% | 2.20 | 2.22 | ~0 |
| 2-1 Spirit | 29.6% | 3.38 | | |
**Ryzyka:** rynek jest wyraźnie bardziej pro-Spirit; jeśli Spirit w formie z 16.11 to p blisko rynku (75%). Brak informacji o draftach i patchu.

### angry birds - Team Spirit Academy (Asgard Championship S2, bo3, 17:00)
**Typ:** angry birds wygra | **p:** 65% | **Fair:** 1.54 | **Pewność:** niska
**Statystyki:** grupa A (zakończona): angry birds 4-2 (mapy 10-5), Spirit Academy 4-2 (9-5). Wczoraj 16.11: angry birds 2-0 Team Lynx, TS.A 2-0 Team Synapse; angry birds przegrali z Xipto 1-2 (15.11), TS.A pokonali Xipto 2-1 (rdy.gg). Brak danych o składach i patchu, tier-3 online.
**Rynek (tips.gg, bukmacher niepodany):** AB 1.41 / TS.A 2.74 -> devig 66.0% / 34.0%. **Liczby:** p mapy 0.60 -> 64.8% (rynek -1.2 pp).
| Rynek | p | Fair |
|---|---|---|
| angry birds wygra | 64.8% | 1.54 |
| AB -1.5 (2-0) | 36.0% | 2.78 |
| TS.A +1.5 | 64.0% | 1.56 |
| Under 2.5 | 52.0% | 1.92 |
**Ryzyka:** bardzo mała próba, rosterowa zmienność akademii, kurs z nieznanego źródła.

### Xipto Esports (XE) - CyberHero (CH) (Asgard Championship S2, bo3, 20:00)
**Typ:** CyberHero wygra | **p:** 59% | **Fair:** 1.70 | **Pewność:** niska
**Statystyki:** Xipto 5-1 w grupie A (mapy 11-6, 1. miejsce), 2-1 angry birds, 2-1 TS.A, 2-0 Allied (16.11). CyberHero 4-1 w grupie B (mapy 8-2), 2-0 Nemiga (16.11), 2-0 InterActive PH (10.11); grupa B w toku, więc słabsza próba.
**Rynek:** Pinnacle CH 63.4% / XE 36.6% (1.485 / 2.58; spread CH -1.5 2.51, XE +1.5 1.51; Over 2.5 1.98, Under 1.80); tips.gg CH 63.1%. **Liczby:** p mapy XE 0.44 (ściągnięte ku Xipto o ok. 4 pp przez bilans grupy 5-1 i wygraną z Allied, rynek nie jest pewny) -> CH 59.0%.
| Rynek | p | Fair | Pinnacle |
|---|---|---|---|
| CH wygra | 59.0% | 1.70 | 1.485 |
| XE wygra | 41.0% | 2.44 | 2.58 (EV +6%, graniczne) |
| CH -1.5 (2-0) | 31.4% | 3.19 | 2.51 ujemne |
| XE +1.5 | 68.6% | 1.46 | 1.51 (EV +3.6%, graniczne) |
| Under 2.5 / Over 2.5 | 50.7% / 49.3% | 1.97 / 2.03 | 1.80 / 1.98 |
**Ryzyka:** wyrównane, brak mocnego typu; dane tier-3.

---
To są oszacowania, nie gwarancje; kursy Superbet na e-sport niedostępne.
