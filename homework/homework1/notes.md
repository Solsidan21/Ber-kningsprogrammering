# Genomgångsplan — Homework 1

Mål: Kunna förklara **varje cell** i `solution.ipynb` muntligt för läraren.

Notebooken är strukturerad efter uppgifterna: varje Task har en markdown-cell
som beskriver uppgiften och en eller flera kod-celler med lösningen.

---

## Steg 1: Förstå matematiken (utan kod)

Innan ni tittar på koden, se till att ni kan förklara följande med egna ord:

### Carlsons AGM-iteration
- **Aritmetiskt medelvärde:** medelvärdet av två tal, `(a + g) / 2`
- **Geometriskt medelvärde:** `sqrt(a * g)`
- Algoritmen: starta med `a_0 = (1+x)/2` och `g_0 = sqrt(x)`, beräkna sedan
  nya medelvärden upprepat. Sekvensen `a_i` konvergerar mot det
  *aritmetisk-geometriska medelvärdet* (AGM)
- **Varför ger detta ln(x)?** Carlson visade att `(x-1)/AGM((1+x)/2, sqrt(x)) = ln(x)`.
  Ju fler iterationer, desto närmare AGM, desto bättre approximation
- **Konvergenshastighet:** Kvadratisk — antalet korrekta siffror *fördubblas*
  ungefär för varje iteration

### Richardson-extrapolation (Task 4)
- Felet i `(x-1)/a_i` kan skrivas som en serie i `4^(-i)`
- Richardson-extrapolation kombinerar resultat från olika `i` för att
  *eliminera* feltermer systematiskt
- Tabellen `d[k,i]` bygger bort fler och fler feltermer med ökande `k`
- Resultat: **mycket** snabbare konvergens — kan nå maskinprecision med bara
  4–5 iterationer

**Trolig följdfråga:** "Vad är Richardson-extrapolation?"
→ Svar: En teknik som kombinerar grova och fina approximationer för att
  ta bort systematiska feltermer. Samma idé används i t.ex. Romberg-integration.

---

## Steg 2: NumPy-koncept att kunna

Dessa koncept är nya (från kap 4–5, Unit 04). Kunna förklara dem:

| Koncept | Var i notebooken | Förklaring |
|---------|------------------|------------|
| `np.asarray(x, dtype=float)` | Task 1 (`approx_ln`) | Konverterar input till NumPy-array. Gör att funktionen fungerar med både `2.0` och `[1.0, 2.0, 3.0]` |
| `zeros(n+1)` | Task 4 (`_compute_a_values`) | Skapar en array fylld med nollor |
| `zeros((n+1, n+1))` | Task 4 (`fast_approx_ln`) | Skapar en 2D-matris (n+1 x n+1) med nollor |
| `linspace(0.01, 5, 200)` | Task 2, 5 (plottfunktioner) | Skapar jämnt fördelade punkter på ett intervall |
| Vektorisering | Task 1 (`approx_ln`) | Alla operationer (`+`, `/`, `sqrt`) appliceras på *hela arrayen* samtidigt — ingen loop behövs per element |
| `np.vectorize` | Task 5 (`plot_fast_convergence`) | Gör om en skalär funktion till en som kan ta arrays. *Inte* äkta vektorisering (fortfarande en loop under huven), men bekvämt |
| Indexering `d[k, i]` | Task 4 (`fast_approx_ln`) | Åtkomst av element i 2D-array med `[rad, kolumn]` |

**Trolig följdfråga:** "Varför använda `np.asarray` istället för att bara räkna med float?"
→ Svar: Gör funktionen generell — samma kod fungerar för en enskild punkt
  och för en hel array av x-värden. Det är NumPy-idiomatiskt.

### Import-val och varför

Vår första cell ser ut så här:
```python
import numpy as np
from numpy import sqrt, log, zeros, linspace
import matplotlib.pyplot as plt
```

