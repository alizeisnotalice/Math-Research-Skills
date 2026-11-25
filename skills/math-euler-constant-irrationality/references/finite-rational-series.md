# Finite rational series: Vacca/Glaisher and Gregory-polynomial boundary

## Scope and status

This note records two superficially similar sources, but only one gives a
classical finite rational approximation to Euler's constant.  It is a
**source-audited tool note**, not an irrationality proof.

| local id | verified version and citation | mathematical role |
| --- | --- | --- |
| EXT-0019 | Jonathan Sondow, *New Vacca-Type Rational Series for Euler's Constant and Its "Alternating" Analog* \(\ln(4/\pi)\), arXiv:math/0508042v1 (2005), local PDF pp. 1--6; SHA-256 `1ba9c7fa19cc537329d52f52a10b80ba703df50079af41f09f0343812a54c3ab`.  The [Springer version of record](https://link.springer.com/book/10.1007/978-0-387-68361-4?page=2) is the chapter “New Vacca-Type Rational Series for Euler’s Constant \(\gamma\) and Its ‘Alternating’ Analog \(\ln(4/\pi)\),” in *Additive Number Theory*, Springer New York, 2010, pp. 331--340.  The local source is the six-page **v1 preprint**, not the publisher pagination. | usable rational partial sums and a certified elementary tail bound |
| P27 | Toshiki Matsusaka, Taichi Miyazaki, Shunta Yara, *On finite analogues of Dobiński's formula and of Euler's constant via Gregory polynomials*, arXiv:2604.01578v1, 2 Apr. 2026, local PDF pp. 1--14; SHA-256 `b8766f9be74d0a25c80b04e382449902c83a2c7f60641d746cb4974fd97fc6a4`.  The [authors’ Kyushu University affiliations and v1 record](https://arxiv.org/html/2604.01578) identify this as an arXiv preprint; no journal version is asserted here. | exact coefficient recurrence, but for Dobiński/Bessel values and finite-adelic analogues, **not** a classical rational approximation to \(\gamma\) |

The file names and hashes were checked against the local literature indexes
`07_Irrationality_Transcendence_Compendium/01_文献索引.csv` (EXT-0019) and
`04_Attachment_References/01_附件文献索引.csv` (P27).  Page references below
refer to those pinned local PDFs.

## EXT-0019: a finite, rational Vacca/Glaisher enclosure

For \(n\geq1\), let \(N_1(n)\) and \(N_0(n)\) be respectively the numbers of
ones and zeros in the usual binary expansion (with no leading zero).  Put

\[
d_+(n)=N_1(n)+N_0(n),\qquad d_-(n)=N_1(n)-N_0(n).
\]

Sondow’s Theorem 1 and its paired form (local pp. 1--2, equation (5) and
Corollary 1) give the infinite identities

\[
 \gamma=\sum_{n\geq1}\frac{d_+(n)}{2n(2n+1)},\qquad
 \log\frac4\pi=\sum_{n\geq1}\frac{d_-(n)}{2n(2n+1)}. \tag{V}
\]

For a finite computation use, for \(K\geq1\),

\[
 S_K^{\pm}=\sum_{n=1}^{2^K-1}\frac{d_\pm(n)}{2n(2n+1)}\in\mathbb Q. \tag{F}
\]

The digit recurrences are exact and avoid any string manipulation in a
replay program:

\[
\begin{aligned}
d_+(2n)&=d_+(n)+1,& d_+(2n+1)&=d_+(n)+1,\\
d_-(2n)&=d_-(n)-1,& d_-(2n+1)&=d_-(n)+1,
\end{aligned}\qquad(n\geq1), \tag{R}
\]
with \(d_+(1)=d_-(1)=1\).  These conditions matter: the binary expansion has
no leading zeros, and the recurrences are only stated for \(n\geq1\).

Here is a fully rational tail certificate obtained directly from (V), rather
than from decimal numerics:

\[
 0<\gamma-S_K^+<\frac{K+2}{2^{K+1}},\qquad
 \left|\log\frac4\pi-S_K^-\right|<\frac{K+2}{2^{K+1}}. \tag{T}
\]

Indeed, on \(2^j\leq n<2^{j+1}\), \(|d_\pm(n)|\leq d_+(n)=j+1\), while
\(2n(2n+1)>4n^2\).  Thus the absolute tail after \(2^K-1\) is bounded by

\[
 \sum_{j\geq K}\frac{2^j(j+1)}{4(2^j)^2}
 =\frac14\sum_{j\geq K}\frac{j+1}{2^j}
 =\frac{K+2}{2^{K+1}}.
\]

This certificate is deliberately modest, but has the right status: (F) is an
exact rational number and (T) is a proved finite remainder bound.  It is a
safe numerical-probing route and a test oracle for series implementations.

### Replayed checks

An exact Python `Fraction` replay of (F) and (R), run 2026-11-25, gave

| \(K\) | \(S_K^+\) | \(S_K^-\) | rigorous bound in (T) |
| --- | --- | --- | --- |
| 3 | \(50059/120120\) | \(82949/360360\) | \(5/16\) |
| 5 | \(5415006898610558271900391/10370762141252826907994400\) | \(141343252350505977672337631/591133442051411133755680800\) | \(7/64\) |

The same replay checked all four relations in (R) for \(1\leq n\leq64\).
MATLAB R2026b with Symbolic Math Toolbox was used only for the following
non-rigorous decimal sanity check: for \(K=5\), the observed errors were
\(0.05507401081125737407689918\) for \(\gamma-S_K^+\), and
\(0.002458983522295130688901093\) for
\(\log(4/\pi)-S_K^-\).  Those decimals are evidence of an implementation
check; (T), not the decimals, is the certificate.

### Irrationality boundary

Do not promote (V) to an irrationality criterion.  For example,
\(L_K=\operatorname{lcm}_{1\leq n<2^K}\{2n(2n+1)\}\) makes
\(L_K S_K^+\) integral, but (T) gives no compensating control showing
\(L_K(\gamma-S_K^+)\to0\), let alone a nonzero integer of absolute value
less than one.  Infinite rational series identities, even with a rational
finite tail bound, are compatible with rational limits.  A usable
irrationality proof must additionally supply the same-denominator integer
linear form, a nonvanishing proof, and smallness after the chosen denominator
scaling.

## P27: Gregory data, correctly separated from the classical target

P27 is valuable as a boundary/reference check, not as a source of the
finite rational forms above.  On local p. 3 it defines the Gregory
coefficients by

\[
 \frac{t}{\log(1+t)}=\sum_{n\geq0}G_n t^n,
 \qquad
 \gamma=\sum_{n\geq1}\frac{(-1)^{n-1}G_n}{n}.
\]

But its main finite objects live in the quotient ring
\[
 \mathcal A=\left(\prod_{p\ \mathrm{prime}}\mathbb Z/p\mathbb Z\right)
 \bigg/\left(\bigoplus_{p\ \mathrm{prime}}\mathbb Z/p\mathbb Z\right)
\]
(local p. 1), and therefore are not rational numbers tending to the real
Euler constant.

The exact finite recurrence that can safely be reused is P27 Theorem 1.2
(local pp. 2--3): for \(r\geq1\), define
\[
D_r(n)=\sum_{k=0}^{\infty}\frac{k^n}{(k!)^r}.
\]
Then
\[
D_r(n)=\sum_{j=0}^{r-1}b_{r,j}(n)D_r(j),
\]
where \(b_{r,j}(n)=\delta_{j,n}\) for \(0\leq n\leq r-1\), and
\[
b_{r,j}(n+r)=\sum_{k=0}^{n}\binom nk b_{r,j}(k)\qquad(n\geq0). \tag{D}
\]
Thus (D) is an integer, finite recurrence for coefficient generation.  It
concerns Dobiński/Bessel-type values; it provides neither a rational
approximation \(p_K/q_K\) to \(\gamma\), nor a classical real remainder
bound.  The \(\mathcal A\)-formula in P27 Theorem 1.3 (local p. 3) likewise
does not change that conclusion.

As a replay, exact integer arithmetic at \(r=2\) produces
\[
 (b_{2,0}(n),b_{2,1}(n))_{n=0}^{9}
 = (1,0),(0,1),(1,0),(1,1),(2,2),(5,4),(13,10),(36,29),(109,90),(359,295).
\]
MATLAB R2026b Symbolic Math Toolbox evaluated the defining Dobiński series
to 70 digits and numerically checked the induced recurrence
\(D_2(n+2)=\sum_{k=0}^n\binom nkD_2(k)\) for \(n=0,1,2,3\); the displayed
residuals were respectively \(0\), \(1.33\!\times\!10^{-74}\),
\(1.33\!\times\!10^{-74}\), and \(4.38\!\times\!10^{-73}\).  This is only
a numerical reproduction check, while the exact coefficient list above is
integer arithmetic.
