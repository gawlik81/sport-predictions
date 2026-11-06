# Analiza NBA + NHL, noc 05→06.11.2026 (czas PL, CET)

Skille: `nba-analyst`, `nhl-analyst` (subagenty). Źródła: NHL API, ESPN, nba_stats, Pinnacle/theoddsapi/FanDuel (tylko jako odniesienie rynku, nie Betclic), Daily Faceoff (bramkarze). Brak xG/CF%/GSAx (MoneyPuck, Natural Stat Trick niedostępne), BettingPros pominięty (brak klucza). Rynki zawodnika: jedno źródło liczb, pewność niska, domyślnie poza kuponami. Skład i bramkarze mogą zmienić się do startu.

Uwaga: VAN@WPG startuje 01:00 PL (00:00 UTC), nie 02:00.

## NBA

### 03:00 Orlando Magic @ Phoenix Suns (US 05.11, 21:00 ET)
Model: PHX 111.0 – ORL 109.5. PHX 1-5, B2B (wczoraj POR), net -10.3; ORL 2-5, bez Banchero, Suggsa, Isaaca, Pendy, Nelsona. PHX bez M. Williamsa, Goodwina, Fleminga; Booker niepotwierdzony (górna część ciała).
Rynek (odniesienie): PHX -1.5, total 221.5, ML ok. 50/50.
| Rynek | p | fair | pewność |
|---|---|---|---|
| PHX ML | 53,2% | 1.88 | niska |
| ORL ML | 46,8% | 2.14 | niska |
| ORL +4.5 | 59,5% | 1.68 | niska |
| ORL +2.5 | 53,2% | 1.88 | niska |
| Under 221.5 | 52,2% | 1.92 | niska |
| Under 225.5 | 60,7% | 1.65 | niska-średnia |
| Over 219.5 | 52,2% | 1.92 | niska |
Zawodnik (niska pewność): Wagner pkt O19.5 60,9% / ast O5.5 67,1% / PRA O32.5 61,9%; Bane pkt O16.5 61,8%, 3PM O2.5 61,4%; Black pkt O14.5 62,5%; Booker pkt O21.5 60,4%, ast O3.5 64,5%; Bridges 3PM O1.5 61,3%.
Ryzyka: Booker OUT → ORL ok. 60%; total drużyny Under to pułapka (kalibracja 2/6).

### 04:00 Miami Heat @ Golden State Warriors (US 05.11, 22:00 ET)
Model: GSW 121.0 – MIA 113.5. GSW 5-3 (W5), 3 dni odpoczynku; MIA 3-5, B2B po dogrywce w LA, Giannis (nadgarstek) niepotwierdzony. GSW bez Butlera, Porzingisa, Moody'ego, Santosa.
Rynek (odniesienie): GSW -7.5 (DK), total 235.5 (DK) / 232.5 (ESPN), ML GSW 1.36-1.385.
| Rynek | p | fair | pewność |
|---|---|---|---|
| GSW ML | 70,5% | 1.42 | średnia |
| GSW -3.5 | 62,1% | 1.61 | średnia |
| GSW -5.5 | 56,1% | 1.78 | niska-średnia |
| GSW -6.5 | 53,1% | 1.88 | niska |
| GSW -7.5 | 50,0% | 2.00 | niska |
| MIA +9.5 | 56,1% | 1.78 | niska-średnia |
| Over 229.5 | 60,4% | 1.66 | niska-średnia |
| Over 232.5 / Under 232.5 | 54,2% / 45,8% | 1.85 / 2.18 | niska |
| Under 235.5 | 52,1% | 1.92 | niska |
Zawodnik (niska pewność): Curry 3PM O3.5 66,8% (1.50), O4.5 48,4% (DK +125, przewaga ok. 4 pp), pkt O27.5 52%; Lendeborg pkt O18.5 58,3%; Draymond ast O5.5 56,5%; Podziemski pkt O14.5 62,5%; Adebayo zb U9.5 66,6% (fair 1.50, wrażliwe na brak Giannisa); Thompson 3PM O2.5 57,1%.
Ryzyka: Giannis OUT → GSW ML ok. 80%, total w dół; blowout skraca minuty Curry'ego.

## NHL (wszystkie z dogrywką, o ile nie zaznaczono; 01:00 PL, chyba że podano inaczej)

