# Analiza reprezentacji UEFA (Liga Narodów) - 13.11.2026

Skill: football-analyst. Czas polski: 20:45 (mecze z 19:45 UTC), Mołdawia - Kazachstan 18:00 (17:00 UTC).

## Źródła i ograniczenia danych (czytaj najpierw)
- Superbet MCP: `superbet_stats` (średnie, sędzia), `superbet_missing_players`, `superbet_h2h`, `superbet_event_odds` (1X2; dla Szkocji DC), `superbet_lineups` tylko dla Holandii-Grecji i Serbii-Niemiec (składy "przewidywane", niepotwierdzone).
- Średnie Superbet to próba ok. 4 meczów Ligi Narodów (np. gole 0,3 czy 0,0): bardzo mała, nie traktować jako stałej siły drużyn. Kartki i rożne regresowane do średniej.
- Listy nieobecnych mają źródło "manual", powód "nieznany", bez dat. Dla Holandii są sprzeczne z oficjalną kadrą (beIN Sports 06.11: van Dijk, Gakpo, Brobbey w kadrze lub sprzeczne doniesienia o urazach Gakpo/Brobbey). Dla Liechtenstein-Azerbejdżan brak danych o nieobecnych.
- Newsy z sieci znalezione tylko dla grupy A2 (Holandia/Niemcy/Grecja/Serbia); dla pozostałych meczów brak konferencji i składów (nie zmyślam).
- Kursy: tylko 1X2 (Szkocja: DC). Rynki O/U goli i BTTS u Superbet nie pobrane, więc ich "fair" nie ma porównania z rynkiem. Kurs 1X2 po usunięciu marży użyty jako punkt odniesienia.
- Brak średniej kartek/fauli sędziów (znane nazwiska, bez statystyk): kartki liczone ze średnią drużyn zregresowaną do ~4,0; pewność niska, bez rekomendacji na kupon.
- Kalibracja: λ ≥ 0,7 dla każdej reprezentacji; korekty kadrowe łącznie < 15%; Under 2.5 przy łącznym λ ≤ 2,0 maks. średnia pewność; nie schodzę pod rynek o >5 pp bez konkretów (korygowałem λ w górę dla Niemiec, Szkocji, Azerbejdżanu, Andory).
- Skala ostrzeżeń: to oszacowania probabilistyczne, nie gwarancje.

---

### Holandia - Grecja (Liga Narodów A2, 13.11, 20:45, Amsterdam; sędzia Rohit Saggi)
**Typ:** Holandia wygra lub zremisuje (1X) | **p:** 80,7% | **Fair:** 1.24 | **Pewność:** średnia (typ graniczny, 1.15-1.20 po kursie rynkowym 1.16)
Najlepszy typ wynikowy bez krótkiego kursu: Holandia -1.5 (p 30,8%) jest zbyt niskie; Under 3.5 75,8% (fair 1.32).
λ: Holandia 1.65, Grecja 0.85 (łącznie 2.5).

| Rynek | p | fair | Uwagi |
|---|---|---|---|
| 1 / X / 2 | 56,3 / 24,4 / 19,2% | 1.78 / 4.09 / 5.20 | rynek (bez marży) 59,6 / 22,0 / 18,4% (kursy 1.59/4.30/5.15) |
| DC 1X / X2 / 12 | 80,7 / 43,6 / 75,6% | 1.24 / 2.29 / 1.32 | rynek 1X 1.16, X2 2.35, 12 1.22 |
| Over 1.5 / 2.5 / 3.5 | 71,3 / 45,6 / 24,2% | 1.40 / 2.19 / 4.13 | |
| Under 2.5 / 3.5 | 54,4 / 75,8% | 1.84 / 1.32 | |
| BTTS tak / nie | 46,3 / 53,7% | 2.16 / 1.86 | Grecja traci mało (0,8/m), ale remisuje często |
| Holandia -1.5 | 30,8% | 3.25 | |
| Rożne (średnia 10,0) | O 9.5: 52,8%; O 10.5: 41,6% | 1.89 / 2.40 | NED 7,5 + GRE 4,0 w próbce, dominacja gospodarzy; pewność niska |
| Kartki (śr. 4,0) | O 3.5: 53,8%; O 4.5: 37,0% | 1.86 / 2.70 | sędzia bez statystyk; pewność niska |