Detta är en **medveten hybrid**: alias för NumPy-systemverktyg och selektiv import
för matematiska funktioner. För att försvara valet ärligt behöver vi titta på vad
kursboken faktiskt säger — och boken är **inte konsekvent själv**:

**Kap 1.1.4 "Configuration"** rekommenderar uttryckligen wildcard-import som
default-header i alla Python-filer (det är den enda direkta rekommendationen i
setup-kapitlet):

> *"Most Python codes will be collected in files. We recommend that you use the following
> header in all your Python files:*
> ```python
> from numpy import *
> from matplotlib.pyplot import *
> ```"

Boken erkänner att Python varnar för wildcard-imports men skriver: *"In this particular
case, we ignore the warning."*

**Kap 13.3.1 "Modules"** presenterar **tre alternativ neutralt** (ingen avråds från):
selektiv import (`from numpy import array, vander`), wildcard (`from numpy import *`),
och namespace/alias (`import numpy` eller `import numpy as np`). Boken skriver:

> *"Which of these alternatives you use affects the readability of your code as well as
> the possibilities for mistakes."*

Boken pekar ut **shadowing** som ett konkret problem med `from`-stilen — om man råkar
tilldela en variabel samma namn som en importerad funktion blir funktionen otillgänglig
— och visar att namespace-stil (`import scipy.linalg as sl` och sedan `sl.eig`) är ett
sätt att undvika det. Men: boken **avråder inte uttryckligen** från `from numpy import *`,
och i samma kapitel erkänner författarna:

> *"Throughout this book, we have used many commands, objects, and functions. These were
> imported into the local namespace by statements such as `from scipy import *`.
> Importing objects in this manner does not make the module from which they are imported
> evident."*

#### Vårt val: hybrid (selektiv from-import + alias)

| Stil | Användning hos oss | Fördel | Nackdel |
|------|--------------------|--------|---------|
| `import numpy as np` | `np.asarray(x)`, `np.vectorize(...)` | Tydlig namnrymd för systemverktyg | Längre att skriva |
| `from numpy import sqrt, log, ...` | `sqrt(x)`, `log(x)`, `zeros(n)` | Matematisk läsbarhet — koden ser ut som formler | Måste plockas in selektivt |
| `from numpy import *` (boken kap 1.1.4) | Vi använder inte | Slipper allt prefix; matchar bokens default-header | Skuggar Python-inbyggda namn (`sum`, `min`, `any`, `abs`, `max` finns alla i numpy); oklart varifrån funktioner kommer |

**Varför båda?** Funktioner som *ser matematiska ut* (`sqrt`, `log`, `zeros`, `linspace`)
plockar vi in selektivt så koden läses som formler. NumPy-specifika verktyg
(`np.asarray`, `np.vectorize`) behåller vi med prefix för tydlighet. Selektiv
from-import är ett av de tre alternativ kap 13.3.1 explicit nämner — vi följer alltså
boken, bara inte det specifika exempel kap 1.1.4 visar.

**Varför `plt.` alltid kvar?** matplotlib är en *ritmiljö*, inte enskilda
matematiska funktioner — konvention är att alltid hålla det i sin namnrymd.

**Trolig följdfråga: "Varför inte `from numpy import *` som boken rekommenderar i kap 1.1.4?"**
→ Svar: Den importerar ~600 namn varav flera skuggar inbyggda Python-funktioner.
Konkret: efter `from numpy import *` är `sum([1,2,3])` faktiskt `numpy.sum`, inte
Pythons inbyggda `sum`. Samma sak med `min`, `max`, `any`, `abs`, `round`. Det är
ett pedagogiskt problem för läsare (och för oss själva) eftersom man inte ser av
`sum` ensam vilken sum det är. Vi valde en explicit variant där varje importerat
namn syns på första raden.

