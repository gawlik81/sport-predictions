# Analiza tenis WTA 250 Prudential Hong Kong Tennis Open - 1. runda, 03.11.2026

Twardy outdoor (Victoria Park). Godziny polskie (CET), źródło terminarza: ESPN (scoreboard); losowanie i rozstawienie: tennis.com. Status w chwili analizy (ESPN): wszystkie 8 meczów "Scheduled" (mecze o 07:00 dopiero startowały, brak wyników do wyłączenia z wyceny).

## Źródła i ograniczenia danych
- Ranking WTA z 02.11.2026 (MCP sportsdata `wta_rankings`), terminarz ESPN, drabinka tennis.com (rozstawienie, Q/LL/WC), kwalifikacje z ESPN (30.10-01.11).
- Kursy: **Pinnacle** (MCP `pinnacle_matchup_markets`, kursy amerykańskie przeliczone, marża usunięta proporcjonalnie). Brak Pinnacle dla Samsonova - Shubladze (brak w feedzie).
- **Brak statystyk sezonu (serwis/return %) i H2H**: `apitennis_*` wymaga klucza API_TENNIS_KEY (niedostępny), wyszukiwanie WWW nie zwróciło statystyk ani wiarygodnych wyników z ostatnich tygodni większości zawodniczek. Wszystkie p_serve są więc **oszacowane** (skalibrowane do rankingu i rynku) -> **total gemów nie jest typowany** (reguła Skalibruj). Pewność wszędzie niska lub średnia-niska.
- Kontuzje: osobne wyszukiwanie wykonane dla Cîrstea, Badosa, Eala, Samsonova; dla pozostałych nie znaleziono informacji (brak = nie potwierdzono braku).
- Model: `tennis_model.py` (bo3) z p_serve dobranym tak, by p meczu odpowiadało liczbie po korektach; rozkład wyniku setowego spłaszczony (WTA).

## Korekty (Skalibruj), które zmieniły liczby
- **Kwalifikantki** (Sakatsume, Shubladze) i **lucky loser** (Pridankina, 2 mecze kwalifikacji, rytm i aklimatyzacja): faworytkom odjęto 4-6 pp względem rynku/rankingu.
- **R1 bez własnych statystyk**: p >= 70% obniżone/ograniczone (zakres ~75%).
- **Powrót po kontuzji / kontuzjogenność**: Badosa (pull-out z US Open 2026 z powodu pleców, seria urazów w 2026; niepotwierdzony stan na teraz), Cîrstea (uraz z US Open, powrót w Wuhan; Wuhan R2 i Ningbo R2 odpadnięcie, potem Tokio - wynik nieznany; 36 lat).
- **Rozbieżność z rynkiem >5 pp** bez twardej informacji: przyjęto dolną część rozstępu między moją estymacją a rynkiem.

## Tabela zbiorcza

| Mecz | Rynek | p | Fair | Pewność |
|---|---|---|---|---|
| Sönmez - Yastremska (07:00) | Sönmez wygra | 52,5% | 1,90 | niska |
| Oliynykova - Gibson (07:00) | Gibson wygra | 76% | 1,32 | średnia-niska |
| Joint - Inglis (08:30) | Joint wygra | 69% | 1,45 | niska |
| Timofeeva - Cîrstea (08:30) | Cîrstea wygra | 62% | 1,61 | niska |
| Valentova - Sakatsume (10:00) | Valentova wygra | 70% | 1,43 | niska |
| Samsonova - Shubladze (10:00) | Samsonova wygra | 66% | 1,52 | niska (brak rynku) |
| Eala - Parks (11:30) | Eala wygra | 75% | 1,33 | średnia-niska |
| Badosa - Pridankina (13:00) | Badosa wygra | 66% | 1,52 | niska |

Zwycięzca 1. seta i wynik setowy - patrz sekcje poniżej. Żaden typ nie kwalifikuje się do rankingu TOP-N (R1 bez statystyk, kwalifikantki/LL, rynek zbliżony); typy z fair <= 1,35 (Gibson 1,32, Eala 1,33) są graniczne/krótkie.

---

### Zeynep Sönmez (67.) - Dayana Yastremska (99.) (WTA 250 Hong Kong, R1, hard, 03.11 07:00)
**Typ:** Sönmez wygra | **p:** 52,5% | **Fair:** 1,90 | **Pewność:** niska (moneta)
- Zwycięzca 1. seta: Sönmez 50% (fair 2,00) / Yastremska 50%.
- Wynik setowy (spłaszczony): Sönmez 2-0 26% (3,85), Sönmez 2-1 26% (3,85), Yastremska 2-1 24% (4,15), Yastremska 2-0 23% (4,35).
**Statystyki:** ranking 67 vs 99; brak danych serwis/return. Yastremska to hitterka z dużą wariancją (wiele break pointów i błędów), Sönmez równiejsza; tyle z ogólnej wiedzy, nie z researchu.
**H2H:** nieustalone (brak klucza apitennis).
**Media:** brak potwierdzonych kontuzji; oba mecze 07:00 jako pierwsze na korcie (chłodniejsze warunki poranne - niepotwierdzone).
**Ryzyka:** wysoka wariancja Yastremskiej; dowolny wynik.
**Rynek:** Pinnacle (bez marży): Sönmez 51,2%, Yastremska 48,8%; 1. set Yastremska 51,2%. Zgodne z moją liczbą, brak value.