**Statystyki:** Holandia 8 pkt z 4 meczów (2 wygrane z Serbią, remisy 1-1 z Niemcami u siebie i 2-2 z Grecją na wyjeździe), xG 2,5/m. Grecja 8 pkt: 2-1 Serbia, 1-0 Niemcy, 0-0 Niemcy, 2-2 Holandia; traci 0,8/m (Superbet, próba 4 meczów).
**H2H:** 01.10.2026 Grecja - Holandia 2:2; 2023: 3:0 u siebie, 0:1 na wyjeździe dla Holandii.
**Informacje:** Holandia bez Gravenbercha, Frimponga, Hato, Akego (beIN); powrót de Jonga i Malena; Superbet dodatkowo wymienia van Dijka i Xaviego Simonsa jako nieobecnych (sprzeczne z kadrą beIN, niepotwierdzone). Grecja bez Konstantelias, Saliakasa i Zafeirisa (zawieszenia). Mecz o 1. miejsce w grupie (obie po 8 pkt). Przewidywane XI Superbet (niepotwierdzone) zawiera Gakpo.
**Ryzyka:** remis (Grecja nie przegrała w grupie), remis 2:2 w pierwszym meczu; wygrana Grecji (Holandia osłabiona kadrowo, p 19,2%). Sprzeczne źródła o składzie Holandii obniżają pewność.
**Rynek:** 1.59 (Holandia), mój fair 1.78, więc rynek wyżej wycenia Holandię (różnica 3 pp, w normie).

### Serbia - Niemcy (A2, 13.11, 20:45, Belgrad; sędzia Javier Alberola Rojas)
**Typ:** Niemcy wygrają | **p:** 71,7% | **Fair:** 1.39 | **Pewność:** średnia (rynek 1.30; granica 1.15-1.20 dla DC X2: fair 1.12, pomijać)
Alternatywa: Niemcy -1.5 (p 47,6%, fair 2.10), Over 1.5 78,5% (fair 1.27).
λ: Serbia 0.70 (podłoga), Niemcy 2.20 (xG 2,0/m, Serbia traci 2,0/m, bez 5 graczy z listy).

| Rynek | p | fair | Uwagi |
|---|---|---|---|
| 1 / X / 2 | 10,4 / 17,9 / 71,7% | 9.60 / 5.60 / 1.39 | rynek 11,2 / 16,3 / 72,5% (8.40/5.80/1.30) |
| DC 1X / X2 / 12 | 28,3 / 89,6 / 82,1% | 3.53 / 1.12 / 1.22 | X2 i 12 poniżej progu 1.15/zbyt krótkie |
| Over 1.5 / 2.5 / 3.5 | 78,5 / 55,4 / 33,0% | 1.27 / 1.80 / 3.03 | |
| Under 2.5 | 44,6% | 2.24 | |
| BTTS tak / nie | 44,8 / 55,2% | 2.23 / 1.81 | |
| Niemcy -1.5 | 47,6% | 2.10 | |
| Rożne (śr. 9,5) | O 8.5: 58,8%; O 9.5: 47,1% | 1.70 / 2.12 | Niemcy 6,0 vs Serbia 2,5 (próba); pewność niska |
| Kartki (śr. 3,8) | O 3.5: 50,2%; O 4.5: 33,6% | 1.99 / 2.98 | niska pewność |

**Statystyki:** Niemcy w 4 meczach: 1-1 Holandia, 0-1 Grecja, 0-0 Grecja, 2-0 Serbia (tylko 3 gole mimo xG 2,0). Serbia: 0 pkt z 4 meczów (1-2 Grecja, 1-2 Holandia x2 porażki).
**H2H:** 01.10.2026 Niemcy - Serbia 2:0.
**Informacje:** Serbia bez Pavlovicia, Terzicia, A. Stankovicia (kontuzje) i Gudelja, Maksimovicia (zawieszenia); trener Paunovic. Niemcy (trener Klopp) bez Gnabry'ego, Vagnomana, Baura (kontuzje, Superbet manual). Przewidywane XI Serbii z Superbet zawiera Milenkovicia, a wcześniejszy preview z września wymieniał go jako kontuzjowanego, więc dane niespójne. Serbia gra o uniknięcie dna grupy.
**Ryzyka:** niska skuteczność Niemców w próbce (3 gole w 4 meczach, remisy i porażka z Grecją); Serbia u siebie, z motywacją (0 pkt), może wymusić remis lub 1-0 (underdog w desperacji, wygrana/remis łącznie 28%).
**Rynek:** Niemcy 1.30, mój fair 1.39 po korekcie z 65,9% (podniesiono λ po zasadzie nie schodzić pod rynek >5 pp bez konkretów).

