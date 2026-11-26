# 近期原稿与常数专题的补充文献

[回到索引](README.md)。

## A01 · VP ≠ VNP over Every Field

- 原件。Claude manuscript; abstract says Lean formalization, but the formal artifact was not inspected。PDF 物理页 1, 2。SHA-256 882f5eefb1e067cc8c99ddfe660c10d1d67f9fcee7b69364bd0bab06c0c1f97c。
- arithmetic-circuit lower bounds。Abstract; Theorem 1.1 (physical p.2)。在任意特征下对 Hamiltonian-cycle 多项式、且特征非二时对 permanent，声称算术电路规模具有 m^{c(log m)^{1/3}} 下界；这是算术而非布尔电路结论。
- 条件或证据待查。全域下界证明及所称 Lean 工件均未逐项审计。 仅核对题名、摘要和主定理陈述；未核对证明、代码库、形式化范围或与现有工具的可迁移性。
- 第五批定向筛选。unresolved。The asserted VP != VNP result is said to be Lean-formalized, but no Lean project, commit, theorem name, or dependency manifest is included in the raw paper; the primary proof dependency is therefore unavailable. 后续条件。Acquire the Lean repository/commit and build instructions, reproduce the theorem, and isolate any standalone finite algebraic lemma.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The source names its main Lean theorem and Mathlib revision, but the bundled text itself says the printed Lean file contains definitions only and records divergences from the prose route. Without the associated project and a replayed build, the claimed general circuit lower bound cannot yield a standalone verified component.。定位。1, 2, 66, 70。全卷 70 页。后续条件。The canonical Lean release/revision, reproducible build log, and a selected finite circuit lemma with an explicit input/output contract.。

## A03 · A 2^o(n) Time Algorithm for 3-SAT

- 原件。Claude manuscript dated 2026-10-26; Lean 4 formalization claim uninspected。PDF 物理页 1, 2。SHA-256 7af518b09342c967ea371c74b8989806684c5d02aabe5763ca08554aff5025a0。
- exact exponential algorithms。Abstract; Theorem 1 (physical p.1)。声称对 k-CNF 计数给出 2^{o(n)} 确定性算法，因此按文中定义否定 ETH；对象是输入变量数与子句数均须跟踪的计数问题。
- 条件或证据待查。算法递归、运行时间常数及 Lean 形式化工件未审计。 不能由摘要或定理页确认 ETH 反例；未形成可调用数学工具。
- 第五批定向筛选。unresolved。The asserted subexponential #3-SAT algorithm is said to be Lean-formalized, but no formal artifact or executable recurrence/cost certificate is included in the raw source for independent dependency checking. 后续条件。Acquire the Lean project/commit and exact algorithm specification; reproduce its asymptotic and finite-cost bounds before considering adoption.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The paper gives an asserted #3-SAT rate, but its Lean appendix describes a definitions-only file and explicitly leaves encoding and machine-simulation steps outside the formal proof. The recursion and a complete finite cost certificate are not supplied as an executable artifact.。定位。1, 2, 40, 44。全卷 49 页。后续条件。Pinned source of the algorithm and Lean proof, plus a finite recurrence/cost verifier that covers the text-to-machine encoding bridge.。

## A09 · Discovering state-of-the-art quantum circuits with large language models

- 原件。arXiv:2610.22367。PDF 物理页 1, 29, 46。SHA-256 3607f457c3349db74e10b131abadef23a4a2dea0fefa0cf6ac6d0ed9f37fdfd9。
- quantum-circuit search。Abstract; Appendix A Proposition A.2; conclusion/appendix endpoint。研究以 LLM 提议和进化搜索量子电路，附录含特定模块算术规则；可见内容是面向实验基准的电路搜索，而非一般数学证明工具。
- 归档定位。电路评测、搜索实现与量子模型前提未复核。 未审计实验数据或把附录规则外推为通用量子算法。
- 第六批定向筛选。adjacent。The verified preprint is an empirical LLM-plus-evolutionary quantum-circuit search framework. Its Appendix A decoder rule is architecture-specific and not a general mathematical tool. 定位。Abstract p.1; reversible walk/decoder discussion p.29; Theorem A.6 equation (A11) p.46.。全卷 46 页。 后续条件。A reusable component would require a declared circuit-state representation, gate semantics, and independent evaluator contract.

## A21 · Worse Together: How Performance Breaks Down in Multi-User Multi-Agent Teams

- 原件。arXiv:2610.00583, preprint under review。PDF 物理页 1, 9。SHA-256 d57efb1e2019b8ffbe2a19cddc0c50e927b8dc66421150ec53f0654fc791ff7e。
- multi-agent empirical evaluation。Abstract; Conclusion (physical p.9)。在四类共享资源环境和多模型实验中比较单协调者与分用户代理，报告多代理协作可出现性能下降。
- 归档定位。结论依赖所列场景、提示和评价协议，未复现实验。 经验性 AI 协作研究，不是数学工具构件。
- 第六批定向筛选。citation。This under-review empirical multi-agent study reports scenario-dependent coordination failures, not a transferable mathematical proof or computation primitive. 定位。Abstract and experimental setting p.1; safety/implications discussion p.9.。全卷 63 页。 后续条件。Reproduction would require the 77 scenario prompts, model versions, evaluation protocol, and raw episode data.

## A25 · Lowered crossover points of Anthropic's subexponential 3-SAT algorithm

- 原件。arXiv:2610.41622。PDF 物理页 1, 2。SHA-256 48b490c8412fe8b8724b8ee607135f0781417ba99376b2932e56443d640bc4ad。
- 3-SAT asymptotic crossover analysis。Abstract and introductory main-result paragraph (physical p.1)。对所称 Anthropic #3-SAT 递归的显式常数和分组参数作交叉点估计，声称降低若干渐近界的实际交叉规模。
- 条件或证据待查。关键递归及 2^{o(n)} 基础结果依赖 A03，且各常数推导未逐页复核。 不能将数值交叉点或 ETH 结论当作已核验的算法证书。
- 第五批定向筛选。unresolved。Its crossover estimates explicitly depend on the unverified A03 recursion and its proved constants; without that upstream formal/executable artifact the claimed numerical crossover interface has no checked dependency chain. 后续条件。First resolve A03 with its Lean/executable proof artifacts, then obtain the integer tables and recurrence inputs used for this crossover calculation.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The local arXiv:2610.41622v1 manuscript's crossover calculations and Signed Network Sums analysis explicitly build on the unclosed Anthropic #3-SAT recursion. Although scripts are linked by the record, neither the upstream proof artifact nor the claimed integer tables/schedules are in this assigned bundle.。定位。1, 2, 3, 4, 54, 55, 56。全卷 56 页。后续条件。First close the upstream #3-SAT recurrence; then pin and run the cited scripts with all schedule and integer-table inputs.。

## A26 · A Mathematical Theory of the Jacobian Lens

- 原件。arXiv:2610.31955 preprint。PDF 物理页 1, 3, 4。SHA-256 89454dc3ee81ba4a6e354eee08eec603dc8fad86f953b0f4ce8d112b92203d90。
- dynamical-systems analysis of neural representations。Abstract; Sections 1–2 and displayed bound (8) (physical pp.1,3–4)。把 transformer 深度与 token 位移下的 Jacobian 平均联系到有限时间/对流 Lyapunov 模态；在上下文残差重叠受控等假设下，平均抑制不相干方向。
- 条件或证据待查。结论取决于文中 Jacobian 分解、独立上下文重叠界及前序 J-lens 定义；均未完整审计。 只核对局部数学叙述，未验证模型实验或把该不等式移用于其他网络。
- 第五批定向筛选。unresolved。The J-lens paper is model- and data-dependent. This screen found no standalone finite mathematical interface whose hypotheses can be checked without the cited architecture, trained models, and empirical setup. 后续条件。Provide the precise J-lens definition, model checkpoints/data, and a bounded theorem with all dynamical assumptions isolated.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The local 27-page Jacobian-Lens preprint states a conditional suppression inequality for independent contexts and bounded modal scales, not a generic finite operator certificate. Moreover, arXiv now lists v2 while this local source has no matching current-version identifier, so its scope cannot be promoted from the checked local text.。定位。1, 3, 4。全卷 27 页。后续条件。A pinned version, precise J-lens/Jacobian inputs, and a reproducible finite model/checkpoint dataset that verifies the stated coherence assumptions.。

## A27 · Hilbert Series in Four Variables and Linear Factors of High Multiplicity

- 原件。arXiv:2608.24797v4。PDF 物理页 1, 2。SHA-256 cb6b597a08a65e5bd5f433f32d6dcea41b00cc19a48590a8abbe8db1d04d4498。
- commutative algebra and Hilbert series。Abstract; Theorem 1.1 and Corollary 1.2 (physical p.2)。在特征零四元多项式环中，定理对一般 quintic 或 septic 形式的任意个数给出 Fröberg 预测 Hilbert 级数；另给出高重线性因子情形的阻碍。
- 条件或证据待查。一般位置、逆系统和文中 exact certificates 的证明/计算输入未复核。 仅核对主陈述；未验证证书，不能推广到其他次数、变量数或正特征。
- 第五批定向筛选。adopt。The paper proves an elementary modular-rank-to-characteristic-zero transfer and specifies endpoint propagation; the full quintic/septic result relies on ancillary certificate files not present here, so adoption is restricted to the proved transfer interface. 后续条件。For full Hilbert-series claims, acquire and run the named quintic/septic verifier sources and certificate JSON, then verify their reported maximal minors.
- 已采用方法。物理页 2, 3, 4, 5, 6, 7。A nonzero maximal minor after integral specialization modulo a prime certifies the corresponding characteristic-zero rank locus; endpoint injectivity/surjectivity propagates under the stated multiplication-map hypotheses. [方法说明](../../../math-l17-filtered-linear-algebra-certificates/references/wave5-c08-01-modular-rank-transfer.md)。

## A28 · Formalizing inverse problems in the age of AI: possibilities, pitfalls, and an invitation

- 原件。arXiv:2611.06962v1, work in progress。PDF 物理页 1, 2。SHA-256 23946706504bf7f0252e619a8f4fbee9d92746177c7775f3f4ea3ba126d0f13a。
- formalized inverse problems。Abstract; introduction (physical pp.1–2)。介绍 AutoIP 的 Lean 4 正则化理论库，并强调形式证明只认证已编码陈述，仍须核对自然语言命题与假设是否一致。
- 条件或证据待查。库覆盖度、接口和每项形式化定理均未检查。 可作形式化审阅流程线索；不把工作进行中的库视为已安装或已验证工具。
- 第五批定向筛选。hold。arXiv:2611.06962v1 calls AutoIP work in progress. The overview correctly limits formal certification to statements actually encoded, but it supplies no stable repository revision or checked theorem interface to distill. 定位。physical pp. 1-2; 13-page PDF 后续条件。Pin a public Lean repository revision, identify a theorem with its exact types and hypotheses, and compile it before creating a formalization route.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The current arXiv v1 overview correctly says that Lean certifies only the statement actually encoded, but it is explicitly work in progress and supplies no pinned AutoIP repository revision or theorem-level interface to inspect and compile.。定位。1, 2。全卷 13 页。后续条件。Public repository revision, exact theorem declarations and dependencies, followed by a successful Lean build and statement-to-prose audit.。

## G13 · Applications of a theorem by A. B. Shidlovski

