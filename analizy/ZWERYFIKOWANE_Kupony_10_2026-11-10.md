# Kupony, noc NBA + NHL 10/11.11.2026

## 1. Okres i źródło kursów
- Okres: noc 10/11.11.2026 (mecze USA z 10.11, godziny polskie 11.11). Poziomy luzowania wybrane przez użytkownika: tylko 0-2.
- Kursy pobrane 10.11.2026 (wieczór). **Betclic.pl: tylko zwycięzca NBA, z statycznego HTML (bez przeglądarki MCP, bez potwierdzenia na gg397.bet).** Betclic nie wystawił NHL, handicapów ani totali w pobranej treści.
- **Fallback (nie Betclic, kursy zwykle wyższe niż krajowe):** NHL i spready/totale NBA z Pinnacle (theoddsapi, 10.11 18:31 UTC), DraftKings/FanDuel (ESPN). Wszystkie nogi kuponów poniżej mają kurs z fallbacku Pinnacle, a nie z Betclic, z wyjątkiem nóg NBA ML (Betclic).
- Analizy: `analizy/Analiza_NBA_NHL_noc_2026-11-10.md`.

## 2. Terminarz
13 wydarzeń: NBA 6, NHL 7 (inne sporty poza zakresem). Brak pominiętych. Terminarz NBA tylko z ESPN, NHL z ESPN i oficjalnego API.

## 3. Pula nóg po filtrach (p > 50%, fair > 1.15, EV ≥ ~0)
| Mecz (godz. PL) | Rynek | p | Kurs | Fair | EV | Pewność | Źródło kursu |
|---|---|---|---|---|---|---|---|
| CBJ-FLA (01:30) | FLA +1.5 | 75.4% | 1.40 | 1.33 | +5.6% | średnia | Pinnacle |
| TOR-COL (01:00) | TOR +1.5 | 67.1% | 1.60 | 1.49 | +7.4% | niska (flaga) | Pinnacle |
| LAK-NSH (04:00) | NSH +1.5 | 72.0% | 1.44 | 1.39 | +3.7% | niska | Pinnacle |
| MTL-MIN (01:00) | MTL +1.5 | 70.2% | 1.43 | 1.42 | +0.4% | średnia | Pinnacle |
| WPG-NJD (01:00) | NJD ML | 59.4% | 1.71 | 1.68 | +1.6% | średnia | Pinnacle |
| STL-DET (02:00) | STL ML | 59% | 1.695 | 1.69 | 0% | średnia | Pinnacle |
| PHI-BOS (02:00) | BOS ML | 57% | 1.77 | 1.75 | +0.9% | niska-średnia | Betclic |
| OTT-WSH (01:00) | OTT ML | 52.4% | 1.96 | 1.91 | +2.7% | niska-średnia | Pinnacle |
| PHX-LAC (03:00) | LAC +3.5 | 53.3% | 1.95 | 1.88 | +3.9% | niska | DraftKings |
| UTA-MIA (03:00) | MIA ML | 73.9% | 1.21 | 1.35 | -10.6% | średnia | Betclic |
| SAC-ORL (04:00) | ORL ML | 69.8% | 1.40 | 1.43 | -2.3% | niska-średnia | Betclic |
| OTT-WSH (01:00) | WSH +1.5 | 70.8% | 1.38 | 1.41 | -2.3% | niska | Pinnacle |

Odrzucone: NYK ML (fair 1.14), BTTS FLA-CBJ (fair 1.13), rynki zawodnika (brak linii i drugiego źródła), nogi bez kursu (STL +1.5, Under 6.5 MIN-MTL).

## 4. Kupony

### Poziom 0 (bazowy)
**Kupon 1 (poziom 0 bazowy)**
| Noga | Godz. PL | p | Kurs | EV | Źródło |
|---|---|---|---|---|---|
| FLA +1.5 (Florida @ Columbus) | 01:30 | 75.4% | 1.40 | +5.6% | Pinnacle (fallback) |
| TOR +1.5 (Colorado @ Toronto) | 01:00 | 67.1% | 1.60 | +7.4% | Pinnacle (fallback) |

Łączne p 50.6% | fair 1.98 | kurs 2.24 | EV +13.3% | stawka 1/4 Kelly 2.7% (obie nogi "przewaga niepotwierdzona": po korekcie p do rynku +5 pp EV ok. +7%, stawka ok. 1.6%).
Ryzyko: puck line +1.5 przegrywa przy porażce o 2+ gole (puste bramki); TOR +1.5: model 6 pp nad rynkiem.

**Kupon 2 (poziom 0 bazowy)**
| Noga | Godz. PL | p | Kurs | EV | Źródło |
|---|---|---|---|---|---|
| NSH +1.5 (Nashville @ LA Kings) | 04:00 | 72.0% | 1.44 | +3.7% | Pinnacle (fallback) |
| MTL +1.5 (Minnesota @ Montreal) | 01:00 | 70.2% | 1.43 | +0.4% | Pinnacle (fallback) |

Łączne p 50.5% | fair 1.98 | kurs 2.06 | EV +4.1% | stawka 1/4 Kelly 1.0% (NSH "po bramkarzu", niepotwierdzeni; po korekcie EV ok. +2.6%, stawka ok. 0.6%).
Ryzyko: bramkarze NSH i LAK niepotwierdzeni; Wallstedt (MIN) niepotwierdzony.

### Poziom 2 (poniżej progów: EV < 0, ranking po p)
**Kupon 3 (poziom 2)**
| Noga | Godz. PL | p | Kurs | EV | Źródło |
|---|---|---|---|---|---|
| MIA ML (Miami @ Utah) | 03:00 | 73.9% | 1.21 | -10.6% | Betclic (niepotwierdzone na gg397.bet) |
| WSH +1.5 (Washington @ Ottawa) | 01:00 | 70.8% | 1.38 | -2.3% | Pinnacle (fallback) |

Łączne p 52.3% | fair 1.91 | kurs 1.67 | EV -12.6% | stawka 0%.
Złamane progi: EV > 0 (poziom 2). Giannis Probable, Markkanen Q, Thompson (WSH) niepotwierdzony.

## 5. Ostrzeżenia
- Powstały tylko 3 kupony z 10 żądanych: kupon dwunogowy z p > 50% wymaga obu nóg z p ≳ 70%, a takich nóg jest za mało; poziom 1 (EV ≥ -5%) nie dał dodatkowych kuponów. Poziom 3 (p > 45%, nogi p ≥ 55%) dałby ok. 1 kupon więcej (np. WSH +1.5 + WPG +1.5, p ok. 45.6%, EV ok. -6%); nie stosuję go bez zgody.
- Żaden mecz nie ma wyraźnej przewagi nad rynkiem, a dodatnie EV kuponów 1 i 2 wynika głównie z p modelu powyżej rynku o 3-7 pp na puck line +1.5 (flaga "przewaga niepotwierdzona").
- Kursy z Pinnacle/DraftKings są zagraniczne i zwykle wyższe niż w Betclic; kursów Betclic NHL i handicapów nie udało się pobrać, więc faktyczny kurs i EV mogą być niższe. Przed postawieniem sprawdź kursy na Betclic.
- Założenie niezależności meczów; kursy mogą się zmienić; składy, statusy Questionable (Giannis, Markkanen, Embiid) i bramkarze NHL do potwierdzenia przed meczami. To oszacowania probabilistyczne, nie gwarancje.
