# Weryfikacja kuponów TOP5 + Ekstraklasa z 09.10.2026 (stan: sobota 10.10, ok. 19:30)

Zweryfikowane pliki: `Analiza_TOP5_kolejka_2026-10-09_12.md` (podstawa), `Top5_kupony_2026-10-09.md`, `Top5_kupony_wynik_i_gole_2026-10-09.md`, `Kupony_TOP5_Ekstraklasa_2026-10-09.md` (wersja pierwotna + Aktualizacja + Aktualizacja 2; za obowiązującą biorę Aktualizację 2).

Źródła wyników: ESPN scoreboard (Premier League, La Liga, Serie A, Bundesliga, Ligue 1), OpenLigaDB, ekstraklasa.org (terminarz i wyniki 10. kolejki).
**Weryfikacja częściowa:** mecze z 11-12.10 i część z 10.10 jeszcze się nie odbyły (lista na końcu); do uzupełnienia w kolejnej weryfikacji. Dortmund - Werder opisany osobno w `Weryfikacja_Dortmund_Werder_2026-10-10.md`.

## Wyniki zakończonych meczów

| Mecz | Wynik |
|---|---|
| Dortmund - Werder | 2-2 |
| Lens - Lyon | 2-1 |
| Wieczysta - Wisła Płock | 3-0 |
| Raków - GKS Katowice | 1-4 |
| Arsenal - Leeds | 2-1 |
| Chelsea - Bournemouth | 5-1 |
| Augsburg - Bayern | 2-2 |
| Union Berlin - Elversberg | 1-0 |
| Lille - Le Havre | 1-0 |
| Cracovia - Zagłębie | 3-1 |
| Śląsk - Lech | 1-4 |

## Typy (pojedyncze nogi) z tabel w plikach

| Typ | p | Wynik |
|---|---|---|
| Dortmund wygra | 69% | ❌ |
| Arsenal wygra | 66% | ✅ |
| Bayern wygra (Augsburg) | 78% | ❌ (2-2) |
| Lille wygra | 65% | ✅ |
| Chelsea lub remis | 78% | ✅ |
| Cracovia lub remis | 77% | ✅ |
| Wieczysta lub remis | 71% | ✅ |
| Raków lub remis | 67% | ❌ (1-4) |
| Over 1.5: Śląsk - Lech | 83% | ✅ (5 goli) |
| Over 1.5: Raków - GKS | 84% | ✅ (5) |
| Over 1.5: Wieczysta - Płock | 80% | ✅ (3) |
| Over 1.5: Cracovia - Zagłębie (kurs 1.26) | ok. 77% z kursu | ✅ (4) |
| Over 2.5: Wieczysta - Płock | 59% | ✅ |
| Over 2.5: Raków - GKS | 65% | ✅ |
| Over 2.5: Union - Elversberg | 63% | ❌ (1 gol) |
| Under 3.5: Lens - Lyon | 59% | ✅ (3 gole) |
| Under 3.5: Chelsea - Bournemouth | 58% | ❌ (6 goli) |
| Under 3.5: Dortmund - Werder | 53% | ❌ (4 gole) |

**Bilans: 12/18.** Suma p z tabeli = 12,5 oczekiwanych trafień, czyli kalibracja bardzo dobra. Wg rynków: wygrana/1X 5/8 (średnia p 71%, oczekiwane 5,7), Over 1.5 4/4, Over 2.5 2/3, Under 3.5 1/3.

## Kupony zakończone (obowiązujące wersje)

| Plik / kupon | Nogi | Kurs | Wynik |
|---|---|---|---|
| Ekstraklasa Akt. 2, K2 | Arsenal ✅ + Cracovia - Zagłębie O1.5 ✅ | 1.77 | ✅ |
| Ekstraklasa Akt. 2, K4 | Legia (11.10) + Dortmund ❌ | 1.77 | ❌ |
| Ekstraklasa Akt. 2, K5 | Everton (11.10) + Raków 1X ❌ | 1.79 | ❌ |
| Top5_kupony K1 | Dortmund ❌ + Arsenal ✅ | 1.88 | ❌ |
| Top5_kupony K2 | Bayern ❌ + Betis (11.10) | 1.75 | ❌ |
| wynik_i_gole K1 | Dortmund ❌ + Chelsea U3.5 ❌ | 2.19 | ❌ |
| wynik_i_gole K2 | Bayern ❌ + Atalanta U3.5 (12.10) | 1.81 | ❌ |
| wynik_i_gole K3 | Lille ✅ + Lens - Lyon U3.5 ✅ | 2.32 | ✅ |

Wcześniejsze wersje kuponów w pliku Ekstraklasa: pierwotny K5 (Chelsea 1X ✅ + Union O2.5 ❌) i K5 z Aktualizacji (Union O2.5 ❌ + Wieczysta O1.5 ✅) też przegrały, obie przez Union. Kupony po jednej przegranej nodze są przegrane, więc te z Bayernem i Dortmundem rozstrzygnięte.

