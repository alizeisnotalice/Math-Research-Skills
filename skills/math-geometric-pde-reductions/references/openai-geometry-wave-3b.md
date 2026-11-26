# OpenAI geometry wave 3b: source-bound analytic interfaces

This staged reference retains methods and explicit interfaces from sixteen
current OpenAI originals selected in `inputs/geometry-b.jsonl`. It assumes the
original statements, retains every displayed hypothesis, and makes no
independent proof audit or global theorem claim.

## Exact radial Calabi-flow algebra

For a smooth `H(t,x)` on `x in [0,1]`, let `v_*=x(1-x)`, `w=x^(n-1)`, and
require `b=1+v_*H>0`. The source sets
`v=v_*+v_*^2H`, `K(H)=w^(-1)(w v_*^2H)''`, and
`A_H=[w^(-1)(w v_*^2H)'']''`. Then scalar curvature is
`S=n(n+1)-K(H)`, with average `n(n+1)` because
`int_0^1 K(H)w dx=[(w v_*^2H)']_0^1=0`. Under
`H_t+(1+v_*H)^2A_H=0`, the construction gives the source's exact radial
Calabi-flow reduction.

Run the staged algebra checker (it does not certify `b>0`):

```sh
python3 scripts/calabi_radial_identity.py --self-test
python3 scripts/calabi_radial_identity.py --n 2 --h 1 1
```

The fixture uses `H=1+x`; it returns an exact zero weighted average. The
checker only verifies polynomial endpoint divisibility and the integral
identity, not smooth Kähler extension or a flow solution.

## Retained procedures

### Curvature and geometric comparison

For complete simply connected `sec<=0`, the Cartan--Hadamard component uses
`D_p=d(p,.)^2/2`, with `Hess D_p>=g`, `(exp_p)^*g>=g_p`, and
`|d log_p(X)|<=|X|`; a nonatomic compactly supported probability measure is
balanced by choosing the center/scale in the source's `Phi_{p,a}` map.

For the metric Blaschke source, use the normal Jacobi Lagrangian graph and
its determinant interpretation only after the paper's periodic normal-Jacobi
input is supplied. The least-volume source reduces a cone comparison to its
stationary density inequality; the explicit constants are
`d_j=sigma_j(j/(2pi e))^(j/2)` and the source proves strict decrease of
`d_k d_l/d_(k+l)` in `l`.

### Four-dimensional, symplectic, and flow interfaces

For a definite hypersymplectic pair, form its positive Gram matrix `K`; the
source coefficient-sphere map is the normalized radial map
`v -> K^(-1)v/|K^(-1)v|`. The taming-current component takes a finite measure
whose projection obeys `mu(B_r(x))<=Cr^2` and the fourth-angle bound (5.2),
then obtains `theta(x)=lim r^(-2)mu(B_r(x))` and closedness of the positive
density restriction. It is not a general current regularity test.

For a compactly supported two-form `eta=h(x,y)dx wedge dy` of zero integral
on a coordinate disk, the packing source takes `h_0(y)=int h(x,y)dx`,
`A=int_(-infty)^x(h(v,y)-rho(v)h_0(y))dv`, and
`B(y)=int_(-infty)^y h_0(v)dv`; then
`alpha=A dy-rho(x)B(y)dx` is compactly supported and `d alpha=eta`.

The two Ricci-flow papers, and the held distributional Alexandrov source, are
**Scoped reference.** Their root-end functionals, warped barriers, and
sign-symmetric RCD tests require the complete source-specific PDE/compactness
setup; the usable interface is the stated hypotheses, not a finite solver.

### Metric-measure, index-form, complex, and transport interfaces

On an RCD space, the weak Hessian evaluation retained from (1.2) is
`H_F(nabla g,nabla g)(h)=-int div(h nabla g)<nabla F,nabla g>dm
-int h<nabla F,nabla_(nabla g)nabla g>dm`. The change of reference measure
is `m_lambda=e^(lambda F)m`; generator-domain closure is part of the input.

