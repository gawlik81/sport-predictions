# Liga Mistrzów UEFA 2026/27 — 1. kolejka: TOP 10 typów Value Bet

**Powiązany raport:** pełna analiza wszystkich 18 meczów z modelem Poissona — [LigaMistrzow_kolejka1_2026-09-08_10.md](LigaMistrzow_kolejka1_2026-09-08_10.md)

## Metodologia

Value bet = mecz/rynek, w którym moje prawdopodobieństwo z modelu Poissona jest wyraźnie WYŻSZE niż prawdopodobieństwo implikowane przez realny kurs bukmacherski (1/kurs). Liczę:
- **Edge** = moje % − implikowane % z kursu (w punktach procentowych)
- **Value ratio** = moje % × kurs dziesiętny (>1,05-1,10 = realna przewaga; ~1,0 = mieści się w marginesie bukmachera, czyli szum)

Kursy zebrane 7-8.09.2026 z kilku źródeł (Stake, DraftKings/ESPN, 22bet/1xbet, średnia OddsPortal z 7-8 bukmacherów) — mogą się jeszcze przesunąć do startu meczów.

**Ważne zastrzeżenie:** wysoki value ratio nie zawsze oznacza dobry zakład. Odsiałem z rankingu głównego pozycje, które research oznaczył jako prawdopodobne artefakty, a nie realną przewagę:
- **Como – Leipzig, Leipzig wygrywa (kurs 3,85, ratio 1,53)** — margines bukmacherski w zebranych kursach wyszedł podejrzanie niski (~102% zamiast typowych 105-108%), co sugeruje błąd przy odczycie kursu, nie prawdziwy edge.
- **Bayern – Bodø/Glimt, Under 2,5 gola (kurs 5,90, ratio 1,63)** — rynek wycenia dużo więcej goli Bayernu niż mój model; bardziej prawdopodobne, że to model nie docenia potencjału ofensywnego Bayernu, niż że rynek się myli.
- **PSG – Slovan Bratislava, remis (2,56) i Slovan wygrywa (2,52)** oraz **Barcelona – Feyenoord, Feyenoord wygrywa (2,60-2,99)** — skrajne mismatche, gdzie model Poissona może z kolei NIEDOSZACOWAĆ szansy na "zmiażdżenie" (blowout), co sztucznie zawyża tu szansę remisu/underdoga. To odwrotny mechanizm niż klasyczna wada "zaniżania remisu" i wymaga dodatkowej ostrożności.
- **Manchester United – Sabah, Sabah wygrywa (1,38) i remis (1,35)** — rynek na ten mecz ma bardzo niską płynność (brak notowań O/U 2,5 i BTTS u żadnego z 8 sprawdzonych bukmacherów), co samo w sobie obniża wiarygodność kursów 1X2.

Te pozycje wypisuję osobno na końcu jako "ekstremalne, spekulacyjne" — nie jako rekomendacje.

---

## 🏆 TOP 10 — wiarygodne value bety

| # | Mecz | Typ | Mój % | Kurs | Value ratio | Edge | Uwaga |
|---|------|-----|-------|------|--------------|------|-------|
| 1 | Club Brugge – Aston Villa | **Brugge wygrywa** | 62% | 2,60 | **1,61** | +23,5 pp | ⚠️ Potwierdzone przez 2 niezależnych bukmacherów jako "prawie remis szans" — sprawdź świeże newsy kadrowe Villi przed obstawieniem, skala rozbieżności jest większa niż typowy efekt kalibracyjny |
| 2 | Real Madryt – Inter Mediolan | **Inter wygrywa** | 32% | 5,00 | **1,60** | +12,0 pp | Model ma już wbudowane udokumentowane osłabienia Realu (3 zawieszenia w pomocy) — solidniejsze niż typowy underdog |
| 3 | FC Porto – Manchester City | **Porto wygrywa** | 27% | 5,10 | **1,38** | +7,4 pp | Value na underdogu, nie na faworycie w strefie ryzyka — ryzyko typu "longshot", nie artefakt modelu |
| 4 | Borussia Dortmund – Villarreal | **BTTS – Nie** | 50% | 2,70 | **1,35** | +13,0 pp | Rynek O/U bez wady kalibracyjnej — jeden z najczystszych sygnałów w tej kolejce |
| 5 | AEK Ateny – LASK Linz | **Under 2,5 gola** | 51% | 2,50 | **1,28** | +11,0 pp | Rynek wycenia dużo bardziej ofensywny scenariusz niż model — sprawdź ewentualne kontuzje w ataku AEK |
| 6 | FC Barcelona – Feyenoord | **Over 9,5 rożnych** | 62% | ~2,02 | **1,25** | +12,5 pp | Rynek rożny, niepowiązany z ryzykiem underdoga na 1X2 |
| 7 | VfB Stuttgart – Viking FK | **Viking wygrywa** | 12% | 10,00 | **1,20** | +2,0 pp | Ratio wysoki, ale edge w punktach procentowych cienki — typowe dla longshotów, potraktuj jako spekulację niskiej wagi |
| 8 | PSV Eindhoven – Szachtar Donieck | **Over 2,5 gola** | 56,6% | 2,10 | **1,19** | +9,0 pp | Rynek O/U — model widzi bardziej "otwarty" mecz niż bukmacher |
| 9 | Bayern Monachium – Bodø/Glimt | **BTTS – Nie** | 51,6% | 2,12 | **1,09** | +4,4 pp | Jedyny "czysty" sygnał z tego meczu — reszta rynków (Under 2,5, remis) to ogon rozkładu, patrz zastrzeżenia wyżej |
| 10 | SSC Napoli – Arsenal | **Over 2,5 gola** | 54,2% | 1,98 | **1,07** | +3,7 pp | Skromny, ale czysty edge na rynku O/U |

