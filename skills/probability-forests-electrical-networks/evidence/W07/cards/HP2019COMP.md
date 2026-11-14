# HP2019COMP — component graph of the uniform spanning forest

**Source and read copy.** Tom Hutchcroft and Yuval Peres, “The Component Graph of the Uniform Spanning Forest: Transitions in Dimensions 9, 10, 11, …,” *Probability Theory and Related Fields* 175 (2019), 141–208, DOI 10.1007/s00440-018-0884-3; author preprint arXiv:1702.05780. Complete local PDF read, 58 physical pages, SHA-256 `36c4b9c07b82099f8e5227afd5088fac2bfcb0f290d080fd9a65546974c26d3f`. The results concern uniform spanning forests on transitive graphs of polynomial volume-growth dimension $d$, not minimal spanning forests.

## Model and objects (§§1–2; PDF pp. 1–14)

The graph $G$ is infinite, connected, locally finite, transitive, and $d$-dimensional, with $|B(x,n)|\asymp n^d$; the paper uses the corresponding heat-kernel estimates. For $d>4$, FUSF and WUSF coincide on these graphs, so the paper writes USF. This is not an assumption that $G=\mathbb Z^d$. A component graph $C_r(F)$ has the forest components as vertices, with two components adjacent when a graph path of length at most $r$ joins them. The component hypergraph $C_r^{\rm hyp}(F)$ records finite sets of forest components that can all be hit by one set of diameter at most $r$.

A finite graph or hypergraph with boundary $H=(\partial V,V_\circ,E)$ is present at assigned boundary vertices when its interior vertices can be realized so its incidences hold; “faithfully present” also requires all interior vertices to be distinct and disjoint from the assigned boundary vertices. “Ubiquitous” and “faithfully ubiquitous” mean this holds at every collection of distinct assigned boundary vertices, respectively. The faithful version is stronger and is the main criterion.

Keep the paper’s two operations distinct (definitions on PDF p. 5). A **coarsening** preserves the vertex set up to a boundary-preserving bijection and merges hyperedges through a surjection on the edge set; it does not merge vertices. A **quotient** may merge vertices through a surjection that is bijective on boundary vertices, while the edge map is bijective and preserves incidence. Thus a quotient is a vertex-identification operation, whereas a coarsening is an edge-merging operation.

For a hypergraph with boundary define
\[
\Delta(H)=\sum_{e\in E}\deg(e)=\sum_{v\in V}\deg(v),\qquad
\eta_d(H)=(d-4)\Delta(H)-d|E|-(d-4)|V_\circ|.
\]
Call $H$ $d$-buoyant when $\eta_d(H)\le 0$. The theorem tests all subhypergraphs after an edge-merging coarsening. This definition is specific to the component-hypergraph argument and is not a generic connectivity statistic.

## Main results and proof dependencies (§§1–5; PDF pp. 3–55)

