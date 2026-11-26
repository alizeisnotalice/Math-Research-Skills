#!/usr/bin/env python3
"""Exact polynomial identity from the U(n)-invariant Calabi-flow reduction.

Given n>=1 and polynomial H(x), calculate K=(w*v_*^2*H)''/w,
w=x^(n-1), v_*=x(1-x), and certify integral_0^1 K*w dx=0.
This checks the source's radial algebra only, not positivity of 1+v_*H or
existence/singularity of a Calabi flow.
"""
from __future__ import annotations
import argparse, json
from fractions import Fraction

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a
def mul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def diff(a):
    return trim([Fraction(i)*a[i] for i in range(1,len(a))] or [Fraction(0)])
def integral01(a):
    return sum((x/Fraction(i+1) for i,x in enumerate(a)),Fraction(0))
def show(a): return [str(x) for x in trim(a)]

def check(n, h):
    if n<1: raise ValueError('n must be at least 1')
    w=[Fraction(0)]*(n-1)+[Fraction(1)]
    v=[Fraction(0),Fraction(1),Fraction(-1)]
    numerator=diff(diff(mul(mul(w,mul(v,v)),h)))
    if any(numerator[i] for i in range(n-1)):
        raise AssertionError('source endpoint divisibility failed')
    k=trim(numerator[n-1:] or [Fraction(0)])
    average=integral01(mul(k,w))
    if average!=0: raise AssertionError('weighted average identity failed')
    b=trim([Fraction(1)]+[Fraction(0)]*(max(len(mul(v,h)),1)-1))
    vh=mul(v,h)
    if len(b)<len(vh): b += [Fraction(0)]*(len(vh)-len(b))
    for i,x in enumerate(vh): b[i]+=x
    return {'n':n,'H_coefficients_low_to_high':show(h),'K_coefficients_low_to_high':show(k),'b_coefficients_low_to_high':show(b),'integral_0_1_Kw':str(average)}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--n',type=int)
    p.add_argument('--h',nargs='+',help='rational H coefficients, constant first')
    p.add_argument('--self-test',action='store_true')
    a=p.parse_args()
    if a.self_test:
        out=check(2,[Fraction(1),Fraction(1)])
        assert out['integral_0_1_Kw']=='0'
        print('PASS: exact radial K identity for n=2, H=1+x')
        return
    if a.n is None or not a.h: p.error('supply --n and --h, or --self-test')
    print(json.dumps(check(a.n,[Fraction(x) for x in a.h]),indent=2,sort_keys=True))
if __name__=='__main__': main()
