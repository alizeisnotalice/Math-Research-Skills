# Proposed primitive: zero-slope apex transport

**Source.** *Prescribed Large-volume Charges on Threefolds with Trivial
Canonical Bundle*, pp. 4–5, 43, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/paper.pdf).

## Input contract

Fix a polarized smooth projective threefold and a rational transverse twist as
in the source. For every finite-slope zero-tilt-slope semistable object at an
apex \((A,b)\), with \(A>0\), establish
\[
D_A(E)\le C S_A(E),\qquad C\ge0,
\]
where \(D_a=z_b-a^2d_b/6\) and
\(S_a=\Delta(E)d_b=d_b-a^2r(E)^2d_b\ge0\). The source's
Harder--Narasimhan/discrete-discriminant continuation hypotheses are required.

## Exact transfer

Along a fixed-class zero-slope branch the source gives
\[
D'_a=-a^3S_a,\qquad S'_a=-a r(E)^2 S_a/d(a)^2.
\]
Use the comparison derivative for \(D_a-k(a)S_a\), continuing a strict
violation through stable factors if semistability changes. Its exact constants
are
\[
R_0=A+3CA,\qquad k_0=\max\{C+A^2/6,\;CR_0A\}.
\]

## Output

For all positive \(a,b\), the cited proposition yields
\(D_a(E)\le k_0d_b(E)\); for \(a>R_0\), it yields \(D_a(E)\le0\).
Thus a fixed-apex certificate gives an all-volume correction and an
uncorrected large-volume tail.

## Boundary

This is a numerical transport primitive, not a construction of a Bridgeland
heart, a proof of the apex estimate, or a test of tilt semistability. It is
restricted to the source's zero-slope branch and discrete continuation rules.

## 固定来源

- 物理页 1, 3, 4, 5, 8, 43。Theorem 1.2; Corollary 1.3; Lemma 2.1; Proposition 7.1 SHA-256 `84ce978a670157043e5a8bc24583d2eb290cecf379a9f1ec495b6084e8c3f3f2`。[Prescribed large-volume charges on threefolds with trivial canonical bundle](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/paper.pdf)
