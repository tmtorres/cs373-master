#!/usr/bin/env python3

"""
CS373: Quiz #13 (10 pts) <Mukund>
"""

""" ----------------------------------------------------------------------
 1. Fill in the TWO blanks below.
    [The Open-Closed Principle]
    (2 pts)

    Software entities (classes, modules, functions, etc.) should be open
    for <BLANK>, but closed for <BLANK>.

extension
modification
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (7 pts)

[2, 3, 4]
[2, 3, 4, 5]
[2, 3, 4, 5]
"""

def f (a) :
    def g () :
        return a
    def h (v) :
        a.append(v)
        return a
    return (g, h)

x = f([2, 3, 4])
print(x[0]())
print(x[1](5))
print(x[0]())
