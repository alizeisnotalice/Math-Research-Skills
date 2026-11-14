"""Finite sanity check of the forward/filtered identity in a trivial observation case.

This exact-formula check illustrates the theorem for one two-state CTMC only;
it is not a proof of the general martingale-problem result.
"""
from __future__ import annotations

import json
import math
import platform
from pathlib import Path


def p_state_1(t: float) -> float:
    """P(X_t=1) for rates 0->1 at 2 and 1->0 at 1, started at 0."""
    return (2.0 / 3.0) * (1.0 - math.exp(-3.0 * t))


def forward_derivative(t: float) -> float:
    p = p_state_1(t)
    # For f=1_{state 1}, Qf=(2,-1), so nu_t Qf=2(1-p)-p.
    return 2.0 * (1.0 - p) - p


def integrated_derivative(t: float) -> float:
    # The same quantity is 2 exp(-3s); integrate analytically on [0,t].
    return (2.0 / 3.0) * (1.0 - math.exp(-3.0 * t))


def main() -> None:
    times = [0.0, 0.1, 0.5, 1.0, 2.0, 5.0]
    rows = []
    for t in times:
        lhs = p_state_1(t)
        rhs = integrated_derivative(t)
        rows.append({
            "t": t,
            "nu_t_f": lhs,
            "nu_0_f_plus_integral_nu_s_Af_ds": rhs,
            "instantaneous_forward_derivative": forward_derivative(t),
            "absolute_forward_identity_error": abs(lhs - rhs),
        })
        assert abs(lhs - rhs) <= 1e-14

    result = {
        "check": "forward equation and filtered-martingale identity for a two-state CTMC with constant observation",
        "generator_rows": [[-2, 2], [1, -1]],
        "initial_law": [1, 0],
        "observation_map": "constant; observation filtration is trivial",
        "test_function": "f(x)=1_{x=1}",
        "derivation": "p_1(t)=2/3(1-exp(-3t)); (Af)(0)=2, (Af)(1)=-1; nu_s Af=2 exp(-3s); hence p_1(t)-p_1(0)=integral_0^t nu_s Af ds.",
        "rows": rows,
        "max_absolute_error": max(r["absolute_forward_identity_error"] for r in rows),
        "runtime": f"Python {platform.python_version()}",
        "scope_limit": "finite example only; it does not prove Theorem 3.2, Markov uniqueness, or any queueing-model interface",
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
