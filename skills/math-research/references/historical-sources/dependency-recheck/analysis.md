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

- 原件 c0bccdafb2038f83254f1b0c3c9e6bd8b473515b7fc59102f027f39a557ce1e2。local arXiv:2607.27796v2 (31 Aug 2026), 15 physical pages。物理页 1, 3, 12, 13, 14。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2607.27796v2; no formal publication identified in the checked authoritative record
- 构件候选。The strongest transferable subargument is Lemma 5.1: a positive-operator weighted sum has a weak-(1,1) estimate when each component has a stated weak bound C_r and sum_r sqrt(a_r C_r) is finite. The source applies it after a Cantor-spectrum-specific decomposition with geometrically decaying weights, then obtains a.e. convergence from weak type and density.
- 结论位置。Theorem 1.3 is stated on p.3; Lemma 5.1 and the weighted weak-(1,1) aggregation occur on pp.12--13; the density argument to almost-everywhere convergence is on p.14.
- 适用范围。The mock-Fourier theorem depends on the canonical spectrum and self-similar cylinder structure of the middle-fourth Cantor measure. It is not a general orthogonal-series or Menshov--Rademacher theorem, and F06's active finite ordered-orthogonal proof is independent of it.
- 相关技能。[math-f06-menshov-rademacher-maximal-partial-sums](../../../../math-f06-menshov-rademacher-maximal-partial-sums/SKILL.md)
- 其余依赖。A reusable implementation must state positivity/sublinearity, verify every individual weak-(1,1) constant, prove the square-root weighted summability, and independently construct the target decomposition before invoking the aggregation lemma.
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

