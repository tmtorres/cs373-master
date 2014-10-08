#!/usr/bin/env python3

"""
CS373: Exercise #3
"""

""" ----------------------------------------------------------------------
Define the function my_zip(), such that it behaves as follows:
"""

# https://docs.python.org/3.4/library/functions.html#zip

def my_zip (a, b) :
    return list(map(lambda x, y : (x, y), a, b))

print("Exercise3.py")

assert   my_zip([2, 3, 4], [5, 6, 7])  == [(2, 5), (3, 6), (4, 7)]
assert list(zip([2, 3, 4], [5, 6, 7])) == [(2, 5), (3, 6), (4, 7)]

print("Done.")
