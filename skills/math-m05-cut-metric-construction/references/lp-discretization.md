# 有限 \(L^p\) 度量的精确坐标离散化

设 \(1\le p<\infty\)，且 \(x_1,\ldots,x_n\) 是实 \(L^p(\mu)\) 中两两不同的点。令 \(E\) 为无序点对集合，\(N=|E|=\binom n2\)。存在 \(y_1,\ldots,y_n\in\ell_p^M\)，其中 \(M\le N\)，使
\[
 \|y_i-y_j\|_p=\|x_i-x_j\|_p\qquad(i,j\in\{1,\ldots,n\}).
\]

这是一条有限距离表示结论。它不主张减少 \(M\) 的量级，也不要求映射从原来的 \(L^p\) 空间线性延拓。

## 构造与证明

选取共同零测集之外的代表元。对 \(t\) 定义
\[
 q(t)=\bigl(|x_i(t)-x_j(t)|^p\bigr)_{ij\in E},\qquad
 s(t)=\sum_{ij\in E}q_{ij}(t),\qquad S=\int s\,d\mu.
\]
点两两不同保证 \(0<S<\infty\)。令
\[
 K=\left\{\bigl(|z_i-z_j|^p\bigr)_{ij\in E}:z\in\mathbb R^n,\ z_n=0,\
              \sum_{ij\in E}|z_i-z_j|^p=1\right\}.
\]
该集合紧。事实上 \(z_n=0\) 且每一个 \(|z_i|^p\) 是求和中的一项，所以标签集有界，条件又闭。对 \(s(t)>0\)，\(q(t)/s(t)\in K\)。由以 \(s(t)d\mu(t)/S\) 为权重的重心表示，
\[
 \frac1S\int q(t)\,d\mu(t)\in\operatorname{conv}(K).
\]
所有 \(K\) 的向量坐标和为一。Carathéodory 定理在这个仿射维数至多 \(N-1\) 的平面中给出至多 \(N\) 个标签 \(z^{(a)}\) 和权重 \(\theta_a\ge0\)，\(\sum_a\theta_a=1\)，使上式等于这些 \(K\) 向量的凸组合。令
\[
 y_i=\bigl((S\theta_a)^{1/p}z_i^{(a)}\bigr)_{a=1}^{M}.
\]
逐点对取 \(p\) 次方并求和，就有
\[
 \|y_i-y_j\|_p^p
 =S\sum_a\theta_a|z_i^{(a)}-z_j^{(a)}|^p
 =\int|x_i-x_j|^p,d\mu.
\]

重复的输入点应先合并，再把同一个输出点复制回去。若只知道伪度量，直接将零距离类商掉也可得到同一处理。

## 有理有限回放

取计数测度上的 \(L^3\)，以及
\[
 x_1=(0,0),\quad x_2=(1,0),\quad x_3=(0,2).
\]
三条点对按 \((12,13,23)\) 排列。两个原子给出的规范化距离立方为
\[
 (1/2,0,1/2),\qquad(0,1/2,1/2),
\]
且总权重分别是 \(2/18=1/9\) 与 \(16/18=8/9\)。两个标签向量的坐标缩放后恰为这两个原子的原始标签，因此所得 \(y_i\) 的立方距离为 \(1,8,9\)，与原三条距离的立方逐条相同。该有限回放只检查构造的归一化和加权方式。

## 原文定位

本构造核对自 OpenAI 预印本 *Subpolynomial dimension reduction in \(L^p\)*，2026-09-23，PDF 第 3–4 页 Lemma 2.1。固定版本为 [官方 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/paper.pdf)，本机 SHA-256 为 `001a29a154753ee273e236ccb13788a8dbba09f9ac4fd59a7707a42ef7d6dc03`。全文的次多项式降维结果还使用后续的电流局部化、稳定过程和 Poisson 构造，并未纳入本接口。
