# Finite overflow order implies convex-divergence order

Source context: T.-H. H. Chan, *Universal Closest Refinement on Measurable
Bipartite Relations*, arXiv:2604.10274v1 in the checked local PDF, Theorem
6.3 and its proof (physical pp. 31--33).  The public arXiv record now lists a
v2, which was not used for this local-v1 component.

For a finite base measure with positive rational weights `w_i`, compare two
nonnegative densities `r*` and `r` of equal total mass.  Define

`Over_r(t) = sum_i w_i max(r_i-t,0)`.

If `Over_r*(t) <= Over_r(t)` at every breakpoint in the union of the density
values (and at zero), the piecewise-linear functions give the inequality for
all `t>=0`.  Consequently any finite piecewise-linear convex objective written
as an affine function plus a nonnegative sum of hinges `(u-t)_+` has no larger
weighted value at `r*` than at `r`; equal mass cancels the affine part.

The checker uses exact rational arithmetic for this finite statement.  It is
not a verifier for the source's measurable truncation/augmentation lemmas,
singular parts, Assumption 2.3, or disintegration construction.  Those are
caller-supplied premises when invoking the source's full measurable theorem.
