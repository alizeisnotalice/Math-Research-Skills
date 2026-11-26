#!/usr/bin/env python3
"""Certified finite augmented-CTMC exit/occupation bounds by uniformization.

The input is deliberately an *augmented finite* killed chain.  A user who has
truncated a larger CTMC must send every transition from the retained states to
the omitted part to the distinguished absorbing ``loss_state``.  Thus this
program never treats discarded mass as a physical exit.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


def frac(value: Any) -> Fraction:
    """Parse an exact JSON integer/string/rational, rejecting binary floats."""
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("all numerical inputs must be integer or rational strings, not float")
    try:
        return Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"invalid rational input: {value!r}") from exc


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def interval(lo: Fraction, hi: Fraction, digits: int) -> dict[str, str]:
    if lo < 0 or hi < lo:
        raise AssertionError("invalid interval")
    with localcontext() as ctx:
        ctx.prec = digits + 12
        return {
            "lower": fstr(lo),
            "upper": fstr(hi),
            "lower_decimal": format(Decimal(lo.numerator) / Decimal(lo.denominator), f".{digits}g"),
            "upper_decimal": format(Decimal(hi.numerator) / Decimal(hi.denominator), f".{digits}g"),
        }


def add(a: Iterable[Fraction]) -> Fraction:
    return sum(a, Fraction(0))


def matvec(vector: list[Fraction], matrix: list[list[Fraction]]) -> list[Fraction]:
    size = len(vector)
    return [add(vector[row] * matrix[row][column] for row in range(size)) for column in range(size)]


def alternating_exp_neg_interval(x: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    """Return rational L,U with L <= exp(-x) <= U for x >= 0.

    We write x=k*y with 0<=y<=1.  The odd/even Taylor partial sums of
    exp(-y) bracket it, then preserve the order by raising nonnegative bounds
    to k.  ``terms`` is the number of paired Taylor refinements.
    """
    if x < 0 or terms < 1:
        raise ValueError("x must be nonnegative and exp_terms at least 1")
    if x == 0:
        return Fraction(1), Fraction(1)
    k = max(1, (x.numerator + x.denominator - 1) // x.denominator)
    y = x / k
    partial = Fraction(1)
    power = Fraction(1)
    lower = upper = None
    # Odd partial sum is a lower bound; the following even one is an upper bound.
    for j in range(1, 2 * terms + 3):
        power *= y / j
        partial = partial - power if j % 2 else partial + power
        if j == 2 * terms + 1:
            lower = partial
        if j == 2 * terms + 2:
            upper = partial
    assert lower is not None and upper is not None and 0 < lower <= upper
    return lower**k, upper**k


def factorial(n: int) -> int:
    return math.factorial(n)


def raw_poisson_tail_upper(y: Fraction, terms: int) -> Fraction:
    """Bound sum_{n>terms} y^n/n! using a geometric majorant."""
    if y == 0:
        return Fraction(0)
    if terms + 2 <= y:
        raise ValueError("terms is too small: require terms + 2 > lambda*time")
    first = y ** (terms + 1) / factorial(terms + 1)
    ratio = y / (terms + 2)
    return first / (1 - ratio)


def nonnegative(value: Fraction, message: str) -> None:
    if value < 0:
        raise ValueError(message)


def parse_model(payload: dict[str, Any]) -> tuple[list[str], list[list[Fraction]], list[Fraction], Fraction, list[int], list[int], int, Fraction, int, int, int]:
    if not isinstance(payload, dict):
        raise ValueError("input must be a JSON object")
    labels = payload.get("state_labels")
    if not isinstance(labels, list) or not labels or not all(isinstance(item, str) and item for item in labels):
        raise ValueError("state_labels must be a nonempty list of distinct strings")
    if len(set(labels)) != len(labels):
        raise ValueError("state_labels must be distinct")
    index = {name: position for position, name in enumerate(labels)}
    size = len(labels)
    raw_q = payload.get("generator")
    if not isinstance(raw_q, list) or len(raw_q) != size or any(not isinstance(row, list) or len(row) != size for row in raw_q):
        raise ValueError("generator must be a square matrix matching state_labels")
    q = [[frac(value) for value in row] for row in raw_q]
    for i, row in enumerate(q):
        for j, value in enumerate(row):
            if i != j:
                nonnegative(value, f"generator[{i}][{j}] must be nonnegative")
        if row[i] > 0 or row[i] != -add(row[j] for j in range(size) if j != i):
            raise ValueError(f"generator row {i} must have diagonal equal to minus its off-diagonal sum")
    raw_initial = payload.get("initial")
    if not isinstance(raw_initial, list) or len(raw_initial) != size:
        raise ValueError("initial must have one exact rational mass per state")
    initial = [frac(value) for value in raw_initial]
    if any(value < 0 for value in initial) or add(initial) != 1:
        raise ValueError("initial must be a nonnegative probability vector with exact total 1")
    time = frac(payload.get("time"))
    nonnegative(time, "time must be nonnegative")
    domain_names, exit_names = payload.get("domain"), payload.get("physical_exit")
    if not isinstance(domain_names, list) or not isinstance(exit_names, list):
        raise ValueError("domain and physical_exit must be lists of state labels")
    try:
        domain = [index[name] for name in domain_names]
        exits = [index[name] for name in exit_names]
        loss = index[payload["loss_state"]]
    except (KeyError, TypeError) as exc:
        raise ValueError("domain, physical_exit, and loss_state must name states") from exc
    if len(set(domain)) != len(domain) or len(set(exits)) != len(exits):
        raise ValueError("domain and physical_exit may not repeat states")
    if set(domain) & set(exits) or loss in domain or loss in exits or set(domain) | set(exits) | {loss} != set(range(size)):
        raise ValueError("domain, physical_exit, and loss_state must be a disjoint partition of all states")
    if initial[loss] != 0:
        raise ValueError("initial loss mass is not supported: model a known initial physical exit instead")
    for i in exits + [loss]:
        if any(q[i][j] != 0 for j in range(size)):
            raise ValueError("physical_exit and loss_state rows must be absorbing (all zero)")
    max_rate = max((-q[i][i] for i in range(size)), default=Fraction(0))
    rate = frac(payload.get("uniformization_rate", max_rate if max_rate else 1))
    if rate <= 0 or rate < max_rate:
        raise ValueError("uniformization_rate must be positive and at least every leaving rate")
    terms = payload.get("terms", 40)
    exp_terms = payload.get("exp_terms", 16)
    digits = payload.get("decimal_digits", 20)
    if not all(isinstance(value, int) and not isinstance(value, bool) for value in (terms, exp_terms, digits)):
        raise ValueError("terms, exp_terms, and decimal_digits must be integers")
    if terms < 0 or exp_terms < 1 or digits < 1:
        raise ValueError("terms >= 0, exp_terms >= 1, and decimal_digits >= 1 are required")
    return labels, q, initial, time, domain, exits, loss, rate, terms, exp_terms, digits


def event_interval(vectors: list[list[Fraction]], raw_weights: list[Fraction], event: list[int], e_lo: Fraction, e_hi: Fraction, tail_raw: Fraction) -> tuple[Fraction, Fraction]:
    partial = add(raw_weights[n] * add(vectors[n][i] for i in event) for n in range(len(vectors)))
    return e_lo * partial, min(Fraction(1), e_hi * (partial + tail_raw))


def certify(payload: dict[str, Any]) -> dict[str, Any]:
    labels, q, initial, time, domain, exits, loss, rate, terms, exp_terms, digits = parse_model(payload)
    size = len(labels)
    p = [[(Fraction(1) if i == j else Fraction(0)) + q[i][j] / rate for j in range(size)] for i in range(size)]
    for i, row in enumerate(p):
        if any(value < 0 for value in row) or add(row) != 1:
            raise AssertionError(f"uniformization matrix row {i} is not stochastic")
    y = rate * time
    tail_raw = raw_poisson_tail_upper(y, terms)
    e_lo, e_hi = alternating_exp_neg_interval(y, exp_terms)
    poisson_tail_upper = min(Fraction(1), e_hi * tail_raw)
    vectors = [initial]
    for _ in range(terms):
        vectors.append(matvec(vectors[-1], p))
    raw_weights = [y**n / factorial(n) for n in range(terms + 1)]
    state_probabilities = {
        labels[i]: interval(*event_interval(vectors, raw_weights, [i], e_lo, e_hi, tail_raw), digits)
        for i in range(size)
    }
    domain_probability = event_interval(vectors, raw_weights, domain, e_lo, e_hi, tail_raw)
    exit_probability = event_interval(vectors, raw_weights, exits, e_lo, e_hi, tail_raw)
    loss_probability = event_interval(vectors, raw_weights, [loss], e_lo, e_hi, tail_raw)
    # Integral of the n-th uniformization summand on [0,t].  The formula
    # (1-exp(-y)*sum_{k<=n}y^k/k!)/rate is bracketed with the exp interval.
    occupation_coefficients: list[tuple[Fraction, Fraction]] = []
    prefix = Fraction(0)
    for n in range(terms + 1):
        prefix += raw_weights[n]
        lo = max(Fraction(0), (1 - e_hi * prefix) / rate)
        hi = min(1 / rate, max(Fraction(0), (1 - e_lo * prefix) / rate))
        occupation_coefficients.append((lo, hi))
    occupation_tail = time * poisson_tail_upper
    occupations: dict[str, tuple[Fraction, Fraction]] = {}
    for i in range(size):
        lo = add(vectors[n][i] * occupation_coefficients[n][0] for n in range(terms + 1))
        hi = min(time, add(vectors[n][i] * occupation_coefficients[n][1] for n in range(terms + 1)) + occupation_tail)
        occupations[labels[i]] = (lo, hi)
    loss_occ = occupations[labels[loss]]
    actual_exit = (exit_probability[0], min(Fraction(1), exit_probability[1] + loss_probability[1]))
    retained_domain_actual = {
        labels[i]: (occupations[labels[i]][0], min(time, occupations[labels[i]][1] + loss_occ[1]))
        for i in domain
    }
    return {
        "certificate_kind": "finite augmented CTMC, exact rational uniformization enclosure",
        "model_interpretation": {
            "tracked_physical_exit": "absorbing physical_exit states; their mass is a lower bound for the untruncated exit event",
            "truncation_loss": "absorbing loss_state; it represents departure from the retained truncation, not a physical exit",
            "coupling_bounds": "for any original CTMC agreeing until loss, P(tracked exit)<=P(original exit)<=P(tracked exit)+P(loss); each retained-domain occupation is between the killed value and killed value plus loss occupation",
        },
        "uniformization": {
            "rate": fstr(rate), "lambda_times_time": fstr(y), "terms": terms,
            "exp_taylor_pairs": exp_terms, "exp_neg_interval": interval(e_lo, e_hi, digits),
            "raw_poisson_tail_upper": fstr(tail_raw), "poisson_tail_upper": fstr(poisson_tail_upper),
            "remainder_statement": "all omitted probability summands are nonnegative; their total is at most poisson_tail_upper, and omitted occupation at any coordinate is at most time*poisson_tail_upper",
        },
        "finite_augmented_chain": {
            "state_probability_intervals": state_probabilities,
            "domain_survival_probability": interval(*domain_probability, digits),
            "tracked_physical_exit_probability": interval(*exit_probability, digits),
            "truncation_loss_probability": interval(*loss_probability, digits),
            "occupation_intervals": {name: interval(*value, digits) for name, value in occupations.items()},
        },
        "original_chain_bounds_if_loss_is_a_truncation": {
            "physical_exit_probability": interval(*actual_exit, digits),
            "retained_domain_occupation_each": {name: interval(*value, digits) for name, value in retained_domain_actual.items()},
            "limit": "These are finite-horizon coupling bounds only. They do not establish ETFSP convergence for a countable exhaustion or a total-variation occupation bound without the source assumptions and an independently certified expectation bound.",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON model with exact rational strings")
    parser.add_argument("-o", "--output", type=Path, help="write JSON certificate (default: stdout)")
    args = parser.parse_args()
    try:
        with args.input.open(encoding="utf-8") as handle:
            result = certify(json.load(handle))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
