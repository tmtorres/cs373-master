#!/usr/bin/env python3

# ----------------------------
# projects/collatz/Collatz2.py
# Copyright (C) 2014
# Glenn P. Downing
# ----------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r is a reader
    return a generator of a list of the two ints, otherwise an empty generator
    """
    return ([int(v) for v in s.split()] for s in r)

# ------------
# collatz_eval
# ------------

def collatz_eval (a) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return a generator of a list of i, j, and the max cycle length
    """
    # <your code>
    return ([i, j, 1] for i, j in a)

# -------------
# collatz_print
# -------------

def collatz_print (a) :
    """
    w is a writer
    v is the max cycle length
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return a generator of a string of i, j, and the max cycle length
    """
    return (str(i) + " " + str(j) + " " + str(v) + "\n" for i, j, v in a)

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    for s in collatz_print(collatz_eval(collatz_read(r))) :
        w.write(s)
