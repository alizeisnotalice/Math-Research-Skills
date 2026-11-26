#!/usr/bin/env python3
"""Exact finite check of binary posterior fusion for two BSC observations."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction


def parse_probability(text: str) -> Fraction:
    value = Fraction(text)
    if not Fraction(1, 2) < value < 1:
        raise ValueError("each BSC correctness probability must lie in (1/2,1)")
    return value


def posterior(sign: int, p: Fraction) -> Fraction:
    return sign * (2 * p - 1)


def direct_posterior(sign_a: int, sign_b: int, p: Fraction, q: Fraction) -> Fraction:
    plus = (p if sign_a == 1 else 1 - p) * (q if sign_b == 1 else 1 - q)
    minus = (1 - p if sign_a == 1 else p) * (1 - q if sign_b == 1 else q)
    return (plus - minus) / (plus + minus)


def run(p: Fraction, q: Fraction) -> dict[str, str]:
    checks: dict[str, str] = {}
    for a in (-1, 1):
        for b in (-1, 1):
            u, v = posterior(a, p), posterior(b, q)
            fused = (u + v) / (1 + u * v)
            exact = direct_posterior(a, b, p, q)
            if fused != exact:
                raise AssertionError(f"fusion mismatch for {(a, b)}: {fused} != {exact}")
            checks[f"{a:+d},{b:+d}"] = str(fused)
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", default="3/4")
    parser.add_argument("--q", default="2/3")
    args = parser.parse_args()
    try:
        p, q = parse_probability(args.p), parse_probability(args.q)
    except (ValueError, ZeroDivisionError) as exc:
        parser.error(str(exc))
    print(json.dumps({"p": str(p), "q": str(q), "posteriors": run(p, q)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
