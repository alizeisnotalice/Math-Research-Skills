# 分析、Fourier 与几何

按原件哈希区分。每条核查保留本机物理页与对应来源。

## A High-Frequency Uncertainty Principle for the Fourier–Bessel Transform

- 原件 d327d8a324d062693d23d742ade9307da898cbafb1685fbc57e8fa7596c2de9b。arXiv:2509.25500v2 (29 Apr 2026), 18-page local PDF。物理页 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 16。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Jaye and Sethi, Journal of Fourier Analysis and Applications 32, Article 48 (2026), DOI 10.1007/s00041-026-10252-4; published 20 Apr 2026。
- 邻近材料。The preprint/version issue is resolved: the local v2 result is now a 2026 published Fourier–Bessel high-frequency sampling theorem. The proof supports the exact source statement for alpha>-1/2, mu_alpha-relative density, and Fourier–Bessel support in [R,R+1] for sufficiently large R; the finite-union extension additionally assumes alpha-1/2 is a nonnegative integer。
- 结论位置。Local pp. 1–4 state Theorems 1.3, 1.6, and 1.8 with their Fourier–Bessel/radial density hypotheses; pp. 5–9 prove Theorem 1.3 through density equivalence, Bessel asymptotics, Kovrijkine's multi-interval theorem, and error absorption; pp. 11–16 show the separate finite-union argument. The official arXiv and journal records recover the canonical publication。
- 适用范围。It is not a tensor-kernel Fourier-positivity or soft-square supremum result. Its observability inequality is L2, Fourier–Bessel/radial, unit-band, and density dependent; its proof imports Bessel asymptotics and a Logvinenko–Sereda theorem rather than giving positivity of a spatial tensor kernel. Thus it cannot justify an F02 positivity/maximal claim。
- 相关技能。[math-f02-tensor-fourier-positivity-soft-square-supremum](../../../../math-f02-tensor-fourier-positivity-soft-square-supremum/SKILL.md)
- 其余依赖。No active F02 claim relies on this source (the current provenance table already labels it irrelevant). Any new uncertainty-principle component must retain the transform, support-band, density, and alpha restrictions and be integrated separately。
- [主来源 1](https://arxiv.org/abs/2509.25500) · [主来源 2](https://doi.org/10.1007/s00041-026-10252-4)

## A note on maximal commutators and commutators of maximal functions

- 原件 41d531dd5399f3fea0341af36d3351036c5b811fd5077c93ad92e6438aff513d。arXiv:1210.6778v2 (11 Jun 2013)。物理页 1, 2, 3, 4。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Journal of the Mathematical Society of Japan 67(2) (2015), 581–593, DOI 10.2969/jmsj/06720581。
- 邻近材料。The published identity is verified through the journal DOI and the local arXiv copy states pointwise iterated-maximal-function control for BMO maximal commutators. The active F06 claim instead concerns finite ordered L2-orthogonal partial sums and its dyadic proof does not invoke commutators。
- 结论位置。Local PDF pp.1–4: definitions and Theorems 1.1–1.3; pp.3–4 state the M-delta(C_b f) and C_b f pointwise bounds by M squared f under BMO hypotheses。
- 适用范围。The paper's BMO symbol, cube maximal operator, and maximal commutator are different objects from F06 partial sums; neither Theorem 1.2 nor the additional bounded-negative-part condition for the maximal-function commutator transfers to F06。
- 相关技能。[math-f06-menshov-rademacher-maximal-partial-sums](../../../../math-f06-menshov-rademacher-maximal-partial-sums/SKILL.md)
- 其余依赖。None; a commutator-specific harmonic-analysis skill would need the full published hypotheses and endpoint statements。
- [主来源 1](https://doi.org/10.2969/jmsj/06720581) · [主来源 2](https://arxiv.org/abs/1210.6778)

## Almost Everywhere Convergence of Mock Fourier Series for the Middle-Fourth Cantor Measure

- 原件 c0bccdafb2038f83254f1b0c3c9e6bd8b473515b7fc59102f027f39a557ce1e2。local arXiv:2607.27796v2 (31 Aug 2026), 15 physical pages。物理页 12, 13, 14。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2607.27796v2; no formal publication identified in the checked authoritative record
- 已有技能。Independent transfer: on a finite measure space, nonnegative operators T_r satisfying mu{T_r f>t}<=C_r||f||_1/t and positive weights a_r with sum sqrt(a_r C_r)<infinity obey mu{sum a_r T_r f>t}<=t^(-1)(sum sqrt(a_r C_r))^2||f||_1. The source's displayed union-bound proof was checked. This is a general weak-type aggregation lemma suitable as a guarded helper, not a statement about its Cantor Fourier system.
- 结论位置。Lemma 5.1 on pp.12–13 proves the weighted weak-(1,1) aggregation. Its proof covers the level set by the union {T_r f > alpha c_r/a_r}, then minimizes sum a_r C_r/c_r over positive c with sum c=1. The Cantor convergence application begins below it and uses additional spectral input.
- 适用范围。Requires nonnegative extended-valued outputs, each stated weak-(1,1) estimate, convergence of the weighted sum, and a finite measure space. It gives no orthogonality estimate, no maximal theorem for signed/complex cancellation, and no almost-everywhere convergence without a separate dense core and weak-type maximal argument.
- 相关技能。[math-f06-menshov-rademacher-maximal-partial-sums](../../../../math-f06-menshov-rademacher-maximal-partial-sums/SKILL.md)
- 已采用构件。非负算子的给定分量弱型界与阈值预算，用有理数核验有限并集上界。 [math-f06-menshov-rademacher-maximal-partial-sums](../../../../math-f06-menshov-rademacher-maximal-partial-sums/references/weighted-weak-aggregation.md)
- 其余依赖。A release component should implement a finite rational witness for the constants/weights and retain the proof contract for countable limits, or be added as a reference lemma to the existing F06 maximal-partial-sums route after checking callers need positive aggregation.
- [主来源 1](https://arxiv.org/abs/2607.27796)

## Best constants for a family of Carleson sequences

- 原件 1525e1c76bb1a99160227f259bf63781bb0483ee2c30dbc8b7ec163605252407。2014 manuscript; earlier card had no verified publication identity。物理页 1, 3, 4, 5。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Leonid Slavin, Advances in Mathematics 289 (2016), 685--724, doi:10.1016/j.aim.2015.11.004。
- 邻近材料。The recovered publication concerns Carleson norms of specific sequences c_Phi,J(w) built from dyadic A2 weights. Local Theorem 2.6 gives its stated Carleson/A2 implications only for increasing Phi (with the displayed divergence condition for the converse); p. 4 explicitly says the h-concave upper estimate is merely best known and likely nonsharp。
- 结论位置。Local pp. 1, 3--5: dyadic A2 setup, Theorems 2.1/2.3 and Theorem 2.6; publisher identity checked at DOI/publisher record。
- 适用范围。This does not define the active skill's private TC-A4 tree, its coefficient normalization, or its square function. The active G05 procedure relies instead on its separately named standard binary embedding theorem; no active claim depends on Slavin's sharp constants。
- 相关技能。[math-g05-tree-carleson-square-function-tc-a4-audit](../../../../math-g05-tree-carleson-square-function-tc-a4-audit/SKILL.md)
- 其余依赖。No integration action: retain as an adjacent weighted-dyadic reference; any future reuse must map c_Phi,J, Phi, dyadic A2 and the exact theorem branch。
- [主来源 1](https://doi.org/10.1016/j.aim.2015.11.004) · [主来源 2](https://www.sciencedirect.com/science/article/pii/S0001870815004533)

## Concentration of the Ratio between the Geometric and Arithmetic Means

- 原件 aa9f44a843a615b40fe673bb6e9d0093cca63f7cd5c75e3694599eea1d3e104e。arXiv:0807.4832v1 (30 Jul 2008), 10-page local PDF。物理页 1, 3, 4, 8, 9。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Aldaz, Journal of Theoretical Probability 23(2) (2010), 498–508, DOI 10.1007/s10959-009-0215-9。
- 邻近材料。The checked theorem is a valid asymptotic concentration result: for its normalized weight arrays bounded above by M and Haar-uniform points on the corresponding weighted Euclidean sphere, the weighted GM/AM ratio lies near e^(-gamma) divided by the weighted geometric-mean factor with probability at least 1-n^(-k). Equal weights yield the e^(-gamma) specialization。
- 结论位置。Local p. 1 gives the source identity; p. 3 states Theorem 2.1 for uniformly bounded normalized weights on weighted Euclidean spheres; p. 4 gives alternate concentration levels; pp. 8–9 supply the finite-dimensional optimization lemma and the Gamma/Stirling-Chebyshev proof step. The arXiv record and journal DOI recover publication identity。
- 适用范围。The current F01 route requires an explicitly defined nonnegative GP-BRANCH kernel and two-winner coverage. This paper has neither a winner map nor a pointwise kernel/branch inequality; its sphere law, normalized weights, and asymptotic dimension quantifiers cannot be dropped. Its gamma occurrence is unrelated to gamma irrationality。
- 相关技能。[math-f01-geometric-mean-kernel-two-winner-audit](../../../../math-f01-geometric-mean-kernel-two-winner-audit/SKILL.md)
- 其余依赖。A future component would need the actual GP-BRANCH interface plus a finite-dimensional kernel inequality or an independently proved link from the sphere concentration model. The paper should remain non-active for F01。
- [主来源 1](https://arxiv.org/abs/0807.4832) · [主来源 2](https://doi.org/10.1007/s10959-009-0215-9)

## Decoupling Inequalities for Quadratic Forms

- 原件 618899b2865aad01cd8d7db6eb4b369b6bbaf16a35442525c5b6f496ad90631c。local PDF matches arXiv:2011.09451v2 (5 Feb 2022; 37 pages)。物理页 1, 4, 5。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Guo, Oh, Zhang, Zorin-Kranich, Duke Mathematical Journal 172(2) (2023), 387–445, DOI 10.1215/00127094-2022-0033。
- 邻近材料。The published paper identifies sharp ell^q L^p decoupling exponents for quadratic-form graphs through the d_{d1,n1}(Q) invariants, with explicit nondegeneracy corollaries. The local PDF agrees with the checked arXiv v2 record, which supplies the Duke journal identity and DOI。
- 结论位置。p. 1, definition of the extension operator; pp. 4–5, Theorem 1.1 and Corollaries 1.2–1.5。
- 适用范围。G03’s active operation is finite Hermitian/PSD matrix arithmetic and refuses undefined private capture-tree/source-to-Gram/common-input interfaces. A Fourier extension decoupling theorem for quadratic manifolds supplies none of those missing interfaces。
- 相关技能。[math-g03-directional-capture-tree-quadratic-audit](../../../../math-g03-directional-capture-tree-quadratic-audit/SKILL.md)
- 其余依赖。A separate integration would require an explicitly defined quadratic graph Q, verified d_{d1,n1}(Q) invariants, and a demonstrated reduction from the requested problem to its Fourier extension estimate。
- [主来源 1](https://arxiv.org/abs/2011.09451) · [主来源 2](https://doi.org/10.1215/00127094-2022-0033)

## Dimension-free estimates for discrete maximal functions over cubes in Z^d

- 原件 01a4d818f5fb3fd69257039b3189812d48d3c13fe5614913b083bc23f724a701。local arXiv:2609.24030v1 (21 Sep 2026), 9 physical pages。物理页 3, 4, 5, 6, 7, 8。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2609.24030v1; no formal publication identified in the checked authoritative record
- 已有技能。Independent transfer: for affine factors z_j(s) with |z_j(s)|<=exp(-c u_j) and |partial_s z_j(s)|<=7u_j, 0<=u_j<=1, the k-th derivative of product_j z_j(s) is uniformly bounded by 7^k e^{ck} sup_{U>=0}e^{-cU}U^k, independently of the number of factors. The source proof is a finite product-rule and nonnegative symmetric-sum estimate and was checked directly.
- 结论位置。Lemma 2.1 on pp.3–4 supplies |b_N-a_N|<=7(1-|a_N|). Proposition 3.1 on pp.4–5 differentiates the tensor product exactly and bounds it by 7^k e^{ck}e^{-cU}U^k. Proposition 4.1 on pp.6–8 requires a separate interpolation framework.
- 适用范围。This tensor-multiplier certificate needs the supplied factor bounds and a fixed c>0. It has no implication for a maximal function, Fourier positivity, weak-(1,1), or the source's p>1 interpolation theorem without separately checking the convolution and interpolation hypotheses.
- 相关技能。[math-f02-tensor-fourier-positivity-soft-square-supremum](../../../../math-f02-tensor-fourier-positivity-soft-square-supremum/SKILL.md)
- 已采用构件。在给定逐因子阻尼与导数条件下，核对有限权重对称和及维数无关符号界。 [math-f02-tensor-fourier-positivity-soft-square-supremum](../../../../math-f02-tensor-fourier-positivity-soft-square-supremum/references/product-derivative-certificate.md)
- 其余依赖。Implement a rational/interval checker for supplied u_j,c and affine factor bounds, then connect it to F02 only for tensor multiplier tasks that expose those hypotheses.
- [主来源 1](https://arxiv.org/abs/2609.24030) · [主来源 2](https://arxiv.org/html/2609.24030v1)

## Distance Stability for the Integral Hardy and Carleman Inequalities

- 原件 b270e46ae6c105456c18588a04f9667e1e8bd4679667fbf91471d6b285c7e522。arXiv:2606.15056v1; local 9-page PDF marked 13 June 2026。物理页 3, 4, 5。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2606.15056v1; official arXiv record checked and lists v1 only
- 已有技能。Independent transfer: for nonnegative compactly supported locally bounded f, the integration-by-parts identity gives the exact nonnegative Hardy deficit integral h^p Phi_p(p' f/h), h=Hf. For p=2 it gives the square residual identity 4||f||_2^2-||Hf||_2^2=||2f-Hf||_2^2; density extends it to nonnegative L2 inputs. The local finite-log Poincare consequence needs its interval stated separately.
- 结论位置。Theorem 1 on pp.3–4 integrates d/dx[x(Hf)^p] with vanishing endpoints. Theorem 2 on p.4 specializes it to 4 integral f^2 minus integral (Hf)^2 = integral (2f-Hf)^2. The finite-log comment is on p.5.
- 适用范围。Virtual profiles x^(-1/p) are outside global Lp, so the identity alone gives neither global distance to extremizers nor compactness. Signs, endpoint terms, and the nonnegative real setting must be retained. This source is an unrefereed v1.
- 相关技能。[math-m03-near-extremizer-stability](../../../../math-m03-near-extremizer-stability/SKILL.md)
- 已采用构件。对有理阶梯函数逐段计算二次亏损、精确对数项与完整尾积分。 [math-m03-near-extremizer-stability](../../../../math-m03-near-extremizer-stability/references/hardy-quadratic-deficit.md)
- 其余依赖。A release helper needs exact piecewise-constant or rational compact-support integration and a checked density/endpoint extension. Any distance statement must separately provide a finite logarithmic interval and Poincare normalization.
- [主来源 1](https://arxiv.org/abs/2606.15056)

## Errata and Addenda to Enumerative Combinatorics, Volume 1

- 原件 3b9670f7863953d84377bbcfafa109254a4f9e352032d083afae6c6b2b02f8ec。Exact local 8-page scan; physical p. 1 identifies errata for Volume 1 and refers to the 1997 hardcover second printing。物理页 1, 2。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。not identified: the official EC1 site has a current 2025 Volume-1 errata record, but the local historic errata sheet must not be merged with it without a byte/version comparison
- 邻近材料。Raw SHA and eight-page count match. The local bytes are an errata-and-addenda sheet for Stanley's Enumerative Combinatorics, Volume 1, not the Volume 2 book asserted by the filename/input title. The checked official EC1 page independently confirms that the author maintains Volume-1 errata, but no local theorem or source locator for the poset-counting skill is present.
- 结论位置。Visual inspection of local physical p. 1 identifies the document and its Volume-1/1997 scope; p. 2 continues correction entries
- 适用范围。Individual corrections cannot be used as a poset-counting/sampling theorem, and neither the intended book edition nor the particular corrected statement is identified. No active probability-poset-counting-sampling claim cites this record.
- 其余依赖。If a book theorem is needed, recover the intended EC volume/edition and its theorem locator, then consult the matching errata version before relying on it.
- [主来源 1](https://math.mit.edu/~rstan/ec/ec1/)

## Estimates for maximal Fourier multiplier operators on R^2 via square functions

- 原件 f03ee0918e2aa99090bd82b94367a4f278a23a54beaaa239728c840a3931afe9。arXiv:2508.00279v2 (local PDF dated 9 March 2026)。物理页 1, 2, 3, 5, 8, 11, 12, 13, 14, 15, 19。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Mathematical Inequalities & Applications 29 (2026), no. 1, 47–73 (publisher record checked; DOI not displayed)。
- 邻近材料。The current local v2 has a verifiable publication identity and proves L^4 and L^2 estimates for special curved multiplier square functions on R^2, assuming compact support away from zero, the transversality condition ψ(t)-tψ'(t)≠0, and curvature where required. The proof uses geometry of dilates and finite-direction/Kakeya-maximal estimates。
- 结论位置。PDF pp. 1–3 state the curved Bochner–Riesz multiplier hypotheses and the L^4/L^2 square-function theorems; pp. 5 and 8–14 prove the localized vector-valued square-function estimate using finite direction sets; pp. 15 and 19 reduce the maximal multiplier theorem to the curved square-function bounds。
- 适用范围。This repairs the former identity hold but not the mathematical mismatch: it is not Rubio de Francia's one-dimensional arbitrary-disjoint-interval projection theorem and supplies no G04 spatial-tree or overlap conclusion. Its curvature, support, and endpoint assumptions must remain attached to any separate citation。
- 相关技能。[math-g04-rubio-de-francia-square-function-scope-check](../../../../math-g04-rubio-de-francia-square-function-scope-check/SKILL.md)
- [主来源 1](https://arxiv.org/abs/2508.00279) · [主来源 2](https://mia.ele-math.com/29-03/Estimates-for-maximal-Fourier-multiplier-operators-on-R-2-via-square-functions)

## Exact Limits of Random Projections for Preserving Geometry: Distance Recovery, Nearest-Neighbor Rankings, and Covariance Shape in Gaussian Models

- 原件 be320e51bb1c62b142dbd19e456ea2907de87d9e4797884fd42287e97a877df7。Local PDF: arXiv:2609.02155v1 (2 Sep 2026)。物理页 1, 3, 4。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.02155v1 (only version listed by the official arXiv record)。
- 邻近材料。The official arXiv record verifies Piyush Sao, v1 identity and the 41-page preprint. Local Proposition 3.1 constructs an independent Gaussian replacement map that can meet the stated sample JL event while I(X^n;Y^n)=0; Proposition 2.1 only gives an order guarantee when the displayed relative margin exceeds epsilon。
- 结论位置。Local pp. 3–4, Proposition 2.1 and Proposition 3.1; official arXiv abstract and v1 record。
- 适用范围。This is Gaussian random-projection information theory, not a filtered-process projection or predictable-compensator theorem; no I02 active claim relies on it. I verified the local v1 label and matching bibliographic identity, but did not byte-compare an official PDF。
- 其余依赖。No dependency should be added to I02. Any geometric-sketch tool would need the Proposition 3.1 supplement proof and its Gaussian/i.i.d. hypotheses reviewed。
- [主来源 1](https://arxiv.org/abs/2609.02155)

## Exponent-one blockers and a Mordell-Weil construction of Euler bricks

- 原件 ac40a21b9e3912051a54831bd97db514c1d5e01613daab59a2086c0a4de14dba。arXiv:2605.00573v1, submitted 1 May 2026。物理页 1, 2, 10, 11, 12, 13, 18, 19, 20。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2605.00573v1 (only version listed on the checked primary arXiv record; local PDF front matter matches v1)。
- 邻近材料。The source is about Euler bricks/perfect cuboids, not Euler's constant or oscillatory/geometric remainders. Its reported exponent-one blocker assertion is explicitly a conjecture verified only on the stated factored database, while the Mordell--Weil generator's output correctness is a separate finite conditional-algorithm statement. Thus it supports no active N03 claim。
- 结论位置。PDF pp. 1--2 identify Conjecture 4.1 as empirical and describe the finite database; pp. 10--13 distinguish the conditional blocker implications from the data verification; pp. 18--19 state reproducibility materials and an internal exact-arithmetic consistency check; p. 20 lists references。
- 适用范围。The ancillary database/code were listed on the checked arXiv record but were not executed or byte-audited here; neither the finite empirical check nor the open Conjectures 4.1/4.14 proves nonexistence of perfect cuboids or any general arithmetic conclusion。
- 相关技能。[math-n03-oscillation-and-geometric-remainder](../../../../math-n03-oscillation-and-geometric-remainder/SKILL.md)
- 其余依赖。If an Euler-brick computational skill is ever desired, download and hash the ancillary release, run the named verification targets with recorded software versions, and separately retain all conjectural claims as conjectural。
- [主来源 1](https://arxiv.org/abs/2605.00573)

## Extremizers and Stability for Fractional Lp Uncertainty Principles

- 原件 c05bae927a4799b1a0a0ac1681382112a0c77ed2b55c9d28ec934f234115bde1。local arXiv:2504.16245v1, dated 22 April 2025 on physical p. 1。物理页 1, 16, 17, 19, 20, 21, 22, 24, 25, 28, 29, 30。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。local PDF identifies arXiv:2504.16245v1; the assigned byte identity is confirmed
- 待核。The controlling p.22 transfer is false in the stated generality, independently of the missing variational assumptions. In the concrete p=beta=2, alpha=1 instance, g_R=1_[R,R+1] has ||g_R||_2=1 but ||x g_R||_2^2=R^2+R+1/3, so multiplication by |x| is not a bounded Lp-to-Lbeta map. The same problem is compounded by the paper's explicit assumptions of a coercive second variation on pp.19--21. Exact arithmetic reproduced the displayed norm.
- 结论位置。pp.16--17 assert uniqueness and a stability estimate; pp.19--21 explicitly assume existence and coercivity of the second variation; p.22 claims global Lp-to-weighted bounds; pp.24--25 use an unproved bounded oscillatory kernel; pp.28--30 insert an unspecified weighted-to-Sobolev comparison.
- 适用范围。No M03 stability, extremizer existence, weighted-profile, dispersive, or Sobolev-constant theorem can use this PDF. The installed M03 elementary deficit identity remains independent of it.
- 相关技能。[math-m03-near-extremizer-stability](../../../../math-m03-near-extremizer-stability/SKILL.md)
- 其余依赖。A usable replacement must state a parameter regime and domains, prove extremizer existence and nondegeneracy modulo symmetries, and replace the false global weighted bounds with valid graph-norm estimates; re-audit a corrected edition before transfer.
- [主来源 1](https://arxiv.org/abs/2504.16245)
- 复核记录。2026-11-26T18:11:16+08:00。hold。dependency。
- 本次依据。The source's transfer from an unweighted Lp norm to a weighted norm is false in its stated generality, and the stability route separately assumes extremizer existence and coercivity of a second variation. It cannot supply an M03 theorem.。定位。Stability claims (pp. 16--17); variational assumptions (pp. 19--21); global weighted transfer (p. 22); later kernel/Sobolev uses (pp. 24--30)。全卷 32 页。后续条件。A corrected edition must give a parameter/domain-specific graph-norm estimate, extremizer existence, and nondegeneracy modulo symmetries before re-review.。

## Finite-dimensional Approximations of Push-forwards on Locally Analytic Functionals

- 原件 8422f6c542ce2dff8d646077b841f7f321365f59be13f8b406b1d1e93bd387ca。arXiv:2404.10769v1 (16 Apr 2024)。物理页 1, 4, 5, 16, 17, 19, 20。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2404.10769v4 (21 Apr 2026); local PDF labels v4 and the checked arXiv record says v4 revised matrix conventions and the approximation/reconstruction statements。
- 邻近材料。Raw SHA and 31-page count match. The primary record identifies the local file as the revised v4 (not merely an unspecified 2024 manuscript) and records material statement/convention revisions. The inspected proofs support finite-dimensional approximation and analytic-map reconstruction under compact absolutely convex neighborhoods, analytic maps, absolutely continuous sampling measures, moment-matrix conditioning, and sample-size conditions. These are push-forward approximation results, not selection results。
- 结论位置。Theorem 1.1 on local p. 4 with proof p. 17; Theorem 1.3 on p. 5 with proof p. 20; underlying Theorems 4.7 and 5.1 on pp. 16 and 19。
- 适用范围。No inspected theorem establishes measurable supremum, analytic projection, measurable argmax, or a selector for a multifunction. Its analytic/Fock-space and moment-matrix hypotheses do not match M04's general selection interface, so the earlier candidate classification must not be used as evidence for an active M04 claim。
- 相关技能。[math-m04-measurable-supremum-selection](../../../../math-m04-measurable-supremum-selection/SKILL.md)
- 其余依赖。A separate theorem linking a specific measurable multifunction/optimization problem to this analytic push-forward framework would be needed before any M04 integration; absent that bridge it remains adjacent only。
- [主来源 1](https://arxiv.org/abs/2404.10769)

## Fourier transform of vector-valued graph signals

- 原件 a404dc2b29e56805c62928b361abc6fecebd1d09acf138122e959c162472826a。Local 39-page PDF by Antonio Caputo; it has no version banner, and its physical pagination differs from the checked current arXiv v2 record (38 pages)。物理页 1, 2, 3, 11, 13, 14, 15, 20, 25, 30, 37, 38, 39。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2505.22325v2 (27 Feb 2026); no journal publication identified on the checked primary record。
- 邻近材料。The local manuscript proves norm identities/estimates for transforms generated by a chosen orthonormal basis of a finite graph and, in the Hilbert-valued case, its p.15 Parseval calculation. The active F02 provenance record already classifies this finite graph-spectral framework as irrelevant, and the active skill does not rely on it。
- 结论位置。Finite-graph setup, pp. 1–3; operator-norm theorems and proofs, pp. 11, 13–15; graph convolution/translation sections, pp. 20, 25, 30; conclusion and references, pp. 37–39。
- 适用范围。A finite graph basis transform, with constants depending on the graph/basis, is not an LCA-group convolution kernel, a tensor positive-definiteness statement, a Fourier-positivity result, or a dimension-uniform soft-max estimate. The local PDF is not byte-identified with the current v2 primary version, so no version-sensitive theorem is imported。
- 相关技能。[math-f02-tensor-fourier-positivity-soft-square-supremum](../../../../math-f02-tensor-fourier-positivity-soft-square-supremum/SKILL.md)
- 其余依赖。None for the active F02 route; any future graph-signal component must first byte-identify a chosen arXiv version and specify the finite graph, basis, Banach/Hilbert target, and norm convention。
- [主来源 1](https://arxiv.org/abs/2505.22325) · [主来源 2](https://arxiv.org/html/2505.22325v2)

## Linear Programming over Exponent Pairs

- 原件 b229047f8662ec4ed0e2a952c380f4627155252753f636f4cc29c90b0282c3d7。local arXiv:1402.1993v2, dated 23 December 2014 on physical p. 1。物理页 1, 2, 6, 7, 8。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。published Acta Universitatis Sapientiae, Informatica 5(2) (2013), 271--287, DOI 10.2478/ausi-2014-0014; assigned local source is arXiv:1402.1993v2
- 待核。The finite contraction calculation is valid: p.6 bounds ||A p-A q||^2 by (3/4)||p-q||^2 (and B is an isometry, so BA shares the bound). This proves only eventual diameter control. It does not certify any numerical output: p.7 expressly records failure of the greedy constrained modification, and p.8 leaves R(V,LC), outer polygons, stopping tolerance, and the claimed PARI/GP output without a frozen rational enclosure. The exact check script records the contraction constant.
- 结论位置。pp.1--2 define the constrained problem and projective A/BA maps; p.6 proves the sqrt(3)/2 contraction estimate; pp.7--8 explicitly say greedy constrained search can miss optima and give an accuracy-stopped backtracking outline.
- 适用范围。No N03 exponent pair, objective value, or strict constraint feasibility is certified by this article alone; contraction plus an unspecified numerical polygon is not a branch-and-bound certificate.
- 相关技能。[math-n03-oscillation-and-geometric-remainder](../../../../math-n03-oscillation-and-geometric-remainder/SKILL.md)
- 其余依赖。Recover/audit the actual implementation or make a rational-interval search that logs every outer polygon, feasibility decision, lower/upper objective bound, tolerance, and active-node certificate.
- [主来源 1](https://arxiv.org/abs/1402.1993) · [主来源 2](https://doi.org/10.2478/ausi-2014-0014)
- 复核记录。2026-11-26T18:11:16+08:00。existing。statement。
- 本次依据。math-n03-oscillation-and-geometric-remainder already carries a full source card for this SHA: exact A/BA projective maps and the contraction are retained, while its constrained-search pseudocode is quarantined pending a global certificate.。定位。Projective maps (pp. 1--3), contraction lemma (p. 6), constrained search and caveat (pp. 7--8)。全卷 11 页。后续条件。Use the existing card with feasible-incumbent filtering, signed denominator checks, and an explicit active-node lower/upper-bound termination certificate.。

## Local Affine Selections of Convex Multifunctions

- 原件 fcfb7ddfbb5675f4a50a0993ad2fcaa4983d2e310df9d675d8fb081eef1886a7。arXiv:1611.02584v1; local 5-page PDF marked 8 November 2016。物理页 2, 3, 4。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:1611.02584v1; official arXiv record checked and lists v1 only
- 已有技能。Independent transfer: if D is convex with x0 in its finite-dimensional interior and F:D=>Y has nonempty values and convex graph, choose a simplex whose relative interior contains x0, select y_i in F(v_i), and define A(sum lambda_i v_i)=sum lambda_i y_i. The graph-convexity calculation proves A(x) in F(x) on that neighborhood. This is a finite local affine-selection construction.
- 结论位置。Lemma 3 and Theorem 4 on pp.2–3 choose values at simplex vertices around x0 and extend by barycentric coordinates. Convexity of the graph proves affine selections stay in F. Proposition 5 on p.4 shows why this does not transfer automatically to infinite dimensions.
- 适用范围。It requires an explicit finite-dimensional simplex contained in D and chosen vertex values. It gives no global selection, Borel/analytic measurability, measurable argmax theorem, or infinite-dimensional selection; the source supplies a Banach-space countermechanism.
- 相关技能。[math-m04-measurable-supremum-selection](../../../../math-m04-measurable-supremum-selection/SKILL.md)
- 已采用构件。有限维有理单纯形、重心系数与给定凸图的仿射选值证书。 [math-m04-measurable-supremum-selection](../../../../math-m04-measurable-supremum-selection/references/local-affine-simplex-selector.md)
- 其余依赖。Add a finite simplex/barycentric verifier to M04 only if callers provide the local simplex, selected graph points, and convex-graph certificate. Add measurability only with a separate finite-patching proof.
- [主来源 1](https://arxiv.org/abs/1611.02584)

## Nondegeneracy and regularity of polynomial pushforwards

- 原件 4201117f4cb6954de0e4930c9905b396d4a20240f89d612effd26b5533d50101。arXiv:2608.01516v1, submitted 2 August 2026。物理页 1, 2, 4, 5, 19, 20, 21, 22, 23, 24。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.01516v1 (only version listed on the checked primary arXiv record)。
- 邻近材料。The local v1 really states a dimension-free Borel-set estimate for a degree-d polynomial map under log-concavity, positive component variances, and det Sigma^d_mu(f)>=eta, with exponent 1/(k(d-1)+1). Its proof uses a Carbery--Wright step and the extended-monomial covariance/Jacobian equivalence. N02's active instructions instead derive PL/BBL marginal inequalities from pointwise slice hypotheses; no N02 claim cites or needs this pushforward theorem。
- 结论位置。PDF pp. 4--5 state Theorem 1.4 and its sharpness example; pp. 19--21 prove the derivative estimate used for the regularity route; pp. 22--24 prove the algebraic-dependence/extended-covariance equivalence。
- 适用范围。The result is a 2026 v1 preprint, and the read proof still invokes earlier polynomial/log-concave estimates. Its variance-plus-extended-covariance assumptions and polynomial-image conclusion do not supply N02's pointwise Prékopa--Leindler/BBL hypotheses, exponents, or equality handling。
- 相关技能。[math-n02-log-concave-marginal-inequalities](../../../../math-n02-log-concave-marginal-inequalities/SKILL.md)
- 其余依赖。Before any separate polynomial-pushforward tool is adopted, audit the cited Carbery--Wright and derivative/moment inputs and independently recheck the assembly from pp. 19--24 to Theorems 1.4 and 1.7。
- [主来源 1](https://arxiv.org/abs/2608.01516)

## On Extremal Volume Projections of the Simplex and the Cube

- 原件 b7d725d4513eaf8aec916691e99cbc5635aed1ea5ef990e2d926bbbd614bb101。local arXiv:2601.18436v1, dated 26 January 2026 on physical p. 1。物理页 1, 3, 11, 12, 13。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。local PDF identifies arXiv:2601.18436v1; assigned byte identity is confirmed
- 构件候选。A limited exact component is independently derivable. For a unit vector a with sum a_i=0, p.12 reduces simplex hyperplane projection volume to a fixed dimensional factor times sum_i |a_i|. With k positive coordinates, Cauchy--Schwarz gives sum_i|a_i|=2S <= 2 sqrt(k(n-k)/n), as on p.13; equality has constant values within each sign class. The exact n=5 equality case (two entries squared 3/10 and three squared 2/15) is checked in exact arithmetic.
- 结论位置。Theorem 1.2 and Propositions 1.3--1.4 are on pp.3--4; pp.11--13 derive the Cauchy--Minkowski projection formula and optimize the zero-sum L1 norm.
- 适用范围。This supplies exact extrema only for the normalized regular simplex and its finite equality orbit. It has no deficit-to-distance estimate and does not establish M03's general near-extremizer, compactness, or constant API.
- 相关技能。[math-m03-near-extremizer-stability](../../../../math-m03-near-extremizer-stability/SKILL.md)
- 其余依赖。Fix a dimension and derive a quantitative deficit-to-distance statement modulo permutations/signs, including the odd-dimensional equality orbit; only then consider a narrowly scoped stability interface.
- [主来源 1](https://arxiv.org/abs/2601.18436)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。Pages 12--13 give a clean zero-sum L1 extremum and equality orbit, but this has no present target-specific projection-normal interface and does not provide a deficit-to-distance estimate for M03.。定位。Cauchy--Minkowski reduction (pp. 11--12) and Proposition 1.4 proof (p. 13)。全卷 16 页。后续条件。Specify the regular-simplex projection normalization and a quantitative distance-to-equality objective before turning the equality calculation into a stability interface.。

## On the Fourier transform of the symmetric decreasing rearrangements

- 原件 7d16bea48a9dfecacffd27f78d08f39a1a8bc3d844c92f0f20c974e13ed665dd。arXiv:0809.0604v1 (3 Sep 2008); the local 20-page PDF hash matches the assigned copy. Its text layer is corrupted, so physical p. 1 was rendered and visually inspected。物理页 1, 2。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Philippe Jaming, Annales de l'Institut Fourier 61(1) (2011), 53–77, DOI 10.5802/aif.2597。
- 邻近材料。The recovered published identity is a rearrangement-inequality paper: it compares local L2 Fourier behavior over a set with that of the symmetric decreasing rearrangement (and gives an L1 variant with finite-support-measure condition). The current F02 provenance expressly records it as non-transferred, and no active F02 assertion depends on it。
- 结论位置。Local physical p. 1, visually rendered: title, abstract, and Theorem 1.1 opening; local p. 2 consulted but text layer is corrupt. The publication primary record identifies the L2 rearrangement theorem and the 2011 journal version。
- 适用范围。The published theorem is neither a tensor-product positive-definite kernel result nor a Fourier-nonnegativity assertion; it gives no soft-square-supremum estimate. The garbled local extraction prevents treating unrendered local theorem/proof pages as independently reread, although the publisher record supplies the narrow published theorem identity。
- 相关技能。[math-f02-tensor-fourier-positivity-soft-square-supremum](../../../../math-f02-tensor-fourier-positivity-soft-square-supremum/SKILL.md)
- 其余依赖。None for the active F02 route. A future rearrangement tool should obtain a clean publisher PDF and inspect the theorem/proof pages under its own Fourier normalization and set-measure hypotheses。
- [主来源 1](https://arxiv.org/abs/0809.0604) · [主来源 2](https://www.numdam.org/articles/10.5802/aif.2597/) · [主来源 3](https://www.numdam.org/item/10.5802/aif.2597.pdf)

## On the variation of maximal operators of convolution type

- 原件 9f204ab3ff567379e7eea703649826fe649ba835d9c86babc3ca2e1fe8f66f00。arXiv:1309.1529v1 (local PDF dated 6 September 2013)。物理页 1, 3, 4, 9, 10。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Journal of Functional Analysis 265 (2013), 837–865; DOI 10.1016/j.jfa.2013.05.012。
- 邻近材料。The source independently verifies variation contraction for heat and Poisson maximal functions: in dimension one for W^{1,p}/BV regimes stated in Theorems 1–2, and in higher dimension in the stated L^2 or L^∞ regimes. Its proof is tied to the heat/Laplace semigroup and subharmonicity of the detachment set。
- 结论位置。PDF p. 1 identifies the arXiv version and the heat/Poisson subject; pp. 3–4 state the continuous heat and Poisson variation theorems; pp. 9–10 begin the heat-flow proof via subharmonicity on the disconnecting set and the associated variational argument。
- 适用范围。Neither the published result nor the inspected proof provides the G04 Fourier-projection inequality for arbitrary pairwise-disjoint intervals, its 2≤p<∞ range, or a spatial-tree packing estimate. It therefore cannot support an active G04 claim。
- 相关技能。[math-g04-rubio-de-francia-square-function-scope-check](../../../../math-g04-rubio-de-francia-square-function-scope-check/SKILL.md)
- [主来源 1](https://arxiv.org/abs/1309.1529) · [主来源 2](https://doi.org/10.1016/j.jfa.2013.05.012)

## Rubio de Francia Extrapolation Theorem for Quasi Non-increasing Sequences

- 原件 5ea94d5f8d21e325a488369c7c2e6792d20283517804bd45ccd95fe7e9933755。local PDF matches arXiv:2603.06109v1 (6 Mar 2026; 19 pages)。物理页 1, 2, 8, 14, 15, 17。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2603.06109v1; no journal publication identified in the checked arXiv record。
- 邻近材料。The local proof establishes a discrete weighted Hardy characterization for quasi non-increasing sequences and uses an open-ended QB_{beta,p} weight step in its extrapolation theorem. These statements match the checked arXiv v1 record。
- 结论位置。pp. 1–2, discrete setting; p. 8, Theorem 2.5; pp. 14–15, open-ended weight step; p. 17, final extrapolation argument。
- 适用范围。The result has no Fourier projection P_I, disjoint frequency interval family, spatial tree, or square function. It therefore cannot support G04’s classical Rubio de Francia square-function conclusion; the active skill correctly treats it as adjacent scope evidence only。
- 相关技能。[math-g04-rubio-de-francia-square-function-scope-check](../../../../math-g04-rubio-de-francia-square-function-scope-check/SKILL.md)
- 其余依赖。A different source or proof must provide the required Fourier interval projections and the stated p-range; quasi-monotone sequence extrapolation cannot fill that gap。
- [主来源 1](https://arxiv.org/abs/2603.06109)

## Sections of Convex Bodies through Their Centroid

- 原件 ef42b564de78a9d53e1fca23598b197313afa5d6120ba4f2665e0bfd71d42beb。Local 8-page publisher PDF, Arch. Math. 69 (1997), 515–522; embedded text is font-encoded but physical p. 1 was visually rendered and read。物理页 1, 2。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Matthieu Fradelizi, Archiv der Mathematik 69(6) (1997), 515–522, DOI 10.1007/s000130050154。
- 引用核对。For a convex body K in R^n and any k-dimensional direction, the maximum volume of a parallel k-section is at most ((n+1)/(k+1))^k times the volume of the section through the centroid; the source states equality characterization. Rendering resolved the prior unreadable-text issue, and the author-hosted version gives the theorem locator。
- 结论位置。Local physical p. 1, visually rendered: abstract and stated centroid-section bound; p. 2 consulted through the same exact local PDF. The author-hosted PDF confirms Theorem 1 on its p. 2。
- 适用范围。This is a sharp finite-dimensional convex-geometry result, not a general outer-approximation or optimization certificate; its equality characterization and measure normalization must be kept exactly as stated。
- 其余依赖。No implementation dependency is identified. If a geometry skill later uses the inequality, audit the proof and equality hypotheses from the published/author PDF first。
- [主来源 1](https://perso.math.u-pem.fr/fradelizi.matthieu/pdf/sectionarxiv.pdf)

## Some applications of the Menshov–Rademacher theorem

- 原件 5ed5e46e2f4a6cd3150d3ca8d6915c2f6fd2363b6eae40b01fe2240878cdcde4。local arXiv:2103.09594v1, dated 17 March 2021 on physical p. 1。物理页 1, 2, 3, 4, 5, 6, 7。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。published Comptes Rendus. Mathématique 359(7) (2021), 861--870, DOI 10.5802/crmath.225; assigned local source is arXiv:2103.09594v1
- 待核。There is an explicit counterexample to the advertised complex formulation. Let X be uniform on {1,i,-1,-i}; then E|X|^2=1 but EX^2=0. Independent copies satisfy E(X_nX_m)=0 for every n,m, so the paper's displayed control L is zero for every coefficient sequence, while the finite Lemma 1 with N=1,a_1=1 would assert E|X_1|^2<=0. Taking a_n=n^(-1/2) also shows why the bilinear zero matrix cannot be a complex covariance criterion. The exact root-of-unity moments were computed in exact arithmetic.
- 结论位置。p.1 and p.2 state real-or-complex variables; pp.3--4 expand E|sum a_nX_n|^2 using E(X_nX_m) without conjugation; pp.5--7 propagate that form to the convergence/covariance corollaries.
- 适用范围。The printed complex dependent-series theorem and covariance corollaries cannot be used. This does not affect F06's independently derived finite orthogonal maximal bound.
- 相关技能。[math-f06-menshov-rademacher-maximal-partial-sums](../../../../math-f06-menshov-rademacher-maximal-partial-sums/SKILL.md)
- 其余依赖。Compare the published edition for a correction; otherwise replace all second moments by Hermitian covariances E(X_n overline{X_m}) and reprove the maximal and convergence statements with the appropriate positivity/boundedness assumptions.
- [主来源 1](https://arxiv.org/abs/2103.09594) · [主来源 2](https://doi.org/10.5802/crmath.225)
- 复核记录。2026-11-26T18:11:16+08:00。existing。statement。
- 本次依据。The live F06 source card records a checked Hermitian finite maximal lemma and a conservative 16L repair, while explicitly withholding the printed 8L and covariance corollaries. A duplicate source record would be misleading.。定位。Lemma 1 (pp. 3--4), Theorem 1 proof (pp. 4--6), later corollaries (pp. 7--9)。全卷 10 页。后续条件。Use math-f06-menshov-rademacher-maximal-partial-sums with Hermitian moments and its stated absolute-energy hypotheses; do not import the printed complex bilinear formulation.。

## Sparse bounds for maximal rough singular integrals

- 原件 d47f3d3e158a7692604adcc3367fd4dd774ef3a59b38abfe25dd844f5fb4b2d3。assigned local PDF labels itself arXiv:2609.03751v2, 8 September 2026, on physical p. 1。物理页 1, 3, 4, 5, 8, 14, 17, 18, 27, 33。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2609.03751v2 as labelled by the assigned local PDF; the byte identity is confirmed
- 邻近材料。The earlier v1-versus-v2 gate is resolved at the assigned source level: this SHA is a v2 PDF, and its p.3 theorem has linear p-prime dependence, not the alleged (p-prime)^4 statement. Its finite reusable reduction is independently transparent: after sorting a nested active chain, the truncation indicator equals 1_{u<=v1(x)}-1_{u<=v2(x)}, hence the truncation is S_v1-S_v2 and is bounded by twice the prefix maximum (p.17). This only imports Rademacher--Menshov after a uniform signed L2 bound, which the source obtains using rough-kernel-specific localization.
- 结论位置。p.1 supplies the v2 header; pp.3--5 state the p-prime sparse theorem and hypotheses; p.8 states the signed Rademacher--Menshov lemma; pp.14--18 prove occupancy-to-prefix reduction; p.27 supplies a signed estimate and p.33 performs the angular-amplitude summation.
- 适用范围。The source is not an extension of the active F06 finite orthogonal API: it additionally requires mean-zero rough kernels, stopping collections, localized atom cancellation, microlocal signed estimates, and amplitude decay. No F06 claim should cite it as a general transfer.
- 相关技能。[math-f06-menshov-rademacher-maximal-partial-sums](../../../../math-f06-menshov-rademacher-maximal-partial-sums/SKILL.md)
- 其余依赖。If a rough singular-integral tool is desired, separately certify the source's localized signed estimate and its stopping hypotheses for the target. Retain the version correction in the historical ledger rather than treating the old discrepancy as a mathematical defect of this v2 PDF.
- [主来源 1](https://arxiv.org/abs/2609.03751) · [主来源 2](https://arxiv.org/html/2609.03751v2)

## Square Function Estimates for Cones over Quadratic Manifolds

- 原件 90f5c45c15c0127eaa4ecb00f5c7c7d3fa4d77c5739eb1aee499359a9afd4a4f。local PDF matches arXiv:2502.13275v1 (18 Feb 2025; 27 pages)。物理页 1, 2, 5, 6。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2502.13275v1; no journal publication identified in the checked arXiv record。
- 邻近材料。Under the determinant transversality condition on Hessian generators, Theorem 1.2 proves an L4 cap square-function estimate near the displayed quadratic manifold; pp. 5–6 derive the finite-overlap alternative used in the proof。
- 结论位置。pp. 1–2, Assumption 1.1 and Theorem 1.2; pp. 5–6, proof by the quadratic four-frequency relations。
- 适用范围。The preprint’s Fourier-support, cap-partition, and Hessian-transversality assumptions do not define G03’s project-specific directional capture tree, feasible leaves, source vectors, or shared-input predicate. Thus it is not an active G03 theorem dependency。
- 相关技能。[math-g03-directional-capture-tree-quadratic-audit](../../../../math-g03-directional-capture-tree-quadratic-audit/SKILL.md)
- 其余依赖。Any future use requires a precise reduction to Fourier-supported caps plus a verified uniform determinant lower bound and an independent bridge to the capture-tree geometry。
- [主来源 1](https://arxiv.org/abs/2502.13275)

## Stability of extremal hyperplane projections of balls in ℓ_p^n(R)

- 原件 c1b3b61ec81c7bee2c24912608a0a1404ba8993d175e9ddd14c8b399705e6020。local arXiv:2608.21787v1, dated 22 August 2026 on physical p. 1。物理页 1, 2, 3, 4, 8, 11, 12。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。local PDF identifies arXiv:2608.21787v1; assigned byte identity is confirmed
- 构件候选。The p=infinity branch is a fully checkable restricted stability calculation. Formula (4) on p.3 gives V(a)/V(a^(n))=(sum_i a_i)/sqrt(n). For ||a||_2=1, 1-(sum a_i)/sqrt(n) >= (1-(sum a_i)^2/n)/2 = (4n)^(-1) sum_{i,j}(a_i-a_j)^2, proving Theorem 1(b) with c_infinity=1/4 for ordered nonnegative a. The rational n=2 input a=(4/5,3/5) is verified exactly in exact arithmetic.
- 结论位置。Theorem 1 is on p.2; pp.3--4 give the p=infinity formula and variance proof; pp.8--12 treat the other p-ranges through comparison and tail arguments.
- 适用范围。This is restricted to central hyperplane projections of normalized ell_infinity balls and ordered nonnegative unit normals. It cannot establish a universal M03 stability or compactness statement; the finite-p parts retain their external comparison inputs.
- 相关技能。[math-m03-near-extremizer-stability](../../../../math-m03-near-extremizer-stability/SKILL.md)
- 其余依赖。To reuse it, define an explicitly scoped projection-normal tool with normalization and symmetry orbit fixed; separately audit the p in (1,infinity) comparison/tail arguments before claiming their constants.
- [主来源 1](https://arxiv.org/abs/2608.21787)
- 复核记录。2026-11-26T18:11:16+08:00。adopted-local。component。
- 本次依据。The p=infinity branch is an exact, finite-dimensional deficit certificate conditional only on the projection-volume identity. Its variance proof is fully source-local and adds a narrowly scoped M03 example rather than a generic stability assertion.。定位。Theorem 1(b) (p. 2), projection formula (4) (p. 3), and variance proof (p. 4)。全卷 15 页。后续条件。Caller must supply the central-projection normalization and the p=infinity Cauchy projection identity; the finite-p branches are not adopted.。
- 已采用构件。物理页 2, 3, 4。An exact p=infinity central-hyperplane-projection deficit conditional on the stated projection-volume identity and normalized ordered nonnegative normal; it is not a general M03 stability theorem. [方法说明](../../../../math-m03-near-extremizer-stability/references/wave7-historical-01-linf-projection-deficit.md)。

## Sunrise strategy for the continuity of maximal operators

- 原件 3e2d5a3fa0011a9a9407ed59dd41a93bca8eaa45b69e4ff7de220fbf4ca7c6f7。arXiv:2008.07810v1 (local PDF dated 18 August 2020)。物理页 1, 2, 10, 25, 26。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。not identified。
- 邻近材料。The checked local manuscript proves a conditional endpoint-continuity strategy for uncentered maximal operators on one-dimensional reductions of radial or polar Sobolev classes. Its abstract P1–P5 framework explicitly requires an a-priori derivative estimate, disconnecting-set geometry, convergence, flatness, singularity control, and a remainder estimate。
- 结论位置。PDF pp. 1–2 state the radial uncentered Hardy–Littlewood W^{1,1} continuity theorem; p. 10 proves the realizing-ball derivative/convergence step; pp. 25–26 formulate the five additional sunrise hypotheses and describe the spherical application。
- 适用范围。G04 concerns scalar Fourier projections indexed by disjoint frequency intervals (and separately spatial-tree packing), whereas this source has no interval-projection square-function theorem or tree/Carleson transfer. It is not an active support for G04's stated p-range or overlap restrictions。
- 相关技能。[math-g04-rubio-de-francia-square-function-scope-check](../../../../math-g04-rubio-de-francia-square-function-scope-check/SKILL.md)
- [主来源 1](https://arxiv.org/abs/2008.07810)

## Symmetric Gamma Function: An Autonomous Definition via Negative-Axis Integral Representation

- 原件 429411dfa8706486d65a6872bfd570d2f8a597d20cd6ce1470ad7044c6f10a43。Research Square preprint DOI 10.21203/rs.3.rs-9842495/v1, posted 1 Jun 2026; local 17-page PDF hash matches the assigned copy。物理页 1, 2, 3, 7, 8, 9, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Research Square version 1; no peer-reviewed canonical publication identified on the checked primary record。
- 邻近材料。The primary preprint identity is recoverable. Its locally inspected content proposes an alternative negative-axis construction and finite regularized values at Gamma poles. The active F04 skill neither uses nor needs this construction: its Gamma use is the ordinary positive shape/rate density and its Poisson–Abel square-function identities are separately spectral calculations。
- 结论位置。Platform front matter and abstract, pp. 1–2; classical Gamma discussion, p. 3; proposed kernel-duality/regularization calculations, pp. 7–9; conclusion, p. 13。
- 适用范围。The article's proposed 'symmetric Gamma' and regularization claims do not supply a proof of the standard Gamma density identity, a Poisson semigroup subordination theorem, or an Abel-limit argument. The Research Square landing page returned 403 to direct fetch, so the checked primary evidence is the platform-served PDF/metadata; no publication-version equivalence or mathematical validation is claimed。
- 相关技能。[math-f04-poisson-gamma-abel-square-function](../../../../math-f04-poisson-gamma-abel-square-function/SKILL.md)
- 其余依赖。None for the active F04 route. Any proposed new Gamma-continuation component would require a clean version comparison and an independent proof of agreement (or explicit non-agreement) with the classical Gamma functional equation and analytic continuation。
- [主来源 1](https://doi.org/10.21203/rs.3.rs-9842495/v1) · [主来源 2](https://www.researchsquare.com/article/rs-9842495/v1) · [主来源 3](https://assets-eu.researchsquare.com/files/rs-9842495/v1_covered_cd48da45-daee-4093-907c-ebebb25a6956.pdf)

## The Gaussian Conjugate Rogers–Shephard Inequality

- 原件 5a41ee8da057969dcc78b4926598a0b7633610522de9dc2adc7dec95b9c83b2a。arXiv:2602.07981v1 (8 Feb 2026)。物理页 1, 2, 3, 8, 12, 21, 40。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2602.07981v1; local 53-page manuscript agrees in title, authors, and opening theorem with the primary record; no journal version identified。
- 邻近材料。The source supports the narrow citation that convex K,L with nonempty interior and Gaussian barycenters at zero satisfy γ(K)γ(L)≤γ(K∩L)γ(K+L), with its stated equality form. The local proof dependency is not merely the abstract: Theorem 1.9 is applied with f_1=1_K, f_2=1_L, h_1=1_{K×L}, h_2=1_{K+L}, and rests on the centered log-concave Gaussian forward-reverse Brascamp–Lieb theorem. It is unrelated to M01’s affine-dependence elimination and Krein–Milman workflow, and no active M01 claim was found to depend on it。
- 结论位置。local p.3, Theorem 1.1; p.8, Theorem 1.9 and indicator-function reduction; pp.12 and 21, FRBL statement/reduction machinery; p.40, equality analysis; primary arXiv record checked。
- 适用范围。The theorem requires the Gaussian-barycenter centering and convex/nonempty-interior hypotheses; the Gaussian sumset term is K+L, not K−L. The broad FRBL machinery and equality cases cannot be transplanted as a generic convex-hull/extreme-point rule, and the source remains a preprint。
- 相关技能。[math-m01-convex-hull-extreme-points](../../../../math-m01-convex-hull-extreme-points/SKILL.md)
- 其余依赖。A separate Gaussian-convexity skill would need to carry the centering test, Gaussian-measure evaluation, and full FRBL proof/dependency audit before use; do not use this source to broaden M01。
- [主来源 1](https://arxiv.org/abs/2602.07981)

## The Parabolic Mellin Transform: Gamma and Zeta Integral Representations

- 原件 7a001fa10a352821acb3b44064e6a07a40947ec9a5dfacab8513e6f2a75db7cd。local manuscript dated 5 Jun 2026; no e-print identifier printed。物理页 1, 2, 3。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2602.17007v2 (3 Jun 2026)。
- 邻近材料。The local manuscript and checked arXiv record identify the PMT as a parabolic-contour Mellin transform for Gamma/zeta representations. Its p.3 change of variables is a contour identity for a special-function transform, whereas the active F04 skill implements Poisson semigroup, Gamma subordination, and Abel square-function checks and does not cite or invoke this paper。
- 结论位置。Local PDF pp.1–3: abstract, introduction, and PMT definition/change-of-variables formula (1)–(2)。
- 适用范围。No semigroup generator, subordination formula, square-function estimate, or Abel-limit transfer is stated in the read locus. The arXiv identity was recovered, but I did not establish byte identity between the supplied PDF and the official v2 PDF。
- 相关技能。[math-f04-poisson-gamma-abel-square-function](../../../../math-f04-poisson-gamma-abel-square-function/SKILL.md)
- 其余依赖。None for the active F04 claim; any future PMT route must verify its contour/branch hypotheses and its own proof separately。
- [主来源 1](https://arxiv.org/abs/2602.17007)

## Transcendence and measures via the refined Diophantine exponent

- 原件 2cfb651d65a9960bc0385a2658005752dd899bb4a8919b08d91c8319a18a87b2。arXiv:2605.30606v2, revised 1 August 2026。物理页 1, 4, 5, 6, 18, 19, 20, 21, 22, 23, 27, 28, 29, 30, 31, 32, 33。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2605.30606v2 (current version on the checked primary arXiv record; local PDF front matter matches v2)。
- 邻近材料。The v2 local PDF proves a refined-word-repetition transcendence dichotomy under a number field/place, S-integer coefficients, h(a_i)=o(i), and Rdio(a)>log H(beta)/log|beta|_v; its quantitative statement excludes alpha in K and carries a degree-dependent exponent. The proof pages explicitly use the Subspace Theorem, height gaps, and a mismatch-variable elimination, not an oscillatory integral or geometric-remainder estimate。
- 结论位置。PDF pp. 4--6 state Theorems A--B and the degree restriction; pp. 18--23 prove Theorem A through the Subspace-Theorem/mismatch-variable construction; pp. 27--33 give the Quantitative Subspace-Theorem setup and proof of Theorem B。
- 适用范围。This does not repair or substantiate any active N03 van-der-Corput, Jacobian, or geometric-remainder claim. It also cannot be applied to Euler's constant from finite numerical data: a concrete coefficient word, the refined-exponent certificate, all place/height hypotheses, and a separate exclusion of the K-valued alternative are required。
- 相关技能。[math-n03-oscillation-and-geometric-remainder](../../../../math-n03-oscillation-and-geometric-remainder/SKILL.md)
- 其余依赖。A future arithmetic-transcendence skill would need a formal checker for the refined-repetition certificate and an audit of the cited Subspace-Theorem inputs; it should remain separate from N03。
- [主来源 1](https://arxiv.org/abs/2605.30606)

## Two quantitative versions of the Nonlinear Carleson Conjecture

- 原件 c42da6797de17584a2bc31fc9e8f9fe73541710ee7b6f312fdd35a0005101670。Earlier card recorded a local 8-page manuscript and held it because identity was not recovered。物理页 1, 3, 5。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Sergey A. Denisov, Comptes Rendus. Mathématique 363 (2025), 1533--1541, doi:10.5802/crmath.806; matching preprint arXiv:2505.06788。
- 邻近材料。Publication identity resolves the previous hold. The local text explicitly labels qNCC-I and qNCC-II as conjectures; Theorem 2.1 is only the implication qNCC-I implies qNCC-II, while Theorem 3.1 assumes qNCC-II. Thus it supplies no established TC-A4 Carleson-square-function bound。
- 结论位置。Local p. 1 abstract, p. 3 qNCC-I/qNCC-II and conditional Theorem 2.1, p. 5 conditional Theorem 3.1; publisher/arXiv records checked。
- 适用范围。The paper concerns nonlinear Carleson/OPUC matrix products rather than the active skill's binary-tree packing and square-function interface; conditional consequences cannot be entered as an unconditional tool。
- 相关技能。[math-g05-tree-carleson-square-function-tc-a4-audit](../../../../math-g05-tree-carleson-square-function-tc-a4-audit/SKILL.md)
- 其余依赖。None for the active skill. A nonlinear-Carleson skill would have to retain the conjectural premises and separately audit the OPUC dependencies。
- [主来源 1](https://doi.org/10.5802/crmath.806) · [主来源 2](https://arxiv.org/abs/2505.06788)

## Uniform Estimates for Oscillatory Integrals with Parameter-Dependent Phases

- 原件 34015312e4b564e013dfc5f2a4ffc6df46f2777a5d9b44a9e53b9322aa7fe167。arXiv:2402.08391v1 (13 Feb 2024), local 15-page PDF。物理页 1, 3, 4, 5, 9, 10, 11, 12。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2402.08391v1; no journal edition established in this review
- 待核。I independently rehashed the assigned bytes (SHA-256 matches) and counted 15 physical pages. The actual one-dimensional normal-form computation uses Ff=(2π)^(-d/2)∫e^(-ix·ξ)f and proves the displayed Theorem-2.1 leading coefficient after y=(2φ)^(1/2). An independent regularized Fresnel audit gives ∫exp[-εy²+iλy²/2]dy=sqrt(π/(ε-iλ/2)); after multiplication by sqrt(λ/(2π))e^(-iπ/4), the values at (λ,ε)=(10,1/10),(100,1/100),(1000,1/1000) are respectively 0.999850043736-0.009997500787i, 0.999999985000-0.000099999998i, and 0.999999999998-0.000001000000i. Thus the d=1 coefficient is independently consistent with the stated convention. In contrast, the d≥2 printed transform on p.10 retains the branch-sensitive factor (-λπ^-1)^(-d/2)e^(-iπ sgn(A)/4), so the text does not specify a branch-independent reusable exact constant; and pp.11--12 explicitly import Bessel estimates (3.4)--(3.5), including [5].
- 结论位置。Theorem 2.1 and its Fourier convention are on physical pp. 3--5; Theorem 2.6 and the multidimensional Fourier-normal-form calculation are pp. 9--10; the Bessel application and its imported estimates are pp. 11--12.
- 适用范围。The local calculation closes only the normalized d=1 leading coefficient, not a parameter-uniform multidimensional API. The d≥2 branch/normalization and the external Bessel input remain independently unverified; support localization, Hessian nondegeneracy, derivative bounds and dimension must remain guards.
- 相关技能。[math-n03-oscillation-and-geometric-remainder](../../../../math-n03-oscillation-and-geometric-remainder/SKILL.md)
- 其余依赖。Audit the d≥2 Fourier branch against a fixed Gaussian regularization and verify cited Bessel source [5], before promoting any exact N03 constant or Bessel branch.
- [主来源 1](https://arxiv.org/abs/2402.08391)
- 复核记录。2026-11-26T18:11:16+08:00。existing。statement。
- 本次依据。math-n03-oscillation-and-geometric-remainder already retains the verified one-dimensional Fourier-normal-form coefficient and explicitly holds the branch-sensitive multidimensional and Bessel-dependent portions.。定位。Theorem 2.1 and normal form (pp. 3--5); Theorem 2.6 (pp. 9--10); Bessel application (pp. 11--12)。全卷 15 页。后续条件。For a multidimensional application, fix a Gaussian/Fourier branch and separately audit the imported Bessel estimates before using a constant.。
