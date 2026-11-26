# 有限原子 ideal-sparsity 的精确分解

本附件给 B03 增加一个有限、可复核的前处理：当原子测度已显式列出，且每个原子满足图的非边双线性理想 `x_i x_j=0`，把该测度按图的极大团拆为低维局部原子测度，并逐个重算指定单项式矩。它不构造 Moment--SOS 松弛，也不替代 C03 的 PSD、平坦延拓或 SDP 证书。

## 来源、正式版本与实际核对

- Milan Korda, Monique Laurent, Victor Magron, Andries Steenkamp, “Exploiting ideal-sparsity in the generalized moment problem with application to matrix factorization ranks,” *Mathematical Programming* **205**, 703--744 (2024), DOI [10.1007/s10107-023-01993-x](https://doi.org/10.1007/s10107-023-01993-x)。出版方记录：2023-07-08 online，2024 issue。
- 本地 SHA-256 `d2ee235cf7790ae962261d9030372694b43f3f51e6a310c6739341d431e39bc8` 的候选文件是 2023-07-11 预印本印本，不应被当作正式排印版。已另核对 [arXiv:2209.09573v2](https://arxiv.org/abs/2209.09573) 的 §3.1：式 (2)--(11)、Proposition 6 及其完整双向证明、Theorem 7 及其证明。

源文把非边集 `overline(E)` 的约束写成 `x_i x_j=0`。于是每个支持集是图 `G=(V,E)` 的团，故包含于某极大团；Proposition 6 用这些极大团覆盖 `K`，再用按团顺序选择的互不相交集合 `Lambda_k` 分割原测度。正向将局部测度零填充并相加；反向把原测度限制到 `Lambda_k` 后投影。两方向都保持目标和每一个积分约束。

## 本工具的独立有限证明

对每个显式原子 `a`，脚本精确检查所有非边积 `a_i*a_j=0`。因此其非零坐标集不含任何非边，即为团，必包含于一个极大团。工具以极大团的字典序作固定顺序，将原子分配到第一个包含该支持的团；零向量也按此规则只分配一次。局部原子坐标就是原坐标在该团上的限制，零填充后恢复原子本身。因此，有限测度的和以及每个要求的单项式积分均逐项保持。所有运算使用 `fractions.Fraction`。

这比“只看单个低阶矩为零”严格得多：本工具需要逐个列出的原子满足每一个非边等式，并要求所有权重非负（源文的有限正 Borel 测度）。它也不验证 `g_j>=0` 等其他半代数约束；调用者必须已分别检查这些约束。若原子表不完整、测度不是有限原子、坐标仅为浮点近似，或目的在于获得 Theorem 7 的 SDP 下界/收敛性，本工具不适用。

## 使用

```sh
python3 scripts/finite_ideal_sparse_decompose.py examples/path_graph_exact.json
python3 scripts/finite_ideal_sparse_decompose.py examples/nonedge_violation.json
```

输出中的 `decomposed` 只表示上述有限分解及指定单项式的 exact recombination；`not_ideal_feasible` 给出违反的原子、非边和精确乘积。