- 原件。public-source copy per inventory; scanned PDF has no extractable text。PDF 物理页 1。SHA-256 0e39a6cbb76c8357b7ffe6eb4a5ec6765aa19cf0f2eb567a88a9c69470ae70c0。
- E-functions and Shidlovskii theory。physical p.1 image-only; no machine-readable theorem locator。库存题名表明主题为 Shidlovskii 定理的应用，但该副本 25 页均无可提取文本，未能从原页确认作者、版本或命题。
- 条件或证据待查。不可读的源文本阻断对所用 E-函数假设和外部定理的审计。 需人工视觉定位或可检索版本后再提取；当前不得采用任何数学结论。
- 第五批定向筛选。hold。Mahler's 1968 Proceedings of the Royal Society paper is formally published (DOI 10.1098/rspa.1968.0111), but this local 25-page scan is image-only and no theorem or hypothesis could be verified from the actual copy. 定位。physical p. 1 (image-only); 25-page PDF 后续条件。Acquire searchable authoritative text or manually transcribe and verify the specific Shidlovskii application before use.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The supplied 25-page copy is image-only: actual p.1 has no extractable theorem text. Publication metadata alone cannot identify the statement, hypotheses, or which Shidlovskii application would be usable.。定位。1。全卷 25 页。后续条件。Searchable authoritative text or a checked manual transcription of the selected theorem and all E-function hypotheses.。

## G18 · How can we escape Thomae's relations?

- 原件。arXiv:math/0502276v1 (2005-02-13)。PDF 物理页 1, 2。SHA-256 70e270a25ad4a8fbf71614c9712773d6ca7d358530285d4a5aa28bd100721597。
- hypergeometric transformations and zeta linear forms。Abstract; Theorems 1–2 (physical p.2)。给出两族超几何 3F2(1) 关系以解释超出 120 个 Thomae 关系的例子；定理有参数非极点与实部收敛条件。
- 既有方法覆盖。与整系数线性形式/γ 判据的实际嵌入未由本文两页核完。 现有 γ 工具已保留 Thomae 变换的条件性接口；本次未审计全文证明或断言新的 γ 无理性结论。
- 相关入口。[math-euler-constant-irrationality](../../../math-euler-constant-irrationality/SKILL.md)。

## G20 · Automatic Discovery of Irrationality Proofs and Irrationality Measures

- 原件。arXiv:1912.10381v1 (2019-12-22)。PDF 物理页 1, 2。SHA-256 7f21845a06486d86b662bb7c6df5c234380b14c8af69290028e2448615db12b4。
- symbolic experimental irrationality search。Abstract/package list (physical p.1); introductory workflow (p.2)。以 Maple 包自动产生若干积分或对数常数的候选小线性形式，并区分可完全自动化的例子与仍需人工证明的步骤。
- 构件候选。每个包的正确性、整数性、误差界和非零性均须按具体常数另审，本文概述不构成通用证明。 候选是“搜索与审计分离”的工作流，不部署脚本、不采纳任一自动发现结论。
- 相关入口。[math-tool-router](../../../math-tool-router/SKILL.md)。
- 第五批定向筛选。unresolved。The PDF identifies its concrete automatic outputs as external Maple packages; those packages and their generated certificates are not in the assigned raw bundle, so the claimed automated proof/measure dependencies cannot be checked here. 后续条件。Acquire the cited ALLADI/GAT/BEUKERS/SALIKHOV package sources and representative output certificates; then screen their exact recurrences and integrality bounds.
- 复核记录。2026-11-26T18:35:59+08:00。citation。citation。
- 本次依据。This is the arXiv v1 text with a 2021 journal reference. It explicitly presents four external Maple packages and distinguishes automatic discovery from proof completion; those packages and their generated integrality, error, and nonvanishing certificates are absent here.。定位。1, 2。全卷 10 页。后续条件。Acquire pinned ALLADI/GAT/BEUKERS/SALIKHOV sources and concrete outputs before screening any constant-specific certificate.。

## G21 · Mellin transforms, transfinite diameter and rational approximations of integrals

- 原件。arXiv:2604.20741。PDF 物理页 1, 2。SHA-256 fcbcc22ee7504b9e057c534c0e5fae3f3812af8548d132cd2018ce4857a20bef。
- periods and multivariate rational approximation。Abstract; Section 1 and Theorem 1.1 (physical p.2)。提出用 Mellin 积分像的多变量 transfinite diameter 控制周期的小线性形式，并以 M0,5 上 ζ(2) 的五参数积分作为示例。
- 构件候选。从行列式/直径估计到可用有理线性形式仍依赖分母清除、非零性及后续定理；本次未完整复核。 仅保留一般候选路线，不能转用于 γ 或其他周期而不逐项满足其解析与算术假设。
- 第五批定向筛选。adopt。The PDF proves a finite matrix/Minkowski irrationality interface and states its denominator and nonzero-determinant hypotheses explicitly; the adopted reference is restricted to that conditional criterion. 后续条件。For a period application, supply a verified Mellin family, basis of periods, denominator matrices, and determinant/transfinite-diameter bounds.
- 已采用方法。物理页 4, 5, 21, 22。For a Mellin-integral matrix Q with nonzero determinant and verified denominator factor delta_N, the stated transfinite-diameter/Minkowski condition gives a conditional irrationality or period-space dimension conclusion. [方法说明](../../../math-integer-linear-form-rates/references/wave5-c08-01-mellin-transfinite-diameter.md)。

## G27 · A class of relations among multiple zeta values

- 原件。arXiv:math/0702824v3 (2009-01-28)。PDF 物理页 1, 2, 3。SHA-256 23bf9292e11c2dd178c702e87d9408f7d936148a2587dd4a32384373047d904b。
- multiple zeta value relations。Abstract; Sections 1 and 5 discussion (physical pp.1–3)。以有限多重调和和的 Newton 级数导出包含 Ohno 关系的一类 MZV 线性关系；文中固定权重独立数目的公式是相对该类关系的计数。
- 条件或证据待查。Newton 级数收敛、关键有限和对偶公式与关系推导未完整复核。 不能把相对关系空间的维数与全部 MZV 的线性独立维数混同。
- 第五批定向筛选。adopt。The published Journal of Number Theory 129 (2009), 755-788 paper supplies an exact finite multiple-harmonic binomial-duality identity and a Newton-coefficient interface. The adopted Corollaries 3.9-3.10 were checked with their stated Theorem 3.8 generating-function induction, and do not assert MZV independence. 定位。physical pp. 2-3, 14-15; 36-page PDF 后续条件。For any infinite Newton-series or MZV conclusion, separately verify convergence and the relevant product/derivative hypotheses; finite identity checks are insufficient.
- 已采用方法。物理页 2, 3, 14, 15。Exact finite multiple-harmonic binomial duality and Newton coefficients only; no claim of complete MZV relations or linear independence. [方法说明](../../../math-mzv-newton-harmonic-relations/references/kawashima-newton-harmonic-duality.md)。

## G27 · A note on Kawashima functions

- 原件。arXiv:1702.01377v1 (2017-02-05); inventory groups it with G27 but observed title differs。PDF 物理页 1, 3。SHA-256 fed2200529adfe9c15b50a1af1440b4fede19533bb8bd10b89326c030205f0f2。
- Kawashima functions and MZVs。Abstract; Theorem 2.1 (physical p.3)。综述 Kawashima 函数作为 digamma 函数推广，并记录其积分表达及与 Kawashima 型 MZV 关系的联系。
- 版本与引用。定理 2.1 的第一积分式明确引自另一文献，其他综述性关系也依赖所引原始工作。 只作为 G27 的背景/题录；未把综述转写为独立证明或数值算法。
- 第六批定向筛选。existing。Its Newton-series, integral, and finite-harmonic duality interfaces are already covered by math-mzv-newton-harmonic-relations. The physical source is a survey and attributes the integral theorem to prior work. 定位。Survey abstract p.1; Theorem 2.1 with explicit attribution p.3; Newton/integral formulas (2.5)--(2.9) pp.4--5.。全卷 12 页。 后续条件。Use the existing route and its primary Kawashima source for any new MZV claim.

## G33 · Periods

- 原件。IHES/M/01/22 (May 2001) survey/prepublication。PDF 物理页 1, 2, 4。SHA-256 7d43a82180893c0012e6d59f13270af9a8bde4d54dfe1f92009f39f60eae8e1a。
- periods survey。Abstract and introduction (physical pp.2–4)。定义代数函数在半代数域上的积分所形成的 periods，并综述其与微分方程、超越论和开放问题的关系。
- 版本与引用。该文是综述，具体例子和猜想依赖参考文献。 不将“period”身份自动推出代数性、超越性或可判定性。
- 相关入口。[math-research](../../../math-research/SKILL.md)。
- 第六批定向筛选。citation。Kontsevich--Zagier is a survey and status source for periods. It explicitly presents conjectural equality verification and does not supply a γ-specific transfer. 定位。Title p.1; abstract and survey scope p.2; introductory conjectural-status discussion p.4.。全卷 38 页。 后续条件。A proposed period identity must be checked against the relevant primary integral/motive source.

## G39 · Transcendence of values of logarithms of E-functions

- 原件。Mathematische Annalen 394 (2026), accepted 2025-11-12; local article PDF。PDF 物理页 1, 2。SHA-256 86669c0103d2a589c9a45970734a9ebac47c737382c015fa026b546960c0301d。
- E-functions and logarithmic values。Abstract; Theorem 1 (physical p.2)。对不经有理缩放同构的超越 E-函数，给出其有理点值相交的有限性；摘要还说明在额外严格 E-函数条件下得到对 log f(ξ) 的算术结论。
- 版本与引用。适用需核对具体函数的 E-函数性质、例外集与定理的严格系数条件。 正式发表版本仅作题录/定理范围核对；未证明 γ 或候选生成函数满足这些条件。
- 相关入口。[math-euler-constant-irrationality](../../../math-euler-constant-irrationality/SKILL.md)。
- 第六批定向筛选。adopt。Published Theorem 2 supplies a nonduplicate strict-E logarithm irrationality-measure admission gate, useful for rejecting invalid γ transfers while preserving its hypotheses. 定位。Published abstract p.1; Theorem 2 equation (1.1) and implementation assumptions pp.3--4.。全卷 20 页。 后续条件。A γ candidate must prove an exact ln(f(xi)) representation, strict rational E-function status, regular rational evaluation, positivity, and irrationality.
- 已采用方法。物理页 1, 3, 4。Strict rational E-functions, a nonzero rational regular point with positive value, and an independently established irrational logarithm. [方法说明](../../../math-euler-constant-irrationality/references/supp19-e-function-logarithm-admission.md)。

## G40 · The Unbounded Denominators Conjecture

- 原件。J. Amer. Math. Soc. 38 (2025), 627–702; article published 2025-02-06。PDF 物理页 1, 2。SHA-256 867026fbcc5592728173e5c4d6a87f58d57a55b0d0d8b0109b9774e84290ee1e。
- modular forms and arithmetic holonomicity。Theorem 1.0.1 (physical p.1); contents (p.2)。在文中指定的上半平面全纯、有限指标子群变换及 cusp 亚纯条件下，证明整系数分数 q 幂级数模形式来自 congruence subgroup。
- 版本与引用。定理适用取决于全部模形式/边界假设；与 γ 线性形式没有已核验桥梁。 已核对正式版本和主定理陈述，不外推为任意递推序列的分母结论。
- 第六批定向筛选。citation。The formally published unbounded-denominators theorem concerns modular forms and congruence coverings. No verified bridge connects its hypotheses to γ linear forms. 定位。Published Theorem 1.0.1 p.1 and its modular-lambda reformulation p.2.。全卷 76 页。 后续条件。Need a candidate modular form with the complete upper-half-plane, finite-index transformation, cusp-meromorphy, and integral Puiseux hypotheses.

## G41 · Arithmetic holonomy bounds and effective Diophantine approximation

- 原件。ICM-style preprint/source copy; publication status not established from local PDF。PDF 物理页 1, 2。SHA-256 1b3fe13a89d04c3bc570b78c1130e5a03e33d4c2915ab4b065c3dc248b3eb98f。
- arithmetic holonomy and Diophantine approximation。Abstract; Theorem 1.1 (physical p.1)。对数域、赋值、有限生成乘法群和 ε 的数据，陈述有效高度有界性：满足 |1-Aγ|_v≤H(γ)^{-ε} 的群元素高度受可计算界控制。
- 版本与引用。算术 holonomy 界及其构造/证明未在本次逐项审计；这与现有 γ 技能中另行审计的来源版本不可自动等同。 仅登记陈述与入口；未建立任何 γ 候选满足其全部函数、分母和维数门槛。
- 相关入口。[math-euler-constant-irrationality](../../../math-euler-constant-irrationality/SKILL.md)。
- 第六批定向筛选。existing。The Apéry-limit holonomy and denominator-array interfaces are already captured by math-euler-constant-irrationality's E-operator/holonomy admission route. This local ICM-style copy does not displace the already checked primary preprint version. 定位。Theorem 1.1 pp.1--2; Apéry-limit setup and Theorem 2.1 formulas (2.1)--(2.3) pp.3--4.。全卷 20 页。 后续条件。Use the existing gate with an actual Apéry pair, meromorphic pullback, denominator array, holonomicity, and strict derivative threshold.

