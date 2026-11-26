# 优化、矩与严格计算

按原件哈希区分。每条核查保留本机物理页与对应来源。

## A Moment-SOS Hierarchy for Robust Polynomial Matrix Inequality Optimization with SOS-Convexity

- 原件 c5f8382a8abdf2fd9f3860040cb8e2fd24c0997ecda894bf90475a72c4718a98。Local PDF arXiv:2304.12628v5, 38 physical pages, SHA-256 c5f8382a8abdf2fd9f3860040cb8e2fd24c0997ecda894bf90475a72c4718a98.。物理页 1, 2, 9, 10, 17, 18, 19, 20, 21, 22。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2304.12628v5, last revised 8 October 2024; the checked record lists related DOI 10.1287/moor.2023.0361, but no byte comparison to that edition was made.
- 构件候选。The reusable bounded contract is a robust-PMI hierarchy only under stated SOS-convexity, compact uncertainty and Slater assumptions: construct matrix moment/localizing PSD constraints and obtain monotone decreasing SDP bounds. A flat extension plus the theorem's matching feasibility/equality conditions yields an atomic matrix-valued measure and optimizer extraction.
- 结论位置。Local pp.1–2 define RPMIO and Assumption 1; pp.9–10 define the matrix moment/localizing cone and quote matrix flat extension; pp.17–18 impose Slater and derive conic reformulation; pp.19–22 define the hierarchy and prove convergence/flat-extraction directions.
- 适用范围。The proof depends on the imported matrix flat-extension theorem [28, Theorem 6.2] and an SOS-convex optimization result [33, Theorem 3.3]. Flatness alone is insufficient, and an entrywise scalar Lasserre substitute does not establish the robust matrix-PMI claims.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Read and verify those two imported theorems in their exact formulations, then implement RPMIO degree encoders, Assumptions 1–3 checks, primal/dual hierarchy construction, matrix flatness, atom recovery and certified PSD/residual validation.
- [主来源 1](https://arxiv.org/abs/2304.12628)

## Adaptive Metrics for Norm-Minimization-Based Outer Approximation in Convex Vector Optimization

- 原件 67390e5e27908c306cf188094be34cb7d57e6302960cd0be72e7d2baebed22b4。Local 27-page PDF labels itself July 2026 and matches the assigned SHA-256; its text presents an epsilon-regularized uniformly conditioned metric theorem.。物理页 1, 14, 15, 16, 17, 18, 19。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Unresolved. arXiv:2605.14320 current v3 is authoritative metadata, but its checked primary abstract retains a strictly-convex-boundary/dispersion theorem that the local PDF's pp. 15–19 explicitly supersedes or rejects; the local bytes were not matched to the official v3 PDF.
- 待核。The local document contains a coherent bounded construction: exact norm-minimization scalarizations and valid dual cuts preserve the compact upper-image slice; a selected external vertex is removed; uniform spectral bounds yield Euclidean Hausdorff convergence and the stated asymptotic rate. However, the primary arXiv v3 abstract currently describes a materially different dispersion/curvature theorem and associated experimental claim, so the local source cannot yet be safely identified with that public revision.
- 结论位置。Local p. 14 Lemma 11 gives selected-vertex removal; pp. 15–16 Theorem 12 gives qualitative Hausdorff convergence; pp. 17–18 Theorem 14 and Remark 6 derive the rate from mI<=M_k<=MI; p. 19 records the corrected experimental qualification.
- 适用范围。The source-family identity conflict blocks citation or implementation of its rate/performance claims. Even the local proof assumes a compact slice, exact solves, valid dual pairs/cuts, farthest-vertex selection, and a k-independent positive conditioning lower bound; it is not generic OA. A02 does not assert its rate, dispersion, or performance claims, so no false active claim was found.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Download and byte-compare the official arXiv v3 PDF (and any publisher text) with the local file; reconcile the dispersion/curvature and experimental statements before rechecking the full proof chain.
- [主来源 1](https://arxiv.org/abs/2605.14320) · [主来源 2](https://arxiv.org/pdf/2605.14320)

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

- 原件 d9b756f8eea5f0231655aed07b96f43ce6375d5238eecdbd4afb37a1abdf6a9b。Local 25-page PDF matching arXiv:2507.08525v2 (2025-09-29)。物理页 1, 2, 3, 10, 11, 12, 15, 20, 21, 22。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2507.08525v2; no published version identified
- 构件候选。For one fixed mixed-integer matrix A=(A_R|A_I), Theorem 9 gives a finite universal augmentation test set through padded circuits and finitely enumerated coefficient directions. This is a bounded, independently checkable candidate only after each direction is tested for exact feasibility and objective improvement.
- 结论位置。Model/infinite-set issue (pp.2–3); finite construction scope (pp.10–12); Lemma 6 and finite coefficients (pp.15,20–21); Theorem 9 (p.22).
- 适用范围。The proof depends on the cited universal MIP-Graver test-set result, its nondegeneracy/basis-path construction, and Algorithm 4 enumeration; it promises neither a small black-box list nor polynomial-time construction. It is not installed as an L04 method.
- 相关技能。[math-l04-mathematical-programming-workflow](../../../../math-l04-mathematical-programming-workflow/SKILL.md)
- 其余依赖。Verify the cited universal-test-set result and Lemma 6 hypotheses, then implement a matrix-specific exact enumerator with retained feasibility/improvement certificates.
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

- 原件 e6358fcb0f1598334408a9e27b2a8e28f2122f391b338b74fbbe573b018f1498。local arXiv:1611.02610v2 (12 Dec 2017), 33 pages。物理页 1, 8, 9, 11, 13, 26。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Stochastic Processes and their Applications 130(5) (2020), 2918–2953, DOI 10.1016/j.spa.2019.08.009
- 构件候选。A defensible discrete transferable core is the nonanticipativity constraint: on a finite time grid, require a coupling's conditional law of target prefixes given a source path to depend only on the matching source prefix, then solve the resulting constrained LP. The paper's continuous result connects that causal condition, under Wiener reference and nu≪gamma, to an enlarged-filtration Brownian decomposition; it separately establishes causal duality with a weak-continuity assumption.
- 结论位置。PDF p. 1 abstract; pp. 8–9 enlargement/semimartingale direction; p. 11 Theorem 3.4; p. 13 Theorem 3.8; p. 26 Theorem 5.6 causal duality.
- 适用范围。The continuous theorems require filtrations, causality direction, path-space Wiener reference, absolute continuity, adapted drift/Orlicz conditions and cost growth. They do not validate static D01 OT or arbitrary stochastic path couplings.
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Verify finite-grid causal constraints against the source definition and LP dual; for continuous use reconcile v2 with the 2020 journal theorem, then check the weak-continuity property and every Brownian/absolute-continuity hypothesis.
- [主来源 1](https://arxiv.org/abs/1611.02610) · [主来源 2](https://www.sciencedirect.com/science/article/pii/S0304414918303995)

## Conditional Optimal Transport on Function Spaces

- 原件 870ae0faefdc7627c50e64b1af4217c145cc64db3c97202ba3a2aba21b8d712c。local 33-page manuscript, PDF created 6 Feb 2024。物理页 4, 5, 12, 14, 15, 16。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。SIAM/ASA Journal on Uncertainty Quantification 13(1) (2025), 304–338, DOI 10.1137/23M1618922; arXiv:2311.05672v3
- 构件候选。The reusable finite/transferable contract is conditional OT by strata: retain the conditioning coordinate, couple only samples within a fixed stratum, and use the infinite cost chi(y,z) to prohibit cross-stratum mass. Proposition 3.6 derives the associated partial-c-transform duality under Polish/disintegration and lsc bounded-below cost; Proposition 3.8 reduces a unique conditional map to Monge solvability on the conditionals.
- 结论位置。PDF pp. 4–5 conditional problem and Theorems 1.6–1.7; p. 12 infinite equality-enforcing cost; pp. 14–16 Proposition 3.6 duality and conditional Monge proof route.
- 适用范围。It is not ordinary OT on the product: finite feasibility, the fixed equality coordinate, disintegration, and reference-conditional regularity are indispensable. The local manuscript was not byte-compared with the journal version.
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Diff the local manuscript against the published version and, for any proposed use, certify the conditional-coordinate law, Polish regular conditional distributions, feasibility, cost assumptions and the conditional Monge theorem separately.
- [主来源 1](https://arxiv.org/abs/2311.05672) · [主来源 2](https://epubs.siam.org/doi/10.1137/23M1618922)

## Converging Outer Approximations to Global Attractors Using Semidefinite Programming

- 原件 6b26fbd168b3aff091ff344da20a7881f3c036333e11c43d4cd57ffbd05d78a0。arXiv:2005.03346v3 (4 Oct 2023), local 22-page PDF with assigned SHA-256。物理页 1, 8, 9, 14, 15, 16。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Schlosser and Korda, Automatica 134 (2021) 109900, DOI 10.1016/j.automatica.2021.109900; arXiv v3 identity was checked, while the publisher page returned 403 and the publisher bytes were not compared
- 构件候选。A precise specialized outer-approximation construction is verified. Any feasible dual triple gives A contained in {w>=1}; with the stated polynomial dynamics and SOS hierarchy, Theorem 6 gives A subset X_k subset Y_k and Lebesgue volume of Y_k minus A tending to zero. The proof order is containment first, then volume convergence.
- 结论位置。Local pp. 8–9 Theorem 2 gives dual no-gap and containment; p. 14 supplies the polynomial/basic-semialgebraic SOS setup; p. 15 Theorem 5 gives SDP-value convergence; p. 16 Theorem 6 proves outer containment and volume-discrepancy convergence.
- 适用范围。This is global-attractor certification, not an objective-error or generic MINLP OA result. It requires the paper's continuous/discrete dynamical assumptions, polynomial dynamics, compact basic semialgebraic set with the required SOS/Archimedean condition, and exact feasible SDP/SOS certificates. It establishes volume, not Hausdorff convergence or a finite relaxation certificate. A02 makes none of those stronger claims.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。If added, create a separate attractor-SOS interface that verifies all dynamics/set assumptions and reports certified containment with volume-only convergence; do not fold it into generic A02 termination logic.
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

- 原件 eeaf5dbad4c207b58e1e8eb5c4a6f012a7a407bd0bdb21300919f872cec69d0a。arXiv:2602.23725v3 (20 Jul 2026), byte-matched local 39-page PDF。物理页 1, 3, 11, 30, 32。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2602.23725v3; no publisher edition was identified in the checked arXiv record
- 构件候选。The preprint supports a sharply bounded obstruction. For a symmetric cone K of rank r>=5, p.11 embeds COP_r as a linear section using pairwise orthogonal extreme-ray generators, then states non-spectrahedral-shadow status. For a five-ray Horn transformation, p.30 obtains an exposed COP(K) ray by a cone automorphism, while p.32 gives a direct restriction argument showing q_H(x^2) is not SOS of quadratic forms and therefore H is not in I_0. C02 does not misstate this as a finite-level result for its R_+^n moment hierarchy.
- 结论位置。PDF pp. 1 and 3 state the rank-at-least-five symmetric-cone setting; p.11 proves the embedded COP_r lemma and Theorem 3.2; p.30 proves the exposed Horn-ray result; p.32 proves exclusion from the zeroth SOS inner level.
- 适用范围。The proofs use Euclidean-Jordan-algebra structure, rank at least five, the non-spectrahedrality input for COP_r, and the classical five-dimensional Horn non-SOS result. They say nothing about ranks 3–4, nor do they establish arbitrary-level nonmembership or finite-level exactness of C02's Lasserre hierarchy.
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。To make an obstruction tool, formalize the Jordan frame and five orthogonal extreme-ray inputs, independently check the inherited COP_r and Horn non-SOS references, and state the result only as an I_0/exposed-ray diagnostic for the specified symmetric cone.
- [主来源 1](https://arxiv.org/abs/2602.23725)

## Copositive Matrices with Ordered Off-Diagonal Entries

- 原件 05990838c18871a47d433307d452dcc18e9c528011a686a602b1f3e30c08218e。arXiv:2605.15970v1 (15 May 2026), byte-matched local 17-page PDF。物理页 1, 2, 5, 6, 11, 12, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2605.15970v1; no publisher edition was identified in the checked arXiv record
- 构件候选。A bounded special-case construction is verified. For a symmetric A whose off-diagonal entries satisfy the paper's two-index monotonicity defining M_n, pp. 5–6 reduce a copositive A recursively by either deletion or a positive-diagonal Schur complement, preserve M_n, and invoke the n<=4 COP=SPN base; hence A in COP intersect M_n implies A in SPN. The same pages make the ordering test a concrete guard, and pp. 11–13 correctly restrict St-QP/DNN exactness to the compatible Q class. C02 makes no false general-copositivity claim from this source.
- 结论位置。PDF pp. 1–2 state the ordered-entry/SPN and St-QP aims; pp. 5–6 state and prove Theorem 3.5; pp. 11–12 give the CP/COP and DNN/SPN value relation; p. 13 states the separable-QP application.
- 适用范围。The theorem presupposes copositivity and does not decide it for arbitrary matrices. The proof is an existence proof through COP-preserving deletion/Schur steps and does not itself output rational PSD-plus-nonnegative factors; the relaxation statement also requires the shift-invariant objective class rather than merely an ordered Q.
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。Implement a guarded finite route that first verifies symmetry and M_n (including an allowed permutation/rescaling), then requires an independent COP witness or a separately specified St-QP exactness hypothesis; add exact PSD/nonnegative factor recovery and a checkable recursion trace before exposing an SPN certificate.
- [主来源 1](https://arxiv.org/abs/2605.15970)

## Disjunctive Sum of Squares

- 原件 6e6581b0fab0b52347c7ec6e7bc00a2ee8cad7f51cc79a383625bde81ae81c4c。Local PDF arXiv:2605.28674v1 dated 27 May 2026, 45 physical pages, SHA-256 6e6581b0fab0b52347c7ec6e7bc00a2ee8cad7f51cc79a383625bde81ae81c4c.。物理页 1, 8, 14, 25, 26, 29。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2605.28674v1, submitted 27 May 2026; no journal edition was identified in the checked authoritative record.
- 构件候选。For fixed dimension and even degree, Theorem 1 gives a bounded-degree-per-branch strict-positivity construct; Theorem 10 verifies that its union cones yield nondecreasing lower bounds converging for the cited compact-POP framework. The Horn-matrix two-cone calculation on p.29 is a finite, checkable disjunctive nonnegativity witness.
- 结论位置。Local p.8 states the fixed-(n,d) disjunctive Positivstellensatz; p.14 shows one degree-preserving SOS transformation; pp.25–26 define the compact-POP hierarchy and Theorem 10; p.29 provides a concrete copositivity disjunction.
- 适用范围。Finite-stage membership concerns strict positivity, not arbitrary boundary nonnegativity. The POP conclusion imports the compact reduction in reference [2] and also needs a radius/compactness contract; it does not license ordinary single-cone SOS completeness.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Audit Theorems 2, 4, 8 and 9 plus the rest of Theorem 1's construction, then independently read reference [2], Theorems 2.1 and 2.4, before implementing any lower-bound hierarchy.
- [主来源 1](https://arxiv.org/abs/2605.28674)

## Enhancing Presolve in Mixed Integer Programming by Combining Probing and Dual Fixing

- 原件 3bf4856c846a0a634e0a356a50ffb92aa94e0e71f80b3ae99f34b1071a2a7b09。Local 15-page manuscript matching arXiv:2607.10767v1 (2026-07-12)。物理页 1, 5, 8, 9, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2607.10767v1; checked record says accepted for Mathematical Programming Computation, but no version of record/DOI identified
- 构件候选。The reusable finite guard is Theorem 1's auxiliary-MIP lower/upper-bound reachability test: together with the stated objective-sign rule it permits a generalized dual fixing only after the appropriate exact bound and propagation implication have been certified.
- 结论位置。Algorithm 1 (p.5); Theorem 1 and reachability proof (pp.8–9); benchmark conclusion (p.13).
- 适用范围。The method is model- and convention-dependent; a solver status, heuristic propagation, or benchmark speedup is not a proof that a new variable fixing preserves an optimum. No active A01/A04/L04 claim relies on it.
- 相关技能。[math-l04-mathematical-programming-workflow](../../../../math-l04-mathematical-programming-workflow/SKILL.md)
- 其余依赖。Verify rules R1–R4 and bound directions on the target MIP, retain certificates for every auxiliary optimization, and recover the publisher version before citation-level use.
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

- 原件 9613fdac4553e3a2e1296c42ea97484cfac5641069de66fc69d13a01fa899eb3。arXiv:1109.1320v2 (2012-04-02; 21 local PDF pages)。物理页 1, 6, 7, 16, 19。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Yarotsky, Journal of Global Optimization 56(4) (2013), 1773-1790, DOI 10.1007/s10898-012-9936-x; arXiv:1109.1320v2 is the checked manuscript
- 构件候选。The defensible finite counterexample template is exact EI on D=[-1,1] with a stationary kernel satisfying Theorem 2, objective f=-G, and initial point x1=0: Theorem 3 proves the selected design points converge to 0 and hence are not dense. The proof's key finite identity is that the posterior mean equals f because f=-G(.-x1). The smooth Gaussian-kernel failure is obtained only after a separate modification argument.
- 结论位置。Local PDF pp. 6-7 Theorems 2-3 and Gaussian-kernel corollary; p. 16 exact-EI posterior identity; p. 19 induction giving convergence of the selected points to zero.
- 适用范围。This does not say arbitrary EI, arbitrary GP priors, arbitrary initializations, or arbitrary smooth objectives fail. The analytic objective f=-G is distinct from the C-infinity modified objective used for the Gaussian-kernel inconsistency corollary.
- 相关技能。[math-l02-adversarial-input-search](../../../../math-l02-adversarial-input-search/SKILL.md)
- 其余依赖。Any L02 adversarial audit must specify the kernel/spectral-density hypotheses, tie-breaking and exact EI acquisition rule, initial design, and whether it uses the analytic f=-G construction or the separate C-infinity modification; certify those finite choices before extrapolating.
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

- 原件 5f9131bfa83088d87854d91842ca15c71752e137db9929e4d02f3c9b6b6e8341。arXiv:2502.04006v2 (16 Apr 2026), byte-matched local 40-page PDF。物理页 1, 3, 10, 15, 20。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2502.04006v2; no journal edition was identified in the checked arXiv record
- 构件候选。The v2 identity and a limited facial classification are verified. With L_n the second-order cone, an interior defining vector (1;v), ||v||<1, gives subfaces S_+(X) and exposedness in Theorem 3.1. On the boundary, Theorem 3.9 and Proposition 3.10 distinguish S_+(X) from S_+(X)+R_+J_n and make exposedness conditional on (1;-v) not lying in X; p.20 explicitly exhibits boundary rank-one rays as non-exposed. This is a useful case-split template, not an active C02 dependency.
- 结论位置。PDF pp. 1 and 3 delimit COP(L_n)/CP(L_n) and the second-order-cone scope; p. 10 gives Theorem 3.1 and proof; p. 15 gives Theorem 3.9/Proposition 3.10; p. 20 identifies the boundary rank-one non-exposed rays.
- 适用范围。Every displayed conclusion uses the special representation of COP(L_n), the Lorentz-cone interior/boundary split and the cited preliminary lemmas. It neither classifies faces of COP(R_+^n) nor general symmetric-cone CP/COP faces, and it is not a finite CP-factorization procedure.
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。Before adding a facial tool, independently verify the COP(L_n)=S_+^n+R_+J_n representation and Lemmas 2.3–2.8, then implement the interior/boundary tests with explicit witnesses H(V); retain separate output states for exposed and non-exposed cases.
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

- 原件 e112ec7f105cf4cf7fcf6aa1008cbd7668460072730e6fd7e982bee8a397c618。arXiv:2608.26395v1, submitted 26 August 2026; local 30-page PDF has matching v1 front matter.。物理页 1, 2, 7, 8, 9, 10, 11, 12, 15, 16, 20, 21, 23, 28, 29, 30。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.26395v1 (only version on the checked primary record).
- 构件候选。A narrowly reusable collision-handling construction is verified: an exact convergent sequence of finite extremal unit-diameter configurations, after merging coincidences and taking the diameter-graph core, yields an extremal core. For dual-pair functionals, Proposition 5 gives only lower semicontinuity under compatible convergence, and equality needs stability plus axis-vanishing of the cost. The paper explicitly says arbitrary collision compatibility/stability is unproved.
- 结论位置。PDF pp. 7--9 prove the exact-limit/core Proposition 2; pp. 10--12 state the added compatible/stable dual-pair hypotheses and prove their lower-semicontinuity/continuity consequences; pp. 15--16 prove the tetrahedral additive minimum; pp. 20--21 prove the spherical-product supremal reformulation; pp. 23 and 28--30 delimit numerical conclusions.
- 适用范围。This does not establish general concentration compactness, feasibility of approximate numerical solver output, or attainment of intrinsic dual-edge functionals. The 10,644-graph experiment uses local optimization and expressly does not certify a fixed graph's global maximum; the K4/constant-width claims remain conjectural.
- 相关技能。[math-a03-compactness-concentration](../../../../math-a03-compactness-concentration/SKILL.md)
- 其余依赖。Any use must supply an exact convergent configuration sequence or a validated numerical certificate, reconstruct the unit-distance core and exposed pairs, and separately prove compatibility/stability for the target class before passing a functional to the limit.
- [主来源 1](https://arxiv.org/abs/2608.26395)

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

- 原件 4e4f65485ed8c30eae404e5693b9cd6761e5e9723ccbfff42d91c086116ea495。local arXiv:2512.14072v3, revised 25 Jun 2026, 22 pages。物理页 4, 5, 9, 10, 14, 15, 16。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2512.14072v3
- 构件候选。A bounded finite implementation lead is explicit: add one isolated skip state per optional intermediate stage, enumerate active paths, minimize the displayed path cost while optimizing intermediate marginals, and require the paper's coercive tightness guard. The source proves attainment under that guard and proves a Monge path only after singleton optimal continuations follow from sequential twist plus local control.
- 结论位置。PDF pp. 4–5 augmented skip-point path cost; p. 9 Theorem 2.2 attainment; pp. 10 and 14–16 sequential-twist/local-control definitions and Theorem 3.1 proof.
- 适用范围。The model is not standard MOT: mass may bypass intermediate spaces and their marginals are optimization variables. The claimed uniqueness depends on Kellerer-dual/cyclic-monotonicity support, sequential twist, and strong coercivity, none of which D01 currently implements.
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Audit Lemma 3.1 and the Kellerer-duality/c-cyclical-monotonicity route producing the support set, then supply a finite active-index test and separate coercivity/twist verification before any new branch.
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

- 原件 69909f6afc65e3b2954766721918786782fc880653a9198fb07caea45dc1d34c。arXiv:2602.04122v1 (Zhou Wei, He-Yi Liu, Bo Zeng; 4 Feb 2026)。物理页 1, 6, 7, 10, 11, 12, 13, 14。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2602.04122v1; the checked primary record has one version and the local 25-page PDF has the assigned SHA-256
- 构件候选。A reusable bounded contract is independently read: under A1 and selected KKT-compatible subgradients/multipliers, feasible cuts preserve the fixed-integer NLP optimum; Proposition 3.3 excludes an infeasible integer assignment; Theorem 3.2 identifies the full master with the stated MINLP; and the termination proof requires finite Y intersect Z^p and no master assignment repeat.
- 结论位置。Local p. 6 states Slater A1 and feasible subproblem KKT conditions; p. 7 proves the feasible-cut implication; pp. 10–11 formulate/prove infeasible-assignment exclusion; p. 12 Theorem 3.2 gives master equivalence; pp. 13–14 prove termination by nonrepetition.
- 适用范围。The theorem does not follow from arbitrary subgradients or generic nonlinear-solver output. It needs a bounded closed polyhedral X, finite integer choices, Slater for every feasible fixed-integer subproblem, solved feasibility problems, and the particular rho/subgradient/multiplier conditions. A02 already requires global masters and valid cuts, but does not falsely advertise this nonsmooth finite-termination theorem.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Provide an implementable certificate for the KKT-compatible subgradients, multipliers, rho choices, and infeasibility solve before adding a nonsmooth A02 subroutine.
- [主来源 1](https://arxiv.org/abs/2602.04122) · [主来源 2](https://arxiv.org/pdf/2602.04122)

## On Computing the Copositive Minimum and its Representatives

- 原件 673f26accc0cd74ed08fceae15ee0ad05f6381cbc8eb573dab336f6878d1a732。arXiv:2509.23696v1 (28 Sep 2025), byte-matched local 19-page PDF。物理页 1, 2, 3, 4, 7, 8, 12, 13, 15。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2509.23696v1; no publisher edition was identified in the checked arXiv record
- 构件候选。Two limited claims are checked. Theorem 2.3's full pp.3–4 calculation gives a deterministic Subset-Sum reduction to the integer strictly-copositive MinCOP decision instance. Separately, the pp.12–13 one-difficult-coordinate contract is constructive: when the leading block is positive definite, compute f(1)=min{Q(x):x>=0,x_n=1}; homogeneity gives f(s)=s^2f(1), hence an exact upper bound on integral x_n under Q[x]<=lambda before ordinary finite enumeration of the remaining coordinates. This is a candidate certificate route, not a claim of an efficient general COP optimizer.
- 结论位置。PDF pp. 1–2 define MinCOP and strict copositivity; pp. 3–4 prove the Subset-Sum reduction in Theorem 2.3; pp. 7–8 give exact LDLT completion-of-squares; pp. 12–13 prove the one-difficult-coordinate finite bound and state the SPN special case; p.15 records the general bound obstruction.
- 适用范围。The paper's practical implementation uses floating-point bounds and heuristics, and the general difficult-coordinate bounding problem is explicitly nonconvex/NP-hard on p.15. The SPN route additionally needs an exact S+N decomposition; an LDLT factorization alone neither proves strict copositivity nor provides a rigorous finite search bound.
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。For a reusable finite certificate, require rational Q, a proof that the selected leading block is positive definite, an exact rational/interval solution or certified lower bound for f(1)>0, and exact enumeration checks; keep general multi-difficult-coordinate and numerical-performance claims out of the skill.
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

- 原件 3971b19fd8672edb6d104fa7c15ac24261e14e965991a717c0c36a6217d96570。Local 31-page PDF, arXiv:2007.10863v7 dated 5 May 2025; local front matter matches that identifier and author list.。物理页 1, 3, 12, 13, 14, 24, 25。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2007.10863v7 (checked primary record; it supersedes the earlier v1 citation).
- 构件候选。Lemma 3.9 is verified for a transitive permutation-symmetric ILP with objective normalized to <1,x>: if l is the LP-optimum floor, checking the n integer layers l-n<j<=l decides infeasibility or locates an optimal feasible layer. Its proof uses orbit averaging into Fix_R(G)=span(1), then the integral fixed point on a layer divisible by n and convexity. This is a bounded symmetry-aware layer reduction, not a premise of A02's general outer-relaxation inequalities.
- 结论位置。PDF p. 12 states and proves Lemma 3.9; pp. 13--14 delimit finite essential sets and Algorithm 1 subproblems; pp. 24--25 give the direct-product algorithm and its stated symmetry scope.
- 适用范围。It requires an actual bounded LP relaxation, exact transitive coordinate-permutation invariance, this objective normalization, and globally solved integer subproblems. The finite essential-set inequalities are outer approximations; the source itself permits non-core integer points satisfying them, so they do not provide a generic symmetry-breaking or relaxation-error certificate.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Implement exact group/model-invariance and layer checks plus global subproblem certification; separately prove any bridge from this special ILP construction to A02's set-map and objective-error framework.
- [主来源 1](https://arxiv.org/abs/2007.10863)

## Piecewise SOS-Convex Moment Optimization and Applications via Exact Semi-Definite Programs

- 原件 ec78cd78268be31b62458211841946b2fa513fdf2974656b371fc86340e71fee。arXiv:2402.07064v6, 2 July 2024; local 30-page PDF front matter matches v6.。物理页 1, 2, 9, 10, 11, 12, 13, 14。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。EURO Journal on Computational Optimization 12 (2024), article 100094, DOI 10.1016/j.ejco.2024.100094; checked e-print version arXiv:2402.07064v6.
- 构件候选。Theorem 3.4 supports equality of the stated moment optimum and SOS/SDP dual only with a minimizer and Assumptions 3.2--3.3 (including interior and compact strictly feasible projected-spectrahedron conditions and SOS-convex data). The recovery result is narrower: Theorem 3.6 additionally assumes strong (R)--(S) duality, nonnegative zeroth moments, and signs for inactive k. B03 presently does not use this paper, and neither B02 exchange nor L02 finite search gains a general guarantee from it.
- 结论位置。PDF pp. 1--2 define the projected-spectrahedron piecewise SOS-convex moment model; pp. 9--11 state/prove Theorem 3.4; pp. 12--14 state/prove Theorem 3.6 and Corollary 3.7 on recovery.
- 适用范围。This is not generic moment-SOS exactness and Theorem 3.4 alone does not recover a measure from a numerical SDP. The proof uses the paper's representation theorem and conic-duality appendix; recovery has its own strong-duality and sign conditions.
- 相关技能。[math-b03-generalized-moments](../../../../math-b03-generalized-moments/SKILL.md)
- 其余依赖。Translate every Assumption 3.2--3.3 and Theorem 3.6 recovery condition into a preflight checklist, then separately audit the invoked representation and conic-duality inputs before an exact-SDP/recovery interface is added.
- [主来源 1](https://arxiv.org/abs/2402.07064) · [主来源 2](https://doi.org/10.1016/j.ejco.2024.100094)

## Polyhedral Outer-Approximations for MISOCP: Geometry and Cutting Planes

- 原件 8c3ba961d10739df057624c0b1f80e52d2adf0bbda9fee10d6d6bb5a72b76436。Local 36-page author PDF by Yongzheng Dai with assigned SHA-256; title/abstract differ from the checked arXiv record's current title.。物理页 1, 4, 5, 6, 7, 9, 10。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。Unresolved. The checked arXiv:2608.10055v2 is titled 'Polyhedral Outer Approximation for MISOCP: Geometry and Progressive Integrality'; the local author PDF was not byte-matched to v1, v2, or a publisher version.
- 待核。One local finite geometric identity was checked: Proposition 2.1 makes the normalized projection support inequality simultaneously a deepest, supporting, and gradient SOC cut. The local document also states angular marginal-effect bounds. But the local title/abstract and the official v2 title/scope differ, and the local proof itself refers key results to appendices not read in this pass, so this cannot yet be attached to an A02 module.
- 结论位置。Local p. 4 Proposition 2.1 identifies the SOC projection/deepest/gradient cut; pp. 5–7 give marginal-direction and bounded-volume statements; pp. 9–10 describe progressive integrality and only its relaxation/bound motivations.
- 适用范围。The official arXiv v2 advertises progressive-integrality transfer and experiments, whereas the local source is an unbyte-matched author version. Any claims about novelty, finite convergence, residual feasibility, or runtime transfer remain MISOCP-specific and unverified here. A02 has no active candidate-specific MISOCP claim, so there is no false active claim to retract.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Byte-compare local PDF with arXiv v1/v2 and recover the publisher version; then audit the cited appendices and exact global-master, cut-validity, lower/upper-bound, and residual-feasibility hypotheses.
- [主来源 1](https://arxiv.org/abs/2608.10055) · [主来源 2](https://arxiv.org/pdf/2608.10055)

## Positive Semidefinite and Sum of Squares Biquadratic Polynomials

- 原件 2c37bb1f76571f695475ea033c8f65691b4f6a14b098267e664597df3952a91e。Local 24-page manuscript dated 18 July 2025, SHA-256 2c37bb1f76571f695475ea033c8f65691b4f6a14b098267e664597df3952a91e.。物理页 1, 4, 5, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2506.17260v4, last revised 17 July 2025; no journal edition was identified in the checked authoritative record.
- 构件候选。The defensible narrow transfer is existential: via the stated reduction of a 2×2 biquadratic to a ternary quartic and Hilbert's ternary-quartic result, the source claims PSD 2×2 biquadratic forms are SOS. Its Section 4 itself constructs only three restricted cross-term configurations.
- 结论位置。Local p.1 gives the claimed 2×2 consequence; pp.4–5 state the biquadratic/tripartite transformations; p.13 specifies which 2×2 constructive subcases are actually covered.
- 适用范围。The local pages do not yield a general Gram-construction algorithm: the hard full-cross plus two-neighbor-half-cross configuration is expressly left out of the explicit constructions, and the key ternary-quartic SOS theorem is imported rather than proved.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Byte-compare/recover the official arXiv v4 PDF, then independently formalize the homogenize/dehomogenize equivalence and the imported Hilbert theorem before admitting a 2×2-only constructor.
- [主来源 1](https://arxiv.org/abs/2506.17260)

## Refined Outer-Approximation Algorithms for Monotonic Optimisation

- 原件 2004c934d1c055c87b75e8c77f28178d8a7a2f59bdc960d33b3defa63d77e3f7。arXiv:2608.13694v1 (13 Aug 2026); local PDF and checked arXiv record identify v1。物理页 1, 3, 8, 9, 10, 11, 12, 13。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2608.13694v1; checked arXiv record lists only v1
- 构件候选。Raw SHA and 21-page count match. This v1 supplies a concrete, proof-backed finite construction: with exact projections onto the eroded normal set, the δ-relaxed polyblock algorithm returns a δ-relaxed ε-optimal point or detects emptiness, and nonfinal tree edges lose at least δ coordinate sum, yielding the stated finite node-depth/count bound. It is a useful candidate addition to A02, whose current text already prevents misreading residual tolerances as original-objective error.
- 结论位置。Local p. 3 fixes the bounded normal/co-normal monotonic model; pp. 8–10 define balanced anchors, δ-relaxation, and Algorithm 2; Lemmas 1–2 on pp. 10–11 and their counting argument on p. 12 prove finite termination; p. 13 gives the vectorized extension
- 适用范围。The guarantee is only for the defined bounded normal/co-normal monotonic maximization framework, exact feasibility/projection oracle, and δ-eroded feasible set. It is not a generic outer-relaxation guarantee, nor a floating-point certificate or an ε-objective bound for the unrelaxed problem.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Before implementation, establish a numerical projection-oracle invariant strong enough to preserve the strict δ coordinate descent and distinguish the δ feasibility relaxation from all original feasibility/objective errors.
- [主来源 1](https://arxiv.org/abs/2608.13694)

## Separation, Constraint Qualifications, and Cycling in Outer Approximation

- 原件 36c55973344a6d115da3bf8ecac8a7d4256794e82350c5b87d0a8146c9aa64e0。arXiv:2606.26897v1 (Erik Tamm and Jan Kronqvist; 25 Jun 2026)。物理页 1, 6, 9, 10, 11, 12, 16。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2606.26897v1; the checked primary record has one version and the local 16-page PDF has the assigned SHA-256
- 构件候选。A concrete limited fallback is verified. At a CQ-satisfying optimal fixed-integer NLP, Lemma 6 establishes the no-descent inequality used by OA cuts. Theorem 7's constructed convex-MINLP scheme uses infeasibility OA cuts, OA cuts at optimal assignments, and ECP cuts at the other feasible assignments; p. 12 explains a repeat-detection ECP fallback. This supports the existing A02 warning that an approximate NLP point need not separate the MILP iterate.
- 结论位置。Local pp. 6 and 9 identify CQ-dependent separation failure; pp. 10–12 state the relaxed-CQ/ECP construction and prove its finite convergence; p. 16 gives the ECP algorithm.
- 适用范围。The proof is for the paper's finite-integer, convex differentiable MINLP construction with exact theoretical cut/subproblem semantics. Its practical fallback still says that optimal assignments must be solved accurately enough and gives no residual-to-separation certificate. A02 itself does not claim this theorem or finite convergence under loose solver tolerances, so no false active claim was found.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Specify and independently certify a subproblem accuracy/separation test, and prove that repeat detection has the cut semantics of Theorem 7 before integrating the fallback.
- [主来源 1](https://arxiv.org/abs/2606.26897) · [主来源 2](https://arxiv.org/pdf/2606.26897)

## Solving Stochastic Constraints by Oracle-based Gradient Descent and Interval Arithmetic

- 原件 05f5202493ea0d79313dce16155209e328695bd85d49502ac1d74eb4b65c9cf5。Local 30-page manuscript matching arXiv:2604.17275v1 (2026-04-19)。物理页 1, 2, 5, 6, 7, 26。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2604.17275v1; no journal version identified in checked record
- 构件候选。The strongest defensible finite component is pointwise: under compactness, computable masses for disjoint axis-aligned boxes, and sound interval constraint propagation, the mass of proven inner boxes is B(x;epsilon)≤V_phi(x), and retained boundary-box mass gives a local upper enclosure. This yields a lower bound on the global optimum only through max_x V_phi(x)≥B(x;epsilon), not a global upper certificate.
- 结论位置。Problem/framework (pp.1–2); assumptions (p.5); Definition 1 and Theorem 1 enclosure (pp.6–7); adaptive-oracle proof step (p.26).
- 适用范围。The preprint invokes interval arithmetic/ICP and a box-mass oracle but does not furnish an audited directed-rounding implementation, input-error enclosure, or distribution-mass API. Its SGD result additionally rests on oracle/concentration assumptions. No active L03 claim uses this method.
- 相关技能。[math-l03-rational-and-interval-certificates](../../../../math-l03-rational-and-interval-certificates/SKILL.md)
- 其余依赖。Audit a concrete outward-rounded engine and exact/validated box-mass oracle, then separately verify the stochastic-oracle assumptions and distinguish the local enclosure from global optimization bounds.
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

- 原件 0866821532b1970e753a4228b30402966ff9a495bb954c2fbecf01d728c1c1ab。arXiv:2512.02734v2 (11 Dec 2025), byte-matched local 13-page PDF。物理页 1, 3, 4, 5, 7, 9。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2512.02734v2; no journal edition was identified in the checked arXiv record
- 构件候选。A finite SOS construction is verified for the stated diagonal-dominance class. Given the symmetric tensor convention on p.3 and inequality (2), the coefficient matrix M indexed by (i,j) is symmetric diagonally dominant with nonnegative diagonal (p.4), hence PSD; an exact factorization of M yields B(x,y)=z^T Mz as a sum of squares of bilinear forms in z_(i,j)=x_i y_j. This is directly compatible with C03's Gram-matrix workflow and does not create a false general nonnegative-implies-SOS claim.
- 结论位置。PDF p.1 identifies v2; pp.3–4 state and prove Theorem 2.1 by forming the mn-by-mn coefficient matrix; p.5 explicitly labels M- and B0-biquadratic SOS assertions as conjectures; pp.7 and 9 give the monic-symmetric PSD and vertex-SOS route.
- 适用范围。The construction is only as valid as the tensor symmetries and exact diagonal-dominance inequality. The source's M-biquadratic and B0-biquadratic extensions are conjectures on p.5 and cannot be imported; the monic-symmetric branch has separate parameter conventions and must not be conflated with the diagonal-dominant criterion.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Implement an exact rational checker for symmetry and (2), construct M, certify M PSD by a rational LDL^T/Gram factorization, then expand the bilinear-square identity. Treat the M/B0 conjectures and any floating Gram output as excluded.
- [主来源 1](https://arxiv.org/abs/2512.02734)

## Sum of Squares Submodularity

- 原件 22ee0c0eb9f8ca40979a7eee88dbb7d655bda13c4952d974f0946eb29b66439f。Local PDF arXiv:2510.24550v2, 49 physical pages, SHA-256 22ee0c0eb9f8ca40979a7eee88dbb7d655bda13c4952d974f0946eb29b66439f.。物理页 1, 6, 7, 10, 30, 32。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2510.24550v2, submitted 28 October 2025 and revised 26 June 2026; no journal edition was identified in the checked authoritative record.
- 构件候选。A finite transferable component is the Boolean-ideal Gram test: for every pair i!=j, reduce −d²F/(dx_i dx_j) modulo I2[x_{−i,j}] and seek a degree-t SOS Gram representation. Proposition 6 gives fixed-t polynomial-size SDP verification, while the p.32 telescoping/ideal calculation explains why these pairwise certificates imply diminishing marginal derivatives and hence submodularity.
- 结论位置。Local pp.6–7 define the Boolean ideal and t-SOS submodularity; p.10 is Proposition 6; p.30 gives a finite Gram-SDP instance; p.32 starts the proof that t-SOS submodularity implies submodularity.
- 适用范围。This applies only to a set function's multilinear extension on the Boolean variety and the stated reduced ideal. It neither supplies a general semialgebraic SOS hierarchy nor turns a floating PSD matrix into an exact certificate.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Implement an explicit set-function-to-multilinear-polynomial encoder, ideal reduction and coefficient-matching Gram SDP; validate returned Gram matrices by rational reconstruction or directed intervals.
- [主来源 1](https://arxiv.org/abs/2510.24550)

## The Effective Countable Generalized Moment Problem

- 原件 858d0c6799128b324a1a303b2521f19c47b0540b6fd8b4358d3e0826f87f56d2。arXiv:2501.09385v4, 1 September 2025; local 27-page PDF front matter matches v4.。物理页 1, 2, 8, 9, 10, 12, 13, 14。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2501.09385v4 (checked primary record; no journal version was identified in the checked record).
- 构件候选。Under Assumptions 1.3, 1.9, and 2.1, the inspected proof gives quantitative Moment-SoS gaps; Corollary 2.5 calls Proposition 1.8 for GMP strong duality. Theorem 2.13 additionally requires a unique GMP minimizer to conclude weak-star convergence of canonical truncated optimizers. This is a real countable-constraint/vector-of-measures extension, not support for B03's current finite-moment workflow.
- 结论位置。PDF pp. 1--2 set the countable-GMP assumptions; p. 8 states the effective Positivstellensatz input; pp. 9--10 derive the rate and invoke GMP strong duality; pp. 12--13 control truncated feasibility sets; p. 14 states and begins the weak-star optimizer-convergence proof.
- 适用范围。Neither countable constraint enumeration, S-fullness, weighted functional spaces, dual attainment, nor the effective Positivstellensatz constants are implemented by B03. Hence its rates and weak-star convergence cannot be inferred for a finite numerical hierarchy merely from PSD feasibility or a small objective gap.
- 相关技能。[math-b03-generalized-moments](../../../../math-b03-generalized-moments/SKILL.md)
- 其余依赖。Formally map a target GMP to the paper's countable-index/vector-of-measures setting, prove Assumptions 1.3/1.9/2.1 and uniqueness where needed, and obtain the required Positivstellensatz constants before use.
- [主来源 1](https://arxiv.org/abs/2501.09385)

## The Fundamental Theorem of Weak Optimal Transport

- 原件 cf4106429915f4a29b6b5d433c53028694884c472785b9c70cb8c0c9cccb7553。local arXiv:2501.16316v1 (27 Jan 2025), 38 pages。物理页 1, 2, 6, 15, 32。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2501.16316v1; official record lists v1 only
- 构件候选。The transferable component is a finite lifted-plan certificate: represent a weak conditional law rho explicitly, optimize a cost C(x,rho), and record complementary slackness against the lifted plan rather than an ordinary edge coupling. Theorem 2.15 states relaxed primal/dual attainment under p-weak lsc and an integrable affine lower bound, with dual attainment only under (B),(C).
- 结论位置。PDF pp. 1–2 ordinary/WOT setup; p. 6 announces relaxed nonconvex formulation; p. 15 Theorem 2.15; p. 32 verifies its hypotheses in a later application.
- 适用范围。This is not an unlifted ordinary Kantorovich theorem. The source itself says non-relaxed nonconvex WOT duality can fail; Theorem 2.15 relies on earlier relaxed duality/lifting material rather than a proof on its statement page.
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Audit cited Theorem 3.1 and the lifting/compactification construction; then define the finite rho representation, p-moment topology, (B)/(C) checks, and the exact projection back to ordinary couplings.
- [主来源 1](https://arxiv.org/abs/2501.16316)

## The Interacting 2D Bose Gas and Nonlinear Gibbs Measures

- 原件 139a7e2dcb60ec7c8dce46d2d19e57f388b0b4b2b2aafe32933fd326e7dbceee。arXiv:1805.03506v1 (4 May 2018)。物理页 1, 2, 3, 4。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:1805.03506v1; no later version listed on the checked arXiv record
- 待核。The active D02 skill does not rely on this note for its finite-domain Gibbs identity; its provenance correctly treats it as a four-page announcement. The note defines a Bose-gas free-energy minimizer and announces a renormalized nonlinear-Gibbs limit, but p. 3 says the detailed proof will appear in a future paper.
- 结论位置。Local pp. 1–3: announced high-temperature theorem, free-energy/Gibbs-state setup, and explicit statement that proof/details are postponed.
- 适用范围。No theorem proof occurs in this four-page source, so it cannot validate the source-specific quantum/field limit. A related later proof publication was located bibliographically as Lewin–Nam–Rougerie, Classical field theory limit of many-body quantum Gibbs states in 2D and 3D, Invent. Math. 224 (2021), 315–444, DOI 10.1007/s00222-020-01010-4, but its theorem-to-note correspondence and proof were not read here.
- 相关技能。[math-d02-gibbs-entropy-duality](../../../../math-d02-gibbs-entropy-duality/SKILL.md)
- 其余依赖。If the quantum Bose-gas limit is ever made an active skill dependency, read the cited 2021 full proof and map its exact assumptions and conclusions; otherwise retain this source as non-proof background.
- [主来源 1](https://arxiv.org/abs/1805.03506)

## The Unified Separation Condition: A General Constraint Qualification for Smooth and Nonsmooth Optimization

- 原件 3ddb21fea039dbe46d48d0da0c34b7d61bcf9753e03c11ce5d25934a6e1aceeb。arXiv:2609.16981v1, submitted 15 September 2026; local 16-page PDF front matter matches v1.。物理页 1, 2, 5, 6, 7, 8, 9, 10。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2609.16981v1 (only version on the checked primary record).
- 构件候选。A limited local nonsmooth-CQ component is verified: for the stated finite max-type violation function, Lemma 3.1 derives phi_down(x)=-dist(0,partial phi(x)), and the displayed MFCQ/LICQ arguments give local uniform separation. This is adjacent to B04's finite-dimensional closed-conic LP/facial-reduction scope and does not support a minimax or strong-duality claim there.
- 结论位置。PDF pp. 5--8 connect USC to the quoted Demyanov exact-penalty conditions; pp. 6--7 prove the lower-derivative/subdifferential distance identity for the displayed max-type violation function; p. 8 states Theorem 3.4; pp. 9--10 prove MFCQ/LICQ imply local USC.
- 适用范围。Theorem 3.4 is not self-contained: it explicitly invokes Demyanov exact-penalty theorems, whose hypotheses include lower boundedness, attainment of penalized infima, a neighborhood descent condition, and local Lipschitzness. The text's assertion that these are automatic after localization needs an independently checked local theorem; USC is not a general conic duality qualification.
- 相关技能。[math-b04-qualification-facial-minimax](../../../../math-b04-qualification-facial-minimax/SKILL.md)
- 其余依赖。Retrieve and verify the cited Demyanov local exact-penalty result with its topology and attainment assumptions, then build a separate finite-dimensional nonsmooth-CQ checker rather than widen B04's PPS/facial-minimax interface.
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

- 原件 7658d5ec4efa90569b4e4577e8562f2114785929275e9dc7609648335a3310d7。Local 11-page PDF bearing arXiv:2607.15834v2 (2026-07-20); original submission v1 was 2026-07-17。物理页 1, 2, 3, 4, 5, 6, 7, 8, 10, 11。
- 依赖复核。根据本轮对原件及现有技能的复核更新。
- 规范版本。arXiv:2607.15834v2
- 构件候选。The defensible finite statement is the two-start Hamming identity d_H(sigma,tau)+d_H(not-sigma,tau)=n: every satisfying assignment is within floor(n/2) of one complementary start. It is a coverage invariant, not a solver guarantee.
- 结论位置。Theorem 2/proof (p.3); algorithm and budget (pp.4–5,10–11); empirical/limitations (pp.6–8).
- 适用范围。The MCTS search is nonexhaustive and returns Unknown after budget exhaustion; its experiments are not reproducible correctness or UNSAT evidence. It supplies no proof trace, completeness, or polynomial-time SAT guarantee. No active L05 claim relies on it.
- 相关技能。[math-l05-csp-sat-smt-encoding](../../../../math-l05-csp-sat-smt-encoding/SKILL.md)
- 其余依赖。If used, keep only the coverage lemma; independently rerun code with assignment rechecking and use proof-producing SAT/SMT machinery for all SAT/UNSAT certificates.
- [主来源 1](https://arxiv.org/abs/2607.15834)
