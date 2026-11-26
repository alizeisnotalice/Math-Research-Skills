# Thue–hypergeometric lower bounds over imaginary quadratic fields

**Source and version check.** Paul M. Voutier, *Thue’s Fundamentaltheorem, I: The general case*, *Acta Arithmetica* 143(2) (2010), 101–144, DOI [10.4064/aa143-2-1](https://doi.org/10.4064/aa143-2-1).  The local arXiv:0805.3176v3 copy has SHA-256 `429b07e0ba92e93132c36ab446411ec2b2f8a57ddbaefdbe8d59ffa7ee5aeb3c`.  The source's generic Diophantine step (Lemma 6.1) and its actual parameter substitution in the proof of Theorem 2.4 were checked on physical pp. 40–41.

## Good consecutive approximants

Let \(K=\mathbb Q\) or an imaginary quadratic field, \(\theta\in\mathbb C\), and suppose that, for every \(r\ge0\), algebraic integers \(p_r,q_r\in K\) satisfy
\[
 |q_r|<k_0Q^r,\qquad |q_r\theta-p_r|\le l_0E^{-r},\qquad
 p_rq_{r+1}\ne p_{r+1}q_r,
\]
for positive \(k_0,l_0\) and \(E,Q>1\).  Then for algebraic integers \(p,q\in K\) with \(|q|\ge 1/(2l_0)\), Lemma 6.1 gives
\[
 \left|\theta-\frac pq\right|>\frac1{c|q|^{\kappa+1}},\qquad
 \kappa=\frac{\log Q}{\log E},\quad
 c=2k_0Q(2l_0E)^\kappa.
\]

The nonzero consecutive determinant is a required certificate, not an optional regularity condition.  In a Thue–hypergeometric application, separately retain the algebraic-integrality/denominator ledger used to form \(p_r,q_r\), and prove \(E,Q>1\) before computing \(\kappa\).

## Source-specific construction gate

Theorem 2.4 supplies one such family from its normalized hypergeometric forms under its named \(K,\beta_i,\gamma_i,\tau,x,n,U,Z,W,A,d,g,h,C_n,D_n,N_{d,n}\) data.  Its conclusion requires \(E>1\) and
\(\max(|1-W(x)|,|1-1/W(x)|)<1\).  That route is target-specific: do not use the lower-bound template merely because a number has an algebraic expression.  No current Euler-constant construction supplies this hypergeometric data.
