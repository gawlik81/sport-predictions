---
name: mma-analyst
description: Analiza walk MMA (gale UFC, KSW i inne organizacje) na podstawie czterech filarów - statystyk zawodników (rekord, sposoby wygranych i porażek, trafienia/obrona w stójce, obalenia, submission, finisze, zasięg, wiek, waga), statystyk poprzednich walk (H2H, wspólni rywale, styl vs styl, przebieg walk), informacji medialnych z internetu (kontuzje, zastępstwa z krótkim wyprzedzeniem, ścinanie wagi i ważenie, przerwa, zmiana trenera/obozu, forma, warunki walki) oraz kursów rynkowych - i wycena prawdopodobieństw (zwycięzca, sposób wygranej KO/TKO/submission/punkty, walka na dystans, Over/Under rund, runda finiszu) z fair odds. Używaj zawsze, gdy użytkownik prosi o analizę, typ, prognozę lub przegląd walki/gali MMA, UFC, KSW, pyta o szanse zawodnika, formę, kursy, value bet albo podaje same nazwiska zawodników, numer gali (UFC 330, KSW 100) lub datę - nawet bez słowa "MMA".
---

# Analiza walk MMA (UFC, KSW)

Cel: dla każdej walki zebrać aktualne dane z czterech źródeł, przełożyć je na prawdopodobieństwa i uczciwie pokazać niepewność. MMA ma największą wariancję z analizowanych dyscyplin (pojedynczy cios, decyzja sędziów, zmiana na karcie w ostatniej chwili), więc zawsze zaczynaj od researchu (WebSearch/WebFetch/MCP), a nie od rekordu z pamięci, i trzymaj p z dala od 0% i 100%.

Skill jest nowy: **nie ma jeszcze weryfikacji typów MMA**. Reguły w Kroku 3 pochodzą z zasad działających w pozostałych skillach tego repo (sygnał musi zmienić liczbę, nie schodź daleko pod rynek, nie dopychaj rankingu) i z ogólnych cech MMA. Po pierwszych gałach zweryfikuj typy (`Weryfikacja_predykcji_*`) i skoryguj ten krok na podstawie wyników, tak jak w tennis-analyst i football-analyst.

## Serwer MCP `sportsdata` (używaj w pierwszej kolejności dla UFC)

Narzędzia `mcp__sportsdata__*` są deferred: załaduj je przez ToolSearch (np. `select:mcp__sportsdata__ufc_event_card,mcp__sportsdata__ufc_athlete,mcp__sportsdata__ufc_search_athletes`). Kształty odpowiedzi sprawdzaj na realnym payloadzie.
- **Karta gali UFC:** `ufc_events` (lista, godziny kart: early prelims / prelims / main card) i `ufc_event_card` (`title` = "UFC 330"; walki są w polu `included`, nie w `data`).
- **Zawodnik:** `ufc_search_athletes` (partial name → `fightmetric_id`), potem `ufc_athlete` (`title` = pełne imię; statystyki kariery są w `included`: `win_ko`, `win_sub`, `win_dec`, `first_rd_fin`, `sig_str_land_min`, `sig_str_abs_min`, `sig_str_def`, `takedown_average`, `takedown_acuracy` (tak jest pisane upstream), `takedown_defense`, `submission_average`, `knockdown_average`, `avg_fight_time` w sekundach; zasięg i wzrost w calach; pola procentowe są stringami) oraz aktualny ranking. Dane to kariera w UFC, nie ostatnie walki: formę i rywali ustal osobno.
- **Wyniki i historia walk:** `ufc_fights` (po tytule "A vs B"), `apisports_mma_fights` (wymaga `API_SPORTS_KEY`; kształt niezweryfikowany).
- **Kursy (filar 4):** `theoddsapi_odds` (`THE_ODDS_API_KEY`, klucz sportu MMA wyszukaj w `theoddsapi_sports`), `pinnacle_sports`/`pinnacle_sport_matchups` (sprawdź, czy oferują MMA; kursy amerykańskie przelicz na dziesiętne), `polymarket_search` jako dodatkowy odnośnik. Brak klucza lub danych = przejdź dalej i napisz, że kursów nie ma.
- **Gdy `ufc_*` zwraca stronę z bot-challenge lub puste dane** (zdarzyło się przy gali z 10.10.2026): nie rezygnuj ze statystyk kariery, tylko pobierz je z ufcstats.com, Tapology lub Sherdog przez WebFetch/WebSearch i napisz, z jakiego źródła pochodzą. Samo "brak statystyk" jako powód, by zostawić p równe rynkowi, to ostateczność.
- **KSW i inne organizacje (brak MCP):** karta i zawodnicy z WebSearch/WebFetch: oficjalna strona KSW, Sherdog, Tapology, polskie media (np. Sport.pl, Interia, mmarocks, Przegląd Sportowy) i konferencje/ważenia. Pełnych statystyk uderzeń zwykle nie ma - patrz Krok 3.

