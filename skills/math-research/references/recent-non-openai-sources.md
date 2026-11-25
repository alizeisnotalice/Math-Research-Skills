# 近期非 OpenAI 数学文献逐篇核对

本页按八类主题收录实际归档的 95 份 PDF。来源属性分别为 Anthropic 官方 6 份、关联作者 4 份、其他 GitHub 作者 83 份和黎曼假设导读 2 份。每份标出固定的本机 SHA、页码、局部方法及依据。

来源的 Lean 声称、人工复核与本机精确回放分别判定。需要采用一条断言时，从条目的原文定位和依赖出发。正式来源保留版本或题录，外部仓库链接用于定位发布入口。

## 形式化、证书与计算表示

### Prove2Me

- 来源与本机版本。Anthropic 关联。External methodology paper, cited by Anthropic's FLT release; manuscript first posted Aug 28, v2 Aug 31。15 页。SHA-256 为 `87aaad288301d9c124cabf456d425b9e334232faed498323f54f7493a7f8423b`。 [发布入口](https://arxiv.org/abs/2608.28433)
- 原文位置。local PDF sha256=87aaad288301d9c124cabf456d425b9e334232faed498323f54f7493a7f8423b; pp. 1, 3–5, 8–10, 12
- 局部构件。Anthropic-related methodology/platform paper, not an Anthropic mathematical theorem. It documents Lean theorem cards, a sensitivity-conjecture example, and an audit workflow.
- 依赖。Lean acceptance is scoped to the pinned toolchain/Mathlib environment, but pp. 3 and 12 explicitly say statement faithfulness still requires human audit. No platform mission, source checkout, or kernel build was independently run here.
- 审阅状态。exclude from theorem-skill evidence; retain only as a formalization-workflow reference.

### Formalizing Fermat’s Last Theorem in Lean

