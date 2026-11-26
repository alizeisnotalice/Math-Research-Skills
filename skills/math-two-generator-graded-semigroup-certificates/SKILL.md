---
name: math-two-generator-graded-semigroup-certificates
description: 精确计算双生成分层数值半群的 Wilf 型有限不等式，或枚举给定数值半群分解为不可约超半群交集的长度。
---

# 数值半群的分层计数与分解长度

给定互素整数 `2 <= a < b` 和维数 `d >= 1`，对 `T=<a,b>` 的总度分层精确计算 Frobenius 数、锥区计数、可行层计数和原子层计数。仅报告输入参数的整数不等式证书。

运行 `scripts/check_two_generator_graded_wilf.py a b d`。输出的 `c`、`n`、`e` 分别来自有限总度层的组合计数，`wilf_holds` 核对 `d*c <= e*n`。它不分类任意广义数值半群，也不替代来源所用的半群结构定理。

## 文献复核采用的构件

- [Two-generator graded-semigroup count](references/recent-01-graded-wilf.md)

## 不可约超半群交集的分解长度

给出小规模有限缺口集，按[分解长度来源卡](references/numerical-semigroup-special-gap-lengths.md)枚举包含该半群的数值半群。以缺口的并集核对交表示及最小性。计算返回这个半群的全部不可约交分解长度。缺口为空时，采用空交为全体非负整数的约定并返回长度零。
