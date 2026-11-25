# π 的截断对数分母证书

本页从 Family 017 的算术半边抽出可复用的条件性引理：一旦另有论证选出非零的满行子式，截断对数的分母可在高斯整数环中统一清除。它不提供该子式的非零性，也不把 \(\pi\) 的插值定理迁移到 \(\gamma\)。

## 原文、范围与前置非零性

来源是 OpenAI, *The irrationality exponent of pi is 2*，2026-09-24，Lemma 3.1、式 (3.1)--(3.8)，PDF 12--13 页。本机原件为

`/Volumes/data/Math_Research_Literature/02_Recent_Math_Papers/OpenAI/current/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf`

其 SHA-256 是 `26eec5de7ac9dc49d28183fdea458e0858bc3323b5ba93c3d41bb105d8e3eab6`。页级提取件是

`/Volumes/data/CodexTemp/Math-Research-Skills/openai-corpus.gruR7ANo/pages/26eec5de7ac9dc49d28183fdea458e0858bc3323b5ba93c3d41bb105d8e3eab6.json`。

取正有理数 \(w_0,v_0,\theta,F_0\)，正整数 \(m,K,H\)。取整数 \(p_i\ne0\)、\(q_i\ge2\)，并令

\[
w_i=\lceil\log q_i\rceil,\qquad
r_i=\frac{2\mathrm i\,p_i}{q_i},\qquad
T_i=\left\lceil\frac{F_0w_i}{v_0}\right\rceil,
\qquad
G_i(t)=\sum_{1\le k<T_i}\frac{(-1)^{k+1}t^k}{k}.
\]

这里 \(\mathrm i^2=-1\)，不是指标。完整的 \(\pi\) 应用还假设 \(|\pi-p_i/q_i|\le q_i^{-\nu}\)（\(\nu>2\)）、加权插值的全部条件，以及 \(F_0>2/\theta\)。以下分母论证本身只用显示出的整数性、权约束和已选定的非零子式。

令列为 \(Y^hX^\alpha\)，满足

\[
w_0h+w_\alpha\le H,\qquad w_\alpha=\sum_iw_i\alpha_i,
\]

令行为 \(\rho=(j,s,\beta)\)，满足

\[
0\le j<K,\qquad v_0s+\frac{w_\beta}{\theta}<H.
\]

条目是 \((1+t)^h\prod_i(jr_i+G_i(t)+u_i)^{\alpha_i}\) 中 \(t^su^\beta\) 的系数。必须先由独立的秩/插值论证选出一个使用所有这些行的方形子式 \(\Delta_H\ne0\)。在原文中，这一步来自 Theorem 2.1，并且只对固定参数后的充分大、充分可整除 \(H\) 声明；本页没有替代该定理。

## 逐行缩放和整性

令

\[
L_i=\operatorname{lcm}(1,\ldots,T_i-1)\quad(L_i=1\text{ 若 }T_i=1),
\qquad
D_H=\prod_iL_i^{\lfloor H/w_i\rfloor}.
\]

将列 \(Y^hX^\alpha\) 乘以 \(\prod_iq_i^{\alpha_i}\)，将行 \((j,s,\beta)\) 乘以 \(\prod_iq_i^{-\beta_i}\)。缩放条目在 \(\alpha\not\ge\beta\) 时为零；否则精确为

\[
\prod_i\binom{\alpha_i}{\beta_i}
[t^s](1+t)^h\prod_i\bigl(q_i(jr_i+G_i(t))\bigr)^{\alpha_i-\beta_i}.
\]

这里 \(q_ijr_i=2\mathrm i j p_i\in\mathbb Z[\mathrm i]\)，而 \(G_i(t)\) 的系数属于 \(L_i^{-1}\mathbb Z\)。故该条目的分母整除 \(\prod_iL_i^{\alpha_i-\beta_i}\)。又 \(\alpha_i\le\lfloor H/w_i\rfloor\)，所以它整除 \(D_H\)。因此，把缩放矩阵的每一项乘以 \(D_H\) 后得到 \(\mathbb Z[\mathrm i]\) 矩阵；非零子式给出非零 Gaussian integer 行列式。

特别地，若 \(M=M_H\) 为该方阵阶数，且

\[
\bar b=\frac1{MH}\sum_{\rho=(j,s,\beta)}w_\beta,
\]

则缩放方向必须给出

\[
\log|\Delta_H|\ge
-M\log D_H
-\sum_{\text{columns }\alpha}\sum_i\alpha_i\log q_i
+\sum_{\text{rows }\beta}\sum_i\beta_i\log q_i.
\tag{A}
\]