Bramkarze: potwierdzeni tylko Dobes (MTL), Binnington (STL), Skinner (WPG), Tomkins (EDM), Blackwood (COL), Varlamov (NYI), Woll (PHI), Garand (NYR), Silovs (PIT), DeSmith (DAL), Talbot (CBJ). Niepotwierdzeni: Cossa, Hart/Hill, Söderblom, Hellebuyck, Merilainen, Brossoit, Saros, Bussi, Swayman. Kontuzje skaterów w większości niezweryfikowane. B2B: tylko CHI (04.11 @ FLA).

| Mecz | ML (p / fair) | PL +1.5 | Total | Uwagi |
|---|---|---|---|---|
| UTA @ MTL | UTA 52,3% / 1.91; MTL 47,7% / 2.10 | UTA +1.5 74,4% / 1.34; MTL +1.5 70,5% / 1.42 | O4.5 81,9% (1.22); O5.5 65,2% (1.53); O6.5 52,9% (1.89) | λ UTA 3.40 / MTL 3.25; Dobes .853 |
| VGK @ DET | VGK 56% / 1.79; DET 44% / 2.27 | VGK +1.5 80,4% (1.24); DET +1.5 66,9% (1.49) | O4.5 70,6% (1.42); O5.5 50,5% (1.98) | Tarasov .938 (mała próba), Hart niepotw. |
| CHI @ TBL | TBL 76% / 1.32; CHI 24% / 4.17 | CHI +1.5 49,1% (2.04); TBL -1.5 50,9% (1.97) | O4.5 79,0% (1.27); O5.5 61,6% (1.62); O6.5 48,4% | CHI B2B, Söderblom .829 |
| STL @ NJD | NJD 63% / 1.59; STL 37% / 2.70 | NJD +1.5 84,4% (1.18); STL +1.5 60,5% (1.65) | O4.5 73,2% (1.37); O5.5 53,8% (1.86) | Binnington .846 |
| CAR @ NYI | CAR 62% / 1.61; NYI 38% / 2.63 | NYI +1.5 63% (1.59) | O5.5 56% (1.79); U6.5 57% (1.75) | Bussi niepotw. |
| PHI @ NYR | NYR 56% / 1.79; PHI 44% / 2.27 | PHI +1.5 66,5% (1.50) | O5.5 54% (1.85) | Woll vs Garand |
| BOS @ PIT | BOS 51% / 1.96; PIT 49% / 2.04 | BOS/PIT +1.5 72% (1.39) | O5.5 62% (1.61); O6.5 50% | Swayman niepotw.; brak info o Crosby, Malkin, Pastrnak |
| DAL @ CBJ | DAL 53% / 1.89; CBJ 47% / 2.13 | CBJ +1.5 69% (1.45); DAL +1.5 74% (1.35) | O5.5 54% (1.85); U6.5 57% (1.75) | DeSmith zamiast Oettingera (powód nieznany) |
| VAN @ WPG (01:00) | WPG 62% / 1.61; VAN 38% / 2.63 | VAN +1.5 61% (1.64); WPG +1.5 79% (1.27) | O5.5 65% (1.54); O6.5 51% | Skinner .881, Merilainen niepotw. |
| ANA @ EDM (02:00) | EDM 61% / 1.64; ANA 39% / 2.56 | ANA +1.5 62% (1.61); EDM +1.5 79% (1.27) | O5.5 74% (1.35); O6.5 58% (1.72) | Tomkins (4. bramkarz), Brossoit niepotw. |
| NSH @ COL (03:30) | COL 62% / 1.61; NSH 38% / 2.63 | NSH +1.5 62% (1.61); COL +1.5 80% (1.25) | O5.5 61% (1.64); U7.5 69% (1.45) | Saros niepotw. |

Rynek zawodnika NHL (niska pewność, jedno źródło, poza kuponami domyślnie): McDavid pkt O0.5 84% (1.19), Draisaitl pkt O0.5 82% (1.22), MacKinnon pkt O0.5 76% (1.32), Kucherov pkt O0.5 72% (1.39), Connor pkt O0.5 66% (1.52), Eichel pkt O0.5 66%, J. Hughes pkt O0.5 70%.

Kalibracja z weryfikacji: bez Under 4.5 (0/8 z 29-30.10); modele Poissona zaniżają remisy po 60' i ogony.

Wniosek: żaden typ nie ma wyraźnej przewagi nad rynkiem odniesienia (różnice ≤ 3-4 pp); EV rozstrzygną kursy Betclic.
