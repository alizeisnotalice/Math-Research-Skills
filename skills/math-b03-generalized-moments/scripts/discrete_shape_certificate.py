#!/usr/bin/env python3
"""Exact finite certificates for discrete log-concavity and increasing failure rate.

Input JSON:
{
  "masses": ["32/53", "16/53", "4/53", "1/53"],
  "piece_budget": 2
}

All masses must be JSON integers or strings accepted by fractions.Fraction.  Indices in
the output are zero based.  `piece_budget` only tests the displayed candidate; it is never
an optimizer or a certificate that an optimum has this form.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


def rational(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("Boolean values are not rational numbers")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError("Each mass must be a JSON integer or a rational string such as '5/12'")


def show(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def local_gaps(values: list[Fraction]) -> list[Fraction]:
    return [values[i] * values[i] - values[i - 1] * values[i + 1] for i in range(1, len(values) - 1)]


def log_concavity_certificate(masses: list[Fraction], piece_budget: int | None) -> dict[str, Any]:
    positive = [index for index, value in enumerate(masses) if value > 0]
    nonnegative = all(value >= 0 for value in masses)
    left = positive[0] if positive else None
    right = positive[-1] if positive else None
    interval_support = bool(positive) and positive == list(range(left, right + 1))
    gaps = local_gaps(masses)
    lc = nonnegative and interval_support and all(gap >= 0 for gap in gaps)
    result: dict[str, Any] = {
        "positive_support_indices": positive,
        "support_is_nonempty_interval": interval_support,
        "local_log_concavity_gaps_xj_squared_minus_neighbors": [show(gap) for gap in gaps],
        "strict_log_concavity_break_indices": [index + 1 for index, gap in enumerate(gaps) if gap > 0],
        "is_log_concave": lc,
    }
    if not lc:
        result["piecewise_geometric"] = False
        result["piece_count"] = None
        result["message"] = "A piecewise-geometric decomposition is withheld because consecutive support or all log-concavity inequalities fail."
        return result
    assert left is not None and right is not None
    breaks = [index + 1 for index, gap in enumerate(gaps) if gap > 0 and left < index + 1 < right]
    boundaries = [left] + breaks + [right]
    pairs = [(left, right)] if left == right else list(zip(boundaries, boundaries[1:]))
    pieces: list[dict[str, Any]] = []
    for start, end in pairs:
        ratio = masses[start + 1] / masses[start] if end > start else None
        pieces.append({
            "left_index": start,
            "right_index": end,
            "common_ratio": None if ratio is None else show(ratio),
        })
    piece_count = len(pieces) if positive else 0
    result.update({
        "piecewise_geometric": True,
        "piece_boundaries_shared_between_adjacent_pieces": breaks,
        "geometric_pieces": pieces,
        "piece_count": piece_count,
        "piece_budget": piece_budget,
        "candidate_satisfies_piece_budget": None if piece_budget is None else piece_count <= piece_budget,
        "message": "Each listed piece has zero interior log-concavity gap, hence constant adjacent ratio exactly.",
    })
    return result


def ifr_certificate(masses: list[Fraction]) -> dict[str, Any]:
    tails = [sum(masses[index:], Fraction(0)) for index in range(len(masses))]
    tail_gaps = local_gaps(tails)
    positive_tail = [index for index, value in enumerate(tails) if value > 0]
    failure_rates = [masses[index] / tails[index] for index in positive_tail]
    nonnegative = all(value >= 0 for value in masses)
    tails_nonincreasing = all(tails[index] >= tails[index + 1] for index in range(len(tails) - 1))
    ifr = nonnegative and bool(positive_tail) and tails_nonincreasing and all(gap >= 0 for gap in tail_gaps)
    return {
        "tail_values": [show(value) for value in tails],
        "positive_tail_indices": positive_tail,
        "tail_is_nonincreasing": tails_nonincreasing,
        "tail_log_concavity_gaps_yj_squared_minus_neighbors": [show(gap) for gap in tail_gaps],
        "failure_rates_on_positive_tails": [show(value) for value in failure_rates],
        "failure_rates_nondecreasing": all(failure_rates[index] <= failure_rates[index + 1] for index in range(len(failure_rates) - 1)),
        "is_increasing_failure_rate": ifr,
        "equivalence_scope": "Finite nonnegative mass vector: positive-tail log-concavity is equivalent to nondecreasing discrete failure rates; trailing zero tails are omitted from the ratio list.",
    }


def analyze(raw: dict[str, Any]) -> dict[str, Any]:
    values = raw.get("masses")
    require(isinstance(values, list) and values, "masses must be a nonempty list")
    masses = [rational(value) for value in values]
    budget = raw.get("piece_budget")
    require(budget is None or (isinstance(budget, int) and not isinstance(budget, bool) and budget >= 0),
            "piece_budget must be a nonnegative integer when supplied")
    probability_valid = all(value >= 0 for value in masses) and sum(masses, Fraction(0)) == 1
    return {
        "arithmetic": "exact rational (fractions.Fraction)",
        "masses": [show(value) for value in masses],
        "total_mass": show(sum(masses, Fraction(0))),
        "is_probability_distribution": probability_valid,
        "log_concavity": log_concavity_certificate(masses, budget),
        "increasing_failure_rate": ifr_certificate(masses),
        "scope": "This certifies only the supplied finite mass vector. It does not optimize a moment problem or prove the source theorem's existence/optimality conclusion.",
    }


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON instance")
    parser.add_argument("-o", "--output", type=Path, help="write JSON output here instead of stdout")
    args = parser.parse_args(argv)
    try:
        raw = json.loads(args.input.read_text(encoding="utf-8"))
        require(isinstance(raw, dict), "top-level JSON value must be an object")
        result = analyze(raw)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "input_error", "message": str(error)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 2
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
