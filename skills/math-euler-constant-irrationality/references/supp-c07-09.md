# Harmonic-zeta/log-sine approximation: scoped analytic interface

## Source/version check

Emre Alkan, *Approximation by special values of harmonic zeta function and log-sine integrals*, **Communications in Number Theory and Physics** 7(3) (2013), 515--550, DOI `10.4310/CNTP.2013.v7.n3.a5`.  The local source has this journal header and pagination, 36 physical PDF pages, and SHA-256 `8db6b969a795b46f4268e4d1c04efd151b67ba2fc9952382ca5f0f273a7192e4`.  The publisher record confirms the same volume, title, author, and pages.

## Exact usable statement

For a Lipschitz, non-polynomial `f:[0,2\pi]\to\mathbb R`, set
\[
 I_{f,2\pi}=\int_0^{2\pi} f(t)\log(2\sin(t/2))\,dt.
\]
Theorem 1 (physical p. 519) says that for each `n\ge3` there is an integer `r\le n`, tending to infinity with `n`, and a linear combination
\[
 L=\sum_{k=1}^{\lfloor r/2\rfloor}
 Q[\pi^s:1\le s\le r-2k+1]\,[\zeta_H(2k)-\zeta(2k+1)]
\]
whose displayed coefficients are nonzero and depend on `f,n` but not on the special values, with
\[
 |I_{f,2\pi}-L|\ll_f n^{-1}.
\]
For smooth `f`, the stated error is `O_{f,q}(n^{-q})` for every fixed `q\ge1`.  Theorem 2 gives the analogous squared-log-sine formula for
\[
 J_{f,2\pi}=\int_0^{2\pi}f(t)\log^2(2\sin(t/2))\,dt,
\]
but includes the extra term `\pi^3P_r(\pi)` and odd harmonic-zeta values.

The Fourier input used for the first family is
\[
 \sum_{n\ge1}(H_n/n-1/n^2)\sin(nt)
 =\tfrac12(t-\pi)\log(2\sin(t/2)),\qquad 0<t<2\pi,
\]
with uniform convergence only on compact subintervals `[\delta,2\pi-\delta]`; the proof first integrates there and then controls endpoint limits (physical pp. 523--524).

## Boundary

This is an analytic representation/approximation interface.  Although Theorem 1 also specializes to an arbitrary real target `\alpha`, its coefficients may depend on `\alpha` and `n` and lie in expressions involving `\pi`; the theorem does **not** give rational or integer coefficients, an integral clearing scheme, or a nonzero lower bound.  It therefore cannot alone prove irrationality or transcendence of Euler's constant or any other target.
