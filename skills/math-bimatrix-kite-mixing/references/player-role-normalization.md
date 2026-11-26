# 玩家角色归一化的精确后悔值传递

## 可调用范围

这是 Google Cogentic 的 *An Exact Polynomial-Time Algorithm for 1/5-Approximate Nash Equilibria in Bimatrix Games* 之 `MaximinKiteNE` 的 Step 2（固定版 PDF 物理页 11；随后紧接的主定理证明亦逐项写出此恒等式）。它是供“行玩家锚定”例程复用的有限代数接口，而不是该文的全局近似均衡定理。

给定收益在 `[0,1]` 的有理双矩阵博弈 `G=(R,C)` 和策略对 `(x,y)`，若外部安全值比较要求交换角色，则令

\[
\widetilde G=(C^\mathsf T,R^\mathsf T),\qquad
(\widetilde x,\widetilde y)=(y,x).
\]

直接由双线性收益和最佳回应的指标改名得到严格恒等式

\[
 f^{\widetilde G}_1(y,x)=f^G_2(x,y),\qquad
 f^{\widetilde G}_2(y,x)=f^G_1(x,y).
\]

因此仅当归一化例程已经给出了 `(\widetilde x,\widetilde y)` 的局部后悔上界时，才可将它按 `(y,x)` 映回原博弈；交换不会改变最大后悔值。脚本不自行计算论文 Step 1 的零和安全值，也不证明应当交换，更不推出 `1/5`、多项式时间或必停。

## 版本和依赖

本机原件 `03_bimatrix_nash_equilibrium.pdf` 与 Google Research 固定提交 `4a7bc8ab0bc7` 一致：SHA-256 为 `ed65664e8817e323a1613f95f4fc98689719c86fb2708974bb69cc1edc139485`，共 41 个 PDF 物理页。2026-11-26 的修订稿 SHA-256 为 `32196e6a64d13fbd216c7e7353a3b44a46e8389eb3d15bad48ffb3dd926cc337`，亦为 41 页；两版此处的转置、策略映射和后悔值等式未变。其余的全局论证仍依赖 Lemma 2.3、Volterra 嵌入、Sections 3--5 与未取得的 Lean 工程。

## 精确回放

```sh
PYTHONDONTWRITEBYTECODE=1 python3 \
  scripts/check_player_role_normalization.py \
  examples/player-role-normalization-swap.json

PYTHONDONTWRITEBYTECODE=1 python3 \
  scripts/check_player_role_normalization.py \
  examples/player-role-normalization-invalid.json
```

前者必须输出 `valid: true`，并精确报告 `f_tilde=(f_2,f_1)`；后者因 `C[0][1]=5/4` 不在归一化收益范围内而以状态码 2 拒绝。全部计算使用 Python `fractions.Fraction`，没有浮点比较。

固定版论文：[Google Research commit 4a7bc8ab0bc7](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/bimatrix_nash_equilibrium/paper.pdf)。
