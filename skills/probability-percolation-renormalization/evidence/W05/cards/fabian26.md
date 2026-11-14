# fabian26 — Graph bootstrap percolation: a discovery of slowness

**Reading status:** `fulltext_read`; complete 42-page arXiv v2 / survey chapter read, PDF pp. 1–42. Theorem 4.2’s statement and the survey’s own proof were checked on rendered PDF pp. 15 and 20; other selected theorem statements were checked on source pages. R03’s round-7 decision requested an attribution correction; this revised card is awaiting recheck.

**Reference:** David Fabian, Patrick Morris, and Tibor Szabó, “Graph Bootstrap Percolation — A Discovery of Slowness,” arXiv:2602.12736v2 (16 March 2026); *Surveys in Combinatorics 2026*, pp. 141–188, DOI [10.1017/9781009766012.006](https://doi.org/10.1017/9781009766012.006). Local PDF SHA-256: `11d4c4e4454b37f5a9f420457cd92a4a984ae57999dac57071bc8c6e17ff043d`.

## Model and representative results

For a fixed graph (H), the synchronous (H)-process on (K_n) adds in each round every missing edge that is the final absent edge of a copy of (H). The paper distinguishes the random-host threshold (p_c(n,H)), the weak-saturation count (\mathrm{wsat}(n,H)), and maximum number of synchronous rounds (M_H(n)=\max_G\tau_H(G)); results about one of these observables do not imply results about the others.

Theorem 4.2 is an original result proved in this survey, not merely a theorem summary: the authors note that the clique case had previously been stated without proof, then prove the general result in §4.3. For every fixed (2,1)-inseparable graph (H), there is a constant (C(H)) such that for every (n), some (H)-percolating graph (\\widetilde G) has at most (C(H)n) vertices and satisfies (\\tau_H(\\widetilde G)\\ge M_H(n)). The proof is given in §4.3 (PDF pp. 17–21; the detailed construction begins on p. 20) using a slow process, a high-girth bipartite auxiliary graph, and chain gadgets.

The remaining selected theorem statements below are survey summaries attributed to the cited primary results:

- Theorem 5.1: if (H) has (k\ge6) vertices and (\delta(H)>3k/4), then (M_H(n)=\Omega(n^2)); if (k\ge5) and (\delta(H)\ge k/2+1), then (M_H(n)\ge n^{2-O(1/\sqrt{\log n})}=n^{2-o(1)}).
- Theorem 6.3 gives (M_T(n)\le (t^2+6t+68)/8) for every (t)-vertex tree (T) and (n\ge2t). A (t)-vertex star has exact maximum (t-1) for all sufficiently large (n); equality for all trees is a conjecture. Theorem 6.6 states, for fixed `k ≥ 3` and all sufficiently large `n`, `M_Ck(n) = ⌈log_(k−1)(n+k²−4k+2)⌉` when `k` is odd, and `M_Ck(n) = ⌈log_(k−1)(2n+k²−5k)⌉` when `k` is even.
- Theorem 7.10 gives (M_H(n)=\Omega(n^{1+2/(3v(H)-2)})) for ((2,1))-inseparable (H). Theorem 8.3 gives (M_H(n)\ge n^{3/2-o(1)}) for a bipartite (H) with parts of sizes (3\le r\le s), when every vertex in the (r)-side has degree at least (s/2+1) and every vertex in the (s)-side has degree at least (r/2+1). For (Q_3), the paper records (\Omega(n^{3/2})\le M_{Q_3}(n)\le O(n^{8/5})).
- The K5 lower bound remains (n^{2-O(1/\sqrt{\log n})}); the survey presents (M_{K_5}(n)=o(n^2)) as an open conjecture, not a theorem.

## Proof ideas and limits

The survey’s toolbox includes clique chains and ladder chains, Behrend-type dilation sets avoiding bounded-coefficient linear equations, high-girth constructions that prevent unwanted copies of (H-e), and simulations that transfer a slow process into a different infection rule. These are specialized construction methods; a transfer requires checking the exact copy-avoidance and percolation conditions. The survey is useful for routing A188/A190/A193/A199 and C189/C197/C198, but its cited theorem summaries are not independent proofs and weak saturation still means a sequential edge order, not synchronous rounds.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/fabian26`).
