#!/usr/bin/env python3

"""
CS373: Quiz #9 (10 pts) <Raul>
"""

from math import sqrt

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (9 pts)

0 1 2 3
0 1 2 3 4 else

[2, 3, 4]
[2, 3, 4]

[2.0, 3.0, 4.0]
[2.0, 3.0, 4.0]

[2.0, 3.0, 4.0]
[]
"""

def test (w) :
    for v in range(5) :
        print(v, end = " ")
        if v == w :
            print()
            break
    else :
        print("else")

test(3)                  # 3 pts
test(7)
print()

x = range(2, 5)          # 2 pts
print(list(x))
print(list(x))
print()

a = [4, 9, 16]           # 2 pts
x = [sqrt(v) for v in a]
print(list(x))
print(list(x))
print()

x = map(sqrt, a)         # 2 pts
print(list(x))
print(list(x))
