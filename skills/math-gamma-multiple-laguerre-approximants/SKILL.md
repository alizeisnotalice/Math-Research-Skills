---
name: math-gamma-multiple-laguerre-approximants
description: 用 Wolfs–Van Assche 的混合型多重 Laguerre 显式有限和生成欧拉常数有理逼近，并审计算术整化、约分、余项和渐近障碍。
---

# 多重 Laguerre 逼近的算术工作台

本机全文 G09 / EXT-0020 对应 arXiv:2404.09799v3，SHA-256 d56423c36c73e318ae6850d1c8a36a309766db668041d9c3161500c54adf9459。具体构造见作者稿物理页 9 Proposition 2.5，整化见页 10 Proposition 2.6，整体估计见页 3 Theorem 1.2。正式引用使用 *Combinatorial and Number Theory* 14 (2025), 141–162。[正式版](https://doi.org/10.2140/cnt.2025.14.141) · [作者稿 v3](https://arxiv.org/abs/2404.09799v3)

## 直接生成系数

设 H₀=0、Hⱼ=Σᵢ≤ⱼ1/i，bₖ=binom(n,k)²/k!，cₖ=binom(n+k,k)，Bₖ=Σ₁≤ℓ≤ₙ (−1)^ℓ binom(n+k,n−ℓ)/ℓ。

- F₂(x)=Σₖ bₖcₖxᵏ。
- F₁(x)=Σₖ bₖ[cₖ(3Hₖ−2Hₙ₋ₖ)+Bₖ]xᵏ。
- 原文的混合型正交函数为 F₁(x)−F₂(x)(γ+log x)。直接研究 γ 取 x=1。
- 取 D=n!·lcm(1,…,n)。Proposition 2.6 给出 n!F₂∈Z[x] 和 DF₁∈Z[x]。同乘 D 后形成整数对 (P,Q)，同时保留约掉 gcd(P,Q) 后的原始整数对。

用 [整数对生成脚本](scripts/laguerre_pairs.py) 复现或扫描小指标，例如 python3 laguerre_pairs.py 1 2 3 8。脚本还核对系数整化命题在每个给定 n 的有限多项式上成立。以 (P,Q) 为基线，给出待研究素数及同一 n 下的整除模式。对统一算术增益的猜想，优先从有限和证明各项的分母与跨项消去，再转为可证明的共同因子下界。

## 余项和进展判据

Theorem 1.2 在 x=1 给出绝对误差 O(exp(−4n^(3/4)+n^(1/2)+3n^(1/4)/8))。用 D 乘清分母时，log Q 的主阶为 n log n。因而论文给出的误差上界乘 Q 以后不足以认证 Qγ−P 趋零。若提出更好的 gcd、参数选择或余项界，用同一缩放计算 log|Q|+log|γ−P/Q|，并另证非消失。绝对误差上界本身不提供误差下界。

要移植到新正交族，先重做权函数、矩消失和分支的推导。通过递推推断主导解时，核对初值、递推起点和投影系数。高精度残差仅用于猜测符号及选择指标；严格非零须有积分符号、行列式或认证区间。

需要 Aptekarev 或 Rivoal 的独立递推作对照时，读 [两条精确对照递推](references/comparison.md)。

从 Gamma 导数矩、Bernoulli 正矩或 Legendre 修正矩开始，读 [三类矩和 Padé 输入](references/legendre-pade-moments.md)。按分支保留余项、归一化和分母门槛。

## 文献复核采用的构件

- [Aptekarev gamma pairs from a finite Jacobi--Laguerre formula](references/jacobi-laguerre-aptekarev-gamma-pairs.md)
