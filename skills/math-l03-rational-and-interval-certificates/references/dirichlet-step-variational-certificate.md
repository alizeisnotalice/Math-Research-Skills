# Rational step certificate for a compact variational functional

For `C >= 1`, define `F_C(t)=t` on `[0,1]` and `F_C(t)=C` on `(1,2]`.
For an even nonnegative step function `f` on `[-1,1]`, normalized by
`integral f=1`, the source uses

\[
 Q_{F_C}(f)=\int f^2+\iint f(x)f(y)F_C(|x-y|)\,dx\,dy,
 \qquad p(C)=2-\inf_fQ_{F_C}(f).
\]

If `f` has heights `f_i` on `n` equal cells, `h=2/n`, then the exact finite
evaluation is

\[
 Q_{F_C}(f)=h\sum_i f_i^2+\sum_{i,j}f_if_j\kappa_{i-j},
 \quad\kappa_m=G((m+1)h)-2G(mh)+G((m-1)h),
\]

where `G` is even, `G(x)=|x|^3/6` for `|x|<=1`, and
`G(x)=1/6+(|x|-1)/2+C(|x|-1)^2/2` for `1<|x|<=2`.

`scripts/check_dirichlet_step_variational.py` accepts rational `C` and
comma-separated rational heights, checks evenness/nonnegativity/normalization,
and returns the exact value of `Q` and the certified lower bound `p(C)>=2-Q`.
This evaluates a caller-supplied finite step function; it does not optimize
over functions, reproduce an unavailable ancillary candidate, or prove any
statement about zeros of individual Dirichlet L-functions.

## Source and audit boundary

Nic Johns, *Simple critical zeros in a weighted family of Dirichlet
L-functions, from polylogarithmic to polynomial height* (September 2026
author manuscript), physical pp. 2 and 43, equations (1.3), Lemma 7.1, and
Proposition 7.3.  The global family-zero lower bounds depend on the preceding
large-sieve, form-factor, and limiting arguments; they are not adopted by
this finite functional calculator.
