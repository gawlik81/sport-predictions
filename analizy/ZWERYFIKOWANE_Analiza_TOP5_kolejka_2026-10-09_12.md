# Analiza kolejki TOP5 (9-12.10.2026) - pod kupony

Czas polski. Ekstraklasa w tym terminie nie gra: 12. kolejka to 23-25.10 (ekstraklasa.org), a 11. kolejka była 3-5.10. Przerwa reprezentacyjna zakończyła się 6.10.

## Metoda i ograniczenia (czytaj najpierw)

- **Kursy:** DraftKings (ESPN scoreboard, kursy zamknięcia), marża usunięta proporcjonalnie. Kursów dla Hamburg - Hoffenheim brak.
- **Research mediów:** wyszukiwarka nie zwróciła wiarygodnych, aktualnych zapowiedzi (składy, kontuzje) dla większości meczów. Potwierdzone jedynie: Parma zmieniła trenera pod koniec września (Gilardino, bilans 1-1-3), Inter bez poważnych absencji, Napoli i Frosinone bez zgłoszonych absencji. Niepotwierdzone (nie użyte): plotka o absencji Saki i Ødegaarda w Arsenalu z niewiarygodnego serwisu.
- **Konsekwencja:** prawdopodobieństwa to przede wszystkim kurs rynkowy bez marży, sprawdzony modelem Poissona (np. λ 1,95/0,85 daje 63% wygranej gospodarza, rynek 66-69%). Nie mam informacji, które uzasadniałyby schodzenie pod rynek o >5 pp, więc korekty są małe (do -3 pp). **Nie ma tu udowodnionego value; to wybór typów o największym prawdopodobieństwie, nie wartościowych kursów.**
- **Rozbieżność terminów:** serwis Comuniate podaje Real Madrid - Villarreal i Barcelona - Getafe na 11.10 21:00, ESPN na 10.10. Termin niezweryfikowany, więc te mecze nie trafiły na kupony (Barcelona i tak ma kurs ok. 1.08).

## Typy o największym prawdopodobieństwie (po kalibracji)

Kursy DK: wygrana z moneyline; podwójna szansa (1X) przybliżona z moneyline (rzeczywiste kursy DC mogą być niższe).

| Mecz | Typ | p rynek | p moje | Fair | Kurs DK | Pewność | Uwagi / ryzyka |
|---|---|---|---|---|---|---|---|
| Dortmund - Werder (pt 20:30) | Dortmund wygra | 69% | 69% | 1.45 | 1.33 | średnia | Dortmund 4-0-0 (W5), Werder 2-1-1; ryzyko: remis 18%, wygrana Werderu 13% |
| Arsenal - Leeds (sob 13:30) | Arsenal wygra | 68% | 66% | 1.52 | 1.41 | średnia | Leeds 5. miejsce, 9 pkt, tylko 3 stracone; -2 pp za niepotwierdzone doniesienia kadrowe. Ryzyko: remis 19%, Leeds 13% |
| Lille - Le Havre (sob 17:15) | Lille wygra | 66% | 65% | 1.54 | 1.44 | średnia | Le Havre LDLDL; Lille formą też niestabilny (LWLWD) |
| Napoli - Frosinone (sob 20:45) | Napoli wygra | 65% | 62% | 1.61 | 1.43 | niska-średnia | Napoli DWLLL, Frosinone WDWLW (3-1-1). -3 pp za słabą formę faworyta. Ryzyko: remis 20%, Frosinone 15% |
| Chelsea - Bournemouth (sob 16:00) | Chelsea lub remis (1X) | 79% | 78% | 1.28 | ok. 1.22 | średnia | Bournemouth LDWLW; Chelsea wygrana tylko 56%, więc 1X bezpieczniejsze |
| Man Utd - Tottenham (sob 18:30) | Man Utd lub remis (1X) | 78% | 76% | 1.32 | ok. 1.23 | niska-średnia | Man Utd LLDDL (słaba forma), Spurs DLLWD; -2 pp |
| Leipzig - Frankfurt (sob 18:30) | Leipzig lub remis (1X) | 79% | 78% | 1.28 | ok. 1.16 | średnia | Leipzig LWLLW; Frankfurt DWLDW (nie kryzys) |
| Augsburg - Bayern (sob 15:30) | Bayern wygra | 80% | 78% | 1.28 | 1.15 | średnia | Bayern LDWWW, Augsburg WWWDW (forma lepsza niż zwykle u gospodarza). Ryzyko: remis 11%, Augsburg 9% |
| Betis - Osasuna (nie 18:30) | Betis wygra | 63% | 62% | 1.61 | 1.51 | średnia | Betis DWWWW, Osasuna DLLLW |
| Freiburg - Schalke (nie 17:30) | Freiburg wygra | 58% | 58% | 1.72 | 1.61 | średnia | Freiburg 3-1-0 (DWWWW), Schalke 1-2-1 |
| Lazio - Monza (nie 15:00) | Lazio lub remis (1X) | 82% | 80% | 1.25 | ok. 1.12 | średnia | Monza WDWWW to formą mocny beniaminek; -2 pp |
| Inter - Parma (sob 18:00) | Inter wygra | 83% | 80% | 1.25 | 1.12 | wysoka | Fair 1.20-1.25 = przypadek graniczny; kryzys Parmy (zmiana trenera) -3 pp; nie na kupon z powodu kursu DK 1.12 |
| Atalanta - Venezia (pon 18:30) | Atalanta wygra | 59% | 59% | 1.69 | 1.54 | niska-średnia | Atalanta LLLWW (2-0-3), Venezia 0-0-5; zmęczone kadrowo, brak zapowiedzi |

Pominięte (fair ≤ 1.15 lub brak mocnego typu): Barcelona - Getafe (88%, fair 1.14), PSG - Le Mans (87%, fair 1.15), Inter - Parma wygrana jako pojedynczy typ (graniczny), Dortmund 1X (fair 1.15). Mecze wyrównane (np. Villa - Brentford, Ipswich - Fulham, Sunderland - Brighton, Rayo - Athletic, Como - Roma, Lens - Lyon, Cagliari - Juventus) - **brak mocnego typu**.

## Rynek totali (opcjonalnie)

Under 3.5 ma ok. 57-60% (fair 1.67-1.75) w meczach Napoli - Frosinone, Atalanta - Venezia, Chelsea - Bournemouth, Man Utd - Tottenham, Lens - Lyon, Köln - Gladbach. Nie użyte na kuponach: korelują z wynikiem 1X2 w tych samych meczach, a priorytetem są typy wynikowe.

*To oszacowania probabilistyczne, nie gwarancje.*
