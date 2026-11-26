---
name: probability-bernoulli-factory
description: Select and audit exact coin factories, fixed-depth event representations, and random-stopping constructions with assumptions, output types, and cost clocks explicit.
metadata:
  short-description: Exact Bernoulli factories and stopping rules
---

# Bernoulli-factory analysis

Use this skill for exact sampling from unknown biased coins, finite-depth event representations, or random-stopping factories. Fix the parameter domain, input-coin model, permitted auxiliary randomness, requested output, endpoint behavior, and cost clock before selecting a construction. A Bernoulli factory returns a bit of probability \(f(p)\). An unbiased estimator, categorical output, and acceptance event each need their own contract.

## Choose the construction

- For exactly \(N\) input tosses, represent the event by a degree-\(N\) Bernstein polynomial. With input tosses alone its unnormalised coefficients are integer event counts in \([0,\binom Nj]\). With allowed independent auxiliary randomness, coefficients in \([0,1]\) can encode the matching finite-depth event.
- For an almost-surely finite stopping time, use an applicable envelope, series, reverse-time, recursive, or residual-mixture construction. Prove almost-sure termination separately from finite mean cost and tail bounds.
- For categorical/vector output or nonnegative unbiased estimators, preserve that output contract. Do not relabel it a Bernoulli factory.

## Record the cost and boundary

State whether cost counts unknown-\(p\) tosses, fair bits, uniforms, iterations, Poisson points, leaf calls, or every primitive operation. An iteration bound becomes a toss bound only with an explicit conversion. Check \(p=0,1\) when they are in the domain. An interior lower bound does not establish endpoint behavior.

Read [method selection](references/method.md) for construction gates, [source cards](references/sources.md) for theorem-specific scope, and the [positive](examples/positive.md) and [negative](examples/negative.md) cases for boundary examples. The [finite debiasing ledger](references/finite_debiased_ledger.md) verifies supplied finite Bernstein coefficients, rational truncation, expectation identities, point bias, and input-coin cost. Its [HNP dependency audit](references/hnp-envelope-adjudication.md) records the additional envelope assumptions.

## Source-use boundary

For a published theorem, verify the edition and the cited statement. For a preprint, verify the version, proof interface, and every transferred hypothesis. Historical ledgers remain available through [the central evidence guide](../math-research/references/evidence.md); they do not widen a construction's stated output or cost guarantee.
