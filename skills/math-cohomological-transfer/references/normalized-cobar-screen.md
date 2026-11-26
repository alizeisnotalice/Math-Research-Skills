# Normalized cobar weight/sparsity deductions

## Provenance

OpenAI, *A finite Smith–Toda complex V(4) at the prime 1009*, pinned `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`, PDF SHA-256 `a9cf0165a9ea294995b42fac2290fa90a519101e446be81331f7c31726c6d635`, physical pp. 7–8, Lemmas 2.3–2.8 and Corollary 2.7.  The installed result below is independently derived from its stated grading assumptions; the source's realization, filtered May calculation, and Adams–Novikov convergence uses are not imported.

## Independent proof

Let `M` have nonnegative integer weights, and suppose every element of the reduced cooperation object `bar Gamma` which occurs as a bar factor has weight at least one.  A homogeneous tensor in

\[
M\otimes\bar\Gamma^{\otimes s}
\]

has weight at least `s`; weights add over tensor factors.  Thus its weight-`w` component is zero for `w<s`.  This proves weight vanishing without any topology.

In the displayed Adams–Novikov indexing, `d_r` sends `(s,t)` to `(s+r,t+r-1)`.  If source and target internal degrees lie in `q Z`, then `q` divides `r-1`.  Since a positive differential has `r>=2`, write `r=qk+1` with `k>=1`.  Page-to-page passage preserves a `q Z` support condition because each page is a subquotient of the preceding page.  This is only a support obstruction: it says nothing about whether an allowed differential is nonzero.

For the comparison, inspect any of the three cochain degrees `d=s-1,s,s+1`.  A tensor with a nonconstant coefficient needs weight at least

\[
u_m+(s-1)>w,
\]

because it has at least `s-1` reduced factors and `w-u_m<s-1`.  It therefore cannot occur.  A tensor using an excluded coordinate likewise cannot occur when that coordinate alone has weight `>w`.  Consequently only scalar coefficients and the retained additive coordinates occur in all three degrees.  The asserted common additive coproduct formula identifies the three cochain groups and commutes with the two differentials.  Equality of the middle kernels and incoming images gives the cohomology isomorphism.  If `w<u_m`, the coefficient exclusion does not depend on the cochain length, so the same argument applies in every degree.

## Exact arithmetic example and boundary

Take `s=5`, `w=7`, `u_m=8`, and suppose each reduced bar has weight at least one while every excluded coordinate has weight at least `13`.  Then

\[
7<8+1,\qquad 7-8=-1<4=s-1.
\]

The comparison screen passes once the common scalar/retained-coordinate and additive-coproduct hypotheses have been separately proved.  If the internal support is in `3Z`, the length screen rejects `r=2` and permits only lengths congruent to `1 mod 3`, e.g. `4,7,10`.

At `s=5,w=12,u_m=8`, the inequality is instead `12-8=4`, not `<4`; a positive coefficient together with four minimum-weight bars is no longer excluded.  The three-degree conclusion must then be withheld, even if some individual finite cochains happen to agree.
