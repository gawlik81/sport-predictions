# Szablony raportów

Wybierz szablon w zależności od tego, o co poprosił użytkownik. Traktuj je
jako szkielet — jeśli dla danego meczu brakuje jakichś danych (np. statystyki
rożnych dla mniej popularnej ligi), zaznacz to wprost zamiast pomijać sekcję
po cichu lub zmyślać liczby.

We wszystkich szablonach poniżej rożne mają dostać pełny model probabilistyczny
(λ + uzasadnienie + tabela przewagi/over-under), tak jak gole — patrz
`SKILL.md` Krok 4. To priorytet analizy tego skilla, nie statystyka
dodatkowa.

---

## 1. Pojedynczy mecz (typowanie przedmeczowe)

```markdown
# {Drużyna A} vs {Drużyna B}
**Rozgrywki:** {liga/puchar/turniej} | **Termin:** {data, godzina} | **Ranga meczu:** {np. walka o mistrzostwo, środek tabeli, derby, mecz o utrzymanie}

## Kontekst i forma
- **Forma {A}** (ostatnie 5 meczów): {wyniki, np. W-W-D-L-W}, gole strzelone/stracone, xG/xGA jeśli dostępne
- **Forma {B}**: analogicznie
- **Bezpośrednie spotkania (H2H)**: ostatnie 3-5 meczów, wynik i kontekst
- **Kadra**: kontuzje, zawieszenia, kluczowi gracze do gry/poza grą
- **Inne czynniki**: motywacja (np. walka o LM, nic do grania), zmęczenie
  (mecze co 3 dni), zmiana trenera, czynniki pogodowe/boiskowe jeśli istotne

## Model bazowy (oczekiwane gole)
- Wyjaśnij krótko, jak wyliczone zostały lambda_home i lambda_away
  (siła ataku/obrony względem średniej ligowej, korekta dom/wyjazd,
  ewentualne korekty jakościowe na podstawie kontekstu powyżej)
- λ({A}) = X.XX, λ({B}) = Y.YY

## Model rożnych (priorytet analizy — patrz SKILL.md Krok 4)
- Wyjaśnij krótko, jak wyliczone zostały lambda_rożne_home i
  lambda_rożne_away (siła rożna ataku/obrony względem średniej ligowej,
  korekta dom/wyjazd, korekty jakościowe — styl gry skrzydłami, pressing,
  blok defensywny generujący rożne przeciwnika)
- λ_rożne({A}) = X.XX, λ_rożne({B}) = Y.YY

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| {A} wygrywa | XX% | X.XX |
| Remis | XX% | X.XX |
| {B} wygrywa | XX% | X.XX |

*Uzasadnienie: krótkie wyjaśnienie, dlaczego model i kontekst dają taki rozkład.*

### Rożne — przewaga i over/under (sekcja priorytetowa)
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| {A} więcej rożnych | XX% | X.XX |
| Remis rożny (tyle samo) | XX% | X.XX |
| {B} więcej rożnych | XX% | X.XX |
| Over 8.5 | XX% | X.XX |
| Over 9.5 | XX% | X.XX |
| Over 10.5 | XX% | X.XX |

- {A}: oczekiwane rożne λ = X.XX (realny zakres ~XX-XX)
- {B}: oczekiwane rożne λ = X.XX (realny zakres ~XX-XX)
- Łącznie: oczekiwana wartość λ_rożne({A}) + λ_rożne({B}) i realny zakres

*Uzasadnienie: dlaczego model (siła rożna ataku/obrony) i kontekst (styl gry,
dom/wyjazd, ewentualne korekty jakościowe) dają taki rozkład — to jedna z
najważniejszych sekcji raportu, potraktuj ją z takim samym uzasadnieniem jak
1X2.*

### Najbardziej prawdopodobne wyniki (gole)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| ... | ... | ... |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1.5 | XX% | X.XX |
| Over 2.5 | XX% | X.XX |
| Over 3.5 | XX% | X.XX |
| BTTS - Tak | XX% | X.XX |
| BTTS - Nie | XX% | X.XX |

*Uzasadnienie.*

### Strzały i strzały celne
- {A}: strzały (zakres), strzały celne (zakres)
- {B}: analogicznie
- Krótki komentarz, jeśli któraś drużyna wyróżnia się skutecznością/objętością gry

### Faule i kartki (drużynowo i indywidualnie — patrz SKILL.md Krok 6)
**Drużynowo:**
- {A}: faule popełnione (zakres, średnio ~X.X/mecz), żółte kartki (zakres),
  ryzyko czerwonej (jeśli istotne)
- {B}: analogicznie
- Łącznie fauli w meczu: przedział + średnia; kartki: przedział + średnia
  (uwzględniając styl sędziego, jeśli ta informacja jest dostępna)

**Indywidualnie (kluczowi zawodnicy):**
- Najczęściej faulujący: {zawodnik A1} (X.X faula/90), {zawodnik B1}
  (X.X faula/90) — podwyższone ryzyko kartki
- Najczęściej faulowani: {zawodnik A2}, {zawodnik B2} — potencjalne źródło
  rzutów wolnych w groźnych strefach dla ich drużyn
- Zawodnicy na progu zawieszenia (jeśli dotyczy): {zawodnik}, X. żółta
  kartka w sezonie, zawieszenie przy Y — ryzyko asekuracyjnej gry lub
  wcześniejszej zmiany
- Jeśli powyższe wpłynęło na korektę λ w modelu bazowym (Krok 2), krótko
  przypomnij to tutaj zamiast zostawiać jako osobny, niepowiązany fakt

### Inne istotne statystyki (opcjonalnie)
- Np. spalone, posiadanie piłki, rzuty wolne — tylko jeśli wnoszą coś do analizy
  tego konkretnego meczu

## Podsumowanie
- 2-3 zdania syntezy: gdzie widać największą przewagę któregoś z modeli/rynków
  nad "typowym" oczekiwaniem, na co warto zwrócić uwagę — uwzględnij rożne
  jako jeden z głównych wątków, obok wyniku meczu, a nie tylko gole

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady
finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
```

