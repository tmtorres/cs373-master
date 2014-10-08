#!/usr/bin/env python3

"""
CS373: Quiz #2 (10 pts) <Raul>
"""

""" ----------------------------------------------------------------------
 1. List any TWO pieces of advice from "Advice for Computer Science
 	College Students".
    (2 pts)

write
learn C
learn microeconomics
excel in non-CS classes
take programming-intensive classes
stop worrying about jobs going to India
get a good summer internship
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
 	In the context of Project #1: Collatz, what is f() computing?
    (4 pts)

5
11
For odd n it's computing (3n + 1) / 2.
(3n + 1) / 2
3n/2 + 1/2
n + n/2 + 1/2
n + n/2 + 1, because n is odd
n + (n >> 1) + 1
"""

def f (n) :
    return n + (n >> 1) + 1

print(f(3))
print(f(7))

""" ----------------------------------------------------------------------
 3. Given positive integers, b and e, let m = e / 2. If b < m, then
    max_cycle_length(b, e) = max_cycle_length(m, e). True or False?
    [Collatz]
    (2 pts)

True

Consider b = 10, e = 100.
Then m = 100 / 2 = 50.
max_cycle_length(10, 100) = max_cycle_length(50, 100)
All the numbers in the range [10, 49] can be mapped to numbers in the
range [50, 100] by one or more doublings, so none of the numbers in the
range [10, 49] could have a larger cycle length than the numbers in the
range [50, 100].
"""
