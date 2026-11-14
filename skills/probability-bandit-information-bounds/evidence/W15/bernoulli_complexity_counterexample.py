"""Numerically check Degenne (2023), Theorem 10's two-arm Bernoulli witness.

Uses only Python's decimal Decimal arithmetic (including Decimal.ln) so the
small-x calculation is not lost to cancellation. This is numerical evidence,
not a proof of the limiting theorem.
"""
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 100
D = Decimal


def kl_bernoulli(p: Decimal, q: Decimal) -> Decimal:
    return p * (p / q).ln() + (1 - p) * ((1 - p) / (1 - q)).ln()


def inverse_static_difficulty(p: Decimal, q: Decimal) -> Decimal:
    """Return H_Csp((p,q))^{-1}; supports either arm order."""
    high, low = max(p, q), min(p, q)
    chernoff_mean = ((1 - low) / (1 - high)).ln() / (
        (high * (1 - low) / ((1 - high) * low)).ln()
    )
    return kl_bernoulli(chernoff_mean, high)


def witness_ratio(x: Decimal) -> tuple[Decimal, Decimal]:
    mu1, mu2 = x * (1 + x), x
    lambda1 = (x / 2, x)
    lambda2 = (x * (1 + x), D(1) / 2)
    term1 = inverse_static_difficulty(*lambda1) / kl_bernoulli(mu1, lambda1[0])
    term2 = inverse_static_difficulty(*lambda2) / kl_bernoulli(mu2, lambda2[1])
    return term1 + term2, term1


def main() -> None:
    x = D("1e-9")
    ratio, first_term = witness_ratio(x)
    out = (
        "Degenne (2023), Theorem 10 two-arm Bernoulli witness\n"
        f"Decimal precision: {getcontext().prec}\n"
        f"x: {x}\n"
        f"mu(x): ({x * (1 + x)}, {x})\n"
        f"lambda1(x): ({x / 2}, {x})\n"
        f"lambda2(x): ({x * (1 + x)}, {D(1) / 2})\n"
        f"Corollary-4 difficulty-ratio lower bound: {ratio}\n"
        f"Decimal lower bound > 1: {ratio > 1}\n"
        f"First summand: {first_term}\n"
        "Interpretation: one finite numerical witness only; the universal theorem and limit are proved in the source, not by this computation.\n"
    )
    print(out, end="")
    result = Path(__file__).with_name("bernoulli_complexity_counterexample_results.txt")
    result.write_text(out)


if __name__ == "__main__":
    main()
