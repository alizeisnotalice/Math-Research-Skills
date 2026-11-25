# Missing-condition and rejected-scope examples

## A degree-2 test can fail while a later depth works

Let `f(p)=3p(1−p)`. Its degree-2 unnormalized count vector is `(0,3,0)`, but the middle count exceeds `binom(2,1)=2`, so it is not a depth-2 p-word event. At depth 3 its counts are `(0,3,3,0)`, within `(1,3,3,1)`, and “exactly one or two heads” implements it. A single failed depth test is not nonexistence at all depths.

## A Bernstein approximation is not an exact target

For Guan–Wang’s admitted scalar Theorem 2(i) scope, `B_n(p²)=p²+p(1−p)/n`. The theorem provides a boundary-aware bias bound for the surrogate. At interior `p`, that bias is positive; calling the surrogate an exact p² coin would be false. The old Theorem 2(ii) `r≥0` submission remains separately rejected.

## Residual or coefficient interfaces require valid data

For N002, if `f_k−q_k/4` is not pointwise in `[0,3/4]`, the recurrence does not supply a next `[0,1]` function. Also divide the observed head count by `η_L`, not by `L`. For N003, merely having a smooth target is insufficient: lower/upper compatibility, the `k₀−1` base buffer, and the verified remainder must all be supplied.

## Initialization, literal pseudocode, and output type matter

- For X012, start by comparing the first-stage uniform with the raw coefficient interval at `N₀`; apply the reverse-time transfer only after the first stage. Do not splice an unperformed coefficient-calibration stage into the operational initialization.
- For X045, the admitted result is Theorem 3’s standalone balance and positivity with a separate correct Bernstein race. The literal Algorithm 1 has an independently recorded incorrect marginal on an admissible instance.
- Jacob–Thiery’s accepted output is a nonnegative unbiased estimator, not a Bernoulli bit. FTPS local correctness alone does not imply exactness without a.s. finite recursion.

A positive minimum over `(0,1)` cannot be assumed when either `f` or `1−f` vanishes at an endpoint. Likewise, a.s. termination, finite mean cost, a uniform tail, and optimality are separate claims.