### Słowenia - Szwajcaria (Liga Narodów B1, 13.11, 20:45, Lublana; sędzia Jasper Vergoote)
**Typ:** brak mocnego typu wynikowego; najlepszy: Under 3.5 (77,9%, fair 1.28) | **Pewność:** średnia
Szwajcaria wygra 53,8% (fair 1.86).
λ: Słowenia 0.85 (bez Szeszki, kontuzja manual), Szwajcaria 1.55.

| Rynek | p | fair | Uwagi |
|---|---|---|---|
| 1 / X / 2 | 20,6 / 25,6 / 53,8% | 4.86 / 3.91 / 1.86 | rynek 16,9 / 28,2 / 54,8% (5.50/3.30/1.70) |
| DC 1X / X2 / 12 | 46,2 / 79,4 / 74,4% | 2.16 / 1.26 / 1.34 | rynek X2 ~ 1.20 |
| Over 1.5 / 2.5 / 3.5 | 69,2 / 43,0 / 22,1% | 1.45 / 2.32 / 4.52 | |
| Under 2.5 / 3.5 | 57,0 / 77,9% | 1.76 / 1.28 | |
| BTTS tak / nie | 45,1 / 54,9% | 2.22 / 1.82 | |
| Szwajcaria -1.5 | 28,2% | 3.55 | |
| Rożne (śr. 9,5) | O 8.5: 58,8%; O 9.5: 47,1% | 1.70 / 2.12 | SLO 4,5 + SUI 5,8; niska pewność |
| Kartki (śr. 3,8) | O 3.5: 50,2%; O 4.5: 33,6% | 1.99 / 2.98 | Słowenia 3,3 kartki/m (próba), Szwajcaria 0,3; zawieszeni Janza i Zec; niska pewność |

**Statystyki:** Szwajcaria 2,8 gola/m, traci 0,3 (3-0 MKD, 3-0 SCO, 2-1 SLO, 3-0 MKD); Słowenia 0-0 SCO, 2-0 MKD, 1-2 SUI, 2-1 SCO (w tabeli Superbet 1,3 gola/m).
**H2H:** 03.10.2026 Szwajcaria - Słowenia 2:1; 2025: 0:0 (Lublana), 3:0 (Szwajcaria).
**Informacje:** Słowenia bez Szeszki (kontuzja), Janzy i Zeca (zawieszenia); Szwajcaria bez Monteiro i Botelego (kontuzje). Brak nowszych newsów z sieci.
**Ryzyka:** remis w Lublanie (2025: 0:0), przewaga Szwajcarii w grze, ale u siebie Słowenia traci mało; wygrana Słowenii p 20,6%.
**Rynek:** Szwajcaria 1.70, mój fair 1.86; zgodne (1 pp różnicy).

### Szkocja - Macedonia Północna (B1, 13.11, 20:45, Glasgow; sędzia Michal Ocenas)
**Typ:** Szkocja wygra | **p:** 76,7% | **Fair:** 1.30 | **Pewność:** średnia (rynek: DC 1X 1.02, 12 1.09 - bardzo krótkie; 1X2 Szkocji u Superbet nie pobrane)
Alternatywa: Szkocja -1.5 (p 54,5%, fair 1.83), Over 1.5 (82,9%, fair 1.21 - graniczny).
λ: Szkocja 2.50, Macedonia 0.70 (podłoga, w próbce 0 goli w 4 meczach).

