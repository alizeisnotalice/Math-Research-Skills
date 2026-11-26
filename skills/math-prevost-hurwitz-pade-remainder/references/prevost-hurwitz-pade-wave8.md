# Prévost, *Expansion of Euler's Constant in Terms of Zeta Numbers*

- Status: 16-page author manuscript; the exact statement below is located in this single-author manuscript. The related coauthored Elsner–Prévost journal article is recorded separately.
- Verified SHA-256: `b83d327d542f20257ff21441626c5689912d7eff9b77a07e86087d3488c95148`.
- Adopted locus: physical pp. 5--8, Theorem 2, equations (2.1)--(2.6), and its proof.

## Adopted finite interface

Theorem 2 gives the displayed \(\gamma\)--Hurwitz-zeta identity and signed
remainder in the skill for integers \(m,n\ge0\) with \(m+n>0\), and real
\(s>-1\).  Its Padé coefficients are the terminating Pochhammer formulas
on physical pp. 5--6.  On pp. 7--8 the source substitutes the Padé residual
into an integral and obtains
\[
 \varepsilon_{n,m}^{(s)}=(-1)^{n+1}\int_0^1(1-x)^m x^n
 \zeta(m+n+1,s+2-x)\,dx.
\]
For real \(s>-1\), the integrand is positive after the displayed sign is
removed; its beta-integral estimate gives (R).

## Checked proof chain and limits

1. The source defines \(P_n,Q_m\) by terminating hypergeometric sums
   (pp. 5--6) and uses the Padé contact of \(e^{-t}\).
2. On pp. 6--7, elementary Laplace integrals evaluate the polynomial pieces
   as the explicit \(\log(s+1)\), rational, and Hurwitz-zeta terms.
3. On pp. 7--8, the source's integral Padé residual cancels \(Q_m\), leaving
   the signed positive Hurwitz-zeta integral and its beta bound.

This interface leaves every \(\log\) and Hurwitz-zeta term visible.  It does
not verify the later integer scaling/lcm asymptotic, eliminate the auxiliary
constants, or convert this multi-constant identity into an irrationality
claim about \(\gamma\).

[Institutional copy of the inspected manuscript](https://www-lmpa.univ-littoral.fr/publications/articles/lmpa388.pdf) · [Elsner–Prévost, JMAA 398(2), 508–526 (2013)](https://doi.org/10.1016/j.jmaa.2012.08.065)
