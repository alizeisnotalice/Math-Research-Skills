# Elliptic q-difference special-ring criterion

Source checked: Ehud de Shalit, Charlotte Hardouin, and Julien Roques, *Hypertranscendence and q-difference equations over elliptic functionfields*, arXiv:2409.10092v1 (2024), physical pp. 1--5 and 36--39.

## Certified caller contract

Fix a commensurability class of complex lattices and its elliptic-function field $K$. Let $q\ge2$, let φ act by $g(z)\mapsto g(qz)$, and work in $F=\mathbb C((z))$. Let $f\in F$ be known to satisfy a homogeneous linear φ-difference equation over $K$.

For the fixed reference lattice Λ₀, set
\[
 S=K[z,z^{-1},\zeta(z,\Lambda_0)].
\]
The source's main theorem gives the exact equivalence
\[
 f\text{ is differentially algebraic over }K
 \quad\Longleftrightarrow\quad f\in S.
\]

Thus a caller may conclude differential transcendence only after a proof that $f\notin S$, or may record differential algebraicity only after a proof of membership. The criterion is structural; it does not provide a general decision procedure for special-ring membership.

## Audit boundary

The field, automorphism, Laurent-series embedding, and derivation are fixed in pp. 4--5. The proof uses parametrized Picard--Vessiot theory, monodromy, and a final rank-one inhomogeneous reduction (pp. 36--39). Do not apply it to a generic q-recurrence, a different base field, a non-linear equation, or a value at a point without separately checking those changes.
