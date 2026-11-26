#!/usr/bin/env python3
"""Compute exact rational enclosures for the Sondow--Zudilin q-logarithm.

The series is ln_q(1+z) = sum_{mu>=1} (-1)^(mu-1) z^mu/(q^mu-1).
For integral q >= 2 and rational 0 <= z < q, its terms decrease in
absolute value.  This program therefore uses adjacent partial sums as an
exact enclosure.  It also applies Lemma 1 of arXiv:math/0304021v1 to a
geometric-index reciprocal tail.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction


def parse_fraction(text: str) -> Fraction:
    try:
        return Fraction(text)
    except (ValueError, ZeroDivisionError) as error:
        raise argparse.ArgumentTypeError(f"invalid rational number {text!r}") from error


def require_q_and_z(q: int, z: Fraction) -> None:
    if q < 2:
        raise ValueError("q must be an integer at least 2")
    if z < 0 or z >= q:
        raise ValueError("require 0 <= z < q for the alternating-series enclosure")


def partial_sum(q: int, z: Fraction, terms: int) -> Fraction:
    if terms < 0:
        raise ValueError("terms must be nonnegative")
    value = Fraction()
    power = Fraction(1)
    for index in range(1, terms + 1):
        power *= z
        term = power / (q**index - 1)
        value += term if index % 2 else -term
    return value


def q_log_bounds(q: int, z: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    """Return closed rational bounds using consecutive alternating partial sums."""
    require_q_and_z(q, z)
    if terms < 1:
        raise ValueError("terms must be positive")
    first = partial_sum(q, z, terms)
    index = terms + 1
    next_term = z**index / (q**index - 1)
    second = first + (next_term if index % 2 else -next_term)
    return min(first, second), max(first, second)


def reciprocal_tail_bounds(q: int, n: int, k: int, terms: int) -> tuple[Fraction, Fraction]:
    """Enclose sum_{nu=n+1}^infinity 1/(q^nu+k) by Lemma 1."""
    if q < 2 or terms < 1:
        raise ValueError("require integer q >= 2 and positive terms")
    if n < 0:
        raise ValueError("n must be nonnegative")
    if k < 0:
        raise ValueError("k must be nonnegative")
    if k == 0:
        exact = Fraction(1, q**n * (q - 1))
        return exact, exact
    if k >= q ** (n + 1):
        raise ValueError("Lemma 1 requires 0 < k < q**(n+1)")
    lower, upper = q_log_bounds(q, Fraction(k, q**n), terms)
    return lower / k, upper / k


def emit(payload: dict[str, object]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    log_parser = subparsers.add_parser("q-log", help="enclose ln_q(1+z)")
    log_parser.add_argument("--q", type=int, required=True)
    log_parser.add_argument("--z", type=parse_fraction, required=True)
    log_parser.add_argument("--terms", type=int, default=12)

    tail_parser = subparsers.add_parser("geometric-tail", help="enclose a Lemma 1 reciprocal tail")
    tail_parser.add_argument("--q", type=int, required=True)
    tail_parser.add_argument("--n", type=int, required=True)
    tail_parser.add_argument("--k", type=int, required=True)
    tail_parser.add_argument("--terms", type=int, default=12)

    arguments = parser.parse_args()
    try:
        if arguments.command == "q-log":
            lower, upper = q_log_bounds(arguments.q, arguments.z, arguments.terms)
            emit({"object": "ln_q(1+z)", "q": arguments.q, "z": str(arguments.z),
                  "terms": arguments.terms, "lower": str(lower), "upper": str(upper),
                  "domain": "integer q >= 2, rational 0 <= z < q"})
        else:
            lower, upper = reciprocal_tail_bounds(arguments.q, arguments.n, arguments.k, arguments.terms)
            emit({"object": "sum_{nu=n+1}^infinity 1/(q^nu+k)", "q": arguments.q,
                  "n": arguments.n, "k": arguments.k, "terms": arguments.terms,
                  "lower": str(lower), "upper": str(upper),
                  "identity": "Lemma 1: ln_q(1+k/q^n)/k for k > 0"})
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
