# AUX-W07-LYONS-RANDOM-COMPLEXES-2009 — determinantal matroidal measures on complexes

**Source and read copy.** Russell Lyons, “Random Complexes and $\ell^2$-Betti Numbers,” *Journal of Topology and Analysis* 1(2) (2009), 153–175, DOI [10.1142/S1793525309000072](https://doi.org/10.1142/S1793525309000072). Read the full 25-physical-page author PDF, version dated 27 May 2015, at `evidence/fulltexts/AUX-W07-LYONS-RANDOM-COMPLEXES-2009.pdf`; SHA-256 `5ba66f6159e90beaa37c8a651a1848a572b5628369de9a3046b971fa9b3bdc0d`. The author's erratum was consulted for Proposition 4.11 and Corollary 6.2; the read 2015 version displays the corrected sign in the Proposition 4.11 proof and the sum over $(k+1)$-cobases in Corollary 6.2. Rendered PDF pp. 3, 7, 14, and 22 for determinant, projection, amenable-limit, and enumeration formulas.

## Projection determinantal measures (§2; PDF pp. 3–4)

For a finite set of coordinates $E$ and a vectorial matroid represented by a matrix $M$ with row space $H$, the basis law is
\[
\mathbb P_H(T)=\frac{|\det M_{A,T}|^2}{\det(M_{A,E}M_{A,E}^*)}=\det(Q_H)_{T,T},
\]
where the selected rows span $H$ and $Q_H$ is the orthogonal projection onto $H$. The Cauchy–Binet formula normalizes the law. For every finite coordinate set $D$, $\mathbb P_H[D\subseteq T]=\det(Q_H)_{D,D}$; this defines the infinite-coordinate projection DPP when $H$ is closed. Proposition 2.1 says samples have size $\dim H$ in the finite case; Proposition 2.2 identifies the complementary law with the orthogonal-complement measure. Theorem 2.3 gives stochastic domination $\mathbb P_H\preceq\mathbb P_{H'}$ for closed $H\subseteq H'$, with equality iff $H=H'$. Theorem 2.4 gives a trivial tail sigma-field for infinite-coordinate projection DPPs.

**A141 use note.** A finite weighted UST fits the vectorial-matroid formula by taking the reduced incidence column for edge $e$ and multiplying it by $\sqrt{c(e)}$; the squared basis determinant then has the product-conductance weight. This is a direct representation from equation (2.1), not a theorem in the paper about BK events. Determinantal negative association controls fixed coordinate sets, not a union over random, configuration-dependent disjoint witnesses.

## Finite CW complexes (§3; PDF pp. 5–9)

For a finite CW complex $X$, a $k$-base is a basis of the vector matroid of the cellular boundary matrix $\partial_k$, equivalently a maximal $k$-cell set with $Z_k(X_T)=0$; a $k$-cobase is a basis of the coboundary matroid. The lower matroidal law $P_k$ has projection kernel onto the coboundary space $B^k(X)$ and is supported on $k$-bases. Proposition 3.1 shows $P_k(T)$ is proportional to $t_{k-1}(T)^2$, the squared torsion order of the relevant homology of the subcomplex. The upper law is the complement of the cobase law and has kernel onto $Z^k(X)$; Proposition 3.3 gives its corresponding squared-torsion formula. Theorem 2.3 yields upper-law stochastic domination over the lower law, with equality exactly when $H^k(X)=0$. In a connected finite graph with $k=1$, the 1-bases are spanning trees and the lower law is uniform because zero-dimensional homology has no torsion.

These are complex-level matroidal laws, not ordinary forests in general dimensions. The graph/UST case is the $k=1$ specialization. The paper's broader higher-dimensional models should not be called spanning forests without that distinction.

## Infinite complexes, $\ell^2$-homology, and applications (§4–§6; PDF pp. 9–23)

Assuming local finiteness unless noted, §4 constructs four free/wired lower/upper extensions as projection DPPs on closures of boundary, cycle, coboundary, and cocycle spaces. At $k=1$, the wired lower law is WSF and the free lower law is FSF. **Corollary 4.4** identifies these laws as weak limits along finite exhaustions and combinatorial interiors (physical PDF p. 11). Proposition 4.6 bounds the $(k-1)$-Betti number of the complement inside a finite complex by the size of its boundary for all four measures under $\widetilde b_{k-1}(X)=0$.

For a bounded-degree complex, the $\ell^2$ Hodge decomposition identifies the obstruction between the four laws with reduced $\ell^2$-homology. If a countable group acts freely and cocompactly, its von Neumann dimension is $\beta_k(X;\Gamma)$. Proposition 4.7 says amenability and cocompactness of the $k$-skeleton imply equality of free and wired lower/upper laws. The exact density statement in **Proposition 4.9** (physical PDF p. 14) assumes that $\Gamma$ is amenable and acts freely on a complex $X$ whose $k$-skeleton is cocompact, and that $\widetilde b_{k-1}(X)=0$. Writing $f_j=f_j(X/\Gamma)$, it gives the expected number of $k$-cells in a sample $F\sim P_k$ per vertex of $X$ as
\[
\frac{f_{k-1}}{f_0}+\sum_{j=0}^{k-2}(-1)^{k+j-1}\frac{f_j-\beta_j(X;\Gamma)}{f_0}.
\]
The proposition also states that this equals the average number of $k$-cells per vertex $P_k$-almost surely. Corollary 4.10 specializes to the cubical $\mathbb Z^d$ complex, where a given $k$-cell belongs with probability $k/d$. Proposition 4.11 relates expected degree to von Neumann dimension for a Cayley graph, using the corrected proof in the author's erratum.

Section 5 (pp. 19–20) gives a percolation analogy and Proposition 5.1 for invariant projection subspaces on Cayley graphs. Section 6 (pp. 21–23) develops torsion-weighted higher-dimensional tree enumeration: Lemma 6.1 is a determinant/torsion identity and Corollary 6.2 is a Cauchy–Binet enumeration; use the corrected indexing over $(k+1)$-cobases in the 2015 read copy/erratum. References occupy pp. 23–25.

## Full reading coverage and scope

All 25 physical pages were read, including references. Detailed coverage is in `evidence/W07/reading_coverage.json`: introduction (pp. 1–2), determinantal measures (pp. 3–4), finite CW-complex laws (pp. 5–9), infinite measures and $\ell^2$-Betti applications (pp. 9–18), percolation analogy (pp. 19–20), enumeration (pp. 21–23), and bibliography (pp. 23–25).

For A141 this is **auxiliary projection-DPP context** for the finite weighted UST representation and fixed-coordinate dependence results. It supplies no BK inequality for increasing events with configuration-dependent disjoint witnesses; that interface remains open.
