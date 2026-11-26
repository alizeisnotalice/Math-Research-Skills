#!/usr/bin/env python3
"""Exact finite audit for the Hermitian Rademacher setup in Lemma 3.1."""
from __future__ import annotations
import argparse, itertools, json, sys
from fractions import Fraction

def rat(x):
    if isinstance(x, bool): raise ValueError("Boolean is not a rational entry")
    return Fraction(str(x))
def zp(x):
    if isinstance(x, dict):
        if set(x) - {"re", "im"}: raise ValueError("complex entry has only re and im")
        return rat(x.get("re",0)), rat(x.get("im",0))
    return rat(x), Fraction(0)
def za(x,y): return x[0]+y[0],x[1]+y[1]
def zn(x): return -x[0],-x[1]
def zs(c,x): return c*x[0],c*x[1]
def zm(x,y): return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def zc(x): return x[0],-x[1]
def zz(): return Fraction(0),Fraction(0)
def zo(): return Fraction(1),Fraction(0)
def iszero(x): return x == zz()
def zero(n): return [[zz() for _ in range(n)] for _ in range(n)]
def eye(n):
    r=zero(n)
    for i in range(n): r[i][i]=zo()
    return r
def madd(a,b): return [[za(x,y) for x,y in zip(r,s)] for r,s in zip(a,b)]
def mscale(c,a): return [[zs(c,x) for x in r] for r in a]
def mmul(a,b):
    n=len(a); r=zero(n)
    for i in range(n):
        for k in range(n):
            if not iszero(a[i][k]):
                for j in range(n): r[i][j]=za(r[i][j],zm(a[i][k],b[k][j]))
    return r
def mpow(a,e):
    r=eye(len(a)); b=a
    while e:
        if e&1: r=mmul(r,b)
        b=mmul(b,b); e>>=1
    return r
def tr(a):
    r=zz()
    for i in range(len(a)): r=za(r,a[i][i])
    return r
def det(a):
    n=len(a)
    if not n: return zo()
    a=[[x for x in row] for row in a]; d=zo()
    for j in range(n):
        p=next((i for i in range(j,n) if not iszero(a[i][j])),None)
        if p is None: return zz()
        if p!=j: a[j],a[p]=a[p],a[j]; d=zn(d)
        x=a[j][j]; d=zm(d,x); den=x[0]*x[0]+x[1]*x[1]; inv=(x[0]/den,-x[1]/den)
        for i in range(j+1,n):
            f=zm(a[i][j],inv)
            for k in range(j+1,n): a[i][k]=za(a[i][k],zn(zm(f,a[j][k])))
    return d
def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("input")
    ns=ap.parse_args()
    try:
        d=json.load(open(ns.input,encoding="utf-8")); mats=[[[zp(x) for x in r] for r in m] for m in d["matrices"]]
        a=int(d["a"]); v=rat(d["variance_upper"])
        if not mats or a<1 or v<0: raise ValueError("require nonempty matrices, a>=1, variance_upper>=0")
        n=len(mats[0]); q=len(mats)
        if not 1<=n<=8 or q>18: raise ValueError("audit caps are 1<=dimension<=8 and number of signs<=18")
        if any(len(m)!=n or any(len(r)!=n for r in m) for m in mats): raise ValueError("all matrices must be square of one common size")
        if any(m[i][j]!=zc(m[j][i]) for m in mats for i in range(n) for j in range(n)): raise ValueError("every matrix must be Hermitian")
        var=zero(n)
        for m in mats: var=madd(var,mmul(m,m))
        slack=madd(mscale(v,eye(n)),mscale(Fraction(-1),var)); minors=[]
        for r in range(1,n+1):
            for ix in itertools.combinations(range(n),r):
                x=det([[slack[i][j] for j in ix] for i in ix])
                if x[1]: raise ValueError("variance slack determinant was non-real")
                minors.append(x[0])
        if any(x<0 for x in minors):
            print(json.dumps({"accepted":False,"reason":"variance certificate fails: vI-sum(L_i^2) is not PSD","minimum_principal_minor":str(min(minors))},sort_keys=True)); return 2
        total=Fraction(0)
        for signs in itertools.product((-1,1),repeat=q):
            s=zero(n)
            for sign,m in zip(signs,mats): s=madd(s,mscale(Fraction(sign),m))
            x=tr(mpow(s,2*a))
            if x[1]: raise ValueError("even Hermitian trace power was non-real")
            total+=x[0]
        actual=total/(1<<q); odd=1
        for j in range(1,2*a,2): odd*=j
        upper=Fraction(n*odd)*v**a
        print(json.dumps({"accepted":True,"dimension":n,"signs":q,"a":a,"variance_upper":str(v),"minimum_principal_minor":str(min(minors)),"rademacher_trace_moment":str(actual),"gaussian_trace_moment_upper":str(upper),"rademacher_moment_within_gaussian_upper":actual<=upper,"scope":"exact finite enumeration only; no general expectation-norm proof"},sort_keys=True))
    except (KeyError,ValueError,ZeroDivisionError,json.JSONDecodeError) as exc:
        print(json.dumps({"accepted":False,"reason":str(exc)},sort_keys=True)); return 2
    return 0
if __name__=="__main__": sys.exit(main())
