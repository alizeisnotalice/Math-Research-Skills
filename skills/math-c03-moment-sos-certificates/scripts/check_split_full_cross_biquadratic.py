#!/usr/bin/env python3
"""Check an exact two-Gram SOS certificate for a split full-cross form."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import sys


def rational(value: object) -> Fraction:
    return Fraction(str(value))


def psd_two_by_two(left: Fraction, cross: Fraction, right: Fraction) -> bool:
    return left >= 0 and right >= 0 and left * right - cross * cross >= 0


def check(document: dict[str, object]) -> dict[str, object]:
    coefficients = document["coefficients"]
    split = document["split"]
    if not isinstance(coefficients, dict) or not isinstance(split, dict):
        raise ValueError("coefficients and split must be objects")
    keys = ("a11", "a12", "a21", "a22", "b")
    if set(coefficients) != set(keys) or set(split) != {"b_uz", "b_vw"}:
        raise ValueError("unexpected coefficient or split keys")
    a11, a12, a21, a22, b = (rational(coefficients[key]) for key in keys)
    b_uz, b_vw = (rational(split[key]) for key in ("b_uz", "b_vw"))
    if b != b_uz + b_vw:
        raise ValueError("the split does not reconstruct b")
    first_cross, second_cross = -b_uz / 2, -b_vw / 2
    if not psd_two_by_two(a11, first_cross, a22):
        raise ValueError("the (x1y1,x2y2) Gram matrix is not PSD")
    if not psd_two_by_two(a12, second_cross, a21):
        raise ValueError("the (x1y2,x2y1) Gram matrix is not PSD")
    return {
        "status": "verified-split-full-cross-biquadratic-sos",
        "gram_uz": [[str(a11), str(first_cross)], [str(first_cross), str(a22)]],
        "gram_vw": [[str(a12), str(second_cross)], [str(second_cross), str(a21)]],
        "reconstructed_cross_coefficient": str(-(b_uz + b_vw)),
        "not_certified": "general biquadratic PSD or SOS, an automatically found split, or a rational square-factor list",
    }


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_split_full_cross_biquadratic.py INPUT.json")
    try:
        result = check(json.loads(Path(sys.argv[1]).read_text()))
    except (KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        print(json.dumps({"status": "rejected", "reason": str(error)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