## G41 · Products of two logarithms and arithmetic holonomy bounds

- 原件。preprint, local text cites arXiv:2611.00703 context。PDF 物理页 1, 2。SHA-256 d567cc1c0acea2b8f0962019e7253747825f14b772731384bd6c7ca78d68fdc2。
- logarithmic linear independence。Abstract; Theorems 1–4 setup (physical pp.1–2)。在所列 holonomy 定理条件下声称若干 q 范围内 1、两个对数及其乘积的 Q-线性无关，并用 Hermite–Padé 形式和区间证书处理一个微分算子。
- 条件或证据待查。作者明确把核心 holonomy 结果及一个算子不可约步骤作为假设/继承项；这些决定性依赖未闭合。 不得采纳四项线性无关或相关无理性结论；仅记录条件性路线。
- 相关入口。[math-euler-constant-irrationality](../../../math-euler-constant-irrationality/SKILL.md)。
- 第五批定向筛选。hold。The local 2026 preprint makes its logarithm-product conclusions conditional on arithmetic-holonomy and irreducibility inputs. Those decisive inputs were not closed, so no linear-independence claim is reusable. 定位。physical pp. 1-2; 27-page PDF 后续条件。Verify the exact holonomy theorem and the required differential-operator irreducibility for each proposed application.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The source itself makes its logarithm-product independence results conditional on an unrefereed arithmetic-holonomy preprint and an inherited irreducibility step. Its asserted exact/ball certificates are not provided in the PDF bundle, so no independent finite certificate is available.。定位。1, 2。全卷 27 页。后续条件。Pinned certificate data and software, plus a checked version of the holonomy theorem and the order-13 operator irreducibility input.。

## G42 · Linear independence of odd zeta values using Siegel's lemma

- 原件。author preprint dated 2026-03-26; publication status not established。PDF 物理页 1, 2, 4。SHA-256 1576b611c8c0771fb63406274faf022898d568a085f243a469dda1c0f7ece7f5。
- zeta linear independence via Siegel lemma。Abstract; Theorem 1 (physical p.2); Section 2 roadmap (p.4)。声称对充分大奇 s，1 与 ζ(3),…,ζ(s) 的 Q-张成维数至少为 0.21√(s/log s)，路线是非显式 Siegel 引理线性形式、精化线性独立判据和 Shidlovskii 型重数估计。
- 条件或证据待查。新判据、重数估计及常数优化的证明链未逐项复核。 不能把渐近维数下界转用于 γ、单个奇 ζ 值或有限 s。
- 第五批定向筛选。hold。This 2026 author preprint's asymptotic odd-zeta span bound depends on its refined Siegel-lemma criterion and Shidlovskii-type multiplicity estimate; neither proof chain was adopted or independently checked. 定位。physical pp. 1-2, 4; 46-page PDF 后续条件。Audit the non-explicit linear forms, multiplicity estimate, and all parameter ranges before using the stated asymptotic bound.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The author preprint explicitly bases its asymptotic odd-zeta span lower bound on a new refined linear-independence criterion and a Shidlovskii-type multiplicity estimate. The local theorem page is not a finite-s certificate and no independently checked proof chain or parameter certificate is supplied.。定位。1, 2, 4。全卷 46 页。后续条件。Audit the non-explicit Siegel forms, multiplicity estimate, criterion, and asymptotic parameter ranges before any selected application.。

## G42 · Linear independence of values of Dirichlet L-functions

- 原件。arXiv:2512.02612v2 per inventory。PDF 物理页 1, 3, 4。SHA-256 5a4e375dc4a5ee848780175b61d155875d84d7bf0f7db59f45ef90162013b283。
- Dirichlet L-value linear independence。Abstract; introduction remarks and construction roadmap (physical pp.1,3–4)。对 Dirichlet character 的相反奇偶性 L 值，声称在 Q(ζ_{φ(N)}) 上给出约 √(s/log s) 的张成维数下界，并推广 Fischler 的主特征情形。
- 条件或证据待查。依赖精化 Siegel 引理、线性独立判据和 Shidlovskii 型引理，且关联的 Fischler 结果未在本次闭合审计。 不从此推出单个 L 值的无理性，亦不转移到 γ。
- 第五批定向筛选。hold。arXiv:2512.02612v2 is a preprint whose Dirichlet-L span claim imports the same refined Siegel-lemma and multiplicity machinery. It gives neither a direct Euler-constant tool nor a checked standalone finite certificate. 定位。physical pp. 1, 3-4; 36-page PDF 后续条件。Verify the cited Fischler extension, multiplicity lemma, and character/parity assumptions for any selected L-value application.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The local arXiv:2512.02612v2 matches the current record, but its Dirichlet-L span claim rests on non-explicit Siegel forms, a refined criterion, and a Shidlovskii-type lemma. It provides no direct Euler-constant result or standalone finite L-value certificate.。定位。1, 3, 4。全卷 36 页。后续条件。A checked proof of the cited linear-independence and multiplicity steps together with explicit character, parity, and parameter data for a finite application.。

## G48 · Computing hypergeometric functions rigorously

- 原件。arXiv:1606.06977v2 (2016-07-05)。PDF 物理页 1, 7。SHA-256 20467d7a2378c13f48b9e8ceb1e6fc330205c26b4a40cf4903a8b462e6764078。
- rigorous hypergeometric interval computation。Abstract; Theorem 1 (physical p.7)。为 pFq 级数首项后的尾部给出在 p≤q+1 与 Re(b_i+N)>0 条件下的几何级数上界，服务于任意精度区间计算。
- 构件候选。完整算法还依赖参数变换、分支选择及 Arb/实现的定向区间保证；本次未运行或审计代码。 可作为带条件的尾界线索；不能把其实现能力等同于本机现有区间 API 已验证。
- 相关入口。[math-l03-rational-and-interval-certificates](../../../math-l03-rational-and-interval-certificates/SKILL.md)。
- 第五批定向筛选。unresolved。The paper describes an Arb-based arbitrary-precision implementation, but its required implementation/library dependency is not part of this input and no bounded self-contained algorithmic certificate was isolated in this screen. 后续条件。Provide the referenced Arb source/version and a target-function test suite with interval outputs; then distill a verified evaluation interface.
- 复核记录。2026-11-26T18:35:59+08:00。adopted-local。component。
- 本次依据。Physical p. 7 states a self-contained ratio-majorant theorem, and its proof reduces the tail to a geometric series. The exact real-rational tail factor is independently replayed locally.。定位。Theorem 1 and proof, physical p. 7。全卷 27 页。后续条件。For a concrete evaluation, supply the exact hypergeometric summand, a certified value/enclosure for T(N), and directed complex arithmetic if parameters are not rational real.。
- 已采用构件。物理页 7。For a supplied hypergeometric summand, the stated p<=q+1, Re(b_i+N)>0, and D<1 hypotheses certify the explicit geometric tail multiplier; no complex interval implementation is adopted. [方法说明](../../../math-l03-rational-and-interval-certificates/references/g48-hypergeometric-tail-bound-wave8.md)。

## G52 · Transcendence results for Γ^(n)(1) and related sequences of generalized constants

- 原件。arXiv:2511.01849。PDF 物理页 1, 2, 5。SHA-256 d21affc210dfe9ba7d57c6233052be25f165b6ea305ad83f6c4e4cafea49d40b。
- Gamma derivatives and generalized constants。Abstract; identities (5)–(10) (p.2); Theorem 1 (p.5)。定义 γ^(n)、δ^(n)、η^(n) 的 Gumbel 矩序列并陈述偶阶导数的有理张成关系、无穷多 γ^(n) 超越及 γ 与 γ^(2) 的析取超越结论；不推出 γ 自身无理性。
- 条件或证据待查。算术部分使用 Shidlovskii 定理及生成函数论证；其适用和所有外部前提未独立复核。 保留 γ+δ/e=η 型身份的背景，不将析取结论强化为 γ 的结论。
- 相关入口。[math-euler-constant-irrationality](../../../math-euler-constant-irrationality/SKILL.md)。
- 第五批定向筛选。no-adopt。The arXiv:2511.01849v7 source gives useful Gumbel-moment identities, but its gamma-derivative Bell-polynomial content is already represented by the installed gamma recurrence tooling. Its transcendence claims depend on Shidlovskii applications and do not establish irrationality of gamma. 定位。physical pp. 1-2, 5; 15-page PDF 后续条件。A distinct adoption would need a new, fully specified generalized-constant computation not reducible to the existing Bell/gamma-zeta interface.
- 复核记录。2026-11-26T18:35:59+08:00。scoped-reference。statement。
- 本次依据。Physical pp. 2 and 5--6 give Gumbel-moment identities and derivative/transcendence statements, but the finite gamma/Bell recurrence interface already covers the computable derivative content. Its arithmetic conclusions do not decide irrationality of Euler's constant.。定位。Definitions and identities (5)--(10), physical p. 2; Theorem 1 and proof, pp. 5--6。全卷 15 页。后续条件。A new admission needs a fully specified generalized-constant computation that is not reducible to the installed gamma/Bell interface; preserve any Shidlovskii hypotheses for arithmetic claims.。

## G57 · Special values of derivatives of L-series and generalized Stieltjes constants

- 原件。arXiv:1809.06921v1 (2018-09-18)。PDF 物理页 1, 3, 4。SHA-256 48e3914fd94c437e8a4d78a764cdf2031102f4bc2fce04178a192162daeee70c。
- generalized Stieltjes constants and L-derivatives。Abstract; Theorems 1.1–1.2 and Corollary 2 (physical pp.3–4)。把 L′(1,f) 与广义 Stieltjes 常数联系；对 p>7 的结论明确以 Gun–Ram Murty–Rath 猜想为条件，才得到一批 γ_1(a,p) 的超越性。
- 条件或证据待查。决定性的 Conjecture 1 未证明，且 L′(1,f) 到常数的线性关系须保留其周期函数假设。 不转化为通常 Euler 常数 γ 的无理/超越结论，也不删除条件。
- 相关入口。[math-euler-constant-irrationality](../../../math-euler-constant-irrationality/SKILL.md)。
- 第五批定向筛选。no-adopt。The formal Acta Arithmetica 2018 paper (DOI 10.4064/aa170615-13-3) derives its generalized-Stieltjes transcendence count conditional on the Gun-Ram-Murty-Rath conjecture. It is not a statement about ordinary gamma and creates no new unconditional local tool. 定位。physical pp. 3-4; 11-page PDF 后续条件。Any use must retain Conjecture 1 and verify periodic-function, parity, and nonvanishing hypotheses for the specified L-series.
- 复核记录。2026-11-26T18:35:59+08:00。citation。citation。
- 本次依据。The L-derivative/generalized-Stieltjes conclusions are explicitly conditional on the Gun--Ram Murty--Rath conjecture and concern generalized constants rather than ordinary Euler gamma.。定位。Conjecture 1, Theorems 1.1--1.2 and L'(0,f) relation, physical pp. 2--5。全卷 11 页。后续条件。Retain and separately establish Conjecture 1, plus the periodic-function, parity, and nonvanishing hypotheses for any specified L-series before using its count.。

## O22 · A gauge-invariant measure for lattice chiral fermions

