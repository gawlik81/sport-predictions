# Szablony raportów

Wybierz szablon w zależności od prośby. Traktuj je jako szkielet: jeśli
brakuje danych (np. statystyk stron dla drużyny tier-2), zaznacz to wprost
zamiast pomijać sekcję po cichu lub zmyślać liczby.

We wszystkich szablonach **handicap mapowy** i (w CS2) **total rund**
dostają pełny model, tak jak zwycięzca serii. To priorytet tego skilla,
nie statystyka dodatkowa.

---

## 1. Pojedynczy mecz (seria)

```markdown
# {Drużyna A} vs {Drużyna B} — {gra}
**Turniej:** {nazwa, tier} | **Faza:** {grupa/Swiss/playoff, runda} | **Format:** {BO1/BO2/BO3/BO5, ewentualny advantage} | **LAN/online** | **Patch/pula map:** {patch LoL/Dota lub active duty CS2} | **Termin:** {data, godzina}

## Składy i kontekst
- **Skład {A}**: piątka, ewentualny stand-in/świeża zmiana, trener
- **Skład {B}**: analogicznie
- **Forma {A}** (ostatnie 10-15 serii): bilans serii i map, ranking/rating,
  wyniki z LAN-ów vs online, poziom rywali
- **Forma {B}**: analogicznie
- **H2H**: ostatnie serie (z adnotacją o zmianach składów od tego czasu)
- **Inne czynniki**: stawka, podróż/jet lag, kalendarz, patch, motywacja

## Model bazowy (p_map)
- Skąd wziął się punkt wyjścia (rating Elo/Glicko, ranking, bilans map)
- Zastosowane korekty (skład, patch, LAN, przerwa, kryzys) z krótkim
  uzasadnieniem i wielkością w pp
- **CS2:** przewidywane veto i p_map per mapa:

| Mapa | Kto wybiera | Win rate {A} / {B} (3 mies.) | p_map {A} |
|---|---|---|---|
| {mapa 1} | pick {A} | XX% (n) / XX% (n) | XX% |
| {mapa 2} | pick {B} | ... | XX% |
| {decider} | decider | ... | XX% |

- **LoL/Dota:** p_gry {A} = XX% (plus uwagi o stronie, drafcie, fearless)

## Prawdopodobieństwa

### Zwycięzca serii
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| {A} wygrywa | XX% | X.XX |
| {B} wygrywa | XX% | X.XX |
| Remis 1-1 (tylko BO2) | XX% | X.XX |

*Uzasadnienie: dlaczego model i kontekst dają taki rozkład. Przy 50-85%
wymień główny scenariusz niespodzianki.*

### Dokładny wynik serii
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 2-0 | XX% | X.XX |
| 2-1 | XX% | X.XX |
| ... | ... | ... |

### Handicap mapowy i total map (sekcja priorytetowa)
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| {A} -1.5 map | XX% | X.XX |
| {B} +1.5 map | XX% | X.XX |
| Over 2.5 map | XX% | X.XX |
| Under 2.5 map | XX% | X.XX |

### CS2: total rund i handicap rundowy per mapa (sekcja priorytetowa)
| Mapa | p rundy {A} (CT/T) | Oczekiwane rundy (po korekcie) | Over 21.5 | Under 21.5 | {A} -3.5 rundy | Dogrywka |
|---|---|---|---|---|---|---|
| {mapa 1} | XX%/XX% | ~XX.X | XX% (X.XX) | XX% (X.XX) | XX% (X.XX) | XX% |
| {mapa 2} | ... | ... | ... | ... | ... | ... |
| {decider} (gra się z p=XX%) | ... | ... | ... | ... | ... | ... |

- Uzasadnienie: strony CT/T obu drużyn, siła pistoletówek, styl (wyrównane
  vs jednostronne mapy), korekta na ekonomię z SKILL.md Krok 4 pkt 3.

### LoL/Dota: kille i czas gry
| Rynek (na grę) | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over X.5 killi | XX% | X.XX |
| Under X.5 killi | XX% | X.XX |
| Czas gry Over XX.5 min | XX% | X.XX |

- Oczekiwane kille: ~XX (przedział XX-XX); oczekiwany czas: ~XX min
- Opcjonalnie: first blood / first dragon / first Roshan

### Gracze (jeśli użytkownik pyta)
- {gracz}: oczekiwane kille na mapę/serię, przedział, O/U

## Podsumowanie
- 2-3 zdania: gdzie model widzi największą przewagę, na co uważać (skład,
  veto, patch). Uwzględnij handicap mapowy i total rund jako główne wątki
  obok zwycięzcy serii.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady
finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
```

