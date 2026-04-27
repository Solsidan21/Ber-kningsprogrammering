# Training Assignment 07 – Arrays and Numerical Linear Algebra

**Kurs:** NUMA01: Computational Programming with Python
**Lärare:** Malin Christersson, Robert Klöfkorn

---

This assignment has 5 tasks.

This task trains various aspects of arrays in connection with some methods of numerical linear algebra. It is based on Chapter 4 and 5 of the course book.

---

## Warming-up Exercises

### Task 1

Read Chapter 5 of the course book.

### Task 2

A student has produced the following code for implementing a matrix-vector product. Help the student to make the code run properly. After you provided an improved version the student wants to know why your code is correct. With confidence you explain why your version is correct!!

*Hint:* Each line of `matvec` contains one or more mistakes.

```python
from numpy import *

# returns y = A * x
def matvec(A, x):
    # make sure A has as many columns as x has entries
    y = x
    assert A.shape[1] == len(x)
    for r in range(1, A.shape[1]):
        for c in range(1, A.shape[0]):
            y[r] = A[c, r] * x[r]
    return y

x = array([1., 2., 3])
M = array([[1., 2, 3.],
           [4., 5., 6]])

z = matvec(M, x)
# is this correct?
print(z)
```

---

## Exercises

### Task 3

A central theorem in linear algebra says that the eigenvalues of real symmetric matrices are real and that their eigenvectors are orthogonal. Try to verify this theorem by using square random matrices of dimensions not less than 5.

Test your function.

### Task 4

For n ∈ ℕ construct an n × n matrix A with the properties

    A_{i,i}   = -2,   i = 1, ..., n
    A_{i+1,i} =  1,   i = 1, ..., n-1
    A_{i,i+1} =  1,   i = 1, ..., n-1

and all other elements being zero.

Do this task by using the numpy command `diag` or `eye`, or alternatively, by using for-loops. Write a function that takes an integer n and returns such a matrix.

### Task 5

Create a vector `x = linspace(0, 2*pi, 500)` and a vector `u = sin(x)`. Create the matrix D by calling the function from the previous task with n being the length of vector u. Compute y = D u and plot the result. Compare with a plot of the second derivative of sin(x).
