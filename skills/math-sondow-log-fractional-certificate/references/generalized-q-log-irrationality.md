# Generalized q-logarithm: an irrationality route distinct from gamma

This reference adds a theorem-level route for a q-logarithm specialization.
It does **not** turn a finite q-logarithm enclosure into an Euler-constant
irrationality certificate.

## Source and version

Wadim Zudilin, *On the irrationality of generalized q-logarithm*,
arXiv:1601.02688v2, 24 January 2016, Theorem 1 (physical PDF pp. 3--4),
Padé remainder identity (pp. 5--6), and Hankel determinant proof (pp. 7--10).
The local source is `EXT-0336_On_the_irrationality_of_generalized_q_logarithm.pdf`,
SHA-256 `53947bb2fc82e853c12ccfdb293a526229f6fe2ac99d9c991d2170ae6e1266e3`.

The published version is *Research in Number Theory* **2** (2016), Article
15, DOI [10.1007/s40993-016-0042-x](https://doi.org/10.1007/s40993-016-0042-x).
The source consulted and its theorem/page locators are the local arXiv v2;
do not silently substitute journal pagination.

## The exact theorem interface

For an integer `p` with `|p|>1`, define

\[
 \ell_p(x,z)=x\sum_{n\geq1}\frac{z^n}{p^n-x}.
\]

Theorem 1 proves `ell_p(x,z)` irrational provided

\[
 x,z\in\mathbb Q\setminus\{0\},\quad x\notin\{p,p^2,p^3,\ldots\},
 \quad |z|<|p|.
\]

The last condition makes the series converge; the exclusion on `x` prevents
a zero denominator.  These are theorem hypotheses, not optional numerical
screening suggestions.  The proof uses a Padé remainder and a Hankel
determinant whose q-adic leading term supplies the needed nonvanishing;
do not replace that argument by a finite table of partial sums.

For the existing positive-integer q-logarithm interface, take `p=q>=2`,
`x=1`, and `z=-w`.  Then

\[
 \ln_q(1+w)=\sum_{n\geq1}\frac{(-1)^{n-1}w^n}{q^n-1}
            =-\ell_q(1,-w).
\]

Hence the theorem certifies irrationality of `ln_q(1+w)` for rational
`0<w<q`.  The endpoint `w=0` is excluded (and gives the rational value zero);
the installed alternating-tail code deliberately allows it for numerical
enclosure, so its acceptance is not a theorem-admission signal.

## Exact finite replay and boundary

```sh
python3 scripts/q_log_bounds.py q-log --q 2 --z 1/2 --terms 20
```

was run against the installed script.  It returned exact rational lower and
upper bounds for `ln_2(3/2)` using 20 terms.  That finite computation verifies
only the enclosure.  Its irrationality follows here from the cited Theorem 1
with `(p,x,z)=(2,1,-1/2)`, not from the enclosure.

No identity in this reference represents Euler's constant as one of these
values.  Any proposed gamma transfer must first provide such an identity and
then separately preserve the theorem's rational-parameter hypotheses.
