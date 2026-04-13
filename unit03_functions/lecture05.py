#!/usr/bin/env python
# coding: utf-8

# # Computational Programming with Python
# ### Lecture 5: Functions and Lists Revisited
# 
# ### Center for Mathematical Sciences, Lund University
# Lecturer: `Robert Klöfkorn`
# 

# ## This lecture
# 
# - Revision: recurrence relations
# - Revision: list comprehension
# - Functions returning functions (partial application)
# - Unpacking arguments, the star operator
# - Star operators in function definitions
# - Using an optional number of arguments
# - Numerical integration
# - The bisection method, recursive functions

# ## Revison: recurrence relations and fixed point iteration
# 
# A recursive equation 
# 
# \begin{cases}
# x_0 = c \\
# x_{n+1} = f(x_n), n \ge 0
# \end{cases}
# 
# and the corresponding fixed point iteration

# A number $x_0$ such that $f(x_0)=x_0$ is called a *fixed point*. 
# 
# The sequence will converge to that fixed point if $f$ is a contraction ($|f(x) - f(y)| < \alpha |x - y| \ \forall x,y$ and $\alpha \in [0,1)$) and a self map (e.g. $f: \mathbb{R} \to D \subset \mathbb{R}$) onto a closed set (see [Banach's fixed point theorem](https://en.wikipedia.org/wiki/Banach_fixed-point_theorem)). 
# 
# An example is visualised using a **cob web diagram**, see [www.geogebra.org/m/za7tarfg](https://www.geogebra.org/m/za7tarfg).
# Here you see that a fixed point can be **repelling** or **attracting**. If the initial value $c$ is \"close to\" an attracting fixed point ($f$ is a contraction), the sequence will converge to that fixed point.

# ## Revison: recurrence relations and fixed point iteration
# 
# A recursive equation, same thing, different notation: 
# 
# \begin{cases}
# x^{(0)} = c \\
# x^{(n+1)} = f(x^{(n)}), n \ge 0
# \end{cases}
# 
# and the corresponding fixed point iteration

# In[ ]:


from numpy import sin, linspace
from matplotlib.pyplot import *
def f(x, a=0.5):
     return sin(x) - a*x + 30.

x = 0.5              # some initial value for x
for i in range(100): # for some n = 100
    x = f(x)         # where f is the function from exercise 02

print(x)    

xv = linspace(0.,30., 300)
plot(xv, f(xv))
plot(x,x,'o')


# ## Revision: list comprehension
# 
# The syntax of  a list comprehension is:
# 
# `[<expr> for <variable> in <list>]`
# 
# You can use a conditional in a list comprehension:
# 
# `[<expr> for <variable> in <list> if <condition>]`
# 
# You will be given some easy examples during the break

# ## List comprehension and nested lists
# 
# **Example**
# 
# Produce following matrix as nested lists
# 
# $$
# \begin{bmatrix}
# 1 & 2 & 3 \\
# 10 & 20 & 30 \\
# 100 & 200 & 300
# \end{bmatrix}
# $$

# In[ ]:


m1 = [ [1, 2, 3],
       [10, 20, 30],
       [100, 200, 300]]
print(m1)


# We can make each row using list comprehension

# In[ ]:


n = 3
m2 = [ [i for i in range(1, n+1)],
       [10*i for i in range(1, n+1)],
       [100*i for i in range(1, n+1)]]
print(m2)


# or changing the arguments of the range-function

# In[ ]:


m3 = [ [i for i in range(1, n+1)],
       [i for i in range(10, n*10 + 1, 10)],
       [i for i in range(100, n*100 + 1, 100)]]
print(m3)


# ### Using nested list comprehension

# In[ ]:


n = 4
m4 = [ [10**exponent*i for i in range(1, n+1)] for exponent in range(n)]
print(m4)


# or

# In[ ]:


m5 = [ [i for i in range(10**k, n*10**k+1, 10**k)] for k in range(n)]
print(m5)


# ### Using a for loop and list comprehension

# In[ ]:


m6 = []

for row in range(n):
    m6.append([10**row*i for i in range(1, n+1)])
print(m6)


# ### Using a nested for loop

# In[ ]:


m7 = []
k = 3 
i = 4

for row in range(n):
    m7.append([])
    #m7.append(k)
    #m7.append(i)
    for i in range(1, n+1):
        m7[row].append(10**row*i)
