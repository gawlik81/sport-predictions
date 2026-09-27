# Weryfikacja predykcji z 24.09.2026 (Liga Narodów + WTA/ATP Azja)

Źródło predykcji: `Top10_predykcje_2026-09-24.md` (wersja końcowa: bez Ruse–Ku, z typem Kosowo–Irlandia Over 7,5 rożnych).

## Ranking TOP 10 — wynik

| # | Mecz | Typ | Prawd. | Wynik | Status |
|---|------|-----|--------|-------|--------|
| 1 | Hurkacz – Szewczenko | Hurkacz wygrywa | 83,9% | 6-3 7-6(10) | ✅ |
| 2 | Andora – Malta | Under 2,5 gola | 79,6% | 1-2 (gol Malty na 2-1 w 81') | ❌ |
| 3 | Sakkari – Hibino | Sakkari wygrywa | 85,6% | 7-5 6-1 | ✅ |
| 4 | Portugalia – Walia | Portugalia wykona więcej rożnych | 83,6% | brak danych o rożnych (strzały 22-5 dla Portugalii) | ❔ prawdopodobnie ✅, niezweryfikowane |
| 5 | Austria – Izrael | Over 1,5 gola | 78,5% | 3-1 | ✅ |
| 6 | Norwegia – Dania | Over 1,5 gola | 78,5% | 3-2 | ✅ |
| 7 | Holandia – Niemcy | Over 1,5 gola | 76,0% | 1-1 (wyrównanie w 90+2') | ✅ |
| 8 | Serbia – Grecja | Under 2,5 gola | 67,7% | 1-2 (gol na 1-2 w 90+5') | ❌ |
| 9 | Kosowo – Irlandia | Over 7,5 rożnych | 71,0% | brak wiarygodnych danych o rożnych | ❔ niezweryfikowane |
| 10 | Portugalia – Walia | 1 (Portugalia) | 64,5% | 1-0 | ✅ |

**Bilans rozstrzygniętych: 6/8 (75%).** Oczekiwana liczba trafień wg modelu dla tych 8 typów wynosiła ok. 6,2, więc wynik zgadza się z oczekiwaniem. Dwa typy rożnych są nie do sprawdzenia: Sofascore podaje dla meczu Kosowo–Irlandia strzały 22-3 i xG 2,22 do 0,28, ale bez liczby rożnych. Potwierdza się uwaga z Kroku 2b pkt 4 skilla piłkarskiego.

Usunięty na życzenie typ **Ruse – Ku (74,7%)** wszedłby, choć ledwo: Ruse wygrała 2-6 7-6(1) 6-1, a przegrywała 6-2, 4-2.

## Szersza kontrola modeli (wszystkie przeanalizowane mecze)

### Piłka nożna — 1X2 i gole

| Mecz | Faworyt modelu | λ łącznie | Wynik | Faworyt wygrał? | Gole: realnie vs model |
|---|---|---|---|---|---|
| Holandia – Niemcy | Holandia 40,6% | 2,75 | 1-1 | ❌ (remis) | 2 vs 2,75 |
| Portugalia – Walia | Portugalia 64,5% | 2,55 | 1-0 | ✅ | 1 vs 2,55 |
| Norwegia – Dania | Norwegia 51,4% | 2,90 | 3-2 | ✅ | 5 vs 2,90 |
| Serbia – Grecja | brak (34,6 / 30,9 / 34,6) | 2,00 | 1-2 | — | 3 vs 2,00 |
| Austria – Izrael | Austria 60,3% | 2,90 | 3-1 | ✅ | 4 vs 2,90 |
| Kosowo – Irlandia | Kosowo 39,4% | 2,25 | 1-0 | ✅ | 1 vs 2,25 |
| Andora – Malta | Malta 45,6% | 1,55 | 1-2 | ✅ | 3 vs 1,55 |
| Liechtenstein – Litwa | Litwa 64,7% | 2,00 | 0-2 | ✅ | 2 vs 2,00 |

- **1X2:** faworyt modelu wygrał w 6 z 7 meczów, w których model wskazał faworyta. Jedyny wyjątek to remis Holandia–Niemcy.
- **Gole:** średnio 2,63 na mecz wobec 2,36 z modelu. **Model najbardziej zaniżył mecze o najniższym λ:** Andora–Malta (1,55 → 3 gole) i Serbia–Grecja (2,00 → 3 gole). Obie korekty λ w dół okazały się przesadzone. Andora, której λ wynosił 0,55 („nie strzela w 6 z 7 meczów”), strzeliła w 17. minucie. Serbia po korekcie -20% za brak napastników strzeliła w 4. minucie.
- **Późne gole:** w meczach reprezentacji rozstrzygały końcówki. 3 z 8 meczów miały gol w 90+ minucie (Holandia–Niemcy, Serbia–Grecja, Austria–Izrael), a oba typy Under przegrały przez gole po 80. minucie.
- **Over 1,5:** 3/3 w rankingu, a 6/8 we wszystkich meczach dnia.
- **Litwa, rozbieżność model–rynek:** model dał 64,7%, rynek ok. 79%. Litwa wygrała pewnie 2-0, więc racja była po stronie rynku. Obniżyłem λ Litwy za jej własny „kryzys wynikowy”, ale reguła kryzysu z Kroku 2b dotyczy kryzysowego *underdoga*, nie faworyta. To było błędne zastosowanie reguły.

### Tenis — zwycięzcy i total gemów

| Mecz | Faworyt (model) | Wynik | Status | Gemy: realnie vs model |
|---|---|---|---|---|
| Hurkacz – Szewczenko | Hurkacz 83,9% | 6-3 7-6(10) | ✅ | 22 vs 23,6 |
| Sakkari – Hibino | Sakkari 85,6% | 7-5 6-1 | ✅ | 19 vs 22,2 |
| **Eala – Prozorova** | **Eala 90,8%** | **4-6 7-5 6-3 dla Prozorovej** | **❌** | 31 vs 21,2 |
| Ruse – Ku | Ruse 74,7% | 2-6 7-6(1) 6-1 | ✅ (o włos) | 28 vs 23,4 |
| Marozsán – Bolt | Marozsán 73,8% | 6-4 6-2 | ✅ | 18 vs 24,2 |
| Vallejo – Cui | Vallejo 69,7% | 6-1 6-7(2) 6-4 | ✅ | 30 vs 24,3 |
| Ostapenko – Preston | Ostapenko 60,5% | 4-6 1-6 | ❌ (ryzyko oflagowane, typ pominięty) | 17 vs 24,1 |
| Shapovalov – Griekspoor | Shapovalov 54,9% | 6-4 7-6(3) | ✅ | 23 vs 25,7 |

- **Zwycięzcy:** 6/8. Obie porażki faworytów padły w WTA.
- **Eala – największy błąd dnia.** Eala była rozstawiona z nr 3, miała wolny los i wróciła po ok. 3 tygodniach przerwy od US Open. Model dał jej 90,8%, a przegrała z nr 180 po prowadzeniu 1 set i 4-2. Research zaliczył „2 h 51 min maratonu” Prozorovej do jej ryzyk. W praktyce rytm meczowy i pewność siebie underdoga przeważyły nad zmęczeniem, a brak rytmu faworytki po przerwie nie był w ogóle skorygowany.
- **Ostapenko:** flaga kryzysu formy (9-13 na twardej) okazała się trafna. Pominięcie typu było słuszne.
- **Total gemów przy szacunkowych p_serve jest nieprzydatny.** Błąd bezwzględny wynosił średnio ok. 5 gemów (od -7 do +10). Przy p_serve szacowanych z rankingu, bez rzeczywistych statystyk serwisu i returnu, model dobrze wskazuje faworyta, ale nie trafia w dynamikę meczu. Wpisanie tego typu do rankingu byłoby losowe.

## Wnioski wdrożone do skilli

1. **football-predictor (Krok 2b, nowy pkt 5): mecze reprezentacji.**
   - Nie obniżaj λ słabego ataku poniżej ok. 0,7 i nie kumuluj korekt kadrowych w dół powyżej ok. 15%.
   - Typ Under 2,5 przy łącznym λ ≤ 2,0 ma najwyżej średnią pewność. Preferuj Over 1,5.
2. **football-predictor (Krok 2b, nowy pkt 6).** Korekta „kryzysowa” dotyczy tylko underdoga. Nie stosuj jej do faworyta, gdy rywal jest wyraźnie słabszy. Przy rozbieżności z rynkiem powyżej 10 pp w meczu o dużej różnicy klas zaznacz, że rynek bywa lepiej skalibrowany.
3. **tennis-predictor (nowy Krok 2b): kalibracja.**
   - Obniż pewność faworyta grającego pierwszy mecz po wolnym losie lub dłuższej przerwie, jeśli rywal ma rytm meczowy.
   - Nie traktuj zmęczenia underdoga po maratonie jako mocnego argumentu za faworytem.
   - Nie typuj total gemów, gdy p_serve jest tylko szacunkowe.
   - Flaga kryzysu formy faworyta działa, więc ją zachowujemy.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
