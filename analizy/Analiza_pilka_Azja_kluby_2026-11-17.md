# Analiza piłka: reprezentacje towarzyskie (Azja/Zatoka) + Luton - Peterborough + Atletico Nacional - Once Caldas, 17.11.2026

Źródła: Superbet (superbet_event_odds, _h2h, _stats), WebSearch/WebFetch (Football Australia, Tehran Times, ysscores, Africa Soccer, Win Sports, Noticias RCN, footballpredictions.com, El Heraldo/La Prensa HN). Model: poisson.py (λ ręcznie z formy, rynku i kadr). Kursy: Superbet (marża usunięta tam, gdzie piszę "devig"). Brak sędziów (poza Luton), brak danych rożnych/kartek w sieci dla meczów reprezentacji, więc rynki rożne/kartki/faule: **brak podstaw** (nie wyceniam). Oszacowania probabilistyczne, nie gwarancje.

Ranga: wszystkie mecze reprezentacji to **towarzyskie** (nieoficjalne, bez stawki, dużo zmian w drugiej połowie, rotacje). Stosuję zasady dla reprezentacji: λ nie niżej niż ~0,7, korekty kadrowe łącznie do ~15%, Under 2.5 przy łącznym λ ≤ 2,0 najwyżej średnia pewność.

---

## 1. Arabia Saudyjska - Uzbekistan (16:30 PL, Superbet 15683192)
Towarzyski, Doha (Jassim Bin Hamad Stadium), neutralny; Saudi "gospodarzem" tylko formalnie. Trenerzy: Donis / Cannavaro.
- **Forma:** Saudi: 3-2 z Koreą Płd. (13.11), 2-0 ZEA, 2-0 Irak, 3-0 Oman (wyjazd), 1-0 Kuwejt. Uzbekistan: 2-3 z Rosją (12.11), 0-2 Korea Płd., 4-1 Syria, 3-1 Iran.
- **H2H:** Saudi 3-0 (2021), 3-2 (2019); stare, waga niska.
- **Kadry:** Saudi w pełnym składzie przed Koreą (Africa Soccer); Al-Braikan wrócił po przeziębieniu. To drugi mecz zgrupowania (rotacje możliwe). Składy i nieobecni Uzbekistanu: brak danych. Sędzia nieznany.
- **λ:** Saudi 1,25 / Uzbekistan 1,10 (total 2,35, rynek ~2,4).
- **Rynek (devig):** 38,4 / 29,0 / 32,6; O2.5 43,8%.

| Rynek | p | fair | kurs Superbet | EV | Pewność |
|---|---|---|---|---|---|
| 1 | 39,7% | 2.52 | 2.42 | -4% | niska |
| X | 27,9% | 3.58 | 3.20 | -11% | niska |
| 2 | 32,4% | 3.09 | 2.85 | -8% | niska |
| 1X | 67,6% | 1.48 | 1.38 | -7% | niska |
| X2 | 60,3% | 1.66 | 1.51 | -9% | niska |
| 12 | 72,1% | 1.39 | 1.30 | -6% | niska |
| Under 3.5 | 78,9% | 1.27 | 1.22 | -4% | średnia |
| Under 2.5 | 58,3% | 1.72 | 1.64 | -4% | niska |
| Over 1.5 | 68,1% | 1.47 | 1.35 | -8% | niska |
| BTTS nie | 52,4% | 1.91 | 1.83 | -4% | niska |
| BTTS tak | 47,6% | 2.10 | 1.85 | -12% | niska |

**Wniosek:** wyrównany, "brak mocnego typu"; rynek wycenia bardzo zbliżone. Najlepszy: Under 3.5 (p 79%, fair 1.27, kurs 1.22, bez przewagi). Ryzyko: rotacje, gole po zmianach w friendly.

---

## 2. Jordania - Australia (17:00 PL, Superbet 15444656)
Towarzyski, **Doha** (mecz przeniesiony z Ammanu przez względy bezpieczeństwa; neutralny teren, Jordania formalnie gospodarz).
- **Forma:** Australia: 3-0 z Katarem (13.11), 2-4 i 1-1 z Brazylią (wrzesień). Jordania: 1-1 Syria (wrz.), wcześniej mundial (1-3 Argentyna, 1-2 Algieria, 1-3 Austria).
- **H2H:** Australia 2-1 (2022), 1-0 (2021), 1-0 (2019); 5-3 w historii.
- **Kadry:** Australia: skład Popovicia bez Ryana, Irvine'a, Degeneka i O'Neilla, 7 niedebiutantów, "osiem zmian" (Football Australia, Doha squad). Skład Jordanii nieznany. Sędzia nieznany.
- **λ:** Jordania 1,00 / Australia 1,40 (korekta kadrowa Australii -0,10 do -0,15, zgodnie z limitem; rynek devig 21,8 / 25,7 / 52,5, moje 46,1% Australii to -6 pp wobec rynku: uzasadnione tylko częściowo, bo rynek mógł już wycenić skład, więc dodatkowo obniżam pewność).
- **Rynek:** O2.5 devig 47,7%.