## BettingPros (skill `bettingpros-odds`)

Dla NBA/NHL/piłki (i innych sportów, które API zwraca - sprawdź `events --sport <X>`) wywołaj skill `bettingpros-odds` jako dodatkowe źródło: konsensus linii i kursów z wielu bukmacherów, `best_lines`, a przy rynkach zawodnika rekomendacje `props` (probability, EV, bet rating, forma last_N). Skill najpierw pyta o klucz API, jeśli `BETTINGPROS_API_KEY` nie jest ustawiona; bez klucza pomiń to źródło i zaznacz to w raporcie (nie blokuj analizy). To kontrola i źródło kursów, nie zamiennik własnego p: różnica >10 pp względem rynku bez marży wymaga wyjaśnienia (skład, kontuzje), a niezgodność z `props` BettingPros to flaga do sprawdzenia, nie powód do zmiany liczby bez konkretów. W raporcie oznacz "BettingPros" przy każdej użytej linii/kursie.

## Krok 1: Zbierz dane (cztery filary)

1. **Statystyki zawodników** - rekord, seria, sposoby wygranych (KO/TKO, submission, punkty) i porażek (kto jak przegrywał: brodą, parterem), ostatnie 5 walk z kim i jak, trafienia istotne na minutę vs przyjęte (SLpM/SApM), celność i obrona w stójce, obalenia (średnia, celność, obrona), submission na 15 min, knockdowny, % finiszów w 1. rundzie, średni czas walki, wiek, zasięg i wzrost, stójka (orto/południowa), kategoria wagowa (czy zmienia dywizję). Liczby sezonowe i z ostatnich walk ważą więcej niż rekord.
2. **Poprzednie spotkania** - H2H (rzadkie w MMA); częściej **wspólni rywale** i **styl vs styl** (zapaśnik vs słaby w obronie obaleń, bokser vs słabsza broda), jakość rywali (poziom rankingu, a nie sama liczba wygranych). Walki sprzed 3+ lat albo w innej kategorii wagowej waż nisko.
3. **Informacje medialne** - dla KAŻDEGO zawodnika osobne zapytanie "[nazwisko] injury / kontuzja / weigh-in [rok]". Do tego: zastępstwo na krótki termin (ile dni przygotowania, w jakiej wadze), ścinanie wagi i wynik ważenia (przekroczenie limitu, widoczne odwodnienie, walka w "catchweight"), długa przerwa (≥12 miesięcy), zmiana trenera/obozu, wysokość nad poziomem morza i podróż (UFC w Denver/Meksyk/Salt Lake), walka o pas i liczba rund, motywacja (kontrakt, odejście), niezwykłe wydarzenia pozasportowe. Plotki oznaczaj jako niepotwierdzone.
4. **Rynek** - kursy bukmacherów po zdjęciu marży (zwycięzca, sposób, Over/Under rund, "przejdzie dystans"). To niezależny punkt odniesienia i w MMA bywa najlepszym pojedynczym predyktorem. Gdy Twoja liczba różni się o >8 pp, najpierw szukaj, czego nie wiesz.

Jeśli brakuje kluczowych danych (szczególnie przy KSW i mniejszych galach), napisz to wprost i obniż pewność. Przy każdym kluczowym fakcie podaj źródło.

