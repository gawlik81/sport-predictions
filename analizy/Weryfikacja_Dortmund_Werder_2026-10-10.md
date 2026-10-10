# Weryfikacja: Dortmund - Werder (Bundesliga, 09.10.2026)

Zweryfikowany plik: `Dortmund_Werder_2026-10-09.md` (wycena przed i po składach, 2 + 3 kupony jednomeczowe).

Wynik: **Dortmund 2-2 Werder** (0-0 do przerwy). Gole od 80' do 90'+2: 1-0 Svensson 80', 2-0 Schlotterbeck 85' (głową po rożnym), 2-1 Reis 88' (po błędzie Schlotterbecka), 2-2 Füllkrug 90'+2 (głową po wolnym Grülla). Statystyki wg Sofascore/livescore: xG 2,42 - 1,13, strzały 21:11, posiadanie 72%, 9 rożnych Dortmundu.
Źródła: OpenLigaDB (wynik, minuty goli), livescore.com i Sofascore (xG, strzały, przebieg), ESPN. Uwaga: strona ESPN podaje niespójną listę strzelców (Silva, Wójcik zamiast Svensson, Reis, Füllkrug) i jej statystyk nie użyłem; wynik i minuty potwierdza OpenLigaDB. Kartek i rożnych Werderu nie znalazłem (analiza ich nie typowała).

## Typy z analizy

| Typ | p | Wynik |
|---|---|---|
| Dortmund wygra | 69-72% | ❌ |
| Dortmund lub remis | 88% | ✅ |
| Dortmund bez remisu (DNB) | 86% | zwrot stawki |
| Over 1.5 gola | 85% | ✅ |
| Dortmund strzeli 2+ gole | 71% | ✅ |
| Over 2.5 | 64-66% | ✅ |
| Werder strzeli | 59% | ✅ |
| BTTS tak | 54-56% | ✅ |
| Under 3.5 | 56% | ❌ (4 gole) |
| Dortmund wygra 2+ (AH -1.5) | 50% | ❌ |
| Over 3.5 | 42-44% | ✅ |
| Dortmund strzeli 3+ gole | 46% | ❌ |
| Füllkrug strzeli gola | ok. 30% | ✅ |
| Guirassy strzeli gola | ok. 42% | ❌ |
| Remis / Werder wygra | 16-18% / 11-14% | remis zaszedł |

Rynki strzałów zawodników (Guirassy Over 2.5, Füllkrug Over 1.5) pozostają niezweryfikowane: nie znalazłem wiarygodnych statystyk indywidualnych.

**Kupony: wszystkie 5 ❌** (A: AH -1.5 + Over 3.5; B: wygra + BTTS + Over 3.5; 1: AH -1.5 + Over 3.5; 2: wygra + Over 2.5 + Guirassy; 3: wygra + BTTS + Over 3.5). Każda noga kuponów wymagała zwycięstwa Dortmundu, więc jeden scenariusz (remis, p ok. 18%) zabił wszystkie naraz.

Typy goli (Over 1.5/2.5/3.5, BTTS, Dortmund 2+) trafiły; przegrały dokładnie te, które wymagały wygranej Dortmundu: wygrana, AH -1.5, Dortmund 3+, kupony. Model goli (λ 2,35 + 0,95 = 3,3 vs 4 gole) był dobry, błąd leży w wyniku.

## Przyczyna pomyłki

1. **Wariancja końcówki, nie błąd w analizie.** Dortmund prowadził 2-0 w 85' (przy 2-0 w 85' remis wymagał dwóch goli Werderu w kilka minut, czyli zdarzenia rzędu kilku procent; to moje przybliżenie, nie wynik modelu) i stracił dwa gole w 88' i 90'+2, w tym jeden po własnym błędzie Schlotterbecka. xG 2,42:1,13, 21:11 strzałów i 72% posiadania wskazują, że Dortmund był lepszy i wynik nie wynikał z błędnej oceny siły drużyn. Remis (18%) był w analizie wprost jako ryzyko.
2. **p pochodziło z rynku, więc nie było przewagi.** Analiza sama to pisała ("p pochodzi z rynku", EV bliskie zera lub ujemne) i nie rekomendowała typów jako value.
3. **Zgodnie z regułą "ryzyko ma dwie twarze":** remis i wygrana underdoga (11-14%) wymienione, plus zastrzeżenie, że Dortmund stracił 4 gole w 5 meczach. Zrealizowało się to pierwsze.
4. **Skład nie zmienił obrazu:** Werder wyszedł prawie takim samym składem (w 19' Pieper zszedł z urazem), Dortmund zagrał bez niespodzianek. Przeciw Dortmundowi działał tylko przebieg ostatnich minut.
5. **Kupony zbudowane na jednym scenariuszu.** To nie błąd skilla: `bet-slip-builder` normalnie wymaga jednej nogi na mecz, a kupony jednomeczowe powstały na wyraźną prośbę użytkownika ("kurs > 3, jeden mecz"). Plik uczciwie zaznaczał, że to zakłady na wysoką wygraną gospodarzy, nie "pewniaki".

## Kalibracja skilli

**Brak zmian w `SKILL.md`.** Uzasadnienie: żadna reguła nie została naruszona i żadna nie była luką. Remis i wygrana underdoga były uwzględnione, korekta nie schodziła poniżej rynku, p nie było zawyżone ponad rynek. Zmiana reguły po jednym zdarzeniu o prawdopodobieństwie 18% (plus korelacja nóg kuponu, która jest cechą wybranego formatu) byłaby dopasowaniem do szumu, tak jak przy tym samym meczu w `Weryfikacja_predykcji_2026-10-10.md`.

Do obserwacji: Dortmund w obu analizach tego meczu (TOP z 08.10 i ta analiza) miał p 69-70% i oba zestawienia zakończyły się remisem; to jedno zdarzenie, nie dwa. Jeśli w kolejnych weryfikacjach faworyci piłkarscy z p 70-75% będą regularnie remisować częściej niż 18-20%, wtedy warto przesunąć wagę remisu w `football-analyst`.

To oszacowania, nie gwarancje.
