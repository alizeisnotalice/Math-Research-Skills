# Geometric-offspring generalized Derrida–Retaux closure

**Source and version check.** Li and Zhang, *Asymptotic behavior of the generalized Derrida–Retaux recursive model*, *Journal of Statistical Physics* 192:98 (2025), DOI [10.1007/s10955-025-03480-3](https://doi.org/10.1007/s10955-025-03480-3), local published/arXiv-v3 PDF, physical pp. 1 and 3–9, SHA-256 `487ec3f399cdf48298d7855a4be016612235cc05b736d91da7cf791293c328fe`.  The local header identifies the published article and DOI.  The adopted closure calculation is checked in its proof of Theorem 1.1 on physical pp. 6–7.

## Finite-dimensional invariant family

For geometric offspring
\[
\Pr(\eta=n)=m^{-1}(1-m^{-1})^{n-1}\quad(n\ge1),\qquad m>1,
\]
and a geometric-type marginal \(G(r,p)\),
\[
G(r,p)(0)=p,\qquad G(r,p)(k)=(1-p)r(1-r)^{k-1}\quad(k\ge1),
\]
the generalized DR update preserves the family.  The source derives it by composing the probability generating function of the geometric offspring sum and then applying the memoryless shift.  The exact two-parameter map is
\[
r_{n+1}=r_n/m-(m-1)p_n/m,
\qquad
p_{n+1}=1-(1-r_{n+1})\left(1-r_{n+1}p_n/r_n\right).
\]
Its proof also records \(\mathbb E(s^{Y_n})=p_n+(r_n-p_n)s/[1-(1-r_n)s]\) before the update.

Use this only when the offspring law is exactly geometric and the initial marginal is exactly \(G(r_0,p_0)\) with \((r_0,p_0)\in(0,1)^2.  It is not a transfer rule for the fixed-binary DR recursion or arbitrary initial/offspring laws.
