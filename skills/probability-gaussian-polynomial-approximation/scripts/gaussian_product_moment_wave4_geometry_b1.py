#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from fractions import Fraction

def check(a):
    if not a: raise ValueError('at least one coefficient is required')
    s2=sum((x*x for x in a),Fraction(0)); ev2=s2*s2+2*sum((x**4 for x in a),Fraction(0))
    if ev2>3*s2*s2: raise AssertionError('fourth-moment inequality failed')
    return {'coefficients':[str(x) for x in a],'E_V':str(s2),'E_V_squared':str(ev2),'three_s_fourth':str(3*s2*s2),'tail':'P(V>=s^2/2)>=1/12 for s>0'}

def main():
    p=argparse.ArgumentParser(description='Exact Gaussian-square conditional variance identity from OpenAI wave4-b1.')
    p.add_argument('--a',nargs='+');p.add_argument('--self-test',action='store_true');x=p.parse_args()
    if x.self_test:
        assert check([Fraction(1,2),Fraction(1,3)])['E_V']=='13/36';print('PASS: exact conditional Gaussian-square moment identity');return
    if not x.a:p.error('supply --a or --self-test')
    print(json.dumps(check([Fraction(z) for z in x.a]),indent=2,sort_keys=True))
if __name__=='__main__':main()
