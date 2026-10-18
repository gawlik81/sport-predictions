---
name: predictions-verifier
description: Weryfikuje wcześniejsze predykcje, rankingi TOP-N i kupony z plików w analizy/ względem rzeczywistych wyników (piłka, tenis, e-sport, MMA, NBA, NHL), liczy bilans trafień vs oczekiwane z p, EV i zysk hipotetyczny, rozdziela wariancję od błędu procesu, wyświetla podsumowanie weryfikacji i - tylko gdy jest do tego podstawa - poprawia reguły w skillach analitycznych, sports-fixtures-finder i bet-slip-builder. Używaj zawsze, gdy użytkownik prosi o weryfikację, sprawdzenie, rozliczenie lub "jak poszły" typy, TOP10 albo kupony, o weryfikację niezweryfikowanych plików (bez prefiksu ZWERYFIKOWANE_), o kalibrację skilli po wynikach albo o podsumowanie trafności - także gdy nie pada słowo "weryfikacja".
---

# Weryfikacja predykcji i kuponów

Cel: porównać to, co skille wytypowały (`analizy/*`), z tym, co się stało, uczciwie ocenić, czy pudła to pech czy błąd procesu, pokazać użytkownikowi zwięzłe podsumowanie i poprawić skille tylko tam, gdzie jest dla tego podstawa. Weryfikacje są źródłem kalibracji całego flow (terminarz → analiza → kupon).

## Krok 0: Ustal, co weryfikować

- Domyślnie: pliki w `analizy/` bez prefiksu `ZWERYFIKOWANE_`, których nazwa nie zaczyna się od `Weryfikacja_` (analizy, `Top10_predykcje_*`, kupony). Znajdź je poleceniem `ls analizy | grep -v -E "^(ZWERYFIKOWANE_|Weryfikacja_)"`. Jeśli użytkownik wskazał plik, datę lub dyscyplinę, ogranicz się do tego.
- Sprawdź dzisiejszą datę. Mecze, które się jeszcze nie odbyły lub trwają, **nie są rozliczane**: przy częściowej weryfikacji nie dodawaj prefiksu (patrz krok 7).
- Przeczytaj 1-2 ostatnie pliki `Weryfikacja_*` (sekcje "Do obserwacji" i "Kalibracja skilli"): to licznik wzorców z poprzednich kolejek i wzorzec formatu. Nie powtarzaj zmian, które już wprowadzono.

## Krok 1: Wyciągnij typy z dokumentu

Dla każdej nogi zapisz: mecz, rynek i wybór, **p z dokumentu**, kurs, pewność, grupę (np. "piłka 1X2", "piłka Over", "tenis zwycięzca", "NBA spread") i do których kuponów/rankingów wchodzi. Osobno oznacz:
- typy z TOP-N i kuponów (rekomendacje),
- typy "poza kuponami / bez mocnego typu" (rozliczasz je hipotetycznie, osobną sekcją; pokazują, czy wykluczenia były słuszne),
- zalecenie stawki (zwykle 0%): zysk hipotetyczny jest tylko informacją.

Nigdy nie poprawiaj p ani kursu z dokumentu po fakcie. Brak kursu zostaw jako nieznany.

## Krok 2: Pobierz rzeczywiste wyniki

