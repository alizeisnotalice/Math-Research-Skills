# Positive ground state to drift curvature

## Accepted interface

Let \((M,g)\) be a smooth boundaryless Riemannian manifold, with
\(\Delta=\operatorname{div}\nabla\).  If \(v\in C^\infty(M)\) is strictly positive and
\[
(-4\Delta_g+\operatorname{Scal}_g)v\geq\lambda v,
\]
then \(t=-2\log v\) is smooth and
\[
\operatorname{Scal}_g+2\Delta_gt-|dt|_g^2\geq\lambda.
\]

## Independent calculation

From \(t=-2\log v\),
\[
\Delta_gt=-2\left(\frac{\Delta_gv}{v}-\frac{|dv|_g^2}{v^2}\right),
\qquad |dt|_g^2=4\frac{|dv|_g^2}{v^2}.
\]
Adding the two displayed terms cancels the gradient-square terms, hence
\[
\operatorname{Scal}_g+2\Delta_gt-|dt|_g^2
=\operatorname{Scal}_g-4\frac{\Delta_gv}{v}
=\frac{(-4\Delta_g+\operatorname{Scal}_g)v}{v}.
\]
Division preserves the inequality precisely because \(v>0\).  This proves the interface without any appeal to a numerical discretization.

For a genuine compact example, take the unit round two-sphere, for which
\(\operatorname{Scal}=2\), and take \(v=1\).  Then \((-4\Delta+\operatorname{Scal})v=2v\),
\(t=0\), and \(D(g,t)=2\), so the conclusion holds with \(\lambda=2\).  This checks the algebraic transfer only; it is not a width computation.

## Source checked

OpenAI, *Spectral scalar curvature and Urysohn width in dimension three*,
preprint dated 2026-10-05, local PDF SHA-256
`2a0852ff04d11752b6a39d3da257ef8d768e11d1dd269e44f76745a55afae99a`.

Physical PDF p. 4, Lemma 2.1 states the quadratic-form hypothesis on a connected smooth
boundaryless manifold and constructs a positive smooth `v`: by the first eigenfunction in the
compact case and a Dirichlet-exhaustion/Harnack/interior-estimate limit in the noncompact case.
It then prints the displayed identity with \(t=-2\log v\).  The present interface deliberately
treats that existence construction as a prerequisite whenever `v` is not independently supplied.
The later stable-surface and width arguments on pp. 5--20 are not imported here.
