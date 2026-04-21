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

## Egna frågor / att följa upp

- [ ] Förstår vi varför `a, g = ...` uppdateras simultant? (Task 1)
- [ ] Kan vi rita Richardson-tabellen för hand med t.ex. n=3?
- [ ] Förstår vi varför konvergensen är långsammare för stora x?
- [ ] Kan vi förklara varje pyplot-anrop i plottfunktionerna?
