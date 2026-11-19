# Analiza: eliminacje AFCON 2027, kolejka 3 (reprezentacje afrykańskie), 13.11.2026

Rozgrywki potwierdzone: eliminacje Pucharu Narodów Afryki 2027 (Superbet: "Africa Cup of Nations Qualification"; CAF/africasoccer: kolejki 3 i 4 w oknie 12-17.11.2026). Godziny polskie: 14:00 (13:00 UTC), 17:00, 20:00, 21:00.

## Jakość danych i metoda (czytać najpierw)

- Źródła: Superbet MCP (kursy 1X2 i totale, forma z `superbet_h2h`, średnie z `superbet_stats` tylko dla Zambia - Burundi), africasoccer.com i notjustok.com (tabele grup), WebSearch.
- **Brak** potwierdzonych kontuzji, zawieszeń, składów i sędziów (`superbet_missing_players` zwraca brak danych; `lineups` nie sprawdzano, składy ogłaszane ok. 60-75 min przed meczem). Statystyk xG/rożnych/kartek dla reprezentacji brak, więc rynków rożne/kartki/faule nie wyceniam.
- Dane z Superbet i serwisów bywają sprzeczne (m.in. daty/wyniki z 4-6.10 pokazują sprzeczne rezultaty Egiptu i RPA, tabela notjustok sama sobie przeczy). Tabele grup traktuję orientacyjnie.
- Metoda: λ ustawione ze statystyk formy i kontekstu, kalibracja z SKILL.md dla reprezentacji (λ drużyny nie niżej niż 0,7; Under przy λ łącznym ≤ 2,0 tylko do średniej pewności). Wynik przepuszczony przez `poisson.py`. Przy 1 (gospodarz) nie schodzę pod rynek bez vig o więcej niż 5 pp (brak konkretnej informacji kadrowej), więc 1X2 jest tam podciągnięte do poziomu (rynek bez vig minus 5 pp); dotyczy to Gabonu, RPA, RZP, Tunezji, Mali, Egiptu, Maroka i Nigerii. BTTS = średnia z modelu (przez podłogę λ 0,7 zawyżony) i z modelu dopasowanego do rynku.
- **Pewność we wszystkich meczach: niska do średniej** (nigdy wysoka): reprezentacje, brak składów, szumne dane. Rynek bukmacherski (Superbet) jest w tych meczach prawdopodobnie trafniejszy niż moja wycena.
- Kolumna "Rynek": kurs Superbet 1 oraz Under/Over 2.5; BTTS rynkowe znane tylko dla Zambia - Burundi (tak 2.35 / nie 1.52).

## Tabela zbiorcza (p, fair odds w nawiasie)

| Mecz | λ | 1 | X | 2 | 1X | X2 | 12 |
|---|---|---|---|---|---|---|---|
| Zambia - Burundi | 1.55/0.80 | 55% (1.81) | 26% (3.91) | 19% (5.18) | 81% (1.24) | 45% (2.23) | 74% (1.34) |
| Mozambik - Etiopia | 1.55/0.70 | 58% (1.73) | 25% (3.92) | 17% (5.97) | 83% (1.20) | 42% (2.37) | 75% (1.34) |
| Komory - Kongo | 1.35/0.85 | 48% (2.06) | 28% (3.58) | 24% (4.24) | 76% (1.31) | 52% (1.94) | 72% (1.39) |
| Gabon - Lesotho | 1.90/0.70 | 69% (1.45) | 19% (5.18) | 12% (8.42) | 88% (1.13) | 31% (3.21) | 81% (1.24) |
| RPA - Kenia | 1.80/0.70 | 68% (1.48) | 20% (5.04) | 12% (8.05) | 88% (1.14) | 32% (3.10) | 80% (1.25) |
| Burkina Faso - Mauretania | 1.50/0.75 | 55% (1.81) | 26% (3.82) | 19% (5.35) | 81% (1.23) | 45% (2.23) | 74% (1.35) |
| Tunezja - Libia | 1.65/0.75 | 62% (1.61) | 22% (4.47) | 15% (6.47) | 85% (1.18) | 38% (2.64) | 78% (1.29) |
| Rep. Zielonego Przylądka - Liberia | 1.80/0.75 | 68% (1.46) | 19% (5.30) | 13% (7.90) | 87% (1.14) | 32% (3.17) | 81% (1.23) |
| Nigeria - Tanzania | 2.20/0.70 | 72% (1.39) | 18% (5.63) | 10% (9.65) | 90% (1.12) | 28% (3.56) | 82% (1.22) |
| Egipt - Malawi | 2.30/0.70 | 78% (1.28) | 14% (7.21) | 8% (12.57) | 92% (1.09) | 22% (4.58) | 86% (1.16) |
| Mali - Rwanda | 1.75/0.75 | 65% (1.54) | 21% (4.77) | 14% (7.04) | 86% (1.17) | 35% (2.84) | 79% (1.27) |
| Maroko - Niger | 2.60/0.70 | 80% (1.25) | 13% (7.77) | 7% (14.21) | 93% (1.08) | 20% (5.03) | 87% (1.15) |

