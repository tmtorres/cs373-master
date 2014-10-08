#!/usr/bin/env python3

"""
CS373: Exercise #6
"""

""" ----------------------------------------------------------------------
Define the function my_zip(), such that it behaves as follows:
"""

# https://docs.python.org/3.4/library/functions.html#zip

def my_zip (*a) :
    if not a :
        return []
    return list(map(lambda *x : x, *a))

print("Exercise6.py")

assert my_zip()                       == []
assert my_zip([])                     == []
assert my_zip((), ())                 == []
assert my_zip([2, 3])                 == [(2,), (3,)]
assert my_zip((2, 3), (4, 5), (6, 7)) == [(2, 4, 6), (3, 5, 7)]
assert my_zip([2, 3, 4], [5, 6, 7])   == [(2, 5), (3, 6), (4, 7)]

assert list(zip())                       == []
assert list(zip([]))                     == []
assert list(zip((), ()))                 == []
assert list(zip([2, 3]))                 == [(2,), (3,)]
assert list(zip((2, 3), (4, 5), (6, 7))) == [(2, 4, 6), (3, 5, 7)]
assert list(zip([2, 3, 4], [5, 6, 7]))   == [(2, 5), (3, 6), (4, 7)]

print("Done.")
