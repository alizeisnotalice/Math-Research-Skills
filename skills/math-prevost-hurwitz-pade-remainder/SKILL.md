---
name: math-prevost-hurwitz-pade-remainder
description: Construct and audit Prévost's finite [n/m] exp(-t) Padé coefficients and its signed Euler-constant/Hurwitz-zeta remainder; preserve all auxiliary zeta and logarithm terms.
---

# Prévost--Hurwitz Padé remainder

Use this for the multi-constant identity from a finite \([n/m]\) Padé
approximation of \(e^{-t}\).  This is separate from the installed Prévost
Legendre/Beta integral: it produces a \(\gamma\) identity with explicit
Hurwitz-zeta and logarithm terms, rather than a single logarithmic fractional
part certificate.

For integers \(m,n\ge0\), \(m+n>0\), set
\[
 P_n(t)=\sum_{k=0}^n\frac{(-n)_k}{(-m-n)_k}\frac{(-t)^k}{k!},\qquad
 Q_m(t)=\sum_{k=0}^m\frac{(-m)_k}{(-m-n)_k}\frac{t^k}{k!}.
\]
The source proves that for real \(s>-1\),
\[
\begin{aligned}
\gamma={}&H_s-\log(s+1)
+\sum_{j=1}^m\frac{(-m)_j}{(-m-n)_j}\frac1{j(s+1)^j}\\
&-\sum_{j=2}^{\max(m,n)}
 \frac{(-m)_j-(-1)^j(-n)_j}{(-m-n)_j}\frac{\zeta(j,s+1)}j
+\varepsilon_{n,m}^{(s)},
\end{aligned}\tag{H}
\]
Here \(H_s=\int_0^1 (1-x^s)/(1-x)\,dx\) is the generalized harmonic
number. For \(s\) a nonnegative integer it equals the finite sum
\(\sum_{k=1}^{s}1/k\). The signed remainder satisfies
\[
0<(-1)^{n+1}\varepsilon_{n,m}^{(s)}
\le {\zeta(m+n+1,s+1)\over(m+n+1){m+n\choose n}}.\tag{R}
\]

For a supplied rational \(s>-1\), the checker verifies the Padé contact
through degree \(m+n\), emits the exact coefficients, and bounds
\(\zeta(r,s+1)\) by \((s+1)^{-r}+(s+1)^{1-r}/(r-1)\).
The checker leaves \(H_s\) symbolic for nonintegral \(s\). For \(s=0\) it reports a strict rational interval if every Hurwitz coefficient
vanishes. [Replay inputs](examples/replay.md) show both cases.

The signed remainder is a rigorous finite bracket only after every displayed
auxiliary \(H_s\), logarithm and Hurwitz-zeta value has its own rigorous enclosure or
algebraic reduction.  Do not discard those terms, infer an integer linear
form in \(\gamma\) alone, or claim irrationality.  The installed
Sondow/Legendre--Padé certificate remains the appropriate tool for its own
one-constant denominator-exclusion route.

Source and dependency boundaries: [reference note](references/prevost-hurwitz-pade-wave8.md).
Run [the exact replay](scripts/check_prevost_hurwitz_pade.py) for positive,
multi-constant, and invalid-domain cases.
