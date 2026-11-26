# Scoped reference. Attained radial defect and aligned chords

**Source.** OpenAI, *A positive solution to Tingley’s problem*, Lemmas 2.2 and 3.1, Proposition 4.2, PDF pp. 3--6; SHA-256 `6b4ae2372e8f56539f55cd0678357248520fc7b7b095b1812690968f68e6f6ae`.

## Input contract

Let `f:S_X -> S_Y` be a surjective isometry of unit spheres of nonzero real Banach spaces.  For its radial defect `D_q(x,y)=||f(x)-qf(y)||-||x-qy||`, assume an attained positive maximal defect `M` at `(x0,y,t)` with `0<t<1`.  The source obtains that attained setting via an ultraproduct; do not assume attainment merely because a supremum is finite.

## Reuse

For an interior point `c` use the unique continuous radial intersection `c+rho(v)v` of each unit direction with the sphere.  Under the attained-defect contract, the Darbo return map on the explicitly constructed closed convex direction set has a fixed point.  Proposition 4.2 then supplies aligned chords
`x=ty+pv`, `z=ty-rv`, `f(x)=tf(y)+sw`, `f(z)=tf(y)-uw`,
with `s-p=r-u=M` and `p+r=s+u=||x-z||`.

This reference is conditional on the sphere isometry, attained positive defect, ultrafilter enlargement, and Darbo noncompactness contraction used in the source.  It is not a generic stability principle for arbitrary almost-isometries.

## 固定来源

- 物理页 3, 4, 5, 6。Lemma 2.2; Lemma 3.1; Proposition 4.2 SHA-256 `6b4ae2372e8f56539f55cd0678357248520fc7b7b095b1812690968f68e6f6ae`。[A positive solution to Tingley’s problem](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/paper.pdf)
