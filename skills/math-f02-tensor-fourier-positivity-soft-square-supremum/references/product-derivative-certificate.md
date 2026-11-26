# Affine product derivative certificate

For finite \(d\), let \(z_j(s)\) be affine complex functions on an interval
\(I\), and suppose, pointwise on \(I\),
\[
 |z_j|\leq e^{-c u_j},\qquad |z_j'|\leq A u_j,
 \qquad c>0,\ A\geq0,\ 0\leq u_j\leq w.
\]
Writing \(U=\sum_j u_j\) and \(M=\prod_jz_j\), affinity gives the exact
finite product rule
\[
 M^{(k)}=k!\sum_{|E|=k}\prod_{j\in E}z_j'\prod_{j\notin E}z_j.
\]
Thus
\[
 |M^{(k)}|\leq k!A^k e^{-cU}
 \sum_{|E|=k}\Bigl(\prod_{j\in E}u_j\Bigr)e^{c\sum_{j\in E}u_j}
 \leq A^ke^{ckw}e^{-cU}U^k.
\]
Here \(k!e_k(u)\leq U^k\) follows by retaining only distinct-index terms
in the nonnegative expansion of \(U^k\).  Finally,
\(e^{-cU}U^k\leq c^{-k}k!\) follows from
\(e^{cU}\geq(cU)^k/k!\).  No decimal approximation is required.

If \(k>d\), the displayed sum is empty and the derivative is zero.  For
\(k=0\), the same formula gives \(|M|\leq1\), because the assumptions imply
\(e^{-cU}\leq1\).  The uniform constant depends on \(A,c,w,k\), but not on
the number of factors.

## Source and scope

Mirek--Szarek--Wróbel, *Dimension-free estimates for discrete maximal
functions over cubes in \(\mathbb Z^d\)*, arXiv:2609.24030v1 (21 September
2026), Proposition 3.1, PDF pp. 4--5.  The historical local-PDF SHA-256 is
`01a4d818f5fb3fd69257039b3189812d48d3c13fe5614913b083bc23f724a701`.
The checked source specializes to
\(z_{N,s}=(1-s)a_N+sb_N\), \(A=7\), \(w=1\), and
\(c=1-s_0\); Lemma 2.1 on PDF pp. 3--4 supplies the factor derivative
bound.  The official versioned HTML exposes equations (3.1)--(3.3) and
Proposition 3.1 at [arXiv v1](https://arxiv.org/html/2609.24030v1).

Only this product-rule component is transferred.  The paper's later
fractional-integration/interpolation argument, its discrete-cube \(\ell^p\)
conclusion for \(1<p<\infty\), and all maximal-function conclusions require
additional hypotheses and are not part of this certificate.
