# 优化、矩与严格计算

按原件哈希区分。每条核查保留本机物理页与对应来源。

## A Moment-SOS Hierarchy for Robust Polynomial Matrix Inequality Optimization with SOS-Convexity

- 原件 c5f8382a8abdf2fd9f3860040cb8e2fd24c0997ecda894bf90475a72c4718a98。local arXiv:2304.12628v5 (8 Oct 2024), 38 physical pages。物理页 1, 9, 10, 17, 18, 19, 20, 21, 22。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。Published as Mathematics of Operations Research, DOI 10.1287/moor.2023.0361 (2024 online); local arXiv v5 was not byte-compared to that edition
- 构件候选。Assigned bytes rehash exactly and pdfinfo reports 38 pages. The actual theorem requires both PSD moment/localizing matrices and the stated extension/flat-rank condition, not rank flatness alone. Exact scalar countercheck: for intended support X=[0,∞), the truncated moments of δ_-1 have M1=[[1,-1],[-1,1]]⪰0, det(M1)=0 (rank one/flat), but the g=x localizing value L(g)=-1<0. Hence a flat PSD moment matrix without the source's localizer cannot certify support or recovered atoms. This is precisely why Theorem 4.11 on pp.21--22 needs the full constructed S(k,*) and invokes Theorem 3.2, while pp.19--21 additionally use Assumptions 1--3, Slater and both SDP sides for equality/extraction.
- 结论位置。Matrix moment/localizing cones and imported flat-extension theorem are pp. 9--10; Slater reduction is pp. 17--18; hierarchy, convergence and the finite-extension condition are pp. 19--22.
- 适用范围。This rejects an entrywise-scalar or flat-rank-only C03 extractor. The local manuscript is not a byte-verified copy of the published DOI edition, and its indispensable matrix flat-extension theorem is cited rather than proved locally.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Byte-diff the journal edition and verify the cited matrix flat-extension theorem; any implementation must validate the RPMIO encoder, all localizers, Slater/SOS-convex hypotheses, primal/dual residuals, flat rank and recovered-atom PMI constraints with exact or interval certificates.
- [主来源 1](https://arxiv.org/abs/2304.12628) · [主来源 2](https://doi.org/10.1287/moor.2023.0361)
- 复核记录。2026-11-26T18:11:16+08:00。existing。statement。
- 本次依据。Current math-c03-moment-sos-certificates explicitly requires moment/localizing matrices, Archimedean conditions and a flat-extension check; its provenance ledger has this exact SHA (E1875). The local Theorem 4.11 remains a conditional RPMIO matrix-moment result and adds no standalone extraction route beyond that guarded interface.。定位。physical pp. 9--10, 17--22; moment/localizing setup, Slater reduction, and Theorem 4.11。全卷 38 页。后续条件。For a matrix-PMI instance, provide all localizers, Slater/SOS-convex hypotheses, exact residuals, matrix flat-extension data and recovered-atom PMI checks; byte-compare the journal edition before treating it as the published statement.。

## Adaptive Metrics for Norm-Minimization-Based Outer Approximation in Convex Vector Optimization

- 原件 67390e5e27908c306cf188094be34cb7d57e6302960cd0be72e7d2baebed22b4。local PDF dated 15 Jul 2026, identified in the text as arXiv:2605.14320v3, 27 physical pages。物理页 1, 14, 15, 16, 17, 18, 19。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。unresolved: the checked current arXiv record advertises earlier dispersion/31--33% claims, whereas local pp.16--19 explicitly replace them by ε0-regularized uniform conditioning and say no evaluation advantage; current official PDF was not byte-compared
- 待核。SHA-256 and all 27 physical pages were rechecked. The source itself gives the substantive guard: Lemma 13/p.16 compares metric and Euclidean distances by sqrt(λmin(Mk)) and sqrt(λmax(Mk)); Theorem 12 and Theorem 14 explicitly need fixed 0<m≤M. Exact countercheck to an unconditioned transfer: with M=diag(ε,1) and displacement e1, e1ᵀMe1=ε while ||e1||²=1; for ε=1/10 and 1/1000 the Euclidean-to-metric-square ratios are 10 and 1000. Thus a small adaptive-metric residual cannot control Euclidean Hausdorff error without a uniform lower spectral bound. Local pp.18--19 say ε0 supplies that bound and retract the claimed evaluation advantage. The web-checked arXiv abstract still exposes the incompatible older dispersion/31--33% statement, so version identity is an active error, not a harmless wording difference.
- 结论位置。Lemma 11 is p.14; Theorem 12 and its use of mI⪯Mk⪯MI are pp.15--16; Theorem 14 and the indispensable ε0 regularization are pp.17--18; corrected experimental qualification is p.19.
- 适用范围。No rate, dispersion, or empirical speedup is portable until official v3/published bytes are compared. Even the local corrected theorem applies only to the compact slice, exact scalarizations, valid dual cuts, farthest-vertex selection and uniform conditioning.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Acquire and byte-compare the official current arXiv PDF with local v3, reconcile the public abstract, and independently audit every cut-validity/compact-slice hypothesis before any A02 extension.
- [主来源 1](https://arxiv.org/abs/2605.14320)
- 复核记录。2026-11-26T18:11:16+08:00。hold。dependency。
- 本次依据。The current A02 interface covers only uniformly conditioned outer relaxations; its ledger records this SHA, but the locally read pp.16--19 require epsilon_0 regularization and retract the claimed evaluation advantage. The official current-version byte identity is unresolved, so no metric/rate extension is safe.。定位。physical pp. 14--19; Lemma 11, Theorems 12 and 14, epsilon_0 conditioning and correction。全卷 27 页。后续条件。Acquire and byte-compare the official arXiv v3 or version of record, then certify mI<=M_k<=MI, compact-slice and valid-dual-cut hypotheses before transferring any convergence statement.。
- 复核记录。2026-11-26T19:04:42+08:00。hold。dependency。
- 本次依据。The local v3 requires epsilon-regularized uniform spectral conditioning and retracts the advertised evaluation advantage. The public version identity has not been byte-compared, while a small metric residual cannot control Euclidean error without a uniform lower eigenvalue bound.。定位。Physical p. 14 Lemma 11, pp. 15-16 Theorem 12 and conditioning, pp. 17-18 Theorem 14 and epsilon regularization, p. 19 qualification.。全卷 27 页。后续条件。Acquire and byte-compare the official current version, then certify uniform mI<=Mk<=MI, compact-slice, exact scalarization, valid-cut, and farthest-vertex assumptions.。
- 复核记录。2026-11-26T19:33:26+08:00。hold。dependency。
- 本次依据。The local v3 gives a conditioned theorem but retracts the claimed evaluation advantage; its official current-version bytes were not compared and publicly advertised older claims conflict with local pp. 16--19。定位。Physical p. 14, Lemma 11; pp. 15--18, Theorems 12 and 14 with conditioning; p. 19, corrected qualification。全卷 27 页。后续条件。Acquire and byte-compare the official current version, then certify the compact slice, exact scalarizations, valid dual cuts, farthest-vertex rule and uniform mI<=M_k<=MI conditioning。
- 复核记录。2026-11-26T20:08:24+08:00。adopted-local。component。
- 本次依据。The checked local 27-page v3 has a fully explicit conditioned Euclidean-transfer proof: exact cuts plus uniform mI<=M_k<=MI give convergence and its stated rate. The public arXiv landing page presently advertises incompatible older claims, so no online-version or empirical claim is transferred。定位。physical pp. 14--18; Lemmas 11 and 13, Theorems 12 and 14, and epsilon_0 regularization。全卷 27 页。后续条件。Caller must certify compact slice, exact scalarizations, valid dual supporting cuts, farthest-vertex selection and uniform spectral bounds; compare official bytes before citing a current-version result。
- 已采用构件。物理页 14, 15, 16, 17, 18。Local-v3 conditioned adaptive-metric transfer only; exact oracles and uniform spectral bounds are required. [方法说明](../../../../math-a02-outer-relaxation-budget/references/adaptive-metric-conditioned-transfer.md)。

## Algebraic Farkas Lemma and Strong Duality for Perturbed Conic Linear Programming

- 原件 c348494de4b520eb8d61f5f2d7e9f2063c22468f512883d259d70eac2a1ffe14。Local PDF is dated 2026-01-16; SHA-256 and 26 physical pages were verified. It has no embedded arXiv version line, but its title, authors, date, and content agree with checked arXiv:2601.10390v1; byte equality was not tested。物理页 1, 7, 8, 10, 13, 14, 15, 16, 17。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2601.10390v1 (submitted 2026-01-15); no publisher version was identified in the checked primary record。
- 引用核对。For a dual pair and conic program, Theorem 4.1 proves that a fixed-perturbation Farkas equivalence is exactly equivalent to equality of the corresponding H and N slice. Theorems 4.5–4.8 identify zero gap and, in the first direction, primal attainment only when the stated slice equality/nonemptiness and feasible dual conditions hold. The p.15–16 proof uses those hypotheses rather than deriving them from conic feasibility alone。
- 结论位置。PDF pp.13–14 Theorems 4.1–4.4; pp.15–17 Theorems 4.5–4.8 and proof. pp.7–10 define the perturbed value objects and prove the separation characterization used by the algebraic condition。
- 适用范围。This supports only a narrow citation-level algebraic dual-pair statement. It does not upgrade B01's finite-dimensional Farkas procedure to infinite-dimensional strong duality: the operationally hard condition is the H=N (or K=M) slice equality, and topology/closure, cone, dual-pair, feasibility, finiteness, and attainment details remain essential。
- 相关技能。[math-b01-lagrange-farkas](../../../../math-b01-lagrange-farkas/SKILL.md)
- 其余依赖。No current B01 assertion was found to rely on this manuscript, so no active-skill defect is triggered. Incorporation would require a separately checkable sufficient condition for the relevant slice equality/closedness and a full translation of the target's topology and dual cones。
- [主来源 1](https://arxiv.org/abs/2601.10390)

## Augmentation Approaches for Mixed Integer Programming

- 原件 d9b756f8eea5f0231655aed07b96f43ce6375d5238eecdbd4afb37a1abdf6a9b。arXiv:2507.08525v2 (29 Sep 2025), local 25-page PDF。物理页 1, 2, 3, 10, 11, 12, 15, 20, 21, 22。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2507.08525v2; no published edition identified in the checked primary record
- 构件候选。The assigned bytes hash exactly and contain 25 physical pages. The paper's actual scope is fixed integer matrix A=(AR|AI), all b,c,u, and exact augmentation. I recomputed the paper's Example-2 kernel checks for A=[1,-1|2,2]: A(-2,0,1,0)^T=A(0,2,1,0)^T=A(0,0,1,-1)^T=0, so the displayed directions are genuine feasible kernel moves, but p.10 also correctly records that a finite double test set does not itself give a finite list of its circuit combinations. The p.20 proof of Lemma 8 obtains finite coefficient sets only through a nonzero basis-difference denominator, and Theorem 9/p.22 additionally imports the universal MIP-Graver direction and an exact basic-integer/basis-path argument. This resolves the prior gate negatively for a generic L04 call: finite directions require the specified matrix construction, not just a direction oracle.
- 结论位置。The MIP model and universal-test-set scope are pp.2--3; p.10 explicitly says the finite double set can still generate infinitely many combinations; Lemma 8/Algorithm 4 are pp.20--21; Theorem 9 and proof are p.22.
- 适用范围。The source is an arXiv preprint; it supplies neither a polynomial-time black-box enumeration nor an unqualified generic MIP certificate. Imported Hemmecke results, nondegeneracy/basis-path conditions, exact feasibility and objective checks remain indispensable.
- 相关技能。[math-l04-mathematical-programming-workflow](../../../../math-l04-mathematical-programming-workflow/SKILL.md)
- 其余依赖。Verify the cited universal MIP-Graver result and the full Lemma-6/Algorithm-4 hypotheses, then build only a matrix-specific rational enumerator retaining basis, coefficient path, feasibility and improving-objective certificates.
- [主来源 1](https://arxiv.org/abs/2507.08525)
- 复核记录。2026-11-26T18:11:16+08:00。existing。statement。
- 本次依据。The present math-l04-mathematical-programming-workflow contains an explicit Graver-augmentation certificate; the source's matrix-specific MIP augmentation is already tracked as P-d9b756f8eea5f023. Its Lemma 8/Theorem 9 require basis-path and universal-direction inputs rather than providing a black-box finite direction oracle.。定位。physical pp. 2--3, 10, 20--22; model scope, double-set warning, Lemma 8 and Theorem 9。全卷 25 页。后续条件。For a new use, certify the integer matrix, feasible basic path, universal MIP-Graver premise and all exact improving/feasible steps; do not infer a finite direction list merely from a finite double test set.。

## Benders Decomposition with Partial Non-Anticipativity Relaxation for Multi-Stage Stochastic Clean Energy Transition Planning

- 原件 17fc1b8f863c4b37e06857824ca506b7bcecf7674c71cc5439d8c5ecb5480708。Local 30-page PDF has no embedded arXiv version line; SHA-256 and page count were verified. Its title, authors, and abstract match the checked canonical arXiv v1; byte equality to the official PDF was not tested。物理页 1, 5, 7, 8, 16, 17, 30。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.14105v1 (submitted 2026-08-14); no publisher version was identified in the checked primary record。
- 邻近材料。The paper retains investment nonanticipativity in a Benders master and relaxes operational inter-node storage couplings. Its finite correction argument repairs each child balance by extra charging and exogenous purchase; pp.16–17 state that this produces a feasible nonanticipative solution with a finite objective increase because installed storage is fixed and bounded。
- 结论位置。PDF pp.7–8 Proposition 1 and its model-specific valid-inequality proof; pp.16–17 Proposition 3 correction construction and finite-increase explanation; p.30 source-code/data note。
- 适用范围。This is not a general partial-nonanticipativity theorem. The repair relies on the clean-energy MILP's storage recursion, nonnegative charging efficiencies, available exogenous purchase, and bounded installed capacities. It does not prove A04's graph-connectivity characterization or an unrestricted Benders relaxation/correction result。
- 相关技能。[math-a04-shared-nonanticipative-mip](../../../../math-a04-shared-nonanticipative-mip/SKILL.md)
- 其余依赖。No active A04 claim relies on this paper. Reuse would require proving an analogous feasible repair and finite cost bound for the target model, plus checking whether the local file is byte-identical to arXiv v1 if exact source identity is needed。
- [主来源 1](https://arxiv.org/abs/2608.14105)

## Causal Optimal Transport and Its Links to Enlargement of Filtrations and Continuous-Time Stochastic Optimization

- 原件 e6358fcb0f1598334408a9e27b2a8e28f2122f391b338b74fbbe573b018f1498。local arXiv:1611.02610v2 (12 Dec 2017), 33 physical pages。物理页 4, 5, 25。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。Stochastic Processes and their Applications 130(5) (2020), 2918--2953, DOI 10.1016/j.spa.2019.08.009; this local preprint was not byte-compared with the journal text
- 已有技能。The finite-path implementation encodes causal and reverse-causal prefix constraints with exact marginal masses, then checks the primal and LP dual.
- 结论位置。Local v2 definition and disintegrated causality condition, physical pp. 4–5, and causal duality assumptions, p. 25.
- 适用范围。The implementation applies to explicit finite path laws. The Wiener decomposition and continuous-path duality retain their own hypotheses.
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 已采用构件。The finite-path implementation encodes causal and reverse-causal prefix constraints with exact marginal masses, then checks the primal and LP dual. [math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/references/finite-information-transport.md)
- 其余依赖。For continuous-path use, establish the filtration and weak-continuity requirements in the applicable version.
- [主来源 1](https://arxiv.org/abs/1611.02610) · [主来源 2](https://doi.org/10.1016/j.spa.2019.08.009)

## Conditional Optimal Transport on Function Spaces

- 原件 870ae0faefdc7627c50e64b1af4217c145cc64db3c97202ba3a2aba21b8d712c。local 33-page manuscript (PDF metadata 6 Feb 2024; no cover version label)。物理页 4, 12。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。SIAM/ASA Journal on Uncertainty Quantification 13(1) (2025), 304--338, DOI 10.1137/23M1618922; local bytes have not been diffed against the published edition
- 已有技能。For common conditioning strata the finite-path implementation uses a block constraint with exact rational masses. Primal and LP dual are checked on the resulting allowed pairs.
- 结论位置。Local conditional transport definition and common conditioning marginal, physical pp. 4 and 12.
- 适用范围。This implementation uses given finite rational laws and stratum labels, with no assertion about continuous conditional maps.
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 已采用构件。For common conditioning strata the finite-path implementation uses a block constraint with exact rational masses. Primal and LP dual are checked on the resulting allowed pairs. [math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/references/finite-information-transport.md)
- 其余依赖。For infinite-dimensional use, retain the source topology, disintegrations and cost hypotheses.
- [主来源 1](https://arxiv.org/abs/2311.05672) · [主来源 2](https://doi.org/10.1137/23M1618922)

## Converging Outer Approximations to Global Attractors Using Semidefinite Programming

- 原件 6b26fbd168b3aff091ff344da20a7881f3c036333e11c43d4cd57ffbd05d78a0。arXiv:2005.03346v3 (4 October 2023), local 22-page PDF。物理页 8, 9, 15, 16。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。Schlosser and Korda, Automatica 134 (2021) 109900, DOI 10.1016/j.automatica.2021.109900
- 构件候选。The controlling containment implication is valid but conditional: dual feasibility gives w-v1-v2-1>=0, while the Liouville inequalities give v1,v2>=0 on A, hence w>=1 on A; p.16 then gives A⊆X_k⊆Y_k and d_k>=lambda(Y_k)>=lambda(A). I independently checked the algebraic core on the exact rational continuous-time instance xdot=-x, beta=1, v1=v2=0,w=1: all three feasibility residuals are identically zero (the deliberately coarse Y=R illustrates that feasibility is containment, not accuracy). The p.9 construction further proves its own identity beta v1-Dv1 f=-p=0 on X, so its limiting w_m decreases to 1_A only under the stated smooth-flow construction.
- 结论位置。Theorem 2 and its constructive proof, physical pp.8–9; SOS hierarchy Theorem 5 p.15; containment/volume Theorem 6 p.16.
- 适用范围。This does not provide a generic A02 finite error budget, a Hausdorff bound, or an executable numerical-SDP certificate. The volume conclusion needs polynomial dynamics, compact basic semialgebraic X with the stated Archimedean hypothesis, exact SOS feasibility and the Putinar step; a floating Gram matrix does not establish either premise.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。A guarded attractor checker needs exact polynomial dynamics/defining inequalities, rational SOS Gram witnesses and symbolic verification of every Liouville/positivity identity. Only then may it emit containment; asymptotic volume convergence must remain a separately cited conclusion.
- [主来源 1](https://doi.org/10.1016/j.automatica.2021.109900) · [主来源 2](https://arxiv.org/abs/2005.03346)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。A02 has the general outer-relaxation direction, and its provenance records this exact source, but it has no installed exact SOS/Liouville attractor checker. The source gives containment only with polynomial dynamics, compact Archimedean X, exact SOS feasibility and its constructive smooth-flow argument.。定位。physical pp. 8--9, 15--16; Theorems 2, 5 and 6。全卷 22 页。后续条件。Encode rational polynomial dynamics and defining inequalities, then symbolically verify every Liouville and positivity identity with rational SOS Gram witnesses before emitting containment; retain volume convergence as a cited asymptotic conclusion.。
- 复核记录。2026-11-26T19:04:42+08:00。candidate。dependency。
- 本次依据。The Liouville/SOS construction gives conditional containment, but A02 has no exact polynomial-SOS certificate route for the source's attractor hierarchy.。定位。Physical pp. 8--9, Theorem 2 and construction; pp. 15--16, Theorems 5--6.。全卷 22 页。后续条件。Supply rational polynomial dynamics, compact Archimedean defining data, rational Gram witnesses, and symbolic verification of every Liouville and positivity identity.。
- 复核记录。2026-11-26T19:33:26+08:00。adopted-local。component。
- 本次依据。The published SOS/Liouville construction supplies a sharply scoped outer-containment and volume-convergence rule。定位。physical pp. 8--9 and 15--16; Theorems 2, 5 and 6。全卷 22 页。后续条件。Use exact polynomial/SOS certificates, compact Archimedean data and symbolic checks; no floating SDP output or Hausdorff claim。
- 已采用构件。物理页 8, 9, 15, 16。Exact SOS/Liouville outer containment and source-stated volume convergence. [方法说明](../../../../math-a02-outer-relaxation-budget/references/attractor-sos-outer-containment.md)。

## Convex Optimal Uncertainty Quantification

- 原件 408d52b16125bf50fc22ba33550c3004de76988eff4420912a773961fda21d52。arXiv:1311.7130v2 [math.OC], 27 April 2015; published as SIAM Journal on Optimization 25(3) (2015), 1368--1387, DOI 10.1137/13094712X。物理页 1, 3, 8, 9, 12, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Local 22-page SHA-matched PDF: arXiv:1311.7130v2 header, with a 25 September 2018 title-page date; publisher identity was recovered separately and no byte match to the publisher file was asserted。
- 邻近材料。The source does support a useful finite construction: under its piecewise concave f, piecewise convex g, affine h, and finite-reduction/duality prerequisites, it rewrites a distributional expectation extremum as a finite convex program in atom weights and first moments. Its direct K-times-L atom-merging argument uses Jensen in the correct directions and explicitly begins from an optimal distribution。
- 结论位置。Local pp. 1 and 3 state the distributional OUQ problem and Theorem 1.1; pp. 8--9 give the attained-optimum atom-merging and perspective proof; pp. 12--13 give the alternative dual/saddle-point derivation. The primary arXiv and SIAM records confirm the paper identity and its piecewise-concave/piecewise-convex scope。
- 适用范围。This is not an active L02 theorem for adversarial functions: its variables are probability laws subject to moment/information constraints, whereas L02 deliberately requires a common realizable source input and does not claim all relaxed averages are attainable. Neither Theorem 1.1 nor the checked merging proof supplies the missing lift from an OUQ law to a maximal-operator counterexample. The K-times-L existence wording also depends on Proposition 2.1/finite reduction and on attainment; without an attainment or epsilon-optimizer argument it must not be read as unconditional optimizer existence。
- 相关技能。[math-l02-adversarial-input-search](../../../../math-l02-adversarial-input-search/SKILL.md)
- 其余依赖。If the finite OUQ component is integrated, separately verify the cited finite-reduction theorem/constraint qualification and prove attainment (or a valid epsilon-optimizer passage) for the concrete compact model before using an atom bound。
- [主来源 1](https://arxiv.org/abs/1311.7130) · [主来源 2](https://epubs.siam.org/doi/10.1137/13094712X)

## Copositive and completely positive cones over symmetric cones of rank at least 5

- 原件 eeaf5dbad4c207b58e1e8eb5c4a6f012a7a407bd0bdb21300919f872cec69d0a。arXiv:2602.23725v3 (20 July 2026), local 39-page PDF。物理页 11, 12, 30, 31, 32, 33。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2602.23725v3 (20 July 2026); no journal version identified
- 构件候选。The usable reduction is exact: for a supplied orthogonal extreme-ray frame, A=f(M) has q_A(x)=y^TMy with y_i=delta_i•x, and testing x=sum_i y_i delta_i/(delta_i•delta_i) gives the converse COP(K)∩V=f(COP_r). The paper’s I_0 obstruction then restricts a putative SOS identity to the Horn quartic. Independently, for the displayed Horn matrix H I obtained char_H(lambda)=(lambda-1)(lambda^2-2lambda-4)^2 and (e1+e2)^T H(e1+e2)=0: this confirms it is neither a PSD surrogate nor a strict-positivity certificate, precisely why the restriction/SOS argument is nontrivial.
- 结论位置。Jordan-frame restriction Lemma 3.1 and Theorem 3.2, pp.11–12; Horn exposedness Theorem 4.6 p.30; I_0 obstruction Theorems 5.1–5.2, pp.31–32; stronger PSD-cone construction begins p.33.
- 适用范围。The paper’s non-spectrahedral conclusion imports COP_r not being a spectrahedral shadow, and Theorem 5.2 imports Horn-quartic non-SOS (Theorem 5.1); neither imported theorem was independently closed here. The conclusions require a symmetric cone, a Euclidean Jordan realization and a rank-at-least-five orthogonal primitive frame. They give no finite-level COP decision procedure or arbitrary-hierarchy exactness.
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。For a future guarded diagnostic, require exact Jordan-frame multiplication/inner-product data and independently certify the Horn non-SOS theorem (and the external COP_r non-spectrahedral result before that stronger claim). Keep the output limited to an I_0 exclusion for the constructed H_Delta.
- [主来源 1](https://arxiv.org/abs/2602.23725)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。C02 covers ordinary orthant COP/CP duality and tracks this exact SHA, but the source's symmetric-cone rank>=5 non-spectrahedral mechanism needs Euclidean-Jordan frame data and imported COP_r/Horn non-SOS theorems. It is not duplicated by a current executable C02 certificate.。定位。physical pp. 11--12, 30--33; frame restriction, Horn exposedness and I_0 obstruction。全卷 39 页。后续条件。Supply exact Jordan-frame operations and an independently certified restriction to COP_r; separately prove the Horn non-SOS and non-spectrahedral-shadow inputs before any general conclusion.。
- 复核记录。2026-11-26T19:04:42+08:00。candidate。dependency。
- 本次依据。The symmetric-cone rank-at-least-five obstruction requires exact Euclidean-Jordan frame data plus imported Horn non-SOS and COP-r non-spectrahedral results. C02 currently covers the orthant interface.。定位。Physical pp. 11--12 frame restriction; pp. 30--33 Horn exposedness and I_0 obstruction.。全卷 39 页。后续条件。Supply exact Jordan-frame operations and a certified reduction to COP-r, then independently establish the Horn non-SOS and external non-spectrahedral-shadow inputs for the intended conclusion.。
- 复核记录。2026-11-26T19:33:26+08:00。candidate。dependency。
- 本次依据。The source's symmetric-cone rank-at-least-five obstruction depends on Euclidean-Jordan frame data and imported Horn non-SOS and COP_r non-spectrahedral results, beyond the installed orthant COP interface。定位。Physical pp. 11--12, frame restriction; pp. 30--33, Horn exposedness and I_0 obstruction。全卷 39 页。后续条件。Supply exact Jordan-frame operations and a certified reduction to COP_r; independently establish the Horn non-SOS and non-spectrahedral-shadow inputs before exposing the conclusion。
- 复核记录。2026-11-26T20:08:24+08:00。adopted-local。component。
- 本次依据。Lemma 3.1 proves the exact conditional Jordan-frame restriction COP(K) intersect V=f(COP_r) from self-duality and orthogonality; it is independent of the paper's imported non-spectrahedral conclusion。定位。physical p. 11; definition (3.1) and Lemma 3.1。全卷 39 页。后续条件。Caller must supply exact self-dual-cone data, pairwise orthogonal extreme-ray generators and inner products; no general COP decision or spectrahedral-shadow conclusion follows。
- 已采用构件。物理页 11。Exact conditional Jordan-frame restriction of a self-dual symmetric cone to COP_r. [方法说明](../../../../math-c02-completely-positive-copositive/references/symmetric-cone-jordan-frame-restriction.md)。

## Copositive Matrices with Ordered Off-Diagonal Entries

- 原件 05990838c18871a47d433307d452dcc18e9c528011a686a602b1f3e30c08218e。arXiv:2605.15970v1 (15 May 2026), local 17-page PDF。物理页 5, 6, 11, 12, 13。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2605.15970v1; no journal version identified
- 构件候选。The prior gap can be reduced to an explicit guarded special case, not a generic copositivity test. Theorem 3.5’s induction is sound conditional on copositivity: Lemma 3.6 supplies an all-nonnegative or all-negative off-diagonal row, deletion or positive-pivot Schur complement preserves M_n, and the recursion stops at COP_4=SPN_4. I exactly reproduced the paper’s p.13 permutation (4,5,3,1,2) of its Q and checked all ordered-off-diagonal inequalities in M_5; the resulting matrix is [[2,0,1,2,2],[0,2,2,2,2],[1,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]. This directly validates the finite membership guard behind the stated DNN exactness interface.
- 结论位置。Definition of M_n and Theorem 3.5, pp.5–6; permutation recognition Proposition 4.8 p.11; St-QP/DNN interface pp.11–13, especially Corollary 5.5 and Proposition 5.7.
- 适用范围。M_n recognition does not establish copositivity, and the source proves existence rather than a rational PSD-plus-entrywise-nonnegative decomposition. A release-quality certificate still needs an independently checked COP_4=SPN_4 base and a replayable factor recovery. The arbitrary-matrix COP/CP hierarchy in C02 is therefore not upgraded.
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。Implement exact DAG/topological-sort recognition of a permutation into M_n, then accept only a separately supplied copositivity witness or a scoped St-QP hypothesis. To emit SPN, recursively retain deletion/Schur-complement data and a verified base-case factorization.
- [主来源 1](https://arxiv.org/abs/2605.15970)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。C02 has no ordered-off-diagonal M_n recognizer or exact SPN factor recovery. The paper's Theorem 3.5 is only a conditional implication from COP plus a permutation into M_n, and its recursion relies on the COP_4=SPN_4 base.。定位。physical pp. 5--6 and 11--13; M_n definition/Theorem 3.5, recognition and DNN application。全卷 17 页。后续条件。Implement exact permutation/DAG recognition and preserve each deletion or Schur-complement witness; accept a separately supplied copositivity certificate and verify a base-case SPN factorization before outputting SPN.。
- 复核记录。2026-11-26T19:04:42+08:00。candidate。dependency。
- 本次依据。Theorem 3.5 is conditional on copositivity plus membership in the ordered-off-diagonal class M_n. Proposition 4.8 gives recognition, but the source does not supply a replayable rational SPN decomposition and its induction uses the COP_4=SPN_4 base.。定位。physical pp. 5--6 and 11--13, Definition of M_n, Theorem 3.5, Proposition 4.8, and Proposition 5.7。全卷 17 页。后续条件。Implement exact permutation recognition and retain deletion or Schur-complement data with a separately supplied copositivity witness and verified SPN base factorization.。
- 复核记录。2026-11-26T19:33:26+08:00。adopted-local。component。
- 本次依据。The preprint's ordered off-diagonal copositive-to-SPN implication is a narrow conditional classifier; it does not test copositivity or construct a rational decomposition。定位。physical pp. 5--7; Theorem 3.5 and Lemma 3.6。全卷 17 页。后续条件。Caller must supply the prescribed ordering and an independent copositivity certificate。
- 已采用构件。物理页 5, 6, 7。Conditional ordered-class COP-to-SPN classification; caller supplies ordering and copositivity. [方法说明](../../../../math-c02-completely-positive-copositive/references/ordered-offdiagonal-copositive-spn.md)。

## Disjunctive Sum of Squares

- 原件 6e6581b0fab0b52347c7ec6e7bc00a2ee8cad7f51cc79a383625bde81ae81c4c。arXiv:2605.28674v1 (27 May 2026), local 45-page PDF。物理页 8, 9, 25, 26, 28, 29。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2605.28674v1; no journal version identified
- 已有技能。A distinct finite certificate is closed for the displayed Horn matrix only. The two rational branch matrices V1,V2 on pp.28–29 cover R_+^5 (their last-coordinate cones respectively cover x4>=x5 and x5>=x4). I exactly multiplied both identities: V_i^T H V_i=P_i+N_i for i=1,2; P_1 and P_2 each have rank one and are PSD, while every entry of N_1,N_2 is nonnegative. Thus each branch quadratic form is nonnegative for nonnegative branch coordinates, proving H copositive without treating H as ordinary P+N. The same exact check gives (e1+e2)^T H(e1+e2)=0, so H is boundary copositive and lies outside the strict-positivity scope of Theorems 1 and 11; this rules out an invalid finite-stage extrapolation.
- 结论位置。Strict-positive-form theorem and local identity, pp.8–9; imported compact-POP reduction and Theorem 10, pp.25–26; fully displayed finite Horn two-cone certificate, pp.28–29.
- 适用范围。The ready result is only this two-branch Horn certificate. The general fixed-dimension strict-positive disjunction theorem is not a boundary-nonnegativity theorem, and p.25’s convergence statement additionally imports [2, Theorems 2.1 and 2.4], a compact radius, and all hierarchy properties. No arbitrary C03 SOS hierarchy is certified.
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 已采用构件。给定 Horn 矩阵及两锥的精确覆盖、余正性和逐锥 SPN 证书。 [math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/references/horn-two-cone-spn.md)
- 其余依赖。If promoted, package the two exact rational V/P/N identities as a tiny Horn-only certificate with symbolic expansion and branch-coverage checks. Audit the net construction and cited compact-POP reduction independently before exposing any general disjunctive hierarchy or lower-bound convergence claim.
- [主来源 1](https://arxiv.org/abs/2605.28674)

## Enhancing Presolve in Mixed Integer Programming by Combining Probing and Dual Fixing

- 原件 3bf4856c846a0a634e0a356a50ffb92aa94e0e71f80b3ae99f34b1071a2a7b09。arXiv:2607.10767v1 (12 July 2026), local 15-page PDF。物理页 5, 6, 8, 9, 13。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2607.10767v1, stated accepted for Mathematical Programming Computation; no version of record/DOI identified
- 构件候选。The reachability theorem has a finite exact core: for each negative a_rj, resetting x_j to its lower bound preserves row r exactly when o^-_rj+a_rj l_j<=b_r; the positive-coefficient case is symmetric. I exhaustively checked the paper’s binary Example 3.1: its feasible set is {(0,0,0),(0,1,0),(0,1,1),(1,0,0),(1,0,1)}, o^-_{2,3}=max(8x1+4x2)=8, and every feasible point with x3=1 remains feasible after x3:=0. This verifies the stated lower-bound-reachability condition rather than relying on a solver status. Conversely, pp.5–6 exhibit why individually optimum-preserving c_j=0 implications cannot simply be accumulated, an active safety constraint on any implementation.
- 结论位置。Algorithm 1 p.5; the zero-objective-coefficient interference counterexample pp.5–6; Theorem 1 and proof pp.8–9; benchmark-only conclusion p.13.
- 适用范围。The theorem needs the exact bounded MIP convention, all original constraints, correctly directed certified auxiliary optima and the stated objective-sign rule. It does not turn probing heuristics or benchmark timing into proof, and the accepted preprint has no checked version of record.
- 相关技能。[math-l04-mathematical-programming-workflow](../../../../math-l04-mathematical-programming-workflow/SKILL.md)
- 其余依赖。A safe L04 extension needs rational MIP certificates (or independently reproducible exhaustive proofs) for each o^- / o^+ bound and each propagation implication, plus an explicit policy that discards/revalidates c_j=0 branch implications before combining reductions.
- [主来源 1](https://arxiv.org/abs/2607.10767)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。Current L04 correctly treats solver outputs as candidates and its provenance labels this source irrelevant to its generic workflow. The source's exact reachability fixing condition is useful but requires certified auxiliary optima and expressly warns that zero-objective branch implications cannot simply be accumulated.。定位。physical pp. 5--6, 8--9 and 13; Algorithm 1, interference counterexample, Theorem 1 and benchmark boundary。全卷 15 页。后续条件。For every proposed fixing, provide a rational/exhaustive certificate for the directed auxiliary bound and an explicit combination policy that discards or revalidates c_j=0 implications.。
- 复核记录。2026-11-26T19:04:42+08:00。candidate。dependency。
- 本次依据。The reachability fixing condition is a genuine finite MIP implication, but each auxiliary o-minus or o-plus bound and propagation implication needs a certificate. The paper explicitly shows that zero-objective branch implications cannot be freely accumulated.。定位。physical pp. 5--6 and 8--9, Algorithm 1, interference example, and Theorem 1。全卷 15 页。后续条件。Provide rational or exhaustive certificates for every directed auxiliary bound and an explicit policy that discards or revalidates zero-objective branch implications before combining reductions.。
- 复核记录。2026-11-26T19:33:26+08:00。adopted-local。component。
- 本次依据。The source gives a safe conditional policy for combining certified probing/dual-fixing reductions, including a concrete warning for zero-objective branches。定位。physical pp. 5--9; Algorithm 1, interference example, Theorem 1。全卷 15 页。后续条件。Certify every auxiliary bound and propagation implication; discard or jointly revalidate zero-objective branch implications。
- 已采用构件。物理页 5, 6, 7, 8, 9。Certified reduction combination guard; zero-objective branches require discard or revalidation. [方法说明](../../../../math-l04-mathematical-programming-workflow/references/probing-dual-fixing-combination-policy.md)。

## Exact SDP Relaxations for a Class of Quadratic Programs with Finite and Infinite Quadratic Constraints

- 原件 01257b41bc5a72ebb2fea41c69442337285364fb9195c5a2d80d5f462ec4fef1。Local PDF dated 10 June 2026, 28 physical pages; SHA verified。物理页 1, 2, 4, 5, 6, 14。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。SIAM Journal on Optimization 36(4) (2026), 1973-1996, DOI 10.1137/24M1692745; checked publisher record. Original e-print: arXiv:2409.07213。
- 已有技能。The local proof supports a conditional exactness component for semi-infinite QCQPs: Theorem 1.4 permits an infinite constraint family only after a face F containing J+(B) and the pairwise nesting condition (B) are established; then J+(B) is in the designated rank-one convex-hull family. The published SIAM record confirms the paper is no longer only a manuscript。
- 结论位置。Local pp. 1-2 define the conic exact-relaxation framework and Theorem 1.1; p. 4 states finite conditions in Theorem 1.2; p. 5 states NIQCC Theorem 1.3; p. 6 states the infinite-family facial condition (B) in Theorem 1.4; p. 14 proves the required convex-hull identity by finite subfamilies and closure。
- 适用范围。This is not B02's constraint-generation/exchange guarantee and it is not a general SDP-exactness test. The proof depends on the facial-reduction setup, condition (B), and the conic result Theorem 1.1; no solver-facing predicate or verifier for those hypotheses is implemented in B02。
- 相关技能。[math-c01-semidefinite-lifting](../../../../math-c01-semidefinite-lifting/SKILL.md)
- 其余依赖。Implement only after specifying computable certificates for F and condition (B), and separately verify that the user QCQP has the paper's homogeneous conic reformulation and finite optimal value。
- 已采用构件。对给定的有限约束、秩一可行点和有理非负乘子，认证 QCQP 与 Shor 松弛同值。原文半无限 ROG 条件另核。[使用说明](../../../../math-c01-semidefinite-lifting/references/arima-kim-kojima-finite-qcqp-certificate.md)
- [主来源 1](https://arxiv.org/abs/2409.07213) · [主来源 2](https://doi.org/10.1137/24M1692745)

## Examples of inconsistency in optimization by expected improvement

- 原件 9613fdac4553e3a2e1296c42ea97484cfac5641069de66fc69d13a01fa899eb3。arXiv:1109.1320v2 (2 April 2012), local 21-page PDF。物理页 6, 7, 16, 17, 19。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。Yarotsky, Journal of Global Optimization 56(4) (2013), 1773–1790, DOI 10.1007/s10898-012-9936-x
- 构件候选。The key source-specific premise is correctly stronger than a numerical EI observation: for f=-G(.-x1), the noiseless posterior interpolant is already f, so exact EI reduces to the conditional-variance expression (36). I independently solved the symbolic 2-by-2 Gaussian-kernel interpolation system at samples 0,t: K^{-1}[-G(0),-G(t)]^T=(-1,0)^T, confirming the claimed posterior-mean identity rather than merely sampling it numerically. With Theorem 2’s spectral hypotheses, the later conditional-variance bounds yield the stated x_K->0; this is a well-defined failure-mode template.
- 结论位置。Kernel spectral assumptions Theorem 2 p.6; non-dense exact-EI construction Theorem 3 and Gaussian corollary p.7; posterior-mean/EI identity p.16; variance/EI bounds pp.16–17; convergence conclusion p.19.
- 适用范围。The result is not a claim about arbitrary Bayesian optimization, noisy observations, hyperparameter refitting, approximate maximization or unspecified tie-breaking. It needs the one-dimensional compact domain, fixed stationary kernel with the exact spectral conditions, x1=0, f=-G for Theorem 3, and a separate smooth modification for the Gaussian C-infinity corollary; the analytic f itself is not that modified objective.
- 相关技能。[math-l02-adversarial-input-search](../../../../math-l02-adversarial-input-search/SKILL.md)
- 其余依赖。Any L02 counterexample replay must fix a concrete kernel satisfying Theorem 2, exact posterior and global EI-maximization/tie rules, then retain a proof/certificate for each maximizer. Do not generalize a finite numerical trajectory into the theorem’s non-density conclusion.
- [主来源 1](https://doi.org/10.1007/s10898-012-9936-x) · [主来源 2](https://arxiv.org/abs/1109.1320)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。L02's current finite counterexample-search scope does not cover exact expected-improvement dynamics; its provenance labels this exact source irrelevant. The paper supplies a narrow, fixed-kernel noiseless non-density construction, not an arbitrary Bayesian-optimization failure certificate.。定位。physical pp. 6--7 and 16--19; Theorems 2--3, exact posterior/EI identity and variance conclusion。全卷 21 页。后续条件。Fix a one-dimensional compact domain, a kernel satisfying Theorem 2, exact posterior/EI global maximization and tie rules; retain a proof for every maximizer rather than extrapolating a numerical trajectory.。
- 复核记录。2026-11-26T19:04:42+08:00。candidate。dependency。
- 本次依据。The fixed-kernel noiseless expected-improvement counterexample is a concrete failure-mode template, but L02 has no exact Gaussian-process posterior, global EI maximization, or tie-rule certificate interface.。定位。Physical pp. 6--7, Theorems 2--3; pp. 16--19 posterior/EI identity and variance conclusion.。全卷 21 页。后续条件。Fix a one-dimensional compact domain and kernel satisfying Theorem 2, then certify each exact posterior and globally maximizing EI point with its tie rule.。
- 复核记录。2026-11-26T19:33:26+08:00。adopted-local。component。
- 本次依据。The published source gives a proof-backed fixed-kernel noiseless EI non-density construction; the posterior identity f=-G(x-x1) removes any reliance on a numerical EI trajectory。定位。Physical pp. 6--7, Theorems 2--3 and Gaussian corollary; pp. 16--19, posterior/EI identity and convergence proof。全卷 21 页。后续条件。Fix a kernel meeting Theorem 2, exact posterior and globally maximizing EI rule with deterministic ties, then retain a proof certificate for each claimed maximizer。
- 已采用构件。物理页 6, 7, 16, 17, 18, 19。Fixed stationary kernel, exact noiseless EI, domain [-1,1], x1=0 and f=-G. It is a non-density counterexample template, not a claim about general Bayesian optimization. [方法说明](../../../../math-l02-adversarial-input-search/references/yarotsky-fixed-kernel-ei-nondensity.md)。

## Exploiting Ideal-sparsity in the Generalized Moment Problem with Application to Matrix Factorization Ranks

- 原件 d2ee235cf7790ae962261d9030372694b43f3f51e6a310c6739341d431e39bc8。Local preprint dated 11 Jul 2023, 37 physical pages; SHA verified。物理页 1, 2, 4, 11, 12, 13, 28, 31。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Mathematical Programming 205 (2024), 703-744, DOI 10.1007/s10107-023-01993-x; checked publisher record. Original e-print: arXiv:2209.09573。
- 已有技能。The source independently supports a conditional ideal-sparsity module: a measure supported on the quadratic-monomial ideal variety is decomposed over maximal cliques, producing an equivalent measure reformulation; Theorem 7 gives the finite-level lower-bound ordering and, with Archimedeanity and its Slater-type condition (7), asymptotic convergence. The canonical journal version is verified。
- 结论位置。Local pp. 1-2 define GMP support constrained by quadratic bilinear monomial ideals; p. 4 defines the dense hierarchy; pp. 11-12 complete the measure decomposition and state Theorem 7 (xi_t <= xi^isp_t <= val plus conditional convergence); p. 13 compares supergraph-clique variants; p. 28 specializes an ideal-sparse nonnegative-rank hierarchy; p. 31 records the maximal-biclique scalability obstruction。
- 适用范围。The construction requires the stated ideal/graph and clique cover; its hierarchy direction is xi_t <= xi^isp_t <= val for minimization. It does not make arbitrary correlative sparsity equivalent, and maximal-clique explosion remains an explicit computational limitation. B03 has no implemented graph/ideal recognition, clique decomposition, or flatness/extraction verifier。
- 相关技能。[math-b03-generalized-moments](../../../../math-b03-generalized-moments/SKILL.md)
- 其余依赖。Implement only with exact validation of monomial-ideal support, clique enumeration, Slater-type condition (7), Archimedeanity, hierarchy direction, and a size guard for maximal-clique enumeration; use flatness separately for factor recovery。
- 已采用构件。显式有限正原子的非边理想检查、极大团分解和局部矩重组，其有限证明独立。[使用说明](../../../../math-b03-generalized-moments/references/ideal-sparse-finite-guide.md)
- [主来源 1](https://arxiv.org/abs/2209.09573) · [主来源 2](https://doi.org/10.1007/s10107-023-01993-x)

## Facial structure of copositive and completely positive cones over a second-order cone

- 原件 5f9131bfa83088d87854d91842ca15c71752e137db9929e4d02f3c9b6b6e8341。Local arXiv:2502.04006v2 PDF dated 17 Apr 2026; independently SHA-256 matched and counted 40 physical pages.。物理页 3, 10, 15, 20。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2502.04006v2 (no journal edition established in the supplied record).
- 构件候选。The source really gives the stated Lorentz-cone case split, but the prior reusable gate is only partly closed. I independently derived the PSD subface step used on p.10: for a=(1,0,0), P⪰0 and a^T P a=P_11=0 imply |P_1j|^2≤P_11P_jj=0, hence Pa=0 and range(P)⊂a^⊥; conversely this is exactly S_+(a^⊥). Exact SymPy evaluation used P=diag(0,1,4), obtaining P a=0 and eigenvalues 0,1,4. This validates that finite PSD-face inference, and p.15 directly shows why the boundary case has the extra R_+J_n branch/non-exposed rays.
- 结论位置。Physical p.10, Theorem 3.1 and its use of (2.6)/Lemmas 2.3, 2.6, 2.8; p.15, Theorem 3.9 and Proposition 3.10; p.20, boundary rank-one rays.
- 适用范围。This does not independently establish the indispensable special representation COP(L_n)=S_+^n+R_+J_n or the H(V) witness Lemmas 2.6--2.8. Therefore it is neither a general COP/CP facial classifier nor a release-ready C02 extension; importing p.10 without those lemmas would be circular.
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。Audit/derive the Lorentz representation and H(V) certificate with an exact input interface; retain separate interior, boundary-exposed, and boundary-non-exposed outcomes.
- [主来源 1](https://arxiv.org/abs/2502.04006)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。C02 tracks this SHA but does not implement the Lorentz-cone facial classifier. The source's PSD subface observation is elementary; the actual interior/boundary/non-exposed classification indispensably uses COP(L_n)=S_+^n+R_+J_n and H(V) witness lemmas not closed in the current skill.。定位。physical pp. 3, 10, 15 and 20; Theorems 3.1 and 3.9, Proposition 3.10 and boundary rays。全卷 40 页。后续条件。Provide an exact Lorentz/Jordan data model and independently certify the representation and H(V) lemmas; keep separate interior, exposed boundary and non-exposed boundary outcomes.。
- 复核记录。2026-11-26T19:04:42+08:00。candidate。dependency。
- 本次依据。The Lorentz-cone facial cases use the special COP(L_n)=S_+^n+R_+J_n representation and H(V) witness lemmas. The elementary PSD subface argument alone does not establish the source's interior, exposed-boundary, and non-exposed-boundary classification.。定位。physical pp. 5--8, 10--16, and 20, Lemmas 2.2--2.8, Theorems 3.1 and 3.9, and boundary rays。全卷 40 页。后续条件。Provide an exact Lorentz or Jordan data model and independently certify the representation and H(V) lemmas while preserving the three distinct face outcomes.。
- 复核记录。2026-11-26T19:33:26+08:00。adopted-local。component。
- 本次依据。The paper provides a source-scoped Lorentz-cone facial case split, explicitly dependent on the special COP(L_n) representation and H(V) witnesses。定位。physical pp. 5--16; Lemmas 2.2--2.8, Theorems 3.1 and 3.9, Proposition 3.10。全卷 40 页。后续条件。Caller must supply Lorentz representation and exact witness data; do not generalize to arbitrary CP/COP cones。
- 已采用构件。物理页 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16。Lorentz-cone source-scoped facial cases requiring representation and witnesses. [方法说明](../../../../math-c02-completely-positive-copositive/references/lorentz-copositive-facial-guard.md)。

## Free Energy and Phase Transition for 2D Directed Polymers with Critical Spatial Correlations

- 原件 25b1a814b6261eccaf5a544d2c50a8be925e9e200046c596de4c301dc7db4386。local PDF metadata: arXiv:2608.30829v2。物理页 1, 2, 3, 4, 5, 7, 10, 11, 13, 15。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.30829v2 (1 Sep 2026)。
- 邻近材料。The local PDF metadata identifies the exact current arXiv v2, matching the checked primary arXiv record. Under its Gaussian 2D spatial-correlation assumptions, Theorem 1.1 gives the stated small-beta free-energy asymptotics; pp. 10–15 derive its upper/lower bounds from a supercritical estimate and subcritical second-moment estimates. D03 does not invoke this model-specific theorem: its installed generic finite-domain inequality is separately derived and its provenance currently labels this source adjacent。
- 结论位置。Local Theorem 1.1 and its bounds, pp. 4, 10–15; second-moment phase transition pp. 5–7。
- 适用范围。The proof is tied to a directed polymer, a specified summable/logarithmic covariance regime, beta downarrow 0 scaling, and imported results named in the text. It cannot justify D03 statements for arbitrary parameters, signs, reference measures, or free-energy conventions。
- 相关技能。[math-d03-parameterized-free-energy](../../../../math-d03-parameterized-free-energy/SKILL.md)
- 其余依赖。No active dependency. Any reuse would need an explicit model match and verification of Assumptions 1–2 plus the imported supercritical result used at p. 10。
- [主来源 1](https://arxiv.org/abs/2608.30829)

## Gibbs Conditioning Principle for Log-Concave Independent Random Variables

- 原件 5cc3b0c173591365eab683597e31d553c48869aba466bd58493c1dcf2527c723。arXiv:2512.24910v3, revised 19 Jun 2026 (local 14-page source PDF)。物理页 2, 3, 4, 5, 6, 7, 12。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Markov Processes and Related Fields 32 (2026), 63–77 is listed as the journal reference by the checked arXiv v3 record; publisher text was not separately inspected。
- 邻近材料。Theorem 1 is verified at its stated level: for independent log-concave Z_+-valued variables, lambda* in the stated moment range, and condition (1), the relevant upper-tail, lower-tail, or exact-sum conditional laws converge in finite-dimensional distribution to the lambda*-tilted product law. The proof uses stochastic ordering of conditioned canonical measures and a moment-generating-function estimate, not D02's finite KL/Gibbs variational identity。
- 结论位置。PDF pp. 2–4 introduce the tilt, condition (1), and Theorem 1; pp. 5–7 prove the conditional-limit theorem using Proposition 2 and Lemma 3; p. 12 completes the canonical-measure monotonicity proof used for Theorem 5。
- 适用范围。D02 correctly confines its reusable result to finite-domain entropy identities and warns against treating a physics source as a general Donsker–Varadhan proof. This conditional-limit theorem is not an entropy-duality dependency and cannot be transferred to arbitrary reference measures, continuous variables, iid-free models, or conditioning events without its log-concavity and condition (1)。
- 相关技能。[math-d02-gibbs-entropy-duality](../../../../math-d02-gibbs-entropy-duality/SKILL.md)
- [主来源 1](https://arxiv.org/abs/2512.24910)

## Isoperimetric Problems Related to Extremal Diameter Graphs in 3D: Theoretical and Numerical Aspects

- 原件 e112ec7f105cf4cf7fcf6aa1008cbd7668460072730e6fd7e982bee8a397c618。Local arXiv:2608.26395v1 PDF; independently SHA-256 matched and counted 30 physical pages.。物理页 7, 8, 10, 11, 12, 15, 16, 20, 21, 28。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2608.26395v1 (26 Aug 2026; no journal edition established in the supplied record).
- 构件候选。The actual controlling limit gate is correctly conditional. Proposition 2 proves exact core preservation only for a convergent sequence of exact extremal configurations. Proposition 5's proof on p.11 is a finite-sum argument: matched terms converge; nonnegative unmatched terms yield liminf; continuity additionally needs stability and F(s,0)=F(0,s)=0. I independently checked the sharp obstruction algebraically: for a disappearing pair with q=(1/n,1), F_prod(s,t)=st has limit 0, whereas F_sum(s,t)=s+t has limit 1. Thus deleting unmatched terms cannot in general give continuity without the axis-vanishing condition; the source's dangling-edge warning is mathematically material, not cosmetic.
- 结论位置。Physical pp.7--9, Proposition 2; pp.10--11, Definition 4, Proposition 5 and Remarks 6--7; pp.15--16, additive bound; pp.20--21, reformulation; p.28, numerical scope.
- 适用范围。The scalar check is a necessary-condition witness, not a geometric realization of every collision. Compatibility/stability of exposed dual pairs is still an additional hypothesis, and finite fixed-graph numerics do not certify arbitrary limits or the Blaschke--Lebesgue problem.
- 相关技能。[math-a03-compactness-concentration](../../../../math-a03-compactness-concentration/SKILL.md)
- 其余依赖。Any usable A03 branch must accept exact configuration/core and compatible-pair witnesses, then explicitly check stability plus the axis-vanishing property of F; a separate geometric proof is needed for a target family.
- [主来源 1](https://arxiv.org/abs/2608.26395) · [主来源 2](https://arxiv.org/pdf/2608.26395)
- 复核记录。2026-11-26T18:11:16+08:00。adopted-local。component。
- 本次依据。Proposition 5 contains a self-contained finite-sum lower-semicontinuity/continuity gate once compatible lifts, stability, bounded sizes, and pairwise continuity are supplied. It is a nonduplicate compactness handoff, with its geometric core construction explicitly left to the caller.。定位。Proposition 2 (pp. 7--9); Definition 4 and Proposition 5 with Remarks 6--7 (pp. 10--11)。全卷 30 页。后续条件。Caller must independently establish the exact extremal core and compatible/stable exposed-pair lifts for the target geometric family.。
- 已采用构件。物理页 7, 8, 9, 10, 11。A finite paired-cost limit gate conditional on caller-provided exact core, compatible lifts, stability, and bounded pair sizes; it is not a general geometric compactness theorem. [方法说明](../../../../math-a03-compactness-concentration/references/wave7-historical-01-paired-functional-collapse.md)。

## Learning-enabled Acceleration of Scenario-based Model Predictive Control

- 原件 f9c697c4e8b985c51b76d60a8dc48a9c8fb5b6ec523f70826993684ed14d3c26。Local 6-page PDF has no embedded arXiv version line; SHA-256 and page count were verified. Its title, authors, consensus model, and experiment text agree with the checked arXiv record, but byte equality and the local revision number were not established。物理页 1, 2, 3, 4, 6。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2607.12775v3 (2026-11-11), the current checked arXiv version; no publisher version was identified in the checked primary record。
- 邻近材料。The source explicitly writes scenario-independent controls as a special P u=0 consensus constraint and gives ADMM updates for its finite-scenario convex MPC formulation. The learning component replaces local proximal calculations by a learned Moreau-envelope gradient; the displayed accuracy evidence is numerical on the microgrid instances。
- 结论位置。PDF p.2 finite-scenario convex MPC and P u=0 nonanticipativity choices; p.3 consensus-ADMM iteration and learned Moreau-envelope replacement; pp.4 and 6 microgrid setup and numerical residual/gap report。
- 适用范围。It provides neither a proof that the learned proximal replacement preserves ADMM convergence nor a general nonanticipativity-equality construction. Its P matrices enforce either all-horizon or first-step equality only, unlike arbitrary scenario-history information blocks in A04。
- 相关技能。[math-a04-shared-nonanticipative-mip](../../../../math-a04-shared-nonanticipative-mip/SKILL.md)
- 其余依赖。No active A04 claim relies on this paper. Any implementation needs an exact local-revision check against arXiv v3, convexity and approximation-error controls for the learned proximal map, and a convergence/residual analysis for the modified ADMM rather than the unmodified consensus iteration。
- [主来源 1](https://arxiv.org/abs/2607.12775)

## Lower Bound for a Polynomial on a Product of Hyperellipsoids Using Geometric Programming

- 原件 843a48df6c822c8c6437e285b1547a30d075937734864304448be51e39022974。arXiv:2510.03105v1 (3 Oct 2025)。物理页 1, 2, 3, 4, 5。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2510.03105v1; local 10-page manuscript matches title, authors, theorem numbering, and v1 metadata (no later formal publication identified)。
- 邻近材料。Theorem 3.1 is confirmed at citation level: for even d≥max(2,deg f), positive N_i, and a partition I_1,…,I_m defining the prescribed product of hyperellipsoids, its geometric program returns s(f,g), a lower bound on f over K_g. The proof invokes Theorem 2.1’s sum-of-binomial-squares lower bound for G(λ)=f−Σλ_jg_j and then optimizes the displayed feasible construction. This is not evidence for L01’s finite-measure average identity or its unproved grid-to-cell transfer。
- 结论位置。local pp.3–5, Theorem 2.1, Theorem 3.1, and proof; arXiv abstract/HTML checked。
- 适用范围。The result is limited to the displayed diagonal even-degree constraint form and coefficient/feasibility conditions. An empty GP feasible set yields the stated −infinity outcome; a numerical solver result, a generic polynomial domain, or a claimed exact optimum does not follow. Runtime comparisons are experiments, not a certificate。
- 相关技能。[math-l01-lower-bound-test-parameters](../../../../math-l01-lower-bound-test-parameters/SKILL.md)
- 其余依赖。Keep as a cited polynomial-optimization method unless a separate geometric-programming skill proves input parsing, GP feasibility, rigorous solution certification, and the lower-bound direction; it cannot close L01-METHOD-01。
- [主来源 1](https://arxiv.org/abs/2510.03105) · [主来源 2](https://doi.org/10.48550/arXiv.2510.03105)

## Monge Solutions and Uniqueness in Multi-Marginal Optimal Transport with Hierarchical Jumps

- 原件 4e4f65485ed8c30eae404e5693b9cd6761e5e9723ccbfff42d91c086116ea495。Local arXiv:2512.14072v3 PDF revised 25 Jun 2026; independently SHA-256 matched and counted 22 physical pages.。物理页 4, 5, 9, 10, 14, 15, 16。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2512.14072v3.
- 邻近材料。The paper's uniqueness proof is correctly source-specific: once local control makes the sequential derivative equal to the same derivative of h for all supported continuations, sequential twist forces the fibre to be a singleton (p.15), and disintegration gives the Monge map (pp.15--16). I independently checked why this cannot transfer to an unconstrained finite LP: with both endpoint marginals (1/2,1/2) and zero cost, all matrices [[a,1/2-a],[1/2-a,a]], 0≤a≤1/2, are optimal. Exact rational checks at a=0,1/4,1/2 give two distinct deterministic couplings and one nondeterministic coupling. Hence existence/finite coupling feasibility alone supplies neither twist nor uniqueness.
- 结论位置。Physical pp.4--5, variable-marginal HJMOT definition; p.9, existence proof; p.10, sequential twist/strong coercivity; pp.14--16, Theorem 3.1 proof.
- 适用范围。This record does not implement the finite causal-OT route, and the general Polish-space theorem still depends on its stated coercivity, local-control and (discrete-type) sequential-twist hypotheses. It is not an extension of basic fixed-marginal Kantorovich duality.
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Keep any finite causal-OT construction separate; an HJMOT installation would need an explicit variable-intermediate-marginal encoding and a per-instance proof of the source's coercivity/twist hypotheses.
- [主来源 1](https://arxiv.org/abs/2512.14072)

## Multistage Distributionally Robust Mixed-Integer Programming with Decision-Dependent Moment-Based Ambiguity Sets

- 原件 d385bcf78de7640dcc31dbdfca79dbe59db48ea33c720efe7860ceb5c8272d28。Local PDF is arXiv:2002.12518v3 (2020-09-25); its SHA-256 and 39 physical pages were verified。物理页 1, 5, 8, 12, 13, 14, 15, 37, 39。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Mathematical Programming, Series B, 196 (2022), 1025–1064; published online 2020-10-21; DOI 10.1007/s10107-020-01580-4. Checked e-print: arXiv:2002.12518v3。
- 邻近材料。The local v3 and publisher record agree on the three decision-dependent ambiguity-set models. For Type 1, Theorem 1 assumes every feasible state has a nonempty ambiguity set; Type 3 explicitly requires strict feasibility and yields an MISDP reformulation. Proposition 1 only makes the relaxed Lagrangian cuts lower-valid for binary prior states, while p.14 states that the cuts need not be tight and do not guarantee optimal convergence。
- 结论位置。PDF p.8 Theorem 1; p.12 Theorem 3; pp.13–15 the exact-McCormick/MISDP bounds and Proposition 1; pp.37–39 the finite-support LP/conic-duality proof steps and Slater use。
- 适用范围。These are decision-dependent DRO Bellman reformulations and SDDiP bounds, not the A04 claim that nonanticipativity equalities are sufficient exactly when each information-block graph is connected. The reported exact MILP language also depends on binary decisions, stated affine moment structures, finite support, and the listed McCormick products; it cannot be imported as a generic shared-choice MIP method。
- 相关技能。[math-a04-shared-nonanticipative-mip](../../../../math-a04-shared-nonanticipative-mip/SKILL.md)
- 其余依赖。No active A04 claim depends on this paper. A separate DRO implementation would need a complete state/filtration contract, nonemptiness (and Type-3 Slater) certificates at every feasible state, verified variable bounds for every McCormick product, and an independent SDDiP convergence argument。
- [主来源 1](https://arxiv.org/abs/2002.12518) · [主来源 2](https://link.springer.com/article/10.1007/s10107-020-01580-4)

## New Extremal Principles with Applications to Stochastic and Semi-infinite Programming

- 原件 ff08a2dba86a58558e9434e2ee4f13e8f057ce0759c8f4e70f604e0ed27c8830。arXiv:1911.10850v3 (22 Jul 2020), 26 physical pages; SHA verified。物理页 1, 2, 23, 24, 25。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:1911.10850v3 (22 Jul 2020); no publisher version was identified from the checked primary source。
- 邻近材料。Theorem 7.1 is a local necessary normal-cone condition, derived through a measure-integral of pointwise normals. Its proof explicitly uses normal regularity of the essential intersection and dense-set CHIP (or the stated conic-at-origin alternative); the inequality specialization adds differentiability, active-index, and continuity requirements。
- 结论位置。Local pp. 1-2 state the measurable-multifunction optimization framework; p. 23 states Theorem 7.1 and begins its proof; p. 24 gives the inequality-constraint specialization; p. 25 gives Corollary 7.4 for linear inequalities。
- 适用范围。B02's implemented workflow concerns global separation and exchange iterates. This paper supplies neither a separation oracle nor a restricted-master convergence/termination statement; moreover the displayed normal inclusion retains a closure. It cannot validate B02's global exchange claims。
- 相关技能。[math-b02-semi-infinite-exchange](../../../../math-b02-semi-infinite-exchange/SKILL.md)
- 其余依赖。If a future variational KKT diagnostic is desired, first encode and check local minimality, normal regularity, measurable CHIP, and the required normal-cone representation; otherwise retain it as an adjacent citation only。
- [主来源 1](https://arxiv.org/abs/1911.10850)

## New Outer Approximation Algorithms for Nonsmooth Convex MINLP Problems

- 原件 69909f6afc65e3b2954766721918786782fc880653a9198fb07caea45dc1d34c。Local arXiv:2602.04122v1 PDF; independently SHA-256 matched and counted 25 physical pages.。物理页 6, 7, 10, 11, 12, 13, 14。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2602.04122v1 (4 Feb 2026).
- 构件候选。The exact operative condition is KKT compatibility, not merely collecting slopes. I independently instantiated the infeasible-cut proof with X=[0,1], y∈{0,1}, g(x,y)=x+y. For y=1, min_X g=1 at x=0; choose λ=1 and (ξ,η)=(1,1), so -λξ=-1 is in N_X(0). The p.11 linearized cut is 1+(x)+(y-1)≤0, namely x+y≤0, which excludes y=1 and retains the feasible point (0,0); exact rational grid evaluation produced min g=0 for y=0 and 1 for y=1. This realizes the source proof's normal-cone/KKT condition and verifies its sign direction.
- 结论位置。Physical pp.6--7, A1/KKT and Proposition 3.1; pp.10--11, infeasibility cut; p.12, master equivalence and KKT warning; pp.13--14, nonrepetition termination proof.
- 适用范围。The one-dimensional instance does not certify a solver's multipliers, selected subgradients, rho parameters, or globally solved nonlinear feasibility subproblems. The finite-termination theorem additionally needs a finite integer set and the nonrepetition argument; arbitrary reported gradients cannot justify the master equivalence.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Require rational/verifiable KKT and infeasibility certificates (including normal-cone and rho checks) before a reusable A02 branch; otherwise retain only as a source candidate.
- [主来源 1](https://arxiv.org/abs/2602.04122) · [主来源 2](https://arxiv.org/pdf/2602.04122)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。Physical pp.10–12 give a precise KKT-gated infeasible-integer cut: solve F(y), choose lambda and subgradients satisfying (3.23)–(3.25), and (3.26) excludes y by the weighted contradiction in Proposition 3.3. This is stronger than merely collecting slopes and is not an executable interface in the current A02 skill, which requires caller-supplied valid cuts and global masters.。定位。Physical pp.10–12: feasibility problem (3.19), KKT relations (3.20)–(3.25), Proposition 3.3 and Theorem 3.2.。全卷 25 页。后续条件。A reusable route needs an exact schema and verifier for F(y)'s global minimizer, the normal-cone inclusion, all multiplier cases, lifted joint subgradients, and the finite-integer/master assumptions in Theorem 3.2.。
- 复核记录。2026-11-26T19:04:42+08:00。candidate。dependency。
- 本次依据。The source gives a KKT-gated infeasible-integer cut, but A02 currently accepts caller-supplied valid cuts and has no verifier for the global convex feasibility subproblem or the nonsmooth multiplier cases.。定位。Physical pp. 10--14, feasibility problem (3.19), KKT relations (3.20)--(3.25), Proposition 3.3 and Theorem 3.2.。全卷 25 页。后续条件。Provide a rational certificate format for the global feasibility minimum, normal-cone inclusion, multiplier and joint-subgradient relations, together with the finite-integer master assumptions.。
- 复核记录。2026-11-26T19:33:26+08:00。adopted-local。component。
- 本次依据。The preprint's feasible and infeasible nonsmooth MINLP cuts are reusable only under its explicit global KKT/subgradient certificates。定位。physical pp. 6--14; Propositions 3.1--3.3 and Theorem 3.2。全卷 25 页。后续条件。Certify global subproblem solutions, normal-cone and multiplier relations, and finite-integer master assumptions。
- 已采用构件。物理页 6, 7, 8, 9, 10, 11, 12, 13, 14。KKT-gated nonsmooth convex MINLP cuts and finite-integer termination only. [方法说明](../../../../math-a02-outer-relaxation-budget/references/nonsmooth-minlp-kkt-outer-cuts.md)。

## On Computing the Copositive Minimum and its Representatives

- 原件 673f26accc0cd74ed08fceae15ee0ad05f6381cbc8eb573dab336f6878d1a732。arXiv:2509.23696v1 (28 Sep 2025), byte-matched local 19-page PDF。物理页 1, 2, 3, 4, 7, 8, 12, 13, 15。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2509.23696v1; no formal publication identified in the checked source record
- 已有技能。A reusable exact finite certificate was independently derived and tested: with a rational SPD leading block, rational nonnegative KKT minimizer for the slice x_n=1, and rational spectral lower bound, f(s)=s^2 f(1) bounds x_n. Completing the square bounds remaining coordinates, so direct rational enumeration covers every nonnegative integer x with Q[x]<=lambda. The source example gives f(1)=3/2, x_n<=1 and nonzero minimum 2. The checker matched brute-force enumeration in 90 seeded rational instances.
- 结论位置。Local pp. 7–8 give exact LDLT completion of squares. Pages 12–13 prove Lemma 5.1 and the one-difficult-coordinate bound. Page 15 records the general multicoordinate obstruction.
- 适用范围。The interface requires the supplied positive-definiteness, KKT and spectral certificates. It does not decide copositivity, create an SPN decomposition or handle several difficult coordinates.
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 已采用构件。给定正定主块、谱下界和单坐标切片 KKT 证人的有限整数最小值枚举。 [math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/references/one-difficult-coordinate.md)
- 其余依赖。Integrate the overlay script, examples and reference into C02, then independently rerun positive, invalid-KKT and finite-enumeration checks in the release package.
- [主来源 1](https://arxiv.org/abs/2509.23696)

## On the Monge-Kantorovich Problem with Additional Linear Constraints

- 原件 335316951595dde0686a29e2d5a482d11054c4d8e448dff06b9c40ed663df864。local arXiv:1404.4962v1 (19 Apr 2014), 20 pages。物理页 1, 5, 6, 8, 9。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:1404.4962v1; official record lists v1 only
- 已有技能。The strongest independently defensible transferable component is a finite constrained-OT constructor: impose the finite linear moments ∫w_j dπ=0 alongside marginals, and certify the LP dual with potentials f_i plus a multiplier omega in span{w_j}, satisfying f_1+...+f_n+omega≤c. Zaev's Theorem 2.1 is the infinite Polish-space analogue for W⊂CL(mu), obtained by ordinary duality plus compact-convex minimax.
- 结论位置。PDF p. 1 problem statement; p. 5 compactness/continuity preparation; p. 6 ordinary CL(mu) duality and minimax inputs; pp. 8–9 Theorem 3.6 and its necessary monotonicity proof.
- 适用范围。This is not ordinary D01 coupling duality and (c,W)-monotonicity is only necessary in the general result. Infinite-dimensional use retains CL(mu), nonempty constrained plans, topology/integrability, and the additional Theorem 3.6 hypothesis.
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 已采用构件。限定接口已写入 [math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/references/finite-constrained-transport.md)。
- 其余依赖。Before integration, implement and test the finite LP primal/dual certificate; for the Polish extension independently verify the CL(mu) closure/minimax hypotheses and the exact restriction condition on W in Theorem 3.6.
- [主来源 1](https://arxiv.org/abs/1404.4962)

## Outer Approximations of Core Points for Integer Programming

- 原件 3971b19fd8672edb6d104fa7c15ac24261e14e965991a717c0c36a6217d96570。Local 31-page PDF matching supplied SHA-256; source record identifies the published Fields Institute Communications 91 (2026) chapter and arXiv:2007.10863v7 lineage.。物理页 12, 13, 14, 24, 25。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。Fields Institute Communications 91 (2026), pp.175--207; arXiv:2007.10863v7 lineage (publisher-byte identity not established here).
- 构件候选。Lemma 3.9's finite layer window is correctly derived from transitive orbit averaging, not from outer-approximation cuts. I independently checked its integer arithmetic in the symmetric bounded relaxation R=[0,1/2]^3: the LP objective is 3/2, l=floor(3/2)=1, and the prescribed window is -2<j≤1, i.e. {-1,0,1}; exhaustive exact enumeration finds the sole integer feasible point (0,0,0), layer 0, so the window captures the optimum. This is the same fixed-space/barycenter mechanism written on p.12.
- 结论位置。Physical p.12, Lemma 3.9 proof; pp.13--14, essential-set qualification and Algorithm 1; pp.24--25, direct-product algorithm and scope.
- 适用范围。This one instance does not prove the general lemma beyond transitive coordinate-permutation symmetry and a bounded relaxation. As p.14 expressly states, a finite essential-set system can admit non-core integer points; it is not a generic OA-error or symmetry certificate.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。A proposed use must exactly verify model invariance, transitivity, objective normalization and global integer layer solves; separately prove any linkage to A02's nonsymmetric outer-relaxation interface.
- [主来源 1](https://arxiv.org/abs/2007.10863) · [主来源 2](https://link.springer.com/book/10.1007/978-3-032-03844-9)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。Lemma 3.9 on physical p.12 is a real finite layer-window result, but only for a bounded transitive coordinate-permutation ILP normalized to objective <1,x>. Its proof uses orbit-barycenters and the fixed-space point k*1, while the essential-set algorithm immediately adds further core-point/orbit-polytope subproblems. No exact interface for this symmetry and global layer feasibility appears in A02.。定位。Physical pp.12–14: Lemma 3.9, essential/projected essential sets, and Algorithm 1 qualifications.。全卷 31 页。后续条件。Specify an invariant bounded relaxation, transitive action, objective normalization, exact LP optimum/layer window, and globally solved integer layer-feasibility certificates; separately prove any core-point or essential-set claims.。
- 复核记录。2026-11-26T19:04:42+08:00。candidate。dependency。
- 本次依据。The layer-window lemma is restricted to a bounded relaxation with transitive coordinate-permutation symmetry and its specified normalization. Essential sets can contain non-core integer points, so it does not yield a generic outer-approximation or core-point certificate.。定位。physical pp. 12--15 and 24--25, Lemma 3.9, essential sets, and Algorithm 1。全卷 31 页。后续条件。Supply exact model invariance, transitivity, objective normalization, LP layer window, and globally solved integer layer-feasibility certificates.。
- 复核记录。2026-11-26T19:33:26+08:00。adopted-local。component。
- 本次依据。Lemma 3.9 gives a finite layer-window reduction for the precisely normalized transitive-symmetry integer-program setting。定位。physical p. 12; Lemma 3.9。全卷 31 页。后续条件。Require global LP optimality, transitivity/invariance and exact layer-feasibility certificates。
- 已采用构件。物理页 12。Transitive-symmetry sum-objective ILP layer-window reduction only. [方法说明](../../../../math-l04-mathematical-programming-workflow/references/transitive-ilp-layer-window.md)。

## Piecewise SOS-Convex Moment Optimization and Applications via Exact Semi-Definite Programs

- 原件 ec78cd78268be31b62458211841946b2fa513fdf2974656b371fc86340e71fee。Local arXiv:2402.07064v6 PDF dated 2 Jul 2024; independently SHA-256 matched and counted 30 physical pages.。物理页 9, 10, 11, 12, 13, 14。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。EURO Journal on Computational Optimization 12 (2024), article 100094; reviewed e-print arXiv:2402.07064v6.
- 构件候选。Theorem 3.4 is conditional equality, and the measure recovery is strictly stronger. I independently constructed an exact valid micro-instance: Ω={v:[[1,v],[v,1]]⪰0}=[-1,1], g(v)=v², no moment inequalities, r=L=1. Strict feasibility holds at v=0 (F(0)=I), δ_0 attains value 0, and the SOS certificate is v²=[1,v]diag(0,1)[1,v]^T with Z=0; the associated moment choice y0=1,y1=y2=0 has PSD affine matrix I and PSD Gram diag(0,1). Thus primal, SOS and recovered Dirac measure all have exact value 0. This directly tracks pp.10--14 rather than treating a numerical SDP as a measure certificate.
- 结论位置。Physical p.9, measure-polar lemma and Assumption 3.2; pp.10--11, Theorem 3.4 proof; pp.12--14, Theorem 3.6 recovery and Corollary 3.7.
- 适用范围。The micro-instance does not discharge the paper's general representation theorem, conic-duality qualification, or Theorem 3.6's additional R--S strong-duality/nonnegative-zero-mass/inactive-index sign assumptions. Numerical SDP output alone remains insufficient for recovery.
- 相关技能。[math-b03-generalized-moments](../../../../math-b03-generalized-moments/SKILL.md)
- 其余依赖。A reusable B03 tool needs a checkable schema for Assumptions 3.2--3.3 and every Theorem 3.6 recovery condition, with independently certified SDP duality and SOS identities.
- [主来源 1](https://arxiv.org/abs/2402.07064) · [主来源 2](https://doi.org/10.1016/j.ejco.2024.100094)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。Theorem 3.4 is an actual conditional exact equality: Assumptions 3.2–3.3, existence of a minimizer, conic strong duality, and Theorem 2.4 give min(P)=max(D); pp.10–11 separately prove the two directions. The later measure recovery has stronger conditions. Current B03/C03 do not encode this piecewise SOS-convex spectrahedral schema or certify its imported duality theorem.。定位。Physical pp.9–14: Lemma 3.1, Assumptions 3.2–3.3, Theorem 3.4 and Theorem 3.6 recovery conditions.。全卷 30 页。后续条件。Provide a checkable schema for all moment/interior, compact projected-spectrahedron/Slater, SOS-convexity, degree, and recovery conditions, plus exact SOS/PSD identities rather than numerical SDP output.。
- 复核记录。2026-11-26T19:04:42+08:00。candidate。dependency。
- 本次依据。The source gives a conditionally exact piecewise SOS-convex moment equality and stronger recovery conditions, while C03 does not encode its projected-spectrahedron, measure-polar, or recovery schema.。定位。Physical p. 9 Lemma 3.1 and Assumptions 3.2--3.3; pp. 10--14 Theorems 3.4 and 3.6.。全卷 30 页。后续条件。Provide a checkable schema for Assumptions 3.2--3.3, compact projected spectrahedra and Slater data, exact SOS/PSD identities, and every Theorem 3.6 recovery condition.。
- 复核记录。2026-11-26T19:33:26+08:00。adopted-local。component。
- 本次依据。The published source proves an exact SDP equality for its precisely conditioned compact projected-spectrahedron, piecewise SOS-convex moment schema, separating it from the stronger later recovery claim。定位。Physical pp. 5--8, Definition 2.2 and Theorem 2.4; pp. 9--10, Assumptions 3.2--3.3 and Theorem 3.4。全卷 30 页。后续条件。For a target, certify the support Slater witness, moment interior condition, SOS-convexity, primal attainment, exact SOS/PSD identities and all additional recovery conditions if an optimal measure is claimed。
- 已采用构件。物理页 5, 6, 7, 8, 9, 10。Caller-certified compact strictly feasible projected spectrahedron and piecewise SOS-convex moment problem. It gives the source exact primal-dual SDP equality, not unconditional measure recovery. [方法说明](../../../../math-c03-moment-sos-certificates/references/piecewise-sos-convex-moment-sdp.md)。

## Polyhedral Outer-Approximations for MISOCP: Geometry and Cutting Planes

- 原件 8c3ba961d10739df057624c0b1f80e52d2adf0bbda9fee10d6d6bb5a72b76436。Local 36-page author PDF, title page marked arXiv:2608.10055v1 (10 Aug 2026); independently SHA-matched.。物理页 1, 4, 5, 6, 7, 9, 10。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2608.10055: local file is v1; prior record identifies v2 as latest checked arXiv version, with acceptance reported but no publisher bytes/DOI recovered.
- 构件候选。The SOC support fact can be independently derived: for infeasible (x,s) with s>=0, cone projection has y=((||x||+s)/(2||x||))x, so its normalized support is (x/||x||)^T u<=t. Exact check x=(3,4),s=4 gives projection ((27/10,18/5),9/2), support value 5, violation 1 and squared cone distance 1/2. Thus it is a valid SOC-only cut primitive; progressive integrality gives valid nondecreasing minimization lower bounds by feasible-set inclusion.
- 结论位置。pp. 4--5 (Proposition 2.1 and residual bound), pp. 6--7 (bounded-volume and angular claims), pp. 9--10 (partial-integrality and recovery).
- 适用范围。The paper's Appendix-dependent marginal/convergence statements were not imported. The primitive does not justify generic SDP/nonlinear OA, any finite-precision residual certificate, or the claimed final-edition identity. Fixed-integer conic recovery is only an upper bound when the recovered subproblem is feasible.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Compare local v1 with arXiv v2/final text and audit each appendix hypothesis before any MISOCP tool; an implementation needs exact/conservatively certified cone separation and explicit lower/upper-bound bookkeeping.
- [主来源 1](https://arxiv.org/abs/2608.10055) · [主来源 2](https://arxiv.org/pdf/2608.10055)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。The SOC support separation at pp.4–5 is a useful narrow primitive, but this local file is arXiv:2608.10055v1 whereas the prior record reports a later v2 without byte identity. The broader volume/angular/convergence claims rely on additional hypotheses and appendices, so only a version-pinned SOC cut could be considered.。定位。Physical pp.4–7: Proposition 2.1, residual/support geometry, and bounded-volume/angular arguments; pp.9–10 partial-integrality discussion.。全卷 36 页。后续条件。Compare the adopted proposition with the chosen current version, then provide an exact/conservative cone-membership, projection, normalized-support-cut, and lower/upper-bound bookkeeping interface; do not infer generic SDP or nonlinear OA convergence.。
- 复核记录。2026-11-26T19:04:42+08:00。adopted-local。component。
- 本次依据。The SOC support inequality has an exact finite certificate when a rational unit direction is supplied. It is a valid conservative separation primitive and does not require the paper's wider MISOCP convergence claims.。定位。Physical pp. 4--5, Proposition 2.1 and residual/support discussion.。全卷 36 页。后续条件。Use exact or conservatively certified unit directions and keep master lower and recovered upper bounds separate before applying it in a MISOCP workflow.。
- 已采用构件。物理页 4, 5。For a supplied rational unit direction, certifies one valid SOC support inequality and a positive cut violation. It does not select the direction, solve a MISOCP, or establish algorithmic convergence. [方法说明](../../../../math-a02-outer-relaxation-budget/references/soc-support-cut.md)。

## Positive Semidefinite and Sum of Squares Biquadratic Polynomials

- 原件 2c37bb1f76571f695475ea033c8f65691b4f6a14b098267e664597df3952a91e。Local 24-page PDF, title page marked arXiv:2506.17260v4 (17 Jul 2025); independently SHA-matched.。物理页 1, 4, 5, 13。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2506.17260v4; no formal publication identified in the source queue.
- 构件候选。The core transfer is algebraically sound on the dense chart and extends by continuity: for bi-homogeneous f, f((X,z),(Y,z))=z^4 g(X/z,Y/z) when z!=0. Exact sanity identity f=(x1^2+x2^2)(y1^2+y2^2), h=(X^2+z^2)(Y^2+z^2), gives h(2,3,5)=f((2,5),(3,5))=986. Hence a 2x2 PSD-to-SOS consequence follows only after invoking Hilbert's ternary-quartic theorem; it is an existence statement, not a Gram-construction algorithm.
- 结论位置。pp. 4--5 (Theorems 2.1--2.2 de-/re-homogenization), p. 13 (only three explicit 2x2 construction cases).
- 适用范围。The imported Hilbert theorem and the paper's SOS homogenization details are indispensable. Page 13 expressly omits the full-cross plus two-neighbor-half-cross construction, so no general explicit 2x2 certificate constructor or numerical Gram test is licensed.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Formalize the SOS-preserving homogenization and the exact Hilbert theorem dependency, then either construct rational/verified Gram witnesses for the omitted configuration or retain this as a non-executable existential reference.
- [主来源 1](https://arxiv.org/abs/2506.17260) · [主来源 2](https://arxiv.org/pdf/2506.17260v4)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。The de-/re-homogenization step on pp.4–5 is valid only with the bi-homogeneous and continuity hypotheses. The small-dimensional PSD-to-SOS consequence additionally invokes Hilbert's ternary-quartic theorem, and p.13 lists only selected explicit cases. Current C03 has structured Gram routes, but no general constructor licensed by this source.。定位。Physical pp.4–5: Theorems 2.1–2.2; p.13 explicit construction cases and their stated omissions.。全卷 24 页。后续条件。Pin the exact dimension/cross-pattern theorem, formalize SOS-preserving homogenization, and provide a rational/interval PSD Gram witness for every claimed construction; retain the external Hilbert theorem as a dependency.。
- 复核记录。2026-11-26T19:04:42+08:00。adopted-local。component。
- 本次依据。For a supplied rational split of the sole full-cross coefficient, two exact 2 by 2 PSD Gram matrices provide a direct SOS certificate. This independently checks a usable subcase from the source's 2 by 2 discussion without claiming its general PSD-to-SOS reduction.。定位。physical pp. 13--14, Lemma 4.4 and Theorem 4.5。全卷 24 页。后续条件。Caller supplies the rational coefficient split and uses a different route for general 2 by 2 PSD, automatic split construction, or a square-factor list.。
- 已采用构件。物理页 13, 14。Exact SOS certificate for a supplied rational split of the full-cross coefficient into two 2 by 2 PSD Gram matrices. [方法说明](../../../../math-c03-moment-sos-certificates/references/split-full-cross-biquadratic.md)。

## Refined Outer-Approximation Algorithms for Monotonic Optimisation

- 原件 2004c934d1c055c87b75e8c77f28178d8a7a2f59bdc960d33b3defa63d77e3f7。Local 21-page PDF marked arXiv:2608.13694v1; independently SHA-matched.。物理页 1, 3, 8, 9, 10, 11, 12, 13。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2608.13694v1 (2026).
- 构件候选。The finite-tree argument is substantive under the stated exact oracle model. Every nonfinal maximal vertex is refined and each parent-child edge loses at least delta in coordinate sum; consequently depth D=floor(delta^-1||b-a||_1)+1 bounds a branching-n tree. Exact check n=2,a=(0,0),b=(1,1),delta=1/3 gives D=7 and the stated node bound 2^7-1=127. The result certifies delta-relaxed, not original-problem, optimality.
- 结论位置。p. 3 (normal/co-normal model and monotone projection), pp. 8--10 (erosion, balanced anchors, Algorithm 2), pp. 10--12 (Lemmas 1--2 and Theorem 2).
- 适用范围。Termination requires exact projection onto the eroded normal set, a closed normal G, co-normal H, increasing f, bounded box, and the algorithm's pruning semantics. Bisection/float outputs without a directed feasibility invariant need not retain strict delta descent; the experimental results prove neither bit complexity nor numerical certification.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Specify a conservative projection-oracle certificate whose lower/upper segment brackets preserve z in G_delta and the >delta refinement test, and expose the relaxed-feasibility/objective distinction before considering a separate route.
- [主来源 1](https://arxiv.org/abs/2608.13694) · [主来源 2](https://arxiv.org/pdf/2608.13694)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。The finite-tree argument in pp.10–12 is conditional on the source's exact projection onto an eroded normal set, bounded box, closed normal G, co-normal H, increasing objective, and pruning semantics. It certifies delta-relaxed feasibility rather than the original problem. Current A02 records outer-relaxation direction but has no exact oracle contract for this method.。定位。Physical pp.8–13: erosion/balanced-anchor construction, Algorithm 2, Lemmas 1–2, and Theorem 2.。全卷 21 页。后续条件。Define a directed/certified projection-oracle contract that preserves membership in G_delta and the strict delta descent test, and expose separately the relaxed feasibility and objective guarantee.。
- 复核记录。2026-11-26T19:04:42+08:00。candidate。dependency。
- 本次依据。The delta-relaxed outer-approximation tree bound is valid under the paper's exact projection oracle, closed normal set, co-normal set, increasing objective, bounded box, and pruning semantics. Current outer-relaxation tooling has no directed oracle contract for these assumptions.。定位。physical pp. 3 and 8--13, Proposition 1, Algorithms 2--3, Lemmas 1--2, and Theorem 2。全卷 21 页。后续条件。Specify certified projection brackets preserving eroded-set membership and the strict delta-descent test, while keeping relaxed feasibility separate from original feasibility.。
- 复核记录。2026-11-26T19:33:26+08:00。adopted-local。component。
- 本次依据。Algorithm 2 supplies an exact-oracle delta-relaxed monotonic outer-approximation depth and iteration budget。定位。physical pp. 8--12; Algorithm 2, Lemma 2, Theorem 2。全卷 21 页。后续条件。Require closed normal/co-normal geometry, exact G_delta projection and pruning; do not treat numerical oracle output as certified。
- 已采用构件。物理页 8, 9, 10, 11, 12。Exact-oracle delta-relaxed monotonic outer-approximation budget. [方法说明](../../../../math-a02-outer-relaxation-budget/references/delta-relaxed-polyblock-outer-approximation.md)。

## Separation, Constraint Qualifications, and Cycling in Outer Approximation

- 原件 36c55973344a6d115da3bf8ecac8a7d4256794e82350c5b87d0a8146c9aa64e0。Local 16-page PDF marked arXiv:2606.26897v1; independently SHA-matched.。物理页 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2606.26897v1 (2026).
- 构件候选。The source's active error mechanism is real: with g=x^2+y^2-1, candidate (1,1), and linearization a=(-1/10,1), exact g(a)=1/100 but the cut value at (1,1) is -21/100, so it fails to separate although a is distance 1/10 from the exact fixed-y optimizer (0,1). This independently exhibits why a generic small NLP residual cannot trigger an OA finite-convergence claim. Theorem 7's finite proof is confined to finite Y, compact polyhedral X, convex differentiable constraints and its exact OA/ECP cut cases.
- 结论位置。pp. 3--6 (model, running example, CQ/separation), pp. 7--9 (approximate-linearization obstruction and Theorem 3), pp. 10--12 (Lemmas 5--6 and Theorem 7), p. 16 (ECP algorithm).
- 适用范围。The practical repeat-assignment fallback on p. 12 inherits the constructed theorem only if optimal fixed-integer NLPs are solved accurately enough to give the theorem's cut semantics. There is no source residual-to-separation tolerance, nor a certificate for nonconvex models or arbitrary local NLP solvers.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。A usable route needs a certified primal/dual subproblem accuracy and separation test, plus a proof that repeat detection selects the exact OA/ECP semantics; otherwise record the counterexample as a rejection guard only.
- [主来源 1](https://arxiv.org/abs/2606.26897) · [主来源 2](https://arxiv.org/pdf/2606.26897)
- 复核记录。2026-11-26T18:11:16+08:00。existing。statement。
- 本次依据。This source is already an exact warning route in the present A02 skill: A02 distinguishes valid cuts from residual tolerances, requires global master solves, and its provenance/source index directly records this SHA. Physical pp.10–12 confirm the indispensable scope of the finite cycling argument: finite Y, exact OA/ECP cut semantics, and a constraint qualification at optimal fixed-integer subproblems. The source provides no residual-to-separation tolerance.。定位。Physical pp.7–12: approximate-linearization obstruction, Lemmas 5–6, Theorem 7, and the ECP fallback discussion.。全卷 16 页。后续条件。For a solver-facing extension, still supply certified subproblem primal/dual accuracy and a separation test; repeat detection alone does not convert arbitrary approximate gradients into valid OA cuts.。

## Solving Stochastic Constraints by Oracle-based Gradient Descent and Interval Arithmetic

- 原件 05f5202493ea0d79313dce16155209e328695bd85d49502ac1d74eb4b65c9cf5。Local 30-page PDF matching the queued SHA; title/source record identifies arXiv:2604.17275v1.。物理页 1, 2, 5, 6, 7, 26。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2604.17275v1 (submitted 19 Apr 2026); no journal version identified in the source queue.
- 构件候选。For any fixed parameter, disjoint certified inner boxes give B<=V_phi(x), hence B<=V_phi^*; boundary boxes only furnish a local upper enclosure. Exact uniform example y in [0,1], predicate y<=x, x=1/2, inner [0,1/4] and boundary (1/4,1/2] gives B=1/4<=V=1/2<=B+mass(O)=1/2, while V*=1 at x=1. This proves the crucial local/global direction distinction.
- 结论位置。pp. 5--7 (Assumptions 1--2, Definitions and pointwise inner/boundary-box enclosure), p. 26 (separate stochastic-oracle concentration step).
- 适用范围。The finite enclosure assumes sound interval/constraint propagation, disjoint proven box classification and computable probability masses. It supplies no audited outward-rounded implementation, input-error enclosure, or generic mass oracle. The oracle-SGD claim depends additionally on separate stochastic-oracle/concentration hypotheses.
- 相关技能。[math-l03-rational-and-interval-certificates](../../../../math-l03-rational-and-interval-certificates/SKILL.md)
- 其余依赖。Bind a concrete directed-rounding interval engine and validated mass oracle for each supported distribution, retain distinct local/global bound types, and separately audit the oracle assumptions before integration with L03.
- [主来源 1](https://arxiv.org/abs/2604.17275) · [主来源 2](https://arxiv.org/pdf/2604.17275)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。Physical pp.5–7 prove a narrow useful enclosure: disjoint inner boxes give B(x)<=V_phi(x)<=B(x)+sum mass(O_l), and only B(x) is automatically a global lower bound V_phi^*. This requires sound interval classification, computable probability mass for boxes, and truncation. Current L03 explicitly has no audited outward-rounded interval API or validated mass oracle, so it is not an existing executable route.。定位。Physical pp.5–7: Assumptions 1–2, Definition 1, and enclosure (7)–(10).。全卷 30 页。后续条件。Bind a concrete directed-rounding interval engine, parameter/input enclosure and distribution-specific validated box-mass oracle; keep local upper enclosure distinct from global optimum bounds and separately audit the stochastic oracle assumptions.。
- 复核记录。2026-11-26T19:04:42+08:00。adopted-local。component。
- 本次依据。The fixed-parameter inner/boundary-box mass accounting is reusable when containment, disjointness, masses, and tail mass are supplied. The source upper display omits a tail term despite domain truncation, so the adopted interface requires an explicit outside-mass bound.。定位。physical pp. 5--7, Assumptions 1--2, Definition 1, and equations (7)--(10)。全卷 30 页。后续条件。Caller supplies directed interval containment, disjoint classification, valid box masses, a satisfaction-tail bound, and a feasible parameter.。
- 已采用构件。物理页 5, 6, 7。Exact bookkeeping for caller-certified disjoint inner and boundary box masses with an explicit outside-mass term. [方法说明](../../../../math-l03-rational-and-interval-certificates/references/stochastic-box-mass-enclosure.md)。

## Sparsity Constrained Nonlinear Optimization: Optimality Conditions and Algorithms

- 原件 55e4faa517792baabfd0cbcd21505a2beed57aa8bfb43863f3d9660e5fdc03df。arXiv:1203.4580v1 [math.OC], 20 March 2012; published in SIAM Journal on Optimization 23(3) (2013), 1480--1509, DOI 10.1137/120869778。物理页 1, 2, 9, 15, 20, 27。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Local SHA-matched 34-page PDF carries the arXiv:1203.4580v1 header and a 27 November 2024 title-page date; it is not asserted byte-identical to the 30-page published pagination。
- 邻近材料。The bibliographic issue in the previous hold is resolved: the archived file is traceable to arXiv v1 and the independently published SIAM article. Mathematically, it gives necessary stationarity conditions and algorithms for a finite-dimensional l0-constrained differentiable optimization problem; for example, the checked IHT descent/convergence statements require a globally Lipschitz gradient and identify stationary accumulation points, not global minimizers。
- 结论位置。Local pp. 1--2 define minimizing a differentiable f under an l0 constraint; p. 9 proves optimal points L-stationary only under Lipschitz-gradient assumptions; pp. 15, 20, and 27 state and prove limited convergence properties of IHT/greedy sparse-simplex methods. The SIAM publisher record confirms the 2013 published article and its stationarity/algorithm scope。
- 适用范围。The source does not match L02's adversarial-input task: it imposes coordinate sparsity on a vector, while L02 concerns realization and auditing of finite input families. Its algorithmic convergence is to stationarity under explicit smoothness/boundedness conditions and does not certify a global adversarial optimum or a lifted function. No active L02 claim was found to rely on the earlier unresolved version attribution。
- 相关技能。[math-l02-adversarial-input-search](../../../../math-l02-adversarial-input-search/SKILL.md)
- 其余依赖。Use only if a future task is explicitly reduced to a finite l0-constrained differentiable program; then supply the objective, sparsity budget, Lipschitz constant, bounded-sublevel/accumulation conditions, and a separate global certificate if a global conclusion is needed。
- [主来源 1](https://arxiv.org/abs/1203.4580) · [主来源 2](https://epubs.siam.org/doi/10.1137/120869778)

## Stability of Weak Supermartingale Optimal Transport Problems

- 原件 59ffa2f370f57a15a0eaeb5c34f40ec55b31a8d80f6ed5a461c6318c831e249f。arXiv:2603.27940v2 (14 Sep 2026), 30 physical pages; SHA-matched local PDF。物理页 1, 3, 4, 5, 6, 7, 8, 9, 10, 19, 20, 21, 22, 23, 24。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2603.27940v2 (14 Sep 2026); no published version identified in the primary arXiv record checked。
- 邻近材料。Theorem 2.1 is genuinely supported in the local v2: on the real line, Wr-convergent r-integrable marginals satisfying µk≤cdνk admit AWr approximation of each supermartingale coupling. The proof reduces to r=1, handles the strict supermartingale component, uses left free mass for barycentre correction, completes residuals via Strassen, then composes a final supermartingale coupling. The D01 provenance already treats this as adjacent rather than an active generic Kantorovich-duality dependency。
- 结论位置。Local pp. 5–8 contain Theorems 2.1, 2.3, and 2.9 with their assumptions; pp. 9–22 contain the construction and completion/gluing proof of Theorem 2.1; pp. 23–24 begin the monotonicity proof and explicitly invoke external abstract duality machinery。
- 适用范围。The result is one-dimensional weak supermartingale OT under decreasing-convex order and exact r-moment/cost hypotheses. It neither proves ordinary positive-coupling Kantorovich duality nor multidimensional SOT stability. The monotonicity argument also relies on cited prior results and an adapted abstract duality step, so it is not a self-contained general duality certificate。
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Use only after the target has real-line marginals, µ≤cdν, the stated Wr and cost conditions, and a supermartingale coupling constraint. For generic static OT, vector measures, or jump-semimartingale SOT, retain the model-specific D01 sources instead。
- [主来源 1](https://arxiv.org/abs/2603.27940)

## Sum of Squares Decompositions and Rank Bounds for Biquadratic Forms

- 原件 a260d9a8da70b44cb94ef3671bf04c937eabd6e544c875cf1ba1b450b7b04aa7。Local PDF arXiv:2601.04965v3, dated 21 January 2026, 32 physical pages, SHA-256 a260d9a8da70b44cb94ef3671bf04c937eabd6e544c875cf1ba1b450b7b04aa7.。物理页 1, 10, 11, 12, 13, 14, 26, 27。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。The checked publisher record identifies Mathematics 2026, 14(4), 635, DOI 10.3390/math14040635; the local proof is the distinct arXiv:2601.04965v3 e-print, so their byte identity was not assumed.
- 已有技能。A strong finite constructor is verified for an m×n monic x-symmetric PSD biquadratic form: form Q=I+B−A and R=I+B+(m−1)A, build the specified Kronecker Gram matrix M, then factor M PSD and reshape its factors into bilinear forms. The proof block-diagonalizes M as diag(R,Q,…,Q), giving SOS-rank at most rank(R)+(m−1)rank(Q). Separately, Theorem 6.2 moves an already-SOS Gram matrix to the PSD boundary to obtain the universal mn−1 rank bound.
- 结论位置。Local pp.10–11 prove Theorem 2.5; pp.12–14 give Theorem 2.7 and factor-extraction procedure; pp.26–27 prove and summarize the general SOS-rank bound.
- 适用范围。PSD-to-SOS is not general: the first construction needs exactly the monic x-symmetric normal form and the specified Q,R. The universal mn−1 statement assumes the form is SOS already. Published and local e-print byte versions were not compared.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 已采用构件。限定接口已写入 [math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/references/qi-cui-xu-monic-xsymmetric-gram.md)。
- 其余依赖。Implement only a syntactically checked monic x-symmetric parser with exact coefficient reconstruction, PSD validation of Q/R or M, and exact/interval verification that extracted bilinear squares reproduce the input.
- [主来源 1](https://arxiv.org/abs/2601.04965) · [主来源 2](https://www.mdpi.com/2227-7390/14/4/635)

## Sum of Squares Decompositions for Structured Biquadratic Forms

- 原件 0866821532b1970e753a4228b30402966ff9a495bb954c2fbecf01d728c1c1ab。arXiv:2512.02734v2, 13 physical pages; local bytes and page count rechecked.。物理页 3, 4, 5。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2512.02734v2, 11 December 2025. No formal publication was identified in the checked source record.
- 已有技能。Theorem 2.1 has a self-contained finite certificate. If the coefficient matrix is symmetric, satisfies a_ijkl=a_kjil, has nonnegative diagonal and is row diagonally dominant, then z^T M z has the explicit exact decomposition sum_p d_p z_p^2 plus sum_{p<q}|M_pq|(z_p+sign(M_pq)z_q)^2 for z_(i,j)=x_i y_j. The private overlay checker validates the tensor symmetries, rational diagonal slacks and reconstruction of this bilinear-square decomposition.
- 结论位置。Pages 3--4 state and prove Theorem 2.1 by forming M_(i,j),(k,l)=a_ijkl and converting the tensor condition to symmetric diagonal dominance. Page 5 explicitly labels the M-biquadratic and B0-biquadratic extensions as conjectures.
- 适用范围。It certifies exactly the supplied symmetric diagonally-dominant coefficient tensor. It does not decide arbitrary PSD or SOS biquadratic forms and excludes the source's M-biquadratic and B0-biquadratic conjectures.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 已采用构件。验证双二次型结构与逐行对角占优，生成并逐项重构有限 SOS。 [math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/references/biquadratic-dd-sos.md)
- 其余依赖。Keep the finite input contract separate from the algorithmic claim. Any future C03 implementation should enforce its exact moment and rank conditions.
- [主来源 1](https://arxiv.org/abs/2512.02734) · [主来源 2](https://arxiv.org/pdf/2512.02734v2)

## Sum of Squares Submodularity

- 原件 22ee0c0eb9f8ca40979a7eee88dbb7d655bda13c4952d974f0946eb29b66439f。Local 49-page PDF marked arXiv:2510.24550v2 (26 Jun 2026); independently SHA-matched.。物理页 6, 7, 10, 30, 31, 32。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2510.24550v2; no journal version identified in the source queue.
- 构件候选。The Boolean-ideal implication can be checked directly: for the two-node cut MLE F=x1+x2-2x1x2, -partial_12 F=2=1^2+1^2 is an exact degree-zero SOS modulo I_2, and f({1})+f({2})-f(empty)-f({1,2})=2. In general the pp. 31--32 telescoping identity and (yj-xj)^2 congruence convert exact t-SOS mixed-derivative witnesses into the stated submodularity certificate.
- 结论位置。pp. 6--7 (Boolean ideal and t-SOS definition), p. 10 (SDP-size table), pp. 30--32 (finite-order/imported hierarchy use and proof turning mixed derivatives into a submodularity certificate).
- 适用范围。The result concerns a set function's multilinear extension over the Boolean ideal, not generic semialgebraic SOS. The finite-order completeness discussion imports Lasserre/exactness results, and a floating SDP feasible point is not itself an exact PSD Gram certificate.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Implement a separate Boolean-set-function parser, square-free ideal reduction and exact/rational-or-interval PSD Gram verification for every pair (i,j); retain the degree and ideal in the certificate schema.
- [主来源 1](https://arxiv.org/abs/2510.24550) · [主来源 2](https://arxiv.org/pdf/2510.24550v2)
- 复核记录。2026-11-26T18:11:16+08:00。adopted-local。component。
- 本次依据。A narrow proof component is closed: Definition 6 makes every negative mixed MLE derivative a t-SOS modulo the Boolean ideal. Physical pp.31–32 derive the telescoping identity and use (y_j-x_j)^2 congruent to y_j-x_j to turn those witnesses into nonnegative discrete cross-differences, hence submodularity. This is a source-gated Boolean-ideal implication, not a numerical SDP conclusion. An exact two-variable check gave -partial_12(x1+x2-2x1x2)=2=1^2+1^2 and discrete slack 2.。定位。Physical pp.6–7: Boolean ideal and Definition 6; pp.31–32: Lemma 5 and proof of Theorem 1.。全卷 49 页。后续条件。A caller must provide the set function's multilinear extension and exact SOS-mod-I2 witnesses for every ordered pair; floating PSD output requires rational or directed-interval Gram certification. Do not use the imported finite-order Lasserre completeness claim without its separate dependencies.。
- 已采用构件。物理页 6, 7, 31, 32。Given exact t-SOS-mod-Boolean-ideal witnesses for every negative mixed derivative of a set function's multilinear extension, derive discrete submodularity. This is not an SDP solver, finite-order completeness assertion, or floating Gram certificate. [方法说明](../../../../math-c03-moment-sos-certificates/references/historical-03-boolean-sos-submodularity.md)。

## The Effective Countable Generalized Moment Problem

- 原件 858d0c6799128b324a1a303b2521f19c47b0540b6fd8b4358d3e0826f87f56d2。arXiv:2501.09385v4, 1 September 2025; local 27-page PDF hash and physical page count independently recomputed.。物理页 1, 2, 8, 9, 10, 12, 13, 14。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。Preprint only in the checked primary records: arXiv:2501.09385v4 and HAL hal-04885482v4; no journal edition identified.
- 构件候选。The rate derivation is conditionally substantive: q=f-h.(v*-epsilon w) has q_min>=epsilon min_i(h_i.w)>0 (p.9), so the displayed degree threshold yields p*-p*_ell<=epsilon(t.w), and Corollary 2.5 needs the source's countable-GMP strong duality. The uniqueness gate is genuinely indispensable: an exact local check has zero objective and mass-one measures delta_-1, delta_1 on [-1,1], whose q(x)=x moments differ by 2; alternating optimizers has no weak-star limit. Hence p.14 cannot be generalized to arbitrary canonical optimizers without uniqueness.
- 结论位置。Source pp. 8--10 derive the rate by perturbing a dual optimizer v* to v*-epsilon w, applying an effective Positivstellensatz, then invoking Proposition 1.8 strong duality; pp. 12--14 convert a uniform objective-gap bound to truncated-set control and require a unique GMP minimizer for full weak-star optimizer convergence.
- 适用范围。This is not an executable finite-GMP upgrade. B03 neither represents a countable index cone K nor checks S-fullness/weighted spaces/dual attainment, and its finite PSD residual cannot supply the Positivstellensatz constants. The source proof itself remains conditional on Assumptions 1.3, 1.9, 2.1 and Proposition 1.8.
- 相关技能。[math-b03-generalized-moments](../../../../math-b03-generalized-moments/SKILL.md)
- 其余依赖。For a specific target, encode the countable constraint map and K, prove Assumptions 1.3/1.9/2.1 and the applicable Positivstellensatz constants, then separately prove uniqueness if full optimizer convergence (rather than value/set convergence) is requested.
- [主来源 1](https://arxiv.org/abs/2501.09385) · [主来源 2](https://hal.science/hal-04885482v4)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。arXiv:2501.09385v4 has a substantive conditional perturb-dual/Positivstellensatz rate argument, but the existing finite generalized-moment skill has no countable cone, S-fullness, weighted-space, dual-attainment, or Positivstellensatz interface. The unique-minimizer gate is indispensable for the asserted full optimizer convergence.。定位。rate argument pp. 8-10; optimizer convergence pp. 12-14。全卷 27 页。后续条件。For a target, encode the countable map and cone, prove Assumptions 1.3/1.9/2.1 and strong duality, provide Positivstellensatz constants, and prove uniqueness when optimizer convergence is requested.。
- 复核记录。2026-11-26T19:04:42+08:00。candidate。dependency。
- 本次依据。The effective countable-GMP rate needs countable-cone strong duality and Positivstellensatz constants absent from the finite B03 interface. The source also needs uniqueness for full optimizer convergence.。定位。Physical pp. 8--10 effective rate and pp. 12--14 optimizer convergence.。全卷 27 页。后续条件。Encode the countable constraint map and cone, prove Assumptions 1.3, 1.9 and 2.1 with strong duality, give applicable Positivstellensatz constants, and prove uniqueness when convergence of optimizers is requested.。
- 复核记录。2026-11-26T19:33:26+08:00。adopted-local。component。
- 本次依据。The checked preprint proves a narrow perturb-dual and effective-Positivstellensatz value-gap rate once its countable-GMP assumptions, dual optimizer and strong-duality input are certified。定位。Physical pp. 8--10, Theorem 2.4 and Corollary 2.5; pp. 12--14, separate optimizer-convergence condition。全卷 27 页。后续条件。For a target, encode the countable cone and constraint map, prove Assumptions 1.3, 1.9 and 2.1, provide Positivstellensatz constants, and prove uniqueness separately if optimizer convergence is requested。
- 已采用构件。物理页 8, 9, 10。A caller-certified countable GMP with Assumptions 1.3, 1.9 and 2.1, dual attainment, strong duality, and applicable effective Positivstellensatz constants. It certifies a value-gap rate, not arbitrary optimizer convergence. [方法说明](../../../../math-b03-generalized-moments/references/effective-countable-gmp-rate.md)。

## The Fundamental Theorem of Weak Optimal Transport

- 原件 cf4106429915f4a29b6b5d433c53028694884c472785b9c70cb8c0c9cccb7553。arXiv:2501.16316v1, submitted 27 January 2025; local 38-page PDF hash and physical page count independently recomputed.。物理页 1, 2, 6, 15, 32。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2501.16316v1; the checked arXiv record lists v1 only.
- 待核。The prior ordinary-coupling transfer is false without a lifting audit. Exact finite check: take X={*}, Y={0,1}, nu=(delta_0+delta_1)/2 and P=(delta_(delta_0)+delta_(delta_1))/2. P has barycentre nu but is not J(pi) for the unique ordinary coupling pi, since J(pi) has mass 1 at rho=nu while P has mass 0 there. Thus p.15 complementary slackness P(dx,d rho)-a.s. is a genuinely lifted statement and cannot certify a D01 ordinary plan merely by identifying rho with a disintegration. This does not duplicate the separate finite causal-OT implementation.
- 结论位置。Pp. 1--2 state ordinary convex WOT Theorem 1.2 and conditions (B),(C); p.6 introduces a relaxed compactification for nonconvex costs; p.15 states Theorem 2.15 and explicitly attributes its relaxed duality to [11, Theorem 3.1], with the claimed Borel generalization only said to follow another proof line by line; p.32 applies it after checking a special cost's hypotheses.
- 适用范围。The source statement does not independently provide the cited relaxed-duality proof, compactification, or the projection/reconstruction needed for a target ordinary coupling. Conditions (B),(C), the affine lower bound and p-weak lsc must hold for the actual C, not just a finite cost table.
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Audit [11, Theorem 3.1] and the source's definitions of the relaxed-plan space; for each proposed finite interface, construct its lift and prove the barycentre/marginal reconstruction plus all (B),(C), lower-bound and topology hypotheses.
- [主来源 1](https://arxiv.org/abs/2501.16316) · [主来源 2](https://arxiv.org/pdf/2501.16316)
- 复核记录。2026-11-26T18:11:16+08:00。hold。dependency。
- 本次依据。arXiv:2501.16316v1 uses relaxed lifted plans, and its complementary slackness is P(dx,d rho)-a.s. The known one-point/two-point counterexample shows a barycentric lifted plan is not automatically an ordinary coupling disintegration, so no D01 transfer is valid.。定位。Theorem 1.2 pp. 1-2; relaxed compactification p. 6; Theorem 2.15 p. 15; application p. 32。全卷 38 页。后续条件。Audit the cited relaxed-duality theorem and construct a lift with barycentre/marginal reconstruction while checking (B), (C), affine lower bound, and p-weak lsc for the target cost.。
- 复核记录。2026-11-26T19:04:42+08:00。adopted-local。component。
- 本次依据。The ordinary convex weak-transport theorem is a useful conditional D01 route. Under the source's measurable, p-weak lower-semicontinuous and convex-in-rho cost hypotheses, it gives primal attainment and strong duality. Conditions (B) and (C) add dual attainment and complementary slackness for an ordinary coupling pi. The paper separately identifies its nonconvex statement on lifted plans P, so the adopted route does not conflate them.。定位。Physical pp. 1--2 state Theorem 1.2 and (B),(C); pp. 7--13 give Assumption 2.1, Theorems 2.2, 2.5, 2.7 and their proof route; pp. 14--15 define lifted plans and Theorem 2.15; pp. 16--17 give a barycentric convex specialization.。全卷 38 页。后续条件。For any use, supply the actual Polish spaces, p-moments, cost, p-weak lower semicontinuity, convexity, and conditions (B),(C). A relaxed nonconvex use additionally requires the lifted-plan theorem and a proved reconstruction to an ordinary coupling.。
- 已采用构件。物理页 1, 2, 7, 8, 9, 10, 11, 12, 13。For an ordinary coupling under the source's measurable, p-weak lower-semicontinuous, convex-in-rho cost and actual (B),(C) hypotheses, check the dual orientation and complementary slackness. The relaxed lifted-plan theorem is excluded. [方法说明](../../../../math-d01-kantorovich-duality/references/wave9-convex-weak-transport-duality.md)。

## The Interacting 2D Bose Gas and Nonlinear Gibbs Measures

- 原件 139a7e2dcb60ec7c8dce46d2d19e57f388b0b4b2b2aafe32933fd326e7dbceee。arXiv:1805.03506v1, 4 physical pages; local bytes and page count rechecked.。物理页 1, 2, 3, 4。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:1805.03506v1, 4 May 2018. The checked record lists v1 only.
- 引用核对。This is a checked four-page announcement and model definition. D02's finite-domain Gibbs identity does not rely on the announcement's quantum-field limit.
- 结论位置。Pages 1--2 define the Fock-space free energy, Gibbs state and announced high-temperature limit. Page 3 explicitly postpones the detailed discussion and proof. Page 4 is bibliography.
- 适用范围。The source expressly defers its theorem proof. It cannot substantiate a renormalized nonlinear-Gibbs limit or a quantum Bose-gas variational theorem.
- 相关技能。[math-d02-gibbs-entropy-duality](../../../../math-d02-gibbs-entropy-duality/SKILL.md)
- 其余依赖。If a later task needs the quantum limit, audit the full 2021 Lewin--Nam--Rougerie proof and map its exact hypotheses and conclusion before adding an active route.
- [主来源 1](https://arxiv.org/abs/1805.03506) · [主来源 2](https://arxiv.org/pdf/1805.03506)

## The Unified Separation Condition: A General Constraint Qualification for Smooth and Nonsmooth Optimization

- 原件 3ddb21fea039dbe46d48d0da0c34b7d61bcf9753e03c11ce5d25934a6e1aceeb。arXiv:2609.16981v1, 15 September 2026; local 16-page PDF hash and physical page count independently recomputed.。物理页 5, 6, 7, 8, 9, 10。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2609.16981v1; no publisher edition identified in the checked primary record.
- 构件候选。A corrected finite-dimensional core is reusable as a diagnostic, not as a B04 duality rule. If K=partial phi(x) is compact convex and v0 is its closest point to 0, then v.v0>=||v0||^2 for v in K. Taking d=-v0/||v0|| proves max_{v in K}<v,d><=-||v0||, while the reverse inequality follows from v0; hence inf_{||d||=1} max_K<v,d>=-dist(0,K). This repairs the source p.7 use of a minimax interchange over the nonconvex unit sphere. The exact local check phi=x^2, f=-|x| shows why USC cannot be dropped: F_lambda(1/(2lambda))=-1/(4lambda)<F_lambda(0) for each positive lambda.
- 结论位置。P.5 quotes the Demyanov exact-penalty prerequisites; pp.6--7 state/prove the finite smooth-max lower-derivative identity; p.8 derives exact penalization from the external theorems; pp.9--10 give the MFCQ/LICQ-to-USC arguments.
- 适用范围。The p.8 exact-penalty theorem is still imported from Demyanov, and p.7's written minimax justification is not valid as stated because the unit sphere is nonconvex (although the identity has the projection proof above). USC is local finite-dimensional nonsmooth regularity; it neither proves conic Slater/strong duality nor B04 minimax conclusions.
- 相关技能。[math-b04-qualification-facial-minimax](../../../../math-b04-qualification-facial-minimax/SKILL.md)
- 其余依赖。Before a separate USC tool, state a finite smooth-constraint input contract, implement exact active-gradient convex-hull separation with certified continuity neighborhoods, and independently verify an applicable local exact-penalty theorem including attainment/lower-bound hypotheses.
- [主来源 1](https://arxiv.org/abs/2609.16981) · [主来源 2](https://arxiv.org/pdf/2609.16981)
- 复核记录。2026-11-26T18:11:16+08:00。candidate。dependency。
- 本次依据。The corrected closest-point separation identity is a finite-dimensional diagnostic, but the source p.7 minimax justification uses a nonconvex unit sphere and the exact-penalty step imports Demyanov. It cannot yet be promoted to B04 strong-duality/minimax machinery.。定位。Demyanov prerequisites p. 5; finite derivative identity pp. 6-7; penalty derivation p. 8; MFCQ/LICQ pp. 9-10。全卷 16 页。后续条件。Implement a finite active-gradient convex-hull separation contract with continuity certification, then independently verify a local exact-penalty theorem including attainment and lower-bound hypotheses.。
- 复核记录。2026-11-26T19:04:42+08:00。candidate。dependency。
- 本次依据。The finite closest-point identity behind the lower derivative can be repaired by projection onto a compact convex hull, but the source's displayed minimax step uses a nonconvex unit sphere. The exact-penalty conclusion also imports Demyanov conditions and does not give a B04 duality rule.。定位。physical pp. 5--10, Demyanov prerequisites, Lemma 3.1, Theorem 3.4, and MFCQ or LICQ arguments。全卷 16 页。后续条件。Implement a finite active-gradient convex-hull separation checker with continuity neighborhoods and independently verify a local exact-penalty theorem including attainment and lower-bound hypotheses.。
- 复核记录。2026-11-26T19:33:26+08:00。adopted-local。component。
- 本次依据。A direct closest-point proof yields an exact finite active-gradient separation diagnostic and avoids the paper's nonconvex-sphere minimax justification。定位。physical pp. 6--8; Lemma 3.1 and Theorem 3.4。全卷 16 页。后续条件。Exact-penalty conclusions still require a separately verified Demyanov theorem and its local hypotheses。
- 已采用构件。物理页 6, 7, 8。Finite convex-hull closest-point separation only; not exact-penalty or minimax duality. [方法说明](../../../../math-b04-qualification-facial-minimax/references/usc-active-gradient-separation.md)。

## Truncated Hausdorff Moment Problem and Analytic Solution of the Time-Optimal Problem for One Class of Nonlinear Control Systems

- 原件 c8906ecb0fe430907ebd1d785c973d842770e48c9150013ae296118459f05352。arXiv:2007.02398v1 (5 Jul 2020); local PDF is 27 pages and carries that v1 header。物理页 1, 7, 9, 10, 11, 12, 13, 14, 21, 22, 23, 24。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。ESAIM: Control, Optimisation and Calculus of Variations 28 (2022), article 15, DOI 10.1051/cocv/2022007。
- 引用核对。The published identity is recovered. For the exact system x1'=u and xj'=x1^(j-1), n>=4, with the paper's generic-point and controllability-case hypotheses, the source gives finite Hankel singularity/positivity tests and reconstruction roots/weights; it does not establish a generic generalized-moment optimization procedure。
- 结论位置。Local pp. 7-14 reduce the specified chained-power dynamics to a truncated Hausdorff problem, state the four finite-support alternatives in Lemma 1, and give the case algorithm; pp. 21-24 give the recalled moment-problem theorem and the Lemma 1 proof。
- 适用范围。The active B03 skill does not rely on this specialized time-optimal-control algorithm. Do not transfer its case split, genericity argument, or finite-support reconstruction to arbitrary moment constraints, supports, or controls。
- 相关技能。[math-b03-generalized-moments](../../../../math-b03-generalized-moments/SKILL.md)
- 其余依赖。If a control-specific tool is proposed, independently check that its dynamics, endpoint convention, genericity regime, and all Lemma 1 case tests match pp. 9-14 before use。
- [主来源 1](https://arxiv.org/abs/2007.02398) · [主来源 2](https://doi.org/10.1051/cocv/2022007)

## Two-Thread Coverage MCTS for SAT and XSAT

- 原件 7658d5ec4efa90569b4e4577e8562f2114785929275e9dc7609648335a3310d7。arXiv:2607.15834v1, 17 July 2026。物理页 1, 2, 3, 4, 8, 10, 11。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2607.15834v2, 20 July 2026. The local 11-page PDF states v2 and its SHA-256 and page count were recomputed.
- 邻近材料。For complementary Boolean starts sigma and not-sigma, d_H(sigma,tau)+d_H(not-sigma,tau)=n. Thus every assignment is within floor(n/2) of one start. This elementary coverage identity is correct, but is already directly usable in a SAT encoding and does not supply a distinct solver or certificate component.
- 结论位置。Local pp. 1-4 give the complementary-start discussion and finite Hamming-distance identity. Pp. 8 and 10-11 specify nonexhaustive rollout and expansion-budget termination.
- 适用范围。The MCTS procedure returns Unknown when both expansion budgets end. Its Hamming coverage is not a completeness, satisfiability, unsatisfiability, proof-trace, or runtime guarantee. Unit propagation also accounts for some reported zero-playout cases.
- 相关技能。[math-l05-csp-sat-smt-encoding](../../../../math-l05-csp-sat-smt-encoding/SKILL.md)
- 其余依赖。Any solver claim needs independently runnable code plus exact assignment checking for SAT and proof-producing SAT/SMT machinery for UNSAT. No active L05 statement relies on this paper.
- [主来源 1](https://arxiv.org/abs/2607.15834)
