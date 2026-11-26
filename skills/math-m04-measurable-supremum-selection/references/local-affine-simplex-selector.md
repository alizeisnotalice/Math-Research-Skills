# Local affine selector on one rational simplex

Source anchor: J. Wąsowicz, *Local Affine Selections of Convex
Multifunctions*, arXiv:1611.02584v1 (2016), SHA-256
`fcfb7ddfbb5675f4a50a0993ad2fcaa4983d2e310df9d675d8fb081eef1886a7`.
The checked local five-page PDF has Lemma 3 and Theorem 4 on pp. 2–3: choose
one graph point at each vertex of a simplex containing the target point in its
interior, then extend the chosen values by barycentric coordinates. Proposition
5 on p. 4 is the stated warning against an automatic infinite-dimensional
extension.

## Exact finite contract

Provide (n+1) rational vertices (v_0,\ldots,v_n\in\mathbb R^n), rational
responses (y_i\in\mathbb R^m), and a rational point (x_0). The script
solves exactly for

\[
x_0=\sum_i\lambda_i v_i,\qquad \sum_i\lambda_i=1.
\]

It accepts the point as a certified *strict* interior point only when every
\(\lambda_i>0\). It returns exactly
\(A(x_0)=\sum_i\lambda_i y_i\).

For an independent membership certificate, provide an H-polyhedron for the
graph, (G=\{(x,y):N(x,y)\le b\}\). The script verifies each
\((v_i,y_i)\in G\), recognizes this finite intersection of half-spaces as
convex, and directly checks \((x_0,A(x_0))\in G\). If no H-polyhedron is
available, `declared_convex_graph_contract: true` yields only a **conditional**
calculation: the caller, not the script, has supplied graph convexity and the
vertex memberships.

## Proof carried by a certified run

Positive barycentric weights sum to one. Thus

\[
(x_0,A(x_0))=\sum_i\lambda_i(v_i,y_i).
\]

When every graph point on the right lies in a convex graph, the left side lies
in that graph. This is the whole finite calculation used here.

## Exclusions

This helper proves neither graph measurability nor Borel/analytic selection,
measurable argmax selection, a global selector, a finite-patching theorem, or
an infinite-dimensional result. It must not be used to close M04's retained
measurable-selection gap.
