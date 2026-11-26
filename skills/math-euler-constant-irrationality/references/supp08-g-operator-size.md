# Quantitative size gate for a Nilsson--Gevrey decomposition

Scoped reference. EXT-0262, SHA `abcad29ca193e2a486b2abe1d74e49124503717a04cabad1e5b4d76710ff852d`, arXiv:2109.08737v1, physical pp. 1--3 and 12--15. This is a preprint-only interface: the proof of the adopted estimate was checked on pp. 12--15, rather than treating the abstract as a certificate.

Use this only after exhibiting a *finite* decomposition
\[
 f(z)=\sum_{(\alpha,k,\ell)\in S}c_{\alpha,k,\ell}z^\alpha(\log z)^k f_{\alpha,k,\ell}(z),
\]
where every \(f_{\alpha,k,\ell}\) is a nonzero G-function and (L_{\alpha,k,\ell}\) is its minimal operator over \(\mathbb Q(z)\).  Put
\(\kappa=\max_S k\) and
\(A=\{\alpha:\exists k,\ell\;(\alpha,k,\ell)\in S\}\).  Then the source's Theorem 2 gives, for the minimal operator \(L\) of \(f\),
\[
 \sigma(L)\leq\max\!\left\{
  1+\log(\kappa+2),\;
  2(1+\log(\kappa+2))\log\!\left(\max_{\alpha\in A}d(\alpha)\right),\;
  \max_{(\alpha,k,\ell)\in S}(1+\log(k+2))\sigma(L_{\alpha,k,\ell})
 \right\}.
\]
Here (d(\alpha)) is the least positive denominator of \(\alpha\), and \(\sigma\) is the p-adic size of the differential module/operator; it is not an archimedean height or an irrationality exponent.

The checked proof passes from the summands to (L) using sums and products of solution modules, controls tensor products by
\(\sigma(M_1\otimes\cdots\otimes M_N)\leq(1+\log N)\max_i\sigma(M_i)\), then uses
\(\sigma(d/dz-\alpha/z)\leq2\log d(\alpha)\) and \(\sigma(z(d/dz)^2+d/dz)\leq1\).  Thus the substantive prerequisites are: a proved finite Nilsson--Gevrey representation, actual minimal operators or valid upper bounds for their sizes, and the stated G-function hypotheses.  Do not infer such a representation from numerical fitting.

For Euler's constant, this can only audit a proposed differential-equation route after its relation to \(\gamma\), all connection constants, and an integer linear-form/denominator argument are independently proved.  Finite size does not itself prove irrationality, nor identify \(\gamma\) as a G- or E-value.
