#!/usr/bin/env python3

# ------------
# Iterables.py
# ------------

from itertools import count

def test_1 (x) :
    assert not hasattr(x, "__next__")
    assert     hasattr(x, "__iter__")
    i = iter(x)                       # i = x.__iter__()

    assert hasattr(i, "__next__")
    assert hasattr(i, "__iter__")
    assert i is iter(i)

    assert next(i) == 2
    assert next(i) == 3
    assert next(i) == 4

    try :
        assert next(i) == 5
        assert False
    except StopIteration :
        pass

def test_2 (i) :
    assert hasattr(i, "__next__")
    assert hasattr(i, "__iter__")
    assert i is iter(i)

    assert next(i) == 2
    assert next(i) == 3
    assert next(i) == 4

print("Iterables.py")

test_1([2, 3, 4])                         # list
test_1((2, 3, 4))                         # tuple
test_1({2, 3, 4})                         # set
test_1({2 : "abc", 3 : "def", 4 : "ghi"}) # dict
test_1([v for v in [2, 3, 4]])            # list comprehension
test_1(range(2, 5))

test_2(iter([2, 3, 4]))                         # list
test_2(iter((2, 3, 4)))                         # tuple
test_2(iter({2, 3, 4}))                         # set
test_2(iter({2 : "abc", 3 : "def", 4 : "ghi"})) # dict
test_2(iter([v for v in [2, 3, 4]]))            # list comprehension
test_2(iter(range(2, 5)))

test_2(((v for v in [2, 3, 4])))                # generator
test_2(count(2))
test_2(   map(lambda v : v,    [2, 3, 4]))
test_2(filter(lambda v : True, [2, 3, 4]))

print("Done.")
