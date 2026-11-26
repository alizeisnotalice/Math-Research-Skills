---
name: math-l22-arithmetic-progression-certificates
description: 用二进尺度求和把有限无等差数列密度界转为加权界，或用已验证的循环着色构造长区间无单色等差数列的证书。
---

# 等差数列的加权上界与着色证书

先固定等差数列长度 \(k\) 与公差约定。区间上的非平凡数列取正公差。循环群上的公差取非零剩余类，即使数列在循环里出现重复位置也必须测试。若已有循环着色排除的只是两两相异的位置序列，应先补验较低阶公差。

## 有限上界转为加权总量

设 \(r_k(N)\) 是长度 \(N\) 的整数区间中不含非平凡 \(k\) 项等差数列的子集最大基数。若 \(A\subseteq\mathbb N_{\ge1}\) 无此等差数列，且 \(w(n)\ge0\)，则
\[
  \sum_{a\in A} w(a)
  \le \sum_{m\ge0} r_k(2^m)\max_{2^m\le n<2^{m+1}} w(n).
\]
逐个平移二进区间，区间中至多 \(r_k(2^m)\) 个点。用单调收敛合并区间。已认证的一列上界 \(B_m\ge r_k(2^m)\) 也可代入。只证明 \(r_k(N)=o(N)\)，并不足以保证 \(w(n)=1/n\) 时右端可和。需要报告无限上界时，给出实际使用的尺度衰减与尾和估计。

## 循环着色的数位积

设 \(N,k\ge2\)，已经逐公差证明 \(C:\mathbb Z/N\to\{0,\dots,q-1\}\) 没有公差非零的单色 \(k\) 项数列。对 \(0\le n<N^m\) 以 \(N\) 进数位上的 \(m\) 个颜色作为新颜色。若区间中存在单色数列 \(a+jd\)，取最大的 \(i\) 使 \(N^i\mid d\)。因 \(0<d<N^m\)，有 \(0\le i<m\)。第 \(i\) 个数位是
\[
 \big\lfloor (a+jd)/N^i\big\rfloor\bmod N
 =\big(\lfloor a/N^i\rfloor+j\,d/N^i\big)\bmod N.
\]
公差 \(d/N^i\) 模 \(N\) 非零，与基色表冲突。这核对了进位，且 \(N\) 无需为素数。平移区间得到 \(W_{q^m}(k)>N^m\)。向更多颜色扩展时，只需把颜色元组注入所用颜色集。全局 van der Waerden 数量级还需要首先构造满足条件的循环着色，并给出 \(N\) 随 \(k\) 的界。

## 核验与来源

运行 [有限回放](scripts/check_progressions.py) 生成一个八色区间见证，并穷举小尺度的无三项数列子集。有限计算只验收给定的色表和权重实例。

- OpenAI *Quasipolynomial Bounds for Arithmetic Progressions*, PDF p. 82, Proposition 11.1。仅使用无需密度增量的尺度求和。SHA-256 481eaf7730dc4d581e5270cc4d514c6ee2ec386d5af643cf914e20b4d00c59be。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf)
- OpenAI *Quantitative Superexponential Bounds for van der Waerden Numbers*, PDF p. 20, Proposition 7.1。基色表的原文构造与本项数位证明分开。SHA-256 042acea33a57b58d17600a9ec5e0d8d6f424787c5edf28b9d8d5f9bd9297bd18。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf)

## OpenAI 原稿中的方法

- [Square-step Fourier fibre contraction](references/wave4-combinatorics2-square-step-contraction.md)