**Trolig följdfråga: "Varför inte bara `import numpy as np` rakt över?"**
→ Svar: `np.sqrt(x)` är längre och mindre matematiskt läsbart än `sqrt(x)`. För
funktioner som ser ut som matematiska formler vinner vi läsbarhet på prefix-fritt.
För systemverktyg är `np.`-prefix värdefullt eftersom det inte är matematiska
operationer — det signalerar "detta kommer från NumPy som verktyg".

**Trolig följdfråga: "Varför skriver ni `sqrt(x)` direkt men `np.asarray(...)` med prefix?"**
→ Svar: Vi importerade `sqrt` selektivt med `from numpy import sqrt`, men inte
`asarray`. Båda finns i NumPy — det är ett medvetet stilval, inte en inkonsekvens.

**Trolig följdfråga: "Boken säger ju `from numpy import *` på sidan 25 — har ni inte följt boken?"**
→ Svar: Vi har valt ett av de tre alternativ boken själv listar i kap 13.3.1 (selektiv
from-import). Boken är inte konsekvent själv — den rekommenderar `from numpy import *`
som default-header i kap 1.1.4 men diskuterar shadowing-problem och visar alternativ
i kap 13.3.1. Vi valde mellanvägen för läsbarhet plus säkerhet mot skuggning.

---

## Steg 3: Gå igenom notebooken cell för cell

### 3a. Task 1 — `approx_ln(x, n)`

Läs koden rad för rad och förklara högt:
1. `x = np.asarray(x, dtype=float)` — "konverterar till array"
2. `a = (1 + x) / 2` — "initierar a_0 enligt formeln"
3. `g = sqrt(x)` — "initierar g_0"
4. Loopen: "kör n iterationer, uppdaterar a och g simultant"
5. `return (x - 1) / a` — "approximationen enligt Carlsons formel"

**Knepig rad:** `a, g = (a + g) / 2, sqrt((a + g) / 2 * g)`
- Python evaluerar *högerledet helt* innan tilldelning
- Alltså används det gamla `a` och `g` i båda beräkningarna
- Ekvivalent med: `a_new = (a+g)/2; g_new = sqrt(a_new * g); a = a_new; g = g_new`

Testcellen direkt efter visar `approx_ln(2, 5)` och `approx_ln(2, 20)` jämfört
med `log(2)` — notera att n=20 ger ungefär maskinprecision.

### 3b. Task 2 — `plot_comparison()`

Två subplots:
- **Vänster:** `ln(x)` och `approx_ln(x, n)` för n = 1, 2, 3, 5 över `linspace(0.01, 5, 200)`
- **Höger:** differensen `approx_ln(x, n) - ln(x)`

**Trolig följdfråga:** "Vad händer nära x = 1?"
→ Svar: Approximationen är exakt vid x = 1 (båda sidor = 0), så felet är minst där.

### 3c. Task 3 — `plot_error_convergence()`

- `x = 1.41`, n = 0..15
- `semilogy` = logaritmisk y-axel
- Visar att felet minskar mycket snabbt (kvadratisk konvergens)

**Trolig följdfråga:** "Varför logaritmisk y-axel?"
→ Svar: Felet minskar exponentiellt, så på en linjär skala ser man inte
  skillnaden mellan t.ex. 10^(-5) och 10^(-15). Log-skala visar konvergenshastigheten tydligt.

### 3d. Task 4 — `_compute_a_values` och `fast_approx_ln`

**`_compute_a_values(x, n)`:** samma iteration som `approx_ln`, men sparar
*alla* `a_i`-värden i en array. Behövs för Richardson-tabellen som kräver
`a_0, a_1, ..., a_n`.

**Trolig följdfråga:** "Varför en separat hjälpfunktion?"
→ Svar: `approx_ln` behöver bara sista `a_n`. `fast_approx_ln` behöver alla.
  Hjälpfunktionen undviker kodduplicering.

