# 优化、矩与严格计算

按原件哈希区分。每条核查保留本机物理页与对应来源。

## A Moment-SOS Hierarchy for Robust Polynomial Matrix Inequality Optimization with SOS-Convexity

- 原件 c5f8382a8abdf2fd9f3860040cb8e2fd24c0997ecda894bf90475a72c4718a98。arXiv:2304.12628v5 (8 Oct 2024), local PDF。物理页 1, 2, 9, 10, 17, 18, 19, 20, 21, 22。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2304.12628v5 (8 Oct 2024); no journal version identified。
- 构件候选。For RPMIO with SOS-convex objective/constraints, PSD-SOS-convex dependence on y, compact X, and Slater, the paper proves monotone decreasing primal/dual SDP upper bounds converging to f*. Its finite certificate additionally requires the stated matrix flat-extension condition and, for exact equality/extracted optimizer, the theorem’s Assumptions 1 and 3 plus matching primal/dual values。
- 结论位置。RPMIO and Assumption 1 pp.1–2; moment/localizing cones pp.9–10; Slater/conic reformulation pp.17–18; hierarchy and upper-bound direction pp.19–20; asymptotic convergence and flat-extension theorem pp.21–22。
- 适用范围。This is a matrix-valued robust-PMI hierarchy, not scalar Lasserre by entrywise reduction. Flatness alone is not the whole certificate: the required moment/localizing matrices, matrix-valued representing measure, Slater/SOS-convexity and equality conditions must be checked。
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。A dedicated C03 component would need exact RPMIO/degree encoders, Assumptions 1–3 checks, both SDP sides, matrix flatness, and rational/interval validation of returned PSD matrices and recovered atoms。
- [主来源 1](https://arxiv.org/abs/2304.12628) · [主来源 2](https://wangjie212.github.io/jiewang/research/pmio.pdf)

## Adaptive Metrics for Norm-Minimization-Based Outer Approximation in Convex Vector Optimization

- 原件 67390e5e27908c306cf188094be34cb7d57e6302960cd0be72e7d2baebed22b4。Local arXiv:2605.14320v3 PDF (14 Jul 2026), 27 physical pages; exact local bytes verified。物理页 1, 14, 15, 16, 17, 18, 19。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。not identified: the checked arXiv primary record confirms 2605.14320, while a publisher DOI was encountered in search metadata but its publisher page was inaccessible and therefore was not used to establish a canonical text。
- 构件候选。For the paper’s bounded convex-vector-optimization slice, exact norm-minimization scalarizations, valid dual cuts, farthest-vertex selection, and uniformly conditioned positive-definite metrics, Lemma 11 proves a selected external vertex is removed, Theorem 12 gives Euclidean Hausdorff convergence, and Theorem 14 gives the stated asymptotic rate. The proof explicitly uses mI⪯M_k⪯MI and exact scalarization solves。
- 结论位置。Local p. 1 (v3 abstract and scope), p. 14 Lemma 11 with proof, p. 15 Theorem 12 with proof, pp. 16–18 Theorem 14 and proof, p. 19 corrected experimental qualification。
- 适用范围。Version control is material: the local v3 abstract/p.19 rejects a uniform dispersion premise and reports no evaluation advantage, whereas the fetched arXiv HTML exposed earlier-looking claims of dispersion and 31–33% savings. No such performance or dispersion assertion may enter A02. The result is not a generic OA guarantee and requires compact slicing, correct dual cuts, exact solves, and uniform conditioning。
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Byte-compare the local v3 against the current arXiv PDF and obtain/check the publisher version before any integration. A02 presently contains only generic preservation/bound-direction safeguards, not this adaptive-metric theorem; do not add the rate without a version-resolved proof audit。
- [主来源 1](https://arxiv.org/abs/2605.14320)

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

- 原件 d9b756f8eea5f0231655aed07b96f43ce6375d5238eecdbd4afb37a1abdf6a9b。Local 25-page PDF is arXiv:2507.08525v2 (2025-09-29); SHA-256 and physical page count rechecked。物理页 1, 2, 3, 10, 11, 12, 15, 20, 21, 22。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2507.08525v2 (latest version on the checked primary record; no published version identified)。
- 构件候选。For a fixed matrix A=(A_R|A_I), Theorem 9 states a finite universal augmentation test set made from padded circuits and finitely many constructed directions. Its proof relies on the cited universal MIP-Graver test set, converts a nonoptimal point to a basic-integer case via padded circuits, and uses Lemma 6 plus the finite coefficient sets I_g/Algorithm 4 to place the improving direction in T(A). This is a potentially useful finite construction beyond L04's currently installed integer-kernel Graver-box routine。
- 结论位置。The MIP model and prior infinite MIP-Graver issue are on pp. 2–3. The finite double-test-set statement and its limitation are on pp. 10–12. Lemma 6 and the finite-fraction construction are on pp. 15 and 20–21. Theorem 9 and proof are on p. 22。
- 适用范围。The result is an arXiv preprint and matrix-specific. The proof explicitly depends on the cited Hemmecke universal-test-set result and on the source's nondegeneracy/basis-path construction; it offers neither a small black-box direction list nor a polynomial-time guarantee. Current L04 makes no unsupported claim that this construction is implemented。
- 相关技能。[math-l04-mathematical-programming-workflow](../../../../math-l04-mathematical-programming-workflow/SKILL.md)
- 其余依赖。Before integration, independently verify the cited Hemmecke Lemma 12/Proposition 1 dependency, Lemma 6's nondegeneracy assumptions, and Algorithm 4's finite enumeration; then implement a matrix-specific construction with an exact feasibility/improvement certificate。
- [主来源 1](https://arxiv.org/abs/2507.08525)

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

- 原件 e6358fcb0f1598334408a9e27b2a8e28f2122f391b338b74fbbe573b018f1498。local arXiv:1611.02610v2 (2017-12-12), 33 physical pages; hash verified。物理页 1, 8, 9, 11, 13, 26。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Stochastic Processes and their Applications 130(5) (2020), 2918–2953, DOI 10.1016/j.spa.2019.08.009。
- 构件候选。The local v2 proves, for Wiener measure gamma and nu absolutely continuous with respect to gamma, equivalence between finite causal variation/Cameron–Martin-type transport cost and the displayed enlarged-filtration Brownian decomposition. It separately proves causal-transport duality for lower-semicontinuous bounded-below cost when the source has the weak-continuity property。
- 结论位置。Local pp.8–9, Theorem 3.1 and proof direction; p.11, Theorem 3.4; p.13, Theorem 3.8; p.26, Theorem 5.6 causal duality and proof。
- 适用范围。D01 is not defective: it does not presently rely on this causal/path-space theorem. These results are not static positive-coupling duality: they retain filtrations, causality, path-space Wiener reference, absolute-continuity and cost/Orlicz hypotheses。
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。If adding a causal-OT branch, reconcile local v2 theorem numbering and hypotheses with the 2020 journal text and implement separate model guards rather than extending D01’s ordinary static duality。
- [主来源 1](https://arxiv.org/abs/1611.02610) · [主来源 2](https://www.sciencedirect.com/science/article/pii/S0304414918303995)

## Conditional Optimal Transport on Function Spaces

- 原件 870ae0faefdc7627c50e64b1af4217c145cc64db3c97202ba3a2aba21b8d712c。local 33-page manuscript with no cover version label; hash verified。物理页 1, 4, 5, 12, 14, 15, 16。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。SIAM/ASA Journal on Uncertainty Quantification 13(1) (2025), 304–338, DOI 10.1137/23M1618922; arXiv:2311.05672v3 (2024-02-06)。
- 构件候选。The paper fixes the conditioning coordinate in a conditional Kantorovich problem. Under Polish spaces, Assumption 3.1, lower-semicontinuous cost bounded below, Proposition 3.6 derives strong duality via the infinite cost enforcing y=z. For V=U, p-power cost, finite p-moments, regular reference eta_V and finite feasibility, Theorem 1.7/Proposition 3.8 gives a unique conditional Monge map。
- 结论位置。Local pp.4–5, Problems 1.3–1.4 and Theorems 1.6–1.7; p.12, constrained infinite-cost formulation and Proposition 3.3; pp.14–16, Proposition 3.6 duality, its proof, and Proposition 3.8 qualification。
- 适用范围。D01 has no active erroneous dependency. This conditional result cannot be substituted for ordinary OT: the equality coordinate constraint, disintegration, finite feasibility and reference-measure regularity are essential; the local PDF has not been byte-matched to the 2025 journal version。
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Diff the published and local versions, then prove that a proposed target satisfies the conditional-coordinate, Polish/disintegration, cost and reference-regularity assumptions before an optional D01 extension。
- [主来源 1](https://arxiv.org/abs/2311.05672) · [主来源 2](https://epubs.siam.org/doi/10.1137/23M1618922)

## Converging Outer Approximations to Global Attractors Using Semidefinite Programming

- 原件 6b26fbd168b3aff091ff344da20a7881f3c036333e11c43d4cd57ffbd05d78a0。arXiv:2005.03346v3 (4 Oct 2023), local PDF。物理页 8, 9, 12, 14, 15, 16。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Schlosser and Korda, Automatica 134 (2021) 109900, DOI 10.1016/j.automatica.2021.109900。
- 构件候选。For its global-attractor LP, every feasible dual triple gives A⊆{w≥1}; under polynomial dynamics and compact basic semialgebraic X with the stated ball constraint, its SOS dual optima decrease to λ(A), and Theorem 6 proves each Yk={wk≥1} contains A with λ(Yk\A)→0. The local proof shows containment precedes the volume argument。
- 结论位置。Continuous-time dual containment/no-gap Theorem 2 and construction pp.8–9; polynomial/basic-semi-algebraic Archimedean setup p.14; SOS convergence Theorem 5 p.15; outer containment and volume convergence Theorem 6 p.16。
- 适用范围。The result is not a generic outer-relaxation objective-error bound: it is a global-attractor construction, uses continuous/discrete dynamics with their separate assumptions, an exact feasible SOS program, and volume discrepancy rather than Hausdorff convergence or finite-k optimality。
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。A specialized A02 add-on would need input checks for polynomial dynamics, compact Archimedean X, time direction/injectivity where applicable, exact SOS feasibility, and explicit reporting of volume-only convergence。
- [主来源 1](https://arxiv.org/abs/2005.03346) · [主来源 2](https://www.sciencedirect.com/science/article/pii/S0005109821004234)

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

- 原件 eeaf5dbad4c207b58e1e8eb5c4a6f012a7a407bd0bdb21300919f872cec69d0a。local PDF: arXiv:2602.23725v3, dated 21 Jul 2026。物理页 1, 3, 11, 30, 32。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2602.23725v3 (20 Jul 2026); no journal version identified。
- 构件候选。The local v3 bytes identify a genuine arXiv preprint. Theorem 3.2 proves non-spectrahedral-shadow status for COP(K) and CP(K) when K is symmetric of rank at least 5, by an explicit embedded COP_r argument; Theorem 4.6 proves the stated Horn transformation is an exposed COP(K) ray; Theorem 5.2 proves it is outside I_0(E+)。
- 结论位置。Local PDF pp. 1, 3, Theorem 3.2 p. 11 and proof, Theorem 4.6 p. 30 and proof, Theorem 5.2 p. 32 and proof; arXiv abstract/version record。
- 适用范围。This does not support the active C02 moment hierarchy claim, which instead depends on Lasserre 2010 for R_+^n. The conclusions require a symmetric cone/Euclidean Jordan algebra and rank at least 5; they do not settle ranks 3--4 or give finite-level exactness。
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。Before implementation, independently audit the inherited non-spectrahedrality input used by the embedded COP_r argument and separately audit Theorems 5.3--5.4 before asserting non-exactness of the union over PSD cones。
- [主来源 1](https://arxiv.org/abs/2602.23725)

## Copositive Matrices with Ordered Off-Diagonal Entries

- 原件 05990838c18871a47d433307d452dcc18e9c528011a686a602b1f3e30c08218e。arXiv:2605.15970v1 (15 May 2026), byte-matched local PDF。物理页 1, 2, 5, 6, 11, 12, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2605.15970v1; no publisher version identified in the checked primary record。
- 构件候选。Theorem 3.5 is verified in the byte-matched v1: for A in the paper’s M_n class, whose off-diagonal entries obey the stated row-and-column partial order, copositivity is equivalent to SPN membership. Its proof uses the recursive Theorem 3.1, deletion/Schur-complement closure and the n<=4 base. Corollary 5.5 then yields exact DNN/SPN relaxation for standard quadratic programs with Q in M_n; Proposition 5.7 obtains the separable-simplex-QP corollary after sorting alpha. Current C02 does not assert this special exactness result。
- 结论位置。PDF pp.1–2 state the ordered-off-diagonal SPN objective; pp.5–6 state and prove Theorem 3.5; pp.11–12 connect St-QP, CP/COP and DNN/SPN values; p.13 proves Corollary 5.5 and Proposition 5.7。
- 适用范围。This is not a general copositivity test or generic finite-stage CP/COP hierarchy certificate. It requires an already copositive matrix in M_n (or a separately certified special QP setting), and its proof relies on the stated recursive class conditions and low-dimensional CP/SPN base。
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。Implement only as a guarded special-case route: formalize the M_n order test, input normalization/permutation, and whether the target is copositivity-to-SPN or St-QP exactness; separately audit the inherited Theorem 3.1/Lemmas 2.1, 2.7, 2.8 if a proof-complete skill claim is desired。
- [主来源 1](https://arxiv.org/abs/2605.15970)

## Disjunctive Sum of Squares

- 原件 6e6581b0fab0b52347c7ec6e7bc00a2ee8cad7f51cc79a383625bde81ae81c4c。local PDF: arXiv:2605.28674v1, dated 27 May 2026。物理页 1, 8, 14, 25, 26, 29。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2605.28674v1 (27 May 2026); no journal version identified。
- 构件候选。The local v1 is the arXiv preprint. Theorem 1 states, for fixed n and even d, an explicit family of one-polynomial-per-branch disjunctions covering every positive-definite form. Theorem 10 verifies that the derived cones meet the four abstract conditions needed for nondecreasing lower bounds converging to p* after the cited compact-POP reduction; Theorem 11 supplies an analogous strict-copositivity construction。
- 结论位置。Local PDF p. 1 (scope), Theorem 1 p. 8, its net/disjunction construction p. 14, Theorem 10 and proof pp. 25--26, Theorem 11 setup/proof p. 29; arXiv abstract/version record。
- 适用范围。The hierarchy only captures strict positivity at finite stage; the compact-POP result additionally requires a radius bound and imports the reduction in cited [2, Theorems 2.1 and 2.4]. It neither certifies boundary nonnegativity at a finite level nor validates arbitrary standard SOS hierarchies。
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Before any C03 implementation, fully audit the local Positivstellensatz construction (Theorems 2, 4, 8, 9 and the continuation of Theorem 1's proof) and independently verify the imported compact-POP reduction [2, Theorems 2.1, 2.4]。
- [主来源 1](https://arxiv.org/abs/2605.28674)

## Enhancing Presolve in Mixed Integer Programming by Combining Probing and Dual Fixing

- 原件 3bf4856c846a0a634e0a356a50ffb92aa94e0e71f80b3ae99f34b1071a2a7b09。Local 15-page PDF is arXiv:2607.10767v1 (2026-07-12); SHA-256 and physical page count rechecked. The local title page still has journal placeholder received/accepted fields。物理页 1, 5, 8, 9, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2607.10767v1, whose checked primary record says accepted for Mathematical Programming Computation; no final publisher version/DOI was identified。
- 构件候选。Theorem 1 exactly characterizes lower/upper-bound reachability by auxiliary MIP optima o⁻_{rj},o⁺_{rj}; combined with the stated objective-sign conditions it justifies generalized dual fixing. Algorithm 1 alternates branch-specific propagation, redundant-row detection, and dual fixing, while the proof on pp. 8–9 supplies the logical reachability implication rather than treating a solver status as a theorem。
- 结论位置。Algorithm 1 appears on local p. 5. Theorem 1 and its lower-bound-reachability proof are on pp. 8–9. The conclusion and benchmark scope are on p. 13。
- 适用范围。It remains a preprint/accepted-manuscript source. Safe application requires the paper's bounded MIP model, valid propagated implications, exact sign convention, and certified auxiliary bounds. Benchmark speedups do not prove any reduction on a new model, and no active A01/A04/L04 claim was found to rely on this unintegrated technique。
- 相关技能。[math-l04-mathematical-programming-workflow](../../../../math-l04-mathematical-programming-workflow/SKILL.md)
- 其余依赖。For integration, independently verify the dual-fixing reduction rules R1–R4 and prove each propagated bound/auxiliary-MIP upper bound on the user model; recover the version of record when published。
- [主来源 1](https://arxiv.org/abs/2607.10767)

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

- 原件 9613fdac4553e3a2e1296c42ea97484cfac5641069de66fc69d13a01fa899eb3。arXiv:1109.1320v2 [math.OC], 2 April 2012; published in Journal of Global Optimization 56(4) (2013), 1773--1790, DOI 10.1007/s10898-012-9936-x。物理页 1, 6, 7, 16, 19。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Local SHA-matched 21-page PDF is arXiv:1109.1320v2 dated 2 April 2012。
- 构件候选。Theorem 3 is a checked failure-mode template: on D=[-1,1], for a stationary covariance kernel satisfying the paper's rapidly decaying spectral-density hypotheses, exact expected-improvement started at x1=0 with f=-G has xK tending to zero and hence is not dense. The proof pages show why the posterior mean equals f for this special f and then compare exact EI through conditional-variance bounds; the Gaussian-kernel corollary only asserts existence of a smooth inconsistent objective after a separate modification argument。
- 结论位置。Local pp. 6--7 state the spectral hypotheses, conditional-variance estimate, and Theorem 3; p. 16 derives the exact EI expression for f=-G; p. 19 is within the induction controlling the selected EI points. The arXiv record supplies the same title, author, date, and one-dimensional claim。
- 适用范围。No active L02 statement currently relies on this source, and it cannot justify a general claim that Bayesian optimization or arbitrary expected-improvement implementations are inconsistent. It requires a one-dimensional compact domain, noiseless exact EI maximization, a fixed stationary analytic kernel satisfying Theorem 2, the special initialization, and the stated objective construction; the final smooth counterexample is not the analytic f=-G itself。
- 相关技能。[math-l02-adversarial-input-search](../../../../math-l02-adversarial-input-search/SKILL.md)
- 其余依赖。A future L02 counterexample module would need an explicit kernel/objective pair, an exact or certified EI maximization rule, and a proof that its implementation preserves the paper's tie-breaking and spectral assumptions。
- [主来源 1](https://arxiv.org/abs/1109.1320) · [主来源 2](https://doi.org/10.1007/s10898-012-9936-x)

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

- 原件 5f9131bfa83088d87854d91842ca15c71752e137db9929e4d02f3c9b6b6e8341。local PDF: arXiv:2502.04006v2, dated 17 Apr 2026。物理页 1, 3, 10, 15, 20。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2502.04006v2 (16 Apr 2026); no journal version identified。
- 构件候选。The actual v2 preprint classifies designated subfaces of COP(L_n): for interior (1;v), Theorem 3.1 obtains PSD faces S_+(X) and exposedness; for boundary v, Theorem 3.9 gives the conditional S_+(X) form and Proposition 3.10 an exposedness condition. Page 20 explicitly identifies boundary rank-one rays as non-exposed。
- 结论位置。Local PDF pp. 1, 3, Theorem 3.1 p. 10 with proof, Theorem 3.9 and Proposition 3.10 p. 15, exposed/non-exposed-ray classification p. 20; arXiv abstract/version record。
- 适用范围。All claimed facial descriptions are specialized to a second-order cone L_n and the case split on v; they are not a general symmetric-cone facial classification or a replacement for C02's basic CP/COP duality route。
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。A reusable facial-classification tool would require an independent audit of the representation COP(L_n)=S_+^n+R_+J_n and Lemmas 2.3--2.8 invoked in the displayed proofs。
- [主来源 1](https://arxiv.org/abs/2502.04006)

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

- 原件 e112ec7f105cf4cf7fcf6aa1008cbd7668460072730e6fd7e982bee8a397c618。Local 30-page PDF; byte-identical to the checked official arXiv PDF。物理页 1, 2, 3, 7, 8, 9, 10, 11, 12, 15, 16, 20, 21, 23, 28, 29, 30。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.26395v1 (26 Aug 2026)。
- 构件候选。A narrowly reusable compactness component is independently confirmed: Proposition 2 proves that an exact convergent sequence of finite extremal unit-diameter configurations has, after merging coincident points and taking the diameter-graph core, another extremal configuration. Proposition 5 proves only lower semicontinuity under compatible dual-pair convergence, and continuity needs stable convergence plus axis-vanishing of the cost. Theorem 10 is a separate proved additive inequality; Theorem 15 is an exact spherical-product supremal reformulation。
- 结论位置。Local PDF pp. 7-9 prove Proposition 2 on the extremal core of an exact convergent sequence; pp. 10-12 specify the extra compatibility/stability hypotheses for functional limits; pp. 15-16 prove the tetrahedral additive minimization; pp. 20-21 prove the spherical-product supremal reformulation; pp. 23 and 28-30 delimit the numerical evidence and open claims。
- 适用范围。This is not generic concentration compactness, not a proof that arbitrary numerical limits are feasible, and not a global solution of the 3D Blaschke-Lebesgue problem. The source expressly leaves arbitrary-collision compatibility/stability and its K4 structural conjecture unresolved; its 10,644-graph computations are noncertifying for a fixed graph。
- 相关技能。[math-a03-compactness-concentration](../../../../math-a03-compactness-concentration/SKILL.md)
- 其余依赖。Any implementation must explicitly require exact configuration convergence or a validated numerical certificate, then reconstruct unit distances, core, and exposed dual pairs. A separate proof is still needed for compatible/stable convergence in the requested class before passing intrinsic functionals to limits。
- [主来源 1](https://arxiv.org/abs/2608.26395) · [主来源 2](https://arxiv.org/pdf/2608.26395)

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

- 原件 4e4f65485ed8c30eae404e5693b9cd6761e5e9723ccbfff42d91c086116ea495。arXiv:2512.14072v3, revised 25 Jun 2026 (local 22-page source PDF)。物理页 4, 5, 9, 10, 14, 15, 16。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2512.14072v3 (current version listed by arXiv)。
- 构件候选。For the paper's augmented product of Polish spaces with isolated skip points and optimised intermediate marginals, Theorem 2.2 derives existence from M finite plus its coercivity/tightness condition. Theorem 3.1 then derives a unique Borel Monge path map only under lower semicontinuity, local control, (discrete-type) sequential twistedness, and strong coercivity; pp. 15–16 give the disintegration argument after singleton optimal continuations are obtained。
- 结论位置。PDF pp. 4–5 define the HJMOT path cost and give the finite-value construction; p. 9 proves Kantorovich attainment from its coercivity definition; pp. 10 and 14–16 define the local-control/sequential-twist hypotheses and prove Theorem 3.1。
- 适用范围。This is a source-specific HJMOT model, not a general Kantorovich-duality extension. Its Monge proof uses Lemma 3.1/Kellerer dual functions and the special definitions of sequential twist and strong coercivity; D01 neither defines nor verifies those interfaces。
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Independently audit Lemma 3.1 and the c-cyclical-monotonicity/duality input used to form the support set, then develop a separate HJMOT specification with explicit variable-intermediate-marginal and coercivity checks before installation。
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

- 原件 69909f6afc65e3b2954766721918786782fc880653a9198fb07caea45dc1d34c。Local 25-page manuscript PDF; byte-identical to the checked official arXiv PDF。物理页 1, 2, 4, 5, 6, 7, 10, 11, 12, 13, 14, 23, 25。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2602.04122v1 (4 Feb 2026)。
- 构件候选。Theorem 3.2 (p. 12) proves equivalence of the full master with the stated MINLP when the feasible and infeasible subproblem cut conditions hold. Theorem 3.3 (pp. 13-14) then proves finite termination by showing no integer assignment repeats, provided Y intersect Z^p is finite. The local copy is byte-identical to arXiv v1。
- 结论位置。Local PDF pp. 1-2 define the bounded-polyhedral convex MINLP; pp. 6-7 derive feasible-subproblem KKT/subgradient cuts under A1; pp. 10-11 derive infeasible-assignment cuts; pp. 12-14 prove equivalent master construction and finite termination; pp. 23-25 are numerical/concluding material。
- 适用范围。The proof relies on bounded closed polyhedral X, finite integer choices, the Slater condition A1 for every feasible fixed-integer subproblem, solvable nonlinear feasibility subproblems, and KKT-compatible selected subgradients/multipliers. Arbitrary subgradients or an unverified subproblem solver do not establish the master equivalence。
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。A usable implementation must state how KKT-compatible subgradients, multipliers, rho parameters, and infeasibility certificates are computed or independently certified; otherwise retain this only as a candidate reference。
- [主来源 1](https://arxiv.org/abs/2602.04122) · [主来源 2](https://arxiv.org/pdf/2602.04122)

## On Computing the Copositive Minimum and its Representatives

- 原件 673f26accc0cd74ed08fceae15ee0ad05f6381cbc8eb573dab336f6878d1a732。local PDF: arXiv:2509.23696v1, dated 27 Sep 2025。物理页 1, 2, 3, 7, 8, 10, 15。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2509.23696v1 (28 Sep 2025); no journal version identified。
- 构件候选。For integer strictly copositive Q, Theorem 2.3 gives an explicit Subset-Sum reduction proving its decision MinCOP variant NP-complete. The paper then gives an LDLT-based finite search framework: positive leading LDLT coefficients bound earlier integral coordinates once later coordinates are fixed。
- 结论位置。Local PDF pp. 1--3 (definition, Lemma 1.1, Theorem 2.3 and reduction), pp. 7--8 (LDLT expansion and coordinate-bounding setup), p. 10 (permutation heuristic), p. 15 (limitations/open directions); arXiv abstract/version record。
- 适用范围。The method is not a general efficient COP optimizer: its applicability relies on usable upper bounds and favorable LDLT/permutation structure, while p. 15 records unresolved extensions to all copositive matrices. It does not certify membership in COP from a numerical LDLT decomposition。
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。Before implementation, complete the remaining pages of Theorem 2.3's reduction and audit the special-case assumptions in Sections 5--6; exact rational arithmetic is required for any resulting enumeration certificate。
- [主来源 1](https://arxiv.org/abs/2509.23696)

## On the Monge-Kantorovich Problem with Additional Linear Constraints

- 原件 335316951595dde0686a29e2d5a482d11054c4d8e448dff06b9c40ed663df864。arXiv:1404.4962v1, submitted 19 Apr 2014 (local 20-page source PDF)。物理页 1, 5, 6, 8, 9。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:1404.4962v1 (the arXiv record lists only v1)。
- 构件候选。Theorem 2.1 proves a constrained Kantorovich equality for Polish Xi, fixed marginals, c and W in CL(mu): the primal over plans annihilating W equals the supremum over f plus omega in W with f+omega<=c. The proof explicitly invokes the ordinary CL(mu) duality and the stated compact-convex minimax theorem. Theorem 3.6 then supplies only necessary (c,W)-monotonicity for a minimizer, with the added condition mu_k restricted to W intersection CL(mu_k) equals zero。
- 结论位置。PDF p. 1 states the constrained-marginal problem; p. 5 is Theorem 2.1; p. 6 gives its reduction to ordinary duality and minimax; pp. 8–9 prove the necessary (c,W)-monotonicity statement。
- 适用范围。D01 presently describes ordinary positive-coupling OT and separately warns that extra constraints need an independent matching theorem; it does not implement this CL(mu)-subspace interface. This source neither licenses arbitrary constraints nor a sufficiency claim for (c,W)-monotonicity。
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Before adding a constrained-OT branch, encode CL(mu), nonempty Pi_W(mu), the exact minimax/topology assumptions, and the separate hypothesis in Theorem 3.6; test martingale/invariant specializations rather than treating W symbolically。
- [主来源 1](https://arxiv.org/abs/1404.4962)

## Outer Approximations of Core Points for Integer Programming

- 原件 3971b19fd8672edb6d104fa7c15ac24261e14e965991a717c0c36a6217d96570。arXiv:2007.10863v1 (21 Jul 2020), originally Shahverdi and Bremner。物理页 1, 3, 12, 13, 14, 24, 25。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Springer chapter in Data Science and Optimization, Fields Institute Communications 91 (2026), pp.175–207, Shahverdizadeh–Banihashemi–Bremner; local 31-page PDF has the three-author text (publisher-byte equality not checked)。
- 构件候选。Lemma 3.9 is independently confirmed: for a transitive permutation-symmetric integer maximization problem normalized to objective <1,x>, it reduces feasibility/optimal-layer search to the n-layer interval l−n<j≤l. Its proof uses orbit averaging into Fix_R(G), the integral fixed point on a multiple-of-n layer, and convexity. The published chapter identity corrects the previous manuscript-only status, but its finite cyclic/direct-product core-point algorithms are a narrow potential addition rather than support for A02’s general outer-relaxation claims。
- 结论位置。local pp.12–13, Lemma 3.9 and proof; pp.14, 24–25, Algorithms 1/3 and their stated symmetry scope; arXiv landing page and Springer table of contents checked。
- 适用范围。The argument requires a bounded LP relaxation, transitive coordinate-permutation symmetry, objective normalization, and exact integer feasibility/global optimization of subproblems. The finite essential-set inequalities are outer approximations and p.14 explicitly permits non-core integer points satisfying them; they are not a generic symmetry-breaking or relaxation-error certificate。
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Before integration, implement an exact symmetry/invariance check, verify the objective normalization and every subproblem’s global solve, and separately prove any claimed relation to A02’s set-map/objective-error framework。
- [主来源 1](https://arxiv.org/abs/2007.10863) · [主来源 2](https://link.springer.com/book/10.1007/978-3-032-03844-9)

## Piecewise SOS-Convex Moment Optimization and Applications via Exact Semi-Definite Programs

- 原件 ec78cd78268be31b62458211841946b2fa513fdf2974656b371fc86340e71fee。arXiv:2402.07064v6 (2 Jul 2024), byte-matched local PDF。物理页 1, 2, 9, 10, 12, 13, 14。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。EURO Journal on Computational Optimization 12 (2024), article 100094, doi:10.1016/j.ejco.2024.100094; checked e-print arXiv:2402.07064v6。
- 构件候选。Theorem 3.4 independently supports equality of the moment optimum and the SOS/SDP dual only when a minimizer exists and Assumptions 3.2–3.3 hold: the moment interior condition, compact strictly feasible projected spectrahedron, and SOS-convex data. The measure-recovery claim is narrower: Theorem 3.6 additionally assumes strong duality of (R)–(S), nonnegative zeroth moments, and sign conditions for inactive k; Corollary 3.7 uses the stronger all-positive-mass case. Current B03 does not rely on this paper。
- 结论位置。PDF pp.1–2 define the compact projected-spectrahedron moment model; pp.9–11 state/prove Theorem 3.4; pp.12–14 state/prove Theorem 3.6 and Corollary 3.7。
- 适用范围。It does not establish generic moment-SOS exactness, nor does Theorem 3.4 by itself recover a measure from a numerical SDP solution. Its proof invokes the paper’s Theorem 2.4 and strong conic duality (Corollary B.2), while recovery separately needs (R)–(S) strong duality。
- 相关技能。[math-b03-generalized-moments](../../../../math-b03-generalized-moments/SKILL.md)
- 其余依赖。To implement, translate Assumptions 3.2–3.3 and every Theorem 3.6 recovery condition into an input checklist; independently audit the cited/appendix conic-duality and piecewise-SOS representation dependencies。
- [主来源 1](https://arxiv.org/abs/2402.07064) · [主来源 2](https://www.sciencedirect.com/science/article/pii/S219244062400011X)

## Polyhedral Outer-Approximations for MISOCP: Geometry and Cutting Planes

- 原件 8c3ba961d10739df057624c0b1f80e52d2adf0bbda9fee10d6d6bb5a72b76436。Local 36-page author PDF by Yongzheng Dai; no arXiv identifier is printed on its inspected title page, but its title/author match arXiv:2608.10055 v1 metadata; exact local bytes verified。物理页 1, 4, 5, 7, 9, 10。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.10055, latest checked record v2; the checked arXiv record says accepted by EURO Journal on Computational Optimization, but no publisher-version DOI was recovered in this pass。
- 构件候选。The local manuscript studies MISOCP only. It gives SOC supporting-cut geometry and a progressive-integrality scheme in which increasingly integral polyhedral relaxations yield minimization lower bounds; fixed-integer conic recovery can yield a feasible upper bound. These are compatible with, but not currently asserted as, a generic A02 method。
- 结论位置。Local pp. 1 and 4–7 (SOC deepest-cut geometry and direction-management statements), p. 9 (partial-integrality relaxation), p. 10 (primal recovery); checked arXiv primary record identifies the manuscript and acceptance status。
- 适用范围。The inspected source does not certify arbitrary conic/SDP/nonlinear OA. Any cut novelty or residual-feasibility statement remains tied to the SOC direction constraints and the paper’s algorithms. The local file’s precise arXiv revision and the final publisher text remain unbyte-matched。
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Before adding a MISOCP module, compare the local PDF against arXiv v2/final publication; then audit the Appendix-A proofs and every condition for cut validity, residual feasibility, global master solves, and lower/upper-bound direction. Current A02 execution steps do not rely on this candidate-specific claim。
- [主来源 1](https://arxiv.org/abs/2608.10055)

## Positive Semidefinite and Sum of Squares Biquadratic Polynomials

- 原件 2c37bb1f76571f695475ea033c8f65691b4f6a14b098267e664597df3952a91e。local manuscript dated 18 July 2025, 24 physical pages; hash verified。物理页 1, 4, 5, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2506.17260v4 (17 July 2025); no journal version identified。
- 构件候选。Theorem 2.1 reduces an m×n biquadratic form to a tripartite quartic while preserving PSD and SOS; for m=n=2 it invokes Hilbert’s ternary-quartic theorem to obtain existence of an SOS of three quadratics. The local proof performs the dehomogenize/re-homogenize reduction, but is not an algorithm for a Gram certificate。
- 结论位置。Local pp. 4–5, Theorem 2.1 and proof; p.13 limits the paper’s explicit constructions to three subcases。
- 适用范围。C03 correctly does not currently claim this result. The source establishes existence for the 2×2 case, whereas its explicit Section 4 constructions omit the full-cross plus two-neighbor-half-cross case; it cannot yet support a general certificate constructor。
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Compare the local bytes with arXiv v4 and independently formalize the homogenization equivalence and the Hilbert-theorem dependency before implementing a 2×2-only helper。
- [主来源 1](https://arxiv.org/abs/2506.17260)

## Refined Outer-Approximation Algorithms for Monotonic Optimisation

- 原件 2004c934d1c055c87b75e8c77f28178d8a7a2f59bdc960d33b3defa63d77e3f7。Local 21-page PDF; byte-identical to the checked official arXiv PDF。物理页 1, 3, 5, 8, 9, 10, 11, 12, 13, 16, 19, 20。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.13694v1 (2026)。
- 构件候选。For the stated bounded monotonic maximization model, the exact delta-relaxed polyblock algorithm has a proved finite node bound: the proof on pp. 11-12 shows every nonfinal selected vertex is reduced by more than delta in each relevant coordinate and bounds the vertex-tree depth. Balanced anchors make the removed box isotropic. The local PDF is exactly arXiv v1。
- 结论位置。Local PDF p. 3 gives the bounded normal/co-normal monotonic model; pp. 8-10 define balanced anchors and the delta-relaxed algorithm; pp. 11-12 prove Lemmas 1-2 and the finite tree-depth bound; pp. 13-17 define vectorized/tree variants; pp. 19-20 are experiments。
- 适用范围。The theorem is a real-arithmetic result for the exact projection onto the eroded normal set and for the normal/co-normal/increasing-objective framework. It is not an outer-relaxation error-budget theorem for a generic nonlinear program, and the runtime tables do not prove solver complexity or floating-point correctness。
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Implementation needs a verified projection-oracle error invariant: the paper notes bisection for projection computation, while the strict delta descent used by the finite-bound proof must survive numerical rounding. Retain delta as a feasibility relaxation, not a certified original-objective error。
- [主来源 1](https://arxiv.org/abs/2608.13694) · [主来源 2](https://arxiv.org/pdf/2608.13694)

## Separation, Constraint Qualifications, and Cycling in Outer Approximation

- 原件 36c55973344a6d115da3bf8ecac8a7d4256794e82350c5b87d0a8146c9aa64e0。Local 16-page PDF; byte-identical to the checked official arXiv PDF。物理页 1, 2, 3, 6, 9, 10, 11, 12, 16。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2606.26897v1 (2026)。
- 构件候选。Theorem 7 (pp. 10-12) does prove finite convergence for its constructed convex-MINLP OA scheme: infeasible assignments receive OA feasibility cuts, assignments in the unknown optimal set receive OA cuts, and other feasible assignments receive ECP cuts. Lemma 6 supplies the key no-descent-direction argument at a CQ-satisfying optimal NLP solution. The local copy is exactly the official arXiv v1。
- 结论位置。Local PDF pp. 1-3 state the convex MINLP/OA issue; p. 6 links CQ to separation; pp. 9-12 state and prove the relaxed-CQ/ECP finite-convergence result; p. 16 gives the ECP algorithm。
- 适用范围。This does not validate an unrestricted OA fallback. The theorem is tied to the paper's finite integer-assignment setting, convex differentiable model and exact theoretical cut/subproblem framework. The repeat-triggered practical fallback is discussed after the theorem, but source p. 12 still requires optimal assignments to be solved accurately enough and supplies no tolerance-to-separation certificate。
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Before implementation, specify a certified subproblem accuracy/separation test and prove that a detected repeat has the theorem's cut semantics; do not inherit Theorem 7 from a loose NLP termination residual。
- [主来源 1](https://arxiv.org/abs/2606.26897) · [主来源 2](https://arxiv.org/pdf/2606.26897)

## Solving Stochastic Constraints by Oracle-based Gradient Descent and Interval Arithmetic

- 原件 05f5202493ea0d79313dce16155209e328695bd85d49502ac1d74eb4b65c9cf5。arXiv:2604.17275v1 [cs.LO], submitted 19 April 2026; no published journal version identified from the checked primary record。物理页 1, 2, 5, 6, 7, 26。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Local SHA-matched 30-page PDF; its title/authors and 2026 preprint content match arXiv:2604.17275v1, but byte equality with the remote arXiv PDF was not tested。
- 构件候选。The fixed-parameter construction is a potentially useful finite component: assuming exact computable probability masses for axis-aligned boxes and sound interval/constraint propagation, disjoint proven inner boxes give B(x;epsilon) <= V_phi(x), while the retained boundary boxes give a local upper enclosure B plus epsilon. Thus B(x;epsilon) is also a valid lower bound on the global maximum, without converting a search heuristic into a global certificate。
- 结论位置。Local pp. 1--2 formulate the stochastic-constraint objective and framework; p. 5 states compact-domain and computable-box-mass assumptions; pp. 6--7 define B and prove the inner-box lower and local boundary-box upper enclosure; p. 26 is a proof step for the adaptive-oracle concentration analysis. The primary arXiv record confirms v1 and its claimed certified-lower-bound framework。
- 适用范围。This preprint does not validate L03's active generic interval-API claim: it invokes standard interval arithmetic/ICP and computable box masses but does not supply an audited implementation with directed rounding, input-error enclosure, or a verified probability-mass oracle. Its local upper bound is not an upper bound on the global optimum, and its oracle-SGD convergence additionally relies on external stochastic-oracle results and the paper's concentration proof. L03 currently makes no active claim derived from this paper, so no existing certificate promise is broadened here。
- 相关技能。[math-l03-rational-and-interval-certificates](../../../../math-l03-rational-and-interval-certificates/SKILL.md)
- 其余依赖。Before integration, verify a concrete outward-rounded interval engine and mass-integration oracle for every operation/distribution, audit the cited oracle assumptions and concentration argument, and retain separate notation for local V_phi(x) enclosure versus global V_phi-star lower bound。
- [主来源 1](https://arxiv.org/abs/2604.17275)

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

- 原件 a260d9a8da70b44cb94ef3671bf04c937eabd6e544c875cf1ba1b450b7b04aa7。arXiv:2601.04965v3 (20 Jan 2026), local PDF。物理页 10, 11, 12, 13, 14, 26, 27。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Qi, Cui, and Xu, Mathematics 14(4) (2026), 635, DOI 10.3390/math14040635。
- 构件候选。The local arXiv proof and the published canonical article agree on the narrow constructive claim: a PSD monic x-symmetric biquadratic form has a PSD Kronecker Gram matrix and hence an SOS of bilinear forms; its rank bound is rank(R)+(m−1)rank(Q). Separately, any already-SOS m×n form has SOS rank at most mn−1。
- 结论位置。Theorem 2.5 and PSD Gram construction pp.10–11; rank bound Theorem 2.7 pp.12–13; constructive factor extraction p.14; universal SOS-rank Theorem 6.2 proof pp.26–27。
- 适用范围。PSD alone is not enough outside the stated monic x-symmetric (or transposed) class; the universal mn−1 theorem assumes SOS as input. Numerical Cholesky factors require independent exact/interval PSD and coefficient-identity verification。
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Implement only after a parser verifies the exact partial-symmetry/monic normal form and constructs the specified Q,R,M; preserve the distinction between PSD→SOS in that class and SOS-rank reduction in the general class。
- [主来源 1](https://arxiv.org/abs/2601.04965) · [主来源 2](https://www.mdpi.com/2227-7390/14/4/635)

## Sum of Squares Decompositions for Structured Biquadratic Forms

- 原件 0866821532b1970e753a4228b30402966ff9a495bb954c2fbecf01d728c1c1ab。local manuscript dated 12 December 2025, 13 physical pages; hash verified。物理页 1, 3, 4, 5, 7, 9。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2512.02734v2 (11 December 2025); no journal version identified。
- 构件候选。For a diagonally dominated symmetric biquadratic tensor, Theorem 2.1 constructs the coefficient matrix M, proves it symmetric diagonally dominant with nonnegative diagonal, hence PSD, and writes its decomposition as squares of bilinear forms。
- 结论位置。Local pp. 3–4, Theorem 2.1 and full diagonal-dominance-to-PSD-Gram proof; p.5 labels M-tensor/B0-tensor statements as conjectures; pp.7–9 state the monic-symmetric result。
- 适用范围。C03 has no contrary live claim, but this only covers the stated symmetric diagonal-dominance convention. The paper itself leaves symmetric M-biquadratic and B0-biquadratic SOS assertions conjectural, so those must not be added。
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Byte-compare local PDF against arXiv v2, then independently verify the tensor indexing convention and construct a rational Gram/SOS checker for the diagonal-dominant subclass。
- [主来源 1](https://arxiv.org/abs/2512.02734)

## Sum of Squares Submodularity

- 原件 22ee0c0eb9f8ca40979a7eee88dbb7d655bda13c4952d974f0946eb29b66439f。arXiv:2510.24550v2 (26 Jun 2026), local PDF。物理页 6, 7, 10, 30, 32。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2510.24550v2 (26 Jun 2026); no journal version identified。
- 构件候选。The local v2 gives a checkable Boolean-ideal t-SOS submodularity component: Definition 6 requires −∂²F/∂xi∂xj to be t-SOS modulo I2[x−i,j]; Proposition 6 gives fixed-t SDP sizes, and the p.32 proof derives a sum-of-squares first-order certificate, hence submodularity。
- 结论位置。Definition 5 (Boolean ideal) p.6; Definition 6 p.7; Proposition 6 p.10; Corollary 2/Proposition 5 proof pp.30–31; Theorem 1 proof p.32。
- 适用范围。This is only for a set function’s multilinear extension on {0,1}^n with the specified reduced Boolean ideal and degree t. The general C03 skill correctly does not claim this hierarchy, finite-order completeness, or that floating SDP Gram matrices are certificates。
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Implement a separate Boolean-set-function encoder, coefficient/ideal reduction, and exact or interval-verified PSD Gram check; do not infer general semialgebraic SOS convergence。
- [主来源 1](https://arxiv.org/abs/2510.24550)

## The Effective Countable Generalized Moment Problem

- 原件 858d0c6799128b324a1a303b2521f19c47b0540b6fd8b4358d3e0826f87f56d2。arXiv:2501.09385v4 (1 Sep 2025), 27 physical pages; SHA verified。物理页 1, 2, 8, 9, 10, 12, 13, 14。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Preprint only in checked sources: arXiv:2501.09385v4 and HAL hal-04885482v4 (2025); no journal version identified。
- 构件候选。Under Assumptions 1.3, 1.9, and 2.1, the paper proves quantitative Moment-SoS bounds; Corollary 2.5 uses its Proposition 1.8 strong duality, and Theorem 2.13 additionally requires a unique GMP minimizer for weak-star convergence of canonical truncated optimizers. The source is a genuine countable-constraint extension, not a generic finite-GMP claim。
- 结论位置。Local pp. 1-2 give the countable-GMP setting and claimed hypotheses; p. 8 states the effective Positivstellensatz input; pp. 9-10 derive the rate and invoke GMP strong duality; pp. 12-13 prove truncated feasibility-set control; p. 14 states and begins proof of weak-star optimizer convergence。
- 适用范围。No B03 execution step currently implements countable constraint enumeration, S-fullness, the weighted functional spaces, dual attainment, or the effective Positivstellensatz constants. Thus its rates and optimizer convergence cannot be invoked from B03's present finite-moment workflow。
- 相关技能。[math-b03-generalized-moments](../../../../math-b03-generalized-moments/SKILL.md)
- 其余依赖。Before integration, formally map the requested GMP to the paper's vector-of-measures/countable-index setting, prove Assumptions 1.3/1.9/2.1 and unique minimizer where needed, and obtain the Positivstellensatz constants。
- [主来源 1](https://arxiv.org/abs/2501.09385) · [主来源 2](https://hal.science/hal-04885482v4)

## The Fundamental Theorem of Weak Optimal Transport

- 原件 cf4106429915f4a29b6b5d433c53028694884c472785b9c70cb8c0c9cccb7553。arXiv:2501.16316v1, submitted 27 Jan 2025 (local 38-page source PDF; title page dated 28 Jan 2025)。物理页 1, 2, 6, 15, 32。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2501.16316v1 (the arXiv record lists only v1)。
- 构件候选。Theorem 2.15 states, for the relaxed/lifted weak transport formulation, primal attainment and equality with its C-transform dual when C(x,rho) is measurable, p-weakly lower semicontinuous in rho, and has the stated integrable affine lower bound; dual attainment additionally needs (B) and (C), and complementary slackness is P(dx,d rho)-a.s. This is not the ordinary coupling duality currently implemented in D01。
- 结论位置。PDF pp. 1–2 define WOT and hypotheses (A)–(C); p. 6 identifies Theorem 2.15 as the relaxed non-convex theorem; p. 15 states Theorem 2.15; p. 32 shows a later application invoking that theorem under derived hypotheses。
- 适用范围。The local v1 states the result but the inspected pages do not supply a self-contained proof: p. 15 attributes the relaxed duality to an earlier Theorem 3.1 and says the generalization follows line by line from another proof. D01 cannot rely on it as verified support for ordinary or unlifted WOT。
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Audit the cited relaxed-duality Theorem 3.1 and the lifting/compactification construction, then verify conditions (B), (C), p-moment topology, and the exact relation between P and an ordinary coupling before any WOT implementation。
- [主来源 1](https://arxiv.org/abs/2501.16316)

## The Interacting 2D Bose Gas and Nonlinear Gibbs Measures

- 原件 139a7e2dcb60ec7c8dce46d2d19e57f388b0b4b2b2aafe32933fd326e7dbceee。arXiv:1805.03506v1 (4 May 2018)。物理页 1, 2, 3, 4。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:1805.03506v1; no later version listed on the checked arXiv record。
- 待核。The active D02 skill does not rely on this note for its finite-domain Gibbs identity; its provenance correctly treats it as a four-page announcement. The checked arXiv record confirms it has only v1. The local note defines a Bose-gas free-energy minimizer and announces a renormalized nonlinear-Gibbs limit, but p. 3 says the detailed proof will appear in a future paper。
- 结论位置。Local pp. 1–3: announced high-temperature theorem, free-energy/Gibbs-state setup, and explicit statement that proof/details are postponed。
- 适用范围。No theorem proof occurs in this four-page source, so it cannot validate the source-specific quantum/field limit. A related later proof publication was located bibliographically as Lewin–Nam–Rougerie, Classical field theory limit of many-body quantum Gibbs states in 2D and 3D, Invent. Math. 224 (2021), 315–444, DOI 10.1007/s00222-020-01010-4, but its theorem-to-note correspondence and proof were not read here。
- 相关技能。[math-d02-gibbs-entropy-duality](../../../../math-d02-gibbs-entropy-duality/SKILL.md)
- 其余依赖。If the quantum Bose-gas limit is ever made an active skill dependency, read the cited 2021 full proof and map its exact assumptions and conclusions; otherwise retain this source as non-proof background。
- [主来源 1](https://arxiv.org/abs/1805.03506)

## The Unified Separation Condition: A General Constraint Qualification for Smooth and Nonsmooth Optimization

- 原件 3ddb21fea039dbe46d48d0da0c34b7d61bcf9753e03c11ce5d25934a6e1aceeb。arXiv:2609.16981v1 (15 Sep 2026), byte-matched local PDF。物理页 1, 2, 5, 6, 8, 9, 10。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.16981v1; no publisher version identified in the checked primary record。
- 构件候选。The local finite-dimensional USC mechanism is a plausible new qualification lead: for the specified max-type violation function, Lemma 3.1 identifies the lower derivative with minus the distance of zero from the subdifferential, and Theorems 4.3/4.5 prove MFCQ/LICQ imply local USC. Theorem 3.4 presents local exact penalization, but explicitly derives it through cited Demyanov theorems. Current B04 has no USC claim and covers finite-dimensional closed conic LP/facial reduction rather than this nonsmooth nonlinear setting。
- 结论位置。PDF pp.1–2 state USC and scope; p.5 gives quoted Demyanov exact-penalty prerequisites; pp.6–7 prove the lower-derivative/subdifferential identity for a finite smooth maximum; p.8 states Theorem 3.4; pp.9–10 prove MFCQ/LICQ implications。
- 适用范围。The source does not justify importing USC into B04’s conic strong-duality/minimax assertions. Exact-penalty conclusions require the local setting, locally Lipschitz objective, the specified violation/subdifferential calculus, and the external Demyanov exact-penalty dependencies; it is not a general duality qualification。
- 相关技能。[math-b04-qualification-facial-minimax](../../../../math-b04-qualification-facial-minimax/SKILL.md)
- 其余依赖。Independently retrieve and verify the cited Demyanov exact-penalty/local-minimum results and check whether their hypotheses match Theorem 3.4; then decide whether to create a separate local nonsmooth-CQ component rather than widen B04。
- [主来源 1](https://arxiv.org/abs/2609.16981)

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

- 原件 7658d5ec4efa90569b4e4577e8562f2114785929275e9dc7609648335a3310d7。arXiv:2607.15834v1 (17 Jul 2026)。物理页 1, 2, 3, 4, 5, 6, 7, 8, 10, 11。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2607.15834v2 (20 Jul 2026); local 11-page PDF bears v2 and was checked against the primary arXiv record。
- 构件候选。The finite construction is valid: for every satisfying Boolean formula and complementary starts σ, not-σ, any satisfying assignment has distance at most floor(n/2) from one start, by the displayed identity d_H(σ,τ)+d_H(not-σ,τ)=n. This can be used as a verified two-start coverage invariant. The paper itself correctly says the two radius-floor(n/2) balls have total worst-case volume 2^n and its MCTS threads are not exhaustive. Thus it provides no completeness, polynomial-time, UNSAT, or proof-trace guarantee for L05。
- 结论位置。local p.3, Theorem 2 and proof; pp.4–5 and 10–11, algorithm/budget specification; pp.6–8, empirical results and stated limitations; primary arXiv HTML checked。
- 适用范围。The reported SAT/XOR runs are unreplicated empirical claims with modest samples and no CDCL/SLS baseline; some structured instances are solved by preprocessing/unit propagation at zero MCTS playouts. The supplied algorithm returns Unknown after an expansion budget, so failure cannot certify unsatisfiability。
- 相关技能。[math-l05-csp-sat-smt-encoding](../../../../math-l05-csp-sat-smt-encoding/SKILL.md)
- 其余依赖。If adopted, retain only the finite Hamming-coverage lemma and require independently runnable code, exact formula/assignment rechecking, and proof-producing SAT/SMT machinery for any satisfiable/unsatisfiable certificate claim. No active L05 claim was found to rely on the paper。
- [主来源 1](https://arxiv.org/abs/2607.15834)
