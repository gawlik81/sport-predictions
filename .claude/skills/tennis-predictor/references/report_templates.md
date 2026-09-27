# Szablony raportów

Wybierz szablon w zależności od tego, o co poprosił użytkownik. Traktuj je
jako szkielet — jeśli dla danego meczu brakuje jakichś danych (np. statystyki
serwisu per nawierzchnia dla mało znanego zawodnika), zaznacz to wprost
zamiast pomijać sekcję po cichu lub zmyślać liczby.

We wszystkich szablonach poniżej total gemów dostaje pełny model
probabilistyczny (p_a_serve/p_b_serve + uzasadnienie + tabela over/under),
tak jak zwycięzca meczu — patrz `SKILL.md` Krok 4. To priorytet analizy tego
skilla, nie statystyka dodatkowa.

---

## 1. Pojedynczy mecz (typowanie przedmeczowe)

```markdown
# {Zawodnik A} vs {Zawodnik B}
**Turniej:** {nazwa, ranga np. Wielki Szlem/Masters 1000/ATP 250} | **Runda:** {runda} | **Nawierzchnia:** {twarda/mączka/trawa} | **Format:** {best-of-3/best-of-5} | **Termin:** {data, godzina}

## Kontekst i forma
- **Forma {A}** (ostatnie 10-15 meczów): {bilans W-L}, ranking ATP/WTA i
  Elo (ogólny + per nawierzchnia, jeśli dostępny), wynik na tej nawierzchni
  w bieżącym sezonie
- **Forma {B}**: analogicznie
- **Bezpośrednie spotkania (H2H)**: ostatnie starcia, w tym rozbicie per
  nawierzchnia jeśli grali na różnych
- **Kondycja/zmęczenie**: liczba meczów/setów w ostatnich 1-2 tygodniach,
  długość poprzedniego meczu, ewentualna kontuzja lub powrót po przerwie,
  podróż/strefa czasowa
- **Inne czynniki**: motywacja (np. obrona dużej liczby punktów rankingowych,
  pierwszy start po urlopie), zmiana trenera, warunki (kort otwarty/kryty,
  wysokość, wiatr)

## Model bazowy (prawdopodobieństwo wygrania punktu na serwisie)
- Wyjaśnij krótko, jak wyliczone zostały p_a_serve i p_b_serve (siła
  serwisu/returnu względem średniej turowej dla tej nawierzchni, ewentualne
  korekty jakościowe na podstawie kontekstu powyżej)
- p({A} na serwisie) = XX.X%, p({B} na serwisie) = XX.X%

## Prawdopodobieństwa

### Zwycięzca meczu
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| {A} wygrywa | XX% | X.XX |
| {B} wygrywa | XX% | X.XX |

*Uzasadnienie: krótkie wyjaśnienie, dlaczego model i kontekst dają taki rozkład.*

### Dokładny wynik meczu (sety)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| {np. 2-0} | XX% | X.XX |
| {np. 2-1} | XX% | X.XX |
| ... | ... | ... |

### Total gemów i handicap gemowy (sekcja priorytetowa)
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over X.5 gemów | XX% | X.XX |
| Under X.5 gemów | XX% | X.XX |
| Over Y.5 gemów | XX% | X.XX |
| {A} -Z.5 gemów (handicap) | XX% | X.XX |

- Oczekiwana liczba gemów: X.X
- Uzasadnienie: dlaczego model (p_a_serve/p_b_serve) i kontekst (styl gry —
  serwujący vs returner, dominacja serwisu na tej nawierzchni, długość
  potencjalnego meczu) dają taki rozkład — to jedna z najważniejszych sekcji
  raportu, potraktuj ją z takim samym uzasadnieniem jak zwycięzcę meczu.

### Pierwszy set
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| {A} wygrywa 1. set | XX% | X.XX |
| {B} wygrywa 1. set | XX% | X.XX |

Najbardziej prawdopodobne wyniki 1. seta: {np. 6-4, 7-6, 6-3 z prawdopodobieństwami}

### Asy, podwójne błędy, break pointy
- {A}: asy (zakres), podwójne błędy (zakres), oczekiwane przełamania
- {B}: analogicznie
- Krótki komentarz, jeśli któryś zawodnik wyróżnia się serwisem/returnem

### Ryzyko wycofania (jeśli istotne)
- Wspomnij, jeśli research w Kroku 1 wykazał sygnały kontuzji/zmęczenia
  podnoszące ryzyko przerwania meczu

## Podsumowanie
- 2-3 zdania syntezy: gdzie widać największą przewagę któregoś z modeli/rynków
  nad "typowym" oczekiwaniem, na co warto zwrócić uwagę — uwzględnij total
  gemów jako jeden z głównych wątków, obok zwycięzcy meczu, a nie tylko wynik

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady
finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
```