**`fast_approx_ln(x, n)` stegvis:**
1. Hämta alla a-värden: `a_vals = _compute_a_values(x, n)`
2. Skapa tom tabell: `d = zeros((n+1, n+1))`
3. Fyll första raden: `d[0, i] = a_i` (basvärdena)
4. Dubbelnästlad loop: fyll resten av tabellen med Richardson-formeln
5. Returnera `(x-1) / d[n, n]` (det mest förfinade värdet)

**Förstå tabellen:**
```
d[0,0]  d[0,1]  d[0,2]  d[0,3]   ← a-värdena direkt
        d[1,1]  d[1,2]  d[1,3]   ← 1 felterm eliminerad
                d[2,2]  d[2,3]   ← 2 feltermer eliminerade
                        d[3,3]   ← 3 feltermer eliminerade (bästa!)
```

Testcellen visar att `fast_approx_ln(2, 5)` redan når maskinprecision
— jämför med `approx_ln(2, 20)` som behöver 20 iterationer för samma noggrannhet.

### 3e. Task 5 — `plot_fast_convergence()`

- `x ∈ linspace(0.01, 20, 300)`, n = 2..6
- `np.vectorize(fast_approx_ln)` eftersom `fast_approx_ln` endast tar skalär input
- Semilog-plot av `|fast_approx_ln(x, n) - ln(x)|`
- Visar att felet redan vid n=4–5 ligger nära maskinprecision (~1e-15)

---

## Designval — försvar av lösningens arkitektur

Läraren frågar ofta "varför gjorde ni så här?" snarare än "vad gör koden?".
Här är de val vi har gjort och hur vi försvarar dem:

1. **Varför AGM-iteration över t.ex. Taylor-serien?**
   AGM har **kvadratisk konvergens överallt** för x > 0. Taylor-serien för
   ln(x) konvergerar bara på (0, 2] och **långsamt** nära intervallets kanter.
   AGM är robust för stort spann av x.

2. **Varför hjälpfunktion `_compute_a_values` med underscore?**
   Underscore signalerar **"intern användning"** (Python-konvention). Helpern
   undviker kodduplicering med `approx_ln` och separerar AGM-iterationen från
   Richardson-logiken — varje funktion gör en sak.

3. **Varför simultant tilldelning `a, g = ..., ...` i Task 1, men separata rader i `_compute_a_values`?**
   I Task 1 är det kompakt och elegant. I helpern *behöver* vi ändå lagra
   `a_vals[i+1]` mellan iterationerna, så två rader läses tydligare. **Båda
   är korrekt** — valet är stilistiskt, inte funktionellt.

4. **Varför `np.asarray(x, dtype=float)` i `approx_ln` men inte i `_compute_a_values`?**
   `approx_ln` är vårt **publika API** (Task 1 säger att den ska kunna ta
   arrayer). Helpern är intern och anropas bara med skalär. Vi validerar bara
   där det behövs.

5. **Varför `np.vectorize` i Task 5 istället för att skriva om `fast_approx_ln`?**
   Richardson-tabellen är 2D **per skalärt x**. Äkta vektorisering skulle
   kräva en 3D-tabell (en per x-värde) — krångligt med liten vinst för 300
   punkter. `np.vectorize` är en pragmatisk genväg. Lärare kan invända: "Det är
   inte äkta vektorisering" — håll med och förklara avvägningen.

6. **Varför Richardson-tabell istället för en formel `d[n,n]` direkt?**
   Tabellen exponerar **mellanresultat** — vi kan kontrollera, debugga och
   förklara varje steg. Det finns en sluten formel men den döljer strukturen.
   Pedagogiskt val.

7. **Varför `linspace(0.01, 5, ...)` istället för `linspace(0, 5, ...)`?**
   `ln(0) = -∞` och `g_0 = sqrt(0) = 0` → division med noll i `(x-1)/a`. 0.01
   är ett säkert avstånd från singulariteten.

