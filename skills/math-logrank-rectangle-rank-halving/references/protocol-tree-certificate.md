# 有限 rank-halving 协议树证书

Google Cogentic 的 *Breaking the Square-Root Barrier for the Log-Rank Conjecture* 在物理 PDF pp. 35--36 的 Proposition A.3 中，以一个给定的单色矩形为节点，将当前矩阵划分为单色块、一个满足 rank-halving 的交叉块与一个面积缩小的余块。该稿的全局结论还需要统一的单色矩形密度假设。

`check_rank_halving_tree.py` 只检查用户已经提供的有限分割树。每个 `split` 在其父矩形的行、列索引中给出 `a_rows`、`b_cols` 和 `low_rank_branch`。程序以有理 Gauss 消元检查

\[
 \operatorname{rank}(M_{A,B^c})+\operatorname{rank}(M_{A^c,B})
 \leq \operatorname{rank}(M)+1,
 \qquad
 \operatorname{rank}(\text{selected branch})\leq\lfloor(\operatorname{rank}(M)+1)/2\rfloor.
\]

它递归检查低秩块与余块，并要求每个叶矩形单色、叶矩形精确无重叠覆盖根矩阵。输出树中实际使用的秩、密度、叶数和分割面积。

这是一份给定有限协议分割的证书。它不搜索单色矩形，不给出某秩类的统一密度下界，也不证明原稿 Theorem 1.1 或一般通信复杂度上界。
