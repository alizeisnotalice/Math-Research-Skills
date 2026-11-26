# Zero-sum \(\ell^1\) extremizers for regular-simplex hyperplane projections

For a real vector \(a\in\mathbb R^d\) with \(\sum_i a_i=0\) and \(\sum_i a_i^2=1\), choose a sign split with \(k\) positive coordinates and \(d-k\) negative coordinates. Cauchy--Schwarz on each sign class gives
\[
 \sum_i |a_i|\le 2\sqrt{\frac{k(d-k)}d}.
\]
The equality vector has constant magnitude within each sign class. Its positive-coordinate square is \((d-k)/(dk)\), its negative-coordinate square is \(k/(d(d-k))\), and its squared \(\ell^1\) norm is \(4k(d-k)/d\). The global maximum is attained exactly by the balanced sign counts \(k\in\{\lfloor d/2\rfloor,\lceil d/2\rceil\}\), up to coordinate permutation and overall sign.

For the regular \((d-1)\)-simplex in the source normalization, the Cauchy--Minkowski calculation makes the hyperplane-projection volume a fixed dimension-dependent multiple of \(\sum_i|a_i|\). This file certifies only the finite-dimensional zero-sum optimization and equality data. It needs the simplex normalization and projection formula before it can be used as a volume calculation. It provides no deficit-to-distance stability bound.

Source checked in local arXiv:2601.18436v1, physical pp. 11--13, especially the simplex projection reduction on pp. 11--12 and Proposition 1.4 on p. 13.

Run `python3 scripts/simplex_zero_sum_extremizer.py 5 2` for the odd-dimensional equality orbit. The output uses rational squares because the coordinates themselves can contain square roots.