## Krok 2: Policz

Skrypt nie wylicza zwycięzcy z surowych statystyk, tylko spójnie rozkłada Twoje oszacowania. Najpierw ustal trzy liczby:

- **P(A wygra)** - z porównania statystyk (różnica trafionych/przyjętych uderzeń, obrona obaleń vs obalenia, finisz vs odporność), skorygowana o informacje medialne i skonfrontowana z rynkiem.
- **fa, fb** - P(A wygra przez finisz), P(B wygra przez finisz): zacznij od udziału finiszów w wygranych każdego i od tego, jak często rywal przegrywał przed czasem; uwzględnij rundy (5 rund daje więcej finiszów niż 3) i klasę wagową (cięższe = więcej KO).
- **da** - P(A wygra na punkty | dystans): z P(A wygra) wylicz `da ≈ (pA - fa) / (1 - fa - fb)`; potem sprawdź wynik skryptu i skoryguj fa/fb/da tak, by P(A) w wyniku zgadzało się z Twoim.

```bash
python scripts/mma_model.py <fa> <fb> <da> [--rounds 2|3|5] [--w 1.3,1,0.8] [--ko-a 0.7] [--ko-b 0.7] [--draw 0.02] [--name-a A] [--name-b B]
```

Skrypt zwraca P(zwycięzca) i fair odds, sposób wygranej (KO/TKO, submission, punkty dla obu), P(dystans)/P(finisz), finisz w poszczególnych rundach oraz Over/Under rund (linie co 0,5 rundy; finisz równomiernie w rundzie). `--w` to względna intensywność finiszu w kolejnych rundach (UFC: najwięcej w 1. rundzie, np. 1.3,1,0.8); domyślnie płasko. Liczba rund: UFC zwykle 3, walki o pas i main eventy 5; KSW zwykle 3, ale potwierdź na karcie (walki o pas bywają dłuższe). Przy "sposób wygranej" skrypt zakłada, że finisz to KO/TKO lub submission; dyskwalifikację i lekarza traktuj jako część finiszu.

## Krok 3: Skalibruj

Reguły wstępne (do weryfikacji po pierwszych typach):

