# Method selection and proof workflow

## 1. State the target contract

Write the target as a function `f` on its exact domain and say whether the required output is a `{0,1}` coin, an estimator in `[0,∞)`, a categorical vertex, a sample from a target law, or an event with probability `exp(-∫φ)`. Record the unknown inputs and their independence. State which fair coins, uniforms, Poisson processes, exponentials, and known-parameter coins are available. Treat p-tosses and auxiliary randomness as separate resources.

## 2. Fixed-depth events

For a deterministic depth `N`, a terminal event has

`P_p(E)=Σ_(j=0)^N A_(N,j) p^j(1-p)^(N-j)`, with integer `0≤A_(N,j)≤binom(N,j)`.

This is the pure p-word event criterion. In normalized Bernstein form `β_(N,j)=A_(N,j)/binom(N,j)`. Degree elevation preserves `[0,1]` by convex averaging, but it does not make a noninteger coefficient into an event count. If extra independent randomness implements coefficients, use the matching Goyal finite-depth criterion and keep that model explicit. Wästlund’s fixed-degree finiteness result gives existence of some finite maximal depth for its integer-polynomial class; it is not a sharp or effective formula for `N(m)`.

Guan–Wang Theorem 2(i), scalar `d=1`, `r=0/1`, gives an endpoint-aware *bias certificate* for `B_n f`, not an exact `f`-factory. Do not replace a surrogate by its target when the bias is nonzero.

## 3. Random stopping and exact factories

The accepted rows support several different routes; do not merge their conditions:

- Nacu–Peres envelope characterization separates lower/upper Bernstein envelopes and stopping tails. Holtz–Nazarov–Peres is admitted here only for its stated necessity/interface claims and consistent-scheme lemmas, not as a blanket sufficiency construction.
- Mendo’s power-series factory needs the nonnegative summable coefficient representation. Reverse-time martingale sampling needs the source’s nested conditional relations and its own iteration clock.
- Huber’s linear/logistic constructions use their stated martingale kernels or exponential race. Exactness under a.s. absorption is separate from any stronger uniform-tail or moment claim.
- The Keane–O’Brien geometric mixture is admitted when the actual computable residual arrays and sample sizes are supplied. At level `k`, the sample mean denominator is `η_k`; the printed `BinCount/L` in its pseudocode is not the Eq. (2) formula.
- The debiased factory is admitted as a conditional coefficient interface: all lower and upper hypergeometric compatibility inequalities, the polynomial gap, the upper buffer, the starting-index buffer, and a verified remainder must be supplied. HNP Theorem 8 supplies an existence result for the compatible arrays and rate. Actual coefficients, the start threshold, and remainder constants are supplied or separately derived before an operational application. [HNP envelope audit](hnp-envelope-adjudication.md).
- Flegal–Herbei’s accepted interface is a smooth concave extension on its restricted parameter range. Initialize the first operational threshold by testing the raw coefficient interval at `N0`; only later doublings use the reverse-time transfer. The printed iteration-tail wording is not admitted as a toss-tail bound.

## 4. Structured outputs and composition

For a finite Bernoulli race, implement nonnegative Bernstein monomials and coefficient randomization exactly; require positive total weight wherever a.s. termination is claimed. For flow polytopes, use the admitted standalone weight identities with a separate correct race; the literal rejected algorithm is excluded. The Dughmi and Schmon races have distinct proposal/acceptance conventions, so preserve each row’s formula.

For an exponential event in diffusion simulation, choose the uniform-area alternating-event construction only under `0≤φ≤1/T`, or the Poisson zero-under-graph event under a fixed finite envelope `M`. These are separate randomization models, not p-coin factories.

For an MCMC odds merger, first verify valid independent leaf coins and factorization. A finite recursive two-coin tree multiplies odds by rejection-until-agreement; its expected-cost recursion needs finite child expectations and fresh independent attempts. It supplies no leaf factory or general complexity bound. For recursive perfect simulation, local correctness plus a.s. finite recursion gives exactness, not finite expected runtime.

## 5. Proof and audit checklist

1. Match the input law, allowed randomness, domain, endpoint cases, and output type.
2. Quote the theorem and physical/printed locator from its scoped card.
3. Check every coefficient, compatibility, positivity, envelope, or independence assumption before invoking the construction.
4. Prove exactness and a.s. termination; then separately derive any expectation or tail claim.
5. State the exact cost clock and retain constants and index conversions.
6. Give one exact positive example and one missing-condition example. Use rational computation for finite checks; do not treat computation as a proof for all inputs.
7. Keep rejected branches, unresolved source mismatches, and open target claims visible.
