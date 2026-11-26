#!/usr/bin/env python3
"""Exact finite replay of the Ryser witness used in vp-vnp/Paper/Ryser.lean.

This is deliberately a bounded check: it expands the n=1,...,4 instances in
Z[x_{ij}], not the claimed VP--VNP lower bound or a Lean proof.
"""

from collections import Counter
from hashlib import sha256


def ryser_coefficients(n: int) -> Counter[tuple[int, ...]]:
    """Return coefficients of sum_S (-1)^(n-|S|) prod_i sum_(j in S) x_ij.

    A monomial is encoded by (f(0), ..., f(n-1)), meaning prod_i x_(i,f(i)).
    All arithmetic is over Python integers, hence exact.
    """
    result: Counter[tuple[int, ...]] = Counter()
    for mask in range(1 << n):
        selected = tuple(j for j in range(n) if (mask >> j) & 1)
        sign = -1 if (n - len(selected)) % 2 else 1
        # Expanding one summand chooses a selected column independently per row.
        partial = [()]
        for _row in range(n):
            partial = [monomial + (column,) for monomial in partial for column in selected]
        for monomial in partial:
            result[monomial] += sign
    return Counter({monomial: coefficient for monomial, coefficient in result.items() if coefficient})


def permanent_coefficients(n: int) -> Counter[tuple[int, ...]]:
    """The permanent's coefficient dictionary in the same monomial encoding."""
    from itertools import permutations
    return Counter({permutation: 1 for permutation in permutations(range(n))})


def digest(coefficients: Counter[tuple[int, ...]]) -> str:
    payload = "\n".join(
        f"{','.join(map(str, monomial))}:{coefficient}"
        for monomial, coefficient in sorted(coefficients.items())
    ).encode("ascii")
    return sha256(payload).hexdigest()


if __name__ == "__main__":
    for n in range(1, 5):
        ryser = ryser_coefficients(n)
        permanent = permanent_coefficients(n)
        assert ryser == permanent
        print(
            f"n={n} subsets={1 << n} ambient_functions={n ** n} "
            f"nonzero_monomials={len(ryser)} digest={digest(ryser)}"
        )
