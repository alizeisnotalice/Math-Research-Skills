#!/usr/bin/env python3
"""Exact finite certificate for the Machin admissibility equation in EXT-0192."""
import argparse
import json
import math
import sys


def valid(P, u, v):
    if not all(isinstance(x, int) for x in (P, u, v)) or P <= 0 or v <= 0:
        return None
    left = P * P - u * u - v * v
    right = 2 * P * v
    if left == right:
        return 1
    if left == -right:
        return -1
    return None


def check_file(path):
    item = json.load(open(path, encoding="utf-8"))
    sign = valid(item.get("P"), item.get("u"), item.get("v"))
    if sign is None:
        raise ValueError("P,u,v do not satisfy P^2-(u^2+v^2)=+/-2Pv with P,v>0")
    print(json.dumps({"status": "valid", "P": item["P"], "u": item["u"], "v": item["v"], "sign": sign, "primitive": math.gcd(math.gcd(item["P"], abs(item["u"])), item["v"]) == 1}, sort_keys=True))


def enumerate_limit(limit):
    if limit < 2:
        raise ValueError("limit must be at least 2")
    rows = []
    for P in range(2, limit + 1):
        for u in range(1, P):
            for v in range(1, P):
                sign = valid(P, u, v)
                if sign == 1 and math.gcd(math.gcd(P, u), v) == 1:
                    rows.append([P, u, v])
    print(json.dumps({"limit": limit, "primitive_positive_sign_solutions": rows, "count": len(rows)}, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("input", nargs="?", help="JSON file with integer P,u,v")
    group.add_argument("--limit", type=int, help="enumerate primitive plus-sign configurations")
    args = parser.parse_args()
    if args.input:
        check_file(args.input)
    else:
        enumerate_limit(args.limit)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"invalid: {error}", file=sys.stderr)
        sys.exit(2)
