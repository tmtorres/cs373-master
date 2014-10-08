#!/usr/bin/env python3

"""
CS373: Exercise #10
"""

""" ----------------------------------------------------------------------
Define the functions cross_join(), theta_join, such that it behaves as
follows:
"""

def cross_join_1 (r, s) :
    x = []
    for v in r :
        for w in s :
            y = {}
            for u in v :
                y[u] = v[u]
            for u in w :
                y[u] = w[u]
            yield y

def cross_join_2 (r, s) :
    return (dict(list(v.items()) + list(w.items())) for v in r for w in s)

def test_cross_join (f, r, s) :
    x = f(r, s)
    assert (
        list(x)
        ==
        [{'A': 4, 'B': 6, 'C': 6},
         {'A': 1, 'B': 6, 'C': 7},
         {'A': 2, 'B': 6, 'C': 8},
         {'A': 2, 'B': 6, 'C': 9},
         {'A': 4, 'B': 7, 'C': 6},
         {'A': 1, 'B': 7, 'C': 7},
         {'A': 2, 'B': 7, 'C': 8},
         {'A': 2, 'B': 7, 'C': 9},
         {'A': 4, 'B': 8, 'C': 6},
         {'A': 1, 'B': 8, 'C': 7},
         {'A': 2, 'B': 8, 'C': 8},
         {'A': 2, 'B': 8, 'C': 9}])

def theta_join_1 (r, s, bp) :
    x = []
    for v in r :
        for w in s :
            if bp(v, w) :
                y = {}
                for u in v :
                    y[u] = v[u]
                for u in w :
                    y[u] = w[u]
                yield y

def theta_join_2 (r, s, bp) :
    return (dict(list(v.items()) + list(w.items())) for v in r for w in s if bp(v, w))

def test_theta_join (f, r, s) :
    x = f(r, s, lambda v, w : v["A"] == w["A"])
    assert (
        list(x)
        ==
        [{'A': 1, 'B': 6, 'C': 7},
         {'A': 2, 'B': 7, 'C': 8},
         {'A': 2, 'B': 7, 'C': 9}])

def match (v, w) :
    for i in v :
        for j in w :
            if (i == j) and (v[i] == w[j]) :
                return True
    return False

def natural_join_1 (r, s) :
    x = []
    for v in r :
        for w in s :
            if match(v, w) :
                y = {}
                for u in v :
                    y[u] = v[u]
                for u in w :
                    y[u] = w[u]
                yield y

def natural_join_2 (r, s) :
    return (dict(list(v.items()) + list(w.items())) for v in r for w in s if match(v, w))

def test_natural_join (f, r, s) :
    x = f(r, s)
    assert (
        list(x)
        ==
        [{'A': 1, 'B': 6, 'C': 7},
         {'A': 2, 'B': 7, 'C': 8},
         {'A': 2, 'B': 7, 'C': 9}])

print("Exercise11.py")

r = [ \
    {"A" : 1, "B" : 6},
    {"A" : 2, "B" : 7},
    {"A" : 3, "B" : 8}]
assert len(r) == 3

s = [ \
    {"A" : 4, "C" : 6},
    {"A" : 1, "C" : 7},
    {"A" : 2, "C" : 8},
    {"A" : 2, "C" : 9}]
assert len(s) == 4

test_cross_join(cross_join_1, r, s)
test_cross_join(cross_join_2, r, s)

test_theta_join(theta_join_1, r, s)
test_theta_join(theta_join_1, r, s)

test_natural_join(natural_join_1, r, s)
test_natural_join(natural_join_2, r, s)

print("Done.")