- 来源与本机版本。Anthropic 官方。Anthropic technical report; formalization of a known theorem。17 页。SHA-256 为 `0e469ae87a0318cef9aa9fc653aabaeead0d5ebd3e31f3f1fa9b077be746a118`。 [发布入口](https://www.anthropic.com/research/formalizing-fermats-last-theorem)
- 原文位置。local PDF sha256=0e469ae87a0318cef9aa9fc653aabaeead0d5ebd3e31f3f1fa9b077be746a118; pp. 1–2, 17; linked repository anthropics/fermats-last-theorem
- 局部构件。Official Anthropic technical narrative/selected agent-reasoning excerpts about formalizing the already known FLT, not a new mathematical theorem. It reports 29,511 theorem dependencies and a Wiles–Taylor–Wiles route.
- 依赖。It builds on Mathlib, Imperial College’s FLT project, and flt-regular (p. 2). The document explicitly says the quoted mathematical claims were not independently verified; no repository revision, full dependency audit, or replay was run here.
- 审阅状态。exclude as new-theorem evidence; keep only as a formalization-engineering case study.

### A Whole Table Row in One Natural Number: Kernel-Checked Dynamic Programming with a Proved Width Bound

- 来源与本机版本。其他 GitHub 作者。作者公开稿。16 页。SHA-256 为 `4d6280e746446fdd750538dc4bb456c3aa7ebe16856669f1f48f55b124852f72`。 [发布入口](https://github.com/Amey-Thakur/SAIR-FOUNDATION-FOR-SCIENCE-AND-AI-RESEARCH/blob/main/papers/V-lean-kernel.pdf)
- 原文位置。local PDF p. 1 (locked partition-counting specification and measured claim); local PDF implementation/provenance section
- 局部构件。Packed-natural-number encoding of an entire dynamic-programming row, intended to make Lean reduction of partition-number recursion substantially cheaper than list or direct evaluation.
- 依赖。The numerical step counts and universal correctness claim depend on the exact Lean 4 implementation, evaluator and checked proof objects, rather than on a mathematical derivation recoverable from the PDF text alone.
- 有限齐次整数位宽证明与 Python 精确回放已复核。Lean 性能主张留待独立重放。 [定宽打包的非负递推](../../math-l23-packed-nonnegative-recurrences/SKILL.md)

### Exact rational certificates and a Lean formalization of the eleven-variable Vasc inequality

- 来源与本机版本。其他 GitHub 作者。作者公开稿。11 页。SHA-256 为 `0f2724a10778fbb1472cd9633914297a841ffe96a290fd8c0892517841c3444a`。 [发布入口](https://mechmath.github.io/publication/vasc-n11/)
- 原文位置。local PDF pp. 1–3 Theorem 1 and reduction; pp. 4–10 rational Gram/certificate format, construction and Lean replay design
- 局部构件。Exact SOS/Gram certificate pipeline: denominator clearing, translate by the minimum coordinate, certify derivative and boundary polynomials with rational Gram matrices, and check identities in Lean.
- 依赖。The theorem depends on six external JSON proof-object arrays and a Lean project/native_decide replay; the PDF describes their semantics and sizes but does not embed all certificate payloads.
- 审阅状态。held—method is reusable, but the 11-variable inequality is not locally replayable from the PDF alone; require hashes/data and Lean replay.

### Length as Priority, Not Constraint: Search Geometry of the Andrews-Curtis Challenge Pool

- 来源与本机版本。其他 GitHub 作者。作者公开稿。18 页。SHA-256 为 `f3d6dfde39e6e5a214c8f98a59a16e7f0061b27a6f1e4cbb27677364ff9bafd9`。 [发布入口](https://github.com/Amey-Thakur/SAIR-FOUNDATION-FOR-SCIENCE-AND-AI-RESEARCH/blob/main/papers/III-andrews-curtis.pdf)
- 原文位置。Author-hosted experimental manuscript, 11 Nov 2026, PDF pp. 1–16, Propositions 1–4 and conclusion; no formal publication identifier stated.
- 局部构件。Best-first search ordered by relator length plus weighted depth, with bounded-search exclusion diagnostics.
- 依赖。The formal propositions use the specified Andrews–Curtis move semantics; all empirical scope is the SAIR pool, reference verifier, snapshots, tie rule, machine budget, and stated weights. Negative experimental results are not general impossibility theorems.
- 审阅状态。held

### The Verdict Is Free: A Saturated Benchmark for Equational Implication, and What It Leaves to Prove

- 来源与本机版本。其他 GitHub 作者。作者公开稿。11 页。SHA-256 为 `fb6e073a70ca63d3a9feb5d13b6e841f2623465610d80ec0e9dc672a990d4fb7`。 [发布入口](https://github.com/Amey-Thakur/SAIR-FOUNDATION-FOR-SCIENCE-AND-AI-RESEARCH/blob/main/papers/IV-equational-distillation.pdf)
- 原文位置。IV-equational-distillation.pdf, pp.1-9
- 局部构件。Benchmark audit separating total verdict lookup from accepted Lean certificates.
- 依赖。Author empirical audit; counts depend on dataset, ETP snapshot, custom harness; none rerun.
- 审阅状态。hold


## 数论、特殊函数与丢番图逼近

### Riemann Hypothesis and Dirichlet GRH: author’s note

- 来源与本机版本。Anthropic 关联。Personal note by Anthropic researcher; not a conventional paper or official Anthropic release。4 页。SHA-256 为 `3fc97784b71ddd44ff8aa0a177e99622a1c61b13cfa843a0989ee4a7a0cfeb8d`。 [发布入口](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)
- 原文位置。local PDF sha256=3fc97784b71ddd44ff8aa0a177e99622a1c61b13cfa843a0989ee4a7a0cfeb8d; pp. 1–4
- 局部构件。Personal announcement/narrative by an Anthropic researcher, not an official Anthropic paper and not a proof exposition. It asserts a Lean formalization and sketches the intended theta-lift/Stepanov route.
- 依赖。The claimed RH/Dirichlet-GRH conclusion depends on the external multi-part Lean archive named on p. 1; the note supplies no theorem statement, derivation, source revision pin, or independently checked build.
- 审阅状态。hold; do not promote RH/GRH or create a mathematics tool from this note.

### A proof of the Applegate–Lagarias Conjecture A and the 3x+1 growth exponent conjecture

- 来源与本机版本。其他 GitHub 作者。作者公开稿。15 页。SHA-256 为 `5f1e5513421c68e2b2ccc9ae6485636499a07d4dd7086b157645d278a2f556f9`。 [发布入口](https://github.com/neljaouh/ConjectureA/blob/main/paper/applegate-lagarias-conjecture-a-proof.pdf)
- 原文位置。local PDF pp. 1, 3–5, 7–11, 13 (dependency diagram, imported theorem, 3x-1 estimates, conclusion and caveat)
- 局部构件。Claims a positive-density predecessor construction for every target prime to 3, reducing positive targets to an imported 3x+1 theorem and negative targets to a parallel 3x-1 weighted inverse-history argument.
- 依赖。The paper explicitly identifies Theorem 2.2 as its only imported input and says its human-readable proofs in references \[5,6\] are unrefereed; its own Section 9 stresses that kernel checking is not independent mathematical review. The claimed growth result is consequently downstream of that unaudited input.
- 审阅状态。held — do not use either claimed resolution as a mathematical tool; the primary inverse-history proof and its Lean sources require separate, independent audit.

### An irrationality measure for Catalan’s constant

- 来源与本机版本。其他 GitHub 作者。作者公开稿。64 页。SHA-256 为 `b283e8c7f3b5ca61695e40c8a0ca7862765959d25502c3d0ea4d1645de1df97a`。 [发布入口](https://github.com/slitsey/catalan-irrationality-measure/tree/main/paper)
- 原文位置。local PDF p. 2 Theorem 1.1; pp. 52–53 §8 proof; pp. 17–26 modular-corank inputs; p. 54 §10 formalization
- 局部构件。Determinant irrationality-measure pipeline: integerize linear forms, prove modular corank gains, combine a local determinant upper bound with a prime-selection criterion.
- 依赖。Explicitly uses the prime number theorem and a prior OpenAI Catalan proof; the claimed kernel check is an external Lean 4 formalization, while the PDF supplies the mathematical outline and parameter bounds.
- 采用给定合格缩放和秩证书后的局部行列式估值。全文无理性测度留作来源主张。 [模素数余秩估值](../../math-openai-arithmetic-determinants/references/litsey-catalan-corank.md)

### Chebotarev Fingerprints: Identifying Degree-24 Galois Groups Without Computer Algebra

- 来源与本机版本。其他 GitHub 作者。作者公开稿。16 页。SHA-256 为 `8ab9be29e6190279d6cc7dbfcea2229308fc514afa44aa5b4535dae902844b36`。 [发布入口](https://github.com/Amey-Thakur/SAIR-FOUNDATION-FOR-SCIENCE-AND-AI-RESEARCH/blob/main/papers/II-inverse-galois.pdf)
- 原文位置。local PDF pp. 1, 9–10: abstract, asymptotic caveat, and 600-case evaluation table
- 局部构件。Abstaining statistical classifier: factor at fixed primes, score cycle-type fingerprints against sampled group profiles, and threshold the likelihood margin.
- 依赖。Chebotarev only licenses asymptotic equidistribution; labels/profiles/576,682-server corpus and Magma computations are external, and the paper expressly says no effective theorem validates 60 small primes.
- 审阅状态。held—empirical method, not a proof-producing Galois-group identification tool or a universal accuracy theorem.

### Exact Zero Detection and Compact Arithmetic Realizations for the Riemann Xi Function

- 来源与本机版本。其他 GitHub 作者。作者公开稿。208 页。SHA-256 为 `5c6d8d3e070a56576ef938c2dcfe47a7e2a8a1c6ed429612eac503b5a30ee04d`。 [发布入口](https://github.com/LeonardSEO/riemann-xi-zero-detection/blob/v1.0.0/paper/paper.pdf)
- 原文位置。local PDF pp. 1–6 abstract/contents/main-results overview; p. 9 Theorem 6; p. 17 §8 says global positivity is still missing; pp. 204–205 conclusions
- 局部构件。Conditional/diagnostic Xi workflow: compact spectral packets, Weil-form negative-index identities, and energy lower bounds detecting a hypothetical off-line zero.
- 依赖。Uses standard xi analytic continuation/zero-counting and many cited analytic-number-theory inputs; crucial global positivity/source upper bound is explicitly unproved, so no RH consequence is established.
- 审阅状态。held—retain only conditional diagnostics; reject any reading as a proof of RH, zero simplicity, or an effective zero detector without the missing global estimate.

### Hanna's OEIS congruence conjectures: eleven proved, three more resolved

- 来源与本机版本。其他 GitHub 作者。作者公开稿。11 页。SHA-256 为 `73050b3d880f844b2126055a3f30225e91a8fddea42ff59614ab41f93a4e4561`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/oeis-hanna/note.pdf)
- 原文位置。local PDF pp. 1–2 theorem list/scope; pp. 4–7 formal-series proofs; pp. 8–9 Lean and attribution notes
- 局部构件。Formal-power-series congruence toolkit: differentiate functional equations in F_p\[\[x\]\], use x-adic uniqueness, and exploit dyadic/additive composition recursions.
- 依赖。Sequence definitions and historical attributions come from OEIS and cited literature; the claimed Lean proofs are external, while several direct coefficient proofs are printed locally.
- 审阅状态。candidate—local elementary congruence arguments can be distilled, while OEIS identity/version and full Lean-validation claims must remain separately checked.

### Irrationality measures from Löwner determinants

- 来源与本机版本。其他 GitHub 作者。作者公开稿。73 页。SHA-256 为 `c53187157e4e46ac2f75d33e55566fa727cfc218533916337c200ffad3f19c34`。 [发布入口](https://github.com/slitsey/catalan-irrationality-measure/tree/main/paper-trigamma)
- 原文位置。Author-hosted 73-page manuscript; PDF pp. 2–16, Theorems 1.1–1.6 and determinant setup; no archival identifier stated in the local copy.
- 局部构件。Rectangular Löwner-determinant framework for rational approximants to digamma/trigamma combinations.
- 依赖。Needs exact finite-difference identities, rational shifts and frames, prime-by-prime denominator bounds, Hermite interpolation nonvanishing, and a geometry-specific logarithmic-energy decay certificate; the stated bounds are for named planes and special points only.
- 采用有限正原子 Gram 特例，保留原文复测度与插值非零性的条件。 [Löwner 差商与正原子 Gram](../../math-openai-arithmetic-determinants/references/loewner-divided-difference-audit.md)

### November addendum to Exact Zero Detection and Compact Arithmetic Realizations for the Riemann Xi Function

- 来源与本机版本。其他 GitHub 作者。作者公开稿。3 页。SHA-256 为 `29f905db5fd468064d3b6d2e807ce02fdcb867c5566bb411520a6996dc91c296`。 [发布入口](https://github.com/LeonardSEO/riemann-xi-zero-detection/blob/main/paper/addendum.pdf)
- 原文位置。Author-hosted addendum, 24 Nov 2026, PDF pp. 1–3, Theorem 1; no journal/preprint identifier stated.
- 局部构件。Conditional transfer from prime-power-window control to fixed-band Möbius energy bounds.
- 依赖。Assumes P(a), imports the one-sided interval lemma and (FB1)/(FB2)/(FB4) from the October preprint, and requires 0&lt;a&lt;b&lt;1/2 with fixed q,H,h. It proves neither P(a) nor RH.
- 审阅状态。held

### On some positivity properties of the Riemann Xi function

- 来源与本机版本。其他 GitHub 作者。v3 · 作者公开原稿。53 页。SHA-256 为 `d3cd19f47a11051eb024ca7f81e9f7c799c1e407ad076a3f3854975873fdcab4`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/riem-xi/v3/riem-xi-v3.pdf)
- 原文位置。arXiv:2611.02944v1; Sra author preprint v3 dated 2 Nov 2026; local PDF pp. 1–53, Theorems 1.1–1.3 and Appendix C certificates.
- 局部构件。Signed-perturbation and moving-frame method for finite Pólya-frequency orders of reciprocal-Xi densities.
- 依赖。Relies on published critical-line verification through the stated height, selected zero enclosures, directed Arb interval calculations, exact covers, and particular reciprocal-Xi normalization. PF_{k*} is finite; no RH proof or extension of verified zero height follows.
- 审阅状态。held

### Sharp order-four sign regularity of a Jacobi theta kernel

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。11 页。SHA-256 为 `174241481c47fe7a7228ee173d9784e68f8b2f4223ee3b83e19cfc9553bf02a0`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/csordas/v1/csordas-v1.pdf)
- 原文位置。csordas-v1.pdf, pp.1-10, Thms.1.1-1.4
- 局部构件。Wronskian-to-Hankel-minor transfer and claimed order-4 theta-kernel signs.
- 依赖。v1 preprint; compact signs and sharp failure depend on interval enclosures and Assumption 1.5; no code rerun.
- 审阅状态。hold

### Simple critical zeros in a weighted family of Dirichlet L-functions

- 来源与本机版本。其他 GitHub 作者。作者公开稿。74 页。SHA-256 为 `e68819fb5cb25397d5125d744149f0af917510f505a6287650093ba91c313614`。 [发布入口](https://github.com/nic410/dirichlet-critical-zeros/blob/main/paper/main.pdf)
- 原文位置。dirichlet-critical-zeros.pdf, pp.1-10/Table 2; 28-45; 59-67
- 局部构件。Time-integrated majorant plus weighted Farey/Toeplitz large-sieve proof architecture.
- 依赖。Author manuscript; needs stated weights, classical/cited zero-density inputs and claimed rational/Lean/interval certificates; none rerun.
- 审阅状态。hold

### Some positivity properties of Riemann Xi under smoothing

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。35 页。SHA-256 为 `f617cae40dd4b1787bd7d305b01d5ee67c1f384e747ba26105a17913369cd031`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/riem-xi-smoothing/v1/riem-xi-smoothing-v1.pdf)
- 原文位置。riem-xi-smoothing-v1.pdf, pp.1-9, Prop.2.2/Thms.2.3-4.1
- 局部构件。Exact CM criterion through positivity of the smoothed zero profile.
- 依赖。v1 preprint; prime/height improvements require explicit-formula bounds and verified-zero data; no enclosure rerun and no RH proof.
- 审阅状态。hold

### The decomposition lengths of a numerical semigroup form an interval

- 来源与本机版本。其他 GitHub 作者。作者公开稿。9 页。SHA-256 为 `528fe7e19805ae7af8a83eb6c88d437e0413b0d764c439e942ca74b1dd4299c9`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/numerical-semigroup-lengths/note.pdf)
- 原文位置。pp. 2–6, Theorems 1–2; Lemmas 2, 5–7
- 局部构件。Special-gap cover characterization plus normalizing exchange: replace a nonnormal irreducible oversemigroup by a same-Frobenius exchange and at most one repair, with a strictly decreasing integer potential; normal decompositions have r(S) parts.
- 依赖。Author GitHub preprint. Requires a numerical semigroup, irreducible oversemigroups, and the special-gap covering lemma of Rosales–García-Sánchez. The claimed Lean replay and its kernel were not independently replayed.
- 审阅状态。held

### The generalized Wilf conjecture for semigroups graded by a two-generated numerical semigroup

- 来源与本机版本。其他 GitHub 作者。作者公开稿。9 页。SHA-256 为 `089d5d3d8a6018278d981c4478cd14a551e12be6a66653b4a9556d8dc6ade787`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/graded-wilf/note.pdf)
- 原文位置。pp. 1–7, Corollary 1; Propositions 1–3
- 局部构件。Layer-counting certificate for T=⟨a,b⟩-graded generalized numerical semigroups: atoms are total-degree layers a,b, the below-gap region has degree at most F, and the full F−1 layer plus binomial inequalities prove d c(S)≤e(S)n(S).
- 依赖。Author GitHub preprint. Restricted to coprime 2≤a&lt;b, d≥1, and T-graded GNSs; uses Sylvester Frobenius/reflection and cited Cisto–Navarra/Bhardwaj–Cisto–Deshpande facts. Claimed Lean verification was not replayed.
- 审阅状态。candidate

### Z is Diophantine in Q, version 21

- 来源与本机版本。其他 GitHub 作者。v21 · 作者公开原稿。833 页。SHA-256 为 `61410502c6d71bcbd7f699a697c8ea2e7a7d9ea294c61b31225f1e37754e9d47`。 [发布入口](https://github.com/elliotglazer/diophantine-z-q/blob/main/manuscripts/quartic_v21.pdf)
- 原文位置。p. 366, Theorem 1.1; p. 367, Theorem 1.2; pp. 799–821, Appendix A33–A34
- 局部构件。Explicit finite sum-of-weighted-squares/quadratic-equation compilation purportedly preserves rational projection while producing quartic Diophantine definitions.
- 依赖。833-page v21 project manuscript. Theorem 1.1 depends on many external arithmetic/modularity/height inputs and author-specific supporting proofs; Theorem 1.2 has an explicitly ineffective N0, while N≥53 is only a coefficient threshold. This bounded review cannot certify the dependency chain.
- 审阅状态。held

### A roadmap of the claimed Lean proof of the Riemann hypothesis and GRH for Dirichlet L-functions

- 来源与本机版本。黎曼假设导读。导读。23 页。SHA-256 为 `115571f7519dc0a24d6414091fe07a0f1f090112708b5a2100e83a8e05c749bb`。 [发布入口](https://peabrane.github.io/)
- 原文位置。local PDF sha256=115571f7519dc0a24d6414091fe07a0f1f090112708b5a2100e83a8e05c749bb; pp. 1, 3–6, 15–18
- 局部构件。RH introduction/reading guide, not a proof. It maps a claimed Lean dependency chain from windowed Landau estimates through forced divisibility, slope/covolume/trace inputs to RH/Dirichlet GRH.
- 依赖。p. 1 and p. 3 explicitly say the authors did not build the development and make no correctness claim; p. 15 identifies unproved high-risk arithmetic inputs. The dependency is the massive external Lean archive, whose comparator build was still pending in the guide.
- 审阅状态。exclude from proof evidence; retain as an audit roadmap only, with RH/GRH strictly unendorsed.

### The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function

- 来源与本机版本。黎曼假设导读。v2 解释草稿。265 页。SHA-256 为 `b49de5037af55c6df66843db710332a358c4eb1d2799581c673cd2ea17e8ea40`。 [发布入口](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)
- 原文位置。local PDF sha256=b49de5037af55c6df66843db710332a358c4eb1d2799581c673cd2ea17e8ea40; pp. 1–6, 193–208, 223–261
- 局部构件。RH explanatory working draft, not an independently complete proof. It proves/reduces some analytic pieces but states that the central inequality (M) is quoted and then reduced to thirteen hypotheses.
- 依赖。pp. 1–3 and 5 state that none of the thirteen hypotheses is proved outright in the draft; they include theta-kernel integrality/divisibility, covolume, trace-formula, Galois-cohomology, map/weight, and scale inputs. The underlying Lean archive was not built or independently audited.
- 审阅状态。hold as conditional exposition; do not promote RH or distill it into a theorem tool. The explicit blocker is the unproved (M) input chain, not merely lack of prose polish.


## 图论、组合概率与离散结构

### The Aaronson–Ambainis conjecture on influences

- 来源与本机版本。Anthropic 关联。PSI publication using a non-public Anthropic model; adjacent to A28, not an Anthropic publication。60 页。SHA-256 为 `7b411d8daf83c29a4a613e8c19f3d82810deff82f413f25b8cd52285ae9ea87d`。 [发布入口](https://psi.inc/research/aaronson-ambainis/index.html)
- 原文位置。local PDF sha256=7b411d8daf83c29a4a613e8c19f3d82810deff82f413f25b8cd52285ae9ea87d; pp. 1–2, 5–14, 18
- 局部构件。Related PSI paper (not Anthropic publication): claims a polynomial influence lower bound (Theorem 1.1/Corollary 1.2) and an AI-produced Lean formalization. The readable route runs bijection theorem → determinant/antipodal/all-pairs inequalities → row bound → averaging.
- 依赖。The conclusion relies on the detailed combinatorial lemmas and the cited/linked PSI Lean repository; pp. 1–2 report kernel checking but this audit neither inspected the complete proof chain nor built the stated Lean revision.
- 审阅状态。hold as a related preprint/formalization claim; no reusable theorem skill until statement-to-source and pinned Lean replay are independently audited.

### Critical bond percolation on the integer lattice

- 来源与本机版本。Anthropic 官方。Anthropic release at pinned commit; technical guide accompanying Lean。15 页。SHA-256 为 `5540fee046a4dfff0247410630aec8d6b42c8f3c074c19e98a3b66f8f9410a75`。 [发布入口](https://github.com/anthropics/formal-math/blob/795efb86f191735c5481675763537cfb4ff37e55/percolation/README.md)
- 原文位置。local PDF sha256=5540fee046a4dfff0247410630aec8d6b42c8f3c074c19e98a3b66f8f9410a75; pp. 1–4; source commit 795efb86f191735c5481675763537cfb4ff37e55
- 局部构件。Official Anthropic formalization guide. It describes a Lean claim θ(pc)=0 for nearest-neighbour Bernoulli bond percolation on Z^d, d≥2, via additive gluing and a conditioned-slack hierarchy; it is a formalization artifact, not a conventional independently reviewed paper.
- 依赖。The stated result depends on the pinned formal-math source, Lean/Mathlib, comparator/nanoda checks, and faithful transcription of the top-level statement. p. 1 explicitly says no independent human mathematical review and warns mechanical checking does not establish semantic faithfulness.
- 审阅状态。hold; record as a major formalization candidate only. No theorem skill or factual promotion without source checkout/build, dependency review, and statement audit.

### A negative answer to a question of Carenini on almost independent sets in regular graphs

- 来源与本机版本。其他 GitHub 作者。作者公开稿。20 页。SHA-256 为 `902d56412030f1fb983d1581e264bcb0c8ed4fe3f6fbcc7236e2a7bcb1f576c2`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/carenini-almost-independent/note.pdf)
- 原文位置。local PDF pp. 1, 4, 6–10 (counterexample statements, exact threshold count, switched constructions and Cramer argument)
- 局部构件。Counts low-induced-edge vertex subsets in regular graphs to refute the K_{d,d}-union maximizer proposal; small thresholds are handled by exact subgraph enumeration and fixed gamma by large-deviation comparison.
- 依赖。The finite formula on pp. 6–7 depends on the triangle and exceptional 4/5-set counts; the asymptotic part explicitly invokes Cramer's theorem and an external entropy upper bound. The open fixed-gamma range (0,1/8\] remains open in the paper.
- 审阅状态。candidate — preprint-audited counterexample/counting route only; keep its n,d,gamma divisibility and threshold hypotheses, and do not imply the unanswered range is resolved.

### A product inequality for Walsh coefficients and two conditional Fourier entropy–influence bounds

- 来源与本机版本。其他 GitHub 作者。作者公开稿。10 页。SHA-256 为 `101196d99d383432ef15512bca0854863fa17f05a725798f85666758741ee822`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/fei-nonflat-spectra/note.pdf)
- 原文位置。local PDF pp. 1, 3–4 (conditional FEI statements and determinant/log proof); p. 8 (formalization report)
- 局部构件。Integer determinant/product lower bound for selected Walsh coefficients, converted by logarithmic averaging into FEI bounds under lower-mass or inclusion-comparability assumptions.
- 依赖。The proof on pp. 3–4 relies on the stated determinant/minor selection theorem and elementary log/layer lemmas; it is conditional on the explicit Fourier-support mass assumptions. The reported Lean build is not independently replayed here.
- 审阅状态。candidate — retain only the conditional Fourier entropy–influence lemma with its support and mass hypotheses; do not claim the general FEI conjecture or a verified formal certificate.

### Answers to three problems of Hak, Kozerenko and Oliynyk on the triameter of graphs

- 来源与本机版本。其他 GitHub 作者。作者公开稿。13 页。SHA-256 为 `a6357d250a51afa65a5d4e642358e048c2247292647bb58e5f2497c79cf5cb79`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/hko-triameter/note.pdf)
- 原文位置。local PDF pp. 1–3: Abstract, Theorems A–C and literature-scope statement; subsequent sections give proofs
- 局部构件。Small finite graph counterexample/minimality workflow: enumerate labelled graphs, certify median/distance-hereditary predicates and triameter witnesses, then reduce the structural alternative.
- 依赖。Uses prior definitions/results of Hak–Kozerenko–Oliynyk and Bandelt–Mulder; claims Lean verification but the Lean sources are external to the PDF.
- 审阅状态。candidate—finite graph mechanism and stated scope are explicit; literature priority and kernel check need independent source/repository verification.

### Arbitrarily large antichains of trees of equal order in the independence polynomial order

- 来源与本机版本。其他 GitHub 作者。作者公开稿。10 页。SHA-256 为 `090da46a2500847c9bb51995ad7e33c31f1aab1dd1f2633af519361e28a5c4aa`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/tree-antichains/note.pdf)
- 原文位置。local PDF pp. 1–3: Abstract and Theorem 1; §3 begins decorated-path polynomial proof
- 局部构件。Decorated-path antichain construction: compare gadget substitutions at two negative evaluation points while locating both points in each tree’s root interval.
- 依赖。Order is the Beaton–Cameron/Csikvári independence-polynomial order; any claimed formalization and cited comparison facts are external to the local PDF.
- 审阅状态。candidate—construction and quantifier n≥11 are stated and proof route is local; retain cited order theory as an explicit dependency.

### Connected cographs with distance eigenvalues just below −2

- 来源与本机版本。其他 GitHub 作者。作者公开稿。4 页。SHA-256 为 `6936a2a60b103c3ffad02d80b7a3ab5d0746abab5d943f2eb75a05af9aded699`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/cograph-distance/note.pdf)
- 原文位置。local PDF pp. 1–3: Theorem 1, graph-distance lemma, cubic-root proof and Lean artefact description
- 局部构件。Equitable-partition/small-quotient spectral construction: reduce the distance matrix of K1∨(K1∪mK2) to a cubic and bracket its smallest root.
- 依赖。Question attribution uses Lou–Lin and Manna–Mandal–Tura; the claimed Lean 4 check is external ai4math-results v1.18.0/Mathlib v4.34.1.
- 审阅状态。candidate—compact explicit construction with elementary local proof; formal verification claim still requires the hosted project.

### Critical graphs with the fewest cycles of length 0 modulo k

- 来源与本机版本。其他 GitHub 作者。作者公开稿。13 页。SHA-256 为 `6485685e4afb9b06f4688fa1dc11f34dedd9ab5f96ed41491995551a5407d53b`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/critical-cycles-mod-k/note.pdf)
- 原文位置。local PDF pp. 1–4: abstract, equality setup, Lemmas 2–4; pp. 5–10 case machinery
- 局部构件。Equality-rigidity analysis for critical graphs: inject counted cycles through colorings, force every counted multiple-of-k cycle to have length k, then exclude degree/cycle configurations.
- 依赖。Imports Choi–Sieniawski counting, Kim–Picollelli constructions, and Gao–Huo–Liu–Ma arithmetic-progression paths; Lean verification is claimed but source files are external.
- 审阅状态。candidate—proof architecture is explicit, but the imported graph theorems remain mandatory dependencies.

### Fourteen new weights of the Reed–Muller code RM(7,14)

- 来源与本机版本。其他 GitHub 作者。作者公开稿。13 页。SHA-256 为 `e6ff49669127853f9c7817f1131e05e5b3125f10845552e17e8b6e0e8aa0191e`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/rm714-weights/note.pdf)
- 原文位置。local PDF pp. 1, 4–5: theorem scope and explicit codewords/finite witnesses; pp. 8–9: Lean statement/check description
- 局部构件。Finite codeword witness workflow: encode low-degree Boolean polynomials, compute Hamming weights via elementary symmetric sums, and kernel-check a finite JSON witness set.
- 依赖。The asserted full witness list (7,901 objects, SHA prefix given) and Lean modules live in external ai4math-results v1.4.0; cited Lou–Wang statements are also used for the middle-interval reduction.
- 审阅状态。held—individual explicit examples are local, but broad weight-set claims require the absent witness corpus and Lean replay.

### Maximal energy of integral circulant graphs of order p^a q^b when one prime is 3 or one exponent is at most 2: the orders p^(2r)·3^(2s+1), pq^m and p²q^b; for exponents of equal parity, every order p^a q^b with min(a,b) ≤ 2, and every order in which one of the primes is 3

- 来源与本机版本。其他 GitHub 作者。作者公开稿。33 页。SHA-256 为 `84620c31de933ee0dd8ba6efffe042a60ec1cd8901e178f08bb87446aa1f78b0`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/icg-q3-general/note.pdf)
- 原文位置。Author-hosted manuscript v3, 9 Nov 2026, PDF pp. 1–33; no journal/preprint identifier stated.
- 局部构件。Weighted-Ramanujan-transform sign-matrix/potential proof for restricted integral-circulant energy maximizers.
- 依赖。Only covers two odd primes in the listed exponent/parity ranges; uses Jiang–Yang's conditional reduction and explicit divisor-set/transform conventions. The withdrawn v1.5 computer-assisted range is explicitly not a formal proof.
- 审阅状态。held

### Multisets of bars that do not tile a 2 × n rectangle: the optimal growth order

- 来源与本机版本。其他 GitHub 作者。作者公开稿。10 页。SHA-256 为 `d7f50c9bd23a6b583397fc9a7b5f32fcbd4c33b15976c4860d6b2bf83507930b`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/bar-tiling-defect/note.pdf)
- 原文位置。Author-hosted manuscript, 22 Nov 2026, PDF pp. 1–10, main theorem and Lean discussion; no journal/preprint identifier stated.
- 局部构件。Two-row tileability criterion with bounded Bézout counting for defective bar multisets.
- 依赖。Counts only 1×ℓ bars with ℓ≤k and the paper's multiset/rotation convention for a 2×n rectangle; the Θ(n^e) claim depends on the stated congruence subsequences and formalization bundle.
- 审阅状态。held

### Tensor products of Mycielskians of odd cycles with odd wheels and with extended Mycielskians of odd cycles are not word-representable

- 来源与本机版本。其他 GitHub 作者。作者公开稿。9 页。SHA-256 为 `8e76ce77af955bc6674149c8733a2d856f70ab771c6a8f385404f3bd19094f39`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/wordrep-tensor/note.pdf)
- 原文位置。10_wordrep-tensor.pdf, pp.1-8, Thms.1-3
- 局部构件。Induced-subgraph obstruction embeddings for the indicated tensor products.
- 依赖。Author v2; depends on known non-word-representability including Alshammari arXiv:2609.20881v1; embeddings not rerun.
- 审阅状态。hold

