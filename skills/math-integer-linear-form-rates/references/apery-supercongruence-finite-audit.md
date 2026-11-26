# Generalized Apéry supercongruences: finite p-adic audit

These congruences can be evidence for a proposed p-adic divisibility gain in
an Apéry-type coefficient family.  They do not by themselves yield a common
denominator bound, a small real linear form, or irrationality.

## Verified source and theorem

Robert Osburn and Brundaban Sahu, *Supercongruences for Apéry-like numbers*,
arXiv:0906.3413v3 (12 January 2011), physical PDF pp. 2--5, definition (5),
Theorem 1.1 and its product/valuation proof.  Local source
`EXT-0289_Supercongruences_for_Apery_like_numbers.pdf` has SHA-256
`256eb0988467191b8c5d9ddaaa453d5fb6dabd7c8ebed786f1524807d63fcfd1`.

The version of record is *Advances in Applied Mathematics* **47** (2011),
631--638, DOI [10.1016/j.aam.2011.03.002](https://doi.org/10.1016/j.aam.2011.03.002).
The local archival v3 was checked against its stated published bibliographic
record; all formula locators here refer to that v3 PDF.

For

\[
 C(n,A,B)=\sum_{k=0}^n\binom nk^A\binom{2k}{k}^B,
\]

Theorem 1.1 says that for prime `p>3` and positive `m,r`,

\[
 C(mp^r,A,B)\equiv C(mp^{r-1},A,B)\pmod {p^{3r}}
 \quad(A\ge3),
\]

and modulo `p^(2r)` when `A=2`.  Its proof splits the binomial sum according
to `p | k`; the `p`-free factors are controlled by the product congruences,
then the divisible terms reduce to the smaller index.  That all-index argument
is the actual source dependency—not a finite numerical pattern.

## Local finite primitive

```sh
python3 scripts/apery_supercongruence.py --a 2 --b 1 --p 5 --m 1 --r 1
```

computes both integer sums and `ord_p` of their difference exactly.  It is an
audit tool for a selected instance; it accepts only prime `p>3` and reports the
theorem's required valuation separately from the observed one.  Before using a
positive result to reduce a denominator, prove that the candidate's actual
coefficient family is exactly `C(n,A,B)` and separately link those congruences
to the desired global LCM/gcd estimate.
