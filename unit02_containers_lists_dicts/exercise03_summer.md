# Training Assignment 03 – Containers, Lists, Dicts

**Kurs:** NUMA01: Computational Programming with Python
**Författare:** Malin Christersson, Robert Klöfkorn

---

## Syfte

Syftet med denna tränningsuppgift är att repetera list comprehensions, ge exempel på slicing, arbeta mer med funktioner och undersöka mängder (sets) i Python.

Uppgiften har **8 tasks**.

---

## Warming-up Exercises

Du ska *inte* köra koden innan du har skrivit ner vad den gör vid exekvering.

### Task 1

Anta att vi har lagrat följande värden i en lista:

```python
L = [0, 1, 2, 1, 0, -1, -2, -1, 0]
```

Vad blir resultatet av följande kommandon?

```python
L[0]
L[-1]
L[:-1]
L + L[1:-1] + L
L[2:2] = [-3]
L[3:4] = []
L[2:5] = [-5]
```

---

### Task 2

Vilka delar av koden nedan genererar ett fel, och varför?

```python
d = dict()

print(d['nokey'])
d['key'] = 3
print(d['key'])

del d['key']
print(d['key'])

d[(1, 2)] = 'tuple'
d[[1, 2]] = 'list'
```

---

### Task 3

*(Ingen beskrivning given i PDF:en -- troligen en muntlig/tavle-uppgift under övningen.)*

---

## Programming Exercises

### Task 4

Låt en avståndstabell mellan några byar ges av följande data:

```
 0  20  30  40
20   0  50  60
30  50   0  70
40  60  70   0
```

Konstruera en lista (av listor) som innehåller denna data. Kalla listan `distance`.

Konstruera från denna lista en lista `reddistance` som bara innehåller den relevanta datan i följande form:

```
20
30  50
40  60  70
```

Använd slicing för denna uppgift. Lös uppgiften på **två sätt**:

1. Med for-loopar
2. Med *enbart* list comprehension och slicing (inga for-loopar alls)

---

### Task 5

Låt A och B vara mängder. Mängden (A \ B) ∪ (B \ A) kallas den **symmetriska differensen** av de två mängderna.

Skriv en funktion som utför denna operation. Jämför dina resultat med resultatet av kommandot `A.symmetric_difference(B)`.

---

### Task 6

Studera även andra operationer på mängder. Du hittar en komplett lista genom att använda "tab"-tangenten i Spyder / IPython efter `A.`, där `A` är en tidigare definierad mängd i Python.

Studera särskilt metoderna `update` och `intersection_update`.

Förklara vad skillnaden mellan de två kommandona `intersection` och `intersection_update` är.

---

### Task 7

Testa i Python genom att betrakta ett par exempel påståendet att den tomma mängden är en delmängd av varje mängd.

---

## Bisection Method

> Om du inte hinner med följande uppgift under övningstillfället bör du göra den hemma, så att du kan ställa frågor under nästa föreläsning.

En kontinuerlig funktion som byter tecken i ett intervall [a, b] har minst ett nollställe i detta intervall. Ett sådant nollställe kan hittas med **bisektionsmetoden**.

Metoden utgår från det givna intervallet. Sedan undersöker den teckenbyten i delintervallen [a, (a+b)/2] och [(a+b)/2, b].

- Om tecknet byter i det **första** delintervallet, omdefinieras b till:

  b := (a + b) / 2

- Annars omdefinieras a på samma sätt:

  a := (a + b) / 2

Processen upprepas tills b - a är mindre än en given tolerans.

**Notera:** Ett teckenbyte karaktäriseras av villkoret f(a) * f(b) < 0.

---

### Task 8

Implementera denna algoritm. Den behöver det initiala intervallet [a, b] och toleransen.

Testa metoden med funktionen `arctan` och även med polynomet:

f(x) = 3x^2 - 5

i intervallet [-0.5, 0.6] och alternativt i [-1.5, -0.4].

Om du är osäker på dina resultat kan det vara hjälpsamt att plotta funktionerna i de givna intervallen.
