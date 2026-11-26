# C13--15: conditional exponential-polynomial reduction

## EXT-0087 · Polynomial exponential equations and Zilber's conjecture

**Checked source.** Mantova, with an appendix by Mantova and Zannier,
*Polynomial exponential equations and Zilber's conjecture*, arXiv:1402.0685v2
(24 November 2015), published in *Bulletin of the London Mathematical Society*
48 (2016), 309--320, DOI `10.1112/blms/bdv096`.  The local PDF rehashes to
`6cabea1010c8dcb47325e491ee10849990fe33fc1aebe9cfd007e2dfb4b4896c`.
The cited statements are on physical pp. 1--3, 6, and 9.

**Reusable conditional interface.** Let `k` be a finitely generated subfield of
`C`, and let `p(X,Y) in k[X,Y]` be irreducible with both partial derivatives
nonzero.  Under Schanuel's conjecture
\[
 \operatorname{trdeg}_{\mathbb Q}(z,\exp z)
 \ge \operatorname{lin.dim}_{\mathbb Q}(z),
\]
the source proves the one-variable strong exponential-algebraic-closedness
conclusion: some `z` satisfying `p(z,exp z)=0` has
`trdeg_k(z,exp z)=1`.  The operational reduction is narrower: all algebraic-over-
`k` solutions lie in a finite-dimensional Q-space; after denominator control and
a function-field reduction, it is enough to prove finiteness of rational solutions
to
\[
 p(x\mathbin\cdot b,\exp(x\mathbin\cdot b))=0,
 \qquad x\in\mathbb Q^\ell,
\]
for Q-linearly independent `b` (Theorem 1.3 / Proposition 2.11).

**Actual dependency boundary.** The positive generic-solution conclusion depends
on Schanuel.  Its reduction also cites Gunaydin's denominator step and Zannier's
function-field Laurent theorem (Theorem 2.7); the appendix replaces only a later
Schanuel step by Baker's theorem and gives the stated unconditional finiteness
result, not Theorem 1.2.  This is not a numerical root certificate, an effective
root bound, or an unconditional solution algorithm.
