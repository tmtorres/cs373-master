#!/usr/bin/env python3

"""
CS373: Exercise #10
"""

""" ----------------------------------------------------------------------
Define the function project(), such that it behaves as follows:
"""

def project_1 (r, *a) :
    for v in r :
        y = {}
        for w in a :
            if w in v :
                y[w] = v[w]
        yield y

def project_2 (r, *a) :
    return ({w : v[w] for w in a if w in v} for v in r)

def test (f) :
    r = [ \
        {"A" : 1, "B" : 6},
        {"A" : 2, "B" : 7},
        {"A" : 3, "B" : 8}]
    assert len(r) == 3

    x = f(r, "B")
    assert (list(x) ==
        [{'B': 6},
         {'B': 7},
         {'B': 8}])

    r = [ \
        {"A" : 4, "C" : 6},
        {"A" : 1, "C" : 7},
        {"A" : 2, "C" : 8},
        {"A" : 2, "C" : 9}]
    assert len(r) == 4

    x = f(r, "C", "A")
    assert (list(x) ==
        [{'C': 6, 'A': 4},
         {'C': 7, 'A': 1},
         {'C': 8, 'A': 2},
         {'C': 9, 'A': 2}])

print("Exercise10.py")

test(project_1)
test(project_2)

print("Done.")
