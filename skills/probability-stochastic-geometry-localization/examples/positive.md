# Positive examples: keep the random object exact

## A124: separate the accepted point-hit identity from the unaccepted concentration branch

Let `S` be compact metric, seed locations have law `θ`, arrival times form a rate-`λ` Poisson process, and every ball grows at speed `v`. If `C(s)` is the first time a fixed point `s` is hit, the exact point-survival law is
\[
\mathbb P_\theta(C(s)>t)=\exp\!\left(-\lambda\int_0^t\theta(B(s,vu))\,du\right).
\]
For `c^*=\max_s\mathbb E_\theta C(s)`, Aldous's Proposition 3.1 gives
\[
\frac{\operatorname{Var}(C)}{(\mathbb E_\theta C)^2}\leq\frac{c^*}{\mathbb E_\theta C}.
\]
R12 accepts the one-point void formula as a restricted G22.03 ingredient. The adjacent variance inequality is stated by the article, but its printed proof has the continuous-drift defect identified by R05; it is outside the accepted method use. R05 separately derives Proposition 3.1 with an age-augmented marked-Poisson martingale. Even using that derived repair, concentration requires proving `c_n^*/E C_n→0` for the exact sequence. See the point-hit card（本机附件：`evidence/referenced/814698e14501132b-UC-EXSRC-G22-POINT-HIT.md`）, concentration card（本机附件：`evidence/referenced/3ba3897b62cd3416-UC-EXSRC-G22-CONCENTRATION.md`）, and R05 neutral audit（本机附件：`evidence/referenced/4a51220eb3168961-review.json`）.

## A125: bound the optimized value without claiming an optimizer

For standardized growth on connected compact `S`, let `cov(r)` be its least radius-`r` covering number. Aldous's Propositions 5.1 and 5.3 give
\[
\chi(S)\leq\min_{r>0}\{r+\operatorname{cov}(r)(1+\log\operatorname{cov}(r))\},\qquad
\chi(S)\geq\sup\{r:\operatorname{cov}(3r)>9r\}.
\]
The upper bound uses seeds uniform on centers of a finite cover; the lower bound uses the positive-probability event that cover time and Poisson seed count are simultaneously small. R12 accepts these compact-space covering-number bounds as a G22.04 use for the variational value `χ(S)`. They do not characterize a minimizing law, prove attainment, or show that Haar attains the minimum; see the covering-number use card（本机附件：`evidence/referenced/b55684fb74d9a431-UC-EXSRC-G22-COVERING-NUMBERS.md`）.

## A124: transfer a restricted J-M cover-time theorem through its exact Poisson mark map

For a compact polygonal `A⊂R²`, let space-time arrivals be a PPP of intensity `ρ` on `A×[0,∞)`, and grow unit-speed balls from their arrival points. At any fixed `t`, the centers arriving by time `t` are PPP of intensity `ρt`, and the elapsed ages `t−s` are iid uniform on `[0,t]`. Thus the time-t covered union has exactly the restricted Boolean model with radii `tY`, `Y~Unif[0,1]`. Penrose–Higgs (2026, Theorem 2.2 and its proof) yields

\[
\Pr\{\pi\rho T_\rho^3-2\log\rho-4\log\log\rho\le\beta\}\to
\exp\!\left[-(4\pi)^{-1/3}|A|e^{-\beta/3}-(2\pi^2)^{-1/3}|\partial A|e^{-\beta/6}\right].
\]

R12 accepts this exact planar k=1 mapping and restricted weak cover-time limit as a G22.03 use. The perimeter term is part of the restricted-model limit; the unrestricted J-M process has a different volume-only limit. The broader source theorem for `d≥3` assumes `∂A∈C²` and `A=\bar A°`, and remains outside the accepted use. This is a weak-limit result for the stated Poisson/Euclidean model, not a Haar or fixed-sample theorem; see the source card（本机附件：`evidence/referenced/17474a78d25fb496-EXSRC-9c442ea403eae4f3-PenroseHiggs2026.md`）.

## G22.01/G22.04: use accepted net and local-minimum methods only under their source gates

Aldous (2022)'s compact-space covering-number estimates for `χ(S)`, Penrose (2023)'s exact Euclidean net/de-Poissonization subinterfaces, and Penrose–Yang (2026)'s compact C² manifold net criterion are accepted only with their stated geometry, local-mass, sample-law, radius, and varying-k conditions. Penrose–Yang (2024) is accepted for the adjusted-radius mean of its exact local-minimum count, not a coverage probability or full rate theorem. PH2026's separate Mecke corner estimate remains a candidate; its smooth-domain net/local-block branch remains outside the accepted planar k=1 use because of the isolated Eq. (29)/Eq. (71) mark-cutoff issue. None supplies a generic compact entropy estimate, a SIRSN stabilization tail, or an Efron–Stein bound. See the Penrose 2023 net card（本机附件：`evidence/referenced/0f12a631303c9a45-UC-EXSRC-G22-PENROSE2023-NETS-DEPOISSON.md`）, manifold net card（本机附件：`evidence/referenced/2a3aeb03dcfa51e3-UC-EXSRC-G22-PENROSEYANG2026-MANIFOLD-BOUNDARY.md`）, Penrose–Yang 2024 card（本机附件：`evidence/referenced/4899db8bbbaa8995-UC-EXSRC-G22-HALL-JANSON-RATE.md`）, and Aldous covering-number card（本机附件：`evidence/referenced/b55684fb74d9a431-UC-EXSRC-G22-COVERING-NUMBERS.md`）.

