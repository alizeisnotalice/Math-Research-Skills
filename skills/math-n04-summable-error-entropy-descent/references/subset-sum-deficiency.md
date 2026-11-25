# 子集和缺损与无放回方差

对固定的数值输入、指标集合 \(V\)，设 \(N(V)\) 为所有子集的不同精确和的数目，\(D(V)=|V|-\log_2N(V)\)。重复权仍对应不同指标。添加一个指标时 \(N(V)\) 至多翻倍且不会下降，故 \(D\) 的单步增长在 \([0,1]\)。对不交的 \(V,W\)，每个合并和是两块原和的相加，故 \(D(V\cup W)\ge D(V)+D(W)\)。单独反号一批指标 \(F\) 对应对所有子集切换 \(F\) 的选取并平移和值，所以保持 \(D\)。两个同样大小的集合若仅交换一个指标，它们各由共同部分加一步得到，缺损差至多 1。

从固定指标集中无放回均匀抽取 \(v\) 个指标，按顺序暴露。给定前缀，对两个不同的下一指标，交换这两指标耦合剩余的顺序，最终集合最多相差一个位置。于是缺损的 Doob 条件期望在每个暴露步的条件范围至多 1。差分正交，得到 \(\operatorname{Var}D(V)\le v\)。这不对输入数值施加概率模型。空块的缺损和方差均为零。

- OpenAI 预印本 PDF 5 页，Lemma 2.1。算法的空间界尚需其其余参数证明。SHA-256 88f951cb233cf765b963cc3881f761846175bf5932649404d6ef3f69756d78ce。[A Low-Space Algorithm for Worst-Case Subset Sum](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/paper.pdf)
