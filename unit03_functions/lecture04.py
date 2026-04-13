#!/usr/bin/env python
# coding: utf-8

# # Computational Programming with Python
# ### Lecture 4: Functions
# 
# ### Center for Mathematical Sciences, Lund University
# Lecturer: `Robert Klöfkorn`
# 

# ## This lecture
# 
# 
# - Basic features of functions
# - Scope of variables
# - Default arguments
# - Docstring
# - Parameters and arguments
# - Functions are objects

# ## Basic features
# 
# Comparing functions in mathematics and functions in Python

# In[ ]:


from numpy import*
from matplotlib.pyplot import *
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Functions in mathematics
# 
# A function is written as a map, that uniquely assigns an element $y$ from the range $R$ to every element $x$ of the domain $D$.
# 
# $$f:x \mapsto y$$
# 
# $f$ is the function, $x$ is its argument, $y$ is its (return) value
# 
# There can be several arguments of different type. Consider:
# 
# $$ f(g, a, b) = \int_a^b g(x) dx $$
# 
# The arguments are not interchangeable. Position matters.

# ## Functions in Python
# 
# Definition of a function:
# 
# ```python
# def f(x1, x2, x3):
#     # some computations
#     y = ... #
#     return y
# ```
# 
# Evaluation (call) of a function:
# 
# ```python
# f(17, 18, -2)
# f([1, 2, 3], {'tol': 1.e-10}, 'ro')
# ...
# ```
# 
# Wording:
# 
# `x1, x2, x3` are called **parameters** (needed for definition)
# 
# `17, 18, -2` are called **arguments** (needed for evaluation)

# ## Passing arguments
# 
# Consider:

# In[ ]:


def subtract(x1, x2):  
    return x1 - x2


# Passing arguments by position: (Position matters.)

# In[ ]:


subtract(2, 1) 
subtract(1, 2)


# Passing arguments by keywords: (Position doesn't matter)

# In[ ]:


subtract(x2=2, x1=1)


# ## Passing arguments (cont)
# 
# Positional arguments come first, then keyword arguments.

# In[ ]:


def add(x1, x2, x3, x4):
    return sum([x1, x2, x3, x4])

a1 = add(1, 2, x4=4, x3=3)  # this works
print("a1 =", a1)


# In[ ]:


a2 = add(1, 2, x3=3, 4)  # this doesn't work


# ## Scope of variables
# 
# Variables defined inside the function are said to belong to the function’s **scope**. They are unknown outside the function. 

# In[ ]:


c = 3 
def mult2(x):
    # global c
    # c = 2.   # a local variable
    #print(c)
    return c*x

print(mult2(20)) 
print(f"final result for c = {c}") # doesn't work, still has value 3


# ## Parameters and global variables
# 
# Compare:
# 
# `a` is a parameter of the function:
# ```python
# def multiply(x, a):
#     return a*x
# ```
# 
# `a` is referenced from outside of the  functions scope, a is a **global** variable:
# ```python
# a = 3
# def multiply(x):
#     return a*x
# ```

# ## Changing argument values inside a function
# 
# Example:

# In[ ]:


def myfunc(a, interval):
    a = 0
    print(a)
    interval1 = interval.copy()
    interval1[0] = 0


my_a = 10
my_interval = [-5, 7]
a = myfunc(my_a, my_interval)

print(f"my_a = {my_a}, my_interval = {my_interval}")


# ## Global variables
# 
# Example 1:

# In[ ]:


a = 3
def multiply(x):
    a = 4
    # a += 1 
    x = 4 
    return a*x

print(f"result = {multiply(5)} a = {a}")


# Inside the function, `a` is a local variable that is assigned a value.
# 
# The following code doesn't work:
# 
# ```python
# a = 3
# def multiply(x):
#     a = a + 1  # doesn't work
#     return a*x
# ```

# ## Default arguments
# 
# #### Example &hyphen; Free fall due to gravity
# 
# The force $F$ is proportional to the mass $m$, $F = mg$,
# where $g$ is the acceleration of gravity. 
# 
# On earth $g \approx 9,81 \text{ m}/\text{s}^2$.

# In[ ]:


def F(m, g = 9.81):
    return m*g