| Mecz | O1.5 | O2.5 | U2.5 | U3.5 | BTTS tak | BTTS nie | Superbet 1 / U2.5 / O2.5 |
|---|---|---|---|---|---|---|---|
| Zambia - Burundi | 68% (1.47) | 42% (2.40) | 58% (1.72) | 79% (1.27) | 42% (2.39) | 58% (1.72) | 1.57 / 1.54 / 2.30 |
| Mozambik - Etiopia | 66% (1.52) | 39% (2.56) | 61% (1.64) | 81% (1.24) | 41% (2.43) | 59% (1.70) | 1.56 / 1.61 / 2.15 |
| Komory - Kongo | 65% (1.55) | 38% (2.65) | 62% (1.61) | 82% (1.22) | 42% (2.37) | 58% (1.73) | 1.82 / 1.48 / 2.42 |
| Gabon - Lesotho | 73% (1.36) | 48% (2.08) | 52% (1.93) | 74% (1.36) | 41% (2.47) | 59% (1.68) | 1.23 / 1.87 / 1.82 |
| RPA - Kenia | 71% (1.40) | 46% (2.19) | 54% (1.84) | 76% (1.32) | 39% (2.57) | 61% (1.64) | 1.25 / 1.74 / 1.97 |
| Burkina Faso - Mauretania | 66% (1.52) | 39% (2.56) | 61% (1.64) | 81% (1.24) | 40% (2.48) | 60% (1.68) | 1.54 / 1.55 / 2.27 |
| Tunezja - Libia | 69% (1.45) | 43% (2.32) | 57% (1.76) | 78% (1.28) | 39% (2.53) | 61% (1.65) | 1.36 / 1.60 / 2.17 |
| Rep. Zielonego Przylądka - Liberia | 72% (1.38) | 47% (2.13) | 53% (1.88) | 75% (1.34) | 41% (2.43) | 59% (1.70) | 1.24 / 1.85 / 1.83 |
| Nigeria - Tanzania | 79% (1.27) | 55% (1.80) | 45% (2.24) | 67% (1.49) | 43% (2.35) | 57% (1.74) | 1.18 / 2.10 / 1.64 |
| Egipt - Malawi | 80% (1.25) | 58% (1.73) | 42% (2.36) | 65% (1.55) | 39% (2.54) | 61% (1.65) | 1.10 / 2.15 / 1.61 |
| Mali - Rwanda | 71% (1.40) | 46% (2.19) | 54% (1.84) | 76% (1.32) | 40% (2.51) | 60% (1.66) | 1.30 / 1.66 / 2.07 |
| Maroko - Niger | 84% (1.19) | 64% (1.56) | 36% (2.78) | 58% (1.72) | 42% (2.41) | 58% (1.71) | 1.07 / 2.55 / 1.44 |

Typy z fair odds ≤ 1.15 (np. DC 1X Maroko/Egipt/Nigeria/RPA/Gabon/Rep. Z. Przylądka, 12 Maroko, O1.5 Maroko) nie nadają się do rankingów i kuponów.

## Mecze (skrót: dane, ryzyka)

### Zambia - Burundi (gr. I, 14:00, Levy Mwanawasa)
Typ: najlepszy wskaźnik to Under 2.5 (58%, 1.72) i BTTS nie (58%, 1.72); 1X 81% (1.24). Pewność: niska-średnia. Forma Zambii: 2-0 z Togo, 1-3 z Algierią; Burundi: 2-2 z Algierią (wyjazd), 0-1 z Togo; Burundi ma kartek mniej (1,0 vs 2,5 u gospodarzy wg Superbet). Średnie sezonu (Superbet): gole 1,5 / 2,5 (próbka malutka). H2H: brak w bazie. Ryzyka: Burundi punktuje w grupie (4 gole w 2 meczach), remis ok. 26%, wygrana gości ok. 19%. Sędzia: Washington Dolo, brak historii kartek. Rynek zbieżny (1 = 58% bez vig vs moje 55%).

