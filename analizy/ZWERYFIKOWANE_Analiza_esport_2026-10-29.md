# Analiza e-sport - 29-30.10.2026 (LoL Worlds 2026, Swiss Stage, runda 4)

Zakres zawężony na prośbę użytkownika: tylko wydarzenia po 21:30. KC - CFO (29.10 21:00) pominięty, nie analizowany.

### Top Esports (TES) - Bilibili Gaming (BLG) (Worlds 2026, Swiss R4, bo3, 30.10.2026 00:00 czasu polskiego = 07:00 UTC+8)
**Typ:** BLG wygra serię | **Prawdopodobieństwo:** 70% | **Fair odds:** 1.42 | **Pewność:** średnia

**Stawka meczu:** oba zespoły 2-1, zwycięzca awansuje do ćwierćfinałów.

**Statystyki drużyn:**
- Sezon 2026 (gry): BLG 127-53 (70,6%), TES 78-65 (54,5%) (Strafe).
- Worlds 2026 (gry): obie 2-1 (66,7%). Średni czas gry: TES 29:58, BLG 35:32. Smoki 2,33 na grę u obu; Barony TES 1,0, BLG 0,67.
- Swiss: TES przegrało z Hanwha Life, pokonało Anyone's Legend i G2. BLG przegrało z Movistar KOI, pokonało Team Liquid i Karmine Corp.
- Składy: TES 369 / Tian / Creme / JackeyLove / Zhuo; BLG Bin / Xun / knight / Viper / ON. Kluczowy pojedynek: mid, Creme vs knight, przewaga BLG wg Strafe.

**H2H:** BLG wygrało 3-0 finał Road to MSI 2026 z TES (Strafe). Brak danych o stand-inach po obu stronach, składy podstawowe.

**Informacje medialne:** nie znalazłem doniesień o zmianach składów, chorobach ani problemach z podróżą. Godzina startu różni się w źródłach (Strafe podaje 21:00 lub 23:00 UTC), ale oficjalny wpis BLG: 30.10 07:00 UTC+8. Brak danych o patchu i drafcie (nie znalazłem), co obniża pewność.

**Rynek:** kursy orientacyjne TES 4.00 / BLG 1.25 (Strafe, bez marży ok. 76% BLG). Kalshi BLG 77%, Polymarket 76%. Moje 70,5% jest o ok. 6 pp poniżej rynku: obniżyłem (p gry BLG 0,64) ze względu na to, że w Worlds obie ekipy mają identyczny bilans 66,7% i TES z JackeyLove ma doświadczenie w decydujących seriach; brak konkretnej informacji uzasadniającej większe odejście od rynku. Kurs 1.25 = brak value po mojej wycenie (EV ujemne).

**Model:** `series.py 0.36 --bo 3` (p mapy TES = 0,36, stałe, bez rozbicia na strony, bo draftów nie znamy).

| Rynek | p | Fair odds |
|---|---|---|
| Zwycięzca serii: BLG | 70,5% | 1.42 |
| Zwycięzca serii: TES | 29,5% | 3.38 |
| Wynik 2-0 BLG | 41,0% | 2.44 |
| Wynik 2-1 BLG | 29,5% | 3.39 |
| Wynik 2-1 TES | 16,6% | 6.03 |
| Wynik 2-0 TES | 13,0% | 7.72 |
| Handicap BLG -1.5 | 41,0% | 2.44 |
| Handicap TES +1.5 | 59,0% | 1.69 |
| Handicap BLG +1.5 | 87,0% | 1.15 (graniczne, pomijać w rankingach) |
| Handicap TES -1.5 | 13,0% | 7.72 |
| Total map Over 2.5 | 46,1% | 2.17 |
| Total map Under 2.5 | 53,9% | 1.85 |

**Ryzyka (BLG przegrywa):**
- BLG przegrało z MKOI w pierwszej rundzie; TES w tym Worlds trzyma ten sam bilans, a forma turniejowa jest wyrównana.
- Mecz o awans: wysokie napięcie, zwiększona losowość pojedynczej gry (p gry BLG 0,64, nie 0,70).
- Brak informacji o drafcie, stronach i patchu; możliwy comfort pick TES.
- Dane H2H (3-0 w Road to MSI) to jedna seria; niska waga.

**Ocena:** typ najpewniejszy: BLG wygra serię (70%), ale kurs rynkowy ok. 1.25 jest poniżej fair 1.42, więc bez wartości. Najbardziej wartościowo wygląda TES +1.5 map (fair 1.69, p 59%), o ile bukmacher da kurs > 1.69; do sprawdzenia. Total map blisko 50/50: brak mocnego typu.

Źródła: [Strafe preview](https://www.strafe.com/esports-betting/news/lol-worlds-2026-swiss-4-predictions-top-esports-vs-bilibili-gaming/), [Sheep Esports](https://x.com/Sheep_Esports/status/2114854556068970832), [BLG na X](https://x.com/BilibiliGaming/status/2115760566140829875), [Liquipedia Swiss Stage](https://liquipedia.net/leagueoflegends/World_Championship/2026/Swiss_Stage), [Strafe Day 4](https://www.strafe.com/news/read/worlds-2026-swiss-stage-day-4-lpls-top-seed-exits-winless-as-los-survives/).

To są oszacowania, nie gwarancje.
