# Bradley-normalized multiple q-zeta stuffles

**Source.** David M. Bradley, *Multiple q-zeta values*, arXiv:math/0402093v1
(2004; manuscript dated 2018), physical pages 2--5, raw PDF SHA-256
`39b3f44aee161ed2c85e4ef22f5613847cafb981ada905a61d7dddb69ed18b49`.

**Status and scope.** Scoped reference. This preprint's adopted proof was
read on physical pages 3--5.  It begins by splitting two nested sums according
to the order/equality of their leading indices, then uses the q-integer
identity on page 4.  It applies only to the source normalization and its
convergence conditions: \(0<q<1\), a first index greater than \(1\), and
the remaining indices at least \(1\).  It is not a statement about an
alternative q-zeta normalization, finite truncated sums, classical MZV
independence, or Euler's constant.

For an admissible index \(s=(s_1,\ldots,s_m)\), the source defines
\[
 \zeta_q[s]=\sum_{k_1>\cdots>k_m>0}
 \prod_{j=1}^m\frac{q^{(s_j-1)k_j}}{[k_j]_q^{s_j}},
 \qquad [k]_q=\frac{1-q^k}{1-q}.
\]
When two leading summation indices agree, the source uses
\[
 \frac{q^{(a-1)k+(b-1)k}}{[k]_q^{a+b}}
 =(1-q)\frac{q^{(a+b-2)k}}{[k]_q^{a+b-1}}
 +\frac{q^{(a+b-1)k}}{[k]_q^{a+b}}.
\]
Thus each equal-index merge has two formal outputs,
\[
 (a,b)\text{-merge}\quad\longmapsto\quad (a+b) +(1-q)(a+b-1),
\]
while unequal leading indices retain their order.  Recursing this rule gives
equation (2.2), the q-stuffle product.  For depth one this says exactly
\[
 \zeta_q[a]\zeta_q[b]=\zeta_q[a,b]+\zeta_q[b,a]+\zeta_q[a+b]
 +(1-q)\zeta_q[a+b-1].
\]

The accompanying helper expands the rule as a polynomial in a formal
`r=1-q`.  It checks formal combinatorics only: a printed expansion becomes a
q-zeta identity only under the displayed source series definition and its
convergence hypotheses.
