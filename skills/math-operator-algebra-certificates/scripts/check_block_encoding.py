#!/usr/bin/env python3
"""Exact finite real-matrix replay of the four-to-two block encoding."""
import json
import sys
from fractions import Fraction


def q(x): return Fraction(str(x))


def mat(a):
    if not isinstance(a, list) or not a or any(not isinstance(r, list) for r in a):
        raise ValueError("matrix must be a nonempty list of lists")
    n = len(a)
    if any(len(r) != n for r in a): raise ValueError("matrix must be square")
    return [[q(x) for x in r] for r in a]


def zero(n): return [[Fraction(0) for _ in range(n)] for _ in range(n)]
def ident(n):
    z = zero(n)
    for i in range(n): z[i][i] = 1
    return z
def add(x, y): return [[x[i][j]+y[i][j] for j in range(len(x))] for i in range(len(x))]
def sub(x, y): return [[x[i][j]-y[i][j] for j in range(len(x))] for i in range(len(x))]
def scale(c, x): return [[c*x[i][j] for j in range(len(x))] for i in range(len(x))]
def mul(x, y):
    n=len(x)
    return [[sum((x[i][k]*y[k][j] for k in range(n)), Fraction(0)) for j in range(n)] for i in range(n)]
def sym(x): return x == [list(r) for r in zip(*x)]
def rs(x): return max(sum(abs(v) for v in r) for r in x)
def block(a, b, c, d):
    n=len(a); z=zero(2*n)
    for i in range(n):
        for j in range(n): z[i][j],z[i][j+n],z[i+n][j],z[i+n][j+n]=a[i][j],b[i][j],c[i][j],d[i][j]
    return z
def flat(x): return [v for r in x for v in r]


def rank(vectors):
    rows=[list(v) for v in vectors if any(v)]; r=0; cols=len(rows[0]) if rows else 0
    for c in range(cols):
        pivot=next((i for i in range(r,len(rows)) if rows[i][c]), None)
        if pivot is None: continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        lead=rows[r][c]; rows[r]=[v/lead for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                z=rows[i][c]; rows[i]=[rows[i][j]-z*rows[r][j] for j in range(cols)]
        r += 1
        if r == len(rows): break
    return r


def algebra_dimension(gens):
    n=len(gens[0]); basis=[ident(n)]; changed=True
    while changed:
        changed=False
        for x in list(basis):
            for g in gens:
                y=mul(x,g)
                if rank([flat(z) for z in basis]+[flat(y)]) > len(basis):
                    basis.append(y); changed=True
                    if len(basis) == n*n: return len(basis)
    return len(basis)


def main(path):
    try:
        with open(path) as f: d=json.load(f)
        aa=[mat(d[f"a{i}"]) for i in range(1,5)]
        n=len(aa[0])
        if any(len(a)!=n for a in aa) or not all(sym(a) for a in aa):
            raise ValueError("all a_i must be same-size real symmetric matrices")
        C=q(d["C"]); R1,R2=rs(aa[0]),rs(aa[1])
        if not C > R1+R2:
            raise ValueError(f"strict sufficient gap fails: C={C} is not > R1+R2={R1+R2}")
        I=ident(n); Z=zero(n)
        A=block(aa[0],Z,Z,add(aa[1],scale(C,I)))
        B=block(aa[2],I,I,aa[3]); E11=block(I,Z,Z,Z); E22=block(Z,Z,Z,I); E12=block(Z,I,Z,Z); E21=block(Z,Z,I,Z)
        checks=[mul(mul(E11,B),E22)==E12, mul(mul(E22,B),E11)==E21,
                mul(mul(E11,A),E11)==block(aa[0],Z,Z,Z),
                sub(mul(mul(E12,A),E21),scale(C,E11))==block(aa[1],Z,Z,Z),
                mul(mul(E11,B),E11)==block(aa[2],Z,Z,Z),
                mul(mul(E12,B),E21)==block(aa[3],Z,Z,Z)]
        if not all(checks): raise AssertionError("a displayed corner identity failed")
        dN=algebra_dimension(aa); dM=algebra_dimension([A,B])
        print(f"accepted n={n} R1={R1} R2={R2} C={C} lambda={(R1+C-R2)/2}")
        print(f"corner_identities=6/6 generated_dimensions=N:{dN}/{n*n}, M2N:{dM}/{(2*n)**2}")
    except (KeyError, TypeError, ValueError, AssertionError, json.JSONDecodeError) as e:
        print(f"rejected: {e}", file=sys.stderr); return 2
    return 0


if __name__ == "__main__":
    if len(sys.argv)!=2:
        print("usage: check_block_encoding.py INPUT.json", file=sys.stderr); sys.exit(2)
    sys.exit(main(sys.argv[1]))
