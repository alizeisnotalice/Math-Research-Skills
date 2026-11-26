---
name: math-l05-csp-sat-smt-encoding
description: 将有限数学条件编码为 CSP、SAT 或 SMT，核对量词、完备性及可检查证书。
---

# L05 · CSP、SAT、SMT

> **当前核验范围（2026-10-07）：** 本 Skill 仍属于 L–N 组进行中的审核；逐条数学与能力状态记录在完整交付包的 `audit_current/ln/claims.json`，案例定义记录在 `audit_current/ln/cases.json`；单独安装目录不包含这两份包级账本。请按 [`references/portable-audit-access.md`](references/portable-audit-access.md) 通过 bundle-root resolver 访问。以下限定只陈述已绑定账本的证据边界，不代表整项验收完成。

> 便携文献定位见 [本 Skill 证据索引](references/handoff-evidence-index.csv)。若需读取包外 PDF，以数据包根目录为 `EVIDENCE_ROOT`，按索引中的相对路径定位。

> **本项边界：** 账本 L05-BOOL-01 覆盖两变量 OR 的四个布尔赋值。L05-SOLVER-01 仍未运行 SAT/SMT 求解器或 proof-trace API；全空间罚项、舍入和一般 UNSAT 证书须逐案证明，有限真值表不构成通用求解能力。

## 输入与产出

有限变量与精确定义域、硬约束、可选代价/软约束、CSP/SAT/SMT 模型、求解器输出或证明轨迹。连续 Fourier 扩张须明确变量盒、符号舍入规则和 FE_c 的端点编码。

产出应包含适用性判断、使用的假设、数学步骤、证书或界的方向、常数依赖，以及尚未解决的缺口。

## 执行步骤

1. 声明每个变量的确切定义域，并区分硬可行约束和加权偏好/优化代价。
2. 把原约束翻译到目标 CSP、SAT 或 SMT 语言；用可手工枚举的小实例核对真值表和每种变量编码。
3. 若用连续 Fourier 代价，明确布尔编码（本源中 +1=False、−1=True；FE_c 在 Boolean 顶点对满足约束取0、违反约束取1）、变量定义域、零点符号舍入和罚项系数；逐点检查零坐标与舍入阈值等号。
4. 有界公式先严格保留 x∈[−1,1]^n 硬约束。若改用全空间平方形式，令每个 FE_c 为对应布尔约束的 Walsh–Fourier 多线性扩张（在布尔顶点对满足约束取0、违反约束取1），并使用 F_sq(x)=Σ_{c∈C}FE_c(x)^2+αΣ_i(x_i^2−1)^2，α>0。对有限变量公式，该目标非负且强制平方罚项使其在全空间具有全局最小值；公式可满足当且仅当全局最小值为0，且任一零点按 sgn(0)=+1 舍入后给出满足赋值（Zhang 等，Prop. 9，PDF 第5页及附录A.1）。这是全局数学归约，不保证数值优化器找到该最小值。
5. 省去变量盒罚项时，逐个约束核验全空间舍入条件：存在 ε_c≥0，使所有 l∈R^n 满足 |FE_c(l)|≤ε_c 时，sgn(l) 都满足 c；对有限约束集可取共同阈值 min_c ε_c。此时 α=0 的平方（或绝对值）目标的每个精确零点都舍入为满足赋值，且公式可满足当且仅当该目标有一个取到的零值（Zhang 等，定义12与推论13，PDF 第6页）。省去罚项后目标未必强制存在最小值；原文的“min=0”不证明不可满足输入上最小值总能取到，也不能把 infimum 为0或数值近零当作可满足/不可满足证书。近零推论须另有残差—违反数界。
6. 小规模先用完整枚举查编码。需要 SAT/SMT 时，按 [数学工具引导](../math-tool-router/SKILL.md) 核对本轮实际存在的求解器、理论和证明输出支持，再保存精确编码和求解配置。
7. 若用连续局部搜索或 BDD 消息传递，先在一到三个变量的小模型上穷举赋值，再用中心差分与解析梯度逐坐标对照。
8. 把满足赋值代回原始约束；若声称不可满足，要求求解器支持证明轨迹或提供可独立核验的证书。
9. 若编码了优化目标，另行核验目标值和最优性界，不能把可行性等同于最优性。

## 共享标签与投影约束

涉及有限投影游戏、共同见证或抽样后标签兼容时，读[纤维标签与顺序对齐](references/label-consistency.md)。核对可达输出、跨表示的一致性及抽样律的量词。

若要把已明确的有限约束或 permutation constraint 变成图目标，或审计这类变换的局部值保持性质，读[局部图 gadget 证书](references/graph-gadget-certificates.md)。它只覆盖其中逐项列出的构造和前提；不得据此推出任何一般 hardness gap 或近似阈值。

## 有界宽度的 CNF 分解

需对满足集分块计数、且分块不得重叠时，读[向日葵分支的互斥性与稀疏预算](references/disjoint-cnf-sunflowers.md)。侧条件与活跃子句分开记录。

需要最大度三的完美匹配实例时，读[匹配奇偶路径与见证恢复](references/perfect-matching-degree-reduction.md)。

## 证据与失败处理

满足赋值只证明编码模型成立。定义域写错、漏约束、用实数放松或未经核验的求解器状态都会使数学结论失效。Fourier 扩张 FE_c 只在 Boolean 顶点编码0/1违约；超出变量盒时可能为负，故全空间目标要按来源平方 FE_c 并取 α>0。

引用定理前按 [来源与阅读状态](references/provenance.md) 定位版本和证据。只有预印本支持的陈述须核对实际依赖的结论、证明步骤和假设。来源或适用范围未核实时，保留已独立推导的部分，并将相应陈述留作研究线索。
需要完整步骤时读 [方法说明](references/method.md)。只有当前请求明确涉及对应的中心立方体研究任务时，才使用 [历史课题接口](references/cube-interface.md)，并先复核当前问题与该接口的假设。
遇到定义缺失、条件不满足或来源未核验，指出具体缺项，保留可证明的弱结论。不得将迁移推断写成原文定理。
依赖表提供方法路线，不表示所有工具之间存在无条件定理蕴含。

用 [适用案例](examples/positive.md) 与 [条件缺失案例](examples/negative.md) 检查适用边界。

三个并行机器的单位作业有序分解，使用[三元槽位的路径式排程见证](references/three-machine-schedule-certificates.md)验证间隙与跨分块前置关系。

局部填充和擦除定义有限状态图时，读[分阶段互反的局部证书](references/reciprocal-transcript-transitions.md)。

## OpenAI 原稿中的方法

- [Finite-support recovery for Euclidean Ramsey configurations](references/openai-euclidean-ramsey-finite-support.md)
- [Disjoint probability-tree covering](references/openai-kahn-kalai-tree-covering.md)
- [Prime-order Ryser construction: finite concentration inputs](references/openai-ryser-cylinder-concentration.md)
- [Bounded Maker-game certificate reconstruction](references/openai-snaky-certificate-reconstruction.md)
- [Translational-tile period obstruction](references/openai-translational-tile-period-obstruction.md)

- [Finite-product divisibility transfer](references/finite-product-divisibility-transfer.md)
- [Fresh proper-clause interfaces](references/openai-proper-clause-interfaces.md)

- [Bounded-occurrence counting polynomial](references/openai-bounded-occurrence-count-polynomial.md)
