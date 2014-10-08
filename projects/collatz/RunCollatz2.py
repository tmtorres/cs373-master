#!/usr/bin/env python3

# -------------------------------
# projects/collatz/RunCollatz2.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To run the program
    % coverage3 run --branch RunCollatz1.py < RunCollatz.in

To obtain coverage of the run:
    % coverage3 report -m

To document the program
    % pydoc -w Collatz1
"""

# -------
# imports
# -------

import sys

from Collatz2 import collatz_solve

# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)

"""
% coverage3 run --branch RunCollatz2.py < RunCollatz.in > RunCollatz2.out



% coverage3 report -m
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz2         11      0      4      0   100%
RunCollatz2       5      0      0      0   100%
---------------------------------------------------------
TOTAL            16      0      4      0   100%
"""
