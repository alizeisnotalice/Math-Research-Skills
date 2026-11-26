---
name: math-l16-prime-sieve-certified-transfers
description: 审查或应用素数筛中的有限局部条件、尾部剔除、Kummer 完全分裂与加权区间到稠密度转移；显式保留条件性解析输入，不把分裂判别或有限算例写成素数密度定理。
---

# L16 · 素数筛的认证转移

用于以下相互容易混淆的转移：多项式的局部避开条件到整数输入密度、加权空区间到连续素数间隙、以及 order-index 条件到 Kummer 完全分裂。这是一个**审计与组装** skill；先固定对象、量词、固定参数和外部输入，再写任何渐近结论。

固定来源、页码和 SHA-256 见[来源清单](references/sources.md)。只在当地页码所给的假设下使用相应组件。

## 1. 多项式 k-幂自由：有限筛与大素数尾部

对 `f=s c g ∈ Z[x]`，先分别记录 `s`、content `c`、primitive polynomial `g`，并逐素数检查 `ρ_f(p^k)<p^k`。在 `k≥2` 且

`T_g(X)=#{X<n≤2X: p^k | g(n) for some p>X}=o(X)`

的**独立上界**已给出时，才能作如下两阶段转移：

1. 固定 `Y`，以 `Q_Y=∏_{p≤Y}p^k` 的 CRT 允许类得到精确有限筛主项 `c_Y X+O(Q_Y)`；content primes 保留精确 local factor，不能一概按 primitive 情形替换。
2. 对 `Y<p≤X` 单独作 root-count union bound，对 `p>X` 只调用上述 tail hypothesis；先令 `X→∞`（`Y` 固定），再令 `Y→∞`。不得交换两个极限，也不得把 `T_g=o(X)` 简化成 Euler product 的形式结论。

若另有固定同余条件，和 `p^k` 条件以最小公倍数合并；不要求、也不可假设重叠条件独立。该转移只给**整数输入**的 k-幂自由值密度，绝不自动给 `n` 或 `f(n)` 为素数的密度。

## 2. 从带权相邻区间到素数间隙

对 `h=floor(λ log X)`，保留两段区间的角色：`J=(m,m+h]` 用于检测一个素数，`I=(m+h,m+2h]` 用于排除后继素数。要从来源的权重命题推出普通起点密度，必须同时有：

- `E(W V_J)→λ` 与独立的上界 `limsup E(W V_J²)≤K_λ`；
- `limsup E(W V_I)≤ε`；
- 固定所选权重族后才有 `E(W²)≤M`。

先选定 `λ>C`，再取 `ε=λ²/(2K_λ)`；`K_λ` 必须与 `ε` 无关，而 `M` 可以依赖已经固定的 `ε`。两次 Cauchy–Schwarz 分别控制加权探测质量和普通起点数量，不能合并或删除任一二阶矩条件。最后取第一个区间的末素数；每个被选中的 prime start 至多对应 `h` 个起点，才把 interval starts 转为不同的连续素数间隙。

该数量型 prime-gap 结论在本 skill 中一律标为**条件性**：它依赖来源 Proposition 2.1 的平滑除数和、Bombieri–Vinogradov 与奇异级数平均估计；本 skill 仅认证 pp.3–4 的 transfer。

## 3. 单底数 primitive root：CRT、Kummer 判别与异常剔除

对于 admissible `a`（整数、非 `−1`、非平方），先构造实际的 `(M,c,u)` 并逐项核验

`M` 是 `8` 的倍数，`c∈{2,4}`，`(u,M)=1`，`c|(u−1)`，`gcd((u−1)/c,M/c)=1`。

CRT 的作用是同时强制 `(a/p)=-1`、上述进程条件及 `p∤a`；不得以“选了 nonresidue”代替 `p∤a` 的验证。对 `p∤aq`，下式是局部 Kummer 的**等价判别**，不是一个计数估计：

