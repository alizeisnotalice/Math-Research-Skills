# Scoped transfer patterns from OpenAI arithmetic-2 sources

These are source-indexed, conditional patterns, not replacements for cited
theorems. Each use must supply all stated hypotheses.

## Finite slice detects a nonzero nearby-cycle stalk

**Source.** *The Restricted Geometric Langlands Equivalence in Positive
Characteristic*, pp. 29–30, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/paper.pdf).

**Input.** Over an excellent complete strictly henselian DVR, take a smooth
affine chart, a point in the closure of a nonzero-stalk locus, and a permitted
singular-support cone with the cited half-dimensional bound. Choose a cotangent
plane transverse to that cone and lift a basis to equations \(f_1,\ldots,f_d\).

**Procedure.** On \(J=V(f_1,\ldots,f_d)\), isolate the special point and
retain a generic generization. Replace its quasi-finite neighbourhood by a
finite henselian local factor \(Q\). Proper compatibility gives
\[
(\Psi_QH)_u\simeq R\Gamma(Q_K,H)\simeq\bigoplus_{x\in|Q_K|}H_x.
\]

**Output.** A nonzero generic stalk produces a nonzero nearby-cycle stalk,
which may contradict an independently established microlocal vanishing result.

**Boundary.** It neither proves the support/singular-support premise nor
identifies monodromy; the calculation forgets inertia action.

## Marked Hecke singular-support test

**Source.** *Tame Hecke Eigensheaves with Several Marked Points*, pp. 1–2,
13, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/Tame-Hecke-Eigensheaves-with-Several-Marked-Points.pdf).

**Input.** Let \(X\) be a smooth projective geometrically connected curve of
genus at least two over a finite field of characteristic \(p>n\ge2\), with
at least two rational marked points, Borel level and \(G=\mathrm{SL}_n\).
The eigendata must have the cited lisse tame-unipotent local-system condition
and the stated bounded/proper and exact-position smooth Hecke geometry.

**Procedure and output.** Apply the Hecke eigenrelation chartwise to obtain the
paper's parabolic-nilpotent singular-support conclusion. If a bad
specialization is proposed, use the finite-slice detector above on its
nonzero-stalk closure.

**Boundary.** No claim applies to other groups, \(p\le n\), fewer marked
points, wild/non-unipotent monodromy, or arbitrary Hecke actions.

## Hodge-tensor transport through exact maps

**Sources.** *Algebraic Kuga–Satake Correspondences and Hodge Conjectures on a
K3 Quadratic Locus*, pp. 59–61, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/paper.pdf); *Abelian Covers, Gale Correspondences, and the Hodge Conjecture for Powers*, pp. 17, 31, 44, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf).

**Input.** Provide an inclusion \(i:W_T\hookrightarrow W_U\) of polarizable
rational weight-one Hodge structures, rational Hodge retraction \(p\),
rational polarizations \(E_U,E_T\), and a Hodge map
\(j:H\to\operatorname{End}(W_U)\). For the generic-family route also remove
the cited countable union of proper Hodge loci in the full marked family.

**Procedure.** Put
\[
b=(E_T^\flat)^{-1}i^\vee(-1)E_U^\flat,
\qquad(p\otimes b)\iota_{j,E_U}=\iota_{pji,E_T}.
\]
For abelian \(H^1\)'s, realize rational Hodge maps by normalized transpose
graphs after clearing denominators. In a marked family, a remaining integral
Hodge tensor transports along every path.

**Output.** An already algebraic exact ambient tensor transfers to the exact
restricted tensor, rather than merely to an unspecified nonzero map.

**Boundary.** The source tensor's algebraicity, retraction, exact period data,
and quadratic-locus assumptions are essential; this is not a general Hodge
tensor algebraicity oracle.

## CM four-factor and determinant reduction

**Sources.** *The Rational Hodge Conjecture for CM Abelian Varieties*, pp. 3,
8, 26, 45, 47, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf); *Weil Classes and Hodge Classes on Abelian Powers*, pp. 6, 9–10, 12, 15, 21–23, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/Weil-classes-and-Hodge-classes-on-abelian-powers.pdf).

