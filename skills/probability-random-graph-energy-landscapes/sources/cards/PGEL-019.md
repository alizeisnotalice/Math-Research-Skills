> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-019 — Graph Homology and Stability of Coupled Oscillator Networks

## Identity and reading record
Jared C. Bronski, Lee DeVille, and Timothy Ferguson, “Graph Homology and Stability of Coupled Oscillator Networks,” read local arXiv:1508.01507v1 (6 August 2015); published as *SIAM Journal on Applied Mathematics* 76(3):1126–1151 (2016), DOI [10.1137/15M1034258](https://doi.org/10.1137/15M1034258). [Official arXiv record](https://arxiv.org/abs/1508.01507); [SIAM publication page](https://epubs.siam.org/doi/abs/10.1137/15M1034258). The exact local 18-page arXiv v1 PDF, SHA-256 `51d84dbb4b2edbc74322ee92c6b57d129d789bb9f1c8e4f273e4debc1db698be`, was read in physical-page order through all proofs and references. The publisher full text was not read; no claim is made that its statements match arXiv v1. The canonical full-read index had no exact title/hash match before this read. R05 helper stage passed; mother-hash binding is pending (R05 metadata_verified=false).
## Model and definitions

The main result is deterministic linear algebra on a finite, connected, simple, undirected weighted graph. Every edge weight γ_e is real and nonzero (the cycle form uses (D^{-1})); the graph need not have positive weights. With an arbitrary fixed edge orientation and signed incidence matrix (B), the paper uses the **negative** of the usual weighted Laplacian:

\[
L_G=-B D B^{\mathsf T},\qquad D=\operatorname{diag}(\gamma_e).
\]

Write (C=|E|-|V|+1=\dim\ker B), choose a cycle-space basis (Y\in\mathbb R^{|E|\times C}), and define the cycle-intersection form

\[
Z_G=-Y^{\mathsf T}D^{-1}Y.
\]

The matrix entries depend on the chosen basis, but its inertia is invariant under a basis change by congruence. “Stable Laplacian” in this paper means (n_+(L_G)=0); it is an index criterion, not by itself a nonlinear basin statement.

## Main theorem and proof chain

**Theorem 2.6 as printed (physical p. 4, arXiv v1).** For a connected weighted graph with the paper's nonzero real edge weights, the paper states

\[
n_+(L_G)=\#\{e:\gamma_e<0\}-n_+(Z_G).
\]

This is a source statement, but its unrestricted form has a singular-boundary counterexample in the read version. For the triangle with weights \((1,1,-1/2)\), the exact eigenvalues of \(L_G\) are \((-3,0,0)\), while \(Z_G=0\); hence the two sides are 0 and 1. The definitions do not exclude this connected, nonzero-weight graph. In the proof (physical pp. 14–15), the covering-tree reduction invokes Haynsworth's Appendix Lemma A.1 (physical p. 17), whose hypotheses require both the matrix and its restriction to the selected subspace to be nonsingular. The read proof does not provide a perturbation/limit extension across a singular restriction. Therefore do not use the displayed identity at extra-zero-mode/singular-restriction cases; use it only in a case where the nonsingularity hypotheses needed at each application have been independently checked. This card does not assert a maximal repaired theorem or make a claim about the unread journal full text.

The same p. 4 paragraph also prints \(n_+(L_G)\le\#\{e\in\mathrm{Tree}(G):\gamma_e<0\}\), where the page-4 definition makes \(\mathrm{Tree}(G)\) the edges contained in every spanning tree. This auxiliary inequality is not used: for an all-negative triangle, that set is empty but \(n_+(L_G)=2\). Keep it quarantined as another read-v1 source-local inconsistency.

**Stable-graph negative-edge bound (independent derivation, not attributed as a verified consequence of the defective equality).** In the stated finite, connected, undirected, nonzero-weight model, if “stable” means the paper's \(n_+(L_G)=0\), then \(L_G\preceq0\). The positive-edge subgraph \(G_+\) must be connected: otherwise take a vector constant on each component of \(G_+\), with different values across a component cut. Positive-edge contributions to \(x^{\mathsf T}L_Gx=-\sum_e\gamma_e(x_u-x_v)^2\) vanish, while at least one negative edge crosses the cut and makes the quadratic form positive, a contradiction. Thus \(G_+\) has at least \(|V|-1\) edges, so the number \(m_-\) of negative edges satisfies

\[
m_- = |E|-|E(G_+)|\le |E|-|V|+1=C.
\]

If \(m_-=C\), then \(|E(G_+)|=|V|-1\), so connectedness makes \(G_+\) a spanning tree. This independently proves the stable-graph bound printed later on p. 4; it does not prove the general inertia identity.

For a one-cycle graph with one negative edge, the source gives the strict criterion \(Z_G=-\sum_{e\text{ on cycle}}1/\gamma_e>0\) (physical pp. 7–8). Treat this as a strict/nondegenerate criterion only: do not state an iff for the paper's semidefinite stability convention at \(Z_G=0\). The triangle above has \(Z_G=0\) and is stable by \(n_+(L_G)=0\), so the boundary is not classified by the strict criterion.

The proof (physical pp. 12–15) builds a covering tree \(T\) whose edge set maps bijectively to \(E(G)\), and a surjective vertex map identifying tree vertices to recover \(G\). The graph Laplacian is the restriction of the covering-tree Laplacian to the subspace of vectors constant on each fiber. On the orthogonal complement, the compressed inverse is the cycle form (Lemma 5.10). Haynsworth's inertia identity (Appendix Lemma A.1) then subtracts the positive index of that compressed inverse from the positive index on the tree. On a tree the index is exactly the number of negative edge weights. The needed nonsingularity is a hypothesis of the cited inertia lemma, not a perturbation/limit argument established in this proof.

The paper works out a diamond (two independent cycles), general one-cycle graphs, and general two-cycle graphs (physical pp. 6–9). These are explicit low-cycle calculations of the theorem, not claims that independent cycles decouple in arbitrary topology.

## Kuramoto application and evidence boundary

In the paper’s ring application, all couplings are equal and rescaled to one, so the edge weights in this linear criterion are $\gamma_i=\cos(\theta_i^*-\theta_{i+1}^*)$. The graph theorem gives the unstable-manifold dimension from the signed Laplacian index. For a ring with one negative cosine edge, the reciprocal-cosine criterion above is exact (physical pp. 9–11).

The “longest stable link” discussion is not a proved all-(n) formula: the authors derive a symmetric candidate using a constrained optimization and then explicitly say existence of a root for every (n), which root is largest, and the table values are shown numerically/empirically (physical p. 10, Table 4.1). Keep those table entries as numerical evidence, not a theorem.

## Source-level sign discrepancy to quarantine

**Theorem 2.8 / Eq. (2.3), physical p. 5 of the read arXiv v1 PDF, is inconsistent with that version’s own definitions as printed.** It states

\[
\frac{1}{|V|}\det_{\rm red}(L_G)=\det(Z_G)\prod_e\gamma_e.
\]

For the unit-weight triangle, $L_G=-B B^{\mathsf T}$ has eigenvalues $0,-3,-3$, so the determinant restricted to $\mathbf 1^\perp$ is $9$ and the left side is $3$. The cycle basis $Y=(1,1,1)^{\mathsf T}$ gives $Z_G=-3$, while $\prod_e\gamma_e=1$, making the printed right side $-3$. The discrepancy is also visible in the rendered p. 17 proof’s tree determinant sign step. The exact arithmetic witness is saved in `../math/exact_checks.py` and `../math/exact_checks.json`. I read the D02 arXiv v1 PDF; I did not read the publisher’s full text to check whether this identity changed in the journal version. I do not rely on Theorem 2.8 or its printed determinant formula; this countercheck does **not** affect Theorem 2.6 or its inertia proof.

## Transfer limits

This is not a random-graph theorem and does not count or exclude all nonlinear equilibria. The index formula applies to a specified weighted undirected graph/Laplacian; its nonlinear interpretation requires a phase-locked state whose Jacobian has the paper’s Laplacian form. It does not transfer to a general oriented/asymmetric model, nor does a negative index alone characterize global synchronization.

Coverage: all physical pages 1–18 were read. Rendered theorem/proof and formula pages are listed in the batch `../../reading_coverage.json` (mother entry; rendered images remain under `../renders/PGEL-019/`). Review is pending.
