# OpenAI geometry wave 2: scoped analytic transfers

This staged note distills nine candidate sources in families 336--359. Every assertion retains its source hypotheses; it does not review the papers' original conclusions or promote a global geometry theorem from a finite check.

## Finite Einstein-four curvature block check

For an oriented Einstein four-manifold normalized by `Ric = 3g`, family 348 uses the curvature operator `diag(Id+T,Id+U)` on `Lambda+ + Lambda-`, with `T,U` symmetric and trace-free. For eigenvalues `t_s,u_s`, put `x=-min t_s`, `y=-min u_s`, `v^2=|T|^2/6`, and `b^2=|U|^2/6`. The common pointwise calculation gives `min sec=1-(x+y)/2`, `v<=x<=2v`, and `b<=y<=2b`. Thus `x+y<2` is strict positivity and `x+y=2` is only nonnegative.

Run the staged exact-rational checker from this skill directory:

```sh
python3 scripts/einstein_four_block_check.py --self-test
python3 scripts/einstein_four_block_check.py --t -1 0 1 --u -1/2 0 1/2
python3 scripts/einstein_four_block_check.py --t -1 0 1 --u -1 0 1
```

The second fixture has `min sec=1/4`; the third has `min sec=0`, and is accepted only by the nonnegative convention. The self-test also rejects a non-trace-free triple and a negative-curvature case. The checker neither constructs a metric from blocks nor proves a global rigidity/classification.

## Procedures retained from cached source pages

### Pressure law (family 336)

Input `A0,P0,epsilon,b0>0`. Choose `k`, `Y`, `D_g`, and `T`, in that order, as in (2.6)--(2.9). With a smooth probability density `rho` on `[1,2]`, put `h(y)=D_g(1+y)^(-1/4)` and `g(y)=integral_[1,2] max(y,r h(y))rho(r)dr`. Define `X(f,t)=k^(-1) atan(f^(1/3)/g(t f^(2/3)))`, then invert `X(.,t)` in `f` to obtain odd `F(x,t)`. The output obeys `F_x>=A0t`, `|F_t|<=epsilon|F|`, `F F_t<=epsilon F_x`, `F_x<=b0t^2 or -F F_t>=P0F_x`, and `F_x<=b0t^2+epsilon F^2`. This is only the one-dimensional pressure construction, not metric stretching or width reconstruction.

### Stationary-varifold center measures and integer counts (family 346)

For a stationary integral `m`-varifold with `m-1<s<dim_H Sing(V)`, select a compact density level, a point `p`, and scales `L_i` as in Proposition 2.1, then form `sigma_i=L_i^(-s)(eta_{p,L_i})#(H^s restricted to K_Q cap B_{L_i}(p))`. The output is `V_{L_i}->Q|Pi|`, support on singular density-`Q` points, `sigma_i(B_u(X))<=Cu^s`, and `c<=sigma_i(B_1)<=C`.

For the tube count, input a reference disk `S`, nearest projection `pi`, scaled error `e+lambda`, and `gamma=l+sup|z_phys|`. The source establishes `|int div_S X dM-int B:nabla_SX dmu|<=C gamma int(e+lambda)(|nabla X|+|X|)dmu`, `|J_pi-1|<=C(e+lambda)`, and `pi#(J_pi mu)=N vol_S` for integer-valued `N`. The eventual constant-count assertion still needs the stated weak-type potential step; this is not a finite point-cloud routine.

### Support-sensitive Sobolev transfer (family 348)

Input a closed four-manifold, `a>0`, `P>=0`, and `||f||_2^2<=C Vol{f!=0}^{1/2}E(f)` for every Lipschitz `f`, with `E(f)=int(a|grad f|^2+Pf^2)`. For each integer `k`, form `f_k=min((|f|-2^k)_+,2^k)`, `m_k=Vol{|f|>2^k}`, and `b_k=2^(4k)m_k`. The source gives `b_(k+1)<=16C b_k^(1/2)E(f_k)`, disjoint gradient layers, and `sum_k E(f_k)<=C_2E(f)`. Summing yields `||f||_4^2<=C' E(f)`. The procedure does not establish the support estimate.

### Planar logarithmic profiles (family 350)

Given subprobability measures `mu_j` and `S_j->infinity`, choose a countable relatively compact basis, diagonalize `ell_i=lim log(mu_j(G_i))/(2S_j)`, and set `V(x)=inf_(x in G_i)ell_i`. This yields compact/open profile bounds. For subharmonicity additionally require `Delta U_j+K_j^2p_jU_j=0`, `K_jD_j->0`, bounded `p_j`, and `K_j^2||grad p_j||S_jD_j->0`, with `D_j=S_j+|B_j|`; apply local Carleman estimate (2.3). The scope is planar and sequential, not a nodal-length bound.

### Kähler tube transfer (family 359)

Input a smooth strictly plurisubharmonic `ell` whose potential metric is complete and has nonpositive real sectional curvature. On `T_ell={Im w-ell(z)>0}`, set `b=Im w-ell(z)` and `g_T=b^(-1)pi^*g_ell+b^(-2)partial b tensor bar-partial b`, equivalently `g_T=b^(-1)pi^*g_ell+(db^2+(du+d^c ell)^2/4)/b^2`. Completeness follows by controlling `log b`, the base projection, and then `u` along finite-length curves. Adapted normal coordinates compare it with `-log(Im w-c-|z|^2)`, whose real planes have curvature `-1-3 beta^2`; the base contribution is nonpositive, hence `Sec(g_T)<=-1`. No lower curvature or Liouville conclusion is retained.

