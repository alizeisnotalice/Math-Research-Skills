---
name: probability-measure-convergence
description: Analyze weak convergence, tightness, conditional laws, changing integrands, and martingale-problem limits. Use when a proof passes from stochastic models to limits of probability measures or needs a precise convergence mode.
---

# Probability measures and convergence

Fix the state space, topology, source and target laws, test class, and conclusion before choosing a theorem. For subsequence arguments, establish tightness, identify each subsequential limit with a determining class, then use uniqueness to pass to the full sequence. Record any moment or tail hypothesis separately.

| Task | Method |
| --- | --- |
| Weak-law transfer for an expectation or a probability | Use [weak convergence and varying integrands](references/source-specific-limits.md#weak-convergence-and-varying-integrands). For moving tests use the joint lower envelope and check negative tails. For set probabilities check zero boundary mass. |
| Compare two finitely supported real laws | Use the [exact scalar Wasserstein certificate](references/finite-scalar-wasserstein.md). It produces a monotone coupling, an optimal 1-Lipschitz potential, and the exact cost. |
| Conditional laws or kernels | Use the [disintegration and conditional LDP conditions](references/source-specific-limits.md#conditional-laws-disintegration-and-conditional-ldp). Specify a version, distinguish support from almost-everywhere assertions, and match topologies. |
| Process limits | Use the [tightness, path and representation conditions](references/source-specific-limits.md#tightness-paths-and-representations). Fix the path topology and justify the continuity of evaluation or of the relevant functional. |
| Martingale-problem or adapted-law limits | Use the [adapted-law conditions](references/source-specific-limits.md#martingale-problem-and-adapted-law-limits). Preserve the filtration, determining family and integrability needed to pass the conditional identities. |
| A standardized law under a supplied joint perturbation | Use the [finite standardization certificate](references/standardization-perturbation.md). Pass to an asymptotic statement only after proving the required relative perturbation tends to zero. |

For stochastic optimization objectives with changing decision sets and laws, use [probability variational limits](../probability-variational-limits/SKILL.md) alongside the exact weak-law result. Consult the [source-specific applications](references/source-specific-limits.md) for versions, adverse examples and evidence.

## OpenAI 原稿中的方法

- [Wave 4 PA3: canonical normalization with varying tests](references/openai-wave4-pa3.md)
- [Scoped FK metric and conformal convergence interfaces](references/wave4-pa2-fk-metric-convergence.md)

- [Critical-SK conditional-law references](references/openai-critical-sk-conditioning.md)

## 补充来源中的方法

- [Continued-fraction limit laws: two scoped references](references/wave5-c07-11-continued-fraction-laws.md)