| Rynek | p | fair | Uwagi |
|---|---|---|---|
| 1 / X / 2 | 76,7 / 15,0 / 8,3% | 1.30 / 6.66 / 11.99 | rynek z DC: ok. 78,4 / 13,8 / 7,8% |
| DC 1X / X2 / 12 | 91,7 / 23,3 / 85,0% | 1.09 / 4.29 / 1.18 | rynek 1X 1.02, X2 4.35, 12 1.09: 1X i 12 zbyt krótkie |
| Over 1.5 / 2.5 / 3.5 | 82,9 / 62,0 / 39,7% | 1.21 / 1.61 / 2.52 | |
| Under 2.5 / 3.5 | 38,0 / 60,3% | 2.63 / 1.66 | |
| BTTS tak / nie | 46,2 / 53,8% | 2.16 / 1.86 | |
| Szkocja -1.5 | 54,5% | 1.83 | |
| Rożne (śr. 9,5) | O 8.5: 58,8%; O 9.5: 47,1% | 1.70 / 2.12 | SCO 4,0 + MKD 1,8 w próbce; faworyt dominujący obniża rożne MKD, ale podnosi SCO; pewność niska |
| Kartki (śr. 4,4) | O 3.5: 60,4%; O 4.5: 43,7% | 1.65 / 2.29 | MKD 3,0 kartki/m, SCO 1,8 (w tym 0,5 czerwonej/m); niska pewność |

**Statystyki:** Szkocja: 0-0 SLO, 0-3 SUI, 2-0 MKD (wyjazd), 1-2 SLO (w tabeli 0,8 gola/m, xG 2,0, 5,3 celnych/m). MKD: 0-3 SUI, 0-2 SLO, 0-2 SCO, 0-3 SUI (0 goli w 4 meczach, traci 2,5).
**H2H:** 03.10.2026 Macedonia - Szkocja 0:2 (czerwona kartka).
**Informacje:** Szkocja bez Binksa, Shanklanda, McKenny, Welsha (kontuzje, manual; osłabiona obrona, atak bez Shanklanda). MKD bez zgłoszonych nieobecnych. Trener Szkocji Pocognoli; seria porażek 1-2 SLO i 0-3 SUI nie obniża p faworyta (zasada).
**Ryzyka:** Szkocja skuteczność ofensywna w próbce niska (3 gole w 4 meczach); wcześniejsza porażka z kontuzjami obrońców; remis lub 1-0 przy zamkniętej grze MKD; wygrana MKD p 8,3% (underdog nie w kryzysie, ale bez goli).
**Rynek:** 1X2 nie pobrano; z DC wynika p Szkocji ok. 78%, mój 76,7% (-1,7 pp).

### Słowacja - Wyspy Owcze (Liga Narodów, 13.11, 20:45, Koszyce; sędzia Mohammad Al-Emara)
**Typ:** Słowacja wygra | **p:** 68,0% | **Fair:** 1.47 | **Pewność:** średnia
Alternatywa: Słowacja -1.5 (42,6%, fair 2.35).
λ: Słowacja 2.00, WO 0.70.

| Rynek | p | fair | Uwagi |
|---|---|---|---|
| 1 / X / 2 | 68,0 / 20,0 / 12,1% | 1.47 / 5.00 / 8.29 | rynek 68,0 / 19,8 / 12,1% (1.37/4.70/7.70) - zgodne |
| DC 1X / X2 / 12 | 88,0 / 32,1 / 80,1% | 1.14 / 3.12 / 1.25 | 1X pod progiem 1.15 |
| Over 1.5 / 2.5 / 3.5 | 75,1 / 50,6 / 28,6% | 1.33 / 1.97 / 3.50 | |
| Under 2.5 / 3.5 | 49,4 / 71,4% | 2.03 / 1.40 | |
| BTTS tak / nie | 43,5 / 56,5% | 2.30 / 1.77 | |
| Słowacja -1.5 | 42,6% | 2.35 | |
| Rożne (śr. 9,5) | O 8.5: 58,8%; O 9.5: 47,1% | 1.70 / 2.12 | SVK 7,0 + FRO 4,8 w próbce; niska pewność |
| Kartki (śr. 3,5) | O 2.5 ~ 69%; O 3.5: 44,7% | 1.45 / 2.24 | SVK 1,0, FRO 1,8; niska pewność |

