# Missing hypotheses and invalid inferences

## The domain is part of an SOS certificate

On `[1,2]`, `x²−1=3(x−1)²+2(2−x)(x−1)` certifies `x²≥1`. If the box constraint is removed, `x=0` has `x²=0`; the identity does not certify a global lower bound because the generator `(2−x)(x−1)` is negative there. The exact result is bundled with the [positive case](positive.md).

## Farkas contradiction

The pair `x≥1` and `−x≥0` has nonnegative multipliers `(1,1)` whose weighted left-hand side is `0` and right-hand side is `1`. Any feasible point would imply `0≥1`, a strict contradiction. Exact rational multipliers certify infeasibility; a floating solver status alone does not.

## Decimal MIP repair is not exact feasibility

For integer `x≥0` with rational row `y−x≥1/3`, fixing `x=1` admits exact repair `y=4/3`. The decimal `1.333333` misses the row by `1/3−333333/1000000=1/3000000`. One failed fixed-integer repair would not prove the whole MIP infeasible. The exact repair case and code are in the R04 case packet（本机附件：`evidence/R04/optimization_whole_entry_cases_v1/cases.txt`）.

## Rounded activity screen

If the true activity is enclosed by `[s−μ,s+μ]` for row `a·x≥b`, accept the row only when `s−μ≥b`; certify violation only when `s+μ<b`. If the interval touches `b`, use the exact fallback. Reversing those directions can reject a feasible point or accept an infeasible one. This is the accepted S026 screen, not a claim about the full solver implementation.

## KKT stationarity without feasibility

For convex differentiable programs, a valid primal/dual pair with correct multiplier signs, stationarity, and complementary slackness is sufficient for global optimality. Stationarity alone, or a negative multiplier, is not a certificate. Slater and attainment hypotheses concern the separate necessity/duality direction; they are not prerequisites once a complete feasible KKT certificate has been checked.

## Finite-order SOS and box convergence

An exact finite SOS identity proves only its displayed polynomial inequality on its declared domain. For a nested-box hierarchy, degree-preserving inclusion gives monotone bounds; it does not by itself prove the full source algorithm, finite termination, or that a returned point is globally optimal. The scoped S024 use is the finite certificate and nested-box inclusion only.

## Quasi branch-and-bound

A quasi-lower bound may be valid only on boxes containing a global minimizer. It cannot be used to prune an arbitrary box without the minimizer-retention argument. The accepted S023 scope is qBnB2 plus the constrained sampling/BFS interface and Appendix Theorem 2 under its uniform `ψ(r)→0` condition; qBnB3/Newton claims are outside this scope.

The exact packet is cases.md（本机附件：`evidence/R04/optimization_whole_entry_cases_v1/cases.txt`）, its executable cases.py（本机附件：`evidence/R04/optimization_whole_entry_cases_v1/cases.py`）, and exact output cases.result.json（本机附件：`evidence/R04/optimization_whole_entry_cases_v1/cases.result.json`）.
