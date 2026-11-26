---
name: math-mixed-littlewood-pseudoadic
description: 对满足有限素数支撑和增长条件的伪绝对值序列，调用已发表的混合 Littlewood 存在性定理；不把它当作给定 alpha 的有限逼近算法。
---

# 伪绝对值混合 Littlewood 门槛

使用前读[Harrap--Haynes 定理接口](references/harrap-haynes-pseudoadic.md)，并把输入写成整数 \(a\ge2\) 与完整伪绝对值序列 \((n_k)\)，而非有限前缀。

- 必须证明所有 \(n_k\) 的素因子落在某个有限固定素数集，且该集与 \(a\) 互素。
- 必须给出一个 \(\delta>0\) 并证明对每个 \(k\ge2\)，\(\log n_k\le k^\delta\)；有限样本不认证这个全称条件。
- 条件满足时，唯一可输出的主结论是对任意实 \(\alpha\)，\(\inf_{n\ge1}n|n|_a|n|_{\mathcal D}\lVert n\alpha\rVert=0\)。

该结论是非有效存在性结论。它不生成逼近整数 \(n\)，也不认证给定 \(\alpha\) 的收敛速率；源证明使用测度刚性和 Baker--Wüstholz 型对数下界。
