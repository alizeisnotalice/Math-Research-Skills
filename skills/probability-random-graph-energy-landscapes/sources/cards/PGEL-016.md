> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-016 — When is sync globally stable in sparse networks of identical Kuramoto oscillators?

## Source and reading evidence

- Yury Sokolov and G. Bard Ermentrout, arXiv:1812.08153v2 (7 Nov 2019), published DOI 10.1016/j.physa.2019.122070.
- Exact local source: ../pdfs/PGEL-016.pdf, 23 physical pages, SHA-256 5c1bf38a2969f633fe52413329e10d52dea1dadc67165a04e73c4cd92d302471.
- Complete physical PDF pp. 1–23 read in order, including all algorithm sections, numerical experiments, conclusion, and references. Section coverage and formula-page hashes are in reading_coverage.json#sources.PGEL-016.
- Canonical full-read index was checked before reading; no accepted exact-title, arXiv-ID, or source-hash match was found. R02 accepted the complete reading and source content; it approved tool eligibility only for the narrow local certificate below.

## Model and theorem status

The paper considers identical oscillators with zero natural frequencies on a connected simple undirected graph, with positive unit edge couplings:
\[
\dot\theta_j=\sum_{i\sim j}\sin(\theta_i-\theta_j),
\]
on the phase torus modulo common rotation. Its energy is the standard sum over undirected edges of 1−cos(θ_i−θ_j). The work gives an algorithmic route for finding initial conditions outside synchrony's basin and reports graph-family experiments.

**The central structural input is explicitly an unproved ansatz, not a theorem.** Ansatz 1 (physical p. 7) says that every stable phase-locked solution has a point \(\widetilde\theta\) in its basin (possibly the solution itself) with \(L\widetilde\theta=s\), \(s\perp\mathbf1\), and \(s_i=2\pi c_i\), \(c_i\in\mathbb Z\). The subsequent “boundary vector/core” construction and broad existence claims depend on this premise. The paper states the ansatz without proof; do not promote it to a general existence theorem.

## Concrete results and proof mechanisms

- **Exact-equilibrium local certificate (physical p. 9, Eq. (9)).** At an exactly verified equilibrium θ* on a connected simple undirected graph, the source writes the Jacobian as \(J(\theta^*)=-B^\top W B\), with edge weights \(w_{ij}=\cos(\theta_i^*-\theta_j^*)\), and obtains
  \[
  x^\top J(\theta^*)x=-\sum_{i\sim j}w_{ij}(x_i-x_j)^2\le0.
  \]
  The number of zero eigenvalues equals the number of connected components of the weighted graph. In particular, if every edge difference satisfies the strict condition \(|\theta_i^*-\theta_j^*|<\pi/2\), then every \(w_{ij}>0\); connectedness makes the kernel exactly span{1}, so J is strictly negative on 1-perp. This gives the standard local exponential-stability certificate modulo common rotation for that exact equilibrium. It is a rigorous, reusable conditional method; it says nothing about how to find such an equilibrium, whether a non-synchronous equilibrium exists, or global synchronization.
- **Algorithm and graph motifs (physical pp. 13–14).** The procedure uses planar embeddings, candidate boundary edges from a cutset, long induced paths without cut vertices, or cyclic graph clustering/community detection, then constructs a boundary vector and an initial condition via a Laplacian pseudoinverse. The text claims a sufficiently long induced subpath or a cyclic clustering with enough clusters can imply a nonsynchronous stable phase-locked state. This is conditional on the unproved Ansatz 1 and on the construction's stated graph conditions; the paper does not give a complete classification of all stable equilibria.
- **Notation issue in the printed algorithm (physical p. 14).** It writes i.c.=2π A^+ BoundVector, whereas p. 6 defines A as adjacency and p. 9 derives \(\widetilde\theta=L^+s\) using the graph Laplacian. If A on p. 14 literally means that adjacency matrix, the step is inconsistent with the preceding derivation. The exact local C6 test below confirms the distinction; no author intent is inferred.
- **Stochastic block model experiments (physical pp. 15–16).** The paper examines finite samples (10 graph realizations per parameter combination) and reports patterns “mostly” or “almost always” under conditions. These observations are numerical, conditioned on sampled graphs and procedure choices. They are not a whp theorem for a uniform Erdős–Rényi graph and do not establish a probability limit.
- **Path augmentation experiments (physical pp. 17–18).** Added long paths are used to test the heuristic on finite generated networks; the work remains computational. It does not turn the numerical detection rate into a theorem.
- **Conclusion and references (physical pp. 19–23).** The conclusion recaps the proposed algorithm and its heuristic/ansatz dependence; the remainder is references. No additional proof repairs Ansatz 1.

## Local exact calculations

Ran the saved SymPy checks in ../math/pgel_l03_b7_checks.py; exact results are in ../math/pgel_l03_b7_checks.json.

1. On the six-cycle, use the standard adjacency A, Laplacian \(L=2I-A\), and zero-sum boundary vector \(s=(2\pi,-2\pi,0,0,0,0)\). Exact arithmetic gives
   \[
   L A^{-1}s-s=(-6\pi,6\pi,-2\pi,-2\pi,2\pi,2\pi)\ne0,\qquad LL^+s-s=0.
   \]
   Thus, if p. 14's A is the adjacency defined earlier, the literal printed step does not solve the Laplace equation; the source's derivation uses L. This flags notation, not an established correction.
2. For the q=1 twist on C6, each edge cosine is 1/2; the weighted Laplacian eigenvalues are 0 (multiplicity 1), 1/2 (2), 3/2 (2), and 2 (1). This verifies local linear stability modulo rotation for this single example only.

Rendered and viewed formula/model pages 3–20 except no formula depended on unread pp. 21–23; p. 19 was rerendered after a blank first image and the second image was visually checked. Formula pages include 6–9 and algorithm p. 14. Full physical-page sequential reading, not these images alone, supports the claimed scope.

## Use and exclusions

This source is eligible only for the exact-equilibrium conditional local Jacobian/weighted-Laplacian certificate from p. 9 Eq. (9), under connectedness and strict positive edge cosine. Its Ansatz-driven global existence/core search remains unproved; the finite-sample detection experiments do not give a whp result for uniform ER. No transfer to signed or oriented graphs is made, and this work does not resolve C106/C107 or C118.

## Review state

Complete full-text read and narrow local-certificate use passed R02 review. The independent review did not endorse Ansatz-driven global existence, heuristic search, finite-sample-to-whp inference, or a signed-graph interface. No mother ledger or skill has been changed.
