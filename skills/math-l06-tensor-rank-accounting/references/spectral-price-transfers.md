# 谱价格的有限转移

本页把 Family 379 中能在固定有限格式内逐项核验的步骤放在一起。每次使用前固定域、所有外部腿的放置、是否讨论精确 rank 或固定次数的 degree-component border complexity。价格 \(H\) 本身不是秩，也不是 border rank。

## 相等边和状态和

对有限 loopless multigraph \(G=(V,E)\)，给每条边 \(e\) 一个状态 \(a_e\in[q]\)，并给每个顶点 \(v\) 的每种邻边状态元组一个独立变量 \(X_{v,\alpha}\)。有限状态和为
\[
 Z_{G,q}(X)=\sum_{a\in[q]^E}\prod_{v\in V}X_{v,a|_{E(v)}}.
\]
它的槽系数张量是每条边上的 equality wire
\[
 E_q=\sum_{i=1}^q e_i\otimes e_i.
\]
因此，对一个固定的顶点切割 \(C\mid V\)，其扁平化秩恰为
\[
 q^{|\partial C|}.
\]
证明只用边的张量积。切割内部的 wire 留在一侧，成为非零向量，跨切割的每条 wire 是秩 \(q\) 的恒等矩阵。这个等式是**精确有限 rank**陈述，不能替代任何图多项式的 circuit、formula 或 border 下界。

同一系数模型中，边端的状态只能由一条 equality wire 连接。把一项的低扁平化秩替换为一个共享的辅助标签，必须给出该标签的秩分解、辅助站点与到每个端点的局部映射。不同求和项可以有不同的辅助站点，输出站点及其放置则必须保持不变。

来源为 *Paths, trees and grids separate Valiant's hierarchy*，PDF pp. 2–6，SHA-256 `5fb87fe08aba63af8258ae71d8105b6a26c94dd8fec1fe57a45e68e6303edb99`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Paths-trees-and-grids-separate-Valiants-hierarchy-November-24-2026/paper.pdf)

## 固定放置的价格规则

设一个兼容谱价格系统在固定站点上给每个非零张量价格 \(H\)。二元 wire 的价格给出站点距离 \(d\)，多方 diagonal 的价格为 \(\delta(S)\log_2q\)。在同一格式和同一输出放置下，有
\[
 |H(T;x)-H(T;y)|\le\sum_i d(x_i,y_i)\log_2q_i,
\]
以及
\[
 H\left(\sum_{j=1}^{L}T_j\right)
 \le\max_jH(T_j)+\delta(S)\log_2L.
\]
前者需要逐个索引由 wire 移动，后者来自直接和折叠到普通和。若 \(T\) 位于一个在同一有限张量格式、同一放置中价格不超过 \(B\) 的集合的 Zariski 闭包，则 \(H(T)\le B\)。该闭包结论使用 \(T^{\otimes n}\) 的单项式维数界，再令 \(n\to\infty\)。

所有三个步骤都要求一个已经给定的谱价格系统。普通和的额外项取决于**输出**站点的 \(\delta(S)\)，并不允许为每个求和项悄悄改变输出放置。闭包是在固定格式内的几何闭包，不能用它将精确 rank 断言升级为 border rank 断言，或反向升级。

来源为 *Circuit lower bounds for Hamiltonian cycle and the permanent*，PDF p. 7，SHA-256 `a7bab8a78dfe73c3f59f190d7c6cc289c30c6340e06afaa5514621f88e62be01`，以及 *Euclidean geometry in the asymptotic spectrum of tensors*，PDF pp. 8–10，SHA-256 `7800f8d812fefb03a080baf10662fa905cb932aaa3da94c8897eb8477fc385e5`。[前者](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Circuit-lower-bounds-for-Hamiltonian-cycle-and-the-permanent-November-24-2026/paper.pdf) [后者](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026/paper.pdf)

## 共享标签的相等过滤

令 \(P,T\) 是不交且非空的站点组，\(K=P\cup T\)，并写
\[
 g=w(P)+w(T)-w(K),\qquad g_-=\max(0,-g),\qquad
 \ell=\log_2(2|K|).
\]
在定义了这些 \(w\) 的同一谱价格系统中，一个 \(b\)-bit equality filter 的最小净成本 \(c_b(P,T)\) 满足
\[
 g_-b\le c_b(P,T)\le g_-b+Cw(K)\sqrt{b\ell}.
\]
当 \(g>0\) 时，选择有限 \(b\) 可得到与字母表大小无关的有界净成本。它只适用于实际构造出的受控局部映射，且必须分别验证一致标签时返回固定非零 \(Q\)，违反等式时输出零。不能从“两个站点都可读出标签”直接推出有 equality filter。

来源为 *An exponential bound for sunflowers*，PDF pp. 5–8，Theorem 3.1，SHA-256 `47b3518a852dfa303732ff3158124b4f8d700ac1d4ea983140ff86c649ee990c`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-exponential-bound-for-sunflowers-November-24-2026/paper.pdf)

## 齐次分量与双线性化

若齐次 \(f\) 的次数是 \(D\)，将变量以 affine forms 替换后得到齐次 \(g\)，且 \(f\) 有 degree-component border size \(s\)，则同一模型中 \(g\) 的界为
\[
 O((s+1)(D+1)^2)\quad\text{(circuits)},\qquad
 O((s+1)^2)\quad\text{(formulas 或 ABPs)}.
\]
这里的对象始终是 degree-\(D\) 分量的系数向量的 Zariski 闭包。一般的非齐次 border approximation 不自动给出这个结论。

在无限域上，若一个 formal rational circuit 在选定 \(A,B\) 的所有中间分母均非零，则在双零元 \(u^2=v^2=0\) 中展开输入 \(A+uX,B+vY\)。每个非线性乘法或除法门为 mixed 系数引入至多两个新的“\(X\)-线性形式乘 \(Y\)-线性形式”的乘积。因此，若有 \(q\) 个这类门，矩阵乘法张量的**精确 bilinear rank**至多 \(2q\)。这只是在已知电路和正则评价点下的有限代数变换。它不证明任何 ω 的下界，也不把 border decomposition 变成 rank decomposition。

前一项来源为 *Paths, trees and grids separate Valiant's hierarchy*，PDF p. 5，SHA 同上。后一项来源为 *The matrix multiplication exponent is nine fourths*，PDF pp. 8–9，Lemmas 2.4–2.5 的双线性化部分，SHA-256 `ddde9ab7755596c6f0210c148985f9761f2c291582e4d0a045987ad1766e5a01`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf)

## 实际有限复算

本机以有理数穷举一条有两条边的三顶点路径、\(q=2\) 的全部边状态。得到 4 个状态和项，跨中间顶点切割的系数扁平化矩阵秩为 \(2=2^{|\partial C|}\)。随后在双零元形式代数中直接展开
\[
 (A+uX)(B+vY)=AB+uXB+vAY+uvXY,
\]
并对 \(2\times2\) 矩阵的四个条目逐项核对 \(uv\) 系数恰为 \(XY\)。这是 equality-wire 与单个乘法门的有限检查，不检验各来源论文的谱价格构造、压缩、复杂度分离或矩阵乘法指数。
