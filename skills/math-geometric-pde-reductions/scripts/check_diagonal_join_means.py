#!/usr/bin/env python3
"""Exact arithmetic check for the scalar-leaf mean identities on source p.6."""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


def q(x):
    if isinstance(x, bool) or not isinstance(x, (int, str)):
        raise ValueError("all values must be integer or rational strings")
    return Fraction(x)


def text(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main(argv):
    if len(argv) != 2:
        print("usage: check_diagonal_join_means.py INPUT.json", file=sys.stderr); return 2
    try:
        raw=json.loads(Path(argv[1]).read_text()); M=q(raw["M"]); alpha=[q(x) for x in raw["alpha"]]
        if len(alpha)!=3 or M<=0 or any(x<=0 or x>=M for x in alpha):
            raise ValueError("require three values with 0 < alpha_i < M")
    except (OSError,json.JSONDecodeError,KeyError,ValueError,ZeroDivisionError) as exc:
        print(f"input rejected: {exc}",file=sys.stderr); return 2
    rows=[]
    for i,a in enumerate(alpha,1):
        d2=1-a/M
        # Mean of 1+-d is 1; harmonic mean is 1-d^2, expressed without choosing sqrt(d2).
        if (1-d2)*M != a: raise AssertionError("identity failure")
        rows.append({"coordinate":i,"d_squared":text(d2),"arithmetic_mean_t":"1","harmonic_mean_Mt":text(a)})
    print(json.dumps({"status":"pass","M":text(M),"coordinates":rows},indent=2)); return 0


if __name__=="__main__": raise SystemExit(main(sys.argv))