- **Każdy sygnał ryzyka musi zmienić liczbę, nie tylko opis.** Wzmianka bez korekty to najczęstszy błąd z tenisa i piłki.
- **Nie schodź pod rynek ani nie wchodź nad niego o >5 pp bez konkretnej informacji** (kontuzja, stand-in, konkretna statystyka). Rynek MMA zwykle dobrze wyceniony; samo "wydaje mi się" nie jest przewagą.
- **Pułap p:** nie dawaj >85% na zwycięzcę walki ani >92% na "wygra przed czasem/Over 0.5" bez wyjątkowej przepaści i potwierdzonych liczb; nawet bardzo wyraźny faworyt przegrywa przez pojedynczy cios lub niefortunne obalenie. Dla KSW bez statystyk uderzeń i bez rynku pułap p zwycięzcy ok. 75%.
- **Zastępstwo na krótki termin (<~3 tygodnie):** zastępca ma mniej czasu na obóz i ścięcie wagi (zwykle na jego niekorzyść), a rywal musi przygotować się na kogoś innego niż planował. Zmień p o kilka pp w stronę zawodnika z pełnym obozem, ale nie więcej niż o ~5 pp bez konkretów (stan formy zastępcy, jego ostatnia walka), i obniż pewność o jeden stopień.
- **Ważenie i przekroczenie wagi:** sprawdź w komunikacie z ważenia konkretną karę (w KSW m.in. punkt ujemny na starcie walki i 30-50% gaży; w UFC zwykle tylko % gaży, nieraz catchweight). Rozdziel dwa efekty. (1) **Punkt ujemny działa mechanicznie tylko przy decyzji:** przesuń `da` na korzyść rywala (przy walce wyrównanej i bez przewagi finiszowej to kilka pp w p zwycięzcy), nie pisz "bez znaczenia". (2) **Efekt fizyczny (odwodnienie, kondycja) jest niepewny:** w KSW 122 (10.10.2026) wszyscy trzej, którzy przekroczyli limit (Soldaev, Zając, Zerhouni), dostali punkt ujemny, a dwóch z nich zakończyło walkę w 1. rundzie; nie odejmuj więc więcej niż ~5 pp od p zwycięzcy za sam fakt przekroczenia wagi, chyba że masz konkretną informację (widoczne wyczerpanie, zmiana planu walki). Przy walce, która najpewniej skończy się finiszem, kara punktowa jest praktycznie bez znaczenia.
- **Długa przerwa (≥12 mies.) lub powrót po kontuzji / KO:** obniż pewność i p, szczególnie dla zawodnika 35+ (odporność na ciosy spada z wiekiem); wiek 35+ w walce 5-rundowej to dodatkowe ryzyko ogonowe.
- **Rozpiętość statystyk vs jakość rywali:** wysokie liczby z walk przeciw słabszym (regionalne, KSW poza topem, mniejsze organizacje) nie przekładają się wprost na UFC/KSW elitę. Bilans z mniejszych gal nie liczy się jak bilans z top 15. Nie typuj niżej notowanego zawodnika >55% bez konkretnych statystyk z porównywalnego poziomu.
- **Styl vs styl:** zapaśnik przeciw słabej obronie obaleń to realna przewaga, ale tylko jeśli ma statystyki obaleń z porównywalnego poziomu; sam zasięg lub wyższy ranking nie wystarczą. Styl faworyta oparty na dystansie traci wartość, gdy rywal skraca dystans i dobrze wchodzi w klincz.
- **Decyzje sędziów:** walki kończące się na punkty mają większą wariancję niż KO; dla walki wyrównanej przesuń da w stronę 50%, nie wskazuj "punktów dla A" jako pewnego typu. Nie dodawaj premii za zawodnika "u siebie" ani za kraj bez danych potwierdzających.
- **Nie uśredniaj mechanicznie** model / zewnętrzne modele / rynek. Gdy rozstęp >8 pp, p jest niepewne: przyjmij dolną część rozstępu zwycięzcy, oznacz pewność "niska".
- **Rynki sposobu i Over/Under rund** mają mniej danych niż zwycięzca: pewność co najwyżej "średnia", chyba że znasz dokładne wskaźniki finiszu obu stron z ostatnich walk i liczbę rund jest potwierdzona.
- **Dane z mniejszych gal (KSW, regionalne):** często brak statystyk uderzeń, tylko rekordy i sposoby wygranych. Pracuj na rekordzie i przebiegu walk, obniż pewność o jeden stopień, nie wpisuj typów sposobu/rund do rankingu.

## Krok 4: Raport

Po polsku, zwięźle, dla każdej walki:

```
### Zawodnik A - Zawodnik B (gala, kategoria, rundy, data, godzina PL)
**Typ:** <rynek> | **Prawdopodobieństwo:** XX% | **Fair odds:** X.XX | **Pewność:** niska/średnia/wysoka
**Statystyki zawodników:** rekord, forma, SLpM/SApM, obalenia, finisze, wiek/zasięg z liczbami
**H2H / wspólni rywale:** 1-2 zdania (styl vs styl)
**Informacje medialne:** kontuzje, ważenie, przerwa, stand-in, obóz (ze źródłem)
**Ryzyka:** scenariusze, w których typ przegrywa
**Rynki dodatkowe:** tabela: zwycięzca, sposób wygranej, dystans, Over/Under rund (p, fair, kurs, pewność)
**Rynek:** kurs vs fair odds (jeśli znany)
```

Przy przeglądzie gali dodaj ranking top-N **ze wszystkich rynków** (zwycięzca, sposób wygranej, dystans, Over/Under rund). Pomijaj typy z fair odds ≤ 1.15, przypadki 1.15-1.20 oznacz jako graniczne. Nie dobijaj listy do N na siłę: jeśli mocnych typów jest mniej, pokaż mniej. Na końcu jedno zdanie: to oszacowania, nie gwarancje.
