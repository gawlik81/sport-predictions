# Valencia - Real Madryt (LaLiga, 12. kolejka, 07.11.2026, 21:00 czasu polskiego, Mestalla)

Superbet event_id: 14454002. Kursy z publicznego API Superbet (stan ok. 20:00 PL, ruszają się).

## Typ główny
**Real Madryt wygra** | p ≈ 71% | fair 1.41 | pewność: średnia | kurs Superbet 1.28 (EV ≈ -9%, brak value)

## Dane
- **Tabela:** Valencia 19. (9 pkt/11 m., 8 goli - najgorszy atak ligi, Aguirre), Real 3. (9 W, 2 L, 3 pkt za Barceloną, Mourinho). Źródło: Sports Mole.
- **Forma Valencia (od najnowszego):** W 1-0 Elche, L 1-2 Villarreal, D 0-0 Athletic, D 2-2 Racing, L 2-3 Real Sociedad.
- **Forma Real:** 7 wygranych z rzędu we wszystkich rozgrywkach (3-2 AEK, 3-0 Racing, 2-1 Barcelona, 4-1 Leipzig, 4-1 Sevilla).
- **Absencje Valencia:** Canos, D. Lopez, Otorbi (kontuzje), Copete wątpliwy; Sadiq wrócił.
- **Absencje Real:** Rodrygo, Asencio, Mendy (kontuzje), Vinicius (ostatni mecz zawieszenia). Spodziewany skład: Courtois; Valverde, Konate, Huijsen, Cucurella; Tchouameni, Bernardo; Guler, Bellingham, Diomande; Mbappe.
- **H2H:** brak wiarygodnych danych z ostatnich 3 lat w tym researchu - nie ważone.
- **Sędzia:** nieznany (nie znaleziono obsady) - rynki kartek/fauli bez typu.

## Model
λ Valencia 0.8, λ Real 2.3 (skalibrowane do rynku; wersja 0.75/2.05 schodziła >5 pp pod rynek bez konkretnej informacji, co łamie regułę z SKILL.md).

| Rynek | p | fair | kurs Superbet | EV |
|---|---|---|---|---|
| Real wygra | 71,1% | 1.41 | 1.28 | -9% |
| Remis | 17,5% | 5.71 | 6.00 | +5% (p<50%) |
| Real -1.5 (handicap) | 47,8% | 2.09 | 1.74 | -17% |
| Real -2.5 | 26,7% | 3.75 | 2.77 | -26% |
| Over 2.5 | 59,9% | 1.67 | 1.48 | -11% |
| Over 3.5 | 37,5% | 2.67 | 2.20 | -17% |
| BTTS tak | 49,5% | 2.02 | 1.88 | -7% |
| Valencia 0 goli | 44,9% | 2.23 | 2.02 | -9% |

Ryzyka typu głównego: remis (17,5%) i wygrana Valencia (11,4%) - zmęczenie Realu pucharami i rotacja przy 7 meczach z rzędu, desperacja gospodarzy na dnie tabeli.

## Kupon z kursem > 2
Przeszukano 11 kombinacji Superbet z wynikiem i golami wycenialnych modelem. Najlepsza:
**Poniżej 5.5 gola w meczu + Valencia strzeli powyżej 0.5 gola, kurs 2.05, p ≈ 47%, EV ≈ -4%.**
Żadna kombinacja z kursem > 2 nie ma dodatniego EV ani p > 50%, więc **wg progów projektu nie ma kuponu do zagrania** (nie fabrykuję typu).

*To oszacowania probabilistyczne, nie gwarancje.*
