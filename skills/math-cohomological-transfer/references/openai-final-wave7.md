# Albanese-maximal group-extension obstruction

**Source.** *The Abelianity Conjecture for Special Compact Kähler Manifolds*,
pp. 2, 5–9, 17, 29, 42, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/paper.pdf).

**Input.** Supply an exact extension
\(1\to N'\to G'\to\Lambda\to1\), where \(\Lambda\) is the lattice of a
maximal quasi-Albanese torus after the source's finite-isogeny construction.
Require a certified equality \(b_1(X')=2\dim A'\), injection
\(H^2(\Lambda,\mathbb C)\to H^2(G',\mathbb C)\), and the finite character
step making a common eigenvector of \(\operatorname{Hom}(N',\mathbb C)\)
\(\Lambda\)-invariant.

**Procedure.** Apply inflation--restriction:
\[
0\to H^1(\Lambda,\mathbb C)\to H^1(G',\mathbb C)
\to\operatorname{Hom}(N',\mathbb C)^\Lambda\to H^2(\Lambda,\mathbb C).
\]
The supplied \(H^2\)-injection kills transgression. A nonzero invariant then
contradicts the Albanese Betti-number equality. Hence
\(\operatorname{Hom}(N',\mathbb C)=0\); when \(N'\) is finitely generated this makes its abelianization finite.

**Boundary.** The interface does not establish specialness, the maximal
Albanese cover, torsion of character-support points, the \(H^2\) injection, or
finite generation. Those remain original global/analytic dependencies.

## 固定来源

- 物理页 2, 5, 6, 7, 8, 9, 17, 29, 42。§§2–6, especially final inflation--restriction argument on p. 42 SHA-256 `dfbf9ad2335b9d20dedd8a2ae527ebb45b74155a976acc6d284dd851144e22b8`。[The abelianity conjecture for special compact Kähler manifolds](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/paper.pdf)
