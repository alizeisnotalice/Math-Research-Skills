#!/usr/bin/env python3
"""Direct finite check of D(K_a join mB,x)."""
import argparse, json

def edges_of(g):
    n = g['n']; seen = set()
    for u, v in g['edges']:
        if not (0 <= u < n and 0 <= v < n) or u == v:
            raise ValueError('edge endpoint out of range or loop')
        e = tuple(sorted((u, v)))
        if e in seen:
            raise ValueError('duplicate edge')
        seen.add(e)
    return n, seen

def domination_poly(n, edges):
    closed = [1 << v for v in range(n)]
    for u, v in edges:
        closed[u] |= 1 << v; closed[v] |= 1 << u
    full = (1 << n) - 1; out = [0] * (n + 1)
    for mask in range(1 << n):
        cover = 0
        for v in range(n):
            if mask >> v & 1:
                cover |= closed[v]
        if cover == full:
            out[bin(mask).count("1")] += 1
    return out

def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return out

def binom_row(n):
    r = [1]
    for _ in range(n): r = [1] + [r[i] + r[i+1] for i in range(len(r)-1)] + [1]
    return r

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--petal-json', required=True); ap.add_argument('--clique', type=int, required=True); ap.add_argument('--copies', type=int, required=True)
    a = ap.parse_args(); b, petal_edges = edges_of(json.loads(a.petal_json))
    if a.clique < 1 or a.copies < 0: raise SystemExit('clique must be >=1 and copies >=0')
    n = a.clique + a.copies*b
    edges = set()
    for u in range(a.clique):
        for v in range(u+1, a.clique): edges.add((u,v))
    for c in range(a.copies):
        off=a.clique+c*b
        edges |= {(off+u,off+v) for u,v in petal_edges}
        edges |= {(u,off+v) for u in range(a.clique) for v in range(b)}
    direct=domination_poly(n,edges); db=domination_poly(b,petal_edges)
    power=[1]
    for _ in range(a.copies): power=mul(power,db)
    formula=binom_row(n); sub=binom_row(a.copies*b)
    formula[:len(sub)]=[formula[i]-sub[i] for i in range(len(sub))]
    formula[:len(power)]=[formula[i]+power[i] for i in range(len(power))]
    print(json.dumps({'vertices':n,'direct':direct,'formula':formula,'exact_match':direct==formula}))
    if direct != formula: raise SystemExit('identity mismatch')

if __name__ == '__main__': main()
