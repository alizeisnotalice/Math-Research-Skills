---
name: probability-brownian-potential-fractals
description: Analyze Brownian path sets, planar SLE and loop-erasure interfaces, potential-capacity comparisons, or reflected Brownian couplings using the exact source scopes in the accompanying references.
---

# Brownian path, potential, and coupling methods

Use this skill when a proof concerns Brownian ranges, cut points, disconnection, planar SLE or loop-erasure, potential kernels and capacity, or reflected-Brownian couplings.

## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

## Workflow

1. **Name the object and event.** Distinguish a trace from its frontier, a cut-time set from its image, a Jordan arc from a connected subset, and disconnection from nonintersection. State the time interval, stopping rule, ambient metric, and whether the claim is almost sure, positive probability, a dimension, or an exponent.
2. **Select an admitted source scope.** Read [sources.md](references/sources.md) for its exact use, hypotheses, proof interface, and transfer limits. The full standard row and reviewer authority are in source_admissions.json（本机附件：`references/source_admissions.json`）. A paper’s presence here does not qualify every theorem in it.
3. **Keep the proof chain explicit.** List every external exponent, separation estimate, conformal transfer, regularity condition, and convergence step. If one is not included in the admitted scope, mark it as an unresolved dependency instead of silently importing it.
4. **For a coupling, verify both marginals and the pair law.** Specify the reflection rule, shared or transformed noise, common filtration, coupling class, stopping time, and post-meeting continuation. A single-particle Skorokhod result does not establish a pair coupling.
5. **Separate rates and conclusions.** Keep generator normalization, spatial-distance decay, survival probability, meeting-time tails, total variation, and spectral bounds distinct. A survival lower bound is not a meeting-tail upper bound.
6. **Use the worked checks.** See [positive cases](examples/positive.md) and [missing-condition cases](examples/negative.md).

## Scope boundaries

This is a scoped Brownian source toolkit, not a claim that the full historical Brownian source ledger is high-qualified. The current exact union has 35 accepted scoped works (34 papers and one book) and five current held works; it adds no global full-read credit. M0224 is one acquired book with four complete used units totaling 107 physical pages, not a whole-book read. See the source index for exact counts and work-by-work limits.

The held work-level claims are M0171, M0175, M0192, M0201, and W08-R003 general Lambda. M0196 Proposition 1 has a separate adopted scope; its earlier held row is historical. A separately accepted disk-only W08-R003 use is retained as historical bounded scope and is not counted in the current 35-row union.

## References

- [Proof interfaces and method map](references/method.md)
- [Admitted source scopes and authorities](references/sources.md)
- Exact source admissions（本机附件：`references/source_admissions.json`）
- Historical hold and bounded-scope dispositions（本机附件：`references/held_and_historical_dispositions.json`）
- [Positive examples](examples/positive.md)
- [Missing-condition examples](examples/negative.md)

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。
