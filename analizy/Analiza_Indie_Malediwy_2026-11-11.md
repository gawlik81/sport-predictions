# Indie - Malediwy (SAFF Championship 2026, grupa B, Dhaka), 11.11.2026, 10:30 (czas polski)

Superbet event_id 15657817. Reprezentacje seniorskie: pewność obniżona o jeden poziom. Źródła: connector superbet (kursy, H2H, forma, średnie) oraz rezerwa WebSearch (kontekst turnieju). Sędzia: brak danych. Składy: brak danych (status "brak"). Nieobecni: brak danych w connectorze.

## Dane
- **Forma Indii (connector):** Pakistan 2:3 Indie (05.11, otwarcie SAFF), wcześniej towarzyskie: 1:6 Urugwaj, 0:4 Brazylia, 1:1 Panama, dwa mecze z Tadżykistanem 1:3 i 1:1, 0:1 Zimbabwe, 0:2 Jamajka, 2:1 Hongkong. Gole: 11 strzelonych i 20 straconych w 10 meczach, ale część z rywalami o dużo wyższej klasie.
- **Forma Malediw (connector):** 0:3 Pakistan (08.11), 0:6 Liban, 0:5 Kirgistan, 0:3 Chiny, 1:1 Bangladesz U23, 0:3 Pakistan, 0:1 Afganistan, 2:1 Timor Wschodni, 0:2 Filipiny, 0:3 Tadżykistan. Gole strzelone w 3 z 10 ostatnich meczów.
- **H2H:** od 2006 bilans 5-0-1 dla Indii, ostatni mecz 3:0 (marzec 2025).
- **Kontekst (WebSearch):** Indie mają 28-osobową kadrę na SAFF, a trzech zawodników z tej kadry powołano na towarzyski mecz z Nową Zelandią (12.11), więc skład na Malediwy jest osłabiony i niepotwierdzony. Pakistan pokonał Malediwy 3:0, a Indie Pakistan tylko 3:2.
- **Statystyki sezonowe (connector):** próba to jeden mecz (Indie 3 gole, 14 strzałów, 10 rożnych), więc bez wartości predykcyjnej.

## Model
Przyjęto λ Indii 2,3-2,6 i λ Malediw 0,7 (dolna granica dla reprezentacji, zasada skilla). `poisson.py 2.3 0.7`:

| Rynek | p (λ 2,3/0,7) | p (λ 2,6/0,7) | Rynek Superbet (kurs) | Rynek bez marży (ok.) |
|---|---|---|---|---|
| Indie wygrają | 73,5% | 78,1% | 1.10 | ok. 87% |
| Remis | 16,9% | 14,1% | 7.70 | ok. 11% |
| Malediwy wygrają | 9,7% | 7,7% | 14.00 | ok. 6% |
| Powyżej 2.5 gola | 57,7% | 64,1% | 1.37 | ok. 69% |
| Powyżej 3.5 gola | 35,3% | 42,0% | 2.00 | ok. 48% |
| BTTS tak | 45,3% | 46,6% | 2.32 | ok. 41% |

Rynek jest o ok. 10-14 pp pewniejszy w zwycięstwie Indii niż mój model. Powód rozbieżności: nie mam konkretnej informacji kadrowej (składu), która uzasadniałaby zejście pod rynek, ale nie mam też informacji, która uzasadniałaby pójście za nim (Indie osłabione, słaba forma, 2 stracone gole z Pakistanem). Zgodnie z zasadą skilla traktuję to jako sygnał niskiej pewności, nie jako value.

## Kandydaci na kupon (kurs > 2.0), wycena przy λ 2,0/0,6 → 3,0/0,6

| Kupon | Kurs Superbet | p (zakres) | EV (zakres) |
|---|---|---|---|
| Indie wygra i poniżej 3.5 gola | 2.12 | 40-49% | -15% do +3% (centralnie -7%) |
| Indie wygra i powyżej 3.5 gola | 2.10 | 22-45% | -54% do -6% |
| Handicap Indie -2.5 | 1.95 | 23-45% | poniżej 2.0 |
| Indie wygra i powyżej 2.5 (kurs 1.49) | 1.49 | 41-65% | poniżej progu kursu 2.0 |

Żaden kandydat z kursem > 2.0 nie ma p > 50% ani stabilnie dodatniego EV. Pewność każdej nogi: niska (niepotwierdzone składy reprezentacji, rozbieżność z rynkiem > 10 pp, wynik zależny od założeń λ). Zgodnie z regułą pewności minimum "średnia" kuponu nie przygotowano.

## Co podniosłoby pewność
Oficjalne składy (ok. 60-75 min przed startem, tj. ok. 09:15-09:30) pokazujące, kto z kadry Indii gra (zwłaszcza napastnicy i bramkarz), oraz informacja o sędzi.

To oszacowania probabilistyczne, nie gwarancje.
