# Weryfikacja: KSW 122 (Rzeszów) i UFC Fight Night Allen vs Duncan (Apex), 10.10.2026

Zweryfikowany plik: `ZWERYFIKOWANE_Gale_KSW122_UFC_Apex_2026-10-10.md` (wszystkie typowane walki rozstrzygnięte).

Źródła wyników: UFC.com (Main Card Results, scorecards), Fightful, ESPN, CBS Sports; PolsatSport.pl, mmarocks.pl, mma.pl (KSW 122); komunikat z ważenia: Lowking.pl, kswmma.com. Bleacher Report ma inną wersję części walk (Godínez - Kamaka, Tanzilovi - Meerschaert), więc nie użyłem go; wyniki oficjalne UFC i media polskie są spójne.

## Wyniki

| Walka | Typ | p | Wynik | Status |
|---|---|---|---|---|
| Godínez - Souza (UFC) | Godínez | 70% | Godínez, UD 29-28 x3 | ✅ |
| Camilo - Herbert (UFC) | Camilo | 63% | Herbert, UD 29-28 x3 | ❌ |
| Wellmaker - Tanzilovi (UFC) | Wellmaker | 62% | Tanzilovi, KO (kopnięcie w głowę) R2 2:39, jego pierwsza wygrana w UFC | ❌ |
| Fili - Kamaka III (UFC) | Fili | 57% | Fili, KO (kopnięcie w głowę) R2 0:22 | ✅ |
| Allen - Duncan (UFC, 5 rund) | brak typu | Allen ~54% (rynek), modele: Duncan | Allen, RNC R5 2:46 | - |
| Yakymenko - Morelli (KSW, pas) | Yakymenko | 62% | Yakymenko, dźwignia na kolano R5 (obrona pasa) | ✅ |
| Makarowski - Soldaev (KSW) | Soldaev (po korekcie) | ~65% | Soldaev, KO prawym R1 | ✅ |
| Zerhouni - Grzebyk (KSW) | brak typu | 51/49 | Grzebyk, majority decision 28-28, 29-27, 29-27 | - |

**Bilans: 4/6 typów.** Oczekiwane trafienia z podanych p: 3,8. Kalibracja w normie przy próbie 6 walk.

**Kupony:**
1. Godínez ✅ + Camilo ❌ (kurs ~2.16) → ❌
2. Wellmaker ❌ + Yakymenko ✅ (kurs ~2.2, drugi kurs założony) → ❌

Flat stake 1 j. na każdy: -2 j. Oba kupony przegrały przez jedną nogę z p 62-63% (obaj zawodnicy byli faworytami wg rynku), tak jak w pierwszych cyklach tenisowych.

## Analiza pomyłek

### 1. Camilo - Herbert (63%, ❌) i Wellmaker - Tanzilovi (62%, ❌)
Oba typy miały pewność "niska-średnia" i p niemal równe rynkowi (64% i 64%; moje 63% i 62%, czyli bez przewagi). Plik wprost mówił o ograniczeniach: brak statystyk kariery (bot-challenge MCP), kursy tylko z artykułów, rozbieżne między źródłami. Camilo przegrał minimalnie (29-28 u wszystkich sędziów), a Wellmaker (2 porażki z rzędu, nazwane w pliku) przegrał KO po kopnięciu w głowę z rywalem bez wygranej w UFC. Przy tak małej próbie i bez statystyk obie porażki mieszczą się w niepewności 36-38%. **Wniosek: wariancja, bez zmiany reguł.**

### 2. Przekroczenie wagi w KSW: błąd w ocenie, ale bez kosztu dla typów
Komunikat z ważenia (9.10, dzień przed galą) mówił wprost: Soldaev (+0,9 kg), Zając (+5 lb) i Zerhouni (+1,2 kg) tracą 30-50% gaży i **zaczynają walkę z punktem ujemnym**. Analiza:
- **Soldaev:** obniżyła model z 76% do ~65% (-11 pp) za samo przekroczenie wagi. Soldaev wygrał KO w 1. rundzie. Typ przeszedł, ale korekta była duża i nieuzasadniona liczbami: punkt ujemny nic nie zmienia przy KO, a efekt fizyczny jest niepewny (Zając też przekroczył wagę o ok. 2,6 kg i zakończył walkę w 1. rundzie).
- **Zerhouni - Grzebyk:** analiza stwierdziła, że przekroczenie wagi "jest bez znaczenia dla wyniku", a nie wzięła pod uwagę punktu ujemnego. Walka poszła na punkty (majority decision 28-28, 29-27, 29-27), a punkt ujemny przy walce wyrównanej (51/49) i sporej szansie na decyzję to realna przewaga rywala. Nie wiem, czy punkt rozstrzygnął, ale w tak wyrównanym pojedynku mógł. Typu nie było, więc kosztu nie ma, ale to luka analityczna.
Wynik 2 z 3 przekraczających wagę wygrało, obaj przez finisz w 1. rundzie.

### 3. Główne źródło ryzyka: brak statystyk UFC
`ufc_*` zwróciło stronę z bot-challenge, a analiza nie sięgnęła po ufcstats.com/Tapology/Sherdog; zostały artykuły i modele bukmacherskie. Skutek: p ≈ rynek, pewność obniżona, rynki sposobu wygranej i rund pominięte (poprawnie wg skilla). Wynik 4/6 nie pozwala ocenić, czy statystyki pomogłyby, ale każdy z typów, w których poszedłem za rynkiem, opierał się wyłącznie na kursach.

### Co zadziałało
- **Brak typu w Allen - Duncan:** rynek miał Allena ~54%, modele Duncana 52-63%, a Allen zakończył walkę w 5. rundzie. Odrzucenie jako "zbyt niepewna" było zgodne z regułą.
- **Yakymenko 62%:** obrona pasa w 5. rundzie z dźwigni, więc niska pewność i p blisko 60% dobrze oddały wyrównany przebieg.
- **Fili 57% (niska):** KO w 2. rundzie, trafione, ale z niską pewnością; nie wnosi wniosku.

## Kalibracja skilli (`mma-analyst`)

Dwie zmiany w `.claude/skills/mma-analyst/SKILL.md`:
1. **Ważenie:** dotychczasowa reguła ("przesuń p o kilka pp") rozdzielona na dwa efekty: punkt ujemny (KSW; działa przy decyzji, przesuń `da`, nie pisz "bez znaczenia") i efekt fizyczny (niepewny, maks. ~5 pp na p zwycięzcy bez konkretnej informacji). Uzasadnienie: Zerhouni - Grzebyk (kara pominięta) i Soldaev (korekta -11 pp przy KO w R1). Próba to 3 zawodników, więc reguła opisuje mechanikę kary i nie przesądza o sile efektu fizycznego.
2. **MCP `ufc_*` z bot-challenge:** dodane fallback do ufcstats.com/Tapology/Sherdog przez WebFetch/WebSearch, zamiast zostawiać p równe rynkowi z powodu braku statystyk.

Bez zmian: pułapy p, reguły zastępstw, długiej przerwy i rynków dodatkowych: za mało danych (nie było takich przypadków z weryfikowalnym wynikiem).

To oszacowania, nie gwarancje; próba 6 walk jest bardzo mała, a reguły MMA nadal wstępne.
