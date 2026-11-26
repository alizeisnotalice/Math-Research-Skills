# Elsner 的整系数调和数与对数变换

Carsten Elsner，*On a Sequence Transformation with Integral Coefficients for Euler’s Constant, II*，J. Number Theory 124 (2007), 442–453。原件 EXT-0534 的 SHA-256 为 `6de9db636e0e3e13536eba8c5c080b2aba11e69ee69e629535a9899af80f82be`。物理页 3–4 为 Theorems 4–5 和 Corollary 4，页 8–12 为式 (12)–(15) 与正核积分、上界的推导。 [期刊版](https://doi.org/10.1016/j.jnt.2006.10.002)

## 整系数变换

设 \(d\ge2\)、\(m\ge2\)，记 \(n=\tau_2=dm\)、\(\tau_1=(d-1)m-1\)。使用 \(s_j=H_{j-1}-\log j\)。取
\[
c_k=(-1)^{n+k}\binom{n+\tau_1+k}{n}\binom nk,\qquad
T=\sum_{k=0}^n c_k s_{n+k}.
\]
\(\sum_k c_k=1\)，可按对 \(k\) 的 \(n\) 阶有限差分理解。实际计算先取得精确有理分量和对数的整系数，再以向外有理区间处理对数的符号抵消。

Theorem 5 的使用范围是 \(1\le\tau_1\)、\(1+\tau_1\le\tau_2\le1+n+\tau_1\)。式 (12) 的分部积分边界因 \(u^{n+\tau_1}(1-u)^n\) 在两端至少有 \(n\) 阶零点而消失。式 (13) 中有理分解的多项式部分次数小于 \(n\)，残留的正核给出 \(T-\gamma\) 非零，符号为 \((-1)^{n+\tau_2-\tau_1}=(-1)^{(d-1)m+1}\)。\(d=2,m=1\) 仅调用 Corollary 4 单列的双边误差界。

## 可复核误差区间

Corollary 4 的界以 \(3<\pi\) 作保守整化：
\[
|T-\gamma|<
\begin{cases}
(16/21)^2\,64^{-m}, & d=2,\\[2pt]
\dfrac1{144}\left(\dfrac{(1-1/d)^d}{(d-1)4^d}\right)^{m-2}, & d\ge3.
\end{cases}
\]
对 \(d\ge3\) 的几何因子取式 (15) 的 \(f_1\) 最大值，见物理页 11。程序复用 Sondow 的有理对数区间。已知误差符号时仅在对应一端加余项。输出的小数端点向外取整。

~~~sh
python3 scripts/elsner_transform_interval.py --m 2
python3 scripts/elsner_transform_interval.py --d 3 --m 5 --exact-fractions
~~~

有限点可以与 [Brent–McMillan 区间](brent-mcmillan-enclosure.md) 作严格对照。这个构造仍包含对数线性组合，若要生成只含 \(1,\gamma\) 的整数形式，需另行证明消去和整化代价。
