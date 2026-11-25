# Gamma--Laguerre、正矩 Padé 与 Legendre 修正矩：可复用的局部模块

本页只蒸馏三个本机全文中已逐式核验的模块。它们都与 Euler 常数有关，
但**不是同一个逼近构造**：不要把任一构造的余项、分母或正性迁移到另一个
构造。

| 模块 | 可以安全复用的对象 | 不能据此声称 |
| --- | --- | --- |
| Rivoal--Gamma | 多 Laguerre 正交性、Gamma 矩恒等式、无穷远的 II 型 Padé 展开 | 在固定点（特别是 \(z=1\)）有本页所未给出的显式尾项常数 |
| Prévost--Rivoal | Bernoulli 系数的正矩表示、近对角 Padé 的精确误差和显式上界 | 得到了适合无理性判别的有理 \(\gamma\) 逼近（式中仍有 \(\log n\)） |
| Prévost--Legendre | Legendre 修正矩、\([n/n]\) 对数 Padé 替换及 \(O(4^{-n})\) | 任意 \(m,n\) 下都是有理逼近；有理化须额外的 \(n-m+1=2^p\) 条件 |

## 来源、版本与依赖边界

所有页码均为下列**本机 PDF 的物理页码**，不是期刊的连续页码。SHA-256
用于防止将以后下载的同名版本混入本页。

