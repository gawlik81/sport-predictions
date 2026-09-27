# RC Deportivo vs Real Betis
**Rozgrywki:** La Liga (jornada 7) | **Termin:** niedziela 20.09.2026, ok. 18:30 (Estadio Municipal de Riazor; część źródeł podaje 13:30 — rozbieżność w harmonogramach, godzina do potwierdzenia bliżej meczu) | **Ranga meczu:** na papierze "mocniejszy vs. słabszy" (Betis 3. miejsce vs Deportivo 7.), ale pogłębiony research pokazuje mecz znacznie bardziej wyrównany niż sugeruje tabela

## Kontekst i forma
- **Forma Deportivo** (beniaminek, 7. miejsce, 9 pkt): 2W-3D-1L, 9:7 bramek, **niepokonani w 5 z 6 meczów** — jedyna porażka to 0-1 z Sevillą w ostatniej kolejce. **Pierre-Emerick Aubameyang strzelił w każdym z pierwszych 5 meczów ligowych klubu** — pierwszy taki wyczyn w LaLiga od Zlatana Ibrahimovicia w sezonie 2009/10. To kluczowy, bardzo aktualny sygnał ofensywny.
- **Forma Betisu** (3. miejsce, 15 pkt): 5W-0D-1L, 8:6 bramek, Pellegrini. Wygrali ostatnio 1-0 z Getafe. Solidna defensywa sezonowo, **ale straciła gola w każdym z ostatnich 3 meczów wyjazdowych** — realna rysa w wyjazdowej odporności defensywnej.
- **H2H**: brak istotnej świeżej historii bezpośrednich starć po awansie Deportivo — pomijam jako mało miarodajne.
- **Kadra**: Deportivo — Noe Carrillo wątpliwy, Angeliño nieobecny (linia obrony: Altimira, Loureiro, Giménez, Quagliata) — drużyna poza tym w komplecie. Betis — Aitor Ruibal (łąkotka) i Ismael Barea (więzadła, powrót nie wcześniej niż grudzień) nieobecni — to gracze drugiego planu, nie osłabiają kluczowego składu.
- **Rynek bukmacherski**: Betis notowany jako wyraźny faworyt (~2,10, ok. 47,6% implikowanego prawdopodobieństwa) — **mój model tego nie potwierdza** (patrz niżej), co samo w sobie jest istotną informacją.

## Model bazowy (oczekiwane gole)
Siła ataku/obrony względem średniej ligowej: Deportivo 1,5 gola/mecz strzelone, 1,17 stracone; Betis 1,33 strzelone, 1,00 stracone. Mimo przewagi Betisu w tabeli (6 pkt różnicy), surowe współczynniki wychodzą **niemal identyczne dla obu drużyn** — tabela myli, bo bierze pod uwagę wynik z Getafe i Realem Madryt, a nie specyficzną siłę Deportivo w Riazorze z gorącym w formie Aubameyangiem. Nie widzę podstaw do dalszej korekty w żadną stronę — model bazowy już odzwierciedla oba czynniki (forma Deportivo w górę, defensywna solidność Betisu w dół z uwagi na 3 mecze wyjazdowe ze stratą gola).

- λ(Deportivo) = 0,98, λ(Betis) = 1,02

## Model rożnych
Dane ograniczone: dostępna informacja to, że 9 z ostatnich 10 meczów Deportivo kończyło się poniżej 10 rożnych łącznie — sygnał niskorożnego meczu, ale bez pełnego rozbicia dom/wyjazd dla obu drużyn. **To przybliżenie z szerszym marginesem niepewności niż zwykle.**

- λ_rożne(Deportivo) = 4,5, λ_rożne(Betis) = 4,3

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Deportivo | 33,5% | 2,98 |
| Remis | 30,8% | 3,24 |
| Betis | 35,6% | 2,81 |

*Uzasadnienie: **to praktycznie trójstronny remis prawdopodobieństw — brak wyraźnego faworyta.** Pozycja w tabeli (3. vs 7.) sugeruje przewagę Betisu, ale forma strzelecka Deportivo (Aubameyang), niepokonana passa u siebie i wyraźna rysa w wyjazdowej obronie Betisu (gol stracony w 3 ostatnich meczach na wyjeździe) neutralizują tę przewagę niemal całkowicie.*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Deportivo więcej rożnych | 45,8% | 2,18 |
| Remis rożny | 13,6% | 7,34 |
| Betis więcej rożnych | 40,5% | 2,47 |
| Over 7,5 | 65,2% | 1,53 |
| Over 8,5 | 51,8% | 1,93 |

*Uzasadnienie: brak wyraźnej przewagi rożnej — spójne z ogólnym obrazem wyrównanego meczu.*

### Najbardziej prawdopodobne wyniki (gole)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 0-1 | 13,8% | 7,24 |
| 0-0 | 13,5% | 7,39 |
| 1-1 | 13,5% | 7,39 |
| 1-0 | 13,3% | 7,54 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1,5 | 59,4% | 1,68 |
| Over 2,5 | 32,3% | 3,09 |
| BTTS — Tak | 39,9% | 2,50 |

*Uzasadnienie: surowy model daje BTTS-Tak tylko 39,9%, ale to prawdopodobnie zaniżone — Aubameyang w świetnej formie strzeleckiej u siebie oraz udokumentowana skłonność Betisu do tracenia goli na wyjeździe (3/3 ostatnie mecze) sugerują realną wartość bliższą 50-55%. Sygnalizuję to jako korektę jakościową, której nie przełożyłem wprost na λ z uwagi na brak twardych danych do precyzyjnego przeliczenia — traktuj BTTS-Tak jako niedoszacowane przez model bazowy.*

### Faule i kartki
**Drużynowo:** dane sezonowe 2026/27 zbyt skąpe dla obu drużyn (Deportivo po awansie, krótki sezon), by policzyć rzetelną średnią — zaznaczam to wprost zamiast zgadywać. Betis w ub. sezonie należał do bardziej zdyscyplinowanych zespołów ligi (58 żółtych/29 meczów). Brak sygnału o zawodnikach na progu zawieszenia w żadnej z drużyn.

## Podsumowanie
**To jeden z trzech analizowanych meczów kolejki, ale — inaczej niż sugerowała wstępna triaż oparta na samej tabeli — pogłębiony research NIE potwierdza wyraźnego faworyta.** Aubameyang w historycznej formie strzeleckiej i niepokonana passa Deportivo w Riazorze realnie neutralizują przewagę tabelaryczną Betisu, a jego defensywa na wyjeździe ostatnio przecieka. Model 1X2 (33,5% / 30,8% / 35,6%) jest praktycznie płaski. **Najbezpieczniejszy typ to Over 1,5 gola (59,4%, kurs 1,68)** — ale to średnia, nie wysoka pewność. Rekomendacja: **ten mecz nie nadaje się jako "pewniak" tej kolejki** — pozycja w tabeli myli, rzeczywista siła obu drużyn w tym konkretnym starciu jest zbliżona.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
