#!/usr/bin/env python3

"""
CS373: Exercise #9
"""

""" ----------------------------------------------------------------------
Define the function select(), such that it behaves as follows:
"""

def select_1 (r, up) :
    for d in r :
        if up(d) :
            yield d

def select_2 (r, up) :
    return (d for d in r if up(d))

def select_3 (r, up) :
    return filter(up, r)

def test (f) :
    r = [ \
        {"A" : 1, "B" : 6},
        {"A" : 2, "B" : 7},
        {"A" : 3, "B" : 8}]
    assert len(r) == 3

    x = f(r, lambda d : d["B"] > 6)
    assert (list(x) ==
        [{'A': 2, 'B': 7},
         {'A': 3, 'B': 8}])

    r = [ \
        {"A" : 4, "C" : 6},
        {"A" : 1, "C" : 7},
        {"A" : 2, "C" : 8},
        {"A" : 2, "C" : 9}]
    assert len(r) == 4

    x = f(r, lambda d : d["C"] > 8)
    assert (list(x) ==
        [{'A': 2, 'C': 9}])

print("Exercise9.py")

test(select_1)
test(select_2)
test(select_3)

print("Done.")