print(m7)


# ### Making slices of a nested list
# 
# Given `m1 = [ [1, 2, 3], [10, 20, 30], [100, 200, 300]]`, <br>
# produce
# 
# $$
# \begin{bmatrix}
# 1  \\
# 10 & 20  \\
# 100 & 200 & 300
# \end{bmatrix}
# $$
# 
# This could be done like that:

# In[ ]:


s1 = [ m1[0][: 1],
       m1[1][: 2],
       m1[2][:]]
print(s1)


# Program the above using a `for` loop and `append`. After that use `list comprehension` to create the same solution. **(5min, let's go)**

# In[ ]:





# In[ ]:


s2 = []
n = 3
for i in range(1,n+1): 
    s2.append([j*10**(i-1) for j in range(1,i+1)] )
print(s2)  

s3 = []
n = len(m1)
for i in range(n): 
    s3.append(m1[i][0:i+1]) 
print(s3) 

s4 = [m1[n][:n+1] for n in range(len(m1)) ]
print(s4)


# ### An optional number of arguments
# 
# In order to handle
# 
# $$g(x) = A\sin(\omega x)$$
# 
# we need to handle a variable number of arguments.

# In[ ]:


from numpy import sin
A = 2.5 
omega = 0.4 
g = lambda x: A*sin(omega * x)

print(g(0.25))


# In[ ]:


from numpy import sin
def g(x, A=0.25, omega=0.4): # A and omega are optional
    return A*sin(omega * x)

print(g(0.25))


# ### An optional number of arguments
# 
# Another example:
# 
# $$h(x) = ax^4 +bx^3 +cx^2+dx +e$$
# 
# we need to handle a variable and/or optional  number of arguments.

# In[ ]:


def makePolynomial(a, b, c, d, e): # a,b,c,d,e are mandatory (non-optional)
    return lambda x: a*x**4 + b*x**3 + c*x**2 + d*x + e

coefficients = [1., 3., 4. , 0.5, 2.]
# use unpacking to cast the list into a,b,c,d,e
h = makePolynomial(*coefficients)
print(h)

print(h(0.5))


# ### An optional number of arguments
# 
# Another example:
# 
# $$h(x) = ax^4 +bx^3 +cx^2+dx +e$$
# 
# we need to handle a variable and/or optional number of arguments.

# In[ ]:


def makePolynomial(a, b, c, d, e): # a,b,c,d,e are mandatory (non-optional)
    return lambda x: a*x**4 + b*x**3 + c*x**2 + d*x + e

coefficients = { "a": 1., "d": 0.5, "b": 3., "c": 4. , "e": 2.}
# use double star unpacking to cast the dict into a,b,c,d,e
h = makePolynomial(**coefficients)
print(h)

print(h(0.5))


# # Parameters and arguments
# 
# ## Unpacking arguments
# 
# Positional arguments remind us of `list` (lists). Keyword arguments remind us of `dict` (dictionaries).

# In[ ]:


from numpy import*
from matplotlib.pyplot import *
get_ipython().run_line_magic('matplotlib', 'inline')
figure(figsize = (4, 4))  # make it square-shaped

data = [[1, 4], [1, 4]]
my_style = {'linewidth': 3, 'marker': 'o', 'color': 'green'}

plot(*data, **my_style) # Star operators unpack these to form a valid parameter list.


# ## Star operator to unpack containers
# 
# Unpacking lists

# In[ ]:


a, b = [0, 1]   
print("a =", a)

*c, d = [0, 1, 2, 3, 4]
print("c =", c, "d =", d)

c, *d = [0, 1, 2, 3, 4]
print("c =", c, "d =", d)

c, *d, e = [0, 1, 2, 3, 4]
print("c =", c, "d =", d, "e =", e)


# Unpacking dictionaries

# In[ ]:


*a, b = {"nr1": 10, "nr2": 36, "nr3": 57}  # we get the key words
print("a =", a, "b =", b)

*a, b = {"nr1": 10, "nr2": 36, "nr3": 57}.items() # we get key-word-value pairs
print("a =", a, "b =", b)

*a, b = {"nr1": 10, "nr2": 36, "nr3": 57}.values() # we get the values
print("a =", a, "b =", b)


