---
name: math-cyclotomic-euler-t-parity
description: 对满足收敛条件的根单位 cyclotomic Euler T-sum，调用围道留数奇偶归约到较低阶和；不提供未展开余项的数值公式，也不采纳猜想的 multiple-t 奇偶性。
---

# Cyclotomic Euler T-sum parity reduction

Fix roots of unity (x,x_1,\ldots,x_r), positive integers
(p_1,\ldots,p_r,q), and the source's series normalization. Check
((p_j,x_j)\ne(1,1)) for all (j) and
((q,xx_1\cdots x_r)\ne(1,1)). The source then reduces

\[
xT_{p_1,\ldots,p_r;q}(x_1,\ldots,x_r;(xx_1\cdots x_r)^{-1})
+(-1)^{p_1+\cdots+p_r+q+r}
T_{p_1,\ldots,p_r;q}(x_1^{-1},\ldots,x_r^{-1};xx_1\cdots x_r)
\]

to a combination of lower-order cyclotomic Euler T-sums and cyclotomic Euler
sums. Record the order, all roots, and the convergence checks. The theorem is
a reduction modulo lower-order terms, not an explicit evaluator for the
discarded expression.

Do not replace this theorem with the paper's distinct multiple-t-value
conjecture or its Panzer-dependent consequence.

## Source

- [Contour-residue parity reduction](references/ext-0068-cyclotomic-euler-t-parity.md)
