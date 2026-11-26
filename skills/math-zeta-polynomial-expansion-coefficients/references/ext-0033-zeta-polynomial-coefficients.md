# Exact coefficients in a Riemann-zeta polynomial expansion

Source reviewed: local arXiv:2512.11405v5, *A new expansion of the Riemann
zeta function*; physical pages 11--15 of the reviewed 26-page PDF.

Lemma 4 (p.13) supplies the finite binomial transform after the
Ramanujan-summation setup. Theorem 6 (p.15) states, for (m\geq1),

\[
x_m=\gamma+\sum_{k=1}^{m}\binom{m}{k}(-2)^k\zeta(k+1)+r_m,
\qquad
r_m=(-1)^{m+1}+\sum_{k=1}^{m}\frac{1+(-1)^{k-1}}{k},
\]

and (x_0=\gamma-1). The displayed examples on the same page give the
first five coefficients. The source's Theorem 6 asserts an infinite expansion
of ζ in (0<\Re(s)<1); Lemma 3 and the preceding argument (pp.11--14)
supply its convergence justification.

This component keeps only the finite exact coefficient map. It neither
evaluates ζ-values nor turns the expansion into an irrationality or linear
independence result.
