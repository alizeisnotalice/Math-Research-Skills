#!/usr/bin/env python3
"""Exact finite clause-collision probability for with-replacement k-SAT."""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction


def collision_free_probability(variables: int, clause_size: int, clauses: int) -> Fraction:
    """Return P(NC)=((n)_k/n**k)**m, checking n >= k >= 1 and m >= 0."""
    if isinstance(variables, bool) or isinstance(clause_size, bool) or isinstance(clauses, bool):
        raise ValueError("parameters must be integer values, not booleans")
    if not all(isinstance(value, int) for value in (variables, clause_size, clauses)):
        raise ValueError("variables, clause_size, and clauses must be integers")
    if clause_size < 1:
        raise ValueError("clause_size must be at least 1")
    if variables < clause_size:
        raise ValueError("variables must be at least clause_size")
    if clauses < 0:
        raise ValueError("clauses must be nonnegative")
    falling = 1
    for offset in range(clause_size):
        falling *= variables - offset
    return Fraction(falling, variables**clause_size) ** clauses


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON file with variables, clause_size, clauses; use - for stdin")
    args = parser.parse_args()
    data = json.load(sys.stdin if args.input == "-" else open(args.input, encoding="utf-8"))
    if set(data) != {"variables", "clause_size", "clauses"}:
        raise ValueError("input keys must be exactly variables, clause_size, clauses")
    value = collision_free_probability(data["variables"], data["clause_size"], data["clauses"])
    print(json.dumps({
        "variables": data["variables"],
        "clause_size": data["clause_size"],
        "clauses": data["clauses"],
        "no_collision_probability": str(value),
        "conditional_model": "independent uniform proper signed k-clauses",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
