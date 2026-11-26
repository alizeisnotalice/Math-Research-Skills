#!/usr/bin/env python3
"""Certify finite-horizon finite-state Markov endpoint bridges over Q.

Input is JSON with exact nonnegative rational transition probabilities.  A
``target_states`` run certifies the law conditional on X_T in that set.  A
``terminal_distribution`` run certifies the related terminal-reweighting
identity.  This is deliberately not a sampler or an asymptotic claim.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


ZERO = Fraction(0)
ONE = Fraction(1)


class InputError(ValueError):
    pass


def rat(value: Any, where: str) -> Fraction:
    if isinstance(value, bool):
        raise InputError(f"{where}: Boolean is not an exact rational")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise InputError(f"{where}: expected integer or p/q string") from exc
    raise InputError(f"{where}: floats and non-rational JSON values are forbidden")


def show(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def vector(values: Any, n: int, name: str) -> list[Fraction]:
    if not isinstance(values, list) or len(values) != n:
        raise InputError(f"{name}: expected a length-{n} list")
    out = [rat(value, f"{name}[{i}]") for i, value in enumerate(values)]
    if any(x < ZERO for x in out):
        raise InputError(f"{name}: all entries must be nonnegative")
    if sum(out, ZERO) != ONE:
        raise InputError(f"{name}: entries must sum exactly to 1")
    return out


def read_instance(path: Path) -> tuple[list[list[Fraction]], list[Fraction], int, list[int], list[list[int]], list[Fraction] | None]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise InputError(f"cannot parse JSON input: {exc}") from exc
    if not isinstance(raw, dict):
        raise InputError("top-level JSON must be an object")
    trans_raw = raw.get("transition")
    if not isinstance(trans_raw, list) or not trans_raw:
        raise InputError("transition must be a nonempty square matrix")
    n = len(trans_raw)
    P = [vector(row, n, f"transition[{i}]") for i, row in enumerate(trans_raw)]
    mu = vector(raw.get("initial_distribution"), n, "initial_distribution")
    horizon = raw.get("horizon")
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 1:
        raise InputError("horizon must be an integer at least 1")
    targets = raw.get("target_states")
    if not isinstance(targets, list) or not targets:
        raise InputError("target_states must be a nonempty list")
    if any(isinstance(x, bool) or not isinstance(x, int) or x < 0 or x >= n for x in targets):
        raise InputError("target_states contains an invalid state index")
    if len(set(targets)) != len(targets):
        raise InputError("target_states must not contain duplicates")
    paths = raw.get("paths", [])
    if not isinstance(paths, list):
        raise InputError("paths must be a list when supplied")
    for k, path_values in enumerate(paths):
        if not isinstance(path_values, list) or len(path_values) != horizon + 1:
            raise InputError(f"paths[{k}] must contain horizon+1 states")
        if any(isinstance(x, bool) or not isinstance(x, int) or x < 0 or x >= n for x in path_values):
            raise InputError(f"paths[{k}] contains an invalid state index")
    terminal = raw.get("terminal_distribution")
    q = None if terminal is None else vector(terminal, n, "terminal_distribution")
    return P, mu, horizon, targets, paths, q


def multiply_dist(dist: list[Fraction], P: list[list[Fraction]]) -> list[Fraction]:
    n = len(P)
    return [sum((dist[x] * P[x][y] for x in range(n)), ZERO) for y in range(n)]


def backward_h(P: list[list[Fraction]], terminal_weight: list[Fraction], T: int) -> list[list[Fraction]]:
    n = len(P)
    h = [[ZERO] * n for _ in range(T + 1)]
    h[T] = terminal_weight[:]
    for t in range(T - 1, -1, -1):
        h[t] = [sum((P[x][y] * h[t + 1][y] for y in range(n)), ZERO) for x in range(n)]
    return h


def bridge_kernel(P: list[list[Fraction]], h: list[list[Fraction]], T: int) -> list[list[list[Fraction] | None]]:
    n = len(P)
    Q: list[list[list[Fraction] | None]] = []
    for t in range(T):
        rows: list[list[Fraction] | None] = []
        for x in range(n):
            if h[t][x] == ZERO:
                rows.append(None)
            else:
                row = [P[x][y] * h[t + 1][y] / h[t][x] for y in range(n)]
                if sum(row, ZERO) != ONE:
                    raise AssertionError("Doob row did not normalize")
                rows.append(row)
        Q.append(rows)
    return Q


def path_prob(path: list[int], init: list[Fraction], kernels: list[list[list[Fraction] | None]]) -> Fraction:
    out = init[path[0]]
    for t, (x, y) in enumerate(zip(path, path[1:])):
        row = kernels[t][x]
        if row is None:
            return ZERO
        out *= row[y]
    return out


def encode_kernels(kernels: list[list[list[Fraction] | None]]) -> list:
    return [[[show(x) for x in row] if row is not None else None for row in matrix]
            for matrix in kernels]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON instance with rational entries")
    parser.add_argument("--pretty", action="store_true", help="pretty-print JSON output")
    parser.add_argument("--include-kernels", action="store_true", help="include exact h and kernel rows")
    args = parser.parse_args()
    try:
        P, mu, T, target, paths, q = read_instance(args.input)
        n = len(P)
        terminal_original = mu[:]
        for _ in range(T):
            terminal_original = multiply_dist(terminal_original, P)
        target_set = set(target)
        original_kernels = [P] * T
        target_weight = [ONE if x in target_set else ZERO for x in range(n)]
        h_target = backward_h(P, target_weight, T)
        event_probability = sum((mu[x] * h_target[0][x] for x in range(n)), ZERO)
        if event_probability == ZERO:
            raise InputError("target event has exact probability 0; conditional bridge is undefined")
        target_initial = [mu[x] * h_target[0][x] / event_probability for x in range(n)]
        target_Q = bridge_kernel(P, h_target, T)
        target_terminal = target_initial[:]
        for t in range(T):
            target_terminal = multiply_dist(target_terminal, [row if row is not None else [ZERO] * n for row in target_Q[t]])
        if sum(target_terminal[x] for x in target) != ONE:
            raise AssertionError("conditioned law did not end in target")
        result: dict[str, Any] = {
            "certificate": "finite-state finite-horizon exact-rational endpoint bridge",
            "state_count": n,
            "horizon": T,
            "target_states": target,
            "target_event_probability": show(event_probability),
            "conditional_initial_distribution": [show(x) for x in target_initial],
            "conditional_terminal_distribution": [show(x) for x in target_terminal],
            "zero_h_states_by_time": [[x for x in range(n) if h_target[t][x] == ZERO] for t in range(T)],
            "identities_verified": [
                "h_t(x)=sum_y P(x,y)h_{t+1}(y)",
                "Q_t(x,y)=P(x,y)h_{t+1}(y)/h_t(x) on h_t(x)>0",
                "sum_y Q_t(x,y)=1 on every admitted row",
                "Law_Q(path)=Law_P(path)/P_mu(X_T in target) for every target-ending path",
            ],
        }
        if args.include_kernels:
            result["h"] = [[show(x) for x in row] for row in h_target]
            result["conditioned_kernels"] = encode_kernels(target_Q)
        path_reports = []
        for path in paths:
            p = path_prob(path, mu, original_kernels)
            qb = path_prob(path, target_initial, target_Q)
            target_ending = path[-1] in target_set
            conditional = p / event_probability if target_ending else ZERO
            if conditional != qb:
                raise ArithmeticError("conditioned path probabilities disagree")
            path_reports.append({
                "path": path,
                "original_probability": show(p),
                "conditional_target_probability": show(conditional),
                "bridge_probability": show(qb),
                "identity_holds": conditional == qb,
            })
        if path_reports:
            result["path_checks"] = path_reports
        if q is not None:
            if any(q[x] > ZERO and terminal_original[x] == ZERO for x in range(n)):
                raise InputError("terminal_distribution gives positive mass to an endpoint unreachable under the supplied initial law")
            gT = [q[x] / terminal_original[x] if terminal_original[x] > ZERO else ZERO for x in range(n)]
            hq = backward_h(P, gT, T)
            normalizer = sum((mu[x] * hq[0][x] for x in range(n)), ZERO)
            if normalizer != ONE:
                raise AssertionError("terminal reweighting failed normalization")
            qinit = [mu[x] * hq[0][x] for x in range(n)]
            qkernel = bridge_kernel(P, hq, T)
            qterminal = qinit[:]
            for t in range(T):
                qterminal = multiply_dist(qterminal, [row if row is not None else [ZERO] * n for row in qkernel[t]])
            if qterminal != q:
                raise AssertionError("terminal reweighting did not produce q")
            original_abs_continuous = all(terminal_original[x] == ZERO or q[x] > ZERO for x in range(n))
            reweight_path_checks = []
            for path in paths:
                p = path_prob(path, mu, original_kernels)
                p_tilde = path_prob(path, qinit, qkernel)
                if p_tilde == ZERO:
                    reweight_path_checks.append({
                        "path": path,
                        "original_probability": show(p),
                        "new_probability": "0",
                        "identity_checked_on_new_support": False,
                    })
                else:
                    likelihood = terminal_original[path[-1]] / q[path[-1]]
                    if p != likelihood * p_tilde:
                        raise ArithmeticError("reweighted path probabilities disagree")
                    reweight_path_checks.append({
                        "path": path,
                        "original_probability": show(p),
                        "new_probability": show(p_tilde),
                        "terminal_likelihood_ratio": show(likelihood),
                        "identity_holds": p == likelihood * p_tilde,
                    })
            result["terminal_reweighting"] = {
                "requested_terminal_distribution": [show(x) for x in q],
                "terminal_distribution_reproduced": [show(x) for x in qterminal],
                "new_measure_is_supported_by_original": True,
                "original_measure_is_absolutely_continuous_wrt_new": original_abs_continuous,
                "likelihood_ratio_on_new_support": "P(path)/P_tilde(path)=r_T(X_T)/q(X_T)",
                "original_terminal_distribution_r_T": [show(x) for x in terminal_original],
                "zero_h_states_by_time": [[x for x in range(n) if hq[t][x] == ZERO] for t in range(T)],
            }
            if args.include_kernels:
                result["terminal_reweighting"]["h"] = [[show(x) for x in row] for row in hq]
                result["terminal_reweighting"]["reweighted_kernels"] = encode_kernels(qkernel)
            if reweight_path_checks:
                result["terminal_reweighting"]["path_checks"] = reweight_path_checks
        print(json.dumps(result, indent=2 if args.pretty else None, ensure_ascii=False))
        return 0
    except InputError as exc:
        print(f"input error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
