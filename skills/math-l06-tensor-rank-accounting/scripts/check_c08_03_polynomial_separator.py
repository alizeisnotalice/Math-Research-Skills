#!/usr/bin/env python3
"""Exact prime-field checks for the polynomial separator's finite identities."""

from __future__ import annotations

import argparse


def is_prime(p: int) -> bool:
    if p < 2:
        return False
    d = 2
    while d * d <= p:
        if p % d == 0:
            return False
        d += 1
    return True


def rank_mod(matrix: list[list[int]], p: int) -> int:
    a = [[x % p for x in row] for row in matrix]
    rows, cols, rank = len(a), len(a[0]), 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(inv * x) % p for x in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col]:
                c = a[r][col]
                a[r] = [(x - c * y) % p for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


def substitute(power: int, a: int, n: int, p: int) -> dict[tuple[int, int], int]:
    """Return (a + eps*u)^power in F_p[eps,u]/(u^n)."""
    out: dict[tuple[int, int], int] = {}
    for e in range(power + 1):
        if e < n:
            out[(e, e)] = (out.get((e, e), 0) + pow(a, power - e, p)
                            * _binom(power, e)) % p
    return {k: v for k, v in out.items() if v}


def multiply(left: dict[tuple[int, int], int], right: dict[tuple[int, int], int],
             n: int, p: int) -> dict[tuple[int, int], int]:
    out: dict[tuple[int, int], int] = {}
    for (de, du), x in left.items():
        for (ee, eu), y in right.items():
            if du + eu < n:
                key = (de + ee, du + eu)
                out[key] = (out.get(key, 0) + x * y) % p
    return {k: v for k, v in out.items() if v}


def _binom(n: int, k: int) -> int:
    num = den = 1
    for j in range(1, k + 1):
        num *= n - k + j
        den *= j
    return num // den


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--M", type=int, required=True)
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--p", type=int, required=True)
    args = parser.parse_args()
    if args.M < 1 or args.n < 1 or not is_prime(args.p):
        raise SystemExit("M,n must be positive and p must be prime")
    ell = args.M + args.n - 1
    if args.p < ell:
        raise SystemExit("FAIL: F_p lacks the required M+n-1 distinct elements")
    points = list(range(args.M))
    vandermonde = [[pow(a, degree, args.p) for degree in range(args.M)]
                   for a in points]
    if rank_mod(vandermonde, args.p) != args.M:
        raise SystemExit("FAIL: evaluation map is not invertible")
    max_degree = 0
    for a in points:
        for i in range(args.M):
            for k in range(args.n):
                lhs = multiply(substitute(i, a, args.n, args.p),
                               substitute(k, a, args.n, args.p), args.n, args.p)
                rhs = substitute(i + k, a, args.n, args.p)
                if lhs != rhs:
                    raise SystemExit("FAIL: substitution does not preserve products")
                sigma = multiply(substitute(i, a, args.n, args.p),
                                 {(0, k): 1}, args.n, args.p)
                degrees = [key[0] for key in sigma]
                if degrees:
                    max_degree = max([max_degree, *degrees])
    bound = min(args.M - 1, args.n - 1)
    if max_degree > bound:
        raise SystemExit("FAIL: truncated-family degree bound violated")
    print(f"PASS F_{args.p}, M={args.M}, n={args.n}, ell={ell}")
    print(f"evaluation rank={args.M}; product identity checked for {args.M * args.M * args.n} basis pairs")
    print(f"epsilon degree <= {max_degree} <= {bound}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
