# 正矩 Hankel 行列式与整化

Zudilin，*A Determinantal Approach to Irrationality*，本机 EXT-0555 的 PDF 为 arXiv:1507.05697v2，SHA-256 `5b9ce0da2370473eff453a436dcf2901ed886e58fd9521db01e5c1818166788c`。物理页 2–3 的 Proposition 2 与式 (2)–(4) 是矩、行列式和容量步骤，物理页 4 的式 (6)–(7) 给出对数积分算例。[正式版](https://doi.org/10.1007/s00365-016-9333-7)

## 从矩到整数形式

设 \(m_k=a_k\xi+b_k=\int t^k\,d\mu(t)\)，其中 \(a_k,b_k\in\mathbb Q\)，\(\mu\) 为 \([0,\varepsilon]\) 上有限正测度，且支撑有无穷多点。给定正整数链 \(\delta_k\mid\delta_{k+1}\)，满足 \(\delta_k a_k,\delta_k b_k\in\mathbb Z\)、\(\delta_k\le C\Delta^k\)。如果原矩从下标 1 开始，用 \(t\,d\mu(t)\) 构造移位矩。定义 \(H_n=\det(m_{i+j})_{0\le i,j<n}\)。以下三步须同时成立。

1. **正性。** \(H_n\) 是单项式 \(1,t,\ldots,t^{n-1}\) 的 Gram 行列式。非零多项式的有限零点无法覆盖无穷支撑，所以 \(H_n>0\)。仅有定义域上的函数非恒定时，还需检查其推前测度的支撑。有限支撑的矩在阶数超过支撑点数后给出零行列式。
2. **整化。** 第 \(i\) 行乘 \(\delta_{n-1+i}\)，用连续整除关系统一清分母。得到 \(D_n H_n=P_n(\xi)\)，其中 \(D_n=\prod_{i=0}^{n-1}\delta_{n-1+i}\)，\(P_n\in\mathbb Z[X]\)、\(\deg P_n\le n\)。若 \(\xi=p/q\)，则 \(q^nD_nH_n\) 为正整数。
3. **容量。** Heine 公式将 \(H_n\) 写成 Vandermonde 平方的 \(n\) 重积分除以 \(n!\)。由区间 \([0,\varepsilon]\) 的 Fekete–Chebyshev 常数 \(\varepsilon/4\)，有 \(\limsup H_n^{1/n^2}\le\varepsilon/4\)。乘入上面的整化因子后，\(n^2\) 次根上界为 \(\varepsilon\Delta^{3/2}/4\)。若严格小于 1，得到正整数趋零的矛盾。固定移位只额外贡献 \(O(n)\) 的对数高度。

对正有理输入，严格容量不等式可用 \(\varepsilon^2\Delta^3<16\) 核对。有限行列式和对数直线拟合各自无法证明所需的矩表示或统一增长界。

## 对数原例与本机调用

对正整数 \(a\ge2\)，令
\[
m_k=\int_1^a\left(\frac{(x-1)(a-x)}x\right)^k\frac{dx}{x}.
\]
非恒定连续核与正密度 \(dx/x\) 给出无穷支撑。展开式 (7) 得 \(\delta_k=\operatorname{lcm}(1,\ldots,k)\)，取 \(\delta_0=1\)。由素数定理 \(\delta_k^{1/k}\to e<3\)。当 \(a=3\) 时，核的最大值 \((\sqrt3-1)^2=4-2\sqrt3<3/5\)。因此可取 \(\Delta=3\)、\(\varepsilon=3/5\) 并直接比较 \(243/25<16\)。这是该例使用的严格容量门槛，外部分析依赖仍为上述容量常数与素数定理。

运行本机 SymPy 环境：

```sh
python3 scripts/moment_hankel_denominator.py --order 2 --log-argument 3
```

[精确脚本](../scripts/moment_hankel_denominator.py)给出整化因子 \(2\) 与多项式 \(12X^2+16X-32\)，其中 \(X=\log3\)。同时核对单点矩 \(m_k=2^{-k}\) 的二阶行列式为零。有限符号计算只检查这一步整化和反例。研究 \(\gamma\) 时，构造共同的正测度矩表示及全局速率仍是首要缺口。