- 原件。arXiv:2610.09093v1 (2026-10-06), prepared for JHEP。PDF 物理页 1, 2, 3。SHA-256 45c8d3eaecb57f220a444192220464af64f00e3a15cab1d50c4719f62e934382。
- lattice gauge theory。Abstract; contents (physical pp.1–3)。研究四维 Euclidean lattice 上手征费米子的规范不变测度，并将其作为 Standard Model 的非微扰格点定义候选。
- 归档定位。主构造依赖可接受规范场、局部性和全局可积性条件；未核对证明。 仅目录化物理主题与版本；不蒸馏为当前数学工具。
- 第六批定向筛选。adjacent。The preprint's gauge-invariant lattice-fermion construction is a physics-specific nonperturbative model with admissibility, locality, and global-integrability conditions, outside the current mathematical-tool routes. 定位。Abstract p.1 and contents/scope pp.2--3.。全卷 126 页。 后续条件。Any adoption needs a dedicated lattice-gauge workflow with explicit admissible-field and chiral-projector contracts.

## O24 · Proof by OpenAI of the Existence of Quantum Yang--Mills theory

- 原件。2026-10 shepherding-committee statement (not the proof)。PDF 物理页 1, 2。SHA-256 dbab31f0f954ac8265a3fc1c1a29664c7fa0b7f16c616d58012e65896557bd12。
- quantum Yang--Mills status statement。committee statement, pp. 1--2。委员会仅报告 OpenAI 声称构造含费米子的量子 Yang--Mills 连续极限；同时明确质量隙与禁闭仍未解决，正式证明及 Lean 对应仍待发布和核对。
- 条件或证据待查。该文本本身不含定义、RG 估计或证明；结论依赖尚未公开的 OpenAI 手稿与未来审查。 未阅 OpenAI 原证明、形式化文件或委员会后续评估。
- 第五批定向筛选。no-adopt。This two-page committee statement reports an unreviewed OpenAI claim but supplies neither definitions nor proof artifacts. It explicitly leaves mass gap and confinement unresolved. 定位。physical pp. 1-2; 2-page PDF 后续条件。Wait for a public primary manuscript/formalization and a theorem-level review before any mathematical tool is distilled.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The two physical pages are a shepherding-committee status statement, not a proof: definitions, estimates, primary manuscript, and Lean objects are absent; it expressly leaves mass gap and confinement open.。定位。Committee statement, physical pp. 1--2。全卷 2 页。后续条件。A public primary manuscript or formalization plus theorem-level independent review and replay.。

## O27 · A Proof of the Linear Hadwiger Conjecture

- 原件。arXiv:2610.05291 (PDF first page)。PDF 物理页 1, 2, 5。SHA-256 12075e4195b3f3cd899ab0e2bfdf546144aa68fdbffeb5eec48de15330bfd34e。
- graph minors and colouring。Theorems 2--4; §2.1。对 Hadwiger 数 h(G)<t 的图，作者声称存在绝对 C 使 χ(G)≤C h(G)；路线先处理 |V|≤t(log t)^{1/2-ε}，再用既有归约提升到 polylog 规模。
- 条件或证据待查。关键归约显式依赖 Delcourt--Postle 的定理；小图范围的两个关键引理及 bootstrap 尚未逐项核验。 仅核对开篇定理和 §2.1 路线，未核验关键引理、常数或完整 preprint。
- 第五批定向筛选。hold。The 41-page arXiv:2610.05291v1 preprint's Theorems 4-5 give a clear small-order-to-polylog bootstrap, but adoption would rely on the central Theorem 5 proof and Delcourt-Postle reduction; those proof dependencies were not fully checked in this screening pass. 定位。physical pp. 1-2, 5; 41-page PDF 后续条件。Verify Theorem 5's exponent-boost proof and the exact imported Delcourt-Postle reduction before adding a graph-colouring component.
- 复核记录。2026-11-26T18:35:59+08:00。candidate。dependency。
- 本次依据。The 41-page preprint gives a potentially reusable small-order-to-polylog bootstrap, but its asserted linear Hadwiger conclusion depends on central Theorem 5 and an imported Delcourt--Postle reduction not replayed here.。定位。Theorems 2--5 and Section 2.1, physical pp. 1--5。全卷 41 页。后续条件。Verify the exact Delcourt--Postle version and all hypotheses, then replay the exponent-boost proof of Theorem 5 with its constants.。

## O28 · The occupation time of a random walk generated by the uniform random permutation -- a GPT-6 Astra proof

- 原件。arXiv:2609.25102v1 (20 Sep 2026)。PDF 物理页 1, 2, 3。SHA-256 f23fafe8c40fe263d3158924171a4c8e403a7cf1a8833f5bce7a225db004c78c。
- permutation random walks and arcsine laws。Theorem 0.1; equations (0.3)--(0.7)。对均匀排列诱导的 ±1 路径，奇数时刻正性把占据边数写成 2#{k:T_k>0}；由环形差分构造得到 i.i.d. 连续对称增量 T，遂以 Sparre--Andersen 给出离散 arcsine 分布。
- 构件候选。决定步骤是 U_j 的模一差分 V_j 仍为 i.i.d. Uniform 及由此的路径恒等式；最后调用 Sparre--Andersen。 可作为“排列路径到 i.i.d. 对称增量”的专用转移工具；尚未独立复核变换的测度保持细节和引用定理的适用条件。
- 第五批定向筛选。adopt。The four-page source gives a complete pathwise reduction to i.i.d. continuous symmetric increments and states the final Sparre-Anderson dependency; the adopted scope ends at that reduction and law invocation. 后续条件。For any variant, prove the transformed increments are i.i.d., continuous, and symmetric before invoking Sparre-Anderson.
- 已采用方法。物理页 1, 2, 3。Uniform-permutation ascent walks of even length reduce pathwise to occupation time of an iid continuous symmetric-increment walk. [方法说明](../../../probability-permutation-subset-sums/references/wave5-c08-01-permutation-walk-arcsine.md)。

## O29 · FrontierMath Erdős

- 原件。arXiv:2609.25050 (PDF first page)。PDF 物理页 1, 8, 9。SHA-256 49a0289087c9378b02e0a85cded14cc0ce9d8b43a814065af2e54895eef6babc。
- AI mathematics benchmark。Abstract; Appendix A benchmark list。这是 68 个截至 2026-08 仍开放的 Erdős 问题的 Lean 基准与评测报告，而非某一数学证明；报告称固定预算评测中 GPT-6 Astra 解决比例为 3%。
- 版本与引用。其数学条目是各题的外部定义与 Lean 任务，论文不提供可迁移的通用证明机制。 未逐题审计 68 个形式化任务、模型运行或基准版本。
- 第六批定向筛选。citation。This is a Lean benchmark/evaluation report for 68 externally specified open problems, rather than a mathematical proof component. 定位。Abstract and benchmark protocol p.1; problem-list appendix pages 8--9.。全卷 12 页。 后续条件。Individual benchmark problems require their own source statements, Lean artifacts, and proof review.

## O30 · GPT, the Counterexample Machine

- 原件。PDF dated Aug. 2026; publication status not established from source。PDF 物理页 1, 3, 19。SHA-256 3e79d9cf748c0589ef4dc9ce68ad37ae6c1085e6c9319c29dee767dc59f3380d。
- counterexample cataloguing。Abstract; case-study sections。论文汇集多个由模型协助发现的反例，并以人类说明和部分机器证书组织；其可迁移价值是“先构造候选、再给可复验反例证书”的工作流，不是统一定理。
- 既有方法覆盖。每个反例都依赖其单独的对象定义、计算与仓库证书；不能从目录摘要迁移为一般反例算法。 现有 L02 已规定候选搜索与独立重算/解析证书边界；未逐个核验该文十五余例及关联仓库。
- 相关入口。[math-l02-adversarial-input-search](../../../math-l02-adversarial-input-search/SKILL.md)。

## O31 · What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics

- 原件。arXiv:2610.17090 (PDF first page)。PDF 物理页 1, 2, 8, 22。SHA-256 812f9ea9ffdb64dc754a4cf241533a0b08550a3436e96c0fccf3ef4b2afe703e。
- secondary survey of AI-generated mathematics。Abstract; selected family discussions。二次综述尝试把 OpenAI 发布材料拆成引理、构造、不等式和证明机制，并明确把有效性与新颖性留作后续核验；它是线索索引而非独立证明来源。
- 版本与引用。所有“instrument”均依赖被综述的原始论文；作者也未以本文替代原始论证。 未逐项复核其 38 个问题族与原稿之间的对应关系。
- 第六批定向筛选。citation。This is a secondary survey that labels its extracted instruments as requiring later validity and novelty review. It is an index, not an independent proof source. 定位。Abstract p.1; survey organization p.2; family table p.8; Hilbert--Smith survey discussion p.22.。全卷 56 页。 后续条件。Use the original OpenAI manuscript for each claimed instrument; do not adopt survey prose as a theorem interface.

## O32 · On the proof of Falconer distance conjecture

- 原件。2026 preprint (PDF first page; exact repository version unverified)。PDF 物理页 1, 3, 14。SHA-256 60a892c1f5d0a70d608976e21b88dc232ec68284f385b313072964b3c747e6f3。
- Falconer distance and microlocal energy。Theorem 1.1; §§3--8。声称对紧集 E⊂R^d、dim_H E>d/2 证明距离集有正 Lebesgue 测度；证明组织为距离测度、microlocal Mattila 积分及左右分支区间切割。
- 条件或证据待查。主结论依赖多尺度分支切割、M/E 状态转换及 Proposition 2.2；仅定位章节结构，未核验这些估计。 未检查全部频率分解、端点/紧性处理或与原 OpenAI 证明的实际依赖。
- 第五批定向筛选。hold。This is a third-party explanatory arXiv:2611.13789v1 manuscript, not an OpenAI original. Its Falconer proof depends on Proposition 2.2 and the multiscale M/E transition estimates, which were not checked; existing Frostman preprocessing remains the only admitted local component. 定位。physical pp. 1, 3, 14; 20-page PDF 后续条件。Verify Proposition 2.2 and the full branching-energy induction, or use an audited primary OpenAI source, before extending Falconer tooling.
- 复核记录。2026-11-26T18:35:59+08:00。adjacent。context。
- 本次依据。This is a third-party Falconer exposition. Its source-stated route uses Proposition 2.2 and multiscale M/E transitions that were not verified, while the existing Frostman-energy preprocessing already covers the only local prerequisite isolated here.。定位。Theorem 1.1; Sections 3--8; Proposition 2.2, physical pp. 1, 3, 14。全卷 20 页。后续条件。An audited primary source, or a full replay of Proposition 2.2 and the branching-energy induction including endpoint and compactness conditions.。

## O33 · The satisfiability conjecture for random k-SAT formulas: Human-friendly exposition of the recent OpenAI resolution

- 原件。arXiv:2611.10139v1 (PDF dated 10 Nov 2026)。PDF 物理页 1, 3, 11。SHA-256 c1177271fde645c12e239c4f9b8763143091957c6e925b3c16b1c7ca9fdb820e。
- random k-SAT threshold。Abstract; §3 roadmap and technical propositions。文本阐释随机 k-SAT 的可满足性阈值：固定子句/变量比附近概率急剧转变；其路线讨论条件下解数集中、超可加变体及相变窗口。
- 条件或证据待查。核心阈值论证依赖文中 Proposition 3.7、3.10 及所引用 OpenAI/Carenini 结果，未逐条审计。 未核验一般 k 的定量窗口、原始解析论证或预印本间的版本关系。
- 第五批定向筛选。hold。The arXiv:2611.10139v1 human-oriented k-SAT exposition cites OpenAI/Carenini results and rests on technical Propositions 3.7 and 3.10. It has no independently checked primary threshold proof or finite SAT certificate. 定位。physical pp. 1, 3, 11; 19-page PDF 后续条件。Compare with the cited primary proof, then verify the concentration and superadditivity propositions with all fixed-k and density-window hypotheses.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The human-friendly random k-SAT exposition routes the threshold assertion through cited OpenAI/Carenini work and technical Propositions 3.7 and 3.10; no primary proof or finite certificate is supplied by this source.。定位。Roadmap and technical propositions, physical pp. 1, 3, 11。全卷 19 页。后续条件。Compare the cited primary proof and verify the concentration and superadditivity propositions with fixed-k and density-window hypotheses.。

