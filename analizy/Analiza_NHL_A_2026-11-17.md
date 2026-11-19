# Analiza NHL, noc 17->18.11.2026 (część A, 6 meczów)

Sprawdzenie: 17.11.2026 ok. 13:10 PL. Skład i bramkarze mogą się zmienić do startu.
Źródła: NHL.com standings (sportsdata MCP, stan 17.11), ESPN scoreboard (mecze z 16.11), DailyFaceoff starting goalies 17.11 (wszyscy 22 bramkarze "Unconfirmed", 0/22), kursy Superbet (superbet-mcp), model `nhl_model.py` + kalibracja ręczna remisu.
BettingPros: pominięte (nie sprawdzano klucza w tym zadaniu), dlatego rynek odniesienia = Superbet (kursy bez marży liczone samodzielnie).
Rynki zawodnika: Superbet w pobranym zakresie ma tylko kombinacje "zawodnik + wygrana drużyny" (Boost/Bet Builder), bez czystych linii strzałów/punktów/obron, a drugiego niezależnego źródła średnich nie zebrano -> **brak podstaw do typów zawodnika** (nie rekomenduję żadnego).

## Ustalenia wspólne
- **Back-to-back:** ESPN dla 16.11 (czasu USA) pokazuje tylko dwa mecze (MTL@NYR, VAN@UTA); żadna z 12 drużyn z tej listy nie grała poprzedniej nocy -> brak back-to-back, brak korekty zmęczenia. Wszystkie mecze: gospodarz = pierwszy podany w Superbet (BOS, FLA, NYI, PHI, WPG, TBL).
- **Remis po 60':** Poisson zaniża remis (16-17% vs rynek ~22-24%), więc w tabelach 60' remis ustawiono na 22%, a 1/2 przeskalowano proporcjonalnie.
- **Rozliczenie:** "Mecz" 1X2 = 60 minut; "Zwycięzca (z dogrywką i karnymi)" = moneyline; total i handicap Superbet liczą dogrywkę i karne (z OT). Total modelu = regulamin + gol w OT.
- **Rynek totalu:** wszędzie ok. 5.5-6.0 (O5.5 ~1.72-1.77 / U5.5 ~2.0-2.1). Własne p totalu trzymam w granicach 3 pp od rynku bez marży (zasada Poissona z Kalibracji).
- Wniosek ogólny: **żaden rynek nie ma dodatniego EV względem Superbet** (różnice własne p vs rynek <3-4 pp, a marża ~6-8%). Brak mocnych typów, pułapy p na zwycięzcę ~55-59%.

## 1. Boston Bruins - Los Angeles Kings (18.11, 01:00 PL; 19:00 ET 17.11) | Superbet 15585794
**Typ:** Boston ML (z OT) | **p:** 59% | **fair:** 1.69 | **Pewność:** niska-średnia (bramkarze niepotwierdzeni) | kurs 1.62 (EV ~ -4%)
| Rynek | p | fair | Kurs Superbet | Uwaga |
|---|---|---|---|---|
| 60' BOS / X / LAK | 48% / 22% / 30% | 2.08 / 4.55 / 3.30 | 2.02 / 4.10 / 2.90 | brak value |
| ML BOS (z OT) | 59% | 1.69 | 1.62 | |
| ML LAK | 41% | 2.44 | 2.25 | |
| Puck line LAK +1.5 | 65% | 1.54 | 1.47 | EV -4% |
| Puck line BOS +1.5 | 81% | 1.23 | 1.21 | krótki, EV -2% |
| Puck line BOS -1.5 | 35% | 2.87 | 2.57 | |
| Total O5.5 / U5.5 | 54% / 46% | 1.85 / 2.17 | 1.73 / 2.07 | |
| Total U6.5 | 58% | 1.72 | 1.70 | EV ~ -1% |
| Total O4.5 | 74% | 1.35 | 1.23 | EV -9% |
**Statystyki:** BOS 13-6-1 (27 pkt/20 m.), GF 3.60, GA 2.60 (najlepsza obrona z tej szóstki), L2. LAK 5-11-2 (18 m.), GF 2.72, GA 3.50, L4, 3 wygrane w ostatnich 10. Gospodarz +0.1 gola.
**H2H:** poprzednie mecze w sezonie (Kings-Bruins 17.10.2026) bez wiążących danych; waga niska.
**Bramkarze:** BOS Swayman .906 / 2.60 (9-5-1), LAK Forsberg .908 / 2.39 (0-6-1) - obaj Unconfirmed (DailyFaceoff, 17.11 ok. 13:15). Różnica jakości niewielka, brak korekty λ.
**Media:** web search nie dał świeżych newsów (kontuzje/skład) - brak potwierdzonych absencji; oznaczam jako lukę.
**Oczekiwane gole:** BOS 3.25 - LAK 2.65 (razem 5.9). Korekta: kryzys LAK (underdog) wpisana w λ LAK (2.65 zamiast ~2.8).
**Ryzyka:** zmiana bramkarza, OT (gospodarz wygrywa w ML także po OT), pusta bramka.

