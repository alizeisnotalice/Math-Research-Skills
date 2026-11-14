---
name: probability-poset-counting-sampling
description: Count linear extensions and related finite poset families, derive entropy bounds, or build exact samplers; also use for finite graph-labeling peak constraints that admit a verifiable counting recurrence.
---

# Poset counting and exact sampling

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill when a task counts linear extensions, counts permutations with local peak constraints on a graph, or needs a uniform exact sampler for one of these finite spaces.

First specify the state space precisely: the poset or graph, strict versus weak order, graph versus sequence peaks, label convention, boundary edges, and conditioning event. A sequence peak and a graph-local maximum are different statistics.

For fixed-poset linear extensions, use the ideal/maximal-element recurrence and sample branches in proportion to their exact completion counts. For graph-labeling peak constraints, order vertices from highest label downward and use the residual-neighbor recurrence in [references/method.md](references/method.md). Never assume that an exact peak event is itself the set of linear extensions of one poset: nonpeak constraints are disjunctions.

For large instances, keep exact counting, approximate counting, approximate sampling, and exact sampling distinct. A Markov-chain or CFTP result applies only after its target state space, invariant distribution, coupling, and termination or mixing assumptions are verified. An entropy upper bound alone does not prove concentration; pair it with a lower bound and a strict gap for atypical configurations.

Read [references/method.md](references/method.md) for recurrences and sampler checks, [references/sources.md](references/sources.md) for the evidence register, and the two examples for valid and invalid transfers.

## A022 evidence boundary

The current stage includes exact Python counts for free-boundary squares through n=4, with brute-force cross-checks through n=3. This finite evidence is not an asymptotic result. Do not transfer torus/cycle, Eden-growth, regular-tree, or fixed-metric-graph-subdivision results to the growing free-boundary square without a separate proof. Thirty full-text papers have passed independent source review. Book excerpts and unread candidates are outside that completed-paper count.
