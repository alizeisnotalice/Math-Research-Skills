# Exact generalized hyperharmonic coefficients

## Source and adopted proof route

Ce Xu, *Euler sums of generalized hyperharmonic numbers*, arXiv:1701.00391v2
(19 Jan. 2018), local PDF pp. 1--13, SHA-256
`c5fe39a0ba79385fd9036b293330fad03b11a4b6e77a0ff199cd156921af6ef0`.
It is a preprint; no journal publication is asserted.

The adopted finite portion is pp. 4--6: Lemma 2.1, generating identities
(2.3)--(2.8), and recurrence (2.11).  The proof differentiates
\((1-z)^{-x}=\sum_n(x)_nz^n/n!\), then evaluates at integer \(x=m\).
Thus the coefficient can be evaluated with exact rational arithmetic as

\[
h_n^{(m)}(k)=\binom{m+n-1}{m-1}
 e_k\!\left(\frac1m,\frac1{m+1},\ldots,\frac1{m+n-1}\right).
\]

For \(k=1,2,3,4\), source equations (2.12)--(2.15) give the equivalent
ordinary-harmonic-number expressions.  The script computes the elementary
symmetric sum by exact dynamic programming and independently checks these
four source contacts.

## Boundary

No claim about the paper's infinite sums \(S(k,m;p)\), zeta reductions, or
Euler--Mascheroni irrationality is adopted.  The preprint dependence used here
is only the displayed generating-function differentiation proof through (2.8).
