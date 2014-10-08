#!/usr/bin/env python3

"""
CS373: Quiz #18 (10 pts) <Raul>
"""

""" ----------------------------------------------------------------------
 1. What's the output of the following?
    (9 pts)

[{'sName': 'Fay',   'sID': 678},
 {'sName': 'Irene', 'sID': 876}]
[]
"""

def select (r, up) :
    return [v for v in r if up(v)]

def project (r, a) :
    return [{w : v[w] for w in a if w in v} for v in r]

Student = [ \
    {"sID" : 123, "sName" : 'Amy',   "GPA" : 3.9, "sizeHS" : 1000},
    {"sID" : 678, "sName" : 'Fay',   "GPA" : 3.8, "sizeHS" :  200},
    {"sID" : 876, "sName" : 'Irene', "GPA" : 3.9, "sizeHS" :  400},
    {"sID" : 654, "sName" : 'Amy',   "GPA" : 3.9, "sizeHS" : 1000}]

print(
    project(
        select(
            Student,
            lambda v :
                ("GPA"       in v)      and
                (v["GPA"]    >  3.7)    and
                ("sizeHS"    in v)      and
                (v["sizeHS"] <  1000)),
        ["sID", "sName"]))

print(
    select(
        project(
            Student,
            ["sID", "sName"]),
        lambda v :
            ("GPA"       in v)      and
            (v["GPA"]    >  3.7)    and
            ("sizeHS"    in v)      and
            (v["sizeHS"] <  1000)))
