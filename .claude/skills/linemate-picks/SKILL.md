---
name: linemate-picks
description: Zbiera z serwisu linemate.io (trendy, hit rate, kursy, cheatsheety, parlaye) najlepsze picki dla podanych wydarzeń sportowych - rynki zawodnika i drużyny w NBA, NHL, NFL, MLB, NCAAB/NCAAF, WNBA, AFL, NRL oraz piłce (EPL, LaLiga, Bundesliga, Serie A, Ligue 1, LM, LE, MLS, Brasileirão, World Cup) - i zwraca ranking najlepszych predykcji z hit rate, kursem i oceną wiarygodności próby. Wymaga zalogowanej sesji na linemate.io w przeglądarce (Claude in Chrome); jeśli użytkownik nie jest zalogowany, skill prosi go o samodzielne zalogowanie. Używaj zawsze, gdy użytkownik wspomina Linemate/linemate.io, prosi o "picki/trendy z Linemate", "props, które trafiają w 100% meczów", hit rate zawodnika, cheatsheet, albo chce wzbogacić analizę NBA/NHL/piłki o trendy zawodników - także gdy podaje tylko mecz lub datę i pisze, żeby sprawdzić trendy/picki.
---

# Linemate - picki i trendy dla wskazanych wydarzeń

Cel: dla podanych meczów wyciągnąć z linemate.io najmocniejsze trendy (hit rate zawodnika/drużyny przy danej linii), zważyć je i zwrócić uporządkowany ranking predykcji. Linemate to **historia trafień**, nie model prawdopodobieństwa. Hit rate 5/5 mówi, co się działo, a nie ile wynosi p; dlatego skill nie podaje go jako gotowego p, tylko jako sygnał do zestawienia z analizami z repo (`nba-analyst`, `nhl-analyst`, `football-analyst`) i kursami (`bet-slip-builder`).

## Krok 0: sesja i logowanie (zawsze pierwszy)

Skill nie zna użytkownika ani jego hasła i **nie wpisuje haseł w formularze** - logowanie robi użytkownik. Powód: hasło przepisane przez agenta trafiłoby do historii rozmowy, a reguły bezpieczeństwa zabraniają wpisywania danych logowania w cudzych serwisach.

1. Załaduj narzędzia Chrome jednym `ToolSearch` (`tabs_context_mcp`, `navigate`, `get_page_text`, `read_page`, `find`, `computer`, `tabs_create_mcp`, `tabs_close_mcp`; dodaj `javascript_tool`, `read_network_requests`, jeśli będą potrzebne). Zacznij od `tabs_context_mcp`, otwórz własną kartę (`tabs_create_mcp`).
2. Wejdź na `https://linemate.io/<liga>` (np. `/nba`, `/nhl`, `/epl`) i sprawdź stan sesji: w nagłówku zalogowany użytkownik ma awatar (kółko z inicjałem) obok lupy; niezalogowany ma przycisk logowania/rejestracji.
3. Jeśli **niezalogowany**: napisz użytkownikowi, żeby zalogował się w tej karcie Chrome (konto Linemate), i poczekaj na jego potwierdzenie. Nie proś o hasło w czacie. Jeśli użytkownik mimo to poda login i hasło, odmów ich użycia i powtórz prośbę o samodzielne zalogowanie; nie zapisuj ich nigdzie (repo, `analizy/`, pamięć).
4. Plan Linemate+ (m.in. wpływ kontuzji na kolegów z drużyny) jest płatny. Nie obchodź paywalla; zaznacz w raporcie, które dane były niedostępne.
5. Nie klikaj akcji kontowych (zakup, zmiana planu, ustawienia), nie akceptuj okien zgód poza koniecznym zamknięciem banera; tylko czytaj.

## Krok 1: ustal wydarzenia i ligi

