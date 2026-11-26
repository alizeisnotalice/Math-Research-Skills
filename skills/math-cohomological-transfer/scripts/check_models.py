#!/usr/bin/env python3
"""Exact F_2 coproduct checks for the two finite symbolic models in the reference."""
from collections import defaultdict

def add(*terms):
    out = defaultdict(int)
    for t in terms:
        for m, c in t.items(): out[m] ^= c & 1
    return {m:c for m,c in out.items() if c}
def mul(a,b, truncate_x=False):
    out = defaultdict(int)
    for (a0,a1,a2,a3), ca in a.items():
        for (b0,b1,b2,b3), cb in b.items():
            m=(a0+b0,a1+b1,a2+b2,a3+b3)
            if not (truncate_x and (m[0] >= 2 or m[2] >= 2)):
                out[m] ^= ca & cb
    return {m:c for m,c in out.items() if c}
one={(0,0,0,0):1}
x={(1,0,0,0):1}; X={(0,0,1,0):1}
y={(0,1,0,0):1}; Y={(0,0,0,1):1}
dx=add(x,X)
dy=add(y,Y,mul(x,X))
for truncated in (False, True):
    assert mul(dx, dx, truncated) == add(mul(x,x,truncated), mul(X,X,truncated))
    assert add(dy,y,Y) == mul(x,X,truncated)
    dy_sq=mul(dy,dy,truncated)
    expected=add(mul(y,y,truncated), mul(Y,Y,truncated))
    if not truncated: expected=add(expected, mul(mul(x,X),mul(x,X),False))
    assert dy_sq == expected
assert add(mul(dx,dx,False), mul(x,x,False), mul(X,X,False)) == {}
assert add(mul(dy,dy,True), mul(y,y,True), mul(Y,Y,True)) == {}
assert add(dy,y,Y) != {}
print('PASS polynomial: x^2 primitive with primitive root x')
print('PASS boundary quotient: y^2 primitive but y nonprimitive; Frobenius is not injective')
