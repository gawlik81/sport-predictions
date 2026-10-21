# Kupony na 19.10.2026 (cel: 10; spełniających wszystkie progi: 0; po pominięciu EV > 0 i bez sprzeczności między kuponami: 3)

## 1. Okres i źródło kursów

- Okres: poniedziałek 19.10.2026 (NHL: noc 19→20.10). Czasy polskie.
- Kursy: **Betclic.pl** (przeglądarka, strony meczów), pobrane rano 19.10 (ok. 07:00). Kursy mogą się zmienić do startu. Zebrano komplet dla piłki, NHL i WTA (Ningbo/Osaka). Dla ATP Lyon nie otwierano stron Betclic; kursy odniesienia z innych serwisów (Faria 1.53, Musetti 1.33, Sonego ok. 1.50) są niżej niż moje fair odds, więc EV ujemne i nogi odpadają.
- Betclic nie oferuje w NHL puck line ani linii total 6.5 (są linie 3.5-5.5); wyceny z analiz NHL na puck line i 6.5 nie mają więc zastosowania na Betclic.
- Analizy: [ZWERYFIKOWANE_Analiza_dnia_2026-10-19.md](ZWERYFIKOWANE_Analiza_dnia_2026-10-19.md).
- Ograniczenia (skill daily-coupons): min. 2 nogi, kurs nogi > 1.2, kurs kuponu > 1.5 i < 2.5, p kuponu > 50%, EV > 0 (z CLAUDE.md), bez powtórzeń nóg i sprzeczności.

## 2. Terminarz (skrót)

16 wydarzeń przeanalizowanych: 5 meczów piłkarskich, 7 tenisowych (ATP Lyon 3, WTA Ningbo 3, WTA Osaka 1), 4 NHL. Brak: NBA (start sezonu 20.10 USA), MMA (UFC 333 dopiero 24.10), tier-1 e-sport, LoL. Pominięte z powodu rangi: Sporting Braga - Gil Vicente, Rodez - Montpellier. Pominięte, bo już trwały: WTA Osaka Krueger - Tjen, Ningbo Cirstea - Han; Challengery, ITF i debel poza zakresem.

## 3. Pula nóg po wycenie (Betclic)

Tylko nogi z kursem > 1.2 i fair > 1.15. "Przewaga niepotwierdzona" = moje p wyższe od p rynku (po usunięciu marży) o ponad 5 pp bez twardej informacji.

### Nogi z EV > 0

| Mecz | Rynek | p | Kurs Betclic | Fair | EV | Uwagi |
|---|---|---|---|---|---|---|
| Wisła Płock - Radomiak (19:00) | Under 2.5 | 54,4% | 2.30 | 1.84 | +25,1% | przewaga niepotwierdzona (rynek ok. 40,7%, +13,7 pp); wsparcie: H2H Under 2.5 w 7 z 8, słaby atak Radomiaka na wyjeździe |
| Wisła Płock - Radomiak | BTTS nie | 50,9% | 2.37 | 1.96 | +20,6% | przewaga niepotwierdzona (+11,5 pp) |
| Tottenham - Coventry (21:00) | Under 2.5 | 48,1% | 2.33 | 2.08 | +12,1% | p < 50% |
| PIT @ UTA (03:00) | PIT po 60' (3-way) | 34,2% | 3.12 | 2.93 | +6,7% | p < 50%, bramkarze niepotwierdzeni |
| SJS @ TOR (01:30) | Under 5.5 | 43,0% | 2.50 | 2.33 | +7,5% | p < 50% |
| ANA @ NYR (01:00) | ANA po 60' (3-way) | 38,5% | 2.70 | 2.60 | +4,0% | p < 50% |
| PIT @ UTA | Under 5.5 | 41,4% | 2.50 | 2.41 | +3,5% | p < 50% |
| Getafe - Rayo (21:00) | BTTS nie | 62,5% | 1.66 | 1.60 | +3,7% | przewaga niepotwierdzona (+6,3 pp) |
| Getafe - Rayo | Under 2.5 | 70,4% | 1.47 | 1.42 | +3,5% | przewaga niepotwierdzona (+6,8 pp); λ łączne 1,90 wymaga zachowania ostrożności |
| Parma - Torino (20:45) | BTTS nie | 56,8% | 1.82 | 1.76 | +3,4% | przewaga niepotwierdzona (+5,5 pp) |
| Parma - Torino | Under 2.5 | 63,6% | 1.61 | 1.57 | +2,4% | przewaga niepotwierdzona (+5,6 pp) |
| Getafe - Rayo | 1X | 68,6% | 1.47 | 1.46 | +0,8% | na granicy (+5,2 pp) |

Pewność: wszystkie niska lub niska-średnia (składy i bramkarze niepotwierdzone, brak sędziów i danych o rożnych/kartkach).

### Nogi z p > 50% i EV ≤ 0 (najbliższe zera)

