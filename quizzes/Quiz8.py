#!/usr/bin/env python3

"""
CS373: Quiz #8 (10 pts) <Raul>
"""

""" ----------------------------------------------------------------------
 1. In the paper, "A Bug and a Crash" about the Ariane 5, what was the
    software bug?
    (3 pts)

the conversion of a 64-bit number to a 16-bit number
"""

""" ----------------------------------------------------------------------
 2. In the paper, "Mariner 1", what was the software bug?
    (3 pts)

the ommission of a hyphen
"""

""" ----------------------------------------------------------------------
 3. What is the output of the following?
    (3 pts)

1
"""

from functools import reduce

print(reduce(lambda x, y : (2 * y) - x, [2, 3, 4], 5))
