# Layer window for a transitive-symmetry integer program

Source: A. Shahverdi, M. Hojny, and M. E. Pfetsch, *Outer Approximations of
Core Points for Integer Programming*, arXiv:2005.08657, Lemma 3.9 (physical
p. 12).  The statement is retained as a source-scoped finite reduction.

If a transitive permutation group preserves an integer program with objective
`sum_i x_i`, first solve its global LP relaxation `R`, let
`ell = floor(sum_i x_i^*)`, and certify feasibility in each integer layer
`ell-n < j <= ell`.  Under the source's invariance and normalization
hypotheses, the highest feasible such layer is integer-optimal; if none is
feasible, the integer program is infeasible.

The reduction does not replace global LP optimality, transitivity, or exact
layer-feasibility certificates.  It is not a general symmetry-breaking rule.
