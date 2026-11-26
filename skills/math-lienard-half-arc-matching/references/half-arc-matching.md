# Half-arc matching: checked transfer

## Source and admitted statement

The source is *Two limit cycles for quintic Lienard systems* (OpenAI Math pinned preprint, 24 September 2026), SHA-256 `33941e46486c5fef246371cc3db57c18edb1935e49bc9e71dce6c30d8afbe71a`, pp. 3--11. Lemma 2.1 (pp. 3--4) gives positive-height arcs; Lemma 2.4 (pp. 8--9) gives their transverse limiting data at height zero; Proposition 2.5 (pp. 10--11) gives the following scoped transfer. The pinned source URL is <https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/two-limit-cycles-for-quintic-lienard-systems-September-24-2026.pdf>.

Let `F` be smooth on the real line and satisfy `F(0)=0`. For each sign, assume the arc equation
\[
  u_y=\phi_\pm(u)-y,\qquad \phi_\pm(u)=F(\pm\sqrt{2u}),\quad u\geq0,
\]
has the transverse height-zero endpoint parametrization supplied by Lemma 2.4. Thus, for every `r` in an open interval `I_±`, one gets endpoints
\[
  a_\pm(r)=M_\pm(0,r)-r<0<M_\pm(0,r)+r=b_\pm(r),
\]
with `M_±` smooth and `|M_{±,r}|<1`. Then, on the common open interval `I=I_+ intersection I_-`, geometric nonconstant periodic orbits of the Lienard vector field are in bijection with zeros of
\[
 \Delta(r)=M_+(0,r)-M_-(0,r).
\]
Moreover an orbit is isolated exactly when that zero is isolated.

## Independent derivation of the transfer

On `x>0` and `x<0`, `y` is strictly monotone along an excursion because `dot y=-x`. With `u=x^2/2`, division of `dot u=x dot x` by `dot y` gives `u_y=F(x)-y`, hence the corresponding signed arc equation. A nonconstant closed solution crosses both half-planes: integrating `dot y=-x` over its period gives integral `x dt=0`; it cannot contain the unique equilibrium by uniqueness. Axis crossings are transverse because `dot x=y` there. The endpoint order from the arc construction makes each physical half-plane endpoint map strictly decreasing. Their positive-to-positive composition is increasing, hence cannot have a nontrivial finite cycle; a closed orbit has one positive and one negative axis intersection and therefore one arc of each sign.

The two arcs close precisely when their two endpoint pairs coincide. Since each pair is `(M_±-r,M_±+r)`, coincidence is exactly `Delta(r)=0`. Conversely, at a zero use those common endpoints to reconstruct `x=+sqrt(2u_+(y))` and `x=-sqrt(2u_-(y))`. The endpoint relations `u_y(a)=-a>0` and `u_y(b)=-b<0` give simple zeros, so `dy/sqrt(2u)` is integrable at both endpoints. The finite-time arcs join with derivative `(dot x,dot y)=(y,0)` at the axis; uniqueness for the smooth vector field then gives a periodic solution. Finally `r+M_+(0,r)` has derivative `1+M_{+,r}>0`, so it is a local positive-section coordinate. Near a matched orbit the return-map fixed-point equation is precisely `Delta=0`. Smooth flow dependence identifies nearby distinct roots with nearby distinct orbit images, and conversely an isolated return fixed point has an isolating flow neighborhood. This proves the stated isolation equivalence without hyperbolicity.

## Exact check: the zero profile

For `F=0`, both profiles vanish. The arc through peak width `r` is
\[
 u(y)=(r^2-y^2)/2,\qquad -r\le y\le r.
\]
It obeys `u_y=-y`, has `M_+=M_-=0`, and hence `Delta=0` on `(0,infinity)`. The reconstructed vector field is the harmonic oscillator, so all nonzero energy ellipses are periodic and none is isolated. This is both a direct check of the correspondence and a boundary warning: a continuum of zeros must not be labelled as a family of limit cycles.

## Exclusions

The result does not construct or validate `M_±` from samples, certify their transverse domains, give a bound on zeros, or imply the paper's two-cycle theorem. The source's later quadratic-fit and sign arguments are not imported. A finite numerical plot or floating-point ODE run is not a verification of the arc hypotheses or of isolation.
