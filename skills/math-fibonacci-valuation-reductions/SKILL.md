---
name: math-fibonacci-valuation-reductions
description: 对给定 Fibonacci 指数的精确整除前提，检查 F_l 的精确幂整除并应用三分支的指数约化；不宣称解完原始指数丢番图方程。
---

# Fibonacci 精确赋值约化

当某个证明已得到 \(F_l^k\Vert F_n\)（\(l\ge3,k\ge2\)）时，可用[精确检查器](scripts/check_fibonacci_valuation_reduction.py)在具体整数输入上验证该前提，并检查来源引理对应的 \(F_l^{k-1}\mid nl\) 或 \(F_l^{k-2}\mid nl\) 结论。完整分支和边界见[来源接口](references/ibrahimov-mahmudov-fibonacci-valuation.md)。

检查器采用整数快速倍增 Fibonacci 算法和精确整除；它的成功只认证该有限三元组的算术断言。它不证明文献引理，不替代原文引用的赋值结果，也不验证 Matveev、连分数约化或最终的全局唯一解。
