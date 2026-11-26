# Descent and suspension for the classical one-phase energy

## Source and verified locus

OpenAI, *The critical dimension for one-phase Bernoulli minimizers* (pinned
PDF, commit `3344da59991ed94f9ba711217b29c1d760badfa6`), Lemma 2.3 on PDF
page 6 and Proposition 2.6 on PDF pages 8--9.  Local file SHA-256:
`eb1a535a1d8a9dc4c87d9eba7f861d5eda65531b75ac473eb5a5cb3ab7d3f727`;
the reviewed PDF has 50 pages.

## Contract

For an open set `D`, write
\[
  J(w;D)=\int_D\left(|\nabla w|^2+\mathbf 1_{\{w>0\}}\right).
\]
Call `w>=0`, in `H^1_loc(R^m)`, a global minimizer if for every ball `A` and
every nonnegative `z in H^1(A)` with `z-w in H^1_0(A)`,
\[
  J(w;A)\le J(z;A).
\]
The two statements below use exactly this convention.  A fixed multiplicative
constant in front of the whole energy is harmless, but changing the relative
coefficient of the volume term requires a separate proof (or rescaling with
its stated effect on the free-boundary normalization).

## Descent: independent proof

Assume `U(y,s)=v(y)` is a global minimizer on `R^k x R`.  If `v` failed to be
one in `R^k`, some ball `B` and nonnegative `q in H^1(B)`, with
`q-v in H^1_0(B)`, would satisfy
\[
  J(v;B)-J(q;B)=\delta>0. \tag{1}
\]
Let `psi` be the zero extension of `q-v`, and take the piecewise-linear cutoff
`eta_L`, equal to one on `[-L,L]`, zero off `[-L-1,L+1]`, with values in
`[0,1]` and `|eta'_L|<=1`.  The perturbation
\[
 V_L(y,s)=v(y)+\eta_L(s)\psi(y)
\]
is nonnegative: in `B` it is `(1-eta_L)v+eta_L q`.  Its difference from `U`
has compact support and hence is an admissible perturbation in a sufficiently
large ball of `R^(k+1)`.

On the central cylinder, (1) makes the energy difference `-2L delta`.  On a
transition cylinder, convexity of the squared norm and the derivative of the
cutoff give
\[
 |\nabla_y V_L|^2\le(1-\eta_L)|\nabla v|^2+\eta_L|\nabla q|^2,
 \qquad |\partial_sV_L|^2\le |q-v|^2.
\]
The change of the positivity indicator is at most one.  Since both transition
cylinders have height one, their combined excess is bounded above by a finite
constant depending on `B,v,q`, for example
\[
 C=2\int_B\bigl(|\nabla q|^2+|q-v|^2+1\bigr),
\]
and not on `L`.  Thus `J(V_L)-J(U)<=-2L delta+C`, negative for sufficiently
large `L`, contradicting global minimality.  Therefore `v` is a global
minimizer.

The long-cylinder cutoff is essential: restricting a competitor to one slice
does not itself yield an admissible compactly supported perturbation in the
higher-dimensional problem.

## Suspension: independent proof

Conversely, let `v` be a global minimizer on `R^k`, set `U(y,s)=v(y)`, and
take a ball `A=B_R((y_c,s_c))` in `R^(k+1)`.  Let `V>=0` satisfy
`V-U in H^1_0(A)`.  For almost every `s` in `(s_c-R,s_c+R)`, the horizontal
slice
\[
 A_s=B_{\sqrt{R^2-(s-s_c)^2}}(y_c)
\]
has `V_s-v in H^1_0(A_s)`.  One way to justify this without adding a trace
regularity hypothesis is to extend `V-U` by zero, approximate it in `H^1` by
smooth compactly supported functions in `A`, and use Fubini on a convergent
subsequence.  Slice minimality and Fubini then give
\[
 \begin{aligned}
 J(U;A)&=\int_{s_c-R}^{s_c+R}J(v;A_s)\,ds\\
 &\le\int_{s_c-R}^{s_c+R}J(V_s;A_s)\,ds
 \le J(V;A),
 \end{aligned}
\]
where the last inequality discards the nonnegative `|partial_s V|^2` term.
So `U` is a global minimizer.

## Scope boundary

These proofs do not state or prove a classification of cones, the critical
dimension, free-boundary regularity, or the nature of singular sets after
suspension.  They also do not apply automatically to weighted, two-phase,
anisotropic, fractional, obstacle, or merely stationary problems.
