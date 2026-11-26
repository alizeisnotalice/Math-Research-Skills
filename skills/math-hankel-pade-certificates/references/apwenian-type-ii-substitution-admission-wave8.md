# Type-II apwenian substitution admission

- Source: Guo, Han, and Wu, [*Criteria for apwenian sequences*](https://arxiv.org/abs/2001.10246), arXiv:2001.10246v5, 27 physical pages.
- Verified SHA-256: `b3885e2dc069a7b6836ccc50b1a77d2584fface6e9fa3e56e8934f39ea1cee19`.
- Adopted locus: physical pp. 4 and 12--15, especially (5.1)--(5.3), Theorem 5.2, and its reduction to the sequence criterion.  The connection to Hankel/Padé approximants is on pp. 2 and 6--10.

## Narrow admission rule

Let \(p\ge3\) be odd and let \(v_0=1\),
\(v_j\in\{-1,1\}\).  Extend \(v\) periodically and set
\[
 P(x)=\sum_{j=0}^{p-1}v_jx^j,\qquad
 f(x)=P(x)f(x^p).
\]
If, for every \(0\le j\le p-2\),
\[
 \frac{v_j+v_{j+1}-v_{2j+1}-v_{2j+2}}2\equiv1\pmod2,\tag{A}
\]
then the fixed-point coefficient sequence is apwenian in the source's
terminology: its Hankel determinants are nonzero (indeed have the stated
2-adic parity).  This supplies the otherwise-infinite Hankel-nonvanishing
premise required by the existing Mahler--Hankel admission workflow.

The supplied finite checker verifies the exact input predicate (A), the
functional-equation recurrence, and only a finite prefix of Hankel
determinants.  Its finite prefix does **not** prove the infinite conclusion;
that transfer is precisely the scoped source theorem above.

For an integer \(b\ge2\), the additional nonvanishing condition needed by
the Mahler--Hankel route is automatically true for this particular
\(P\): if \(0<x\le1/2\), then
\[
 |P(x)-1|\le\sum_{j=1}^{p-1}x^j<1.
\]
Thus \(P(b^{-p^m})\ne0\) for every \(m\ge0\).  This elementary argument
does not itself establish transcendence or an irrationality exponent; those
conclusions additionally require the external theorems invoked by the
source.  Use the existing skill's theorem-admission audit for them.

## Checked proof chain

The source defines the type-II fixed point and derives
\(d_{np+j}=v_jd_n\), hence the functional equation, on physical p. 12.
On pp. 13--14 its proof reduces the global sequence criterion to the finite
residue conditions (A) when \(p\) is odd.  The global criterion itself is
proved via the 0--1 Hankel/J-fraction relation on pp. 5--10.  The source's
value-level statement (p. 4) cites separate Padé/Hankel results; it is not
adopted as an automatic value conclusion here.
