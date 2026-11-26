#!/usr/bin/env python3
"""Exact rational verifier for the finite three-strip/token lemma interface."""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


def q(value: object) -> Fraction:
    return Fraction(str(value))


def fail(message: str) -> None:
    raise ValueError(message)


def vec(raw: object, label: str) -> tuple[Fraction, Fraction]:
    if not isinstance(raw, list) or len(raw) != 2:
        fail(f"{label} must be a length-two list")
    return q(raw[0]), q(raw[1])


def dot(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> Fraction:
    return a[0] * b[0] + a[1] * b[1]


def sqnorm(a: tuple[Fraction, Fraction]) -> Fraction:
    return dot(a, a)


def main(path: str) -> None:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    D, theta = q(raw["D"]), q(raw["theta"])
    if D < 1 or theta < 0:
        fail("D must be at least 1 and theta must be nonnegative")
    points_raw = raw["points"]
    if not isinstance(points_raw, dict) or not points_raw:
        fail("points must be a nonempty object")
    points = {str(k): vec(v, f"point {k}") for k, v in points_raw.items()}
    inside = {str(x) for x in raw["inside"]}
    if not inside <= points.keys():
        fail("inside references an unknown point")
    for name in inside:
        if sqnorm(points[name]) > D * D:
            fail(f"inside point {name} violates the D bound")
    states = raw["states"]
    if not isinstance(states, list) or len(states) < 2:
        fail("at least two states are required")
    parsed = []
    sizes = set()
    for i, state in enumerate(states):
        normal = vec(state["normal"], f"state {i} normal")
        threshold = q(state["threshold"])
        marked = {str(x) for x in state["marked"]}
        if not marked <= points.keys():
            fail(f"state {i} references an unknown marked point")
        if sqnorm(normal) != 1:
            fail(f"state {i} normal is not exactly unit")
        cut_marked = {name for name, x in points.items() if dot(normal, x) < threshold}
        if cut_marked != marked:
            fail(f"state {i} marked set does not equal its strict cut")
        parsed.append((normal, threshold, marked))
        sizes.add(len(marked))
    if len(sizes) != 1:
        fail("all marked sets must have the same cardinality")
    nu0 = parsed[0][0]
    for i, (normal, _, _) in enumerate(parsed):
        if sqnorm((normal[0] - nu0[0], normal[1] - nu0[1])) > theta * theta:
            fail(f"state {i} violates the theta directional bound")
    transfers = raw["transfers"]
    if not isinstance(transfers, list) or len(transfers) != len(parsed) - 1:
        fail("one transfer list is required for each state transition")
    crossing = 0
    active: set[str] = set()
    for i, pairs in enumerate(transfers, start=1):
        previous, current = parsed[i - 1][2], parsed[i][2]
        losses, gains = previous - current, current - previous
        if not isinstance(pairs, list):
            fail(f"transfer {i} must be a list")
        got_losses: set[str] = set()
        got_gains: set[str] = set()
        for pair in pairs:
            if not isinstance(pair, list) or len(pair) != 2:
                fail(f"transfer {i} pairs must be [lost, gained]")
            lost, gained = str(pair[0]), str(pair[1])
            got_losses.add(lost)
            got_gains.add(gained)
            if (lost in inside) != (gained in inside):
                crossing += 1
        if got_losses != losses or got_gains != gains or len(pairs) != len(losses):
            fail(f"transfer {i} is not the loss--gain bijection")
        active |= losses | gains
    rho = D * theta
    thresholds = [row[1] for row in parsed]
    centers = {thresholds[0], min(thresholds), max(thresholds)}
    outside: list[str] = []
    for name in sorted(active & inside):
        t = dot(nu0, points[name])
        if all(abs(t - center) > 3 * rho for center in centers):
            outside.append(name)
    if len(outside) > 2 * crossing:
        fail("three-strip conclusion failed; verify the hypotheses and input")
    print(json.dumps({
        "active_inside": len(active & inside),
        "boundary_transfers": crossing,
        "outside_three_strips": outside,
        "bound": 2 * crossing,
        "status": "certified",
    }, sort_keys=True))


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("usage: check_three_strip.py certificate.json")
        main(sys.argv[1])
    except (KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        print(f"invalid certificate: {error}", file=sys.stderr)
        raise SystemExit(2)
