# 等差类欧拉积的对数截断

Olivier Ramaré, *Accurate Computations of Euler Products over Primes in Arithmetic Progressions*,
*Functiones et Approximatio Commentarii Mathematici* 65(1) (2021), 33–45,
DOI 10.7169/facm/1853。本机原件为 arXiv:1911.10991v1，SHA-256
ffbb4f9dd7e664019dee3943e07cb294032d27ef4546a85336a949491a3be4db。
采用物理页 2 的 Theorem 2、Corollary 3 和物理页 4–5 的 §2 式 (9)。

## 对数符号

设 \(a\) 是模 \(q\) 的单位，\(P\ge2\)，实数 \(s>1\)。定义
\(L_P(s,\chi)=\prod_{p\ge P}(1-\chi(p)p^{-s})^{-1}\)。
对数取欧拉级数分支，向实无穷远趋于零。记 \(Y_L\) 为 §2 式 (9)
截在 \(\ell\le L\) 的和，外层权重取 \(+1/(\ell\varphi(q))\)。
展开对数后按总次数 \(h=k\ell\) 收集。令 \(g=dk\)，
\(\sum_{d\mid g}\mu(d)\) 只保留 \(g=1\)，角色正交性选出 \(p\equiv a\bmod q\)。
所以
\[
 Y_\infty=-\log\prod_{p\ge P,\ p\equiv a\bmod q}(1-p^{-s}).
\]
这一符号来自 §2 的展开。Theorem 2 和 Corollary 3 的显示式与该展开符号相反。
小素数校正按定义为
\(\log L_P=\log L+\sum_{p<P}\log(1-\chi(p)p^{-s})\)。
取 \(q=1,P=2\) 时，所有 \(\ell>1\) 的 Möbius 和为零，
\(Y_L=\log\zeta(s)>0\)，原乘积却小于 1，可直接检出符号差异。

## 独立余项

写 \(R=P^{-s}\)、\(v=(L+1)s\)。对 \(t=\ell s,\ell>L\)，
\[
 |\log L_P(t,\chi^d)|
 \le \frac{\sum_{n\ge P} n^{-t}}{1-P^{-t}}
 \le \frac{P^{-t}(1+P/(t-1))}{1-P^{-t}} .
\]
先对每个对数级数取绝对值，再保留 \(n=P\) 项并用积分控制其余项。
平方自由因子数除以 \(\ell\) 至多为 1，角色平均也至多为 1。逐层求和得
\[
 |Y_\infty-Y_L|\le E=
 \frac{(1+P/(v-1))R^{L+1}}{(1-R^{L+1})(1-R)} .
\]
若已有有理证书 \(Y_L\in[A,B]\)，则乘积的实对数属于 \([-B-E,-A+E]\)。
工具在整数 \(s\ge2\) 时精确计算该封套。求 \(A,B\) 须对有限个
Dirichlet-\(L\) 对数和角色运算分别给出定向误差界。

~~~sh
python3 scripts/ap_euler_log_tail.py --start 2 --through 4 --exponent 2 \
  --main-lower 49/100 --main-upper 1/2
~~~

例中 \(q=1\)。所给主和区间可由 \(\zeta(2)=\pi^2/6\)、
\(\pi\) 的有理上下界和对数的正项展开核对。转回乘积时可对指数函数作定向封套。
有理函数扩展须另外认证逆根与归一化。

[作者提供的刊载版](https://ramare-olivier.github.io/Maths/FA1853.pdf)