**Input.** For a four-factor switch take a Galois CM field and odd sign
functions satisfying \(v_1+v_2=v_3+v_4\). For determinant supply, give actual
admissible summands, all-conjugate pair tensors, the stated classical derived
images, and simultaneous balance
\[
\sum_j\epsilon_\gamma(W_j)+\sum_a\epsilon_\gamma(\ell_a)=0
\quad\hbox{for every }\gamma.
\]

**Procedure and output.** Reduce balanced lines to pair tensors and
four-label switches, retaining repeated summands. Use invariant-theory
generators only after the all-conjugate balance check, then move supplied
factors by algebraic correspondences and contractions.

**Boundary.** Hodge type alone is insufficient: the exact sign equality,
balance and source-specific CM/theta supply remain mandatory.

## Global-generation descent by finite analytic norm

**Source.** *B-semiampleness for Compact Log-smooth Kähler Fibrations*,
pp. 30–31, 35–37, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026/paper.pdf).

**Input.** Let \(r:P\to S\) be proper surjective between connected compact
complex manifolds, with Stein factorization \(P\to T\xrightarrow qS\),
\(q\) finite of generic degree \(d\), and \(r^*A^{\otimes n}\) globally
generated.

**Procedure.** Projection formula supplies global generation on \(T\). At a
given base point choose one section nonzero on the whole finite fibre. Take its
finite norm over the covering locus, extend it across branching by local
boundedness and normality, and use \(\operatorname{Nm}_q(q^*c)=c^d\).

**Output.** \(A^{\otimes nd}\) is globally generated. Rational line bundles
follow after clearing denominators and torsion.

**Boundary.** This descends a known globally generated pullback; it does not
test semiampleness. Properness, the Stein factorization, and finite generic
degree are essential, though flatness is not.

## 固定来源

- 物理页 1, 2, 13。Theorem 1.1; Theorems 4.1–4.2 SHA-256 `fb3f3a7a4115f5ec312f24d5f4020b68acb41fd5c672bdc9b5802ad2a86fb259`。[Tame Hecke Eigensheaves with Several Marked Points](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/Tame-Hecke-Eigensheaves-with-Several-Marked-Points.pdf)
- 物理页 29, 30, 31。§7.2 transverse slice and finite henselian factor SHA-256 `52c37d4f70f505c0685f98e590d93f629bb686b0436b645a820d5d3efeb67ea0`。[The Restricted Geometric Langlands Equivalence in Positive Characteristic](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/paper.pdf)
- 物理页 1, 17, 31, 44。Lemma 4.3; Lemma 4.14; Proposition 4.2; Lemma 7.7 SHA-256 `3467c8077855a568ec75b4f4c025fa50024cc9944df46346c57fe499fae6c8e8`。[Abelian covers, Gale correspondences, and the Hodge conjecture for powers](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf)
- 物理页 1, 2, 5, 49, 59, 60, 61。Theorems 1.1–1.2; Lemma 9.1; Propositions 9.2, 9.4 SHA-256 `c9fde2b758f255059c3aa153c73971330b18ed67ddd24d3272a1c793cc16dffd`。[Algebraic Kuga–Satake correspondences and Hodge conjectures on a K3 quadratic locus](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/paper.pdf)
- 物理页 1, 2, 3, 8, 26, 45, 47。Theorem 2.5; Proposition 2.6; Theorem 5.1; Corollary 6.7 SHA-256 `6e3e66a407773ad5091d4cb48d9b4dc55a69c58fb0948a88daf19f3bb21bf27b`。[The rational Hodge conjecture for CM abelian varieties](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf)
- 物理页 1, 3, 6, 9, 10, 12, 15, 21, 22, 23, 24, 94。Lemma 2.1; Theorem 2.5; Lemma 3.3; §3.6 SHA-256 `c035db86eb70657344f5b43f1a1b9a39952b946a9dca4cde21cf047300dfdbde`。[Weil classes and Hodge classes on abelian powers](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/paper.pdf)
- 物理页 1, 2, 3, 27, 30, 31, 33, 35, 36, 37。Theorem 1.1; Lemmas 7.3–7.4, 8.3; Proposition 7.5 SHA-256 `afad4b593eede2ddf61795187a33ccddbf38dd470c67580982682623ae351d19`。[B-semiampleness for compact log-smooth Kähler fibrations](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026/paper.pdf)
