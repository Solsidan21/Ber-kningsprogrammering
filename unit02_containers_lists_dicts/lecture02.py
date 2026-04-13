#!/usr/bin/env python
# coding: utf-8

# # Computational Programming with Python
# ### Lecture 2: Lists and elementary plotting
#
# ### Center for Mathematical Sciences, Lund University
# Lecturer: Malin Christersson, Robert Klöfkorn


# ## This lecture
#
# - Intro Survey
# - Use of AI in Programming
# - Lists
# - More about for loops
# - Elementary plotting


# ## Lists
#
# A Python list is an ordered list of objects, enclosed in square brackets.
# One accesses elements of a list using zero-based indices inside square brackets.
# Note: list is the most commonly used container in Python.

# ### List examples

L1 = [1, 2]
print(L1[0])
print(L1[1])
print(type(L1))

L2 = ['a', 1, [3, 4]]
print(L2[0])
print(L2[2])
print(L2[2][0])


# ### Negative indices

L2 = ['a', 1, [3, 4]]
print(L2[-1])  # last element
print(L2[-2])  # second last element


# ### List utilities - range
# range(n) can be used to fill a list with n elements starting with zero.

L3 = list(range(5))  # numbers 0,1,2,3,4
print(L3)


# ### List utilities - len
# The function len(L) gives the length of a list:

L4 = ["Stockholm", "Paris", "Berlin"]
L5 = [[0,1], [10, 100, 1000, 10000]]
print(len(L4))
print(len(L5))
print("len(L5[-1])", len(L5[-1]))


# ### List utilities - append
# Use the method append to append an element at the end of the list.

L6 = ['a', 'b', 'c']
print(L6[-1])
print(len(L6))
L6[0] = 'd'
print(L6[0])
print(L6[-1])
print(len(L6))


# ### List comprehension
# A convenient way to build up lists.
# Syntax: [<expr> for <variable> in <list>]

L1 = [2, 3, 10, 1, 5]
L2 = [x*2 for x in L1]
L3 = [x*2 for x in L1 if 4 < x <= 10]
print(L1)
print(L2)
print(L3)


# ### Operations on lists
# Adding two lists concatenates them:

L1 = [1, 2]
L2 = [3, 4]
L3 = L1 + L2
print(L3)

# Multiplying a list with an integer:
L = [1, 2]
L2 = 3*L
print(L2)


# ## Some more functions

L = [4, 9, -1, 2]
print("The sum is", sum(L))
print("The minimum value is", min(L))
print("The maximum value is", max(L))


# ## Some more methods

L = [4, 9, -1, 2]
L3 = L.copy()
print("L =", L)
L.reverse()
print("L =", L)
L.sort()
print("L =", L)


# ## Programming example: sum(i) for i=0..n

s = 0
n = 10
for i in range(n+1):
    s += i
print(s)

s = sum(range(n+1))
print(s)


# ## Enumerating lists

L = ['C', 'l', 'o', 'u', 'd']
for i, l in enumerate(L):
    print(f"The {i}-th element of L is '{l}'")


# ## Slicing
# L[i:j] - elements from index i to j-1

L = ['C', 'l', 'o', 'u', 'd']
print(L[1:4])
print("L[1:] =", L[1:])
print("L[:3] =", L[:3])
print("L[-2:] =", L[-2:])
print("L[:-2] =", L[:-2])


# ## for loops - break and else

x_values = [0, 2, 3, 4, 5]
threshold = 3.5
for x in x_values:
    if x > threshold:
        break
    print(x)

threshold = 3.5
for x in x_values:
    if x > threshold:
        print("not all x are below the threshold")
        break
    print(x)
else:
    print("all the x are below the threshold")


# ## Elementary plotting

from numpy import *
from matplotlib.pyplot import *

x_list = list(range(100))
y_list = [sqrt(x) for x in x_list]

plot(x_list, y_list, '-')
title('My first plot')
xlabel('x')
ylabel('Square root of x')
show()


# ## More about plots - with labels and legend

x_vals = [.2*n for n in range(20)]
y1 = [sin(.3*x) for x in x_vals]
y2 = [sin(2*x) for x in x_vals]
plot(x_vals, y1, label='sin(0.3*x)')
plot(x_vals, y2, label='sin(2*x)')
xlabel('x')
ylabel('sin...')
legend()
show()


# ## A plot with more keywords

plot(x_vals, y2,
     color='green',
     linestyle='dashed',
     marker='o',
     markerfacecolor='blue',
     markersize=12,
     linewidth=6)
show()
