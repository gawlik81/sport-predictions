# Value — niedziela, 27.09.2026 (piłka, tenis i e-sport; kursy Betclic ok. 09:40)

Użyte skille: football-predictor, tennis-predictor i esports-predictor.

**EV** = p (konserwatywne) × kurs Betclic. Value oznacza EV > 1.

## Rozliczenie wczorajszych typów tenisowych (Laver Cup)

| Typ | Wynik | Status |
|---|---|---|
| de Minaur +1,5 seta | de Minaur wygrał z Zverevem 2-6 7-6(5) 11-9 | ✅ |
| Fritz +1,5 seta | Fritz przegrał z Alcarazem 3-6 6-4 11-13 (miał 2 piłki meczowe) | ✅ |

Model dobrze wycenił zbyt krótkie kursy na faworytów w Laver Cup.

## 5 typów

| # | Dyscyplina | Mecz (godz.) | Typ | Model | Konserw. | Fair | Betclic | EV |
|---|---|---|---|---|---|---|---|---|
| 1 | Piłka (LN D1) | Gibraltar – Andora (18:00) | **1 (Gibraltar)** | 41,1% | ~35% | 2,86 | 3,55 | 1,24 |
| 2 | Tenis (Laver Cup) | Jodar – Fritz (ok. 16:30) | **Fritz +1,5 seta** | 90,0% | ~84% | 1,19 | 1,27 | 1,07 |
| 3 | Piłka (LN A2) | Serbia – Holandia (18:00) | **1X** | 43,7% | ~38% | 2,63 | 2,75 | 1,05 |
| 4 | Tenis (Laver Cup) | Zverev – Tien (ok. 14:10) | **Tien +1,5 seta** | 64,0% | ~58% | 1,72 | 1,79 | 1,04 |
| 5 | Tenis (ATP Chengdu QF) | Mannarino – Shapovalov (10:00) | **Over 20,5 gema** | 67,9% | ~65% | 1,54 | 1,57 | 1,02 |

**Bezpieczniejsza wersja #1:** Gibraltar 1X @1,53. Model daje 72,1%, a wersja konserwatywna ok. 66%, co daje EV 1,01-1,10.

## Uzasadnienie

1. **Gibraltar – Andora.**
   - Gibraltar nie przegrał 3 meczów (8:1 w bramkach). W H2H ma 2 wygrane i 1 remis, zawsze z czystym kontem.
   - Andora zdobywa średnio ok. 0,4 gola na mecz. Dwa dni temu przegrała 1-2 z Maltą, mimo że prowadziła, i może rotować składem z powodu zmęczenia.
   - Rynek wycenia Andorę na ok. 40%, a model na 28%. Rozjazd przekracza 10 pp, prawdopodobnie przez wyższe miejsce Andory w rankingu, dlatego obciąłem p Gibraltaru.
   - λ: 1,10 : 0,85.
2. **Fritz +1,5 seta.**
   - Model na danych z Tennis Abstract (twarda) liczy p_serve 0,676 dla Fritza i 0,618 dla Jodara; Fritz wygrywa w nim w 76,2%.
   - Obcięcie o 6 pp: Fritz gra dziś najpierw debla (z de Minaurem), a wczoraj rozegrał super tie-break do 13-11.
   - **Ryzyko zwrotu:** jeśli Europa, która prowadzi 7-5, wygra debla i mecz Zverev–Tien, osiągnie 15 pkt i zakończy Laver Cup. Kolejne mecze nie zostaną rozegrane, a zakład zostanie zwrócony.
3. **Serbia – Holandia, 1X.**
   - Serbia gra bez Vlahovicia i Ivanovicia i przegrała 1-2 z Grecją.
   - Holandii prawdopodobnie zabraknie Brobbeya (uraz), niepewny jest też Timber. Holandia zremisowała 1-1 z Niemcami.
   - Model daje Holandii 56%, a rynek ok. 67%. Rozjazd przekracza 10 pp, a zgodnie z regułą 6 w meczach o różnicy klas rynek bywa trafniejszy, więc obciąłem p do ~38%.
   - λ: 0,90 : 1,70. Obcięcie Serbii ograniczyłem do 15% (reguła 5).
4. **Tien +1,5 seta.**
   - Model daje Zverevowi 64,8% (p_serve 0,665 : 0,634), a rynek (2-0 @1,92) ok. 50% na wygraną w dwóch setach.
   - Tien pokonał wczoraj Cobolliego. Zverev przegrał z de Minaurem, a potem grał jeszcze debla.
   - H2H 2-1 dla Zvereva.
5. **Mannarino – Shapovalov, Over 20,5.**
   - Model oczekuje 24,7 gema (p_serve 0,608 : 0,664, dane z Tennis Abstract).
   - Obcięcie o ~3 pp za ekonomię wymian (break w serii).
   - Kurs na zwycięzcę jest zgodny z modelem (Shapovalov 75,7% wobec 75,8% w kursie 1,32), więc value leży tylko w totalu.

## Bez value (sprawdzone)

| Mecz | Model | Betclic | EV |
|---|---|---|---|
| Norwegia – Portugalia | O2,5 56,5%, BTTS 59,3% | 1,45 / 1,42 | 0,82 / 0,84 |
| Izrael – Irlandia (Debreczyn) | 1X 64,8%, X2 62,4% | 1,46 / 1,45 | 0,95 / 0,90 |
| Austria – Kosowo | Kosowo 19,8% | 5,25 | 1,04 (za mało) |
| Litwa – Azerbejdżan, Dania – Walia, Niemcy – Grecja | model zgodny z rynkiem | — | ≤1,07 przy p <20% |
| Alcaraz – de Minaur | de Minaur +1,5 seta 39%, konserw. ~33% | 3,20 | 1,06, ale niskie p i zmęczenie de Minaura |

**Tenis poza typami:** Rublev – Gaston oraz Muller – Davidovich Fokina (brak danych Davidovicha na twardej) nie weszły. Finał WTA Seul prawdopodobnie już trwa.

## E-sport — brak value

- **CS2 i Dota 2:** Betclic nie ma dziś meczów.
- **LCS, Cloud9 – Team Liquid (22:00, BO5, finał górnej drabinki playoffów, stawka: awans na Worlds).**
  - Liquid wygrał 5-0 w mapach w dwóch ostatnich seriach z C9.
  - Rynek wycenia pojedynczą mapę dla C9 na @2,15 (~43%), a model na p_map 0,42.
  - Wyceny są zgodne: C9 +1,5 @1,65 przy 55,9% (EV 0,92) i C9 +2,5 @1,20 przy 80,5% (EV 0,97).
- **CBLOL i EMEA Masters:** tier-2, bez danych (reguły 7-8). WSCI to akademie.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
