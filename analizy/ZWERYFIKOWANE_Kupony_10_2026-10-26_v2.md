# Kupony NBA i NHL, noc 26/27.10.2026 (v2, uzupełnienie `ZWERYFIKOWANE_Kupony_10_2026-10-26.md`)

**Wynik: poziomy 0-2: 0 kuponów; poziom 3 (za zgodą użytkownika): 2 kupony zamiast 10, oba z EV ujemnym i stawką 0%.** Na poziomach 0-2 żadna noga z pewnych danych nie ma EV > 0. Nie dobijałem do 10 na siłę.

## 1. Źródło kursów i ograniczenia
- Betclic.pl, pobrane 26.10 ok. 22:10-22:20 CET przez WebFetch (odczyt strony i streszczenie modelem). **MCP przeglądarki (`mcp__claude-in-chrome__*`) nie było w tej sesji**, więc nie wykonano zalecanego odczytu `get_page_text`. Kursy tej jakości traktować jako orientacyjne.
- Potwierdzenia na gg397.bet **nie robiłem**.
- Betclic: NBA ma moneyline, spready i totale, ale odczyt pokazał tylko skrajne linie (np. spread ±13,5 do ±24,5, total 218,5-232,5), a nie linie główne (spread 4-10, total 217-240). Spready i totale NBA są więc **niewycenione**. NHL: 3-way po 60', moneyline 2-way, totale 3,5-5,5 (brak 6,5), team totale, brak puck line i brak rynków bramkarza (Jarry).
- Analizy (p, fair): `analizy/ZWERYFIKOWANE_Analiza_NBA_NHL_2026-10-26.md`.

## 2. Terminarz w skrócie
NBA 9 meczów, NHL 3 mecze (patrz analiza). Pominięte: brak.

## 3. Pula nóg (kurs Betclic vs własne p)
Wszystkie wycenione nogi mają EV ujemne.

| Mecz | Rynek | p | Kurs Betclic | Fair | EV |
|---|---|---|---|---|---|
| IND @ MIL | IND wygra | 62,0% | 1,57 | 1,61 | -2,7% |
| OKC - PHX | OKC wygra | 75,0% | 1,29 | 1,33 | -3,3% |
| HOU - ATL | HOU wygra | 65,0% | 1,49 | 1,54 | -3,1% |
| CLE - MIN | CLE wygra | 63,5% | 1,52 | 1,57 | -3,5% |
| DEN - GSW | DEN wygra | 71,0% | 1,34 | 1,41 | -4,9% |
| BOS - CHI | BOS wygra | 85,1% | 1,11 | 1,18 | -5,5% |
| CHA - WAS | CHA wygra | 57,9% | 1,62 | 1,73 | -6,2% |
| MIA - DAL | MIA wygra | 71,0% | 1,32 | 1,41 | -6,3% |
| UTA - MEM | UTA / MEM | 51,5% / 48,5% | 1,77 / 1,97 | 1,94 / 2,06 | -8,8% / -4,5% |
| TOR @ CGY | Over 5,5 goli | 62,0% | 1,49 | 1,61 | -7,6% |
| DET @ EDM | Over 5,5 goli | 64,0% | 1,42 | 1,56 | -9,1% |
| TOR @ CGY | TOR wygra (2-way) | 57,0% | 1,65 | 1,75 | -5,9% |
| LAK @ NYR | NYR wygra (2-way) | 55,5% | 1,68 | 1,80 | -6,8% |
| DET @ EDM | EDM wygra (2-way) | 59,5% | 1,53 | 1,68 | -9,0% |
| LAK @ NYR | NYR po 60' | 44,5% | 2,13 | 2,25 | -5,2% |

Underdogi NBA (WAS, MIN, CHI, DAL, PHX, MIL, ATL, GSW) mają EV od -7% do -24%. Nogi o p poniżej 50% i tak nie przechodzą progu.

## 4. Kupony

