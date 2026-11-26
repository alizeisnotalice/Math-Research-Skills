---
name: math-gamma-continued-fraction-recurrence
description: 用精确递推生成并审查 Hessami Pilehrood 的欧拉常数有理逼近与非简单连分数。适用于有限系数、收敛子和分母高度核对，不用于无理性结论。
---

# 欧拉常数连分数递推

当需要 Hessami Pilehrood 的 \(p_n/q_n\) 或其非简单连分数时使用。先生成精确有理数并核验有限恒等式；原始来源、版本、渐近范围和反例边界见[来源与范围](references/source-and-scope.md)。

取 \(H_0=0\)、\(n\ge0\)，并定义

\[
q_n=\sum_{k=0}^n\binom nk^2k!,\qquad
p_n=\sum_{k=0}^n\binom nk^2k!\,(2H_{n-k}-H_k).
\]

令 \(D_n=\operatorname{lcm}(1,\ldots,n)\) 且 \(D_0=1\)。原文给出 \(q_n\in\mathbb Z\)、\(D_np_n\in\mathbb Z\)，以及

\[
q_{n+2}-2(n+2)q_{n+1}+(n+1)^2q_n=0,
\quad
p_{n+2}-2(n+2)p_{n+1}+(n+1)^2p_n=-\frac n{n+2}.
\]

## 精确有限回放

运行既有命令：

~~~sh
python3 scripts/gamma_continued_fraction.py --through 12
~~~

脚本由 Theorem A 生成有理部分分子/分母，并核验每个收敛子为 \(p_n/q_n\)。它接受 \(n=0\) 初值、拒绝负指标；输出的非简单连分数允许有理部分元素。原文的整系数等价变换须按原文另行核对，不能与脚本的有理部分元素逐项混同。若要同时逼近 \(\gamma\) 与 \(\zeta\) 值，读 [Bell 多项式逼近](references/bell-gamma-zeta-approximants.md) 并运行其有限系数脚本。

## 不可跳过的边界

Theorem 1 的 \(p_n/q_n-\gamma\sim2\pi e^{-4\sqrt n}\) 是次指数收敛；\(D_np_n\in\mathbb Z\) 也不意味着 \(D_n(p_n-\gamma q_n)\to0\)。若意图得到无理性或逼近指数，必须回到[共享整数线性形式门槛](../math-integer-linear-form-rates/references/integer-linear-form-proof-gates.md)，对同一整化后形式证明无穷子列非零与趋零。平衡次数多项式连分数的阶乘约化另见[准入说明](references/pcf-factorial-reduction-admission.md)。

## 补充来源中的方法

- [Exact folding of a polynomial continued-fraction layer](references/supp-14-esma-folding-transform.md)
