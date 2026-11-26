---
name: probability-permutation-subset-sums
description: Analyze invariant k-subsets of random permutations through cycle counts, Poisson limits, and random subset-sum reachability while keeping fixed-k limits separate from adjacent-k monotonicity.
---

# Permutation cycles and random subset sums

Use this skill when a uniform random permutation preserves a subset of prescribed size, or when a multiset of random cycle lengths generates a subset-sum set.

For cycle counts `C_j`, a size-`k` invariant set exists exactly when integers `a_j` satisfy `0≤a_j≤C_j` and `Σ_j j a_j=k`. This is a Boolean reachability event. It is not the expected number of representations.

## Choose the probability model

- For a finite uniform permutation in `S_n`, work with its actual cycle-count law. The independent `Poisson(1/j)` vector is a conditioned representation and its unconditioned form is a fixed-coordinate limit, not a finite-n identity.
- For a fixed target `k`, a finite-dimensional Poisson limit can transfer the bounded reachability event. A growing target requires a stated uniform total-variation or coupling estimate.
- For Ewens, weighted, conditioned, or product-permutation models, retain the model-specific Poisson means and conditioning. Do not substitute the uniform-permutation law.

Read [method notes](references/method.md) for fixed-coordinate limits, labelled-cycle EGFs, conditional models, multi-target comparisons, and their exact restrictions. Read [source status](references/sources.md) before citing a source-specific result. The [positive](examples/positive.md) and [negative](examples/negative.md) examples distinguish an exact reachability calculation from the expected-count shortcut.

## Work sequence

1. State whether the target is a finite-n probability, a fixed-k limit, or a growing-k asymptotic.
2. Express preservation as a submultiset reachability event with cycle multiplicities.
3. For a fixed Poisson target, cap `Z_j` at `floor(k/j)` when forming a finite dynamic program. Explain that the cap preserves this target event.
4. For a generating function, identify whether it counts representations or the Boolean reachability event.
5. For a one-sided comparison, provide an event inclusion under a measure-preserving injection or an explicit coupling.

## Monotonicity boundary

The assertion `p(k+1)≤p(k)` is an adjacent pointwise claim. A relative asymptotic, including a log-periodic one, does not control the sign of its adjacent difference. Finite calculations certify only the tested targets.

For a published result, verify the edition and cited statement. For preprints, verify the active version, relevant proof steps, and model assumptions. Central archive material is described in [evidence and local attachments](../math-research/references/evidence.md).

## 补充来源中的方法

- [Uniform-permutation ascent walk to an arcsine occupation law](references/wave5-c08-01-permutation-walk-arcsine.md)
