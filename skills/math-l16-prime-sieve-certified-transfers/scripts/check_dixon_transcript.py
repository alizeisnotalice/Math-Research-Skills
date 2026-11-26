#!/usr/bin/env python3
"""Compute exact CRT split probabilities for supplied square-root transcripts."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd, prod
from pathlib import Path

from audit_supplied_exponent_split import is_prime_trial


def integer(value: object, label: str) -> int:
    if type(value) is not int:
        raise ValueError(f"{label} must be an integer")
    return value


def rank_f2(rows: list[int]) -> int:
    pivots = {}
    for row in rows:
        while row:
            column = row.bit_length()
            if column not in pivots:
                pivots[column] = row
                break
            row ^= pivots[column]
    return len(pivots)


def check(data: object) -> dict[str, object]:
    if not isinstance(data, dict):
        raise ValueError("input must be an object")
    n = integer(data.get("n"), "n")
    factors = data.get("prime_powers")
    if not isinstance(factors, list) or len(factors) < 2:
        raise ValueError("supply at least two distinct odd prime powers of n")
    powers = {}
    for pair in factors:
        if not isinstance(pair, list) or len(pair) != 2:
            raise ValueError("each prime power must be a [prime, exponent] pair")
        prime, exponent = (integer(pair[0], "prime"), integer(pair[1], "exponent"))
        if prime <= 2 or prime in powers or not is_prime_trial(prime):
            raise ValueError("prime bases must be distinct odd primes")
        if not 1 <= exponent <= n.bit_length():
            raise ValueError("prime exponent outside the possible range for n")
        powers[prime] = prime**exponent
    moduli = list(powers.values())
    if prod(moduli) != n:
        raise ValueError("supplied prime powers must multiply to n")
    raw_roots = data.get("reference_roots")
    if not isinstance(raw_roots, list) or not raw_roots:
        raise ValueError("supply at least one reference root")
    roots = [integer(value, "reference root") % n for value in raw_roots]
    if any(gcd(root, n) != 1 for root in roots):
        raise ValueError("all reference roots must be units")
    trials = data.get("trials")
    if not isinstance(trials, list) or not trials:
        raise ValueError("supply at least one trial")
    masks = []
    offsets = []
    for trial in trials:
        if not isinstance(trial, dict) or not isinstance(trial.get("indices"), list):
            raise ValueError("each trial must have a list of root indices")
        indices = [integer(index, "root index") for index in trial["indices"]]
        if not indices or len(set(indices)) != len(indices) or any(not 0 <= i < len(roots) for i in indices):
            raise ValueError("trial indices must be nonempty, distinct and in range")
        reference = prod(roots[index] for index in indices) % n
        target = integer(trial.get("target"), "target") % n
        if pow(reference, 2, n) != pow(target, 2, n):
            raise ValueError("target square does not equal the selected square product")
        ratio = target * pow(reference, -1, n) % n
        offsets.append([int(ratio % modulus == modulus - 1) for modulus in moduli])
        masks.append(sum(1 << index for index in indices))
    rank = rank_f2(masks)
    augmented_ranks = []
    for coordinate in range(1, len(moduli)):
        augmented = [
            mask | ((bits[0] ^ bits[coordinate]) << len(roots))
            for mask, bits in zip(masks, offsets, strict=True)
        ]
        augmented_ranks.append(rank_f2(augmented))
    failure_probability = (
        Fraction(1, 2**(rank * (len(moduli) - 1)))
        if all(augmented_rank == rank for augmented_rank in augmented_ranks)
        else Fraction(0)
    )
    return {
        "mask_rank": rank,
        "augmented_ranks": augmented_ranks,
        "single_trial_split_probability": str(1 - Fraction(1, 2**(len(moduli) - 1))),
        "all_trials_fail_probability": str(failure_probability),
        "some_trial_splits_probability": str(1 - failure_probability),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = check(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
