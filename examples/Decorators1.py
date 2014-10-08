#!/usr/bin/env python3

# --------------
# Decorators1.py
# --------------

class cache :
    def __init__ (self, f) :
        self.f = f
        self.d = {}

    def __call__ (self, k) :
        if k in self.d :
            return self.d[k]
        v = self.f(k)
        self.d[k] = v
        return v

def cycle_length_1 (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

@cache
def cycle_length_2 (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

print("Decorators1.py")

assert cycle_length_1( 1) == 1
assert cycle_length_1( 5) == 6
assert cycle_length_1(10) == 7

cycle_length_1 = cache(cycle_length_1)

assert cycle_length_1( 1) == 1
assert cycle_length_1( 5) == 6
assert cycle_length_1(10) == 7

assert cycle_length_2( 1) == 1
assert cycle_length_2( 5) == 6
assert cycle_length_2(10) == 7

print("Done.")
