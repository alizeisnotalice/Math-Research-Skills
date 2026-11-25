# Catalan 增长主块的条件化 Frobenius 化简

本页处理固定 \(48\times48\) 块的非零性传到尺度 \(N=p\) 的增长过滤行列式。这一步使用手稿 Lemma 3.1。其全指标局部整性与两组数位同余见[独立数位化简](catalan-digit-reductions.md)。

## 输入与结论

设 \(G\in\mathbb Q\)，取 \(N=p\)，其中 \(p>260\) 是不整除 \(G\) 分母的素数。令 \(B_0,B_1\) 为固定尺度 \(N=1\) 的有理 \(48\times48\) 块。以下三项共同成立时，固定块证书可传到增长矩阵。

1. Lemma 3.1 在所有 \(0\le i,j<H=65p\) 上成立，使原始列乘以 \(p^2\) 后局部 \(p\)-整。
2. \(B_0,B_0+B_1,B_0-B_1\) 都在 \(\mathbb Q\) 上非奇异。
3. \(p\) 避开固定块条目分母及三个固定行列式分子、分母构成的有限素数集。

令 \(F_p\) 为原始的已过滤 \(48p\times48p\) 矩阵。则

\[
\det(p^2F_p)=p^{2(48p)}\Delta_p
\]

是 \(p\)-进单位，因此

\[
v_p(\Delta_p)=-2(48p)=-96p.
\]

这里不能写成“\(p^2\Delta_p\) 是单位”。矩阵有 \(48p\) 阶，标量 \(p^2\) 对行列式贡献 \(p^{96p}\)。

## 归约链

以 \(r=pr_0+i\) 和过滤后的列指标 \(k=\ell+pk_0\) 编号，其中 \(0\le r_0,k_0<48\) 且 \(0\le i,\ell<p\)。在 \(\mathbb F_p\) 中，手稿的两个回文基为

\[
U_\ell(w)=(2w)^\ell(1+w^2)^{p-1-\ell},\qquad
Q_i(w)=w^i\sum_{j=0}^{p-i-1}w^{2j}.
\]

写 \(Q_i=\sum_\ell a_{\ell i}U_\ell\)，另设 \(Q'_0=0,\ Q'_i=Q_{p-i}\)（\(i>0\)）并展开 \(Q'_i=\sum_\ell b_{\ell i}U_\ell\)。低次项三角性给出

\[
a_{\ell i}=0\quad(\ell<i),\qquad a_{ii}=2^{-i},\qquad b=a\Pi,
\]

其中 \(\Pi e_0=0\)，且 \(\Pi e_i=e_{p-i}\) 对 \(i>0\)。在有理函数域内令 \(t=2w/(1+w^2)\)、\(E(t)=(1-t^2)^{(p-1)/2}\)，得到

\[
E(t)w^i=\sum_{\ell=0}^{p-1}t^\ell(a_{\ell i}+b_{\ell i}w^p)
\]

结合该式与 Frobenius 代换 \(t'=t^p,w'=w^p\)，得到原始行的两个提取恒等式。再以 Lemma 3.1 的 \(p^2M_0\) 与 \(p^2Z_0\) 数位化简替换混合矩，缩放矩阵的 \((i,\ell)\) 块为

\[
a_{\ell i}B_0+b_{\ell i}B_1.
\]

在 \(\mathbb F_p[s]\) 中，过滤恒等式

\[
s^{7p+k}(1-s)^{4p}=s^\ell(s^p)^{7+k_0}(1-s^p)^4
\]

使四阶差分保留剩余类。缩放约化矩阵于是是

\[
L_p=a^\mathsf T\otimes B_0+b^\mathsf T\otimes B_1.
\]

乘以 \((a^\mathsf T)^{-1}\otimes I\) 后，

\[
L_p((a^\mathsf T)^{-1}\otimes I)
=I_p\otimes B_0+\Pi^\mathsf T\otimes B_1.
\]

\(\Pi\) 的特征值 \(0,1,-1\) 的重数为 \(1,(p-1)/2,(p-1)/2\)。因此

\[
\det L_p=(\det a)^{48}\det B_0
\det(B_0+B_1)^{(p-1)/2}
\det(B_0-B_1)^{(p-1)/2}.
\]

这个步骤只把三个固定矩阵的非零行列式带到避开有限坏素数的 \(p\)。它不说明其他 \(N\) 的非零性，也不替代有限位或实位界。

## 本机复放与核验边界

本机运行 `scripts/check_fixed_blocks.py`，在 \(\mathbb F_{101}\) 重建 \(B_0,B_1\)，得到

\[
\det B_0=27,\qquad
\det(B_0+B_1)=50,\qquad
\det(B_0-B_1)=74\pmod {101}.
\]

另以 SymPy 1.14.0 对 \(p=3,5,7,11\) 逐一核对两个回文基的三角展开、\(E(t)w^i\) 恒等式、Kronecker 行列式分解，以及所有剩余类的过滤恒等式。这些是有限代数复放，不能验证任意素数上的数位化简。

原文 PDF 11–13 页 Lemma 3.1 提供全部 \(i,j\) 的 \(p^2M_0(i,j)\)、\(p^2Z_0(i,j)\) 同余、\(i'=-1\) 边界及局部整性。调用本页时使用数位化简所述的素数和索引范围。

## 欧拉常数的迁移条件

该链条依赖 \(f(t)=\sqrt{1-t^2}\)、\(G/\zeta(2)\) 矩分解、Chebyshev 行及相应的消去。它没有给出欧拉常数 \(\gamma\) 的矩阵、伴随常数消去、\(p\)-进数位化简或实位比较。对 \(\gamma\) 只能把它视为设计检查表，不能由此推出有理线性形式或无理性结论。

## 来源

OpenAI, *Catalan’s constant is irrational*, 2026-09-24，固定本机 SHA-256 4023d0344abceb79dc46a16380dac3a662193f9d4f23e6c340b2162068b04c0e，PDF 20--25 页，式 (51)--(60) 与 Proposition 4.1。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf)
