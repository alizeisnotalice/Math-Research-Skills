#!/usr/bin/env python3
"""Check the index weights in the explicit weight-(2q+1) F_q MZV relation."""

from __future__ import annotations

import argparse
import json


def is_prime_power(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value and value % divisor:
        divisor += 1 if divisor == 2 else 2
    if divisor * divisor > value:
        return True
    while value % divisor == 0:
        value //= divisor
    return value == 1


def relation_indices(q: int) -> list[tuple[int, ...]]:
    return [
        (q + 2, q - 1), (3, 2 * q - 2), (q, 2, q - 1),
        (1, q, q), (1, 1, 2 * q - 1), (1, q - 1, 1, q),
        (q + 1, 1, q - 1), (2, q - 1, 1, q - 1),
        (2, q, q - 1), (2, 1, 2 * q - 2),
        (q, 1, 1, q - 1), (1, 1, q - 1, q),
    ]


def check(q: int) -> dict[str, object]:
    if not is_prime_power(q):
        raise ValueError("q must be a prime power at least 2")
    terms = relation_indices(q)
    target = 2 * q + 1
    if not all(all(entry > 0 for entry in term) and sum(term) == target for term in terms):
        raise AssertionError("the displayed relation has an invalid index")
    return {
        "q": q,
        "threshold_weight": target,
        "independence_range": f"weights < {target}",
        "displayed_relation_term_count": len(terms),
        "all_displayed_terms_have_target_weight": True,
        "indices": [list(term) for term in terms],
        "scope": "This checks index weights only; the F_q-linear relation and independence theorem remain source theorems.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q", type=int)
    args = parser.parse_args()
    try:
        print(json.dumps(check(args.q), ensure_ascii=False, sort_keys=True))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
