# Hurwitz-zeta fourth moment under a strict irrationality-exponent premise

Source checked: Winston Heap and Anurag Sahay, *The fourth moment of the Hurwitz zeta function*, Journal für die reine und angewandte Mathematik **818** (2025), 291--319, DOI: 10.1515/crelle-2024-0086. The local source is arXiv:2405.10888v1; the used statements are Theorem 1 and Corollary 2 on physical pp. 3--4.

## Certified caller contract

Supply a fixed real α together with an independent proof that
\[
 0<\alpha<1,\qquad \alpha\notin\mathbb Q,\qquad \mu(\alpha)<3.
\]
For sufficiently large $T$, the published theorem gives
\[
 \int_T^{2T}\left|\zeta(\tfrac12+it,\alpha)\right|^4\,dt
 \ll_\alpha T(\log T)^2.
\]
Its corollary gives, for every real $0\le k\le2$,
\[
 \int_T^{2T}\left|\zeta(\tfrac12+it,\alpha)\right|^{2k}\,dt
 \asymp_\alpha T(\log T)^k.
\]

## Audit boundary

The strict condition μ(α)<3 is a mathematical premise, not something a finite list of rational approximations can certify. The theorem is an upper bound (and the corollary an order comparison); it is not an asymptotic formula, does not cover every irrational α, and should not be combined with an unproved irrationality-exponent assertion.