Źródła w tej kolejności (dane zawsze z sieci, nie z pamięci); dla każdego meczu potrzebny jest wynik końcowy i status "zakończony":
- **Piłka, NBA, NHL, tenis:** `espn_scoreboard` albo bezpośrednio `https://site.api.espn.com/apis/site/v2/sports/<sport>/<liga>/scoreboard?dates=RRRRMMDD` (przez Bash/curl, pojedynczy dzień; godziny w UTC, więc mecz po 22:00 czasu polskiego bywa pod następną datą). Ligi: `soccer/uefa.champions`, `uefa.europa`, `uefa.europa.conf`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `basketball/nba`, `hockey/nhl`, `tennis/atp`, `tennis/wta`. Gospodarza wskazuj po polu `homeAway`, nie po `shortName` (tam jest "gość @ gospodarz"). Dla tenisa ESPN zwraca wiele dni i rund naraz, więc filtruj po nazwiskach z dokumentu. Zawsze ogranicz wydruk (filtr w Pythonie), bo odpowiedź bywa ogromna.
- **NHL/NBA:** `nhl_scores`, `nba_scoreboard_today`, `nba_boxscore`/`nhl_boxscore` dla rynków zawodnika.
- **MMA:** `ufc_event_card`/`ufc_fights` (przy bot-challenge: ufcstats.com, Tapology, Sherdog); KSW z Tapology/Sherdog/relacji.
- **E-sport:** `pandascore_matches` (wymaga klucza), HLTV, Liquipedia, Wikipedia; przy 403 użyj `web-fetch` agenta na zapasowym źródle (np. Wikipedia).
- **Ekstraklasa, 1. Liga, mniejsze ligi:** Flashscore (przeglądarka `mcp__claude-in-chrome__*`) albo WebSearch.
- Załaduj potrzebne narzędzia MCP jednym wywołaniem ToolSearch. Gdy narzędzie zwraca błąd klucza, przejdź do kolejnego źródła, nie powtarzaj w pętli.

Zasady wiarygodności:
- Wynik z jednego źródła oznacz w raporcie ("jedno źródło"); wyniki sprzeczne między źródłami rozstrzygnij trzecim lub napisz o niepewności.
- **Nigdy nie zgaduj wyniku.** Brak danych = nogę oznacz "nierozliczona" i nie licz jej; weryfikacja staje się częściowa.
- Rynków, na które nie masz źródła (rożne, kartki, faule, rynki zawodnika), nie rozliczaj z pamięci; napisz, że nie sprawdzono.

## Krok 3: Rozlicz każdą nogę

Rozliczaj dokładnie według definicji rynku z dokumentu:
- **Piłka:** wynik po 90 minutach (bez dogrywki i karnych), chyba że dokument mówi o awansie. Handicap: sprawdź linię i push (różnica równa linii to zwrot lub przegrana zależnie od definicji w dokumencie, opisz ją).
- **Tenis:** krecz i walkower: zwycięzcę meczu rozlicz jak w dokumencie; zakłady setowe/gemowe przy kreczu opisz jako niepewne (zasady bukmachera są różne). Total gemów licz z wyniku setów.
- **NHL:** zwycięzca z dogrywką/karnymi vs wynik po 60 minutach: sprawdź, który rynek wytypowano. Puck line i total po 60' lub z dogrywką zgodnie z dokumentem.
- **NBA:** dogrywka wlicza się w spread, total i zwycięzcę; rynki zawodnika z boxscore (zawodnik, który nie zagrał = zwrot, nie przegrana).
- **MMA:** zwycięzca, sposób, runda; walka odwołana lub zmiana rywala = zwrot (nierozliczona).
- **E-sport:** serie bo3/bo5 z wynikiem map; handicap ±1,5 i total map z wyniku serii.
- Zdarzenie przełożone/odwołane = nierozliczone.

## Krok 4: Policz bilans skryptem

Zbierz nogi do pliku JSON w scratchpadzie (format w nagłówku `scripts/verify.py`) i uruchom z katalogu skilla:

```bash
python scripts/verify.py <plik.json>
```

Skrypt zwraca trafienia vs oczekiwane (suma p) z różnicą w odchyleniach standardowych, wynik Briera, rozbicie na grupy i pasma p, status każdego kuponu (p, kurs, EV, które nogi przegrały) oraz hipotetyczny zysk przy stałej stawce 1. Różnica do ~1 odchylenia standardowego to wariancja; powyżej ~2 jest sygnałem wartym zbadania, ale dopiero po sprawdzeniu przyczyn (krok 5).

## Krok 5: Rozdziel wariancję od błędu procesu

Dla każdego nietrafionego typu (i dla grup z dużą różnicą do oczekiwań) ustal przyczynę:

1. **Wariancja:** wynik o niskim prawdopodobieństwie (przegrana nogi z p 75% to 1 na 4, nie błąd); żadna informacja dostępna przed meczem go nie zapowiadała.
2. **Błąd procesu** (jedyna podstawa do zmiany skilli). Szukaj konkretnych przypadków:
   - sygnał ryzyka opisany w dokumencie, ale liczba bez zmian (najczęstszy błąd);
   - istniejąca reguła ze skilla nie została zastosowana (sprawdź w SKILL.md dyscypliny);
   - p różne od rynku o >5 pp bez twardej informacji (kontuzja, skład, statystyka);
   - informacja dostępna przed meczem, której nie znaleziono (skład, bramkarz startowy, injury report, zmiana rywala, ważenie);
   - błąd definicji lub rozliczenia rynku (np. 60 minut vs dogrywka, handicap graniczny);
   - błąd danych wejściowych (zły terminarz, zła godzina, mecz, który się nie odbył, odwrócony gospodarz).
3. **Błąd budowy kuponu:** noga o niskiej pewności lub rotacji w zestawie zachowawczym, skorelowane nogi, sprzeczne typy, noga z kursem poniżej progu, wymuszone nogi z EV < 0 tylko po to, by trafić w przedział kursu.
4. **Wykluczenia:** czy typy pominięte ("brak mocnego typu", zbyt wysoka linia, fair ≤ 1,15) były słusznie pominięte (wyniki hipotetyczne).

Nie oceniaj decyzji po wyniku: dobry proces może przegrać, zły wygrać. Pojedyncze pudło z wyraźnym naruszeniem reguły lub powtarzalny wzorzec (≥ 2 podobne pudła z różnych meczów, najlepiej potwierdzone w poprzednich weryfikacjach) to podstawa do zmiany; jeden wynik "pod wiatr" nie jest.

Dla grup (rynek, dyscyplina, pasmo p) sprawdź, czy odchylenie utrzymuje się od poprzednich weryfikacji. Jeśli tak i próba to co najmniej ok. 30-60 nóg, rozważ korektę globalną (np. przesunięcie p dla grupy). W przeciwnym razie zapisz w "Do obserwacji".

## Krok 6: Skalibruj skille (tylko z podstawą)

Zmieniaj pliki w `.claude/skills/*/SKILL.md` wyłącznie dla ustalonych błędów procesu lub potwierdzonych wzorców. Domyślnie wynik to **brak zmian** + wpis w "Do obserwacji".

Gdzie wprowadzić zmianę:
- **Błąd w wycenie** (p, korekty, ryzyka, brak informacji): sekcja "Skalibruj" skilla dyscypliny (`football-analyst`, `tennis-analyst`, `esports-analyst`, `mma-analyst`, `nba-analyst`, `nhl-analyst`).
- **Błąd selekcji lub budowy kuponu** (progi, spójność, zestaw zachowawczy, stawki, wymuszanie nóg o EV < 0): `bet-slip-builder`.
- **Błąd terminarza lub źródeł** (zły mecz, godzina, pominięta liga lub dyscyplina, nieaktualne narzędzie MCP, kłopot z dostępem do danych): `sports-fixtures-finder` (kroki 1-2 i lista MCP).
- **Zasada przekrojowa** dla wielu skilli: dopisz jedno zdanie do listy "Zasady, które wynikają z weryfikacji" w `CLAUDE.md` i wpisz szczegóły do odpowiednich skilli.

Format zmiany:
- konkretna reguła z liczbą (np. "odejmij 3-5 pp", "p nie powyżej ~75%") albo jasnym warunkiem, a nie "uważaj";
- w nawiasie uzasadnienie: data weryfikacji i przykład (mecz, p, wynik), tak jak istniejące reguły;
- 1-3 zdania, wstawione w istniejącą listę, nie nowy rozdział; jeśli istnieje podobna reguła, doprecyzuj ją zamiast dublować;
- zachowaj dotychczasowe uzasadnienia; nie usuwaj reguły po jednym kontrprzykładzie;
- nie przywracaj starych skilli `*-predictor`;
- po edycji przeczytaj fragment lub `git diff`, żeby sprawdzić, że zmiana jest tam, gdzie miała być.

