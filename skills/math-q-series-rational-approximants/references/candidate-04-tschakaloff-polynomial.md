# Tschakaloff finite q-polynomial certificate

Scoped reference for Wadim Zudilin, *An elementary proof of the irrationality of
Tschakaloff series*, arXiv:math/0506086v1, SHA-256
`2a2f512086e806c1c4ffc9c4739a3a5683f5b1049b209e1283421d47b681671a`.

## Extracted finite construction

For an integer \(n\geq1\), source equations (3)--(6), on physical p. 2, define

\[
 R_n(T;q)=\prod_{j=1}^{n}(1-q^jT)=\sum_{k=0}^{n}C_{k,n}(q)T^k.
\]

They give \(C_{k,n}\in\mathbb Z[q]\) and
\(\deg C_{k,n}\leq n(n+1)/2\).  Thus, if \(q=q_1/q_2\) with nonzero
integers \(q_1,q_2\),

\[
q_2^{n(n+1)/2}C_{k,n}(q_1/q_2)\in\mathbb Z.
\]

For nonzero rational \(z=z_1/z_2\), equations (8)--(10) (physical pp. 3--4)
express a finite scaled linear form \(\widetilde I_n=B_nT_q(z)-A_n\), with
\(A_n,B_n\in\mathbb Z\), from these coefficients and the truncated sums in (8).

## Replay boundary

`scripts/tschakaloff_finite_certificate.py` constructs the coefficient list by
exact polynomial multiplication and evaluates the displayed finite formula for
\(A_n,B_n\) using `Fraction`.  It verifies the coefficient denominator inclusion
and the claimed integrality of the two scaled finite coefficients.  The tool requires
\(|q|>1\), which is the source's convergence regime for \(T_q\).

The output is a finite arithmetic certificate.  It does not evaluate \(T_q(z)\),
prove a nonzero remainder, check the asymptotics in (11)--(14), or prove the source's
irrationality theorem (whose additional strict logarithmic condition remains a
separate hypothesis).
