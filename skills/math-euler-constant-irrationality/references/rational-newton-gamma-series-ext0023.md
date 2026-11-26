# Rational-term Newton series for Euler's constant

Verified formal source: Maple Transactions 5(1) (2025), Article 16090, DOI `10.5206/mt.v5i1.16090`; local PDF SHA-256 `d8ba69ea1fed0411461239e7902cf52941e3427245a3890d8ea4b9c63d5a51b3`, 10 physical pages.

Physical p.5, Theorem 2.6 derives a Newton expansion for `Gamma(x)` on real `x>=1` from an integral representation and an absolute convergence estimate. Differentiating after the allowed interchange produces Corollary 2.7:

`gamma = -1 + sum_{n>=2} (n-2)! sum_{k=1}^n (-1)^(k+1)/((n-k)! k^k)`.

Every finite summand is rational, so this is suitable for exact partial-sum experiments. The source supplies no common-denominator/height-vs-tail estimate capable of proving irrationality. Physical p.9 labels its inverse-Gamma Newton expansion Conjecture 3.1; never use it as a proved extension.

## 严格有理区间

令 \(a_n\) 为上式的第 \(n\) 项。有限二项式求导恒等式给出
\[
 a_n=\frac{1}{n-1}\int_0^\infty e^{-t}(1-te^{-t})^{n-1}\,dt>0.
\]
展开有限乘积时，\(\int_0^\infty t^{k-1}e^{-kt}dt=(k-1)!/k^k\)，所以与原式逐项相等。用非负项的单调收敛把 \(n\ge2\) 的和放入积分，得到
\(\int_0^\infty e^{-t}(t-\log t)\,dt=1+\gamma\)。

写 \(j=n-1\)。在 \(0<t\le1\)，\(te^{-t}\ge t/e\)，因此
\[
 \int_0^1e^{-t}(1-te^{-t})^j\,dt
 \le \int_0^1(1-t/e)^j\,dt < \frac{3}{j+1}.
\]
在 \(t\ge1\)，\(te^{-t}\ge e^{-t}\)。换元 \(u=e^{-t}\) 给出该段积分上界 \(1/(j+1)\)。故 \(0<a_{j+1}<4/(j(j+1))\)。给定 \(N\ge2\)，令 \(S_N=-1+\sum_{n=2}^N a_n\)，则
\[
 S_N<\gamma<S_N+4/N .
\]
这是对计算式的独立余项证明。分母高度与无理性仍按共享整数线性形式门槛处理。

~~~sh
python3 -B scripts/gamma_newton_interval.py --through 3
~~~

该例的严格区间为 \((1/27,37/27)\)，宽度 \(4/3\)。区间的用途是精确认证这条 Newton 表示的有理截断。需要窄区间时可与 Gregory 或 Brent–McMillan 例程组合。

[原刊 Corollary 2.7](https://mapletransactions.org/index.php/maple/article/download/16090/17474/58719)
