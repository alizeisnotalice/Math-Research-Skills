# 有理核到 \(1,\gamma,\log\) 线性形式

这个模块是对现有 Sondow 分数部分证书的通用输入层。它只处理已经给定的部分分式系数，避免把由正积分、整数性或尾项估计承担的命题混入代数变换。

实际依赖是 Jonathan Sondow, with an appendix by Sergey Zlobin, *A Hypergeometric Approach, Via Linear Forms Involving Logarithms, to Irrationality Criteria for Euler’s Constant*, arXiv:math/0211075v4, 29 April 2009，本机件 `P05_A_Hypergeometric_Approach_Via_Linear_Forms_Involving_Logarithms_to_Irrationality_Criteria_for_Euler_.pdf`，SHA-256 `a709a732b9101326b55fa927d265ccbb8232960ae74fa22fbd6626bcf51b1517`。命题在物理页 3--4 的 Proposition 1，专门核在物理页 4--5 的 Lemma 2--3 与 Theorem 1。

文献目录将正式发表版本列为 Sondow--Zlobin, *Mathematica Slovaca* 59 (2009), DOI [10.2478/s12175-009-0127-2](https://doi.org/10.2478/s12175-009-0127-2)。本机没有该正式 PDF，因此下列公式的逐页依据是上述 v4 预印本。这里没有把期刊版当成已逐页复核的实际依赖。

## 可调用的精确变换

输入正整数 \(n\) 及有理数 \(b_{k,2},b_{k,1}\)，其中 \(0\leq k\leq n\)，并令

\[
R(t)=\sum_{k=0}^n\left(\frac{b_{k,2}}{(t+k)^2}+
\frac{b_{k,1}}{t+k}\right).
\]

先严格检查

\[
\sum_k b_{k,1}=0,
\qquad
\sum_k(b_{k,2}-k b_{k,1})=0.
\]

它们正是 \(R(t)=O(t^{-3})\) 的 \(t^{-1}\) 与 \(t^{-2}\) 系数消失条件。条件成立时，Proposition 1 给出

\[
 \sum_{\nu=n+1}^{\infty}\int_\nu^\infty R(t)\,dt
 = B\gamma+L-A,
\]

\[
B=\sum_kb_{k,2},\qquad
L=\sum_{m=1}^n\left(\sum_{k=m}^n b_{k,1}\right)\log(n+m),
\qquad
A=\sum_k b_{k,2}H_{n+k}.
\]

命令行脚本 [rational_kernel_linear_form.py](../scripts/rational_kernel_linear_form.py) 从显式 JSON 输入返回全部有理数和对数权重。它拒绝缺项、重项和不满足渐近消失的输入。退出码 `0` 表示这两个系数均为零，退出码 `1` 表示输入已解析却未达到 \(O(t^{-3})\)。输出中的 `required_decay_certified` 只对应此代数条件。

```json
{
  "n": 1,
  "coefficients": [
    {"k": 0, "double": "1", "simple": "-2"},
    {"k": 1, "double": "1", "simple": "2"}
  ]
}
```

该例返回 \(B=2\)、\(A=5/2\)、\(L=2\log 2=\log4\)。它是原文中
\(R_1(t)=[t(t+1)]^{-2}\) 的直接有限核，故

\[
\sum_{\nu=2}^{\infty}\int_\nu^\infty\frac{dt}{t^2(t+1)^2}
=2\gamma+\log4-\frac52.
\]

原文的专门族是

\[
R_n(t)=\left(\frac{n!}{t(t+1)\cdots(t+n)}\right)^2,
\quad
b_{k,2}=\binom nk^2,
\quad
b_{k,1}=2\binom nk^2(H_k-H_{n-k}).
\]

Lemma 2 才额外证明了它的特定公分母和整数对数权重性质，Lemma 3 才将其识别为正双积分。对于任意新核，必须分别证明这两件事。

## 域、正性与结论边界

命题适用的级数从 \(\nu=n+1\) 开始，因此 \(t\geq n+1>0\)，所有显示极点均在积分域左侧。对于上述 \(R_n\)，积分核逐点为正。一般 JSON 输入中的 \(R\) 可以变号，脚本不试图认证正性或尾项大小。

这个变换不产生 \(\gamma\) 的无理性结论。要得到现有技能所使用的有限分母排除，仍须使用其专门的整数化、正余项界和分数部分论证。无穷多个指标上的下界才可能导出无理性。

这里的 `log` 是通常实对数。q-对数公式属于 Sondow--Zudilin 的独立工作，不能通过此变换导入。该模块也没有 \(\pi\)、\(e\) 或 \(\pi+e\) 的迁移结论。