---

## 2. Przegląd dnia turniejowego

Dla każdego meczu danego dnia — skrócona wersja powyższego, bez pełnego
modelu opisowego, skupiona na liczbach. Format tabelaryczny dla szybkiego
przeglądu, plus 1-2 zdania kontekstu tam gdzie jest coś istotnego (kontuzja
gwiazdy, seria zwycięstw, mecz o duże punkty rankingowe). Nawet w tej
skróconej wersji total gemów dostaje własną, wytłuszczoną linijkę z
oczekiwaną wartością i over/under — nie redukuj jej do jednej liczby bez
kontekstu, jak pozostałych statystyk drugorzędnych.

```markdown
# {Turniej} — {dzień/runda} ({data})

## {Zawodnik A} vs {Zawodnik B} ({godzina, kort})
- Forma: {A} {ostatnie wyniki}, {B} {ostatnie wyniki}
- Zwycięzca meczu: {A} XX% / {B} XX% (kursy uczciwe: X.XX / X.XX)
- **Total gemów** (p_serve {A}=XX%, {B}=XX%): oczekiwane ~X.X, Over Y.5 XX%
- Dokładny wynik: najbardziej prawdopodobny {np. 2-0} XX%
- Kontekst: {1-2 zdania, jeśli istotne}

## {Zawodnik C} vs {Zawodnik D} (...)
... (analogicznie dla każdego meczu)

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady
finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
```

---

## 3. Analiza formy zawodnika/zawodniczki (bez konkretnego meczu)

Bez tabel prawdopodobieństw — to analiza opisowa trendów, nie typowanie.

```markdown
# Analiza formy: {Zawodnik/Zawodniczka}

## Okres analizy
{np. ostatnie 10-15 meczów / bieżący sezon}

## Wyniki i trendy
- Bilans: W-L, ranking ATP/WTA i jego zmiana, Elo (ogólny i per nawierzchnia
  jeśli dostępny)
- Trend wyników per nawierzchnia — czy forma jest spójna na wszystkich
  nawierzchniach, czy silnie zależna od jednej

## Statystyki gry
- **Serwis i return (priorytet)**: % punktów wygranych na serwisie i
  returnem, per nawierzchnia jeśli dostępne, i trend w ostatnich meczach
  (rosną/maleją) — to główna statystyka tej sekcji, opisz ją najpełniej
- Asy, podwójne błędy, break pointy wygrane/obronione — średnie i trend

## Kontekst
- Kontuzje, zmiana trenera, kalendarz startów (zagęszczenie turniejów),
  ewentualny powrót po przerwie

## Wnioski
- 2-4 zdania: co się zmieniło, jakie są implikacje na najbliższe turnieje
```

---

## 4. Mecz w ramach Wielkiego Szlema / Masters 1000 (WTA 1000)

Jak szablon "Pojedynczy mecz", plus dodatkowa sekcja na początku:

```markdown
## Stawka meczu
- Runda turnieju, co oznacza wynik dla dalszej drabinki i punktów
  rankingowych każdego zawodnika
- Format meczu (best-of-3 czy best-of-5 — mężczyźni grają best-of-5 tylko
  w Wielkim Szlemie) i aktualny regulamin tiebreaka w secie decydującym
  (zweryfikuj przez research, patrz `references/data_sources.md` — różni
  się między turniejami i sezonami)
- Krótka rekapitulacja dotychczasowych wyników obu zawodników w tym turnieju
  (poprzednie rundy, ewentualne trudne/wyczerpujące mecze wpływające na
  zmęczenie)
- Ewentualna presja/motywacja specyficzna dla rundy (np. pierwszy raz w
  tej fazie Wielkiego Szlema, obrona tytułu, duża liczba punktów do obrony)
```

Reszta raportu jak w szablonie 1. Pamiętaj, że:
- Dla best-of-5 model w Kroku 3 wymaga `--best-of 5` oraz poprawnego
  `--final-set-tiebreak-to` — jeśli turniej to Wimbledon, zaznacz w raporcie,
  że model nie odwzorowuje dokładnie zasady "tiebreak przy 12-12" i podaj
  szerszy przedział niepewności dla scenariuszy z długim, wyrównanym
  ostatnim setem.
- Best-of-5 wydłuża oczekiwaną liczbę gemów znacząco względem best-of-3 —
  warto to explicite skomentować w sekcji total gemów, żeby uniknąć
  nieporozumienia przy porównaniu z innymi meczami.
- Zmęczenie z poprzednich rund (szczególnie po długich meczach 4-5-setowych)
  jest tu istotniejszym czynnikiem korekty p_serve niż przy standardowym
  meczu ATP 250/WTA 250 wcześnie w sezonie.
