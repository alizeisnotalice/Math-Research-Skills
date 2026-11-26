# Modular rank certificates and endpoint propagation

Source: Qihang Wang, *Hilbert Series in Four Variables and Linear Factors of High Multiplicity*, local PDF SHA-256 \`cb6b597a08a65e5bd5f433f32d6dcea41b00cc19a48590a8abbe8db1d04d4498\`, physical pp. 2-7.  Dependency check: Lemmas 2.1-2.2 are proved in the PDF; the full quintic/septic certificate data referenced by later propositions are not included in this input.

For \(F=(F_1,\ldots,F_r)\in(S_d)^r\), define
\[
\mu^{(d)}_{r,j}(F):S_{j-d}^r\longrightarrow S_j,\qquad
(h_i)\longmapsto\sum_i h_iF_i.
\]
The rank-\(\ge s\) locus is Zariski open.  If an integral specialization has an \(s\times s\) minor nonzero modulo a prime \(p\), that determinant is a nonzero integer, so the same rank locus is nonempty over every characteristic-zero field.

The source's endpoint propagation lemma says that an injective \(\mu^{(d)}_{b,q}\) and a surjective \(\mu^{(d)}_{a,q+1}\), for \(a\le b\), propagate the corresponding endpoint behavior over the specified prefix block.  A certificate must therefore include: the exact integral forms, prime, selected minor, matrix basis order, and endpoint maps.  A modular pass does not establish a characteristic-\(p\) generic Hilbert-series claim.
