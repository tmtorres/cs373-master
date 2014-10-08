#!/usr/bin/env python3

"""
CS373: Exercise #1
"""

""" ----------------------------------------------------------------------
Define the function rmse(), such that it behaves as follows:
"""

from functools import reduce
from math      import sqrt
from sys       import version
from time      import clock

def sqre_diff (x, y) :
    return (x - y) ** 2

def rmse_while (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__getitem__"))
    assert(hasattr(p, "__getitem__"))
    assert(len(a) == len(p))
    s = len(a)
    i = 0
    v = 0
    while i != s :
        v += sqre_diff(a[i], p[i])
        i += 1
    return sqrt(v / s)

def rmse_range_for (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__getitem__"))
    assert(hasattr(p, "__getitem__"))
    assert(len(a) == len(p))
    s = len(a)
    v = 0
    for i in range(s) :
        v += sqre_diff(a[i], p[i])
    return sqrt(v / s)

def rmse_zip_for (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__iter__"))
    assert(hasattr(p, "__iter__"))
    assert(len(a) == len(p))
    s = len(a)
    z = zip(a, p)
    v = 0
    for x, y in z :
        v += sqre_diff(x, y)
    return sqrt(v / s)

def rmse_zip_reduce (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__iter__"))
    assert(hasattr(p, "__iter__"))
    assert(len(a) == len(p))
    s = len(a)
    z = zip(a, p)
    v = reduce(lambda v, a : v + sqre_diff(a[0], a[1]), z, 0)
    return sqrt(v / s)

def rmse_map_sum (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__iter__"))
    assert(hasattr(p, "__iter__"))
    assert(len(a) == len(p))
    s = len(a)
    v = sum(map(sqre_diff, a, p))
    return sqrt(v / s)

def rmse_zip_list_sum (a, p) :
    """
    O(n) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__iter__"))
    assert(hasattr(p, "__iter__"))
    assert(len(a) == len(p))
    s = len(a)
    z = zip(a, p)
    v = sum([sqre_diff(x, y) for x, y in z])
    return sqrt(v / s)

def rmse_zip_generator_sum (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__iter__"))
    assert(hasattr(p, "__iter__"))
    assert(len(a) == len(p))
    s = len(a)
    z = zip(a, p)
    v = sum((sqre_diff(x, y) for x, y in z))
    return sqrt(v / s)

def test (f) :
    print(f.__name__)
    assert f((2, 3, 4), (2, 3, 4)) == 0
    assert f((2, 3, 4), (3, 2, 5)) == 1
    assert f((2, 3, 4), (4, 1, 6)) == 2
    assert f((2, 3, 4), (4, 3, 2)) == 1.632993161855452
    a = 1000000 * [1]
    p = 1000000 * [5]
    b = clock()
    assert f(a, p) == 4
    e = clock()
    print("%5.3f" % ((e - b) * 1000), "milliseconds")
    print()

print("Exercise1.py")
print(version)
print()

test(rmse_while)
test(rmse_range_for)
test(rmse_zip_for)
test(rmse_zip_reduce)
test(rmse_map_sum)
test(rmse_zip_list_sum)
test(rmse_zip_generator_sum)

print("Done.")

"""
Exercise1.py
3.2.3 (default, Feb 27 2014, 21:31:18)
[GCC 4.6.3]

rmse_while
700.000 milliseconds

rmse_range_for
630.000 milliseconds

rmse_zip_for
580.000 milliseconds

rmse_zip_reduce
740.000 milliseconds

rmse_map_sum
540.000 milliseconds

rmse_zip_list_sum
590.000 milliseconds

rmse_zip_generator_sum
590.000 milliseconds

Done.
"""
