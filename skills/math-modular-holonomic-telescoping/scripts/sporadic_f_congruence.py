#!/usr/bin/env python3
"""Check Kazalicki's finite congruence for the (17,6,72) sequence.

The checker implements the published theorem's explicit CM branch only.  It
does not construct the modular form or prove the ASD congruence behind it.
"""

from __future__ import annotations

import json
from math import comb, isqrt
from pathlib import Path
import sys


def prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1 if divisor == 2 else 2
    return True


def sporadic_value(index: int) -> int:
    return sum(
        (-1) ** k * 8 ** (index - k) * comb(index, k)
        * sum(comb(k, j) ** 3 for j in range(k + 1))
        for k in range(index + 1)
    )


def cm_coefficient(modulus: int) -> tuple[int, tuple[int, int] | None]:
    """Return gamma(p) for the CM branch and one representation if present."""
    if modulus % 24 in {5, 11}:
        raise ValueError("the published CM formula does not cover p == 5 or 11 mod 24")
    for b in range(1, isqrt(modulus // 6) + 1):
        remainder = modulus - 6 * b * b
        a = isqrt(remainder)
        if a * a == remainder:
            return 2 * (a * a - 6 * b * b), (a, b)
    return 0, None


def check(modulus: int) -> dict[str, object]:
    if type(modulus) is not int or modulus <= 3 or not prime(modulus):
        raise ValueError("p must be a prime greater than 3")
    gamma, representation = cm_coefficient(modulus)
    index = (modulus - 1) // 2
    value = sporadic_value(index)
    return {
        "prime": modulus,
        "index": index,
        "F_index": value,
        "gamma_p": gamma,
        "representation_p_equals_a2_plus_6b2": list(representation) if representation else None,
        "F_mod_p": value % modulus,
        "gamma_mod_p": gamma % modulus,
        "congruent": value % modulus == gamma % modulus,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: sporadic_f_congruence.py INPUT.json", file=sys.stderr)
        return 2
    try:
        payload = json.loads(Path(sys.argv[1]).read_text())
        result = check(payload["p"])
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["congruent"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