**Statystyki:** Słowacja: 2-0 MDA, 2-1 KAZ, 1-1 FRO (wyjazd), 4-0 MDA (wyjazd); 2,3 gola/m, traci 0,5. Wyspy Owcze: 1-1 KAZ, 1-1 MDA, 1-1 SVK, 2-2 KAZ (4 remisy w 4 meczach).
**H2H:** 02.10.2026 WO - Słowacja 1:1.
**Informacje:** Słowacja bez Suslova i Lobotki (kontuzje, manual); WO bez Agnarssona (zawieszenie). Brak newsów z sieci.
**Ryzyka:** WO zremisowały wszystkie 4 mecze Ligi Narodów (w tym 1:1 ze Słowacją): remis p 20% może być niedoszacowany; brak Lobotki (kontrola środka).
**Rynek:** zgodny (68,0% vs 68,0%).

### Luksemburg - Estonia (Liga Narodów, 13.11, 20:45, Luksemburg; sędzia Ishmael Barbara)
**Typ:** brak mocnego typu (wyrównane); najlepszy rynek: Under 2.5 (73,1%, fair 1.37) | **Pewność:** średnia-niska
λ: Luksemburg 0.95, Estonia 0.85 (łącznie 1.8; wg zasad Under 2.5 przy λ ≤ 2,0 maks. średnia pewność).

| Rynek | p | fair | Uwagi |
|---|---|---|---|
| 1 / X / 2 | 36,3 / 32,8 / 30,9% | 2.75 / 3.05 / 3.24 | rynek 39,1 / 30,7 / 30,2% (2.40/3.05/3.10) |
| DC 1X / X2 / 12 | 69,1 / 63,7 / 67,2% | 1.45 / 1.57 / 1.49 | |
| Over 1.5 / 2.5 / 3.5 | 53,7 / 26,9 / 10,9% | 1.86 / 3.71 / 9.20 | |
| Under 1.5 / 2.5 / 3.5 | 46,3 / 73,1 / 89,1% | 2.16 / 1.37 / 1.12 | Under 3.5 pod progiem |
| BTTS tak / nie | 35,1 / 64,9% | 2.85 / 1.54 | |
| Rożne (śr. 9,0) | O 8.5: 53,0%; O 9.5: 41,2% | 1.89 / 2.43 | LUX 3,5 + EST 4,8; niska pewność |
| Kartki (śr. 4,4) | O 3.5: 60,4%; O 4.5: 43,7% | 1.65 / 2.29 | LUX 2,8 kartki/m, EST 2,0; niska pewność |

**Statystyki:** Luksemburg: 2-1 BUL (wyjazd), 0-3 ISL, 0-1 EST, 0-2 BUL (strzelił 0,5/m, traci 1,8). Estonia: 1-1 ISL, 1-0 LUX, plus 2 mecze bez wyniku w danych (Bułgaria, Islandia).
**H2H:** 03.10.2026 Estonia - Luksemburg 1:0.
**Informacje:** Luksemburg bez Barreiro (kontuzja) i Carlsona (zawieszenie); Estonia bez zgłoszonych. Brak newsów z sieci.
**Ryzyka:** niska skuteczność obu (0,5 gola/m); remis p 32,8%; Under jest wrażliwe na gola po 80. minucie. Luksemburg przegrał 3 z 4 meczów.
**Rynek:** różnica 1X2 w normie (≤ 3 pp).

### Bułgaria - Islandia (Liga Narodów, 13.11, 20:45, Sofia; sędzia Florian Badstubner)
**Typ:** Islandia wygra | **p:** 49,7% | **Fair:** 2.01 | **Pewność:** niska-średnia; wyrównany (blisko 50%): brak mocnego typu
Alternatywa: Islandia wygra lub zremisuje (X2) 77,8% (fair 1.29). Under 3.5 82,9% (fair 1.21, graniczny).
λ: Bułgaria 0.80, Islandia 1.35 (Islandia xG 1,8; Bułgaria traci 1,3).

