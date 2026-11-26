# q-scaled symmetric orthogonal-polynomial recurrence gate (EXT-0621)

## Version and exact source statement

W. A. Al-Salam and M. E. H. Ismail, *Orthogonal Polynomials Associated with the Rogers--Ramanujan Continued Fraction*, **Pacific Journal of Mathematics** 104(2) (1983), 269--283, DOI [10.2140/PJM.1983.104.269](https://doi.org/10.2140/PJM.1983.104.269).  The local PDF is the published journal issue, SHA-256 `3e4e9330819d3a3cea341b5eee70119ac28bcf07ffc29dfbf5e76a12ed6529de`, 19 physical pages.  The characterization statement is on PDF p. 3 and the coefficient conclusion is on p. 6; the general orthogonality relation is Theorem 5.1 on p. 14.

## Reusable finite recurrence screen

For a **symmetric** orthogonal polynomial sequence normalized by
\[
 P_0(x)=1,\qquad P_1(x)=cx\quad(c\ne0),\qquad
 P_n(x)=xP_{n-1}(x)-\lambda_nP_{n-2}(x),
\]
the source characterizes the additional property that the scaled sequence `P_n(q^n x)` is again an OPS.  Under the source's real positivity setting, it forces the geometric coefficient pattern stated there (equivalently, after its normalization, `c\lambda_n=\lambda_2q^{2n-4}` for the indicated `n` range).  A broader recurrence family used later is
\[
 U_{n+1}(x;a,b)=x(1+aq^n)U_n(x;a,b)-bq^{n-1}U_{n-1}(x;a,b),
\]
with `0<q<1`, `b>0`, `a>-1`.  For the general symmetric solution `p_n`, Theorem 5.1 gives a positive discrete orthogonality measure when `c>0`, `b>0`, and `1+aq>0`.

## Gate and boundary

Use this only to recognize or reject a supplied finite recurrence after separately establishing the OPS, symmetry, normalization, parameter range, and q-scaling claim.  It is not a recurrence for Euler's constant, does not turn a Rogers--Ramanujan continued fraction into a gamma continued fraction, and does not yield irrationality from convergence alone.  The publication relies on Favard-type orthogonality infrastructure and its own q-series/continued-fraction analysis; those hypotheses are not created by a coefficient pattern match.
