# Lecture 02 – Lists and Elementary Plotting

**Kursbok:** Kapitel 2 och 3 (sid 20, 22, 37)
**Lecturer:** Malin Christersson, Robert Klöfkorn

---

## Innehåll

- Användning av AI i programmering
- Listor
- Mer om for-loopar
- Grundläggande plotting

---

## AI i programmering

Kursen rekommenderar att man **undviker generativ AI** under kursen:
1. De flesta problem på denna nivå har svar via vanlig googling
2. Grundkunskapen du bygger här behövs för att kunna bedöma AI-genererad kod
3. Misstagen du gör nu har redan gjorts och övervunnits av alla som lärt sig programmera

---

## Listor

En Python-lista är en ordnad samling objekt, omsluten av hakparenteser `[]`. Element nås med **nollbaserade** index.

### Skapa och komma åt element

```python
L1 = [1, 2]
print(L1[0])   # 1
print(L1[1])   # 2
# print(L1[2]) # IndexError!

L2 = ['a', 1, [3, 4]]   # Kan blanda typer, inkl. nästlade listor
print(L2[2][0])          # 3
```

### Negativa index

```python
L2 = ['a', 1, [3, 4]]
print(L2[-1])   # [3, 4]  (sista elementet)
print(L2[-2])   # 1       (näst sista)
```

### range

```python
L3 = list(range(5))  # [0, 1, 2, 3, 4]
```

### len

```python
L4 = ["Stockholm", "Paris", "Berlin"]
print(len(L4))   # 3

L5 = [[0, 1], [10, 100, 1000, 10000]]
print(len(L5))       # 2 (antal toppnivå-element)
print(len(L5[-1]))   # 4
```

### append

```python
L6 = ['a', 'b', 'c']
L6.append('d')       # Lägger till i slutet
print(L6)            # ['a', 'b', 'c', 'd']

L6[0] = 'z'          # Kan ändra enskilda element
```

---

## List comprehension

Syntax: `[<uttryck> for <variabel> in <lista>]`

```python
L1 = [2, 3, 10, 1, 5]
L2 = [x*2 for x in L1]                    # [4, 6, 20, 2, 10]
L3 = [x*2 for x in L1 if 4 < x <= 10]    # [20]  (med villkor)
```

**Matematisk analogi:** L2 = {2x; x ∈ L1}

---

## Operationer på listor

### Konkatenering (sammanfogning)

```python
L1 = [1, 2]
L2 = [3, 4]
L3 = L1 + L2    # [1, 2, 3, 4]
```

### Multiplikation

```python
L = [1, 2]
L2 = 3 * L      # [1, 2, 1, 2, 1, 2]
```

---

## Inbyggda funktioner för listor

```python
L = [4, 9, -1, 2]
sum(L)    # 14
min(L)    # -1
max(L)    # 9
```

### Min/max för strängar

Jämför ledande tecken enligt UTF-8-ordning.

```python
L = ['!adbg', 'Berlin', 'Berl']
print(min(L))  # '!adbg'
print(max(L))  # 'Berlin'
```

---

## Metoder på listor

```python
L = [4, 9, -1, 2]
L3 = L.copy()      # Skapar en kopia
L.reverse()         # Vänder listan på plats
L.sort()            # Sorterar på plats
L.sort(reverse=True, key=myFunc)  # Med argument
L.insert(100, 8)    # Infoga 8 vid index 100 (eller i slutet)
```

---

## Programmerings-exempel

Beräkna summan 0 + 1 + 2 + ... + n:

```python
# Med for-loop
s = 0
n = 10
for i in range(n+1):
    s += i
print(s)   # 55

# Med list comprehension
s = sum([i for i in range(n+1)])

# Enklast
s = sum(range(n+1))
```

---

## Enumerering av listor

```python
L = ['C', 'l', 'o', 'u', 'd']

# Med enumerate (bästa sättet)
for i, l in enumerate(L):
    print(f"The {i}-th element of L is '{l}'")
```

---

## Slicing

`L[i:j]` ger element från index i till (men inte inklusive) j.

```python
L = ['C', 'l', 'o', 'u', 'd']

print(L[1:4])    # ['l', 'o', 'u']
print(L[1:])     # ['l', 'o', 'u', 'd']    (till slutet)
print(L[:3])     # ['C', 'l', 'o']          (från början)
print(L[-2:])    # ['u', 'd']               (sista 2)
print(L[:-2])    # ['C', 'l', 'o']          (allt utom sista 2)
```

### Sammanfattning av slicing

| Syntax | Beskrivning |
|--------|-------------|
| `L[i:]` | Alla element utom de i första |
| `L[:i]` | De första i elementen |
| `L[-i:]` | De sista i elementen |
| `L[:-i]` | Alla element utom de i sista |

---

## for-loopar (fördjupning)

### break

Avbryter loopen innan alla element har använts.

```python
x_values = [0, 2, 3, 4, 5]
threshold = 3.5
for x in x_values:
    if x > threshold:
        break
    print(x)
# Skriver ut: 0, 2, 3
```

### else (på for-loop)

`else`-blocket körs om loopen **inte** avbröts av `break`.

```python
threshold = 3.5
for x in x_values:
    if x > threshold:
        print("not all x are below the threshold")
        break
    print(x)
else:
    print("all the x are below the threshold")
```

---

## Grundläggande plotting

### Importera

```python
from numpy import *
from matplotlib.pyplot import *
```

### Enkel graf

```python
x_list = list(range(100))
y_list = [sqrt(x) for x in x_list]

plot(x_list, y_list, '-')
title('My first plot')
xlabel('x')
ylabel('Square root of x')
show()
```

### Flera kurvor med legend

```python
x_vals = [.2*n for n in range(20)]
y1 = [sin(.3*x) for x in x_vals]
y2 = [sin(2*x) for x in x_vals]

plot(x_vals, y1, label='sin(0.3*x)')
plot(x_vals, y2, label='sin(2*x)')
xlabel('x')
ylabel('sin...')
legend()
show()
```

### Fler nyckelord

```python
plot(x_vals, y2,
     color='green',
     linestyle='dashed',
     marker='o',
     markerfacecolor='blue',
     markersize=12,
     linewidth=6)
show()
```