### The Macdonald (q,t)-permanent II: Probability laws and their regions of validity

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。27 页。SHA-256 为 `88917e9bf6c910b3203b08a81c956d0fcd682ff6e969cfb1d152163f24d9dbe1`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/macperm2/v1/macperm2-v1.pdf)
- 原文位置。macperm2-v1.pdf, pp.1-18, Thms.4.1-5.8
- 局部构件。Cycle-weighted scalar/matrix law regions and special realizations.
- 依赖。v1 preprint; matrix claims use CM derivative criteria and Wishart/Schur/Okounkov; some regions conjectural.
- 审阅状态。hold

### The equality case of Chen's bound for invariant parking with one special preference

- 来源与本机版本。其他 GitHub 作者。作者公开稿。11 页。SHA-256 为 `44988b0c7471819b7c884a320f0296b75c5a472684b4299ceccb59a3c87ab1c8`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/variable-length-parking/note.pdf)
- 原文位置。pp. 2–6, Theorems 1–2; Lemmas 1, 6–10
- 局部构件。Parking-gap residual recursion reduces one-special-preference invariance to subset sums; for a superdecreasing tail, extremality is equivalent to symmetry of a translated subset-sum prefix, and ruler-word/palindromic-prefix counting gives the first-length count.
- 依赖。Author GitHub preprint. Requires Chen's ordered positive-length parking model and a superdecreasing tail for the classification/count; imports Chen arXiv:2311.15699v1 and Chen et al. ECA 2024. Claimed Lean verification was not replayed.
- 审阅状态。held