# ## Star operators in function definitions
# 
# A function can take an optional number of **positional** arguments by using a **single star**.

# In[ ]:


def add(*args):
    print(type(args))
    return sum(args)

s = add(1, 2, 3, 4, 5)
print("s =", s)

s2 = add (2,3,4)
print("s =", s2)


# ## Star operator in function definitions (cont)
# 
# A function can take an optional number of **keyword arguments** by using a **double star**.

# In[ ]:


def myfunc(*args, **kwargs):
    print(type(kwargs))
    for key, val in kwargs.items():
        print(f"the key {key} has the value {val}")

myfunc(name = "Joe", age = 20)


# You can use any names you want. The names `args` and `kwargs` are often used.

# ## Passing (tunneling) arguments
# Also in the definition of functions you might find these constructs. This is often used to pass arguments through a function.

# In[ ]:


def outer(f, x, *args, **kwargs): 
    return f(x, *args, **kwargs)

def inner(x, y, z, u): 
    print(f"y = {y} z = {z}, u = {u}")
    return x**2

outer(inner, 3, 1, 2, u=15)


# Note, the function `outer` cannot know how many arguments it needs to provide a full parameter list to the `inner` function f.

# ## Using an optional number of arguments
# 
# Instead of using
# 
# ```python
# def makeOneParameterFunc(f, a, b, c, d):
# ```
# 
# we could use
# 
# ```python
# def makeOneParameterFunc(f, *args, **kwargs):
# ```
# 
# Inside the definition of the function, `args` is a **tuple** and `kwargs` is a **dictionary**.
# 

# ### A new partial application

# In[ ]:


def g(x, A=2, omega=3): 
    return A*sin(omega*x)

# numerical differentiation
def derivative1(f, x, h = 1e-6): 
    return (f(x+h)-f(x))/h

def makeOneParameterFunc(f, *args, **kwargs):
    def newf(x):
        return f(x, *args, **kwargs) # args and kwargs are unpacked
    return newf

newg = makeOneParameterFunc(g, A=1.5, omega=4)
dgdx = derivative1(newg, 0)

print("d/dx(2 sin(3x)) when x = 0 is", dgdx)


# In[ ]:


def dgdx_exact(x, A, omega):
    return A*omega*cos(omega*x)

print("We expect d/dx(2 sin(3x)) to be", dgdx_exact(0, 2, 3))


# ### Summary
# 
# Partial applications (or closures) are used to make a new funcion with a reduced number of parameters.
# 
# Using closures we avoid having to use global variables.
# 
# 
# ```python
# def make_function(...):
#     # possible code
#     def some_function(...):  # fewer parameters
#         # code accessing variables from the enclosing scope
#     return some_function
# ```

# ## Numerical integration
# 
# The module `scipy.integrate` has a function `quad` that can be used to integrate a function over an interval.
# 
# Use `quad(f, a, b)` to find
# 
# $$\int_a^b f(x) dx.$$
# 
# `quad` returns the result of the integral and the estimated error (in a tuple).

# In[ ]:


from scipy.integrate import quad
from numpy import sin,pi
integral = quad(sin, 0, pi)
print(integral)


# ### Plots with filled area between curves
# 
# The `matplotlib.pyplot` method `filled_between` shows a filled area between two curves.
# 
# If only one $y$-argument is used, the area is filled between the $y$-values and the $x$-axis.

# In[ ]:


from numpy import *
from matplotlib.pyplot import *
x = linspace(-2*pi, 2*pi, 100)
y = sin(x)

plot(x, y) 
xlabel('x')
ylabel('sin(x)')
fill_between(x, y, alpha=0.1)  # use semi transparent color for area
grid()                          # show a grid for better readability


# ### Fill area between two $x$-values
# 
# To show filled area where $ -\pi \lt x \lt \pi/2$, use two $x$-arrays.

# In[ ]:


x = linspace(-2*pi, 2*pi, 100)  # for the graph
x1 = linspace(-pi, pi/2, 50)    # for the filled area

plot(x, sin(x))                       
xlabel('x')
ylabel('sin(x)')
fill_between(x1, sin(x1), alpha = 0.2) 
grid() 


# ### Fill area between two graphs

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = linspace(-2*pi, 2*pi, 100)
y1 = sin(x)
y2 = cos(x)