For the no-conjugate-points passage assembly, concatenate the intrinsic index
form across portions outside the transition region with the supplied passage
forms inside it. This proves only the stated nonnegativity for compactly
supported `H^1` normal fields after its curvature and passage assumptions.

For the Hartogs-domain obstruction, centered chart bounds and Cauchy's
estimate give `|partial_w F_l(z,0)|<=B exp(phi(z)/2)`; the Jacobian estimate
is `log|d(z)|^2<=2log6+6logB+4log(1/(1-|z|))+phi(z)`. It is not a generic
bounded-coordinate criterion.

For weak MTW, smooth nonconjugate branches give the branch Hessian framework.
The power reduction is especially reusable: if section oscillation
`F(r)<=C_0r^beta` for `0<r<r_0`, then both optimal maps have representatives
with every Holder exponent at most `min(beta,1)/2`; it follows from
`|p-q|^2/8<=F(r)+r` on each lifted convex section.

## Source ledger

| Source | Physical pages | Scoped adoption |
| --- | --- | --- |
| [Generalized Cartan–Hadamard isoperimetry and Euclidean equality rigidity](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/paper.pdf) (`a7310d708fef81eaa14c96d4a420e39098858ee98e23201381ff5e86b584b29f`) | 8, 20, 25 | For complete simply connected sec<=0, use Hess D_p>=g, exp expansion and log contraction, then the source balancing map; retain no global isoperimetric equality theorem. |
| [Deforming hypersymplectic four-manifolds to hyperkähler triples](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026/paper.pdf) (`92c36602fb4968087ec043e7b3816473b15ab21d0072899f31154337676b2bec`) | 7, 8 | For a supplied definite pair and positive Gram matrix K, retain v->K^(-1)v/|K^(-1)v| and the stated self-dual/almost-complex conventions; exclude the deformation theorem. |
| [Taming implies compatibility on four-manifolds](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/paper.pdf) (`cbddc627efab3dd49a69a32b270b52b6ea4528846bd3b313038a696ed3281265`) | 11, 12, 16 | For the source current P+Q and measures satisfying (5.1)--(5.2), retain the density theta=lim r^(-2)mu(B_r) and closed positive-density restriction only. |
| [Symplectic Ball Packings in Higher Dimensions](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/paper.pdf) (`54a390c7a58b2f003896a3ea5319b0e8376dbf69059b7c00645d0d55babdbdb2`) | 11, 12 | For compactly supported eta=h dx wedge dy of zero integral on a disk, use the A,B,rho primitive formula on p.12; retain support and smooth-parameter dependence. |
| [The metric Blaschke theorem](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-metric-Blaschke-theorem-September-23-2026/paper.pdf) (`c631e2d36940a81e3c5f5476a13bdfbf12d77b9debd6ce2f3852357627256257`) | 6, 7, 19 | Scoped reference. Requires the source periodic Jacobi and cut-incidence hypotheses; retain only its normal-Jacobi determinant interface. |
| [The Solomon–Yau least-volume theorem](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/paper.pdf) (`b44def9b041e8f318f01e2fad404216fb52f5f1c3642cddb45df23ea8322cb96`) | 4, 5 | For the source cone/immersion setup, retain d_j=sigma_j(j/(2pi e))^(j/2), strict product-ratio decrease, and stationary density comparison; exclude least-volume theorem. |
| [A closed Ricci flow with bounded scalar curvature and finite-time curvature blowup](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/paper.pdf) (`88b1d8270cb2bc5fb315b3421f984f9db84a4431d4780f89b1bcf6504839510b`) | 4, 5, 6, 7, 8, 9, 10, 16, 17, 18 | Scoped reference. The r,phi profile bounds and R>=-C rely on the paper’s doubly warped flow/barrier construction; no standalone blowup routine. |
| [Bounded scalar curvature and smooth extension of four-dimensional Ricci flow](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/paper.pdf) (`95655c4053c94f2bf129eddfda0c10b9d2c007f45a10548a02cd1c5624567bca`) | 5, 6, 7, 8, 26, 30, 35, 40, 45, 50, 55, 56 | Scoped reference. Requires root-end analytic family, concentration/exterior estimates and smooth-extension passage; no general Ricci-flow extension test. |
| [A finite-time singularity of Calabi flow on projective space](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/paper.pdf) (`486e9e5ff47e92a4db90c7904eb5842085de78f02f825f5b68bcc5bd2719f25d`) | 4, 5, 6, 9 | For smooth H with 1+v_*H>0, retain v=v_*+v_*^2H, K=w^(-1)(wv_*^2H)double-prime, A_H=Kdouble-prime and the exact radial flow equation; see staged exact polynomial checker. |
| [The Isoperimetric Conjecture for the Cubic Flat Three-Torus](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Isoperimetric-Conjecture-for-the-Cubic-Flat-Three-Torus-September-24-2026/article.pdf) (`ce66c455780d2efc19b18a9b767a7453d2e951d55f4b58d5167ec2716b3974c2`) | 8, 9, 13, 14 | Scoped reference. Retain the exact flux identity and h,s,t constraints only with the source cube-symmetry and slice hypotheses. |
| [Gigli’s distributional curvature characterization of Alexandrov spaces](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/main.pdf) (`e104c43128bea2923c4f6d33f911a519f0c0fd2ca6904a2bcdad807ed7a42fd6`) | 1, 4, 6, 10, 12, 16, 17, 19, 24, 30, 36, 42, 48, 52, 53 | Scoped reference. Held: requires companion weak-Hessian theorem and full RCD/test-field construction; not adopted as an Alexandrov recognizer. |
| [Weak Hessian bounds along every geodesic in RCD spaces](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/weak-hessian-geodesics.pdf) (`eb34f06c23632a5745015f9e4ef363b9074540a400f95ed3de7aa9dc10aaecc2`) | 2, 6, 7, 8, 9, 10 | For full-support RCD data and compact tests, retain weak Hessian evaluation (1.2) and bounded m_lambda=e^(lambda F)m reweighting only after generator-domain hypotheses. |
| [A Three-Manifold Without Conjugate Points and Without a Nonpositively Curved Metric](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026/paper.pdf) (`0ac6d8b58c960941ae1b45338abf08664ca3f61e5bcfa0e28d91758fea63c5bd`) | 19, 20 | For a complete manifold with the paper’s nonpositive exterior curvature and supplied passage forms, concatenate index forms and retain compactly-supported H^1 nonnegativity. |
| [A negatively pinched Kähler threefold without bounded holomorphic coordinates](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/paper.pdf) (`59e7bcf19b96d5d90e787622473764011de3be9d93854b39fc065f019667e022`) | 5, 6 | For the source Hartogs domain and centered chart bounds, retain the Cauchy derivative and Jacobian inequalities only; exclude the threefold conclusion. |
| [Global Support and Convex Injectivity Domains under Weak MTW](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/paper.pdf) (`e16087753fc93a840bd357fe203ffd1d7a511245db91f5e629132e91db440724`) | 1, 5, 6, 7, 8, 9, 10, 18, 20, 22, 23, 24 | Scoped reference. Requires compact weak-MTW geometry and smooth nonconjugate branches; retain only the branch-energy/Hessian contradiction interface. |
| [Uniform Bi-Holder Transport from Weak MTW](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/paper.pdf) (`1e1a412dff1dd2634c638857ed802fa444b2cd044346277297f6415ba1889b10`) | 16 | If F(r)<=C_0 r^beta for 0<r<r_0, use |p-q|^2/8<=F(r)+r to obtain inverse optimal-map Holder exponents <=min(beta,1)/2. |
