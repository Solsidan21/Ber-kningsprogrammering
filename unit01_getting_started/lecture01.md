# Lecture 01 – First Steps: A Bit of Everything

**Kursbok:** Kapitel 1
**Lecturer:** Robert Klöfkorn (Malin Christersson)

---

## Innehåll

- Om kursen
- Om Python
- Datatyper och variabler
- Villkorsuttryck (conditional expressions)
- Loopar
- Importera moduler

---

## Om kursen

14 föreläsningar:
- 5 grundläggande (datatyper, for-loopar, plotting, funktioner etc.)
- 2 om matriser/vektorer och linjär algebra
- 2 om objektorienterad programmering
- 1 om filhantering (data I/O)
- 2 om avancerad plotting inkl. interaktiv plotting
- 1 om debugging, timing och tidskomplexitet
- 1 om dataanalys med pandas

**Examination:**
- Training exercises (hand-in möjlig)
- Homework 1 & 2 (muntlig presentation 15-20 min)
- Final projects (muntlig presentation 20-40 min)
- Behöver klara HW1, HW2, Quiz och Final Project

**Kursbok:** *Scientific Computing with Python* – Führer, Solem, Verdier (2nd ed.), 2021. Finns som eBook via LU-biblioteket.

---

## Varför Python?

- Gratis och open source
- Skriptspråk (tolkat, ej kompilerat)
- Mängder av bibliotek: linjär algebra, visualisering, ODE-lösare, statistik etc.
- Används överallt: vetenskaplig beräkning, web, data mining...
- Relativt lätt att lära sig
- Ett av de mest populära programspråken

---

## Förutsättningar

- Python >= 3.x
- IPython shell
- Spyder eller VS Code
- Program börjar med `from numpy import *`

---

## Datatyper och variabler

### Numeriska datatyper

| Typ | Python | Matematisk notation |
|-----|--------|---------------------|
| Heltal | `int` | i ∈ Z |
| Reellt tal | `float` | x ∈ R |
| Komplext tal | `complex` | z ∈ C |

### Aritmetiska operatorer

| Operator | Beskrivning |
|----------|-------------|
| `+ - * /` | Addition, subtraktion, multiplikation, division |
| `**` | Exponentiering |
| `%` | Modulus (rest) |
| `//` | Heltalsdivision (kvot) |

### Variabler

Variabler är referenser till objekt. Man använder tilldelningsoperatorn `=`.

```python
my_int = 42
my_float = 3.14
my_complex = 5 + 1j  # OBS: j är suffix, inte variabel
z = 5 + 1j           # 5+j fungerar INTE (j tolkas som variabel)

my_int2 = int(3.14)  # => 3 (trunkerar, avrundar inte)
my_int3 = int(3.76)  # => 3
```

### Strängar

```python
str1 = '"Eureka" he shouted.'
str2 = "He had found what is now known as Archimedes' principle."
str3 = """This "Hello" is
a long,
long string."""
```

---

## Villkorsuttryck (Conditional Expressions)

### Booleska värden

```python
x = True
y = False
print(type(x))  # <class 'bool'>
```

### Jämförelseoperatorer

`==`, `!=`, `<`, `>`, `<=`, `>=`

```python
a = True
b = 0 < 3 < 6      # True (kedjad jämförelse)
c = (3*15 == 10)    # False
```

### Booleska operatorer

`and`, `or`, `not`

```python
print(not 3 > 5)                # True
print(36 % 6 == 0 and 36 < 0)  # False
print(36 % 6 == 0 or 36 < 0)   # True
```

Prioritet: `not` > `and` > `or` (jfr: teckenändring > multiplikation > addition)

### if-satser

```python
# En gren
x = -5
if x >= 0:
    print(x)
else:
    print(-x)

# Flera grenar
age = 6
if age < 18:
    print("You are a child.")
elif age < 68:
    print("You are an adult.")
else:
    print("You may retire.")
```

### Felhantering med villkor

```python
denom = 0
num = 3
if not denom == 0:
    frac = num / denom
else:
    print("Don't divide by zero!")
```

---

## Loopar

### while-loop

```python
i = 0
while i <= 10:
    print(i)
    i += 1  # GLÖM INTE detta, annars oändlig loop!
print("We obtain i =", i)
```

### for-loop

```python
s = 0
for i in range(11):  # 0, 1, 2, ..., 10
    s = s + 1
print("We obtain s =", s)
```

### Indentering

Indentering i Python är **obligatorisk** (till skillnad från många andra språk).

```python
for elt in my_list:
    do_something()      # inuti loopen
    something_else()    # inuti loopen
print("loop finished")  # utanför loopen
```

### range-funktionen

| Syntax | Beskrivning |
|--------|-------------|
| `range(stop)` | Heltal >= 0 och < stop |
| `range(start, stop)` | Heltal >= start och < stop |
| `range(start, stop, step)` | Start, sedan öka med step så länge < stop |

```python
for i in range(0, 100, 15):
    print(i)  # 0, 15, 30, 45, 60, 75, 90
```

---

## Importera moduler

```python
# Alternativ 1: importera hela modulen
import numpy
print(numpy.exp(1j * numpy.pi))

# Alternativ 2: ge kortare namn
import numpy as np
print(np.exp(1j * np.pi))

# Alternativ 3: importera specifika funktioner
from numpy import exp, pi
print(exp(1j * pi))

# Alternativ 4: star import (importera allt)
from numpy import *
print(exp(1j * pi))
```

---

## Exempel: Linjär algebra

```python
from numpy import array
from scipy.linalg import solve

M = array([[1., 2.],
           [3., 4.]])
V = array([2., 1.])
x = solve(M, V)
print(x)  # [-3.   2.5]
```

**OBS:** En rad kan fortsätta på nästa rad utan speciellt tecken så länge parenteser/brackets inte stängts.

---

## Exempel: Beräkningar

```python
from numpy import *
print(exp(1j * pi))   # Eulers formel: e^(iπ) ≈ -1
print(2**100)          # Python hanterar godtyckligt stora heltal
```

Allt efter `#` är en kommentar.