8. **Varför `n=2..6` i Task 5, inte `n=1..6`?**
   Richardson kräver minst två a-värden för att eliminera en felterm. Med n=1
   ger Richardson-tabellen samma resultat som ren Carlson — ingen poäng.

---

## Edge cases och begränsningar

Vad händer om läraren testar ovanlig input? Var ärlig om begränsningarna:

- **x ≤ 0:** Vi har **ingen validering**. `sqrt(x)` ger NaN för negativt x →
  NaN propagerar genom hela beräkningen. Borde haft
  `if x <= 0: raise ValueError("x måste vara > 0")`.
- **x = 1:** Returnerar **exakt 0** för alla n (täljaren `x - 1 = 0`). Ingen
  bugg — matematiskt korrekt eftersom ln(1) = 0.
- **x mycket stor (≫ 20):** Konvergensen blir långsammare. Carlson har en
  felterm proportionell mot avståndet `|x - 1|`. Plotten i Task 5 visar detta.
- **n = 0:** Ger formeln `2(x-1)/(1+x)` (nollte iteration, bara `a_0`). Test
  `test_zero_iterations` verifierar detta.
- **`fast_approx_ln([1, 2, 3], 5)`:** **Kraschar** — `_compute_a_values` är
  bara skriven för skalär. Vi har `np.vectorize` som workaround, men det är
  inte dokumenterat i `fast_approx_ln`'s docstring.
- **Mycket stort n:** `4**(-n)` underflödar runt n ≈ 540, men vi når
  maskinprecision långt före det (vid n ≈ 5–6) så det är aldrig ett problem
  i praktiken.

---

## Numerisk kontext — vad lärare gärna fördjupar i

- **Kvadratisk konvergens:** Antalet korrekta siffror **fördubblas** för
  varje iteration. Det är därför Task 3 visar att vi går från ~1 korrekt
  siffra (n=1) till ~15 korrekta siffror (n=15) — felet sjunker som
  `O(c^(2^n))` för någon konstant c < 1.

- **Maskinprecision (kursboken kap 2.2.2):** För `float64` är
  `sys.float_info.epsilon ≈ 2.22e-16`. Felkurvorna i Task 3 och Task 5
  **planar ut runt 10^(-15) till 10^(-16)** — det är inte algoritmens fel,
  det är representationens absoluta gräns. Man kan inte göra bättre än så
  med 64-bit floats oavsett hur många iterationer man gör.

- **Vektorisering vs loop:** `approx_ln` är **äkta vektoriserad** — alla
  NumPy-operationer (`+`, `/`, `sqrt`) fungerar element-för-element på hela
  arrayen, körs i C internt. `np.vectorize` är en **wrapper** som anropar
  funktionen en gång per element i Python — alltså en dold for-loop. Lärare
  kan fråga: "Vilken är snabbare för 1 miljon punkter?" → äkta vektorisering
  vinner stort (faktor 10–100x).

- **Extrapolation som koncept:** Richardson-idén används överallt i numerisk
  analys — Romberg-integration, Aitken-acceleration, finita differenser. Det
  vi visar är att vi förstår **idén** (känn felets struktur → eliminera
  ledande termer), inte bara formeln. Generaliserbar kunskap.

---

## Genomgång av test_solution.py

Vi bör veta vad varje test gör — läraren kan bläddra dit och fråga.

| Test | Vad det testar |
|------|----------------|
| `test_ln_of_one` | `ln(1) = 0` exakt, för alla n |
| `test_zero_iterations` | n=0 ger formeln `2(x-1)/(1+x)` |
| `test_convergence` | Felet är monotont avtagande med n |
| `test_accuracy_high_n` | n=10 ger noggrannhet ≤ 10⁻¹⁰ |
| `test_array_input` | `approx_ln` kan ta NumPy-array som input |
| `test_various_x` | Parametriserad sweep över [0.1, 0.5, 1.0, 1.41, 2.0, 5.0, 10.0] |
| `test_better_than_basic` | `fast_approx_ln(x, n)` är bättre än `approx_ln(x, n)` |
| `test_accuracy_fast` | `fast_approx_ln` med n=4 ger noggrannhet ≤ 10⁻¹⁴ |

