# Scoped reference. Shifted Legendre kernels for finite Beukers-style checks

## Source and version

F. M. S. Lima, *Lecture notes on Legendre polynomials: their origin and main
properties*, arXiv:2210.10942v2, 3 March 2025, local SHA-256
`76cf0ad2b9e000cb43436f09aa6499cea8dd740c68f54e7b4a379d32daa7238e`.
The local PDF has 18 physical pages.  A formal journal version was not identified
in the version check on 2026-11-26; this is consequently a scoped preprint
reference, not a new proof of an irrationality statement.

## Exact imported identities and locus

For an integer \(n\geq0\), set \(\widetilde P_n(x)=P_n(1-2x)\).  Physical
pages 11--13 give

\[
 \widetilde P_n(x)=\sum_{m=0}^n(-1)^m\binom nm\binom{n+m}m x^m
 =\frac1{n!}\frac{d^n}{dx^n}\left[x^n(1-x)^n\right],
\]
and
\[
 \int_0^1x^d\widetilde P_n(x)\,dx=0\quad(0\leq d<n),\qquad
 \int_0^1x^n\widetilde P_n(x)\,dx
 =\frac{(-1)^n(n!)^2}{(2n+1)!}.
\]
For a function \(f\in C^n[0,1]\), the same locus gives the integration-by-parts
identity
\[
 \int_0^1\widetilde P_n(x)f(x)\,dx
 =\frac{(-1)^n}{n!}\int_0^1x^n(1-x)^nf^{(n)}(x)\,dx.
\]

The source derives the explicit expression by substituting \(1-2x\) into the
ordinary Legendre formula (p. 11), derives Rodrigues by the same substitution
(pp. 11--12), and obtains the stated diagonal moment from orthogonality
(p. 13).  That short used chain was spot-checked.  The included program performs
only finite, exact polynomial integrations; it does not establish the source's
functional-analytic assertions or any irrationality proof.

## Permitted use

Use this only to prepare exact finite kernels or to discharge the polynomial
moment side of a separately justified integer-linear-form construction.  A user
must separately prove all arithmetic integrality, non-vanishing, error bounds,
and any all-\(n\) conclusion.  In particular, these identities do not by
themselves construct a rational approximation to a specified constant.

Run:

```sh
python3 scripts/supp_c07_08_shifted_legendre.py '{"n":4}'
python3 scripts/supp_c07_08_shifted_legendre.py --self-test
```
