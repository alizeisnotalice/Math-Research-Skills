#!/usr/bin/env python3
"""Exact finite consistency check for the conditional Lemma 3.2 interface."""

from __future__ import annotations

import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path


def fail(message: str) -> None:
    raise ValueError(message)


def exact_fraction(value: object, field: str) -> Fraction:
    if not isinstance(value, str):
        fail(f"{field} must be an exact rational string, not a number")
    try:
        answer = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"{field} is not a rational string: {value!r}") from exc
    if answer < 0:
        fail(f"{field} must be non-negative")
    return answer


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: check_purity_lfactor.py CERTIFICATE.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
        q = data["residue_cardinality"]
        if not isinstance(q, int) or isinstance(q, bool) or q < 2:
            fail("residue_cardinality must be an integer at least 2")
        if data.get("kernel_inertia_in_m0") is not True:
            fail("kernel_inertia_in_m0 must be true: the external WD inclusion is required")
        records = data["graded_spectrum"]
        if not isinstance(records, list) or not records:
            fail("graded_spectrum must be a nonempty list")

        labels: list[str] = []
        degree_by_label: dict[str, int] = {}
        degree_counts: Counter[int] = Counter()
        for index, record in enumerate(records):
            if not isinstance(record, dict):
                fail(f"graded_spectrum[{index}] must be an object")
            label = record.get("label")
            degree = record.get("degree")
            if not isinstance(label, str) or not label:
                fail(f"graded_spectrum[{index}].label must be a nonempty string")
            if label in degree_by_label:
                fail(f"graded_spectrum labels must be unique; duplicate {label!r}")
            if not isinstance(degree, int) or isinstance(degree, bool):
                fail(f"graded_spectrum[{index}].degree must be an integer")
            modulus_squared = exact_fraction(record.get("modulus_squared"),
                                             f"graded_spectrum[{index}].modulus_squared")
            expected = Fraction(q) ** degree
            if modulus_squared != expected:
                fail(f"{label}: modulus_squared={modulus_squared} != Q^degree={expected}")
            labels.append(label)
            degree_by_label[label] = degree
            degree_counts[degree] += 1

        for degree, count in degree_counts.items():
            if count != degree_counts[-degree]:
                fail(f"monodromy symmetry fails in degree {degree}: {count} != {degree_counts[-degree]}")

        requested = data.get("local_factor_labels")
        if not isinstance(requested, list):
            fail("local_factor_labels must be a list")
        available = Counter(labels)
        used = Counter()
        for label in requested:
            if not isinstance(label, str):
                fail("local_factor_labels entries must be strings")
            used[label] += 1
            if used[label] > available[label]:
                fail(f"local factor uses {label!r} more often than supplied graded spectrum")
            degree = degree_by_label[label]
            if degree > 0:
                fail(f"local-factor eigenvalue {label!r} has positive degree {degree}, not in M_0")

        print(f"PASS: Q={q}; {len(records)} pure graded eigenvalues; "
              f"{len(requested)} local-factor eigenvalues all have degree <= 0.")
        print("CONCLUSION (conditional): L(s) is holomorphic and nonzero for Re(s)>0; |det Fr|=1.")
        return 0
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"REJECT: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
