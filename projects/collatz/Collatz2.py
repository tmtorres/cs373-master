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

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    # <your code>
    return 1

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    for a in collatz_read(r) :
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