### Poziom 3 (zgoda użytkownika; poniżej progów bazowych, stawka 0%)
Poziom 3 dodaje do poziomów 1-2 próg p zestawu > 45% (nogi pojedyncze p ≥ 55%). Zostają: kurs zestawu 1,5-2,5, co najmniej dwie nogi z kursem > 1,2, fair nogi > 1,15, jedna noga na mecz, żadna noga w dwóch kuponach. Z 11 nóg o p ≥ 55% tylko 5 ma p ≥ 65%, więc p zestawu > 45% przechodzą tylko pary faworytów; **powstają 2 kupony zamiast 10** (nie dobijam na siłę). Wszystkie nogi to zwycięzca meczu, więc jest to jedna rodzina rynków. Kursy z Betclic (WebFetch, 22:10-22:20 CET), bez potwierdzenia gg397.bet.

| # | Nogi (godzina PL) | p | Kurs | EV | Stawka | Złamane progi |
|---|---|---|---|---|---|---|
| 1 | OKC wygra PHX (01:00, kurs 1,29, p 75%) + DEN wygra z GSW (03:00, kurs 1,34, p 71%) | 53,2% | 1,73 | -8,0% | 0% | EV ≤ 0 (poziomy 1-2) |
| 2 | MIA wygra z DAL (00:30, kurs 1,32, p 71%) + HOU wygra z ATL (01:30, kurs 1,49, p 65%) | 46,1% | 1,97 | -9,2% | 0% | EV ≤ 0, p zestawu < 50% (poziom 3) |

Uwagi do nóg: OKC gra B2B, bez J. Williamsa i Holmgrena, Wallace niepewny. DEN: C. Johnson doubtful. MIA: Flagg i Martin (DAL) niepewni, MIA 0-3 w sezonie. HOU: Smart i Adams Out (rezerwowi). Wszystkie nogi średniej pewności. Daty lokalne USA: 26.10 (mecze zaczynają się 27.10 w Polsce).
Odrzucone: BOS wygra (kurs 1,11, p 85,1%) wchodzi tylko w trójce BOS + OKC + DEN (kurs 1,92, p 45,3%, EV -13,1%), która zabiera nogi z kuponu 1 i ma najgorsze EV. CLE, IND i TOR/CGY Over 5,5 mają p 62-63,5% i w parze nie osiągają p > 45% przy kursie ≤ 2,5. CHA (p 57,9%) i NYR (55,5%) mają niską pewność.

### Bez poziomu 3
Najbliższe EV zera to IND ML (-2,7%), HOU ML (-3,1%) i OKC ML (-3,3%), a ich łączny kurs wyszedłby poniżej progu 1,5 (np. IND x HOU = 2,34, EV ok. -5,7%).

## 5. Ostrzeżenia
- Nie mam kursów na główne linie spreadów i totali NBA oraz rynków bramkarza NHL. Jedyny kandydat z dodatnim EV w analizach (Jarry Under 26,5, ok. +12% na kursie u-115 u innego bukmachera) nie jest dostępny na Betclic.
- Jedynie rynek zawodnika Booker Over 24,5 pkt (Betclic 2,18) mógłby mieć przewagę, ale p pochodzi z jednego źródła i odczyt kursu był niepewny, więc go nie używam.
- Statusy do sprawdzenia przed meczem: Edwards (MIN), Reid (CHA), Flagg i Martin (DAL), Nembhard (IND), Wallace i J. Williams (OKC), Backlund (CGY), bramkarze Kuemper i Bobrovsky.
- Założenie niezależności nóg, kursy mogą się zmienić do startu (pierwsze mecze o 00:00).

## 6. Uzupełnienie: spready i totale NBA z fallbacku (MCP `sportsdata`, The Odds API, ok. 22:30 CET)
Źródło: **fallback, nie Betclic** (Pinnacle, Unibet NL, William Hill, Tipico DE; kursy 1,80-2,04). Ceny Betclic dla tych linii nie zostały potwierdzone.