---

## 2. Przegląd kolejki ligowej

Dla każdego meczu w kolejce — skrócona wersja powyższego, bez pełnego
modelu opisowego, skupiona na liczbach. Format tabelaryczny dla szybkiego
przeglądu, plus 1-2 zdania kontekstu tam gdzie jest coś istotnego (kontuzja
gwiazdy, seria bez porażki, mecz o stawkę). Nawet w tej skróconej wersji
rożne dostają własną, wytłuszczoną linijkę z λ obu drużyn i pełnym rozkładem
(przewaga/remis/over-under) — nie redukuj ich do jednej liczby "łącznie",
jak pozostałych statystyk drugorzędnych.

```markdown
# {Liga} — Kolejka {N} ({daty})

## {Drużyna A} vs {Drużyna B} ({data, godzina})
- Forma: {A} {W-W-D}, {B} {L-W-D}
- 1X2: {A} XX% / Remis XX% / {B} XX% (kursy uczciwe: X.XX / X.XX / X.XX)
- **Rożne** (λ_rożne {A}=X.X, {B}=X.X): przewaga {A} XX% / remis rożny XX% /
  przewaga {B} XX%, łącznie ~X.X, Over 9.5 XX%
- Gole: Over 2.5 XX%, BTTS XX%
- Faule: ~X.X (łącznie) {+ jednym zdaniem, jeśli istotne: zawodnik na progu
  zawieszenia lub drużyna z wysokim ryzykiem czerwonej kartki}
- Kontekst: {1-2 zdania, jeśli istotne}

## {Drużyna C} vs {Drużyna D} (...)
... (analogicznie dla każdego meczu)

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady
finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
```

---

## 3. Analiza formy drużyny / zawodnika (bez konkretnego meczu)

Bez tabel prawdopodobieństw — to analiza opisowa trendów, nie typowanie.

