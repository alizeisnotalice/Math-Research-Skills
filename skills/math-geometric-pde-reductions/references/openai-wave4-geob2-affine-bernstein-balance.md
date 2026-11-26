# Affine-maximal section balance in dimensions 3--9

Source: *The affine Bernstein theorem in dimensions three through nine*,
OpenAI (24 September 2026), SHA-256
`f028b02be7ed31404334d03f5874bd368ad32b2a5b4d5820fc075bac0872efb3`,
[official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-affine-Bernstein-theorem-in-dimensions-three-through-nine-September-24-2026/main.pdf).

## Scoped interface

This source-bound route concerns a smooth locally uniformly convex entire
solution of the affine maximal equation in ambient graph dimension
`3<=n<=9`.  It must not be applied to an arbitrary convex graph: the source
uses its affine-area stationarity, compactly supported variations, and the
dimension-dependent positivity below.

For the paired covector terms on physical p. 14, the coefficient matrix at
`lambda=1` has determinant

\[
 n-1-\frac{(n+2)^2}{16}=\frac{(n-2)(10-n)}{16}.
\]

This is positive precisely in the stated dimensional window.  Choosing
`lambda` near one handles the remaining scalar term and yields the source's
weighted energy estimate; with `v(s)=tilde v(log s)`, it concludes

\[
 \int v^2\,d\sigma\le C_n\int|D_sv|^2\,d\mu. \tag{4.19}
\]

Keep the source's compact support/cutoff condition on every integration by
parts.

## Balance-to-rigidity sequence

1. Use the maximal-direction centering and model-exclusion results to exclude
   the source's multi-direction degenerations; no finite numerical test
   substitutes for that step.
2. Obtain uniform tangent-section balance
   `-rho K_a(t) subset K_a(t)` (Lemma 6.1, p. 20).
3. Normalize a section with the source's affine map to obtain fixed inner and
   outer Euclidean-ball controls, thereby meeting the stated
   Trudinger--Wang interior-estimate section hypothesis.
4. Apply that estimate only on a bounded convex domain with positive-definite
   Hessian and `-1<=f<=0`; the paper gets smooth bounds, then `D^3u=0` and
   `u(x)=1/2 x^TQx+b dot x+c`, `Q>0` (pp. 22--23).

## Record boundary

The conclusion is the stated affine Bernstein rigidity, not a generic
regularity theorem in dimensions outside 3--9 or for degenerate Hessians.

Locators: physical pp. 5--8, 14--15, and 20--23; (4.19), Lemma 6.1,
Theorem 6.4.