**Vad som *inte* testas (var ärlig om det):**
- x ≤ 0 (ingen validering finns ändå)
- Array-input för `fast_approx_ln` (skulle krascha)

Kör testerna före mötet:
```bash
cd homework/homework1
pytest test_solution.py -v
```

---

## Steg 4: Kör notebooken och experimentera

```bash
cd homework/homework1
source ../../.venv/bin/activate
jupyter lab solution.ipynb    # eller öppna i VS Code
pytest test_solution.py -v    # Kör testerna
```

I VS Code: öppna `solution.ipynb` och kör cellerna i ordning (Shift+Enter).

Prova i en extra cell eller i `scratch/playground.py`:
```python
from homework.homework1.solution import approx_ln, fast_approx_ln
import numpy as np

# Testa för hand — följ iterationen steg för steg
x = 2.0
a = (1 + x) / 2   # = 1.5
g = np.sqrt(x)     # ≈ 1.414

# Steg 1
a = (a + g) / 2    # ≈ 1.457
g = np.sqrt(a * g) # ≈ 1.443

print(f"approx_ln(2, 1) = {(x-1)/a:.6f}")
print(f"numpy ln(2)     = {np.log(2):.6f}")

# Jämför basic vs fast
for n in range(6):
    err_basic = abs(approx_ln(x, n) - np.log(x))
    err_fast = abs(fast_approx_ln(x, n) - np.log(x))
    print(f"n={n}: basic error = {err_basic:.2e}, fast error = {err_fast:.2e}")
```

---

## Steg 5: Öva muntlig förklaring

Öva att förklara dessa tre saker i **max 2 minuter var**:

1. **"Beskriv algoritmen"** — AGM-iterationen, varför den ger ln(x), vad konvergens innebär
2. **"Vad gör Richardson-extrapolation?"** — Eliminerar feltermer, tabellstrukturen, varför det ger snabbare konvergens
3. **"Förklara en specifik cell/rad"** — Var beredd på att läraren pekar på valfri rad och frågar "vad gör denna?"

---

## Hur jag använt Claude i detta arbete

Vi har blivit rekommenderade att **inte använda AI för att skriva kod**, för att vi
ska kunna lära oss själva. Däremot är det OK att använda AI för att **lära sig**.
Här är vad jag faktiskt gjort, formulerat så jag kan säga det rakt ut om läraren
frågar.

**Konkret formulering att kunna säga muntligt:**

> *"Jag har använt Claude som ett pedagogiskt verktyg, inte för att skriva kod.
> Specifikt bad jag Claude visa mig vad kursboken faktiskt säger om NumPy-imports,
> och fick ordagranna citat från kap 1.1.4 (som rekommenderar `from numpy import *`
> som default-header) och kap 13.3.1 (som visar tre alternativ och diskuterar
> shadowing). Med citaten framför mig diskuterade jag och Sixten för- och nackdelar
> och valde en hybrid: selektiv from-import för matematiska funktioner, alias för
> systemverktyg. Det är ett av de tre alternativ boken själv nämner i kap 13.3.1."*

**Backup-formuleringar** om läraren ifrågasätter AI-användningen:

- *"Varje rad kod är min — jag kan förklara den. Claude har inte skrivit lösningen."*
- *"Claude hjälpte mig hitta och citera relevanta avsnitt i kursboken så jag kunde ta
  ett välgrundat beslut. Det är ett verktyg för att läsa boken effektivare, inte för
  att slippa läsa själv."*
- *"När Claude tidigare gav mig ett svar som inte stämde med boken — i just det här
  fallet hade Claude sagt att kap 13.3 'avråder uttryckligen' från `from numpy import *`,
  vilket inte är sant — hittade jag felet genom att läsa boken själv. Det är så jag
  kvalitetssäkrar AI-användningen: jag verifierar mot källan."*

