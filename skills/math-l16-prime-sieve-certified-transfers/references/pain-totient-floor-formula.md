# Coprime floor-sum identity for the Euler totient

## Source and adopted proof step

Jean-Christophe Pain, *Explicit formulas for Euler's totient function and
the number of divisors*, arXiv:2505.08434v1 (13 May 2025), local PDF pp. 1--9,
SHA-256 `4325bdd4fde139c114c8af0e6829852f1c6442eaeb006243d3a735e4fd2311b9`.
This is a preprint; no published version is asserted here.

The adopted component is local p. 4, equations (2)--(3).  The source first
derives

\[
\gcd(k,n)=2\sum_{j=1}^{n-1}\left\lfloor\frac{jk}{n}\right\rfloor+k+n-kn,
\]

from a lattice-point/floor-sum identity, then sums over reduced residues and
uses \(\sum_{(k,n)=1}k=n\phi(n)/2\) for \(n>1\).  Solving the displayed
equation gives, for \(n\ge3\),

\[
\phi(n)=\frac{4}{(n-1)(n-2)}
 \sum_{\substack{1\le k\le n\\(k,n)=1}}
 \sum_{j=1}^{n-1}\left\lfloor\frac{jk}{n}\right\rfloor.
\]

The fraction layout in text extraction of source equation (3) is ambiguous;
the denominator above is fixed by the actual p. 4 derivation, not by OCR.

## Exact interface and boundary

The script computes the double sum using integer arithmetic, checks exact
divisibility by \((n-1)(n-2)\), then independently counts reduced residues.
It rejects \(n<3\), where this rearranged formula has a zero denominator.
This is a finite identity checker, not a factoring algorithm or a complexity
claim.  Its adopted preprint dependency is precisely the p. 4 gcd/floor
identity and the standard reduced-residue sum; no later Menon/Pillai or
divisor-count formula is used.
