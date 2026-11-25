# 来源、公式与证明边界

## 固定来源

- OpenAI, *Short Egyptian fractions*, 2026-09-25，Family 025。
- 本机盘点：`current/Short-Egyptian-fractions-September-25-2026/Short-Egyptian-fractions-September-25-2026.pdf`；SHA-256 `25eebdc1f077f2451bada4d3f8301b59f8158dcdb9019425ce555c5e9c5a2646`。
- 固定版本：[PDF（OpenAI math 仓库提交 3344da5）](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Short-Egyptian-fractions-September-25-2026/Short-Egyptian-fractions-September-25-2026.pdf)。
- 核对位置：第 5 页 Lemma 2.2、Lemma 2.3；第 6 页两者的证明。

本文只蒸馏上述两个引理，不采纳 Proposition 2.1 或 Theorem 1.1 的未复核外部输入。

## 去重的实质

将重复的分母 (d) 写为 (2p) 或 (2p+1)。直接通分给出
\[
\frac2{2p}=\frac1{p+1}+\frac1{p(p+1)},
\qquad
\frac2{2p+1}=\frac1{p+1}+\frac1{(p+1)(2p+1)}.
\]
在 (0<x<1) 的正项和中，没有分母 (1)，也没有重复的分母 (2)。故偶数公式只在 (p\ge2) 使用、奇数公式只在 (p\ge1) 使用，新分母均为正整数且不为 (1)。项数保持为二，和不变；分母总和的增量分别是
\[
(p-1)^2\quad\hbox{和}\quad2p^2,
\]
均为正。

终止不能只从“分母在增大”推出。固定正有理 (x) 与项数 (k) 时，非降列表是有限的：首个分母不超过 (k/x)；固定它后，对余下正和及 (k-1) 项归纳。每个替换仍在这个有限集合内并严格增加分母和，所以不可能无限进行。这也解释了为什么 (x=1) 不在该引理的范围：重复的 (2) 会给出零增量的退化替换。

## 贪心界的实质

对正状态 (x=A/C<1)，令 (z=\lceil C/A\rceil=\lceil1/x\rceil)。则
\[
0\le A'=Az-C<A,qquad C'=Cz\le C^2.
\]
后一式用 (A\ge1) 所以 (z\le C)。若 (A'>0)，分母尚未首次达到 (T) 时有 (C<T)；下一步因此给出 (C'<T^2)。分子始终不超过初始 (a)。

又由 (\lceil1/x\rceil\le1+1/x)，正余数满足
\[
0\le x-\frac1{\lceil1/x\rceil}\le\frac{x^2}{1+x}.
\]
第一次正余数小于 (1/2)，此后至少平方递减；第 (j\ge1) 个正余数至多 (2^{-2^j+1})。若尚未停止，整数分子给出 (x_j\ge1/C_j>1/T)。当 (2^j-1\ge\log T/\log2) 时矛盾，得到技能入口所列步数上界。所有正状态小于 (1)，所以 (z\ge2)。

这些是局部代数和终止/计数结论。它们不保证贪心项彼此不同，也不保证任何后续密集集、分解或全局长度界。