Weź mecze z zapytania (albo z terminarza `sports-fixtures-finder`). Dla każdego ustal ligę i sług URL: `nba`, `nhl`, `nfl`, `mlb`, `ncaab`, `ncaaf`, `wnba`, `afl`, `nrl`, `epl`, `laliga`, `bundesliga`, `seriea`, `ligue1`, `championsleague`, `europaleague`, `mls`... Jeśli nie jesteś pewien sługa, otwórz selektor ligi (przycisk z nazwą ligi w nagłówku, lista rozwija się po kliknięciu) i wybierz ligę - adres zmieni się na właściwy.

**Pokrycie:** Linemate nie ma tenisa, MMA ani e-sportu. Dla takich wydarzeń powiedz wprost, że serwis ich nie obsługuje, i odeślij do właściwego skilla analitycznego, zamiast zgadywać.

## Krok 2: zbierz trendy

Dwa miejsca, oba na `https://linemate.io/<liga>`:

- **Strona główna ligi** (`/<liga>`): "This Week's Matchups" (kto z kim i kiedy - czas w UTC/lokalny przeglądarki, w raporcie podaj czas polski), "Trending today" (karty z kursem i hit rate), **Cheatsheets** (propsy z 100% trafień: Recent Form, Versus Opponent, Alternate Lines, 1st Quarter, Home/Away, Team Form, Unders Only) i Parlays dla meczu. Ta strona daje się czytać `get_page_text`.
- **Trendy** (`/<liga>/trends`): lista kart w zakładkach Player / Team / Parlay / SGP, filtr (przycisk Filters) i panel szczegółów po kliknięciu karty (hit rate Recent Form / Head to Head / Home-Away, wykres, statystyki per game). Strona renderuje się po stronie klienta: po `navigate` odczekaj ok. 4 s (`computer` → `wait`), dopiero potem `get_page_text` (bez czekania zwraca pustkę albo sam nagłówek). Tekst zawiera ok. 20 kart z listy oraz pełny gamelog pierwszej karty (długi, ignoruj go). Kolejne karty doczytują się przy przewijaniu; gdy potrzebujesz więcej, przewiń listę i odczytaj ponownie albo użyj `find`/`read_page` i zrzutów ekranu (`computer` z `zoom`). Lista jest posortowana wg Linemate i miesza mecze, więc odfiltruj ją do zawodników z interesujących meczów. Gdy nazwa zawodnika jest skrócona ("J. Harden"), dopasuj ją do składu meczu przez drużynę/przeciwnika widoczne na karcie ("vs WAS", "@ BUF").

Karta trendu zawiera: zawodnika/drużynę, przeciwnika, rynek i linię (np. "Over 2.5 Turnovers"), kurs dziesiętny, kilka wierszy hit rate ("Hit in 4 of last 5 games", "vs <rywal>", "home/away", "bez <zawodnika>", "jako starter") i ranking matchupu ("<rywal> is a good <rynek> matchup, 26th" = miejsce obrony rywala na tym rynku). Zapisuj dla każdego picka: n i k (np. 4/5), kurs, którą ramkę zasięgu to dotyczy, ranking matchupu. Przy kilku pickach tego samego zawodnika (np. Over 11.5 i 12.5 yds) bierz jedną, najbardziej sensowną linię.

Surowe zrzuty i odczyty trzymaj w scratchpadzie, nie w repo.

## Krok 3: oceń wiarygodność (to, co robi z hit rate'u sygnał)

Same procenty są mylące, więc każdy pick przejdź przez poniższe filtry; liczby mają zmienić ocenę, nie tylko opis:

