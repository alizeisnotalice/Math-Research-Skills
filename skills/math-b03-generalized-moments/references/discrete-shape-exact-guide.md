# 离散 LC / IFR 形状的精确有限核验

此附件补充 B03 的一般矩/对偶工作流：对一个已经给定的有限质量向量做**有理算术**的形状证书。它不是非凸离散矩问题的求解器，不能仅因某候选有少量几何片就称其为最优解。

## 来源与版本核验

- Xi Chen, Simai He, Bo Jiang, Christopher Thomas Ryan, Teng Zhang, “The Discrete Moment Problem with Nonconvex Shape Constraints,” *Operations Research* **69**(1), 279--296 (2021), DOI [10.1287/opre.2020.1990](https://doi.org/10.1287/opre.2020.1990)。INFORMS 的出版记录给出在线发表日期 2020-10-26、正式卷期页码及 DOI。
- 本地候选 SHA-256 `6f0d6890eb9f2625f06fdb1f922d114c85b3ecd9f21244d75da54f8c371c0995` 是 2017-08-07 的 [arXiv:1708.02079v1](https://arxiv.org/abs/1708.02079) 31 页稿，而不是已逐页比对的期刊排印版。实际阅读并复核 arXiv HTML 的 Definition 2.1（离散 LC）、Lemma 2.6（IFR 当且仅当尾序列 LC）、Theorem 3.6（其紧约束计数的技术假设）、Theorems 4.1--4.2（最优极点的片段几何结论和证明）。出版网页摘要确认正式文章还覆盖 LC、IFR、IGFR；本附件不声称期刊版的每一个定理编号/假设与 v1 完全相同。

## 可独立证明并实现的有限部分

对有限非负质量 `x_0,...,x_{n-1}`，离散 LC 要求正支撑是一个连续整数区间并且

\[
  x_j^2-x_{j-1}x_{j+1}\ge0 \quad (1\le j\le n-2).
\]

脚本逐条输出这些有理缺口。支撑内部缺口为零时
`x_{j+1}/x_j=x_j/x_{j-1}`，故零缺口的连续区间是几何序列；严格正缺口恰是片段的共享断点。由此可对一个**已给候选**精确计算片数和每片公比。`piece_budget=m` 仅报告候选是否至多 `m` 片，绝不反向推出 Chen 等人 Theorem 4.1 所要求的“某个最优极点存在”结论。

令尾和 `y_j=Σ_{k=j}^{n-1}x_k`。在正尾区间，失败率
`r_j=x_j/y_j=1-y_{j+1}/y_j`。因此

\[
 r_j\le r_{j+1}
 \Longleftrightarrow y_{j+1}^2\ge y_jy_{j+2}.
\]

这给出 IFR--尾序列对数凹的直接有限证明；程序同时输出两侧的有理差和失败率。尾和为零后的比值未定义，脚本明确不把它列入失败率序列。

## 运行与边界

```sh
python3 scripts/discrete_shape_certificate.py examples/lc_two_geometric_pieces.json
python3 scripts/discrete_shape_certificate.py examples/ifr_not_lc.json
```

输入拒绝浮点数，只接受 JSON 整数和有理字符串。它检查质量是否为概率分布，但仍会诚实给出未归一化向量的代数差；任何 `is_probability_distribution=false` 输出都不能作为概率分布的形状证书使用。一般矩最优化、未知/无限支撑、IGFR、连续分布，或以数值公比近似证明形状，均不属于本工具的结论范围。