`p splits completely in Q(μ_q,a^(1/q))  ⇔  p≡1 (mod q)` 且 `a^((p−1)/q)≡1 (mod p)`。

当一个受控 reservoir 给出 `p−1=c r Q` 时，先由二次非剩余性推出 index 为奇数；若 index 非一，分别处理 `q=Q`（整除有限积 `∏|a^j−1|`）和 `q|r`（应用 Kummer splitting bound）。保持二者的误差来源、范围和 `p∤aq` 条件分开记录。

reservoir 的正下界以及 uniform complete-splitting bound 均为外部/重型解析输入。尤其零点自由区域和其常数不得从局部 Kummer 判别、有限例子或本 skill 推出；引用时标作**条件性解析输入**。

## 4. 多底数情形

只对有限个互异正素数 bases 使用来源的 simultaneous 版本。它明确假设四个 Inputs：uniform Hecke zero-free、marked Type II、block sieve、rough-number density。CRT 只给满足 `gcd(a(a−1),M)=1` 的固定进程；`2` 的二次非剩余性还须由 `p≡5 (mod 8)` 单独处理。完成的结论必须写成“在 Inputs 3.1、4.1、5.1、5.2 下”。

## 有限核验

可运行 `scripts/check_finite_instances.py`。它用纯整数算术检查：

- `x²+1` 的有限 CRT 筛类与直接计数一致；
- 若干小 `a,q,p` 的 Kummer 同余判别与 `X^q-a` 在 `F_p` 中的根数一致。

这只核验有限恒等式和程序实现；不验证大素数 tail、prime reservoir、零点自由区或任一无限素数密度结论。

对数坐标上的固定维平滑同余条件，及 channel 投影后留下的 Ramanujan
残余因子，见[Fourier 与残余类分离](references/fourier-residue-separation.md)。前者
只提供有限维 Fourier 系数的截断控制，后者只计算给定的有限残余和。

## 严格边界

- 永远区分 local splitting equivalence、有限筛恒等式、tail hypothesis、prime-density lower bound 与连续 prime-gap count。
- 不把 local admissibility、CRT 可解性或一个有限算例提升为正 Euler-product density 或素数定理。
- 若修改指数范围、允许负/合数 base、改变 `p∤aq`、或使用依赖 `x` 的同余模数，重新做 local compatibility 和 uniformity 审计。

## 已认证有限子群指数的整除传递

当素域中的子群指数已有上界、且生成元满足共同幂等式时，按[有限子群指数传递](references/cogentic-finite-arithmetic.md)核对整个素域单位群阶的整除结论。

## 有限算术级数上的筛坐标

给定互异筛素数、整数区间与非退化等差参数时，用 [CRT 与容斥](references/jacobsthal-progression-coordinate-crt.md)核对排除剩余类、有限幸存数以及周期平均的误差。

## 平方根见证与给定指数的有限分裂

已提供奇整数的完整素数幂分解、参考根和固定掩码时，用 [Dixon 平方根概率](references/cogentic-dixon-transcript.md) 核验平方同余，按 CRT 和二元秩计算条件分裂概率。

已提供正整数指数 \(E\)、单位底数 \(a\bmod n\) 和待检的素因子 \(q\mid E\) 时，用 [给定指数的分裂检查](references/cogentic-supplied-exponent-splitting.md) 核对 \(a^E\equiv1\pmod n\) 和 \(\gcd(a^{E/q}-1,n)\)。介于 \(1\) 和 \(n\) 之间的 gcd 是因子证书。

## OpenAI 原稿中的方法

- [Twist selection from congruence and density inputs](references/twist-selection-positive-density-arithmetic-1.md)

- [Finite-field tree comparison](references/finite-field-tree-comparison.md)
- [Exact dyadic order-trial bookkeeping](references/openai-exact-dyadic-order-trials-2026.md)
- [Twist and Kummer local interfaces](references/twist-kummer-local-interfaces.md)

- [Rough-cell Buchstab proxies](references/rough-cell-buchstab-proxies.md)
