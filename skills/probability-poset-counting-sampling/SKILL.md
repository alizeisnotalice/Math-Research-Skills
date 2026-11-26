---
name: probability-poset-counting-sampling
description: Count linear extensions and related finite poset families, derive entropy bounds, or build exact samplers; also use for finite graph-labeling peak constraints that admit a verifiable counting recurrence.
---

# Poset counting and exact sampling

Use this skill for a specified finite poset, graph-labeling peak family, or exact finite target distribution. State strict or weak order, graph or sequence peaks, endpoint and boundary convention, labels, and conditioning event. [Method guidance](references/method.md) gives the recurrence and proof obligations. Use [source cards](references/sources.md) only after matching the source convention. [Positive](examples/positive.md) and [negative](examples/negative.md) examples record finite scope and predicate failures.

For a fixed poset, count linear extensions with the ideal or maximal-element recurrence and weight exact-sampling branches by completion counts. For graph peaks, use the descending-order recurrence only after proving its state retains every future constraint. The direct strict-local-maximum predicate differs from source conventions that exclude vertices of degree zero or one.

A conjunction of comparisons can form one poset event. Peak constraints often contain disjunctions over neighbors, so they need not be linear extensions of one poset. An encoding by a union needs a disjointness proof or correct overlap weights. Keep exact counting, approximate counting, approximate sampling, and exact sampling distinct.

The free-boundary-square calculation covers only sizes 2, 3, and 4, with independent permutation enumeration through size 3 and one finite sampler trace. It does not yield a growing-square, torus, cycle, Eden-growth, regular-tree, or fixed-metric-subdivision theorem.

For an approximation of a finite uniform draw from a fixed number of fair bits, use [the fixed-bit budget calculation](references/fixed-bit-uniform-draw.md) to account for total variation and repeated draws.
