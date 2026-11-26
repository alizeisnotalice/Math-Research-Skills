---
name: math-alternating-reciprocal-criteria
description: "用 Sondow 的交错倒数和—连分数判据，严格区分可证明的无理性、有限前缀核验，以及需要整条简单连分数假设的超越性结论。适用于 Pierce 展开或快速增长分母的交错倒数和；不用于仅凭数值近似宣称无理或超越。"
---

# 交错倒数和的连分数判据

处理
\[
 \alpha=\sum_{n\geq0}\frac{(-1)^n}{B_n}
\quad\text{或}\quad
 \alpha=\sum_{n\geq0}\frac{(-1)^n}{A_0A_1\cdots A_n}
\]
时，先说明给出的是有限前缀、一个明确定义的无限序列，还是一个已证明对全部指标成立的结构命题。有限计算只可核验截断恒等式和已检查的门槛；它不能自动证明无理性或超越性。

本技能依据 Jonathan Sondow, *Irrationality and Transcendence of Alternating Series Via Continued Fractions*, arXiv:2009.14644v1 (2020)。在需要精确公式、定位或反例时读 [来源与适用范围](references/source-and-scope.md)。

## 类型 I：一般交错倒数和

令 \(0<B_0<B_1<\cdots\) 为整数。有限第 \(N\) 个截断满足精确的广义连分数恒等式
\[
 \sum_{k=0}^{N}\frac{(-1)^k}{B_k}
 =\cfrac{1}{B_0+\cfrac{B_0^2}{B_1-B_0+
 \cfrac{B_1^2}{B_2-B_1+\ddots+
 \cfrac{B_{N-1}^2}{B_N-B_{N-1}}}}}.
\]
因此，若已对每个 \(n\ge0\) 证明
\[
 B_{n+1}\ge B_n(B_n+1),
\]
则 Sondow 的 Proposition 1（经其 Irrationality Lemma）推出 \(\alpha\notin\mathbb Q\)。提交结论时必须一并给出严格递增性与这个全称不等式的证明。

该不等式是充分而非可由有限样本外推的判据。特别是若无限序列满足
\(B_{n+1}+1=B_n(B_n+1)\)，其和恰为 \(1/(B_0+1)\)，所以把“接近阈值”写成无理性结论是错误的。

## 类型 II：Pierce 展开

令 \(A_0,A_1,\ldots\) 为正整数且 \(A_n\ge2\)（\(n\ge1\)）。令 \(B_n=A_0\cdots A_n\)，再使用类型 I 的有限恒等式；当所有 \(x_n=1\) 时，原文的等价连分数为
\[
 \alpha\sim\cfrac1{A_0+\cfrac{A_0}{A_1-1+
 \cfrac{A_1}{A_2-1+\ddots}}}.
\]

若对所有 \(n\ge0\) 证明 \(A_{n+1}>A_n\)，Theorem 1(ii) 推出 \(\alpha\notin\mathbb Q\)。不要以仅有限个严格增长的 \(A_n\) 代替这个全称条件。

超越性需要另一道门：必须证明原文 Theorem 1(iii) 的**整条**等价连分数可经某个正实序列 \((x_n)\) 化为简单连分数（等价地，全部相应部分和是同一个简单连分数的连分数收敛分数）。这时才可引用其 \(\mu(\alpha)\ge2.5\)，再用 Thue--Siegel--Roth 定理排除代数性。单独的无理性判据、有限个收敛分数，或高精度近似均不建立这一门槛。

## 精确检查

运行下列脚本以有理数核对有限截断与广义连分数，或显示门槛失败；它不会把有限输入标为“已证明无理”：

```sh
python3 scripts/alternating_reciprocal.py --self-test
python3 scripts/alternating_reciprocal.py type-i 1 3 15 255
python3 scripts/alternating_reciprocal.py type-i 2 5 29 869
python3 scripts/alternating_reciprocal.py type-ii 2 3 4 5
```

对递归定义的无限序列，应在研究笔记中给出归纳步骤，证明其定义在每一步都保持所需全称门槛。脚本的 `type-i` / `type-ii` 输出只是一项有限核验和精确截断恒等式，不是该归纳的替代品。
