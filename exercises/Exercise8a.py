#!/usr/bin/env python3

"""
CS373: Exercise #8a
"""

""" ----------------------------------------------------------------------
Define the function my_list(), such that it behaves as follows:
"""

# https://docs.python.org/3.4/tutorial/datastructures.html

class my_list :
    class iterator :
        def __init__ (self, x) :
            self.x = x
            self.i = 0

        def __iter__ (self) :
            return self

        def __next__ (self) :
            if self.i == len(self.x.a) :
                raise StopIteration
            v = self.x.a[self.i]
            self.i += 1
            return v

    def __init__ (self) :
        self.a = []

    def __iter__ (self) :
        return my_list.iterator(self)

    def append (self, v) :
        self.a.append(v)

def test (c) :
    x = c()
    x.append(2)
    x.append(3)
    x.append(4)
    assert not hasattr(x, "__next__")
    assert     hasattr(x, "__iter__")

    p = iter(x)
    assert hasattr(p, "__next__")
    assert hasattr(p, "__iter__")
    assert iter(p) is p

    assert next(p) == 2
    assert next(p) == 3
    assert next(p) == 4

    try :
        assert next(p) == 5
    except StopIteration :
        pass

print("Exercise8a.py")

test(my_list)
test(   list)

print("Done.")