## O34 · A Note on OpenAI's Construction of Counterexamples to the Kaplansky Direct-Finiteness Conjecture

- 原件。2026 preprint (PDF dated 21 Oct 2026)。PDF 物理页 1, 2, 19。SHA-256 39b63a11775dde74d822328f4faf738dadb6b93a20f780e27e6eee989144915c。
- group algebras and direct finiteness。Abstract; §1 and construction section。作者给出特征 2 非直接有限群代数的说明，并声称可推广为每个素数 p 存在双曲群 G_p 使 F_p[G_p] 非直接有限。
- 条件或证据待查。必须核验群的演示、元素 a,b 的 ab=1≠ba 计算及双曲性证明；这些不由摘要或历史背景推出。 未逐行复算群环乘法或核查其与原 OpenAI 构造的依赖。
- 第五批定向筛选。exclude。SHA matches the local 32-page preprint dated 21 Oct 2026, bibliographically arXiv:2611.08268v1. Its pp.1--5 state the characteristic-p direct-finiteness construction and matrix reduction, but a reusable witness needs the source-specific group presentation, the explicit group-ring a,b product calculation, and the hyperbolicity proof; no finite generic input contract is supplied. 定位。O34 physical pp.1--5, especially the stated reduction through Mat_nd(F_p[G]). 后续条件。Audit the full presentation and ab=1 != ba computation for a named p, then independently check the group-theoretic/hyperbolicity chain before exposing any witness checker.

## O35 · The geometric case of the Erdős Similarity Conjecture: a human exposition of the OpenAI proof

- 原件。arXiv:2611.02454 (PDF first page)。PDF 物理页 1, 2, 4。SHA-256 19f0529a050ee61878889ff77e69248e59e3f8ab64e7ca2b044d8829d581eb84。
- random covering and geometric similarity。Abstract; construction overview。对固定 q∈(0,1)，文本声称构造测度可任意接近 1 的紧集，避免所有平移缩放的 {q^n}；机制是嵌套网格随机树与有限代表 dilation 的并界。
- 条件或证据待查。决定步骤是每个拷贝的独立命中机会、依赖范围控制以及从有限代表到全部 dilation 的离散化；均需完整估计。 可考虑发展为随机树覆盖工具，但尚未核验网格尺度、常数、可数化和极限传递。
- 第五批定向筛选。exclude。SHA matches the local arXiv:2611.02454 preprint. Proposition 2.1 on p.4 is a useful target statement, but the all-dilation conclusion depends on the nested-grid geometry, finite representative net, tree stopping calculation, and exceptional-base-point repair in later sections. None is a standalone finite interface here. 定位。O35 physical pp.1--4; Proposition 2.1 on p.4. 后续条件。A future extraction must fix q,p, all grid and tree parameters, prove the finite-representative-to-continuum cover transfer, and give the exact stopping probability bound.

## O36 · Deterministic Polynomial-Time Primality Testing with a Single Binomial Congruence

- 原件。arXiv:2611.02280 (PDF dated 30 Oct 2026)。PDF 物理页 1, 2, 5。SHA-256 dfdd6e53577a94fede588a075057377c693483ac18fa756b6507331b07b2e8fa。
- primality testing and binomial congruences。Abstract; Theorem 1.1; main congruence discussion。提出在 C_n[X]/(X^r-b(Y)) 检验单一二项式同余；有限域根计数和格界意在推出接受数是素数幂，再排除完美幂。参数构造依赖 Dedekind ζ 的统一零点自由区。
- 条件或证据待查。算法正确性依赖零点自由定理、参数 b 构造、根计数及格界的量化衔接；并非仅靠同余式。 未复算复杂度、输入编码或外部零点自由定理/Lean 声明；不应作为无条件素性工具部署。
- 第五批定向筛选。exclude。SHA matches arXiv:2611.02280v1. Theorem 2.3 on pp.3--5 gives only the conditional acceptance-to-prime-power algebraic criterion after identities (3)--(5) and size condition (8); the advertised deterministic construction of b and L^(32+o(1)) bound rely on the external uniform Dedekind-zeta zero-free theorem and later Jacobi-sum construction. 定位。O36 physical pp.1--5; equations (3)--(8), Lemmas 2.1--2.2, Theorem 2.3. 后续条件。Check the exact version and proof/formalization status of the cited zero-free theorem, then audit parameter construction, input encoding, perfect-power preprocessing, and all complexity bounds before using as a primality algorithm.

## O37 · A remark on the AI proof of the Deligne--Drinfeld conjecture

- 原件。arXiv:2611.01745 (PDF first page)。PDF 物理页 1, 2, 8。SHA-256 afb6f82b5a6694c3f1708d9a61d97533946c631692194348947886d4b03994f6。
- associators in characteristic two。Abstract; Lemma 1.5 and reconstruction discussion。文章把特征 2 论证中的投影/重构解释为 z↦z^2 双覆盖与填补穿孔，并给出归一化 level-two associator 图像上的显式重构。
- 条件或证据待查。依赖 OpenAI 的约化方程、cabling 恒等式及 pro-2 关联子理论；Lemma 1.5 只覆盖其中的 augmentation-algebra 接口。 未核验 associator 定义、重构逆与完整 Deligne--Drinfeld 结论。
- 第五批定向筛选。exclude。SHA matches arXiv:2611.01745. The arrangement augmentation Lemma 1.5 (p.3) and normalized level-two formulas (p.5) are only interfaces to the cited OpenAI reduced/cabling equations and pro-2 associator framework. The existing operator-algebra skill already holds the narrow finite Lie-lattice interface. 定位。O37 physical pp.1--5, Lemma 1.5 and Proposition 2.1. 后续条件。A new transfer would require the exact associator input, cabling identities, coefficient reconstruction inverse, and compatibility with the claimed Deligne--Drinfeld conclusion.

## O38 · Limits and Constants of OpenAI's Claimed ETH Refutation

- 原件。arXiv:2611.00517 (PDF dated Oct 2026)。PDF 物理页 1, 2, 8。SHA-256 a0ee953196f8d0a359809fbe9a0d809c493b9bc69ec4e4dcf5c12e4f7f58a052。
- asymptotic complexity audit。Abstract; constants analysis。该文审查一项 #k-SAT 亚指数时间声称：区分 tensor-contraction 与 interpolation 指数，并指出隐藏常数下有限规模可能不优于 2^n。
- 版本与引用。结论条件于被审查的 OpenAI 算法及作者抽取的常数；它提供尺度审计而非独立 ETH 定理。 未复核原始算法、常数推导或实验性阈值计算。
- 第六批定向筛选。adjacent。This complexity note audits asymptotic constants of another preprint. It supplies scale estimates conditional on that algorithm, not a standalone proof or general computation certificate. 定位。Abstract p.1; algorithm and scope disclaimer p.2; threshold table p.8.。全卷 29 页。 后续条件。Re-use would require the original tensor-contraction proof, fixed cost model, and independent derivation of every hidden constant.

## O39 · Proof of the Harary--Hill conjecture: an exposition

- 原件。arXiv:2610.34444 (PDF dated 6 Nov 2026)。PDF 物理页 1, 2, 9。SHA-256 8eb7d67e87163d02a37e32ae18ac3ac7967a4a52255d758576584547351209ea。
- graph crossing numbers。Abstract; introductory reduction discussion。文本声称任意 K_n 绘制的交叉数等于经典 floor-product，并将 OpenAI 论证改写为较短的 exposition，还讨论其他图族的推论。
- 条件或证据待查。完整下界需核验 drawing reductions、关键计数不等式和所有 n 的边界情形；本次未完成。 未核验原 proof、计算辅助小 n 情形或导出图族结论。
- 第五批定向筛选。exclude。SHA matches the local 16-page preprint dated 6 Nov 2026. The headline lower crossing-number statement on p.1 is obtained through drawing reductions and a global crossing-counting argument. The small displayed constructions do not give an input-parameterized finite certificate usable independently of those reductions. 定位。O39 physical pp.1--3, Theorem 1 and start of its proof. 后续条件。Audit the drawing model, reduction lemmas, all-n counting inequality, and boundary cases before extracting a crossing-number tool.

## O40 · On OpenAI's proof of the Nagata conjecture

- 原件。arXiv:2610.30050v1 (PDF first page)。PDF 物理页 1, 3, 9。SHA-256 347c49db68edac09689c18fd5a31ac30fe2ffd726505730258e744c23899a9ce。
- algebraic geometry and interpolation。Abstract; Proposition 2.4 examples。路线把一般点的 fat-point 插值转为退化椭圆曲线/正常锥上的单项式方案，最终到三角晶格点插值；样例将满秩矩阵用于排除指定次数曲线。
- 条件或证据待查。决定依赖 theta 函数结点退化、插值对偶与 Proposition 2.4 的秩结论；图示有限矩阵例子不能替代一般点定理。 未核验退化族、genericity、矩阵秩一般证明或与原稿的对应。
- 第五批定向筛选。exclude。SHA matches arXiv:2610.30050v1. The fat-point interpolation route depends on a degeneration family, theta-function nodes, genericity, dual interpolation, and a general-rank theorem. A finite matrix example cannot certify the generic Nagata step. 定位。O40 physical pp.1, 3, 9; Proposition 2.4 examples. 后续条件。Verify the degeneration family and Proposition 2.4 with its genericity and rank hypotheses, then compare it to the original OpenAI proof before any reusable interpolation interface.

## O41 · Brennan's Conjecture and the Universal Integral Means Spectrum

- 原件。arXiv:2610.23853 (PDF first page)。PDF 物理页 1, 2, 3。SHA-256 415931c428e582ec42c0df3204b93dac57fcb7aaaf022753e2d858ee7b9150a5。
- conformal integral means spectrum。Abstract; equations (4)--(5) and §1.2。作者称在验证两份 OpenAI 预印本时得到更短且更强的谱结果；论证用对数超调和的势、临界点目标映射、Jacobian 符号和加权有向面积不等式。
- 条件或证据待查。主结论依赖势函数构造、临界值计数和 signed-area 不等式；原文也将背景中的 OpenAI 预印本作为前置。 未逐项核验 Brennan 范围、Kraetzer 反例或所有解析边界条件。
- 第五批定向筛选。exclude。SHA matches arXiv:2610.23853. The claimed integral-means spectrum improvement depends on a logarithmic-superharmonic potential, critical-value accounting, Jacobian sign, and signed-area inequality, with OpenAI preprints as inputs. The source does not isolate a finite checkable component with independent scope. 定位。O41 physical pp.1--3; introduction and displayed spectrum equations (4)--(5). 后续条件。Audit the potential construction and every boundary/critical-point hypothesis, then verify the signed-area estimate and the cited OpenAI dependencies at their precise versions.

## O42 · Primes between 8th powers?

- 原件。2026 preprint (PDF first page)。PDF 物理页 1, 4, 5。SHA-256 af0717cf0727451bc842f985e5186521cd2c7fe34799873cc7d7355ecc5d8ba2。
- conditional prime gaps。Abstract; conditional implications。在假定所称 7/8 版 quasi-Riemann hypothesis 成立时，文章推出每个 n 的 (n^8,(n+1)^8) 等区间含素数及更短区间版本。
- 条件或证据待查。所有新结论条件于未在本文证明的 QRH 声称；需要显式公式和误差项才可审计。 未核验 QRH 来源、零点范围、有限 n 检查或不等式常数。
- 第五批定向筛选。exclude。SHA matches the local 11-page preprint. Its p.4 eighth-power interval statement is explicitly conditional on the asserted QRH_7/8 and uses imported explicit Chebyshev-function bounds. It provides no unconditional prime-gap method. 定位。O42 primes preprint physical pp.1--5; QRH assumptions on p.3 and theorem (3.1) on p.4. 后续条件。Verify the QRH source and the explicit-formula/error constants, then separately certify the finite numerical range before using a conditional interval conclusion.

