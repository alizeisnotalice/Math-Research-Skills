# 混合 \(\gamma+\log\) 逼近与高度审计

本页只记录三份已逐页核对的来源能安全支撑的内容。它的目的不是把
“收敛得快”误写为 \(\gamma\) 无理性的证据：每次使用前都要分别核对
目标常数、分母/整系数、余项是否非零、以及清分母后的形式是否趋于零。

## 来源、版本与本地指纹

| 标记 | 已核对的版本与状态 | 本地文件（页） | SHA-256 |
|---|---|---|---|
| G08 | Carsten Elsner, *On Rational Approximations to Euler’s Constant \(\gamma\) and to \(\gamma+\log(a/b)\)*, **International Journal of Mathematics and Mathematical Sciences** (2009), Article ID 626489, 22 pp., DOI [10.1155/2009/626489](https://doi.org/10.1155/2009/626489)。本地件首页给出期刊卷、Article ID、收稿/录用日期和 DOI，按正式开放获取期刊版本使用。 | `08_OpenAI_Anthropic_Gamma_PiE/PDF/G08-supp.pdf`（PDF pp. 1–22） | `c76817e3c589125a192bf291806fc55631a826eb2a972161defb3db59b12e679` |
| G26 | José A. Adell and Alberto Lekuona, *Rational approximation to Euler’s constant at a geometric rate of convergence*, **Mathematics of Computation** 89(325) (2020), 2553–2561, DOI [10.1090/MCOM/3528](https://doi.org/10.1090/MCOM/3528)。本地件首页仍是 `Volume 00`/`XXXX` 的排版稿；它与正式题名、作者相符，但本审计**不把该 PDF 称为最终出版 PDF**。 | `08_OpenAI_Anthropic_Gamma_PiE/PDF/G26-supp.pdf`（PDF pp. 1–8） | `02e459a234ae8fbd961e4240142cc70886803e7d40f064e9fade148f81656d25` |
| P16 | A. I. Aptekarev, *On linear forms containing the Euler constant*, [arXiv:0902.1768v2](https://arxiv.org/abs/0902.1768), 28 Feb. 2009, 6 pp. 本地件首页和 arXiv 条目均为 v2；这里仅作为预印本引用，未假定存在或已核到同行评议发表版。 | `04_Attachment_References/PDF/P01-P21/P16_On_linear_forms_containing_the_Euler_constant.pdf`（PDF pp. 1–6） | `84f09b5f2122f9fe01ce1fd9e75fe6c7bdbcbb322c8b24912b485fc45ddffa16` |

“页”均指 PDF 的物理页。G26 的正式书目信息采用 [期刊 DOI](https://doi.org/10.1090/MCOM/3528)；P16 的作者、题名、日期和 v2 状态以 arXiv 条目交叉核对。

## G08：两个不同层次的混合对象

### 1. 真正趋零的整数**多对数**形式，但不是 \(\gamma\) 的单变量形式

设 \(B_m=\operatorname{lcm}(1,\ldots,4m)\)，并令

\[
A_m=B_m\sum_{k=0}^{2m}(-1)^k
 {3m+k-1\choose2m}{2m\choose k}H_{k+2m-1}\in\mathbb Z .
\]

G08 的 Corollary 1.8（PDF p. 4）给出（对充分大的 \(m\)）

\[
 \left|\gamma B_m-A_m+
 B_m\sum_{k=0}^{2m}(-1)^k{3m+k-1\choose2m}{2m\choose k}
       \log(k+2m)\right|
 <\left(\frac{16}{7\pi}\right)^2\!\left(\frac{55}{64}\right)^m. \tag{G08.1}
\]

这确实是系数为整数、右端趋于零的混合线性形式；但其对数目标随
\(m\) 改变。把对数按素数重新收集也只会得到一列不断变化的
\(\log p\)。来源没有给出该形式的非零性，且 (G08.1) 既不隔离
\(\gamma\)，也不产生只含固定 \(\gamma,\log q\) 的整数形式。因此不能由它推出
\(\gamma\) 无理，更不能把“误差趋零”改写成这种结论。

### 2. 对固定 \(\gamma+\log(a/b)\) 的有理逼近，不等于可用整数形式

给定正整数 \(a,b\)，定义（G08 (6.24)，PDF p. 20）

\[
 T_n=H_{an-1}-H_{bn-1}+2H_{n-1}-H_{n^2-1},\qquad
 C_{d,m}(T)=\sum_{k=0}^{dm}(-1)^k
 { (2d-1)m+k-1\choose dm}{dm\choose k}T_{dm+k}.
\]

Theorem 6.2（PDF p. 20）断言，对 \(d\ge42\)，存在只依赖
\(a,b,d\) 的 \(c_5>0\)，使

\[
 \left|C_{d,m}(T)-\gamma-\log\frac ab\right|
 <\frac{c_5}{\sqrt m}\left(\frac{18}{4^{d+1}}\right)^m. \tag{G08.2}
\]

这给出的是有理数 \(C_{d,m}(T)\) 对固定目标的指数收敛。若
\(a=b\)，目标才退化为 \(\gamma\)；若 \(a\ne b\)，单独的一列逼近不可能
“消去” \(\log(a/b)\)。特别地，\(\gamma\) 有理并不与
\(\gamma+\log(a/b)\) 的这种逼近矛盾。

高度关口也必须保留。G08 对含 Bernoulli 校正的 \(S_n\) 变换证明其既约分母
\(b_m\mid Z_m\)，其中（Theorem 4.1、(4.14)–(4.15)，PDF pp. 11–13）

\[
 Z_m=2(ab)^{2dm}D_{dm}D_{4d^2m^2}(D_{2dm})^{4dm}
       \prod_{p\le2dm+1}p,
 \qquad \log Z_m\sim12d^2m^2 . \tag{G08.3}
\]

对简化的 \(T_n\) 变换，作者只在 PDF p. 22 说明有同型的
\(\log b_m\ll d^2m^2\) 分母估计。故已写出的资料只给出
\(\lvert\text{误差}\rvert=e^{-\Theta_d(m)}\)，而清分母的安全上界是
\(e^{O_d(m^2)}\)：它**没有**给出
\(b_m(C_{d,m}(T)-\gamma-\log(a/b))\to0\)。也不能把 (G08.3) 乘进
(G08.2) 后称为趋零整数形式。实际既约分母若有额外消去，须逐项证明，不能由
上界臆测。

## G26：几何速度的计算公式，作者明确排除无理性用途

令 \(\lambda>0\)，并取最小 \(m(\lambda)\ge\lambda\) 满足
\(\lambda^{m+1}/(m+1)!\le e^{-\lambda}\)。Corollary 3.2（PDF p. 6）为

\[
 \left|\gamma+\sum_{k=1}^{m(\lambda)}\frac{(-\lambda)^k}{k!k}
                  +\log\lambda\right|
 \le\frac{2e^{-\lambda}}\lambda . \tag{G26.1}
\]

当 \(\lambda=2^N\) 时，\(\log\lambda=N\log2\)，且
\(\log2=2\sum_{j\ge0}[(2j+1)3^{2j+1}]^{-1}\)。于是 Corollary 3.4
（PDF p. 7）得到明确的有理数

\[
 R_N=-\sum_{k=1}^{m(2^N)}\frac{(-2^N)^k}{k!k}
 -2N\sum_{j=0}^{2^{N-1}}\frac1{(2j+1)3^{2j+1}},
 \qquad
 |\gamma-R_N|\le\frac{3e^{-2^N}}{2^N}. \tag{G26.2}
\]

这已把唯一的对数换成有理截断，因而 \(R_N\in\mathbb Q\)。但这是“有理逼近”而非
已构成 \(A_N+B_N\gamma\to0\) 的结论。一个保守的共同分母为

\[
 D_N=(m(2^N)!)^2\,3^{2^N+1}(2^N+1)!,
\]

因为 \(k!k\mid(m!)^2\)（\(k\le m\)），而第二个有限和的分母整除
\(3^{2^N+1}(2^N+1)!\)。结合文中 \(m(\lambda)\le3.6\lambda\) 的估计，
\(\log D_N=O(2^N N)\)，而 (G26.2) 的误差**上界**是 \(3e^{-2^N}/2^N\)。该安全分母不能使清分母余项趋零；
本地稿 PDF p. 2 也明确说速度不足以证明 \(\gamma\) 无理性。

实际复核（Python `fractions.Fraction` 精确构造，再以 80 位 `mpmath` 比较）：
\(N=4,\lambda=16,m(16)=55\) 时，\(R_4\) 的分子/分母各为 79/80 位十进制数，

\[
 R_4=0.577215672475146224639745257609801892\ldots,
\quad |\gamma-R_4|=7.57361336403323317\times10^{-9}
 <2.1100345259861084\times10^{-8}.
\]

这是有限实例的数值交叉检查，不是对任意 \(N\) 的额外证明。

## P16：双常数行列式及渐近系数的待核问题

令 \(\delta=\int_0^\infty e^{-x}/(1+x)\,dx\)。按原文 PDF p. 3 的递推 (8) 构造三组有理序列 \(p,q,r\)，并用印出的归一化
\[
 f_n=p_n-\gamma q_n,\qquad
 g_n=e f_n-\delta q_n+r_n .
\]
记 \(\Delta(a,b)_n=a_{n+1}b_n-a_nb_{n+1}\)，由 p. 4 的 (10)–(11) 取
\[
 (u_n,v_n,w_n)=\big(\Delta(q,p)_n,\Delta(q,r)_n,\Delta(p,r)_n\big)/(n!)^2 .
\]
双线性立即给出
\[
 \ell_n=\delta u_n-\gamma v_n+w_n
      =\frac{\Delta(f,g)_n}{(n!)^2}.
\]
这一等式使用 (9) 的 \(g_n\)。若把 \(g\) 重新除以 \(e\)，右端必须同时乘回 \(e\)。原文 `4 D 的若干恒等式写成了重缩放后的形式，应先统一归一化。

### 印出公式的交叉核对

原文 (9) 写出
\[
 f_n\sim\frac{2\sqrt\pi}{(4e)^{3/8}}(2n)!e^{-\sqrt{2n}}n^{-1/4},
 \qquad 16^n g_n\longrightarrow \frac18 .
\]
若这两式同时成立，则 \(f_n/f_{n+1}=O(n^{-2})\)，\(g_{n+1}/g_n\to 1/16\)，所以 \(\Delta(f,g)_n\sim f_{n+1}g_n\)。用 \(\binom{2n}{n}\sim4^n/\sqrt{\pi n}\) 代入，得
\[
 \lim_{n\to\infty}\frac{e^{\sqrt{2n}}4^n\ell_n}{n^{5/4}}
 =\frac4{\sqrt\pi}\frac{2\sqrt\pi}{(4e)^{3/8}}\frac18
 =(4e)^{-3/8}.
\]
式 (3) 写出的首项常数则为 \(4(4e)^{-3/8}\)。两处印出常数不相容。实际以 320 位 mpmath 复算，\(n=40\) 时 \(16^ng_n\) 约为 \(-0.040832218149634\)，规范化的 \(\ell_n\) 约为 \(-0.10913557212828\)。这些有限值用于查找误差来源，真实渐近仍需另证。

### 原始差分方程给出的小解尺度

将 (8) 的任一解写为 \(y_n=n!z_n\)。逐项约去 \(n!\)，得到 Tulyakov 正式论文的式 (3)。该文式 (4) 给出三个渐近基解。两个大分支为 \((4n/e)^n n^{-1/4}e^{\pm\sqrt{2n}}\) 乘以趋 1 的因子。剩下一个基解的首项为
\[
 z_{3,n}\sim\left(\frac{e}{16n}\right)^n n^{-3/2},
 \qquad
 n!z_{3,n}\sim\sqrt{2\pi}\,\frac{16^{-n}}n .
\]
因此 P16 (9) 的 \(g=O(16^{-n})\) 若成立，两个大分支的系数都必须为零。在唯一小分支上 \(16^ng_n\to0\)，与同一行给出的 \(1/8\) 矛盾。若后续独立证明实际的 \(g\) 为非零小分支，行列式里的幂应为 \(n^{1/4}\)，需另行识别首项常数。该分支识别不能由上述有限数值代替。[Tulyakov 正式版，原文 p. 46，式 (3)–(4)](https://doi.org/10.4213/spm16)

本机用精确递推生成到 \(n=320\)，再分别以 2,600 和 2,700 位 mpmath 计算残差。以下数字在两次计算中一致，作为有限诊断保留。

| \(n\) | \(n16^ng_n\) | \(\ell_n e^{\sqrt{2n}}4^n/n^{1/4}\) |
| ---: | ---: | ---: |
| 80 | \(-1.64786980904559584\) | \(-4.64830863952627024\) |
| 200 | \(-1.65673193179846883\) | \(-4.92022177281248063\) |
| 319 | \(-1.65894925549969616\) | \(-5.02254129701113526\) |

### 采用范围

有限构造可直接使用。运行 [精确回放](../scripts/check_aptekarev_mixed_forms.py)，检查 \(0\le n\le40\) 的 123 个规范化整数行列式与递推 (2) 完全一致。选用已安装 `mpmath` 的 Python 并加 `--numeric` 可重放上述有限高精度比较。默认精确检查只用 Python 标准库。

原文对 \(p,q,r\) 的整性调用 [13]，对行列式整化调用 [14]，对 (9) 调用 [11] 与 [12]。从原文引用追踪时保留相应的序列、第三解初值与 \((n!)^2\) 归一化。本页仅采用恒等式与精确有限复算，将 P16 的全指标估值和渐近结论保留为待核材料。[Tulyakov 正式版](https://doi.org/10.4213/mzm5260) [Aptekarev–Lysov 的 \(f_n\) 渐近](https://doi.org/10.1134/S0081543811030126) [Aptekarev–Tulyakov 格行列式](https://doi.org/10.1090/S0077-1554-09-00175-7)

若需要 \((\gamma,\delta)\) 的联合作用，独立引用 Rivoal 的正式版 Theorems 1–2 在 \(z=1\) 的结论，保留其联合量词。P16 的行列式本身含 \(\delta\)。[Rivoal，Michigan Mathematical Journal 61 (2012), 239–254](https://doi.org/10.1307/mmj/1339011525)

## 使用门槛

1. 需要 \(\gamma\) 单独结论时，先把最终对象写成 \(A_n+B_n\gamma\)，并分别证明
   \(A_n,B_n\in\mathbb Z\)、非零和趋零；不得以 G08 的混合对数或 P16 的 \(\delta\) 形式替代。
2. 需要由有理逼近导出无理性时，必须给出实际既约分母 \(b_n\) 的控制并验证
   \(b_n\,|x-a_n/b_n|\to0\)（或等价的严格整数形式）；仅有共同分母上界不足。
3. 使用 G08 的 \(a\ne b\) 时，把 \(\log(a/b)\) 当作保留的独立目标；只有另有同尺度的、经整性核对的消元构造，才讨论消去它。
4. 本页可安全依赖的是：G08 的 (G08.1)–(G08.3)、G26 的 (G26.1)–(G26.2)，以及 P16 的精确有限行列式构造。任何进一步的单常数结论均需新的证明或经核验的外部定理。
