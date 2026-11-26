---
name: math-gamma-continued-fraction-recurrence
description: 用精确递推生成并审查 Hessami Pilehrood 的欧拉常数有理逼近与非简单连分数。适用于有限系数、收敛子和分母高度核对，不用于无理性结论。
---

# 欧拉常数连分数递推

需要使用 Kh. Hessami Pilehrood 与 T. Hessami Pilehrood 构造的有理序列
\(p_n/q_n\)，或其非简单连分数时调用。先生成精确有理数，再核验有限恒等式。

来源为 *On a continued fraction expansion for Euler's constant*，
arXiv:1010.1420v3，2013-12-29。正式发表记录为 *Journal
of Number Theory* 133(2) (2013)，DOI
[10.1016/j.jnt.2012.08.016](https://doi.org/10.1016/j.jnt.2012.08.016)。
原始下载文件为 `04_Attachment_References/PDF/P01-P21/P20_On_a_continued_fraction_expansion_for_Euler_s_constant.pdf`，SHA-256 为
`0fc9404ea3f673bc2215cbce0858ba8a18a9f8f0c00c73d0465c642953aea0dc`。作渐近或无理性主张前，先读[来源与范围](references/source-and-scope.md)。

## 精确有限构造

取 \(H_0=0\) 且 \(n\geq0\)，原文定义

\[
q_n=\sum_{k=0}^n\binom nk^2k!,\qquad
p_n=\sum_{k=0}^n\binom nk^2k!\,(2H_{n-k}-H_k).
\]

其中 \(D_n=\operatorname{lcm}(1,\ldots,n)\)，约定 \(D_0=1\)。原文证明 \(q_n\in\mathbb Z\)、\(D_np_n\in\mathbb Z\)，并给出

\[
q_{n+2}-2(n+2)q_{n+1}+(n+1)^2q_n=0,
\]
\[
p_{n+2}-2(n+2)p_{n+1}+(n+1)^2p_n=-\frac n{n+2}.
\]

运行 `scripts/gamma_continued_fraction.py --through 12`。脚本从 Theorem A
直接推得有理部分分子和分母，并核验每个收敛子恰为 \(p_n/q_n\)。它接受
\(n=0\) 的初值案例，拒绝负指标。输出的非简单连分数允许有理部分元素。
原文还给出一个整系数等价变换，使用该变换时必须依据原文的对应证明单独核对，不能和脚本的有理部分元素逐项混同。

## 使用范围

Theorem 1 给出 \(p_n/q_n-\gamma\sim2\pi e^{-4\sqrt n}\)。这是次指数收敛，不能直接成为无理性判据。定理的 \(D_np_n\in\mathbb Z\) 也不使 \(D_n(p_n-\gamma q_n)\) 趋于零。超过有限有理逼近的结论，必须另证整系数线性形式、非零子列和清分母余项趋零。
