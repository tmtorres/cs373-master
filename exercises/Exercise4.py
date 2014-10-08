#!/usr/bin/env python

"""
CS373: Exercise #4
"""

""" ----------------------------------------------------------------------
Define the function my_reduce_1() and my_reduce_2(), such that it behaves
as follows:
"""

# https://docs.python.org/3.4/library/functools.html

from functools import reduce
from operator  import sub

def my_reduce_1 (bf, a, v) :
    for w in a :
        v = bf(v, w)
    return v

def my_reduce_2 (bf, a) :
    p = iter(a)
    v = next(p)
    for w in p :
        v = bf(v, w)
    return v

print "Exercise4.py"

assert my_reduce_1(sub, [],        5) ==  5
assert    reduce  (sub, [2, 3, 4], 5) == -4

assert my_reduce_2(sub, [2, 3, 4])    == -5
assert    reduce  (sub, [2, 3, 4])    == -5

print "Done."