## 2. Florida Panthers - Edmonton Oilers (01:00 PL) | Superbet 15591978
**Typ:** brak mocnego typu (mecz równy) | ML 50/50 | **Pewność:** niska
| Rynek | p | fair | Kurs | Uwaga |
|---|---|---|---|---|
| 60' FLA / X / EDM | 39% / 22% / 39% | 2.56 / 4.55 / 2.56 | 2.32 / 4.00 / 2.50 | |
| ML FLA / EDM | 50% / 50% | 2.00 / 2.00 | 1.83 / 1.97 | brak value |
| Puck line FLA +1.5 / EDM +1.5 | 73% / 75% | 1.37 / 1.34 | n/d | |
| Total O5.5 / U5.5 | 56% / 44% | 1.79 / 2.27 | 1.72 / 2.10 | |
| Total U6.5 | 57% | 1.75 | 1.71 | |
**Statystyki:** EDM 16-3-3 (35 pkt), GF 3.95 (najlepszy atak), GA 2.73, W5. FLA 12-7-3, GF 3.18, GA 2.86, ostatni mecz OT. Własne λ (EDM 3.1 / FLA 3.0) wynikają z regresji ataku EDM do średniej (próbka 22 m.), mała przewaga EDM zbita z domem FLA; rynek daje FLA ok. 52% (nie schodzę pod rynek o >5 pp).
**H2H:** brak danych do wniosków (finały 2024/2025 są nieistotne dla obecnych składów).
**Bramkarze:** EDM Devon Levi .906 / 2.48 (9-1-0), FLA Markstrom .906 / 2.41 - obaj Unconfirmed; DailyFaceoff wcześniej wskazywał Jarry jako opcję w EDM (wątpliwość kto w bramce).
**Oczekiwane gole:** FLA 3.0 - EDM 3.1 (6.1).
**Ryzyka:** niepewność bramkarza EDM, wysoki ofensywny potencjał (O5.5 56%).

## 3. New York Islanders - Columbus Blue Jackets (01:00 PL) | Superbet 15586862
**Typ:** NYI ML | **p:** 58% | **fair:** 1.72 | **Pewność:** niska-średnia | kurs 1.67 (EV -3%)
| Rynek | p | fair | Kurs | Uwaga |
|---|---|---|---|---|
| 60' NYI / X / CBJ | 47% / 22% / 31% | 2.13 / 4.55 / 3.23 | 2.12 / 3.85 / 2.82 | |
| ML NYI / CBJ | 58% / 42% | 1.72 / 2.38 | 1.67 / 2.17 | |
| Puck line CBJ +1.5 / NYI +1.5 | 66% / 80% | 1.52 / 1.25 | n/d | |
| Total O5.5 / U5.5 | 53% / 47% | 1.89 / 2.13 | 1.83 / 1.95 | |
| Total U6.5 | 59% | 1.69 | 1.62 | |
**Statystyki:** NYI 9-6-4 (19 m.), GF 3.16, GA 2.95, W2. CBJ 7-11-0 (18 m.), GF 2.50, GA 3.22, L4 (kryzys underdoga wliczony).
**H2H:** brak istotnych danych.
**Bramkarze:** NYI Sorokin .915 / 2.53 (7-4-2), CBJ Talbot .909 / 2.50 - Unconfirmed. Przewaga bramkarska NYI zawarta w λ.
**Oczekiwane gole:** NYI 3.2 - CBJ 2.65 (5.85).
**Ryzyka:** niska skuteczność ataku NYI, OT.