1. **Wielkość próby.** 5/5 to 100%, ale 20/20 to inna jakość dowodu. Policz p skorygowane do średniej: `p_adj = (k + 10·p_kurs) / (n + 10)`, gdzie `p_kurs = 1/kurs` (p implikowane przez rynek, bez marży, jeśli znasz drugą stronę). To prosta kotwica bayesowska: mała próba ciągnie p w stronę rynku, duża w stronę własnej historii. Pick, którego `p_adj` nie przekracza `p_kurs` o co najmniej ~3 pp, nie ma przewagi.
1a. **Efekt selekcji.** Linemate pokazuje trendy już wyselekcjonowane po wysokim hit rate, więc `p_adj` zawyża prawdziwe p (przewagi rzędu +15-25 pp nad rynkiem to sygnał do ostrożności, nie dowód). Traktuj `p_adj` jako ranking kandydatów, a stawkę i EV licz dopiero od własnego p. W rankingu ograniczaj się do max 2 picków z jednego meczu (korelacja: ten sam przebieg meczu, np. wiele unders na PP w jednym spotkaniu).
2. **Niezależność ramek.** Wiersze "last 5", "vs rywal", "home" zwykle dotyczą tych samych meczów; nie traktuj ich jako osobnych dowodów i nie mnóż. Najważniejsza jest największa próba.
3. **Zgodność z dzisiejszą sytuacją.** Sprawdź status zawodnika (injury report, minuty, back-to-back, blowout w rynkach zawodnika NBA, potwierdzony bramkarz w NHL, skład w piłce). Wiersz "bez <zawodnika>" liczy się tylko wtedy, gdy ten zawodnik faktycznie dziś nie gra. Trend z sezonu poprzedniego lub przy innej roli to szum.
4. **Matchup.** Ranking rywala (np. 26./30. na danym rynku) to dodatkowy argument, ale słabszy niż próba; używaj go do rozstrzygania remisów między pickami.
5. **Linia i kurs.** Linia na Linemate może różnić się od linii w Betclic/gg397.bet. Przelicz p dla linii, którą realnie można wziąć; kurs z Linemate to orientacyjny kurs któregoś z książek, nie kurs polskiego bukmachera i tak go opisuj.
6. **Rynki unders / "100% Unders Only".** Często opierają się na rynkach, gdzie zawodnik rzadko się pojawia w statystyce (np. 1Q yards); sprawdź, czy kurs nie jest śmieciowy (fair odds ≤ 1.15 odpada zgodnie z regułami repo).

## Krok 4: połącz z analizami z repo

Zgodnie z regułą "zawsze pełna analiza": pick wyłącznie z Linemate nie wchodzi do kuponu ani TOP-N. Dla każdego kandydata uruchom odpowiedni skill analityczny (lub wykorzystaj istniejące `analizy/`), policz własne p (np. `nba_props.py`, `nhl_props.py`, `markets.py`) i zestaw: własne p, `p_adj` z Linemate, p rynku. Rozbieżność >10 pp: znajdź przyczynę (kontuzja, minuty, rola) albo obniż pewność. Zgodność własnego p i hit rate'u wzmacnia pick; niezgodność to flaga, nie powód do zmiany p bez konkretów. Jeśli użytkownik prosi o kupony, przekaż wyselekcjonowane picki do `bet-slip-builder` (progi i spójność typów robi tamten skill).

## Krok 5: raport

Zacznij od jednego zdania: ile wydarzeń pokryto, które ligi/rynki były dostępne, co niedostępne (brak ligi, paywall, brak zalogowania). Potem tabela rankingowa (sortuj po `p_adj - p_kurs`, a przy remisie po wielkości próby):

| # | Mecz (czas PL) | Pick i linia | Kurs (źródło) | Hit rate (n/k, ramka) | p_adj | p rynku | Własne p | Flagi |

Pod tabelą: 3-5 zdań uzasadnienia dla najmocniejszych pozycji (próba, matchup, status zawodnika) i lista picków odrzuconych z powodem (mała próba, zawodnik niepewny, kurs ≤ 1.15). Nie wymyślaj pickow, jeśli Linemate nic nie ma dla danego meczu; napisz, że brak. Na prośbę zapisz wynik w `analizy/Linemate_<Opis>_<RRRR-MM-DD>.md`.

## Czego nie robić

- Nie wpisuj ani nie zapisuj loginu i hasła; nie szukaj ich w plikach ani w pamięci.
- Nie podawaj hit rate'u jako prawdopodobieństwa i nie mnóż ramek.
- Nie omijaj paywalla ani nie wykonuj akcji kontowych.
- Nie zostawiaj otwartych kart: zamknij własną kartę (`tabs_close_mcp`), gdy skończysz.