```markdown
# Analiza formy: {Drużyna / Zawodnik}

## Okres analizy
{np. ostatnie 10 meczów / bieżący sezon}

## Wyniki i trendy
- Bilans: W-D-L, gole strzelone/stracone, punkty na mecz
- Trend xG/xGA jeśli dostępny — czy wyniki odpowiadają jakości gry, czy
  drużyna ma "szczęście"/"pecha" (rozjazd między wynikami a xG)
- Domowe vs wyjazdowe rozbicie, jeśli relevantne

## Statystyki gry
- **Rożne (priorytet)**: średnia zdobytych/oddanych, rozbicie dom/wyjazd
  jeśli dostępne, i trend w ostatnich meczach (rosną/maleją) — to główna
  statystyka tej sekcji, opisz ją najpełniej
- Strzały, strzały celne — średnie i trend
- Faule i kartki — średnia drużynowa i trend, plus (jeśli analiza dotyczy
  zawodnika, lub jest to istotne dla drużyny) profil indywidualny: faule
  popełnione/sprowokowane na 90 min, kartki w sezonie, dystans do
  zawieszenia — patrz SKILL.md Krok 6b

## Kontekst
- Zmiany kadrowe, kontuzje, zmiana trenera, kalendarz (zagęszczenie meczów)

## Wnioski
- 2-4 zdania: co się zmieniło, jakie są implikacje na najbliższe mecze
```

---

## 4. Mecz w ramach turnieju/pucharu (MŚ, ME, fazy pucharowe, Puchar Króla,
   EFL Cup/Carabao Cup, playoffy MLS)

Jak szablon "Pojedynczy mecz", plus dodatkowa sekcja na początku:

```markdown
## Stawka meczu
- Faza turnieju/rundy, co oznacza wynik dla awansu/odpadnięcia każdej drużyny
- Czy któraś drużyna może sobie pozwolić na rotacje (np. już awansowała,
  gra o nic, priorytet to inny mecz w tym tygodniu) — to istotnie wpływa na
  model i warto to jasno zaznaczyć; w Pucharze Króla i EFL Cup rotacje
  czołowych klubów są częste i często ważniejsze niż średnie sezonowe
- Czy regulamin tej rundy dopuszcza remis, czy rozstrzyga dogrywka/karne
  (zweryfikuj aktualnie obowiązujący format, patrz `references/data_sources.md`)
- Krótka rekapitulacja dotychczasowych wyników drużyn w turnieju/pucharze
```

Jeśli runda **nie dopuszcza remisu**, dodaj do sekcji "Prawdopodobieństwa"
(obok/zamiast klasycznego 1X2) tabelę:

```markdown
### Prawdopodobieństwo awansu
| Scenariusz | Prawdopodobieństwo |
|---|---|
| {A} awansuje w 90 minutach | XX% |
| {B} awansuje w 90 minutach | XX% |
| Dogrywka/karne (remis po 90 min) | XX% |
| **{A} awansuje łącznie** (90 min + ~50/50 po dogrywce/karnych) | XX% |
| **{B} awansuje łącznie** | XX% |

*Uzasadnienie: metodologia w SKILL.md Krok 3 ("Mecze pucharowe bez remisu").*
```

Reszta raportu jak w szablonie 1. Pamiętaj, że:
- Dla reprezentacji statystyki sezonowe "ataku/obrony" trzeba liczyć z
  mniejszej próby (mecze kadry w ostatnich ~12-18 miesiącach, eliminacje +
  towarzyskie), więc warto bardziej polegać na jakościowej ocenie kadry i
  formy klubowej kluczowych zawodników.
- Dla Pucharu Króla i EFL Cup, gdy przeciwnicy grają w różnych ligach, model
  bazowy goli (i rożnych) wymaga normalizacji opisanej w SKILL.md Krok 2
  ("Mecze międzyligowe") — zaznacz szerszy przedział niepewności.
- Dla playoffów MLS pamiętaj, że to koniec długiego, innego niż europejski
  kalendarza sezonowego (luty/marzec-grudzień) — forma z ostatnich 5-10
  meczów i ewentualne zmęczenie/rotacje z długiego sezonu ważą więcej niż
  przy standardowym meczu ligowym w środku sezonu.
