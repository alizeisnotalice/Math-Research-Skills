> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see review index (historical project reference; target is outside the runtime package).

# PGEL-011 — Guarantees for Spontaneous Synchronization on Random Geometric Graphs

## Identity and reading record
Pedro Abdalla, Afonso S. Bandeira, and Clara Invernizzi, “Guarantees for Spontaneous Synchronization on Random Geometric Graphs.” The local read is arXiv:2208.12246v2 (15 February 2024), [official arXiv record](https://arxiv.org/abs/2208.12246), with arXiv identifier DOI [10.48550/arXiv.2208.12246](https://doi.org/10.48550/arXiv.2208.12246). The separately verified journal publication is SIAM Journal on Applied Dynamical Systems 23(1), 779–790 (2024), published 7 March 2024, journal DOI [10.1137/23M1559270](https://doi.org/10.1137/23M1559270). R05 verified both official records and the metadata. The exact 14-physical-page local file is the arXiv v2 PDF, SHA-256 `6fd995cd07bfc86927603c687f6c008b335dbc4ff69738cfc54f4df13d58fea6`; journal full-text equivalence was not checked. Reader L03 read all physical pages 1–14 in order, including proofs and references. No accepted canonical full-read match was found by exact title or PDF hash. R05 L03_B4 helper-stage review passed; mother-card hash binding is pending.
## Model and terminology

The graph is a random geometric graph on the sphere: (X_1,\ldots,X_n\) are i.i.d. uniform on (S^{d-1}\), and (i\sim j\) iff \(\langle X_i,X_j\rangle\ge\tau(p,d)\), with the threshold chosen so each edge has marginal probability (p\). Edges are dependent. The Kuramoto model is homogeneous, with identical natural frequencies and positive, symmetric, unweighted adjacency.

The paper’s Definition 1 (physical p. 5) calls a graph “globally synchronizing” when **every local minimum** of the associated energy is constant modulo rotation. This is a landscape statement, stronger than showing convergence for one selected initialization. The energy used on physical p. 2 is \(E_G(\theta)=\sum_{i,j}a_{ij}(1-\cos(\theta_i-\theta_j))\).

## Theorems and hypotheses

The simplified Theorem 1 (physical p. 4) gives two sufficient regimes, with probability tending to one:

1. \(np=\Omega(\log^2 n)\) and \(d=\widetilde\Omega(n^2p^2)\);
2. \(np=\Omega(\log^{10} n)\) and \(d=\Omega(\log^3 n)\).

The more precise Theorem 3 (physical p. 7) states: for every fixed \(\alpha>0\), there are absolute constants \(C_p,C_d>0\) such that if

\[
d\ge C_d(n^2p^2+\log^4n)\log^4n,\qquad \alpha/n<p<1/2,\qquad np\ge C_p\log^2n,
\]

then the graph globally synchronizes with probability at least \(1-n^{-\Omega(1)}\).

The deterministic sufficient criterion invoked as Theorem 2 (physical p. 6) uses \(\Delta_A=A-pJ_n\), \(\Delta_L=L+pJ_n-npI_n\), with \(L=D-A\), and requires

\[
\frac{\|\Delta_A\|}{np}<\frac1{12},\qquad
\frac{\|\Delta_L\|}{np}<\frac14,
\]

and

\[
\frac{\pi/4}{\sin^{-1}(12\|\Delta_A\|/(np))}
>
\frac{\log(n/6)}{\log(np/(2\|\Delta_L\|)-1)}+1.
\]

For the second regime, Theorem 4 (physical p. 11) prints \(d=C_d\log^3n\), \(np=C_n\log^{10}n\) and concludes synchronization with high probability. Its following prose says the same result holds for any range of \(p=o(1)\); the explicit usable range supplied immediately afterward is Corollary 1: if \(np\ge C_n\log^{10}n\) with \(C_n>2304\), then for some absolute \(C_d\), \(d=C_d\log^3n\) implies \(\|\Delta_A\|/(np)<1/(48\log n)<1/12\) with high probability. Keep this explicit corollary separate from the unexpanded prose extension.

## Proof route and dependencies

For Theorem 3 the paper verifies the deterministic criterion by coupling the RGG between Erdős–Rényi graphs \(G^-\sim G(n,p(1-\epsilon))\) and \(G^+\sim G(n,p(1+\epsilon))\), with \(G^-\subseteq G\subseteq G^+\) with high probability. It combines a standard centered-adjacency norm bound for ER graphs, a Chernoff bound for degree fluctuations, Laplacian quadratic-form monotonicity under edge inclusion, and the deterministic criterion. The proof adds self-loops for the convenient matrix centering \(\mathbb E A=pJ_n\), explaining that this does not change the Kuramoto energy; do not silently mix this convention with a loopless adjacency matrix.

For Theorem 4, a high-dimensional RGG spectral bound gives \(\|\Delta_A\|/(np)\le\max\{(1+\epsilon(d,\tau))\tau,\log^4n/\sqrt{np}\}\), where \(\epsilon(d,\tau)\to0\) when \(d\tau^2\to\infty\). The proof then checks the deterministic criterion. The tail relation in Lemma 3 is stated for fixed \(p<1/2\); its use in the vanishing-(p\) argument is combined with the explicit spherical-cap bounds printed in the lemma. The proof is on physical pp. 11–12.

## Transfer limits

This is a positive, symmetric, high-dimensional random-geometric-graph result. It supplies a spectral-concentration-to-landscape route and exact conditions for that route. It does not cover signed edges, an oriented/nonpotential system, or fixed low-dimensional (S^2). Theorem 3’s definition excludes spurious local minima; it is not just a trajectory theorem for one smooth initial condition. No source defect was identified in the rendered theorem/proof pages; all formulas used here were checked against rendered source pages 2, 4–12.

Complete physical-page and section coverage is recorded in `../reading_coverage.json` (mother source entry PGEL-011; rendered images remain in `../renders/PGEL-011/`).
