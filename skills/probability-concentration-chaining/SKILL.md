---
name: probability-concentration-chaining
description: Select scoped concentration, deviation, chaining, anti-concentration, and certificate methods after matching the probability model, tail regime, and exact parameters.
---

# Concentration, large deviations, and chaining

Use this skill to bound a random variable or process only after fixing its law, event, target scale, and permitted source interface. It does not turn a tail estimate into a small-ball estimate, a finite calculation into a uniform theorem, or a source card into blanket approval of its paper.

## Start with five gates

1. **Object and regime.** State a scalar/sum, matrix, martingale, process supremum, empirical statistic, finite law, or Poisson process; then say upper, lower, two-sided, interval/small-ball, fixed-time, time-uniform, finite-sample, moderate-deviation, or asymptotic.
2. **Dependence.** Record independent coordinates, sampling without replacement/exchangeability, an actual filtration and conditional law, Markov dependence, arbitrary joint law, or a specified Gaussian process. Never replace one model by another.
3. **Parameters and constants.** Keep the deviation level, confidence, variance/bracket proxy, range/envelope, dimension factor, time horizon, and (for a process) semimetric, gamma/entropy functional, diameter, basepoint, and any approximation error visible.
4. **Transfer mechanism.** Prove how the target produces the theorem's summands, replacements, increments, coupling, or supermartingale. The cited theorem does not furnish this reduction.
5. **Scope.** Select a theorem row in [accepted theorem scopes](references/accepted-theorem-scopes.md); use its exact hypotheses, normalization, constants, exceptions, and exclusions.

## Route by problem type

- **Independent scalar, matrix, or permutation statistic:** choose a row that matches boundedness, weights, replacement structure, and finite-array/sampling convention. Do not use iid formulas for merely exchangeable or dependent inputs.
- **Function of product inputs:** use the stated coordinate-replacement or certificate interface. For adaptive positive certificates, read [adaptive positive certificates](references/adaptive-positive-certificates.md); every successful transaction needs its own newly queried positive certificate and the remaining conditional product law.
- **Martingale or time-uniform crossing:** specify the filtration, conditional means, one-sided increment cap, and predictable (not realized) variance/bracket. Do not infer a two-sided or Cramér statement without its separate sign and scale conditions.
- **Process supremum or generic chaining:** state the increment tail class and semimetric(s); retain gamma/entropy and diameter terms and add a separate bound at the basepoint. A bound for $X_t-X_{t_0}$ is not automatically a bound for $\sup_t X_t$.
- **Gaussian coupling, maxima, or short bands:** keep coupling and anti-concentration distinct. An interval/CDF conclusion needs a separately matched concentration-function or Gaussian anti-concentration row.
- **LDP, MDP, or high excursion:** state speed, topology, threshold regime, and every scale restriction. Concentration by itself is not an LDP; a local high-threshold asymptotic is not a finite-threshold bound.

## Specialized reusable components

- For a fixed finite family of labelled Poisson witnesses, with a finite nonatomic intensity space and injective slot assignments, read [Poisson witness lower tail](references/poisson-witness-lower-tail.md). Keep repeated labels and all partial-matching diagrams.
- For an all-cut expansion hypothesis on a finite graph, read [edge-splitting](references/edge-splitting.md). Its sufficient union-bound condition certifies existence only; failure of that condition is not nonexistence.
- For an arbitrary correlated finite binary law and a fixed-coordinate upper-tail witness, read [upper-tail conditional sampling](references/upper-tail-sampling.md). It neither assumes independence nor proves a repetition theorem.

## Non-negotiable distinctions

- Upper/lower/two-sided tails, interval probabilities, and small-ball estimates have different interfaces.
- Predictable conditional variance, realized quadratic variation, and unconditional variance are not interchangeable.
- A coupling controls joint-space distance; distributional transfer also needs a modulus/anti-concentration estimate.
- Exact finite profiles, enumeration, and numerical checks are instance evidence only.
- Near equality, stability, bootstrap, full empirical-process, and optimizer claims require their own admitted row; do not promote an exact or finite-vector statement.

## Evidence and source status

The detailed ledger preserves the historical 30 scoped concentration uses, including held and excluded routes, plus their limits. The four specialized components have their own linked interfaces. Local evidence pointers can be unavailable in portable copies; see [evidence access](../math-research/references/evidence.md).
