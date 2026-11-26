---
name: math-graded-character-order
description: Certify finite graded multiplicity comparisons through cumulative coefficient differences and optimal ordered matching.
---

# Graded character order

Given two finite nonnegative integer coefficient arrays of equal total, compute the coefficients of their divided difference by `1-q`, the stochastic-order direction, and the exact minimal unmatched mass for degree-nonincreasing matching.

Use this only after the arrays have been independently identified as the multiplicities of the same irreducible type. It does not construct plethysms, representations, or a global Schur-positivity proof. Read [the source reduction](references/q-foulkes-graded-order.md) for that distinction.

Run `python3 scripts/graded_character_order.py examples/positive.json`.

## 有限 q-整数系数

当已给出的表示论归约把缺陷系数化为 q-整数式时，用[q-整数系数恒等式](references/q-integer-defect-source.md)精确验证多项式相等与系数非负。源表示论同一性和蕴含范围由各自的论证承担。
