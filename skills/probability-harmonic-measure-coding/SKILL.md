---
name: probability-harmonic-measure-coding
description: Analyze harmonic and boundary measures on trees, symbolic codings, exact dimensions, and equivalence or singularity of pushforward measures on a common metric space.
---

# Harmonic measures, tree boundaries, and coding comparisons

Use this skill for probability flows on rooted trees, random-walk boundary laws, symbolic or geometric codings, and comparisons of two coded measures. Establish the tree, the probability law, and the common target space before choosing a theorem. A nonlinear boundary capacity needs countable additivity and total mass one before probability tools apply.

## Common setup

For a comparison, write

`ν₁ = π₁# μ₁` and `ν₂ = π₂# μ₂`.

State that both are Borel probability measures on the same standard Borel space. Record endpoint treatment, overlapping cylinders, and multiple codings. Use [method notes](references/method.md) for model-specific conditions, [source status](references/sources.md) for primary-source scope, and the packaged [positive](examples/positive.md) and [negative](examples/negative.md) examples for the distinction between valid and invalid transfers.

## Route by question

- **Flow and dimension.** Verify a unit flow, its conservation equations, and the link from descendant current to cylinder mass. For exact dimension, establish a stationary ergodic boundary process, information rate, metric contraction rate, integrability, and cylinder-to-ball control.
- **Symbolic IFS or rescaling dimension.** Define the shift law and coding map first. Projection-entropy and CP-chain arguments require their own ergodicity and finite-scale hypotheses. A dimension computation does not compare measure classes.
- **Equivalence or singularity.** Work on the common target with a full-measure Borel set, a Radon–Nikodym derivative, or a valid likelihood or Hellinger criterion. Equal exact dimensions do not imply equivalence.
- **Hyperbolic-group boundaries.** Keep the group, walk support, visual or Floyd metric, Hausdorff reference, and entropy–drift assumptions fixed. Different exact dimensions imply singularity only after both exact-dimensional conclusions are available on that common boundary.
- **Base-change codings.** A digit-frequency separator needs a common compact target, unique Borel digit coding on the required full-measure set, and genuinely different digit-frequency laws.

## Boundaries

Do not identify forward child-uniform visibility with undirected simple-random-walk harmonic measure. A theorem for random Galton–Watson trees does not transfer to deterministic coding trees. A measure separator on a source boundary needs a Borel transport argument before it becomes a separator on the target space.

For a published theorem, verify the edition and cited statement. For a preprint, verify its active version, relevant proof steps, and model assumptions. Central archive material is described in [evidence and local attachments](../math-research/references/evidence.md).

## OpenAI 原稿中的方法

- [Planar height and current interfaces](references/wave4-probability-b-planar-height-current.md)
