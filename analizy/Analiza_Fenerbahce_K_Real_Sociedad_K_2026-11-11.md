# Fenerbahce (K) - Real Sociedad (K), UEFA Women's Europa Cup, rewanż, 11.11.2026 18:00 (PL)

Superbet event_id 15658035. Analiza zwięzła (mało czasu przed startem). Źródła: connector superbet-mcp (składy oficjalne, statystyki przedmeczowe, H2H, kursy); `superbet_missing_players` zwróciło "Brak danych" (rezerwy nie sprawdzano ze względu na czas, więc absencje są niepotwierdzone).

## Kontekst
- Pierwszy mecz (28.10): Real Sociedad - Fenerbahce 2:0 (czerwona kartka w meczu). Real prowadzi w dwumeczu 2:0 (awans Real 1.006).
- Fenerbahce: 1:0 z Galatasaray (07.11), 0:8 w Giresun (01.11), 5:0 z Haymana (24.10), 1:1 z Yuksekova - wyniki głównie ze słabymi rywalami krajowymi. Średnia w pucharze: 1,7 gola strzelonego i 1,0 straconego (próbka 2 meczów).
- Real Sociedad: Eibar 1:2 (wyjazd, wygrana), Alaves 1:1, Espanyol 1:1, Barcelona 2:1, Valencia 0:1 (wyjazd, wygrana). Straciła gola w 4 z 5 ostatnich ligowych meczów, w pucharze średnio 2,0 gola strzelonego, 18,5 strzału i 61,5% posiadania.
- Składy oficjalne (connector): Fenerbahce 4-2-3-1, Real 4-1-4-1, obie w mocnych jedenastkach (3 zawodniczki ofensywne po stronie Fenerbahce w XI).
- Sędzia: Michaela Pachtova (CZE); brak statystyk kartek, więc rynków kartek nie wyceniam.

## Model (poisson.py, λ gosp. 1,05 / goście 1,65)
| Rynek | p modelu | Fair | Kurs Superbet (z marżą) |
|---|---|---|---|
| 1 / X / 2 | 24,1 / 24,5 / 51,4% | 4,14 / 4,08 / 1,95 | 4,70 / 3,85 / 1,54 (bez marży ok. 19 / 23 / 58%) |
| Over 2.5 | 50,6% | 1,97 | 1,66 |
| BTTS tak | 52,5% | 1,90 | 1,75 |
| Rożne Over 8.5 (średnia 9-9,5) | 53-59% | 1,7-1,9 | 1,69 |

Model schodzi pod rynek na zwycięstwie Realu o ok. 6 pp, bez konkretnej informacji kadrowej, więc wynik 1X2 traktuję jako zgodny z rynkiem (rynek bywa trafniejszy). Real prowadzi 2:0 i może grać zachowawczo, Fenerbahce musi atakować: to podnosi szansę Fenerbahce na gola, ale też kontr Realu.

## Najlepszy rynek: Poniżej 4.5 gola; Fenerbahce strzeli powyżej 0.5 gola (kurs 1.85)
- P(Fenerbahce strzeli) ok. 60-65% (λ 0,92-1,05; rynek po usunięciu marży ok. 59%); odjęcie scenariusza 5+ goli (ok. 2-3%) daje p kuponu **ok. 55-63%**, środek ok. 59%.
- Fair odds ok. 1,70 (1,59-1,82); kurs 1.85 → **EV ok. +9% (zakres +2% do +17%)**.
- Pewność: **średnia** (próbka statystyk 2 mecze, brak potwierdzonych absencji, Fenerbahce strzelała głównie słabszym rywalom, pierwszy mecz 0:2).
- Ryzyka: Real broni 2:0 i zamyka grę (0:1, 0:2, 0:0 łącznie ok. 30%); wysoka klasa obrony Realu.

## Pozostałe typy
- Over 8.5 rożnych: p ok. 53-59% przy kursie 1.69, EV ok. -10% do 0% - brak przewagi.
- Zwycięstwo Realu 1.54: p ok. 51-58%, EV ujemne/zerowe - brak przewagi.

Oszacowania probabilistyczne, nie gwarancje.
