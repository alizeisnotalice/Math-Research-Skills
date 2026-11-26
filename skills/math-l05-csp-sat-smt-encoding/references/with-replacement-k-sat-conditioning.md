# With-replacement k-SAT conditioning

For fixed integers \(n\geq k\geq1\) and \(m\geq0\), form each of the
\(m\) clauses by independently drawing its \(k\) signed literals uniformly
from \(\{\pm x_1,\ldots,\pm x_n\}\).  Let \(NC\) be the event that no
clause repeats an *underlying variable* (opposite signs of the same variable
also count as a repetition).  Then

\[
 \Pr(NC)=\left(\frac{(n)_k}{n^k}\right)^m,
 \qquad (n)_k=n(n-1)\cdots(n-k+1).
\]

Conditional on \(NC\), the clauses are independent standard proper random
\(k\)-SAT clauses: their variable supports are uniform \(k\)-subsets and
their signs are independent fair bits.  Thus, for any event \(A\) of the
formula, writing \(p_w=\Pr(A)\) and \(p_s=\Pr(A\mid NC)\),

\[
 p_s\leq p_w/\Pr(NC),\qquad
 1-p_s\leq(1-p_w)/\Pr(NC).
\]

For fixed \(k,C\) and \(m\leq Cn\), the displayed probability is bounded
away from zero for all sufficiently large \(n\).  Consequently a supplied
with-replacement zero--one limit transfers to the proper-clause model at the
same fixed linear density.  This page does not prove such a threshold,
superadditivity, or a finite-size window; those are caller premises.

`scripts/check_clause_collision_transfer.py` computes the finite probability
in exact rational arithmetic and validates the parameter regime.

Source checked: David Gamarnik, *The satisfiability conjecture for random
k-SAT formulas: Human-friendly exposition of the recent OpenAI resolution*,
arXiv:2611.10139v1, physical pp. 4--5, SHA-256
`c1177271fde645c12e239c4f9b8763143091957c6e925b3c16b1c7ca9fdb820e`.
The elementary conditioning reduction is printed there; the threshold proof
itself is routed there through separate technical propositions.