| Mecz | Rynek | p | Kurs | EV |
|---|---|---|---|---|
| Monza - Cagliari | BTTS nie | 51,2% | 1.95 | -0,2% |
| Monza - Cagliari | Under 2.5 | 57,0% | 1.74 | -0,8% |
| Monza - Cagliari | 12 | 72,4% | 1.33 | -3,7% |
| Wisła Płock - Radomiak | 1X | 74,8% | 1.28 | -4,3% |
| Parma - Torino | 12 | 70,6% | 1.35 | -4,7% |
| Tottenham - Coventry | BTTS tak | 55,4% | 1.70 | -5,8% |

Pozostałe nogi (wygrany faworyta, Over 1.5/2.5, tenis WTA: Sasnovich 1.66, Bouzkova 1.30, Eala 1.26, Boulter 1.44, NHL moneyline) mają EV od -10% do -35%. Tottenham do wygrania wycenia Betclic na 1.50 (ok. 63%), mój model 43%, więc Spurs i Over 2.5 odpadają.

## 4. Kupony

**Żaden kupon nie spełnia wszystkich warunków jednocześnie.** Powody:

- Nogi z dodatnim EV mają p ≤ 50% (NHL, Tottenham Under) albo przewagę niepotwierdzoną, a łączone dają p kuponu < 50%. Dwie nogi z p ~ 70% i EV ≈ 0 dają p kuponu ~ 50%, a przy kursie nogi 1.3-1.5 kurs kuponu ~ 1.9-2.2; żaden zestaw nie ma jednocześnie p > 50% i EV > 0 (marża Betclic ok. 7%).
- Nogi z największym EV (Wisła Płock Under 2.5 2.30, BTTS nie 2.37) łączone z jakąkolwiek nogą > 1.2 dają kurs kuponu > 2.5.
- Żeby złożyć 10 kuponów bez powtórzeń trzeba ≥ 20 nóg spełniających kryteria; jest 0 nóg z p > 50% i potwierdzonym EV > 0.

Nie fabrykuję kuponów, żeby dobić do 10.

### Kupony poniżej progów (do wyboru, jeśli zrelaksujesz warunki)

**R1: EV dodatnie, p poniżej 50% (relaksacja p do ok. 45%).** Kupon poniżej progów.

| Noga | Godz. | p | Kurs Betclic |
|---|---|---|---|
| Getafe - Rayo, Under 2.5 | 21:00 | 70,4% | 1.47 |
| Parma - Torino, Under 2.5 | 20:45 | 63,6% | 1.61 |

Kurs kuponu 2.37, p 44,8%, fair 2.23, **EV +6,0%**. Stawka: ¼ Kelly 1,1% bankrolla (pełny Kelly 4,4%). Obie nogi to przewaga niepotwierdzona (+5-7 pp nad rynkiem) i mecze o niskiej liczbie goli, więc ryzyko skorelowane na poziomie ligi i stylu (niezależność meczów założona). Mimo p < 50% to jedyny zestaw z dodatnim EV i kursem w przedziale.

**R2: p > 50%, kurs w przedziale, ale EV ujemne (relaksacja EV).** Nie polecam: stawka 0%.

| Noga | Godz. | p | Kurs Betclic |
|---|---|---|---|
| Getafe - Rayo, 1X | 21:00 | 68,6% | 1.47 |
| Wisła Płock - Radomiak, 1X | 19:00 | 74,8% | 1.28 |

Kurs kuponu 1.88, p 51,3%, fair 1.95, **EV -3,4%**. Brak przewagi nad rynkiem.

**Pojedynczy typ (nie kupon, tylko informacja): Wisła Płock - Radomiak, Under 2.5 @ 2.30** (p 54,4%, EV +25%, ale przewaga niepotwierdzona o 13,7 pp; rynek wycenia Over 2.5 na 1.58, więc model i rynek mocno się rozjeżdżają). Przy zakładaniu: stawka symboliczna, maks. 0,5-1% bankrolla (limit 2%, a EV oparte na modelu bez twardej informacji); mecz o 19:00.

## 5. Które warunki zrelaksować

1. **Najuczciwsza opcja:** nie grać kuponami dzisiaj. Jest 1 zestaw (R1) z EV +6% przy p 44,8% i 1 pojedynczy typ z niepotwierdzoną przewagą.
2. Jeśli chcesz dodatnie EV: zrelaksuj p kuponu do ok. 45% (R1) i przedział kursu do 2.5; to daje 1 kupon, nie 10.
3. Jeśli chcesz p > 50%: zrelaksuj EV do ok. -3% (R2); to są kupony bez przewagi nad rynkiem.
4. Więcej nóg z wartością będzie przy większym terminarzu (weekend z Top 5 ligami, NBA po starcie sezonu); do 10 kuponów bez powtórzeń potrzeba ok. 20 kwalifikowanych nóg, co wymaga rozszerzenia o jutro (20.10: Liga Mistrzów 21:00, NBA/NHL).