不要把行缩放写成 \(q_i^{\beta_i}\)：那会反转 (A) 中最后一项的符号。

## 常数核对：\(v_0\) 与 \(w_*\) 都在分母

令 \(w_*=\min_iw_i\)，\(\Lambda=4\log2\)。原文的有用 lcm 界是

\[
\log\operatorname{lcm}(1,\ldots,n)\le\Lambda n.
\]

其给出的证明按 dyadic 区间累加：\((\ell,2\ell]\) 内每个素数幂的对数权由 \(\binom{2\ell}{\ell}\) 控制，故该区间的增量至多 \(2\ell\log2\)；累加至不小于 \(n\) 的最小二幂得到 \(4n\log2\)。这是 \(4\log2\)，不是渐近的 \(n\) 估计或未经证明的 \(\operatorname{lcm}\) 启发式。

由 \(T_i\le F_0w_i/v_0+1\) 得

\[
\frac{\log D_H}{H}
\le\Lambda\sum_i\frac{T_i}{w_i}
\le\frac{\Lambda F_0m}{v_0}+\Lambda\sum_i\frac1{w_i}.
\]

另一方面，\(0\le w_i-\log q_i<1\)，列权给出每列 \(\sum_i\alpha_i\log q_i\le H\)，行权给出 \(\sum_i\beta_i\le w_\beta/w_*<\theta H/w_*\)。代入 (A) 得到原文 Lemma 3.1 的确切形式

\[
\frac{\log|\Delta_H|}{MH}\ge-(1-\bar b)-E_{\rm ar},
\qquad
E_{\rm ar}=
\frac{\Lambda F_0m}{v_0}
+\Lambda\sum_i\frac1{w_i}
+\frac{\theta}{w_*}.
\]

PDF 中 (3.6) 与最后一行均为 \(\Lambda F_0m/v_0\)，最后一项为 \(\theta/w_*\)；文本抽取丢失分式横线时不能把它们误记为乘积。

## 精确有限复放

本机用 Python 3.13 和 SymPy 1.14.0 检查 \(m=1\)、\(K=2\)、\(H=4\)、\(w_0=v_0=1\)、\(\theta=1/2\)、\(F_0=3\)、\(p/q=3/2\)。于是 \(w=1,T=3,L=2,D_H=16\)。以下脚本检查了 \(j=0,1\) 的全部允许行，且缩放因子只出现一次。

```python
import sympy as S

H, K, theta = 4, 2, S.Rational(1, 2)
q, p, w, v0, T = 2, 3, 1, 1, 3
t = S.symbols("t")
G = sum(S.Rational((-1) ** (k + 1), k) * t ** k for k in range(1, T))
r = 2 * S.I * p / q
cols = [(h, a) for h in range(H + 1) for a in range(H + 1) if h + w * a <= H]
rows = [(j, s, b)
        for j in range(K) for b in range(H + 1) for s in range(H + 1)
        if v0 * s + w * b / theta < H]
A = S.Matrix([
    [S.expand(S.binomial(a, b) * (1 + t) ** h
              * (q * (j * r + G)) ** (a - b)).coeff(t, s)
     if a >= b else 0 for h, a in cols]
    for j, s, b in rows
])
pivots = A.rref()[1]
D_H = S.ilcm(*range(1, T)) ** (H // w)
assert D_H == 16
assert all(all(part.is_integer for part in (D_H * x).as_real_imag()) for x in A)
B = A[:, pivots]
power = sum(cols[k][1] for k in pivots) - sum(b for _, _, b in rows)
assert (len(rows), len(pivots), B.det(), power) == (12, 12, 3869835264, 13)
assert B.det() / q ** power == 472392
```

所得满行子式的缩放行列式为 \(3869835264\)，原始行列式为 \(472392\)。有限测试只检查清分母与缩放。测试中的逼近和截断参数并未满足原文的大尺度插值命题。

## 迁移边界

可迁移的是：在某个固定离散整数环中，缩放后中心必须是环元素，截断级数的系数必须有可控的统一公分母，且有独立的非零 minor。不能从本页推出的是 \(\gamma\) 的有理逼近、对数曲线的满秩插值、解析碰撞上界，或任何 \(\gamma\) 的无理性结论。对其他周期，先重新证明相应的整数环、中心缩放和非零性接口。

## 来源

OpenAI, *The irrationality exponent of pi is 2*, 2026-09-24，PDF 12--13 页，§3.1、Lemma 3.1、式 (3.1)--(3.8)。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf)
