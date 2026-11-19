# Urawa Red Diamonds - Cerezo Osaka (Puchar J. League, 11.11.2026, 11:30 czasu PL)

Event Superbet 15721414. Analiza szybka (start za ok. 50 min), bez wariantów kadrowych. Źródła: connector superbet (kursy, składy oficjalne, H2H, forma, sędzia, średnie sezonu); rezerwa nie była używana. Brak danych w connectorze: nieobecni ("Brak danych"), xG, statystyki sędziego Jumpei Iidy.

## Dane
- **Składy oficjalne.** Urawa 4-1-4-1 (Jo): Arai; Danilo Junior, Miyamoto, Kudo, Naganuma; Seko; Hidano, Minamino, Ueki, Hayakawa; Onaiwu. Na ławce m.in. Nishikawa, Savio, Gustafsson, Kaneko (część ofensywy poza XI). Cerezo 3-4-2-1 (Machin): Abe; Cools, Takahashi, Hernandez; Nakamura, Okazawa, Tanaka, Sakata; Fernandes, Komi; Uejo.
- **Sędzia:** Jumpei Iida (statystyk kartek nie sprawdzano, rynków kartek i fauli nie wyceniam).
- **Forma Urawy (6 meczów, ostatni pierwszy):** 2:2 Kobe, 0:4 w Kashiwie (czerwona), 1:0 Nagasaki, 3:2 JEF, 1:0 Mito, 4:0 Yokohama FC. Strzelone 11, stracone 8 (1,8 / 1,3 na mecz); strzeliła w 5 z 6.
- **Forma Cerezo:** 3:2 w Gamba, 1:4 w Kashimie, 3:1 w Mito, 2:2 JEF, 1:1 Nagoya, 2:4 z Kawasaki. Strzelone 12, stracone 14 (2,0 / 2,3 na mecz); strzeliło w 6 z 6.
- **Średnie sezonu (connector, mała próba):** gole strzelone Urawa 3,0 / Cerezo 2,7, stracone 1,0 / 1,3; rożne 5,0 / 4,3 na mecz.
- **H2H** (od 2023): 0:0, 1:1, 0:1, 1:2, 0:2, 2:1 z perspektywy gospodarza; średnio 1,5 gola, ale to inne składy i trenerzy, więc waga niska.

## Wycena (poisson.py)
λ Urawa 1,70, λ Cerezo 1,25 (suma 2,95; rynek ok. 3,0-3,1). Czułość: 1,5/1,1 oraz 1,9/1,4. Obie drużyny mają otwartą defensywę, więc nie schodzę pod rynek.

| Rynek | p (zakres) | fair | kurs Superbet | EV (środek) |
|---|---|---|---|---|
| 1 / X / 2 | 48% / 24% / 28% | 2.09 / 4.19 / 3.55 | 1.88 / 3.65 / 3.65 | -10% / -13% / ok. +3% |
| BTTS tak | 58% (52-64%) | 1.71 | 1.53 | -11% (zakres -21% do -2%) |
| Over 2.5 | 57% (48-64%) | 1.77 | 1.58 | -11% (zakres -24% do +1%) |
| Over 1.5 | 79% | 1.26 | 1.17 | -7% |
| Over 2.5 i BTTS tak | 47% (40-54%) | 2.12 | 1.87 | -12% |
| 12 i Over 2.5 | 49% | 2.04 | 1.69 | -17% |
| 1X | 72% | 1.39 | 1.24 | -11% |

**Pewność:** średnia dla rynków goli (składy oficjalne, rynek i forma zgodne), niska dla wyniku 1X2 (brak mocnego typu, Urawa ok. 48%) oraz dla kartek, fauli i rożnych (brak danych o sędzi i próbie).

## Ryzyka
Puchar z możliwą rotacją (Urawa bez części ofensywy w XI). Jedna z drużyn może zostać bez gola: Urawa nie strzeliła w Kashiwie, Cerezo ma najgorszą obronę z tej pary. Czułość pokazuje, że przy niższych λ (1,5/1,1) żaden gol-rynek nie ma przewagi.

## Wniosek
Brak kuponu z EV > 0 (najlepszy: Over 2.5 w wariancie wysokim, +1%). Wariant awaryjny: **BTTS tak** (najwyższe p w kursie 1.5-2.5, pewność średnia), p ok. 58% (52-64%), kurs 1.53, EV ok. -11%. Przewaga bukmachera jest po jego stronie. To oszacowania probabilistyczne, nie gwarancje.
