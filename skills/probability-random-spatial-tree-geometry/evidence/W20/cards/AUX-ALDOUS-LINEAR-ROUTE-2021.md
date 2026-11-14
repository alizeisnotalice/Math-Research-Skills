# AUX-ALDOUS-LINEAR-ROUTE-2021 — Which Connected Spatial Networks on Random Points have Linear Route-Lengths?

**Author/year:** David J. Aldous; author-hosted manuscript title page dated 22 June 2021, associated arXiv record 0911.5296 first submitted in 2009. **Read source:** complete 22-page author PDF, SHA-256 `f67857d710b6060a6e2f46196b0c3021260982acdd3cc21f937e68e1ed51492b`. The arXiv banner and title-page date differ; both are retained. Review pending.

## Model and theorem

A rate-one planar Poisson process carries a network produced by a deterministic, translation-invariant road rule; the rule may depend on the whole configuration. When two roads cross, the crossing is a usable junction. For the square `S_L`, `G_L` consists only of roads guaranteed to remain present for every exterior configuration (the rule is “edge iff edge for every outside configuration”). Write `N_L⁰` for the number of cities outside the largest component of `G_L`. The **asymptotic essential connectedness** hypothesis is `L⁻² E N_L⁰ → 0`.

**Theorem 1 (physical pp. 5–16):** under that condition, for all bounded `A,B`,

`E sum_{ξ∈A} sum_{ξ′∈z+B} ℓ(ξ,ξ′) = O(|z|), as |z|→∞.`

The conclusion is about a Poisson pair-sum, not a supremum over a route family. **Corollary 2** upgrades the pair-sum to every fixed `k`-th moment under the same assumptions. **Proposition 9** verifies the condition for the relative-neighborhood graph (RNG).

## Proof mechanism

The block construction marks squares “nice” when all four half-square counts are in a fixed density window, their frozen-core largest component contains at least `0.99L²` cities, and frozen-core road length is at most `c_L L`. A site is good if its square and four adjacent midpoint squares are nice. Disjoint-square dependence makes the good-site process 1-dependent, and the density condition lets `L,c_L` be chosen so its good probability exceeds the oriented-percolation threshold `p₀`.

Proposition 3 gives finite moments of the first site on a doubly-infinite oriented good path. Intersections of adjacent large components let a good path be converted into a network route of length at most linear in the lattice path length (Lemma 4). Six affine lattices handle directions and crossings (Lemmas 5–6). A finite-moment random circuit around each bounded endpoint window supplies local access to the global route (Propositions 6–7); combining the two local routes with the global good path yields the pair-sum bound and all-moment Corollary 2.

For the RNG, a deterministic component-chain lemma produces a sequence of strictly decreasing interpoint distances until a component reaches the square boundary. A Poisson factorial-count estimate makes a long decreasing sequence unlikely; a known longest-edge bound for the finite-window MST then forces a single large frozen-core component with high probability. This proves Proposition 9.

## A136 boundary

The result controls average distances between *all Poisson points in two translated bounded windows*. A136 instead asks for `E sup_i ℓ(r(0,U_i))` in one shared SIRSN realization, with one fixed origin and an iid sequence of uniform endpoints in a bounded disk. This paper supplies neither that supremum nor a tail integral for it. The proof's pair-sum and finite-moment estimates cannot be relabeled as fixed-origin iid-star integrability.

**Rendered check:** original physical p. 4 definitions (3)–(4) and Theorem 1; full section coverage in `evidence/W20/reading_coverage.json`.
