# Training Assignment 05 – Polynomials, Integrals and Zeros

**Kurs:** NUMA01: Computational Programming with Python
**Lärare:** Malin Christersson, Robert Klöfkorn

---

This assignment has 8 tasks.

---

## Warming-up Exercises

Consult the lecture notes for solutions to the warming-up exercises.

### Task 1

Write a function that implements the following polynomial

    p(x) = ax^3 + bx^2 + cx + d.

### Task 2

Rewrite your polynomial from the previous task such that the coefficients are represented by a list (of length 4 in this case).

### Task 3

Discuss with your colleagues how to use the packing/unpacking techniques to use a list as input for the polynomial from the first task.

### Task 4

Rewrite your polynomial such that arbitrary polynomials can be represented, i.e. lists of coefficients of arbitrary length.

---

## Exercises

### Task 5

**Integrals**

Compute approximately the integral

    integral from 0 to pi/2 of sin(omega * x) dx

for omega = 2*pi.

For this end run at the beginning of your program the import statement

```python
from scipy.integrate import quad
```

The method to integrate a function f over an interval [a, b] is `quad` (quadrature is another word for integrate) and it is used as `quad(f,a,b)`.

It returns a tuple with the approximated solution and the estimated error. Check the help page of that function to see if it has some default arguments which you could set by other values.

### Task 6

**Integrals and plots**

Compute the integral

    integral from 0 to pi/2 of sin(omega * x) dx

for 1000 equidistant values of omega in the interval [0, 2*pi] and plot the results versus omega.

Label the axes and put a title to the plot.

### Task 7

**Zeros of a function**

In a previous training exercise you wrote your own program to find a zero (nollstalle) of a given function. Now we see how this can be done by a `scipy` method.

For this end use first

```python
from scipy.optimize import fsolve
```

The simplest use of the method is `fsolve(f,x0)` where f is the function of which a zero is calculated and x_0 is a guess where you expect the zero.

Compute the positive zero of the polynomial p(x) = x^2 + x - 3. Use your implemented polynomial with the appropriate coefficients.

### Task 8

**Zeros of a parameter dependent function**

Plot the positive zeros of the polynomials p(x) = a*x^2 + x - 3 for a in [1, 5] versus a.

Do the zeros depend linearly on a?