### Oleksandra Oliynykova (62.) - Talia Gibson (36., rozstawiona 5) (R1, 03.11 07:00)
**Typ:** Gibson wygra | **p:** 76% | **Fair:** 1,32 | **Pewność:** średnia-niska
- Zwycięzca 1. seta: Gibson 68% (fair 1,47).
- Wynik setowy: Gibson 2-0 44% (2,27), Gibson 2-1 32% (3,13), Oliynykova 2-1 14% (7,1), Oliynykova 2-0 10% (10,0).
**Statystyki:** ranking 36 vs 62 (+2 miejsca w rankingu Gibson), 31 turniejów w sezonie u Gibson (duże obciążenie), 30 u Oliynykovej. Brak %.
**H2H:** nieustalone.
**Media:** brak potwierdzonych kontuzji; Gibson kończy sezon przy sporym przebiegu meczów (zmęczenie - ryzyko).
**Ryzyka:** pierwszy mecz seed 5 w tygodniu, zmęczenie końcówką sezonu, serwis Oliynykovej.
**Rynek:** Pinnacle: Gibson 81,0% (fair 1,23); 1. set 76,2%. Różnica -5 pp (moja korekta za brak statystyk i wysoką p w R1); fair 1,32 poniżej rynku, więc brak value.

### Maya Joint (90.) - Maddison Inglis (WC) (R1, 03.11 08:30)
**Typ:** Joint wygra | **p:** 69% | **Fair:** 1,45 | **Pewność:** niska
- Zwycięzca 1. seta: Joint 63% (1,59).
- Wynik setowy: Joint 2-0 40% (2,50), Joint 2-1 29% (3,40), Inglis 2-1 18% (5,6), Inglis 2-0 13% (7,7).
**Statystyki:** Joint (rank 90, +4) w wzroście, 20 lat; Inglis dzika karta (ranking niżej, nie ustalony w top 100). Derby australijskie - Inglis gra przed własną publicznością w sensie kibicowskim, nie warunkowym (Hongkong).
**H2H:** nieustalone.
**Media:** brak potwierdzonych kontuzji.
**Ryzyka:** wild card z rytmem po sezonie krajowych turniejów; mecz otwarcia Joint po podróży z Europy/Ameryki (nieustalone).
**Rynek:** Pinnacle: Joint 72,9% (fair 1,37); 1. set 68,7%. Moja p niższa o 4 pp (brak statystyk) - bez value.

### Maria Timofeeva (70.) - Sorana Cîrstea (15., rozstawiona 1) (R1, 03.11 08:30)
**Typ:** Cîrstea wygra | **p:** 62% | **Fair:** 1,61 | **Pewność:** niska
- Zwycięzca 1. seta: Cîrstea 58% (1,72).
- Wynik setowy: Cîrstea 2-0 34% (2,94), Cîrstea 2-1 28% (3,53), Timofeeva 2-1 20% (4,9), Timofeeva 2-0 17% (5,8).
**Statystyki:** ranking 15 vs 70, ale Cîrstea ma 36 lat i w 2026 wraca po urazie z US Open (nie jest znana pełna diagnoza); po Wuhan (R2 odpadnięcie) i Ningbo (R2, przegrana z Bejlek 7-6(3) 6-4 21.10) miała jeszcze Tokio (26.10-01.11, wynik niepotwierdzony) - 3. turniej z rzędu w Azji. Timofeeva w głównej drabince jako alternate (niekwalifikantka), 24 turnieje w sezonie.
**H2H:** nieustalone.
**Media:** uraz z US Open (Romanian press: powrót w Wuhan); brak informacji o aktualnych dolegliwościach. Plotki - brak.
**Ryzyka:** nawrót urazu, zmęczenie azjatyckim tournée, wiek; seed 1 pod presją.
**Rynek:** Pinnacle: Cîrstea 66,4% (fair 1,51); 1. set 63,7%. Moja p niższa o ~4 pp (kontuzja + zmęczenie).

### Tereza Valentova (85.) - Himeno Sakatsume (Q) (R1, 03.11 10:00)
**Typ:** Valentova wygra | **p:** 70% | **Fair:** 1,43 | **Pewność:** niska
- Zwycięzca 1. seta: Valentova 64% (1,56).
- Wynik setowy: Valentova 2-0 41% (2,44), Valentova 2-1 29% (3,45), Sakatsume 2-1 17% (5,9), Sakatsume 2-0 13% (7,7).
**Statystyki:** Valentova (rank 85, 18 lat); Sakatsume przeszła 2 rundy kwalifikacji (wygrane z Hong Yi Cody Wong i z Pridankina w finale kwalifikacji) - rytm, aklimatyzacja, przewaga warunków (Japonka w Azji).
**H2H:** nieustalone.
**Media:** brak.
**Ryzyka:** kwalifikantka z rytmem; Valentova młoda i falująca.
**Rynek:** Pinnacle: Valentova 79,1% (fair 1,26); 1. set 72,2%. Różnica -9 pp, ale tu jest konkretna korekta (kwalifikantka), nie błąd; przy tak dużym rozstępie pewność niska.

