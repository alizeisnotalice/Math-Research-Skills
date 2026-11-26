# Finite compression and perturbation certificates from OpenAI operator-algebra sources

Use these components only after the represented algebras, Hilbert spaces, matrix conventions, and norm topology have been fixed.  They are finite- or representation-level certificates; none decides an abstract classification problem by itself.

## Scalar compression from a small-trace matrix projection

**Source.** *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI (23 September 2026), physical pp. 4–5, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/paper.pdf), SHA-256 `df6227b61598580506210a8236216e043d1acd4ba062a9901b3063559ff62a5a`.

For a subgroup \(\Lambda\le K\), the reduced inclusion \(C_r^*(\Lambda)\subseteq C_r^*(K)\) is isometric and preserves the canonical trace and its *unnormalized* matrix extension
\[
 \tau_{\Lambda,N}(x)=\sum_{j=1}^N\tau_\Lambda(x_{jj}).
\]
Given a projection \(p\in M_N(C_r^*(\Lambda))\) with \(a=\tau_{\Lambda,N}(p)\) and \(a<(3-\sqrt5)/2\), set \(K=\Lambda*F_N\), \(U=(\lambda_K(t_1),\ldots,\lambda_K(t_N))\), and \(A=pU^*Up\).  The source obtains the lower bound \(\|U\xi\|\ge(\sqrt{1-a}-\sqrt a)\|\xi\|\) for \(\xi=p\xi\), hence \(A\) is invertible in the corner and
\[
 e=(Up)A^{-1}(Up)^*\in C_r^*(K),\qquad \tau_K(e)=a.
\]
Reusable output: a checkable conversion of a supplied small-trace matrix projection into a scalar projection.  Keep the strict trace threshold and the unnormalized trace convention.

## Rectangular derivation implementation

**Source.** *Kadison's similarity theorem through uniform derivation estimates*, OpenAI (23 September 2026), physical pp. 5–6, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026/paper.pdf), SHA-256 `6c1ce1a87b0498395bf39facdf1eff7f474c294497798cc7cc51ba7ef0b491da`.

For unital *-representations \(\sigma:A\to B(K)\), \(\lambda:A\to B(F)\), a rectangular derivation satisfies
\[
 \Delta(ab)=\Delta(a)\sigma(b)+\lambda(a)\Delta(b).
\]
Its finite-matrix diagnostic is the unital triangular homomorphism
\[
 \Phi(a)=\begin{pmatrix}\lambda(a)&d^{-1}\Delta(a)\\0&\sigma(a)\end{pmatrix},\quad d=\|\Delta\|>0.
\]
The stated conclusion is: if \(\Delta\) is completely bounded then there is \(V\in B(K,F)\) with \(\Delta(a)=V\sigma(a)-\lambda(a)V\), and one may take
\[
 \|V\|\le d\left(1+\|\Delta\|_{cb}/d\right)^2.
\]
Use the triangle construction to package a proposed derivation; report separately any method used to bound \(\|\Delta\|_{cb}\).

## Sequence-envelope and strong perturbation steps

**Source.** *Close Separable C*-Algebras Without Spatial Conjugacy*, OpenAI (5 October 2026), physical pp. 2–3, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Close-Separable-Cstar-Algebras-Without-Spatial-Conjugacy-October-5-2026/paper.pdf), SHA-256 `1ea2edc84a981a7ec7287034d2af336e64e6fbff569a85d53517932294d8b903`.

For a unital norm-separable \(D\subset B(L)\) and \(P\subset D\), form
\[
 E_D(P)=c_0(\mathbb N,D)+\{(p,p,\ldots):p\in P\}.
\]
The source proves norm separability and exact preservation \(d_{KK}(E_D(P),E_D(Q))=d_{KK}(P,Q)\); a unitary conjugacy of envelopes forces one normalizer sequence to approximate every element of \(Q\) by conjugates of elements of \(P\).  Reuse this as an explicit reduction from a common-normalizer obstruction to a spatial-conjugacy obstruction.

**Scoped reference.** *Near Inclusions of von Neumann Algebras Without Small Spatial Embeddings*, OpenAI (5 October 2026), physical pp. 3–4 and 8–10, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Near-Inclusions-of-von-Neumann-Algebras-Without-Small-Spatial-Embeddings-October-5-2026/near-inclusions.pdf), SHA-256 `0e3e4d1bbe2ef13bd40ab9972a1361c3a8da9bd65eaf4f485db18618141bc4a9`.  Under its specific free-group representation construction, the Laurent coefficients obey \(\|A_k(g)\|\le c_k=\mathbf1_{k=0}+2t^{|k|}/(1-t)\).  Its perturbation step replaces almost projections by \(Q_i=1_{(1/2,\infty)}(T_i^*T_i)\), then uses the polar part of \(S=P E+(I-P)(I-E)\) to conjugate \(E\) to \(P\).  Apply only when the commuting-algebra and norm-convergence hypotheses shown there have been established.

**Source.** *Universal strong Kadison–Kastler stability*, OpenAI (23 September 2026), physical pp. 7–9, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026/paper.pdf), SHA-256 `3e801d4ed2d8c928e93581e9c4e53fd5d6c4a5ba0b1165ec61d83ae4b7f79691`.

The local correction interface is: bound \(\operatorname{dist}(h,A')\) by \(\|\operatorname{ad}_h|_A\|_{cb}\), polar-decompose an invertible intertwiner close to the identity, and then use the source's completely-positive correction criterion.  Treat the distance estimate, the required cb norm, and the closeness constant as separate inputs rather than silently upgrading a pointwise commutator estimate.
