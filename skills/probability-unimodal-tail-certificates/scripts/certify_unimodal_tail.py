#!/usr/bin/env python3
"""Exact-rational checks for the Ion--Klaassen--van den Heuvel tail bounds.

The source theorem is analytic. This program selects its stated branches and
checks displayed extremizers with Fraction arithmetic; it is not a new proof.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Iterable

Q = Fraction
SOURCE = {
    "local_version": "arXiv:2208.08813v2 (2022-10-10)",
    "local_theorems": {"one_sided": "Theorem 5.2, Eq. (5.27), PDF p. 11", "asymmetric": "Theorem 5.4, Eq. (5.30), PDF pp. 11-12"},
    "published_version": "TEST 32 (2023), 566-601, DOI 10.1007/s11749-022-00844-9",
    "published_theorems": {"one_sided": "Theorem 5.2, Eq. (27)", "asymmetric": "Theorem 5.5, Eq. (30)"},
}


def rational(text: str) -> Q:
    try:
        return Q(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(f"not an exact rational threshold: {text!r}") from exc


def qtext(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def render(x):
    if isinstance(x, Q):
        return {"exact": qtext(x)}
    if isinstance(x, dict):
        return {key: render(value) for key, value in x.items()}
    if isinstance(x, list):
        return [render(value) for value in x]
    return x


@dataclass(frozen=True)
class Atom:
    weight: Q
    value: Q


@dataclass(frozen=True)
class UniformPiece:
    weight: Q
    left: Q
    right: Q


def one_sided_bound(v: Q) -> tuple[str, Q]:
    if v < 0:
        raise ValueError("The cited one-sided theorem requires v >= 0.")
    if v * v <= Q(5, 3):
        return "low-threshold", (3 - v * v) / (3 * (1 + v * v))
    return "large-threshold", Q(4, 9) / (1 + v * v)


def asymmetric_bound(u: Q, v: Q) -> tuple[str, Q]:
    # For v>0, v >= sqrt(3) iff v^2 >= 3; this makes the gate exact.
    if v <= 0 or v * v < 3 or u < v:
        raise ValueError("The cited asymmetric theorem requires sqrt(3) <= v <= u.")
    if u - v <= 2 / v:
        return "near-asymmetric", Q(4, 9) * (4 + (u - v) ** 2) / (u + v) ** 2
    return "plateau", Q(4, 9) / (1 + v * v)


def one_extremizer(v: Q) -> tuple[list[Atom], list[UniformPiece]]:
    if v <= 0:
        raise ValueError("No equality construction is claimed here at v = 0 because its formula divides by v.")
    if v * v <= Q(5, 3):
        p = (3 - v * v) / (3 * (1 + v * v))
        return [Atom(p, v)], [UniformPiece(1 - p, -(3 + v * v) / (2 * v), v)]
    p = (3 * v * v - 1) / (3 * (1 + v * v))
    return [Atom(p, -1 / v)], [UniformPiece(1 - p, -1 / v, (1 + 3 * v * v) / (2 * v))]


def near_extremizer(u: Q, v: Q) -> tuple[list[Atom], list[UniformPiece]]:
    """Translate source Z=(v-u)/2+U*Y exactly into mixed-law pieces."""
    shift, span = (v - u) / 2, u + v
    values = [-Q(3, 4) * span, Q(0), Q(3, 4) * span]
    weights = [
        Q(4, 3) * (2 + v * (v - u)) / span**2,
        1 - Q(4, 3) * (4 + (v - u) ** 2) / span**2,
        Q(4, 3) * (2 + u * (u - v)) / span**2,
    ]
    atoms, pieces = [], []
    for y, p in zip(values, weights, strict=True):
        if y == 0:
            atoms.append(Atom(p, shift))
        else:
            pieces.append(UniformPiece(p, min(shift, shift + y), max(shift, shift + y)))
    return atoms, pieces


def moments(atoms: Iterable[Atom], pieces: Iterable[UniformPiece]) -> tuple[Q, Q, Q]:
    mass = mean = second = Q(0)
    for a in atoms:
        mass += a.weight
        mean += a.weight * a.value
        second += a.weight * a.value * a.value
    for p in pieces:
        mass += p.weight
        mean += p.weight * (p.left + p.right) / 2
        second += p.weight * (p.left * p.left + p.left * p.right + p.right * p.right) / 3
    return mass, mean, second


def interval_event(p: UniformPiece, kind: str, *, u: Q | None = None, v: Q) -> Q:
    width = p.right - p.left
    right = max(Q(0), p.right - max(p.left, v)) / width
    if kind == "right":
        return right
    left = max(Q(0), min(p.right, -u) - p.left) / width
    return left + right


def event(atoms: Iterable[Atom], pieces: Iterable[UniformPiece], kind: str, *, u: Q | None = None, v: Q) -> Q:
    if kind == "right":
        atom_part = sum((a.weight for a in atoms if a.value >= v), Q(0))
    else:
        atom_part = sum((a.weight for a in atoms if a.value <= -u or a.value >= v), Q(0))
    return atom_part + sum((p.weight * interval_event(p, kind, u=u, v=v) for p in pieces), Q(0))


def equality(atoms: list[Atom], pieces: list[UniformPiece], kind: str, *, v: Q, bound: Q, u: Q | None = None) -> dict:
    mass, mean, second = moments(atoms, pieces)
    probability = event(atoms, pieces, kind, u=u, v=v)
    return {"claimed_by_source": True, "mass": mass, "mean": mean, "second_moment": second, "event_probability": probability, "exact_bound_difference": probability - bound}


def one_certificate(v: Q) -> dict:
    branch, bound = one_sided_bound(v)
    result = {"status": "available", "mode": "one-sided", "v": v, "branch": branch, "bound": bound, "source": SOURCE, "requirements": ["Z is scalar, standardized (E Z=0, E Z^2=1), and unimodal", "event is P(Z >= v) with v >= 0"]}
    if v == 0:
        result["equality_check"] = {"claimed_by_source": False, "reason": "The theorem includes v=0, but its displayed equality constructions are only stated for v>0."}
    else:
        atoms, pieces = one_extremizer(v)
        result["equality_check"] = equality(atoms, pieces, "right", v=v, bound=bound)
    return result


def asymmetric_certificate(u: Q, v: Q) -> dict:
    branch, bound = asymmetric_bound(u, v)
    result = {"status": "available", "mode": "asymmetric", "u": u, "v": v, "branch": branch, "bound": bound, "source": SOURCE, "requirements": ["Z is scalar, standardized (E Z=0, E Z^2=1), and unimodal", "event is P(Z <= -u or Z >= v)", "sqrt(3) <= v <= u"]}
    atoms, pieces = near_extremizer(u, v) if branch == "near-asymmetric" else one_extremizer(v)
    result["equality_check"] = equality(atoms, pieces, "asymmetric", u=u, v=v, bound=bound)
    return result


def rejects(action: Callable[[], object]) -> bool:
    try:
        action()
    except ValueError:
        return True
    return False


def verify() -> dict:
    checks = []
    for v in (Q(1, 4), Q(5, 3), Q(2)):
        rec = one_certificate(v)["equality_check"]
        checks.append({"case": f"one-sided v={qtext(v)}", "mass_minus_one": rec["mass"] - 1, "mean": rec["mean"], "second_moment_minus_one": rec["second_moment"] - 1, "event_minus_bound": rec["exact_bound_difference"]})
    for u, v in ((Q(2), Q(2)), (Q(3), Q(2)), (Q(4), Q(2))):
        cert = asymmetric_certificate(u, v)
        rec = cert["equality_check"]
        checks.append({"case": f"asymmetric u={qtext(u)}, v={qtext(v)}, {cert['branch']}", "mass_minus_one": rec["mass"] - 1, "mean": rec["mean"], "second_moment_minus_one": rec["second_moment"] - 1, "event_minus_bound": rec["exact_bound_difference"]})
    v, u = Q(2), Q(3)
    left = Q(4, 9) * (4 + (u - v) ** 2) / (u + v) ** 2
    right = Q(4, 9) / (1 + v * v)
    checks.append({"case": "branch boundary u=v+2/v at v=2", "left_minus_right": left - right})
    checks.extend([
        {"case": "out-of-domain v<sqrt(3)", "rejected": rejects(lambda: asymmetric_bound(Q(9, 5), Q(17, 10)))},
        {"case": "out-of-domain reversed direct orientation", "rejected": rejects(lambda: asymmetric_bound(Q(2), Q(3)))},
        {"case": "out-of-domain negative one-sided threshold", "rejected": rejects(lambda: one_sided_bound(Q(-1, 10)))},
    ])
    zero_fields = ("mass_minus_one", "mean", "second_moment_minus_one", "event_minus_bound", "left_minus_right")
    all_zero = all(all(row[key] == 0 for key in zero_fields if key in row) for row in checks if "rejected" not in row)
    all_rejected = all(row["rejected"] for row in checks if "rejected" in row)
    return {"status": "exact-rational-check", "all_exact_residuals_zero": all_zero, "all_invalid_thresholds_rejected": all_rejected, "checks": checks, "interpretation": "Zero residuals are exact Fraction identities for selected extremizers; they check arithmetic, not the analytic theorem."}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("one-sided", "asymmetric", "verify"), required=True)
    parser.add_argument("--v", type=rational, help="exact rational: 2, 5/3, or 1.25")
    parser.add_argument("--u", type=rational, help="exact rational: 3 or 7/2")
    args = parser.parse_args()
    try:
        if args.mode == "verify":
            result = verify()
        elif args.mode == "one-sided":
            if args.v is None:
                parser.error("--v is required for --mode one-sided")
            result = one_certificate(args.v)
        else:
            if args.u is None or args.v is None:
                parser.error("--u and --v are required for --mode asymmetric")
            result = asymmetric_certificate(args.u, args.v)
    except ValueError as exc:
        params = {key: value for key, value in (("u", args.u), ("v", args.v)) if value is not None}
        result = {"status": "unavailable", "reason": str(exc), "parameters": params, "source": SOURCE}
    print(json.dumps(render(result), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
