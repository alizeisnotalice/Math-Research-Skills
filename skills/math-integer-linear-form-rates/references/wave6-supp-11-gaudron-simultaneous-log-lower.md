# Simultaneous lower bounds for algebraic logarithmic forms

**Source and version.** Éric Gaudron, *Minorations simultanées de formes
linéaires de logarithmes de nombres algébriques*, **Bulletin de la Société
Mathématique de France** 142(1) (2014), 1--62,
[doi:10.24033/bsmf.2658](https://doi.org/10.24033/bsmf.2658).  The supplied
primary preprint is arXiv:1004.3652v3; raw PDF SHA-256
`41722386b413e66ae4b3e34fe462de57adbe6268d7fbfa0a80dda6edd31f81e3`.
The formal edition metadata and the exact used theorem were checked; the
adopted statement is on physical page 4 (Theorem 2.1), with its notation set
up on pages 1--8.

**Status and scope.** Scoped reference. This is a published theorem for a
finite *family* of algebraic-logarithmic forms at a chosen Archimedean or
\(p\)-adic place. It supplies a nonvanishing lower-bound input only after all
of its source-defined parameters are constructed. It is not a numerical
certificate for an integer form and does not by itself establish an
irrationality measure.

Let \(k\) be a number field embedded in \(\mathbb C_{p_0}\), let
\(u_1,\ldots,u_n\) be logarithms with \(e^{u_j}\in k\), and let
\[
 \Lambda_i=\beta_{i,0}+\sum_{j=1}^{n}\beta_{i,j}u_j\quad(1\leq i\leq t)
\]
for the coefficient matrix described in the source.  In the source notation,
if at least one \(\Lambda_i\) is nonzero, Theorem 2.1 gives
\[
 \log\max_{1\leq i\leq t}|\Lambda_i|_{p_0}
 \geq -(4n)^{91n^2}a^{1/s}
 \bigl(\log b+a\log e+D\log\log e\bigr)
 \prod_{j\in I}\left(1+\frac{D\log a_j}{\log e}\right)^{1/s}.
\]
Here \(a,b,e,D,I,s\), including their admissibility inequalities, are exactly
the quantities defined in the paper.  Preserve those definitions rather than
substituting informal heights or treating the displayed right side as a
universal constant.

**Safe use.** First fix the place, field, branches of the logarithms, and the
entire finite family.  Prove that at least one chosen \(\Lambda_i\) is
nonzero, construct all source parameters, and only then insert the stated
bound into a separate height/remainder argument.  Pages 5--8 introduce the
adelic-vector-bundle and auxiliary-section framework behind the theorem; no
attempt is made here to reprove it or to turn its constants into code.
