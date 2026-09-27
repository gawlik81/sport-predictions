# Źródła danych

Te źródła dają najlepszy stosunek sygnału do szumu dla każdego typu informacji.
Szukaj po nazwie drużyny + nazwie serwisu (np. "Lech Poznań FBref" albo
"Legia Warszawa Sofascore"), a nie ogólnych fraz — to znacznie skraca
liczbę potrzebnych zapytań.

## Statystyki drużynowe i meczowe (forma, xG, rożne, strzały, faule, kartki)

**Rożne mają priorytet w tym skillu** (patrz `SKILL.md` Krok 4) — dla nich
warto sprawdzić więcej niż jedno źródło, jeśli pierwsze nie ma pełnego
rozbicia dom/wyjazd "for"/"against".

- **FBref** (fbref.com) — najpełniejsze statystyki: xG, xGA, strzały, strzały
  celne, faule, kartki, posiadanie. Ma osobne tabele "for" i "against" per
  drużyna oraz rozbicie dom/wyjazd — to jest podstawowe źródło do liczenia
  współczynników ataku/obrony. Dane o rożnych bywają na FBref niepełne
  (zależnie od ligi) — jeśli brakuje rozbicia, dociągnij FootyStats lub
  Sofascore. Dla profilu **indywidualnego zawodników** (Krok 6b) sprawdź
  tabelę drużyny "Miscellaneous Stats" — ma per zawodnik faule popełnione
  (Fls), faule sprowokowane (Fld) oraz żółte/czerwone kartki, w tym wartości
  per 90 minut.
- **FootyStats** (footystats.org) — specjalizuje się w statystykach rożnych i
  over/under: średnie rożnych zdobytych/oddanych per drużyna, rozbicie
  dom/wyjazd, gotowe % over/under dla typowych progów. Najlepsze pierwsze
  źródło do liczenia λ_rożne z Kroku 4.
- **Sofascore** (sofascore.com) — szybki wgląd w formę (ostatnie 5-10 meczów),
  szczegóły meczu live/po meczu (w tym rożne i faule per mecz), oceny
  zawodników, składy. Karta zawodnika pokazuje sezonowe faule/mecz i liczbę
  kartek — przydatne uzupełnienie FBref dla profilu indywidualnego (Krok 6b),
  zwłaszcza w ligach, gdzie FBref ma płytsze pokrycie.
- **Flashscore** (flashscore.pl) — wyniki, terminarze, H2H, statystyki live
  (w tym rożne). Dobre do szybkiego sprawdzenia terminarza i wyników
  bezpośrednich starć.
- **WhoScored** (whoscored.com) — szczegółowe statystyki meczowe i sezonowe,
  rankingi drużyn, mapy nacisku.
- **American Soccer Analysis** (americansocceranalysis.com) — najlepsze
  źródło xG/xGA specyficznie dla MLS (FBref pokrywa MLS płycej niż ligi
  europejskie). Sprawdzaj tu w pierwszej kolejności dla meczów MLS.
- **MLSsoccer.com** — oficjalne statystyki ligowe, tabele konferencji,
  terminarz, komunikaty klubowe dla MLS.

## Puchary krajowe bez rewanżu (Copa del Rey, EFL Cup/Carabao Cup)
- **RFEF** (rfef.es) — oficjalna federacja hiszpańska: losowania, wyniki i
  terminarz Copa del Rey, przydatne zwłaszcza dla wczesnych rund z udziałem
  drużyn z Segunda RFEF/Tercera, gdzie FBref/Sofascore bywają niepełne.
- **EFL / Carabao Cup** (efl.com, thefa.com dla regulaminu) — oficjalny
  regulamin rundy (dogrywka tak/nie, format półfinału w danym sezonie) —
  zawsze zweryfikuj na bieżąco, bo format zmieniał się między sezonami.
- FBref/Sofascore/Flashscore pokrywają obie te rozgrywki wystarczająco dobrze
  dla klubów z lig zawodowych, ale dane dla bardzo niszowych rywali z niższych
  poziomów bywają skąpe — zaznacz to wprost zamiast zgadywać.
- **Zapowiedzi przedmeczowe są tu kluczowe** — rotacje składu w pucharach są
  trudniejsze do przewidzenia niż w lidze, więc świeże artykuły o
  planowanym składzie ważą więcej niż średnie sezonowe.

## Składy, kontuzje, zawieszenia
- **Transfermarkt** (transfermarkt.pl / .com) — historia kontuzji, wartości
  rynkowe, zawieszenia za kartki, najbliższe powroty do gry. Profil każdego
  zawodnika ma zakładkę "Kartki" z liczbą żółtych/czerwonych w sezonie — to
  najszybszy sposób sprawdzenia dystansu do zawieszenia (Krok 6b).
- Oficjalne strony klubów i lig (np. ekstraklasa.org, premierleague.com,
  laliga.com) — komunikaty o kadrze meczowej, oficjalne składy.

## Artykuły medialne / kontekst (forma, motywacja, plotki transferowe, zmiany trenerskie)
- Wyszukuj świeże artykuły z ostatnich 3-7 dni: "[drużyna] przedmeczowo",
  "[drużyna] [przeciwnik] preview", "[drużyna] team news injuries".
- Lokalna prasa sportowa (np. Przegląd Sportowy, Sport.pl, Meczyki.pl) dla
  Ekstraklasy i kadry Polski — często ma informacje o nastrojach w szatni,
  kryzysach formy, rotacjach.
- Dla reprezentacji: oficjalne strony federacji oraz UEFA/FIFA dla terminarzy,
  rankingów i archiwów H2H.

## Ligi i rozgrywki w zakresie
- Top 5: Premier League, La Liga, Serie A, Bundesliga, Ligue 1
- Polska: Ekstraklasa (i w razie potrzeby Fortuna 1 Liga)
- **MLS** (Major League Soccer) — bez spadków, podział na konferencję
  wschodnią/zachodnią, sezon luty/marzec-grudzień, playoffy na koniec sezonu
  (traktuj jako mecze turniejowe/pucharowe, patrz `SKILL.md` Krok 0)
- Puchary klubowe: Liga Mistrzów, Liga Europy, Liga Konferencji
- **Puchary krajowe bez rewanżu**: Puchar Króla (Copa del Rey), Puchar Ligi
  Angielskiej (EFL Cup / Carabao Cup) — mecze jednorundowe, możliwa
  dogrywka/karne zamiast remisu, duże znaczenie rotacji składu i różnic
  klasowych między drużynami z różnych lig (patrz `SKILL.md` Krok 2-3)
- Reprezentacje: eliminacje MŚ/ME, mecze towarzyskie, Mistrzostwa Świata,
  Mistrzostwa Europy i inne turnieje kontynentalne
- Inne ligi europejskie (Eredivisie, Liga Portugalska, Championship itd.) —
  obsługiwane na żądanie tym samym schematem, choć dane bywają mniej
  szczegółowe (np. brak pełnych statystyk rożnych/faulów na FBref dla
  niektórych lig — wtedy zaznacz to wprost w raporcie zamiast zgadywać).
