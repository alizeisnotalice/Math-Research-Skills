# 有限跳过程的全时域退出证书

`scripts/finite_exit_phase_type_certificate.py` 补充有限时域 ETFSP：它只对一个已明确给出的、有限且已经杀死/吸收的 CTMC，精确计算无穷时间的退出类别概率、占用 Green 矩阵、均值、有限阶原始矩及指定 Laplace 点。输入和输出均是有理数；没有浮点 ODE 误差或时间截断余项。

## 来源核对与边界

相关原文为 N. Burch, M. D’Elia, R. B. Lehoucq, “The Exit-Time Problem for a Markov Jump Process,” *European Physical Journal Special Topics* **223** (2014), 3257–3271, DOI [10.1140/epjst/e2014-02331-7](https://doi.org/10.1140/epjst/e2014-02331-7)。本地 PDF SHA-256 是 `3ca42b9ac0084b5b4d5312a791970cd6ae84453946be8f6f9bc8ed6bdd2d5f14`，对应 [arXiv:1411.1817v1](https://arxiv.org/abs/1411.1817)。

该文的 (16)–(18) 在有限跳程连续状态模型中定义交互域退出体积，给出存活概率/跨域流和均值的后向 Poisson 方程。它并未给出下面有限矩阵的 phase-type 定理；以下是对有限吸收 CTMC 独立的线性代数推导。不能将其反推为原文对任意离散化、无限状态截断或一般 balayage 的结论。

## 精确范围

状态划分为暂态集 \(T\) 和若干物理退出类别 \(E_c\)，所有退出态在停止链中必须吸收。检查所有 \(i\in T\) 沿正速率有向边可到达某个退出态。这是有限图上的可核验证书：若有闭的暂态沟通类，它的状态不能到达退出；反之该条件排除了全部闭暂态类，故吸收几乎必然，退出时间 \(\tau\) 是 phase-type，所有矩有限。

设行生成元的暂态块为 \(Q_{TT}\)，\(G=(-Q_{TT})^{-1}\)，类别出口速率矩阵为 \(B_{ic}=\sum_{e\in E_c}q_{ie}\)。则

\[
  G=\int_0^\infty e^{tQ_{TT}}dt,\qquad
  H=GB,\qquad m_1=G\mathbf 1,\qquad m_k=kGm_{k-1}.
\]

这里 \(G_{ij}\) 是从暂态 \(i\) 出发在暂态 \(j\) 的期望占用时间，\(H_{ic}\) 是从 \(i\) 最终由类别 \(c\) 退出的概率。初始行分布为 \(\alpha\) 时，\(\mathbb E_\alpha[e^{-s\tau};E_c]=\alpha(sI-Q_{TT})^{-1}B_{\cdot c}\)。

## 输入限制

- 所有数值必须为整数或如 `"3/7"` 的有理数字符串；拒绝二进制浮点。
- `transient` 和 `exit_classes` 必须严格划分全部状态，退出态行必须为零。初值限于暂态；若原问题含初始已退出质量，应把它作为 \(\tau=0\) 原子单独记账。
- 被 ETFSP 截断丢弃的 `loss` 状态不是物理退出，除非研究对象的定义明确把该跳转计为退出。否则应使用有限时域脚本中的单独 loss 账本。
- 若图可达性失败，工具拒绝均值/高阶矩，而不是把可能无穷的量打印成有限数。

## 例子与实际验收目标

`examples/finite-exit-phase-type.json` 有 \(a\to b\) 速率 1、\(a\to\mathrm{left}\) 速率 1、\(b\to\mathrm{right}\) 速率 2。从 \(a\) 开始，应精确得到：左右退出概率各为 \(1/2\)，Green 行为 \((1/2,1/4)\)，\(\mathbb E\tau=3/4\)，\(\mathbb E\tau^2=1\)，方差 \(7/16\)，且 \(\mathbb E[e^{-\tau}]=5/9\)。

```sh
python3 scripts/finite_exit_phase_type_certificate.py examples/finite-exit-phase-type.json
```

还必须测试一个不能图可达退出的闭暂态状态；脚本应以非零状态退出，不产生全时域有限矩证书。
