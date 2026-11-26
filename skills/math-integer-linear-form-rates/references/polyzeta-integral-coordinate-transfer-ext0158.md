# Vasilyev--Sorokin multiple-integral coordinate transfer

**Source/version.** Stéphane Fischler, *Formes linéaires en polyzêtas et
intégrales multiples*, arXiv:math/0202064v1 (7 February 2002), local PDF
SHA-256 `70f0570f920fb550c317323d52e830e48cb2419ed4caeeb55a5ab57fff2eefd4`,
4 physical pages.  The adopted statement is Theorem 2.1 and Corollary 2.2 on
physical p. 2; the stated change of variables and the finiteness condition for
the target integral occur on the same page.

## Parameter conversion

For `n>=2`, take integer arrays
`p=(a_1,...,a_n,b_1,...,b_n,c_2,...,c_n)` describing the source integral
`J(p)`.  The theorem converts it to the nested-product integral `K(P)` with

\[
 A_k=a_{n+1-k},\quad
 B_k=b_{n+1-k}\ (k\ge2),\quad
 B_1=a_{n-1}+b_n-\sum_{j=2}^n c_j,
\]

\[
 C_k=\begin{cases}
 a_{n+1-k}+b_{n+1-k}-\sum_{j=k}^n c_j,&k\text{ even},\\
 \sum_{j=k}^n c_j-a_{n-k},&k\text{ odd},\ k\ge3.
 \end{cases}
\]

The equality `J(p)=K(P)` is the source's theorem, from the explicitly stated
alternating coordinate substitution on p. 2.  Before attempting a series or
linear-form expansion, check the source's target convergence gate:

\[
 A_k,B_k\ge0\quad(1\le k\le n),\qquad
 \sum_{k=2}^n(C_k-B_k)_+\le B_1.
\]

`scripts/check_polyzeta_coordinate_transfer_ext0158.py` performs only this
integer parameter conversion and target-gate check exactly.

## Scope

Scoped reference. The four-page preprint states that the equality follows
from the displayed change of variables, but it does not provide a separately
expanded Jacobian proof on the page; use the theorem only for the stated
integral families.  The checker does not prove convergence of `J`, evaluate
either integral, expand a multiple zeta series, supply denominator estimates,
or establish a nonzero integer linear form/rate.
