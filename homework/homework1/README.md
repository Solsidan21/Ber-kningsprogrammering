# Homework 1 — Approximating the Logarithm

**Deadline:** Fredag 24 april 2026, kl 23:30
**Presentation:** Muntlig (grupp om 2)
**Studenter:** Arvid Brenner & Sixten Midsem

---

## Bakgrund

Vi approximerar log-funktionen med en iterationsmetod baserad på:

> B.C. Carlson: *An Algorithm for Computing Logarithms and Arctangents*, MathComp. 26 (118), 1972 pp. 543-549.

Metoden bygger på aritmetiskt och geometriskt medelvärde:

- Givet x > 0, initiera a_0 = (1 + x) / 2, g_0 = sqrt(x)
- Iterera: a_{i+1} = (a_i + g_i) / 2 och g_{i+1} = sqrt(a_{i+1} * g_i)
- Approximera ln(x) som (x - 1) / a_i

---

## Uppgifter

### Task 1
Skriv en funktion `approx_ln(x, n)` som approximerar logaritmen med *n* steg av ovanstående algoritm.

### Task 2
Plotta bada funktionerna, ln och `approx_ln`, i en plot och differensen av bada funktionerna i en annan plot. Gor detta for olika varden av *n*.

### Task 3
Betrakta x = 1.41. Plotta absolutvardet av felet mot *n*.

### Task 4
I artikeln foreslas en metod for att accelerera konvergensen (Richardson-extrapolation).
For i = 0, ..., n:

- d_{0,i} = a_i
- d_{k,i} = (d_{k-1,i} - 4^{-k} * d_{k-1,i-1}) / (1 - 4^{-k}),    k = 1, ..., i for i > 0

Som approximation till ln tas vardet (x - 1) / d_{n,n}. Skriv en funktion `fast_approx_ln(x, n)` som implementerar detta.

### Task 5
Gor en plot som illustrerar konvergenshastigheten for den accelererade metoden. Plotten ska visa felbeteendet med logaritmisk y-axel, for iterationer 2 till 6, med x pa x-axeln (0 till 20).

---

## Krav
- Funktioner ska vara **dokumenterade** (docstrings)
- Funktioner ska vara **testade** (pytest)
- Lamna in som .py eller .ipynb
- Muntlig presentation i grupp
