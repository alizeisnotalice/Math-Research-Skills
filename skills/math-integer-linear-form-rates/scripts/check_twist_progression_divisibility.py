#!/usr/bin/env python3
"""Exact check of Sprang Lemma 1.2 for one finite arithmetic progression."""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path


def main(argv):
    if len(argv) != 2:
        print("usage: check_twist_progression_divisibility.py INPUT.json", file=sys.stderr); return 2
    try:
        raw=json.loads(Path(argv[1]).read_text())
        D,n,k,i=(raw[x] for x in ("D","n","k","i"))
        if any(isinstance(x,bool) or not isinstance(x,int) for x in (D,n,k,i)) or D<1 or n<1:
            raise ValueError("D and n must be positive integers; k and i integers")
    except (OSError,json.JSONDecodeError,KeyError,ValueError) as exc:
        print(f"input rejected: {exc}",file=sys.stderr); return 2
    nf=math.factorial(n); divisor=nf//math.gcd(D**n,nf); product=math.prod(D*j+i for j in range(k,k+n))
    if product%divisor:
        raise AssertionError("stated divisor failed")
    print(json.dumps({"status":"pass","divisor":divisor,"product":product,"quotient":product//divisor},indent=2)); return 0


if __name__=="__main__": raise SystemExit(main(sys.argv))