## O42 · Polynomial Separation of a Shared Tensor Leg and Matrix Multiplication in Arbitrary Characteristic

- 原件。2026 preprint (PDF dated 9 Oct 2026)。PDF 物理页 1, 2, 4。SHA-256 b9f5231c18a786b07819150152072c75ddb50caf68453c57538c92b9fe34567f。
- tensor degeneration and polynomial separation。Abstract; §1 replacement; characteristic discussion。对共享第一空间而其余 matched sectors 独立的 M 个 tensor blocks，文章声称以 M+n−1 个和块退化为带 n 维 dot-product 的全直和；构造避免单位根/阶乘分母，并拟将矩阵乘法指数上界延至任意特征。
- 条件或证据待查。核心是多项式插值与截断局部代换的 degeneration 证书；最终 ω≤9/4 另依赖引用预印本的谱/离散增长论证。 未核对 degeneration 的边界项、域中不同元素数量、任意特征转移或引用论文的关键依赖。
- 第五批定向筛选。adopt。SHA matches the local 5-page preprint dated 9 Oct 2026 and identified as arXiv:2610.18914v1. Proposition 2.1 on pp.2--3 is a self-contained, finite shared-leg separation construction using polynomial evaluation and truncated substitution. It replaces the installed Fourier separator when the field has at least M+n-1 elements and avoids roots of unity and factorial denominators. The later omega <= 9/4 claim in pp.4--5 is expressly not adopted because it depends on the cited OpenAI spectral, discrete-growth and detecting-character chain. 定位。O42 polynomial-separation preprint, arXiv:2610.18914v1, physical pp.1--3, Proposition 2.1 and equations (2.1)--(2.4). 后续条件。For a concrete tensor use, provide the matched-sector tensor A, its three-leg spaces, a field with at least M+n-1 distinct elements, and explicit polynomial-multiplication restriction/rank accounting. Independently prove every subsequent character or exponent step.
- 已采用方法。物理页 1, 2, 3。For M matched tensor blocks A_h:X x Y_h x Z_h over a field containing at least M+n-1 distinct elements, degenerate A^(direct sum M+n-1) to direct-sum_h(A_h tensor B_X(n)). Use only with supplied matched Y_h/Z_h sectors, explicit distinct field points, and the polynomial-multiplication rank restriction. It avoids the Fourier separator's root-of-unity and characteristic assumptions. It does not certify the source's spectral inequality, entropy passage, detecting-character argument, or omega <= 9/4 headline. [方法说明](../../../math-l06-tensor-rank-accounting/references/c08-03-polynomial-shared-leg-separator.md)。

## O43 · Finite-Time Blowup for Navier--Stokes with Smooth Forcing, Part I

- 原件。2026 preprint (PDF first page)。PDF 物理页 1, 2, 5。SHA-256 fed9da4bbcdb3deb0c37da1139275db9d97724730d4b4f6c5f4004c9631a6551。
- forced Navier--Stokes similarity construction。Abstract; contents and leading-order construction。Part I 声称构造轴对称近自相似背景场，残差分为散度形式项与在固定 similarity sectors 平坦的余项，并以 admissible stress/shear cone 为接口。
- 条件或证据待查。后续结论依赖 Part II 的振荡脉冲残差校正及长篇 profile/stress 估计；Part I 本身未证明最终 blowup。 未核验全部 182 页构造、PDE 正则性、cone 条件或 Part II 拼接。
- 第五批定向筛选。exclude。SHA matches the local 182-page Part I preprint. The paper supplies a profile/stress construction and cone interface, but its own introduction says the final residual cancellation requires later oscillatory-pulse work. Part I alone is not a blowup proof or a portable PDE certificate. 定位。O43 Navier--Stokes Part I physical pp.1--5 and p.8, especially equations (1.5), (1.13)--(1.15). 后续条件。Audit all profile regularity, moment corrections, uniform cone estimates, and the Part II pulse/gluing construction before considering a scoped PDE interface.

## O43 · Self-similar swirl between contracting porous walls: the GD1998 exact Navier--Stokes solution revisited

- 原件。preprint dated 15 Sep 2026。PDF 物理页 1, 4, 17。SHA-256 a38af23a5873e7671ecf0bcd7f3d4c45851c67689a7551ae0e51203ba166fe95。
- computational fluid comparison。Abstract; §§4--7 roadmap。文章把旧的 porous-wall exact swirl 与所称 OpenAI 强迫爆破相似变量比较，并报告 Chebyshev collocation、continuation、manufactured/resolution checks 与一个负结果。
- 版本与引用。数值比较依赖离散化、Newton/continuation 参数和公开代码；它不能验证强迫 Navier--Stokes 有限时爆破。 未重跑数值、检查误差证书、或核验与 OpenAI profile 的变量字典。
- 第六批定向筛选。candidate。The preprint reports a potentially reusable Chebyshev-collocation/continuation diagnostic, but its own physical pages show unresolved wall-layer eigenvalue nonconvergence, so no validated component is extracted. 定位。Abstract p.1; numerical workflow p.4; unresolved mode variation p.17.。全卷 31 页。 后续条件。Need source code, parameters, residual definitions, convergence criterion, and a numerical error certificate that resolves the stated instability.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The preprint's collocation/Newton/continuation comparison is explicitly numerical and its own wall-layer eigenvalues fail to converge under refinement and mapped grids, so it supplies no validated PDE diagnostic component.。定位。physical p. 1 (preprint objective); p. 4 (numerical workflow); p. 17 (unresolved grid-dependent eigenvalues)。全卷 31 页。后续条件。Obtain code, exact discretization/continuation parameters and residual norms, then supply a directed numerical error certificate resolving the wall-layer mode instability.。

## O43 · The Erdős--Sós Conjecture: A Visual Exposition of the Proof Discovered by GPT-6 Astra

- 原件。preprint dated 25 Sep 2026。PDF 物理页 1, 2, 8。SHA-256 1104c7598fb0102413e87dd0712087d2e7715d538e3e187a270160715b4afc3b。
- extremal tree embedding。Theorem 1; reveal-and-stop exposition。声称平均度大于 t−2 的有限简单图含每棵 t 顶点树；正文以随机顶点序、early neighbors、reveal-and-stop 与交换组织归纳。
- 条件或证据待查。需要核验跳边/期望计数引理到所有树的归纳闭合；视觉化例子不构成一般证明。 未逐步审计归纳、严格阈值与所谓 Lean 对应文件。
- 第五批定向筛选。exclude。SHA matches the local 27-page visual exposition dated 25 Sep 2026. It restates the same Erdős--Sós tree-embedding route as O43 but provides worked visual cases rather than a distinct general-purpose proof interface. The more compact O43 source already contains the formal jumping-edge statement. 定位。O43 visual exposition physical pp.1--3 and worked reveal-and-stop setup. 后续条件。Use the O43 formal theorem route if a finite tree-embedding contract is later created; do not treat visual examples or an asserted Lean correspondence as a general proof certificate.

## O43 · The Erdős--Sós Theorem

- 原件。preprint dated 17 Sep 2026。PDF 物理页 1, 2。SHA-256 65c23edb27fe836023ea27fd6c176c43748a88bffd46d8cc8ef4f057a77b428d。
- extremal tree embedding。Theorem 1; introductory reductions。这是 Erdős--Sós 声称证明的短 exposition；它区分 minimum-degree 贪心结论与平均度严格阈值的真正难点。
- 条件或证据待查。中心证明依赖引用的 GPT-6 Astra/Lean 结果和文中未在本次逐节复核的计数论证。 未核验主证明、Lean 工件或所有 t≥2 的边界情况。
- 第六批定向筛选。hold。The exposition states the Erdős--Sós theorem but attributes the proof and Lean verification to external GPT-6/FrontierMath artifacts not physically available here. Its introductory greedy argument only proves a stronger minimum-degree case. 定位。Theorem 1 and contrast with the greedy minimum-degree reduction p.1; Ramsey consequence p.2.。全卷 7 页。 后续条件。Require the cited primary proof/Lean repository and a theorem-to-artifact replay covering every t>=2 boundary case.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The short Erdős--Sós exposition attributes its claimed proof and Lean verification to unavailable external artifacts. Its elementary greedy discussion addresses only a stronger minimum-degree premise, not the average-degree theorem.。定位。Theorem 1 and minimum-degree contrast, physical pp. 1--2。全卷 7 页。后续条件。The cited primary proof/Lean repository and a theorem-to-artifact replay covering every t>=2 boundary case.。

## O43 · A short proof of the Erdős--Sós Conjecture

- 原件。preprint dated 8 Oct 2026。PDF 物理页 1, 2, 5。SHA-256 7c0c00147aef984df69ea90b5c11f71ccf3a1f049cb13c4b463dbf44e9a8427d。
- extremal tree and oriented-tree embedding。Theorems 2, 4--6, 8。以随机排序中的 T-jumping edges 给出树嵌入证明，并扩展到反定向树和 Eulerian 有向树；定理还声称刻画若干极值图。
- 条件或证据待查。关键是随机排序下 jumping-edge 期望下界及额外的 Eulerian 引理；其证明和外部原结果均未完全核验。 未复核全部树方向、极值分类、或与另两篇 exposition 的版本/依赖关系。
- 第五批定向筛选。exclude。SHA matches the local 14-page preprint dated 8 Oct 2026. Theorem 7's jumping-edge expectation proof on pp.3--4 is an interesting self-contained exposition, but a separate tree-embedding skill would overlap the specialized source theorem and needs a clear input contract for host graph, rooted target tree, ordering involution, and induction witness data. No existing target skill owns that contract. 定位。O43 short proof physical pp.1--5; Theorems 7--8 and their proofs. 后续条件。If this becomes a new skill, formalize the finite graph/tree input and exact jump predicate, independently check the induction and involution for all root-degree cases, and retain directed/Eulerian extensions separately.

## P10 · Méthode de Mahler : relations linéaires, transcendance et applications aux nombres automatiques

- 原件。arXiv:1508.07158v2 (28 Oct 2016)。PDF 物理页 1, 8, 9。SHA-256 d44bec7a6c2b016d4a65971e60e583a9d013e8389948c52393911f5b12b7e7dd。
- Mahler functions and specialization。abstract; Proposition 2.1。研究 Mahler 函数在非奇异代数点的代数/线性关系专门化；Proposition 2.1 把小代数点的值关系提升为函数域关系，前提含超越度保持与正则扩张。
- 版本与引用。全局结论依赖 Philippon/Nishioka 型专门化结果与 Mahler 函数方程迭代；并不直接给 E-functions/M-functions 的 2025 结果。 输入目录题名混合了另一来源；未核对期刊版、E/M-function 论文或该方法与 γ 的直接接口。
- 第六批定向筛选。existing。Mahler specialization/relation lifting is already covered by math-euler-constant-irrationality and math-hankel-pade-certificates with a newer published primary route. This French survey/tutorial adds no nonduplicate executable interface. 定位。Abstract p.1; local-to-global transport discussion p.8; Theorem 3.1 relation-lifting statement pp.10--11.。全卷 46 页。 后续条件。Use the existing Mahler admission only after a homogeneous equation, a regular algebraic in-disk point, and full-orbit nonsingularity are proved.

## P14 · Open Diophantine Problems

- 原件。arXiv:math/0312440v2 (24 Jan 2004)。PDF 物理页 1, 2, 17。SHA-256 2d3283afda1f3997c1a7a190a7b6a41ace5ca86ad02ab83575ee47c5d363729c。
- Diophantine and transcendence problem survey。Abstract; contents; selected approximation discussion。这是一份 2004 年问题综述，覆盖丢番图方程、逼近、超越、height 等；它可作历史问题定位，不能当作当前状态或新证明工具。
- 版本与引用。各开放问题与结果依赖被引用文献，且二十余年后状态可能已变化。 未做逐题现代文献更新，也未将其开放问题直接用于现有研究路线。
- 第六批定向筛选。citation。Physical pp. 1--2 identify a 2004 open-problem survey; it supplies historical problem taxonomy, not a current theorem or a gamma approximation/linear-form construction. The checked p. 17 discussion concerns Waring and Mahler/Z-number questions, not Euler's constant. 定位。Abstract and contents, physical p. 1; example discussion, physical p. 17.。全卷 58 页。 后续条件。For any listed open problem, use a current primary result and separately verify whether it concerns the target constant.