F1 = F(50)
F2 = F(50, 1.625)
print(f"On earth, the force is {F1:0.1f} Newton.")
print(f"On the mooon, the force is {F2:0.1f} Newton.")


# In the definition of the function, mandatory parameters must precede optional parameters (those with default values). Why?

# ## Arguments, Parameters - Summary
# 
# Make sure that you understood the difference
# 
# - between `arguments` and `parameters`
# - between function `definition` and function `evaluation` (call)
# - between `positional` arguments and `keyword` arguments

# ## Return
# 
# The `return` statement returns a **single** object!
# 
# ```python
# def myfunc(x):
#     return 1, 2, 3, 4, 5, 6
# ```
# 
# What is the object returned here? Which type does it have?
# 
# Statements after the `return` statement are ignored.
# 
# ```python
# def myfunc(x):
#     return 1, 2, 3
#     z = 25  # ignored
# ```

# ## No return
# 
# A function without a return statement returns `None`.

# In[ ]:


def show_message():
    print("Hello World!")

a = show_message()
print(type(a))

print(a is None)


# ## Returning multiple values
# 
# A function may return several values:

# In[ ]:


def argmin(L):  # return the minimum and index
    minimum = min(L)
    minimum_index = L.index(minimum)
    return minimum, minimum_index  # a tuple

min_info = argmin([1, 2, 0, 5])
print(type(min_info))
print("min_info =", min_info)
print(f"m = {min_info[0]} and i = {min_info[1]}")

# often unpacking is used directly
m, i = argmin([1, 2, 0, 5])
print(f"m = {m} and i = {i}")


# ## Functions as arguments
# 
# ### Example &hyphen; Numerical differentiation
# 
# 
# Let 
# 
# $$ f(x) = x^3 + x^2,$$
# 
# then
# 
# $$ f'(x) = 3x^2 + 2x$$
# 
# and 
# 
# $$f'(1) = 5.$$

# ###  Approximating the derivative
# 
# We can use some approximation to find the derivative.
# 
# Example 1:
# 
# $$f'(x) \approx \frac{f(x+h)-f(x)}{h} $$
# 
# Example 2:
# 
# $$f'(x) \approx \frac{f(x+h)-f(x-h)}{2h} $$
# 
# Where $h$ is some small number, e.g. $h=10^{-8}$.

# ### Example - Numerical differentiation (10min, let's go)
# 
# #### Part 1
# 
# Change the code so that the two derivative functions implement the approximations from last slide. Make it so that $h$ has a default value. Does a smaller value of $h$ make the approximation better?

# In[ ]:


def f(x):
    return x**3 + x**2

# TODO 1: Write a function that returns the derivative of f
def df(x):
    return 3*x**2 + 2*x

def derivative1(x, h = 1e-8):
    ...

def derivative2(x, h):
    ...

# TODO 2: write a function that uses the above approximations to 
#         compute the derivative, taking x, h as parameters
print(f"Exact derivative   f'(1) = {df(1)}")
print(f"Using derivative1, f'(1) = {derivative1(1, 0.00001)}")
print(f"Using derivative2, f'(1) = {derivative2(1, 0.00001)}")


# Discuss the result!

# In[ ]:


def f(x):
    return x**3 + x**2

def df(x):
    return 3*x**2 + 2*x

def derivative1(g, x, h = 1e-8):
    return (g(x+h) - g(x))/h

def derivative2(g, x, h = 1e-8):
    return (g(x+h)-g(x-h))/(2*h)

print(f"Exact derivative1, f'(1) = {df(1)}")
print(f"Using derivative1, f'(1) = {derivative1(f, 1, 0.00001)}")
print(f"Using derivative2, f'(1) = {derivative2(f, 1, 0.00001)}")


# #### Part 2
# 
# Change the code so that $h$ takes on the values 0.001, 0.0001, 0.00001,..., 0.000000001. Replace the stars ('*') in the f-strings with numerical values matching the top row, where `f'(1)` is the value obtained from `derivative1`. 

# In[ ]:


print("   h               f'(1)                 error")
print(56*"-")
for i in range(8):
    print(f"{'*':6} {'*':23} {'*':25}")


