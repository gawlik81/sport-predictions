# Leicester - Walsall (Football League Trophy, 10.11.2026, 20:00 PL)

Analiza skrócona (start za ok. 30 min). Źródła: connector Superbet (kursy, składy, forma, H2H, średnie), model Poissona (`poisson.py`). Brak danych z connectora: sędzia (nieznany), nieobecni ("Brak danych"). Rezerwa (WebSearch) nie była użyta ze względu na czas.

## Dane
- Składy: oficjalne. Leicester 3-4-2-1 (Cornell; O'Hora, Aluko, Thomas; Alves, Smallbone, Lundstram, Watson; Chaplin, Doyle; Bristric), Walsall 4-2-3-1. Ławka Leicester: Okoli, Coulibaly, De Cordova-Reid; ocena rotacji bez własnych danych o pierwszej jedenastce.
- Forma Leicester (6 ost.): 4:2 (Oxford City, wyjazd), 2:2 Stevenage, 3:0 Wigan, 1:2 Luton, 4:0 Bromley (wyjazd), 2:1 Doncaster. Średnio 2,3 gola strzelone, 1,2 stracone; gole straciło w 4 z 6.
- Forma Walsall (6 ost.): 1:3 Newport, 3:1 Colchester, 4:2 Salford, 3:0 Oldham, 1:1 Swindon, 3:2 Fulham U21 (wyniki z perspektywy Walsall; wyjazdowe porażki/wygrane mieszane). Strzelili w 6 z 6.
- H2H: ostatni 2023 Walsall 0:1 Leicester; bilans całościowy 6-1-0 dla Leicester (stare, mała waga).
- Średnie sezonowe z connectora (Trophy, mała próba): Leicester 3,5 gola strzelone/1,5 stracone, rożne 10,0; Walsall 2,0/4,0, rożne 2,5.

## Model
λ Leicester 2,5-2,8, λ Walsall 0,9-1,0 (korekta względem rynku: 1 = 1.22, X = 6.60, 2 = 7.90).
- Leicester wygra: 70-77% (rynek bez marży ok. 79%)
- Over 1.5: 86-88%; Over 2.5: 68-72%; Over 3.5: 46-51%
- BTTS tak: 56-58%

## Kupony (Superbet, kurs wiążący z kuponu w przeglądarce)
Wszystkie rynki łączone z Superbet mają EV < 0 przy moim p (najlepsze: "Leicester wygra lub zremisuje; Obie drużyny strzelą gola" 1.55, p ok. 50%, EV ok. -22%). Zwykły zwycięzca Leicester 1.22 (EV ok. -10%) jest poniżej progu kursu. Brak kuponu z EV > 0 w przedziale 1.5-2.5.

Pewność: średnia dla wyniku, niska dla rożnych i kartek (brak sędziego, mała próba średnich).