### The largest domination roots of friendship graphs and of joins with repeated petals

- 来源与本机版本。其他 GitHub 作者。作者公开稿。11 页。SHA-256 为 `e0e58ebd36a299e344320071c0ae536a74ee7ca743320ecb480ba8f4fa544932`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/domination-root-radius/note.pdf)
- 原文位置。pp. 1, 4–6, Theorem 2 and Propositions 1–2
- 局部构件。For J_m=K_a∨mB, normalize the domination-root equation Q(1/y)^m=1−y^a; combine a loss/upper bound with a logarithmic local analytic zero argument to obtain the root-radius scale (cs m/(a log m))^(1/c).
- 依赖。Author public draft. Requires fixed nonempty B, c=1+δ(B), s equal to the number of distinct minimum closed neighborhoods, and the stated branch/log estimates; it uses standard join domination-polynomial identities. Claimed Lean build was not replayed.
- 审阅状态。candidate

### The maximum Manhattan length of a path through all lattice points of a box

- 来源与本机版本。其他 GitHub 作者。作者公开稿。10 页。SHA-256 为 `634bbf691adc91458f25e575111c9de05a983a27ccc4d0c2c325246aa6506006`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/lattice-box-paths/note.pdf)
- 原文位置。pp. 1–3, Theorem 1; pp. 5–7, Lemma 1, Proposition 1, Lemmas 2–4
- 局部构件。Centered-coordinate loss identity for Manhattan Hamiltonian orderings, followed by supported-ordering inflation from parity seeds; this reduces the optimum to mandatory endpoint cost plus sign-pattern loss.
- 依赖。Author public draft. Exact formula concerns finite integer boxes with unit-axis restoration and explicit small seeds; claimed Lean repository artifacts were not replayed. Yuan's coordinatewise upper bound is an external input.
- 审阅状态。candidate

### The minimum order of a counterexample to a conjecture on integral generalized sun graphs

- 来源与本机版本。其他 GitHub 作者。作者公开稿。18 页。SHA-256 为 `40208497f595e0d75f36cebdf860f96958aacb99bf965c3b269f7a7cb9b85fe2`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/sun-graphs/note.pdf)
- 原文位置。pp. 1–3, Theorems 1–2; pp. 4–7 spectral lemmas; pp. 9–12 finite classification
- 局部构件。Spectral-window reduction for integral unicyclic/generalized-sun graphs: Schur-complement inertias, trace moments, and modular characteristic-polynomial tests prune a finite parameter search.
- 依赖。Author public draft. The minimum-order assertion relies on source-specific claimed Lean finite enumeration/classification and Braga–Moraes–Santos reduction to P1/P2; neither was replayed or independently audited here.
- 审阅状态。held

### The switching conjecture for main eigenvalues holds for trees of diameter at most 4

- 来源与本机版本。其他 GitHub 作者。作者公开稿。17 页。SHA-256 为 `376072720e813cbb0ada3d9e20c9a6e5910a4de72049f77403f879b8774c2a54`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/switching-diam4/note.pdf)
- 原文位置。pp. 1–3, Theorem 1 and scope; pp. 4–11, Lemmas 2.2–5.4 and proof
- 局部构件。Krylov-rank (including mod-p sufficient) certificate for all eigenvalues being main, coupled to secular-polynomial/orbit decomposition for radius-2 trees and constrained leaf-sign selection.
- 依赖。Author public draft. Restricted to trees of diameter at most 4, excluding K2; completion uses source-specific finite small-branch case enumeration claimed Lean-checked but not replayed. General tree and regular-graph conjectures remain open.
- 审阅状态。candidate

### The unfair 0–1 polynomial conjecture for trinomial factors

- 来源与本机版本。其他 GitHub 作者。v2，2026-11-20。8 页。SHA-256 为 `62e2bdedb2d26c5376e6e4cf840c326308a6005df40e9e2bcd0e301ac335d72c`。 [发布入口](https://github.com/esonde/unfair-polynomials-conjecture)
- 原文位置。pp. 1–5, Theorem 1; Lemmas 2–3; Proposition 4
- 局部构件。Widest-strip contradiction for a coefficient-array recurrence: four forced binary rows plus an ℓ¹ Fourier-kernel bound exclude 0&lt;a&lt;1 when AB is binary and one factor is a trinomial.
- 依赖。v2 preprint, hexagon:2611.00674v2. Requires an algebraic conjugate \|λ\|&gt;1, a finite-support coefficient recurrence, and the Appendix-A Fourier estimate; Ghidelli/Dvorsky are used only for earlier cases.
- 审阅状态。candidate


## 代数、半群与对称函数

### A Koteljanskii inequality for permanents

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。9 页。SHA-256 为 `783c4168003ca8ba2325f17e3b6eb1a56c5058cff63e73835978d670a94ae484`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/perm-m-matrix/v1/perm-m-matrix-v1.pdf)
- 原文位置。local PDF pp. 1–4 (Theorem 1.1, Proposition 2.2, Lemma 2.3); pp. 5–6 (counterexample and scope)
- 局部构件。For a positive-diagonally symmetrizable inverse M-matrix, convert principal permanents into complex-Gaussian squared-modulus moments, prove the density MTP2, then obtain log-supermodularity by tilted FKG.
- 依赖。The proof page explicitly depends on the Gaussian permanent-moment representation, Ginibre correlation inequality for the Ising expansion, and Karlin–Rinott FKG for MTP2 densities; it excludes nonsymmetrizable inverse M-matrices by its own counterexample.
- 审阅状态。candidate — preprint-audited MTP2/tilting template, usable only with the symmetry, inverse-M, positivity, and finite-moment hypotheses retained.

### A Proof of McLeod's 1959 Conjecture on Complete Homogeneous Symmetric Ratios

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。11 页。SHA-256 为 `797790ddf9082e835141137c1fbeb6d3f7b977066a9c64cb1208afe5bf83de75`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/mcleod-hk/v1/mcleod-hk-v1.pdf)
- 原文位置。local PDF pp. 1–2 (Theorem 1.1 and strategy); pp. 3–5 (queueing and tensorization proof); p. 6 (power extension)
- 局部构件。Convexity/subadditivity of (h_{ell+r}/h_ell)^(1/r) through a closed-queue throughput representation for h_{k-1}/h_k and an auxiliary-variable tensorization curvature coupling.
- 依赖。The proof uses the closed Gordon–Newell queue stationary/throughput formula and standard finite-state ergodic facts (Appendix A), then the paper's tensorization/Hessian limiting argument; no external publication status is asserted by the local v1.
- 审阅状态。candidate — preprint-audited symmetric-polynomial/queueing technique; keep x in R_+^n, ell&gt;=0, r&gt;=1 and the stated homogeneous-ratio normalization.

### A new proof of van der Waerden's inequality, and beyond

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。31 页。SHA-256 为 `847c0df5f3dfaa5a6a87bb8c226ee0ec77ba0341d98d51ea3ab48d0ee9b247ed`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/gurvits-lower/v1/gurvits-lower-v1.pdf)
- 原文位置。local PDF pp. 1, 5–7 (permanent theorem, pair averaging and completion); pp. 11–12 (Lorentzian extension/remainder)
- 局部构件。Monotone pair-averaging of a maximum-entropy correlation functional, obtaining van der Waerden and partial-matching bounds from a quadratic Alexandrov–Fenchel cofactor inequality.
- 依赖。The local proof uses Gibbs parameters/entropy duality and the quadratic Alexandrov–Fenchel inequality; the Lorentzian generalization assumes the corresponding contraction inequality. Published classical theorem names in the text are inputs, not re-proved here.
- 审阅状态。candidate — preprint-audited entropy/averaging framework, conditional on the precise Alexandrov–Fenchel or Lorentzian hypothesis and not a replacement for those inputs.

### A sharp Brégman–Minc bound for permanents

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。12 页。SHA-256 为 `1610d9f183733a5c3b37c6b29622b38dcf7ea9e933819b3b917f52da2fee57b1`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/gurvits/v1/gurvits-v1.pdf)
- 原文位置。local PDF pp. 1–3 (Theorem 1.1 and scalar Gamma lemma); pp. 7–8 (simplex completion and permanent/equality argument)
- 局部构件。Sharp permanent bound for entrywise phi(A), phi(x)=Gamma(1+1/x)^(-x), via a scalar simplex inequality then Hölder separation of normalized minors; yields an Orlicz row-norm corollary.
- 依赖。The proof derives its scalar representation from Weierstrass's Gamma product and Tonelli, then uses the paper's simplex inequality and Hölder induction. Its equality characterization assumes the stated row-stochastic, square, nonnegative setting.
- 审阅状态。candidate — preprint-audited permanent/Gamma-function module; preserve phi's exact normalization and all row-stochastic/nonnegative hypotheses.

