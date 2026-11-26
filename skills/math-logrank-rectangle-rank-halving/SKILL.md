---
name: math-logrank-rectangle-rank-halving
description: 从有限 Boolean 通信矩阵的单色矩形出发，精确核验互补块秩分裂，并把给定矩形或协议分割转为 rank-halving 递归证书。用于审计 Log-Rank 路线的有限接口，不搜索大矩形或认证高秩渐近定理。
---

# 单色矩形与秩减半接口

输入为有限 \(0/1\) 矩阵 \(M\)、一个非空单色矩形 \(A\times B\)，以及可选的已证明密度下界。先用精确有理消元检查实秩，随后检查 Appendix Proposition A.3 所需的互补块秩分裂：

\[
 \operatorname{rank}(M_{A,B^c})+\operatorname{rank}(M_{A^c,B})
 \leq \operatorname{rank}(M)+1.
\]

因此至少一个互补块的秩不超过 \(\lfloor(r+1)/2\rfloor\)。这给出递归协议或单色矩形分割时可实际调用的 rank-halving 接口。

## 已核对的来源与范围

Google Research `cogentic_research_papers/logrank_conjecture/paper.pdf`，固定提交
`4a7bc8ab0bc7`，本机原件 SHA-256
`9c941a918c5e5cea1624adee676c010efb85b60b3cd77455640cd578f54f6bc9`。
物理 PDF pp. 35--36 的 Proposition A.3 证明该秩分裂，并在假设每个秩至多 \(k\) 的 Boolean 矩阵含密度至少
\(2^{-C_0 k^{1/2-\varepsilon_0}}\) 的单色矩形时，给出
\(D_{cc}(M)\le 750C_0r^{1/2-\varepsilon_0}\) 的归约。p. 2 的 Theorem 1.1 是该稿的全局主张。

本技能把 Proposition A.3 的有限秩分裂、单步递归和给定协议分割树作为可调用内容。它不独立认证 Theorem 1.1 的高秩结构定理、Gaussian/KL 论证、论文的全部结论，或尚未发布的 Lean 形式化。

## 单步检查

用 [精确核验脚本](scripts/check_rectangle_rank_halving.py) 读取 JSON。`rows` 为 0/1 行列表，`a_rows` 与 `b_cols` 为零基下标。

```sh
python3 scripts/check_rectangle_rank_halving.py examples/positive.json
python3 scripts/check_rectangle_rank_halving.py examples/not-monochromatic.json
```

第一个调用核对一个 1-单色矩形和秩减半候选。第二个调用以退出码 2 拒绝非单色输入。脚本不会寻找矩形，不能从有限验证推导对任意秩的单色矩形密度定理。

需要把条件性归约用于一条新矩形定理时，另行提供每个 \(k\) 的统一密度界和其证明。只有此界的量词覆盖所有 \(1\leq\operatorname{rank}(M)\leq k\)，Proposition A.3 才能进入协议复杂度结论。

## 给定协议分割树

当一个有限协议已通过选定单色矩形递归展开时，使用 [协议树证书](scripts/check_rank_halving_tree.py) 检查每个节点的秩、选定支路与叶矩形覆盖。

```sh
python3 scripts/check_rank_halving_tree.py examples/three-by-three-protocol-tree.json
python3 scripts/check_rank_halving_tree.py examples/nonmonochromatic-leaf.json
```

首个输入给出 \(3\times3\) 例子的四个单色叶矩形。第二个输入应以退出码 2 拒绝非单色叶。该树仅认证已给定的分割，不能替代矩形发现或原稿的统一密度假设。完整输入字段与范围见[协议树证书说明](references/protocol-tree-certificate.md)。

## 单步递归的行列分块

原单步检查器同时输出低秩互补块与余块的行列索引，并核验各块面积与余块缩减。可用输入字段 low_rank_branch 指定支路。省略时选精确秩较小的一支。[证明与适用范围](references/source-audit.md)