| Rynek | p | fair | kurs | EV | Pewność |
|---|---|---|---|---|---|
| Australia wygra (2) | 46,1% | 2.17 | 1.76 | -19% | niska |
| Jordania wygra (1) | 26,9% | 3.72 | 4.25 | +14% | niska (patrz uwaga) |
| X2 (Australia lub remis) | 73,1% | 1.37 | 1.18 | -14% | niska |
| 12 | 73,1% | 1.37 | 1.25 | -9% | niska |
| Under 3.5 | 77,9% | 1.28 | 1.28 | 0% | średnia |
| Under 2.5 | 57,0% | 1.76 | 1.76 | 0% | niska |
| Over 1.5 | 69,2% | 1.45 | 1.29 | -11% | niska |

**Wniosek:** brak mocnego typu. EV Jordanii +14% wynika z mojego λ i niepewności składów Australii, nie traktuj jako value (różnica vs rynek ~5 pp, rynek bywa trafniejszy). Ryzyko: Australia rotuje, Jordania (finalista Pucharu Azji) bez presji.

---

## 3. Irak - Iran (17:15 PL, Superbet 15865955)
Towarzyski, **Basra, Irak** (turniej towarzyski Irak/Iran/Palestyna/Liban). Uwaga: Tehran Times podaje terminy 22-26.11 (Iran-Irak 26.11), ysscores i Superbet podają 17.11; datę przyjmuję za Superbetem i ysscores, ale to niepotwierdzone, a jeśli mecz jest 26.11, nie typować.
- **Forma:** Irak: 2-0 z Saudi (wrz.), 3-2 Kuwejt, 1-1 Oman; ostatni mecz z Libanem (13.11, wynik brak). Iran: 2-0 Palestyna (14.11), 0-2 Rosja, 1-3 Uzbekistan.
- **H2H:** Iran wygrywa 3 z ostatnich 4 (1-0, 3-0, 1-0, 2-1 dla Iraku w 2019).
- **Kadry:** Iran: Ghalenoei zapowiedział szansę dla młodych; w kadrze 29 graczy **bez Taremiego i Beiranvanda** (Tehran Times), są Azmoun, Ezatolahi, Gholizadeh, Mohebi. Irak: skład nieznany. Faktor: Irak u siebie (Basra).
- **λ:** Irak 0,90 / Iran 1,20 (total 2,1; Iran -0,10 za brak Taremiego i eksperymenty, dom Iraku +0,05; rynek devig 23,7 / 28,1 / 48,2, moje Iran 42,9% to -5,3 pp: granica).

| Rynek | p | fair | kurs | EV | Pewność |
|---|---|---|---|---|---|
| Iran wygra (2) | 42,9% | 2.33 | 1.92 | -18% | niska |
| X2 | 72,4% | 1.38 | 1.22 | -12% | niska |
| 1X | 57,1% | 1.75 | 1.78 | +2% | niska |
| Under 2.5 | 65,0% | 1.54 | 1.53 | -1% | średnia/niska (λ ≈ 2,1) |
| Under 3.5 | 83,9% | 1.19 | 1.17 | -2% | średnia |
| BTTS nie | 58,5% | 1.71 | n/d | n/d | niska |

**Wniosek:** brak mocnego typu; relatywnie najlepszy Under 2.5/3.5 (niski λ, zamknięty derby). Ryzyko: data meczu, rotacje Iranu, gole po 80'.

---

## 4. Kuwejt - Honduras (17:30 PL, Superbet 15716939)
Towarzyski, Kuwait City (Al Sadaqua Walsalam), Kuwejt u siebie. Brak H2H (pierwszy mecz).
- **Forma:** Kuwejt: 3-0 Syria (13.11), 1-3 Oman, 2-3 Irak, 0-1 Saudi; u siebie śr. 2,0 gola strzelone / 1,6 stracone (footballpredictions.com, 10 meczów). Honduras: 1-3 ZEA (13.11, wynik z Superbet; źródła hond. nie potwierdziły), 1-1 Jamajka, 1-2 Martynika, 1-0 Jamajka, 2-3 Surinam; 1 wygrana w 7 wyjazdowych.
- **Kadry:** Honduras bez Bryana Rócheza i Alexa Guity (El Heraldo/La Prensa); trener Molina, "bez świeżych urazów" (footballpredictions). Kuwejt: brak danych o nieobecnych. Honduras to drugi mecz tournée po Abu Zabi (podróż).
- **λ:** Kuwejt 1,10 / Honduras 1,35 (Honduras słabszy bez Rócheza, ale klasa kadry wyższa; rynek devig 24,7 / 27,7 / 47,5, moje Honduras 42,5%: -5 pp).

