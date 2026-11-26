---
name: math-n12-frostman-energy-preprocessing
description: 将有界支撑测度的 Frostman 球质量界、有限 Riesz 能量、紧限制与随机正交投影相互转换，并核对维数范围。
---

# N12 · Frostman 能量与投影预处理

用于将几何或分形问题的测度输入整理成可用于后续估计的有限能量、球质量界或典型正交投影。给出测度的总质量、支撑直径、指数和所需保留质量。此技能处理预处理，不提供距离集、restriction 或 Falconer 型结论。

## 三个可复核转换

令 \(\mu\) 为 \(\mathbb R^d\) 中有界支撑的有限正 Radon 测度，定义
\[
 I_t(\mu)=\iint |x-y|^{-t}\,d\mu(x)d\mu(y).
\]

### 从球界到有限能量

若 \(0<t<s\)，且对所有 \(0<r\leq1\) 有
\[
 \mu(B(z,r))\leq C r^s,
\]
则 \(I_t(\mu)<\infty\)。对每个 \(x\)，按距离 \(2^{-j}\) 的 dyadic annuli 分解近对角部分。第 \(j\) 层最多贡献常数倍 \(C2^{-j(s-t)}\)，可求和。距离至少 1 的部分由 \(\mu(\mathbb R^d)^2\) 控制。

这个方向必须严格使用 \(t<s\)。临界 \(t=s\) 时几何级数不再可求和，不能把球界直接当作有限 \(s\)-能量证书。

### 从有限能量取得紧的球界限制

若 \(I_t(\mu)<\infty\)，则对任意 \(\varepsilon>0\)，存在紧集 \(K\) 使
\[
 \mu(K)\geq\mu(\mathbb R^d)-\varepsilon,
 \qquad
 (\mu\!\restriction_K)(B(z,r))\leq M(2r)^t
\]
对所有 \(z\) 和 \(r>0\) 成立，其中 \(M<\infty\) 依赖于所选限制。

证明时先取势函数
\[
 U_t^\mu(x)=\int |x-y|^{-t}\,d\mu(y).
\]
有限能量意味着它在 \(\mu\)-几乎处处有限。选取 \(M\) 使 \(\{U_t^\mu\leq M\}\) 丢失的质量足够小，再由 Radon 正则性取紧的 \(K\) 。若 \(K\cap B(z,r)\) 非空，从其中选 \(x\)，则
\[
 (\mu\!\restriction_K)(B(z,r))\leq\mu(B(x,2r))
 \leq (2r)^tU_t^\mu(x).
\]
空交时结论平凡。这里是限制后的测度满足球界。原测度不因有限能量自动有处处球界。

### Haar 典型正交投影保留能量

令 \(0<t<m\leq d\)，\(P_V\) 是到 Haar 随机 \(m\)-维线性子空间 \(V\) 的正交投影。若 \(I_t(\mu)<\infty\)，则
\[
 I_t((P_V)_\#\mu)<\infty
\]
对 Haar 几乎每个 \(V\) 成立。

所需核界为
\[
 \int_{G(d,m)} |P_Vz|^{-t}\,dV\leq c_{d,m,t}|z|^{-t}\quad(z\ne0).
\]
它来自旋转不变性，以及单位向量前 \(m\) 个坐标在原点附近的径向密度积分 \(\int_0^1r^{m-1-t}\,dr\)。将此界对 \((x,y)\) 积分并用 Tonelli，得到投影能量的有限平均，因而几乎处处有限。\(t<m\) 是这里的可积性门槛。

## 使用顺序

1. 先记录测度是否有界支撑、有限质量，以及具体的 \(s,t,m\)。
2. 已知 Frostman 界时，选严格较小的能量指数 \(t<s\)。
3. 需要严格球界时，从有限能量做紧限制，并报告丢失质量 \(\varepsilon\) 与新常数 \(2^tM\)。
4. 需要投影时，先验证 \(0<t<m\)，再把“几乎每个 \(V\)”保留为量词。后续若要固定一个投影，必须另行选择满足该结论的 \(V\)。

## 来源与范围

三个步骤来自 OpenAI 预印本 *The Falconer distance conjecture in all dimensions*，PDF p. 6，Lemma 2.1，SHA-256 `98a7e721547308b9cec673140ed1d86ecef44d73c56995b68a2c46fd8d4beb23`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/paper.pdf)

本技能独立重列该引理的测度论证明。原文随后所用的线性投影增益、距离集论证和主定理属于其他输入链，未被此技能采用。

运行 [有限模型检查](scripts/check_interval_energy.py) 核对单位区间 Lebesgue 测度的精确 \(I_{1/2}=8/3\)、球界及坐标投影。该检查只是一个有界实例，不代替上述一般证明。

## OpenAI 原稿中的方法

- [Wave 4 PA3: spectral variogram and signed logarithmic energy](references/openai-wave4-pa3.md)
