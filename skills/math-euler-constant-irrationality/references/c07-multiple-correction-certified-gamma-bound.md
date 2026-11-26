# Twice-corrected harmonic approximation with an all-`n` gamma enclosure

## Checked source, version, and locus

X. Cao, H. Xu, and X. You, *Multiple-correction and Faster Approximation*,
arXiv:1409.0968v1 (3 September 2014), local SHA-256
`9e72f9ca7fd09115e564a7815893a4d0f07872fb09b83296e29200b91c6b62b9`.
The source is an arXiv preprint (no formal publication was located in this
check).  The adopted statement is equations (3.13)--(3.17) on physical pp.
8--9 and Theorem 1 with its proof on physical pp. 9--10.

## Procedure

For an integer \(n\geq1\), form
\[
 H_n=\sum_{k=1}^n\frac1k,\qquad
 \eta_0(n)=\frac{6n-1}{12n^2},
\]
and
\[
 \eta(n)=\frac{1}{120n^4+\frac{10}{21}n^2-\frac{241}{882}},\qquad
 \mu(n)=H_n-\log n-\eta_0(n)-\eta(n).
\]
Theorem 1 proves, for every positive integer \(n\),
\[
 \frac{13775}{3056130\,(n+3/4)^{10}}
 < \gamma-\mu(n) <
 \frac{13775}{3056130\,(n-1/4)^{10}}. \tag{MC}
\]
Thus an independently certified enclosure for \(\log n\), combined with
the exact rational quantities above, yields a finite certified enclosure for
\(\gamma\).  The error is positive, so \(\mu(n)<\gamma\).

## What was proof-checked

The preprint's required proof step was checked at the adopted locus: it writes
the forward difference of \(\mu\) as a logarithmic expression, defines a
rationally differentiated remainder \(\omega\), proves two signed derivative
comparisons against shifted \(x^{-12}\), and sums/integrates those comparisons
to obtain both sides of (MC).  The numerical asymptotic statement alone is
not used here.

## Boundary

This is an approximation/enclosure route only.  The bound does not control a
common denominator of rational approximants after replacing \(\log n\), and
therefore does not prove irrationality of \(\gamma\).  Do not replace the
source's all-`n` derivative proof by a fitted asymptotic expansion.

`scripts/c07_multiple_correction_gamma_bound.py` evaluates the rational
correction and the two exact error offsets.  Its output intentionally leaves
`log(n)` symbolic; attach a directed logarithm enclosure before reporting
numeric digits.
