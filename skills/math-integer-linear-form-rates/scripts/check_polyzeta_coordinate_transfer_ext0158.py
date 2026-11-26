#!/usr/bin/env python3
"""Exact integer parameter map and K(P) finiteness gate from EXT-0158."""
from __future__ import annotations

import argparse
import json
import sys


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="JSON with n and 1-indexed-looking arrays a,b,c")
    ns = ap.parse_args()
    try:
        d = json.load(open(ns.input))
        n = int(d["n"])
        a, b, c = list(map(int, d["a"])), list(map(int, d["b"])), list(map(int, d["c"]))
        if n < 2 or len(a) != n or len(b) != n or len(c) != n - 1:
            raise ValueError("require n>=2, len(a)=len(b)=n, len(c)=n-1 for c_2,...,c_n")
        # Dictionaries retain the source's one-based subscripts.
        aa = {i + 1: a[i] for i in range(n)}
        bb = {i + 1: b[i] for i in range(n)}
        cc = {i + 2: c[i] for i in range(n - 1)}
        A = {k: aa[n + 1 - k] for k in range(1, n + 1)}
        B = {1: aa[n - 1] + bb[n] - sum(cc.values())}
        B.update({k: bb[n + 1 - k] for k in range(2, n + 1)})
        C = {}
        for k in range(2, n + 1):
            tail = sum(cc[j] for j in range(k, n + 1))
            C[k] = aa[n + 1 - k] + bb[n + 1 - k] - tail if k % 2 == 0 else tail - aa.get(n - k, 0)
        deficit = sum(max(C[k] - B[k], 0) for k in range(2, n + 1))
        nonnegative = all(A[k] >= 0 and B[k] >= 0 for k in range(1, n + 1))
        if not (nonnegative and deficit <= B[1]):
            raise ValueError(f"K(P) finiteness gate fails: nonnegative={nonnegative}, deficit={deficit}, B1={B[1]}")
        print(json.dumps({"accepted": True, "A": [A[k] for k in range(1, n + 1)],
                          "B": [B[k] for k in range(1, n + 1)],
                          "C": [C[k] for k in range(2, n + 1)],
                          "deficit": deficit}, sort_keys=True))
        return 0
    except (OSError, KeyError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"rejected: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
