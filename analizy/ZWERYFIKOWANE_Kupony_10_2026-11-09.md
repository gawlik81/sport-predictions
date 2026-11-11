# Kupony NBA + NHL, noc 09→10.11.2026 (czas polski)

Analizy: `analizy/Analiza_NBA_NHL_noc_2026-11-09.md` (skille `nba-analyst`, `nhl-analyst`). Kupony złożone wg `bet-slip-builder`.

## 1. Okres, źródło kursów
- Okres: noc NBA i NHL z 09.11 na 10.11.2026. Wszystkie mecze startują po 01:00 PL, żaden nie jest rozegrany ani trwający.
- **Betclic.pl i gg397.bet niedostępne**: w sesji nie było MCP przeglądarki (`mcp__claude-in-chrome__*`). Wszystkie kursy to **fallback, nie kursy Betclic**: DraftKings (ESPN pickcenter), FanDuel. Kursy krajowe będą zwykle niższe, więc EV na Betclic może wyjść gorsze.
- Kursy z godzin popołudniowych 09.11, mogą się zmienić do startu.
- Poziomy luzowania: wybrane 0-2 (automatycznie).

## 2. Terminarz (11 wydarzeń)
NBA 8, NHL 3. Nic nie pominięto. Godziny PL (USA ET w nawiasie):
- 01:00 CLE@CHA, WAS@DET, LAL@ATL (19:00 ET)
- 01:30 MEM@TOR; 02:00 IND@DAL; 02:30 DEN@HOU; 03:00 SA@PHX; 04:00 NO@GS
- NHL: 02:00 NYR@EDM; 03:30 PHI@VAN; 04:00 NYI@SJ

## 3. Pula nóg po filtrach (jedna noga na mecz, p > 50%, fair > 1.15)
| Mecz | Rynek | p | Kurs (źródło) | Fair | EV | Pewność |
|---|---|---|---|---|---|---|
| CHA-CLE | CLE ML | 76% | 1.297 (DK) | 1.31 | -1.4% | średnia (Allen DTD) |
| PHX-SA | SA ML | 75% | 1.268 (DK) | 1.33 | -4.9% | średnia |
| GS-NO | GS ML | 75.5% | 1.262 (DK) | 1.32 | -4.7% | średnia |
| DET-WAS | DET ML | 76.8% | 1.204 (FanDuel) | 1.30 | -7.5% | średnia (Davis) |
| PHI@VAN | VAN +1.5 | 76.9% | 1.459 (DK) | 1.30 | +12.2% | niska, przewaga niepotwierdzona |
| NYI@SJ | SJ +1.5 | 76.9% | 1.459 (DK) | 1.30 | +12.2% | niska, przewaga niepotwierdzona |
| HOU-DEN | HOU ML | 71% | 1.31 (Novibet) | 1.41 | -6.9% | niska (Jokić/Murray) |

Odpadły (p ≤ 50% albo niemożliwe do sparowania z p > 50%): DAL ML (61%, 1.649), EDM ML (61%, 1.617), NYR +1.5 (63%, 1.54), TOR-MEM Under 228.5 (52%), ATL ML (55%), PHI ML i NYI ML (54%), spready i totale (monety). Rynki zawodnika: brak potwierdzonych statusów i linii, więc żaden nie wszedł.

Warunek p > 50% przy kuponie dwunogowym wymaga nóg o p ≥ ok. 70%, a tych jest 7. Stąd maksymalnie 3 kupony.

## 4. Kupony (3 zamiast 10, nie dobijam na siłę)

### Kupon 1, poziom 0 (bazowy formalnie), ryzykowny: "po bramkarzu"
| Godzina PL (USA) | Mecz | Typ | p | Kurs | Fair | EV |
|---|---|---|---|---|---|---|
| 01:00 (09.11 19:00 ET) | CHA-CLE | CLE ML | 76% | 1.297 DK | 1.31 | -1.4% |
| 03:30 (09.11 18:30 PT) | PHI@VAN | VAN +1.5 puck line | 76.9% | 1.459 DK | 1.30 | +12.2% |

Łączne p 58.4% | fair 1.71 | kurs 1.89 | EV +10.6% (model).
Po korekcie "przewaga niepotwierdzona" (p nogi VAN = rynek + 5 pp = 70.7%): p 53.7%, EV +1.7%.
Stawka: 0.5% bankrolla (1/4 Kelly od p po korekcie). Sugestia, nie porada finansowa.
Ryzyko: bramkarze PHI/VAN niepotwierdzeni, PHI gra drugi dzień z rzędu (możliwy rezerwowy). Model Poissona zaniża ogon wysokich wyników.

### Kupon 2, poziom 0 (bazowy formalnie), ryzykowny: "po bramkarzu"
| Godzina PL (USA) | Mecz | Typ | p | Kurs | Fair | EV |
|---|---|---|---|---|---|---|
| 03:00 (09.11 21:00 ET) | PHX-SA | SA ML | 75% | 1.268 DK | 1.33 | -4.9% |
| 04:00 (09.11 19:00 PT) | NYI@SJ | SJ +1.5 puck line | 76.9% | 1.459 DK | 1.30 | +12.2% |

Łączne p 57.7% | fair 1.73 | kurs 1.85 | EV +6.7% (model).
Po korekcie (p nogi SJ 70.7%): p 53.0%, EV -1.9%, więc stawka **0%**.
Ryzyko: Sorokin i Askarov niepotwierdzeni; Wembanyama i Vassell bez potwierdzonego statusu (spread skoczyłby o 4-6 pkt).

### Kupon 3, poziom 2 (poniżej progów: EV -11.9%)
| Godzina PL (USA) | Mecz | Typ | p | Kurs | Fair | EV |
|---|---|---|---|---|---|---|
| 04:00 (09.11 22:00 ET) | GS-NO | GS ML | 75.5% | 1.262 DK | 1.32 | -4.7% |
| 01:00 (09.11 19:00 ET) | DET-WAS | DET ML | 76.8% | 1.204 FanDuel | 1.30 | -7.5% |

Łączne p 58.0% | fair 1.72 | kurs 1.52 | EV -11.9%. Stawka 0%.
Złamany próg: EV (poziom 2, ranking po p). Kurs 1.52 ledwie nad dolną granicą 1.5.
Ryzyko: Davis (WAS) questionable; Curry i Zion bez potwierdzenia; b2b NO.

## 5. Ostrzeżenia
- Kursy to fallback (DraftKings, FanDuel), nie Betclic; rozbieżności względem Betclic niezweryfikowane.
- Założenie niezależności meczów.
- Noga "+1.5" w NHL ma EV opartą na p wyższym od rynku o ok. 11 pp bez twardej informacji: traktować jako przewagę niepotwierdzoną.
- Składy, bramkarze i statusy DTD (Reaves, Allen, Davis, Jokić, Murray, Wembanyama) mogą się zmienić do startu.
- Nie wszedł do kuponów HOU ML (p 71%, EV -6.9%, status Jokicia niepewny).
- Oszacowania probabilistyczne, nie gwarancje.
