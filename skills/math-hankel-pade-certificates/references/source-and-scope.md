# 来源、公式与边界

## 已核对的原始版本

- Yann Bugeaud, Guo-Niu Han, Zhi-Ying Wen, Jia-Yan Yao, *Hankel determinants, Pade approximations, and irrationality exponents*, arXiv:1503.02797v2, 1 September 2015。
- 本机原文：`/Volumes/data/Math_Research_Literature/07_Irrationality_Transcendence_Compendium/PDF/EXT-0320_Hankel_determinants_Pade_approximations_and_irrationality_exponents.pdf`。
- 已核对文件 SHA-256：`daf2a3e99f3d3efe5531cd8e7ff3793208fef8b5111e2dadb406902284be3ac8`；28 个 PDF 页。本文引用 PDF 页码（与文内页码不同）。

本技能依据原文 PDF 第 6 页（Theorem 2.1）、第 9--11 页（定义 (3.1)、(3.2)、Theorem 3.1 及其证明）和第 12--15 页（Theorem 4.1）。它没有把文中引用的 [H15a]/[H15b] 的未重核结果当作本技能的已证事实。

## 精确对象与索引

对 `f(z)=sum_{j>=0} c_j z^j`，定义

`H_n(f)=det(c_(i+j))_(0<=i,j<n)`，以及 `H_0(f)=1`。

Theorem 3.1 的边界行列式是

`H_(k,r)(f)=det M`，其中 `M` 前 `k` 行是 `(c_(i+j))_(0<=j<=k)`（`0<=i<k`），最后一行是 `(c_(r+j))_(0<=j<=k)`。

若 `H_k H_ell != 0` 且 `ell>k`，取最小的 `r`，满足 `k<=r<ell` 与 `H_(k,r)!=0`。原文给出

`f(z)-[k-1/k]_f(z) = (H_(k,r)/H_k) z^(k+r) + O(z^(k+r+1))`。

脚本通过独立的线性方程重建 `Q(0)=1` 的分母，再将卷积的低阶项作为 `P`；它另外直接复核该余项公式，而不只信任行列式计算。

## Theorem 2.1：不得合并的门槛

原文 Theorem 2.1（PDF 第 6 页）要求 `d>=2`、整数序列 `(c_j)`、`f` 在单位圆内收敛，且有整数多项式 `A,B,C`：

`f(z)=A(z)/B(z)+C(z) f(z^d)`。

还要求：

1. 所选整数 `b>=2` 满足 `B(b^(-d^m)) C(b^(-d^m)) != 0`，对所有 `m>=0`；
2. 存在递增的无限正整数序列 `(n_i)`，使 `H_(n_i)(f)!=0` 且 `n_(i+1)/n_i ->1`。

满足这些前提时才可得到 `f(1/b)` 超越且无理度指数为 2。有限 Hankel 计算、有限 `m` 的非零检查和数值评估均不能替代其中任何一个“所有/无限”量词。Theorem 4.1（PDF 第 12 页）是更一般的 `A/B+(C/D)f(z^d)` 版本；它还有 `D` 的逐层非零要求，不能误当成 Theorem 2.1。

## JSON 输入

最小的有限证书输入：

```json
{
  "coefficients": [1, 1, 2, 5, 14, 42, 132, 429, 1430],
  "order": 2,
  "later_order": 4
}
```

`coefficients` 必须从 `c_0` 开始，接受 JSON 整数或形如 `"-3/7"` 的有理数字符串。为计算 `H_ell`，至少提供到 `c_(2 ell-2)`。

可选的准入审计段：

```json
"theorem_2_1": {
  "d": 2,
  "b": 2,
  "B": [1],
  "C": [1, -1],
  "nonvanishing_prefix": 5,
  "functional_equation_proof": "external-proof-required",
  "infinite_hankel_proof": "external-proof-required"
}
```

多项式以升幂系数表示，例如 `[1,-1]` 是 `1-z`。脚本精确检查 `m=0,...,prefix-1`；两个 `*_proof` 字段只是审计记录，程序不把文本值当作证明，也不输出 Theorem 2.1 的“准入通过”。
