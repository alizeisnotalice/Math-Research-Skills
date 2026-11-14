# fabian24 — Slow graph-bootstrap percolation II: accelerating properties

**Reading status:** `fulltext_read`; complete 27-page paper read (PDF pp. 1–27), including tree bounds, layered lower-bound construction, process simulations, connectivity upper bound and open problems. Theorem 1.2 was located on PDF p. 3; Proposition 3.3 was visually checked on PDF p. 8. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** David Fabian, Patrick Morris, and Tibor Szabó, “Slow Graph Bootstrap Percolation II: Accelerating Properties,” *Journal of Combinatorial Theory, Series B* 172 (2025), 44–79, DOI [10.1016/j.jctb.2024.12.006](https://doi.org/10.1016/j.jctb.2024.12.006), arXiv [2311.18786](https://arxiv.org/abs/2311.18786), v2 (17 Dec 2024). Local PDF SHA-256: `d9891438ae432a8119676b24c5d1746ff4b717a1d1155e6bd6f8850d79daccf3`.

## Main running-time results

The process is the synchronous edge `H`-bootstrap process and `M_H(n)` maximizes its number of rounds over all `n`-vertex starting graphs. Theorem 1.2 (PDF p. 3) proves that every `t`-vertex tree `T`, for `n≥2t`, satisfies

\[
M_T(n)\le \frac18(t^2+6t+68).
\]

The proof handles a star separately by Lemma 3.1, then for non-star trees roots `T`, chooses a minimum vertex cover `U` with no leaves, and defines an induced-forest duration parameter `μ=M_{T[U]}(|U|)` and an outside-degree parameter `δ`. Proposition 3.3 (PDF p. 8) shows that after `2+3⌈ht_z(T)/2⌉+μ+δ` rounds, unless the process has already stopped, it has at least `|U|+δ−2` universal vertices; one additional round completes the graph. A diameter-centered root bounds the remaining parameters and yields the stated quadratic-in-`t` constant. The paper explicitly leaves a sharper star-like conjecture and forest-duration problem open.

Other proved conclusions: Theorem 1.4 (PDF p. 3) says every connected `H` with `δ(H)≥2` and `Δ(H)≥3` has `M_H(n)=Ω(n)`, with bipartite starts when `H` is bipartite. Proposition 1.5 (PDF pp. 4, 14–16) sharpens this to `M_{K_{2,s}}(n)=Θ(n)` for `s≥3`, using a partition into blocks that merge at most once per four rounds. Theorem 1.6 (PDF pp. 4, 16–18) constructs, for each `t≥1`, a connected target of minimum degree `t` with quadratic running time by simulating a long `K_6` process whose states remain `K_7`-free. Theorem 1.7 (PDF pp. 4, 18–21) constructs a target with `δ=1, Δ=3` and linear running time by simulating a long bipartite process with a triangle-free invariant. Theorem 1.8 (PDF p. 4; proof pp. 21–23) proves `M_H(n)=O(n)` if some edge `e` has `κ(H−e)≤2` and `H` itself percolates to the clique on its vertex set. Its proof chains overlapping copies of `H`, completes each to a clique, and bounds each merge interval by a constant depending on `H`.

## Scope and transfer limits

The layered construction for Theorem 1.4 delays the first new edges across successive layers; its scale depends on fixed `H`, giving only an asymptotic `Ω(n)` result. The simulation theorems require their stated locked subgraph and invariant; they do not imply a generic monotonicity principle for `M_H`. Forthcoming chain-construction results cited in the introduction/conclusion are previews or external work, not theorems proved in this paper. Open questions include the sharp tree bound, whether all sublinear cases are constant or logarithmic, and the tree-width-two upper bound.

**Visual check:** rendered PDF p. 8 and verified Proposition 3.3’s round count and universal-vertex conclusion against the image.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/fabian24`).
