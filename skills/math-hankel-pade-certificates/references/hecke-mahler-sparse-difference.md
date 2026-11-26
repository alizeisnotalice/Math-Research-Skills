# Hecke--Mahler sparse finite-difference audit

For a sequence
\[
u_m=f(\lfloor m\theta+\alpha\rfloor),
\]
with irrational rotation slope, a different route from Hankel--Pade tests is to apply a high-order translated finite difference
\[
w_m=\sum_{j=0}^{s}(-1)^j\binom{s}{j}u_{m+jr},\qquad s=\deg f+1.
\]

Luca--Ouaknine--Worrell use suitable convergent denominators `r` to make the nonzero support of this sequence sparse.  Their global condition also requires an unbounded sequence of such shifts, infinite support with gaps comparable to the shifts, polynomial variation on that support, and a polynomial bound for `u`.  With the p-adic Subspace Theorem, those facts give transcendence of the associated base-`beta` series for algebraic `|beta|>1`.

`scripts/hecke_mahler_sparse_difference.py` is a finite exact diagnostic for slopes of the form `(a+b*sqrt(d))/c` with rational `alpha`.  It computes floors without floating point, forms the displayed difference over a requested finite prefix, and reports the nonzero positions and the least observed gap.  It does **not** prove irrationality of the slope, equidistribution, the all-shift Condition (*), the Subspace-Theorem step, or transcendence of a value.

## Source and boundary

Florian Luca, Joel Ouaknine, and James Worrell, *Transcendence of Hecke-Mahler Series*, arXiv:2412.07908v2 (2024), PDF pp. 1--8, SHA-256 `a1eb6556e9cbd03d2566205e908de3c8eaadac254cb79c1d628b7c98dd32944b`.

The preprint chain used here was spot-checked.  Definition 4 and Theorem 5 on pp. 2--4 turn Condition (*) into transcendence using the quoted p-adic Subspace Theorem and the lacunary-polynomial root proposition.  Theorem 7 and Claims 8--9 on pp. 4--7 verify that condition for the floor-polynomial sequence through continued-fraction denominators, best approximation, equidistribution, and exact finite-difference cancellation.  Theorem 10 on p. 7 combines them.  The local checker covers only the last, finite cancellation calculation for supplied data.

This is unrelated to the Euler constant unless a separately established representation supplies exactly this floor-rotation sequence and all global hypotheses.
