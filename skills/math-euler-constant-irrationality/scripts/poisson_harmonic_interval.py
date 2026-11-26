"""Enclose Euler's gamma by Poisson harmonic expectations in exact arithmetic."""

import argparse
import json
import runpy
from fractions import Fraction
from pathlib import Path


def gamma_interval(power: int, terms: int, log_terms: int) -> tuple[Fraction, Fraction]:
    if power < 1 or terms < (1 << power) - 1 or log_terms < 1:
        raise ValueError("require power >= 1, terms >= 2**power - 1, log_terms >= 1")

    rate = 1 << power
    exponential_term = exponential_lower = Fraction(1)
    harmonic_sum = Fraction(0)
    for k in range(1, terms + 1):
        exponential_term *= Fraction(rate, k)
        harmonic_sum += (-1) ** (k + 1) * exponential_term / k
        exponential_lower += exponential_term

    k = terms + 1
    next_harmonic_term = (-1) ** (k + 1) * exponential_term * rate / (k * k)
    log_script = (
        Path(__file__).resolve().parents[2] / "math-sondow-log-fractional-certificate"
        / "scripts" / "sondow_certificate.py"
    )
    log_lower, log_upper = runpy.run_path(str(log_script))["log_unit_bounds"](
        Fraction(2), log_terms
    )
    lower = (
        harmonic_sum + min(0, next_harmonic_term)
        - power * log_upper - 1 / (rate * exponential_lower)
    )
    upper = harmonic_sum + max(0, next_harmonic_term) - power * log_lower
    return lower, upper


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--power", type=int, default=4)
    parser.add_argument("--terms", type=int)
    parser.add_argument("--log-terms", type=int)
    parser.add_argument("--candidate", type=Fraction, help="test the sign of q*gamma - p")
    args = parser.parse_args()
    if args.power < 1:
        parser.error("require power >= 1")
    rate = 1 << args.power
    terms = args.terms if args.terms is not None else 4 * rate
    log_terms = args.log_terms if args.log_terms is not None else rate // 2 + 1
    try:
        lower, upper = gamma_interval(args.power, terms, log_terms)
    except ValueError as exc:
        parser.error(str(exc))
    result = {
        "power": args.power,
        "rate": rate,
        "terms": terms,
        "log_terms": log_terms,
        "gamma_interval": [str(lower), str(upper)],
    }
    if args.candidate is not None:
        p, q = args.candidate.numerator, args.candidate.denominator
        residual_lower, residual_upper = q * lower - p, q * upper - p
        result["candidate"] = str(args.candidate)
        result["scaled_residual_interval"] = [str(residual_lower), str(residual_upper)]
        result["candidate_excluded"] = residual_lower > 0 or residual_upper < 0
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