# In[ ]:


df_1 = 5.
print("   h                  f'(1)                 error")
print(56*"-")
h = 0.001
for i in range(12):
    print(f"{h:.6e} {derivative1(f,1,h):20.10f} {abs(df_1 - derivative1(f,1,h)):20.8f}")
    h *= 0.1


# ## Functions are objects
# 
# Functions are objects, they can be deleted, reassigned, copied ...

# In[ ]:


def square(x):
    return x**2

print("square(4) =", square(4))

sq = square  # now sq is the same as square

del square # square doesn't exist anymor

print("sq(4) =", sq(4))


# ### A functions that returns a function

# In[ ]:


def f(x, a, b, c, d): 
    return a*x**3 + b*x**2 + c*x + d

def derivative1(f, x, h = 1e-6): 
    return (f(x+h)-f(x))/h

def makeOneParameterFunc(f, a, b, c, d):
    def newf(x):
        return f(x, a, b, c, d)
    return newf  # a function is returned

newf = makeOneParameterFunc(f, 1, 1, 0, 0)

print(newf)
print("newf(1) =", newf(1))  
der = derivative1(newf, 1)
print("der =", der)


# ## Docstring
# 
# All functions (and everything else) should be documented carefully.
# 
# A docstring is the leading comment in a function (or class):
# 
# ```python
# def newton(f, x0): 
#     """
#     Newton’s method for computing a zero of a function on input:
#     f (function) given function f(x)
#     x0 (float) initial guess 
#     on return:
#     y (float) the approximated zero of f 
#     """
# ...
# ```
# 
# `help(newton)` in Python or `newton?` in IPython displays the docstring as a help text.

# ## Partial Application (or closures)
# 
# In mathematics we often "freeze" a parameter of a function: $f_\omega(x) = f(x, \omega) = \sin(\omega x)$
# 
# In Python we can do this:

# In[ ]:


def make_sin(omega):
    def f(x):
        return sin(omega*x)
    return f

fomega = make_sin(2)
figure(figsize = (4, 3))
x = linspace(0, 2*pi, 100)
xlabel('x')
ylabel('sin(omega *x)')
plot(x, fomega(x))


# ## Anonymous functions &hyphen; the `lambda` keyword
# 
# With $\lambda$-functions one has a handy tool making one-line function definitions:

# In[ ]:


f = lambda x: 3*x**2 + 2*x + 0.5

print(f(3))

g = lambda x, y: 3*x - 2*y

print(g(1, 1))


# Example for a common application, compute $\int_0^1 (x^2+5) \text{d}x$.

# In[ ]:


import scipy.integrate as si
result, error = si.quad(lambda x: x**2+5, 0, 1)
print(result)


# ## Closures and $\lambda$
# 
# $$f_\omega(x)=f(x, \omega) = \sin(\omega x)$$

# In[ ]:


omega = 3
fomega = lambda x: sin(omega*x)

result, error = si.quad(fomega, 0, 2*pi)
print(result)
x = linspace(0, 2*pi, 100)
plot(x, fomega(x))


# ### A shorter version of the derivative example

# In[ ]:


def f(x, a, b, c, d): 
    return a*x**3+b*x**2+c*x+d

def derivative1(f, x, h = 1e-6): 
    return (f(x+h)-f(x))/h

# fix parameters a,b,c,d to the given arguments
newf = lambda x: f(x,1,1,0,0)

print(newf)
print("newf(1) =", newf(1))  
der = derivative1(newf, 1)
print("der =", der)


# ## The plot example from Lecture 2

# In[ ]:


from numpy import *
from matplotlib.pyplot import *
from matplotlib.pyplot import plot as _plot
from matplotlib.pyplot import show as _show

def plot(*args, show=False, **kwargs):
    _plot(*args, **kwargs)
    legend()
    if show:
        _show()

x_vals = [0.2*n for n in range(20)] 
y1 = [sin(.3*x) for x in x_vals] 
y2 = [sin(2*x) for x in x_vals] 
xlabel('x')
ylabel('sin...')

plot(x_vals ,y1, label='sin(0.3*x)') 
plot(x_vals, y2, label='sin(2*x)', show=True)


# In[ ]:




