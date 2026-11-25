---
name: math-discrete-proof-transfer
description: 为固定二叉 Derrida–Retaux/H3、连续 Cantelli、自由边界方格双峰 A022、非负因子 A30/A175、布尔 Fourier 谱维数 A28/A165 审核可迁移引理并制作可独立核验的证书。另用于周期图的有限连通分支与例外顶点预算。不要因同名 Fourier、稳定性或张量术语就迁移结论。
---

# 离散与概率课题的论文迁移审计

本入口用于指定专题的研究核验。预印本及项目材料按固定版本引用，使用具体结论前核验原文假设、证明依赖和迁移步骤。涉及既有课题状态时，先对照当前项目记录。

1. 先读目标的 README、STATE、最近完整轮次和引用。区分主分支、工作分支与本地工作树；轮次自述不是独立核验。
2. 对每个候选方法给出「源定理与版本、对象与归一化、假设、可推出的结论、目标尚缺的桥、核验证据」。标为直接引理、可重证的本地推导、启发、或不适用。
3. 每次推进以具体关键引理、最小反例、可复算证书或明确缺口收尾。作者声明、形式化覆盖、本次实际检验要分开。可参照 Anthropic FLT 的做法先冻结目标声明、拆依赖图，再比较实际证明与原目标；内核通过不能认证被弱化的自然语言目标。
4. 张量欧氏价格不能直接估计概率质量、Walsh 谱维数或非负实卷积。向日葵只适用于实有的有限集合族，仍需保真桥。

- 固定二叉 DR 与连续 Cantelli：读 [递推与变换](references/probability.md)。
- A022 首触传输、A30 非负卷积、A28 相位匹配：读 [离散结构](references/discrete.md)。
- 版本、形式化范围与项目基线：读 [来源](references/sources.md)。

- 需要精确 DFT 的等宽矩阵变换时，读 [Newton–Toeplitz 分解](references/exact-fourier.md)，检查根的阶与所用域。

- 审查有限域分解时，用 [Frobenius 固定子代数的分离元](references/finite-field-separation.md) 核对特征多项式和精确 gcd。

核对素数参数差分问题的等差限制时，读 [原文构件](references/local-root-restriction.md)。

若计数对象有多个算术见证，用 [同值见证的并集去重](references/totient-witness-unions.md) 核对共享阈值空间和跨前缀碰撞。

构造特征二的显式有限域或核对一元商代数的乘法迹时，按[有限域扩张与一元乘法迹](references/finite-algebra-operations.md)保留域与判别条件。

周期图逐分支控制用 [有限位移证书](references/periodic-component-bounds.md) 检查闭路位移和有限例外点。