## P16 · Galois theory, motives and transcendental numbers

- 原件。arXiv:0805.2569v1 (2008)。PDF 物理页 1, 2, 7, 10。SHA-256 9f6b09cc598dd4e644f3b8c2c3c842794699e76bb3137b83db3f1fcfbad051e5。
- motive-period conjectures。§§2,4.1,5.6–5.7。综述以动机 Galois 群描述周期的预期代数关系；对 log(q)、π 与奇 ζ 值的强独立性结论在文中明确是 Grothendieck 周期猜想的推论。
- 版本与引用。核心等式依赖未证的周期猜想及动机范畴；不是可直接产生 γ 整数线性形式的定理。 未逐章核对其动机形式主义；只核对了与周期猜想和 ζ/log 示例有关的段落。
- 相关入口。[math-euler-constant-irrationality](../../../math-euler-constant-irrationality/SKILL.md)。
- 第六批定向筛选。candidate。The motive-period discussion makes the stated algebraic-independence consequences explicitly conditional on Grothendieck's period conjecture. It treats rational Gamma values, logarithms, and odd zeta values, but gives no realization of Euler's constant as a covered period or any integer linear form for it. 定位。Grothendieck period conjecture, physical p. 7; Gamma/log/zeta consequences, physical p. 10.。全卷 13 页。 后续条件。A proved realization of Euler's constant in the relevant motivic period category plus an unconditional theorem covering it.
- 复核记录。2026-11-26T18:35:59+08:00。citation。citation。
- 本次依据。This survey explicitly presents its period-Galois consequences under Grothendieck's period conjecture and gives no Euler--Mascheroni realization or integer linear form. It is contextual, not an unconditional callable theorem.。定位。physical pp. 7-9 (period torsor and conjecture); p. 10 (Gamma-value examples and conditional consequences)。全卷 13 页。后续条件。Require a proved motivic realization of the target plus an unconditional period theorem; do not route an Euler-constant question through the conjectural discussion.。

## P18 · Transcendence and linear relations of 1-Periods

- 原件。arXiv:1805.10104v8 (2022)。PDF 物理页 1, 2, 17。SHA-256 9a77cbc0c31b4e32f920f7f6dc432e50b89393fa1b4081ef73643f94623f46cd。
- 1-motive periods。Abstract; Chs. 1,9–13。专著给出 Deligne 1-motive 周期的超越性、Q 线性关系和周期空间维数的完整描述，属于 1-周期框架。
- 版本与引用。结论经解析子群定理和 1-motive 比较；适用对象是代数 1-形式沿路径的周期，未给出 γ 的此类实现或整数逼近接口。 未审阅全部 237 页的分类公式；未验证其是否可对 γ 给出新接口。
- 相关入口。[math-euler-constant-irrationality](../../../math-euler-constant-irrationality/SKILL.md)。
- 第六批定向筛选。adjacent。The monograph's abstract and introduction give a complete framework for periods of algebraic 1-forms along algebraic paths, including transcendence and Q-linear relations. The checked source does not identify Euler's constant as such a 1-period or derive an integer approximation interface for it. 定位。Abstract, physical p. 2; Chapter 1 period-integral setup, physical p. 17.。全卷 237 页。 后续条件。A verified 1-motive/relative-period representation of Euler's constant with its path, form, and field of definition.

## P19 · Exponential periods and o-minimality

- 原件。arXiv:2007.08280v4 (2025)。PDF 物理页 1, 2, 6。SHA-256 c482d3abac6921cb919c27b626a95dbe0ddd03e55a3874ef13ccf5ec27ee998f。
- exponential periods。Theorem 0.1 / Theorem 12.4。在 k 对 k∩R 代数的条件下，证明 naive、cohomological 与 exponential-Nori 三类指数周期一致，并把实虚部表成相应 o-minimal 可定义集的体积。
- 版本与引用。等价证明依赖快速衰减同调、twisted de Rham 比较和可定义三角剖分；这是对象刻画，不提供 γ 的近似或无理性判据。 仅检查主定理和技术障碍说明，未逐一审计比较定理的所有前提。
- 相关入口。[math-euler-constant-irrationality](../../../math-euler-constant-irrationality/SKILL.md)。
- 第六批定向筛选。adjacent。Theorem 0.1 classifies several notions of exponential period under k algebraic over k intersect R, and the paper explains its rapid-decay/de Rham comparison dependencies. This is an object-characterisation result; no gamma representation, denominator statement, or small linear form follows from it. 定位。Theorem 0.1, physical p. 2; technical comparison dependencies, physical pp. 6--7; Theorem 12.4, physical p. 69.。全卷 72 页。 后续条件。An explicit exponential-period representation of the target and an independent arithmetic approximation/denominator mechanism.

## P21 · Algebraic independence of the exponential and Weierstrass ℘-functions

- 原件。arXiv:2609.15294v1 (2026-09-14)。PDF 物理页 1, 2, 3。SHA-256 8ababca8ca341314e929a25f4b89030bbafe8935356a6329349b4cbb014423f8。
- semi-elliptic algebraic independence。Theorem 0.1; §§1–2。对具有代数不变量且有 CM 的格，若 t_i 在 Q 上、p_j 在端同态域上分别线性无关且均代数，则 e^{t_i} 与 ℘(p_j) 合在一起代数无关。
- 条件或证据待查。预印本证明诉诸相应 1-motive 的幂零根 Lie 代数的 Tannakian 描述，并且 CM 与输入的代数性不可删去。 仅检查 v1 的主定理和开头证明路线；未独立复核所引 1-motive Lie 代数结果，也与 γ 无直接连接。
- 第六批定向筛选。adjacent。The preprint states algebraic independence of selected exponential and Weierstrass values under algebraic invariants, CM, and linear-independence hypotheses. The target constants and hypotheses are disjoint from Euler's constant, and its proof route is through the stated 1-motive/Tannakian decomposition plus imported classical results. 定位。Theorem 0.1 and hypotheses, physical pp. 1--3; imported Philippon--Wüstholz and Lindemann--Weierstrass inputs, physical p. 2.。全卷 12 页。 后续条件。A target-specific bridge to the allowed exponential/elliptic values, or a separately checked theorem for a representation of Euler's constant.

## P25 · Sur la nature arithmétique des valeurs de fonctions modulaires

- 原件。Astérisque 245 (1997), pp. 105–140。PDF 物理页 1, 2, 3。SHA-256 b59b4644da9387d5144bb357609c0c656518bf37fd032be6af24fb7e293d0eb0。
- modular-function transcendence survey。Introduction; Théorème 1。综述 Schneider 的代数点 j 值定理、Mahler 型问题与 Ramanujan Eisenstein 级数值的超越度结果。
- 版本与引用。它主要转述 Schneider、Barré-Sirieix–Diaz–Gramain–Philibert 与 Nesterenko 的定理；没有 γ 的线性形式或误差尺度。 目标读段为引言与第一定理；未核对全部历史引文版本。
- 第六批定向筛选。citation。The checked pages are a Bourbaki survey introduction and a statement of Schneider's algebraic-point j-value theorem. Its modular-function results are attributed to the cited primary works and provide no Euler-constant approximation or linear-form tool. 定位。Survey identity, physical p. 1; introduction and Schneider theorem, physical pp. 2--3.。全卷 37 页。 后续条件。If modular-function transcendence is needed, use the cited primary theorem with matching hypotheses.

## P27 · On the criteria for linear independence of Nesterenko, Fischler and Zudilin

- 原件。arXiv:0912.4904v1; Chamchuri J. Math. 1 (2009)。PDF 物理页 1, 2, 3。SHA-256 3afe3013c605a88ac90c5b8b7d6e2df25b08f139c19ffc9fbea2593aa92e0e5e。
- integer linear-form criteria。Theorems 1.1–1.2; §2。给出 Siegel、Nesterenko 及 Fischler–Zudilin 型整数线性形式判据：系数高度与非零值的双侧指数控制可推出目标数的 Q 线性维数下界。
- 构件候选。应用必须对同一无穷序列证明整系数、下界和上界，以及 σ(n+1)/σ(n)→1；仅有数值小余项或有限秩不能代入。 尚未把任一 γ 构造验证为满足该判据；后续应只蒸馏明确版本及必要量词。
- 相关入口。[math-euler-constant-irrationality](../../../math-euler-constant-irrationality/SKILL.md)。
- 第五批定向筛选。adopt。Published article; its proof gives a concrete Minkowski convex-body bound on coefficient/linear-form parameters. The adopted interface records only this finite-dimensional criterion. 后续条件。For a new instance, provide integer coefficient forms, nonvanishing values, growth bounds A_n,B_n,Q_n, and the rank/number-of-forms parameters.
- 已采用方法。物理页 1, 4, 5, 6, 7。Integer linear forms with the source's A_n, B_n, Q_n and rank hypotheses yield the stated quantitative coefficient lower bound via a Minkowski body. [方法说明](../../../math-integer-linear-form-rates/references/wave5-c08-01-nesterenko-fischler-zudilin.md)。

## P28 · A geometric introduction to transcendence questions on values of modular forms

- 原件。arXiv:2011.14401v1 (2020)。PDF 物理页 1, 2, 8。SHA-256 bf3017cb71ede0c21b94c0774ccc7a2009d9a43ab335df6bff9f8706ae2adb37。
- modular-form transcendence survey。Theorems 1.1, 3.1–3.2。讲解 Ramanujan 微分方程、Nesterenko 的代数独立性及其对 j 值和椭圆周期的解释。
- 版本与引用。主结论是对既有 Nesterenko 与 Mahler 型结果的说明，D-property/zero lemma 路线要求专门微分系统；未构造 γ 的所需对象。 未审计该讲义的完整证明草图和全部参考文献。
- 第六批定向筛选。citation。This is an expository source for Nesterenko, Mahler, and modular-form transcendence. The displayed results concern q, Eisenstein-series and modular values; the paper points readers to the primary source and supplies no target-specific gamma construction. 定位。Theorem 1.1 and exposition status, physical pp. 1--2; Theorems 3.1--3.2, physical p. 8.。全卷 27 页。 后续条件。Use the underlying primary theorem only after matching a target object to its differential-system hypotheses.

## P29 · Linear independence measures for Chowla–Selberg periods

- 原件。4-page author addendum; formal publication/version unverified。PDF 物理页 1, 2, 3。SHA-256 6c378e7a1b03e0f1be1018a2110621af4a7395bbdd49fd2dc8f9504079862d0c。
- simultaneous hypergeometric Padé。Abstract; Theorem 1。对四组特定 (D,d)，由 3F2 的同时 Padé 逼近给出 1、π√d、Ω_D/π、π/Ω_D 的整数线性形式下界，指数 μ_{D,d} 明确。
- 版本与引用。论证实质依赖作者早先论文的 Ramanujan 型 1/π 公式、显式同时 Padé 构造和 Chowla–Selberg CM 评价；参数表不是一般模板。 未复核所引旧论文的 Padé 系数和渐近估计；与 γ 仅有方法类比。
- 相关入口。[math-gamma-multiple-laguerre-approximants](../../../math-gamma-multiple-laguerre-approximants/SKILL.md)。
- 第六批定向筛选。adjacent。Theorem 1 gives an explicit four-constant linear-independence measure for four listed (D,d) pairs, from simultaneous Pade approximants to 3F2. The note declares itself an addendum to its 2005 source and says its arithmetic proof must be adapted for f2, so the present four pages do not independently establish a reusable general Pade/integrality interface. Its constants are Chowla--Selberg periods and pi, not Euler's constant. 定位。Abstract and dependence on [10], physical p. 1; Theorem 1 and denominator caveat, physical p. 2; explicit CM evaluations, physical p. 3.。全卷 4 页。 后续条件。Read and verify the cited 2005 Pade construction, its modified denominator proof for f2, and a separate Euler-constant specialization before adoption.

