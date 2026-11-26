#!/usr/bin/env python3
"""Build the finite Lemma-5 sparse-polynomial table for a small exact-3-CNF."""

import argparse
import json
from pathlib import Path


def odd_primes(count):
    found, candidate = [], 3
    while len(found) < count:
        if all(candidate % p for p in range(2, int(candidate ** 0.5) + 1)):
            found.append(candidate)
        candidate += 2
    return found


def add(left, right):
    out = dict(left)
    for exponent, coefficient in right.items():
        out[exponent] = out.get(exponent, 0) + coefficient
        if not out[exponent]:
            del out[exponent]
    return out


def multiply(left, right):
    out = {}
    for a, ca in left.items():
        for b, cb in right.items():
            out[a + b] = out.get(a + b, 0) + ca * cb
    return {e: c for e, c in out.items() if c}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text())
    n = payload.get("variables")
    clauses = payload.get("clauses")
    shift = payload.get("shift", 0)
    if not isinstance(n, int) or n < 1 or not isinstance(clauses, list) or not clauses:
        parser.error("variables must be positive and clauses must be nonempty")
    if not isinstance(shift, int) or shift < 0:
        parser.error("shift must be a nonnegative integer")
    if any(not isinstance(c, list) or len(c) != 3 for c in clauses):
        parser.error("each clause must contain exactly three literals")
    if any(not isinstance(v, int) or v == 0 or abs(v) > n for c in clauses for v in c):
        parser.error("literal indices must be nonzero and in [-variables, variables]")
    primes = odd_primes(n)
    N = 1
    for q in primes:
        N *= q
    m = [N // q for q in primes]
    literal = {}
    for i, (q, mi) in enumerate(zip(primes, m), start=1):
        literal[i] = {mi: 1, 0: -1}
        literal[-i] = {r * mi: 1 for r in range(q)}
    S = {}
    for clause in clauses:
        C = {0: 1}
        for v in clause:
            C = multiply(C, literal[v])
        S = add(S, multiply(C, {-e: c for e, c in C.items()}))
    if not S:
        raise AssertionError("Lemma 5 predicts a nonzero S for valid input")
    d = max(abs(e) for e in S)
    A = {e + d: 3 * c for e, c in S.items()}
    F = add(A, {shift + N: 1, shift: -1})
    satisfying_residues = []
    for t in range(N):
        assignment = [(t * mi) % N == 0 for mi in m]
        sat = all(any(assignment[v - 1] if v > 0 else not assignment[-v - 1]
                      for v in clause) for clause in clauses)
        if sat:
            satisfying_residues.append(t)
    print(json.dumps({
        "odd_primes": primes,
        "N": N,
        "shift": shift,
        "A_terms": sorted(A.items()),
        "F_terms": sorted(F.items()),
        "satisfying_Nth_root_residues": satisfying_residues,
    }))


if __name__ == "__main__":
    main()
