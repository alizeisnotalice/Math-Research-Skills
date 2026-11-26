# First correction for the nearest-neighbor lattice heat kernel

## Statement

Let
\[
 I(t)=\frac1{2\pi}\int_{-\pi}^{\pi}e^{-2t(1-\cos k)}\,dk \quad (t\ge1).
\]
There is an absolute constant C such that
\[
 \left|I(t)-(4\pi t)^{-1/2}\left(1+\frac1{16t}\right)\right|
 \le C t^{-5/2}. \tag{1}
\]
Consequently, for each fixed positive integer d,
\[
 I(t)^d=(4\pi t)^{-d/2}\left(1+\frac d{16t}+O_d(t^{-2})\right). \tag{2}
\]

## Independent proof

Set u=sqrt(t) k.  On |u| <= t^(1/10), Taylor's theorem (with a uniform sixth-derivative bound for cosine) gives
\[
 2t(1-\cos(u/\sqrt t))=u^2-\frac{u^4}{12t}+O(u^6/t^2).
\]
The exponent perturbation is uniformly small on this region, so the Taylor remainder for the exponential gives
\[
 e^{-2t(1-\cos(u/\sqrt t))}
 =e^{-u^2}\left(1+\frac{u^4}{12t}
 +O\!\left((u^6+u^8)/t^2\right)\right). \tag{3}
\]
All constants here are independent of t >= 1 after enlarging them for a compact initial interval.

There is c>0 with 2(1-cos k) >= c k^2 for |k| <= pi.  Thus the part with |u| > t^(1/10) is bounded by a Gaussian tail O(exp(-c t^(1/5))); the same is true when the Gaussian integrals in (3) are extended to the real line.  Integrating (3), using
\[
 \int_{\mathbb R}e^{-u^2}du=\sqrt\pi,
 \qquad \int_{\mathbb R}u^4e^{-u^2}du=\frac34\sqrt\pi,
\]
gives
\[
 I(t)=\frac1{2\pi\sqrt t}
 \left(\sqrt\pi+\frac{1}{12t}\frac34\sqrt\pi+O(t^{-2})\right),
\]
which is (1).  Formula (2) follows by the finite binomial expansion, because the relative remainder in (1) is O(t^-2).

## Checked scope and exclusion

This proof uses exactly one non-degenerate minimum of the nearest-neighbor symbol on the torus fundamental domain and coordinate factorization for (2).  It remains valid for a fixed dimension d, with a d-dependent constant.  It does not cover another lattice symbol, degenerating minima, dimensions varying with t, an interacting Gibbs state, or any identification of a magnetization correction.

## Source checked

OpenAI Math, *The first lattice correction to Bloch's law*, pinned repository commit `3344da59991ed94f9ba711217b29c1d760badfa6`, physical PDF p. 36, Section 9.4, "The explicit lattice correction".  Local source SHA-256: `4c19762cfd46fbb074ee35290bfd6200bc9827def6fa58c08f471dad7b2f5456`; reviewed PDF pages 33--36 (the calculation is on PDF p. 36).  The source uses the same small-frequency split and records the d=3 coefficient 3/16; the proof above supplies the reusable normalized statement.
