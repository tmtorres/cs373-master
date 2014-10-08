#!/usr/bin/env python3

# -------------------------------
# projects/collatz/RunCollatz3.py
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

from Collatz3 import collatz_solve

# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)

"""
% coverage3 run --branch RunCollatz3.py < RunCollatz.in > RunCollatz3.out



% coverage3 report -m
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz3          9      0      8      0   100%
RunCollatz3       5      0      0      0   100%
---------------------------------------------------------
TOTAL            14      0      8      0   100%
"""