- Linie główne po kalibracji rynku: WAS @ CHA 227,5-228,5 / CHA -2,5 do -3,5; MIN @ CLE 231,5-232,5 / CLE -4,5; CHI @ BOS 232,5 / BOS -14,5; DAL @ MIA 240,5-241,5 / MIA -7,5; IND @ MIL 238,5-239,5 / IND -4,5; PHX @ OKC 221,5 / OKC -8,5; ATL @ HOU 229,5 / HOU -4,5; MEM @ UTA 237,5 / UTA -0,5 do -1,5; GSW @ DEN 236,5 / DEN -7 do -7,5.
- Spready i totale w większości meczów dają p 47-53% przy kursach 1,85-1,95, czyli EV od -3% do -8%. Nie przechodzą progu p ≥ 55% dla nogi (poziom 3).
- Dwie nogi mają p ≥ 55% wobec obecnych linii (model `nba_model.py`):
  - PHX @ OKC Under 221,5: p 58,8%, kurs 1,89 (Unibet NL) / 1,93 (Pinnacle), EV ok. +11%.
  - DAL @ MIA Under 240,5: p 57,7%, kurs 1,93 (Unibet NL), EV ok. +11%.
  Oba EV pochodzą z p wyższego od rynku o ok. 7-8 pp (model 217,5 i 237 vs linia rynku 221,5 i 240,5) bez twardej informacji w analizie, więc według skilla to "przewaga niepotwierdzona" i nie ufam im. Linia MIA-DAL wzrosła od czasu analizy (236,5-239,5 → 240,5-241,5), przyczyny nie znam.
- Żaden kupon z tych nóg nie spełnia poziomu 3: para Under OKC-PHX + Under MIA-DAL ma p 33,9%, a z DEN lub BOS p poniżej 45% (albo tylko jedna noga z kursem > 1,2). **Liczba kuponów bez zmian: 2 (OKC + DEN, MIA + HOU).**

## 7. Poziom 4 (zgoda użytkownika; poniżej progów bazowych, stawka 0%)
Poziom 4 dokłada do poziomów 1-3 luz: kurs > 1,2 wymagany tylko dla jednej nogi. Nadal: p zestawu > 45%, nogi pojedyncze p ≥ 55%, fair nogi > 1,15, kurs zestawu 1,5-2,5, jedna noga na mecz, żadna noga w dwóch kuponach. Jedyna noga z kursem ≤ 1,2 i fair > 1,15 to BOS (1,11). **Powstają 4 kupony** (ułożone tak, by użyć najwięcej nóg bez powtórzeń). To alternatywa dla 2 kuponów z poziomu 3 (te same nogi), nie dodatek. Kursy Betclic (WebFetch, 22:10-22:20 CET), bez gg397.bet. `slip.py` flaguje kurs zestawu > 2,0 według starego progu, aktualny próg to 2,5.

| # | Nogi (godzina PL) | p | Kurs | EV | Stawka | Złamane progi |
|---|---|---|---|---|---|---|
| 1 | BOS wygra z CHI (00:30, 1,11, p 85,1%) + IND wygra w MIL (01:00, 1,57, p 62%) | 52,8% | 1,74 | -8,1% | 0% | EV ≤ 0, jedna noga ≤ 1,2 (poziom 4) |
| 2 | OKC wygra z PHX (01:00, 1,29, p 75%) + TOR @ CGY Over 5,5 goli (01:30, 1,49, p 62%) | 46,5% | 1,92 | -10,6% | 0% | EV ≤ 0, p zestawu < 50% (poziom 3) |
| 3 | DEN wygra z GSW (03:00, 1,34, p 71%) + HOU wygra z ATL (01:30, 1,49, p 65%) | 46,1% | 2,00 | -7,9% | 0% | EV ≤ 0, p zestawu < 50% (poziom 3) |
| 4 | MIA wygra z DAL (00:30, 1,32, p 71%) + CLE wygra z MIN (00:00, 1,52, p 63,5%) | 45,1% | 2,01 | -9,5% | 0% | EV ≤ 0, p zestawu < 50% (poziom 3) |

Uwagi: kupon 2 zawiera nogę NHL zależną od bramkarza (Bobrovsky "Likely", Cooley Confirmed), więc "po bramkarzu" i tylko jako zestaw ryzykowny. Kupon 4: Edwards (MIN) DTD, MIN na B2B. Kupon 1: IND na B2B, Nembhard questionable, Zubac Out. OKC na B2B bez J. Williamsa i Holmgrena. Kupony 1, 3 i 4 to wyłącznie zwycięzcy meczu.
Odrzucone: BOS + DEN, BOS + MIA, BOS + OKC mają kurs zestawu 1,43-1,49, poniżej dolnej granicy 1,5 (poziom 5). Nogi o p 55-60% (CHA, NYR, EDM, TOR ML) nie tworzą par z p > 45%.