## A136: derive the one-route marginal, then stop at the actual gap

Let `U` be uniform on the unit disk and let $\Delta_{\mathrm{route}}=\mathbb E\,\mathrm{len}\,r(0,e_1)<\infty$ be the mean route length between points at unit separation in an isotropic scale-invariant network. The radial density of `|U|` is `2r` on `[0,1]`, so
\[
E|U|=\int_0^1 r(2r)\,dr=\frac23,
\qquad E\,\mathrm{len}\,r(0,U)=\frac23\Delta_{\mathrm{route}}.
\]
This is a valid finite marginal. The L12 SymPy check at `sirsn_marginal_mean_check.py`（本机附件：`evidence/calculations/sirsn_marginal_mean_check.py`） with `output`（本机附件：`evidence/calculations/sirsn_marginal_mean_check.out.txt`） verifies the exact integral. It does not bound `E sup_i len r(0,U_i)`: all endpoints use the same random network and their route lengths may be strongly dependent. Aldous's source states that maximum as Open Problem 34.

## A137: use Mecke only for a Poisson count identity

For a nonnegative measurable score `f(x,η)`, Last–Penrose Theorem 4.1 gives
\[
E\sum_{x\in\eta}f(x,\eta)=\int E f(x,\eta+\delta_x)\,\lambda(dx)
\]
for a Poisson process `η` with s-finite intensity `λ`. This can justify a Poisson-input expectation or insertion calculation when the score and process match. To conclude a fixed-k span asymptotic, separately couple `η` with k uniform points in the same area-k window, bound the add/remove-point effect on the span, control routes crossing the boundary, and prove uniform integrability. The Mecke identity supplies none of those transfer estimates.


## Accepted discrete cover and concentration subinterfaces; no growing-ball transfer

R12 accepts three separate finite-model tools. Aldous (1991) proves the iid random-set residual criterion using `T=S\range(X_1,…,X_{C−1})`, the points still uncovered before the final coupon. Falgas-Ravry–Larsson–Markström (2020) use `B=C_T\C_{T−1}=V\C_{T−1}`, exactly that same terminal residual in coupon notation, and give coupon-type-specific Poisson occupancy moments. Aldous (2016) proves `Var(T)≤D ET` for a finite-state pure-jump CTMC when the finite mean hitting potential is nonincreasing on every possible transition; handle a start already in the target separately. The two iid-coupon formulations use the same residual set, while the finite-state CTMC has a different set of hypotheses. None provides an iid-block or finite-state representation for an age-dependent growing-ball process.

R12 also accepts Gieringer–Last's Boolean occupied-measure upper-tail bound only under its grain-mass/exponential-integrability hypotheses. Penrose–Yang (2024) is admitted for the exact adjusted-radius mean of its local-minimum count; its coverage probability and full-rate branches are outside this admission. Penrose (2023)'s uniform-iid fixed-k CDF bridge, Penrose–Yang (2026)'s compact-C² manifold net criterion, and Falgas-Ravry–Larsson–Markström's source-specific coupon criteria remain tied to their exact sample design, local-mass/covering, window, boundary, and radius assumptions. None proves the assigned Haar claim or growing-ball concentration.


## G22.02: a self-bounding Poisson count

Let `η` be a unit-intensity Poisson process on `[0,1]`, and set `F=η([0,1])`. For `x∈[0,1]`, insertion adds one, so `D_xF=1`; outside this interval the difference is zero. Thus the first term of `V+` vanishes, and the deletion term contributes one for each atom, giving `V+=F`. The nonnegative self-bounding condition holds with `α=1` and `c=1`, while `EF=1`. The accepted Corollary 3.6 interface gives

`P(F≥5) ≤ exp(−(√5−1)²/2) = 0.4658311626…`.

The exact Poisson tail is `P(Pois(1)≥5)=0.0036598468…`. The saved local Python run is `poisson_count_check.py`（本机附件：`evidence/calculations/poisson_count_check.py`） with its `stdout`（本机附件：`evidence/calculations/poisson_count_check.out.txt`） and `run metadata`（本机附件：`evidence/calculations/poisson_count_check_run.json`）. This numerical comparison illustrates the inequality; the source proof and the independent bounded-entropy closure establish the general result. The example uses a diffuse standard-Borel intensity and the v1 Corollary 3.6 numbering.
