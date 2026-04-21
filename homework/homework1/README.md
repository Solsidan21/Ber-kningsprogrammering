# Homework 1 — Approximating the Logarithm

**Deadline:** Friday 24 April 2026, 23:30
**Presentation:** Oral (group of 2)
**Students:** Arvid Brenner & Sixten Midsem

---

## Background

We approximate the logarithm with an iterative method based on:

> B.C. Carlson: *An Algorithm for Computing Logarithms and Arctangents*, MathComp. 26 (118), 1972 pp. 543-549.

The method uses the arithmetic and geometric means:

- Given x > 0, initialize a_0 = (1 + x) / 2, g_0 = sqrt(x)
- Iterate: a_{i+1} = (a_i + g_i) / 2 and g_{i+1} = sqrt(a_{i+1} * g_i)
- Approximate ln(x) as (x - 1) / a_i

---

## Tasks

### Task 1
Write a function `approx_ln(x, n)` that approximates the logarithm with *n* steps of the algorithm above.

### Task 2
Plot both functions, ln and `approx_ln`, in one plot and the difference of the two in another plot. Do this for several values of *n*.

### Task 3
Consider x = 1.41. Plot the absolute value of the error against *n*.

### Task 4
The article proposes a method to accelerate convergence (Richardson extrapolation).
For i = 0, ..., n:

- d_{0,i} = a_i
- d_{k,i} = (d_{k-1,i} - 4^{-k} * d_{k-1,i-1}) / (1 - 4^{-k}),    k = 1, ..., i for i > 0

The approximation of ln is taken as (x - 1) / d_{n,n}. Write a function `fast_approx_ln(x, n)` that implements this.

### Task 5
Make a plot illustrating the convergence rate of the accelerated method. The plot should show the error behavior with a logarithmic y-axis, for iterations 2 through 6, with x on the x-axis (0 to 20).

---

## Requirements
- Functions must be **documented** (docstrings)
- Functions must be **tested** (pytest)
- Submit as .py or .ipynb
- Oral presentation in group
