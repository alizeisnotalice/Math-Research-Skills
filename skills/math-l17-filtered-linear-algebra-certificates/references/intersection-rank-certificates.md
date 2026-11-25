# 交空间与三角秩枢轴证书

本页补充两个有限维的线性代数接口。它们分别来自两篇 OpenAI 预印本的局部证明。原文的交叉数和高度二同伦主结论均未作为本页结论使用。

## 成对子空间的总交维数

令 (W) 是维数 (N) 的实向量空间，

\[
U_1,\ldots,U_m,V_1,\ldots,V_m\subseteq W,
\qquad U_i\cap V_i=\{0\}.
\]

则

\[
 \sum_{i,j=1}^m\dim(U_i\cap V_j)
 \le \left\lfloor\frac{m^2}{4}\right\rfloor N.
\]

同一证明适用于有至少 (m) 个元素的任意域。元素不足的有限域不能直接套用下述插值节点论证，除非先给出可保留所需维数的标量扩张步骤。

取互异节点 (t_1,\ldots,t_m)，并对任意 (Z\subseteq W) 定义

\[
 P_h(Z)=\{P\in Z[\xi]:\deg P\le h,\ P(t_i)\in U_i\ \forall i\},
 \qquad k_h(Z)=\dim P_h(Z)-\dim P_{h-1}(Z).
\]

在非节点 (t) 处，除以 (\xi-t) 给出

\[
 \dim\{P(t):P\in P_h(Z)\}=k_h(Z).
\]

Lagrange 插值则给出

\[
 \sum_{h=0}^{m-1}k_h(Z)=\sum_{i=1}^m\dim(U_i\cap Z).
\]

按 (h) 递增选取在一个固定非节点处独立的多项式列，令
\(\ell_h=k_h(W)-k_{h-1}(W)\)。对应的 (k_h(W)\) 阶非零子式
\(\Delta_h\) 满足

\[
 \deg\Delta_h\le\sum_{e=0}^h e\ell_e.
\]

在节点 (t_j)，商映射 (W\to W/V_j) 的多项式矩阵秩比较和
\(U_j\cap V_j=0\) 给出至少 (k_h(V_j)) 的亏秩。因此

\[
 \prod_{j=1}^m(\xi-t_j)^{k_h(V_j)}\mid\Delta_h.
\]

对 (h=0,\ldots,m-1) 求和，使用
\(e(m-e)\le\lfloor m^2/4\rfloor) 及
\(\sum_e\ell_e\le N\)，得到所述界。这里每一项的可除性需要先固定同一个非零子式。只知道每个节点存在某个不同的低秩子式并不构成证书。

### 矩阵差分版本

若 (X_i,Y_i\) 是实 (d\times d) 矩阵且每个 (X_i-Y_i) 可逆，取

\[
 U_i=\{(v,X_iv):v\in\mathbb R^d\},\qquad
 V_j=\{(v,Y_jv):v\in\mathbb R^d\}.
\]

则 (\dim(U_i\cap V_j)=d-\operatorname{rank}(X_i-Y_j))，从而

\[
 \sum_{i\ne j}\operatorname{rank}(X_i-Y_j)
 \ge 2d\left\lfloor\frac m2\right\rfloor
          \left\lfloor\frac{m-1}2\right\rfloor.
\]

输入应提供全部 (X_i,Y_i) 的精确条目，并实际核验每个对角差可逆。近奇异浮点差分不能替代此门槛。

来源为 *The crossing number of complete bipartite graphs*，OpenAI 预印本，PDF pp. 3–5，Lemma 2.1 与 Corollary 2.3，SHA-256 `95b9fc254d730aa35a82585779dfcbe7e1e39840749ef17b329aecc55659f599`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/paper.pdf)

## 逐对角线的三角矩阵枢轴

设 (A=(A_{l,j})_{l,j\in\mathbb Z}) 满足 (A_{l,j}=0) 当 (l>j)。记有限块

\[
 R(l,j)=\operatorname{rank} A_{\{l,\ldots,j\}\times\{l,\ldots,j\}},
 \qquad R(l,j)=0\quad(l>j).
\]

则二次差分

\[
 \mu(l,j)=R(l,j)-R(l,j-1)-R(l+1,j)+R(l+1,j-1)
\]

只取 (0,1)，且 (\mu(l,j)=1) 构成行、列各至多一次的部分匹配。任何有限块的秩等于块内的匹配数。

若依次固定深度 (j-l=0,1,\ldots)，新角元 (A_{l,j}) 只有在它的行、列尚未匹配时才可能新增匹配。把该块经行列操作写为

\[
 \begin{pmatrix}c&r\\u&B\end{pmatrix},
 \qquad r=\rho B,\quad u=B\eta,
\]

则唯一禁止值是 (c=\rho B\eta)。这个标量与 (\rho,\eta) 的选择无关。它只由更小深度的条目决定，所以同一深度中没有共同行列的测试可以独立进行。无限矩阵的说法始终只指这些有限块秩，不能由此推出有界算子、闭值域或 Fredholm 性质。

来源为 *Counterexamples to the Hahn–Wilson conjecture at height two*，OpenAI 预印本，PDF p. 34，Lemma 4.5，SHA-256 `a90ada966eb4154038e29bad22b3110b4a4fbed8e9f6c816563613019e8c931a`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Counterexamples-to-the-Hahn-Wilson-conjecture-at-height-two-September-26-2026/paper.pdf)

## 已运行的精确小例

本机用 `Fraction` 实际计算了两个例子。

1. 令 (m=4,W=P\oplus Q)，其中 (\dim P=\dim Q=1)。前两个指标取
   ((U_i,V_i)=(P,Q))，后两个取 ((Q,P))。交维数总和为 (8)，正好等于
   \(\lfloor 4^2/4\rfloor\dim W=8\)。取
   \(X=(0,0,1,1),Y=(1,1,0,0)\) 的一维矩阵版本，非对角秩和为 (4)，正好等于上式的秩下界。
2. 取有限三角块
   \[
   A=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}.
   \]
   逐块精确 RREF 给出匹配 ((0,1),(1,2))，且
   \(R(0,2)=2\)。全部二次差分均为 (0) 或 (1)。

这些计算重放上述有限公式，不能认证来源论文中的任何全局构造。