## P31 · La fonction zêta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs

- 原件。arXiv:math/0008051v1 (2000)。PDF 物理页 1, 2, 3, 4。SHA-256 f9921534f4a2fc32b4579ed01e9791db3b8b2b8545f669385efd4957eaf927c6。
- odd-zeta hypergeometric linear forms。Lemme 1; §3 proof of Théorème 1。构造 S_n(1) 的有理函数级数并利用对称性消去偶 ζ，清分母后得到奇 ζ 的整数线性形式；结合 Nesterenko 判据给出维数至少按 log(a) 增长。
- 构件候选。结论同时需要偏分式恒等式、积分/鞍点渐近、LCM 整性和判据的两侧尺度；该论文不涉及 γ。 尚未提取可执行的通用参数化或复核所有引理的渐近常数。
- 第五批定向筛选。adopt。The four-page preprint contains the stated linear-form construction, integrality normalization, and the Nesterenko-criterion deduction. The adoption is limited to its displayed lower-dimension-bound parameter transfer. 后续条件。For reuse, independently provide the rational functions, integer normalization, asymptotic alpha/beta bounds, and a valid linear-independence criterion invocation.
- 已采用方法。物理页 1, 2, 3, 4。The supplied normalized zeta linear forms and asymptotic alpha/beta estimates feed a Nesterenko-style lower bound for the rational span dimension. [方法说明](../../../math-integer-linear-form-rates/references/wave5-c08-01-rivoal-odd-zeta.md)。

## P32 · Irrationalité d’une infinité de valeurs de la fonction zêta aux entiers impairs

- 原件。2002 scan; authors Keith Ball and Tanguy Rivoal; formal publication/version unverified。PDF 物理页 1, 2。SHA-256 53b13a8f8c6db6fe97085f92e8c6831060e970ff61124e858ff85c10f0a10a57。
- odd-zeta simultaneous Padé linear forms。Introduction; Théorèmes 1–2。证明 δ(a)=dim_Q⟨1,ζ(3),…,ζ(a)⟩ 至少为 (1/3)log a，并渐近达到 log(a)/(1+log 2)；还给出某奇 j≤169 使 1、ζ(3)、ζ(j) 线性无关。
- 构件候选。路线以 Nikishin 型多对数第一类 Padé、奇偶消去、分母控制与 Nesterenko 判据组成；每项缺失都不能推出维数下界。 只核对扫描件引言和两条主定理；尚未逐页复核后续 Padé 系数和渐近优化。
- 第五批定向筛选。unresolved。The assigned supplement's text encoding is not reliably extractable with the available bundled reader, so its difference from the preceding zeta source and its internal dependency chain cannot be established from this pass. 后续条件。Provide a searchable/OCR-clean copy or a publisher PDF; compare theorem statements, normalization, and proof dependencies against P31 before adoption.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The 17-page scanned Ball--Rivoal supplement is not reliably machine-readable in the available source copy, so neither its precise theorem normalization nor the Padé/integrality/asymptotic dependency chain was verified.。定位。Scan identity and stated introductory theorems; physical pp. 1--17。全卷 17 页。后续条件。A searchable authoritative copy or a manual page-verified transcription, followed by comparison with P31 and replay of the Padé coefficients, denominator control, and Nesterenko criterion.。

## P36 · The Unbounded Denominators Conjecture

- 原件。arXiv:2109.09040v4 (2024-09-16)。PDF 物理页 1, 2, 3。SHA-256 9bffb12953db37d237e75451ed659219d955bf57d55da8dbc09ad888f62956ad。
- noncongruence modular forms。Theorem 1.0.1; Introduction。证明：具有整数 q^{1/N} 展开、有限指标群变换律且尖点亚纯的上半平面全纯函数必为某同余子群的模形式；等价地排除非同余模形式的有界分母。
- 版本与引用。证明需要算术 holonomicity、Nevanlinna 第二主定理、SL2(Z[1/p]) 同余子群性质及 Fuchsian 一致化；与 γ 的逼近对象不同。 未逐节审计 v4 的长证明或正式发表版本与 v4 的差异。
- 第六批定向筛选。adjacent。The checked preprint theorem proves the unbounded-denominators conjecture for functions with the exact modular transformation, q-expansion integrality, and cusp-meromorphic hypotheses. The arithmetic-algebraisation mechanism is tied to modular forms; no target gamma q-series satisfying those hypotheses is supplied. 定位。Theorem 1.0.1 and contrapositive, physical p. 2; arithmetic-algebraisation discussion, physical p. 3.。全卷 62 页。 后续条件。A concrete target q-series with all Theorem 1.0.1 hypotheses and a proof that its conclusion yields a relevant arithmetic statement.

## P40 · Zur Approximation der Exponentialfunktion und des Logarithmus I

- 原件。K. Mahler, J. reine angew. Math. 166 (1931)。PDF 物理页 1。SHA-256 9396946fb3a6dad9c6ef85a4957c15cb0aa0a64636f692fb87596aecd7c639f5。
- classical exponential-logarithm approximation。title page。Mahler 关于指数函数与对数逼近的第一部分，扫描首页确认论文身份与期刊卷年。
- 版本与引用。本轮只核对身份，未提取定理及其假设；不能据此把经典逼近法转写为 γ 的无理性工具。 扫描文字不可机器提取，未审阅正文公式和版本关系。
- 第六批定向筛选。hold。The physical PDF is a scan. Visual inspection of physical p. 1 verifies Mahler's 1931 Part I bibliographic identity, but no theorem, auxiliary function, error estimate, or hypotheses were transcribed and checked from the actual scan. 定位。Title page, physical p. 1 (image scan).。全卷 20 页。 后续条件。A searchable authoritative text or a manually transcribed, page-verified theorem and proof segment with its approximation and integrality conditions.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The 20-page Mahler Part I source is an image scan. Physical p. 1 establishes bibliographic identity only; no theorem, auxiliary function, error bound, or integrality condition was transcribed and checked.。定位。Title page, physical p. 1。全卷 20 页。后续条件。A searchable authoritative text or manually transcribed, page-verified lemma chain with approximation and coefficient-arithmetic hypotheses.。

## P40 · Zur Approximation der Exponentialfunktion und des Logarithmus II

- 原件。K. Mahler, J. reine angew. Math. 166 (1932)。PDF 物理页 1。SHA-256 1f366a2b5f4f23504dd60143087fab95784aa6380ffa4b61530a79afea9f120f。
- classical exponential-logarithm approximation。title page / §IV opening。Mahler 第二部分；扫描首页确认其为同题第二篇及期刊来源。
- 版本与引用。本轮没有逐式核对该部分的辅助函数或误差界，故不能采用为可复用构造。 仅核对可见首页；正文 OCR 不可用，定理编号与适用范围未验证。
- 第六批定向筛选。hold。The physical PDF is a scan. Visual inspection of physical p. 1 verifies Mahler's 1932 Part II identity and the opening of Section IV, but the displayed definitions have not been fully transcribed, and no applicable error/integrality theorem has been verified. 定位。Part II title and Section IV opening, physical p. 1 (image scan).。全卷 14 页。 后续条件。A searchable authoritative text or a manually transcribed and checked lemma chain, including coefficient arithmetic and asymptotic hypotheses.
- 复核记录。2026-11-26T18:35:59+08:00。hold。dependency。
- 本次依据。The 14-page Mahler Part II source is an image scan. Its title and Section IV opening are visible, but definitions and an applicable error/integrality theorem have not been completely transcribed.。定位。Title and Section IV opening, physical p. 1。全卷 14 页。后续条件。A searchable authoritative text or manually transcribed and checked lemma chain, including coefficient arithmetic and asymptotic hypotheses.。

## P40 · On the approximation of π

- 原件。K. Mahler, Proc. Koninkl. Nederl. Akad. Wetensch. Ser. A 56 (1953)。PDF 物理页 1。SHA-256 d5de265eef39bf88389041f65e84e29b9e084ee10462507c16795c81ea10108f。
- classical irrationality-measure approximation。Theorem 1。定理在有理或代数 α 的条件下，构造有整数系数的多项式并由关于 log(z) 的恒等式导出 π 的近似/无理性测度型界。
- 版本与引用。其结论依赖该多项式族的非零性和明确高度、余项估计；论文对象为 π/对数而非 γ。 只核对首页定理陈述，未复核后续常数和完整证明。
- 第六批定向筛选。adjacent。Visual inspection of physical p. 1 confirms Mahler's pi-approximation setup: under its displayed logarithmic-size condition it constructs integer-coefficient polynomials and an identity involving log z to obtain pi bounds. It is a pi/log construction, and no Euler-constant analogue or its required nonzero/height/remainder proof is supplied. 定位。Opening lemma and log-identity setup, physical p. 1 (image scan).。全卷 13 页。 后续条件。A target-specific construction with verified determinant nonvanishing, coefficient heights, and remainders after replacing the logarithm/pi identity.

## P42 · The Irrationality Measure of Pi is at most 7.103205334137...

- 原件。arXiv:1912.06345v2 (2020-01-08)。PDF 物理页 1, 2, 3, 13。SHA-256 b922ee68a427ad5b74617bd2ac6b6a549824eb2d5a8c97eed0d34b2de984155f。
- π irrationality measure via complex integrals。Abstract; Part I strategy; final bound。以 Salikhov 型复路径积分、偏分式与鞍点估计构造 A_n+B_nπ，并在整数化后得到 μ(π)≤7.103205334137…；末页给出该常数计算。
- 版本与引用。严格结论依赖积分恒等式、整数性、LCM 增长和所有鞍点/系数界，Maple 仅用于发现而非替代证明。 未复核 Maple 包或全文鞍点分析，且没有 γ 的直接迁移。
- 相关入口。[math-openai-arithmetic-determinants](../../../math-openai-arithmetic-determinants/SKILL.md)。
- 第六批定向筛选。adjacent。The paper's checked pages give a pi-specific Salikhov complex-integral strategy, its LCM/integrality scaling, and the final asymptotic ratio. Its computer-generated discovery route is explicitly distinguished from the human proof; no Euler-constant integral, arithmetic scaling, or saddle analysis is present, so it is not a nonduplicate gamma tool. 定位。Abstract and scope, physical p. 1; general linear-form strategy, p. 2; Salikhov integral/integrality scheme, p. 3; final integral forms and asymptotics, p. 13.。全卷 13 页。 后续条件。A gamma-specific contour/integral identity and fully verified coefficient integrality, common-divisor, nonzero, and saddle/remainder bounds.

## P44 · Arbeitsgemeinschaft: Arithmetic Holonomy Bounds and Applications to Irrationality

- 原件。Oberwolfach Report 14/2026。PDF 物理页 1, 7, 43, 49, 65。SHA-256 d62c6e89a2ee8afc7bd2dbc4a5f78f16c0e010f352fdcc08e9baaa0148998c9c。
- arithmetic holonomy bounds。Introduction; C.4 Theorem 0.1; C.6; D.1 Proposition 2.3。研讨报告说明 CDT 的 holonomy bound：在整数系数、φ 合成后单位圆内亚纯且 Q(x) 线性无关时，函数数目受边界重排积分/|φ′(0)| 控制；其具体应用是 1、ζ(2)、L(2,χ−3) 线性无关。
- 既有方法覆盖。报告的核心界和 L 值应用依赖其所引 Calegari–Dimitrov–Tang arXiv:2408.15403v2；把界移植到 γ 仍须另有 Apéry 数据、分母型、延拓、独立性和严格阈值。 核对的是报告的讲义版陈述与其明确预印本依赖，未独立验证 2408.15403v2 或为 γ 建立任一门槛。
- 相关入口。[math-euler-constant-irrationality](../../../math-euler-constant-irrationality/SKILL.md)。
