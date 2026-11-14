# Method routing and proof checks

## 1. Define the endpoint object

Write the target before choosing a theorem:

- scalar coordinate: \(R_j f\), with scalar absolute value;
- vector: \((R_1f,\ldots,R_nf)\), with the Euclidean norm;
- weak norm: \(\sup_{\lambda>0}\lambda\,\mu\{|Tf|>\lambda\}\), recording whether a refinement uses `>` or `≥`;
- input field: real or complex;
- domain and measure: \(\mathbb R^n\), normalized \(\mathbb T^n\), or a line/circle times a transverse space;
- dimension dependence and whether an asserted constant is only an upper bound or is claimed optimal.

Do not infer a vector norm estimate from a scalar component estimate or infer a sharp scalar constant from a vector upper bound. The pointwise relation \(|R_j f|\le |Rf|\) transfers an already proved vector bound to each coordinate with the same upper constant; it does not transfer sharpness in either direction.

## 2. Choose a route supported by the sources

### Finite positive-atom reduction (CZ-03)

For an odd homogeneous mean-zero Calderón–Zygmund kernel satisfying the stated angular continuity condition, Theorem 4.1 is printed as a scalar weak-distribution reduction to a regular term plus finite positive atomic measures with total mass at most `16 ||f||_1`. Its proof chain is: Whitney decomposition of `{f>lambda}`; L2 estimate for the good part; replace each bad cube by a center atom of equal mass; use zero-mass cancellation outside `n r_k`; account for the annulus and pass to the finite-sum limit. **Check the L2 norm:** Lemma 3.4 gives `||T||_(2->2) <= C2 ||Omega||_1`, so the first squared Chebyshev step contributes `4 C2^2 ||Omega||_1^2 lambda^-1 ||f||_1`. The next finite-sum error estimate must likewise carry `16 C2^2 ||Omega||_1^2 lambda^-2 ||b-b^(N)||_2^2`; with this corrected fixed-kernel factor it still tends to zero by the source's dominated-convergence argument. Both displayed p. 11 estimates omit the squared angular-norm dependence, and Theorem 4.1's printed proof therefore does not establish its stated linear dependence on `||Omega||_1` for variable general-kernel norm. For general kernels, use this reduction architecture only with an independently certified L2 operator norm `M2(T)` or an independently completed norm argument. For Riesz coordinates, the fixed angular mass `||Omega||_1=2/pi` lets the squared factors be absorbed into absolute constants, so the scalar Riesz reduction remains supported. Its finite-atom Riesz bound is `O(log n)`, not dimension-free. The theorem statement also does not restate the oddness used by Lemma 3.4; keep that proof-level condition visible.

### Vector obstacle decomposition (CZ-04)

For real data on \(\mathbb R^n\), the source proves the fractional obstacle decomposition for nonnegative \(f\in L^1\cap L^2\), level \(\lambda>0\), and (0<\alpha<2). At \(\alpha=1\), apply it to the positive and negative parts, use \(Rf=R\mu+\nabla u\), vanishing gradient off the positivity set, and vector (L^2) isometry for the bounded remainder to obtain vector weak-(1,1) constant 2. The paper's printed vector theorem omits an explicit real/complex qualifier, but the proof uses positive/negative parts and establishes the real case; do not claim a complex extension from this source alone.

### Scalar coordinate and product semigroup Bellman route (CZ-05)

For real inputs and a scalar horizontal derivative, the source claims the exact weak-(1,1) constant \(K_D=\pi^2/(8\beta(2))\). Its product extension requires a nonzero standard sigma-finite transverse space, (L\ge0) self-adjoint, and (e^{-tL}) symmetric sub-Markov, on a line or circle product. The operator is \(-\partial_x(-\partial_x^2+L)^{-1/2}\); there is no derivative in the transverse variables. The proof route is:

1. Build a superharmonic majorant from harmonic extension of `|x|` in a strip and derive the increasing capped integral function `Phi`. In the circle proof, compose the superharmonic `U` with the analytic map and use its superharmonic mean-value upper bound. The later finite-space proof instead uses subharmonicity of a different function, `Re(Psi_tilde)`, so keep the signs and objects separate.
2. Prove the harmonic-conjugate integral inequality on the circle.
3. On finite reversible transverse spaces, use analyticity and \(\Re F'>0\) to prove positivity of weighted Fourier partial sums; subordination represents the product-generator correction.
4. Remove the strip constraint by vertical regularization, a penalized maximization, subgradient Euler identities, a localized cutoff test, and the sub-Markov Dirichlet form.
5. Pass from finite spaces to general (Y) through compression of (e^{-rL}), (L^2) spectral convergence, and Fatou; extend to (L^1) through weak-type convergence in measure.
6. Establish sharpness by high horizontal frequencies approximating the one-dimensional Hilbert transform.

The same paper claims the stronger \(\Phi\)-integral and truncated second-moment estimates. Its scalar identities can be checked computationally; numerical checks do not verify the operator proof.

## 3. Stop before transferring

Do not apply these sources without additional justification when the target is complex-valued, the requested operator is a vector norm with a sharp constant, the numerator differentiates in transverse variables, the semigroup is not symmetric/sub-Markov, the transverse space is zero or fails standard sigma-finiteness, or a dimension-free estimate is inferred from a finite-atom reduction whose atom term has not been controlled.

For each proof, track every density extension, (L^2) realization, threshold rescaling, normalization of torus measure, and use of Fatou or convergence in measure. Consult the source cards for exact physical pages and the remaining independent-review flags.

## 4. Finite measures and martingale transforms (AEP-006)

For a finite bounded Radon measure on \(\mathbb R^n\), write \(\mu=f\,dx+\nu\) with \(\nu\) singular. Varopoulos studies the Euclidean norm distribution of the classical Riesz conjugate system and proves
\[
N(\lambda):=\lambda\,m\left\{x:\left(\sum_{j=1}^n|R_j\mu(x)|^2\right)^{1/2}>\lambda\right\},\qquad
\liminf_{\lambda\to\infty}N(\lambda)\ge k_n\|\nu\|,
\]
with a positive dimension-dependent constant not explicitly computed. The source's underlined `lim` on its main theorem, Poisson-maximal lemma, and closing proof line means `liminf`; its equation (1.3) separately uses overlined `lim` (`limsup`) for an upper-tail estimate. The proof first lower-bounds the Poisson maximal tail by a dyadic Calderón–Zygmund selection that captures the singular mass; a subharmonic power of the full harmonic conjugate vector is then majorized by the Poisson extension of its boundary values, and a Hardy–Littlewood maximal estimate transfers the lower tail to the Riesz system.

The additional all-threshold comparison is narrower: it assumes a positive singular measure and uses \(\sum_j |R_j\nu|\), not the Euclidean norm distribution used in the main theorem. The one-dimensional exact identities cited in the article have separate hypotheses (Jones's asymptotic singular-part formula and Loomis's identity for positive finite atomic measures); they are not higher-dimensional constants. For the martingale section, the equivalence between uniform integrability and terminal weak-tail conditions requires the source's bounded, relatively orthonormal finite-increment system, an \(L^1\)-bounded martingale, and the no-common-real-eigenvector condition on the transform matrices. The maximal-transform criterion is only sufficient and additionally requires matrices \(P_j\) with \(\sum_jP_jM_j=I\). Do not generalize either statement to arbitrary martingales or Calderón–Zygmund kernels.

## 5. Sharp weak-\(L^p\) coordinate estimates (AEP-007)

For real-valued scalar input and one Euclidean Riesz coordinate \(R_j\) at a time, Osękowski's Theorem 1.1 gives, for \(1<p<\infty\), the sharp positive-part estimate with constant
\[
C_p^+=\frac{2^{1-1/p}}{\pi}\int_0^\infty\frac{r^{-1/p}}{\sqrt{1+r^2}}\,dr,
\]
and the full absolute-value estimate with constant \(2C_p^+\), not claimed sharp. These constants are for the paper's rearrangement quantity \(\sup_{r>0}r^{1/p}f^{**}(r)\), not the distribution quasi-norm with an identical sharp constant. The proof route is: a sharp convex-excess martingale inequality for orthogonal differentially subordinate martingales; the Gundy–Varopoulos Brownian representation of a single Riesz coordinate; an excess-integral estimate; then rearrangement, duality, and integration by parts. The theorem begins at \(p>1\): its separate endpoint profile assumes \(0\le f\le1\) and is not a universal weak-\(L^1\) operator norm. Its sphere results concern one directional transform and claim sharpness only on \(S^1\). None of these scalar estimates determines a sharp vector norm or permits complex-input transfer.

For the martingale theorem, the printed proof on PDF p. 311 sets \(U_\lambda(X_0,0)=U_\lambda(\|X\|_1,0)\) even though \(X_0\) may be random. Do not export that pointwise equality. The source's Lemma 2.3(ii) gives concavity in the open strip, and its continuous extension to the closed strip makes \(x\mapsto U_\lambda(x,0)\) concave on \([0,1]\); the required comparison is the proof-supported step \(\mathbb E U_\lambda(X_0,0)\le U_\lambda(\mathbb E X_0,0)=U_\lambda(\|X\|_1,0)\). The B2 card records this repair and its mathematical conditions. On PDF p. 317, the printed lower-boundary line says \(m\to\infty\), immediately before taking \(m\to0\); treat it as a typo for \(m\downarrow0\), as documented in the card.

The AEP-006 and AEP-007 routes are specific to the classical Riesz system and martingale/Brownian representations in their source hypotheses. They do not fill the general-kernel L2-factor gap recorded for CZ-03.


## 6. Standard Calderón–Zygmund weak-(1,1) construction (AEP-009)

For a scalar-output operator `T` on `R^n`, AEP-009 Theorem 1 assumes the standard kernel size bound, Hölder smoothness in both variables away from the diagonal, `L²` boundedness, and the off-support integral representation. Its proof decomposes `{f>lambda}` into Whitney cubes, estimates the good part by `L²` Chebyshev, and constructs successively centered sets `E_i` with `|E_i|=lambda^(-1) integral_{Q_i} f`. The differences `b_i-lambda 1_{E_i}` have zero mass. Kernel smoothness gives exterior `L¹` control, while doubling controls the dilated exceptional union; an `L²` bound controls the remaining `T 1_E` term. The finite construction is passed to the countable decomposition as in the paper. This yields an implicit weak-(1,1) constant depending on the operator and dimension. It is not a sharp-constant theorem.

The same source's Theorem 2 is a separate source-stated weighted result for `w in A_p`, `1<p<infinity`, with level sets measured by `w(x) dx` and a bound proportional to `[w]_{A_p} max{p, log(e+[w]_{A_p})}`. Its proof on p. 5 uses an arbitrary-set affine-dilation estimate that does not follow from doubling (which controls centered cubes); quarantine that proof/use until the needed weighted estimate is separately established. The unweighted Lebesgue proof is not affected. Do not call the weighted dependence sharp. See the [AEP-009 card](../evidence/W25/cards/AEP-009.md).

## 7. Martingale log and event estimates (AEP-016)

Theorem 2.2 applies to continuous `R^d`-valued martingales with differential subordination and matrix process `dM_t=V_t M_t dt`, where `V_t` is adapted, continuous, symmetric, and nonpositive. The `p>1` bound is `p*−1`, independent of dimension; its proof uses a matrix drift inequality. A pointwise scalar covariance ratio does not replace that operator condition.

Theorems 2.5–2.6 give logarithmic and event-integral inequalities for this martingale class. The event estimate has `1<p<infinity`; the printed p<2 proof of Lemma 2.7 has a global-minimum gap, and the card records a separate W25 analytic supplement that R01 accepted. Attribute the repair to that supplement, not to the source proof. Taking `E={|Y_t|>lambda}` yields a distribution weak-Lp bound for the martingale output, not a weak-(1,1) operator theorem. For vector log Theorems 3.3, 3.7, and 3.9, the printed `K>2/pi` conflicts with a remainder `1/(K−1)`; restrict use to `K>1`. Scalar directional estimates use `L(K)` and keep `K>2/pi`. The group, sphere, and finite-dimensional Gauss applications retain their own transform definitions, geometric hypotheses, and vector/directional norms. On manifolds and infinite-dimensional Gauss space, the authors say the weak-(1,1) question was open to them. Consult the [AEP-016 card](../evidence/W25/cards/AEP-016.md).

## 8. General diffusion multipliers and generalized Riesz transforms (AEP-017)

The extension/multiplier route requires the paper's symmetric locally subelliptic diffusion setup, essential self-adjointness, complete intrinsic metric and nonexplosion, a nonpositive potential where used, and an independent killed vertical diffusion satisfying its scale/hitting assumptions. Its reusable method takes: (i) a base diffusion and independent vertical killed diffusion with those hypotheses, (ii) a smooth/dense input and multiplier growth/decay assumptions, and (iii) the hitting transform `K(y,lambda)` and Green kernel. It constructs `U_f=K(y,−L)f` solving `(L+B)U_f=0`, then represents `W=Phi(−L)` by a conditional expectation of a stopped potential-weighted vertical stochastic integral. The source proves the identity by pairing with a smooth test function, Itô isometry, Green occupation, self-adjoint spectral calculus, and a starting-height limit. To transfer an inequality, independently match the target multiplier and certify the stochastic-integrand subordination/matrix norm and the conditional-expectation norm.

The paper's operator conclusions are strong-Lp for `1<p<infinity`; a strong bound implies a distribution estimate only at that same p by Chebyshev, not weak-(1,1). R01 accepted AEP-017 as quota-eligible because this stopped-extension representation is a reusable method, not because its p>1 results prove an endpoint. Quarantine Theorem 4.11's generic linear-`C` use (the recorded normalized-circle example contradicts it) and the all-index second-order diagonal reading; retain `i!=j` or an independent matrix-norm bound and the separate first-order/Remark 4.7 scopes. See the [AEP-017 card](../evidence/W25/cards/AEP-017.md).


## 9. Bellman/Bochner Riesz estimate on weighted manifolds (AEP-018)

For a complete weighted manifold with weighted Ricci lower bound `Ric_phi≥−a²g`, use the source's weighted Hodge/Bochner identity and Bellman Hessian only with the exact smoothness, real-data, and range/domain hypotheses in the card. Theorem 3 gives the bilinear estimate with `3(p*−1)`; Corollary 4 yields a nonsharp vector Riesz strong-Lp upper bound `12(p*−1)` on the source's specified closure of the range. The proof regularizes the Bellman function, uses curvature to cancel the Bochner term, and passes through distance cutoffs, integration by parts, Fatou, scaling, and optimization. It does not identify the sharp C207 vector constant or give weak-(1,1). R01 accepted the source at mother integration; the card is frozen.

## 10. One-dimensional Jacobi and Hardy endpoint (AEP-019)

Bakry's one-dimensional Jacobi generator for `alpha,beta≥0` has a spectral basis and commutator ` [L,H]=hH`. On mean-zero polynomials, Theorem 2 compares `||Cf||_p` and `||Hf||_p` for `1<p<infinity`; the martingale proof uses an independent Brownian coordinate with quadratic variation `2t`, harmonic/Poisson extensions, bracket estimates, and duality. The duality reverse step is expressly one-dimensional. Theorem 4 extends the Jacobi transform from source `H¹` to `L¹`; it does not state `L¹→L¹`, weak-(1,1), or `H¹→H¹`. Do not transfer it to the Euclidean vector Riesz operator. R01 accepted the source at mother integration; the card is frozen.

## 11. Intrinsic Gamma2 semigroup method (AEP-020)

For a symmetric Markov semigroup and the source's bounded dense test algebra/domain conditions, pointwise `Gamma2≥0` yields two differently directed facts: the diffusion-only Theorem 2 gives `||Cf||_p≤c_p||sqrt(Gamma(f))||_p` for `1<p<infinity`; Theorem 7 gives `||sqrt(Gamma(f))||_p≤c_p||Cf||_p` for general symmetric semigroups only when `p>2` and `f` lies in the source good core. The low-p dual consequence is the first direction, which after `f=Vg` is a lower Riesz-norm bound. All-p equivalence needs the extra §4.3 diffusion representation with common `h`, preserving `H_i`, commutation and the source's no-invariant-component conditions.

The official 1986 corrigendum corrects row 3/column 4 of Proposition 1's proof matrix: replace `(f,f)(g,g)` by `(f,f)(f,g)`. The original displayed coefficient 2 remains. R01's independent local Hessian expansion verifies `M34=2 Gamma(f,f) Gamma(f,g)` with exact residual zero; this local reviewer check is distinct from the source/erratum and does not prove the general Gamma2 argument. Proposition 1 feeds the diffusion-only Theorem 2 proof; the correction changes no theorem hypotheses, statements, or constants. The correction's two physical pages are same-work support, not another source. R01 accepted the source at mother integration; the card is frozen.


## 12. Manifold good-λ criterion (AEP-023)

Apply Theorem 2.1 only when the input is `f∈L²`, the estimates hold for every base point and every ball containing it, and the separate target-space condition `Tf∈L^p` whenever `f∈L^p` is available. For its Riesz application, carry the approximants `T_ε`, their individual `L^p` bounds, convergence in `L²`, and the criterion constants uniform in `ε`; only then pass to the limiting transform. The conclusion is strong type for `2<p<p0`, under the manifold doubling/Poincaré and heat-gradient hypotheses. This is not a weak-endpoint argument. See [AEP-023](../evidence/W25/cards/AEP-023.md).

## 13. Schrödinger square-root weak estimate (AEP-024)

Keep the typed map: `f∈C_0^∞(R^n)` is sent to `H^(1/2)f`, and its distribution is controlled by `||∇f||_1+||V^(1/2)f||_1` for a nonnegative `V∈A_∞`. The proof truncates `V`, uses a Whitney decomposition of the Sobolev-energy level set, controls the good term by the quadratic-form identity, splits bad terms into short-time Gaussian-off-diagonal and long-time square-function pieces, and then passes through the truncation limits. This method does not bound a scalar Riesz coordinate from an arbitrary `L¹` input. See [AEP-024](../evidence/W25/cards/AEP-024.md).

## 14. Local-oscillation sparse domination (AEP-041)

For the reusable sparse route, require an `L²`-bounded Euclidean Calderón–Zygmund operator with the stated size and smoothness bounds, plus the classical weak-`(1,1)` estimate used inside Proposition 2.3. The paper prints an origin-centered annulus `ε<|y|<ν` for `K(x,y)`; because this need not exclude `y=x`, quarantine that literal notation and state explicitly that the tool uses the standard centered truncation `ε<|x-y|<ν`. Its output is sparse domination and then a weighted `A₂` strong-`L²` bound, not a new weak-`(1,1)` proof. In the complexity series, `m=0` is the sparse-average term directly; apply the `c(n)m` estimate only for integers `m≥1`. See [AEP-041](../evidence/W25/cards/AEP-041.md).

## 15. Isolated C208 endpoint-method analogies (AEP-EXT-003/005/015)

These are source-specific auxiliary templates only; they do not establish the formal C207 vector-Lp target or solve the isolated C208 scalar-Riesz question. For AEP-EXT-003, stay within the one-dimensional multiplier classes in the paper; Proposition 5.1 uses `supp(m_I)⊂I`, `ξ_I∈I`, uniform order-zero bounds, and compact-set-to-same-set Orlicz mapping with `C_K`. For AEP-EXT-005, require polynomial growth, the stated kernel regularity and uniformly L2-bounded truncations; keep `β>α^n` for large cubes separate from `β>α^d` for small cubes, and use a localized limit or countable annular finite-overlap argument for unbounded `Ω`. These conditions and finite-family limits do not produce a dimension-free C208 constant. See the [AEP-EXT-003 card](../evidence/W25/cards/AEP-EXT-003.md) and [AEP-EXT-005 card](../evidence/W25/cards/AEP-EXT-005.md).

AEP-EXT-015 is a separate normalized Dini-CZO result: Theorem 1.6 needs its Young-function summability condition; Theorem 1.11 is for intrinsic square functions and includes `p=1,w∈A_1`, while the `p<2` proof is imported. Keep the printed p.4 cone/dilation, p.5 Dini monotonicity, and p.6 reverse-Hölder exponent defects explicit. If a conventional operational definition and separate reciprocal-order reverse-Hölder input are used, mark these as external/conditional inputs rather than corrections proved by the source. Its bounds carry structural constants and give no dimension-free C208 Riesz conclusion. See the [AEP-EXT-015 card](../evidence/W25/cards/AEP-EXT-015.md). All listed papers are included in the R01-approved 30-source inventory; source-specific proof and input limits below remain in force.

## 16. Rearrangement and near-p=1 extrapolation (AEP-EXT-001/002/004)

Use AEP-EXT-001 for the one-dimensional Hilbert/conjugate rearrangement identities and the paper’s odd homogeneous kernel class. Keep its Theorem 3 coefficient ||Ω|| distinct from the ||Ω||/2 indicator lemma, use sin(s/4) in Theorem 4, and do not multiply the printed Ap by an extra p′ Hardy factor. These are source-specific distribution/strong-Lp facts, not a general vector-Riesz endpoint.

Yano’s AEP-EXT-002 requires real input on a finite interval, finite-measure output, the stated countable subadditivity/sign symmetry, and an Lp growth bound of order (p−1)^−k for 1<p<2. It yields an L log^k L to L1-type conclusion with an additive finite-measure term, not a weak distribution estimate. The footnote’s Young comparison does not control the weighted remainder: use the independent completion in the card and handle the two lowest dyadic levels separately.

Bakas’s AEP-EXT-004 is a different analytic Hardy model on the one-dimensional torus. The operator is defined on measurable functions and satisfies modulus subadditivity, |T(f+g)|≤|Tf|+|Tg|, and complex homogeneity, |T(αf)|=|α||Tf|. Its growth hypothesis applies to every g∈H^p for every 1<p≤2, with ||Tg||_p≤C₀(p−1)^−r after normalization. Do not narrow that operator or growth domain to polynomials: the proof uses analytic H∞ pieces G_λf that need not be trigonometric polynomials. Theorem 1 concludes only for analytic trigonometric polynomial f. Extension to the full Hardy–Orlicz space additionally requires the pointwise-difference condition and density/unique extension in the card. Do not transfer its endpoint exponent to unrestricted Lp or a Euclidean Riesz coordinate.

## 17. Hardy-space and operator-adapted endpoint methods (AEP-EXT-006/014)

The AEP-EXT-006 weak factorization is an H1 method for the stated multilinear Riesz-transform atoms. Verify the Hölder/size assumptions and the partial-adjoint denominator lower bound for every atom configuration before division; do not promote the factorization into a scalar Riesz weak-(1,1) theorem.

For AEP-EXT-014, the self-adjoint Gaussian route requires sublinear T bounded on L2 and H_L^p to Lp for one 0<p<1, with the source doubling/heat assumptions and atom parameter M>n/2(1/p−1/2). The self-adjoint Theorem 1.6 chain is separate from the general analytic-semigroup route. Proposition 3.8’s printed non-self-adjoint formula has an explicit scalar counterexample; Theorem 3.4’s downstream proof is not source-verified until its molecule estimates are independently repaired.

## 18. Martingale, multiplier, and sparse method boundaries (AEP-EXT-009/010/011/021/044/045)

For AEP-EXT-009, require the source’s submartingale decomposition, X0=0, orthogonality and strong differential subordination for the maximal theorem; the smooth harmonic-measure theorem has its separate real C2, subharmonic, gradient/Laplacian, and bounded-domain hypotheses. Attribute the printed (3.2) sign and boundary-starting sharpness exit as source defects. The int(J−1) stopped path and two-budget selector are independent reader derivations; the source does not settle smooth-function sharpness.

AEP-EXT-010 also distinguishes its continuous real martingale maximal event from the nonmaximal harmonic-measure norm. Keep the open connected domain and gradient constraints; its source’s closed-strip sharpness notation is not literally an admissible open domain. The separately derived open-strip example has its own boundary-limit convention.

AEP-EXT-011 is restricted to its Lévy-symbol class and p>1. The structured vector weak-(p,p) theorem is not a vector Riesz strong-Lp theorem. Preserve the p. 748 versus Eq. (3.6) measure-coefficient/weak-norm exponent discrepancy; do not silently repair Theorem 1.2.

AEP-021’s product-cone and smooth homogeneous assumptions remain part of its martingale/second-order Riesz results. Do not extend arbitrary axis-value representatives from the proof. AEP-044’s literal minimum-exponent statement is contradicted by the recorded legal p=3 witness; isolate that theorem statement without generalizing the counterexample to the whole article. AEP-045 is a real scalar Haar/martingale positive-contraction result with fixed initial coefficient 1 and a one-sided event, not a Riesz/vector theorem.

## 19. Survey and weighted dyadic method boundary (AEP-026/040)

AEP-026 is a survey: distinguish its martingale statements and proof outlines from cited primary proofs. Its sharp martingale estimates are martingale inputs; the separate Brownian stochastic-integral representation and conditional-expectation projection yield strong-Lp estimates for Riesz coordinates. Since conditional expectation need not preserve weak type, martingale weak-L1 does not transfer through that projection to a Riesz weak-(1,1) bound. At the unnumbered projection discussion and Problem 7 (physical p. 37; printed p. 35), the source asks for the optimal coefficient C_p in \(\lambda^p\,\operatorname{Leb}\{x\in\mathbb R^n:|R_j f(x)|>\lambda\}\le C_p\|f\|_p^p\) for the scalar Euclidean coordinate R_j, 1≤p<∞; the p=1 discussion says a dimension-independent constant is unknown and cites a C log(n) upper estimate. Remark 3.4.2 and Problem 8 (physical p. 38; printed p. 36) ask for weak-(1,1) of the Gaussian vector transform \(R_g f=\nabla(-L)^{-1/2}f\) on \(\mathbb R^n\) with Gaussian measure. Keep these two questions separate; neither is C207, the vector strong-Lp best-constant problem. A reusable Bellman verification is limited to a smooth/localized majorant U≥V, V(x,y)=|y|^p−c^p|x|^p, with E U(X_0,Y_0)≤0, nonpositive Itô drift on the allowed quadratic-variation directions, and justified localization, expectation, and limit steps; only then does the argument yield the moment bound with coefficient c^p. The survey defers the full Itô/approximation proof details to primary references [23,24], which are not certified here as fully checked.

AEP-040 proves a sharp weighted A2 strong-L2 estimate for standard Calderón-Zygmund operators. Its Proposition 5.1 weak-(1,1) estimate is for each bounded dyadic shift with O(u) dependence. The paper explicitly does not use its separate weak-L2 reduction; do not report a weak-L1 theorem for T or a dimension-free scalar-Riesz endpoint.

## 20. Problem boundary after method selection

After selecting any method, write the residual interface explicitly. C207 is the vector strong-Lp best-constant problem for 1<p<infinity; scalar weak-Lp, vector weak-(1,1), weighted strong-L2, and martingale bounds do not solve it. C208 is isolated; no source here establishes a dimension-free scalar-coordinate weak-(1,1) estimate. The [30-source guide](sources.md) records the boundary for every paper, and the exact source decision/card pair is in evidence/W25 (historical project reference; target is outside the approved runtime scope).