| Rynek | p | fair | Uwagi |
|---|---|---|---|
| 1 / X / 2 | 22,2 / 28,1 / 49,7% | 4.51 / 3.56 / 2.01 | rynek 21,8 / 26,8 / 51,5% (4.30/3.50/1.82) |
| DC 1X / X2 / 12 | 50,3 / 77,8 / 71,9% | 1.99 / 1.29 / 1.39 | |
| Over 1.5 / 2.5 / 3.5 | 63,3 / 36,4 / 17,1% | 1.58 / 2.75 / 5.85 | |
| Under 2.5 / 3.5 | 63,6 / 82,9% | 1.57 / 1.21 | |
| BTTS tak / nie | 40,8 / 59,2% | 2.45 / 1.69 | |
| Islandia -1.5 | 23,9% | 4.18 | |
| Rożne (śr. 9,5) | O 8.5: 58,8%; O 9.5: 47,1% | 1.70 / 2.12 | BUL 4,0 + ISL 6,3; niska pewność |
| Kartki (śr. 4,4) | O 3.5: 60,4%; O 4.5: 43,7% | 1.65 / 2.29 | BUL 3,0 kartki/m, ISL 1,8; niska pewność |

**Statystyki:** Islandia: 3-0 BUL, 3-0 LUX, 1-1 EST, plus mecz z Estonią bez wyniku (1,8 gola/m, traci 0,3). Bułgaria: 1-2 LUX, 0-3 ISL, 0-2 LUX (wyjazd), mecz z EST bez wyniku.
**H2H:** 03.10.2026 Islandia - Bułgaria 3:0.
**Informacje:** Islandia bez M. Andersona (kontuzja); Bułgaria bez zgłoszonych nieobecnych (trener Ribarski). Brak newsów z sieci.
**Ryzyka:** remis (28%) i wygrana Bułgarii u siebie (22%); wygrana Islandii zależy od ofensywy w wyjeździe. Obie drużyny u siebie bywały defensywne.
**Rynek:** 51,5% vs mój 49,7%; zgodne.

### Andora - Gibraltar (Liga Narodów, 13.11, 20:45, Encamp; sędzia Robert Hennessy)
**Typ:** brak mocnego typu; Under 2.5 (70,4%, fair 1.42) jako najlepszy rynek | **Pewność:** niska
λ: Andora 1.25, Gibraltar 0.65 (łącznie 1.9). Różnica z rynkiem: Andora 50,9% vs rynek 54,9% (-4 pp).

| Rynek | p | fair | Uwagi |
|---|---|---|---|
| 1 / X / 2 | 50,9 / 29,8 / 19,3% | 1.97 / 3.35 / 5.17 | rynek 54,9 / 29,0 / 16,0% (1.69/3.20/5.80) |
| DC 1X / X2 / 12 | 80,7 / 49,1 / 70,2% | 1.24 / 2.04 / 1.42 | |
| Over 1.5 / 2.5 | 56,6 / 29,6% | 1.77 / 3.38 | |
| Under 1.5 / 2.5 / 3.5 | 43,4 / 70,4 / 87,5% | 2.31 / 1.42 / 1.14 | Under 3.5 pod progiem |
| BTTS tak / nie | 34,1 / 65,9% | 2.93 / 1.52 | |
| Rożne (śr. 8,0) | O 7.5: 53,2%; O 8.5: 40,7% | 1.88 / 2.46 | AND 4,0 + GIB 2,5; niska pewność |
| Kartki (śr. 4,6) | O 3.5 ~ 64%; O 4.5 ~ 48% | 1.57 / 2.10 | AND 3,7 kartki/m, GIB 1,5; niska pewność |

**Statystyki:** Andora: 1-2 MLT, 0-3 LIT, 0-1 MLT, wynik z Gibraltarem w danych nieznany (xG 0,7/m, traci 1,0). Gibraltar: 1-1 MLT, 2-0 Liechtenstein, 4-1 Kajmany (towarzyski), xG 0,3/m (próba).
**H2H:** Gibraltar wygrał 1:0 w 2022 i 2024, 0:0 w 2021; mecz z 27.09.2026 bez wyniku w danych.
**Informacje:** Andora bez zgłoszonych nieobecnych (trener Álvarez de Eulate); Gibraltar bez Torrilli (zawieszenie, Superbet). Brak newsów z sieci.
**Ryzyka:** wygrana Gibraltaru (19,3%) i remis 29,8%; Andora zdobywa mało (0,3 gola/m). Wynik 1:0 lub 0:0 najbardziej prawdopodobny.
**Rynek:** różnica 4 pp pod rynkiem uzasadniona formą Andory (0 punktów, brak goli); w granicach zasady.