| Rynek | p | fair | kurs | EV | Pewność |
|---|---|---|---|---|---|
| Honduras wygra (2) | 42,5% | 2.36 | 1.95 | -17% | niska |
| 1X | 57,6% | 1.74 | 1.76 | +1% | niska |
| X2 | 69,6% | 1.44 | 1.24 | -14% | niska |
| 12 | 72,9% | 1.37 | 1.28 | -7% | niska |
| Under 3.5 | 76,8% | 1.30 | 1.26 | -3% | średnia |
| Under 2.5 | 55,7% | 1.80 | 1.72 | -4% | niska |
| Over 1.5 | 70,2% | 1.42 | 1.31 | -8% | niska |
| BTTS | 49,4% / 50,6% | 2.02 / 1.98 | 1.83 (tak) | -10% | niska |

**Wniosek:** wyrównany; brak mocnego typu. Honduras jest nieznaną w składzie ekipą z kilkoma absencjami; Kuwejt 1X na granicy value tylko z moim λ (niska pewność).

---

## 5. Luton Town - Peterborough United (20:00 PL, EFL Trophy, Superbet 15752323)
Fazą grupową EFL Trophy (Starting11: to ostatni mecz Peterborough w tym sezonie w Trophy, Peterborough prawdopodobnie już odpadło; stawka Luton nieznana). Kenilworth Road. Trenerzy: Wilshere (Luton) / Savage (Peterborough). Sędzia: Niall Smith (brak danych o średniej kartek). Składy i nieobecni: brak (Superbet: brak danych).
- **Forma Luton (8 meczów):** 2-0 Forest Green, 1-1 Huddersfield, 2-0 w Peterborough (31.10), 3-1 Doncaster, 2-1 Leicester, 2-1 Barnsley, 1-2 MK Dons, 4-1 Wycombe: 17 strzelonych / 7 straconych (2,1 / 0,9).
- **Forma Peterborough:** 0-5 Reading (7.11), 0-2 Luton, 0-2 Bradford, 1-1 Bromley, 1-4 Huddersfield, 2-2 Burton, 3-1 Leicester, 4-1 Ipswich U21: 11 strzelonych / 20 straconych (1,4 / 2,5). Serie bez wygranej w lidze.
- **H2H:** Luton wygrało ostatnie 4 z 5 (0-2 31.10.2026, 2-1 kwi. 2026, 0-2 sierp. 2025, 0-2 2022).
- **Rotacja:** puchar z rotacją (w Trophy obowiązkowi młodzi gracze U21), więc obniżam pułap pewności faworyta o kilka pp.
- **λ:** Luton 2,10 / Peterborough 1,10 (total 3,2). **Rynek jest wyżej (O2.5 devig ~70%, implikowany total ~3,4)**; moje O2.5 62% to -8 pp: nie schodzę mocno, bo mało danych, ale uczciwie: rynek wycenia więcej goli (Trophy z młodzieżą i słabą defensywą Peterborough).

| Rynek | p | fair | kurs | EV | Pewność |
|---|---|---|---|---|---|
| Luton wygra (1) | 59% (po korekcie za rotację z 60,3%) | 1.69 | 1.51 | -11% | średnia |
| 1X | 79% | 1.27 | 1.14 | -10% | średnia |
| Over 1.5 | 82,9% | 1.21 (granica 1.15-1.20) | 1.07 | -11% | średnia |
| Over 2.5 | 62,0% | 1.61 | 1.31 | -19% | średnia |
| Under 3.5 | 60,3% | 1.66 | 1.90 | +15% | niska (λ vs rynek +8 pp) |
| Under 4.5 | 78,1% | 1.28 | 1.39 | +9% | niska/średnia |
| BTTS tak | 58,5% | 1.71 | n/d | n/d | niska |

**Wniosek:** najlepszy mecz dnia dla typu wynikowego (Luton 1X/wygra), ale kursy skrócone, brak EV. **Jedyne dodatnie EV: Under 3.5 / Under 4.5 (rynek wycenia ~3,4 gola, ja 3,2)**; pewność niska, bo to wynika wyłącznie z rozbieżności λ i nie ma potwierdzonych składów; ryzyko: Peterborough pogrążone w kryzysie (5-0, brak wygranej w lidze) może się rozsypać. Ryzyko typu Luton: remis i wygrana Peterborough (rotacja Luton, ~20/19%).

---

## 6. Atletico Nacional - Once Caldas (18.11 00:30 PL, Copa BetPlay, półfinał rewanż, Superbet 15844627)
Rewanż półfinału Copa Colombia, Medellín (Atanasio Girardot); ida (10.11, Manizales) 1-1, **w dwumeczu 1-1** (bez bramek na wyjeździe), więc po 90' możliwa dogrywka/karne. Rynek 1X2 Superbet dotyczy 90 minut. 3 dni po ligowym 1-1 (14.11, Nacional - Once Caldas, Fecha 19, Once Caldas zapewniło sobie ósemkę).
- **Forma Nacional:** 1-1 Once Caldas (14.11), 1-1 Once Caldas (10.11), 4-3 Pereira, 1-1 Bucaramanga, 2-0 Santa Fe, 2-1 Medellín, 3-0 Pasto, 0-1 Cúcuta. Once Caldas: 1-1 x2 z Nacional, 1-0 Águilas Doradas, 2-0 Santa Fe, 1-0 Valledupar, 1-1 Pereira, 1-1 Millonarios, 2-0 Medellín (mała liczba straconych goli).
- **Kadry:** Nacional bez Rengifo i Velásqueza (kadra Kolumbii na towarzyskie z Chile) i, wg Lucasa Gonzáleza, osiem graczy zawodowych w kadrach: "variantes se limitan" (Noticias RCN, 11.11); Cardona poza listą, wątpliwości Haydar (hamstring, ze źródła do pierwszego meczu). Once Caldas: Gómez (strzelec z idy) pauzuje za kartki, obie drużyny mają zawieszonych (Win Sports, jedno źródło). W Superbet brak listy nieobecnych. Sędzia nieznany.
- **H2H:** ostatnie 8: 3 remisy w tym dwa ostatnie 1-1, Nacional 3 wygrane w 2025, Once Caldas 1-0 (maj 2026). Niski scoring w ostatnich dwóch.
- **λ:** Nacional 1,55 / Once Caldas 0,85 (osłabienie kadrowe Nacional -0,1; Once Caldas z mocną defensywą; półfinał dwumeczu 1-1: obie strony ostrożne). Rynek devig: 57,0 / 24,1 / 18,9; moje 1 = 53,8% (-3 pp).
- **Puchar z rotacją i stawką:** pułap pewności obniżony.

| Rynek | p | fair | kurs | EV | Pewność |
|---|---|---|---|---|---|
| Nacional wygra (1, 90') | 53,8% | 1.86 | 1.63 | -12% | średnia/niska |
| X | 25,6% | 3.91 | 3.85 | -2% | niska |
| Once Caldas (2) | 20,6% | 4.86 | 4.90 | +1% | niska |
| 1X | 79,4% | 1.26 | 1.14 | -10% | średnia |
| 12 (bez remisu) | 74,4% | 1.34 | 1.23 | -8% | średnia/niska |
| Under 3.5 | 77,9% | 1.28 | 1.29 | +1% | średnia |
| Under 2.5 | 57,0% | 1.76 | 1.78 | +1% | niska |
| Over 1.5 | 69,2% | 1.45 | 1.29 | -11% | średnia |
| BTTS nie | 54,9% | 1.82 | n/d | n/d | niska |

**Wniosek:** typ wynikowy Nacional 1X (79%, fair 1.26, kurs 1.14) bez wartości. Under 2.5/3.5 neutralne wobec rynku. Ryzyko Nacional: remis i wygrana Once Caldas (~26%/21%) przy osłabionym składzie; dogrywka/karne nie wchodzą w 90'.

---

## Podsumowanie

- Brak typów z wyraźną przewagą nad rynkiem (poza niskopewnymi: Luton Under 3.5/4.5 i Kuwejt 1X, +1 do +15% EV z mojego λ).
- Kandydaci o p >= 50% (wszystkie bez EV, pewność niska/średnia): Luton 1X 79% (fair 1.27, granica), Nacional 1X 79,4% (fair 1.26), Saudi - Uzbekistan Under 3.5 78,9% (fair 1.27), Jordania - Australia Under 3.5 77,9% (1.28), Irak - Iran Under 3.5 83,9% (fair 1.19, granica 1.15-1.20), Kuwejt Under 3.5 76,8% (1.30), Luton Over 1.5 82,9% (fair 1.21).
- Rożne/kartki/faule/strzały: brak podstaw (brak danych o sędziach i średnich dla reprezentacji, składy niepotwierdzone).
- Składy oficjalne pojawią się 60-75 min przed meczem (superbet_lineups); do sprawdzenia przed kuponem.