**Rozstrzygnięte: 2 ✅ / 6 ❌ z 8.** Flat stake 1 j. na każdy: zwroty 1.77 + 2.32 = 4,09 przy stawce 8 → -3,91 j. (ROI -49%). Oczekiwane trafienia kuponów (p 36-51%): ok. 3,6 z 8; 2 to mało, ale to próba ośmiu zdarzeń, które nie są niezależne: te same trzy nogi (Dortmund, Bayern, Union) zabiły sześć kuponów. Liczone po unikalnych nogach bilans to powyższe 12/18, czyli zgodny z oczekiwaniem.

## Przyczyny pomyłek

1. **Bayern (2-2 w Augsburgu).** p 78% przy rynku 80%, ryzyko "Augsburg w formie (WWWDW)" nazwane wprost w dwóch plikach, i właśnie to się zdarzyło: Augsburg strzelił w 1', prowadził 2-1 w 64', Bayern wyrównał w 81'. Typ zrobił z tego jedną nogę dwóch kuponów (K2 w obu plikach). Wariancja.
2. **Chelsea Under 3.5 (5-1).** To jedyna pomyłka z sygnałem, który powinien był zmienić liczbę: Kupon 5 w pliku Ekstraklasa ostrzegał, że "Chelsea straciła 12 goli w 5 meczach", a p dla Under 3.5 pozostało na poziomie rynku (58%). Sygnał otwartych meczów mówi przeciw Under, a nie wpłynął na liczbę. Przeciw korekcie: linia rynkowa (DK) już zawiera tę formę, więc nie miałem informacji spoza rynku. Jedno zdarzenie z 42% nie uzasadnia nowej reguły.
3. **Union Over 2.5 (1-0, gol w 81').** Ryzyko ("4 gole w 4 meczach") nazwane, p = rynek. Wariancja.
4. **Raków lub remis (1-4 u siebie).** Dla Ekstraklasy brak danych o formie, więc p wyłącznie z Pinnacle (67%) i pewność tak opisana. Reszta typów z Ekstraklasy trafiła (8/9 łącznie z tym), więc to nie wzorzec. Jedyny mecz tej ligi, w którym faworyt przegrał wyraźnie.
5. **Dortmund (2-2, 2-0 w 85').** Patrz `Weryfikacja_Dortmund_Werder_2026-10-10.md`.
6. **Błąd procesu: "Ekstraklasa nie gra".** `Analiza_TOP5_kolejka_2026-10-09_12.md` i oba pliki `Top5_kupony*` stwierdzały, że Ekstraklasa w tym terminie nie gra (następna kolejka 23-25.10). W rzeczywistości 10. kolejka rozgrywana była 9-12.10 (9 meczów, w tym 9.10, 10.10 i 12.10; terminarz ligi pokazuje też przełożone mecze). Plik `Kupony_TOP5_Ekstraklasa_2026-10-09.md` to później poprawił, ale dwa pierwsze zestawy powstały na błędnej przesłance. Wniosek został wyciągnięty z numeracji kolejek, a nie z terminarza po dacie. Ten błąd nie wpłynął na wyniki typów (kupony TOP5 nie zawierały Ekstraklasy), ale odrzucił dziewięć meczów z analizy, w tym kilka z p 80%+ (Over 1.5), które okazały się trafione.

## Kalibracja skilli

- **`sports-fixtures-finder` - zmieniony** (jedyny błąd o charakterze procesu): dodana zasada "ligę krajową sprawdzaj po dacie, nie po numerze kolejki; wniosek 'liga nie gra' potwierdź terminarzem na każdą datę zakresu".
- **`football-analyst`, `bet-slip-builder` - bez zmian.** 12/18 przy oczekiwanych 12,5; ryzyka nazwane w analizach; p nie zawyżone ponad rynek; ujemne EV kuponów zostało powiedziane wprost. Przy Chelsea Under 3.5 (punkt 2) brakowało tylko korekty o sygnał już zawarty w rynku, a nie nowej informacji. Zmiana reguły po jednym zdarzeniu 42% byłaby dopasowaniem do szumu (ta sama zasada co w poprzednich weryfikacjach).

Do obserwacji w kolejnych weryfikacjach: trafność Under 3.5 (teraz 1/3; w tym weekendzie średnia goli w zakończonych meczach TOP5 + Ekstraklasa ok. 3,5 na mecz, a 9 z 20 meczów miało 4+ goli, czyli 45% przy p(4+) ok. 42% w analizach, więc zgodnie z oczekiwaniem).

## Do uzupełnienia po rozegraniu

10.10: Man Utd - Tottenham (w trakcie, 0-0), Leipzig - Frankfurt (w trakcie, 4-0), Inter - Parma, Napoli - Frosinone, Brest - Angers, Real Madrid - Villarreal, Jagiellonia - Górnik. 11.10: Betis - Osasuna, Freiburg - Schalke, Lazio - Monza, Rennes - Auxerre, Troyes - Marseille, Liverpool - Man City, Legia - Wisła Kraków, Everton - Hull, Köln - Gladbach. 12.10: Radomiak - Motor, Atalanta - Venezia. Nierozstrzygnięte kupony: Ekstraklasa Akt. 2 K1, K3; Top5_kupony K3, K4, K5; wynik_i_gole K4, K5.

To oszacowania, nie gwarancje; próba jest mała i nie ma jeszcze kompletu wyników.
