#!/usr/bin/env python3
"""Evaluate the 1980 Brent--McMillan B1 recurrence at a requested finite cutoff.

The default mode is numerical.  The optional --rigorous mode returns an exact
Fraction interval by bounding the positive Bessel-series tail, log(n), and the
source's infinite-quotient Bessel error separately.
"""

import argparse
from fractions import Fraction
import json
from math import ceil

from brent_mcmillan_interval import integer_log


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def finite_b1_sums(n: int, last_index: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return S_N, V_N, b_(N+1), H_(N+1) for B1's positive series."""
    if n < 1 or last_index < 0:
        raise ValueError("require n >= 1 and a nonnegative last index")
    harmonic = Fraction()
    weight = Fraction(1)
    s_sum = Fraction()
    v_sum = Fraction(1)
    for k in range(1, last_index + 2):
        harmonic += Fraction(1, k)
        weight *= Fraction(n * n, k * k)
        if k <= last_index:
            s_sum += weight * harmonic
            v_sum += weight
    return s_sum, v_sum, weight, harmonic


def exp_lower(value: int, terms: int) -> Fraction:
    if value < 0 or terms < 1:
        raise ValueError("require nonnegative exponential argument and at least one term")
    term = Fraction(1)
    total = term
    for index in range(1, terms):
        term *= Fraction(value, index)
        total += term
    return total


def rigorous_interval(n: int, last_index: int, exp_terms: int, log_digits: int) -> dict[str, object]:
    s_sum, v_sum, next_weight, next_harmonic = finite_b1_sums(n, last_index)
    ratio = Fraction(n * n, (last_index + 2) ** 2)
    if ratio >= 1:
        raise ValueError("require n^2/(N+2)^2 < 1 for the positive B1 tail bound")
    s_tail = next_weight * (next_harmonic / (1 - ratio) + ratio / ((last_index + 2) * (1 - ratio) ** 2))
    if log_digits < 1:
        raise ValueError("require positive log digits")
    log_lower, log_upper = integer_log(n, Fraction(1, 10**log_digits))
    bessel_upper = Fraction(22, 7) / exp_lower(4 * n, exp_terms)
    lower = s_sum / v_sum - log_upper - bessel_upper
    upper = (s_sum + s_tail) / v_sum - log_lower
    return {
        "mode": "rigorous_fraction_interval",
        "n": n,
        "last_included_index_N": last_index,
        "lower": fraction_text(lower),
        "upper": fraction_text(upper),
        "positive_series_tail_upper": fraction_text(s_tail),
        "log_bounds": [fraction_text(log_lower), fraction_text(log_upper)],
        "bessel_error_upper": fraction_text(bessel_upper),
        "proof_scope": "S_N/V_N is below the infinite S/V because it is a weighted average of increasing H_k values. The positive tail bounds S-S_N, V is at least V_N, and the source identity gives gamma above U/V minus pi*exp(-4n).",
    }


def evaluate(n: int, terms: int, digits: int) -> dict[str, object]:
    if n < 1 or terms < 1 or digits < 20:
        raise ValueError("require n >= 1, terms >= 1, and digits >= 20")
    try:
        import mpmath as mp
    except ImportError as error:
        raise ValueError("numeric mode requires mpmath in the selected Python environment") from error
    with mp.workdps(digits):
        log_n = mp.log(n)
        b = mp.mpf(1)
        a = -log_n
        u = a
        v = b
        for k in range(1, terms):
            b = b * n * n / (k * k)
            a = (a * n * n / k + b) / k
            u += a
            v += b
        approximation = u / v
        source_upper = mp.pi * mp.exp(-4 * n)
        return {
            "n": n,
            "terms": terms,
            "working_digits": digits,
            "b1_finite_quotient": mp.nstr(approximation, digits - 5),
            "source_bessel_error_upper_for_infinite_quotient": mp.nstr(source_upper, digits - 5),
            "scope": "The source proves 0 < U(n)/V(n)-gamma < pi*exp(-4n) for its infinite sums. This finite floating-point recurrence is a numerical evaluation, not a directed enclosure.",
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int)
    parser.add_argument("--terms", type=int)
    parser.add_argument("--digits", type=int, default=80)
    parser.add_argument("--rigorous", action="store_true")
    parser.add_argument("--tail-index", type=int)
    parser.add_argument("--exp-terms", type=int, default=80)
    parser.add_argument("--log-digits", type=int, default=40)
    args = parser.parse_args()
    try:
        if args.rigorous:
            tail_index = args.tail_index if args.tail_index is not None else max(12, 4 * args.n)
            result = rigorous_interval(args.n, tail_index, args.exp_terms, args.log_digits)
        else:
            terms = args.terms if args.terms is not None else max(20, ceil(3 * args.n + args.digits / 5))
            result = evaluate(args.n, terms, args.digits)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