## 6. Ostrzeżenia

- Zakładam niezależność nóg z różnych meczów; łączone Under 2.5 z dwóch ligowych meczów o niskiej liczbie goli mogą mieć dodatnią korelację (styl, sędziowie), co zawyżałoby p kuponu.
- Nogi z "przewagą niepotwierdzoną" opierają się na rozbieżności modelu i rynku bez twardej informacji; przy kalibracji z weryfikacji 07.10 takie typy częściej przegrywały.
- Kursy Betclic mogą się zmienić do startu; składy do potwierdzenia ok. godziny przed meczem (Tottenham: Porro/Kulusevski/Maddison; Rayo: Ratiu; Płock/Radomiak: brak potwierdzonych absencji), bramkarze NHL niepotwierdzeni (Daily Faceoff niedostępny w momencie analizy).
- Brak sędziów w meczach piłkarskich (kartki/faule nie wchodzą do puli); rożne bez dwóch niezależnych źródeł.
- Odrzucone przez regułę fair ≤ 1.15: Over 0.5 i Under 3.5 w większości meczów.
- Dane o kontuzjach tenisistów ograniczone; statystyki serwisu/returnu w tenisie szacowane, więc bez total gemów.

## 7. Kupony po pominięciu kryterium EV > 0 (na prośbę użytkownika)

Warunki: min. 2 nogi, na kuponie co najmniej dwie nogi z kursem > 1.2 (pozostałe mogą być ≤ 1.2, ale fair > 1.15), kurs kuponu 1.5-2.5, p kuponu > 50%, bez powtórzeń nóg, jedna noga na mecz w kuponie, **brak sprzeczności także między kuponami**: ten sam mecz w różnych kuponach tylko z nogami z różnych rodzin rynków (wynik / gole / BTTS), nigdy dwie nogi z rynku wyniku (np. 1X i 12 dają przeciwne pokrycie remisu: remis wygrywa jeden kupon i przegrywa drugi). Pula: 37 nóg z p > 50% (Betclic) plus krótkie nogi ≤ 1.2; 21 kandydatów-kuponów. Ranking po EV. Wszystkie EV ≤ 0, więc Kelly = 0%; stawka płaska symboliczna tylko jeśli i tak chcesz grać.

Poprzednia wersja miała kupon 2 (Płock 1X + Getafe 1X) i kupon 3 (Płock 12 + Getafe 12) na tych samych meczach: remis w obu meczach wygrywał kupon 2 i przegrywał kupon 3. Kupon 3 usunięty.

| # | Nogi (godz.) | Kursy Betclic | p nóg | Kurs kuponu | p kuponu | Fair | EV | Stawka |
|---|---|---|---|---|---|---|---|---|
| 1 | Monza - Cagliari 12 (18:30) + Getafe - Rayo Under 2.5 (21:00) | 1.33 / 1.47 | 72,4% / 70,4% | 1.96 | 51,0% | 1.96 | -0,3% | Kelly 0%; płaska do 0,5% |
| 2 | Płock - Radomiak 1X (19:00) + Getafe - Rayo 1X (21:00) | 1.28 / 1.47 | 74,8% / 68,6% | 1.88 | 51,3% | 1.95 | -3,4% | Kelly 0%; płaska do 0,5% |
| 3 | Parma - Torino 12 (20:45) + COL @ PHI Colorado lub remis po 60' (01:00 20.10) | 1.35 / 1.26 | 70,6% / 72,1% | 1.70 | 50,9% | 1.96 | -13,4% | Kelly 0%; nie polecam |

Uwagi:
- Kupony 1 i 2 oba zawierają Getafe - Rayo, ale w różnych rynkach (Under 2.5 i 1X), które da się wygrać jednocześnie (np. 1-1, 0-0, 1-0 dla Getafe); nie są sprzeczne, są za to skorelowane (ten sam mecz). Wariant ściśły (każdy mecz tylko w jednym kuponie) daje 2 kupony: Monza 12 + Getafe Under 2.5 (1.96, p 51,0%, EV -0,3%) oraz Płock 1X + Parma 12 (1.73, p 52,8%, EV -8,7%).
- Dodanie krótkich nóg (Tottenham 1X 1.14, Over 1.5 1.17, 12 po 60' w NHL i inne) nie dało nowych kuponów: dodatkowa noga obniża p kuponu poniżej 50%.
- Kupon 3 łączy NHL (bramkarze niepotwierdzeni, COL gra drugi mecz z rzędu następnego dnia) z Serie A; Betclic nie ma w NHL puck line, więc noga to podwójna szansa po 60 minutach.
- Zakładana niezależność nóg z różnych meczów. Fair odds kuponów 1.95-1.96 wobec kursów 1.70-1.96: długoterminowo -0,3% do -13%.
- Przewaga niepotwierdzona: Getafe Under 2.5 (+6,8 pp nad rynkiem) w kuponie 1, Getafe 1X (+5,2 pp) w kuponie 2.