### Mozambik - Etiopia (gr. J, 14:00)
Typ: 1X 83% (1.20), Under 2.5 61% (1.64). Pewność: niska-średnia. Mozambik: 4-1 Sudan, remis 1-1 z Senegalem (wg tabeli), Etiopia bez punktu i bez gola w ostatnich dwóch meczach (0-1 z Senegalem, 0-1 Sudan). H2H: jedno 0-0 (2023). Ryzyka: wyniki 1-0/1-1 łatwo; Etiopia w ostatnich 5 meczach strzeliła tylko 3 gole.

### Komory - Kongo (gr. G, 14:00)
Typ: brak mocnego typu (1 ok. 48%). Najuczciwiej Under 3.5 82% (1.22), Under 2.5 62% (1.61). Pewność: niska. Komory: 1-0 Namibia, 1-3 Kamerun; Kongo (Brazzaville): 1-1 Kamerun, 0-1 Namibia (dane z 2025 w części formy, nieaktualne). Wyrównany układ, 1X2 bez przewagi.

### Gabon - Lesotho (gr. A, 17:00)
Typ: 1 69% (1.45) i 12 81% (1.24). Pewność: średnia. Gabon: 2-0 Niger, 0-2 Maroko; Lesotho: 0-2 Maroko, 1-2 Niger (0 pkt). H2H: 0-0 i 0-2 (2024) dla Gabonu. Ryzyka: remis (ok. 19%) i niespodzianka Lesotho (ok. 12%); Gabon bez gwiazdy w ofensywie? (niepotwierdzone, brak danych kadrowych). Model wolniej niż rynek (1: 69% vs 74%).

### RPA - Kenia (gr. D, 17:00)
Typ: 1 68% (1.48), Under 3.5 76% (1.32). Pewność: średnia-niska. Kenia ma już zapewniony awans jako współgospodarz, więc motywacja i rotacja to ryzyko po stronie gości (obniża Keni λ, ale nie schodzę pod 0,7); RPA 6 pkt (wg tabeli). Dane o formie RPA sprzeczne (0-1 z Egiptem 4.10 vs tabela 2-1 z Gwineą). H2H tylko 2011-12.

### Burkina Faso - Mauretania (gr. F, 17:00)
Typ: brak mocnego typu (1 55%). Under 2.5 61% (1.64). Pewność: niska. Rozbieżność: Superbet wskazuje Burkinę jako gospodarza, a jeden serwis opisuje wyjazd Burkiny do Mauretanii; nie potwierdziłem miejsca gry. Forma Burkiny słaba (1-1 Benin, 1-0 RŚA, 0-7 Argentyna w sparingu), Mauretania wygrała ostatnie H2H 1-0 (08.2025). Ryzyko wyższe niż sugeruje kurs.

### Tunezja - Libia (gr. H, 17:00)
Typ: 1 62% (1.61), Under 3.5 78% (1.28). Pewność: niska-średnia. Tunezja nierówna (1-1 Uganda, 2-2 Botswana, 2 pkt), Libia 1 pkt (0-1 Uganda, 2-2 Botswana). H2H: Tunezja 7 zwycięstw w historii, ostatnio 1-0 i 3-0 (2023). Mecz wg tabeli ważny dla układu grupy. Model poniżej rynku (62% vs 67%), brak konkretów kadrowych.

### Republika Zielonego Przylądka - Liberia (gr. K, 17:00)
Typ: 1 68% (1.46), O1.5 72% (1.38). Pewność: niska-średnia. Obie drużyny bez punktu (RZP 1-3 Mali, 1-2 Rwanda; Liberia 0-1 Mali, 1-3 Rwanda). RZP w czerwcu z mocnymi przeciwnikami (remisy z Urugwajem i Hiszpanią, mundial). Liberia ma czerwone kartki w formie (rywal wyraźnie wymuszany: 3 w 3 meczach).

### Nigeria - Tanzania (gr. L, 17:00)
Typ: 1 72% (1.39), O1.5 79% (1.27), O2.5 55% (1.80). Pewność: średnia. Nigeria musi wygrywać po 0-3 z Gwineą-Bissau (presja), Tanzania współgospodarz AFCON 2027 (awans zapewniony) i bez punktów (0-2 G-B, 1-1 Madagaskar). H2H: Nigeria 2-1 (12.2025). Ryzyko: Nigeria w kryzysie wyników defensywnych (3-0 przegrana, 3-3 z Rosją w sparingu), ale mecz o punkty u siebie. O2.5 zbliżone do rynku (1.64).

