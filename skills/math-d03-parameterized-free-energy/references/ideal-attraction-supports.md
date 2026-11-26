# Ideal-attraction transform: active shifts and supports

**Source.** OpenAI, *A radial continuum phase transition with algebraic decay*,
preprint dated 2026-09-24, PDF SHA-256
`d53cafa68c322a072098e8a3cb2e3b7e059b4239ba95466d089632b8ce368587`,
pp. 8--16. The pinned source is
<https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-radial-continuum-phase-transition-with-algebraic-decay-September-24-2026/paper.pdf>.

## Admissible interface

Fix `beta>0` and `a>0`. Let a pressure in field `h` have the exact dual
representation

\[
 Q(\beta,h)=\sup_{d\geq0}\{hd-H(\beta,d)\}.
\]

Before using this note, establish for the actual model that the quadratic
objective below is finite, attains its maximum, and that the inner pressure
supremum is attained at every shifted field used. In the cited paper these
facts follow from its canonical/grand-canonical duality (Proposition 2.6),
the stability bounds, and the coercive estimate (4.5), for its specific
bounded-core pair-interaction class. They are not consequences of convexity
alone. Its uniform statements additionally require the source's conditions
on `t`, `A`, and `0<a<=2(A+1)` (Propositions 2.3 and 4.2).

Define

\[
 (T_aQ)(\beta,h)=\sup_{u\in\mathbb R}
 \left\{Q(\beta,h+\beta a u)-\frac{\beta a}{2}u^2\right\}.
\]

## Transfer statement and derivation

Under that interface,

\[
 (T_aQ)(\beta,h)=\max_{d\geq0}
 \left\{hd-H(\beta,d)+\frac{\beta a}{2}d^2\right\}. \tag{1}
\]

Indeed, substitute the dual representation and complete the square:

\[
 Q(\beta,h+\beta au)-\frac{\beta a}{2}u^2
 =\sup_{d\geq0}\left\{hd-H(\beta,d)+\frac{\beta a}{2}d^2
 -\frac{\beta a}{2}(u-d)^2\right\}.
\]

Taking the supremum in `u` proves (1). With both suprema attained, an active
shift is exactly a maximizing density in (1): equality in the square
completion forces `u=d`. Thus the active set is nonempty and compact only
after the asserted coercivity/attainment check; it is not licensed at `a=0`.

If `u` is active and `x=(beta,h+beta*a*u)`, comparison in the transform with
`u+r/(beta*a)` gives the parabolic field bound

\[
 Q(\beta,x_h+r)\leq Q(\beta,x_h)+ur+\frac{r^2}{2\beta a}. \tag{2}
\]

Consequently every field-coordinate subgradient of `Q` at `x` equals `u`:
combine its supporting lower bound with (2), divide separately by positive
and negative `r`, and send `r` to zero. In the full `(beta,h)` variables,
the source proves (Proposition 4.4) the sharper formula

\[
 \partial(T_aQ)(\lambda)=\operatorname{conv}\!\bigcup_{u\ \mathrm{active}}
 \{(e+a u^2/2,u):(e,u)\in\partial Q(\beta,h+\beta au)\}.
\]

Its reverse inclusion uses locally bounded subgradients and closedness of the
subgradient graph on the compact set of shifted parameters. Supply those
finite-dimensional convex facts for a new model; do not infer this formula
from merely sampled pressure values.

## Exact nonsmooth sanity calculation

For the finite convex oracle `Q(h)=max(0,h)`, take `beta=a=1` and `h=-1/2`.
The density objective in (1) on `[0,1]` is `-d/2+d^2/2`; its two maximizing
endpoints are `d=0,1`, each of value zero. Directly, the active shifts
`u=0,1` both give zero in the transform. The source's support formula reduces
to the convex hull of the field slopes `{0,1}`, namely `[0,1]`. At active
`u=0`, `r=1` makes (2) an equality: `Q(1/2)=1/2=r^2/2`.

This calculation checks the algebra and the nonsmooth branch behavior only.
It is not a continuum-gas pressure or a verification of the source's
stability, thermodynamic-limit, or phase-transition hypotheses.
