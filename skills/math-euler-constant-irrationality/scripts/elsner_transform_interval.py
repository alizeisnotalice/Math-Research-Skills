#!/usr/bin/env python3
"""Enclose Euler's constant via Elsner's signed two-parameter transform."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import ceil, comb, floor
from pathlib import Path
import runpy


def remainder_majorant(d: int, m: int) -> Fraction:
    """Corollary 4 with π replaced by the strict lower bound 3."""
    if d < 2 or m < 1 or (d > 2 and m < 2):
        raise ValueError("require d >= 2 and m >= 2, with m = 1 also valid when d = 2")
    if d == 2:
        return Fraction(16, 21)**2 / 64**m
    rate = Fraction(d - 1, d)**d / ((d - 1) * 4**d)
    return rate**(m - 2) / 144


def transform(d: int, m: int) -> tuple[Fraction, dict[int, int]]:
    n = d*m
    tau_one = (d - 1)*m - 1
    weights = {
        n+k: (-1)**(n+k)*comb(n+tau_one+k,n)*comb(n,k)
        for k in range(n + 1)
    }
    if sum(weights.values()) != 1:
        raise ArithmeticError("integer transform did not preserve constants")
    harmonic = Fraction()
    rational = Fraction()
    for arg in range(1, 2*n + 1):
        rational += harmonic * weights.get(arg, 0)
        if arg < 2*n:
            harmonic += Fraction(1, arg)
    return rational, weights


def enclosure(d: int, m: int, terms: int | None = None) -> dict:
    bound = remainder_majorant(d, m)
    if terms is not None and terms < 1:
        raise ValueError("log series length must be positive")
    rational, weights = transform(d, m)
    harmonics_and_logs = runpy.run_path(str(
        Path(__file__).resolve().parents[2] / "math-sondow-log-fractional-certificate"
        / "scripts" / "sondow_certificate.py"
    ))
    if terms is None:
        tail = Fraction(3,4)*sum(abs(c)*x.bit_length() for x,c in weights.items())
        terms = 1
        tail /= 9
        while tail > bound/16:
            terms += 1
            tail /= 9
    log_two = harmonics_and_logs["log_unit_bounds"](Fraction(2), terms)
    lo = hi = rational
    for arg, weight in weights.items():
        a, b = harmonics_and_logs["integer_log_bounds"](arg, terms, log_two)
        products = (-weight*a, -weight*b)
        lo += min(products)
        hi += max(products)

    # Equation (13) of the proof gives sign(T-γ) when tau_one >= 1.
    sign = None if (d,m)==(2,1) else (-1)**((d-1)*m+1)
    gamma_lo = lo if sign == -1 else lo - bound
    gamma_hi = hi if sign == 1 else hi + bound
    return {"d":d,"m":m,"n":d*m,"tau1":(d-1)*m-1,"tau2":d*m,
            "rational_component":rational,"log_weights_subtracted":weights,
            "log_terms":terms,"transform_interval":(lo,hi),"remainder_upper_bound":bound,
            "transform_minus_gamma_sign":sign,"gamma_interval":(gamma_lo,gamma_hi)}


def decimal_at(value: int, places: int) -> str:
    integral, fractional = divmod(abs(value),10**places)
    sign = "-" if value < 0 else ""
    return f"{sign}{integral}.{fractional:0{places}d}"


def display_interval(interval: tuple[Fraction,Fraction], places: int) -> list[str]:
    scale = 10**places
    return [decimal_at(bound,places) for bound in (floor(scale*interval[0]),ceil(scale*interval[1]))]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--d",type=int,default=2)
    parser.add_argument("--m",type=int,required=True)
    parser.add_argument("--terms",type=int)
    parser.add_argument("--places",type=int,default=24)
    parser.add_argument("--exact-fractions",action="store_true")
    args = parser.parse_args()
    try:
        if args.places < 1:
            raise ValueError("places must be at least 1")
        result = enclosure(args.d,args.m,args.terms)
        for name in ("gamma_interval","transform_interval"):
            interval = result.pop(name)
            result[f"{name}_outward_decimal"] = display_interval(interval,args.places)
            if args.exact_fractions:
                result[name] = [str(x) for x in interval]
        if not args.exact_fractions:
            result.pop("log_weights_subtracted")
            result.pop("rational_component")
        print(json.dumps(result,default=str,indent=2))
    except (OSError,ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
