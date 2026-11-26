# 二元线性码的低阶均匀边缘

设 \(G\) 是 \(m\times n\) 的二元生成矩阵。取 \(U\) 为 \(\mathbb F_2^m\) 上的均匀行向量，令 \(X=UG\)。线性映射在每个像点上的纤维等大，所以 \(X\) 在码 \(C=\operatorname{rowspan}G\) 上均匀。生成矩阵允许有冗余行。

给定一组坐标 \(S\)，边缘 \(X_S\) 恰为均匀当且仅当子矩阵 \(G_S\) 列满秩。若列相关，某个非空的 \(T\subset S\) 满足 \(\sum_{i\in T}G_i=0\)，从而 \(\sum_{i\in T}X_i=0\) 几乎处处。反过来，若到 \(\mathbb F_2^S\) 的线性映射不满射，则它的像落在某个非零线性形式的零集，给出这样的列关系。因此前 \(k\) 阶边缘均匀等价于对偶码中没有汉明重量 1 到 \(k\) 的非零码字。

[精确检查脚本](../scripts/check_binary_code_independence.py)按汉明重量递增枚举二元列和。发现关系时输出最小汉明重量及从 0 起编号的坐标见证。全空间没有非零对偶码字时可约定对偶距离为 \(+\infty\)。脚本通过后给出所检查阶数与下界。枚举规模为 \(\sum_{j=1}^k\binom{n}{j}\)，适合显式小矩阵及较低的阶。

~~~sh
python3 scripts/check_binary_code_independence.py examples/binary-code-pairwise.json
python3 scripts/check_binary_code_independence.py examples/binary-code-triple-witness.json
~~~

示例列为 \(e_1,e_2,e_1+e_2\)。前两阶通过，第三阶返回三列的异或为零，退出码为 1。非法输入退出码为 2。这个有限判据的概率前提是从线性码均匀采样。用于码行独立采样的随机矩阵时，谱极限还需对应随机矩阵定理及其假设。

来源定位为 Chin Hei Chan 的本机稿 *On the Group Randomness of 0-1 Real Sequences from Binary Linear Codes*，SHA-256 70e39427d74b9b47e7fbb7bdc092e0b45f4881035832c73d9e37b06478e99e3d，物理页 1–2 的均匀码行与对偶距离定义。该 PDF 与 arXiv:2607.05418v1 的官方文件 SHA-256 一致。本页的有限判据使用上述独立线性代数证明。[arXiv 修订记录](https://arxiv.org/abs/2607.05418)
