#!/usr/bin/env python

"""
CS373: Exercise #5
"""

""" ----------------------------------------------------------------------
Define the function my_reduce(), such that it behaves as follows:
"""

# https://docs.python.org/3.4/library/functools.html

from functools import reduce
from operator  import sub

def my_reduce (bf, a, v = None) :
    if (not a) and (v is None) :
        raise TypeError("reduce() of empty sequence with no initial value")
    p = iter(a)
    if v is None :
        v = next(p)
    for w in p :
        v = bf(v, w)
    return v

print "Exercise5.py"

assert my_reduce(sub, [],        5) ==  5
assert    reduce(sub, [2, 3, 4], 5) == -4

assert my_reduce(sub, [2, 3, 4])    == -5
assert    reduce(sub, [2, 3, 4])    == -5

print "Done."
