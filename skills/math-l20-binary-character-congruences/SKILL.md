---
name: math-l20-binary-character-congruences
description: 在有限初等二群角色族中寻找与零顶点同余的非零顶点。适用于 2-adic 群环求值和有限个指定系数的精确匹配，要求核验二进制维数、精度和测试数。
---

# 二进制角色族的同余匹配

设 \(G=(\mathbb Z/2\mathbb Z)^b\)，以 \(x\in\mathbb F_2^b\) 标记其角色。对
\(z_1,\ldots,z_r\in\mathbb Z_2[G]\) 及整数 \(M\ge1\)，只要
\[
 b>r(2^M-1),
\]
便存在非零 \(x\) 使
\[
 z_j(x)\equiv z_j(0)\pmod {2^M}\qquad(1\le j\le r).
\]
这里 \(z_j(x)\) 是把群元 \(g\) 送到 \((-1)^{g\cdot x}\) 的角色求值。该结论仅匹配给定的有限列 2-adic 标量，不会给出群环元素相等、Iwasawa 幂级数相等，或任意解析量的同余。

## 构造与证明核对

1. 固定一个群基，并把每个角色值改写为 Boolean 函数。展开
   \[
   (-1)^{g\cdot x}=\prod_{i:g_i=1}(1-2x_i)
   \]
   后得到
   \[
   z(x)=a_\varnothing+\sum_{\varnothing\ne I\subseteq[b]}
      2^{|I|}a_Ix_I,\qquad a_I\in\mathbb Z_2.
   \]
   若输入不是有限二群的角色求值，或这项整除关系未被独立证明，不能进入本步骤。
2. 对每一个目标 \(z_j(x)\equiv z_j(0)\pmod {2^M}\)，取第 \(0,\ldots,M-1\) 个二进制位。第零位恒定。第 \(h\) 位是 \(\binom a{2^h}\bmod2\)。在 Boolean 立方体上，\((1+Y)^{z(x)}\) 的 \(Y^{2^h}\) 系数是次数至多 \(2^h\) 的 \(\mathbb F_2\) 多项式。
3. 共有 \(rM\) 个方程，其总次数最多
   \[
   r\sum_{h=0}^{M-1}2^h=r(2^M-1)<b.
   \]
   将每个方程 \(P=0\) 的指示子写为 \(1+P\)。所有公共零点的奇偶性是其乘积在 \(\mathbb F_2^b\) 上的和。每个单项式遗漏一个变量，故总和为零。零顶点本来就是解，因而还有非零解。

## 指定 Laurent 系数的较省维版本

若只处理 \(q\) 个固定 Laurent 系数 \(A_i(x)\) 的角色求值，\(A_i\in\mathbb Z_2\)，前一种展开仍成立，但第零位已自动匹配。于是只需匹配位 \(1,\ldots,M-1\)。充分条件为
\[
 b>q(2^M-2).
\]
这是逐个系数的结论。不同 Laurent 系数、分母、极点或随顶点改变的截断范围各自增加一个测试，不能以一项系数匹配代替函数或级数的同余。

## 实施门槛

- 先列出所匹配的标量或系数、精度 \(M\)、总测试数和实际严格不等式。等号情形不受这套奇偶性论证保证。
- 对数值或有限群环输入，使用整数精确求值。参考 [有限复放](scripts/check_binary_congruences.py)，它枚举角色并验算两种维数界下实际找到的顶点。
- 若最终应用需要从系数同余转到商、行列式或特殊化，单独证明清分母和卷积误差，不能由本引理承担。

## 来源和复核范围

- OpenAI 预印本 *A pointwise 2-converse for elliptic curves with rational two-torsion*，PDF p. 8，Lemma 3.4，SHA-256 `df42f33f68fbef7766e5679b298e68e910157f78f2266889fb757824b9e44939`。[固定版本](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/paper.pdf)
- OpenAI 预印本 *Goldfeld's analytic density conjecture and the 2-converse for elliptic curves*，PDF p. 83，Lemma 11.4，SHA-256 `c417858c9fe566daacb7738741dc66e211eea148b3da587eb5ee68eaad208d64`。该版为“指定 Laurent 系数”给出 \(b>q(2^M-2)\) 的变体。[固定版本](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-October-7-2026/paper.pdf)

两篇均为待独立同行审查的预印本。本技能独立保留有限字符值的初等组合证明，未采纳其中的椭圆曲线、Selmer、Heegner 点、L 函数或插值主结论。
