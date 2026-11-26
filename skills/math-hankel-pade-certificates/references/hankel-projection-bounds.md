# 正矩投影给出的单调有理下界

Timothy Ferguson，*Rational Approximations via Hankel Determinants*。本机 EXT-0025，SHA-256 `8f599e72b8609f5be4a978f2aeb727d41a676b758478ebefb1114dde92c26c41`。Theorem 1、Lemma 2 在 PDF 物理页 2，常数例子在页 2–5，证明在页 6–8。[arXiv:2003.10616v1](https://arxiv.org/abs/2003.10616v1)

## 线性代数证书

令 \(m_j=\int y^j\,d\mu(y)\)，\(j\ge 0\)，并定义 \(a_0=0,\ a_j=m_j\)（\(j\ge1\)）。取 \(G_n=(a_{i+j+2})_{0\le i,j\le n}\) 和 \(b_n=(a_1,\dots,a_{n+1})^\mathsf T\)。

- 若 \(G_n\succ0\)，则 \(Q_n=\det G_n>0\)，且 \(P_n=-\det(a_{i+j})_{0\le i,j\le n+1}\) 满足 \(P_n/Q_n=b_n^\mathsf T G_n^{-1}b_n\)。这是有理 Schur 补恒等式，无需输入 \(m_0\)。
- 若 \(\mu\) 是具有所有所需矩的正测度，该比值为 \(1\) 在 \(\operatorname{span}(y,\ldots,y^{n+1})\) 上的 \(L^2(\mu)\) 投影平方范数。相邻空间嵌套给出单调性，缺口为 \(\int (1-\sum_{j=1}^{n+1} c_j y^j)^2\,d\mu(y)\)，其中 \(c=G_n^{-1}b_n\)。正密度区间确保每一阶缺口为正。
- 收敛到 \(m_0\) 还需常数 \(1\) 属于这些空间并的闭包。Ferguson 的 Lemma 2 对有界区间的正可积密度、或半无界区间上另有指数尾的正密度给出稠密性。令 \(y f(y)d\mu(y)\) 为有限符号测度。如果 \(f\) 和 \(y,y^2,\ldots\) 均正交，该符号测度的全部矩为零。由 Cauchy–Schwarz 及指数尾，其傅里叶–拉普拉斯变换在包含虚轴的带状域解析。靠近原点的 Taylor 系数均为零，变换唯一性给出 \(y f(y)=0\) 几乎处处，从而在这里 \(f=0\)。一般正测度若在 0 有原子，常数的该部分可能无法逼近。

## 三个来源例

- \(\gamma\)。从 \(0<x<1\) 上密度 \(w(x)=1/x+1/\log(1-x)>0\) 和变换 \(y=-x\log(1-x)\) 得到矩。PDF 物理页 3 的 Jacobian 分母第二项里应为 \(\log(1-x)\)。直接求导得 \(\sigma'(x)=-\log(1-x)+x/(1-x)\)，所以 \(K(y)=w(x)(1-x)/(x-(1-x)\log(1-x))\)。当 \(x\uparrow1\)，\(1-x=\exp(-y/x)\le e^{-y}\)，密度满足 Lemma 2 的尾部条件。正矩是
  \[
  a_n=(n-1)!\sum_{i=0}^n(-1)^i{n\choose i}\frac{n-2i-1}{(i+1)^{n+1}},\qquad n\ge1.
  \]
  展开 \(\int_0^1 x^{n-1}(-\log(1-x))^n\,dx-\int_0^1 x^n(-\log(1-x))^{n-1}\,dx\) 即得此式。特别地 \(a_1=1/2\)。
- Euler–Gompertz 常数 \(\delta\)。密度 \(e^{1-y}/y\) 位于 \([1,\infty)\)。取 \(a_1=1\)、\(a_{n+1}=n a_n+1\)。
- \(\zeta(k)\)，整数 \(k\ge2\)。密度 \((-\log(1-y))^{k-1}/[(k-1)!\,y]\) 位于 \((0,1)\)。取 \(a_n=\sum_{i=0}^{n-1}(-1)^i\binom{n-1}{i}(i+1)^{-k}\)。

## 调用与边界

```sh
python3 scripts/hankel_projection_bounds.py --constant gamma --order 3
python3 scripts/hankel_projection_bounds.py --constant gompertz --order 3
python3 scripts/hankel_projection_bounds.py --constant zeta --zeta-power 2 --order 3
python3 scripts/hankel_projection_bounds.py --moments moments.json --order 3
```

自定义输入为 JSON 数组，从 \(a_1\) 开始，使用整数或有理数字符串。输出的投影系数按 \(y,\dots,y^{n+1}\) 排列。脚本核验有限 Gram 主子式、投影恒等式和单调性。对自定义序列，先独立证明目标矩表示以及非零残差与收敛所需条件。源文物理页 5–6 的反例有 \(a_n=(n-1)!\) 和 \(m_0=-\gamma\)，正的移位 Gram 子式无法单独认证目标值。对欧拉常数，本路线的下界不提供整化误差趋零的估计。要验证有限余项符号时，可另算 [Brent–McMillan 严格区间](../../math-euler-constant-irrationality/references/brent-mcmillan-enclosure.md)。