Zmiana "w drugą stronę" (reguła zbyt ostrożna): jeśli reguła wykluczyła typy, które po fakcie trafiały w kilku weryfikacjach z rzędu, odnotuj to w "Do obserwacji"; łagodź regułę dopiero przy powtórzeniu.

## Krok 7: Zapisz raport i oznacz pliki

1. Zapisz `analizy/Weryfikacja_<Opis>_<RRRR-MM-DD>.md` (data weryfikowanego dnia), po polsku, według wzorca z ostatnich plików `Weryfikacja_*`:
   - nagłówek z listą zweryfikowanych plików i źródłami wyników (z uwagami o jakości danych, jednym źródle, sprzecznościach);
   - Wyniki (krótka lista meczów z wynikiem);
   - TOP-N (tabela: typ, p, kurs, wynik) i bilans vs oczekiwane;
   - Kupony (tabela: nogi, kurs, p, wynik) i bilans, hipotetyczny zysk z zastrzeżeniem;
   - Typy spoza kuponów (hipotetycznie);
   - Analiza pomyłek (wariancja vs błąd procesu, każde istotne pudło osobno);
   - Co zadziałało;
   - Kalibracja skilli (co zmieniono i dlaczego albo "bez zmian" z uzasadnieniem);
   - Do obserwacji (wzorce z licznikiem i warunek, kiedy zmienić regułę);
   - ostatnie zdanie: to oszacowania, nie gwarancje; mała próba.
2. **Oznaczanie:** po pełnej weryfikacji (wszystkie mecze rozstrzygnięte) zmień nazwę zweryfikowanego pliku na `ZWERYFIKOWANE_<stara nazwa>` (`mv`; `git mv` tylko dla plików śledzonych) i popraw odwołania do starej nazwy w pozostałych plikach: `grep -rn "<stara nazwa>" analizy/`. Przy weryfikacji częściowej nie oznaczaj: wpisz w raporcie, czego brakuje, i uzupełnij później.
3. Nie commituj i nie wypychaj, jeśli użytkownik o to nie prosił; zaproponuj commit po polsku w stylu historii ("Weryfikacja predykcji z ... i kalibracja skilli").

## Krok 8: Wyświetl podsumowanie użytkownikowi

W odpowiedzi (po polsku, bez przepisywania całego raportu) pokaż:
- zakres: które pliki i dni, ile nóg i kuponów rozliczono, czego nie rozliczono i dlaczego;
- tabelkę bilansu: TOP-N, kupony, nogi (trafione/oczekiwane), ewentualnie najciekawsze grupy; hipotetyczny zysk tylko jako informacja;
- 2-4 kluczowe wnioski: główne pudła z oceną "wariancja" lub "błąd procesu";
- **Zmiany w skillach:** plik i jednozdaniowy opis każdej zmiany albo jawne "bez zmian" z powodem;
- "Do obserwacji" i słabe punkty danych (np. wynik z jednego źródła);
- ścieżkę do pliku raportu i propozycję commita.

Przykład:

```
## Weryfikacja 15.10.2026 (Liga Europy/Konferencji, tenis, LoL)
| | Trafione | Oczekiwane |
|---|---|---|
| TOP10 | 9/10 | 7,49 |
| Kupony | 3/5 | 2,74 |
| Nogi kuponów | 8/10 | 7,40 |
Wnioski: ...
Zmiany w skillach: bez zmian (...) / tennis-analyst: dodano regułę ...
Raport: analizy/Weryfikacja_...md
```

## Czego unikać

- Zmieniania skilli po jednej kolejce samej wariancji, bez konkretnego błędu procesu.
- Dopasowywania reguł do pojedynczego wyniku ("overfitting"): rozważ, czy reguła pomogłaby też w typach, które trafiły.
- Zgadywania wyników, rozliczania rynków bez źródła i mylenia gospodarza z gościem.
- Poprawiania p lub kursów z dokumentu po fakcie.
- Pisania, że kupon "wygrał pieniądze", gdy zalecana stawka wynosiła 0%: to zysk hipotetyczny.
- Dodawania prefiksu `ZWERYFIKOWANE_` do pliku, w którym są nierozegrane mecze.
