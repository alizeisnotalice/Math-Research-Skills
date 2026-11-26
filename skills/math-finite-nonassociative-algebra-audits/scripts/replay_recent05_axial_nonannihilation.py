#!/usr/bin/env python3
"""Exact replay of the finite table used in the recent-05 axial-algebra source."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction


Q = Fraction
BASIS = ("a", "b", "x", "c")
Z = (Q(0),) * 4


def vec(*entries: Q) -> tuple[Q, Q, Q, Q]:
    return tuple(entries)  # type: ignore[return-value]


def add(*vectors: tuple[Q, Q, Q, Q]) -> tuple[Q, Q, Q, Q]:
    return tuple(sum(v[i] for v in vectors) for i in range(4))  # type: ignore[return-value]


def scale(scalar: Q, value: tuple[Q, Q, Q, Q]) -> tuple[Q, Q, Q, Q]:
    return tuple(scalar * x for x in value)  # type: ignore[return-value]


def table(zero_cross_product: bool = False) -> dict[tuple[int, int], tuple[Q, Q, Q, Q]]:
    """Return the symmetric multiplication table, optionally with the bad boundary edit."""
    a, b, x, c = (vec(*(Q(i == j) for i in range(4))) for j in range(4))
    entries = {
        (0, 0): a,
        (1, 1): b,
        (2, 2): x,
        (3, 3): c,
        (0, 1): scale(Q(1, 4), add(a, b, scale(-Q(1), x))),
        (0, 2): scale(Q(1, 4), add(a, scale(-Q(1), b), x)),
        (1, 2): scale(Q(1, 4), add(scale(-Q(1), a), b, x)),
        (0, 3): Z,
        (1, 3): Z,
        (2, 3): Z if zero_cross_product else add(
            scale(-Q(1, 2), a), scale(-Q(1, 2), b), scale(Q(1, 2), x), scale(-Q(1, 4), c)
        ),
    }
    return {**entries, **{(j, i): value for (i, j), value in entries.items()}}


def multiply(left: tuple[Q, Q, Q, Q], right: tuple[Q, Q, Q, Q], products: dict) -> tuple[Q, Q, Q, Q]:
    result = [Q(0)] * 4
    for i, li in enumerate(left):
        for j, rj in enumerate(right):
            for k, coefficient in enumerate(products[(i, j)]):
                result[k] += li * rj * coefficient
    return tuple(result)  # type: ignore[return-value]


def rank(rows: list[tuple[Q, Q, Q, Q]]) -> int:
    work = [list(row) for row in rows]
    pivot_row = 0
    for column in range(4):
        pivot = next((r for r in range(pivot_row, len(work)) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        factor = work[pivot_row][column]
        work[pivot_row] = [item / factor for item in work[pivot_row]]
        for r in range(len(work)):
            if r != pivot_row and work[r][column]:
                factor = work[r][column]
                work[r] = [u - factor * v for u, v in zip(work[r], work[pivot_row])]
        pivot_row += 1
    return pivot_row


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def audit(zero_cross_product: bool = False) -> dict[str, object]:
    products = table(zero_cross_product)
    a, b, x, c = (vec(*(Q(i == j) for i in range(4))) for j in range(4))
    mul = lambda u, v: multiply(u, v, products)

    require(all(mul(u, u) == u for u in (a, b, x, c)), "basis idempotents fail")
    require(mul(a, c) == Z and mul(b, c) == Z, "displayed zero products fail")
    require(mul(x, c) != Z, "the source's non-annihilating cross product is absent")

    # The source's eigenspace witnesses for a and b.
    a0 = (add(b, x, scale(-Q(1, 2), a)), c)
    ah = add(x, scale(-Q(1), b))
    b0 = (add(a, x, scale(-Q(1, 2), b)), c)
    bh = add(x, scale(-Q(1), a))
    for witness in a0:
        require(mul(a, witness) == Z, "a zero-eigenvector check fails")
    require(mul(a, ah) == scale(Q(1, 2), ah), "a half-eigenvector check fails")
    for witness in b0:
        require(mul(b, witness) == Z, "b zero-eigenvector check fails")
    require(mul(b, bh) == scale(Q(1, 2), bh), "b half-eigenvector check fails")
    require(mul(ah, ah) == add(scale(Q(3, 4), a), scale(Q(1, 2), a0[0])), "a fusion square fails")
    require(mul(bh, bh) == add(scale(Q(3, 4), b), scale(Q(1, 2), b0[0])), "b fusion square fails")

    # The source's c-eigenvector and its fusion square.
    w = add(scale(Q(2), x), scale(-Q(2), a), scale(-Q(2), b), c)
    require(mul(c, w) == scale(Q(1, 2), w), "c half-eigenvector check fails")
    require(mul(w, w) == add(scale(Q(4), a), scale(Q(4), b)), "c fusion square fails")

    # Direct replay of the P_c functional separation in the simplicity argument.
    def pc(u: tuple[Q, Q, Q, Q]) -> tuple[Q, Q, Q, Q]:
        return add(scale(Q(2), mul(c, mul(c, u))), scale(-Q(1), mul(c, u)))

    phi_row = (Q(0), Q(0), -Q(1, 2), Q(1))
    phi = lambda u: sum(q * z for q, z in zip(phi_row, u))
    require(all(pc(u) == scale(phi(u), c) for u in (a, b, x, c)), "P_c identity fails")
    rows = [
        phi_row,
        tuple(phi(mul(a, basis)) for basis in (a, b, x, c)),
        tuple(phi(mul(b, basis)) for basis in (a, b, x, c)),
        tuple(phi(mul(x, basis)) for basis in (a, b, x, c)),
    ]
    require(rows == [
        (Q(0), Q(0), -Q(1, 2), Q(1)),
        (Q(0), Q(1, 8), -Q(1, 8), Q(0)),
        (Q(1, 8), Q(0), -Q(1, 8), Q(0)),
        (-Q(1, 8), -Q(1, 8), -Q(1, 2), -Q(1, 2)),
    ], "the displayed functional coefficients fail")
    require(rank(rows) == 4, "the four simplicity functionals do not separate vectors")
    xc = mul(x, c)
    require(a == add(scale(Q(1, 2), c), scale(Q(2), xc), scale(-Q(4), mul(a, xc))), "a reconstruction fails")
    require(b == add(scale(Q(1, 2), c), scale(Q(2), xc), scale(-Q(4), mul(b, xc))), "b reconstruction fails")
    require(x == add(a, b, scale(-Q(4), mul(a, b))), "x reconstruction fails")

    return {
        "basis": BASIS,
        "field": "Q",
        "functional_rank": 4,
        "checks": ["idempotents", "eigenvectors", "fusion_squares", "P_c", "reconstruction", "xc_nonzero"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true", help="also require a perturbed table to be rejected")
    args = parser.parse_args()
    result = audit()
    if args.self_test:
        try:
            audit(zero_cross_product=True)
        except AssertionError:
            result["negative_boundary_rejected"] = True
        else:
            raise SystemExit("negative boundary case was incorrectly accepted")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
