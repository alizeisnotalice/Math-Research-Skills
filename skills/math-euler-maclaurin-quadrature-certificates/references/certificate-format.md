# Certificate format and source scope

## Frozen source actually used

- David H. Bailey and Jonathan M. Borwein, *Effective Error Bounds in Euler-Maclaurin-Based Quadrature Schemes*, author manuscript dated 21 June 2005.
- Frozen local file: `/Volumes/共享/Math_Research_Literature/07_Irrationality_Transcendence_Compendium/PDF/EXT-0560_Effective-Error-Bounds-in-Euler-Maclaurin-Based-Quadrature-Schemes.pdf`.
- SHA-256: `5f4ce43913ee010e0b58192611d852e92077be566dffc5b22a5db27f97740bc3` (18 pages; hash verified 2026-11-26).
- Decisive locations: PDF p. 2, equations (2)--(5); p. 5, Theorem 1 and equations (7)--(9); pp. 6--7, Theorems 2--3, equations (10)--(11), and Corollary 1.

No journal version was established in this review. The source discusses estimators as well as bounds; the script implements only the explicitly stated endpoint-vanishing setting and a separately displayed absolute-value derivation below.

## Formula implemented

Let \(h=(b-a)/N\), let \(B_{2i}\) be the usual Bernoulli numbers, and define

\[
 Q_m=h\sum_{j=0}^{N}f(a+jh)-\frac h2(f(a)+f(b))
 -\sum_{i=1}^m\frac{h^{2i}B_{2i}}{(2i)!}
 \bigl(f^{(2i-1)}(b)-f^{(2i-1)}(a)\bigr).
\]

Equation (2) writes \(\int_a^b f=Q_m+E(h,m)\). Under Theorem 3's hypotheses (the Theorem 2 endpoint conditions also hold after replacing \(m\) by \(m+n\)), the source gives

\[
 E(h,m)=E_2(h,m)+R,qquad
 E_2=h(-1)^{m-1}\left(\frac h{2\pi}\right)^{2m}
 \sum_{j=0}^{N} f^{(2m)}(a+jh).
\]

The displayed remainder is

\[
 R=2(-1)^{n-1}\left(\frac h{2\pi}\right)^{P}
 \sum_{k=1}^{\infty}\left(k^{-2n}+(-1)^m k^{-P}\right)
 \int_a^b\cos\!\left(\frac{2k\pi(t-a)}h\right)f^{(P)}(t)\,dt,
 \qquad P=2m+2n.
\]

Taking absolute values in this source formula gives the conservative bound

\[
 |R|\le 2\left(\frac h{2\pi}\right)^{2m+2n}
 [\zeta(2n)+\zeta(2m+2n)]L,
 \quad L\ge\int_a^b|f^{(2m+2n)}(t)|dt.
\]

This inequality is a direct triangle-inequality consequence of Theorem 3, not a claim that the manuscript labels it as a separate theorem. The script obtains a rational valid `L` for a polynomial \(p(x)=\sum c_rx^r\) from

\[
 L\le(b-a)\sum_r |c_r|\max(|a|,|b|)^r.
\]

It converts the even zeta values using the Bernoulli-number identity implicit in the Fourier series on p. 5, then encloses the remaining powers of \(\pi^{-1}\) with supplied rational bounds. Thus the emitted interval is rigorous only conditional on the supplied `pi_lower < pi < pi_upper` being an independently certified enclosure.

## JSON input

All rational values are strings accepted by Python's `Fraction`, such as `"-7/12"` or `"3"`. Coefficients are low-to-high:

```json
{
  "coefficients": ["0", "0", "0", "0", "0", "1", "-5", "10", "-10", "5", "-1"],
  "a": "0",
  "b": "1",
  "subintervals": 2,
  "m": 1,
  "n": 1,
  "pi_lower": "333/106",
  "pi_upper": "355/113"
}
```

The example is \(x^5(1-x)^5\) on two subintervals, so its discrete \(E_2\) term is nonzero. The two rational bounds for \(\pi\) are supplied as assumptions, not proved by the program. Output `exact_error` is independently obtained from exact polynomial integration and is included to test this finite case; a future non-polynomial adapter must not pretend to have it.

## Rejection boundary

The script rejects an input whenever a required endpoint derivative is nonzero. It also rejects malformed rationals, booleans or nonintegral representations for the three integer fields, non-positive grid size, invalid m or n, non-increasing intervals, and non-positive/incorrectly ordered pi bounds. Passing structural validation does not establish a pi enclosure or prove a non-polynomial derivative bound.
