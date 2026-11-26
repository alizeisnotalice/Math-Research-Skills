# 从边卡组恢复有限顶点卡组

Google Cogentic 原稿 *Unconditional Edge Reconstruction of Simple Graphs of Linear Density* 的物理页 10--11，Lemma 2.3 在 \(m\ge4\) 且剥离孤立点后，利用 Edge--Kelly 计数和按边数向下的三角反演推出相同边卡组的图具有相同顶点卡组。本工具仅实现这一有限、可枚举的接口。固定来源 PDF 为 47 页，SHA-256 `170b2fc1f241cc8325e0b5573d444e061b1b7bb8fb3083a3ac88cabd0ce4f196`。[固定发布记录](https://github.com/google-research/google-research/commit/4a7bc8ab0bc7)

对 \(n\)-顶点、无孤立点图 \(G\)，记 \(s(K,Z)\) 为与 \(K\) 同构的生成子图边集数，\(i(J)\) 为 \(J\) 的孤立点数，\(\operatorname{ind}(J,G)\) 为 \(G\) 的顶点删除卡中同构于 \(J\) 的张数。卡组给出每个 \(|E(K)|<m\) 的

\[
s(K,G)=\frac{1}{m-|E(K)|}\sum_{e\in E(G)}s(K,G-e).
\]

对任一 \((n-1)\)-顶点图 \(J\)，以边数从大到小解

\[
(i(J)+1)s(J\sqcup K_1,G)
=\sum_{[J']}\operatorname{ind}(J',G)s(J,J').
\]

同边数项只在 \([J']=[J]\) 出现且系数为 1，故这是单位上三角系统。`scripts/edge_deck_vertex_deck.py` 枚举全部 \((n-1)\)-顶点无标号图类，严格做上述除法，并拒绝负重数、非整除、卡片规格错误或超出 \(n\le6\) 的输入。图输入模式会拒绝孤立点并直接生成顶点卡组交叉核验。只提供卡组时，调用者须已确认它来自无孤立点图，脚本不把可通过整除检查的卡组声明为可实现。

该证书验证的是指定有限卡组的顶点卡组恢复。Google 原稿的线性密度边重构结论与其后续多尺度证明不由这个脚本认证。