---

## Runner-up (dodatnie value, ale niżej w rankingu lub z tego samego meczu co pozycja w TOP 10)

- Club Brugge – Aston Villa: przewaga rożna Brugge (kurs 1,94, ratio 1,38) i BTTS-Nie (kurs 2,50, ratio 1,35) — skorelowane z pozycją #1, ten sam sygnał
- Borussia Dortmund – Villarreal: przewaga rożna Dortmund (kurs 1,49, ratio 1,18) i wygrana Dortmundu (kurs 1,79, ratio 1,18, ⚠️ strefa 50-75%)
- Real Madryt – Inter: Over 2,5 gola (kurs 2,20, ratio 1,19), BTTS-Nie (kurs 2,65, ratio 1,14), remis (kurs 4,40, ratio 1,10)
- PSV – Szachtar: BTTS-Nie (kurs 2,35, ratio 1,14)
- FC Porto – Manchester City: przewaga rożna City (kurs 1,60, ratio 1,14)
- LOSC Lille – Real Betis: przewaga rożna Betis (kurs 2,85, ratio 1,14), Over 9,5 rożnych (kurs 1,94, ratio 1,13)
- AEK Ateny – LASK: LASK wygrywa (kurs 4,60, ratio 1,24), BTTS-Nie (kurs 2,43, ratio 1,17)

## Bez value / bez wiarygodnych kursów

**Brak realnego edge na żadnym sprawdzonym rynku:** Liverpool – Atlético Madryt, Sporting CP – Galatasaray, Slavia Praga – RC Lens (rynek i model wyjątkowo zgodne — dobra wiadomość kalibracyjna, nie zła).
**Brak wiarygodnych kursów do porównania:** Fenerbahçe – AS Roma (sprzeczne dane między bukmacherami, sumy prawdopodobieństw wychodziły nierealistyczne — nie zgadywałem).

## Ekstremalne / spekulacyjne (wysoki ratio, ale niska wiarygodność — NIE rekomendacje)

| Mecz | Typ | Kurs | Ratio | Dlaczego pominięte z TOP 10 |
|---|---|---|---|---|
| Barcelona – Feyenoord | Feyenoord wygrywa | 20-23 | 2,60-2,99 | Model może niedoszacowywać szansy "zmiażdżenia" w skrajnym mismatchu |
| PSG – Slovan Bratislava | Remis | 16,00 | 2,56 | j.w. |
| PSG – Slovan Bratislava | Slovan wygrywa | 36,00 | 2,52 | j.w. |
| Como – Leipzig | Leipzig wygrywa | 3,85 | 1,53 | Podejrzany błąd danych (margines bukmacherski ~102%, nietypowo niski) |
| Bayern – Bodø/Glimt | Under 2,5 gola | 5,90 | 1,63 | Rynek widzi realny blowout Bayernu — raczej luka w modelu niż w rynku |
| Man Utd – Sabah | Sabah wygrywa / remis | 20,63 / 9,10 | 1,38 / 1,35 | Rynek bez głębi (brak notowań O/U, BTTS) — niska wiarygodność kursów 1X2 |

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
