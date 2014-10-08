#!/usr/bin/env python3

"""
CS373: Quiz #15 (10 pts) <Mukund>
"""

""" ----------------------------------------------------------------------
 1. What kind of table is needed to represent a many-to-many association?
    [UML Design: Many-to-many]
    (1 pt)

join or junction table
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (8 pts)

[2, 3, 4]
[2, 3, 4]
[2, 3, 4, 5]
[2, 3, 4, 5]
[2, 3, 4, 5]
(6, 7, 8)
[2, 3, 4, 5]
(6, 7, 8, 9)
"""

class A :
    v = [2, 3, 4]

x = A()
print(A.v)
print(x.v)
x.v += [5]
print(A.v)
print(x.v)
x.v = (6, 7, 8)
print(A.v)
print(x.v)
x.v += (9,)
print(A.v)
print(x.v)
