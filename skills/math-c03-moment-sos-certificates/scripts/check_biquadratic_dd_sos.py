#!/usr/bin/env python3
"""Produce an exact SOS certificate for a diagonally-dominant biquadratic form."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


PACKAGE = Path(__file__).resolve().parents[1]


def exact(value: Any) -> Fraction:
    """Parse only exact JSON coefficient representations."""
    if isinstance(value, bool) or isinstance(value, float) or not isinstance(value, (int, str)):
        raise ValueError("each matrix entry must be an integer or a rational string")
    return Fraction(value)


def load_matrix(value: Any, order: int) -> list[list[Fraction]]:
    if not isinstance(value, list) or len(value) != order:
        raise ValueError("matrix must have exactly m*n rows")
    result: list[list[Fraction]] = []
    for row in value:
        if not isinstance(row, list) or len(row) != order:
            raise ValueError("matrix must be square of order m*n")
        result.append([exact(entry) for entry in row])
    return result


def coordinates(index: int, n: int) -> tuple[int, int]:
    return divmod(index, n)


def certificate(payload: dict[str, Any]) -> dict[str, Any]:
    m, n = payload.get("m"), payload.get("n")
    if not isinstance(m, int) or isinstance(m, bool) or m < 1:
        raise ValueError("m must be a positive integer")
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")
    order = m * n
    gram = load_matrix(payload.get("matrix"), order)

    for p in range(order):
        i, j = coordinates(p, n)
        for q in range(order):
            k, ell = coordinates(q, n)
            if gram[p][q] != gram[q][p]:
                raise ValueError(f"matrix is not symmetric at ({p}, {q})")
            # In tensor notation: a_ijkl = a_kjil.  Together with symmetry of
            # the Gram matrix this checks the two equalities in Theorem 2.1.
            internal_left, internal_right = k * n + j, i * n + ell
            if gram[p][q] != gram[internal_left][internal_right]:
                raise ValueError("matrix does not satisfy a_ijkl = a_kjil")

    slack: list[Fraction] = []
    for p, row in enumerate(gram):
        if row[p] < 0:
            raise ValueError(f"diagonal entry {p} is negative")
        remainder = row[p] - sum(abs(row[q]) for q in range(order) if q != p)
        if remainder < 0:
            raise ValueError(f"row {p} is not diagonally dominant")
        slack.append(remainder)

    terms: list[dict[str, int | str]] = []
    for p, weight in enumerate(slack):
        if weight:
            terms.append({"weight": str(weight), "left": p, "right": p, "sign": 1})
    for p in range(order):
        for q in range(p + 1, order):
            entry = gram[p][q]
            if entry:
                terms.append({
                    "weight": str(abs(entry)), "left": p, "right": q,
                    "sign": 1 if entry > 0 else -1,
                })

    reconstructed = [[Fraction(0) for _ in range(order)] for _ in range(order)]
    for term in terms:
        weight = Fraction(str(term["weight"]))
        left, right, sign = int(term["left"]), int(term["right"]), int(term["sign"])
        if left == right:
            reconstructed[left][left] += weight
        else:
            reconstructed[left][left] += weight
            reconstructed[right][right] += weight
            reconstructed[left][right] += weight * sign
            reconstructed[right][left] += weight * sign
    if reconstructed != gram:
        raise AssertionError("reported SOS terms fail exact Gram reconstruction")

    return {
        "status": "verified-symmetric-dd-biquadratic-sos",
        "m": m,
        "n": n,
        "coefficient_order": "matrix[i*n+j][k*n+l] = a_ijkl",
        "diagonal_slack": [str(value) for value in slack],
        "bilinear_square_terms": terms,
        "square_terms_reconstruct_gram": True,
        "identity": (
            "B(x,y)=sum weight*(x_i*y_j + sign*x_k*y_l)^2; "
            "a term with left=right means weight*(x_i*y_j)^2"
        ),
        "scope": "only the supplied exact symmetric diagonally-dominant coefficient tensor",
        "not_certified": (
            "arbitrary PSD or SOS biquadratic forms; M-biquadratic/B0-biquadratic "
            "conjectures; general moment/SOS hierarchies"
        ),
    }


def replay() -> int:
    positive = PACKAGE / "examples" / "biquadratic-dd-positive.json"
    rejected = PACKAGE / "examples" / "rejected-not-dd.json"
    accepted = certificate(json.loads(positive.read_text(encoding="utf-8")))
    if accepted["status"] != "verified-symmetric-dd-biquadratic-sos":
        raise AssertionError("positive fixture did not verify")
    try:
        certificate(json.loads(rejected.read_text(encoding="utf-8")))
    except ValueError as error:
        if "not diagonally dominant" not in str(error):
            raise
    else:
        raise AssertionError("non-DD rejection fixture unexpectedly verified")
    print(json.dumps({"status": "self-test-passed", "positive": positive.name,
                      "rejected": rejected.name}, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path, help="exact JSON certificate input")
    parser.add_argument("--self-test", action="store_true", help="replay acceptance and rejection fixtures")
    args = parser.parse_args()
    if args.self_test:
        if args.input is not None:
            parser.error("--self-test takes no input file")
        return replay()
    if args.input is None:
        parser.error("an input JSON file is required unless --self-test is used")
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        print(json.dumps(certificate(payload), ensure_ascii=False, indent=2))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "rejected", "reason": str(error)}, ensure_ascii=False))
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
