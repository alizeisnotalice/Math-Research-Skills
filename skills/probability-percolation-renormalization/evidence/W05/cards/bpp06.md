# bpp06 — Bootstrap percolation on trees and non-amenable groups

**Reading status:** `fulltext_read`; complete 17-page article read (PDF pp. 1–17). The regular-tree recursion, fort/branching-number arguments, anchored-expansion boundary count, and concluding scope discussion were read. Theorem 1.4’s displayed hypothesis was rendered and checked. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** József Balogh, Yuval Peres, and Gábor Pete, “Bootstrap Percolation on Infinite Trees and Non-Amenable Groups,” *Combinatorics, Probability and Computing* 15 (2006), 715–730, DOI [10.1017/S0963548306007619](https://doi.org/10.1017/S0963548306007619), arXiv [math/0311125](https://arxiv.org/abs/math/0311125). Local PDF SHA-256: `3c9e234c2c73baf8b1547107878bd496d3ab3f0ac096dbc53c8c1185c6b5cb1b`.

## Tree results

For a countable locally finite graph, each vertex is initially occupied independently with probability `p`, then a vacant vertex becomes occupied when it has at least `k` occupied neighbours. The critical probability `p(G,k)` is the infimum of `p` for which complete occupation has positive probability. A `k`-fort is a connected vertex set whose vertices have at most `k` neighbours outside it; the obstruction to complete occupation is a vacant `(k−1)`-fort.

Theorem 1.1 (PDF pp. 2–3) states that for any infinite tree `T`, if `br(T)<k`, then `p(T,k)=1`. For `2≤k≤d`, Proposition 1.2 (PDF pp. 2, 5–6) says the critical probability on the `(d+1)`-regular tree is the supremum of those `p` for which there is a root `x∈(0,1)` solving

\[
\mathbb P\{\operatorname{Bin}(d,(1-x)(1-p))\le d-k\}=x;
\]

It also states that for any integer sequence satisfying `2≤k_d≤d` and `k_d/d→γ`, we have `p(T_d,k_d)→γ`, and gives explicit endpoint cases. Theorem 1.3 (PDF pp. 3, 9–11) says every vertex lies in a `k`-fort `F` with `br(F)≤max{br(T)−k,0}`. Its proof is an iterative pruning construction controlled by weighted cutset capacities; simply deleting the `k` child subtrees of largest branching number at each generation is explicitly said not to work in general. Theorem 1.1 then uses a quantitative finite-fort lemma to show that if `br(T)<k`, infinitely many bounded-size vacant forts occur almost surely, forcing `p(T,k)=1`.

## Anchored expansion result

Theorem 1.4 (PDF pp. 3, 11–13): if `G_d` is `d`-regular and its anchored Cheeger constant satisfies `ι*(G_d)+2k>d`, then `p(G_d,k)>0`; in particular anchored expansion gives positivity at `k=⌈d/2⌉`. The proof follows a chain of finite connected internally spanned sets. Each newly infected vertex can increase the occupied-boundary size by at most `d−2k`; anchored expansion therefore forces a positive fraction of each large internally spanned set to be initially occupied. A binomial large-deviation estimate beats the bound `((d−1)e)^m` on rooted connected sets for sufficiently small `p`.

The source also distinguishes `q(G,k)`, the onset of an infinite occupied component in the final state, from `p(G,k)`, complete occupation. It gives counterexamples showing that nonamenability alone does not decide the critical probability: a 6-regular non-amenable Cayley graph can have `p(G,2)=0`. Thus this is a sufficient anchored-expansion criterion, not a characterization of amenability, nor a result for finite random-host infection time.

**Visual check:** rendered PDF p. 3 to verify Theorems 1.3–1.5 and the anchored-expansion condition.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/bpp06`).