### Egipt - Malawi (gr. B, 20:00)
Typ: 1 78% (1.28), O1.5 80% (1.25), O2.5 58% (1.73). Pewność: średnia. Egipt: 5-0 Sudan Płd., 0-0 Angola (4 pkt; Superbet pokazuje też 0-1 z RPA z 4.10, dane sprzeczne). Malawi: 2-1 Sudan Płd., 1-3 Angola. H2H 2023: 2-0 i 4-0 dla Egiptu. Ryzyka: Egipt tracił punkty z niżej notowanymi (0-0 Angola), Malawi jest zorganizowane w defensywie. λ Malawi podniesione do 0,7 (reguła), więc BTTS zawyżone o ok. 3-5 pp względem rynku.

### Mali - Rwanda (gr. K, 20:00)
Typ: 1 65% (1.54), U3.5 76% (1.32). Pewność: średnia-niska. Obie 6 pkt (Mali: 3-1 RZP, 1-0 Liberia; Rwanda: 3-1 Liberia, 2-1 RZP). H2H: Mali 3-0 i 1-0 (2021). Mali nie przegrywa, ale ostatnio mało goli (1-0, 1-1 z Marokiem). Rwanda ma 3 gole w 2 meczach i 1 czerwoną kartkę w serii.

### Maroko - Niger (gr. A, 21:00)
Typ: 1 80% (1.25) - krótki, na kupon tylko jako noga; O2.5 64% (1.56). Pewność: średnia. Maroko: 2-0 Lesotho, 2-0 Gabon (6 pkt); H2H 5-0 i 2-1 w kwal. do MŚ 2025. Niger: 0-2 Gabon, 2-1 Lesotho, 0-1 Mauretania (czerwiec). Ryzyka: rotacja Maroka przy dużej przewadze, remis 13%, upset 7%. Moje 1 (80%) jest o 5 pp pod rynkiem bez vig (85%) - to efekt reguły i podłogi λ 0,7 dla Nigru, bez konkretnej informacji nie schodzę niżej.

## Mecze bez rzetelnej wyceny

Żaden mecz nie jest całkowicie niewyceniony (są kursy 1X2/O-U i forma), ale:
- **Komory - Kongo i Burkina Faso - Mauretania**: brak mocnego typu (wyrównane, dane o Kongo i miejscu gry niepewne).
- **Rynki rożne, kartki, faule, zawodnika**: nie wyceniam dla żadnego meczu, bo brak statystyk (reprezentacje w eliminacjach), sędziów (poza Zambia - Burundi, bez historii) i potwierdzonych składów (skill wymaga dwóch niezależnych źródeł, inaczej nie rekomenduje się typu).
- BTTS rynkowe znane tylko w Zambia - Burundi, wycena BTTS w pozostałych meczach nie ma porównania z kursem.

## Kandydaci na kupon (dla bet-slip-builder)

Kursy rynkowe: tylko Superbet 1X2 i O/U 2.5 (patrz tabela). Fair odds z dołu ≤ 1.15 pominięte.

| Mecz | Rynek | p | fair | Pewność | Zależy od | Kurs Superbet |
|---|---|---|---|---|---|---|
| Nigeria - Tanzania | Over 2.5 | 55% | 1.80 | średnia | motywacja Nigerii, skład | 1.64 (poniżej fair) |
| Maroko - Niger | Over 2.5 | 64% | 1.56 | średnia | rotacja Maroka | 1.44 (poniżej fair) |
| Egipt - Malawi | Over 2.5 | 58% | 1.73 | średnia | skład Egiptu | 1.61 (poniżej fair) |
| Gabon - Lesotho | 1 | 69% | 1.45 | średnia | skład | 1.23 (poniżej fair) |
| Mali - Rwanda | 1 | 65% | 1.54 | średnia-niska | Rwanda 6 pkt | 1.30 (poniżej fair) |
| RPA - Kenia | 1 | 68% | 1.48 | średnia-niska | rotacja Kenii | 1.25 (poniżej fair) |
| Zambia - Burundi | Under 2.5 | 58% | 1.72 | niska-średnia | forma | 1.54 (poniżej fair) |
| Mozambik - Etiopia | 1X | 83% | 1.20 (graniczne 1.15-1.20) | niska-średnia | - | brak (DC nie pobrano) |

W żadnym z powyższych kurs Superbet nie przewyższa fair odds, czyli wg moich liczb nie ma w 1X2 i O/U 2.5 wartości (EV ujemne wobec kursu rynkowego po marży ok. 9-10%). Rynek jest tu zapewne trafniejszy niż moje oszacowanie.

To oszacowania probabilistyczne, nie gwarancje.
