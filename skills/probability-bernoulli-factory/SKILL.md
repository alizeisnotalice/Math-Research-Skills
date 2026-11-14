---
name: probability-bernoulli-factory
description: Analyze exact Bernoulli factories, finite coin-flipping degree, and stopping-time tail or moment claims with their model assumptions explicit.
metadata:
  short-description: Bernoulli-factory proofs and limits
---

# Bernoulli-factory analysis

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill when a problem asks which functions can be simulated exactly from biased coins, how many input tosses are needed, or what a stopping-time tail implies about regularity.

First specify the input model: unknown-bias `p`-coin, any auxiliary fair coins or uniforms, admissible parameter set, and whether `N` counts only `p`-coin tosses, fair-coin tosses as well, all primitive random bits, or algorithmic stages. Preserve the paired p/fair input convention of Holtz–Nazarov–Peres and the iteration-count convention of the general Łatuszyński algorithm until an implementation gives a cost conversion. For Flegal–Herbei, separately record that the theorem calls `n` iterations while its algorithm doubles the input prefix `n`; the source does not reconcile those indices. Separate finite deterministic-depth events from almost-surely terminating factories and from factories with fast or polynomial tails.

For exact stopping-time claims, use nested lower and upper Bernstein envelopes and the exact identity between the envelope gap and `P_p(N>n)`. Translate tail bounds to moments with the standard tail-sum formula. Keep pointwise-in-`p` finiteness distinct from uniform tail or moment bounds.

For integer-coefficient probability polynomials, use finite-event Bernstein coefficients only for the finite-depth model. The fixed-degree finiteness theorem does not provide a sharp degree bound. Consult [method notes](references/method.md), [source evidence](references/sources.md), and the [positive](examples/positive.md) and [negative](examples/negative.md) examples.

Evidence state: this reviewed method library is based on 30 complete source reads and a 54-item candidate ledger, including one complete short contribution excerpt. The latest batches add practical envelope cascades, a model-specific genetics factory with an explicitly recorded theorem/proof mismatch, a bounded debiasing construction with a sufficient smoothness-to-moment implication, factorized MCMC factories, and local-correctness perfect simulation. These results do not close the pointwise general moment classification. This evidence set does not establish the sharp general degree bound. R08 has independently accepted the 30-source read-and-claim set; the 24 unread candidates remain excluded.