plot(x, y1, color='red',  label='sin(x)')
plot(x, y2, color='blue', label='cos(x)')
xlabel('x')
legend()   #  show function names within plot
fill_between(x, y1, y2, color='green', alpha=0.1)


# ### Fill area between two graphs using `where`

# In[ ]:


x = linspace(-2*pi, 2*pi, 100)
print(type(x))
y1 = sin(x)
y2 = cos(x)

plot(x, y1, color='red', label='sin(x)')
plot(x, y2, color='blue', label='cos(x)')
xlabel('x')
legend()
fill_between(x, y1, y2, where=y1>y2, color='green', alpha=0.2)


# `where` results in a **Boolean array**, which we will talk about in lectures to come.

# ## More about the bisection method
# 
# One approach using a list as parameter and changing the content of that list:

# In[ ]:


def bisec1(f, interval, tol):
    for i in range(100):
        if interval[1]-interval[0] < tol:
            break
        mid = (interval[0]+interval[1])/2
        if f(interval[0])*f(mid) < 0:
            interval[1] = mid
        else:
            interval[0] = mid
    return interval, mid


# ### Testing `bisec1` 

# In[ ]:


def f(x): return 3*x**2-5

def make_plot(f, interval, m):
    x = linspace(interval[0], interval[1], 50)
    plot(x, f(x))
    plot(m, f(m), 'o')
    grid()  

interval = [-3, 0.5]

i, m = bisec1(f, interval, 1e-9)  
print("mid = ", m)
make_plot(f, interval, m)  # the plot must be made before bisec1 is called


# Why does the above code not work? **(5min, let's go!)**

# ### An approach not changing the content of `interval`

# In[ ]:


def bisec2(f, interval, tol):
    a = interval[0]          # all changes are made on a and b
    b = interval[1]
    for i in range(100):
        if b-a < tol:
            break
        mid = (a+b)/2
        if f(a)*f(mid) < 0:
            b = mid
        else:
            a = mid
    return [a, b], mid


# ### Testing `bisec2` 

# In[ ]:


def f(x): return 3*x**2-5

def make_plot(f, interval, root):
    x = linspace(interval[0], interval[1], 50)
    plot(x, f(x))
    xlabel('x')
    ylabel('f(x)')
    plot(root,0.,'o') # plot root of function as point
    grid()   

interval = [-3, 0.5]
i, m = bisec2(f, interval, 1e-9)  
print("mid = ", m)
make_plot(f, interval, m)        # works since interval is intact since creation


# ### An approach using the end points of `interval` 

# In[ ]:


def bisec3(f, a, b, tol):  # a and b are endpoints of the interval
    for i in range(100):
        if b-a < tol:
            break
        mid = (a+b)/2
        if f(a)*f(mid) < 0:
            b = mid
        else:
            a = mid
    return [a, b], mid


# ### Testing `bisec3` 

# In[ ]:


def f(x): return 3*x**2-5

def make_plot(f, interval, root):
    x = linspace(interval[0], interval[1], 50)
    plot(x, f(x))
    xlabel('x')
    ylabel('f(x)')
    plot(root,0.,'o', label=f'f({root}) = 0') # plot root of function as point
    legend()
    grid()   

interval = [-3, 0.5]
i, m = bisec3(f, *interval, 1e-9)  # pass the end points as arguments
print("mid = ", m)
make_plot(f, interval, m) 


# ### An approach using `return` to break

# In[ ]:


def bisec4(f, a, b, tol):  # a and b are endpoints of the interval
    for i in range(100):
        if b-a < tol:
             return [a, b], mid
        mid = (a+b)/2
        if f(a)*f(mid) < 0:
            b = mid
        else:
            a = mid

i, m = bisec4(f, -3, 0.5, 1e-9)
print(m)


# ## A recursive function

# In[ ]:


def bisec5(f, a, b, tol):
    mid = (a+b)/2
    if b-a <= tol:
        return [a, b], mid
    if f(a)*f(mid) < 0:
        return bisec5(f, a, mid, tol)
    else:
        return bisec5(f, mid, b, tol)

i, m = bisec5(f, -3, 0.5, 1e-9)
print(m)


# In general: **avoid recursive functions in Python** because it's slow and the recursion depth is limited (can be changed).

# In[ ]:


i = 0
def f(x):
    global i
    i += 1
    print(i)
    return f(x)


print(f(1))   