## 8. Korekta do poziomu 4 i test luzowania p do 35%
- **Pominięcie w sekcji 7:** kupony BOS wygra + Under 221,5 (PHX @ OKC) i BOS wygra + Under 240,5 (DAL @ MIA) formalnie spełniają poziom 4 (jedna noga > 1,2, p zestawu ≥ 49%, kurs zestawu 2,10-2,14, p nogi ≥ 55%) i mają EV dodatnie. Pominąłem je w sekcji 7, bo obie nogi Under to "przewaga niepotwierdzona" (p wyższe od rynku o 7-8 pp bez twardej informacji), a ich kursy to fallback (Unibet NL), nie Betclic.

| Zestaw | p | Kurs | EV | Uwagi |
|---|---|---|---|---|
| BOS wygra (1,11) + Under 221,5 PHX @ OKC (1,89, Unibet NL) | 50,0% | 2,10 | +5,0% | EV z niepotwierdzonej nogi, stawka wg skryptu 1,1-2,3% (1/4-1/2 Kelly), do decyzji użytkownika |
| BOS wygra (1,11) + Under 240,5 DAL @ MIA (1,93, Unibet NL) | 49,1% | 2,14 | +5,2% | jw. |
| Under 221,5 OKC + Under 240,5 MIA | 33,9% | 3,65 | +23,8% | p < 35% i kurs > 2,5, nie przechodzi |

- Luzowanie p zestawu do 35% nie tworzy dodatkowych kuponów z EV > 0: EV zależy od nóg, a każda inna wyceniona noga (zwycięzcy, Over NHL, underdogi) ma EV ujemne od -2,7% do -24%.

## 9. Poziom -1 (tryb EV, bez progów p i kursu; za zgodą użytkownika; stawka Kelly 1/4)
Wymóg: EV > 0 zestawu i każdej nogi. Nogi z EV > 0 po cenach Betclic lub fallbacku: tylko dwa Under (wszystkie wyceny zwycięzców, Over NHL i underdogów mają EV < 0).

| # | Nogi (godzina PL) | p | Kurs | EV | Stawka (1/4 Kelly) | Uwagi |
|---|---|---|---|---|---|---|
| 1 | Under 221,5 PHX @ OKC (01:00, 1,89, Unibet NL, p 58,8%) + Under 240,5 DAL @ MIA (00:30, 1,93, Unibet NL, p 57,7%) | 33,9% | 3,65 | +23,8% | ok. 2,2% bankrolla wg `slip.py` | obie nogi to "przewaga niepotwierdzona" (p wyższe od rynku o 7-8 pp), kursy spoza Betclic, p zestawu niskie, więc wariancja wysoka |

Sugerowana stawka ze skryptu zakłada p, w które nie ufam; rozsądniej połowa tej kwoty lub mniej.

### Korekta kursów kuponu poziomu -1 (kursy Betclic podane przez użytkownika)
Użytkownik podał kursy Betclic: Under PHX @ OKC 1,82 i Under DAL @ MIA 1,89 (zakładam te same linie, 221,5 i 240,5, i podane kolejności nóg). Źródło: Betclic (przekazane przez użytkownika, niezweryfikowane przeze mnie ani na gg397.bet).

| Nogi | p | Kurs | EV | Stawka (1/4 Kelly) |
|---|---|---|---|---|
| Under 221,5 PHX @ OKC (1,82, p 58,8%, EV +7,0%) + Under 240,5 DAL @ MIA (1,89, p 57,7%, EV +9,1%) | 33,9% | 3,44 | +16,7% | ok. 1,7% |

Nogi nadal "przewaga niepotwierdzona" (p wyższe od rynku o 7-8 pp bez twardej informacji). Fair nóg 1,70 i 1,73 jest poniżej kursów Betclic, więc EV nóg jest dodatnie.
