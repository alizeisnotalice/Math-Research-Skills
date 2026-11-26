#!/usr/bin/env python3
"""Exhaustively validate the finite affine medial-rack witness in recent-05."""

from __future__ import annotations

import argparse
import json


def is_prime(value: int) -> bool:
    return value >= 2 and all(value % divisor for divisor in range(2, int(value**0.5) + 1))


def audit(prime: int, lam: int) -> dict[str, object]:
    if not is_prime(prime):
        raise ValueError("prime must be a prime integer")
    lam %= prime
    if lam in (0, 1):
        raise ValueError("lambda must be nonzero and different from one modulo prime")
    elements = range(prime)
    op = lambda x, y: ((1 - lam) * x + lam * y) % prime
    for x in elements:
        if op(x, x) != x:
            raise AssertionError("idempotence failed")
        if len({op(x, y) for y in elements}) != prime:
            raise AssertionError("a left translation is not bijective")
    for x in elements:
        for y in elements:
            for z in elements:
                if op(x, op(y, z)) != op(op(x, y), op(x, z)):
                    raise AssertionError("left self-distributivity failed")
                for w in elements:
                    if op(op(x, y), op(z, w)) != op(op(x, z), op(y, w)):
                        raise AssertionError("mediality failed")
    non_two_reductive = any(
        op(op(x, y), z) != op(op(x, z), z)
        for x in elements for y in elements for z in elements
    )
    if not non_two_reductive:
        raise AssertionError("the supplied operation is 2-reductive")
    return {
        "prime": prime,
        "lambda": lam,
        "checks": ["idempotent", "left_bijective", "left_self_distributive", "medial"],
        "two_reductive": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=5)
    parser.add_argument("--lambda", dest="lam", type=int, default=2)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    result = audit(args.prime, args.lam)
    if args.self_test:
        try:
            audit(args.prime, 1)
        except ValueError:
            result["negative_boundary_rejected"] = True
        else:
            raise SystemExit("lambda=1 was incorrectly accepted")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
