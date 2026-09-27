# Źródła danych

Te źródła dają najlepszy stosunek sygnału do szumu dla każdego typu informacji.
Szukaj po nazwisku zawodnika + nazwie serwisu (np. "Jannik Sinner Tennis
Abstract" albo "Iga Świątek Ultimate Tennis Statistics"), a nie ogólnych
frazach — to znacznie skraca liczbę potrzebnych zapytań.

## Statystyki serwisu, returnu i formy (priorytet w tym skillu)

**Statystyki serwisu/returnu per nawierzchnia mają priorytet w tym skillu**
(patrz `SKILL.md` Krok 2) — dla nich warto sprawdzić więcej niż jedno
źródło, jeśli pierwsze nie ma rozbicia per nawierzchnia.

- **Tennis Abstract** (tennisabstract.com) — najpełniejsze statystyki
  point-by-point: % serwisu/returnu ogółem i per nawierzchnia, Elo rating
  (ogólny i per nawierzchnia), match logs, historia H2H. Podstawowe źródło
  do liczenia p_a_serve/p_b_serve z Kroku 2.
- **Ultimate Tennis Statistics** (ultimatetennisstatistics.com) — Elo
  ratings (w tym per nawierzchnia i "in-form"), statystyki serwisu/returnu,
  H2H, rozkłady wyników. Dobre źródło do szybkiej kontroli krzyżowej wobec
  Tennis Abstract.
- **ATP Tour** (atptour.com) — oficjalne statystyki sezonowe serwisu/returnu
  per zawodnik (Aces, 1st Serve %, Break Points Saved itd.), ranking, H2H,
  terminarz turniejów ATP.
- **WTA Tour** (wtatennis.com) — analogicznie dla kobiet: statystyki,
  ranking, terminarz WTA.
- **Sofascore / Flashscore** (sofascore.com, flashscore.pl) — szybki wgląd
  w formę (ostatnie 10-15 meczów), statystyki meczowe live/po meczu, składy
  drabinki, terminarz.
- **Tennis Explorer** (tennisexplorer.com) — H2H, wyniki, terminarze,
  statystyki formy, dobre pokrycie też dla Challengerów i ITF.
- **ITF World Tennis Tour** (itftennis.com) — turnieje niższej rangi
  (Challenger, ITF) — sprawdzaj tu, gdy ATP/WTA/Tennis Abstract nie mają
  wystarczającego pokrycia dla mniej znanych zawodników.

## Orientacyjne średnie turowe % punktów wygranych na serwisie

Potrzebne jako baseline w Kroku 2 do liczenia siły serwisu/returnu. To
**przybliżenia orientacyjne** (różnią się między sezonami) — jeśli to
możliwe, zweryfikuj aktualną wartość sezonową danej nawierzchni/toru przez
Tennis Abstract lub Ultimate Tennis Statistics zamiast polegać wyłącznie na
tej tabeli.

| Nawierzchnia | ATP (mężczyźni) | WTA (kobiety) |
|---|---|---|
| Trawa | ~66-68% | ~57-59% |
| Twarda | ~63-65% | ~55-57% |
| Mączka | ~60-62% | ~53-55% |

Wyższe wartości = serwis bardziej dominuje (krótsze wymiany, więcej asów,
mniej przełamań) → generalnie mniej gemów łamanych = wyższy total gemów przy
wyrównanym meczu. Mączka i WTA mają niższe % serwisu = więcej przełamań,
częściej wynik seta typu 6-2/6-3 zamiast 7-6/6-4.

## Ranking, kadra turniejowa, drabinka
- **ATP Tour / WTA Tour** — oficjalny ranking na żywo, drabinki turniejowe,
  terminarz rund.
- **Tennis Abstract / Ultimate Tennis Statistics** — Elo jako uzupełnienie
  rankingu ATP/WTA (Elo lepiej odzwierciedla bieżącą formę niż ranking, który
  jest średnią z 52 tygodni).

## Kontuzje, zmęczenie, ryzyko wycofania (retirement)
- Oficjalne komunikaty ATP/WTA i strony turniejów o wycofaniach (withdrawal/
  retirement reports).
- Świeże artykuły z ostatnich 3-7 dni: "[zawodnik] injury update", "[zawodnik]
  fitness concern", "[zawodnik] przedmeczowo".
- Tennis.com, ESPN Tennis — dobre źródła kontekstu medialnego i newsów o
  kontuzjach.
- Historia meczów zawodnika w bieżącym turnieju (Sofascore/Flashscore) —
  długie, wyczerpujące mecze (5 setów, tie-breaki, mecze >3h) w ostatnich
  dniach zwiększają ryzyko spadku formy lub wycofania w kolejnej rundzie.

## Regulamin turnieju (format meczu, tiebreak w secie decydującym)
- **Oficjalne strony Wielkich Szlemów** (ausopen.com, rolandgarros.com,
  wimbledon.com, usopen.org) — zawsze weryfikuj tu aktualny regulamin
  tiebreaka w secie decydującym danego roku, bo mógł się zmienić.
- **Od marca 2022 wszystkie 4 Wielkie Szlemy grają ujednolicony format:
  super-tiebreak do 10 punktów przy 6-6 w secie decydującym** (Australian
  Open, Roland Garros, Wimbledon i US Open — włącznie z US Open, które
  wcześniej, od 1970 do 2021, używało standardowego tiebreaka do 7 w
  każdym secie, także decydującym; Wimbledon wcześniej stosował "przewagę
  dwóch gemów" bez tiebreaka do 2018, potem tiebreak dopiero przy 12-12 do
  2021). Zweryfikowane researchem 2026-09-06 — poprzednia wersja tej
  tabeli (tiebreak do 7 na US Open, do 12-12 na Wimbledonie) była
  nieaktualna i pochodziła sprzed unifikacji z 2022 roku. Mimo to zawsze
  potwierdź to researchem przy każdej analizie (Krok 0) — zasady mogły się
  zmienić ponownie.
- **ATP Tour / WTA Tour** — regulamin Masters 1000/WTA 1000, ATP 500/250,
  WTA 500/250 (zawsze best-of-3, standardowy tiebreak do 7 przy 6-6, bez
  zmian w secie decydującym — unifikacja z 2022 dotyczy tylko 4 Wielkich
  Szlemów).

## Artykuły medialne / kontekst (forma, motywacja, zmiana trenera, plotki)
- Wyszukuj świeże artykuły z ostatnich 3-7 dni: "[zawodnik] preview",
  "[zawodnik] press conference", "[zawodnik] [przeciwnik] H2H preview".
- Lokalna prasa sportowa (np. Przegląd Sportowy, Sport.pl) dla polskich
  zawodników (Świątek, Hurkacz, Majchrzak i inni).
- Konferencje prasowe zawodników przed meczem — często zawierają bezpośrednie
  informacje o stanie zdrowia, samopoczuciu, planach taktycznych.

## Rozgrywki i zakres
- **ATP Tour**: Wielki Szlem (Australian Open, Roland Garros, Wimbledon,
  US Open — best-of-5 dla mężczyzn), Masters 1000, ATP 500, ATP 250, ATP
  Finals.
- **WTA Tour**: Wielki Szlem (best-of-3 dla kobiet), WTA 1000, WTA 500,
  WTA 250, WTA Finals.
- **Challenger / ITF World Tennis Tour** — obsługiwane na żądanie tym samym
  schematem, choć dane bywają mniej szczegółowe (mniejsze pokrycie na Tennis
  Abstract/Ultimate Tennis Statistics) — wtedy zaznacz to wprost w raporcie
  zamiast zgadywać.
- Nawierzchnie: twarda (hard), mączka (clay), trawa (grass) — zawsze ustal,
  na jakiej nawierzchni odbywa się dany turniej, bo to kluczowy czynnik
  Kroku 2.
