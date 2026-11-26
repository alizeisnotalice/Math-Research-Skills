"""Replay the exact truncation and perturbation witnesses for Gale's example."""

import argparse
import json
from fractions import Fraction


def gale_witness(cap: int) -> dict[str, object]:
    if cap < 1:
        raise ValueError("the finite constraint cap must be positive")

    # y=(1,-cap) meets every listed dual constraint and the objective cap.
    finite_dual = (1, -cap)
    worst_listed_slack = cap * finite_dual[0] + finite_dual[1]
    omitted_index = cap + 1
    omitted_violation = omitted_index * finite_dual[0] + finite_dual[1]
    if worst_listed_slack != 0 or omitted_violation != 1:
        raise ArithmeticError("unexpected Gale witness")

    # For b=(1,1/cap), the sole nonzero primal variable is x_cap=1/cap.
    weight = Fraction(1, cap)
    if cap * weight != 1:
        raise ArithmeticError("bad perturbation primal certificate")
    return {
        "finite_cap": cap,
        "finite_dual_optimum": 1,
        "finite_dual_optimizer": finite_dual,
        "first_omitted_constraint": omitted_index,
        "violation": omitted_violation,
        "infinite_dual_optimum_from_unbounded_slopes": 0,
        "unperturbed_primal_optimum": 1,
        "perturbed_second_rhs": str(weight),
        "perturbed_primal_support": {cap: str(weight)},
        "perturbed_primal_optimum": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cap", type=int)
    args = parser.parse_args()
    try:
        result = gale_witness(args.cap)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
