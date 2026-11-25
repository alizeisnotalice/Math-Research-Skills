# 纤维标签与顺序对齐

## 以实际可达的纤维为标签

给定有限定义域上的 \(f\) 和 \(g=Qf\)。标签是各函数在正规化后定义域上的非空纤维，且正规化映射须满射、函数须沿其下降。从 \(f\) 的一个纤维恢复唯一的 \(y\in\operatorname{im}f\)。边测试将它送到 \(g\) 中对应 \(Qy\) 的纤维。因为 \(\operatorname{im}g=Q(\operatorname{im}f)\)，边映射满射，其纤维大小至多为 \(Q\) 在全部输出空间的纤维上界。对 \(\mathbb F_2\) 上核维数 1 的线性 \(Q\)，上界为 2。

若同一键从多个来源问题生成，需证明所有表示保留相同的类型化坐标及同一个无序纤维划分。合法标签仍须对应整个联合函数能达到的输出。只核对每个分量可达时，联合输出可能无法实现。若全局满足赋值对每一种表示诱导同一个正规化定义域中的点，选该点所在的部分即可得到共享标签。每条边的两个输出由同一原始满足赋值代入，因 \(g=Qf\) 同时接受。正规化、共享键和保持见证这三步分别要有证明。

本机对 \(\mathbb F_2^3\) 的 255 个非空可达子集穷举了末位商投影，所有诱导商纤维至多 2。Theorem 的全局 soundness 还需要手稿后续的相关结构与重复定理。

来源为 OpenAI 预印本 *Perfect completeness for 2-to-1 games*，PDF 14–15 页，Lemmas 3.4–3.5、Proposition 3.6。SHA-256 2691ba6bd2ac7159a2b0900faa180a222fa078e3df8520607b23adf8a3a38aa9。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026/paper.pdf)

## 对有界列表族预先选择抽样律

给定整数 \(s,d\ge1\) 和 \(\eta>0\)，存在 \(r\ge s\) 及 \(\binom{[r]}s\) 上的有理概率律 \(\mu\)。该律对任意标签宇宙 \(M\) 和任意列表族 \(A_I\subset M\) 通用。列表定义在 \(0<|I|\le s\) 的 \(I\subset[r]\) 上，要求 \(|A_I|\le d\)，且 \(\max I<\min J\) 时 \(A_I\cap A_J=\varnothing\)。以 \(\mu\) 抽中 \(B\) 后，至少 \(1-\eta\) 的概率下，每个在 \(B\) 的子集列表内出现的标签都有一个在其所有出现集合中共同的索引。共同索引可以依赖标签、列表与 \(B\)。这个断言的关键是抽样律先于全部列表固定。

1. 对每个 \(r\)，记录各列表的长度与有序槽位上的等价关系即可穷举所有模式。以 \(B\) 不存在共同索引作为 0–1 损失。若对任意 \(r\) 均无误差至多 \(\xi\) 的抽样律，有限极小极大就给出随机模式，使每个固定 \(s\)-子集坏的概率至少 \(\xi\)。
2. 将每个有序 \(t\)-子集上的模式概率向量分到宽 \(1/k\) 的格子。对 \(1\le t\le k\) 逐个应用有限 Ramsey 定理，可取 \(k\) 个指标，使同样大小的子集的所有模式概率相差至多 \(1/k\)。在各有限单纯形取对角子列极限，得到对每个有序限制都一致的模式分布。
3. 将一致有限分布延拓到可数的有理数系。对某个占用槽位取其等价类 \(L\)，定义 \(q(L)=\sup\{\min J:J\text{ 的列表中出现 }L\}\)。若 \(L\) 出现在 \(I\)，分离假设迫使 \(\min I\le q(L)\le\max I\)。固定 \(I\) 的顺序自同构使 \(q(L)\) 的有限分布不变。它们可以把 \(I\) 内相邻两点间的任意有理点送到同一开间隔的另一有理点，因此分布在每个此类开间隔上为零。于是 \(q(L)\in I\) 几乎处处成立。槽位可数，所以同一类的 \(q(L)\) 属于其所有出现集合，与固定 \(s\)-子集有正坏概率矛盾。
4. 用 \(0<\xi<\eta\) 得到实概率律，再在有限单纯形做有理逼近。损失在 \([0,1]\) 内，\(\ell_1\) 逼近误差小于 \(\eta-\xi\) 即可保留所需上界。固定 \(r\) 时还可用线性规划寻求此律，存在性证明没有给出实际可用的规模界。

本机枚举 \(r=s=3,d=1\) 的单标签出现模式。47 种非空模式满足区间分离，其中 10 种没有公共索引。包括同一标签出现在 \(\{1,2\},\{1,3\},\{2,3\}\) 的情形。因而分离仅是抽样结论的输入，不能对每个固定 \(B\) 直接要求交集非空。

来源为 OpenAI 预印本 *Hardness of finding large independent sets in three-colorable graphs*，PDF 11、17–19 页，Lemma 5.1。SHA-256 3ae304fee935151798fc6d30d9f5e706615a7b1a30f85bdb1f3422466af62e44。这里使用抽象有限列表与顺序极限证明，其在三染色归约中的全部假设另查。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026.pdf)
