#!/usr/bin/env python3
"""Check the finite residue certificate used by a lattice-covering argument."""

from __future__ import annotations

from itertools import product
import json
from pathlib import Path
import sys


def check(data: dict) -> dict:
    modulus = data["modulus"]
    weight = data["weight"]
    threshold = data["threshold"]
    if not isinstance(modulus, int) or modulus < 2:
        raise ValueError("modulus must be an integer at least two")
    if not weight or not all(isinstance(value, int) for value in weight):
        raise ValueError("weight must be a nonempty integer vector")
    if not isinstance(threshold, int):
        raise ValueError("threshold must be an integer")

    def score(residue: tuple[int, ...], shift: int) -> int:
        return sum((value + shift * coefficient) % modulus
                   for value, coefficient in zip(residue, weight))

    minima = [min(score(residue, shift) for shift in range(modulus))
              for residue in product(range(modulus), repeat=len(weight))]
    maximum = max(minima)
    result = {
        "modulus": modulus,
        "dimension": len(weight),
        "residues_checked": modulus ** len(weight),
        "maximum_minimum_score": maximum,
        "threshold": threshold,
        "certificate_holds": maximum <= threshold,
    }
    if "witness" in data:
        witness = tuple(data["witness"])
        if len(witness) != len(weight) or not all(isinstance(value, int) for value in witness):
            raise ValueError("witness must be an integer vector of the stated dimension")
        values = [score(witness, shift) for shift in range(modulus)]
        result["witness_scores"] = values
        result["witness_minimum_score"] = min(values)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_residue_cover.py INPUT.json")
    print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())), sort_keys=True))
