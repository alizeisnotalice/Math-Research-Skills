#!/usr/bin/env python3
"""Audit the exact one-layer identity in supp-14-esma-folding-transform."""

import json
import sys
from fractions import Fraction


def multiply(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def main():
    data = json.load(sys.stdin)
    keys = ("c", "d", "e", "f", "c_next", "e_next", "e_prev")
    missing = [key for key in keys if key not in data]
    if missing:
        raise SystemExit("missing keys: " + ", ".join(missing))
    values = {key: Fraction(data[key]) for key in keys}
    if values["e"] == 0 or values["e_next"] == 0 or values["e_prev"] == 0:
        raise SystemExit("e, e_next, and e_prev must be nonzero")
    c, d, e, f = (values[key] for key in ("c", "d", "e", "f"))
    cn, en, ep = (values[key] for key in ("c_next", "e_next", "e_prev"))
    raw = multiply(multiply([[e, -c], [0, 1]], [[c, d], [e, f]]),
                   [[1, cn], [0, en]])
    determinant = e * d - c * f
    expected_raw = [[0, en * determinant], [e, e * cn + f * en]]
    normalized = [[0, ep * en * determinant], [1, e * cn + f * en]]
    if raw != expected_raw:
        raise SystemExit("internal matrix identity failure")
    def show(matrix):
        return [[str(x) for x in row] for row in matrix]
    print(json.dumps({"raw": show(raw), "normalized": show(normalized),
                      "determinant_expression": str(determinant), "verified": True},
                     sort_keys=True))


if __name__ == "__main__":
    main()
