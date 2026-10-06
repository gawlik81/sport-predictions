# Trzy typy value na wieczór — 06.10.2026 (Liga Narodów, 20:45)

Przygotowane o 20:30 CEST.

**Value** oznacza tu prawdopodobieństwo z modelu × kurs > 1. Model to Poisson z porannego pliku `TOP100_i_Superkupon_multisport_2026-10-06.md`. W tym oknie value wychodzi tylko na Under 2,5. Wynika z tego, że obniżyłem λ za braki ofensywne, czego rynek w kursie nie uwzględnia w pełni.

Zgodnie z regułą 5 skilla Under 2,5 w meczach reprezentacji może mieć **najwyżej średnią pewność**:
- weryfikacja z 24.09: model zaniżał gole o ok. 0,3 na mecz;
- weryfikacja z 26.09: Under wszedł w 4 z 5 meczów.

Dlatego przy każdym typie podaję **kurs minimalny**. Poniżej niego typ nie ma value.

| # | Mecz | Typ | Model | Kurs | Kurs min. | EV | Pewność |
|---|---|---|---|---|---|---|---|
| 1 | Chorwacja – Hiszpania | **Under 2,5 gola** | 40,1% | 2,74 ✓ | 2,60 | 1,10 | Niska/średnia |
| 2 | Szkocja – Słowenia | **Under 2,5 gola** | 62,3% | szac. ~1,70-1,75 | 1,70 | ~1,06-1,09 | Średnia |
| 3 | Luksemburg – Bułgaria | **Under 2,5 gola** | 66,3% | szac. ~1,60-1,65 | 1,60 | ~1,06-1,09 | Średnia |

✓ — kurs z zapowiedzi (weszlo). Kursy 2 i 3 to szacunek, bo Betclic jest zablokowany przez proxy. Sprawdź je u bukmachera.

## Uzasadnienie

**1. Chorwacja–Hiszpania, Under 2,5 @2,74**
- λ 0,90 : 2,20.
- Hiszpanii brakuje Ferrana Torresa, Nico Williamsa i Grimaldo.
- Chorwacja po 0-7 z Anglią (najwyższa porażka w historii) zagra zapewne niskim blokiem. Bilić zapowiedział zmiany: Šutalo w obronie, Vlašić, Matanović.
- Rynek (O2,5 @1,43) wycenia mecz jak zwykłe spotkanie Hiszpanii.
- **Ryzyko:**
  - w poprzednich meczach Hiszpania strzelała 3 gole (3-2 z Anglią, 3-1 z Czechami);
  - przy λ dopasowanym do kursu na zwycięstwo Hiszpanii 1,28 model daje Under 2,5 tylko 35,9%, czyli EV 0,98. Value zależy więc wyłącznie od korekty za braki.
- To typ o najwyższym EV, ale najmniej pewny. Tylko na małą stawkę.

**2. Szkocja–Słowenia, Under 2,5**
- λ 1,35 : 0,85, łącznie 2,2.
- Szkocja ma nowego trenera (Pocognoli). Brakuje McTominaya, Adamsa i Shanklanda, czyli trzech głównych źródeł goli.
- Słowenia gra bez Šeška.
- Kursy 1X2 (1,80 / 3,40 / 4,55) wskazują na mecz o niskim tempie.
- Ryzyko: Over 1,5 ma w modelu 64,5%, więc wynik 2-1 lub 3-0 jest realny.

**3. Luksemburg–Bułgaria, Under 2,5**
- λ 1,15 : 0,90, łącznie 2,05.
- Luksemburgowi brakuje Barreiro (zawieszony, strzelił gola w pierwszym meczu) i Mahmutovicia (zawieszony) oraz kontuzjowanych Sinaniego, Martinsa, Koraca i Jansa.
- Bułgarii brakuje zawieszonych L. Petkova i Velkovskiego. M. Petkov i T. Ivanov wyjechali ze zgrupowania.
- Zapowiedzi zgodnie wskazują wygraną jedną bramką i Under 2,5.
- Ryzyko: pierwszy mecz skończył się 2-1 (3 gole), a Luksemburg oddał w nim 15 strzałów.

## Świadomie odrzucone (pozorne value)

- **Wygrana Chorwacji @9,20** (EV 1,30), **wygrana Słowenii @4,55** (EV 1,07) i **wygrana Estonii @~5,20** (EV 1,14). Reguła 7 skilla mówi, że value na underdoga w meczach reprezentacji typuje się jako X2 lub +1,5, a nie jako zwycięstwo. Takie typy dały 0/3 w weryfikacji z 26.09. Wersje X2 i +1,5 nie mają value przy szacowanych kursach.
- **Anglia–Czechy, Under 2,5 @3,05** (model 37%, EV 1,13). Anglia strzeliła 9 goli w dwóch ostatnich meczach, a przy korekcie +0,3 gola z weryfikacji EV spada do ok. 0,98.
- **Argentyna–Benin, Under 3,5 @3,20** (model 45%, EV 1,45). Model odbiega od rynku o ponad 20 pp w meczu o ogromnej różnicy klas, a według reguły 6 w takich sytuacjach rynek bywał trafniejszy. Dodatkowo to pożegnanie Messiego, a Argentyna wygrała ostatnie mecze 7-0 i 4-0.

Typy są skorelowane, bo wszystkie zakładają mało goli w meczach reprezentacji. Graj je jako pojedyncze zakłady, nie na jednym kuponie.

*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
