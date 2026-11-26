# Exact finite projective-induction transfer

Source locus: *Arithmeticity of twisted finite correspondences for lattices over
local fields*, Lemma 2.1 and Corollary 2.3, PDF pp. 8--9, OpenAI pinned
commit `3344da59991ed94f9ba711217b29c1d760badfa6`.

## Contract

Let \(D=\Gamma\times\Lambda\) be finite for this certificate, with normalized
multiplier \(\alpha((g,h),(g',h'))=\mu(g,g')\omega(h,h')\).  Let
\(C=\{(a,\delta(a)):a\in A\}\), where \(\delta:A\to B\) is an isomorphism.
Choose one representative \(r_x\) in each left coset \(x\in D/C\).  A supplied
one-dimensional projective phase \(\theta\) must satisfy
\[
 \theta(a)+\theta(b)-\theta(ab)=\alpha((a,\delta a),(b,\delta b))\pmod1.
\]
This is the scalar version of a projective graph representation.  Matrix-valued
representations are outside this checker, but obey the same group calculation.

## Derivation

Define \(c(s,x)=r_{sx}^{-1}sr_x\in C\).  Since both `r_{sx}` and `sr_x`
represent the same left coset, the membership is immediate.  Inserting the
unique representatives twice gives
\[
c(s,tx)c(t,x)=r_{stx}^{-1}sr_{tx}r_{tx}^{-1}tr_x=c(st,x).
\]
Set the scalar transport exponent
\[
 p(s,x)=\alpha(s,r_x)+\alpha(r_{sx},c(s,x))+\theta(c(s,x)).
\]
The normalized 2-cocycle identity, the displayed correction identity, and the
projective identity for \(\theta\) cancel term-by-term to give
\[
 p(s,tx)+p(t,x)-p(st,x)=\alpha(s,t)\pmod1.
\]
Thus the corresponding maps obey \(U_sU_t=\alpha(s,t)U_{st}\).  If
\(r'_x=r_xk_x\), \(k_x\in C\), then the fibre map with phase
\(-\alpha(r_x,k_x)+\theta(k_x)\) intertwines the two transports by the same
cocycle calculation.  These are finite algebraic statements, independently of
the source's later local-field argument.

For any finite-dimensional fibre of dimension \(n\), graph freeness makes the
two orbit counts \([\Lambda:B]\) and \([\Gamma:A]\).  Hence the formal module
dimensions are \(n[\Lambda:B]\) and \(n[\Gamma:A]\), provided the external
normal regular-module realization is available.  The checker reports these
finite counts only; it does not establish that external realization.

## Exact model

`examples/c2_graph.json` uses two copies of \(C_2\), identity graph, a
nontrivial rational multiplier \(\mu(1,1)=1/2\), scalar graph phase
\(\theta(1)=1/4\), and two coset systems.  It proves the identities over
\(\mathbb Q/\mathbb Z\), returning dimensions 3 and 3.  The duplicate-representative
input is rejected before any transport claim.