---

## 2. Przegląd dnia turnieju

Skrócona wersja per seria, skupiona na liczbach, plus 1-2 zdania kontekstu
tam, gdzie jest coś istotnego (stand-in, seria porażek, mecz o awans).
Nawet w wersji skróconej handicap mapowy i (w CS2) total rund dostają
własną linijkę.

```markdown
# {Turniej} — {gra}, {dzień/faza} ({data})

## {A} vs {B} ({godzina}, {format})
- Forma/skład: {1 linijka}
- Zwycięzca serii: {A} XX% / {B} XX% (kursy uczciwe: X.XX / X.XX)
- **Handicap/total map:** {A} -1.5 XX% (X.XX), Over 2.5 map XX%
- **CS2 total rund** (mapa 1 {nazwa}, p_map {A}=XX%): oczekiwane ~XX.X, Over 21.5 XX%
- **LoL/Dota:** kille/grę ~XX, Over XX.5 XX%; czas ~XX min
- Kontekst: {1-2 zdania, jeśli istotne}

## {C} vs {D} (...)
...

## Ranking najlepszych typów dnia (opcjonalnie)
| # | Mecz | Typ | Prawd. | Kurs uczciwy | Uwagi |
|---|---|---|---|---|---|
| 1 | ... | ... | XX% | X.XX | ... |

(Tylko typy z fair odds >1.15; bez totali opartych na szacunkach z
rankingu, patrz SKILL.md Krok 2b.)

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady
finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
```

---

## 3. Analiza formy drużyny/gracza (bez konkretnego meczu)

Bez tabel prawdopodobieństw. To analiza opisowa trendów, nie typowanie.

```markdown
# Analiza formy: {drużyna/gracz} ({gra})

## Okres analizy
{np. ostatnie 3 miesiące / bieżący split / od ostatniego patcha}

## Wyniki i trendy
- Bilans serii i map, ranking/rating i jego zmiana, wyniki LAN vs online
- Najważniejsze turnieje w okresie i osiągnięte miejsca

## Statystyki gry
- **CS2:** pula map (win rate, stałe bany/picki), strony CT/T, pistoletówki,
  kluczowi gracze (rating, ADR)
- **LoL:** GD@15, strona blue/red, obiektywy, czas gry, pule bohaterów
- **Dota:** Radiant/Dire, czas gry, styl draftu, kluczowi bohaterowie

## Kontekst
- Zmiany składu, trenera, patch/pula map, kalendarz, bootcampy

## Wnioski
- 2-4 zdania: co się zmieniło i co to oznacza na najbliższe turnieje
```

---

## 4. Mecz fazy pucharowej / finał dużego turnieju

Jak szablon 1, plus sekcja na początku:

```markdown
## Stawka meczu
- Faza turnieju, co oznacza wynik (awans, eliminacja, pula nagród, punkty
  do rankingu/kwalifikacji)
- Format zweryfikowany na Liquipedii (BO3/BO5, advantage w wielkim finale,
  fearless draft, zasady wyboru strony/mapy)
- Droga obu drużyn w turnieju (dolna/górna drabinka, liczba rozegranych
  map, zmęczenie)
- Doświadczenie w dużych finałach, presja areny
```

Pamiętaj, że:
- BO5 wzmacnia przewagę faworyta mocniej niż BO3 (SKILL.md Krok 3), więc
  błąd w p_map rośnie; uzasadnij p_map szczególnie starannie.
- W CS2 BO5 veto zostawia więcej map "komfortowych" dla obu drużyn;
  pokaż p_map dla wszystkich 5 map i `p_map_played`.
- Przy advantage 1-0 dla drużyny z górnej drabinki licz serię od tego stanu
  (np. do 3 wygranych przy 1-0 to dla faworyta "BO5 z mapą w zapasie") i
  zaznacz to w raporcie.