### A simple primitive axial algebra with a disconnected non-annihilation graph, and a decomposable axial block

- 来源与本机版本。其他 GitHub 作者。作者公开稿。11 页。SHA-256 为 `6e02d61590ee5b2efe3a3325f0bae35c3a6b5f4c86ec24232028be96a518f304`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/axial-nonannihilation/note.pdf)
- 原文位置。local PDF pp. 1, 4–5 (definitions, explicit multiplication/eigenbasis, simplicity and graph computation)
- 局部构件。A four-dimensional rational algebra claimed to be a simple primitive axial algebra for an enlarged Jordan-type fusion law while its chosen-axis non-annihilation graph is disconnected.
- 依赖。The argument computes eigenvectors/fusion products and proves simplicity by explicit linear-function separation; applicability to the named conjectures depends on the precise axial-algebra/fusion-law conventions cited in the paper, which were not independently checked.
- 审阅状态。held — finite example is plausible but unrefereed and convention-sensitive; require an independent multiplication-table/fusion verification before using it as a counterexample.

### A terrace for the alternating group `A_7`

- 来源与本机版本。其他 GitHub 作者。作者公开稿。9 页。SHA-256 为 `665e1e254dcd6bd7bf911b953e2b374f1fc3ad18f5b6f6c8e13195aa7b537ea0`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/a7-terrace/note.pdf)
- 原文位置。local PDF pp. 1, 5 (explicit encoded terrace and proof of Theorem 1); p. 4 (published consequences)
- 局部构件。Encoded 2520-term arrangement for A_7; an injective row encoding and a quotient-edge matching are intended to certify the terrace condition.
- 依赖。Theorem 1 reduces the claim to finite assertions (R1), (R2), and (S) about the supplied data; its wider symmetric-sequencing consequences import Anderson–Ihrig and survey results. The actual 2520-row data/certificate was not independently replayed.
- 审阅状态。held — finite computational certificate only; require the data file, parser and independent exact replay before treating A_7 as verified.

### An axial algebra whose automorphism group does not preserve its Frobenius form: an answer to a question of Shpectorov

- 来源与本机版本。其他 GitHub 作者。作者公开稿。6 页。SHA-256 为 `fb6d86171badb285190f775523cbcc00424f8e87b17e2c54ab95917382516329`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/axial-frobenius/note.pdf)
- 原文位置。local PDF pp. 2–5: Theorem 1; coordinate proof; Lean statement/module map
- 局部构件。Finite-field structure-constant audit: diagonalize each multiplication map, verify fusion products and Frobenius identities, then check a signed automorphism.
- 依赖。Works over F_11 and uses the definitions/question attributed to Gorshkov–Shpectorov; kernel check is asserted for external ai4math-results v1.20.0, Mathlib v4.34.1 (commit d13f23b7), not bundled in the PDF.
- 审阅状态。candidate—finite explicit algebra component only; theorem claim remains dependent on the separately hosted Lean artefact.

### Complete mappings of the Brauer and partial Brauer monoids

- 来源与本机版本。其他 GitHub 作者。作者公开稿。16 页。SHA-256 为 `35bc80dc9ec4051a1511c0ce9a0e86af7fe6efef1ae1a1b8dff586bbc0574979`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/brauer-complete-mappings/note.pdf)
- 原文位置。local PDF pp. 1–4: abstract, Theorem 1.1 and reduction table; pp. 5–8: Rees coordinates and construction
- 局部构件。Rees 0-matrix complete-mapping construction using half-diagrams, parity of the index set, and a complete mapping on the maximal subgroup.
- 依赖。Uses Araújo–Bentz–Cameron–Hendrey–Kinyon principal-factor reduction and Hall–Paige; Lean verification is asserted in §9 but not bundled.
- 审阅状态。candidate—explicit finite-semigroup construction is auditable in the text, with external reduction/formalization dependencies retained.

### Inverse Problem in Difference Galois Theory

- 来源与本机版本。其他 GitHub 作者。作者公开稿。14 页。SHA-256 为 `945652e0952b6f59f6372d83e3f8cd9c8e9e0d020a4ffcd24ac84b44a6747d37`。 [发布入口](https://mechmath.github.io/publication/inverse-galois/)
- 原文位置。arXiv:2611.11397 (author preprint, 8 Nov 2026); local PDF pp. 2–13, Theorems 1.1, 2.8 and construction.
- 局部构件。Shift-difference Picard–Vessiot realization via a coefficient-group rigidity criterion.
- 依赖。Requires K=C(x), σ(x)=x+1, C algebraically closed of characteristic 0, an embedded closed G≤GL_n(C) with cyclic G/G°, van der Put–Singer coefficient-group results, and the manuscript's singularity/semisimple-limit construction.
- 审阅状态。held

### Irreducibility Testing of Sparse Polynomials over Integers is NP-hard and Probabilistic Polynomial Time

- 来源与本机版本。其他 GitHub 作者。作者公开稿。18 页。SHA-256 为 `1ad33a8a38ac0e351a29753ff2961ba5f2f87d8e14e717a1751096599b582ce1`。 [发布入口](https://mechmath.github.io/publication/sparse-irr/)
- 原文位置。arXiv:2610.37179v1 (27 Oct 2026); local PDF pp. 3–13, Theorems 2/4/10 and Appendix A.
- 局部构件。Sparse-polynomial irreducibility reduction and modular-root majority test.
- 依赖。Hardness uses the displayed 3-CNF-to-gap-polynomial construction; PP/PSPACE upper bound additionally depends on Cureton–Thorner's zero-free theorem and Frei–Sofos–Widmer's effective prime-ideal estimate, plus the stated sparse encoding and cutoff analysis.
- 审阅状态。held

### Medial racks and quandles of prime order: a proof of a conjecture of Vojtěchovský and Yang

- 来源与本机版本。其他 GitHub 作者。作者公开稿。10 页。SHA-256 为 `f957e18c52d09b7cabea84f1e1ea36e4bd7e6e0225373d85bdf8de6372ebe36d`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/prime-medial-racks/note.pdf)
- 原文位置。Author-hosted manuscript, 22 Nov 2026, PDF pp. 1–7, Theorems 1–2 and Lean discussion; no journal/preprint identifier stated.
- 局部构件。Prime-order medial-rack classification through displacement groups and affine quandles.
- 依赖。Requires prime cardinality, medial and rack axioms, and the non-2-reductive branch; the claimed Lean statements need the referenced source files. It neither classifies composite orders nor arbitrary racks.
- 审阅状态。held

### Monotonicity of Turán-ratios of symmetric polynomials

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。10 页。SHA-256 为 `9726933164c82aabc3a86746ef776517e25622b0ef450d0d1adfd4930ae771ed`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/sym-turan/v1/sym-turan-v1.pdf)
- 原文位置。Sra author preprint v1; local PDF pp. 1–10, Theorem 1.1 and the one-row/Meixner proof; no archival identifier stated in the local copy.
- 局部构件。Schur specialization Turán-ratio monotonicity, including a Meixner-zero argument for one-row shapes.
- 依赖。Needs a Schur polynomial with λ padded to n parts, S_{λ,i}=s_λ(1^{n-i},x^i), x&gt;1, and λ_1&gt;λ_n; the Macdonald assertion at the end is conjectural, not a reusable theorem.
- 审阅状态。held

### On a Rank Nullstellensatz Conjecture for Noncommutative Polynomials

- 来源与本机版本。其他 GitHub 作者。作者公开稿。3 页。SHA-256 为 `655ba7c070fca1775a2682d11497aa462ae5391fbd2c0649271570ff6356ddc7`。 [发布入口](https://mechmath.github.io/publication/rank-nullstellensatz/)
- 原文位置。Author-hosted manuscript; local PDF pp. 1–3, Theorems 2.1–2.2; no journal/preprint identifier stated.
- 局部构件。Homogeneous-generator reduction of a rank inequality to two-sided ideal membership.
- 依赖。Needs an algebraically closed characteristic-zero field and homogeneous f_i; the forward implication relies on the Salomon–Shalit–Shamovich homogeneous Nullstellensatz. The manuscript's counterexample blocks extension to nonhomogeneous generators.
- 审阅状态。held

### On majorization inequalities for normalized Jack and Macdonald polynomials

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。20 页。SHA-256 为 `1c1c128f84ce4c0f7f769988c74f25d8da87d486601aef7c66bec9043c4f92c6`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/jackratio/v1/jackratio-v1.pdf)
- 原文位置。Sra author preprint v1; local PDF pp. 1–20, Theorems 1.1–1.2 and Certificate 4.2; no archival identifier stated in the local copy.
- 局部构件。Positive Gelfand–Tsetlin/Dixon–Anderson route for normalized Jack majorization and limited finite-q Macdonald checks.
- 依赖。Jack theorem needs α&gt;0, positive x, equal-size partitions and dominance; Macdonald results are only n=2, selected covers for t≤q, and n=3 with \|λ\|≤8 via exact Bernstein certificates. General finite-q majorization remains open.
- 审阅状态。held

### On the asymptotic Makar-Limanov rank conjecture

- 来源与本机版本。其他 GitHub 作者。作者公开稿。22 页。SHA-256 为 `344713e4b8c4d473adfa429b2a9da2b47b36dfc1e0a560538bd05540c54d0f60`。 [发布入口](https://mechmath.github.io/publication/asymptotic-makar-limanov-rank/)
- 原文位置。arXiv:2610.06800v2 (6 Oct 2026); local PDF pp. 2–21, Theorem 1 and Propositions 10/12/Lemma 13.
- 局部构件。Two-derivation symbol-algebra approximation followed by Taylor/normal-order matrix compression and descent.
- 依赖。Needs k algebraically closed of characteristic 0 and a nonconstant free polynomial; it proves only inf_n r_f(n)/n=0. The construction depends on field extensions, finite-precision residual improvement, and the claimed Lean formalization, not a finite zero or uniform-size bound.
- 审阅状态。held

### On the rank of groups of equivariant permutations: a counterexample to an upper bound

- 来源与本机版本。其他 GitHub 作者。作者公开稿。9 页。SHA-256 为 `656bff9b63341f13484351183dcedad409c8cfec0c6501dc53942fe7d5abe692`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/equivariant-rank/note.pdf)
- 原文位置。14_equivariant-rank.pdf, pp.1-7, Thms.1-3
- 局部构件。C2 and cyclic finite-G-set counterexamples to proposed rank bounds.
- 依赖。Author manuscript; target journal DOI 10.1007/s00233-026-10690-y/arXiv:2607.04053v1; reported Lean not built.
- 审阅状态。hold

