# Paired functional at a compatible collapsed limit

**Source.** Beniamin Bogosel, *Isoperimetric Problems Related to Extremal
Diameter Graphs in 3D: Theoretical and Numerical Aspects*, arXiv:2608.26395v1
(2026), physical pages 7--11, raw PDF SHA-256
`e112ec7f105cf4cf7fcf6aa1008cbd7668460072730e6fd7e982bee8a397c618`.

**Status and scope.** Scoped reference. The source is a preprint.  The
adopted step is the finite-sum proof on physical page 11.  It is usable only
after the caller supplies the geometric facts that produce the exact limit
core and the compatible (and, for continuity, stable) pair lifts.  The
source's Proposition 2 uses the external extended GHS theorem to establish
its particular extremal core; that geometric theorem is not imported here.

Let \(E(X)\) be a finite collection of pairs.  Suppose each pair has two
sizes \(q_X(e)\in[0,Q]\), and define
\[
 J_F(X)=\sum_{(e,e')\in E(X)}F(q_X(e),q_X(e')).
\]
Assume \(F:[0,Q]^2\to[0,\infty)\) is continuous and symmetric.  Given
\(X_n\to X\), suppose injections from every pair of \(E(X)\) into
\(E(X_n)\) identify *compatible* lifts whose endpoints, hence sizes, converge.
Then the matched terms converge one at a time and all unmatched terms are
nonnegative.  Therefore
\[
 J_F(X)\leq\liminf_{n\to\infty}J_F(X_n).
\]

For the stronger conclusion, require *stable* lifting: every unmatched pair
has at least one size tending uniformly to zero.  If in addition
\[
 F(s,0)=F(0,s)=0\qquad(0\leq s\leq Q),
\]
uniform continuity on the compact square makes every unmatched summand tend
to zero.  Since the source setting has a fixed finite number of pairs,
\(J_F(X_n)\to J_F(X)\).

This axis-vanishing condition is material: a disappearing pair with sizes
\((1/n,1)\) has vanishing product cost but has sum cost tending to \(1\).
Likewise, compatibility alone permits several nondegenerate source pairs to
approach one limit pair; stability excludes this multiplicity.  Treat both
conditions as caller-provided certificates, not consequences of pointwise
vertex convergence.
