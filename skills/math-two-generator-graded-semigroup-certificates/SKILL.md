---
name: math-two-generator-graded-semigroup-certificates
description: 对互素双生成数值半群的总度分层进行精确计数，并核验对应 T-graded 广义数值半群的 Wilf 型有限不等式。
---

# 双生成分层半群证书

给定互素整数 `2 <= a < b` 和维数 `d >= 1`，对 `T=<a,b>` 的总度分层精确计算 Frobenius 数、锥区计数、可行层计数和原子层计数。仅报告输入参数的整数不等式证书。

运行 `scripts/check_two_generator_graded_wilf.py a b d`。输出的 `c`、`n`、`e` 分别来自有限总度层的组合计数，`wilf_holds` 核对 `d*c <= e*n`。它不分类任意广义数值半群，也不替代来源所用的半群结构定理。

## 文献复核采用的构件

- [Two-generator graded-semigroup count](references/recent-01-graded-wilf.md)