**Vad jag medvetet inte kommer säga** (för att det skulle vara missvisande):

- *"Claude rekommenderade hybriden därför valde vi den"* — det är inte hela bilden.
  Jag började med Claudes resonemang, upptäckte att en del av motiveringen inte
  stämde med boken, läste boken själv och bestämde mig då medvetet om hybriden.
  Det är min slutsats med Claude som hjälpmedel, inte Claudes diktat.

---

## Beredskap för live-uppgift (Unit 03)

Klasskamrater har rapporterat att läraren ofta ber om en liten task live för
att se att vi har koll på Python utöver homework. Vi har också fått en
**konkret pekpinne**: vi ska kunna programmera **absolutbelopp med `if`**.
Det är högsta prioritet.

### PRIO 1 — Absolutbelopp med `if`

Skriv en egen funktion som **inte** använder Pythons inbyggda `abs`:

```python
def absolutbelopp(x):
    if x < 0:
        x = -x
    return x
```

Alternativ med `else` (också godkänt, men onödigt — `return x` täcker båda fall):
```python
def absolutbelopp(x):
    if x < 0:
        return -x
    else:
        return x
```

Testfall som vi kan visa läraren spontant:
```python
print(absolutbelopp(-3))    # 3
print(absolutbelopp(5))     # 5
print(absolutbelopp(0))     # 0
print(absolutbelopp(-2.5))  # 2.5
```

**Troliga följdfrågor och svar:**

- *"Vad händer för x = 0?"*
  → `0 < 0` är False, så vi går rakt till `return x`. Returnerar 0. Korrekt.
- *"Funkar den för flyttal?"*
  → Ja, `<` och unärt minus fungerar för både int och float.
- *"Funkar den för en NumPy-array?"*
  → **Nej.** `if x < 0:` ger `ValueError: The truth value of an array with
  more than one element is ambiguous`. För arrayer behövs `np.where(x < 0, -x, x)`
  eller helt enkelt `np.abs(x)`.
- *"Vad om jag passerar en sträng?"*
  → `'a' < 0` ger `TypeError` i Python 3. Vi har ingen typvalidering.
- *"Varför inte använda `abs(x)`?"*
  → Pythons inbyggda `abs` gör samma sak (för numeriska typer). Uppgiften är
  pedagogisk: visa att vi behärskar villkorslogik med `if`.
- *"Kan du skriva det utan `if`?"*
  → Ja:
    - `return x if x >= 0 else -x` (conditional expression / ternary)
    - `return max(x, -x)` (smart men "fusk" — använder `max`)
    - `return (x**2)**0.5` (matematiskt korrekt men sämre numeriskt och bara för reella tal)

### PRIO 2 — Övriga sannolika live-uppgifter

Om läraren går vidare eller varierar:

1. **"Skriv Newton's method för en ny funktion."**
   Vi har redan `newton(f, fp, x_0, Tol)` i `unit03_functions/exercise04.ipynb`.
   Variation: `f(x) = sin(x) - 0.5`, `fp(x) = cos(x)`, x_0 = 0. Skiss:
   ```python
   def newton(f, fp, x_0, Tol):
       x_old, x = x_0, x_0 - f(x_0)/fp(x_0)
       for _ in range(400):
           if abs(x - x_old) < Tol:
               return x, True
           x_old, x = x, x - f(x)/fp(x)
       return x, False
   ```

2. **"Implementera bisection rekursivt."** (Inte gjort tidigare!)
   ```python
   def bisect(f, a, b, tol):
       m = (a + b) / 2
       if abs(b - a) < tol:
           return m
       if f(a) * f(m) < 0:
           return bisect(f, a, m, tol)
       else:
           return bisect(f, m, b, tol)
   ```

