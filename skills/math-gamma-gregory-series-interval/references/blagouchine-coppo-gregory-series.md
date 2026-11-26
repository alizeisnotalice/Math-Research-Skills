# Gregory-series rational interval for Euler's constant

## Source and version

I. V. Blagouchine and M.-A. Coppo, *A note on some constants related to
the zeta-function and their relationship with the Gregory coefficients*,
The Ramanujan Journal **47**(2) (2018), 457--473,
DOI [10.1007/s11139-018-9991-0](https://doi.org/10.1007/s11139-018-9991-0).
The local source is arXiv:1703.08601v2 (15 Apr. 2017), PDF pp. 1--15,
SHA-256
`8b1a3e97d4bafc716d5df4061f8d216dece68789931f61b8183c2d54ef66e88b`.
Publication facts were checked against the authors' publication listing and
the DOI record; the local mathematical reading uses the pinned v2 PDF.

## Transferred finite interface

On local p. 3, equations (5)--(8) define the rational Gregory coefficients
by

\[
\frac{z}{\log(1+z)}=\sum_{n\geq0}G_nz^n,
\qquad
\gamma=\sum_{n\geq1}\frac{|G_n|}{n},
\qquad
G_n=\frac1{n!}\int_0^1x(x-1)\cdots(x-n+1)\,dx.
\]

## Strict enclosure

For \(N\ge1\) the script computes \(S_N=\sum_{n=1}^N |G_n|/n\) and the exact remaining coefficient mass
\[
 R_N=1-\sum_{n=1}^N |G_n|.
\]
The integral formula gives \(\operatorname{sgn} G_n=(-1)^{n-1}\) and \(G_n\ne0\) for \(n\ge1\). With \(z=-r\), \(0<r<1\), the generating function satisfies
\[
 1-\sum_{n\ge1}|G_n|r^n=\frac{-r}{\log(1-r)}.
\]
The right side tends to zero as \(r\uparrow1\). Monotone convergence therefore yields \(\sum_{n\ge1}|G_n|=1\). The positive series for \(\gamma\) then gives
\[
 0<\gamma-S_N<\frac{R_N}{N+1},
\]
where strictness at the upper end follows from the terms with \(n>N+1\). The output records exact rational endpoints and \(R_N\). Comparison with a target rational \(a/b\) is rigorous whenever the target lies outside the interval. The interval width and the increasing arithmetic denominator remain separate quantities in any irrationality argument.

~~~sh
python3 -B scripts/gregory_series_interval.py --terms 5
~~~
