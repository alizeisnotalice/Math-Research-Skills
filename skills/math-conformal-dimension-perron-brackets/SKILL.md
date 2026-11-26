---
name: math-conformal-dimension-perron-brackets
description: 对给定扩张共形 Markov 分区、认证导数区间和有理比较向量，验证非负转移矩阵的谱半径界并判断指数与维数的方向。
---

# 共形 Markov 分区的 Perron 根区间

先给出有限分区、转移边、扩张条件以及每条边的倒导数区间。已经知道的维数对象必须满足来源所用的共形密度假设。

对测试指数 \(s\)，用定向区间计算逐项界住幂矩阵。对有理非负比较矩阵 \(A\) 及严格正向量 \(v\)，分别取 \((Av)_i/v_i\) 的最小值和最大值，得到包住 \(
ho(A)\) 的精确有理区间。只有实际提供单调递减的幂矩阵与来源的维数归约时，才把严格越过 1 的谱半径界换成 \(s\) 与维数的比较。

用 [分支样例](examples/two_branch_bracket.md) 查看输入和运行命令。采用的定理条件与四类校验见参考说明。

## 文献复核采用的构件

- [Perron-root brackets for conformal-dimension calculations](references/mcmullen-perron-dimension-brackets.md)
