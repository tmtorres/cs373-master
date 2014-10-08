#!/usr/bin/env python3

"""
CS373: Exercise #2
"""

""" ----------------------------------------------------------------------
Define the function my_map(), such that it behaves as follows:
"""

# https://docs.python.org/3.4/library/functions.html#map

from math import sqrt

def my_map (uf, a) :
    return [uf(v) for v in a]

print("Exercise2.py")

assert   my_map(sqrt, [4, 9, 16])  == [2, 3, 4]
assert list(map(sqrt, [4, 9, 16])) == [2, 3, 4]

print("Done.")