- 原件 01a4d818f5fb3fd69257039b3189812d48d3c13fe5614913b083bc23f724a701。local arXiv:2609.24030v1 (21 Sep 2026), 9 physical pages。物理页 1, 3, 4, 5, 6, 7, 8, 9。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.24030v1; no formal publication identified in the checked authoritative record
- 构件候选。A defensible finite component is the explicit tensor-mixture derivative estimate: for z_{N,s}=(1-s)a_N+s b_N, the product multiplier m_{N,s}=product_j z_{N,s}(xi_j) has dimension-free bounded s-derivatives on s<=s0. The proof uses u_j=1-|a_N|, the elementary |b_N-a_N|<=7u_j bound, exponential product decay, and e^{-cU}U^k control. The following fractional-integral/complex-interpolation construction produces the p>1 difference estimate.
- 结论位置。Theorems 1.1--1.2 on pp.1--2; one-dimensional multiplier inequality in Lemma 2.1 on pp.3--4; tensor derivative estimate in Proposition 3.1 on pp.4--5; interpolation proof on pp.6--8.
- 适用范围。The full discrete maximal theorem is a p>1 result and uses prior dyadic-maximal and almost-orthogonality machinery to pass from the difference family to the final maximal bound. It supplies neither a weak-(1,1) dimension-free estimate nor a continuous centered-cube endpoint, and it does not establish any F02 soft-square-supremum assertion presently active in the skill.
- 相关技能。[math-f02-tensor-fourier-positivity-soft-square-supremum](../../../../math-f02-tensor-fourier-positivity-soft-square-supremum/SKILL.md)
- 其余依赖。To implement the candidate, encode the exact discrete probability-mixture multiplier and independently verify the cited dyadic/maximal and almost-orthogonality inputs; retain the discrete-cube and 1<p<infinity restrictions.
- [主来源 1](https://arxiv.org/abs/2609.24030) · [主来源 2](https://arxiv.org/html/2609.24030v1)

## Distance Stability for the Integral Hardy and Carleman Inequalities

- 原件 b270e46ae6c105456c18588a04f9667e1e8bd4679667fbf91471d6b285c7e522。arXiv:2606.15056v1; local 9-page PDF marked 13 June 2026。物理页 1, 3, 4, 5, 6, 7, 8, 9。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2606.15056v1; official arXiv record checked and lists v1 only
- 构件候选。A strongest directly checkable finite component is the p=2 Hardy residual identity: for nonnegative compactly supported locally bounded f, 4 integral f^2 minus integral (Hf)^2 equals integral (2f-Hf)^2 (local pp. 3--5). The same derivation records the nonnegative Phi_p residual for p>1. This is a usable explicit deficit certificate, and its logarithmic Q transform only gives the stated finite-log/local distance mechanism.
- 结论位置。Local PDF pp. 3--5 prove Theorems 1--2 by the Hardy integration-by-parts identity; pp. 6--9 formulate and prove the finite-log/local Carleman remainder construction.
- 适用范围。The virtual equality profiles x^(-1/p) and 1/x are not in the global natural spaces. Therefore the source does not give a global Lp distance-to-extremizer or general concentration theorem; endpoint/truncation and finite-log hypotheses remain part of the contract. It is an unrefereed v1 and is not an active M03 result.
- 相关技能。[math-m03-near-extremizer-stability](../../../../math-m03-near-extremizer-stability/SKILL.md)
- 其余依赖。To use more than the displayed residual identity, retain an explicit truncation/endpoint argument and prove the required finite-log Poincare/local-distance transfer for the target input class; a subsequent version or independent proof is needed for any global stability assertion.
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

- 原件 c05bae927a4799b1a0a0ac1681382112a0c77ed2b55c9d28ec934f234115bde1。arXiv:2504.16245v1; local 32-page PDF marked 22 April 2025。物理页 1, 7, 8, 16, 17, 19, 20, 21, 22, 24, 25, 28, 29, 30。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2504.16245v1; official arXiv record checked and lists v1 only
- 待核。The advertised quantitative stability statement is not independently defensible from v1. Its proof replaces core steps by assumptions or generic phrases: uniqueness is invoked without a supplied theorem, second-variation coercivity is assumed, and the weighted map from Lp to the asserted weighted target spaces is claimed without parameters or a proof. Later dispersive and embedding claims likewise depend on an unproved boundedness assertion for K1 and an unspecified weighted-to-Sobolev estimate.
- 结论位置。Local pp. 16--17 invoke radial uniqueness and stability; pp. 19--21 assume the coercive second variation used for Theorem 5.4; p. 22 asserts weighted operator bounds; pp. 24--25 assert boundedness of an oscillatory kernel; pp. 28--30 insert an unspecified weighted-to-Sobolev control.
- 适用范围。Do not use this v1 for M03 stability, extremizer existence, or fractional dispersive/embedding constants. M03's current active claim remains its elementary F(x)=1-x^2 identity and does not rely on this source, so no installed statement must be withdrawn.
- 相关技能。[math-m03-near-extremizer-stability](../../../../math-m03-near-extremizer-stability/SKILL.md)
- 其余依赖。A usable source needs a corrected version with explicit parameter ranges, a proved existence/compactness and uniqueness theorem modulo symmetries, a nondegenerate/coercive second variation, and valid weighted mapping plus oscillatory-kernel estimates; those proofs must then be reread rather than inferred from the abstract.
- [主来源 1](https://arxiv.org/abs/2504.16245)

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

- 原件 b229047f8662ec4ed0e2a952c380f4627155252753f636f4cc29c90b0282c3d7。arXiv:1402.1993v2 (23 December 2014), 11-page local PDF。物理页 1, 6, 7, 8。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Acta Universitatis Sapientiae, Informatica 5(2) (2013), 271–287, DOI 10.2478/ausi-2014-0014; local source is arXiv:1402.1993v2
- 待核。The source does provide a concrete finite branch-and-bound design: after a polygon outer enclosure V and a linear-feasibility predicate R(V,LC) are supplied, the routine recursively applies A and BA and compares objective upper/lower bounds. Its own p. 7 explicitly says the constrained greedy variant can miss optima. N03 correctly treats source-program outputs as non-certificates and requires strict feasibility plus active-node bounds.
- 结论位置。Local p. 1 states the exponent-pair setup; p. 6 gives the contraction lemma and warns that unmodified Graham search is not directly global on P; pp. 7–8 describe the constrained greedy failure and tolerance-based backtracking routine.
- 适用范围。The actual PARI/GP program, its polygon representation and rounding discipline were not included in the read PDF. The contraction argument only supports a requested tolerance and does not prove that every feasibility test preserves strict constraints or that a numerical incumbent is an exact optimal exponent pair.
- 相关技能。[math-n03-oscillation-and-geometric-remainder](../../../../math-n03-oscillation-and-geometric-remainder/SKILL.md)
- 其余依赖。Recover and audit the implementation, or implement a rational/interval branch-and-bound whose every active-node polygon, feasibility predicate and objective lower bound is certified; attach the resulting certificate before promoting a computed exponent pair.
- [主来源 1](https://arxiv.org/abs/1402.1993) · [主来源 2](https://doi.org/10.2478/ausi-2014-0014)

## Local Affine Selections of Convex Multifunctions

- 原件 fcfb7ddfbb5675f4a50a0993ad2fcaa4983d2e310df9d675d8fb081eef1886a7。arXiv:1611.02584v1; local 5-page PDF marked 8 November 2016。物理页 1, 3, 4。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:1611.02584v1; official arXiv record checked and lists v1 only
- 构件候选。The paper proves the finite-dimensional local affine construction: if D is convex with nonempty interior in R^n and a convex multifunction has nonempty values in a real vector space, choose values at vertices of a simplex inside D and extend them affinely; graph convexity keeps the map in the multifunction on that simplex. The source separately gives an infinite-dimensional failure mechanism. This is a narrowly reusable finite construction lead, not an active M04 measurable-selection claim.
- 结论位置。Local p. 3: Lemma 3 and Theorem 4 use simplex vertices and graph convexity; p. 4: Proposition 5 gives the infinite-dimensional obstruction.
- 适用范围。A local affine selector does not imply Borel/analytic graph measurability, a measurable argmax selector, a global selector, or an infinite-dimensional theorem. It therefore cannot close M04's retained general measurable-supremum/selection gap.
- 相关技能。[math-m04-measurable-supremum-selection](../../../../math-m04-measurable-supremum-selection/SKILL.md)
- 其余依赖。A use requires a separate verification that the target is genuinely finite-dimensional with the needed interior/simplex patch, and a separate measurable-selection or finite-patching proof if the desired conclusion is Borel/analytic rather than merely local affine.
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

- 原件 b7d725d4513eaf8aec916691e99cbc5635aed1ea5ef990e2d926bbbd614bb101。Local 16-page PDF labelled arXiv:2601.18436v1 (2026-01-26)。物理页 1, 3, 11, 12, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2601.18436v1; checked record lists only v1
- 构件候选。For the paper's normalized regular-simplex projection problem, the proof gives an explicitly checkable formula and identifies exact extremizing directions via the zero-sum constraint and Cauchy–Schwarz. This is a finite extremizer construction.
- 结论位置。Theorem 1.2 and Propositions 1.3–1.4 (pp.3–4); formula proof (p.11); extremizer proofs (pp.12–13).
- 适用范围。Exact extrema for this simplex/cube setting do not give a deficit-to-distance stability inequality, compactness principle, or general M03 near-extremizer API. No active M03 claim depends on the result.
- 相关技能。[math-m03-near-extremizer-stability](../../../../math-m03-near-extremizer-stability/SKILL.md)
- 其余依赖。Derive a dimension- and normalization-fixed quantitative deficit-to-distance estimate modulo the finite extremal orbit before integrating it into M03.
- [主来源 1](https://arxiv.org/abs/2601.18436)

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

- 原件 5ed5e46e2f4a6cd3150d3ca8d6915c2f6fd2363b6eae40b01fe2240878cdcde4。local arXiv:2103.09594v1 (17 Mar 2021), 10 physical pages。物理页 1, 3, 4, 5, 6, 7。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Safari Mukeru, Comptes Rendus. Mathématique 359(7) (2021), 861--870, DOI 10.5802/crmath.225; publisher page was identified but unavailable to this reader
- 待核。The real-valued dyadic-block layout is a recognizable Menshov--Rademacher-style finite construction, but the source advertises complex random variables while the key L2 expansion on pp.3--4 uses a_n a_m E(X_n X_m) without the needed conjugations. The same ambiguity reaches the later covariance formulation.
- 结论位置。Dependent-series statement and Lemma 1 on pp.1--4; convergence proof on pp.5--6; covariance corollary on p.7.
- 适用范围。Thus the local proof does not establish the claimed complex-valued dependent-series theorem. It also does not affect the active F06 finite ordered-orthogonal bound, which is proved directly in that skill and does not cite Safari. The publisher version could not be fetched here to check a correction or erratum.
- 相关技能。[math-f06-menshov-rademacher-maximal-partial-sums](../../../../math-f06-menshov-rademacher-maximal-partial-sums/SKILL.md)
- 其余依赖。Obtain and inspect a legible publisher version/erratum; otherwise restrict the result to real variables with an independently checked proof, or rebuild every quadratic/covariance step using the appropriate Hermitian conjugate form.
- [主来源 1](https://arxiv.org/abs/2103.09594) · [主来源 2](https://comptes-rendus.academie-sciences.fr/mathematique/articles/10.5802/crmath.225/)

## Sparse bounds for maximal rough singular integrals

- 原件 d47f3d3e158a7692604adcc3367fd4dd774ef3a59b38abfe25dd844f5fb4b2d3。local arXiv:2609.03751v2 (8 Sep 2026), 40 physical pages。物理页 1, 3, 4, 5, 17, 18, 27, 33。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.03751v2; current record explicitly says the improved sparse bound is p-prime
- 构件候选。The exact local v2 is now authoritatively pinned and proves the stated linear-p-prime sparse bound for its rough-singular-integral model. Its reusable finite mechanism is explicit: occupancy chains turn each truncation interval into a difference of two prefix sums; a uniform L2 signed-sum estimate feeds Rademacher--Menshov, and amplitude decay absorbs the logarithmic prefix cost. This corrects the prior staged description that treated the local file as an unidentified or v1-mismatched manuscript.
- 结论位置。Theorem 1.1/roadmap on pp.3--5; occupancy-to-prefix identity on pp.17--18; signed-sum plus Rademacher--Menshov reduction on p.27; angular-amplitude summation on p.33.
- 适用范围。The component needs the paper's stopping collections, localized testing spaces, cancellation, microlocal estimates, and rough-kernel hypotheses. It cannot by itself improve the independent F06 finite orthogonal-prefix inequality, and no active F06 claim was found to rely on Wu.
- 相关技能。[math-f06-menshov-rademacher-maximal-partial-sums](../../../../math-f06-menshov-rademacher-maximal-partial-sums/SKILL.md)
- 其余依赖。For transfer, construct an analogous measurable occupancy/prefix representation and prove the required uniform signed L2 estimate with summable amplitude decay; retain all localization, cancellation, and rough-kernel prerequisites.
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

- 原件 c1b3b61ec81c7bee2c24912608a0a1404ba8993d175e9ddd14c8b399705e6020。arXiv:2608.21787v1; local 15-page PDF marked 22 August 2026。物理页 1, 2, 3, 4, 8, 11, 12。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.21787v1; official arXiv record checked and lists v1 only
- 构件候选。The local v1 supplies a bounded geometry-specific stability construction: under ordered nonnegative unit normal coordinates, Theorem 1 gives dimension-free projection-volume deficits for its stated ℓ_p-ball regimes. In particular, the p=infinity case is independently transparent from the Cauchy projection formula and the variance identity on p. 4. Its p-regime arguments use the stated probabilistic projection representation and Gaussian-mixture/comparison inputs. M03 currently does not use this as a general stability API.
- 结论位置。Local PDF pp. 2--4 state Theorem 1 and prove its p=infinity variance case; pp. 8 and 11--12 give the nontrivial Gaussian-mixture and 1<p<2 proof steps.
- 适用范围。The result concerns central hyperplane projections of normalized ℓ_p^n balls, ordered nonnegative normals, and the theorem's named extremizers/deficits. It neither proves general near-extremizer compactness nor transfers to arbitrary variational problems, other symmetries, sections, or unnormalized metrics.
- 相关技能。[math-m03-near-extremizer-stability](../../../../math-m03-near-extremizer-stability/SKILL.md)
- 其余依赖。For any integration, bind a target exactly to the theorem's p-regime, projection normalization, deficit and normal-vector symmetry; then check each imported mixture/comparison lemma or a later peer-reviewed version.
- [主来源 1](https://arxiv.org/abs/2608.21787)

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

- 原件 34015312e4b564e013dfc5f2a4ffc6df46f2777a5d9b44a9e53b9322aa7fe167。arXiv:2402.08391v1; local 15-page PDF marked 13 February 2024。物理页 1, 3, 5, 9, 11, 12。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2402.08391v1; official arXiv record checked and lists v1 only
- 待核。The source identity and its bounded domains are clear: Theorem 2.1 is one-dimensional with support in B1, phi(0)=phi'(0)=0 and two-sided second-derivative bounds, whereas Theorem 2.6 is explicitly d>=2 with its own compact-support, Hessian and derivative hypotheses. The active N03 skill correctly preserves these conditions and quarantines its exact printed leading-term/normalization paths.
- 结论位置。Local p. 3 states the normalized one-dimensional Theorem 2.1; p. 5 gives its change-of-variable remainder discussion and Theorem 2.2 normalization; p. 9 states Theorem 2.6; pp. 11--12 apply Theorem 2.1 to Bessel integrals while importing an earlier result.
- 适用范围。The read pages do not independently certify the printed exact Theorem 2.2 normalization or Theorem 2.6 leading-term/remainder constants, and the Bessel application imports prior result [5]. Thus no general parameter-uniform stationary-phase API, Bessel expansion, or stronger dimensional transfer is cleared by this source alone.
- 相关技能。[math-n03-oscillation-and-geometric-remainder](../../../../math-n03-oscillation-and-geometric-remainder/SKILL.md)
- 其余依赖。Recompute all phase changes of variables and Fourier conventions in Theorems 2.1, 2.2 and 2.6, independently audit the cited Bessel input [5], and check preservation of support, dimension and nondegenerate-Hessian hypotheses before admitting an exact-main-term call.
- [主来源 1](https://arxiv.org/abs/2402.08391)