## 4. Philadelphia Flyers - Buffalo Sabres (01:00 PL) | Superbet 15586943
**Typ:** brak mocnego typu (BUF ML 54%) | **Pewność:** niska
| Rynek | p | fair | Kurs | Uwaga |
|---|---|---|---|---|
| 60' PHI / X / BUF | 36% / 22% / 42% | 2.78 / 4.55 / 2.38 | 2.65 / 3.85 / 2.25 | |
| ML BUF / PHI | 54% / 46% | 1.85 / 2.17 | 1.77 / 2.02 | brak value |
| Puck line BUF +1.5 / PHI +1.5 | 71% / 77% | 1.41 / 1.30 | n/d | |
| Total O5.5 / U5.5 | 53% / 47% | 1.89 / 2.13 | 1.73 / 2.07 | |
| Total U6.5 | 59% | 1.69 | 1.70 | |
**Statystyki:** BUF 8-8-4 (20 m.), GF 2.75, GA 3.50, L1. PHI 6-11-6 (23 m.), GF 2.30, GA 3.35, L1. Obie drużyny z grona słabych defensyw i słabych ataków.
**H2H:** brak istotnych danych.
**Bramkarze:** BUF Lyon .909 / 2.48 (0-1-1, nietypowy bilans - możliwy rezerwowy), PHI Woll .902 / 2.91 - Unconfirmed. Niska jakość obu drużyn = pewność niska.
**Media:** TSN "ice chips" wspomina o Peterce (BUF) z wstrząśnieniem mózgu, ale artykuł nieznanej daty; status JJ Peterka niepotwierdzony - sprawdzić (Superbet ma jego prop strzałów w BOS-LAK, co sugeruje inny kontekst; dane nie wiążące).
**Oczekiwane gole:** PHI 2.8 - BUF 3.05 (5.85).
**Ryzyka:** wyrównany, niskojakościowy mecz.

## 5. Winnipeg Jets - Ottawa Senators (01:00 PL; 18:00 CT) | Superbet 15587141
**Typ:** OTT ML | **p:** 55% | **fair:** 1.82 | **Pewność:** niska-średnia | kurs 1.75 (EV -4%)
| Rynek | p | fair | Kurs | Uwaga |
|---|---|---|---|---|
| 60' WPG / X / OTT | 34% / 22% / 44% | 2.94 / 4.55 / 2.27 | 2.70 / 3.90 / 2.20 | |
| ML OTT / WPG | 55% / 45% | 1.82 / 2.22 | 1.75 / 2.07 | brak value |
| Puck line OTT +1.5 / WPG +1.5 | 77% / 70% | 1.30 / 1.43 | n/d | |
| Total O5.5 / U5.5 | 54% / 46% | 1.85 / 2.17 | 1.77 / 2.02 | |
| Total U6.5 | 58% | 1.72 | 1.66 | |
**Statystyki:** OTT 13-6-2 (28 pkt/21 m.), GF 3.24, GA 2.90, W2. WPG 10-8-3, GF 3.14, GA 3.43, W6 (seria 6 wygranych; forma faworyta/gospodarza już w kursie).
**H2H:** brak istotnych danych.
**Bramkarze:** OTT Ullmark .939 / 1.47 (9-1-0), WPG Daws .892 / 2.58 (4-3-0) - Unconfirmed. Hellebuyck wg TSN został oddany do New Jersey (data niezweryfikowana), więc Daws jako startowy jest spójny. Przewaga bramkarska OTT już wpisana (λ WPG obniżona, λ OTT podniesiona), ale Ullmark ma ekstremalnie wysokie SV% (regresja) i jedna z notatek TSN mówi o jego absencji w innym terminie - sprawdzić przed meczem.
**Oczekiwane gole:** WPG 2.85 - OTT 3.1 (5.95).
**Ryzyka:** zmiana bramkarza OTT (Johansson) zmieniłaby p o ok. 4-5 pp; zimowe warunki/podróż niepotwierdzone.

