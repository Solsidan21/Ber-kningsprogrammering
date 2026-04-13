# Homework 1 -- Approximating the Logarithm

**Kurs:** NUMA01: Computational Programming with Python
**Larare:** Malin Christersson, Robert Klofkorn

---

This assignment has 5 tasks.
Before you start working on this homework, **sign up for a homework group in Canvas (max 2 person / meeting)**.

All the functions must be *properly documented* and also tested. We recommend that you produce a report of your work by **handing in a Python file** or with Jupyter Notebook (see lecture). You should work and present in **groups by two (homework group)**. Upload your solution via the homework page as a \*.py file or an \*.ipynb file. When uploaded book an appointment via the calendar function of the course webpage.

---

## Iterations

### Theory

In this homework we will approximate the log-function by an iteration method. Every iteration improves the result. The iteration is described in:

> B.C. Carlson: *An Algorithm for Computing Logarithms and Arctangents*, MathComp. 26 (118), 1972 pp. 543-549. [DOI:10.1090/S0025-5718-1972-0307438-2](https://doi.org/10.1090/S0025-5718-1972-0307438-2).

It is based on computing the arithmetic and geometric mean of two values a_i, g_i:

- For a given value x > 0, initialize a_0 = (1 + x) / 2, g_0 = sqrt(x),
- Iterate a_{i+1} = (a_i + g_i) / 2 and g_{i+1} = sqrt(a_{i+1} * g_i),
- Consider (x - 1) / a_i as an approximation to ln(x).

---

### Task 1

Write a function `approx_ln(x, n)` that approximates the logarithm by *n* steps of the above algorithm.

### Task 2

Plot both functions, ln and `approx_ln`, in one plot and the difference of both functions in another plot. Do this for different values of *n*.

### Task 3

Consider x = 1.41. Plot the absolute value of the error versus *n*.

### Task 4

In the above article a method is suggested to accelerate the convergence.
For i = 0, ..., n:

- d_{0,i} = a_i
- d_{k,i} = (d_{k-1,i} - 4^{-k} * d_{k-1,i-1}) / (1 - 4^{-k}),    k = 1, ..., i for i > 0

As approximation to ln the value (x - 1) / d_{n,n} is taken. Write a function `fast_approx_ln(x, n)` in which this approach is implemented.

### Task 5

Make a plot, which is **similar** to the plot given below.

> **Figure 1:** A plot to illustrate the speed of convergence of the approximation to ln.
>
> The plot shows "Error behavior of the accelerated Carlsson method for the log" with a logarithmic y-axis (error) and x on the x-axis (0 to 20). Lines are shown for iterations 2 through 6, demonstrating rapidly decreasing error with higher iteration count. The y-axis ranges from 10^{-19} to 10^{-5}.

---

Good luck!
