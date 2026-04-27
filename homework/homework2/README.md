# Homework 2 — Interval Analysis

**Deadline:** Måndag 11 maj 2026, 12:00
**Tillgänglig till:** 15 juni 2026, 23:59
**Presentation:** Muntlig (grupp om 2)
**Studenter:** Arvid Brenner & Sixten Midsem

---

## Background

Interval analysis is a branch of mathematics that deals with the theory of intervals. Instead of e.g. real numbers, the basic objects in interval analysis are closed intervals [a, b].

The motivation: in the real world, measurements are usually not exact, but come with some error margin. So the mass of an object might be m = 3 ± 10⁻³ kg if the scale has a sensitivity of 1 g, naturally expressed as m ∈ [3 − 10⁻³, 3 + 10⁻³] kg. If we also measure the acceleration a ∈ [2 − 10⁻², 2 + 10⁻²] m/s², then by Newton's second law F = ma the force lies in

    F ∈ [(3 − 10⁻³)(2 − 10⁻²), (3 + 10⁻³)(2 + 10⁻²)].

The lower limit on the measurement error is less than the upper limit, so we cannot write F = 6 ± err without losing information.

For a binary operator ⊙,

    [a, b] ⊙ [c, d] = { z ∈ ℝ | z = x ⊙ y, x ∈ [a, b], y ∈ [c, d] }
                    = [min(a⊙c, a⊙d, b⊙c, b⊙d), max(a⊙c, a⊙d, b⊙c, b⊙d)].

For the four basic arithmetic operators:

    [a, b] + [c, d] = [a + c, b + d]
    [a, b] − [c, d] = [a − d, b − c]
    [a, b] · [c, d] = [min(ac, ad, bc, bd), max(ac, ad, bc, bd)]
    [a, b] / [c, d] = [min(a/c, a/d, b/c, b/d), max(a/c, a/d, b/c, b/d)],   0 ∉ [c, d]

The power x ↦ xⁿ for n ≥ 1 must be handled carefully. For odd n,

    [a, b]ⁿ = [aⁿ, bⁿ].                                                    (1)

For even n > 0,

    [a, b]ⁿ = | [aⁿ, bⁿ]            if a ≥ 0,                              (2)
              | [bⁿ, aⁿ]            if b < 0,
              | [0, max(aⁿ, bⁿ)]   otherwise.

Note that powers of intervals are *not* repeated products, i.e. [a, b]² ≠ [a, b] * [a, b].

---

## Tasks

This assignment has 11 tasks.

### Task 1
Construct a class `Interval` which is initialized with two real numbers representing the left and right endpoints respectively.

### Task 2
Provide methods for the four basic arithmetic operations.

### Task 3
Provide a method on your class so that the code

```python
i = Interval(1, 2)
print(i)
```

prints

```
[1, 2]
```

### Task 4
Make sure that the following code works as expected and prints the values given in the comments:

```python
I1 = Interval(1, 4)    # [1, 4]
I2 = Interval(-2, -1)  # [-2, -1]
I1 + I2                # [-1, 3]
I1 - I2                # [2, 6]
I1 * I2                # [-8, -1]
I1 / I2                # [-4., -0.5]
```

Please note: use `__truediv__` for the division.

### Task 5
Implement the `__contains__` method for checking if a real value is within the given interval.

### Task 6
Extend your division function so that it raises appropriate exceptions if the dividing interval contains zero, or if the resulting interval would be infinitely large.

### Task 7
A real number r is naturally identified with a degenerate interval [r, r]. Extend the class so that it can be initialized with only one real value, i.e.

```python
Interval(1)  # [1, 1]
```

### Task 8
Modify your code so that the following works:

```python
Interval(2, 3) + 1      # [3, 4]
1 + Interval(2, 3)      # [3, 4]
1.0 + Interval(2, 3)    # [3.0, 4.0]
Interval(2, 3) + 1.0    # [3.0, 4.0]
1 - Interval(2, 3)      # [-2, -1]
Interval(2, 3) - 1      # [1, 2]
1.0 - Interval(2, 3)    # [-2.0, -1.0]
Interval(2, 3) - 1.0    # [1.0, 2.0]
Interval(2, 3) * 1      # [2, 3]
1 * Interval(2, 3)      # [2, 3]
1.0 * Interval(2, 3)    # [2.0, 3.0]
Interval(2, 3) * 1.0    # [2.0, 3.0]
-Interval(4, 5)         # see the special method __neg__
```

### Task 9
Implement the power function x ↦ xⁿ (see equations (1) and (2)) as the `__pow__` function, so that one can write

```python
x = Interval(-2, 2)  # [-2, 2]
x**2                 # [0, 4]
x**3                 # [-8, 8]
```

### Task 10
Define a list of 1000 intervals by creating a list of lower boundary values with `xl = linspace(0., 1, 1000)` and upper boundaries `xu = linspace(0., 1, 1000) + 0.5`. Evaluate the polynomial

    p(I) = 3 I³ − 2 I² − 5 I − 1

on each interval I of your list of intervals and create in such a way another list of intervals. Extract from this list a list of lower boundaries `yl` and upper boundaries `yu` and plot both versus `xl`.

### Extra Task 11 (in case you want an extra challenge. Not mandatory!)

Based on your results from Task 3, you may be tempted to extend the interval class for multiple interval values all at once. In the end, `print(Interval(1, 1))` looks very similar to `print(array([1, 1]))`. Suppose you have obtained data for some measurement of interval points [aᵢ, bᵢ], i = 1, 2, …, N stored in arrays `A = array([a_1, ..., a_N])` and `B = array([b_1, ..., b_N])`.

1. Verify that the arithmetic operations are consistent. Consider multiplying the vectorized interval with some array C satisfying `C.shape == (N, N)`. From your knowledge in linear algebra, what result do you expect to obtain?
2. Perform Task 10 by writing `Interval(xl, xu)`. Do you get the same plot?
3. Consider Task 10 again. This time, take `xl = linspace(0, 1, 5_000_000)` and `xu = linspace(0, 1, 5_000_000) + 0.5`. What is the time difference between running `P(Interval(xl, xu))` compared to your original interval class (which only stores a single interval per instance)? Which one is faster? Why?

---

## Requirements

- All functions must be **properly documented** (docstrings)
- All functions must be **tested** when possible (`pytest`)
- Submit as `.py` or `.ipynb`
- Oral presentation in group of 2

Good luck!