## 6. Tampa Bay Lightning - Washington Capitals (01:30 PL; 19:30 ET) | Superbet 15587006
**Typ:** TBL ML | **p:** 58% | **fair:** 1.72 | **Pewność:** niska-średnia | kurs 1.61 (EV -7%)
| Rynek | p | fair | Kurs | Uwaga |
|---|---|---|---|---|
| 60' TBL / X / WSH | 47% / 22% / 31% | 2.13 / 4.55 / 3.23 | 2.02 / 4.00 / 2.95 | |
| ML TBL / WSH | 58% / 42% | 1.72 / 2.38 | 1.61 / 2.27 | brak value |
| Puck line WSH +1.5 / TBL +1.5 | 66% / 80% | 1.51 / 1.26 | n/d | |
| Total O5.5 / U5.5 | 57% / 43% | 1.75 / 2.33 | n/d (O5.5 ok. 1.7) | |
| Total U6.5 | 56% | 1.79 | n/d | |
**Statystyki:** TBL 13-5-2 (28 pkt/20 m.), GF 3.70, GA 2.95, L1. WSH 10-8-0 (18 m.), GF 3.44, GA 3.61, L2.
**H2H:** brak istotnych danych.
**Bramkarze:** TBL Vasilevskiy .889 / 2.74 (9-5-1), WSH Thompson .889 / 3.17 (7-5-0) - Unconfirmed; obaj z słabym SV% w sezonie, co podnosi total (λ razem 6.1, O5.5 57%, najwyższe z szóstki).
**Oczekiwane gole:** TBL 3.3 - WSH 2.8 (6.1).
**Ryzyka:** regresja SV% bramkarzy w obie strony (wariancja totalu), rynek totalu dla meczu nie pobrany - sprawdzić.

## Tabela kandydatów na kupon (wszystkie bez dodatniego EV względem Superbet)
| Mecz | Rynek | p | fair | Kurs SB | EV | Pewność | Zależy od |
|---|---|---|---|---|---|---|---|
| BOS-LAK | BOS ML (OT) | 59% | 1.69 | 1.62 | -4% | niska-śr. | Swayman/Forsberg |
| BOS-LAK | LAK +1.5 (puck line) | 65% | 1.54 | 1.47 | -4% | niska-śr. | bramkarze |
| NYI-CBJ | NYI ML | 58% | 1.72 | 1.67 | -3% | niska-śr. | Sorokin |
| WPG-OTT | OTT ML | 55% | 1.82 | 1.75 | -4% | niska-śr. | Ullmark |
| TBL-WSH | TBL ML | 58% | 1.72 | 1.61 | -7% | niska-śr. | Vasilevskiy |
| TBL-WSH | O5.5 | 57% | 1.75 | ok. 1.7 | ~ -3% | niska | bramkarze |
| FLA-EDM | O5.5 | 56% | 1.79 | 1.72 | -4% | niska | oba ataki |
| BOS-LAK | U6.5 | 58% | 1.72 | 1.70 | -1% | niska | |
Pominięte jako fair <= 1.15: Over 3.5, Under 8.5. Over 4.5 (p ~74%, fair 1.35) i Under 7.5 (p ~75%, fair 1.33) mają kursy 1.23-1.27 i ujemne EV (-6 do -9%).

To oszacowania probabilistyczne, nie gwarancje; skład i bramkarze mogą się zmienić do rozpoczęcia meczów.
