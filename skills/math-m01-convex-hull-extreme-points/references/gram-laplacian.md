# Gram 与带权 Laplacian

给定内积空间中的 \(z_1,\ldots,z_m\)，满足 \(\sum_i z_i=0\) 且 \(\langle z_i,z_j\rangle\le0\)（\(i\ne j\)）。令 \(G_{ij}=\langle z_i,z_j\rangle\)。Gram 矩阵的行和为零，将对角项替换为 \(\sum_{j\ne i}-G_{ij}\)，得
\[
\left\|\sum_i a_i z_i\right\|^2
=a^\top G a
=\sum_{i<j}(-G_{ij})(a_i-a_j)^2 .
\]
以严格负内积为边。核向量恰在每个连通分量内为常数，所以若图连通，唯一的线性关系方向是 \((1,\ldots,1)\)。这时维数为 \(m-1\)，每个真子族线性独立。任意固定 \(i\) 的 \(m-1\) 个差 \(z_i-z_j\) 形成一组基，因为差的任一线性关系对应总系数为零的向量关系。若图不连通，分量指标会给出额外依赖。

若 \(z_i=\int_{A_i}x\,d\mu(x)\)，且某个有限分割极大化 \(\sum_i\|z_i\|^2\)，合并两块的变化为 \(2\langle z_i,z_j\rangle\)。只有合并是可行竞争者时，才能由极大性得非正性。若同时取最少活跃块的极大者，零内积也被排除。若 \(\mu\) 居中，向量和为零。这个步骤提供极值候选的维数信息。候选是否达到特定全局常数还需另证。

本机 SymPy 1.14.0 用 \(G=I-\mathbf1\mathbf1^\top/m\) 精确核对了 \(2\le m\le8\) 的二次型恒等式、秩 \(m-1\) 与一个主子式 \(1/m\)。

OpenAI 预印本，PDF 5–6 页，Lemma 2.2 的合并和 Gram 步骤。SHA-256 b546ae5fd2ea7011510d5d582148b642e82d39c6ddfb23c16bc9a0a399ffee09。[The Gaussian propeller bound in every dimension](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/main.pdf)
