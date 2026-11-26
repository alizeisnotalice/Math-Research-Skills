#!/usr/bin/env python3
"""Exact extended-order reduction for a^x + b^y = c^z."""
from __future__ import annotations
import argparse, json
from math import gcd

def extended_order(base: int, modulus: int) -> int:
    if modulus <= 2 or gcd(base, modulus) != 1:
        raise ValueError("require modulus > 2 and base coprime to modulus")
    residue = 1
    for exponent in range(1, modulus + 1):
        residue = residue * base % modulus
        if residue in (1, modulus - 1): return exponent
    raise AssertionError("finite-unit-group search did not find an extended order")

def reduce(a: int, b: int, c: int, d: int) -> dict[str, int]:
    if min(a,b,c) <= 1 or d <= 2 or c % d: raise ValueError("require a,b,c > 1, d > 2, and d dividing c")
    if gcd(a,b) != 1 or gcd(a,c) != 1 or gcd(b,c) != 1: raise ValueError("require pairwise-coprime a, b, c")
    ea, eb = extended_order(a,d), extended_order(b,d); g = gcd(ea,eb)
    return {"a":a,"b":b,"c":c,"d":d,"e_a":ea,"e_b":eb,"g":g,"A":a**(ea//g),"B":b**(eb//g)}

def main() -> None:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("a",type=int); p.add_argument("b",type=int); p.add_argument("c",type=int); p.add_argument("d",type=int); p.add_argument("--solution",nargs=3,type=int,metavar=("x","y","z")); args=p.parse_args()
    try:
        result=reduce(args.a,args.b,args.c,args.d)
        if args.solution:
            x,y,z=args.solution
            if min(x,y,z)<=0 or args.a**x+args.b**y != args.c**z: raise ValueError("the proposed positive exponents do not solve a^x+b^y=c^z")
            sx,sy=result["e_a"]//result["g"],result["e_b"]//result["g"]
            if x%sx or y%sy: raise AssertionError("source divisibility conclusion failed")
            X,Y=x//sx,y//sy
            if result["A"]**X+result["B"]**Y != args.c**z: raise AssertionError("rescaled equation failed")
            result["solution"]={"x":x,"y":y,"z":z,"X":X,"Y":Y}
        print(json.dumps(result,sort_keys=True))
    except ValueError as error: p.error(str(error))
if __name__ == "__main__": main()
