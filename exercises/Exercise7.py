#!/usr/bin/env python3.4

"""
CS373: Exercise #7
"""

""" ----------------------------------------------------------------------
Define the function my_stdev(), such that it behaves as follows:
"""

from functools  import reduce
from math       import sqrt
from statistics import stdev

def stdev_while (a) :
    s = len(a)
    m = sum(a) / s
    i = 0
    v = 0
    while i != s :
        v += (a[i] - m) ** 2
        i += 1
    return sqrt(v / (s - 1))

def stdev_for (a) :
    s = len(a)
    m = sum(a) / s
    v = 0
    for u in a :
        v += (u - m) ** 2
    return sqrt(v / (s - 1))

def stdev_reduce (a) :
    s = len(a)
    m = sum(a) / s
    v = reduce(lambda w, u : w + (u - m) ** 2, a, 0)
    return sqrt(v / (s - 1))

def stdev_map (a) :
    s = len(a)
    m = sum(a) / s
    v = sum(map(lambda v : (v - m) ** 2, a))
    return sqrt(v / (s - 1))

def stdev_list (a) :
    s = len(a)
    m = sum(a) / s
    v = sum([(v - m) ** 2 for v in a])
    return sqrt(v / (s - 1))

def stdev_generator (a) :
    s = len(a)
    m = sum(a) / s
    v = sum(((v - m) ** 2 for v in a))
    return sqrt(v / (s - 1))

def test (f) :
    assert f([2, 3])    == 0.7071067811865476
    assert f([2, 3, 4]) == 1

print("Exercise7.py")

test(stdev_while)
test(stdev_for)
test(stdev_reduce)
test(stdev_map)
test(stdev_list)
test(stdev_generator)
test(stdev)

print("Done.")
