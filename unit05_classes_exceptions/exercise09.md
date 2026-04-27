# Training Assignment 09 – Inheritance (PolyGon, Rectangle)

**Kurs:** NUMA01: Computational Programming with Python
**Lärare:** Malin Christersson, Robert Klöfkorn

---

In this exercise we study inheritance of classes.

This assignment has 4 tasks.

---

## Tasks

### Task 1

Define an abstract class `PolyGon`. It should have a method `plot` which plots the polygon by drawing its edges. It should also have an `__init__` method, which takes a list of corner points as input. Corner points are described by arrays with shape `(2,)` describing the coordinates of the corners. The `__init__` method assigns this corner list as an attribute and also computes the edges. (See also the corresponding method in the triangle example, course book p. 121 and p. 126.)

### Task 2

Define a class `Rectangle` which inherits as much as possible from the parent class `PolyGon`. Provide it also with a method to compute the area.

### Task 3

Define a third class `SpecialRectangle` which describes Rectangles which have all its edges parallel to the coordinate axes. It should be constructed by inheritance from the class `Rectangle`.

### Task 4

Give this class a method `__contains__` such that for two given `SpecialRectangle`s A and B the statement `A in B` evaluates to `True` if A is contained in B and `False` otherwise.
