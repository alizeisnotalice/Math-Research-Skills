# 分段一维 ODE 残差证书

Use this narrow certificate for a classical unknown `u` and a piecewise-polynomial `v` on `[x_0,x_m]` when

\[
 u''+b(x)u'-c(x)u=0,\qquad E=u-v.
\]

On each closed segment require exact rational certificates for `v`, `b`, and `c`, and compute

\[
r=v''+bv'-cv,\qquad E''+bE'-cE=-r.
\]

If every join is `C1`, `c(x)>=mu>0`, `|r(x)|<=rho`, and the *separately certified* endpoint errors obey `|E(x_0)|,|E(x_m)|<=B`, comparison with the constant barriers gives

\[
 \|E\|_{L^\infty[x_0,x_m]}\le \max\{B,\rho/\mu\}.
\]

At an interior positive maximum, `E'=0`, `E''<=0`, hence `E''+bE'-cE<0` above the upper barrier; the lower barrier is analogous. At a join the one-sided argument needs continuity of `E'`. This proves a profile enclosure only.

## Exact finite checker

`scripts/check_piecewise_ode_residual.py` accepts rational monomial coefficients in the local coordinate `t=(x-left)/(right-left)`. It differentiates with the correct segment-length factors, converts the residual and `c` into exact Bernstein coefficients, and uses their convex-hull enclosure. The endpoint bound is an input assertion about the unknown solution; it cannot be inferred from the polynomial table.

The checker deliberately emits `derivative_certificate: not_provided`. To bound `E'`, derive a separate first-order equation such as `F'+aF=f`, certify an anchor value for `F`, and certify the relevant integrating-factor estimate. The source below uses precisely such an additional step; no derivative enclosure follows merely from the displayed profile certificate.

## Source and scope

OpenAI, *Microscopic jamming in the negative spherical perceptron*, pinned `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`, SHA-256 `8d94e973e689e60bdd0443e0f466711519993188fb478dee573993afaf8ff896`, PDF physical p. 115, Lemma 12.1. Equation (12.4), the positive zero-order lower bound, the endpoint barriers, and the maximum-principle argument yield the profile bound. The following paragraph rewrites the derivative as a first-order equation and invokes an integrating factor; that separate material is required for the derivative number. This reference does not validate the perceptron headline theorem or any numerical certificate outside its stated profile.
