# 部分流延拓与树叶消元

这是有限图上的精确线性代数工具。它处理有向边的有符号数值，适用于任意域 (F)，也适用于以有理数表示的实数流。它不包含非负流、容量约束、最小费用或随机过程的可实现性结论。

令有限无向图 (G=(V,E)) 的每条边任取一个方向。对端点 (v) 和边 (e)，取 (epsilon_{ve}=+1) 当 (e) 指向 (v)，取 (-1) 当 (e) 离开 (v)。定义

\[
  (\partial x)_v=\sum_{e\ni v}\epsilon_{ve}x_e.
\]

## 固定边上的部分流

给定 (T\subseteq E) 和 (\sigma\in F^T)，存在循环流 (k\in\ker\partial) 满足 (k|_T=\sigma)，当且仅当对 (G\setminus T) 的每个连通分支 (U)，

\[
  \sum_{v\in U}\sum_{\substack{e\in T\\e\ni v}}
      \epsilon_{ve}\sigma_e=0. \tag{1}
\]

证明时将 (\sigma) 在 (E\setminus T) 上置零，令未知边的目标散度为 (-\partial\sigma)。每个分支上，有限连通图的关联矩阵像正好是坐标和为零的向量。为避免把秩公式作为黑箱，可在一棵生成树上把非树边取零，再逐叶消元。式 (1) 正是每个分支所需的零和条件。

这是一条精确的存在判据。它不会给出满足 (0\le k_e\le c_e) 的延拓，除非另行检验带下界、上界的可行流条件。若 (F) 的特征为 (2)，上述正负号合并，仍须按关联矩阵的实际约定重写式 (1)。

## 树上的唯一散度解

若 (T) 是连通的有限树，

\[
  \partial_T z=r
\]

有解当且仅当 (\sum_{v\in V(T)}r_v=0)。这时解唯一。对森林，条件逐连通分支检查，解亦逐分支唯一。

递归步骤固定且可审计。选树叶 (v)，记相邻边为 (h)、另一端点为 (w)。叶方程强制

\[
  z_h=\epsilon_{vh}^{-1}r_v.
\]

删去 (v,h)，并将 (w) 的残差更新为

\[
  r'_w=r_w-\epsilon_{wh}z_h=r_w+r_v.
\]

其余残差不变。总和保持零，直到单顶点树。逆序回填所有被强制的边值。这个过程还给出唯一性，因为每次删去的边值都已被叶方程唯一固定。

## 有理数有限回放

用尾端系数为 (-1)、头端系数为 (+1) 的路径 (0\to1\to2)。目标

\[
  r=(-3,1,2)
\]

给出 (z=(3,2))，而含负边流的 (r=(4,-5,1)) 给出 (z=(-4,1))。这说明该工具允许负值。总和非零的 (r=(1,0,0)) 必须被拒绝。

对三角形 (0\to1\to2\to0)，固定 (T=\{0\to1,1\to2\}) 且 (\sigma=(1,0))。删去 (T) 后，顶点 (1) 单独成分支，其式 (1) 左边为 (1)，所以不存在循环流延拓。该反例必须保留，不能只检查全图的总散度为零。

本机使用 `Fraction` 逐项计算了这三个树例和该分支失败例，结果与上式一致。该有限回放仅核对符号、消元和拒绝门槛。

## 来源与范围

- OpenAI 预印本 *Choiceless polynomial time with counting does not capture polynomial time*，PDF pp. 15–17，Lemma 12。原文给出部分边赋值延拓到零散度向量的分支平衡判据，并以树叶消元证明充分性。SHA-256 `3e16a83bb7707c83952e2068363ee9b0c8e990f258405058686ee686eccbf10f`。[固定版本原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/paper.pdf)
- OpenAI 预印本 *Witnessed symmetric choice is strictly stronger than choiceless polynomial time with counting*，PDF p. 22，Lemma 5.4。原文在 (F_3^3) 上陈述树的唯一散度解。这里的叶消元证明同样适用于任意域。SHA-256 `d648a0d83b5f41b13ec8fd546b97119e52d525013b6d4a4d00fcaa3c386ddb9f`。[固定版本原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/paper.pdf)

两篇的逻辑、对称选择和有限模型主定理没有被本页采用。这里仅保留有限关联矩阵的直接结论。