### The q-Foulkes problem I: A fusion inequality for Macdonald plethysms

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。20 页。SHA-256 为 `02b122b396de6202bb7e74d56ca43e1c057f6cf2a921c2d8645e68e95cae158f`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/qfoulkes1/v1/qfoulkes1-v1.pdf)
- 原文位置。qfoulkes1-v1.pdf, pp.1-3, Thm.1.2; §§2-4
- 局部构件。Fusion-defect quotient claimed Schur-positive.
- 依赖。v1 preprint; depends on Haiman and Feigin-Loktev/Khoroshkin-Makedonskyi; distorted comparison is not the original conjecture.
- 审阅状态。hold

### The q-Foulkes problem II: Schur positivity with high probability

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。32 页。SHA-256 为 `c737854d2233d148aa35c8f8de8bfd9ac32d73bc05744b814db432775aee20af`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/qfoulkes2/v1/qfoulkes2-v1.pdf)
- 原文位置。qfoulkes2-v1.pdf, pp.1-4, Thm.1.2/Props.2.2-2.3
- 局部构件。Plancherel conditional-degree-law reformulation and weighted high-probability sign bound.
- 依赖。v1 preprint; requires regular modules/wreath induction and concentration estimates; no coefficientwise positivity result.
- 审阅状态。hold

### The q-Foulkes problem III: On Foulkes' conjecture with a graded inner factor

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。18 页。SHA-256 为 `5d863372629ad01fab62be2322fb4df03c8e7843583ebf675b7df77765fa4eb5`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/qfoulkes3/v1/qfoulkes3-v1.pdf)
- 原文位置。qfoulkes3-v1.pdf, pp.1-4, Thms.1.2-1.3
- 局部构件。Conditional graded lift and claimed b&gt;=(a-1)^2 canonical-map threshold.
- 依赖。v1 preprint; full graded conjecture remains conditional/open; prior threshold cited to OpenAI 2026.
- 审阅状态。hold

### The Macdonald (q,t)-permanent I: Algebra and positivity

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。28 页。SHA-256 为 `1b439b04ac1cfeae5e784bace2bae7c59c52ecd5136179ead702e2a262c13da6`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/macperm1/v1/macperm1-v1.pdf)
- 原文位置。macperm1-v1.pdf, pp.1-14, Thms.1.1-4.9
- 局部构件。Hook-content/immanant route from PSD kernels to coefficient signs.
- 依赖。v1 preprint; uses Macdonald identities, immanant positivity, Haar/Gaussian arguments; no calculations rerun.
- 审阅状态。hold

### The integer group determinants of the Heisenberg group of order 125

- 来源与本机版本。其他 GitHub 作者。作者公开稿。13 页。SHA-256 为 `69dabd5c8da57f112c9f5e712f00a3cc2765a18f0a1b628c3964310f663b8396`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/heisenberg-125-determinants/note.pdf)
- 原文位置。pp. 1–7, Theorem 1; Proposition 1; Propositions 3–5
- 局部构件。Cyclotomic ray-factorization and a 5-adic layer test for H_5 group determinants: a lower valuation bound together with a visible-prime obstruction/construction split.
- 依赖。Author public draft. Imports Mossinghoff–Pinner factorization/congruences and Panraksa seed elements; claimed Lean formalization was not locally replayed, and the visible-prime criterion is specific to Z\[ζ_5\].
- 审阅状态。held


## 矩阵不等式、算子与分析

### A Dimension-Independent Commutator Bound

- 来源与本机版本。其他 GitHub 作者。作者公开稿。29 页。SHA-256 为 `5e142fbf0cc1f7dfb6643c8f4d6360669c5aa8d93c9187f280f8062c28cf5eed`。 [发布入口](https://mechmath.github.io/publication/com-bound/)
- 原文位置。local PDF pp. 2, 16–17 (Theorem 1.1 and induction closure); pp. 10–15 (compression construction)
- 局部构件。Finite-dimensional trace-zero commutator assembly: split by a rotated-Hermitian trace-norm test, then either build an identity block or recursively assemble equal-rank small-norm trace-zero compressions.
- 依赖。The actual induction invokes Marcus–Spielman–Srivastava vector selection in Lemma 3.8/Proposition 3.9, plus the paper's block Sylvester and assembly estimates; the Lean declarations on pp. 23–27 are not a substitute for independently checking those analytic inputs.
- 审阅状态。held — unrefereed author manuscript; retain the route as a candidate research lead only, not as a certified uniform-bound module.

### A Proof of Petz's Conjecture on the Scalar Curvature of the Kubo–Mori Metric

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。17 页。SHA-256 为 `182c41808adecbbb57c1d1b7a2d25b4ceaa495375df0ec9673bb553caf442da9`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/kubo-metric/v1/kubo-metric-v1.pdf)
- 原文位置。local PDF pp. 2, 7–12 (Theorem 1.1, Stieltjes representation and completion); pp. 13–17 (boundary-sign inequalities)
- 局部构件。Strict concavity of Dittmann's three-variable function by proving that the reciprocal homogeneous quantity restricts to a Stieltjes function along every positive ray, then applying Cauchy–Schwarz and homogeneity.
- 依赖。The passage from strict concavity to the scalar-curvature statement explicitly imports Dittmann's Theorem 3. The Stieltjes step depends on the manuscript's slit-plane continuation/keyhole reconstruction and a real-variable boundary-sign calculation, all on the stated positive cone.
- 审阅状态。candidate — preprint-audited concavity/Stieltjes method only; Petz's global conclusion remains conditional on the cited Dittmann reduction and independent checking of the long sign computation.

### A Spectral Blakley–Roy Inequality for Nonnegative Matrices

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。10 页。SHA-256 为 `2421188766a358079a059dc7aa1a57fe5b4e539a32c4d7f2d3e8d04451be823a`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/pourya-rho/v1/pourya-rho-v1.pdf)
- 原文位置。local PDF pp. 1–5 (Theorems 1.1–1.2, entropy proof and spectral-radius passage); pp. 6–7 (equality/scope)
- 局部构件。Odd-power path inequality for nonnegative symmetric matrices: compare the Gibbs law of a short weighted path with a backtracking long-path trial law, whose KL remainders give the estimate.
- 依赖。The proof explicitly uses the Gibbs variational principle/KL nonnegativity, endpoint entropy identities and Gelfand's formula; even exponents use a separate standard lemma. Entrywise nonnegativity and symmetry are essential, as the manuscript's counterexamples note.
- 审阅状态。candidate — preprint-audited entropy-on-paths inequality template, restricted to its stated matrix positivity/symmetry and parity conditions.

### A Uniform Commutator Bound in Finite Von Neumann Algebras

- 来源与本机版本。其他 GitHub 作者。作者公开稿。23 页。SHA-256 为 `d7531760c01c791767e436c45998ef69733fe883203b2e88431bf06d9ca71b01`。 [发布入口](https://mechmath.github.io/publication/uni-com-bound/)
- 原文位置。local PDF pp. 1, 10, 17–21 (main assertion, factor construction, assembly tree, central decomposition)
- 局部构件。Proposed extension of a finite-dimensional uniform commutator bound to finite von Neumann algebras by high/low L2 splitting, recursively assembled corners, and measurable selection in central decompositions.
- 依赖。The matrix base case is explicitly imported from reference \[8\], the II_1 construction uses projection comparison/diffuse factor facts, and the general step uses Jankov–von Neumann uniformization plus separable reduction. Its key finite-dimensional source is itself only an author manuscript in this corpus.
- 审阅状态。held — preprint argument with layered unpublished/external dependencies; do not promote the uniform finite-von-Neumann claim to a tool theorem.

### An Explicit Polynomial Counterexample to Connes' Embedding Conjecture

- 来源与本机版本。其他 GitHub 作者。作者公开稿。46 页。SHA-256 为 `558861199f720a2f810ae9711ec6c75bd38b201a2f8d4c984b89b5a57695426a`。 [发布入口](https://mechmath.github.io/publication/poly-connes/)
- 原文位置。local PDF pp. 1–2 (Theorem 1.1); pp. 17–21, 36 (quantitative reconstruction and claimed conclusion); pp. 39–44 (encoding)
- 局部构件。Explicit noncommutative polynomial separation claim: positive normalized trace on every selfadjoint contraction matrix tuple but a negative group-von-Neumann evaluation, via stability/reconstruction estimates and word encoding.
- 依赖。The proof page chain invokes Alekseev–Liu–Thom reconstruction, operator-algebra functional-calculus and spectral-gap inputs, plus a detailed finite group/word construction. The cited facts and long numerical-constant chain were read but not independently certified in this audit.
- 审阅状态。held — extraordinary unrefereed claim with deep external dependencies; no Connes-embedding counterexample or reusable separation theorem is accepted pending full independent verification.

### Beyond Small Balls: A Determinant Inequality for Functions of Matrix Gaussian Series

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。30 页。SHA-256 为 `eaab9688ec2cf012277a08e90523d4e630e03007356ecbb76c6140afe7e7229f`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/gsd/v1/gsd-v1.pdf)
- 原文位置。local PDF pp. 1–3: Theorems 2.1–2.2; pp. 4–10 moment, localization, and main proof
- 局部构件。Penalty-form determinant comparison for a symmetric matrix Gaussian series, reducing even log-concave functions to scalar hinge inequalities plus localization.
- 依赖。Critical matrix-weighted Poincaré input is attributed to Cordero-Erausquin and an Akbas–Sra 2026b lemma; numerical/interval checks in appendices are required for κ=13/5.
- 审阅状态。held—proof chain has substantial external analytic and computer-checked ingredients; do not promote κ=13/5 as independently audited from this PDF.

### Lower bounds for the quantum permanent

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。30 页。SHA-256 为 `40b6a12ec9ad207cd9ca753a46c81a768ed87ca72cd7ccb5ffc7047eb65e308a`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/qperm-lower/v1/qperm-lower-v1.pdf)
- 原文位置。Sra author preprint v1, released 24 Oct 2026; Hexagon:2610.00719v1; local PDF pp. 1–30.
- 局部构件。Orbital-polynomial reduction of quantum-permanent bounds to partition-distribution linear constraints.
- 依赖。Applies to positive bistochastic maps H:M_n(C)→M_n(C); lower bounds use mixed-discriminant normalization, orbital identities, and the manuscript's positivity constraints. The asymptotic statement depends on its first-negative dimension d* and is not a sign theorem for arbitrary positive maps.
- 审阅状态。held

### On Lin's Arithmetic–Geometric Means Conjecture for Singular Values

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。5 页。SHA-256 为 `4793f062c241e6e2d0125ef52607c744609e02d39203524f98707fd79b0e3c68`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/linconj/v1/linconj-v1.pdf)
- 原文位置。Sra author preprint v1; local PDF pp. 1–5, Theorem 1.1 and proof; no archival identifier stated in the local copy.
- 局部构件。Inertia-count route to a weighted singular-value arithmetic–geometric mean inequality.
- 依赖。Requires A,B positive semidefinite and 0≤t≤1; compares σ_j(A^{2(1−t)}B^{2t})^{1/2} with λ_j((1−t)A+tB). The proof uses the manuscript's inertia identity and scalar inequality, not an arbitrary matrix-product template.
- 审阅状态。held

