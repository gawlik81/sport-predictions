# Źródła danych

Szukaj po nazwie drużyny/gracza + nazwie serwisu (np. "Vitality HLTV map
stats", "Gen.G gol.gg 2026", "Team Spirit datdota"), a nie ogólnych
frazach. To znacznie skraca liczbę potrzebnych zapytań.

Wiele serwisów statystycznych renderuje tabele przez JavaScript, więc
WebFetch może zwrócić pustą stronę. Wtedy spróbuj innego serwisu z tej
samej kategorii albo wyszukaj artykuł/zapowiedź, który cytuje statystyki.

## Wspólne dla wszystkich gier

- **Liquipedia** (liquipedia.net/counterstrike, /leagueoflegends, /dota2):
  podstawowe źródło do weryfikacji **formatu turnieju** (BO1/BO2/BO3/BO5,
  advantage w finale, fearless draft), drabinek, terminarza, **aktualnych
  składów i stand-inów** oraz historii transferów. Zawsze sprawdzaj tutaj
  Krok 0 i skład.
- Oficjalne konta drużyn i organizatorów na X/Twitterze: komunikaty o
  stand-inach i zmianach składu, często w dniu meczu.
- Kursy rynkowe (porównywarki kursów, np. OddsPortal): tylko jako punkt
  odniesienia dla reguły "model vs rynek" (SKILL.md Krok 2b, pkt 6), po
  zdjęciu marży. Nie kopiuj kursów jako własnej predykcji.

## CS2 (priorytet: mapy, strony, rundy)

- **HLTV** (hltv.org): ranking drużyn, wyniki, statystyki drużyn per mapa
  (win rate, liczba map, % rund CT/T, pistoletówki), veto z poprzednich
  meczów (do przewidzenia banów/picków), statystyki graczy (rating,
  ADR, KPR), zapowiedzi meczów z H2H.
- **bo3.gg**: statystyki map i drużyn, często łatwiejsze do pobrania niż
  HLTV; dobre do kontroli krzyżowej.
- **Valve Regional Standings** (github.com/ValveSoftware/counter-strike_regional_standings):
  oficjalny ranking Valve, używany do zaproszeń na turnieje.
- **Liquipedia**: format, active duty map pool, regulamin dogrywek.

### Orientacyjna "strona" map (ct-bias = win rate CT w rundach − 0.5)

Wartości zmieniają się z aktualizacjami map i metą. Zawsze sprawdź
aktualne statystyki (HLTV → Stats → Maps) zamiast polegać na tabeli.

| Mapa | Orientacyjny ct-bias | Uwagi |
|---|---|---|
| Nuke | +0.03 do +0.06 | wyraźnie CT |
| Ancient | +0.02 do +0.05 | raczej CT |
| Anubis | −0.02 do +0.01 | zbalansowana/T |
| Mirage | +0.01 do +0.03 | lekko CT |
| Inferno | +0.02 do +0.04 | raczej CT |
| Dust2 | −0.01 do +0.02 | zbalansowana |
| Train | +0.03 do +0.06 | wyraźnie CT |
| Overpass | +0.02 do +0.04 | raczej CT |

Active duty pool zmienia się. Jeśli mapy nie ma w tabeli, ustaw ct-bias
z aktualnych statystyk albo 0.0 z adnotacją.

### Orientacyjne średnie rund (MR12)

Przeciętna mapa na poziomie tier-1 kończy się w okolicach 21-22 rund, a
dogrywka zdarza się na ok. 8-12% map. Model `cs-map` przy p≈0.5 daje
więcej (ok. 23 rundy i ok. 16% dogrywek), bo nie widzi ekonomii. Stąd
obowiązkowa korekta w SKILL.md Krok 4 pkt 3. Zweryfikuj aktualne wartości
w statystykach HLTV/bo3.gg dla danego okresu.

## League of Legends

- **gol.gg** (gol.gg/esports): statystyki drużyn per split/turniej (win
  rate blue/red, GD@15, KPM, średni czas gry, first blood/dragon/Baron %),
  statystyki graczy i pule bohaterów.
- **Oracle's Elixir** (oracleselixir.com): szczegółowe dane meczowe,
  rozbicie na patche, dane do pobrania.
- **Leaguepedia** (lol.fandom.com): składy, wyniki, formaty, historia
  patchy turniejowych, H2H.
- **lolesports.com**: oficjalny terminarz, tabele lig, formaty.
- **Games of Legends** (gamesoflegends.com) i **Mobalytics/U.GG** (dla
  mety solo queue): kontekst patcha.

### Orientacyjne wartości (pro play, zweryfikuj dla patcha)

- Średni czas gry: ok. 30-34 min (LPL bywa szybsza, LEC/LCK wolniejsze
  w zależności od patcha).
- Łączne kille na grę: ok. 22-32 (LPL zwykle wyżej).
- Win rate strony niebieskiej: zwykle ok. 52-56%.

## Dota 2

- **datdota** (datdota.com): ratingi Glicko/Elo drużyn (bezpośredni input
  do `elo`), statystyki drużyn i graczy per patch, draft.
- **Dotabuff Esports** (dotabuff.com/esports) i **Stratz** (stratz.com):
  wyniki, statystyki drużyn, pule bohaterów, Radiant/Dire win rate.
- **Liquipedia Dota 2**: format (BO2 w grupach, advantage w finałach),
  składy, stand-iny, terminarz.
- **dota2.com** (patch notes): data i zakres ostatniego patcha.

### Orientacyjne wartości (pro play, zweryfikuj dla patcha)

- Średni czas gry: ok. 34-40 min.
- Łączne kille na grę: ok. 45-65, duża wariancja (sd często 12-18).
- Radiant win rate: zwykle ok. 50-54%.

## Artykuły, kontekst, składy

- **HLTV News, Dust2.us, Dexerto, Dot Esports, Sheep Esports (LoL),
  Upcomer, Esports Insider**: zapowiedzi, wywiady, komunikaty o
  transferach i stand-inach.
- Polskie źródła: **Cybersport.pl**, **Esportmania.pl**, **Polsat Games**
  (kontekst polskich drużyn i graczy).
- Wyszukuj świeże informacje z ostatnich 3-7 dni: "[drużyna] stand-in",
  "[drużyna] roster change [miesiąc rok]", "[drużyna] vs [rywal] preview",
  "[gracz] visa issue", "[drużyna] bootcamp".

## Rozgrywki i zakres

- **CS2 tier-1**: Majory (Valve), IEM (Cologne, Katowice i inne), BLAST
  (Premier/Open/Austin Major), ESL Pro League, PGL, Esports World Cup.
- **LoL**: Worlds, MSI, First Stand, LCK, LPL, LEC, LTA/LCS, LCP.
- **Dota 2**: The International, Esports World Cup, Riyadh Masters, PGL
  Wallachia, DreamLeague, BLAST Slam, ESL One, FISSURE.
- **Tier-2 i niżej** (CCT, ESEA, ERL, Dota tier-2 ligi): obsługiwane na
  żądanie, ale dane są uboższe. Zaznacz to wprost i stosuj SKILL.md Krok 2b
  pkt 7-8.
