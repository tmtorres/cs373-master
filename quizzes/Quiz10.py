#!/usr/bin/env python3

"""
CS373: Quiz #10 (10 pts) <Raul>
"""

""" ----------------------------------------------------------------------
 1. Define the function my_reduce(), such that it behaves as follows.
    (9 pts)
"""

from functools import reduce
from operator  import sub

def my_reduce (bf, a) :
    p = iter(a)
    v = next(p)
    for w in p :
        v = bf(v, w)
    return v

assert my_reduce(sub, [2, 3, 4]) == -5
assert    reduce(sub, [2, 3, 4]) == -5
