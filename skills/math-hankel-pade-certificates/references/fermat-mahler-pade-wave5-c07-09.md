# Fermat-reciprocal Mahler--Padé lifting

**Source and version.** Michael Coons, *On the rational approximation of the
sum of the reciprocals of the Fermat numbers*, arXiv:1112.5072v1 (21 December
2011), local source SHA-256
`a2d960cd282dd6dba219077b46bc62d692e8ce55b08a0a9c76e6372699f8e378`.
The adoption uses physical pp. 1--2 and verifies the needed Padé/Hankel and
lifting steps on pp. 19--21.

## Scoped input and formulas

For `epsilon in {-1,1}`, set

\[
 H_\epsilon(z)=\sum_{n\ge0}\frac{z^{2^n}}{1+\epsilon z^{2^n}}.
\]

Thus `H_1(1/2)` is the reciprocal-Fermat sum.  The paper proves
`mu(H_epsilon(1/b))=2` for each integer `b>=2` (Theorem 1, physical p. 2).
For finite certification, its usable chain is:

1. A mod-2 Hankel determinant argument gives nonzero shifted Hankel
   determinants for the coefficient sequence of `H_epsilon` (Theorem 3,
   Corollary 9, physical pp. 15--18).
2. If an integer-coefficient series `C` has the relevant nonzero Hankel
   determinants, the `[k-1/k]` Padé remainder has leading coefficient
   `det(H_{k+1})/det(H_k)`; after the shift this produces nonzero `h_k` and
   polynomials `P_k,Q_k` with
   \(H_\epsilon(z)-P_k(z)/Q_k(z)=h_kz^{2k+1}+O(z^{2k+2})\)
   (Lemma 10--11, physical p. 19).
3. The exact functional identity
   \[
   H_\epsilon(z^{2^m})=H_\epsilon(z)-
   \sum_{j=0}^{m-1}\frac{z^{2^j}}{1+\epsilon z^{2^j}}
   \]
   lifts that Padé remainder to order `2^m(2k+1)` (physical pp. 20--21).
   Evaluate at `z=1/b`, clear the explicitly bounded polynomial degrees, and
   then use the source's two-sided error and denominator bounds.

Run `python3 scripts/fermat_mahler_prefix_wave5_c07_09.py --input
examples/fermat-mahler-prefix-wave5-c07-09.json` to verify a requested finite
coefficient prefix of the functional identity exactly.  This is only the
algebraic lifting gate, not a certificate of the infinite Hankel theorem or
irrationality exponent.

## Boundary

Scoped reference. The source is a preprint and the retained result is only
for this two-sign Fermat/Golomb family and integer `b>=2`.  The finite script
does not prove nonvanishing for every Hankel order, the asymptotic two-sided
Padé error, denominator growth, or `mu=2`; those are the source's required
global steps.  It does not apply to an arbitrary Mahler function merely from
a finite prefix identity.
