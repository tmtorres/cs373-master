#!/usr/bin/env python3

"""
CS373: Quiz #16 (10 pts) <Raul>
"""

""" ----------------------------------------------------------------------
 1. Define the EntryExit decorator such that the following works.
    (9 pts)
"""

def EntryExit (f) :
    def g (n) :
        print("Entered with", n)
        v = f(n)
        print("Exited with", v)
        return v
    return g

@EntryExit
def incr (n) :
    return n + 1

i = incr(2)
print(i)
print()

i = incr(3)
print(i)
print()

i = incr(4)
print(i)

"""
Entered with 2
Exited with 3
3

Entered with 3
Exited with 4
4

Entered with 4
Exited with 5
5
"""
