# 正则图的有理惯性验收

令 \(G\) 为给定的有限无向简单 \(d\)-正则图，\(A\) 为其整数邻接矩阵，\(n=|V(G)|\)，并设 \(q=d-1\)。本页只在 \(d\ge2\) 时使用。用有理对比基
\[
 B=[e_1-e_n,\ldots,e_{n-1}-e_n]
\]
表示 \(\mathbf1^\perp\)。计算整数 Gram 矩阵
\[
 Q=B^{\mathsf T}(4qI-A^2)B
   =4qB^{\mathsf T}B-(AB)^{\mathsf T}(AB).
\]
以精确分数或无分数对称消元计算 \(Q\) 的惯性。因为正则性使 \(\mathbf1^\perp\) 在 \(A\) 下不变，
\[
 Q\succ0
 \quad\Longleftrightarrow\quad
 |\lambda|<2\sqrt{d-1}\quad\text{对每个非平凡特征值 }\lambda.
\]
这里的 \(B\) 不正交没有问题，它仍是该子空间上的满列秩坐标同构。不得把仅检查若干向量、浮点正特征值或 \(Q\succeq0\) 写成严格谱界。

## 严格门槛及图论后果

若惯性为 \((n-1,0,0)\)，则通过严格测试。由于 \(d>2\sqrt{d-1}\)，这个严格不等式排除两个常见故障：

- 图不连通时，\(\mathbf1^\perp\) 中有另一个 \(d\)-特征向量。
- 图二分时，存在 \(-d\)-特征向量。

反过来，\(Q\succeq0\) 只证明闭阈值 \(|\lambda|\le2\sqrt{d-1}\)。它不能排除上述等号，也不能推出连通或非二分。

先独立检查图是无向、无环、零对角且每行和为 \(d\)。有重边、加权图、随机游走矩阵或归一化 Laplacian 都需要改写二次型。

## 有限精确回放

运行 [回放](../scripts/check_regular_graph_inertia.py)。它以环图 \(C_5\) 为通过例，得到四个正惯性方向。环图 \(C_6\) 为拒绝例，得到 \((4,0,1)\)，其中零方向对应二分图的 \(-2\) 特征值。这个例子只检验惯性流程和严格/非严格的分界。

来源为 OpenAI 预印本 *Deterministic nonbipartite Ramanujan graphs in every fixed degree*，PDF pp. 81–82，特别是 Theorem 8.3 后的精确验收段及 Proposition 9.1 的对比基说明。PDF SHA-256 为 `6d8ea4bb85aae750e6d9e3101e197669ca9f3f5a5e551ad718a2fc9cb1abbd9e`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Deterministic-nonbipartite-Ramanujan-graphs-in-every-fixed-degree-September-23-2026/paper.pdf)

原文的配对、修补、计数和候选枚举证明了其特定构造会找到通过者。本页不采用该存在性或算法结论。
