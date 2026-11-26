# Delta-relaxed monotonic outer approximation

Source: M. Rashwan, M. Althoff, and coauthors, *Refined Outer-Approximation
Algorithms for Monotonic Optimisation*, arXiv:2608.13694v1, Algorithm 2,
Lemma 2, and Theorem 2 (physical pp. 8--12).  This is a preprint source
statement.

## Certified interface

For a closed normal set `G`, a co-normal set `H`, an increasing objective,
and a bounded box `[a,b]`, Algorithm 2 uses the eroded normal set
`G_delta = {s : B_delta(s) subset G}`.  Its key exact equivalence is
`s in G_delta` iff `s + delta*1 in G`.  It requires exact projection onto
`G_delta` and exact pruning against `H`; numerical projection output is not a
certificate.

With those hypotheses, the stated depth is
`D = floor(delta^(-1) ||b-a||_1) + 1`.  The source's iteration bound is
`(n^D-1)/(n-1)` for `n>1`, and `D` for `n=1`.  The resulting guarantee is for
the delta-relaxed problem, not an exact optimizer of the un-eroded problem.
