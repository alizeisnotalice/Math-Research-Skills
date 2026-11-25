# 锚点消去与符号平滑

## 固定末端位置的候选差

令 \(x,y\) 在索引 \(0,\ldots,d-1\) 一致。对相同的元组判定、相位和阻尼因子，在所有 \(i_1<\cdots<i_k=d+m\) 上各自求和为 \(s_x(m),s_y(m)\)。同一元组的因子只依赖被查询的位置和这些位置的字值。对 \(m<0\)，每个查询都在一致前缀内，故差为零。差生成式 \(\sum_m(s_x(m)-s_y(m))z^m\) 不含负幂。

把相邻差分区分为固定为 1 的边和自由边。若每条自由边至少被一个衰减指数中的区间差覆盖，则所有衰减共同给出 \(\exp(-\lambda\sum_{\rm free}g)\)。从固定末端向前，松开边界后，每条自由边的求和至多 \(1/(e^\lambda-1)\)。整体系数至多这个数的自由边次数乘各掩码的前置常数。区间端点可以重复，但必须按它实际覆盖的边计量。该界只控制系数大小与负幂消去；比较信号的下界仍需另证。

本机对 \(x=0110,y=0101\)、两位置均须为 1、自由边因子 \(2^{-g}\)，精确得到首异位置锚定差 \(1/2-z/4\)。

## Prouhet 符号与公平二项平滑

令 \(\sigma_j=(-1)^{\operatorname{popcount}(j)}\)，\(0\le j<2^s\)，\(\pi_g\) 是 \(g\ge1\) 次公平试验的二项分布。用 \(\widehat h(z)=\sum_jh_j e^{ijz}\)，按二进制展开得
\[
\widehat\sigma(z)=\prod_{a=0}^{s-1}(1-e^{i2^az}),\quad
|\widehat{\pi_g}(z)|=|\cos(z/2)|^g\le e^{-gz^2/8}
\quad (|z|\le\pi).
\]
第一式也给出所有 \(r<s\) 的 \(\sum_j\sigma_j j^r=0\)。第二式用 \((\log\cos u)'=-\tan u\le-u\) 推出。移位或反射公平二项分布只改变相位。再用 \(|1-e^{iw}|\le|w|\)，Fourier 反演与 Parseval 分别给
\[
\begin{aligned}
\|\sigma*\pi_g\|_\infty&\le\frac{2^{s(s-1)/2}}{2\pi}(8/g)^{(s+1)/2}\Gamma((s+1)/2),\\
\|\sigma*\pi_g\|_2^2&\le\frac{2^{s(s-1)}}{2\pi}(4/g)^{s+1/2}\Gamma(s+1/2).
\end{aligned}
\]
范数用整数计数测度。若 \(s,g\) 同时变化，要保留 Gamma 和二进权，而不能只写 \(g\) 的幂。这个局部平滑估计仍需嵌入具体概率模型，才能成为迹分布之间的距离界。

本机以阶 \(s=4\)、\(g=32\) 核对四个矩消去，实际卷积在共同分母 \(2^{32}\) 上的最大绝对分子为 \(223284630\)。

- OpenAI 预印本 PDF 3–4 页，latest-anchor 和系数预算。SHA-256 56113d1f2019792bc3fe96cccde891a44de1c2e5bea1447ddea254051219bece。[A latest-anchor induction with spectrally compact masks for worst-case trace reconstruction](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026/paper.pdf)
- OpenAI 预印本 PDF 25 页，Lemma 5.2。本文显式写出 Gaussian 积分的常数。SHA-256 6b28f84fe939dfe5b740403156413f1d807d1ddad70c38b0f50f12e486dc7596。[Quantitative lower bounds for trace reconstruction](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf)
