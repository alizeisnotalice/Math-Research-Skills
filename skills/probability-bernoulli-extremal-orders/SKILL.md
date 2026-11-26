---
name: probability-bernoulli-extremal-orders
description: Compute or compare independent Bernoulli sum laws exactly, apply fixed-mean and fixed-moment extremal reductions, and check dependence-sensitive convex order, atom comparisons, or Poisson approximation budgets.
---

# Bernoulli sums, extremal laws and stochastic orders

Record the number of trials, the marginal parameters, the dependence model, what is fixed and the objective. For an order comparison, name the order and which variable is intended to be smaller. For an approximation, record its error metric and the margin needed in the target inequality.

| Task | Method |
| --- | --- |
| Independent trials with rational parameters | Use [the exact count-law calculator](references/exact-bernoulli-sum.md) for the pmf, survival probabilities, and stochastic, convex, likelihood-ratio or reversed-hazard order between two given laws. |
| Compare two atoms of one independent sum | Use [Kleiner’s threshold](references/kleiner_distance_two_exact.md). Check the strict atom inequality and the necessary mean threshold separately. |
| Extremize an expectation over independent parameters with fixed cumulants | Use [Mattner’s finite support reduction](references/bernoulli-source-notes.md#fixed-mean-and-fixed-moments). Keep the endpoint multiplicities and enforce every fixed moment or cumulant. |
| Equal Bernoulli margins with arbitrary dependence | Apply the [adjacent-integer convex-order minimum](references/bernoulli-source-notes.md#dependent-common-margin-sums). Randomize the sum between the two adjacent integers at its mean, then pick a uniform subset of that size. |
| Prescribed count law or limited-wise independence | Use the [fixed-sum fiber](references/bernoulli-source-notes.md#arbitrary-dependence-with-a-fixed-sum-law) or [moment polynomial duality](../probability-moment-polynomial-duality/SKILL.md). Supply the finite joint constraints or the required count moments. |
| Likelihood-ratio, reversed-hazard or stochastic order for families | Start with the exact direction and assumptions in the [source notes](references/bernoulli-source-notes.md#stochastic-order-and-discrete-tails). The finite calculator handles instance comparisons and explicit support zeros. |
| Poisson/normal approximations or stochastic precedence | Read the matching [approximation and error section](references/bernoulli-source-notes.md#approximation-and-error-margin). Check whether the bound controls the required event or atom, and retain any independent-comparator requirement. |

For a pointwise tail objective, check survival at the target threshold. A fixed-mean convex-order result controls convex objectives such as stop-loss. Remove (p_i=0) and shift by (p_i=1) before applying a result that uses odds or requires (0<p_i<1). The exact count calculator accepts both endpoints.

For an online selection policy and offline benchmark, use [prophet inequalities](../probability-prophet-online-selection/SKILL.md). For source-specific hypotheses, historical decisions, and the excluded Auld–Neammanee square-exponential estimate, consult the [Bernoulli source notes](references/bernoulli-source-notes.md).

For standardized independent sums with variance at least one, use the [linear-exponential moment bound and exact counterexample](references/standardized-bernoulli-exponential-moments.md) before transferring a local-limit argument.
