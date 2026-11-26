#!/usr/bin/env python3
"""A strict rational Euler–Mascheroni enclosure from positive Newton terms."""

import argparse
from fractions import Fraction
import json
from math import factorial


def coefficient(n: int) -> Fraction:
    if n < 2:
        raise ValueError("the Newton index must be at least 2")
    return factorial(n - 2) * sum(
        (Fraction((-1) ** (k + 1), factorial(n - k) * k**k) for k in range(1, n + 1)),
        Fraction(),
    )


def enclosure(through: int) -> tuple[Fraction, Fraction]:
    if through < 2:
        raise ValueError("--through must be at least 2")
    lower = -1 + sum((coefficient(n) for n in range(2, through + 1)), Fraction())
    return lower, lower + Fraction(4, through)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", required=True, type=int)
    args = parser.parse_args()
    try:
        lower, upper = enclosure(args.through)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps({"through": args.through, "strict_lower": str(lower),
                      "strict_upper": str(upper), "width": str(upper - lower)}))


if __name__ == "__main__":
    main()
