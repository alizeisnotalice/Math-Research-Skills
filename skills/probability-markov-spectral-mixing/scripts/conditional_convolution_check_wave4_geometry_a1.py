#!/usr/bin/env python3
"""Exact finite diagnostic for the algebraic side of Lemma 5.1-style convolution bounds."""

import argparse
import json
from fractions import Fraction
from pathlib import Path


def q(value):
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    if isinstance(value, list) and len(value) == 2:
        return Fraction(value[0], value[1])
    raise ValueError("rational values must be integers, strings, or [numerator, denominator]")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        d = json.loads(args.input.read_text())
        K = d["K"]
        if not isinstance(K, int) or K < 1:
            raise ValueError("K must be a positive integer")
        A, B = [q(x) for x in d["A"]], [q(x) for x in d["B"]]
        if len(A) != 2 * K + 1 or len(B) != 2 * K + 1:
            raise ValueError("A and B must be indexed from -K through K")
        event_probability, epsilon, eta, sqrt_delta = (q(d[x]) for x in ("event_probability", "epsilon", "eta", "sqrt_delta"))
        if not (0 <= event_probability <= 1 and epsilon >= 0 and eta >= 0 and sqrt_delta >= 0):
            raise ValueError("probability and bound parameters must be nonnegative, with probability at most one")
    except (KeyError, TypeError, ValueError, ZeroDivisionError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    def get(values, index):
        return values[index + K] if -K <= index <= K else Fraction(0)

    coefficients = [sum((get(A, v) * get(B, -n - v) for v in range(-K, K + 1)), Fraction(0)) for n in range(2 * K + 1)]
    truncated_l1 = sum((abs(x) for x in coefficients), Fraction(0))
    left = event_probability * epsilon
    right = (2 * K + 1) * (eta + 2 * sqrt_delta)
    print(json.dumps({
        "K": K,
        "coefficients_n_0_to_2K": [str(x) for x in coefficients],
        "truncated_l1": str(truncated_l1),
        "claimed_lower_side": str(left),
        "claimed_upper_side": str(right),
        "inequality_holds": left <= right,
        "scope": "Checks only finite algebraic convolution data; conditional tail hypotheses are external.",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
