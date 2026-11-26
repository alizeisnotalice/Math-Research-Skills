# 优化、矩与严格计算

按原件哈希区分。每条核查保留本机物理页与对应来源。

## A Moment-SOS Hierarchy for Robust Polynomial Matrix Inequality Optimization with SOS-Convexity

- 原件 c5f8382a8abdf2fd9f3860040cb8e2fd24c0997ecda894bf90475a72c4718a98。local arXiv:2304.12628v5, 38 physical pages。物理页 1, 2, 9, 10, 17, 18, 19, 20, 21, 22。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2304.12628v5; related DOI 10.1287/moor.2023.0361 has not been byte-compared
- 待核。For supplied matrix moments, the paper's displayed trace identities reduce a matrix SOS/localizing test to PSD moment matrices. The hierarchy's exactness and atom recovery invoke the quoted matrix flat-extension theorem together with Slater and SOS-convexity assumptions.
- 结论位置。Pages 1--2 state the robust PMI model and SOS-convexity assumptions. Pages 9--10 introduce the matrix moment/localizing cones and quote the flat-extension theorem. Pages 17--22 impose Slater and derive the hierarchy, its convergence, and conditional flat extraction.
- 适用范围。The local paper does not independently prove the imported matrix flat-extension theorem or the quoted SOS-convex optimization result. It therefore does not certify a general robust-PMI hierarchy or a C03 flat-extraction call.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Verify the exact hypotheses of the cited flat-extension and SOS-convex theorems, then implement an RPMIO encoder that checks compactness, Slater, degree truncation, primal/dual residuals, flat rank, recovered atoms, and all PMI constraints.
- [主来源 1](https://arxiv.org/abs/2304.12628)

## Adaptive Metrics for Norm-Minimization-Based Outer Approximation in Convex Vector Optimization

- 原件 67390e5e27908c306cf188094be34cb7d57e6302960cd0be72e7d2baebed22b4。local 27-page PDF labels itself July 2026 and matches the assigned SHA-256。物理页 1, 14, 15, 16, 17, 18, 19。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。Unresolved local revision. arXiv:2605.14320 has a current v3 record, but the local theorem text was not byte-matched to that official version.
- 待核。Conditional on exact scalarization, valid generated halfspaces, compact slices, and uniform bounds mI<=M_k<=MI, the local text gives a qualitative Hausdorff-convergence argument and a conditioning-dependent rate derivation.
- 结论位置。Page 14 proves selected-vertex removal, pp. 15--16 state qualitative Hausdorff convergence and metric conditioning, and pp. 17--18 derive the rate from uniform spectral bounds. Page 19 records experimental qualifications absent from the claimed general certificate.
- 适用范围。The local manuscript asserts a revised dispersion-free result while the public record cannot yet be byte-matched. The full algorithmic guarantee also depends on cut validity, exact scalarizations, compactness, and the cited general rate theorem. No active A02 claim uses it.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Obtain and compare the official arXiv v3 or published bytes with the local PDF, reconcile theorem statements, and independently check the cut-validity and rate-theorem hypotheses before using either convergence result.
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

- 原件 d9b756f8eea5f0231655aed07b96f43ce6375d5238eecdbd4afb37a1abdf6a9b。local arXiv:2507.08525v2 (29 Sep 2025), 25 pages。物理页 1, 2, 3, 10, 11, 12, 15, 20, 21, 22。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2507.08525v2
- 构件候选。For one fixed mixed-integer matrix, the source gives a finite universal augmentation set by combining padded circuits with finitely many basic-integer directions and finite coefficient paths. The final theorem is a matrix-specific finite-test-set statement, rather than a generic solver guarantee.
- 结论位置。Pages 1--3 define universal test sets. Pages 10--12 describe the finite construction through projected integer directions and padded circuits, pp. 15 and 20--21 prove the finite coefficient mechanism, and p. 22 states Theorem 9.
- 适用范围。The construction uses imported results on universal test sets and padded circuits and assumes exact basis and feasibility arithmetic. It does not make test-set enumeration practical in arbitrary size or certify an optimization result without the complete direction enumeration.
- 相关技能。[math-l04-mathematical-programming-workflow](../../../../math-l04-mathematical-programming-workflow/SKILL.md)
- 其余依赖。Verify the cited universal-test-set and padded-circuit statements in their exact forms, then implement a fixed-matrix rational enumerator that retains each basis, coefficient path, feasibility check, and objective-improvement certificate.
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
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。Stochastic Processes and their Applications 130(5) (2020), 2918--2953, DOI 10.1016/j.spa.2019.08.009
- 构件候选。The source's causal duality is a useful continuous target for finite nonanticipative LPs, but it requires causal-plan closedness and the source's weak-continuity property. Its enlargement claims add path-space Brownian and absolute-continuity assumptions.
- 结论位置。Pages 8--9 establish the enlargement and finite-variation setup. Theorem 3.4 on p. 11 and Theorem 3.8 on p. 13 add absolute-continuity, convexity, and integrability hypotheses. Page 26 proves causal duality under lower semicontinuity and the weak-continuity property.
- 适用范围。It does not itself produce a finite-grid encoding or certify a general stochastic-process transport calculation. Existing D01 finite constrained transport lacks the pathwise causal and filtration contract required here.
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Specify a finite time grid, verify each nonanticipativity equality and marginal constraint, derive its LP dual, and separately verify the continuous weak-continuity and filtration assumptions before invoking the journal theorem.
- [主来源 1](https://arxiv.org/abs/1611.02610) · [主来源 2](https://www.sciencedirect.com/science/article/pii/S0304414918303995)

## Conditional Optimal Transport on Function Spaces

- 原件 870ae0faefdc7627c50e64b1af4217c145cc64db3c97202ba3a2aba21b8d712c。local 33-page manuscript, PDF created 6 Feb 2024。物理页 4, 5, 12, 14, 15, 16。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。SIAM/ASA Journal on Uncertainty Quantification 13(1) (2025), 304--338, DOI 10.1137/23M1618922; arXiv:2311.05672v3
- 构件候选。The equality-enforcing cost c_chi makes a conditional coupling an ordinary transport problem only after the common conditioning marginal and Assumption 3.1 are fixed. The dual formula then follows from standard OT, and the map result additionally requires solvability between conditional laws.
- 结论位置。Pages 4--5 formulate conditional Monge/Kantorovich transport and state duality. Page 12 converts equality of the conditioning coordinate into an infinite-cost ordinary OT problem. Pages 14--16 prove the duality and describe the conditional Monge route.
- 适用范围。This does not yield a generic conditional-law or Monge-map interface. Polish spaces, regular conditional laws, feasible finite cost, and the specific cost/regularity hypotheses are essential. The local preprint has not been diffed against the 2025 journal version.
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Compare the local manuscript with the journal theorem and implement a finite-strata certificate that checks common conditioning marginals, each stratum coupling, finite costs, primal/dual equality, and any claimed map uniqueness separately.
- [主来源 1](https://arxiv.org/abs/2311.05672) · [主来源 2](https://epubs.siam.org/doi/10.1137/23M1618922)

## Converging Outer Approximations to Global Attractors Using Semidefinite Programming

- 原件 6b26fbd168b3aff091ff344da20a7881f3c036333e11c43d4cd57ffbd05d78a0。arXiv:2005.03346v3 (4 October 2023), local 22-page PDF。物理页 8, 9, 14, 15, 16。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。Schlosser and Korda, Automatica 134 (2021) 109900, DOI 10.1016/j.automatica.2021.109900. The local preprint is arXiv:2005.03346v3.
- 构件候选。The attractor route has a clear certificate interface: a feasible polynomial SOS dual triple certifies the outer inclusions, while convergence is only asymptotic in Lebesgue volume. It is substantively different from generic outer approximation because it requires forward and backward dynamical Liouville inequalities.
- 结论位置。Theorem 2 on pp.8–9 gives no duality gap and feasible-dual containment. Pages 14–16 specify the polynomial compact semialgebraic SOS relaxation, prove value convergence in Theorem 5, and prove A subset X_k subset Y_k with volume discrepancy tending to zero in Theorem 6.
- 适用范围。It applies to the paper's continuous or discrete dynamical systems, polynomial vector/map data, compact basic semialgebraic X and the Archimedean/SOS assumptions. It neither yields a finite volume-error bound nor Hausdorff convergence, and cannot certify a generic MINLP relaxation.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Implement an attractor-SOS certificate checker that receives the dynamics, defining polynomials, a feasible triple and explicit SOS Gram witnesses. Independently verify every Liouville inequality and report containment separately from unquantified asymptotic volume convergence.
- [主来源 1](https://doi.org/10.1016/j.automatica.2021.109900) · [主来源 2](https://arxiv.org/abs/2005.03346)

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

- 原件 eeaf5dbad4c207b58e1e8eb5c4a6f012a7a407bd0bdb21300919f872cec69d0a。arXiv:2602.23725v3 (20 July 2026), byte-matched local 39-page PDF。物理页 3, 11, 30, 32。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2602.23725v3. No journal edition was identified.
- 构件候选。For a supplied Euclidean Jordan algebra with five pairwise orthogonal extreme-ray generators, the paper reduces a symmetric-cone copositivity obstruction to the five-variable Horn form. The restriction proof is a bounded diagnostic for nonmembership in I_0(E_+), provided the frame and the Horn non-SOS premise are independently certified.
- 结论位置。Page 11 proves the COP_r linear-section identity from a Jordan frame. Page 30 constructs the exposed Horn transformation ray, and p.32 restricts a putative SOS identity to the classical Horn quartic to exclude the zeroth inner SOS level.
- 适用范围。Rank at least five and a valid Jordan-frame representation are indispensable. The argument does not decide copositivity, describe ranks below five, or establish nonmembership at arbitrary hierarchy levels. The non-spectrahedral conclusion separately imports the known non-spectrahedrality of COP_r.
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。Build exact Jordan-frame and quadratic-representation inputs, then independently certify the five-variable Horn non-SOS obstruction and the COP_r reference before exposing an I_0-only diagnostic.
- [主来源 1](https://arxiv.org/abs/2602.23725)

## Copositive Matrices with Ordered Off-Diagonal Entries

- 原件 05990838c18871a47d433307d452dcc18e9c528011a686a602b1f3e30c08218e。arXiv:2605.15970v1 (15 May 2026), byte-matched local 17-page PDF。物理页 5, 6, 11, 12, 13。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2605.15970v1. No journal edition was identified.
- 构件候选。There is a potentially executable guarded route. A symmetric matrix that can be permuted into M_n can be recognized by the acyclicity graph on p.11. Given an independently certified copositivity premise, the proof reduces through deletion or a positive-pivot Schur complement to COP_4=SPN_4.
- 结论位置。Pages 5–6 give the deletion/Schur-complement induction proving COP intersect M_n is contained in SPN. Page 11 turns a permutation test for M_n into topological sorting, while pp.12–13 state the compatible DNN exactness and separable St-QP consequence.
- 适用范围。The M_n test does not prove copositivity. The induction establishes existence of an SPN representation and supplies no rational PSD-plus-entrywise-nonnegative factorization. DNN exactness requires the stated shift-compatible objective class, beyond mere ordering.
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。Implement exact ordering recognition, copositivity premises and recursive PSD/nonnegative factor recovery with a replayable trace. Verify the base COP_4=SPN factorization before issuing an SPN certificate.
- [主来源 1](https://arxiv.org/abs/2605.15970)

## Disjunctive Sum of Squares

- 原件 6e6581b0fab0b52347c7ec6e7bc00a2ee8cad7f51cc79a383625bde81ae81c4c。arXiv:2605.28674v1 (27 May 2026), local 45-page PDF。物理页 8, 14, 25, 26, 29。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2605.28674v1. No journal edition was identified.
- 构件候选。The two p.29 decompositions provide a finite checkable disjunctive nonnegativity certificate for the Horn quadratic form on two displayed simplicial cones. The full strict-positivity and compact-POP convergence claims require the net construction and an imported reduction rather than ordinary SOS completeness.
- 结论位置。Page 8 states the fixed-dimension/even-degree disjunctive Positivstellensatz. Page 14 begins the net-based proof. Pages 25–26 import the compact POP reduction and prove the nested lower-bound hierarchy, while p.29 gives two explicit Horn-matrix cone identities.
- 适用范围。Finite disjunctive membership has strict-positivity scope. The lower-bound hierarchy needs a compactness radius, the exact reduction of reference [2], and all branch certificates. It does not certify arbitrary boundary nonnegativity or a single-cone SOS proof.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。For a reusable tool, encode a finite list of simplicial generators and exact PSD/nonnegative branch identities, then separately audit the net construction and the cited compact-POP reduction before claiming hierarchy convergence.
- [主来源 1](https://arxiv.org/abs/2605.28674)

## Enhancing Presolve in Mixed Integer Programming by Combining Probing and Dual Fixing

- 原件 3bf4856c846a0a634e0a356a50ffb92aa94e0e71f80b3ae99f34b1071a2a7b09。arXiv:2607.10767v1 (12 July 2026), local 15-page PDF。物理页 5, 8, 9, 13。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2607.10767v1. The manuscript reports acceptance by Mathematical Programming Computation, while no version of record or DOI was identified.
- 构件候选。The paper isolates a finite preservation guard for generalized dual fixing: each fixing needs the correctly directed auxiliary MIP bound and a sound propagation implication. This is useful only if every solver-derived conclusion is replaced by independently retained certificates.
- 结论位置。Algorithm 1 on p.5 defines the alternating propagation/dual-fixing loop. Theorem 1 and its reachability argument on pp.8–9 provide the soundness condition. Page 13 is empirical benchmarking only.
- 适用范围。Heuristic propagation, a solver status, and benchmark speedups do not prove preservation of an optimum. Rules R1–R4 depend on the exact MIP convention and objective sign, and this source does not furnish portable certificates for an arbitrary solver run.
- 相关技能。[math-l04-mathematical-programming-workflow](../../../../math-l04-mathematical-programming-workflow/SKILL.md)
- 其余依赖。Specify a target rational MIP certificate format for every auxiliary bound and propagation implication, then replay the proof of Theorem 1 with the selected R1–R4 convention before exposing a presolve action.
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

- 原件 9613fdac4553e3a2e1296c42ea97484cfac5641069de66fc69d13a01fa899eb3。arXiv:1109.1320v2 (2 April 2012), local 21-page PDF。物理页 6, 7, 16, 19。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。Yarotsky, Journal of Global Optimization 56(4) (2013), 1773–1790, DOI 10.1007/s10898-012-9936-x.
- 构件候选。The paper gives a rigorously delimited counterexample family for exact expected improvement, including the crucial posterior-mean identity after the first observation. It is a valid adversarial-search test target once a kernel, noiseless GP convention and tie rule are supplied exactly.
- 结论位置。Theorems 2–3 on pp.6–7 state the spectral-density kernel condition and the non-dense EI construction. Page 16 gives the posterior identity for f=-G, and p.19 completes the induction showing selected points converge to zero.
- 适用范围。It says nothing about arbitrary EI implementations, kernels, noise models, initial designs or tie-breaking. The analytic f=-G construction is distinct from the later smooth modification used for the Gaussian-kernel corollary.
- 相关技能。[math-l02-adversarial-input-search](../../../../math-l02-adversarial-input-search/SKILL.md)
- 其余依赖。Create a finite symbolic/numerical EI replay with an explicit kernel satisfying Theorem 2, exact noiseless posterior formulas, specified tie handling and a clear distinction between the analytic construction and the smooth Gaussian modification.
- [主来源 1](https://doi.org/10.1007/s10898-012-9936-x) · [主来源 2](https://arxiv.org/abs/1109.1320)

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

- 原件 5f9131bfa83088d87854d91842ca15c71752e137db9929e4d02f3c9b6b6e8341。arXiv:2502.04006v2 (16 April 2026), byte-matched local 40-page PDF。物理页 3, 10, 15, 20。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2502.04006v2. No journal edition was identified.
- 构件候选。The paper supplies a precise interior/boundary case split for COP(L_n). Given an independently verified representation COP(L_n)=S_+^n+R_+J_n and explicit subspace witnesses, it distinguishes S_+(X), S_+(X)+R_+J_n and the non-exposed boundary rank-one rays.
- 结论位置。Page 10 proves the interior-vector subface and exposedness classification. Page 15 gives the boundary cases and the exposedness criterion. Page 20 identifies boundary rank-one rays as non-exposed.
- 适用范围。These conclusions are restricted to second-order cones and rely on Lemmas 2.3–2.8 plus the special cone representation. They do not classify faces over nonnegative orthants or general symmetric cones and do not compute a CP factorization.
- 相关技能。[math-c02-completely-positive-copositive](../../../../math-c02-completely-positive-copositive/SKILL.md)
- 其余依赖。Independently certify the Lorentz-cone representation and required witness H(V), then implement exact interior/boundary tests and retain distinct exposed and non-exposed output states.
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

- 原件 e112ec7f105cf4cf7fcf6aa1008cbd7668460072730e6fd7e982bee8a397c618。arXiv:2608.26395v1 (26 August 2026), local 30-page PDF。物理页 7, 8, 10, 11, 12, 15, 16, 20, 21, 28。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2608.26395v1. No journal edition was identified.
- 构件候选。For an exact convergent sequence of finite extremal unit-diameter configurations, merging coincidences followed by the diameter-graph core preserves extremality. Under supplied compatible exposed-pair lifts, a nonnegative dual-pair functional is lower semicontinuous. Stable lifts plus axis-vanishing of the cost yield continuity.
- 结论位置。Pages 7–9 prove the collision/core proposition. Pages 10–12 define compatible/stable dual-pair convergence and prove lower semicontinuity or continuity under its added conditions. Pages 15–16 prove the additive tetrahedral minimum, and pp.20–21 prove the spherical-product reformulation. Page 28 limits the numerical work.
- 适用范围。The result is in three-dimensional extremal diameter geometry. Compatibility and stability are extra hypotheses and the paper explicitly does not prove them for arbitrary collisions. Approximate numerical configurations, fixed-graph local optima and the K4/constant-width conjectures are outside the result.
- 相关技能。[math-a03-compactness-concentration](../../../../math-a03-compactness-concentration/SKILL.md)
- 其余依赖。Encode exact configurations, core reconstruction and exposed-pair witnesses. Require a proof of compatibility/stability for the target family before applying the functional limit theorem, and keep numerical feasibility certificates separate.
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
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2512.14072v3
- 构件候选。The checked skip-state construction is a finite modelling lead when every active path, marginal and path cost is explicitly supplied. Its infinite-space attainment uses tightness, and its uniqueness proof uses a support set plus sequential twist and local control.
- 结论位置。Local pp. 4–5 define the isolated skip states and path cost; p. 9 proves attainment from coercivity; pp. 10 and 14–16 define sequential twist/local control and deduce the Monge map.
- 适用范围。The hierarchical-jump model optimizes intermediate marginals and permits bypassing stages. It does not reduce to the existing fixed-marginal finite constrained-transport LP without a separately verified finite active-path reduction.
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Provide a finite active-index LP encoding and independently prove its relation to the source path model. Keep Polish-space tightness, Kellerer duality and the sequential-twist uniqueness theorem outside that finite branch.
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
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2602.04122v1, local 25-page file has the reviewed SHA-256
- 构件候选。The feasible and infeasible cut calculations are internally consistent under the displayed selected subgradients and KKT multipliers. Finite termination follows only after every integer assignment has a globally solved subproblem and the master cannot repeat an assignment.
- 结论位置。Local p. 6 states Slater A1 and KKT setup, p. 7 proves the feasible fixed-integer cut, pp. 10–11 prove exclusion of an infeasible integer assignment, p. 12 identifies the full master, and pp. 13–14 prove nonrepetition termination.
- 适用范围。Arbitrary nonsmooth solver output does not establish the required multiplier, subgradient or rho conditions. The source requires bounded closed polyhedral X, finite Y intersect integer lattice, Slater for feasible subproblems and an exact infeasibility solve.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Create a rational KKT/subgradient certificate format and an exact finite-integer master checker before adding an A02 branch.
- [主来源 1](https://arxiv.org/abs/2602.04122) · [主来源 2](https://arxiv.org/pdf/2602.04122)

## On Computing the Copositive Minimum and its Representatives

- 原件 673f26accc0cd74ed08fceae15ee0ad05f6381cbc8eb573dab336f6878d1a732。arXiv:2509.23696v1 (28 Sep 2025), byte-matched local 19-page PDF。物理页 1, 2, 3, 4, 7, 8, 12, 13, 15。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2509.23696v1; no formal publication identified in the checked source record
- 已有技能。A reusable exact finite certificate was independently derived and implemented in overlays/04: with a rational SPD leading block, rational nonnegative KKT minimizer for the slice x_n=1, and rational spectral lower bound, f(s)=s^2 f(1) bounds x_n. Completing the square bounds remaining coordinates, so direct rational enumeration covers every nonnegative integer x with Q[x]<=lambda. The source example gives f(1)=3/2, x_n<=1 and nonzero minimum 2. The checker matched brute-force enumeration in 90 seeded rational instances.
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

- 原件 3971b19fd8672edb6d104fa7c15ac24261e14e965991a717c0c36a6217d96570。local 31-page PDF, arXiv:2007.10863v7 dated 5 May 2025。物理页 1, 3, 12, 13, 14, 24, 25。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2007.10863v7
- 构件候选。Lemma 3.9 supplies a bounded symmetry-aware layer reduction for a transitive coordinate-permutation ILP with objective <1,x>: layers l-n<j<=l suffice once l is the floor of the LP optimum. The proof uses exact orbit averaging and a fixed integral layer.
- 结论位置。Local p. 12 states and proves Lemma 3.9; pp. 13–14 delimit finite essential sets; pp. 24–25 state the direct-product construction.
- 适用范围。It needs a bounded LP relaxation, exact transitive coordinate symmetry, the normalized objective and globally solved integral layers. Essential-set inequalities alone allow non-core integer points and do not provide a generic relaxation error certificate.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Implement exact group/model-invariance and layer certificates, then prove any intended connection to A02's outer-relaxation interface.
- [主来源 1](https://arxiv.org/abs/2007.10863)

## Piecewise SOS-Convex Moment Optimization and Applications via Exact Semi-Definite Programs

- 原件 ec78cd78268be31b62458211841946b2fa513fdf2974656b371fc86340e71fee。arXiv:2402.07064v6, 2 July 2024; local 30-page PDF matches v6 front matter。物理页 1, 2, 9, 10, 11, 12, 13, 14。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。EURO Journal on Computational Optimization 12 (2024), article 100094; reviewed e-print arXiv:2402.07064v6
- 构件候选。Theorem 3.4 supports its exact moment/SDP equality only after the stated minimizer, interior and compact strictly feasible projected-spectrahedron hypotheses. Theorem 3.6 recovery adds strong duality, nonnegative zeroth moments and inactive-index sign assumptions.
- 结论位置。Local pp. 1–2 define the projected-spectrahedron model, pp. 9–11 state and prove Theorem 3.4, and pp. 12–14 state Theorem 3.6 recovery conditions.
- 适用范围。The result is not generic moment-SOS exactness, and a numerical SDP solution alone does not recover a measure. The proof invokes a representation theorem and conic-duality results not reproduced in the operational interface.
- 相关技能。[math-b03-generalized-moments](../../../../math-b03-generalized-moments/SKILL.md)
- 其余依赖。Convert Assumptions 3.2–3.3 and every recovery condition into a checkable preflight schema, then audit the representation and duality imports before an exact B03 branch.
- [主来源 1](https://arxiv.org/abs/2402.07064) · [主来源 2](https://doi.org/10.1016/j.ejco.2024.100094)

## Polyhedral Outer-Approximations for MISOCP: Geometry and Cutting Planes

- 原件 8c3ba961d10739df057624c0b1f80e52d2adf0bbda9fee10d6d6bb5a72b76436。local 36-page author PDF by Yongzheng Dai。物理页 1, 4, 5, 6, 7, 9, 10。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。unresolved: local title and scope differ from arXiv:2608.10055v2, and local bytes have not been matched to an official edition
- 待核。The displayed normalized SOC supporting cut has a direct local geometric interpretation. The controlling appendices are absent from the inspected local pages, while the official v2 identity and scope remain unresolved.
- 结论位置。Local p. 4 states Proposition 2.1 on the SOC projection/deepest/gradient cut. Pages 5–7 state angular marginal claims, and pp. 9–10 describe progressive integrality.
- 适用范围。No transfer of convergence, residual feasibility, progressive-integrality or runtime claims is justified from this author manuscript. Current A02 makes none of these source-specific claims.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Byte-compare the local file against arXiv versions or recover a formal edition, then inspect the appendices and master/cut/residual hypotheses.
- [主来源 1](https://arxiv.org/abs/2608.10055) · [主来源 2](https://arxiv.org/pdf/2608.10055)

## Positive Semidefinite and Sum of Squares Biquadratic Polynomials

- 原件 2c37bb1f76571f695475ea033c8f65691b4f6a14b098267e664597df3952a91e。local 24-page manuscript dated 18 July 2025。物理页 1, 4, 5, 13。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2506.17260v4, last revised 17 July 2025; no formal publication identified
- 构件候选。The paper gives a useful 2x2 existential route through a ternary quartic reduction, while its explicit constructions cover only stated cross-term patterns. This does not duplicate the installed monic x-symmetric Gram checker.
- 结论位置。Local p. 1 states the 2x2 PSD-to-SOS consequence; pp. 4–5 give the tripartite transformation; p. 13 lists the restricted explicit constructions and excludes the hard full-cross case.
- 适用范围。The missing full-cross plus neighboring-half-cross configuration lacks a local constructor, and the key Hilbert ternary-quartic theorem is imported. The local manuscript was not byte-matched to the cited v4 PDF.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Recover and compare the v4 source, then formalize the homogenize/dehomogenize reduction and imported SOS theorem before accepting a general 2x2 constructor.
- [主来源 1](https://arxiv.org/abs/2506.17260)

## Refined Outer-Approximation Algorithms for Monotonic Optimisation

- 原件 2004c934d1c055c87b75e8c77f28178d8a7a2f59bdc960d33b3defa63d77e3f7。arXiv:2608.13694v1 (13 Aug 2026), local PDF identified as v1。物理页 1, 3, 8, 9, 10, 11, 12, 13。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2608.13694v1
- 构件候选。For the stated bounded monotonic model, exact projections onto the eroded normal set yield a delta-relaxed epsilon-optimal solution or emptiness, and each nonfinal tree edge loses delta coordinate sum. The counting proof supplies a finite node bound.
- 结论位置。Local p. 3 fixes the normal/co-normal model; pp. 8–10 define balanced anchors and delta relaxation; pp. 10–12 prove termination and the node bound; p. 13 gives vectorization.
- 适用范围。This requires the exact projection oracle, normal/co-normal sets and the delta-eroded feasibility model. It does not certify a floating-point implementation or original-problem epsilon optimality.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Specify a directed projection-oracle certificate that preserves strict delta descent, then encode the relaxed feasibility/objective distinction before an A02 implementation.
- [主来源 1](https://arxiv.org/abs/2608.13694)

## Separation, Constraint Qualifications, and Cycling in Outer Approximation

- 原件 36c55973344a6d115da3bf8ecac8a7d4256794e82350c5b87d0a8146c9aa64e0。arXiv:2606.26897v1, 16 physical pages; local bytes and page count rechecked.。物理页 1, 3, 6, 10, 11, 12, 16。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2606.26897v1 (25 June 2026). No formal publication was identified in the checked source record.
- 构件候选。Theorem 7 is a genuine finite-convergence result for the constructed compact-convex, finite-integer MINLP scheme. It distinguishes infeasible assignments, unknown optimal assignments using OA cuts, and other feasible assignments using ECP cuts. Lemma 6 is the exact CQ-dependent implication needed to retain an optimal fixed-integer value after an OA cut.
- 结论位置。Pages 10--12 define the three-case OA/ECP construction and prove Theorem 7. Page 11 proves the CQ-dependent no-descent Lemma 6. Page 16 gives the ECP iteration, while p.12 explains the repeat-detection fallback.
- 适用范围。The theorem presupposes exact theoretical subproblem/cut semantics and an inaccessible set of optimal integer assignments. Page 12's practical repeated-assignment rule still requires optimal assignments to be solved accurately enough. It provides no residual-to-separation implication for an ordinary nonlinear solver.
- 相关技能。[math-a02-outer-relaxation-budget](../../../../math-a02-outer-relaxation-budget/SKILL.md)
- 其余依赖。Define a certified primal/dual subproblem accuracy condition and prove that a detected repeat implements the theorem's three-case cut semantics before adding a finite-termination route to A02.
- [主来源 1](https://arxiv.org/abs/2606.26897) · [主来源 2](https://arxiv.org/pdf/2606.26897)

## Solving Stochastic Constraints by Oracle-based Gradient Descent and Interval Arithmetic

- 原件 05f5202493ea0d79313dce16155209e328695bd85d49502ac1d74eb4b65c9cf5。arXiv:2604.17275v1, 30 physical pages; local bytes and page count rechecked.。物理页 1, 2, 5, 6, 7, 26。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2604.17275v1, submitted 19 April 2026. No formal publication was identified in the checked source record.
- 构件候选。For a fixed parameter and a sound box classifier, the disjoint certified-inner boxes have total mass B less than or equal to the satisfaction probability. The retained boundary boxes furnish a local upper enclosure B plus epsilon. Thus B is also a lower bound on the global optimum, because the optimum dominates every fixed-point value.
- 结论位置。Pages 5--7 state compactness and computable-box-mass assumptions, define the inner and boundary box quantities, and prove the pointwise enclosure. Page 26 is an oracle-concentration proof step.
- 适用范围。The source supplies neither a directed-rounding implementation nor a verified distributional box-mass oracle. The upper enclosure is local to a fixed parameter, not a global upper bound. Its stochastic-gradient conclusion additionally depends on oracle and concentration hypotheses outside the finite box calculation.
- 相关技能。[math-l03-rational-and-interval-certificates](../../../../math-l03-rational-and-interval-certificates/SKILL.md)
- 其余依赖。Specify a concrete outward-rounded interval/constraint engine and a validated box-mass oracle, then verify the local/global notation and the separate stochastic-oracle assumptions before integration into L03.
- [主来源 1](https://arxiv.org/abs/2604.17275) · [主来源 2](https://arxiv.org/pdf/2604.17275)

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
- 其余依赖。The overlay at overlays/05 supplies a runnable exact JSON contract. Before release, place its script, reference and positive/rejected examples in C03 and run the repository and installation acceptance suite.
- [主来源 1](https://arxiv.org/abs/2512.02734) · [主来源 2](https://arxiv.org/pdf/2512.02734v2)

## Sum of Squares Submodularity

- 原件 22ee0c0eb9f8ca40979a7eee88dbb7d655bda13c4952d974f0946eb29b66439f。arXiv:2510.24550v2, 49 physical pages; local bytes and page count rechecked.。物理页 6, 7, 10, 30, 32。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2510.24550v2, 26 June 2026. No formal publication was identified in the checked source record.
- 构件候选。The Boolean-ideal criterion is a meaningful specialized SOS route. An exact certificate that every negative mixed second derivative is t-SOS modulo the reduced Boolean ideal yields the first-order SOS certificate used to establish submodularity of the multilinear extension.
- 结论位置。Definition 5 gives the Boolean ideal on p.6, Definition 6 gives t-SOS submodularity on p.7, Proposition 6 states fixed-t SDP sizes on p.10, and the proof of Theorem 1 on p.32 turns the derivative certificate into submodularity.
- 适用范围。The statement is confined to a set function's multilinear extension on the Boolean cube, the specified reduced ideal, and an explicit degree t. It does not establish finite-order completeness, generic semialgebraic SOS convergence, or reliability of floating Gram matrices.
- 相关技能。[math-c03-moment-sos-certificates](../../../../math-c03-moment-sos-certificates/SKILL.md)
- 其余依赖。Implement a Boolean-set-function encoder, exact coefficient reduction modulo the Boolean ideal, and exact PSD Gram checks for each mixed derivative before exposing this as a distinct C03 route.
- [主来源 1](https://arxiv.org/abs/2510.24550) · [主来源 2](https://arxiv.org/pdf/2510.24550v2)

## The Effective Countable Generalized Moment Problem

- 原件 858d0c6799128b324a1a303b2521f19c47b0540b6fd8b4358d3e0826f87f56d2。arXiv:2501.09385v4, 27 physical pages; local bytes and page count rechecked.。物理页 1, 2, 8, 9, 10, 12, 13, 14。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2501.09385v4, 1 September 2025. No formal publication was identified in the checked source record.
- 构件候选。The source gives a genuine countable-index, vector-of-measures Moment--SOS extension. Its rate and canonical-optimizer convergence use countable GMP strong duality, S-fullness and weighted spaces, while Theorem 2.13 also assumes a unique minimizer.
- 结论位置。Pages 8--10 state the effective Positivstellensatz input and quantitative rate after the source's GMP duality. Pages 12--14 control truncated feasible sets and state the unique-minimizer weak-star convergence result.
- 适用范围。B03's finite-moment workflow does not encode the countable constraints, weighted spaces, S-fullness, dual-attainment proof or effective Positivstellensatz constants. A small truncated PSD residual alone cannot import the rate or weak-star conclusion.
- 相关技能。[math-b03-generalized-moments](../../../../math-b03-generalized-moments/SKILL.md)
- 其余依赖。Map a concrete target GMP to Assumptions 1.3, 1.9 and 2.1, provide the required Positivstellensatz constants and duality data, and verify uniqueness where optimizer convergence is wanted.
- [主来源 1](https://arxiv.org/abs/2501.09385) · [主来源 2](https://hal.science/hal-04885482v4)

## The Fundamental Theorem of Weak Optimal Transport

- 原件 cf4106429915f4a29b6b5d433c53028694884c472785b9c70cb8c0c9cccb7553。arXiv:2501.16316v1, 38 physical pages; local bytes and page count rechecked.。物理页 1, 2, 6, 15, 32。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2501.16316v1, submitted 27 January 2025. The checked record lists v1 only.
- 待核。Theorem 2.15 states relaxed lifted-plan primal attainment and equality to a C-transform dual under measurable p-weakly lower-semicontinuous cost and an integrable affine lower bound. Dual attainment needs (B) and (C), and complementary slackness is formulated P(dx,d rho)-almost surely.
- 结论位置。Pages 1--2 define weak transport and conditions (A)--(C); p.6 introduces the relaxed non-convex formulation; p.15 states Theorem 2.15; p.32 invokes it in a later application.
- 适用范围。The statement page attributes the relaxed duality to earlier Theorem 3.1 and says the generalization follows another proof line by line. This batch did not independently close that lifting, compactification, p-moment topology or projection to ordinary couplings. It therefore cannot support D01's ordinary finite coupling duality.
- 相关技能。[math-d01-kantorovich-duality](../../../../math-d01-kantorovich-duality/SKILL.md)
- 其余依赖。Read and verify the cited relaxed-duality theorem and its lifting construction, then give an explicit finite rho representation and certify every (B)/(C) and p-moment condition before implementing WOT.
- [主来源 1](https://arxiv.org/abs/2501.16316) · [主来源 2](https://arxiv.org/pdf/2501.16316)

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

- 原件 3ddb21fea039dbe46d48d0da0c34b7d61bcf9753e03c11ce5d25934a6e1aceeb。arXiv:2609.16981v1, 16 physical pages; local bytes and page count rechecked.。物理页 5, 6, 7, 8, 9, 10。
- 依赖复核。已核对本轮采用范围与剩余依赖。
- 规范版本。arXiv:2609.16981v1, submitted 15 September 2026. No formal publication was identified in the checked source record.
- 构件候选。For a finite maximum of smooth constraint functions, the source proves the geometric identity phi_down=-dist(0,partial phi), then derives a local uniform separation bound from MFCQ or LICQ. The MFCQ proof is a direct convex-hull argument and provides a distinct local qualification diagnostic.
- 结论位置。Page 5 records the exact-penalty assumptions invoked by Theorems 2.2--2.3. Pages 6--7 prove the finite smooth-max lower-derivative identity. Page 8 derives Theorem 3.4 from those cited results, while pp.9--10 prove MFCQ/LICQ imply local USC.
- 适用范围。The exact-penalty conclusion imports the attainment, lower-boundedness, descent-neighborhood and local-Lipschitz hypotheses of the stated Demyanov results. USC is a local nonlinear condition and cannot widen B04's conic strong-duality or minimax assertions.
- 相关技能。[math-b04-qualification-facial-minimax](../../../../math-b04-qualification-facial-minimax/SKILL.md)
- 其余依赖。Implement exact finite gradient/active-set separation checks together with certified neighborhood continuity bounds, and independently verify the local exact-penalty theorem before creating a separate nonsmooth-CQ route.
- [主来源 1](https://arxiv.org/abs/2609.16981) · [主来源 2](https://arxiv.org/pdf/2609.16981)

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