3. **"Skriv en lambda för X."**
   T.ex. `dubbel = lambda x: 2*x` eller `lambda x, y: max(x, y)`. Lambda är
   en uttryckskort form av `def` — bara en rad, inget `return`-nyckelord.

4. **"List comprehension för att filtrera/transformera."**
   ```python
   nums = [-2, 3, -5, 7, 0]
   positiva_kvadrater = [x**2 for x in nums if x > 0]   # [9, 49]
   ```

5. **"Closure / `make_adder(n)`."** Returnera en funktion som "kommer ihåg" n:
   ```python
   def make_adder(n):
       def add(x):
           return x + n
       return add

   add5 = make_adder(5)
   print(add5(10))   # 15
   ```

6. **"Plotta f(x) för givet intervall."** Bör kunna utan att slå upp:
   ```python
   import numpy as np
   import matplotlib.pyplot as plt
   x = np.linspace(-5, 5, 200)
   plt.plot(x, np.sin(x))
   plt.show()
   ```

7. **"Förklara `*args` och `**kwargs` med exempel."**
   `*args` = variabelt antal positionsargument (tuple).
   `**kwargs` = variabelt antal keyword-argument (dict).
   ```python
   def summa(*args):
       return sum(args)
   summa(1, 2, 3)       # 6
   summa(*[1, 2, 3])    # 6 — unpacking
   ```

### Allmänna Unit 03-koncept att kunna förklara muntligt

Även utan live-task kan läraren fråga:

- **Scope** — lokal vs global. Variabler inuti funktioner är lokala. `global`
  används för att ändra en yttre variabel inifrån — undvik om möjligt
  (dålig stil, hård att debugga).
- **Mutability** — listor/dicts är *mutable* (passas som referens — funktioner
  kan ändra dem). Tal/strängar/tuples är *immutable*.
- **Default arguments** måste komma **efter** obligatoriska parametrar:
  `def f(x, n=10)` ✓, `def f(n=10, x)` ✗ (SyntaxError).
- **Funktioner är förstklassiga objekt** — kan tilldelas variabler, passas
  som argument, returneras från andra funktioner.
- **Lambda är bara en uttryckskort form av `def`** — inget mer mystiskt än så.

---

## Egna frågor / att följa upp

**Live-uppgift (högst prioritet — bekräftad av läraren):**
- [ ] **Kan vi spontant skriva `absolutbelopp(x)` med `if`** — utan att titta?
- [ ] Kan vi förklara varför vår `absolutbelopp` returnerar 0 för input 0?
- [ ] Vet vi minst ett alternativ utan `if` (ternary, `max`, etc.)?

**Homework-koden:**
- [ ] Förstår vi varför `a, g = ...` uppdateras simultant? (Task 1)
- [ ] Kan vi rita Richardson-tabellen för hand med t.ex. n=3?
- [ ] Förstår vi varför konvergensen är långsammare för stora x?
- [ ] Kan vi förklara varje pyplot-anrop i plottfunktionerna?
- [ ] Kan vi förklara skillnaden mellan vår import-stil och `from numpy import *`?
- [ ] Vet vi vad som händer om x = -1 eller x = 0 i `approx_ln`?
- [ ] Kan vi förklara varför `np.vectorize` inte är "äkta" vektorisering?
- [ ] Kan vi nämna machine epsilon (~2.22e-16) och varför felet planar ut där?

**Unit 03 backup-koncept:**
- [ ] Kan vi spontant skriva en rekursiv `bisect`?
- [ ] Kan vi spontant skriva `make_adder(n)` som closure?
- [ ] Kan vi förklara skillnaden mellan `*args` och `**kwargs`?
- [ ] Kan vi förklara mutability (vad händer när vi passerar en lista till en funktion)?

**Praktiskt före mötet:**
- [ ] `pytest test_solution.py -v` — alla tester gröna?
- [ ] Öppnat notebook:n och kört alla celler en gång?
- [ ] Plottarna ser ut som väntat?