- **Theorem 1.1 (PDF p. 3).** For $d_1\ge d_2\ge9$, every finite graph with boundary that is ubiquitous in $C_{r_1}(F_1)$ is also ubiquitous in $C_{r_2}(F_2)$ almost surely. Here $d_1$ is the higher dimension, so ubiquity in the higher-dimensional component graph implies ubiquity in the lower-dimensional one. If $d_1>d_2$, some finite boundary graph is almost surely ubiquitous in the lower-dimensional component graph $C_{r_2}(F_2)$ but not in the higher-dimensional one $C_{r_1}(F_1)$. The same conclusions hold with “faithfully ubiquitous.” This is a comparison of the stated transitive-graph USF models.
- **Theorem 1.2 (PDF p. 3).** If $d>8$ and $T$ is a finite tree with boundary, then $T$ is almost surely ubiquitous (equivalently, faithfully ubiquitous) in $C_r(F)$, for every $r\ge1$, exactly when
  \[
  \max\left\{\frac{|E(T')|}{|V_\circ(T')|}:T'\text{ is a subgraph of }T\right\}\le\frac{d-4}{d-8}.
  \]
  The ratio uses the interior-vertex count in the paper. It is not a claim about all $d$-dimensional graphs without the transitivity and growth hypotheses.
- **Theorems 1.3–1.5 (PDF pp. 4–6).** Theorem 1.3 separates dimensions 5–8 by ubiquitous tree configurations in the component hypergraph. For a finite simple graph with boundary, Theorem 1.4 says faithful ubiquity in $C_r(F)$ is equivalent to
  \[
  \min_{H'\text{ coarsening of }H}\;\max_{H''\subseteq H'}\eta_d(H'')\le0,
  \]
  and ordinary ubiquity is equivalent to having a quotient that is faithfully ubiquitous. Theorem 1.5 gives the analogous hypergraph criterion: the condition is equivalent to faithful ubiquity in $C_r^{\rm hyp}(F)$ for every $r\ge R_G(H)$; if it fails, faithful ubiquity fails for every $r\ge1$. Ordinary ubiquity again means a quotient is faithfully ubiquitous.

**Proof chain.** Section 2 supplies the BKPS connection estimate (Theorem 2.1, PDF p. 10): for a finite vertex set $K$, the probability all of $K$ lie in one USF component is at most $C\langle K\rangle^{-(d-4)}$, where the spread $\langle K\rangle$ is defined by minimizing a product of pairwise distances over spanning trees. Proposition 2.2 (PDF p. 10) assumes a finite index set $I$ and a finite-vertex-set family $(K_i)_{i\in I}$. Its event is exactly
\[
E=\bigcap_{i,j\in I}\{\,\mathcal F(K_i\cup K_j)\ \Longleftrightarrow\ i=j\,\},
\]
where $\mathcal F(K)$ means every vertex of $K$ lies in one component of the same USF sample. In particular, all vertices of each indexed $K_i$ must lie in one component, and these components must be pairwise distinct for different indices; the sets themselves are not assumed disjoint. The proposition states $\mathbb P(E)\le C\prod_{i\in I}\langle K_i\rangle^{-(d-4)}$, with $C$ depending on $G$, $|I|$, and the set sizes. Its proof uses Wilson’s algorithm: $E$ implies that the USF generated from the independent walk family for each $K_i$ is connected, so $E$ is contained in the intersection of those per-index connection events. Independence bounds the probability by $\prod_i\mathbb P(\mathcal F(K_i))$, and Theorem 2.1 bounds each factor. The proposition is not an unqualified product estimate for arbitrary disjoint-set connection events. Lemma 4.10 (p. 31) separately identifies positive probability that a finite set lies in distinct USF components with positive probability of pairwise nonintersection for independent simple random walks started there; Wilson’s algorithm supplies the forward implication and the Green-function estimate controls the reverse.

For nonubiquity, Proposition 4.1 and Lemmas 4.2–4.9 (PDF pp. 19–30) count witnesses over dyadic scales. The one-scale bound in Lemma 4.2 is optimized by edge-merging coarsenings, with Lemma 2.4 connecting buoyancy of all subhypergraphs to the coarsening criterion. For ubiquity, Proposition 4.11 uses well-separated boundary points, a first-moment lower bound (Lemma 4.13), and a restricted second-moment upper bound (Lemma 4.14), then applies Cauchy–Schwarz. Dimensions $5,6,8$, where logarithmic terms can occur, are handled separately in Proposition 4.15 and Lemma 4.16 before the induction in Theorem 1.5. Section 5 (PDF pp. 52–55) proves the main theorems from these criteria: Theorem 1.2 follows by converting the subgraph ratio into the sign of $\eta_d$; Theorem 1.1 follows from the stated monotonicity direction and an explicit family of trees whose critical ratio changes with dimension.

## Full reading coverage and use limits

All physical pages 1–58 were read, including the open problems and references. Section-by-section coverage is in `evidence/W07/reading_coverage.json`. Rendered pages checked include the main theorem and ratio (p. 3), the separate quotient/coarsening definitions (p. 5), buoyancy and the hypergraph criterion (p. 6), the BKPS bound and its distinct-component event/proof (p. 10), the multiscale/moment proof (pp. 20, 31, 33, 36–37, 40), and the main theorem proofs/open problems (pp. 52, 54–55).

This paper is context for uniform-forest component geometry. It does not prove a threshold or connectivity result for the free or wired minimal spanning forest, so it does not close C105. Keep its $d$-dimensional transitive-graph setting, $d>4$ USF coincidence, exact dimension-monotonicity direction, and $d>8$ tree-ratio theorem explicit when applying it.
