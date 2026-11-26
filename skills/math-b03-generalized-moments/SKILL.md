---
name: math-b03-generalized-moments
description: 用广义矩问题组织概率或解析界，核对矩约束、对偶多项式和达到条件。
---

> 外部文献、claims/cases 与 PDF 属于完整证据包，不随单个 Skill 安装。请使用[便携证据访问指南](references/evidence-guide.md)，按本 Skill 的[来源索引](references/handoff-evidence-index.csv)通过统一 resolver 定位。registry/显式包根路由均不依赖当前工作目录；SHA 检查只确认当前字节，不等于全文阅读或数学验收。


# B03 · 广义矩问题（Bertsimas–Popescu）

当前证据状态：**部分可用**。条件矩变量变换、逐点 majorant 的弱对偶及 `σ>0,t<μ` 的条件尾均值上确界可按所列定义执行；强对偶、有限原子表示和矩锥闭性仅在对应源条件及已列依赖可用。源外引不完整证明仍标为缺口，不将完整文献证明状态由主文覆盖推断。

## 证明类型与交接

本 Skill 是[证书类型分类](../probability-optimization-certificates/references/proof-type-taxonomy.md)的 **C 类**：未知概率测度、广义矩、条件比值和测度层面的弱/强对偶。若支持已完整列举且输入是 Boolean/count/marginal 矩约束，优先交给 [有限矩多项式对偶](../probability-moment-polynomial-duality/SKILL.md)；若只需核验已给的有理或区间见证，用 [L03](../math-l03-rational-and-interval-certificates/SKILL.md)。这些有限工具不能替代本 Skill 的事件分母、矩锥内点、闭性或达到条件。

## 输入与产出

支持集或结构类、测度质量、已知矩 E[h_j(X)]=q_j、待界定事件 Ξ 与目标 g。

产出应包含适用性判断、使用的假设、数学步骤、证书或界的方向、常数依赖，以及尚未解决的缺口。

## 有限原子表上的极点核验

原子已完整列举、矩约束为线性等式或不等式时，用 [有限矩多面体](references/finite-moment-face-guide.md) 检查活跃约束的精确秩。欠秩时输出两个不同的有理可行端点。

## 执行步骤

1. P-91433be844e70d18 (4)先把原未知分布P写成指定支撑的概率测度，明确h₀≡1,q₀=1及每个广义矩约束；变换后的Q则是有限非负测度，不能继续要求全域质量1。
2. P-91433be844e70d18 (5)将无条件事件概率/目标写成测度线性泛函；条件期望保分母P(Ξ)，逐可行P检P(Ξ)>0，单点正值不等于全族统一正下界。
3. P-91433be844e70d18 (6)条件比值设α=1/P(Ξ)>0,dQ=αdP：Q(Ω)=α且Q(Ξ)=1，Q不是一般概率；逆映射P=Q/α并检矩约束。[预印本 Theorem 1](https://arxiv.org/abs/2401.00090) 的强对偶分支另需 g 有界、对所有可行 P 统一满足 P(Ξ)≥ε>0，并核对 q 所在矩锥的内点条件及锥对偶的外部引理。条件未闭合时，仅使用可直接推出的变换与弱对偶。
4. P-91433be844e70d18 (7)逐点majorant积分给弱对偶界；紧界须有可行极值分布或极值序列匹配。Prop1的均值—标准差定理整体假设 `σ>0`：在 `t<μ` 时 `sup E[X|X≥t]=μ+σ²/(μ−t)` 且上确界不达到；在 `t≥μ` 时上确界为 `+∞`。该 sup 只针对均值为 `μ`、方差为 `σ²>0` 的支撑不受限实值分布中满足 `P(X≥t)>0` 者；额外支撑/结构限制下，原式仅在受限可行类为上述原文可行类的子集时可作上界，受限类的精确 sup 须另行求解或证明。先单独处理退化情形 `σ=0`：此时矩约束强制 `X=μ` 几乎处处；若 `t≤μ`，条件事件概率为1且条件均值为 `μ`；若 `t>μ`，条件事件概率为0，条件期望未定义。不得把 `σ>0` 的 `t≥μ` 分支套到 `σ=0`。
5. P-91433be844e70d18 Theorem2仅对满足A1–A3和mixture-generated convex class的极端生成表示归约至≤m+1生成元（包含mass moment）；其Popescu外引cardinality证明仍未独立核，原子数、强对偶和达到分别验收。
6. P-91433be844e70d18 Theorem3的contextual DRO要保C1–C4及附加conic representability/Slater，非紧支持或事件概率趋零不可套紧性/正margin。若另用SOS/SDP，须另给半代数支撑、矩阶数与证书方向，不能由该篇直接认证通用SOS层级。

## 证据与失败处理

有限矩通常不唯一确定分布；条件比值在 P(Ξ)→0 时可能失控，且端点上确界可不达到或为无穷。弱对偶可用可行majorant，但强对偶需相应闭性/Slater条件；有限原子结论依赖具体 moment cone/生成类定理。

引用定理前按 [来源与阅读状态](references/provenance.md) 定位版本和证据。只有预印本支持的陈述须核对实际依赖的结论、证明步骤和假设。来源或适用范围未核实时，保留已独立推导的部分，并将相应陈述留作研究线索。
需要完整步骤时读 [方法说明](references/method.md)。只有当前请求明确涉及对应的中心立方体研究任务时，才使用 [历史课题接口](references/cube-interface.md)，并先复核当前问题与该接口的假设。
遇到定义缺失、条件不满足或来源未核验，指出具体缺项，保留可证明的弱结论。不得将迁移推断写成原文定理。
依赖表提供方法路线，不表示所有工具之间存在无条件定理蕴含。

用 [适用案例](examples/positive.md) 与 [条件缺失案例](examples/negative.md) 检查适用边界。

## 有限概率向量的形状证书

原子位于有限连续整数网格时，用[离散形状检查](references/discrete-shape-exact-guide.md)核验质量向量、对数凹、离散失效率以及零缺口的几何分段。

## 显式有限原子测度的团分解

已给出支持原子和非边理想等式时，用[有限稀疏矩分解](references/ideal-sparse-finite-guide.md)检查正权重与非边乘积，将原子分配到极大团并逐项重组所需单项式矩。

## 文献复核采用的构件

- [Effective countable GMP relaxation rate](references/effective-countable-gmp-rate.md)
