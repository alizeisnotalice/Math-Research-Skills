> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-003 — Expander graphs are globally synchronizing

## Identity and reading record

- Pedro Abdalla, Afonso S. Bandeira, Martin Kassabov, Victor Souza, Steven H. Strogatz, and Alex Townsend. *Advances in Mathematics* 488 (2026), article 110773, DOI [10.1016/j.aim.2025.110773](https://doi.org/10.1016/j.aim.2025.110773); source actually read: arXiv:2210.12788v4 (19 January 2026), [official arXiv record](https://arxiv.org/abs/2210.12788).
- Local PDF: `../pdfs/PGEL-003.pdf`; 35 pages; SHA-256 `f70f8f651dbac9199b1eea03017ba649adf3d236a32e1f631d85eb59d8605798`.
- Strict PDF parse, page count, hash, and title/version identity checked against the D02 identity manifest. Read all 35 physical PDF pages in order, including the bibliography. Rendered pp. 3 (Theorem 1.2), 5, 7, 9, 13 and 27 for theorem, definition, proof, and Theorem 6.2 root-equation checks. Coverage is in ../../reading_coverage.json.
- Review pending. No claim that the arXiv text was line-by-line compared with the 2026 journal version.

## Model and meaning of global synchronization

The paper treats the homogeneous Kuramoto model on simple undirected, unweighted graphs: identical intrinsic frequencies are removed by a rotating frame, and every present edge has symmetric positive unit coupling. For a fixed graph \(G\), “globally synchronizing” means convergence to the all-in-phase state from almost every initial phase vector. The probability in the random-graph results is over the graph draw, separately from this almost-every-initial-condition quantifier.

The proof uses more than a landscape statement alone. The introduction (PDF p. 3) records that every trajectory of this analytic gradient flow on the compact phase torus converges to a critical point, and that the basin of a strict saddle has measure zero. The argument therefore rules out nonsynchronous equilibria with positive-semidefinite Hessian; it does not claim every critical point is synchronous. Common phase rotation is a symmetry. Stable-state and Hessian arguments are understood with that neutral direction accounted for.

## Main results and hypotheses

**Theorem 1.2 (PDF p. 3).** For each fixed \(\epsilon>0\), a graph drawn from \(G(n,p)\) is globally synchronizing with high probability if
\[
p\ge (1+\epsilon)\frac{\log n}{n}.
\]
The probability tends to one as \(n\to\infty\). This reaches the connectivity scale up to the fixed multiplicative slack; it is not a result at \(p=(1+o(1))\log n/n\) uniformly in a vanishing \(\epsilon\).

For the regular-graph result, an \((n,d,\alpha)\)-expander means \(\|A-(d/n)J\|\le\alpha d\). For the nonregular spectral-expander condition, the paper sets
\[
\Delta_A=A-\frac{d^*}{n}J,\qquad
\Delta_D=D-d^*I,\qquad
\Delta_L=\Delta_D-\Delta_A=L-d^*I+\frac{d^*}{n}J,
\]
requires \(\|\Delta_A\|\le\alpha d^*\), and bounds \(c^-d^*I\preceq\Delta_L\preceq c^+d^*I\).

**Theorem 1.4 (PDF p. 5).** Every \(d\)-regular \((n,d,\alpha)\)-expander with \(\alpha\le0.0816\) is globally synchronizing. The paper defines the expander through the centered adjacency spectral norm. The constant \(0.0816\) uses the numerical parameter checks in §5; the authors report the more conservative analytic theorem as \(\alpha\le0.0068\). Preserve that proof provenance when quoting the sharper constant.

**Theorem 1.10 (PDF p. 7).** For an \((n,d^*,\alpha,c^-,c^+)\)-spectral expander with \(c^->-1\) and \(\alpha\le1/5\), the stated sufficient condition is
\[
\frac{32\alpha(1+4c^+-3c^-)}{(1+c^-)^2}
\log\!\left(\frac{1+c^++\alpha}{2\alpha}\right)<1.
\]
Under this condition \(G\) is globally synchronizing. In the proof of Theorem 1.2, Corollary 6.1 supplies, whp for \(p\ge(1+\epsilon)\log n/n\), an expander with \(d^*=pn\), \(\alpha\le(2+\epsilon)/\sqrt{pn}\), and \(-1<c^-<0<c^+<e-1\); substituting these bounds makes the left side tend to zero.

**Theorem 6.2 (PDF p. 27).** For \(0<\epsilon<1\) and \(1+\epsilon<\gamma<1+\epsilon^{-2}\), let \(p=\gamma\log n/n\), \(d^*=pn\), and \(\alpha=8(\gamma\log n)^{-1/2}\). Let \(-1<c^-<0<c^+\) be the two roots of
\[
\gamma\big((1+c)\log(1+c)-c\big)=1.
\]
Then \(G(n,p)\) is an \((n,d^*,\alpha,c^-,c^+)\)-expander with probability at least \(1-C(\gamma,\epsilon)(\log n)^4n^{-\epsilon}\), and is globally synchronizing with the same probability. This is an explicit finite-size version in the near-connectivity scale; the \(\epsilon,\gamma\) restrictions are part of the theorem.

Theorem 1.4 and Corollary 1.6 also give a high-degree regular-graph application (including Ramanujan graphs at degree at least 600). It is not a theorem about uniformly random 3-regular graphs.

## Proof mechanism and scope

Sections 2–4 exclude nonsynchronous stable states deterministically under expansion hypotheses. The authors use the first two Daido order parameters and a Hessian stability inequality to constrain the phase distribution. A half-circle lemma reduces the task to ruling out any phase outside an open semicircle. Spectral estimates bound edge counts inside and between phase-defined vertex sets; an amplification argument repeatedly forces a small set of outlying phases to shrink until it is empty. Section 5 supplies the numerical parameter checks behind the sharper regular-graph constant. Section 6 proves the adjacency/Laplacian concentration and expander estimates needed for \(G(n,p)\), including the logarithmic failure-probability factors in its finite-size theorem.

This is a positive, symmetric, unweighted graph result. Its energy/Hessian route does not transfer to oriented nonpotential dynamics or to signed edges. In particular, it does not resolve a signed complete-graph threshold such as C118. “Whp globally synchronizing” is not the same as “all critical points are synchronous”; the a.e. basin conclusion uses the gradient-flow and strict-saddle facts stated by the authors.
