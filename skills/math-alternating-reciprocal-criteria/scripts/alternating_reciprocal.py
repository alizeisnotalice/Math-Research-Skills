#!/usr/bin/env python3
"""Exact finite checks for Sondow's alternating reciprocal criteria.

This program intentionally never claims that a finite input proves irrationality.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Sequence


def alternating_sum(denominators: Sequence[int]) -> Fraction:
    return sum(
        (Fraction(1, value) if index % 2 == 0 else Fraction(-1, value))
        for index, value in enumerate(denominators)
    )


def generalized_fraction(a: Sequence[int], b: Sequence[int]) -> Fraction:
    """Evaluate b[0]/(a[0]+b[1]/(a[1]+...)) exactly."""
    if len(a) != len(b) or not a:
        raise ValueError("a and b must be nonempty and have the same length")
    value = Fraction(b[-1], a[-1])
    for index in range(len(a) - 2, -1, -1):
        value = Fraction(b[index], 1) / (Fraction(a[index], 1) + value)
    return value


def type_i_data(values: Sequence[int]) -> dict[str, object]:
    if not values or any(value <= 0 for value in values):
        raise ValueError("type I requires at least one positive integer")
    a = [values[0]] + [values[i] - values[i - 1] for i in range(1, len(values))]
    b = [1] + [values[i - 1] ** 2 for i in range(1, len(values))]
    strictly_increasing = all(values[i] > values[i - 1] for i in range(1, len(values)))
    threshold_holds = all(
        values[i] >= values[i - 1] * (values[i - 1] + 1)
        for i in range(1, len(values))
    )
    partial = alternating_sum(values)
    fraction = generalized_fraction(a, b) if strictly_increasing else None
    return {
        "family": "type-I",
        "B": list(values),
        "partial_sum": str(partial),
        "continued_fraction": {"a": a, "b": b, "value": str(fraction) if fraction else None},
        "finite_identity_verified": fraction == partial if fraction else False,
        "strictly_increasing_on_checked_prefix": strictly_increasing,
        "threshold_holds_on_checked_prefix": threshold_holds,
        "infinite_conclusion": (
            "No arithmetic conclusion from a finite prefix. Prove both hypotheses for all n "
            "before invoking Proposition 1."
        ),
    }


def type_ii_data(values: Sequence[int]) -> dict[str, object]:
    if not values or values[0] <= 0 or any(value < 2 for value in values[1:]):
        raise ValueError("type II requires A0>0 and A_n>=2 for every supplied n>=1")
    products: list[int] = []
    product = 1
    for value in values:
        product *= value
        products.append(product)
    result = type_i_data(products)
    simple_a = [values[0]] + [value - 1 for value in values[1:]]
    simple_b = [1] + list(values[:-1])
    simple_fraction = generalized_fraction(simple_a, simple_b)
    result.update(
        {
            "family": "type-II",
            "A": list(values),
            "B_products": products,
            "type_ii_continued_fraction": {
                "a": simple_a,
                "b": simple_b,
                "value": str(simple_fraction),
                "finite_identity_verified": simple_fraction == alternating_sum(products),
            },
            "strict_growth_on_checked_prefix": all(
                values[i] > values[i - 1] for i in range(1, len(values))
            ),
            "infinite_conclusion": (
                "No arithmetic conclusion from a finite prefix. Theorem 1(ii) needs A_(n+1)>A_n "
                "for all n; Theorem 1(iii) additionally needs a global simple-CF equivalence."
            ),
        }
    )
    return result


def self_test() -> dict[str, object]:
    valid = type_i_data([1, 3, 15, 255])
    sharp_failure = type_i_data([2, 5, 29, 869])
    pierce = type_ii_data([2, 3, 4, 5])
    assert valid["finite_identity_verified"]
    assert valid["threshold_holds_on_checked_prefix"]
    assert sharp_failure["finite_identity_verified"]
    assert not sharp_failure["threshold_holds_on_checked_prefix"]
    assert pierce["finite_identity_verified"]
    assert pierce["type_ii_continued_fraction"]["finite_identity_verified"]
    assert pierce["strict_growth_on_checked_prefix"]
    return {
        "valid_type_i": valid,
        "sharp_boundary": {
            "checked_prefix": sharp_failure,
            "infinite_definition": "B_(n+1)+1=B_n(B_n+1), B_0=2",
            "exact_infinite_sum": "1/3",
            "interpretation": "The Proposition 1 threshold fails; this source-provided family is rational.",
        },
        "type_ii": pierce,
        "status": "all exact finite identity and gate tests passed",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", nargs="?", choices=("type-i", "type-ii"))
    parser.add_argument("values", nargs="*", type=int)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        output = self_test()
    elif args.mode == "type-i":
        output = type_i_data(args.values)
    elif args.mode == "type-ii":
        output = type_ii_data(args.values)
    else:
        parser.error("provide --self-test or a mode followed by integer values")
        return
    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