| 标签 | 本机定位与 SHA-256 | 已核对的版本/引用 | 本页实际依赖 |
| --- | --- | --- | --- |
| G03-01 | `08_OpenAI_Anthropic_Gamma_PiE/PDF/G03-01_Rational_approximations_for_values_of_derivatives_of_the_Gamma_function.pdf`；`4244ef49d4eccbb0ec9d91338b6e904ae7bd602e60909617102f9b846301acf3` | T. Rivoal, *Rational approximations for values of derivatives of the Gamma function*, **Trans. Amer. Math. Soc.** 361 (2009), 6115--6149, DOI [10.1090/S0002-9947-09-04905-8](https://doi.org/10.1090/S0002-9947-09-04905-8). 作者的[论文目录](https://rivoal.perso.math.cnrs.fr/articles.html)列为已发表。当前本机件是日期为 2009-01-13 的 37 页作者稿；下列只依赖其物理页 6--11 的命题，不以排版差异推断期刊逐页一致。 | 不导入 Aptekarev 多项式或任何外部递推；只使用本 PDF 自己给出的定义、Propositions 1、3、4。 |
| EXT-0535 | `07_Irrationality_Transcendence_Compendium/PDF/EXT-0535_Application_of_Pade_Approximation_to_Eulers_constant_and_Stirlings_formula.pdf`；`947724ac14cd2e703f46d5d920a26458c799a4685d191c91a1a58850d847ff93` | M. Prévost, T. Rivoal, *Application of Padé approximation to Euler's constant and Stirling's formula*, **Ramanujan J.** 54(1) (2021), 177--195, DOI [10.1007/s11139-019-00201-9](https://doi.org/10.1007/s11139-019-00201-9); 作者目录亦列出该卷页。本机件首页明示 `hal-02017852v3`、2019-08-09；它是本页公式的权威文本，已发表版本只用于核对书目信息。 | 不需要外取 Touchard 多项式文献：正矩、Padé 余项和用于上界的 \(T_k\) 范数均由本 PDF 物理页 6--12 陈述。 |
| P11c | `04_Attachment_References/PDF/P01-P21/P11c_Legendre_modified_moments_for_Euler_s_constant.pdf`；`daf112a9a9a8f9e6f25e9e9cb04fce8f2356c10644654b90ce411ca8c864af56` | M. Prévost, *Legendre modified moments for Euler's constant*, **J. Comput. Appl. Math.** 219(2) (2008), 484--492, DOI [10.1016/j.cam.2007.09.015](https://doi.org/10.1016/j.cam.2007.09.015). 本机件为 2007-06-25 的 15 页预印本；出版元记录核对题名、卷期页码与 DOI，公式本身逐式取自本机物理页 2--12。 | 不把其引用的 Stieltjes 反演或 \(\varepsilon\)-算法文献当作隐含依赖；本页只用预印本明示的积分表示、正密度和 Padé 误差式。 |

## A. Rivoal：多 Laguerre 矩与 II 型 Padé 输入

令 \(n\geq0\)、\(s\geq1\)，并递归定义

\[
A_{0,n}(t)=1,\qquad
A_{r+1,n}(t)=\frac{e^t}{n!}\left(t^n e^{-t}A_{r,n}(t)\right)^{(n)}.
\]

这是 G03-01 物理页 10 的定义。故 \(A_{s,n}\in\mathbb Q[t]\)，次数为
\(sn\)；由定义即有保守而可机械审计的分母界
\(n!^sA_{s,n}\in\mathbb Z[t]\)（未声称它最小）。

### 正交性、矩和对数矩

对 \(0\leq k<n\)、\(1\leq j\leq s\)，有（G03-01，物理页 10，Proposition 3）

\[
 \int_0^\infty t^k A_{s,n}(t)(\log t)^{j-1}e^{-t}\,dt=0. \tag{A1}
\]

对实数 \(v>0\)，反复分部积分给出（同页至物理页 11，Proposition 4 的证明）

\[
 \int_0^\infty t^{v-1}A_{s,n}(t)e^{-t}\,dt
 =\frac{(v-n)_n^{\,s}}{(n!)^s}\Gamma(v),\qquad
 (a)_n=a(a+1)\cdots(a+n-1). \tag{A2}
\]

特别地，若 \(v\in\mathbb Z_{>0}\)，右端为
\(\Gamma(v)\binom{v-1}{n}^{s}\)，其中 \(v\le n\) 时按该式为零；这是一个
避免浮点积分的精确有限测试入口。对于 Gamma 导数，G03-01 物理页 8
Proposition 1 给出

\[
 \int_0^\infty t^a(\log t)^b e^{-t}\,dt
 =\Gamma^{(b)}(a+1)
 =a!\sum_{r=0}^b\binom br H_a^{[b-r]}\Gamma^{(r)}(1), \tag{A3}
\]

其中 \(H_a^{[0]}=1\)，\(H_a^{[q]}=q!\sum_{1\le i_1<\cdots<i_q\le a}
(i_1\cdots i_q)^{-1}\)。论文证明 \(a!\binom brH_a^{[b-r]}\) 为整数。
因此 (A3) 是产生线性形式的公式；它本身不是 \(\gamma\) 无理性的证明。

### II 型 Padé 余项的适用域

取主支对数，并令

\[
 E_j(z)=\int_0^\infty\frac{(\log t)^{j-1}e^{-t}}{z-t}\,dt,
 \quad z\in\mathbb C\setminus[0,\infty),
\]
\[
 B_{j,s,n}(z)=\int_0^\infty
 \frac{A_{s,n}(t)-A_{s,n}(z)}{z-t}(\log t)^{j-1}e^{-t}\,dt,
 \quad R_{j,s,n}=A_{s,n}E_j+B_{j,s,n}.
\]

则（G03-01，物理页 10--11）\(R_{j,s,n}(z)=O(z^{-n-1})\)，但这是在
不含正实轴的无穷远角域中的 Poincaré 展开；不可替换成固定 \(z\) 的误差界。
更精确地，其形式级数为

\[
 R_{j,s,n}(z)\sim\sum_{k\ge1}\frac1{z^k}
 \left.\frac{\partial^{j-1}}{\partial\alpha^{j-1}}
 \left(\frac{(k+\alpha-n)_n^{\,s}}{(n!)^s}\Gamma(k+\alpha)\right)\right|_{\alpha=0}.
 \tag{A4}
\]

对于算术账本，原文只保证存在 \(\widetilde B_{r,s,n}\in\mathbb Q[z]\)，使

\[
B_{j,s,n}(z)=\sum_{r=1}^j\binom{j-1}{r-1}
 \Gamma^{(j-r)}(1)\widetilde B_{r,s,n}(z). \tag{A5}
\]

不要在未实际清分母前，把 (A5) 的 \(\mathbb Q[z]\) 系数误写成整数。

## B. Prévost--Rivoal：Bernoulli 正矩与近对角 Padé

设

\[
 \Phi(z)=\sum_{r\ge0}\frac{(-1)^rB_{2r+2}}{2r+2}z^r,
 \qquad
 \alpha(u)=\frac{\mathbf1_{[0,\infty)}(u)}{e^{2\pi\sqrt u}-1}.
\]

本机 EXT-0535 物理页 6，Proposition 1 给出正矩恒等式

\[
 \frac{(-1)^rB_{2r+2}}{2r+2}=\int_0^\infty u^r\alpha(u)\,du \quad(r\ge0). \tag{B1}
\]

这说明 \(\Phi\) 是 \(\int\alpha(u)/(1-zu)\,du\) 在 0 的形式矩展开；
它不是一个在正实轴上任意延拓的收敛幂级数。

令 \(q_k\) 是关于 \(\alpha\) 的首一正交多项式，\(Q_k(z)=z^kq_k(1/z)\)。
则 \([k-1/k]\Phi=P_k/Q_k\in\mathbb Q(z)\)，\(Q_k(0)\ne0\)，并且若
\(1/z\notin[0,\infty)\)，有精确余项（EXT-0535 物理页 8--9，Proposition 3）

\[
 \Phi(z)-[k-1/k]\Phi(z)
 =\frac{z^{2k}}{Q_k(z)^2}
 \int_0^\infty\frac{q_k(u)^2}{1-zu}\alpha(u)\,du. \tag{B2}
\]

这是分布（正权 \(\alpha\)）、Padé 分母和余项之间的完整接口。论文没有给
一般 \(q_k\) 的简单显式系数，故不要虚构封闭整系数分母；安全的分母声明仅为
标准化后的 \(P_k,Q_k\in\mathbb Q[z]\)。

对实 \(t<0\)，用 \(\alpha\le\delta\) 及 Touchard 型比较多项式，原文给出

\[
 \left|\Phi(t)-[k-1/k]\Phi(t)\right|
 \le |t|^{2k}\frac{(2k+1)(2k+2)}{4k+3}
 \frac{(2k)!^2}{\binom{4k+2}{2k+1}^{\!2}}. \tag{B3}
\]

因此对 \(x>0\)、\(n\ge0\)、\(k\ge1\)，\(x_n=x+n\)，有

\[
 \Psi(x)=\log x_n-\sum_{j=0}^{n-1}\frac1{x+j}
 -\frac1{2x_n}-\frac1{x_n^2}[k-1/k]\Phi(-x_n^{-2})+\varepsilon_k(x_n), \tag{B4}
\]

且 \(|\varepsilon_k(x_n)|\) 等于 (B3) 右端再乘 \(x_n^{-2}\)。这是有
显式常数的尾项界，条件正是 \(x>0,k\ge1,n\ge0\)，不可外推到 \(t\ge0\)。
取 \(x=1\)、\(k=rn\)、\(0<r<2e\) 且 \(rn\in\mathbb Z\) 只产生含
\(\log n\) 的快速逼近，不能直接称为有理 \(\gamma\) 逼近（EXT-0535
物理页 3--4）。

## C. Prévost：Legendre 修正矩和有理化条件

令 \(0\le m\le n\)，并使用移位 Legendre 多项式

\[
 P_n^*(u)=\sum_{k=0}^n\binom nk^2u^{n-k}(u-1)^k
 =\sum_{k=0}^n(-1)^{n+k}\binom nk\binom{n+k}{k}u^k. \tag{C1}
\]

所以 \(P_n^*\in\mathbb Z[u]\)，\(P_n^*(1)=1\)，且它对次数小于 \(n\)
的多项式在 \([0,1]\) 正交。令

\[
 w(u)=\frac1{\log u}+\frac1{1-u},\qquad
 J_{n,m}=\int_0^1u^{n-m}P_n^*(u)w(u)\,du,
\]
\[
 L_{n,m}=\sum_{k=0}^n(-1)^{n+k}\binom nk\binom{n+k}{k}
 \log(n-m+k+1),\quad A_{n,m}=2H_n.
\]

则（P11c 物理页 3--5，Theorem 1）

\[
 \gamma=A_{n,m}-L_{n,m}+J_{n,m}. \tag{C2}
\]

这里 \(A_{n,m}\) 与 \(m\) 无关；若 \(d_n=\operatorname{lcm}(1,\ldots,n)\)，
则 \(d_nA_{n,m}\in\mathbb Z\)。反之 \(L_{n,m}\) 是整系数对数线性形式，
通常并非有理数，故 (C2) 还不是有理逼近。

### 误差的正测度表示

原文先将 \(w\) 写为 Markov--Stieltjes 变换（P11c 物理页 6）

\[
w(u)=\int_0^1\frac{\mu(t)}{1-ut}\,dt,
\quad
\mu(t)=\frac1{t\bigl(\log^2(1/t-1)+\pi^2\bigr)}\ge0. \tag{C3}
\]

其后得到（物理页 7，Theorem 4）

\[
 (-1)^mJ_{n,m}=\int_0^{1/4}v^n\rho_m(v)\,dv=O(4^{-n}), \tag{C4}
\]

其中，令 \(\phi_\pm(v)=(1\pm\sqrt{1-4v})/2\)，该页的显式密度为

\[
\rho_m(v)=\int_{\phi_-(v)}^{\phi_+(v)}
 \left(\frac{u-u^2-v}{uv}\right)^m
 \frac{du}{(u-u^2-v)\left[\pi^2+
 \log^2\!\left(\frac{-uv}{u^2-u+v}\right)\right]}\ge0. \tag{C5}
\]

对实际调用，(C4) 给出的是符号、完全单调性和支撑 \([0,1/4]\)；常数依赖
固定的 \(m\)。不要把它误报为对随 \(n\) 增长的 \(m\) 一致。该论文还记录
\(\varepsilon\)-算法加速后的阶 \(O((7-\sqrt{48})^n)\)，但这不是本技能的有理清分母模块。

### 使对数项变成有理数的专门 Padé 步骤

对 \(\log(1+t)\) 在 \(0\) 的 \([n/n]\) Padé 近似，原文的精确积分余项为

\[
 \log(1+x)-[n/n]_x
 =(-1)^nx^{n+1}P_n^*(-1/x)
 \int_0^1\frac{t^n(1-t)^n}{(1+xt)^{n+1}}\,dt. \tag{C6}
\]

若额外满足 \(n-m+1=2^p\)（\(p\in\mathbb Z_{\ge0}\)），以原文物理页 9--10
的式 (38)--(39) 定义 \(\widetilde L_{n,m}\)：把
\(\log(n-m+1)=p\log2\) 及其余 \(\log(1+k/(n-m+1))\) 全部换为相应的
\([n/n]\) 值。则 \(\widetilde L_{n,m}\in\mathbb Q\)，且（物理页 10--12，
Theorem 5）

\[
 \gamma=A_{n,m}-\widetilde L_{n,m}+O(4^{-n}). \tag{C7}
\]

该 \(O\) 是固定 \(m\) 的结论；若要作无理性判别，仍须实际追踪
\(\widetilde L_{n,m}\) 的最小分母，而不能只使用 \(d_nA_{n,m}\in\mathbb Z\)。

## 已执行的有限精确复核（不是渐近证明）

在本机以 SymPy 运行以下有限例：Rivoal \((s,n)=(2,2)\)，Legendre
\((n,m)=(3,1)\)，以及 \(\Phi\) 的 \([1/2]\) Padé。实际输出为：

```text
A_2,2 = t**4/4 - 3*t**3 + 19*t**2/2 - 8*t + 1
orthogonality j=0: 0
orthogonality j=1: 0
Rivoal moment v=1: lhs=0, rhs=0, ok=True
Rivoal moment v=3: lhs=2, rhs=2, ok=True
Rivoal moment v=5: lhs=864, rhs=864, ok=True
P*_3 = 20*u**3 - 30*u**2 + 12*u - 1
Legendre A= 11/3  2H_3= 11/3  ok=True
Legendre L= -30*log(5) - log(3) + 24*log(2) + 20*log(6)
Phi_[1/2]= -7*(871*z - 790)/(20*(241*z**2 - 3990*z + 3318))
Padé coefficients z^0..z^3: [0, 0, 0, 0]
next residual z^4= 52489/18394992
```

这只验证了 (A1)--(A2)、\(A_{n,m}=2H_n\) 及 \([1/2]\) 的消去阶；没有数值地
验证 (B3)、(C4)、(C6) 的一般常数或任何无理性结论。