### Liudmila Samsonova (40., rozstawiona 7) - Alexandra Shubladze (Q) (R1, 03.11 10:00)
**Typ:** Samsonova wygra | **p:** 66% | **Fair:** 1,52 | **Pewność:** niska (brak rynku)
- Zwycięzca 1. seta: Samsonova 61% (1,64).
- Wynik setowy: Samsonova 2-0 37% (2,7), Samsonova 2-1 29% (3,45), Shubladze 2-1 19% (5,3), Shubladze 2-0 15% (6,7).
**Statystyki:** Samsonova mocny serwis (mocna na twardym), ale rank 40 i seed spoza top 30 -> korekta za kwalifikantkę (-6 pp z ~72%). Shubladze wygrała 2 mecze kwalifikacji (Zhang Ying, Emerson Jones) na tym samym obiekcie. Samsonova grała Japan Open do 3. rundy (19.10); stan zdrowia/późniejsze turnieje niepotwierdzone.
**H2H:** nieustalone.
**Media:** brak kontuzji w wynikach wyszukiwania.
**Ryzyka:** kwalifikantka z rytmem, wysoka wariancja serwisu Samsonovej, możliwa męczliwość końca sezonu.
**Rynek:** brak (nie ma w feedzie Pinnacle). Bez rynku nie sprawdzam value.

### Alexandra Eala (17., rozstawiona 2) - Alycia Parks (59.) (R1, 03.11 11:30)
**Typ:** Eala wygra | **p:** 75% | **Fair:** 1,33 | **Pewność:** średnia-niska
- Zwycięzca 1. seta: Eala 67,5% (1,48).
- Wynik setowy: Eala 2-0 44% (2,27), Eala 2-1 31% (3,2), Parks 2-1 14% (7,1), Parks 2-0 11% (9,0).
**Statystyki:** ranking 17 vs 59; Eala 28 turniejów, Parks 36 (najwięcej w stawce, +6 w rankingu). Parks to potężny serwis i wysoka wariancja (asy/podwójne błędy). Eala w tournée: Wuhan odpadła z Han Shi (6-4 3-6 3-6, wg Stat Sniper), w Ningbo 22.10 pokonała Parry (powrót do wygrywania); dalej niepotwierdzone. W Hongkongu 2025 odpadła w R2 z Mboko w trzech setach.
**H2H:** nieustalone.
**Media:** kontuzji nie stwierdzono; zmęczenie 28 turniejów.
**Ryzyka:** serwis Parks (tie-break loteria), forma Eali w październiku nierówna.
**Rynek:** Pinnacle: Eala 82,6% (fair 1,21); 1. set 75,7%. Moja p niższa o ~8 pp (brak statystyk serwis/return, forma Eali, wariancja Parks); fair 1,33 jest krótkie, graniczne.

### Paula Badosa (57.) - Elena Pridankina (LL) (R1, 03.11 13:00)
**Typ:** Badosa wygra | **p:** 66% | **Fair:** 1,52 | **Pewność:** niska
- Zwycięzca 1. seta: Badosa 61% (1,64).
- Wynik setowy: Badosa 2-0 37% (2,7), Badosa 2-1 29% (3,45), Pridankina 2-1 19% (5,3), Pridankina 2-0 15% (6,7).
**Statystyki:** ranking 57 (+4); Pridankina lucky loser - rozegrała 2 mecze kwalifikacji (wygrana z Gorgodze, porażka z Sakatsume w finale kw.), czyli ma rytm na miejscu i dostała się do drabinki po wycofaniu. Badosa w 2026 uporczywie kontuzjowana (wycofanie Dubaj z biodrem, wycofanie z US Open z powodu pleców; retired w finale Iasi), ale wygrała turniej w Charleston (przełamanie suszy - source: Essentially Sports, termin nieustalony).
**H2H:** nieustalone.
**Media:** nie znaleziono aktualnej informacji o stanie zdrowia Badosy w październiku/listopadzie 2026; ryzyko niepotwierdzonego urazu. Plotki: brak.
**Ryzyka:** nawrót problemów z plecami, brak rytmu (nieustalone czy grała Tokio/Osaka), rytm LL.
**Rynek:** Pinnacle: Badosa 73,9% (fair 1,35); 1. set 68,8%. Moja p niższa o ~8 pp (LL + kontuzjogenność); rozstęp >8 pp -> pewność niska, p z dolnej części.

---
Uwaga: to oszacowania na podstawie ograniczonych danych (brak statystyk sezonu i H2H, p_serve oszacowane), nie gwarancje. Total gemów celowo nie typowany. Żaden mecz nie spełnia wymogów TOP-N (R1, kwalifikantki/LL, brak statystyk).
