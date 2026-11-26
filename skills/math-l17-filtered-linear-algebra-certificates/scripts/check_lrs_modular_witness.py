#!/usr/bin/env python3
"""Exact finite verification for a modular nonzero witness of an integer LRS.

Input JSON: {"modulus": m, "coefficients": [a0,...,a_{d-1}],
"initial": [u0,...,u_{d-1}]}.  It enumerates the companion states modulo m
until repetition and reports whether every term in the resulting orbit is nonzero.
"""
import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_lrs_modular_witness.py INPUT.json")
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        m = data["modulus"]
        coeffs, initial = data["coefficients"], data["initial"]
        if type(m) is not int or m < 2:
            raise ValueError("require an integer modulus >= 2")
        if not isinstance(coeffs, list) or not isinstance(initial, list) or not coeffs or len(initial) != len(coeffs):
            raise ValueError("require equally sized nonempty coefficients and initial arrays")
        if any(type(x) is not int for x in coeffs + initial):
            raise ValueError("coefficients and initial entries must be integers")
    except (OSError, KeyError, TypeError, ValueError) as error:
        print(json.dumps({"error": str(error)}))
        raise SystemExit(2) from error
    state = tuple(x % m for x in initial)
    coeffs = tuple(x % m for x in coeffs)
    seen = {}
    terms = []
    while state not in seen:
        seen[state] = len(terms)
        terms.append(state[0])
        state = state[1:] + (sum(a * b for a, b in zip(coeffs, state)) % m,)
    start = seen[state]
    zeros = [i for i, value in enumerate(terms) if value == 0]
    print(json.dumps({"states_checked": len(terms), "preperiod": start,
                      "period": len(terms) - start, "zero_indices_in_orbit": zeros,
                      "nonzero_witness": not zeros}, sort_keys=True))
    if zeros:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
