#!/usr/bin/env python3

"""
CS373: Quiz #12 (10 pts) <Raul>
"""

""" ----------------------------------------------------------------------
 1. What is a primary key?
    [Basic UML & SQL: Rows & Tables]
    (3 pts)

a minimal unique identifier for each row
"""

""" ----------------------------------------------------------------------
 2. What is the multiplicity of an association?
    [Basic UML & SQL: Associations]
    (3 pts)

how many instances of a class are connected to an instance of another
class
"""

""" ----------------------------------------------------------------------
 3. What is the output of the following?
    (3 pts)

[6, 9, 8, {'b': 7}]
"""

def f (x = 2, y = 3, z = 4, **t) :
    return [x, y, z, t]

a = [6]
d = {"b" : 7 , "z" : 8}

print(f(y = 9, *a, **d))
