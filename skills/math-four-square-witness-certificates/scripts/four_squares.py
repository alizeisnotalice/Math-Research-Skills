#!/usr/bin/env python3
"""Exact finite witnesses for n = a^2+b^2+c^2+d^2; no existence claim."""
from __future__ import annotations
import argparse, json
from math import isqrt

def verify(n: int, values: tuple[int,int,int,int]) -> dict[str,object]:
    if n < 0: raise ValueError("n must be nonnegative")
    if sum(x*x for x in values) != n: raise ValueError("the supplied tuple is not a four-square witness")
    return {"n":n,"squares":list(values),"verified":True}

def search(n: int) -> dict[str,object]:
    if n < 0: raise ValueError("n must be nonnegative")
    pairs: dict[int,tuple[int,int]]={}
    for a in range(isqrt(n)+1):
        for b in range(a,isqrt(n-a*a)+1): pairs.setdefault(a*a+b*b,(a,b))
    for total,(a,b) in pairs.items():
        if n-total in pairs:
            c,d=pairs[n-total]
            return verify(n,(a,b,c,d))
    raise RuntimeError("no witness found by the finite search")

def main() -> None:
    p=argparse.ArgumentParser(description=__doc__); sub=p.add_subparsers(dest="action",required=True)
    s=sub.add_parser("search"); s.add_argument("n",type=int)
    v=sub.add_parser("verify"); v.add_argument("n",type=int); v.add_argument("a",type=int); v.add_argument("b",type=int); v.add_argument("c",type=int); v.add_argument("d",type=int)
    args=p.parse_args()
    try: print(json.dumps(search(args.n) if args.action=="search" else verify(args.n,(args.a,args.b,args.c,args.d)),sort_keys=True))
    except ValueError as error: p.error(str(error))
if __name__ == "__main__": main()
