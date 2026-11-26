# Aguilar–Gatto：有限状态终点桥接证书

## 本次可移植的精确核心

设有限状态空间为 `S`，行随机核为 `P(x,y)`，初始分布为
`mu`，时域为整数 `T>=1`，目标终点集合为非空 `B⊆S`。本补件只在
所有输入概率均为非负有理数时工作。定义

\[
h_T(x)=\mathbf 1_B(x),\qquad
h_t(x)=\sum_{y\in S}P(x,y)h_{t+1}(y),\quad 0\le t<T.
\]

因此 `h_t(x)=P_x(X_T∈B)`。只有在 `h_t(x)>0` 时才允许定义

\[
Q_t(x,y)=P(x,y)\frac{h_{t+1}(y)}{h_t(x)}.
\]

递推立即给出每一已准入行的 `sum_y Q_t(x,y)=1`。若
`p_B=sum_x mu(x)h_0(x)>0`，桥的初始分布为

\[
\mu^B(x)=\frac{\mu(x)h_0(x)}{p_B}.
\]

对每条长度 `T`、终点落在 `B` 的路径 `omega`，逐项相消给出精确等式

\[
\mathbb P_{\mu^B,Q}(\omega)
=\frac{\mathbb P_{\mu,P}(\omega)}{\mathbb P_{\mu,P}(X_T\in B)}
=\mathbb P_{\mu,P}(\omega\mid X_T\in B).
\]

脚本以 `fractions.Fraction` 计算所有这些量；它拒绝浮点数、行和不为一、
零概率目标事件，以及不可达终点的正终点重加权质量。输出中的 `zero_h_states_by_time`
明确列出不能除以零的状态行，因而不是把零支持情况静默当作桥核。

## 与终点重加权似然比的接口

若 `r_T(y)=P_mu(X_T=y)`，给定终点分布 `q` 且 `q(y)>0` 蕴含
`r_T(y)>0`，令 `g_T(y)=q(y)/r_T(y)`（在 `r_T(y)=0` 处取零），再以
`h_T=g_T` 做同一反向递推和 Doob 变换。得到的新路径律的终点分布恰为 `q`，且其
支持内有

\[
\frac{dP}{d\widetilde P}(\omega)=\frac{r_T(X_T)}{q(X_T)}.
\]

要将此式用于**任意**原路径函数的无偏估计，还须额外逐点检查
`r_T(y)>0 => q(y)>0`，即 `P<<P_tilde`。若 `q` 只集中在稀有目标区，脚本会报告该
条件为假；此时它仍是目标条件桥，而不是全路径律的通用重要性抽样证书。

## 原文定位、版本和转移边界

本地来源 SHA-256：
`2b8298fa7a3440f364a85570f0a8b4425ef58978f5d5edfe6b4200be130227e6`。
所读版本为 Aguilar–Gatto, *A Unified Perspective on Exponential Tilt and Bridge
Algorithms for Rare Trajectories of Discrete Markov Processes*, arXiv:2307.12597v2
(14 May 2024；本地 PDF 首页还列提交 2023-07-24、修订 2024-02-02)。正式卷期为 *Phys. Rev. E* 109 (2024), 034113。 [期刊版](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.109.034113)

PDF p.14, Eq. (4.1)--(4.3) 给出固定终点下的前向条件转移：原转移乘以未来命中
终点的概率之比；这正是上面 `Q_t` 在 `B={y}` 时的形式。上面对终点集合的式子是以
指示函数替代固定终点、再由有限求和得到的直接推导，**不是**声称论文逐字陈述了集合版。
PDF pp.15--16, Eq. (4.4)--(4.10) 给出逆向桥及其端点似然比；上面的
`r_T/q` 是在共同可达支持上对此有限状态、任意初始分布版本的显式重写。PDF pp.16--17,
Eq. (4.11)--(4.12) 区分绝对连续与共同支持；脚本分别报告两个方向，避免遗漏零质量端点。

## 明确不转移的结论

- 不声称连续时间、无限状态、非齐次或不可数状态空间的桥存在性。
- 不声称稀有事件估计量的方差最优、有限样本效率或任何渐近收敛。
- 不以这份有限时域代数证书替代 H02 主技能中关于独立数组鞍点近似的条件和误差定理。
- `probability-markov-spectral-mixing` 处理可逆链谱隙/混合；本补件不涉及可逆性、平稳分布或混合时间。

## 复现

```sh
python3 scripts/finite_markov_bridge.py examples/markov-bridge-positive.json --pretty
python3 scripts/finite_markov_bridge.py examples/markov-bridge-impossible-target.json --pretty
```

需要读取实际的有理数转移核时，传入 `--include-kernels`。不可达行以 `null` 表示。

第二条命令必须以状态码 2 拒绝，因为目标事件的精确概率为零。