## Research lead deliberately not adopted

`Path selection and an elliptic inequality on degenerating Ricci-flat trees` (family 351, SHA `a49f3dc92b22b888e356c7d8e02620683b9e1c00ca1b28212cf800dd4d692327`, physical pp. 5--9) remains a research lead only: common holomorphic tail domains and all-order compatible end expansions are not an executable finite-tree interface.

## Source-specific transfer ledger

The generated ledger pins the original URL, SHA-256, physical pages, and exact retained input/procedure/scope boundary for each adoption.

| Source | Physical pages | Scoped adoption |
| --- | --- | --- |
| [Positive scalar curvature and uniform codimension-two width](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Positive-scalar-curvature-and-uniform-codimension-two-width-September-23-2026/paper.pdf) (`f67c30579306bd4dd256ece4d24cdad18ba149930fa97f9ab31a1e6a768cef89`) | 7, 8, 9, 10 | Input A0,P0,epsilon,b0>0; choose k,Y,D_g,T by (2.6)--(2.9), construct g by (2.4), invert X(f,t) in (2.2), and retain exactly the derivative and alternative bounds in (2.1), without geometric stretching. |
| [Spectral scalar curvature and uniform Urysohn width](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Spectral-scalar-curvature-and-uniform-Urysohn-width-October-5-2026/main.pdf) (`1b55879b1d10b0f5b31aa41b220a84f101f44bd01347626293f3fc70c85d917d`) | 6, 7, 8, 10, 11 | Scoped reference. Input the source global prescribed-graph PDE, complete h and scalar comparison; retain D(h,t)=Scal_h+2 Delta_h t-|dt|^2 and h_u=h+du tensor du bookkeeping, not a standalone width algorithm. |
| [A Codimension-One Bound for the Singular Set of a Stationary Integral Varifold](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/varifold-singular-dimension.pdf) (`550b6c1b4bf40bda7958c13378471d3347d592e6d4711e7ef63ccf9e0edad044`) | 4, 5, 6 | For a stationary integral m-varifold with m-1<s<dim_H Sing(V), form sigma_i=L_i^(-s)(eta_{p,L_i})#(H^s restricted to K_Q cap B_{L_i}(p)); retain V_{L_i}->Q|Pi|, sigma_i(B_u)<=C u^s, and c<=sigma_i(B_1)<=C. |
| [Almost-everywhere regularity of stationary integral varifolds](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/paper.pdf) (`f12bd8f9ace9a350d5eba44a7cd57e27b1f955d0751e9c42a2731c43293dec75`) | 7, 8, 9, 10 | With the supplied normal tube, scaled e+lambda error and gamma=l+sup|z_phys|, retain (2.7)--(2.11), including |J_pi-1|<=C(e+lambda) and pi#(J_pi mu)=N vol_S for integer N; weak-type control remains required. |
| [An L² Einstein Gap for Nonnegatively Curved Four-Manifolds](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/einstein-gap.pdf) (`3be17e2ac8ba5f5f2f8de7af7c5d8c47321d3366b0fe012d9b9771b1aaf772ef`) | 5, 6 | For E(f)=integral(a|grad f|^2+P f^2), a>0,P>=0, and the source support estimate, use f_k=min((|f|-2^k)_+,2^k) and b_k=2^(4k)Vol{|f|>2^k} to derive ||f||_4^2<=Cprime E(f). |
| [Positively curved Einstein four-manifolds](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/paper.pdf) (`2eb05d3e177c39f3aaf6084352f658f5afcda414110db8417aec4d565d6ce407`) | 6, 7 | Retain the pointwise Ric=3g oriented Einstein-four block algebra and strict x+y<2 convention only; no global Weyl estimate or classification. |
| [Zero-Plane Rigidity for Einstein Four-Manifolds](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/einstein-boundary.pdf) (`35a3ab1d3d2458b5d78f7b304e94e0c611c06af3f03ab8f9d89c1294683bfb31`) | 5, 6 | Retain the same pointwise block algebra with the nonnegative x+y<=2 equality-face convention only; no zero-plane rigidity conclusion. |
| [Sharp nodal length on smooth surfaces](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Sharp-nodal-length-on-smooth-surfaces-September-23-2026/paper.pdf) (`1301138f44ca53efdafefec7a5f5f817ddf4cd341d46cc66717b61bc499948bf`) | 3, 4, 5 | For planar Delta U_j+K_j^2p_jU_j=0 with S_j->infinity, K_jD_j->0, bounded p_j and K_j^2||grad p_j||S_jD_j->0, diagonalize a countable basis to form V and apply (2.3); retain only planar subharmonicity. |
| [One-sided negative sectional curvature and the holomorphic Liouville property](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/paper.pdf) (`dedbbd2f24f8281c384e8927c78a54fd71d894113da70e5f702b8deb1f5bc046`) | 6, 7, 8, 9 | For complete strictly psh ell with Sec(g_ell)<=0, set b=Im w-ell and g_T=b^(-1)pi^*g_ell+b^(-2)partial b tensor bar-partial b; normal-coordinate comparison yields Sec(g_T)<=-1 only. |
