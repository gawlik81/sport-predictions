# Analiza piłkarska cz.1, 30-31.10.2026 (Ligue 1, LaLiga, Premier League)

Czas polski (CET, po zmianie czasu 25.10). Wszystkie 17 meczów potwierdzone jako "Scheduled" (ESPN, Pinnacle), bez odwołań i przełożeń.

## Metoda i ograniczenia danych (ważne)

- **Źródła:** ESPN (tabele, forma, kursy DraftKings), Pinnacle przez MCP `sportsdata` (1X2, total goli i rożnych dla 9 meczów; kursy bez marży), FPL (`fpl_players`: status zdrowia graczy PL). Skrypty: `poisson.py` (gole, 1X2, BTTS), `markets.py` (rożne, kartki, faule).
- **λ:** dopasowane do rynku bez marży (1X2 + total), potem skorygowane tylko tam, gdzie była konkretna przesłanka (opis przy meczu). Bez xG (brak w MCP). Żadna korekta nie schodzi pod rynek o więcej niż 5 pp.
- **Kontuzje/składy:** dla Premier League status z FPL (stan na 30.10, rano). **Dla LaLiga i Ligue 1 nie znalazłem aktualnych komunikatów o kontuzjach ani przewidywanych składów** (WebSearch zwraca tylko stare sezony). Dlatego pewność w tych ligach maks. średnia, a rynki zawodnika bez typów. Przewidywane składy ogłaszane są dopiero na ~1 h przed meczem.
- **Rożne:** dla 9 meczów jest linia Pinnacle (średnia wyprowadzona z linii i ceny stron: oznaczone "Pinn."). Dla pozostałych 8 to szkic ze średniej ligowej (bardzo niska pewność).
- **Kartki i faule:** brak sędziów (obsady jeszcze nieogłoszone lub niedostępne w MCP) i brak statystyk drużyn. Podaję szkic ze średniej ligowej: kartki PL 4,0, LaLiga 5,3, Ligue 1 4,3 (żółta = 1); faule PL 21,5, LaLiga 24,0, Ligue 1 22,5. **Pewność bardzo niska, bez rekomendacji na kupon** (reguła: nieznany sędzia, brak min. 2 źródeł).
- **BettingPros:** nie użyto (poza zakresem czasowym tej analizy; klucz w środowisku jest, ale nie odpytywałem API).
- **Rynki zawodnika:** brak potwierdzonych składów, więc **żadnych typów** (reguła skilla).
- **Troyes - Le Mans:** to NIE jest Ligue 2 ani puchar. Według ESPN i Pinnacle to **Ligue 1 2026-27** (Troyes i Le Mans to beniaminkowie; 9. kolejka, Stade de l'Aube). Dane są, więc mecz jest przeanalizowany.
- Poisson lekko niedoszacowuje remisów w meczach bardzo jednostronnych (Barcelona, PSG), traktuj p remisu jako dolną granicę.

## Odrzucone mecze

Brak. Wszystkie 17 przeanalizowane. Mecze bez mocnego typu wynikowego (wyrównane): Lille - Lens, Hull - Ipswich, Troyes - Le Mans, Nice - Rennes, Rayo - Celta, Coventry - Sunderland (patrz sekcje).

---

# 30.10 (piątek)

### Le Havre - PSG (Ligue 1, 30.10, 19:00, Stade Océane)
**Typ:** PSG wygra | **p:** 71% | **Fair:** 1.41 | **Pewność:** średnia. Alternatywa: Over 2.5 gola 67% (fair 1.49).
**λ:** 0,95 / 2,50 (rynek bez marży: PSG 73,8%; skorygowano -3 pp, bo (a) Le Havre w desperacji: 0 wygranych w 8 meczach, 2 pkt, (b) PSG po środzie Ligi Mistrzów, ryzyko rotacji, niepotwierdzone).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 12,3% / 16,6% / 71,1% | 8.13 / 6.04 / 1.41 | średnia |
| 1X / X2 / 12 | 28,9% / 87,7% / 83,4% | 3.46 / 1.14 / 1.20 | średnia (X2 poniżej progu 1.15) |
| Over 1.5 / 2.5 / 3.5 | 85,9% / 67,0% / 45,3% | 1.16 / 1.49 / 2.21 | średnia |
| BTTS tak / nie | 56,3% / 43,7% | 1.78 / 2.29 | niska |
| Rożne (Pinn. linia 9.5, średnia 9,6; PSG ok. 6,6) Over 8.5 / 9.5 / 10.5 | 59,9% / 48,2% / 37,2% | 1.67 / 2.07 / 2.69 | niska |
| Kartki (szkic 4,3) Over 3.5 / 4.5 | 58,8% / 42,0% | 1.70 / 2.38 | bardzo niska |
| Faule (szkic 22,5) Over 21.5 | 56,2% | 1.78 | bardzo niska |

**Statystyki:** PSG 5-2-1, 16:9 (2,0 gola/mecz), forma DWWWW; Le Havre 0-2-6, 8:15, DLLLD, najlepszy strzelec Maja 3 gole (ESPN).
**H2H:** nie sprawdzano (poza oknem danych); PSG wygrywało komplet ostatnich spotkań z Le Havre w ostatnich sezonach (niepotwierdzone w tej sesji).
**Kontuzje/skład:** brak aktualnych danych o PSG i Le Havre. **Ryzyka:** (1) rotacja PSG po Lidze Mistrzów, (2) remis 16,6% i wygrana underdoga 12,3% to podobnej wagi scenariusze, (3) Le Havre w desperacji (reguła underdoga w kryzysie).
**Rynek:** Pinnacle PSG ok. 1.30 (-336), total 3.5 po ok. 1.98 (O) / 1.85 (U), O2.5 ok. 1.38; DK PSG -340, total 3.5. Fair rynku PSG 1.36.

### Nice - Rennes (Ligue 1, 30.10, 19:00, Allianz Riviera)
**Typ:** brak mocnego typu wynikowego; najlepszy rynek BTTS tak | **p:** 63% | **Fair:** 1.59 | **Pewność:** niska-średnia.
**λ:** 1,55 / 1,60 (rynek: Nice 37,0%, X 25,4%, Rennes 37,7%, O2.5 61,8%).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 37,1% / 23,6% / 39,3% | 2.69 / 4.23 / 2.55 | niska |
| 1X / X2 / 12 | 60,7% / 62,9% / 76,4% | 1.65 / 1.59 / 1.31 | niska |
| Over 1.5 / 2.5 / 3.5 | 82,2% / 61,0% / 38,6% | 1.22 / 1.64 / 2.59 | średnia |
| BTTS tak / nie | 62,9% / 37,1% | 1.59 / 2.70 | średnia |
| Rożne (Pinn. 10.0, średnia 9,9) Over 9.5 / 10.5 | 51,7% / 40,5% | 1.93 / 2.47 | niska |
| Kartki (szkic 4,3) O3.5 / O4.5 | 58,8% / 42,0% | 1.70 / 2.38 | bardzo niska |
| Faule (szkic 22,5) O21.5 | 56,2% | 1.78 | bardzo niska |

**Statystyki:** Nice 3-2-3, 8:10, DLWWL; Rennes 5-1-2 (2. w tabeli), 18:14, najlepszy strzelec Lepaul 7 goli; Rennes gra otwarto (14 straconych w 8).
**H2H:** nie sprawdzano. **Kontuzje/skład:** brak danych. **Ryzyka:** wyrównany mecz, remis 23,6% (Pinnacle HT: remis najbardziej prawdopodobny po 45'). **Rynek:** Pinnacle 2.62 / 3.82 / 2.57 (1/X/2), total 3.0 po 1.89/2.00.

### Villarreal - Espanyol (LaLiga, 30.10, 21:00, Estadio de la Cerámica)
**Typ:** Villarreal wygra | **p:** 66,7% | **Fair:** 1.50 | **Pewność:** średnia (brak danych kadrowych).
**λ:** 2,25 / 0,95. Rynek bez marży: Villarreal 68,4%; skorygowano -1,7 pp za kryzys underdoga (Espanyol 18., 2-2-6, 8 pkt, DLLDL).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 66,7% / 18,7% / 14,6% | 1.50 / 5.34 / 6.87 | średnia |
| 1X / X2 / 12 | 85,4% / 33,3% / 81,3% | 1.17 / 3.00 / 1.23 | średnia (1X graniczne 1.15-1.20) |
| Over 1.5 / 2.5 / 3.5 | 82,9% / 62,0% / 39,7% | 1.21 / 1.61 / 2.52 | średnia |
| BTTS tak / nie | 54,9% / 45,1% | 1.82 / 2.22 | niska |
| Rożne (Pinn. 10.0, średnia 9,9; Villarreal ok. 6,5) O9.5 / O10.5 | 51,7% / 40,5% | 1.93 / 2.47 | niska |
| Kartki (szkic 5,3) O4.5 / O5.5 | 57,9% / 42,8% | 1.73 / 2.34 | bardzo niska |
| Faule (szkic 24,0) O23.5 | 52,2% | 1.92 | bardzo niska |

**Statystyki:** Villarreal 3-3-4 (10. m.), 15:14, DWLDW, najlepszy strzelec Pape Gueye 3; Espanyol 2-2-6, 12:14, najlepszy strzelec R. Fernández 6.
**H2H:** nie sprawdzano. **Kontuzje:** brak danych. **Ryzyka:** remis 18,7%, wygrana Espanyolu 14,6% (desperacja, 2 gole w ostatnich 3 wyjazdach niepotwierdzone); Villarreal traci średnio 1,4 gola, więc pewniak odpada.
**Rynek:** Pinnacle 1.41 / 5.28 / 7.20 (1/X/2), total 3.25 po 2.02/1.87, O2.5 ok. 1.49; DK Villarreal -240, total 3.5.

### Lille - Lens (Ligue 1, 30.10, 21:05, Decathlon Arena)
**Typ:** brak mocnego typu; najlepszy rynek Under 3.5 | **p:** 72,5% | **Fair:** 1.38 | **Pewność:** średnia.
**λ:** 1,30 / 1,35 (rynek: Lille 34,1%, X 28,6%, Lens 37,3%, total 2.5 dokładnie 50/50).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 35,8% / 26,1% / 38,1% | 2.79 / 3.83 / 2.62 | niska |
| 1X / X2 / 12 | 61,9% / 64,2% / 73,9% | 1.62 / 1.56 / 1.35 | niska |
| Over 1.5 / 2.5 / 3.5 | 74,2% / 49,4% / 27,5% | 1.35 / 2.02 / 3.64 | średnia |
| Under 2.5 / 3.5 | 50,6% / 72,5% | 1.98 / 1.38 | średnia (U3.5) |
| BTTS tak / nie | 53,9% / 46,1% | 1.86 / 2.17 | niska |
| Rożne (Pinn. 9.0, średnia 9,2) O8.5 / O9.5 | 55,3% / 43,6% | 1.81 / 2.30 | niska |
| Kartki (szkic 4,3) O3.5 / O4.5 | 58,8% / 42,0% | 1.70 / 2.38 | bardzo niska |
| Faule (szkic 22,5) O21.5 | 56,2% | 1.78 | bardzo niska |

**Statystyki:** Lille 4-3-1 (3. m.), 11:6 (najlepsza obrona z czołówki), DLDLW, Ethan Mbappé 2 gole; Lens 4-1-3 (7. m.), 16:12, DLWLW, Thauvin 4 gole.
**H2H:** nie sprawdzano. **Kontuzje:** brak danych. **Ryzyka:** mecz bez faworyta (remis 26%); wynik 1-1 najbardziej prawdopodobny (12,4%). **Rynek:** Pinnacle 2.84 / 3.38 / 2.59, total 2.5 po 1.93/1.96.

---

# 31.10 (sobota): Premier League

Statusy zdrowia (FPL, 30.10): Chelsea: João Pedro (udo) out, Martinez (głowa) out, Lacroix 50%, Hato 75%; Man United: Shaw out, Mainoo 25%, Rashford 75%; Bournemouth: Scott out do 8.11; Brentford: Yarmoliuk zawieszony do 8.11; Brighton: Kadıoğlu 75%, Andrés 75%; Man City: Semenyo (kolano) out, Matheus N. 75%; Spurs: Sávio out do 21.11, Bentancur zawieszony do 7.11; Palace: Strand Larsen 75%, Timber 75%; Coventry: Amenda out, Thomas 50%; Sunderland: Ballard out, Mukiele 75%; Forest: Ndoye 50%; Leeds: Stach 50%; Ipswich: Lukić out; Fulham: Affengruber 75%; Aston Villa i Hull: brak istotnych wpisów w FPL (graczy z >300 minut).

### Chelsea - Man United (PL, 31.10, 13:30, Stamford Bridge)
**Typ:** Over 1.5 gola | **p:** 80,1% | **Fair:** 1.25 | **Pewność:** średnia. Wynik: Chelsea wygra 51,4% (fair 1.94), brak mocnego typu.
**λ:** 1,80 / 1,20 (rynek: Chelsea 52,5%, X 24,1%, MU 23,4%; brak odjęcia za absencje João Pedro/Martinez, bo to jedna strona boiska i <3 pp).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 51,4% / 23,1% / 25,4% | 1.94 / 4.32 / 3.93 | niska |
| 1X / X2 / 12 | 74,5% / 48,5% / 76,8% | 1.34 / 2.06 / 1.30 | średnia |
| Over 1.5 / 2.5 / 3.5 | 80,1% / 57,7% / 35,3% | 1.25 / 1.73 / 2.83 | średnia |
| BTTS tak / nie | 58,3% / 41,7% | 1.71 / 2.40 | niska |
| Rożne (Pinn. 10.0, średnia 10,3) O9.5 / O10.5 | 56,2% / 45,0% | 1.78 / 2.22 | niska |
| Kartki (szkic 4,0) O3.5 / O4.5 | 53,8% / 37,0% | 1.86 / 2.70 | bardzo niska |
| Faule (szkic 21,5) O20.5 | 56,3% | 1.78 | bardzo niska |

**Statystyki:** Chelsea 4-1-3 (5. m.), 17:15, DLWWL; MU 1-4-3 (16. m.), 10:13, DLDLD (tylko 1,25 gola/mecz). **H2H:** nie sprawdzano. **Ryzyka:** wygrana MU (underdog w kryzysie, ale nie w rozpadzie) 25%, remis 23%. **Rynek:** Pinnacle 1.84 / 4.01 / 4.14, total 3.0 po 2.01/1.88 (O2.5 ok. 1.63).

### Bournemouth - Leeds (PL, 31.10, 16:00, Vitality)
**Typ:** Under 3.5 gola | **p:** 72,5% | **Fair:** 1.38 | **Pewność:** średnia. Wynik: 1X 70,9% (fair 1.41).
**λ:** 1,50 / 1,15 (rynek: Bournemouth 44,0%, X 28,4%, Leeds 27,6%).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 45,3% / 25,6% / 29,1% | 2.21 / 3.90 / 3.44 | niska |
| 1X / X2 / 12 | 70,9% / 54,7% / 74,4% | 1.41 / 1.83 / 1.34 | średnia |
| Over 1.5 / 2.5 / 3.5 | 74,2% / 49,4% / 27,5% | 1.35 / 2.02 / 3.64 | średnia |
| Under 2.5 / 3.5 | 50,6% / 72,5% | 1.98 / 1.38 | średnia |
| BTTS tak / nie | 53,1% / 46,9% | 1.88 / 2.13 | niska |
| Rożne (Pinn. 9.5, średnia 9,55) O8.5 / O9.5 / O10.5 | 59,4% / 47,7% / 36,6% | 1.68 / 2.10 / 2.73 | niska |
| Kartki (szkic 4,0) O3.5 | 53,8% | 1.86 | bardzo niska |
| Faule (szkic 21,5) O20.5 | 56,3% | 1.78 | bardzo niska |

**Statystyki:** Bournemouth 2-3-3, 12:13, forma DWWWW; Leeds 2-5-1 (5 remisów), 9:6 (najlepsza obrona z tej pary), DDLDW. **Absencje:** Scott (Bournemouth) out. **Ryzyka:** remis 25,6% (Leeds remisują często), wygrana Leeds 29%. **Rynek:** Pinnacle 2.20 / 3.41 / 3.50, total 2.5 po 1.93/1.96.

### Brentford - Nottingham Forest (PL, 31.10, 16:00, Gtech)
**Typ:** Over 1.5 gola | **p:** 77,7% | **Fair:** 1.29 | **Pewność:** średnia. Wynik: Brentford 1X 70,1% (fair 1.43).
**λ:** 1,60 / 1,25 (rynek: Brentford 45,9%, X 25,8%, Forest 28,3%).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 45,5% / 24,6% / 29,9% | 2.20 / 4.07 / 3.35 | niska |
| 1X / X2 / 12 | 70,1% / 54,5% / 75,4% | 1.43 / 1.83 / 1.33 | średnia |
| Over 1.5 / 2.5 / 3.5 | 77,7% / 54,2% / 31,9% | 1.29 / 1.84 / 3.13 | średnia |
| BTTS tak / nie | 56,9% / 43,1% | 1.76 / 2.32 | niska |
| Rożne (Pinn. 10.0, średnia 10,05) O9.5 / O10.5 | 53,4% / 42,2% | 1.87 / 2.37 | niska |
| Kartki (szkic 4,0) O3.5 | 53,8% | 1.86 | bardzo niska |
| Faule (szkic 21,5) O20.5 | 56,3% | 1.78 | bardzo niska |

**Statystyki:** Brentford 2-5-1 (6. m.), 14:9, DDLDW; Forest 1-3-4 (18. m.), 6:10, DLLLW (najsłabszy atak ligi, 0,75 gola/mecz). **Absencje:** Yarmoliuk (Brentford) zawieszony; Ndoye (Forest) 50%. **Ryzyka:** Brentford remisuje (5 remisów w 8), underdog Forest w kryzysie (1 wygrana) = desperacja, więc nie podnosiłem p gospodarzy. **Rynek:** Pinnacle 2.11 / 3.75 / 3.42, total 2.75 po 1.98/1.91.

### Coventry - Sunderland (PL, 31.10, 16:00, Coventry Building Society Arena)
**Typ:** brak mocnego typu wynikowego; najlepszy rynek Under 3.5 | **p:** 75,8% | **Fair:** 1.32 | **Pewność:** średnia.
**λ:** 1,15 / 1,35 (rynek: Coventry 30,4%, X 28,6%, Sunderland 41,0%; Under 2.5 skorygowane tylko +2 pp, bo obie defensywy tracą ok. 1,8 gola/mecz).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 31,8% / 26,8% / 41,3% | 3.14 / 3.73 / 2.42 | niska |
| 1X / X2 / 12 | 58,6% / 68,1% / 73,2% | 1.71 / 1.47 / 1.37 | niska-średnia |
| Over 1.5 / 2.5 / 3.5 | 71,3% / 45,6% / 24,2% | 1.40 / 2.19 / 4.13 | średnia |
| Under 2.5 / 3.5 | 54,4% / 75,8% | 1.84 / 1.32 | niska / średnia |
| BTTS tak / nie | 50,6% / 49,4% | 1.98 / 2.03 | niska |
| Rożne (Pinn. 9.0, średnia 8,95) O8.5 / O9.5 | 52,4% / 40,6% | 1.91 / 2.46 | niska |
| Kartki (szkic 4,0) O3.5 | 53,8% | 1.86 | bardzo niska |
| Faule (szkic 21,5) O20.5 | 56,3% | 1.78 | bardzo niska |

**Statystyki:** Coventry 2-0-6 (19. m.), 6:15, DLWWL; Sunderland 1-2-5 (20. m.), 6:14, DDDLW. Obie drużyny z dołu tabeli i bez bramek. **Absencje:** Coventry: Amenda out, Thomas 50%; Sunderland: Ballard out, Mukiele 75%. **Ryzyka:** remis 26,8%; faworyzowany Sunderland (1 wygrana w 8) to słaby faworyt, p 41% to nie typ. **Rynek:** Pinnacle 3.18 / 3.39 / 2.36, total 2.5 po 2.03/1.86.

### Hull - Ipswich (PL, 31.10, 16:00, MKM Stadium)
**Typ:** brak mocnego typu; najlepszy rynek Over 1.5 | **p:** 75,1% | **Fair:** 1.33 | **Pewność:** średnia.
**λ:** 1,35 / 1,35 (rynek: Hull 35,9%, X 28,3%, Ipswich 35,8%).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 37,1% / 25,8% / 37,1% | 2.70 / 3.87 / 2.70 | niska |
| 1X / X2 / 12 | 62,9% / 62,9% / 74,2% | 1.59 / 1.59 / 1.35 | niska |
| Over 1.5 / 2.5 / 3.5 | 75,1% / 50,6% / 28,6% | 1.33 / 1.97 / 3.50 | średnia |
| BTTS tak / nie | 54,9% / 45,1% | 1.82 / 2.22 | niska |
| Rożne (Pinn. 9.5, średnia 9,45) O8.5 / O9.5 / O10.5 | 58,2% / 46,5% / 35,5% | 1.72 / 2.15 / 2.82 | niska |
| Kartki (szkic 4,0) O3.5 | 53,8% | 1.86 | bardzo niska |
| Faule (szkic 21,5) O20.5 | 56,3% | 1.78 | bardzo niska |

**Statystyki:** Hull 2-4-2 (10. m.), 9:8, DLDLD; Ipswich 3-1-4 (12. m.), 12:16, DLWLL. **Absencje:** Ipswich: Lukić (pomocnik) out. **Ryzyka:** 3-way równy, remis 25,8%. **Rynek:** Pinnacle 2.69 / 3.41 / 2.72, total 2.5 po 1.89/1.99.

### Man City - Brighton (PL, 31.10, 16:00, Etihad)
**Typ:** Over 2.5 gola | **p:** 67,9% | **Fair:** 1.47 | **Pewność:** średnia. Wynik: City 57,8% (fair 1.73), 1X 78,0% (fair 1.28).
**λ:** 2,20 / 1,30 (rynek DK: City 58,9%, X 20,8%, Brighton 20,3%, total 3.5 po ok. 47% Over).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 57,8% / 20,2% / 22,0% | 1.73 / 4.95 / 4.55 | średnia |
| 1X / X2 / 12 | 78,0% / 42,2% / 79,8% | 1.28 / 2.37 / 1.25 | średnia |
| Over 1.5 / 2.5 / 3.5 | 86,4% / 67,9% / 46,3% | 1.16 / 1.47 / 2.16 | średnia (O1.5 graniczne) |
| BTTS tak / nie | 64,7% / 35,3% | 1.55 / 2.83 | średnia |
| Rożne (brak linii, szkic 10,2; City dominuje) O9.5 / O10.5 | 55,1% / 43,9% | 1.82 / 2.28 | bardzo niska |
| Kartki (szkic 4,0) O3.5 | 53,8% | 1.86 | bardzo niska |
| Faule (szkic 21,5) O20.5 | 56,3% | 1.78 | bardzo niska |

**Statystyki:** City 7-0-1 (1. m.), 20:9, DLWWL; Brighton 5-1-2 (3. m.), strzelili 23 gole w 8 meczach (najlepszy atak), stracili 7, DLDWW. **Absencje:** City: Semenyo out, Matheus N. 75%; Brighton: Kadıoğlu i Andrés 75%. **Ryzyka:** Brighton w świetnej formie, więc nie jest "underdogiem w kryzysie"; wygrana gości 22%, remis 20%. **Rynek:** DK -160 / +360 / +370, total 3.5 po +100/-125 (Pinnacle nie pobierany dla tego meczu, id 1638676646).

### Tottenham - Crystal Palace (PL, 31.10, 18:30, Tottenham Hotspur Stadium)
**Typ:** Tottenham wygra | **p:** 60,6% | **Fair:** 1.65 | **Pewność:** średnia-niska. Alternatywa 1X 81,8% (fair 1.22).
**λ:** 2,00 / 1,00 (rynek DK: Spurs 61,4%, X 21,2%, Palace 17,4%). Palace 17. m., 5 porażek, DLDLL: underdog w kryzysie (bez dodatkowych korekt, bo p Spurs już równe rynkowi -1 pp).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 60,6% / 21,2% / 18,3% | 1.65 / 4.72 / 5.48 | średnia |
| 1X / X2 / 12 | 81,8% / 39,4% / 78,8% | 1.22 / 2.54 / 1.27 | średnia |
| Over 1.5 / 2.5 / 3.5 | 80,1% / 57,7% / 35,3% | 1.25 / 1.73 / 2.83 | średnia |
| BTTS tak / nie | 54,7% / 45,3% | 1.83 / 2.19 | niska |
| Rożne (brak linii, szkic 10,3) O9.5 / O10.5 | 56,2% / 45,0% | 1.78 / 2.22 | bardzo niska |
| Kartki (szkic 4,0) O3.5 | 53,8% | 1.86 | bardzo niska |
| Faule (szkic 21,5) O20.5 | 56,3% | 1.78 | bardzo niska |

**Statystyki:** Spurs 2-3-3 (14. m.), 8:10, WWDLL (gorsza forma wyjazdowa nieistotna); Palace 2-1-5 (17. m.), 9:19 (najgorsza obrona ligi, 2,4 gola/mecz). **Absencje:** Spurs: Sávio out, Bentancur zawieszony (osłabiony środek pola); Palace: Strand Larsen 75%, Timber 75%. **Ryzyka:** Spurs strzelili tylko 8 goli w 8 meczach, więc 2,0 λ to szacunek rynku; remis 21%, wygrana Palace 18%. **Rynek:** DK -180 / +350 / +450, O2.5 -170.

### Aston Villa - Fulham (PL, 31.10, 21:00, Villa Park)
**Typ:** Over 1.5 gola | **p:** 79,3% | **Fair:** 1.26 | **Pewność:** średnia. Wynik: Villa 1X 73,8% (fair 1.36).
**λ:** 1,75 / 1,20 (rynek DK: Villa 48,8% bez marży, X 25,4%, Fulham 25,8%).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 50,3% / 23,5% / 26,2% | 1.99 / 4.25 / 3.82 | niska |
| 1X / X2 / 12 | 73,8% / 49,7% / 76,5% | 1.36 / 2.01 / 1.31 | średnia |
| Over 1.5 / 2.5 / 3.5 | 79,3% / 56,6% / 34,2% | 1.26 / 1.77 / 2.93 | średnia |
| BTTS tak / nie | 57,7% / 42,3% | 1.73 / 2.36 | niska |
| Rożne (brak linii, szkic 10,0) O9.5 / O10.5 | 52,8% / 41,6% | 1.89 / 2.40 | bardzo niska |
| Kartki (szkic 4,0) O3.5 | 53,8% | 1.86 | bardzo niska |
| Faule (szkic 21,5) O20.5 | 56,3% | 1.78 | bardzo niska |

**Statystyki:** Villa 3-2-3 (9. m.), 9:12, forma DWWWW; Fulham 2-2-4 (15. m.), 8:10, DWWLD. **Absencje:** Fulham: Affengruber 75%; Villa: brak wpisów w FPL (Onana długoterminowo poza grą wg niepotwierdzonego źródła). **Ryzyka:** wyrównane, wygrana Fulhamu 26%, remis 23,5%. **Rynek:** DK -105 / +275 / +270, O2.5 -150.

---

# 31.10 (sobota): LaLiga i Ligue 1

### Levante - Atlético Madryt (LaLiga, 31.10, 14:00, Ciutat de València)
**Typ:** Atlético wygra lub remis (X2) | **p:** 80,7% | **Fair:** 1.24 | **Pewność:** średnia. Wygrana Atlético 59,4% (fair 1.68).
**λ:** 1,05 / 2,00 (rynek DK: Levante 18,2%, X 19,9%, Atlético 61,9%; skorygowano -2,5 pp na Atlético: 2,0 gola/mecz to jego średnia, DDWWW to wynik bez porażki od 3 kolejek).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 19,3% / 21,3% / 59,4% | 5.18 / 4.70 / 1.68 | średnia |
| 1X / X2 / 12 | 40,6% / 80,7% / 78,7% | 2.46 / 1.24 / 1.27 | średnia |
| Over 1.5 / 2.5 / 3.5 | 80,8% / 58,8% / 36,4% | 1.24 / 1.70 / 2.75 | średnia |
| BTTS tak / nie | 56,2% / 43,8% | 1.78 / 2.28 | niska |
| Rożne (brak linii, szkic 9,8) O9.5 / O10.5 | 50,6% / 39,4% | 1.98 / 2.54 | bardzo niska |
| Kartki (szkic 5,3) O4.5 / O5.5 | 57,9% / 42,8% | 1.73 / 2.34 | bardzo niska |
| Faule (szkic 24,0) O23.5 | 52,2% | 1.92 | bardzo niska |

**Statystyki:** Levante 2-4-4 (14. m.), 16:19 (średnio 3,5 gola w meczach), DWDDL; Atlético 8-1-1 (2. m.), 20:8, DDWWW. **Kontuzje:** brak danych o obu klubach. **Ryzyka:** wygrana Levante 19% (gospodarze są w środku tabeli, ale gra u siebie), remis 21%; mecz zaczyna się o 14:00 (wczesna pora). **Rynek:** DK +425 / +380 / -185, total 3.5 po +135/-170 (linia wyższa niż moja; mój Over 3.5 36% vs rynek 40%). Pinnacle: id 1638653668, nie pobierano.

### Rayo Vallecano - Celta Vigo (LaLiga, 31.10, 16:15, Campo de Fútbol de Vallecas)
**Typ:** brak mocnego typu; najlepszy rynek Under 3.5 | **p:** 76,8% | **Fair:** 1.30 | **Pewność:** średnia-niska.
**λ:** 1,30 / 1,15 (rynek DK: Rayo 39,8%, X 28,9%, Celta 31,3%; Over 2.5 tylko 44%).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 40,0% / 27,2% / 32,8% | 2.50 / 3.67 / 3.05 | niska |
| 1X / X2 / 12 | 67,2% / 60,0% / 72,8% | 1.49 / 1.67 / 1.37 | niska |
| Over 1.5 / 2.5 / 3.5 | 70,2% / 44,3% / 23,2% | 1.42 / 2.26 / 4.31 | średnia |
| Under 2.5 / 3.5 | 55,7% / 76,8% | 1.80 / 1.30 | średnia |
| BTTS tak / nie | 49,7% / 50,3% | 2.01 / 1.99 | niska |
| Rożne (brak linii, szkic 9,6) O8.5 / O9.5 / O10.5 | 59,9% / 48,2% / 37,2% | 1.67 / 2.07 / 2.69 | bardzo niska |
| Kartki (szkic 5,3) O4.5 / O5.5 | 57,9% / 42,8% | 1.73 / 2.34 | bardzo niska |
| Faule (szkic 24,0) O23.5 | 52,2% | 1.92 | bardzo niska |

**Statystyki:** Rayo 2-3-4 (16. m.), 12:20, DLDDW; Celta 2-6-2 (9. m., 6 remisów w 10), 10:7 (druga najlepsza obrona LaLiga), DWWLD. **Kontuzje:** brak danych. **Ryzyka:** remis 27% (Celta remisuje najczęściej w lidze), mecz zamknięty. **Rynek:** DK +140 / +230 / +205, O2.5 +115.

### Real Betis - Málaga (LaLiga, 31.10, 18:30, Benito Villamarín)
**Typ:** Betis wygra | **p:** 70,0% | **Fair:** 1.43 | **Pewność:** średnia.
**λ:** 2,30 / 0,85 (rynek DK: Betis 70,8%, X 17,3%, Málaga 11,9%; total 3.5 DK o 42% Over, moje 38,6%, bo Betis 1,6 gola/mecz, Málaga traci 1,9, więc oczekuję ok. 3,1 gola).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 70,0% / 17,8% / 12,3% | 1.43 / 5.63 / 8.15 | średnia |
| 1X / X2 / 12 | 87,8% / 30,1% / 82,3% | 1.14 / 3.32 / 1.22 | średnia (1X poniżej progu 1.15) |
| Over 1.5 / 2.5 / 3.5 | 82,2% / 61,0% / 38,6% | 1.22 / 1.64 / 2.59 | średnia |
| Under 3.5 | 61,4% | 1.63 | niska |
| BTTS tak / nie | 51,5% / 48,5% | 1.94 / 2.06 | niska |
| Rożne (brak linii, szkic 10,0) O9.5 / O10.5 | 52,8% / 41,6% | 1.89 / 2.40 | bardzo niska |
| Kartki (szkic 5,3) O4.5 / O5.5 | 57,9% / 42,8% | 1.73 / 2.34 | bardzo niska |
| Faule (szkic 24,0) O23.5 | 52,2% | 1.92 | bardzo niska |

**Statystyki:** Betis 6-2-2 (4. m.), 16:14, DWLWW; Málaga 0-5-5 (20. m., zero wygranych), 7:19, DDLDL. **Kontuzje:** brak danych. **Ryzyka:** Málaga to underdog w kryzysie (desperacja), więc nie zawyżałem p Betisu powyżej rynku; remis 17,8% i wygrana Málagi 12,3% to podobnej wagi scenariusze; Betis zdobywa mało (1,6/mecz). **Rynek:** DK -290 / +450 / +700.

### FC Barcelona - Alavés (LaLiga, 31.10, 21:00, Spotify Camp Nou)
**Typ:** Barcelona -1.5 (handicap) lub Over 2.5 | **p:** 68,9% (Barcelona wygra różnicą 2+) / 76,9% (O2.5) | **Fair:** 1.45 / 1.30 | **Pewność:** średnia. Wygrana Barcelony 85,4% (fair 1.17, graniczne 1.15-1.20).
**λ:** 3,30 / 0,75 (rynek DK: Barcelona 86,6% bez marży, total 4.5 po +130/-160 = Over 41%; moje O4.5 38%).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 85,4% / 9,6% / 5,1% | 1.17 / 10.4 / 19.8 | średnia (remis niedoszacowany) |
| 1X / X2 / 12 | 95,0% / 14,6% / 90,4% | 1.05 / 6.85 / 1.11 | średnia (poniżej progu 1.15) |
| Barcelona -1.5 | 68,9% | 1.45 | średnia |
| Over 1.5 / 2.5 / 3.5 / 4.5 | 91,2% / 76,9% / 57,6% / 38,1% | 1.10 / 1.30 / 1.74 / 2.62 | średnia |
| BTTS tak / nie | 50,8% / 49,2% | 1.97 / 2.03 | niska |
| Rożne (brak linii, szkic 11,0) O10.5 / O11.5 | 52,7% / 42,0% | 1.90 / 2.38 | bardzo niska |
| Kartki (szkic 5,3) O4.5 / O5.5 | 57,9% / 42,8% | 1.73 / 2.34 | bardzo niska |
| Faule (szkic 24,0) O23.5 | 52,2% | 1.92 | bardzo niska |

**Statystyki:** Barcelona 9-0-1 (1. m.), 40:11 (4 gole/mecz), DLWWW; Alavés 3-3-4 (7. m.), 14:11, DLLDL. **Kontuzje:** brak danych. **Ryzyka:** Alavés broni się nisko (tylko 11 straconych w 10) i dużo remisuje (3), więc handicap -1.5 i O2.5 obarczone wynikiem 1-0/2-1; rotacja Barcelony przy mocnym składzie tygodniowym niepotwierdzona. **Rynek:** DK -1000 / +1000 / +1900.

### Troyes - Le Mans (Ligue 1, 31.10, 20:45, Stade de l'Aube)
**Typ:** brak mocnego typu; najlepszy rynek Under 3.5 | **p:** 71,4% | **Fair:** 1.40 | **Pewność:** niska-średnia.
**λ:** 1,40 / 1,30 (rynek DK: Troyes 40,5%, X 27,2%, Le Mans 32,3%, total 2.5 po -125/-105). Uwaga: Troyes zdobył tylko 5 goli w 8 meczach (0,6/mecz), więc λ gospodarzy opiera się na rynku (nie obniżano pod rynek bez konkretów).

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| 1 / X / 2 | 39,4% / 25,8% / 34,8% | 2.54 / 3.88 / 2.87 | niska |
| 1X / X2 / 12 | 65,2% / 60,6% / 74,2% | 1.53 / 1.65 / 1.35 | niska |
| Over 1.5 / 2.5 / 3.5 | 75,1% / 50,6% / 28,6% | 1.33 / 1.97 / 3.50 | średnia |
| Under 3.5 | 71,4% | 1.40 | niska-średnia |
| BTTS tak / nie | 54,8% / 45,2% | 1.82 / 2.21 | niska |
| Rożne (brak linii, szkic 9,8) O9.5 / O10.5 | 50,6% / 39,4% | 1.98 / 2.54 | bardzo niska |
| Kartki (szkic 4,3) O3.5 / O4.5 | 58,8% / 42,0% | 1.70 / 2.38 | bardzo niska |
| Faule (szkic 22,5) O21.5 | 56,2% | 1.78 | bardzo niska |

**Statystyki:** Troyes 1-2-5 (17. m.), 5:16, DLLLL (pięć meczów bez wygranej); Le Mans 1-4-3 (15. m.), 11:16, DLLWD, Mafouta 4 gole. **H2H:** brak danych (beniaminkowie, wcześniej Ligue 2). **Kontuzje:** brak danych. **Ryzyka:** oba zespoły z dołu, mało danych, remis 25,8%; mecz o 20:45 (wieczór, po ligach PL). **Rynek:** DK +135 / +250 / +195, O2.5 -125 (Pinnacle: id 1638694279, nie pobierano).

---

# Ranking najlepszych rynków (fair odds > 1.15, wszystkie rynki)

Pewność: Ś = średnia, N = niska. Brak typów zawodnika, kartek i fauli (brak sędziów/składów). Rożne tylko tam, gdzie jest linia Pinnacle; bez typów "wysoka pewność" (brak potwierdzonych składów i sędziów).

| # | Mecz | Rynek | p | Fair | Pewność | Uwagi |
|---|---|---|---|---|---|---|
| 1 | Betis - Málaga | Betis wygra | 70,0% | 1.43 | Ś | rynek 70,8% |
| 2 | Le Havre - PSG | PSG wygra | 71,1% | 1.41 | Ś | rotacja po LM, ryzyko |
| 3 | Villarreal - Espanyol | Villarreal wygra | 66,7% | 1.50 | Ś | |
| 4 | Barcelona - Alavés | Barcelona -1.5 | 68,9% | 1.45 | Ś | |
| 5 | Barcelona - Alavés | Over 2.5 gola | 76,9% | 1.30 | Ś | |
| 6 | Man City - Brighton | Over 2.5 gola | 67,9% | 1.47 | Ś | |
| 7 | Le Havre - PSG | Over 2.5 gola | 67,0% | 1.49 | Ś | |
| 8 | Levante - Atlético | X2 (Atlético lub remis) | 80,7% | 1.24 | Ś | |
| 9 | Tottenham - Palace | Tottenham wygra | 60,6% | 1.65 | Ś-N | |
| 10 | Man City - Brighton | BTTS tak | 64,7% | 1.55 | Ś | |
| 11 | Rayo - Celta | Under 3.5 | 76,8% | 1.30 | Ś-N | |
| 12 | Coventry - Sunderland | Under 3.5 | 75,8% | 1.32 | Ś | |
| 13 | Bournemouth - Leeds | Under 3.5 | 72,5% | 1.38 | Ś | |
| 14 | Lille - Lens | Under 3.5 | 72,5% | 1.38 | Ś | |
| 15 | Brentford - Forest | Over 1.5 | 77,7% | 1.29 | Ś | |
| 16 | Aston Villa - Fulham | Over 1.5 | 79,3% | 1.26 | Ś | |
| 17 | Chelsea - Man United | Over 1.5 | 80,1% | 1.25 | Ś | |
| 18 | Nice - Rennes | BTTS tak | 62,9% | 1.59 | Ś | |
| 19 | Troyes - Le Mans | Under 3.5 | 71,4% | 1.40 | N-Ś | |
| 20 | Le Havre - PSG | Rożne Over 8.5 (Pinn. 9.5) | 59,9% | 1.67 | N | |

Graniczne 1.15-1.20: Barcelona wygra 85,4% (1.17), Villarreal 1X 85,4% (1.17), Le Havre - PSG Over 1.5 (1.16), Man City Over 1.5 (1.16). Pominięte (fair <= 1.15): Barcelona 1X/12/O1.5, Betis 1X, PSG X2.

## Tabela kandydatów na kupon (wejście dla bet-slip-buildera)

| Mecz | Rynek | p | Fair | Pewność | Zależy od | Kurs rynkowy |
|---|---|---|---|---|---|---|
| Betis - Málaga | 1 | 70,0% | 1.43 | Ś | składy Betisu | DK -290 (1.34) |
| Le Havre - PSG | 2 | 71,1% | 1.41 | Ś | rotacja PSG | Pinnacle 1.30 |
| Villarreal - Espanyol | 1 | 66,7% | 1.50 | Ś | składy | Pinnacle 1.41 |
| Barcelona - Alavés | -1.5 / O2.5 | 68,9% / 76,9% | 1.45 / 1.30 | Ś | rotacja Barcelony | DK: 1 -1000 (1.10); handicap nieznany |
| Man City - Brighton | O2.5 / BTTS | 67,9% / 64,7% | 1.47 / 1.55 | Ś | Semenyo out, Matheus N. 75% | DK total 3.5 +100/-125 |
| Levante - Atlético | X2 | 80,7% | 1.24 | Ś | składy | DK X2 nieznany; 2 -185 |
| Tottenham - Palace | 1 | 60,6% | 1.65 | Ś-N | Sávio/Bentancur out | DK -180 (1.56) |
| Bournemouth - Leeds | U3.5 | 72,5% | 1.38 | Ś | Scott out | Pinnacle alt: nie pobierano |
| Coventry - Sunderland | U3.5 | 75,8% | 1.32 | Ś | Thomas 50% | Pinnacle alt: nie pobierano |
| Rayo - Celta | U3.5 | 76,8% | 1.30 | Ś-N | składy | brak |

W żadnym z 17 meczów nie ma rynku o pewności "wysoka". Wszystkie liczby to oszacowania probabilistyczne, nie gwarancje.