### Positive definite functions of noncommuting contractions, Hua-Bellman matrices, and a new distance metric

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。12 页。SHA-256 为 `6d80f678b88c39a0f1f764aca1439ab53cabb1aeddae8f8fcc224ea941c58a62`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/hua/v1/hua-v1.pdf)
- 原文位置。hua-v1.pdf, pp.1-9, Thms.2.1,2.4-2.5,3.1
- 局部构件。Hua-Bellman counterexample and integer-exponent PD via alpha-permanents.
- 依赖。v1 preprint; depends on Hua/Faraut-Koranyi/Gindikin and Vere-Jones/Foata-Zeilberger; no numerical certificate rerun.
- 审阅状态。hold

### The p-Bures-Wasserstein distance via 3x3 block matrices (with application to p-Bures-Wasserstein barycenters)

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。20 页。SHA-256 为 `722e22ee112e7d81446d182559af8db16460378623776dca668a61a9ff73ceb9`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/pbures/v1/pbures-v1.pdf)
- 原文位置。pbures-v1.pdf, pp.1-3, Thms.1.1-1.3; §§2-5
- 局部构件。Schatten partition inequality for claimed metricity and 3x3 block-norm PSD.
- 依赖。v1 preprint; uses interpolation and finite-dimensional PSD/support hypotheses; Appendix E is numerical.
- 审阅状态。hold

### The generalized Lax conjecture holds for mixed determinants

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。31 页。SHA-256 为 `73ac282d825cbfe4abfda851839bb0a1b84be6fef333498ae460a320a9291d3f`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/eta/v1/eta-v1.pdf)
- 原文位置。pp. 1–10, Theorem 1.1; Lemmas 2.3–2.5; Propositions 3.1–3.2, 4.2
- 局部构件。Inductive spectrahedral-cone construction for mixed determinants: a rank-one affine identity and an exit threshold expressed by a compressed-inverse maximal eigenvalue, followed by tensor-sum/Schur-complement construction of the next unital CP pencil and boundary-kernel compression.
- 依赖。2 Nov 2026 v1 author GitHub preprint. Requires Borcea–Brändén mixed-determinant hyperbolicity/interlacing for Hermitian tuples relative to e_{d,m}; the induction and external stability theory were not independently certified.
- 审阅状态。candidate

### Tsallis Metrics on Density Matrices via the S-Divergence

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。14 页。SHA-256 为 `af9de7547106524c4e3bb1b878cd5b3a3784a37d15ab46dcb07f0e3add7f03ca`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/tsallis/v1/tsallis-v1.pdf)
- 原文位置。pp. 1–7, Theorems 1.1–1.2 and 3.2 with proof
- 局部构件。Four-point S-divergence negative-type certificate: a Cayley-coordinate critical-point argument gives PSD \[−log det(I−U_iU_j)\] for i,j≤3, whose integral representation yields three-point trace-power-kernel positivity and a metric criterion.
- 依赖。Author v1. Requires positive-definite matrices/strict contractions, S-divergence identities, the scalar trace-power integral representation, and Schatten-norm geometry.
- 审阅状态。candidate

### Weak positivity of Schur forms under decomposable curvature

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。37 页。SHA-256 为 `25eb3c90d1d5d56ef9e46e27761a82369e027bad5425e410e40621cee64ccf52`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/qperm/v1/qperm-v1.pdf)
- 原文位置。pp. 1–2; pp. 5–10, Theorem 2.3 and Propositions 3.1–3.3; pp. 19–21, Proposition 5.1
- 局部构件。Quaternionic-Gaussian determinant representation certifies nonnegative mixed determinant Γ_n for decomposable positive maps; entanglement-breaking-addition expansion reduces hereditary sign to all square compressions.
- 依赖。Author v1. Requires Kraus decomposability, Gurvits's Gaussian determinant identity, and Finski's incidence/quotient-curvature input. It explicitly does not prove unrestricted positive-map or general Schur-form positivity.
- 审阅状态。candidate

### Wigner–Yanase–Dyson Metrics Have Monotone Curvature

- 来源与本机版本。其他 GitHub 作者。v1 · 作者公开原稿。20 页。SHA-256 为 `e511329cad265f2f83f3ed14fee1a4a97d82a6c9bd448ecb4c535a386233d156`。 [发布入口](https://github.com/suvrit/preprints/blob/main/preprints/wyd/v1/wyd-v1.pdf)
- 原文位置。pp. 1–3, Theorem 1.1; pp. 8–9, Proposition 2.6/Lemma 2.7; pp. 9–15, Theorem 3.12 and conclusion
- 局部构件。Linewise Stieltjes-transform method: prove a boundary-imaginary-part sign for Dittmann's three-variable kernel, then reciprocal-Stieltjes concavity yields WYD scalar-curvature monotonicity uniformly in dimension.
- 依赖。Author v1. Requires Dittmann's curvature formula, the companion p=1 boundary estimate, exact divided-difference decomposition, and non-explicit uniform ε; conclusion applies only for p near 1.
- 审阅状态。candidate


## 几何、覆盖与极大算子

### A Lean-verified strict edge net for crossed polygonal roofs over a parallelogram

- 来源与本机版本。其他 GitHub 作者。作者公开稿。10 页。SHA-256 为 `18811b3183d02d20bcc279c6e050488da45de5461c74ca2c57cd8761089f1e05`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/durer-crossed-roofs/note.pdf)
- 原文位置。local PDF pp. 1, 3 (construction and formal Theorem 1); p. 9 (tooling/provenance disclosure)
- 局部构件。Coordinate unfolding maps for a crossed-roof family, with monotone roof/floor arc-length coordinates intended to give chartwise isometry and strict non-overlap.
- 依赖。The claimed formal statement concerns coordinate maps; the facet/cut-tree/disk-topology arguments remain textual. The document itself says its Lean files, frozen build and generated certificate must be the source for kernel verification, none of which was replayed in this audit.
- 审阅状态。held — author/AI workflow draft; do not use its strict-net conclusion or formalization claim without a reproducible Lean-source audit.

### A non-hollow lattice 4-simplex of covering radius 2 outside the equality list of a conjecture of Codenotti, Santos and Schymura

- 来源与本机版本。其他 GitHub 作者。作者公开稿。10 页。SHA-256 为 `520e8b99fbebb9f3a32398fa5d74f9ad368ee2fc91f64674857be6ab0a0592f9`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/css-covering-equality/note.pdf)
- 原文位置。local PDF pp. 1, 4–5 (simplex claim, volume/equality-list argument and Lemma 4)
- 局部构件。Specific lattice 4-simplex proposed as an equality-case counterexample, combining a covering construction, an interior-lattice-point claim and an invariant excluding direct-sum/translation constructions.
- 依赖。The equality-list exclusion is a textual Lemma 4 and the origin/interior and radius claims are attributed to Lean coordinate checks; this audit read the proof pages but did not obtain/replay the Lean source or independently certify the covering-radius computation.
- 审阅状态。held — retain as an unverified candidate counterexample, not as a settled refutation or a reusable lattice-covering theorem.

### Bounds for the weak type (1,1) constant of the centred maximal operator over squares

- 来源与本机版本。其他 GitHub 作者。作者站在线版。12 页。SHA-256 为 `4cfd1ec7e22e15a6b80e13eb3e72e9d02386c93cdb28dc3aec0721324653e31e`。 [发布入口](https://github.com/tejasvi/square-maximal-weak-type)
- 原文位置。local PDF p. 2 Theorems 1.2–1.3; pp. 6–9 kernel and periodic-measure proofs; p. 12 formalization/disclosure
- 局部构件。Centred-maximal bound workflow: fractional comparison kernel with exact Bernstein/ball-arithmetic positivity checks, plus a finite periodic-measure lower-bound covering certificate.
- 依赖。Upper comparison principle and earlier bounds are attributed to Lin; actual certificate code and the asserted Lean verification are external, while the PDF specifies α=47/40, R=33/20, h=1/32 and proof structure.
- 审阅状态。candidate—use as a router-level certified-computation pattern only; numerical constants require replay of the external exact certificates.

### Centred maximal constants for squares: c₂ &lt; 4

- 来源与本机版本。其他 GitHub 作者。手稿标日期 2026-09-30。9 页。SHA-256 为 `e53e9da9dd9c6f9cf5389bd1b7ed9a7b14e7aa3c82634952e9e64ba27046005d`。 [发布入口](https://github.com/CoolRmal/centered-maximal-constant/commit/72c022b)
- 原文位置。local PDF p. 1 Theorem 1; pp. 5–6 proof via partial balayage/minimum principle
- 局部构件。Conditional comparison-principle transfer: if an even L1 kernel majorizes the diamond and has nonnegative fractional operator off zero, then c₂ is bounded by half its integral.
- 依赖。Relies on Spector–Stockdale partial balayage and Courrège representation; the PDF is an explanatory manuscript and does not itself supply a concrete kernel/certificate yielding the strict numerical conclusion.
- 审阅状态。held—retain only the conditional transfer lemma; do not record c₂&lt;4 as a locally instantiated proof.

### Continuous planar isotropy (extended manuscript)

- 来源与本机版本。其他 GitHub 作者。作者公开稿。5 页。SHA-256 为 `36cd77087f0e9ca47b6ad297183732a165c8ab3b00dc7f0b068fc0f9eca4159d`。 [发布入口](https://github.com/alexodas/pythagorean-isotropy-lean/blob/v0.2.0/manuscript/continuous_planar_isotropy_explained.pdf)
- 原文位置。local PDF pp. 1–3: scope disclaimer, Theorem 2.1 and continuous-action-to-axis-reachability argument
- 局部构件。Conditional rigidity schema: continuity plus a supplied linear isometric action, quarter-turn, axial calibration and rigidity imply the Euclidean norm; a trigonometric model supplies the converse.
- 依赖。All geometry is explicitly assumed as a linear action rather than derived from incidence axioms; Lean theorem is in the external tagged repository v0.2.0.
- 审阅状态。candidate—conditional hypothesis-audit component only; it is not a foundational derivation of planar Euclidean geometry.

### Covering minima of the standard terminal simplex and a discrete surface area bound for the covering radius of simplices

- 来源与本机版本。其他 GitHub 作者。作者公开稿。13 页。SHA-256 为 `1536f6a641b5eb241191a66351eeaac8b7af17d3cedc88e0ddbf85bf4ab406ef`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/css-covering-minima/note.pdf)
- 原文位置。local PDF pp. 3–7: Theorems 1–2, sawtooth averaging Lemma 5, and proofs; pp. 9–10 Lean statement map
- 局部构件。Sawtooth/Hermite averaging certificate for lattice covering: choose a common phase t to control weighted fractional parts, then turn it into a simplex covering decomposition.
- 依赖。Uses Codenotti–Santos–Schymura for conjecture formulation and for the separate lattice-polytope implication; external Lean artefacts cover the stated measured theorem.
- 审阅状态。candidate—core averaging proof is present; do not infer the equality characterization or unformalized cited implication.

### Illumination numbers of convex bodies between a triangular prism and a cube

- 来源与本机版本。其他 GitHub 作者。作者公开稿。8 页。SHA-256 为 `061348a08d4a94960d52d25383f4f9230df7f0e5209fa0751159dca57f8273a7`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/illumination-prism-sandwich/note.pdf)
- 原文位置。Author-hosted manuscript, 23 Nov 2026, PDF pp. 1–6, Theorem 1 and Lean mapping; no journal/preprint identifier stated.
- 局部构件。Coordinate sandwich illumination trichotomy for P⊆K⊆\[0,1\]^3.
- 依赖。Needs exactly the triangular prism P, opposite edge E, compact convex K, and the claimed Lean source bundle; it gives no general 3D illumination bound.
- 审阅状态。held

### Lattice simplices whose Minkowski length exceeds the lattice diameter, and dilates whose Minkowski length is not quasi-linear

- 来源与本机版本。其他 GitHub 作者。作者公开稿。11 页。SHA-256 为 `5070e4926a90b8a6a394013f023ca03b04706d71b36c667ff7ba3a6ab632b528`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/minkowski-length-simplices/note.pdf)
- 原文位置。Author-hosted manuscript, 22 Nov 2026, PDF pp. 2–10, Theorems 1–2 and Lean mapping; no journal/preprint identifier stated.
- 局部构件。Explicit lattice-simplex counterexamples for L(P)=ℓ(P) and quasi-linearity of L(tP).
- 依赖。Uses the two displayed 3D simplices T and U, exact lattice-point/segment packing inequalities, and pyramid transfer; claimed Lean checks are a separate repository dependency. It does not supply a general Minkowski-length algorithm.
- 审阅状态。held

