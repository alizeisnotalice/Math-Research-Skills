# Exact degree-10 cross-endpoint polynomial sublemma

Supporting primary source: Leonard van Hemert, public [`certified-riemann-xi-positivity` certificate script](https://github.com/LeonardSEO/certified-riemann-xi-positivity/blob/6d5f6ce7ad1031cee8740e47b044dda139dd497c/code/theta_moment_certificate.py), commit `6d5f6ce7ad1031cee8740e47b044dda139dd497c`, retrieved 2026-11-26; script SHA-256 `3024c03ee243c2cc5b63e06362e7065b3b30513296e4e80242883aa930305204`.

The pinned source was reviewed and replayed without optimisation under Python 3.12.13, `python-flint==0.9.0`, FLINT 3.6.0, 80 decimal digits and Taylor-series cap 18.  Its captured output SHA-256 is `6a6805eb326cbbde70c030eca4a0078206525e04e73432abe431df2609bf822b` and ends `ALL CERTIFICATE ASSERTIONS PASSED`.  The replay establishes the source program's stated endpoint \(\xi\)-Taylor ball evaluations, all five interval-versus-rational moment comparisons, and its sharp degree-10 cross-endpoint root bracket \(7.0362433<R_{10}<7.0362434\).

Conditional on the five rational comparisons printed by that script, define

\[
P_*(x)=1-\frac{837}{20000}x^2+\frac{199}{240000}x^4
-\frac{403}{36000000}x^6+\frac{429}{4032000000}x^8
-\frac{1497}{1814400000000}x^{10}.
\]

The finite sublemma is exact: write \(q(t)=P_*(\sqrt t)\).  The degree-four Bernstein coefficients of \(q'\) on \(0\leq t\leq51\) are all negative.  After \(t=51+r\), every power-basis coefficient of \(q'(51+r)\) is negative.  Hence \(q\) is strictly decreasing for \(t\geq0\).  Exact rational evaluation further gives \(P_*(7)>0\) and opposite signs at

\[
\frac{70165148}{10^7},\qquad \frac{70165149}{10^7}.
\]

Thus it has one positive root in that displayed bracket.  `check_cross_endpoint_polynomial.py` independently replays only this rational-algebra sublemma.

## Boundary

The small exact script shipped in this skill does **not** itself prove the five moment-ratio inequalities, evaluate \(\Xi\), establish endpoint moment monotonicity, or prove any zero-free region.  Those claims are supported only to the scope of the separately replayed pinned Arb program.  Neither program establishes RH or a general zero detector.