### Liechtenstein - Azerbejdżan (Liga Narodów, 13.11, 20:45, Vaduz; sędzia Kristo Tohver)
**Typ:** Azerbejdżan wygra | **p:** 69,9% | **Fair:** 1.43 | **Pewność:** średnia
Alternatywa: Azerbejdżan -1.5 (45,1%, fair 2.22).
λ: Liechtenstein 0.70 (podłoga reprezentacji; w próbce 0 goli), Azerbejdżan 2.10. Mój p jest 4,6 pp poniżej rynku (74,5%) - różnica w granicy 5 pp.

| Rynek | p | fair | Uwagi |
|---|---|---|---|
| 1 / X / 2 | 11,2 / 18,9 / 69,9% | 8.92 / 5.29 / 1.43 | rynek 7,7 / 17,8 / 74,5% (12/5.20/1.24) |
| DC 1X / X2 / 12 | 30,1 / 88,8 / 81,1% | 3.32 / 1.13 / 1.23 | X2 pod progiem |
| Over 1.5 / 2.5 / 3.5 | 76,9 / 53,1 / 30,8% | 1.30 / 1.88 / 3.25 | |
| Under 2.5 / 3.5 | 46,9 / 69,2% | 2.13 / 1.45 | |
| BTTS tak / nie | 44,2 / 55,8% | 2.26 / 1.79 | BTTS nie wątpliwe: Liechtenstein 0 goli w 4 meczach |
| Azerbejdżan -1.5 | 45,1% | 2.22 | |
| Rożne (śr. 9,0, brak danych LIE) | O 8.5: 53,0% | 1.89 | dane rożnych LIE = 0 (próba niepełna); niska pewność |
| Kartki (śr. 4,3) | O 3.5 ~ 59%; O 4.5 ~ 42% | 1.70 / 2.38 | niska pewność |

**Statystyki:** Liechtenstein: 0-2 CYP, 0-2 LIT, 0-2 MLT (wyjazd), 0-2 GIB; xG 0,1/m. Azerbejdżan: 1-0 LIT, 1-1 LIT, 1-0 TJK, plus 1:0 w pierwszym meczu z Liechtensteinem (wynik w danych brak); xG 1,7/m, ale tylko 0,7 gola/m.
**H2H:** 01.10.2026 Azerbejdżan - Liechtenstein (wynik brak w danych).
**Informacje:** brak danych o nieobecnych (Superbet zwrócił błąd), brak newsów z sieci.
**Ryzyka:** Azerbejdżan strzela mało (0,7/m) mimo xG 1,7, wygrywa głównie 1:0; remis p 18,9%. Under 2.5 (46,9%) nie jest dobrym typem przy λ 2,8 łącznie.
**Rynek:** AZE 1.24, mój fair 1.43; rynek wycenia mocniej (różnica 4,6 pp).

### Mołdawia - Kazachstan (Liga Narodów, 13.11, 18:00, Kiszyniów; sędzia Colombo)
**Typ:** brak mocnego typu (wyrównany): najlepszy Under 3.5 (78,9%, fair 1.27) | **Pewność:** niska
λ: Mołdawia 1.20, Kazachstan 1.15 (łącznie 2.35).

| Rynek | p | fair | Uwagi |
|---|---|---|---|
| 1 / X / 2 | 37,2 / 28,0 / 34,8% | 2.69 / 3.57 / 2.88 | rynek 35,4 / 31,8 / 32,9% (2.65/2.95/2.85) |
| DC 1X / X2 / 12 | 65,2 / 62,8 / 72,0% | 1.53 / 1.59 / 1.39 | |
| Over 1.5 / 2.5 / 3.5 | 68,1 / 41,7 / 21,1% | 1.47 / 2.40 / 4.74 | |
| Under 2.5 / 3.5 | 58,3 / 78,9% | 1.72 / 1.27 | |
| BTTS tak / nie | 47,8 / 52,2% | 2.09 / 1.91 | obie tracą 1,8-2,0/m |
| Rożne (śr. 10,5) | O 9.5: 58,4%; O 10.5: 47,2% | 1.71 / 2.12 | MDA 5,5 + KAZ 5,5; niska pewność |
| Kartki (śr. 3,4) | O 2.5 ~ 65%; O 3.5 ~ 44% | 1.54 / 2.27 | MDA 0,8 kartki/m, KAZ 1,8-2,0, WO 2 czerwone w meczu KAZ-FRO; niska pewność |

