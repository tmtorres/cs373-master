#!/usr/bin/env python3

"""
CS373: Quiz #7 (10 pts) <Mukund>
"""

from functools import reduce
from operator  import add, sub

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (9 pts)

3 pts: [5, 7, 9]
3 pts: -4
3 pts: [(2, 3), (3, 4), (4, 5)]
"""

print(list(map(add, [2, 3, 4], [3, 4, 5])))

print(reduce(sub, [2, 3, 4], 5))

print(list(zip([2, 3, 4], [3, 4, 5])))