### The Chaise Longue Theorem

- 来源与本机版本。其他 GitHub 作者。v12 · 作者公开原稿。82 页。SHA-256 为 `1334d04bfd19dfeca0593a9fdedb31c1dae747915e493922862f7c1c7e56c056`。 [发布入口](https://github.com/tretoef-estrella/chaise-longue-theorem/blob/main/paper/THE_CHAISE_LONGUE_THEOREM_v12.pdf)
- 原文位置。THE_CHAISE_LONGUE_THEOREM_v12.pdf, pp.1-9, 62-67
- 局部构件。Group-ring reduction of Fermat primitivity to characteristic-p dimension counts.
- 依赖。Unrefereed v12; geometric theorem depends on Pham and Degtyarev-Shimada; external Lean/topology not audited.
- 审阅状态。hold

### The Coordinate Pythagorean Theorem from Planar Isotropy (distinct historical manuscript)

- 来源与本机版本。其他 GitHub 作者。作者公开稿。5 页。SHA-256 为 `686bb766e138173770a9dded1923efb369db3528bfd6e11751642485ff6c3de5`。 [发布入口](https://github.com/alexodas/pythagorean-isotropy-lean/blob/64c8ea3ef05d621814bc6460223f1f14d208f543/manuscript/pythagorean_isotropy_ai_disclosure.pdf)
- 原文位置。pythagorean_isotropy_ai_disclosure.pdf, pp.1-5, Thms.2.1,3.1
- 局部构件。Conditional Pythagorean derivation from rigid one-parameter action axioms.
- 依赖。AI-generated author disclosure; claimed Lean only formalizes conditional implication and was not compiled.
- 审阅状态。hold

### The Watermark in Every Even Dimension

- 来源与本机版本。其他 GitHub 作者。作者公开稿。16 页。SHA-256 为 `0b47b0127e542c7aa21b6c457d819674fee4a127cf1f73a921b65382bdf51d8e`。 [发布入口](https://github.com/tretoef-estrella/chaise-longue-theorem/blob/main/paper/THE_WATERMARK_IN_EVERY_EVEN_DIMENSION.pdf)
- 原文位置。THE_WATERMARK_IN_EVERY_EVEN_DIMENSION.pdf, pp.1-15, Thms.1-4
- 局部构件。Fermat Hodge-lattice discriminant formula via group-ring ideals/Hilbert functions.
- 依赖。Unrefereed v2; depends on Pham/Looijenga, Shioda sources, Degtyarev-Shimada, BRR and Chaise Longue; patterns observed.
- 审阅状态。hold

### The discrete quantitative Helly number for five common lattice points

- 来源与本机版本。其他 GitHub 作者。作者公开稿。12 页。SHA-256 为 `3e0f7a08ccc433dc1e80d0c02d9e0d96572d2617bac6dc0efaa29e2fe72113a5`。 [发布入口](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/quantitative-helly-five/note.pdf)
- 原文位置。pp. 2–6, Theorems 1–2; Proposition 2
- 局部构件。Parity/midpoint charging: each same-mod-2 triple of lattice points is charged to three nonvertex midpoint witnesses, yielding binomial capacity bounds; the finite low-dimensional residue-class enumeration is separate.
- 依赖。Author GitHub preprint. Applies to a lattice polytope P⊂R^n with at most five nonvertex lattice points; conversion to quantitative Helly uses Averkov et al.'s polytope characterization. The n=2,3 values require finite tables and a planar argument; claimed Lean proof was not replayed.
- 审阅状态。held


## 算法复杂性与机器学习

### Truly Subquadratic 3SUM and Subcubic APSP

- 来源与本机版本。Anthropic 关联。Alman and Vassilevska Williams paper; Anthropic published a separate Lean formalization。76 页。SHA-256 为 `d91a79c5dbf1fc662f0c5c1bb2b690ac3d83d9ef5bf872bde4cdaf7cc9e76005`。 [发布入口](https://github.com/anthropics/formal-math/tree/main/3sum-apsp)
- 原文位置。local PDF sha256=d91a79c5dbf1fc662f0c5c1bb2b690ac3d83d9ef5bf872bde4cdaf7cc9e76005; pp. 1–3, 63
- 局部构件。External Alman–Vassilevska Williams research paper; Anthropic’s connection is model provenance and a later separate Lean certification. Main claim is a thin-matrix-product algorithm yielding stated 3SUM/APSP exponents.
- 依赖。The formalization reported on p. 63 is a separate anthropics/formal-math artifact. The mathematical claim depends on the paper’s sparse-lopsided-triangle algorithm and fine-grained reductions; no complete proof audit or pinned Lean build was performed.
- 审阅状态。hold as an external theorem paper; do not classify it as an Anthropic theorem or promote its claimed formalization.

### Subexponential 3-SAT

- 来源与本机版本。Anthropic 官方。Anthropic research preprint; formalization reported by publisher。49 页。SHA-256 为 `85034e06e1d058aa4ed7d895c226ae755ebd3a5c6614b07ba14981915c4f7360`。 [发布入口](https://hexagonmath.org/2610.00577v1)
- 原文位置。local PDF sha256=85034e06e1d058aa4ed7d895c226ae755ebd3a5c6614b07ba14981915c4f7360; pp. 1–5, 40–44
- 局部构件。Official Anthropic research preprint. It claims deterministic 2^o(n) counting for #3-SAT (hence ETH false); pp. 40–44 supply Lean-facing statements rather than the proof term.
- 依赖。The argument depends on the graph/tensor decomposition, sparsification, machine-model transfer, and a separate Lean proof file. The printed Lean appendix states definitions/theorem types, but this audit did not build the proof or verify the prose-to-Lean bridge described on p. 44.
- 审阅状态。hold; do not promote ETH refutation or install a theorem skill without a pinned source replay and independent audit of reductions/model translation.

### VP is not equal to VNP

- 来源与本机版本。Anthropic 官方。Anthropic research preprint; formalization reported by publisher。70 页。SHA-256 为 `e6de6806c7fd939ff536451951b0c44231b3ad1b6148bdb33fcc4e3143268b88`。 [发布入口](https://hexagonmath.org/2611.00954v1)
- 原文位置。local PDF sha256=e6de6806c7fd939ff536451951b0c44231b3ad1b6148bdb33fcc4e3143268b88; pp. 1–5, 11, 17, 60–70
- 局部构件。Official Anthropic research preprint. It claims superpolynomial general arithmetic-circuit lower bounds over all fields and a Lean formalization; the written route splits into flat/contracting cases.
- 依赖。The exact statement relies on the full Appendix proof and the formal-math Lean development (Lean 4.33.1/Mathlib commit 0df444a360e reported on pp. 11, 66–70). pp. 17 and 63 expressly mark places where Lean, rather than prose, carries details. No checkout/build or full proof verification was performed.
- 审阅状态。hold; do not promote VP≠VNP, border-complexity consequences, or a theorem skill until independently replayed and statement/dependency-audited.

### Place Value, Not Position: Length Generalisation Limits in Neural Modular Arithmetic

- 来源与本机版本。其他 GitHub 作者。作者公开稿。15 页。SHA-256 为 `6336ab87574a9fc2677ae40a8c2c206aa78737db592251f50eae2b1ad9f5b4eb`。 [发布入口](https://github.com/Amey-Thakur/SAIR-FOUNDATION-FOR-SCIENCE-AND-AI-RESEARCH/blob/main/papers/I-modular-arithmetic.pdf)
- 原文位置。I-modular-arithmetic.pdf, pp.1-12, §§4-9
- 局部构件。Controlled place-value versus position encoding experiment.
- 依赖。Author experimental manuscript; depends on specified implementation, dataset, one seed, and measurement protocol.
- 审阅状态。hold


## 数学物理

### Hawking–Page at Weak Coupling

- 来源与本机版本。Anthropic 官方。Anthropic mathematical-physics preprint。42 页。SHA-256 为 `9ef46fdb93337018a044e743f6f664136e86d30675da917dc3e5742de5c90a52`。 [发布入口](https://hexagonmath.org/2611.00175v1)
- 原文位置。local PDF sha256=9ef46fdb93337018a044e743f6f664136e86d30675da917dc3e5742de5c90a52; pp. 1, 7–8, 20–21
- 局部构件。Official Anthropic mathematical-physics preprint. It reports the perturbative coefficient b=−1.48×10^−3 λ^2 and infers a first-order weak-coupling transition at leading 1/N and order λ^2.
- 依赖。The inference depends on the Hamiltonian/Coulomb-gauge multi-trace computation, counterterm analysis, numerical truncations and reported cross-checks. pp. 7–8 limit the scope and report a remaining diagram-class discrepancy; source code/numerical input were not rerun.
- 审阅状态。hold as an unrefereed preprint; numerical and analytic claims are not independently verified and are not a reusable mathematics-skill theorem.

### The Spinless Modular Bootstrap

- 来源与本机版本。Anthropic 官方。Anthropic mathematical-physics preprint。131 页。SHA-256 为 `dcda16c21f6e14ab7bfb0ee483d57e2fc50bd6a97c98638dd5aea1e2dc18faec`。 [发布入口](https://hexagonmath.org/2611.00174v1)
- 原文位置。local PDF sha256=dcda16c21f6e14ab7bfb0ee483d57e2fc50bd6a97c98638dd5aea1e2dc18faec; pp. 1–5, 120–123
- 局部构件。Official Anthropic mathematical-physics preprint. It claims an exact large-c slope within its functional class and an explicit functional certified with interval arithmetic.
- 依赖。The conclusion is restricted to the defined class A-bar and uses potential-theoretic estimates plus computer-assisted interval bounds/Arb computations (pp. 120–123). Reported certificates, scripts, parameter ranges, and their execution were not independently checked.
- 审阅状态。hold; no general CFT conclusion or skill promotion beyond the stated functional class and unverified computational certificate.
