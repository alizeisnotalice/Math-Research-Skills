# 概率、随机过程与统计

按原件哈希区分。每条核查保留本机物理页与对应来源。

## A Borodin–Okounkov–Geronimo–Case Identity for Tilted Toeplitz Minors

- 原件 f8b1c3386d49e61e767ae969a02131b509a42af276151ff04492b8be75a79214。Local arXiv:2605.24976v1, 34 pages, dated 24 May 2026。物理页 1, 3, 7, 14。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2605.24976v1 (24 May 2026), Leonid Petrov; no journal version identified on the checked primary record。
- 邻近材料。The local v1 and arXiv record match. Under zero winding, log(phi) in C^alpha with alpha>1/2, bounded analytic row/column tilts, and invertible Gram matrix, Theorem 4.4 gives a Fredholm-determinantal identity; its proof depends internally on the trace-class Grassmannian identity. Here “tilt” is an oblique Hardy-space/Toeplitz-minor deformation。
- 结论位置。Local PDF p. 1 metadata; p. 3 standing Hardy-space/trace-class and Gram-invertibility assumptions; p. 7 proves the Grassmannian Jacobi identity; p. 14 states Theorem 4.4 and derives it from Lemma 4.3 plus Theorem 3.1。
- 适用范围。This is not exponential change of measure and has no probabilistic saddlepoint or tail approximation step. Its cited recent TASEP preprints are contextual, not checked substitutes for the theorem’s internal hypotheses。
- 相关技能。[math-h02-exponential-tilting-saddlepoint](../../../../math-h02-exponential-tilting-saddlepoint/SKILL.md)
- 其余依赖。No active H02 claim depends on this source. Any future Toeplitz skill must independently check the stated trace-class, analyticity, and Gram-invertibility hypotheses。
- [主来源 1](https://arxiv.org/abs/2605.24976)

## A debiased Bernoulli factory and unbiased estimation of a probability

- 原件 85bc6a2ec6b57416f3b492bb6d45d5fe0cd5353061f77f95ac2a946cb95bca18。Local 10-page manuscript dated 2 September 2026, SHA-256 85bc6a2ec6b57416f3b492bb6d45d5fe0cd5353061f77f95ac2a946cb95bca18; it has no arXiv identifier printed on p.1。物理页 1, 2, 3, 4, 5, 6。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2510.01941v2 (revised 1 September 2026); arXiv reports v1 2 October 2025 and v2 1 September 2026。
- 已有技能。The local manuscript and official arXiv v2 metadata identify the same four authors/title and ten-page version. Its Theorem 2 is a concrete conditional factory: for f in C^rho, rho>3, supplied nested Bernstein envelopes, 1<lambda<(rho-1)/2 and sufficiently large k, the randomized telescoping estimator is unbiased and [0,1]-valued. This matches the active skill only as a conditional coefficient interface。
- 结论位置。Local pp.1–2 specify the iid x-coin input/output contract; p.3 states imported Theorem 1 (HNP11 Theorem 8); p.4 states Theorem 2; pp.4–6 prove unbiasedness, nonnegativity and the upper bound。
- 适用范围。The proof explicitly imports HNP11 Theorem 8 for the envelope sequences and rate (local p.3); the HNP existence and rate proof was subsequently verified directly and wired into the active skill. Nor does this paper make arbitrary smooth f usable without the concrete envelope, buffer and remainder data required by the skill。
- 相关技能。[probability-bernoulli-factory](../../../../probability-bernoulli-factory/SKILL.md)
- 其余依赖。应用时给出目标函数的实际上下包络系数、余项与启动缓冲。已有的 HNP 存在性依赖见技能内直接核验。
- 已采用构件。有限支撑截断的账本已实现。HNP Theorem 8 的包络存在与统一误差率已另行核对，应用仍需明确的系数阵列、余项和起点。[使用说明](../../../../probability-bernoulli-factory/references/finite_debiased_ledger.md)
- [主来源 1](https://arxiv.org/abs/2510.01941) · [主来源 2](https://arxiv.org/abs/0808.1936v3)

## A nonuniform local limit theorem for Poisson binomial random variables via Stein’s method

- 原件 bcce7e1d8856d6fe309f3218cd50477d928db08813abecce6ec465f6c4ccbb42。Local published PDF: Journal of Inequalities and Applications 2024:10, 18 physical pages, SHA-256 bcce7e1d8856d6fe309f3218cd50477d928db08813abecce6ec465f6c4ccbb42。物理页 1, 3, 5, 6。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Journal of Inequalities and Applications, volume 2024, article 10 (published 24 January 2024), DOI 10.1186/s13660-024-03087-4。
- 待核。The publisher page and local p.3 agree that Theorem 1.1 claims the nonuniform normal point-mass estimate for independent Bernoulli summands with pi in (0,1) and sigma^2>=1. The active G05 skill correctly keeps this source-proof branch held rather than using it。
- 结论位置。Local p.1 identifies the published article and DOI; p.3 states Theorem 1.1; pp.5–6 give the standardized lattice/Stein setup and auxiliary bounds。
- 适用范围。Identity and theorem transcription are recovered, but this review did not repair the known auxiliary high-moment/square-exponential proof failures recorded by the skill. Thus the source still cannot justify a reusable approximation bound。
- 相关技能。[probability-bernoulli-extremal-orders](../../../../probability-bernoulli-extremal-orders/SKILL.md)
- 其余依赖。A separately valid proof of the auxiliary moment and square-exponential estimates (or an independently verified replacement proof of Theorem 1.1) is required。
- [主来源 1](https://journalofinequalitiesandapplications.springeropen.com/articles/10.1186/s13660-024-03087-4)

## A Note on Talagrand's Variance Bound in Terms of Influences

- 原件 c9eb1c702efb826eef81db7f118c01e4c83b7a0247ab45eca7856477c219ff86。arXiv:1007.0677v1, submitted 5 Jul 2010。物理页 1, 2, 4, 8。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:1007.0677v3, last revised 26 Jul 2011; no journal version was identified on the checked primary record。
- 邻近材料。Raw SHA and 10 physical pages match input. The checked arXiv record resolves the earlier metadata concern: the archival canonical version is v3 dated 26 Jul 2011, notwithstanding the local PDF's internal March 2022 date. The actual proof verifies an influence-based variance extension on finite product spaces, using a basis/hypercontractive argument。
- 结论位置。Local p. 1 gives the Bernoulli influence-variance inequality; p. 2 states the finite-alphabet extension (Theorem 1.3); p. 4 builds the product-space orthonormal basis and hypercontractive input; p. 8 completes Theorem 1.3 through (2.18)–(2.19) and Proposition 2.7。
- 适用范围。This is not Talagrand convex concentration: its variables are finite product coordinates and its conclusion controls variance through coordinate influences. It does not justify the K05 skill's convexity, Euclidean Lipschitz, median/mean, or convex-distance steps。
- 相关技能。[math-k05-talagrand-convex-concentration](../../../../math-k05-talagrand-convex-concentration/SKILL.md)
- 其余依赖。If an influence-inequality tool is later created, retain Theorem 1.3's finite-alphabet/minimal-atom conditions and the hypercontractive Proposition 2.7 dependency. No active K05 claim relies on it。
- [主来源 1](https://arxiv.org/abs/1007.0677)

## A proof of the strong Gaussian product inequality conjecture

- 原件 498a05e746649bd16e866638bc0de5e4ce8b13a860d25814c0fd48eec982be9d。arXiv:2609.20234v1; local 17-page PDF marked 27 July 2026。物理页 1, 2, 3, 4, 5, 11。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.20234v1; official arXiv record checked, with no journal version listed。
- 已有技能。The arXiv v1 theorem is independently identifiable and the read proof establishes the positive-exponent scalar statement for every centered jointly Gaussian vector: E product_i |X_i|^{alpha_i} is at least the product of its marginal absolute moments for alpha_i>0, with the stated positive-variance equality criterion. The current route uses this exactly as a negative-transfer boundary: a Wishart block determinant is not a scalar coordinate of a jointly Gaussian vector, so the theorem does not settle either determinant-moment or determinant-event claims。
- 结论位置。Local PDF pp. 2--5: Theorem 1 and its correlation-matrix, branch/Jacobian, kernel and moment-recovery proof; p. 11: the spherical consequence。
- 适用范围。It is an unpublished v1 and applies to centered Gaussian scalar coordinates and positive absolute powers. It does not establish the Wishart determinant GPI, arbitrary nonlinear Gaussian functionals, negative/mixed exponents without the separate hypotheses, or determinant lower-orthant association。
- 相关技能。[probability-random-matrix-tensor](../../../../probability-random-matrix-tensor/SKILL.md)
- [主来源 1](https://arxiv.org/abs/2609.20234)

## A Reformulation of the Discrete Convexity Conjecture via k-Thresholds

- 原件 e17a363cf88a033b85dbac004079461a74707f8fd29814c660f8981bcfe43f6d。arXiv:2608.11183v1, submitted 11 Aug 2026。物理页 1, 4, 6, 20。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.11183v1; no published version is listed on the checked primary record。
- 邻近材料。Raw SHA and 22 physical pages match input; the checked primary arXiv record confirms the four authors and v1. Theorem 1.8 is a verified finite reduction: for an increasing graph property and H in it, the k-threshold is bounded by the best ordinary-threshold maximum over k-decompositions of H. The proof was inspected, as was the source's statement of its still-open general direction。
- 结论位置。Local p. 1 defines the setting and says the discrete convexity conjecture remains open; p. 4 states Theorem 1.8; p. 6 proves it via a k-decomposition and Lemma 2.1; p. 20 records the remaining general decomposition conjecture/open limitation。
- 适用范围。The theorem is about increasing graph properties and k-thresholds, not the product/Gaussian convex concentration framework of K05. It does not resolve the discrete convexity conjecture in full and gives no direct concentration tail estimate。
- 相关技能。[math-k05-talagrand-convex-concentration](../../../../math-k05-talagrand-convex-concentration/SKILL.md)
- 其余依赖。This is a useful finite decomposition construction for a separate graph-threshold tool only after definitions of p_k, r_k, and admissible k-decompositions are implemented with Theorem 1.8's graph-property assumptions. No active K05 claim relies on it。
- [主来源 1](https://arxiv.org/abs/2608.11183)

## A Sharper Hoeffding Bound for Weighted Sums of Exchangeable Random Variables

- 原件 9ca8ad3fe6cf70f7649e819c2d71a9314abc4cbc40c9649ebbd5dcf3658c67ae。arXiv:2608.04900v2 local copy, 14 physical pages。物理页 1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.04900v2。
- 已有技能。The official arXiv v2 record and local PDF agree on the finite-exchangeable weighted theorem. For N>=2, exchangeable X_i in [-1,1], n<=N, arbitrary weights, finite-population centering, and every real lambda, Theorem 1 gives the stated MGF proxy Gamma_N times the squared projected zero-padded weight norm; the local proof chain was read. This exact narrow claim is already described in H05 references/provenance.md entry E2773。
- 结论位置。Local p. 3, Theorem 1 and Corollary 1; pp. 5–8 reduce to Hamming slices/two-level vectors and evaluate Gamma_N; pp. 9–11 prove the auxiliary structural and hypergeometric martingale steps; pp. 12–13 prove the comparison/variance lower bound。
- 适用范围。It is not an iid or arbitrary-dependence theorem, does not center by an unconditional mean, and Section 2 explicitly says the reduction does not directly extend to Bernstein range/variance bounds. The first-order optimal constant remains open between the displayed lower and upper coefficients。
- 相关技能。[math-h05-chernoff-hoeffding-bernstein](../../../../math-h05-chernoff-hoeffding-bernstein/SKILL.md)
- 其余依赖。No missing dependency for the stated H05 exchangeable-Hoeffding interface; any extension to Bernstein, tensor/matrix, different centering, or general dependence needs a separate proof。
- [主来源 1](https://arxiv.org/abs/2608.04900)

## A short operator proof of Hoeffding inequalities for Markov chains

- 原件 728e0a8fa8c27bffc107612988c991770cf36861734152025fb5a6f299dc9beb。arXiv:2609.23098v1, 19 Sep 2026; local 16-page PDF SHA-256 verified。物理页 1, 3, 4, 5, 6, 7, 13, 14。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.23098v1 (the checked arXiv record lists no later version)。
- 构件候选。The local proof confirms the stated stationary-chain bound: for bounded measurable f_t in [a_t,b_t], invariant pi, and ||P-Pi||=lambda<1, its upper tail has Hoeffding exponent multiplied by (1-lambda)/(1+lambda). The source itself says this scalar theorem is Fan–Jiang–Sun (2021, Theorem 1); its new component is the Q_lambda^{1/2} K Q_lambda^{1/2} factorization followed by a scalar resolvent/convexity proof. Current H05 only describes independent/conditional MGF routes and does not yet claim this Markov result。
- 结论位置。p. 1 gives the Fan-et-al. inequality and provenance; pp. 3–4 state Theorem 1, the stationary L2(pi) absolute-gap assumptions, and the MGF target; pp. 5–7 prove the factorization/one-step scalar bound; pp. 13–14 prove the matrix extension's operator reduction。
- 适用范围。The source does not support applying H05's ordinary independent-variable steps to dependent chains: stationarity, an invariant measure, the absolute L2(pi) operator-gap bound, bounded ranges, and one-sided versus union-bound handling are indispensable. Its matrix extension additionally invokes a bounded multi-matrix Golden–Thompson inequality; that external theorem was not independently audited here。
- 相关技能。[math-h05-chernoff-hoeffding-bernstein](../../../../math-h05-chernoff-hoeffding-bernstein/SKILL.md)
- 其余依赖。For adoption, inspect the cited primary Fan–Jiang–Sun 2021 theorem and independently validate the needed Golden–Thompson premise for any matrix route; then add a separately scoped Markov-chain branch rather than broaden the existing independence branch。
- [主来源 1](https://arxiv.org/abs/2609.23098)

## A Structure Theorem for Poorly Anticoncentrated Gaussian Chaoses and Applications to the Study of Polynomial Threshold Functions

- 原件 727923ca18cbee112c86227edd870f63563ac21f5ee040a924809acd0eb54d62。local PDF: arXiv:1204.0543v2 (15 Aug 2012); body date 12 Sep 2018。物理页 1, 2, 3, 4, 10, 11, 12, 13, 14。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:1204.0543v2; FOCS 2012 full version, confirmed from official arXiv and FOCS record。
- 已有技能。The installed skill's narrow use is supported. For fixed d and positive epsilon,c,N, Theorem 1 approximates a degree-d Gaussian polynomial in L2 by one admitting an (epsilon,epsilon^(−c))-diffuse decomposition of bounded parameter-dependent size. The cited proof route really passes through small derivative probability, lower-degree product decomposition, and a well-founded decomposition descent; the skill correctly records the diffuse-box condition with N outside the exponent。
- 结论位置。PDF pp. 1–4 define diffuse decompositions and state Theorem 1; pp. 10–14 give the two-stage proof architecture, Proposition 11/12 and the tensor rank lemma. Existing skill: probability-gaussian-polynomial-approximation/references/sources.md M0237 and evidence/W18/cards/M0237.md。
- 适用范围。This is Gaussian, fixed-degree structural machinery, not a uniform sharp anti-concentration constant. The effective size dependence can be Ackermann-scale, and the 2018 body date does not override the arXiv v2 identity。
- 相关技能。[probability-gaussian-polynomial-approximation](../../../../probability-gaussian-polynomial-approximation/SKILL.md)
- [主来源 1](https://arxiv.org/abs/1204.0543) · [主来源 2](https://ieee-focs.org/FOCS-2012-Papers/4874a091.pdf)

## A Viscosity Solution Theory of Stochastic Hamilton-Jacobi-Bellman Equations in the Wasserstein Space

- 原件 c72ab0d8c833fb1fddc034c43c680cf75c2fc51240a95530df75496bd5537f34。arXiv:2310.14446v1 (22 Oct 2023; local PDF creation date 23 Oct 2023)。物理页 1, 2, 10, 12, 16, 17, 18, 23, 28。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2310.14446v1; no publisher version identified on the checked arXiv record。
- 构件候选。Under (A1)–(A3) and either (B1) or (B2), the paper proves a value function is a viscosity solution for its Brownian common-noise Wasserstein SHJB and then obtains uniqueness through its tailored comparison/approximation argument. The active E02 text does not invoke this paper for any operational step; it is presently only a pending evidence-index entry。
- 结论位置。Local PDF pp. 1–2 (conditional-law SHJB), 10–12 (DPP), 16–18 (Theorems 3.2–3.3 and viscosity proof), 23 and 28 (Theorem 3.4 uniqueness construction)。
- 适用范围。This is a conditional-law, measure-valued Brownian-control theory, not E02’s finite-dimensional Lévy-generator supersolution workflow. Its use of compact conditional-law test sets, its exact control class, and the B1/B2 alternatives cannot be silently substituted for E02 inputs。
- 相关技能。[math-e02-nonlocal-hjb-supersolution](../../../../math-e02-nonlocal-hjb-supersolution/SKILL.md)
- 其余依赖。To distill a component, first specify a measure-valued/common-noise model and independently map its generator, test-function notion, and comparison hypotheses; no transfer to arbitrary nonlocal jump HJB is established。
- [主来源 1](https://arxiv.org/abs/2310.14446)

## A zero-one law for swap-invariant events in uniform spanning forests

- 原件 9a743a44e1ee84a5adb0a50edf45ec38484a4f410aef1c112e170e3b0eecfa8c。local PDF: arXiv:2610.00938v1, dated 2 Oct 2026。物理页 1, 2, 3, 4, 5, 6, 7。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2610.00938v1 (submitted 1 Oct 2026), confirmed from official arXiv record。
- 构件候选。For FSF or WSF on a connected locally finite infinite network, Theorem 1.2 asserts a zero-one law for measurable events invariant under replacement of one present by one absent edge. The local proof reduces edge conditioning to a codimension-one projection-DPP coupling, then holds the conditional event probability fixed along an edge-reveal martingale. This is a meaningful possible finite-constructor lead: a certified finite conditioning/swap coupling would yield an auditable zero-one proof route。
- 结论位置。PDF p. 1 states Theorem 1.2; pp. 3–5 give projection-DPP conditioning, Lemma 2.5 and the reveal-martingale proof; p. 6 proves component/excessive-end applications; p. 7 identifies cited dependencies。
- 适用范围。This is a fresh preprint, not an active installed theorem. Swap invariance is stronger than general update stability and the result does not apply to arbitrary invariant events or arbitrary determinantal laws。
- 相关技能。[probability-forests-electrical-networks](../../../../probability-forests-electrical-networks/SKILL.md)
- 其余依赖。Independently verify the conditional FSF/WSF projection-DPP representation and the one-dimension coupling used in Lemma 2.5/Remark 2.6 (the proof cites Lyons, Determinantal Probability Measures, Proposition 10.3 / forest representation), including the WSF conditioning step。
- [主来源 1](https://arxiv.org/abs/2610.00938)

## AI's Solution of Conjecture 9.1

- 原件 1f5865b792fd628dac4e3d5f357bec6b21b55ef8e0917142d116caf1e09e31bd。arXiv:2609.33644v1, submitted 27 Sep 2026。物理页 1, 2, 4。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.33644v1; the checked record says it is not intended for journal publication。
- 邻近材料。Raw SHA and 5 physical pages match input, and the arXiv primary record identifies the authors and v1. Theorem 2.1 is actually present with a proof in the local version, but it is a p-small/spread-measure inequality for the discrete two-cover setting; the paper itself says the principal Conjecture 1.2 remains open up to a log-log gap。
- 结论位置。Local p. 1 records the still-open principal two-cover conjecture and defines p-small/spread notions; p. 2 states Theorem 2.1; p. 4 supplies its short proof through the Fourier expansion, Cauchy–Schwarz, Lemma 3.2, and integration against a spread measure。
- 适用范围。Neither this theorem nor the claimed AI provenance yields a convex concentration inequality. Treat it as a narrowly verified discrete-combinatorial result, not resolution of Talagrand's main two-cover statement or evidence for K05。
- 相关技能。[math-k05-talagrand-convex-concentration](../../../../math-k05-talagrand-convex-concentration/SKILL.md)
- 其余依赖。Any future p-small-cover skill should independently audit Lemma 3.2 and the prior result labelled [Li], then state exactly Theorem 2.1 rather than the still-open Conjecture 1.2. No active K05 claim depends on this preprint。
- [主来源 1](https://arxiv.org/abs/2609.33644)

## An infinite balls-in-boxes approach to the critical beta-splitting tree: some central limit theorems

- 原件 70e5c36565bdf5a3499d6be8672a30926f6fb98818b7710c05b8ba600909c815。Local 10-page ECP manuscript with placeholder volume/article/DOI fields; submitted to ECP on 13 October 2025。物理页 1, 2, 3, 4, 5, 6。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Electronic Communications in Probability 31 (2026), Paper 15, DOI 10.1214/26-ECP766; the local author manuscript is not asserted byte-identical to the version of record。
- 已有技能。The exact restricted G23.03 use is confirmed: Proposition 2.1 identifies, jointly and with the n-versus-n+1 convention shown there, the selected uniform-leaf decrement counts, total edge height and continuous height with occupied gap counts and the inverse subordinator at an independent exponential-sample maximum. This is an immediately usable finite constructor for the route’s one-lineage diagnostic/recurrence checks。
- 结论位置。Local physical pp. 1–3 define the critical tree and state the joint CLT; p. 4 states Proposition 2.1; pp. 5–6 prove the joint occupied-gap/inverse-subordinator representation and then begin the CLT reduction。
- 适用范围。The source is for the critical beta=-1 model, one uniformly sampled leaf, its particular driftless subordinator and independent Exp(1) sample. It neither gives a fixed cyclic-separation pair representation nor clears the broader full count-vector CLT/stable-proof claims. The local PDF’s placeholder bibliographic fields are repaired by the checked publisher landing page, not by a claim of byte identity。
- 相关技能。[probability-random-recursive-trees-asymptotics](../../../../probability-random-recursive-trees-asymptotics/SKILL.md)
- [主来源 1](https://projecteuclid.org/journals/electronic-communications-in-probability/volume-31/issue-none/An-infinite-balls-in-boxes-approach-to-the-critical-beta/10.1214/26-ECP766.full)

## Anti-concentration of polynomials: Lp balls and symmetric measures

- 原件 52e38ec747eff1f5b2db3b496fa23e54e984001187c2a1b601ce4427fdb94fd0。Earlier card recorded an unidentified 2026 manuscript; the 45-page local PDF identifies arXiv:2603.22664v1, dated 24 Mar 2026, on p. 1。物理页 1, 2, 3, 4, 7, 12, 27。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2603.22664v1, Itay Glazer and Dan Mikulincer, submitted 24 Mar 2026; no journal version was identified from the checked arXiv primary record。
- 邻近材料。The source proves an Lp-ball result for coefficient-normalized homogeneous polynomials, with a special even-integer p=d radial obstruction, and derives polynomial small-ball/Fourier consequences under its log-concave symmetry assumptions. It is not K04’s Gaussian/empirical-process supremum framework, and it supplies neither K04’s approximation errors nor N02’s Prékopa–Leindler/BBL pointwise hypotheses. Neither active skill currently relies on it。
- 结论位置。Local pp. 1–4 state the variance/small-ball/Fourier framework and Theorem 1.3; p. 7 gives its proof strategy; p. 12 states Theorem 2.1; p. 27 concludes its proof and derives Theorem 1.3. The checked arXiv record confirms v1 identity。
- 适用范围。The selected pages verify the theorem’s stated restrictions and its internal reduction to Theorem 2.1, but do not independently audit every external result used in the full proof。
- 相关技能。[math-k04-anti-concentration-empirical-process](../../../../math-k04-anti-concentration-empirical-process/SKILL.md)
- 其余依赖。No active K04/N02 dependency to repair. A future polynomial-small-ball skill would need a separate integration audit of Theorem 2.1, its external moment inputs, and the exact homogeneous/symmetry restrictions。
- [主来源 1](https://arxiv.org/abs/2603.22664)

## Application of the Theory of Boundary Value Problems in the Analysis of a Queueing Model with Paired Services

- 原件 c11a39bd300bdf1dd1262785463b43c8e3a32a111d0461287c456c1a36528ff0。Mathematical Centre Tracts 153, Mathematisch Centrum, Amsterdam (1982); local scan has 260 physical pages。物理页 3, 4, 7, 9, 12, 14, 15, 161。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。published 1982 Mathematical Centre Tracts 153, ISBN 90 6196 247 1; library record gives 244 printed pages。
- 引用核对。The scan and publisher record agree on Blanc’s 1982 tract. Its paired-service model is two independent Poisson customer types at one server, paired when possible; the introduction derives the two-dimensional departure-chain setting and an RH reduction. Theorem II.8.7 gives a unique stationary law under max{c1,c2}a<1 for that stated model。
- 结论位置。physical pp. 3–4 identify the tract; pp. 7–16 give contents, model and stated kernel/RH route; p. 161 states Theorem II.8.7。
- 适用范围。This source is not a generic RH/PGF solver. The displayed scope depends on the paired-service transition model, its LST kernel, contour/map construction and the stated stability parameters. The release skill correctly treats Blanc only as a model-specific book-unit/example, not as an A006 mixed gated/1-limited solution。
- 相关技能。[probability-generating-function-boundaries](../../../../probability-generating-function-boundaries/SKILL.md)
- 其余依赖。For use beyond citation, audit the full proof of Theorem II.8.7 and the book’s assumptions on the service transform and conformal-map regularity; no active unsound release claim was found。
- [主来源 1](https://research.tilburguniversity.edu/en/publications/application-of-the-theory-of-boundary-value-problems-in-the-analy/)

## Asymptotics for Beta-Splitting Trees via Homogeneous Fragmentations and Meromorphic Potential Theory

- 原件 85c9fad6604d435f9f25f141f0d068abc9ad9fd9b50c1744867dd26351ebcf2c。arXiv:2608.18320v1 (18 August 2026), 53-page local PDF。物理页 1, 3, 4, 6, 7, 11, 20, 21, 22, 23, 24。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.18320v1; no journal version of record was identified in the checked primary record。
- 已有技能。The skill’s restricted G23.03–G23.05 uses are confirmed. The paper proves the beta>-2 canonical conservative binary fragmentation embedding and its tagged-subordinator identities; in particular Theorem 2.12 proves the global CTCS maximum-height LLN and mixed-Gumbel law after checking the quadratic martingale and the collision Poisson error. These are the bounded uses recorded in references/sources.md, rather than a claim about the open fixed cyclic-gap pair covariance。
- 结论位置。Local physical pp. 3–4 derive the exact homogeneous-fragmentation embedding; pp. 6–7 state the potential identities and one-leaf consequences; p. 11 states Theorem 2.12; pp. 20–24 prove its collision/Chen–Stein maximum-height conclusions。
- 适用范围。The proof uses the source’s exact beta kernel, zero erosion, paintbox labels, uniform one-leaf or all-leaf maximum observable, and martingale/collision hypotheses. The positive-beta contour expansion and Appendix-C fluctuation material are not cleared by this card; neither the one-leaf nor maximum result transfers to a prescribed circularly separated leaf pair。
- 相关技能。[probability-random-recursive-trees-asymptotics](../../../../probability-random-recursive-trees-asymptotics/SKILL.md)
- [主来源 1](https://arxiv.org/abs/2608.18320)

## Asymptotics of Parking Search in Hyperfractal Networks

- 原件 dae941fd4a3c1e78f84b17f36ada1edf3f2ece00efeb7a54b3029e2cdd77e576。arXiv:2604.24821v1, dated 27 April 2026 in the local 17-page PDF。物理页 2, 6, 7, 16。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2604.24821v1 (no published version identified)。
- 待核。For the paper's recursive Manhattan, prescribed-segment, Poisson slot model, pp. 6--7 derive order/exponent statements through Mellin transforms. However, the proof detail on p. 16 gives f(x)=constant*x^(-1/d_F)*(1+P(log x)) with a periodic factor, whereas p. 2 and the advertised theorem language assert a pure constant-equivalent asymptotic. No argument read establishes P identically zero。
- 结论位置。Local p. 2 states the advertised pure scaling law; pp. 6--7 give Theorems 4.2--4.3 for the prescribed jumpless route; p. 16 derives the residue expansion used for Theorem 4.2。
- 适用范围。Thus the inspected source cannot support a transferable statement E[D]~C lambda^(-1/d_F), nor any route-independent or general spatial-network conclusion. The existing spatial-tree skill has no active use of this source; this is a held incoming dependency rather than a defect in an accepted route。
- 相关技能。[probability-random-spatial-tree-geometry](../../../../probability-random-spatial-tree-geometry/SKILL.md)
- 其余依赖。Resolve whether the periodic term vanishes under the stated parameters, or restate and prove only an order/bounded log-periodic result; then check the exact street-depth, route-selection and intensity normalizations before considering a new interface。
- [主来源 1](https://arxiv.org/abs/2604.24821)

## Bellman Policy Optimization

- 原件 92c83c177a22d2a708d246c71468fdddbdda28a6f6fdd04ffd8590060f6dc31a。Local PDF metadata identifies arXiv:2609.15987v1, 19 pages。物理页 1, 2, 7, 8, 9, 10, 14, 15, 16, 17, 18, 19。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.15987v1 (14 Sep 2026); no publisher version is listed on the official arXiv record checked。
- 邻近材料。For its stated bounded-length autoregressive terminal-reward setting, Appendix A.1 does prove equality of the exact objective’s optimizer with PMD on rollout-reachable states, conditional on its support/finite-KL assumptions. The later practical BPO loss is explicitly obtained through linearization, binary-KL, smoothing, masking, and clipping approximations。
- 结论位置。Local pp. 7–10 define the PMD and trajectory objectives and state Theorem 1; pp. 14–16 contain Appendix A.1’s martingale proof and the binary-KL identity; pp. 17–19 give experimental/ablation details。
- 适用范围。This is a policy-optimization result, not E03’s finite tree with common cross-layer budget and terminal potential. In particular, the exact-optimizer proof does not prove performance or equivalence for the practical clipped loss. E03’s E1489 source record is pending and no active skill claim relies on it。
- 相关技能。[math-e03-tree-bellman-cross-layer-budget](../../../../math-e03-tree-bellman-cross-layer-budget/SKILL.md)
- 其余依赖。No E03 activation without a separately proved mapping from its shared-budget tree hypotheses to this RL model and a quantified approximation error for the practical loss。
- [主来源 1](https://arxiv.org/abs/2609.15987)

## Bellman-sufficient Information Complexity

- 原件 51edc37950a7a94e9f9ef7f1729af8bc6bc463f9a820c23d3a9475163d54f63f。Local PDF metadata identifies arXiv:2606.11171v10, 77 pages。物理页 1, 2, 10, 11, 13, 16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 28, 31, 33, 34, 40, 52, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2606.11171v11 (15 Nov 2026), the latest version on the official arXiv record checked; no publisher version is listed。
- 邻近材料。The official record resolves the earlier missing identity and shows that the local v10 is superseded by v11. The inspected work has a different Bellman program: its state is a sequential-decision history, its information index is charged by a chain rule, and its conclusions require stated admissibility, calibration, and growth assumptions。
- 结论位置。Local p.1 and contents p.2 state the framework; pp.10–18 define sufficient states, indexed information and conditions; pp.20–22 give the Bellman–Fano construction; p.24 records the exact action-index chain rule; pp.25–28 state the GP branch; pp.33–34 state entropy/telescope conditions; pp.58–73 contain selected lower-bound, information, and separation proof passages。
- 适用范围。Those information-risk brackets do not supply E03’s shared real source/receiver capacity, cross-layer tree budget, or terminal-potential telescoping. The proof inspection therefore does not establish a transferable E03 component. E03’s E1527 provenance is pending rather than an active dependency。
- 相关技能。[math-e03-tree-bellman-cross-layer-budget](../../../../math-e03-tree-bellman-cross-layer-budget/SKILL.md)
- 其余依赖。If considered later, re-read canonical v11 and prove a specific reduction from E03’s tree model to the paper’s Bellman-sufficient state and all calibration/admissibility hypotheses。
- [主来源 1](https://arxiv.org/abs/2606.11171)

## Benign landscapes for synchronization on spheres via normalized Laplacian matrices

- 原件 dc1a69bcf5f2dee0be85f4dec77bad21a283a3400201957bb66ddf64f57e1cb1。arXiv:2503.18801v2; local 28-page PDF, front page dated 24 August 2026。物理页 1, 5, 6, 8, 9, 20, 21, 22。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2503.18801v2, revised 21 August 2026; no journal version listed by the checked arXiv record。
- 已有技能。The local v2 and official arXiv record identify the paper and support its limited reusable certificate: with L(z) positive semidefinite and a positive spectral gap, a positive diagonal D and r greater than the condition number lambda_max(D^-1/2 L(z)D^-1/2)/lambda_2 of that normalized Laplacian, every second-order critical point of the specified sphere factorization is globally optimal. The checked proof derives this conclusion from the criticality equations and a trace/Frobenius bound. The route's own source card correctly keeps the theorem as a model-conditional landscape certificate rather than a solution of its signed-threshold target。
- 结论位置。Local PDF p. 6, Theorem 2.1; pp. 8--9, Theorem 3.2 and its signed Erdős--Rényi scope; pp. 20--22, the real-case proof using first- and second-order criticality。
- 适用范围。This is an arXiv v2 result, not a general synchronization theorem: it requires the stated real MaxCut-type factorization, known rank-one certificate z, PSD/gap hypotheses and the strict rank/condition-number inequality. The random signed Erdős--Rényi asymptotic statement in Theorem 3.2 has its separate epsilon, p, delta and n-to-infinity conditions; it cannot be used for an oriented model or a different signed complete-graph threshold。
- 相关技能。[probability-random-graph-energy-landscapes](../../../../probability-random-graph-energy-landscapes/SKILL.md)
- [主来源 1](https://arxiv.org/abs/2503.18801v2)

## Convergence of Virial Expansions

- 原件 191484953805cfcf606b4add0c873c25caa6a99ec74b27804765480902ddd2b4。local complete 7-page Journal of Mathematical Physics scan, 5(7), pp.841--847 (July 1964)。物理页 1, 3。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。J. L. Lebowitz and O. Penrose, Journal of Mathematical Physics 5(7) (1964), 841--847, DOI 10.1063/1.1704186。
- 已有技能。Visual inspection of the local version-of-record scan confirms the restricted source use documented in the skill: in the stated stable classical-pair-potential model with finite Mayer integral B, the p.843 calculation derives a finite-volume virial-radius bound and separately an infinite-volume irreducible-Mayer-coefficient/radius consequence. It supports the skill's warning that a deletion-channel objective has not thereby been represented as a polymer or virial model。
- 结论位置。Physical p.1 / printed p.841 identifies the article and classical-gas model; physical p.3 / printed p.843 contains equations (3.2)--(3.15), including the 0.28952/((u+1)B) radius lower bound and the distinct finite- and infinite-volume coefficient statements。
- 适用范围。The constants and limits rely on the source's stability/Mayer-integrability assumptions and its fugacity-to-density inversion. They neither prove deletion-channel higher-order coefficients nor justify exchanging an input supremum, entropy-rate limit, and small-deletion expansion。
- 相关技能。[probability-information-cluster-expansion](../../../../probability-information-cluster-expansion/SKILL.md)
- 其余依赖。A new use must exhibit an actual compatible gas/polymer representation and independently verify every activity, stability, integrability, incompatibility, and limiting hypothesis; absent that, retain this only as scoped structural citation。
- [主来源 1](https://doi.org/10.1063/1.1704186) · [主来源 2](https://pubs.aip.org/aip/jmp/article/5/7/841/509096/Convergence-of-Virial-Expansions)

## Convergence Theorems for Martingales

- 原件 40752072e4edad8c2fcc42eec5b837b60fbbf733f8360ce3dcf5443e7a9caf83。32-page SHA-matched PDF hosted at the University of Cologne URL; no author, publication, date, or edition is printed in the inspected local document。物理页 1。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。not identified。
- 待核。The accessible material establishes only that the PDF is a 32-page discrete-time martingale chapter containing basic framework/filtration material. Neither the title-page/author nor the exact convergence-theorem statements and hypotheses were recovered. The current skill’s source ledger already classifies W02-S032 as unread, unverified, and excluded from its source count。
- 结论位置。I visually rendered and inspected local physical p. 1. It is headed “Chapter 1 — Martingales: Basic Properties and Stopping Theory” and begins a discrete-time exposition; the official host serves the same 32-page, font-encoded PDF but did not supply author or bibliographic identity。
- 适用范围。The pypdf extraction is unusable due to font encoding, and visual inspection of p. 1 does not identify the chapter’s author or source edition. It cannot certify UI, nonnegative-supermartingale, Lp, reverse-martingale, or optional-stopping hypotheses。
- 相关技能。[probability-martingale-stopping](../../../../probability-martingale-stopping/SKILL.md)
- 其余依赖。Locate an author-attributed original course/book edition with a title page and inspect each intended theorem and proof page; until then retain this record as non-evidence and use the separately verified martingale sources already in the skill。
- [主来源 1](https://www.mi.uni-koeln.de/~moerters/lectures/martingales.pdf)

## Critical exponential tiltings for size-conditioned multitype Bienaymé--Galton--Watson trees

- 原件 7de28a1156643dd4e67fc77affc3fd693d9f5bdba88cfa5709b0f4f9c32a1590。arXiv:2310.12897v1 [math.PR], 19 October 2023。物理页 1, 5, 9, 10。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2310.12897v1; no journal version was identified in the checked primary record。
- 邻近材料。The preprint's theorem route is genuinely a multitype BGW change of offspring law under linear type-count conditioning: the proof identifies tilts preserving a conditional tree law, then seeks a critical tilted mean matrix through the stated entire-offspring and matrix assumptions. This is a different exponential-tilting operation from H02's scalar cumulant-generating-function saddlepoint identity。
- 结论位置。Local p. 1 abstract; p. 5 assumptions (A.1)--(A.3), (B); p. 9 good-tilt condition c in (Ker Gamma)^perp and reduction; p. 10 Lemma 13 and the spectral-radius proof strategy. ArXiv record checked。
- 适用范围。Even within the paper, the claim requires (A.1)--(A.3), (B), a fixed root/type-count conditioning and the later local-limit dependencies. It supplies neither K'(s)=x nor Lugannani--Rice/Mills tail asymptotics. H02 does not rely on it for an active assertion。
- 相关技能。[math-h02-exponential-tilting-saddlepoint](../../../../math-h02-exponential-tilting-saddlepoint/SKILL.md)
- 其余依赖。Keep only as an adjacent branching-process reference; do not promote its preprint theorem into H02. A dedicated BGW-conditioning tool would require full verification of Theorem 4 and its external local-limit inputs。
- [主来源 1](https://arxiv.org/abs/2310.12897) · [主来源 2](https://arxiv.org/pdf/2310.12897)

## Cross Modality of the Extended Binomial Sums

- 原件 d3662771c1c4171cefa00fced6ca176a43f96d3fe3a6f52585ffc52381f151ce。arXiv:2408.06477v1 (12 Aug 2024)。物理页 1, 14, 15, 16, 17, 20, 21。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2408.06477v1; the locally hashed 31-page PDF identifies this version on physical p. 1。
- 已有技能。The arXiv v1 identity and the finite local derivative step are verified: Lemma 1(i),(iii) on pp. 14–15 yields partial_{p_i} f(k)=f_{-i}(k-1)-f_{-i}(k), which is the narrow local modal-sensitivity interface retained by the active Bernoulli skill. The active skill also correctly records that p. 16–17 peak displays have sign/index errors and uses an independently checked adjacent-balance formula instead; no active claim should invoke the paper's printed peak formula, extended-Darroch proof branch, or cross-modality conclusion without further audit。
- 结论位置。Local PDF pp. 14–15 state and prove the convolution/parameter derivative identities; pp. 16–17 contain the peak-skewness displays and Theorem 1; pp. 20–21 state and prove the extended Darroch rule。
- 适用范围。The paper extends to a Poisson component and possibly infinitely many Bernoulli coordinates. Its printed p. 16–17 peak formulae and the p. 14 Lemma 1(vi) indexing are unreliable for the active interface, while Theorem 2's proof on pp. 20–21 depends on that lemma and additional monotone-likelihood arguments. Thus this verification confirms only the finite independent convolution derivative identity, not a general modal or cross-modality theorem。
- 相关技能。[probability-bernoulli-extremal-orders](../../../../probability-bernoulli-extremal-orders/SKILL.md)
- 其余依赖。If adopting extended Darroch or cross-modality claims, reconstruct the proof from a correctly indexed balance identity, separately justify all infinite-coordinate limits and Poisson-component conditions, and test the repaired formulas on finite exact pmfs。
- [主来源 1](https://arxiv.org/abs/2408.06477)

## Dimension Drop of Harmonic Measure for Some Finite Range Random Walks on Fuchsian Schottky Groups

- 原件 9701e54633ccc7cb394cc6313b97cfc06db947675ed0818f8f37d37e464bf4e2。local manuscript dated 25 Jul 2025, 21 physical pages。物理页 1, 2, 6, 11, 12, 13, 14, 15, 16。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2301.09714v3 [math.GT], last revised 24 Jul 2025; published in Probability Theory and Related Fields 193 (2025), 143–161。
- 已有技能。The local 21-page paper is the dated v3 content of arXiv:2301.09714. Theorem A is model-specific: a separated two-generator Fuchsian Schottky group and the required unique prefix ending in a distinguished letter. The source constructs a finite-state hidden-Markov representation, proves the Gibbs-versus-dimension alternative, and uses the unique-prefix factorization on pp. 15–16 to force strict dimension drop。
- 结论位置。model and hidden-Markov construction pp. 1–11; Theorem 2 pp. 12–15; Theorem A contradiction and its unique-prefix calculation p. 16。
- 适用范围。The proof imports Ledrappier’s positive Gibbs density, Bowen pressure, Przytycki–Urbański exact-dimensional Gibbs theory, and Fricker–Furman’s length comparison. A dimension gap by itself is not a Lebesgue-singularity transfer: an additional same-limit-set full-δ Borel reference/separator is required, as the release skill already says。
- 相关技能。[probability-harmonic-measure-coding](../../../../probability-harmonic-measure-coding/SKILL.md)
- 其余依赖。Before expanding the route, independently verify the four imported results and prove the target-level Borel separator. No active release claim was found to omit these dependencies; the existing route states them explicitly。
- [主来源 1](https://arxiv.org/abs/2301.09714) · [主来源 2](https://arxiv.org/pdf/2301.09714)

## Dimension formula for harmonic measures in invariant random graphs on Gromov hyperbolic spaces

- 原件 8865497001c7ebf54c1753e91535f7367210ac31ab2696892185793baf1bce2f。local byte-checked arXiv:2403.11406v2, 27 physical pages (revised 20 Oct 2026)。物理页 1, 2, 15, 20, 21。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Ergodic Theory and Dynamical Systems, Cambridge online version located; arXiv v2 is the checked local e-print。
- 已有技能。The existing skill's restricted h/l route is supported: for the stated invariant-percolation models with indistinguishable infinite clusters and positive speed, the source proves exact dimensionality of the harmonic measure in its Gromov-boundary quasi-metric. The p.15 lower-bound step uses positivity plus ergodicity of the ray-cluster relation; pp.20--21 make the degree-biased Palm/ray-bundle measure and its ergodicity explicit。
- 结论位置。Theorems 1.1--1.2 on physical p.2; percolation exact-dimension proof on p.15; degree-biased ray-bundle and ergodicity setup on pp.20--21。
- 适用范围。This does not compare two coded measures, prove a generic Galton--Watson statement, or authorize h/l in another boundary metric without the scale conversion. The theorem retains the source's invariance, cluster-indistinguishability, integrability, positive-speed, and common-boundary hypotheses。
- 相关技能。[probability-harmonic-measure-coding](../../../../probability-harmonic-measure-coding/SKILL.md)
- 其余依赖。For an application, verify the target random graph satisfies the theorem's model hypotheses and identify the boundary metric normalization (for rho_epsilon comparable to rho^epsilon, rescale the denominator accordingly)。
- [主来源 1](https://arxiv.org/abs/2403.11406) · [主来源 2](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/dimension-formula-for-harmonic-measures-in-invariant-random-graphs-on-gromov-hyperbolic-spaces/B236EFBE107BD0625ABEB8E98AD914EC)

## Equal Subset Sums and Close Divisors

- 原件 21d622bdc46ca42fe02c1b8c695864c10699b2d4c8a24b19437b1d716afb052d。Local PDF: arXiv:2609.26014v1 (2026-09-22)。物理页 1, 2, 3, 4, 7, 10。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.26014v1。
- 构件候选。The arXiv record matches the local title, authors, date and 12-page v1. The source proves the stated equality α_k=β_k/(1−β_k), and the inspected Theorem 4 proves equality of weak and strict entropy endpoints through refinement; its arithmetic transfer is specifically from the independent 1/i random-set and geometric prime-exponent model。
- 结论位置。Theorem 2 (p.1); Theorem 4 and proof (pp.3–4); Theorem 2 proof locations (pp.7,10)。
- 适用范围。This is a 2026 preprint in number theory/combinatorics, not a theorem about permutation-cycle reachability. It cannot support the installed skill's fixed-k Poisson cycle or adjacent-target claims without an explicit model bridge。
- 相关技能。[probability-permutation-subset-sums](../../../../probability-permutation-subset-sums/SKILL.md)
- 其余依赖。If using it, implement a separate finite model bridge from the desired subset-sum law to its independent 1/i construction and audit the translation/uniformity argument in the full Theorem 2 proof。
- [主来源 1](https://arxiv.org/abs/2609.26014) · [主来源 2](https://doi.org/10.48550/arXiv.2609.26014)

## Equality conditions for correlation inequalities

- 原件 bc7895028982e5d81494cf9bc5718840f1f367d91140356d176160e3ff1944df。Earlier card called the PDF undated/unidentified; the 46-page local PDF identifies arXiv:2607.06275v1, dated 7 Jul 2026, on p. 1。物理页 1, 2, 3, 25, 27。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2607.06275v1, Swee Hong Chan and Igor Pak, submitted 7 Jul 2026; no journal version was identified from the checked arXiv primary record。
- 邻近材料。This is now an identifiable preprint about equality in AD/FKG inequalities on finite distributive lattices. Its stated objects and proof reduction are lattice-factorization arguments, not K01’s exceedance-field assumptions or block asymptotics; K01 does not actively rely on it。
- 结论位置。Local pp. 1–3 state the AD/FKG equality theorems and their lattice hypotheses; p. 25 begins Section 8 and p. 27 gives the reduction step labelled Proof of Theorem 1.3. The checked arXiv record supplies author, title, date, and v1 identity。
- 适用范围。Only selected theorem and proof-local pages were read; no claim is made that the entire equality-case proof has been independently rederived。
- 相关技能。[math-k01-chan-lai-asymptotically-gaussian-fields](../../../../math-k01-chan-lai-asymptotically-gaussian-fields/SKILL.md)
- 其余依赖。No K01 dependency to repair. A future discrete-correlation/equality skill would need a full audit of Sections 5–9 and the theorem’s support/lattice-closure hypotheses。
- [主来源 1](https://arxiv.org/abs/2607.06275)

## Extremal separation times and clade-count dynamics in fragmentation trees: a freezing transition

- 原件 0f78583ced23b24943bff94a753d7ab2bd091c476271a682cf62249a9175fd28。arXiv:2609.14325v2 (16 September 2026), 37-page local PDF。物理页 1, 3, 5, 6, 7, 8, 16, 21。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.14325v2; no journal version of record was identified in the checked primary record。
- 已有技能。The route’s selected G23.02 use is confirmed at the strict prethreshold interface: under the stated homogeneous exchangeable-fragmentation assumptions and fixed integer q<theta_*, Theorem 1.1(i), Proposition 3.3 and Corollary 1.2 supply the conditional all-q-set PPP and ranked exponential gaps. The existing skill correctly keeps this separate from a fixed cyclic-gap pair law。
- 结论位置。Local physical pp. 1 and 3 give the CTCS motivation and phase transition; pp. 5–8 state the fragmentation assumptions, Theorem 1.1, Corollary 1.2 and Theorem 1.3; p. 16 records the martingale/extremal inputs; p. 21 proves the strict-prethreshold ordered-gap consequence。
- 适用范围。Equality-critical and frozen decorated-PPP branches require their separately stated hypotheses and are not cleared here. Even the confirmed all-q-subset result uses exchangeable paintbox labels and does not identify the target’s designated cyclicly shifted pair, covariance, or product-uniform-integrability transfer。
- 相关技能。[probability-random-recursive-trees-asymptotics](../../../../probability-random-recursive-trees-asymptotics/SKILL.md)
- [主来源 1](https://arxiv.org/abs/2609.14325v2)

## Fredholm and Sturm–Liouville Type Characterizations of the Limit Measure for the Kac Killing Penalization for Lévy Processes

- 原件 8e140ddf5b4386e6b75db8dbfab6d74c96580fbf7aeaf23e27b5b519b035dc5c。Local 35-page manuscript with no arXiv identifier printed on the consulted first page; expected SHA-256 verified against the shared PDF。物理页 1, 7, 9, 18, 20, 24, 25。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.26642v2, last revised 19 Nov 2026, 35 pages (official record; local/official byte identity not tested)。
- 邻近材料。The recovered official version proves, for the stated recurrent one-dimensional Levy setting and compactly supported finite positive penalizing measure, an exponential-clock Kac-penalization limit, a Fredholm characterization, and an equivalent distributional Sturm–Liouville equation with a growth condition。
- 结论位置。PDF p. 7 states Theorem 1.4; p. 9 states the Fredholm/Sturm–Liouville equivalence; p. 18 proves the exponential-clock penalization limit; pp. 20 and 24–25 give the two implication steps。
- 适用范围。The proof concerns a Feynman–Kac/Kac penalization and a Doob h-transform, not J02’s general first-jump kernel identity or its bounded-perturbation Duhamel formula. Its hypotheses include recurrence, resolvent structure, compactly supported mu, and the displayed growth/normalization conditions。
- 相关技能。[math-j02-killed-process-duhamel-first-jump](../../../../math-j02-killed-process-duhamel-first-jump/SKILL.md)
- 其余依赖。The recovered arXiv identity resolves the earlier bibliographic hold, but it does not activate a J02 dependency. A future Kac-penalization interface would need to separately record the process recurrence/resolvent and penalizing-measure assumptions。
- [主来源 1](https://arxiv.org/abs/2608.26642)

## From Optimal Martingales to Randomized Dual Optimal Stopping

- 原件 dc4c75ab5a20aa34340c524c5810c940a43cae6de58bac65f6b818bbf70c03de。arXiv:2102.01533v1 (2 Feb 2021), 27-page local PDF。物理页 1, 5, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Belomestny and Schoenmakers, Quantitative Finance 23(7–8) (2023), 1099–1113, DOI 10.1080/14697688.2023.2223242。
- 已有技能。The active probability skill's narrow use is confirmed: in a finite discrete horizon, Theorem 3.2 says a weakly optimal non-Doob martingale becomes strictly suboptimal after the specified independent centered pseudo-martingale perturbation, whereas Proposition 3.1 retains the Doob case under its one-sided perturbation bound. The proof explicitly uses the auxiliary product space, iid randomizers supported in (-infinity,1], joint density positive at 1, the Snell decomposition, and optional sampling。
- 结论位置。Local pp. 1, 5–8 define the finite discrete-horizon Rogers dual, weak/sure optimality, and the auxiliary-product randomization; p. 9 states Proposition 3.1 and Theorem 3.2; pp. 17–18 prove them using the Snell Doob decomposition, the perturbation support/density-at-one condition, and Doob sampling. The publisher record and arXiv record establish the published identity。
- 适用范围。This does not establish a general continuous-time Snell-envelope or optional-stopping result. The theorem's randomization is not an F-adapted martingale on the original space, and its conclusion requires the stated finite-grid, integrability, independence, support, and density assumptions。
- 相关技能。[probability-martingale-stopping](../../../../probability-martingale-stopping/SKILL.md)
- 其余依赖。No active unsound dependency found. Any extension to continuous time or an alternative randomization law needs a separate theorem/proof; E04's separate randomized-stopping warnings remain unaffected。
- [主来源 1](https://arxiv.org/abs/2102.01533) · [主来源 2](https://doi.org/10.1080/14697688.2023.2223242)

## Fundamental Limits for Weighted Empirical Approximations of Tilted Distributions

- 原件 b53088de19bb69bf3b7552a99acee5e0214463f3e2add7ce0afe8787cfd0ad24。Local arXiv:2512.23979v1, 84 pages, dated 30 Dec 2025。物理页 1, 5, 7, 29, 43。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2512.23979v1 (30 Dec 2025), Sarvesh Ravichandran Iyer, Himadri Mandal, Dhruman Gupta, Rushil Gupta, Agniv Bandhyopadhyay, Achal Bassamboo, Varun Gupta, and Sandeep Juneja; no journal version identified on the checked primary record。
- 邻近材料。The primary record and local v1 agree on a self-normalized importance-sampling problem: Theorem 1 concerns a fixed-tilt KS scaling limit, while Theorem 2 gives a varying-tilt consistency condition involving M_{theta_n}/n. The inspected proof is an empirical-process/concentration argument, not a saddlepoint-tail approximation。
- 结论位置。Local PDF p. 1 metadata; pp. 5–7 Theorems 1–2 for KS accuracy; p. 29 begins the proof of Theorem 1; p. 43 proves Theorem 2 via Proposition 1 and empirical-process concentration。
- 适用范围。Although it uses exponential tilting, neither the theorem nor proof supplies the H02 saddle equation, LR correction, or Gaussian Mills reduction. It must not be cited for a saddlepoint relative-error claim。
- 相关技能。[math-h02-exponential-tilting-saddlepoint](../../../../math-h02-exponential-tilting-saddlepoint/SKILL.md)
- 其余依赖。No active H02 claim depends on this source. A separately scoped tilted-sampling skill would need to retain the estimator definition, M_theta/n regime, and empirical-process assumptions。
- [主来源 1](https://arxiv.org/abs/2512.23979)

## Generating DDPM-based Samples from Tilted Distributions

- 原件 b54df48bb5e31056c514ffaf84e9639c741f8a00e071f72e53dc9a5b8cd646c9。Earlier card treated the 2026 archive manuscript as unversioned and held it。物理页 1, 2, 5, 6。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。H. Mandal, D. Gupta, R. Gupta, S. R. Iyer, A. Bandyopadhyay, A. Bassamboo, V. Gupta, S. Juneja, arXiv:2604.03015 (2026); no journal version identified in checked primary record。
- 邻近材料。The official e-print resolves the prior identity hold. Its local Theorem 1 concerns a bounded-support one-dimensional plug-in estimator, while later results concern diffusion-based sampling accuracy under DDPM assumptions. These are not saddlepoint tail approximations。
- 结论位置。Local pp. 1--2 define nu proportional to exp(theta^T g(x)) mu and give sampling motivation; p. 5 Theorem 1 is an asymptotic-minimax plug-in-CDF statement; p. 6 begins Wasserstein assumptions/definitions. ArXiv record checked。
- 适用范围。The paper neither proves nor uses H02's required cumulant saddlepoint equation, conditional-independent-array Lugannani--Rice theorem, or Gaussian Mills reduction. Its claims remain preprint-specific and DDPM-dependent, but no active H02 claim relies on them。
- 相关技能。[math-h02-exponential-tilting-saddlepoint](../../../../math-h02-exponential-tilting-saddlepoint/SKILL.md)
- 其余依赖。No H02 integration. A future diffusion/tilted-sampling skill would need full theorem/proof checks, including dimension extension and all DDPM assumptions。
- [主来源 1](https://arxiv.org/abs/2604.03015) · [主来源 2](https://arxiv.org/pdf/2604.03015)

## Hypercontractive Inequality for Pseudo-Boolean Functions of Bounded Fourier Width

- 原件 e1fe1a86b69d0222a37a239d981c913298858603338ff39379ca83458bd6b50d。Local arXiv-stamped PDF arXiv:1106.1049v3, 10 pages, SHA-256 e1fe1a86b69d0222a37a239d981c913298858603338ff39379ca83458bd6b50d; p.1 also prints a conflicting 20 November 2021 date。物理页 1, 2, 3, 4, 5, 6, 7, 10。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Gutin and Yeo, Discrete Applied Mathematics 160(15) (2012), 2323–2328, DOI 10.1016/j.dam.2012.04.020; corresponding arXiv:1106.1049v3 was last revised 1 December 2012。
- 已有技能。The local proof confirms the active skill's narrow bounded-width moment interface: for a nonzero real pseudo-Boolean Fourier expansion under the uniform sign-cube measure, Theorem 1 supplies the sharp displayed (4,2) coefficient and Theorem 2 supplies even-moment control; Corollary 1 handles q>p>=2. The width condition counts nonzero Fourier monomials incident to a coordinate, not degree or Fourier l0 alone。
- 结论位置。Local pp.1–2 define the uniform sign cube and Fourier width; pp.3–4 state/prove Theorem 1; pp.4–6 prove Theorem 2; p.7 gives Corollary 1; p.10 closes the article。
- 适用范围。The stray 2021 date on the local title page conflicts with arXiv v3 and the 2012 publication, but primary arXiv and publisher records recover the canonical version. These inequalities give upper Lq/L2 bounds only and do not imply a real-degree, influence, or Fourier-support lower bound。
- 相关技能。[probability-boolean-fourier-invariance](../../../../probability-boolean-fourier-invariance/SKILL.md)
- [主来源 1](https://arxiv.org/abs/1106.1049) · [主来源 2](https://www.sciencedirect.com/science/article/pii/S0166218X12001795)

## Jump Plus AM-FM Mode Decomposition

- 原件 22840a4e585dc0b73465485039492af2f644ae10640c6dd5089bf7a90bf99501。arXiv:2407.07800v1 (submitted 10 July 2024; local 11-page “Submitted to IEEE TSP” copy, not byte-compared to the e-print)。物理页 1, 2, 4, 5。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2407.07800v1; no publisher version was verified in this review。
- 邻近材料。The recovered arXiv record fixes the former version hold: this is Nazari–Korshøj–ur Rehman’s 2024 signal-processing preprint, not a Markov-jump-process result。
- 结论位置。SHA-256 verified; local pp. 1–2 state the AM–FM/jump signal model, and pp. 4–5 give its augmented-Lagrangian/ADMM updates。
- 适用范围。It has no killing, stochastic process, first-jump kernel, or semigroup/Duhamel theorem; the J02 provenance listing is a topical false positive and the source is not an active J02 dependency。
- 相关技能。[math-j02-killed-process-duhamel-first-jump](../../../../math-j02-killed-process-duhamel-first-jump/SKILL.md)
- [主来源 1](https://arxiv.org/abs/2407.07800)

## Large deviations for Generalized Polya Urns with non-binary increments

- 原件 698b90a7eae801b91675e5929b45e9a91206a99bd1fda24004b5af27d8614a51。arXiv:2506.22234v2 [math.PR], 17 Nov 2025 (local PDF p. 1)。物理页 1, 3, 4, 13, 18。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2506.22234v2, official arXiv record checked。
- 邻近材料。The e-print studies a proposed sample-path-LDP extension for reinforced urns with non-binary increments. The inspected source itself presents a sketch/conditional route and a candidate LDP, rather than a derivation of a filtration-indexed, conditionally centered Bernstein moment bound。
- 结论位置。Local PDF p. 1 explicitly calls the non-binary extension a sketch; pp. 3–4 define the HLS/non-binary setup; p. 13 gives a conditional Varadhan-lemma passage; p. 18 calls the result a candidate LDP for K=2。
- 适用范围。The I01 skill is self-derived under explicit conditional moment and predictable-variance assumptions. This urn manuscript supplies neither those hypotheses nor a verified transfer from its sample-path LDP setup。
- 相关技能。[math-i01-ordered-increment-conditional-bernstein](../../../../math-i01-ordered-increment-conditional-bernstein/SKILL.md)
- 其余依赖。No active I01 claim relies on this source. A future use would require a complete LDP theorem/proof and then a separate derivation of the desired conditional MGF or Bernstein-moment interface。
- [主来源 1](https://arxiv.org/abs/2506.22234)

## Law of two-sided exit by a spectrally positive strictly stable process

- 原件 78c571aa8f110f97e7ed31626a2bb014500238aee815925637d3dcc2578b094b。Local PDF identifies arXiv:1806.07433v1 (19 June 2018) but is dated 9 August 2021; bytes were not matched to the e-print or version of record。物理页 1, 3, 4, 5, 6, 7, 8。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Zhiyi Chi, Stochastic Processes and their Applications 130(7) (2020), 3967–3989, DOI 10.1016/j.spa.2019.11.006; preprint arXiv:1806.07433v1。
- 引用核对。Publication identity is now verified. The source distinguishes continuous lower-boundary exit from upper exit by overshoot and derives their stated laws in this stable model。
- 结论位置。SHA-256 verified; pp. 1 and 3 specify a one-dimensional spectrally positive strictly stable process with index in (1,2) and the two exit mechanisms; p. 4 states the lower-exit density result; pp. 5–8 prove it via the Laplace transform, contour integral, and residues。
- 适用范围。It is not a generic Lévy or nonlocal Dirichlet theorem. In particular, its scale-function/Mittag–Leffler proof, spectral positivity, one-dimensional interval, and stable index assumptions cannot certify an arbitrary exit measure。
- 相关技能。[math-j03-nonlocal-balayage-exit-measure](../../../../math-j03-nonlocal-balayage-exit-measure/SKILL.md)
- 其余依赖。For a broader application, locate and verify an exit-kernel theorem for the intended process and exterior-data convention。
- [主来源 1](https://arxiv.org/abs/1806.07433) · [主来源 2](https://doi.org/10.1016/j.spa.2019.11.006)

## Learning Decision Trees Using the Fourier Spectrum

- 原件 38413e97bcb74ec2305f7afb2601515e074afcbb5ab20f65e0ebe74551f02920。local 22-page author manuscript; physical pages are reverse-ordered and page text is scan-corrupted。物理页 1, 2, 22。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Eyal Kushilevitz and Yishay Mansour, SIAM Journal on Computing 22(6) (1993), 1331–1348, DOI 10.1137/0222080。
- 引用核对。The prior metadata hold is repaired: this is the 1993 Kushilevitz–Mansour SIAM paper, not an unidentified scan. The verified citation-level result is a uniform-distribution, membership-query Fourier learner for polynomially sparse/L1-bounded spectrum, including GF(2)-linear-test decision trees; the installed skill correctly warns that it does not prove the separate support lower-bound questions。
- 结论位置。Local physical pp. 1–2 were inspected and are text-corrupted; the existing evidence card identifies p. 22 as title/abstract and maps printed pp. 4–19 to reversed physical pp. 19–4. Primary SIAM article record confirms the title, authors, journal, DOI, membership-query model, sparse-spectrum learner, and parity decision-tree scope。
- 适用范围。The supplied local scan remains unreadable enough that I did not independently rederive its proof. The algorithm is not a passive iid-labelled-example learner, and parity decision trees are broader than ordinary coordinate-query trees。
- 相关技能。[probability-boolean-fourier-invariance](../../../../probability-boolean-fourier-invariance/SKILL.md)
- 其余依赖。For a theorem-level import beyond the publisher abstract, recover a legible author/journal PDF and verify the reversed physical-page mapping, the correlated within-batch membership-query estimator, Lemma 5.1, and the stated runtime parameters。
- [主来源 1](https://doi.org/10.1137/0222080) · [主来源 2](https://www.cs.princeton.edu/courses/archive/spr07/cos522/KushilevitsMansour.pdf)

## Martingales and Path-Dependent PDEs via Evolutionary Semigroups

- 原件 e801673de1568690c19b0372a8ed46ed04b1f25dca17bd1978e3147a76f209d7。arXiv:2507.01845v1 (2 Jul 2025), 36 physical pages; SHA-matched local PDF。物理页 1, 3, 4, 5, 19, 20, 21, 26, 27。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Denk, Kunze, and Kupper, Journal of Evolution Equations 26, article 99 (2026), version of record published 10 Sep 2026, DOI 10.1007/s00028-026-01236-4。
- 引用核对。The local proof confirms a bounded measurable adapted V and adapted Ψ in L1(0,T;Bb(X)) yield the stated equivalence between M(t)=V(t)−∫Ψ and E-martingality and the shifted semigroup variation-of-constants formula. The stronger continuous/full-generator conclusions require the additional Cb-semigroup, continuity, domain, and full-support-related conditions set out around Theorems 4.10–4.12 and 6.3. The current I02 skill does not rely on this paper for a universal projection or compensator theorem。
- 结论位置。Local pp. 3–5 state the E-martingale/evolutionary-semigroup framework and scope; Theorem 4.10 and its two directions are on pp. 20–21; Theorem 6.3 and its proof are on pp. 26–27. The Springer version-of-record page confirms the publication identity。
- 适用范围。This is an E-martingale associated with the paper’s evolutionary expectation operator, not an arbitrary filtered-space Doob–Meyer theorem. It does not identify optional/predictable projections or compensators of a general counting process without independently checking the process, filtration, and relevant projection theorem。
- 相关技能。[math-i02-filtration-projections-compensators](../../../../math-i02-filtration-projections-compensators/SKILL.md)
- 其余依赖。Any adoption into I02 should first map the target process to the paper’s path-space expectation operator and verify the required adaptedness, Bb/L1 or Cb assumptions; otherwise cite a standard projection/compensator theorem suited to that process。
- [主来源 1](https://arxiv.org/abs/2507.01845) · [主来源 2](https://link.springer.com/article/10.1007/s00028-026-01236-4) · [主来源 3](https://doi.org/10.1007/s00028-026-01236-4)

## On K-wise Independent Distributions and Boolean Functions

- 原件 8cddcf831d7084645bae8bdb1dcf5aaab32c101f6883a1a5c9c343422f94897e。local PDF: arXiv:1201.3261v1 header, 16 Jan 2012; body date 27 Nov 2024。物理页 1, 3, 4, 5, 6, 7, 8, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:1201.3261v1 (16 Jan 2012), confirmed from official arXiv record。
- 已有技能。The date conflict is a local body-date artifact, not a version ambiguity: arXiv confirms v1. The live skill retains only the verified finite Boolean-cube interface: LP pointwise-polynomial duality, the exact unstandardized binomial normalization, and Theorem 16 for two-level odd majority (physical pp. 7–8); it explicitly leaves Section 5 Question 4 on iterated ternary majority open。
- 结论位置。PDF pp. 1–4 set up A(n,k,p), K1/K2 and polynomial duality; pp. 5–8 give the binomial-moment and two-level-majority route; p. 13 poses the iterated-ternary-majority question. Existing skill: probability-boolean-fourier-invariance/references/sources.md BGP2012 and evidence/W10/cards/BGP2012.md。
- 适用范围。BGP2012 does not prove a recursion for arbitrary-depth ternary-majority trees, nor a general Boolean-to-Gaussian finite-independence transfer. For the lower construction, the XOR0/XOR1 parity choice must be selected so the block bias has the claimed sign。
- 相关技能。[probability-boolean-fourier-invariance](../../../../probability-boolean-fourier-invariance/SKILL.md)
- [主来源 1](https://arxiv.org/abs/1201.3261)

## On Lower Bounds for the Capacity of Deletion Channels

- 原件 7b0779b2967b73277633b8af86066ff14809a353922c5b7f7447caaa3d8a3ffc。local Harvard CS Technical Report TR-07-04 scan, 7 physical pages; embedded text encoding unreadable。物理页 1, 2。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。expanded journal article: E. Drinea and M. Mitzenmacher, IEEE Transactions on Information Theory 52(10) (2006), 4648--4657, DOI 10.1109/TIT.2006.881832。
- 引用核对。The prior hold on identity is resolved: the local file is the seven-page Harvard TR-07-04 read-copy, not the one-page ISIT item; the independently checked author-hosted earlier paper identifies the deletion-channel setting and the two advertised improvements. The source supplies achievable lower-bound constructions, not capacity equality or a convergent cluster expansion。
- 结论位置。Local report cover/first article page (physical pp.1--2) were consulted; author-hosted ISIT 2004 PDF gives the binary iid-deletion model and its stronger-typical-output/structured-input scope。
- 适用范围。The local scan remains text-unreadable, and the report itself defers detailed proofs of its stated main lower bounds to a full version. The checked author-hosted ISIT PDF is an earlier version and was not byte-matched to the local TR; the publisher full text was not recovered here。
- 相关技能。[probability-information-cluster-expansion](../../../../probability-information-cluster-expansion/SKILL.md)
- 其余依赖。Before using a detailed Drinea--Mitzenmacher functional or numerical bound, read the relevant theorem and proof in the 2006 journal version (or a byte-identified full version), preserving its run-length law, deletion model, normalization, and error terms。
- [主来源 1](https://www.eecs.harvard.edu/~michaelm/postscripts/isit2004.pdf)

## On the Optimal Stopping Problem for Diffusions and an Approximation Result for Stopping Times

- 原件 4f02f04d686b8fc6b74f3cadd59a2fc02fb3b221aecff5ce733c73b239e0c480。arXiv:2503.02514v1 (4 Mar 2025), 18-page local PDF。物理页 1, 2, 3, 4, 5, 6, 7, 8, 9, 10。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Cosso and Perelli, Stochastic Analysis and Applications 44(6) (2026), 799–823, DOI 10.1080/07362994.2026.2701255; published online 21 Jul 2026。
- 引用核对。The source supports, at citation level, the conditional value equality for its finite-horizon multidimensional Lipschitz diffusion and the resulting equality of the two stopping-time classes, Snell-envelope identification, and dynamic-programming formula. It fixes the prior version-identity gap by supplying arXiv:2503.02514 and a 2026 journal DOI。
- 结论位置。Local pp. 1–4 state the finite-horizon Brownian diffusion, Lipschitz/growth hypotheses, flow property, and value functions; pp. 5–7 state and prove Theorem 2.1 by simple-state/random-time approximation; pp. 7–10 derive Corollary 2.1, the Snell-envelope identification, and the dynamic-programming step. The arXiv and journal records identify the later publication。
- 适用范围。This is not an active general Snell-envelope dependency in the current E04 instructions. The displayed proof relies on Brownian natural-completed filtrations, strong SDE flow/continuity, polynomial growth and the paper's stopping-time approximation; moreover, the reverse direction of Theorem 2.1 is summarized rather than written in full on the inspected local pages. It does not cover arbitrary right processes, jumps, or generic class-D rewards。
- 相关技能。[math-e04-snell-envelope-optimal-stopping](../../../../math-e04-snell-envelope-optimal-stopping/SKILL.md)
- 其余依赖。For a reusable E04 component, independently verify the published version's full approximation theorem and retain every diffusion/filtration assumption; do not replace the finite discrete Snell recursion with this source。
- [主来源 1](https://arxiv.org/abs/2503.02514) · [主来源 2](https://doi.org/10.1080/07362994.2026.2701255)

## On Wilks' Problem: Exact Recursive Formulas via Stein's Method for the Joint Moments of Disjoint Principal Minors of Wishart Random Matrices

- 原件 3064eb3b3db5eb0558e3df7579a72e51b14018874eb6b19f0caa8b1feeaffcad。arXiv:2607.03984v1; local 9-page PDF marked 4 July 2026。物理页 1, 3, 4, 5, 6。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2607.03984v1; official arXiv record checked, with no journal version listed。
- 已有技能。For W distributed as W_p(alpha,Sigma), alpha>p-1, pairwise disjoint principal diagonal blocks and nonnegative integer determinant exponents, Theorem 3.1 gives a finite exact recursion: the stated polynomial operator lowers total degree and is iterated sum_r n_r p_r times. The local proof verifies the homogeneity reduction conditional on the displayed Wishart Stein identity. This is a particularly usable finite constructor for testing integer-exponent instances, and the current route correctly does not promote it to a general product inequality。
- 结论位置。Local PDF pp. 3--6: definitions, Eq. (3.1), Theorem 3.1, the degree-lowering proof through Eq. (3.8), and Remark 3.2。
- 适用范围。The paper does not prove the sign of the all-real-exponent Wishart determinant GPI or any lower-orthant association; for noninteger powers its own Remark 3.2 says the finite polynomial recursion no longer terminates. Its Eq. (3.1) is imported from the forward implication of Bailly et al. (2026), which was not independently recovered or proof-checked in this adjudication。
- 相关技能。[probability-random-matrix-tensor](../../../../probability-random-matrix-tensor/SKILL.md)
- 其余依赖。Recover the precise published/e-print version and proof of Bailly et al. (2026), Corollary 3.3 forward implication supplying the Wishart Stein identity (3.1), before treating the recursion as independently verified rather than source-conditional。
- 已采用构件。非负整数幂的精确矩由高斯分部积分与自由度多项式延拓独立推出。Wishart Stein 刻画及非整数幂另按原条件核验。[使用说明](../../../../probability-random-matrix-tensor/references/wishart-polynomial-moments.md)
- [主来源 1](https://arxiv.org/abs/2607.03984)

## Parabolic-hyperbolic splitting in support propagation for stochastic porous media equations

- 原件 7fae18380b1e05d7036ed9b33a1691bcff364bf719321bc3598adc975d5ca1c8。Local 28-page preprint with no arXiv identifier printed on the consulted first page; expected SHA-256 verified against the shared PDF。物理页 1, 2, 5, 6, 17。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.11468v1, submitted 10 Sep 2026 (official record; local/official byte identity not tested)。
- 邻近材料。The paper proves finite support propagation and waiting-time criteria for a stochastic porous-media equation with linear conservative transport noise by randomly localized energy estimates; its recovered official record fixes the prior missing identity。
- 结论位置。PDF pp. 1–2 define the stochastic porous-media setting and method; pp. 5–6 state assumptions and finite-speed/waiting-time results; p. 17 begins the proof of Theorem 2.5。
- 适用范围。The theorem is about kinetic solutions of a specific SPDE under (A1)–(A3), not a random Carleson packing or an LlogL embedding. Its proof does not provide the I04 missing endpoint step。
- 相关技能。[math-i04-random-carleson-occupancy-llogl](../../../../math-i04-random-carleson-occupancy-llogl/SKILL.md)
- 其余依赖。No active I04 assertion relies on this source. Any future transfer would first require a new, explicit map from the SPDE energy localization to a Carleson occupancy inequality。
- [主来源 1](https://arxiv.org/abs/2609.11468)

## Peak Estimation of Time Delay Systems using Occupation Measures

- 原件 a97f4407517c8a48ab9f9cb86f31cd5363c7d2676e62c83c7a91244a0f27b9b3。arXiv:2303.12863v3 (5 Apr 2023); local 34-page PDF matches the v3 date/header。物理页 1, 7, 8, 9, 11, 19, 24, 25。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Miller, Korda, Magron, Sznaier, 62nd IEEE Conference on Decision and Control (2023), pp. 5294-5300, DOI 10.1109/CDC49753.2023.10384165。
- 引用核对。The formal trajectory-to-measure construction supports an upper-bound LP for the stated finite-horizon deterministic discrete-delay DDE and makes its required consistency constraint explicit. It proves no duality gap between its measure LP and function dual, not equality between the original DDE peak problem and the LP。
- 结论位置。Local p. 7 proves the delayed-coordinate consistency identity; p. 8 proves each DDE trajectory generates the stated measure variables; p. 9 proves measure/function-program duality but labels exactness of the DDE relaxation Conjecture 3.1; p. 19 repeats that tightness remains future work; pp. 24-25 give the discrete-delay analogue and dual construction。
- 适用范围。Current E01 does not claim exact delayed-state lifting from this source. The source's own Conjecture 3.1 leaves the relaxation gap open even under its listed A1-A5 plus convex image-set conditions; it is not a stochastic-delay result。
- 相关技能。[math-e01-occupation-measure-flow-lp](../../../../math-e01-occupation-measure-flow-lp/SKILL.md)
- 其余依赖。Any active DDE peak claim must prove the original-problem-to-LP exactness separately or retain the direction P*<=p* and the history/consistency constraints。
- [主来源 1](https://arxiv.org/abs/2303.12863) · [主来源 2](https://ieeexplore.ieee.org/document/10384165) · [主来源 3](https://doi.org/10.1109/CDC49753.2023.10384165)

## Phase Transitions in Edge-Weighted Exponential Random Graphs: Near-Degeneracy and Universality

- 原件 151a6887b0bec45379e4e50e8972c37e2d49b8d77c1477f77c4a7a5c0e3a74b8。Local arXiv:1706.02163v2, 21 pages, dated 23 Feb 2018; journal-manuscript layout。物理页 1, 7, 8, 10, 15, 16。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。DeMuse, Larcomb and Yin, Journal of Statistical Physics 171(1), 127–144 (2018); DOI 10.1007/s10955-018-1991-3; arXiv:1706.02163v2 is the checked e-print。
- 邻近材料。The e-print identity and publication metadata are recovered. The checked results use Legendre duality and a Cramer rate function to study phase transitions of weighted exponential random graphs under compact-support and symmetry assumptions. This is a variational network-model analysis, not an H02 saddlepoint tail theorem。
- 结论位置。Local PDF p. 1 metadata; p. 7 states limiting variational formula Theorem 1; pp. 8–10 establish the phase-transition/maximization setup; pp. 15–16 prove/state distribution-dependent edge-density versus dual-parameter asymptotics。
- 适用范围。The occurrence of a cumulant-generating function and an exponential-family model does not supply the conditional LR theorem, a general change-of-measure tail formula, or a Mills-prefactor error bound。
- 相关技能。[math-h02-exponential-tilting-saddlepoint](../../../../math-h02-exponential-tilting-saddlepoint/SKILL.md)
- 其余依赖。No active H02 claim depends on this source. Any use must retain the edge-weight support, symmetry, attractive-region, and graph-model assumptions stated in the theorem。
- [主来源 1](https://arxiv.org/abs/1706.02163)

## Philosopher and Prophet Inequalities for Divisible Items

- 原件 1af5c4b36bb4e44920e32026ce339b6d875ed7443f0722fbed7764569c20f80b。arXiv:2607.11742v1; local 30-page PDF dated 14 July 2026 and marked 13 July 2026 on arXiv。物理页 1, 3, 7, 8, 12, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2607.11742v1; arXiv record checked, with no journal version listed。
- 邻近材料。The v1 source proves a 2/3 online/philosopher guarantee only for divisible unit-supply resources with monotone concave DR-submodular valuations, and a 1/2 fixed-price prophet result in that model. The proof-facing local statements expressly use its concave relaxation, per-item capped-OCRS and Aumann--Shapley prices. The route's source inventory already records it as divisible-resource adjacent methodology, while its operational skill boundary does not adopt either ratio for the route's distinct allocation settings。
- 结论位置。Local PDF pp. 1, 3, 7--8 and 12--13: Theorems 1.1, 3.2 and 1.2, the concave relaxation, capped-OCRS definition, and Lemma 4.2。
- 适用范围。Neither theorem transfers to indivisible requests, arbitrary concavity, or a different comparator/arrival/information model. The paper's global guarantees also compose its model-specific relaxation, scaling-function construction and oracle assumptions; reading Lemma 4.2 alone does not supply a general prophet rule。
- 相关技能。[probability-prophet-online-selection](../../../../probability-prophet-online-selection/SKILL.md)
- [主来源 1](https://arxiv.org/abs/2607.11742)

## Policy Iteration for Stationary Discounted Hamilton-Jacobi-Bellman Equations: A Viscosity Approach

- 原件 f359bf848400259e5a963304141abfe911fb9af472db07cc351454720f883a57。arXiv:2604.10191v2 (local PDF metadata identifies v2)。物理页 1, 2, 11, 12, 13, 14, 15, 16。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2604.10191v2 (15 Sep 2026); no publisher version identified on the checked arXiv record。
- 邻近材料。For the specified deterministic, stationary discounted HJB discretization, Proposition 4.6 proves fixed-policy bounded evaluation by a resolvent contraction, Theorem 5.2 gives fixed-mesh geometric policy-iteration convergence, and Theorem 5.8 gives a square-root-h vanishing-viscosity bound under its discount condition. The local metadata matches the current arXiv v2 identity。
- 结论位置。Local PDF pp. 1–2 (deterministic discounted semi-discrete setting), 11–13 (Proposition 4.6, Theorem 5.2 and Proposition 5.3), and 14–16 (Lipschitz conditions and Theorem 5.8)。
- 适用范围。These are numerical, first-order deterministic stationary results with an artificial-viscosity stencil, positive discount, bounded Lipschitz data, and exact fixed-policy evaluations. They do not validate a stochastic nonlocal supersolution, a Lévy jump generator, or an uncontrolled continuous-time comparison step。
- 相关技能。[math-e02-nonlocal-hjb-supersolution](../../../../math-e02-nonlocal-hjb-supersolution/SKILL.md)
- 其余依赖。No E02 integration is indicated. A separate numerical-HJB skill would need to state its discrete scheme, boundary treatment, policy regularity, and exact-evaluation assumptions。
- [主来源 1](https://arxiv.org/abs/2604.10191)

## Probability Distributions on Cladograms

- 原件 e100126d88b6abadd23d3060ef4ba6a2adbddadfc14aa0d8813436115fc94272。local 20-page PDF has encoding-corrupted extraction; its physical p. 1 was inspected but is not legible as theorem evidence。物理页 1。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。David Aldous, 1996, Random Discrete Structures, IMA Vol. 76, pp. 1--18, DOI 10.1007/978-1-4612-0719-1_1。
- 引用核对。The published identity is recovered: Aldous's 1996 chapter embeds the two popular cladogram models in a beta-splitting family and explicitly warns that the sought natural one-parameter neutral-evolution family does not exist in the asserted form. This repairs the prior local identity/legibility hold, but only at citation level because the archived local text is corrupt。
- 结论位置。The local physical p. 1 was inspected and found text-corrupt. The checked Springer publication page identifies the chapter, author, pages and DOI; the checked Aldous author copy supplies the abstract describing the beta-splitting family。
- 适用范围。The recovered metadata and abstract do not verify a source-specific height, uniform-leaf, fixed-gap pair, or finite-n recurrence transfer. The author-copy PDF was checked for identity, but it was not byte-matched to the corrupt local file; no theorem claim is inferred from the corrupt local extraction。
- 相关技能。[probability-random-recursive-trees-asymptotics](../../../../probability-random-recursive-trees-asymptotics/SKILL.md)
- 其余依赖。For a theorem-specific use, obtain a legible canonical chapter copy and read the relevant beta-splitting section, then match leaf labels, ordered/unordered convention and statistic to the target。
- [主来源 1](https://doi.org/10.1007/978-1-4612-0719-1_1) · [主来源 2](https://www.stat.berkeley.edu/~aldous/Papers/me69.pdf)

## Recovered AEP-023 source: Riesz transform on manifolds and heat kernel regularity

- 原件 7408225f4f1f9fa7cc4c37b0e1857cbc1bcdeee86dd8b8e5ae30aa5c002d8b07。The assigned 17-page PDF is a generated cards_math_preview export, not a self-identifying scholarly paper; its pp. 1–7 label the AEP-023 source-card material。物理页 1, 2, 3, 4, 5, 6, 7。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Auscher, Coulhon, Duong and Hofmann, arXiv:math/0411374v1 (17 Nov 2004; local 47-page source SHA256 d2319bea8f65d06695a34f72c39168795639a58a315a457c0d465fb48cddf01c; title page says revised 25 Oct 2004)。
- 引用核对。The prior hold is resolved at the identity level: the preview is a derivative card rendering, but AEP-023 identifies a byte-hashed local copy of Auscher--Coulhon--Duong--Hofmann, and the official arXiv record confirms v1, title and authors. The recovered source proves a strong-Lp Riesz-transform/good-lambda mechanism on complete noncompact manifolds under its doubling, Poincare and heat-gradient assumptions; the active endpoint skill correctly treats it as auxiliary strong-type evidence rather than a scalar weak-(1,1) theorem。
- 结论位置。Assigned preview pp. 1–7 preserves the AEP-023 theorem-card fragments. Recovery matched its identifier to the local 47-page arXiv source, whose physical pp. 1, 3–5, 14 and 21 give the identity, Theorems 1.1–1.4, the good-lambda criterion, and the Riesz-transform regularization step。
- 适用范围。The assigned PDF itself is not a byte-matched paper and cannot independently establish all card prose. The recovered theorem has geometric/vector-output and strict 2<p<p0 hypotheses, so it supplies neither weak-(1,1), L log L, a Euclidean scalar-coordinate result, nor a sharp endpoint constant。
- 相关技能。[probability-analytic-endpoint-methods](../../../../probability-analytic-endpoint-methods/SKILL.md)
- 其余依赖。For any new use, bind the exact 47-page arXiv source and check the target manifold, doubling/Poincare/heat-gradient assumptions, operator output and strict p-range; a separate endpoint argument is required for any weak-type transfer。
- [主来源 1](https://arxiv.org/abs/math/0411374) · [主来源 2](https://doi.org/10.1016/j.ansens.2004.10.003)

## Reflection of Optimal Supports for k-wise Independent Bits

- 原件 f8669d7cb4c3980d7955945d6cb5d169f37d22ce811d5de592a562be2248c9d1。Local PDF: arXiv:2609.25595v1, 22 September 2026。物理页 1, 2, 3, 4。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.25595v1。
- 构件候选。The local v1 and arXiv record agree on a four-page preprint. For even k and the specified paired count bases I=J∪{n}, Theorem 1 proves the displayed positive-factor reflection of basic weights at p and 1-p; Lemma 2 then gives the stated optimality only when such a basis is feasible. The installed skill does not rely on this reflection result。
- 结论位置。Theorem 1 and its interpolation/binomial proof (pp.2–3); Lemma 2 and scope disclaimer (pp.3–4)。
- 适用范围。The paper is a preprint with disclosed substantive AI use. Its argument assumes the prior paired-basis characterization and does not establish endpoint reflection, ordered support components, or equality of objective values. It is therefore not cleared as an active skill dependency。
- 相关技能。[probability-moment-polynomial-duality](../../../../probability-moment-polynomial-duality/SKILL.md)
- 其余依赖。Independently recover and verify the cited Berend–Ernst–Kontorovich–Kumar basis characterization and separately prove any desired endpoint/order transfer before implementation。
- [主来源 1](https://arxiv.org/abs/2609.25595) · [主来源 2](https://doi.org/10.48550/arXiv.2609.25595)

## Remarks on Viscosity Super-Solutions of Quasi-Variational Inequalities

- 原件 da417ef6a12346e008a286c13c73845e2367758b4cbc6a5f9031702ad95f6bb2。arXiv:2010.12738v2 (5 Feb 2021; local PDF dated 8 Feb 2021)。物理页 1, 2, 3, 4, 5, 6, 7, 8, 9, 11。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2010.12738v2; no publisher version identified on the checked arXiv record。
- 构件候选。For its local finite-dimensional impulse-control QVI, the paper demonstrates that the usual supersolution condition need not supply the intervention obstacle needed to compare a subsolution with a supersolution. Its modified definition imposes the obstacle constraint; Theorem 3.1 then gives comparison subject to (H1)–(H2), ordered data, growth, and Hölder conditions. This is a qualified guardrail for a future impulse-QVI extension, not an existing E02 rule。
- 结论位置。Local PDF pp. 1–2 (finite-horizon first-order QVI and motivation), 3–6 (modified supersolution definition, Lemma 2.3 and counterexample), 7–9 (Theorem 3.1 comparison assumptions/proof), and 11 (impulse-control conclusion)。
- 适用范围。The paper treats a local first-order finite-dimensional QVI with an intervention operator, not E02’s Lévy jump integral. The conclusion cannot be applied to a generic nonlocal HJB or to a model without matching impulse cost, obstacle, and regularity assumptions。
- 相关技能。[math-e02-nonlocal-hjb-supersolution](../../../../math-e02-nonlocal-hjb-supersolution/SKILL.md)
- 其余依赖。Before integration, provide an actual impulse-control QVI, verify the corresponding obstacle orientation and H1/H2-type cost hypotheses, and establish the nonlocal-jump comparison theorem needed for that model。
- [主来源 1](https://arxiv.org/abs/2010.12738)

## Saddlepoint Approximation to the Distribution of the Absorption Time of the Diffusion under Resetting and Reflection

- 原件 478d0d2c157c1d59aec7ff988616c63f8f4338bcb45a1cdab134494228fb9ad6。Local 30-page Research Article PDF; author Riccardo Gatto; pre-publication layout with an incomplete DOI line。物理页 1, 12, 13, 14。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。R. Gatto, Methodology and Computing in Applied Probability 28, article 121 (2026), published 12 Nov 2026; DOI 10.1007/s11009-026-10345-z。
- 邻近材料。The recovered version of record confirms this is a saddlepoint treatment of the upper tail of a first-passage time for a drifted Wiener diffusion with an upper reflecting wall and Poisson resetting. The local algorithm is model-specific: it builds the exact reset FPT CGF, requires a saddlepoint, and separately invokes a steepness condition for its tail approximation。
- 结论位置。Local PDF p. 1 title/author; pp. 12–13 Algorithm 3.2 constructs K_r and solves K_r'(s_t)=t; p. 14 Proposition 3.4 gives the Chernoff upper bound。
- 适用范围。This published article does not prove the active H02 conditional-independent-array Lugannani–Rice theorem and cannot justify a generic u^{-1} prefactor. The current skill correctly treats Gatto as an adjacent worked example rather than a proof dependency。
- 相关技能。[math-h02-exponential-tilting-saddlepoint](../../../../math-h02-exponential-tilting-saddlepoint/SKILL.md)
- 其余依赖。No active H02 claim depends on this source. Any use of its tail approximation must separately verify the reflected/reset diffusion transform, steepness, and the invoked Butler–Wood conditions。
- [主来源 1](https://link.springer.com/article/10.1007/s11009-026-10345-z)

## Sharp Concentration Inequalities: Phase Transition and Mixing of Orlicz Tails with Variance

- 原件 1a4418ea22ad46ef62824de3926561d335a67e72b441656270d3c929605e9859。Earlier card called this a manuscript dated 2026-03-30; the 64-page local PDF identifies arXiv:2603.25934v1, dated 26 Mar 2026, on p. 1。物理页 1, 4, 7, 41, 42。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2603.25934v1, Yinan Shen and Jinchi Lv, submitted 26 Mar 2026; no journal version was identified from the checked arXiv primary record。
- 邻近材料。The verified result concerns weighted sums of independent centered scalar sub-Weibull variables. Its proof is a one-dimensional mgf/Markov argument. It does not establish K03’s uniform two-semimetric increment condition over an index set, admissible-partition γ functionals, or measurability/separability. K03 does not cite or use this preprint in its active procedure。
- 结论位置。Local p. 4 states the i.i.d. scalar corollary; p. 7 summarizes Theorem 1’s α-regime tails; pp. 41–42 give the labelled Proof of Theorem 1 from Lemma 1 via an exponential-Markov calculation. The checked arXiv record confirms v1 identity。
- 适用范围。The proof examined reduces Theorem 1 to Lemma 1; this review did not independently reprove that lemma or certify later martingale/vector/matrix extensions。
- 相关技能。[math-k03-dirksen-mixed-tail-generic-chaining](../../../../math-k03-dirksen-mixed-tail-generic-chaining/SKILL.md)
- 其余依赖。No active K03 dependency to repair. To use this source for a future chaining component, prove a uniform increment inequality with common d1,d2 before invoking K03。
- [主来源 1](https://arxiv.org/abs/2603.25934)

## Shephard Type Problems for Lp-Centroid Bodies

- 原件 18f16a91ef1e4b2f6a6970eb1b353b2eeee907c42fba01b72797b08ae23fde7d。Local SHA-matched one-page abstract/reference extract headed Mathematical Inequalities & Applications 17(3) (2014), 865–877, DOI 10.7153/mia-17-63。物理页 1。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Feng Yibin and Wang Weidong, Mathematical Inequalities & Applications 17(3) (2014), 865–877, DOI 10.7153/mia-17-63; official full article recovered。
- 引用核对。The official version verifies the paper’s identity and the narrow theorem family: for example Theorem 1.1 compares normalized Lp-dual affine surface-area expressions under ΓpK⊆ΓpL, while Theorems 1.2–1.4 impose additional polar-projection, symmetry, or counterexample hypotheses. The installed skill correctly records M0336 as partial/not-read and does not make an active claim from it。
- 结论位置。Local physical p. 1 supplies identity only. I also checked the publisher full text at printed pp. 865–867: Theorems 1.1–1.4 state the indicated Lp-centroid-body conclusions, explicitly for 1≤p<n and their listed star/convex-body subclasses。
- 适用范围。The local object is not the full article and has no proof pages. The published results concern geometric Lp-centroid bodies and do not by themselves establish a log-concave moment, concentration, or transport inequality; every body-class and 1≤p<n condition remains required。
- 相关技能。[probability-logconcave-moment-geometry](../../../../probability-logconcave-moment-geometry/SKILL.md)
- 其余依赖。If a future route needs one of these results, archive the official full text under its verified DOI and check the Section 4 proof of the exact selected theorem before adding it to an active source card。
- [主来源 1](https://files.ele-math.com/articles/mia-17-63.pdf) · [主来源 2](https://doi.org/10.7153/mia-17-63)

## Singularity of Harmonic Measure for Finitely Supported Random Walks

- 原件 c79ebd3a2324ac6f3ee664008b4b9aea1e747f68b09bee256cba3e73e3bd8eeb。arXiv:2609.19115v1 [math.DS], 16 Sep 2026。物理页 1, 6, 7, 9, 10, 11, 12。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.19115v1; no journal version identified。
- 引用核对。The local hash is the stated v1. Theorem 1 asserts that for a cocompact Fuchsian group and a finitely supported probability measure whose support semigroup is the group, the boundary hitting measure is singular to Lebesgue measure. The proof by contradiction on pp. 6–11 uses a finite translate family in L²(R), then a nowhere-vanishing Fourier multiplier。
- 结论位置。Theorem 1 on physical p. 1; Fourier lemma/proof on pp. 6–11; references on p. 12。
- 适用范围。The proof’s absolute-continuity-to-two-sided Green estimate invokes Blachère–Haïssinsky–Mathieu Theorem 1.5 and Kim–Zimmer Theorem 1.9; those external dependencies were not independently rechecked here. It applies only to the same cocompact Fuchsian boundary and Lebesgue class, not arbitrary coded target measures。
- 相关技能。[probability-harmonic-measure-coding](../../../../probability-harmonic-measure-coding/SKILL.md)
- 其余依赖。Independently check the cited BHM/Kim–Zimmer equivalence and bounded-density inputs before promoting the 2026 v1 beyond the release skill’s present supplementary/request-only common-boundary citation status。
- [主来源 1](https://arxiv.org/abs/2609.19115) · [主来源 2](https://arxiv.org/pdf/2609.19115)

## Speed of Random Walks in Dirichlet Environment on a Galton-Watson Tree

- 原件 409d0c8addd04f9050a78b16481fd31436ebbaa6a9265603cb5bf1233564812c。arXiv:2405.11845v1, dated 20 May 2024 in the local 35-page PDF。物理页 1, 4, 5, 6, 18, 21。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2405.11845v1 (no published version identified)。
- 待核。The actual v1 establishes, under transience and the finite normalizer condition (7), a limiting law C^(-1) mu_ER for the environment/path seen from the particle and uses it in its speed formula. It does not, in the inspected result, prove the normalized double-tree law is invariant for the required environment chain: p. 18 labels it a limiting measure, while the text says invariance beyond the condition would be proved in a subsequent paper。
- 结论位置。Local pp. 1--4 define the directed Dirichlet/edge-reinforced Galton--Watson model and state the speed conditions; pp. 5--6 define the double-tree measure; p. 18 states Theorem 3.9 and Corollary 3.10, and p. 21 begins the proof of the speed/normalizer equivalence。
- 适用范围。The conclusion is confined to this directed (alpha_p,alpha_c)-ERRW/RWDE on a supercritical Galton--Watson tree, survival conditioning and the explicit integrability/normalizer gates. A convergence-to-limit statement alone does not discharge the installed skill's generator/semigroup or invariant-law proof gates, and it cannot be transferred to its unresolved normalized-law interface。
- 相关技能。[probability-stationary-law-interfaces](../../../../probability-stationary-law-interfaces/SKILL.md)
- 其余依赖。Locate and independently inspect the promised subsequent invariant-measure proof, including the state-space transition kernel, finiteness/normalization and a direct invariance identity; only then consider a narrowly scoped stationary-law card。
- [主来源 1](https://arxiv.org/abs/2405.11845)

## Stability of Compensator Integrals and Nonlinear Operators under Canonical p-th Power Variation Convergence

- 原件 f7f35197558f4bf697497bfac3fd9ba41b2cfabe822183f76266901b082f6a25。Local PDF: arXiv:2605.11783v3 (21 Sep 2026)。物理页 1, 8, 9, 10, 11, 62, 64, 68, 70, 71。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2605.11783v3 (official record lists v3 as current; v1 12 May 2026 and v2 24 May 2026)。
- 构件候选。The official record resolves the previous missing version as Kennerberg arXiv v3. Theorem 4.2 proves p-power-variation convergence of f_n*nu_n to f*nu from realised canonical p-variation convergence only with predictable integrands, compensator integrability, LG0, LU, JC, and BEp. The proof uses threshold-separated jump alignment and then decomposes the compensator-atom difference in (7.19); the local proof pages substantiate that this is not an automatic compensator-continuity claim。
- 结论位置。Local Definition 4.1 and Theorem 4.2, pp. 8–9; worked sharpness example pp. 10–11; proof architecture pp. 62–64, 68, 70–71; official arXiv abstract and v3 record。
- 适用范围。The theorem is a recent preprint and its conclusion is canonical p-power-variation convergence, not generally ucp. It assumes real-valued adapted cadlag processes on a common filtered space, finite variations, predictable compensators, and all named hypotheses; it does not establish general optional/predictable projection or Doob–Meyer existence。
- 相关技能。[math-i02-filtration-projections-compensators](../../../../math-i02-filtration-projections-compensators/SKILL.md)
- 其余依赖。A separate full proof audit of the remaining Theorem 4.2 tail and second-term estimates is required before I02 adopts it. If adopted, I02 must expose LG0/LU/JC/BEp and distinguish the p=2 ucp upgrade。
- [主来源 1](https://arxiv.org/abs/2605.11783)

## Stochastic Calculus for Pathwise Observables of Markov-Jump Processes: Unification of Diffusion and Jump Dynamics

- 原件 9a18c26ae8b9719d60fd10ec82c434c4e83fc171dfe4d1041257e321f12fc1ac。Local 44-page manuscript dated 21 April 2026; its bytes were not matched to e-print v3 or the version of record。物理页 1, 3, 9, 10, 11, 12, 14, 16, 17。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Stutzer, Dieball, Godec, Physical Review X 16, 021038 (published 19 May 2026), DOI 10.1103/9ncx-4pgr; accepted e-print arXiv:2508.04647v3。
- 引用核对。The former manuscript-only status is repaired: a published PRX article and accepted arXiv v3 were checked. It supports the narrow compensated transition-count identity for its Markov-jump model with specified rates and state occupation。
- 结论位置。SHA-256 verified; p. 3 states the finite-state Markov-jump matrix noise equation; p. 9 derives dn_xy=r_xy 1_{X=i}dt+dε_xy from the counted transitions; pp. 10–14 define the path observables and their correlation formulas; pp. 16–17 derive a thermodynamic inequality for the paper’s setup。
- 适用范围。The source does not establish J04’s general integer-valued-random-measure compensation theorem, a stochastic Fubini interchange, exit settlement, or J05’s private frozen-coordinate contract. The active skills do not rely on it for those broader claims。
- 相关技能。[math-j04-jump-compensation-fubini-exit-settlement](../../../../math-j04-jump-compensation-fubini-exit-settlement/SKILL.md)
- 其余依赖。To adopt it as a general compensation dependency, provide a theorem covering the intended filtration, predictable integrand, compensator, integrability/localization, and any Fubini/exit convention。
- [主来源 1](https://arxiv.org/abs/2508.04647) · [主来源 2](https://journals.aps.org/prx/abstract/10.1103/9ncx-4pgr)

## Stochastic filtering of a pure jump process with predictable jumps and path-dependent local characteristics

- 原件 feb30426b68c574f33c9ed473fcf956e581094063f0cea4961c89f816ecd604e。Local 39-page PDF identified as arXiv:2004.12944v3; expected SHA-256 verified against the shared PDF。物理页 1, 5, 6, 7, 18, 19, 20, 21。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Published in Stochastic Processes and their Applications 151 (2022), 396–435, DOI 10.1016/j.spa.2022.06.007; arXiv:2004.12944v3 is the checked e-print record。
- 邻近材料。Under Assumptions 2.1, 2.2, 5.2, and 5.4, Theorem 6.1 gives a filtering SDE with a particular signal jump operator Lt, predictable-jump operator At, and an innovations representation; the proof starts from the signal semimartingale decomposition and conditional projection。
- 结论位置。PDF pp. 5–7 define the pure-jump signal, observed jump-diffusion, predictable projections, and Assumptions 2.1–2.2; p. 18 states Theorem 5.5; pp. 19–21 state and begin proving Theorem 6.1。
- 适用范围。This is a partially observed, path-dependent filtering model with a unique observation SDE, two non-common driving jump measures, specified predictable projections, bounded intensities, and integrability. It does not independently establish the active J01 general small-time generator limit, its domain, or its non-explosion criteria。
- 相关技能。[math-j01-inhomogeneous-jump-generator](../../../../math-j01-inhomogeneous-jump-generator/SKILL.md)
- 其余依赖。The J01 provenance row should remain non-active/adjacent. To use this paper, add a separate filtering interface that verifies all of Assumptions 2.1, 2.2, 5.2, and 5.4; do not cite Theorem 6.1 as a generic jump-generator theorem。
- [主来源 1](https://arxiv.org/abs/2004.12944) · [主来源 2](https://www.sciencedirect.com/science/article/pii/S0304414922001326)

## Stochastic Fokker-Planck PIDE for conditional McKean-Vlasov jump diffusions and applications to optimal control

- 原件 77a57a121def005a8ca4ed68e1f10e0211e7a4beba2be89f36c74ebac690cd8a。arXiv:2110.02193v4 (8 Jan 2023); local 32-page PDF carries the v4 header。物理页 1, 6, 7, 8, 11, 12, 13, 14, 15, 16, 20, 21, 30, 31。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。not identified。
- 待核。The local v4 supports a narrowly conditional, distributional Fokker-Planck calculation and a smooth feedback verification argument if its Dynkin formula, solution existence, admissibility, and a smooth HJB maximizer are available. It does not establish a general nonlocal HJB supersolution result。
- 结论位置。Local pp. 7-11 state and derive the distributional conditional Fokker-Planck PIDE; p. 12 says uniqueness in the jump case is assumed rather than proved; pp. 14-16 give the smooth closed-loop verification theorem using Dynkin's formula; pp. 20-21 state a second verification theorem whose proof is omitted and refers back; pp. 30-31 list the cited stochastic-calculus/viscosity sources。
- 适用范围。The paper explicitly assumes uniqueness of its jump Fokker-Planck PIDE, invokes a jump Ito theorem externally, confines controls to closed-loop Markov form, and leaves non-smooth viscosity treatment as future work. Therefore it cannot clear an active E02 dependency for general controlled nonlocal HJB claims。
- 相关技能。[math-e02-nonlocal-hjb-supersolution](../../../../math-e02-nonlocal-hjb-supersolution/SKILL.md)
- 其余依赖。Escalate any use beyond the displayed smooth conditional McKean-Vlasov model: supply a jump-PIDE uniqueness theorem, a valid Dynkin/Ito domain and integrability argument, and an appropriate viscosity/comparison result for the proposed control class。
- [主来源 1](https://arxiv.org/abs/2110.02193)

## Stochastic Optimal Transport and Hamilton-Jacobi-Bellman Equations on the Set of Probability Measures

- 原件 75ba2f40aae19f93af6c626b5f66d361d02fc0c9aafef10da598e22a000c3f00。arXiv:2306.04283v2 (21 May 2024; local PDF creation date 21 May 2024)。物理页 1, 2, 17, 18, 19, 20, 21, 47, 48。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Charles Bertucci, Ann. Inst. H. Poincaré Anal. Non Linéaire 42 (2025), no. 6, 1543–1600, DOI 10.4171/AIHPC/138。
- 引用核对。The local arXiv v2 states a comparison theorem for its bounded viscosity sub/supersolutions on probability measures under Hypothesis 1, and separately treats a jump process acting on the target measure in Proposition 2.18. The primary publisher record identifies the 2025 AIHP publication and DOI; this resolves the earlier preprint-only identity issue。
- 结论位置。Local PDF pp. 1–2 (measure-valued stochastic transport problem), 17–21 (Hypothesis 1, Theorem 2.11 and jump extension Proposition 2.18), and 47–48 (Theorems 4.12 and 5.1–5.2)。
- 适用范围。The proved comparison is on probability measures over the torus with the source’s Hamiltonian, boundedness, terminal behavior, and target-process structure. It is not a general Lévy nonlocal HJB theorem, and the active E02 instructions do not currently rely on it。
- 相关技能。[math-e02-nonlocal-hjb-supersolution](../../../../math-e02-nonlocal-hjb-supersolution/SKILL.md)
- 其余依赖。If using the measure-target jump result, retain Hypothesis 1, continuous nonnegative intensity, bounded solutions, and its particular operator T; separately prove any relation to an E02 state-space jump kernel。
- [主来源 1](https://arxiv.org/abs/2306.04283) · [主来源 2](https://ems.press/journals/aihpc/articles/14298327) · [主来源 3](https://doi.org/10.4171/AIHPC/138)

## T-product Tensor Expander Chernoff Bound

- 原件 d4372618f5671505d4ea5ea54c439a687ba1d591c004b1f1896d39680debdfdd。arXiv:2109.13831v1, 28 Sep 2021; local 35-page PDF SHA-256 verified。物理页 1, 3, 22, 23, 30, 31, 32。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2109.13831v1 (the checked primary record lists only v1 and an arXiv substantial-text-overlap administrative note)。
- 待核。The cited T-product expander conclusion is not cleared. Theorem 8 defines beta_0(t)=pi/[2(cosh(pi t)+1)] (p. 22), while Theorem 1.1 assumes finite C,sigma with beta_0(t) <= C/(sigma sqrt(2pi)) exp(-t^2/(2sigma^2)) for all real t (p. 3), and pp. 30–32 use exactly that premise. No finite Gaussian majorant of this form can bound beta_0 globally: beta_0 has exponential tails, so its ratio to any fixed Gaussian grows without bound as |t| tends to infinity。
- 结论位置。p. 3 states Theorem 1.1 and its fourth beta_0 majorant premise; pp. 22–23 define beta_0 and prove Theorem 8; pp. 30–32 feed the premise into the displayed Chernoff derivation。
- 适用范围。Thus the printed hypothesis used to pass from the integral to the Gaussian expression is vacuous for finite parameters; the local paper does not furnish an operational tensor Chernoff inequality. This does not invalidate H05's existing standard scalar Chernoff/Hoeffding/Bernstein statements, which do not cite or use this source。
- 相关技能。[math-h05-chernoff-hoeffding-bernstein](../../../../math-h05-chernoff-hoeffding-bernstein/SKILL.md)
- 其余依赖。A corrected nonvacuous tail domination (or a replacement integration argument) and a rechecked tensor interpolation/expander proof are required before any H05 extension can cite this manuscript。
- [主来源 1](https://arxiv.org/abs/2109.13831)

## Tamed Euler Schemes for Singular SDEs with Multiplicative Levy Noise

- 原件 aba7cca952a2a12a43c2cea0efda2004fbefc160a7950f8bb6338f226abe5d42。Local PDF: arXiv:2607.18862v1 (21 Jul 2026)。物理页 1, 9, 10, 11, 67, 72, 73。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2607.18862v1 (only version listed by the official arXiv record)。
- 构件候选。The official record recovers the prior manuscript as Zhang–Zhang arXiv v1. Under Conditions H_gsigma, H_b, and cH_gsigma plus displayed Gamma-integrability, Theorem 2.4 gives the stated strong-error bound. Proposition 8.7 separates W8 (compensated jump martingale freezing) from W9 (nonlocal compensator freezing); pp. 72–73 insert those bounds into the stochastic-Gronwall closure。
- 结论位置。Local Theorem 2.4 and Corollary 2.9, pp. 9–11; Proposition 8.7 p. 67; Theorem 2.4 closure pp. 72–73; official arXiv abstract and v1 record。
- 适用范围。This is a model-specific numerical-SDE rate theorem, not a general compensator result. The rate retains all regularity/exponent, truncation, integrability, and drift-approximation assumptions; Corollary 2.9 explicitly omits a proof segment by reference。
- 相关技能。[math-i02-filtration-projections-compensators](../../../../math-i02-filtration-projections-compensators/SKILL.md)
- 其余依赖。Before integration, create a numerical SDE route and independently audit Conditions H_gsigma, H_b, cH_gsigma and the cited/omitted Corollary 2.9 drift estimate. I02 must not advertise these rates as a general projection/compensator rule。
- [主来源 1](https://arxiv.org/abs/2607.18862)

## The Accessibility of Convex Bodies and Derandomization of the Hit and Run Algorithm

- 原件 4fae8eb0a01529bd08fa45110680b625779da53d78add35d43c86156c1d1143a。arXiv:1312.7061v1, submitted 26 Dec 2013。物理页 1, 3, 4。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Journal of Convex Analysis 24 (2017), no. 3, 903–916; local PDF is arXiv:1312.7061v2 (18 Sep 2016)。
- 邻近材料。Raw SHA and 13 physical pages match input. The active K05 skill has no source-specific dependency on this paper: it audits Talagrand convex concentration for product/Gaussian measures, whereas this published result supplies a finite-direction convex-body accessibility construction and convergence route for a hit-and-run-style Markov chain. The theorem/proof pages establish that bounded finite construction under convex-body hypotheses。
- 结论位置。Local p. 1 states the model and the restricted-direction chain; p. 3 proves the normalized inball accessibility lemma; p. 4 proves Theorem 2.2 using John's ellipsoid and affine invariance, yielding d+1 accessibility with a finite direction set of stated size。
- 适用范围。Accessibility and convergence of this particular chain do not establish a Talagrand convex-distance inequality, a Lipschitz convex-function tail bound, or a product/Gaussian concentration property. Do not use its abstract sampling language as concentration evidence。
- 相关技能。[math-k05-talagrand-convex-concentration](../../../../math-k05-talagrand-convex-concentration/SKILL.md)
- 其余依赖。A separate sampling/walk skill would need the precise Section 3–4 kernel hypotheses and convergence-rate proof before adopting the construction; K05 needs no correction because it makes no reliance on this paper。
- [主来源 1](https://arxiv.org/abs/1312.7061) · [主来源 2](https://journalofconvexanalysis.com/articles/jca24053/)

## The Exit-Time Problem for a Markov Jump Process

- 原件 3ca42b9ac0084b5b4d5312a791970cd6ae84453946be8f6f9bc8ed6bdd2d5f14。Local 15-page EPJ manuscript; its bytes were not matched to the e-print or version of record。物理页 1, 2, 10, 11, 12, 13, 14。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Burch, D’Elia, Lehoucq, European Physical Journal Special Topics 223 (2014), 3257–3271, DOI 10.1140/epjst/e2014-02331-7; related e-print arXiv:1411.1817v1。
- 已有技能。Publication identity is now verified. Under the paper’s finite-range jump kernel and volume constraint, the forward equation records loss from the interior to the interaction domain, and the backward equation is used for exit-time moments。
- 结论位置。SHA-256 verified; local pp. 1–2 set finite-range jumps and the interaction domain; p. 10 gives the backward/forward operators; pp. 11–12 give the volume-constrained exit density and mass balance; pp. 13–14 state the variational/coercivity setting。
- 适用范围。The source does not prove the active J03 general exit-measure workflow for arbitrary right-continuous processes, killing, or a general nonlocal balayage kernel. Its scope must remain a citation for finite-range, volume-constrained models。
- 相关技能。[math-j03-nonlocal-balayage-exit-measure](../../../../math-j03-nonlocal-balayage-exit-measure/SKILL.md)
- 其余依赖。For use beyond citation level, supply a theorem matching the chosen process, killing convention, exterior data, and kernel domain。
- 已采用构件。在给定有限保守吸收链上独立推导全时域退出矩与类别概率。原文连续空间体积约束结论仍作限定引用。[使用说明](../../../../math-j03-nonlocal-balayage-exit-measure/references/finite-exit-phase-type.md)
- [主来源 1](https://arxiv.org/abs/1411.1817) · [主来源 2](https://doi.org/10.1140/epjst/e2014-02331-7)

## The Fourth-Moment Theorem on Hilbert Spaces

- 原件 2718b7bb639fd20c910670fed658b4850e845a1de452d2f455b4113d549ea5c5。Local 51-page manuscript dated 23 Sep 2026; expected SHA-256 verified against the shared PDF。物理页 1, 2, 12, 13, 14, 15, 18, 19, 20, 23, 24, 26, 28, 30。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2509.20342v3, last revised 22 Sep 2026 (official record; local/official byte identity not tested)。
- 邻近材料。The local manuscript and official arXiv record agree on an infinite-dimensional fourth-moment theorem: fixed-chaos convergence requires trace-class covariance convergence and coordinatewise weak fourth-moment/contraction conditions; the proof controls finite projections, tails, and then chaos truncation。
- 结论位置。PDF pp. 12–15: Theorem 3.2 and its trace-class/projection proof; pp. 18–23: finite-chaos Theorem 3.3 and proof; pp. 23–28: infinite-chaos Theorem 3.4/3.5 truncation argument; pp. 28–30: vector case。
- 适用范围。This is a Hilbert-valued Wiener-chaos Gaussian-convergence theorem. It does not prove the active I03 finite-time suffix maximal comparison, whose admitted step is the separately derived Doob L4 endpoint inequality; neither an L4 maximal bound nor a random-start/stop argument occurs here。
- 相关技能。[math-i03-fourth-moment-suffix-maximal-comparison](../../../../math-i03-fourth-moment-suffix-maximal-comparison/SKILL.md)
- 其余依赖。No active I03 claim should depend on this paper. A future Hilbert-chaos normal-approximation skill would need a separate integration decision and must retain trace-class covariance and fixed/infinite-chaos hypotheses。
- [主来源 1](https://arxiv.org/abs/2509.20342)

## The gap between a variational problem and its occupation measure relaxation

- 原件 1377aa658f9785aa0a5e64970e7e842e8134804ca3d2fde2492864e30605d3c8。arXiv:2205.14132v4 (30 Apr 2026); local 55-page PDF carries the v4 arXiv identifier。物理页 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 49, 50。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。ESAIM: Control, Optimisation and Calculus of Variations 32 (2026), article 35, DOI 10.1051/cocv/2026018。
- 构件候选。This published source is a useful guard component, not a blanket exactness theorem: for scalar codomain and CV1-CV6 (or OC1-OC6), it proves equality of classical and relaxed minima; it also supplies explicit integral-constraint gaps and explains higher dimension/codimension gaps. The active E01's warning to recover a process only under proven conditions is consistent with it。
- 结论位置。Local pp. 8-15 state and derive the codimension-one no-gap result under CV1-CV6 and its optimal-control analogue under OC1-OC6; pp. 16-17 identify the decomposition proof mechanism; pp. 49-50 construct positive gaps from inequality/equality integral constraints。
- 适用范围。I checked theorem statements, their reduction, and the proof architecture, but did not independently rederive the full superposition theorem (Theorem 2.2) and all technical lemmas. The conditions require compact support, boundary constraints, the stated convexity/closedness assumptions, and scalar codomain。
- 相关技能。[math-e01-occupation-measure-flow-lp](../../../../math-e01-occupation-measure-flow-lp/SKILL.md)
- 其余依赖。Before integration, bind a separate E01 guard to CV1-CV6 or OC1-OC6 and state that integral constraints, n>1 with m>1, or missing conditions invalidate an exact-relaxation conclusion。
- [主来源 1](https://arxiv.org/abs/2205.14132) · [主来源 2](https://doi.org/10.1051/cocv/2026018)

## The height of discrete-time critical beta-splitting trees

- 原件 89e8f95a743b9fd78e706b94cad111a79287da48e0e7b4cb4fe25246a3ff842f。arXiv:2609.14329v2, dated 16 September 2026 in the local 14-page PDF。物理页 1, 10, 12, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.14329v2 (no published version identified)。
- 构件候选。The local v2 proves for the precisely defined discrete-time critical beta-splitting tree that its maximum root-to-leaf graph height divided by (log n)^2 converges almost surely and in L^p to the stated digamma constant. The proof inspected is not abstract-only: it couples to the interval fragmentation, bounds occupancies, uses the largest-fragment LLN, and constructs a nested lower-bound lineage。
- 结论位置。Local p. 1, Theorem 1.1, states the maximum-height limit; pp. 10 and 12 prove the largest-fragment and nested-fragment bounds used in Propositions 3.1--3.2; pp. 12--13 complete Theorem 1.1。
- 适用范围。This is an e-print-only maximum-height theorem for the exact critical beta-splitting construction. It does not prove the installed skill's uniform-cyclic-shift pair covariance, a uniform-leaf limit, CTCS time-height, or a theorem for another beta-splitting convention. Its proof explicitly imports the fragmentation asymptotic and occupancy inputs cited there。
- 相关技能。[probability-random-recursive-trees-asymptotics](../../../../probability-random-recursive-trees-asymptotics/SKILL.md)
- 其余依赖。Before integration, match the target's finite-n split law, labels and graph-height observable exactly, then independently check the cited fragmentation/occupancy prerequisites or use a published version of this e-print。
- [主来源 1](https://arxiv.org/abs/2609.14329)

## The Influence of Variables on Boolean Functions

- 原件 a82101996175d148c8d7fd36cc7776f70c13fe614b11c593267752d556113374。Local 16-page PDF, SHA-256 a82101996175d148c8d7fd36cc7776f70c13fe614b11c593267752d556113374; its pypdf text layer is font-encoded and does not expose title/authors/theorems。物理页 1, 2。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Kahn, Kalai and Linial, FOCS 1988 extended abstract, DOI 10.1109/SFCS.1988.21923; author-hosted primary PDF was read online。
- 引用核对。The checked primary KKL PDF verifies the uniform-cube influence/Fourier setting and Theorem 3.1's influential-coordinate scale under its stated Boolean/probability assumptions. The current skill uses it only as a partial, sharply bounded source and does not derive a Fourier-support or fixed-error coalition result from it。
- 结论位置。Local pp.1–2 were inspected but are text-layer unreadable. The checked author-hosted primary PDF gives title/authors on p.1 and Theorem 3.1 on its physical pp.4–5。
- 适用范围。No byte match could be made between the local unreadable PDF and the author-hosted source: an attempted direct primary-PDF SHA fetch timed out. Therefore the local artifact itself is not an independently legible theorem witness, and sharp constants/nonbalanced variants remain outside this card。
- 相关技能。[probability-boolean-fourier-invariance](../../../../probability-boolean-fourier-invariance/SKILL.md)
- 其余依赖。If a local-source identity is required, acquire the author-hosted/IEEE PDF and compare SHA or visually compare rendered pages; read the full source before upgrading any theorem-specific use。
- [主来源 1](https://www.ma.huji.ac.il/~kalai/kkl.pdf) · [主来源 2](https://ieeexplore.ieee.org/document/21923)

## The solution infinite horizon noncooperative differential game with nonlinear dynamics without the Hamilton-Jacobi-Bellman equation

- 原件 834c600bcf013121f5d970ee89cde42c6e00212b358487fb44d3b17967539ee2。Local PDF is arXiv:0901.1383v2 (31 Jan 2009), 65 pages; its 432 KB size and 2009-01-31 metadata agree with the official v2 record。物理页 1, 2, 14, 15, 16, 18, 19, 26, 29, 64, 65。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:0901.1383v2 (31 Jan 2009); no publisher version identified on the official arXiv record checked。
- 邻近材料。The official arXiv identity resolves the earlier provenance hold, but the inspected source is a deterministic/noncooperative differential-game proposal explicitly framed as avoiding HJB equations. Its “strong large deviations” statement is imported as [20], rather than proved in the inspected locus。
- 结论位置。Local PDF pp. 1–2 set up an infinite-horizon differential game; pp. 14–16 state Theorem 3.1.1 and attribute it to [20]; pp. 18–19 state the stochastic-game analogue; pp. 26 and 29 state model-specific theorems; pp. 64–65 were consulted for the citation list。
- 适用范围。It neither supplies E02’s nonlocal HJB supersolution comparison step nor a checked proof of the cited large-deviation claim. The active E02 SKILL does not cite it as an operative claim; its current provenance entry E0576 is explicitly pending。
- 相关技能。[math-e02-nonlocal-hjb-supersolution](../../../../math-e02-nonlocal-hjb-supersolution/SKILL.md)
- 其余依赖。No activation: any future use would need the primary source for reference [20], an assumption-by-assumption verification, and a demonstrated bridge to the E02 nonlocal supersolution setting。
- [主来源 1](https://arxiv.org/abs/0901.1383)

## The Unfair 0-1 Polynomial Problem and High-Degree Trinomials

- 原件 7390a9720609c1263ed89b01c2e392d4e7e3f33b7f6a940455723e92cf23a268。local byte-checked arXiv:2608.19173v2, 53 physical pages, dated September 2026。物理页 1, 3, 46。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.19173v2 (preprint; no peer-reviewed version identified in the checked primary record)。
- 构件候选。The checked v2 preprint states the high-degree claim precisely: for k>=341 and 0<a<1, no nonzero nonnegative-coefficient Q can make (1+a x^2+x^k)Q a 0--1 polynomial. The terminal proof explicitly invokes the pre-zero estimate (Theorem 8.1), deterministic continuation (Lemma 9.1), and negative terminal coefficient (Lemma 10.2). This is a potentially useful finite-constructor/exclusion route for that trinomial family only。
- 结论位置。Abstract on p.1; Theorems 1.1--1.2 and even-k reduction on p.3; proof of Theorem 1.2 and its dependency chain on p.46。
- 适用范围。The full-family statement also imports bounded odd degrees from a companion manuscript. For the high-degree preprint, the terminal chain depends on earlier analytic/theta estimates and author-reported outward-rounded interval endpoint certificates; those certificates and all prerequisite estimates were not independently rerun in this adjudication. It is not a theorem for arbitrary nonnegative factors。
- 相关技能。[probability-integer-polynomial-factorization](../../../../probability-integer-polynomial-factorization/SKILL.md)
- 其余依赖。Independently audit Theorem 8.1, Lemmas 9.1 and 10.2, and the Appendix A--B interval-certificate inputs, then verify the companion source before relying on the all-k>=7 combination。
- [主来源 1](https://arxiv.org/abs/2608.19173)

## Tight Asymptotic of Probability of Singularity of n x n Random Matrix with Uniform Distributed ±1 Entries

- 原件 71ea8a10c878f0f571a2bcdb35e7946b19a48b4e232cbfcb96436b11d37f8f9a。Earlier card recorded arXiv:1511.05283v7 (26 Oct 2025); the 9-page local PDF identifies the same version on p. 1。物理页 1, 2, 3, 4。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:1511.05283v7, Vladimir Blinovsky, last revised 26 Oct 2025; no journal version was identified from the checked arXiv primary record。
- 邻近材料。The source asserts a Bernoulli ±1 random-matrix singularity asymptotic, whereas K01 requires local correlation scales, marginal moderate-deviation tails, conditional local-field limits, and cross-block control for a threshold-indexed field. K01 contains no active use of this paper or of its claimed asymptotic。
- 结论位置。Local pp. 1 and 4 state Theorems 1–2; pp. 2–3 give the low-support inclusion–exclusion lower-bound calculation. The checked arXiv record identifies the v7 revision history。
- 适用范围。Reading pp. 1–4 does not independently certify the paper’s global upper-bound proof; it also supplies none of K01’s asymptotically Gaussian-field hypotheses。
- 相关技能。[math-k01-chan-lai-asymptotically-gaussian-fields](../../../../math-k01-chan-lai-asymptotically-gaussian-fields/SKILL.md)
- 其余依赖。No active K01 dependency to repair. Any future use of the singularity asymptotic needs a separate full proof/dependency audit against the v7 source。
- [主来源 1](https://arxiv.org/abs/1511.05283)

## Typical Behavior of the Harmonic Measure in Critical Galton–Watson Trees with Infinite Variance Offspring Distribution

- 原件 c217027d272b0be4a8c9cf2f72e2ccf451edd8540b4d883115daf971cfef17fe。local 35-page manuscript, originally unidentified。物理页 1, 2, 3, 4, 5。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:1603.01200v2 [math.PR], 25 Feb 2017 (arXiv notes Proposition 4 corrected)。
- 已有技能。The local 35-page PDF matches the current arXiv record by title, author, page count and v2-era content. Theorem 1 is a finite-height critical Galton–Watson result: for mean-one offspring in the stable domain α∈(1,2], a uniformly selected height-n vertex has harmonic mass of order n^(−λα). The release’s narrow route is verified by Theorem 2: on the same reduced stable-tree boundary, the local exponent λα is at branching-measure-typical rays, while Corollary 3 separates it from the harmonic-typical exponent βα imported from distinct reference [10]。
- 结论位置。Theorem 1 on physical p. 2; the reduced-stable-tree construction and Theorem 2 on pp. 3–4; Corollary 3 and its imported exponent on p. 5。
- 适用范围。This does not create an infinite-tree Shannon–McMillan theorem or compare arbitrary coded measures. Corollary 3’s harmonic-typical exact-dimension ingredient is external (Lin 2014, cited as [10]); only the source-stated separator under its common stable-tree setting is supported。
- 相关技能。[probability-harmonic-measure-coding](../../../../probability-harmonic-measure-coding/SKILL.md)
- 其余依赖。If relying on Corollary 3 rather than only the branching-measure local-dimension route, independently inspect [10, Theorem 1.2] and preserve its stable-tree metric and measure hypotheses。
- [主来源 1](https://arxiv.org/abs/1603.01200) · [主来源 2](https://arxiv.org/pdf/1603.01200)

## Universality and Sharp Matrix Concentration Inequalities

- 原件 49428efe87cf9ca81eff7fcca32d704f261493a7090b7224d228bec4d25b5d7a。arXiv:2201.05142v3 (25 June 2024), 89-page local PDF。物理页 1, 8, 11, 57, 58, 59, 60, 61。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Geometric and Functional Analysis 34 (2024), 1734–1838, DOI 10.1007/s00039-024-00692-9; the checked local source is arXiv v3。
- 已有技能。The route’s W12-011 statement is supported: for a deterministic plus independent centered self-adjoint sum X, Theorem 2.6 compares sp(X) and the covariance-matched Gaussian G in two-sided Hausdorff distance with the stated sigma_*, sigma and R error terms. The current SKILL.md and references/method.md preserve this as a matrix-specific comparison, not a tensor type-2 theorem。
- 结论位置。Local physical p. 8 defines the independent self-adjoint model; p. 11 states Theorem 2.6; pp. 57–61 prove its two spectral inclusions via resolvents and combine them into the Hausdorff bound。
- 适用范围。The source concerns self-adjoint finite-dimensional independent summands; non-self-adjoint use is only through the stated dilation/singular-value reduction. It does not give a complex-eigenvalue claim, arbitrary dependence, or a Hausdorff comparison to the free model; its Theorem 2.16 is a different one-sided inclusion。
- 相关技能。[probability-random-matrix-tensor](../../../../probability-random-matrix-tensor/SKILL.md)
- [主来源 1](https://arxiv.org/abs/2201.05142) · [主来源 2](https://doi.org/10.1007/s00039-024-00692-9)

## Viscosity Solutions of Stochastic Hamilton–Jacobi–Bellman Equations with Jumps

- 原件 2d74c3b1dfea5078c296371087c33385019be410631aad2a1b17334de9368673。Local PDF metadata identifies arXiv:2605.20593v1, 31 pages。物理页 1, 2, 5, 10, 17, 23, 28, 29, 30, 31。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2605.20593v1 (20 May 2026); no publisher version is listed on the official arXiv record checked。
- 待核。Identity and exact v1 provenance are now recovered. However, the global-uniqueness argument invokes L-infinity weighted convergence after an L2 approximation: p.29 derives only almost-sure eventual bounds with an omega-dependent index from Borel–Cantelli, then asserts uniform-in-omega/L-infinity convergence. That implication is not established by the displayed estimates。
- 结论位置。Local pp. 1–2 give the claimed BSHJB framework; p. 5 states the jump exponential-integrability condition; p. 10 gives the DPP/equation; pp. 17 and 23 develop weak comparison; pp. 28–29 are the uniqueness/approximation proof; pp. 30–31 give cited background。
- 适用范围。Thus the inspected pp.23–29 do not independently support the claimed global uniqueness/weak-comparison transfer. E02 has no active claim depending on this paper: its provenance E0597 remains pending, so no live skill conclusion needs retraction。
- 相关技能。[math-e02-nonlocal-hjb-supersolution](../../../../math-e02-nonlocal-hjb-supersolution/SKILL.md)
- 其余依赖。Require a corrected uniform/essential-supremum approximation lemma or a uniqueness proof that works with the available almost-sure/L2 control before any E02 dependency can be activated。
- [主来源 1](https://arxiv.org/abs/2605.20593)

## Weighted Chernoff Information and Optimal Loss Exponent in Context-Sensitive Hypothesis Testing

- 原件 d71c2862a1947b0bcef83dde64f1762a5471925b2ab00ee0ca8709807cbec967。arXiv:2603.08308v3 [math.ST], 9 May 2026 (local PDF p. 1)。物理页 1, 6, 8, 9, 24, 25。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Entropy 2026, 28(5), 536; DOI 10.3390/e28050536 (publisher page checked)。
- 引用核对。Under i.i.d. P^⊗n versus Q^⊗n, a nonnegative product-factorized context weight, positive finite weighted affinities and the displayed uniform log-likelihood integrability condition, Theorem 3.1 proves the logarithmic weighted-loss exponent. Its proof uses factorization for the upper bound and a tilted law plus LLN for the matching lower exponent; the M-ary statement reduces to finitely many such pairwise problems。
- 结论位置。Local PDF p. 1 gives publication/DOI and e-print version; p. 6 states product-factorized weight and positive finite weighted-normalizer assumptions; Theorem 3.1 and proof are on pp. 8–9; Theorem 4.7 and its pairwise-reduction proof are on pp. 24–25。
- 适用范围。This is a narrowly weighted hypothesis-testing exponent, not H05’s generic Hoeffding/Bernstein bound and not I01’s conditional-moment result. It cannot be invoked without every factorization, integrability and i.i.d. condition。
- 相关技能。[math-h05-chernoff-hoeffding-bernstein](../../../../math-h05-chernoff-hoeffding-bernstein/SKILL.md)
- 其余依赖。No active H05 operational conclusion depends on this paper; it remains a cited narrow comparison. Any adoption needs an application-specific check of all Theorem 3.1 hypotheses。
- [主来源 1](https://arxiv.org/abs/2603.08308) · [主来源 2](https://www.mdpi.com/1099-4300/28/5/536)
