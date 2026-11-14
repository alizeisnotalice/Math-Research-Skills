# LYO2003DPP — determinantal probability measures

**Source/version.** Russell Lyons, “Determinantal Probability Measures,” *Publications Mathématiques de l’IHÉS* 98 (2003), 167–212, DOI 10.1007/s10240-003-0016-0. Read all 46 pages of the local author version dated 10 Mar. 2004. Local PDF page numbers are used; journal pagination is local page +166.

## Determinantal laws and uniform forests (§§1–5; PDF pp. 1–15)

For a finite or countable ground set \(E\), a determinantal probability measure with kernel \(Q\) is characterized by

\[
\mathbb P[A\subseteq S]=\det(Q_A)\qquad(A\subset E\text{ finite}),
\]

where \(Q\) is a positive contraction on \(\ell^2(E)\). The paper develops finite matroid/basis laws, exterior-algebra formulas, and their spanning-forest application. For the infinite connected graph exhausted by finite connected subgraphs in §3 (PDF p. 9), the Hilbert space uses the paper’s unweighted \(\ell^2(E)\) coordinate convention: \(\star(G)\) is the closure of the union of the star spaces of the wired finite graphs, and \(\Diamond(G)\) is the closure of the union of the finite cycle spaces. The WSF projection kernel is \(P_{\star(G)}\); the FSF kernel is \(P_{\Diamond(G)^\perp}\). Thus FSF=WSF iff \(\star(G)=\Diamond(G)^\perp\). This is an infinite-volume forest statement and should not be confused with the finite weighted-UST transfer-current determinant. For general conductances, Remark 5.6 (printed p. 182; local PDF p. 16) uses the weighted spanning-tree measure proportional to the product of edge conductances and transforms each edge coordinate \(e\) to \(\sqrt{w(e)}e\), so the star and cycle spaces are formed in that transformed convention. Edge orientation changes matching row and column signs in transfer-current determinants. The abstract DPP framework itself does not require graph connectedness; connectedness, the exhaustion, and graph-space hypotheses enter in the USF application.

## Negative association: exact proof chain (§6; PDF pp. 16–23)

**Theorem 6.5 (PDF pp. 19–20)**: for a finite ground set and a projection determinantal measure \(P_H\), increasing events on disjoint fixed coordinate sets are negatively associated:

\[
P_H(A_1\cap A_2)\le P_H(A_1)P_H(A_2).
\]

Proof dependencies are explicit. Theorem 6.2 proves stochastic domination \(P_{H_1}\preceq P_{H_2}\) for nested subspaces. Proposition 6.3 identifies conditioning on \(e\in S\) with the projection measure of \((H\cap e^\perp)+[e]\), so for increasing \(A\) ignoring \(e\), conditioning on \(e\in S\) can only lower \(P_H(A)\). For general disjoint-coordinate events, induct on \(|E|\): since \(|S|=\dim H\) a.s., choose a coordinate \(e\) ignored by \(A_2\) with \(P(A_1\mid e\in S)\ge P(A_1\mid e\notin S)\). Apply the induction hypothesis to the conditional measures on the two coordinate slices and use the one-coordinate negative correlation to bound \(P(e\in S\mid A_2)\le P(e\in S)\); mixing the two conditional bounds proves the claim. Corollary 6.6 (PDF p. 21) shows conditioning on inclusion of one set and exclusion of a disjoint set preserves NA.

This is fixed-coordinate negative association, not the BK inequality for arbitrary increasing events with disjoint random witnesses. The paper’s open-question section explicitly leaves the UST BK question unresolved.

## Infinite laws and positive contractions (§§7–8; PDF pp. 23–34)

The infinite-case section treats countable ground sets, limits, tail questions, and the forest applications. **Theorem 8.1 (PDF pp. 32–33)** extends DPP results to positive-contraction kernels by dilating \(Q\) to an orthogonal projection on a larger space and restricting the projection law. It supplies the mixed inclusion/exclusion determinant formula, conditional negative association with external fields and trivial tail, a count concentration bound, and stochastic domination for commuting ordered positive contractions. Its proof links these statements respectively to the determinant identity, Theorem 6.5 / Corollary 6.6, Theorem 7.15, Corollary 6.7, and Theorem 7.1; commutation is needed for the spectral-theorem domination step.

The FSF=WSF discussion is about equality of laws/currents and does not establish mutual singularity for all distinct pairs. The paper also states BK as an open question (PDF p. 35 / journal p. 201). NA for two fixed disjoint coordinate sets cannot be summed over all possible witness pairs without a separate argument.

## Full reading coverage and model boundaries

All 46 local PDF pages were read, including the five open-question sections and references; section coverage is recorded in `evidence/W07/reading_coverage.json`. The abstract DPP theorems are not restricted to unweighted or finite graphs, but the rank-fixed proof of Theorem 6.5 is for finite \(E\); the infinite graph application must retain the paper’s countable-space and projection assumptions. For finite weighted UST, use the weighted transfer-current kernel (diagonal \(c(e)R_{\mathrm{eff}}(e^-,e^+)\)); do not infer weighted BK from NA. The paper does not settle A141’s disjoint-certificate inequality.
