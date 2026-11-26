# Euler T-sums by tangent--digamma residues (EXT-0055)

Verified source: arXiv:1906.07654v4, local SHA-256 `b56b2880253e0c4cf18396930f85617fc43e64088941b1d91186af9dbd920762`, 25 physical pages.

Physical p.4 defines the parametric digamma kernel and records expansions at integral and half-integral poles. For integers `p,q>1`, physical p.6, Theorem 2.4 applies the kernel

`F_{p-1,q}(s)=pi tan(pi s) Psi^{(p-1)}(1/2-s)/(s^q (p-1)!)`

to obtain the displayed reduction for `(1-(-1)^(p+q)) T_{p,q}` in terms of Hoffman t-values and zeta values. Theorem 2.3 is the `p=1` counterpart.

Actual proof steps used are not merely a table lookup: list poles at `0`, integers, and signed half-integers; substitute expansions (2.2)--(2.7); calculate each residue; and use the residue theorem. A zero parity prefactor means the formula cannot be divided through in that case. Inputs outside `q>1`, or with unverified convergence/residue cancellation, are out of scope.
