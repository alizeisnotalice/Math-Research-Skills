# 逐篇复核、来源恢复与数学技能整合

本轮以 27 个独立批次复核 253 份候选或待核原件，逐份重算 SHA-256 并核对页码和具体依赖。122 份提供可调用构件，4 份确认已有工具覆盖，53 份归入引用，4 份列为邻近材料，4 份的当前采用路线经数学核验后排除。待核文献按不同原件从 253 份降至 66 份，其中 30 份为候选，36 份仍有具体依赖待查。

| 分册 | 本轮复核 | 新采用构件 | 当前待核 |
| --- | ---: | ---: | ---: |
| 历史 | 25 | 14 | 7 |
| 近期 | 52 | 21 | 28 |
| 补充 | 176 | 87 | 31 |

共享归档的 5,410 个 PDF 路径全部逐文件复算，与已有清单的路径、字节数和 SHA-256 一致，去重为 5,389 个本机身份。内部写作资料由本机写作资产登记，Google 双矩阵论文的额外修订身份由独立版本卡登记。查询支持重复给出状态，以单次操作读取候选和待核原件的并集。[逐篇来源查询](../skills/math-research/references/literature-source-lookup.md) · [Google 版本记录](../skills/math-research/references/google-cogentic-2026-11-25.md)

## 可复验结果

- **标准化 Bernoulli 和。** 检查刊载稿用作先决条件的统一平方指数矩。对 $S_n\sim\mathrm{Bin}(n,2/n)$，$S_n=n$ 的单个原子已使贡献随 $n$ 发散。用精确整数算术确认 $n=16$ 时其贡献严格超过 $2^{64}$。另将可证明的固定参数线性指数矩上界接入工具。[适用边界与证明](../skills/probability-bernoulli-extremal-orders/references/standardized-bernoulli-exponential-moments.md)
- **有限图。** 对 $n=45,D=\{1,3,5\}$ 的整数循环图，Ramanujan 整数谱给出能量 124，二阶、四阶迹分别为 1710 和 2091690，逐项与邻接矩阵复算一致。任意有限图的谱矩计算与该特定整谱入口各保留输入条件。[图谱矩与循环图](../skills/math-graph-spectral-moment-certificates/SKILL.md)
- **群论数据。** 用本机 Python 解码 A7 公共数据，核对 2520 行排列及 2519 个商条件。H5 的 125 阶整数群行列式见证以 Bareiss 精确算术复现 $11\cdot5^{28}$，零见证返回 0。A7 回放仅涉及压缩数据所代表的有限证书。[有限置换证书](../skills/math-finite-permutation-terrace-certificates/SKILL.md) · [H5 群行列式](../skills/math-heisenberg-group-determinant-certificates/SKILL.md)
- **正式版本恢复。** Gaudron 的本机法文 PDF 有编码问题。通过作者保存的刊载版核对题录和实际定理，采用带数域、赋值、交换群、代数 Lie 子群与高度条件的对数距离界。[Gaudron 入口](../skills/math-algebraic-group-logarithm-distance/SKILL.md) · [作者保存的刊载版](https://lmbp.uca.fr/~gaudron/art6.pdf)
- **Mahler 指数与对数。** 核对原刊及 EMS 重印，把 Part II 调用限定到非零整系数多项式。采用由 Satz 4 和第 22 节导出的次数依赖下界，并登记末页展示式的方向矛盾。可用于指定的有理数实对数或 $2\pi i$。[技能入口](../skills/math-exponential-logarithm-algebraic-independence/SKILL.md) · [EMS 重印](https://ems.press/content/book-chapter-files/27404)
- **调用范围修正。** 对称多项式工具拒绝小数或布尔值充当整数度数和分拆部分。量子永久式工具对一个数学分拆只接受一条权重。模形式同余工具明确区分源定理与程序实现的 CM 素数分支。几何特殊点入口分别写明 $p>2g_X$、有理基域及源文所需的 Hodge 前提。[对称多项式](../skills/math-symmetric-polynomial-ratio-certificates/SKILL.md) · [量子永久式](../skills/math-quantum-permanent-score/SKILL.md) · [CM 同余](../skills/math-modular-holonomic-telescoping/references/ext0290-sporadic-cm-congruence.md)

## 技能目录

本轮新增 37 个独立入口。复指数方程的几何存在性和承担公理后的推论在同一入口分流，两种参数三次范数型共用入口并逐式核对。Mahler 系统的基与提升、赋值过滤的纯性和差分 Galois 微分超越性分别按其实际输入和结论调用。[技能目录](../catalog/README.md)

剩余条目的依赖、原文位置及需要的证据见逐篇索引。欧拉常数无理性仍是开放问题。
