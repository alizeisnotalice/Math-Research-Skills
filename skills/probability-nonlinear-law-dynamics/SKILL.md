---
name: probability-nonlinear-law-dynamics
description: Analyze fixed points and iteration of probability-law operators, including nested stationary-law maps, nonlinear Markov updates, and recursive distributional equations; use when the proof needs operator-specific existence, uniqueness, stability, or global convergence.
---

# Nonlinear probability-law dynamics

Use this skill when a probability law is itself the state of a nonlinear map. State the operator, its domain, and its topology before selecting a result. Read [method gates](references/method.md) for the matching conditions and [source ledger](references/sources.md) for source-specific statements. The [positive](examples/positive.md) and [negative](examples/negative.md) examples give scoped applications and transfer failures.

Keep these models separate.

1. A nested stationary-law map is `Phi(theta) = pi(K_theta)`. Mixing of the frozen kernel `K_theta` does not establish convergence of `theta[n+1] = Phi(theta[n])`.
2. A nonlinear Markov update has the form `mu[n+1] = mu[n] K_{mu[n]}` or a specified law-dependent flow. Its results require the same update, state space, and topology.
3. A recursive distributional equation has `T(mu) = Law(g(xi, X_1, ..., X_m))` with independent copies and specified innovations. Contraction or classification results require that representation or a proved reduction.

Separate existence, uniqueness, local stability, convergence of every orbit, and an almost-everywhere basin claim. Numerical iteration, a density-only condition, or a rate for an inner chain is not a theorem for a different law operator. The source ledger records scoped uses and unresolved interfaces. Candidate records and historical reading data remain provenance, not theorem approval.

## Finite purity update

For a supplied finite probability vector, [the purity-update certificate](references/finite-purity-squaring.md) checks the defect reduction and maximum-atom tail under squared normalization. Its small-root branch requires current defect strictly below `1/2`.

## OpenAI components

- [Tree-posterior components](references/openai-tree-posterior-components.md)
