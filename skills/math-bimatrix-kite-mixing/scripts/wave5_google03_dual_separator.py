#!/usr/bin/env python3
"""Check the finite Branch-2 certificate from Cogentic Lemma 2.3(b)."""
import json
import sys
from fractions import Fraction


def q(value):
    return Fraction(str(value))


def vector(raw, name):
    out = [q(v) for v in raw]
    if not out or any(v < 0 for v in out) or sum(out) != 1:
        raise ValueError(f"{name} must be a nonempty probability vector")
    return out


def matrix(raw, name):
    out = [[q(v) for v in row] for row in raw]
    if not out or not out[0] or any(len(row) != len(out[0]) for row in out):
        raise ValueError(f"{name} must be nonempty and rectangular")
    if any(v < 0 or v > 1 for row in out for v in row):
        raise ValueError(f"{name} entries must lie in [0,1]")
    return out


def row_payoff(strategy, game, col):
    return sum(strategy[i] * game[i][col] for i in range(len(strategy)))


def regrets_at_pure_column(u, R, C, col):
    r_payoff = row_payoff(u, R, col)
    c_payoff = row_payoff(u, C, col)
    return max(R[i][col] for i in range(len(u))) - r_payoff, max(
        row_payoff(u, C, k) for k in range(len(C[0]))
    ) - c_payoff


def in_kite(a, b, r):
    return (1 - r) * a + r * b <= r and r * a + (1 - r) * b <= r


def main(path):
    data = json.load(open(path, encoding="utf-8"))
    R, C = matrix(data["R"], "R"), matrix(data["C"], "C")
    if len(R) != len(C) or len(R[0]) != len(C[0]):
        raise ValueError("R and C must have identical shape")
    xbar, u = vector(data["xbar"], "xbar"), vector(data["u"], "u")
    if len(xbar) != len(R) or len(u) != len(R):
        raise ValueError("xbar and u must have one coordinate per row")
    r, lam = q(data["r"]), q(data["lambda"])
    if not (0 < r < Fraction(1, 2)):
        raise ValueError("r must satisfy 0 < r < 1/2")
    if not (r <= lam <= 1 - r):
        raise ValueError("lambda must lie in [r,1-r]")
    m2_anchor = max(row_payoff(xbar, C, j) for j in range(len(R[0])))
    cap = 2 - r / (1 - r)
    rows = []
    for j in range(len(R[0])):
        separation = (1 - lam) * (row_payoff(u, R, j) - row_payoff(xbar, R, j)) + lam * (m2_anchor - row_payoff(xbar, C, j))
        f1, f2 = regrets_at_pure_column(u, R, C, j)
        welfare = row_payoff(u, R, j) + row_payoff(u, C, j)
        rows.append({"column": j, "separation": str(separation), "f1": str(f1), "f2": str(f2), "outside_kite": not in_kite(f1, f2, r), "welfare": str(welfare)})
        if separation <= r:
            raise ValueError(f"column {j}: separation is not strictly greater than r")
        if in_kite(f1, f2, r):
            raise ValueError(f"column {j}: pure-column profile lies in K_r")
        if welfare >= cap:
            raise ValueError(f"column {j}: welfare cap is not strict")
    print(json.dumps({"valid": True, "r": str(r), "lambda": str(lam), "M2_xbar": str(m2_anchor), "welfare_cap": str(cap), "columns": rows}, sort_keys=True))


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except (IndexError, KeyError, ValueError, json.JSONDecodeError) as err:
        print(json.dumps({"valid": False, "error": str(err)}, sort_keys=True))
        raise SystemExit(2)
