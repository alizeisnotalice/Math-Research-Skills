---
name: probability-markov-spectral-mixing
description: Analyze mixing, spectral gaps and update clocks for a specified finite reversible Markov chain, including heat-bath Glauber dynamics, graph geometry and ferromagnetic Ising correlation bounds.
---

# Markov spectral gaps and Ising Glauber dynamics

Use this skill for finite reversible-chain mixing or spectral-gap questions, including Ising heat-bath Glauber dynamics. State the state space, stationary law and fields, update rule, vertex rates, clock convention, generator/kernel, and Dirichlet form before comparing gaps. Read [formulas and correlation hypotheses](references/method.md) and [source scopes](references/sources.md).

For Ising edge-parameter claims, keep stationary correlation monotonicity, finite-time behaviour, and eigenvalue monotonicity distinct. The arbitrary-graph nonzero-field gap route remains unresolved in the recorded sources. A static correlation sign does not establish a spectral-gap sign.

For a differentiable reversible family with Gibbs law \(\pi_\theta\), account for both density factors in the symmetric conjugate. Along a simple normalised eigenbranch, evaluate the full scalar derivative. At a repeated eigenvalue use an isolated spectral subspace and a directional compressed derivative. Finite enumeration and floating-point spectra are search evidence.

- Use [exact residual sampling](references/exact-residual-sampling.md) only after a finite rational kernel has an explicit total-variation or pointwise certificate and denominator. It is an exact-sampling wrapper.
- Use the [finite Chernoff certificate](references/finite-markov-chernoff.md) for a supplied tilted-operator bound on a stationary rational chain.
- Use the [stationary increment audit](references/openai_critical_slowing_stationary_increment.md) for the stated discrete second moment and Dirichlet form.
- For bounded lazy clocks, retain the fixed-shift and uniformity requirements in [the shifted-Poisson interface](references/openai_shifted_poisson_clock.md).

Further current finite interfaces are listed in [the OpenAI source cards](references/openai-wave4-pa3.md) and [SK interfaces](references/openai-sk-finite-interfaces.md). Historical material is located through [the central evidence guide](../math-research/references/evidence.md).
