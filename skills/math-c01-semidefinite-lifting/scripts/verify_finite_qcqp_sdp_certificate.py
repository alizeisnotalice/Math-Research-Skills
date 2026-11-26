#!/usr/bin/env python3
"""Exact finite certificate for a homogenized QCQP and its Shor SDP relaxation.

The JSON describes
  min z^T Q z  subject to z^T B_j z >= 0 (j finite), z[-1] = 1.
It must also supply tau, nonnegative multipliers mu_j, and a feasible z_star.
This program verifies the exact rational PSD identity
  Q - tau H - sum_j mu_j B_j >= 0,  H=e_n e_n^T,
and objective equality at z_star.  Consequently tau is the global QCQP minimum
and equals the Shor SDP relaxation value.  This is a verifier, not an exactness
test for arbitrary QCQPs and not a solver for the SDP.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


MAX_PSD_DIMENSION = 12


def rat(value: Any) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("all scalars must be exact integers or rational strings; floats are forbidden")
    if isinstance(value, (int, str)):
        return Fraction(value)
    raise ValueError(f"not an exact rational: {value!r}")


def vec(raw: Any, length: int | None = None, name: str = "vector") -> list[Fraction]:
    if not isinstance(raw, list):
        raise ValueError(f"{name} must be a list")
    result = [rat(x) for x in raw]
    if length is not None and len(result) != length:
        raise ValueError(f"{name} has length {len(result)}, expected {length}")
    return result


def mat(raw: Any, n: int | None = None, name: str = "matrix") -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise ValueError(f"{name} must be a nonempty square list of lists")
    size = len(raw)
    if n is not None and size != n:
        raise ValueError(f"{name} has dimension {size}, expected {n}")
    result = [vec(row, size, f"{name}[{i}]") for i, row in enumerate(raw)]
    for i in range(size):
        for j in range(size):
            if result[i][j] != result[j][i]:
                raise ValueError(f"{name} is not symmetric at ({i},{j})")
    return result


def qform(z: list[Fraction], a: list[list[Fraction]]) -> Fraction:
    return sum((z[i] * a[i][j] * z[j] for i in range(len(z)) for j in range(len(z))), Fraction(0))


def determinant(a: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in a]
    answer = Fraction(1)
    sign = Fraction(1)
    for col in range(len(work)):
        pivot = next((row for row in range(col, len(work)) if work[row][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign = -sign
        p = work[col][col]
        answer *= p
        for row in range(col + 1, len(work)):
            factor = work[row][col] / p
            for right in range(col + 1, len(work)):
                work[row][right] -= factor * work[col][right]
            work[row][col] = Fraction(0)
    return sign * answer


def assert_psd(a: list[list[Fraction]], name: str) -> int:
    if len(a) > MAX_PSD_DIMENSION:
        raise ValueError(f"{name} dimension exceeds exact principal-minor cap {MAX_PSD_DIMENSION}")
    checked = 0
    for k in range(1, len(a) + 1):
        for subset in itertools.combinations(range(len(a)), k):
            value = determinant([[a[i][j] for j in subset] for i in subset])
            checked += 1
            if value < 0:
                raise ValueError(f"{name} is not PSD: principal minor {subset} equals {value}")
    return checked


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    q = mat(payload.get("Q"), name="Q")
    n = len(q)
    conditioning = payload.get("homogenization")
    if not isinstance(conditioning, dict):
        raise ValueError("homogenization is required: certify the affine anchor coordinate")
    if conditioning.get("anchor_index") != n - 1 or rat(conditioning.get("anchor_value")) != 1:
        raise ValueError("only the explicit anchor z[n-1]=1 is supported")
    raw_b = payload.get("constraints")
    if not isinstance(raw_b, list):
        raise ValueError("constraints must be a finite JSON list (possibly empty), not an implicit/infinite family")
    b = [mat(item, n, f"constraints[{i}]") for i, item in enumerate(raw_b)]
    certificate = payload.get("certificate")
    if not isinstance(certificate, dict):
        raise ValueError("certificate object is required")
    tau = rat(certificate.get("lower_bound"))
    mu = vec(certificate.get("multipliers"), len(b), "certificate.multipliers")
    if any(value < 0 for value in mu):
        raise ValueError("all constraint multipliers must be nonnegative for >= constraints in a minimization certificate")
    z = vec(certificate.get("candidate_z"), n, "certificate.candidate_z")
    if z[-1] != 1:
        raise ValueError("candidate_z violates required affine anchor z[n-1]=1")
    for i, bi in enumerate(b):
        value = qform(z, bi)
        if value < 0:
            raise ValueError(f"candidate_z violates constraint {i}: z^T B z={value}")
    objective = qform(z, q)
    if objective != tau:
        raise ValueError(f"candidate objective {objective} does not attain claimed lower bound {tau}")

    slack = [[q[i][j] for j in range(n)] for i in range(n)]
    slack[-1][-1] -= tau
    for weight, bi in zip(mu, b):
        for i in range(n):
            for j in range(n):
                slack[i][j] -= weight * bi[i][j]
    minors = assert_psd(slack, "Lagrangian/SDP dual slack")
    return {
        "status": "verified-finite-qcqp-and-shor-sdp-exact",
        "value": str(tau),
        "dimension": n,
        "finite_quadratic_constraints": len(b),
        "psd_principal_minors_checked": minors,
        "method": "exact rational Lagrangian lower certificate plus anchored feasible rank-one point",
        "scope": "the stated finite homogenized QCQP and its stated Shor SDP relaxation",
        "not_certified": "infinite constraint families, S-lemma hypotheses, ROG/NIQCC conditions, how to find multipliers, or a floating-point SDP solution",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON certificate")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        result = verify(payload)
    except (OSError, json.JSONDecodeError, ValueError, ZeroDivisionError) as error:
        print(json.dumps({"status": "rejected", "reason": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
