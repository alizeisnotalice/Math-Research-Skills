# Exact deficit for projections of the \(\ell_\infty\) ball

**Source.** Jacek Jakimiuk, *Stability of extremal hyperplane projections of
balls in \(\ell_p^n(\mathbb R)\)*, arXiv:2608.21787v1 (2026), physical pages
2--4, raw PDF SHA-256
`c1b3b61ec81c7bee2c24912608a0a1404ba8993d175e9ddd14c8b399705e6020`.

**Status and scope.** Scoped reference.  The preprint's adopted p-infinity
proof is the elementary variance argument on physical page 4.  It starts
from the Cauchy-projection identity on physical page 3; use this card only
when that central-projection normalization has been independently supplied.
No finite-\(p\) result, existence claim, or general M03 stability theorem is
imported.

Let \(a=(a_1,\ldots,a_n)\) satisfy
\[
 a_1\geq\cdots\geq a_n\geq0,\qquad \sum_{i=1}^n a_i^2=1.
\]
Under the source's formula
\[
 \frac{\operatorname{vol}_{n-1}(\operatorname{Proj}_{a^\perp}B_\infty^n)}
 {\operatorname{vol}_{n-1}(\operatorname{Proj}_{(a^{(n)})^\perp}B_\infty^n)}
 =\frac1{\sqrt n}\sum_{i=1}^n a_i,
\]
the deficit has the exact certificate
\[
 1-\frac1{\sqrt n}\sum_i a_i
 \;\geq\;\frac1{4n}\sum_{i,j=1}^n(a_i-a_j)^2.
\]
Indeed, put \(S=\sum_i a_i\).  Cauchy--Schwarz gives \(0\leq
S/\sqrt n\leq1\), so
\[
 1-S/\sqrt n\geq\tfrac12(1-S^2/n)
 =\frac1{4n}\sum_{i,j}(a_i-a_j)^2.
\]

The exact helper `scripts/linf_projection_deficit.py` verifies the rational
normalization, the variance identity, and the rational lower bound.  It does
not evaluate the irrational normalized volume ratio.  Thus it certifies the
algebra only after the displayed geometric volume identity is applicable.
