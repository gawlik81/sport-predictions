# TOP 12 najpewniejszych predykcji weekendu — 19-20.09.2026

Zestawienie z 6 równoległych analiz (football-predictor + tennis-predictor) obejmujących
Premier League, Bundesligę, LaLiga, Serie A, Ligue 1, Ekstraklasę i WTA 250 São Paulo.
Każda liga przeszła najpierw triaż (odrzucenie wyrównanych meczów), a dopiero wytypowani
kandydaci dostali pełny model (Poisson/hierarchiczny + rożne/total gemów + korekty
kalibracyjne z Kroku 2b/5 obu skilli). Filtr z pamięci — **fair odds >1,15** — zastosowany;
żaden z 18 przeanalizowanych meczów nie musiał zostać wykluczony z tego powodu.

Kryterium "najpewniejszy" = pewność przypisana przez model PO korektach jakościowych
(Wysoka > Średnia/Wysoka > Średnia), nie surowe %. Tam gdzie agent wprost odradził
traktowanie meczu jako "pewniaka" (patrz sekcja niżej), mecz nie wszedł do rankingu
mimo formalnie sensownego %.

## Ranking

| # | Mecz | Rozgrywki | Typ | Prawd. | Kurs (fair) | Pewność |
|---|------|-----------|-----|--------|-------------|---------|
| 1 | Getafe – Málaga | LaLiga | Getafe 1X | 83,6% | 1,20 | Wysoka |
| 2 | Sevilla – Barcelona | LaLiga | Barcelona X2 | 83,5% | 1,20 | Średnia/Wysoka |
| 3 | Nice – Lille | Ligue 1 | Lille X2 | 82,6% | 1,21 | Średnia/Wysoka |
| 4 | Leeds United – Crystal Palace | Premier League | Over 1,5 gola | 80,1% | 1,25 | Średnia/Wysoka |
| 5 | Badosa [2] – Podoroska | WTA São Paulo (PF) | Badosa wygrywa | 78,5% | 1,27 | Wysoka/Średnia |
| 6 | Lech Poznań – Radomiak Radom | Ekstraklasa | Lech wygrywa | 76,1% | 1,31 | Wysoka |
| 7 | Manchester City – Sunderland | Premier League | City wygrywa | 70,6% | 1,42 | Wysoka |
| 8 | AC Milan – Lecce | Serie A | Milan wygrywa | 70,6% | 1,42 | Wysoka |
| 9 | Hamburger SV – Köln | Bundesliga | Köln wygrywa | 69,5% | 1,44 | Średnia/Wysoka |
| 10 | Motor Lublin – Górnik Zabrze | Ekstraklasa | Górnik wygrywa | 67,5% | 1,48 | Wysoka/Średnia |
| 11 | Auxerre – Brest | Ligue 1 | Over 1,5 gola | 84,1% | 1,19 | Średnia/Wysoka (rynek bramkowy) |
| 12 | Frosinone – Como | Serie A | Como wygrywa | 61,8% | 1,62 | Średnia |

**#11-12 to najlepsi kandydaci "z drugiego szeregu"** — dodani na wyraźną prośbę, poniżej
progu jakości reszty rankingu:
- **Auxerre – Brest** ma najwyższe surowe % z całej puli (84,1%), ale to typ na total goli, nie
  na zwycięzcę — sam 1X2 jest płaski (34%/23%/43%, brak faworyta), więc mecz świadomie nie
  trafił do głównej dziesiątki mimo wysokiej liczby.
- **Frosinone – Como**: Como niepokonane i w dobrej formie, ale Frosinone to normalny,
  nie kryzysowy underdog (7 pkt, ostatnio wygrało 3-0 u Fiorentiny) — przewaga jest realna,
  tylko mniejsza niż w pierwszej dziesiątce, stąd Średnia, nie Wysoka pewność.

## Dlaczego akurat te, a nie wyższe surowe %

- **Getafe i Sevilla/Barcelona** grają typami podwójnej szansy (1X/X2), nie czystym "1"/"2" —
  Málaga i Sevilla to strony z realną historią psucia faworytom (Sevilla ma udokumentowany
  "hoodoo" na Barçę na własnym stadionie), więc podwójna szansa jest bezpieczniejszym,
  a wciąż bardzo prawdopodobnym typem.
- **Leeds–Palace** typowany przez total goli (80,1%), nie 1X2 (62,3%) — Palace ma najgorszą
  obronę ligi, ale to osłabienie kadrowe, nie kryzys morale, więc czysty typ na Leeds byłby
  mniej pewny niż rynek bramkowy.
- **Lech Poznań** świadomie obniżony z surowych ~85%+ do 76,1% (2 porażki z rzędu, niepewna
  kadra).
- **Venezia–Lazio (66%)** i **Gladbach–Mainz (60%)** NIE weszły do rankingu mimo przyzwoitych
  liczb — oba to podręcznikowe przypadki kryzysowego underdoga (zwolniony trener / gra
  "o posadę") z Kroku 2b kalibracji, gdzie historyczna weryfikacja skilla pokazała najwięcej
  niespodzianek.

## Świadomie pominięte mimo obecności w analizie

- **Nottingham Forest – Coventry City** (55,5%) — Coventry w realnym kryzysie (0 pkt, 0 goli),
  ale Forest sam gra osłabioną obroną; agent odradził traktowanie jako pewniaka.
- **Deportivo – Betis** — tabela sugerowała faworyta Betisu, ale dane indywidualne
  (Aubameyang strzela w każdym meczu Deportivo) neutralizują przewagę; brak wyraźnego
  faworyta, tylko Over 1,5 gola (59,4%).
- **Blinkova – Quevedo** (WTA PF, 60,4%) — mecz dwóch zawodniczek w identycznej formie i
  rankingu; zbyt wyrównany na "pewniaka".
- **Stuttgart – Dortmund** (59,5%) — najsłabszy z przeanalizowanych typów Bundesligi, bez
  szczególnego uzasadnienia by wyprzedzić #12.

## Uwaga o finale WTA São Paulo

Finał (niedziela) nie ma jeszcze ustalonej pary w momencie analizy — oba półfinały
(Badosa–Podoroska, Blinkova–Quevedo) rozgrywają się dopiero w sobotę. Brak analizy finału,
żeby nie zgadywać przeciwników.

## Źródła (pełne raporty)

`PremierLeague_ManCity_Sunderland_2026-09-20.md`, `PremierLeague_Leeds_CrystalPalace_2026-09-20.md`,
`PremierLeague_NottinghamForest_Coventry_2026-09-19.md`, `Bundesliga_HSV_Koln_2026-09-19.md`,
`Bundesliga_Stuttgart_Dortmund_2026-09-19.md`, `Bundesliga_Gladbach_Mainz_2026-09-19.md`,
`Nice_Lille_2026-09-20.md`, `Auxerre_Brest_2026-09-20.md`, `Getafe_Malaga_2026-09-20.md`,
`Sevilla_Barcelona_2026-09-19.md`, `Deportivo_Betis_2026-09-20.md`, `Frosinone_Como_2026-09-20.md`,
`Venezia_Lazio_2026-09-19.md`, `Milan_Lecce_2026-09-20.md`,
`Ekstraklasa_kolejka9_Motor_Gornik_2026-09-19.md`, `Ekstraklasa_kolejka9_Lech_Radomiak_2026-09-19.md`,
`SaoPaulo_2026_Polfinal_Badosa_Podoroska_2026-09-19.md`, `SaoPaulo_2026_Polfinal_Blinkova_Quevedo_2026-09-19.md`

---

*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej
ani zachęty do zakładów. Graj odpowiedzialnie.*
