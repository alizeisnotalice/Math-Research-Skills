---
name: probability-spectral-perturbation-certificates
description: Audit finite reversible chains and finite-dimensional spectral families for gap, crossing, derivative, response, or rigorously enclosed eigenvalue claims.
---

# Spectral perturbation and strict gap certificates

Use this skill for a finite reversible kernel or finite-dimensional self-adjoint
family.  State the state space, matrix convention, stationary law, inner
product, update clock, parameter, and target.  The scoped source interfaces
are in [method notes](references/method.md) and [sources](references/sources.md).

For a fixed reversible kernel, use the Dirichlet form and Rayleigh quotient for
the Poincaré gap.  When the stationary law moves, differentiate the symmetric
conjugate or work in the moving weighted inner product.  At a repeated
eigenvalue, use an isolated spectral subspace and its directional compression.
A stationary-law derivative or a static correlation inequality does not give a
spectral-gap derivative.

## Match the certificate to the conclusion

- Full-chain mixing needs a Poincaré or conductance inequality on all functions
  and a laziness or absolute-spectrum condition.  A restricted inequality after
  a projection applies only to the stated projected observables.
- An ordered eigenvalue needs an all-index enclosure with strict separation.
  A residual estimate, an invariant-block interval, or overlapping clusters
  do not identify its order by themselves.
- Record exact arithmetic, validated intervals, and floating-point exploration
  separately.  A finite instance does not establish a uniform parameter claim.

Read [the finite lazy-chain branch](references/lazy-chain-mixing.md) for a
mixing conclusion.  For a supplied regular graph with a claimed Ramanujan-type
bound, use [rational inertia](references/regular-graph-rational-inertia.md).
It checks one adjacency matrix and does not construct a family.

Historical evidence outside the installed package is located through
[the evidence guide](../math-research/references/evidence.md).
