# Bai arctangent partial-fraction denominator gate

Source: Yufei Bai, *The irrationality measure of arctan 1/2 is at most
8.585166*, arXiv:2608.19782v1 (20 August 2026), local source SHA-256
`469bcca0600d0832bc256a70746512540a6285e83e79dd6355673afd816cf597`,
physical pp. 1--3, Lemma 1.

This is a deliberately narrow arithmetic component.  For an integer `n >= 1`,
write the source's even rational function

\[
 R_n(x)=\frac{x^{2n}((x+1)^2+16)^{2n}((x-1)^2+16)^{2n}}
 {(17+x)^{3n+1}(17-x)^{3n+1}}
\]

in the source's partial-fraction form with coefficient `A_j` at
`(17+x)^(-j-1)` (and its symmetric companion), for `0 <= j <= 3n`.
Lemma 1 proves

\[
 2^{-3n-2j+1}5^{n-j}17^{1-j} A_j\in\mathbb Z.
\]

Use this only after matching the rational function and coefficient convention
exactly.  The proof factors the relevant bases in `Z[i]`, tracks the valuations
of the primes over 2, 5, and 17, and then uses `A_j in Q` to descend from
`Z[i]` to `Z`.  It is not a general partial-fraction integrality theorem.

`scripts/verify_bai_arctan_pfd.py 1 2` was run with the local SymPy runtime;
every scaled coefficient was an exact integer for `n=1` and `n=2`.  Those are
finite checks only.  In particular, this card does **not** certify the source's
later contour deformation, saddle asymptotics, linear-form nonvanishing, or
the claimed irrationality-measure bound.
