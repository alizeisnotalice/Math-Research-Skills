---
name: math-l18-multiplicative-kernel-tensorization
description: 用素数指数分解核验整数族的乘法 GCD 核估计；检查局部集中、Euler 乘积与临界指数。适用于含 LCM、GCD 或约化乘积的非负双序列估计。
---

# 整数约化乘积的核估计

给定 \(1/2<u<1\)、非负 \(x_L,y_M\)，令 \(K_s(L,M)=(LM/\gcd(L,M)^2)^{-s}\)。若 \(s>1-u\)，有
\[
  \sum_{L,M\ge1}(x_Ly_M)^u K_s(L,M)
    \le C_{u,s}\Big(\sum_L x_L\sum_M y_M\Big)^u.
\]
需要有限右端时先检查两边总质量有限。若一个总质量为零，左边为零。

1. 先截为有限支撑。因 \(v_p(LM/\gcd(L,M)^2)=|v_p(L)-v_p(M)|\)，逐个素数处理。固定一对当前指数，把其他坐标上的序列作为切片。递推上界依赖切片总质量，序列本身可在素数间耦合。
2. 对一个素数，归一化切片总质量为概率向量 \(\alpha,\beta\)。在 \(q=p^{-s}\) 足够小时，核总质量上界为 \(1+O_u(q^{1/(1-u)})\)。对有限个小素数直接用 \(\ell^1\) 卷积范数 \((1+q)/(1-q)\)。
3. 乘起常数。大素数尾和由 \(s/(1-u)>1\) 控制。用单调收敛去掉有限支撑。若核加入固定离对角倍数 \(A\ge1\)，单坐标结论中的常数依赖 \(u,A\)，且须另外验证全局核被这些因子的乘积支配。

## 单坐标检查

写 \(T=\sum_{i,j\ge0}q^{|i-j|}A^{\mathbf{1}_{i\ne j}}(\alpha_i\beta_j)^u\)，其中 \(0<q<1/2\)。当 \(T\ge1\)，非对角贡献由 Young 不等式和 \(\|\alpha^u\|_2,\|\beta^u\|_2\le1\) 控制为 \(O_A(q)\)。对角和因而至少为 \(1-O_A(q)\)。由 Cauchy–Schwarz 及 \(\sum_i\alpha_i^{2u}\le(\max_i\alpha_i)^{2u-1}\)，两向量的最大原子都趋于 1。若最大原子不在同一位置，分开这两个位置和其余位置后，对角和为 \(o(1)\)。因此当 \(q\) 足够小时存在公共位置 \(k\)。

设 \(d=(1-\alpha_k)+(1-\beta_k)\)。中心项至多 \(1-c_ud\)。仅一侧偏离 \(k\) 时，按几何权重用 Hölder，距离至少 \(a\ge1\) 的部分代价为 \(O_{u,A}(q^a d^u)\)。两侧都偏离时，Young 给出 \(O_A(d^{2u})\)。因 \(2u>1\)，小 \(d\) 时此项可吸收，于是
\[
   T\le1-c'_u d+C_{u,A}q d^u
        \le1+O_{u,A}(q^{1/(1-u)}).
\]
对 \(q\) 在其余紧离零范围内用卷积范数补齐。若总质量为 1 的非负数组被各项逐点支配，则 \(T\ge1\) 强迫 \(d=O_{u,A}(q^{1/(1-u)})\)。此时两个偏离估计直接给出该数组在对应区域的质量上界。

## 临界检验

独立推导。若 \(0<s\le1-u\)，取每个素数的两个指数 \(0,1\)，两侧均用 \((1-\varepsilon,\varepsilon)\)，其中 \(\varepsilon=cq^{1/(1-u)}\)。对充分小的固定 \(c>0\)，单素数核总质量至少为 \(1+c' q^{1/(1-u)}\)。这是因为该量减 1 的两个主贡献分别为 \(-2u\varepsilon\) 与 \(2q\varepsilon^u\)，且 \(c^u/c\) 可任意大。取有限素数集上的乘积测度实现常数乘积，此乘积随素数集增长而无界，因为 \(\sum_p p^{-s/(1-u)}\) 发散。若 \(s\le0\)，在 \(N\) 个整数上取均匀质量，核至少为 1，左边至少为 \(N^{2(1-u)}\)。因此原形式的常数不能延伸到临界或以下。

来源为 OpenAI 预印本 *The Weak Inhomogeneous Duffin–Schaeffer Conjecture*，PDF pp. 8–9，Lemmas 2.5–2.6。上面的局部估计可由所列初等不等式独立重推。整篇的中心构造、加权 LCM 结论和 Diophantine 主结论需要另外核验。PDF SHA-256 为 d91ccb7b68c5b0e2e081710c3c9012d0d790992703fc3609853953c538bc7203。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/paper.pdf)

用 [有限整数例](scripts/check_kernel.py) 复核核因子分解和可分离质量的乘积等式。