**Statystyki:** Mołdawia: 0-2 SVK, 2-1 KAZ (wyjazd), 1-1 FRO, 0-4 SVK (traci 2,0/m, strzela 0,8). Kazachstan: 1-1 FRO, 1-2 MDA, 1-2 SVK, 2-2 FRO (2 czerwone kartki), xG 1,0.
**H2H:** 02.10.2026 Kazachstan - Mołdawia 1:2; 2022 Mołdawia - Kazachstan 1:2; bilans całościowy 3-1-4 dla Kazachstanu.
**Informacje:** Mołdawia bez zgłoszonych nieobecnych (trener Popescu); Kazachstan bez Maliya (zawieszenie; trener van't Schip). Brak newsów z sieci.
**Ryzyka:** wyrównany (3-way ~ 1/3 każde); wynik zależy od formy dnia, remis 28% (rynek 31,8%).
**Rynek:** zgodne w granicach 4 pp.

---

## Ranking top rynków (fair > 1.15; tylko oszacowania)
| # | Mecz | Rynek | p | Fair | Pewność | Zależy od | Kurs rynkowy |
|---|---|---|---|---|---|---|---|
| 1 | Słowacja - WO | Słowacja wygra | 68,0% | 1.47 | średnia | skład (Lobotka out) | 1.37 (Superbet) |
| 2 | Niemcy - Serbia | Niemcy wygrają | 71,7% | 1.39 | średnia | skład Niemców, motywacja Serbii | 1.30 |
| 3 | Szkocja - MKD | Szkocja wygra | 76,7% | 1.30 | średnia | kontuzje obrońców | DC 1X 1.02 (1X2 brak) |
| 4 | Azerbejdżan - LIE | Azerbejdżan wygra | 69,9% | 1.43 | średnia | brak newsów | 1.24 |
| 5 | Holandia - Grecja | 1X | 80,7% | 1.24 | średnia | skład Holandii | 1.16 (graniczny) |
| 6 | Luksemburg - Estonia | Under 2.5 | 73,1% | 1.37 | niska-średnia | λ ≤ 2,0 | nie pobrano |
| 7 | Szkocja - MKD | Szkocja -1.5 | 54,5% | 1.83 | niska-średnia | skuteczność Szkotów | nie pobrano |
| 8 | Niemcy - Serbia | Niemcy -1.5 | 47,6% | 2.10 | niska | j.w. | nie pobrano |

Brak mocnych typów (blisko 50%/wyrównane): Słowenia - Szwajcaria (wynik), Luksemburg - Estonia (1X2), Bułgaria - Islandia, Andora - Gibraltar, Mołdawia - Kazachstan. Typy na rożne i kartki: bez rekomendacji na kupon (brak statystyk sędziów, próby ok. 4 meczów, składy niepotwierdzone).

## Tabela kandydatów na kupon (wejście dla bet-slip-builder)
| Mecz | Rynek | p | Fair | Pewność | Od czego zależy | Kurs rynkowy znany |
|---|---|---|---|---|---|---|
| Słowacja - WO | 1 | 68,0% | 1.47 | średnia | Lobotka | tak, 1.37 |
| Niemcy - Serbia | 2 | 71,7% | 1.39 | średnia | skład | tak, 1.30 |
| Szkocja - MKD | 1 | 76,7% | 1.30 | średnia | kontuzje obrońców | DC tylko, 1X 1.02 |
| Azerbejdżan - LIE | 2 | 69,9% | 1.43 | średnia | brak newsów | tak, 1.24 |
| Holandia - Grecja | 1X | 80,7% | 1.24 | średnia | skład | tak, 1.16 |
| Luksemburg - Estonia | Under 2.5 | 73,1% | 1.37 | niska-średnia | gol po 80' | nie |
| Holandia - Grecja | Under 3.5 | 75,8% | 1.32 | średnia | | nie |
| Mołdawia - Kazachstan | Under 3.5 | 78,9% | 1.27 | niska | | nie |
| Bułgaria - Islandia | X2 | 77,8% | 1.29 | niska-średnia | forma Islandii | nie |
| Słowenia - Szwajcaria | Under 3.5 | 77,9% | 1.28 | średnia | | nie |

Uwaga: to oszacowania probabilistyczne, nie gwarancje.
