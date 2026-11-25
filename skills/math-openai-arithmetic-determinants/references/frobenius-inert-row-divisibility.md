# Frobenius 惰性行整除

本构件把一个双二次整数环上的 Frobenius 同余转成评价行列式的素数估值。它只处理下列完整输入，不能单独给出素数分布、零点排除或无理性结论。

## 输入与行选择

令 \(d\) 为平方自由整数，\(d\ne1,2\)，并设
\[
 K=\mathbb Q(a,b),\qquad a^2=d,\quad b^2=2,\qquad
 R=\mathbb Z[a,b].
\]
令 \(\sigma(a,b)=(-a,b)\)、\(\tau(a,b)=(a,-b)\)。对整数四元组 \(n\)，取
\[
 \theta_n=n_1+n_2a+n_3b+n_4ab.
\]
评价行以
\[
 R_\alpha(n)=\theta_n^{\alpha_1}
   \sigma(\theta_n)^{\alpha_2}
   \sigma\tau(\theta_n)^{\alpha_3}
\]
为坐标，其中 \(\alpha\in\mathbb Z_{\ge0}^3\)。固定 \(H\ge1\)，按
\(w(\alpha)=\alpha_1+H\alpha_2+H\alpha_3\) 及固定 tie-break 递增扫描全部行，只在该行不属于先前保留行的 \(K\)-线性张成时保留。设所留行给出方阵 \(\Delta\ne0\)。

这一步的非零性是独立前提。它可以来自评价满秩或一个明确的非零子式。只知道若干行在 \(R/pR\) 中独立，不能取代此处的 \(K\)-满秩和 greedy 前序条件。

## 一个惰性素数的整除

令 \(p>H\) 为奇素数，\(p\nmid2d\)，并满足 \((d/p)=-1\)。Euler 判别式在 \(R/pR\) 给出
\[
 a^p\equiv-a,\qquad b^p\equiv(2/p)b.
\]
故对每个 \(\theta\in R\)，
\[
 \theta^p\equiv g_p(\theta)\pmod {pR},\qquad
 g_p=
 \begin{cases}
 \sigma,&(2/p)=1,\\
 \sigma\tau,&(2/p)=-1.
 \end{cases}
\]
设 \(j=2\) 或 \(3\)，分别对应这两个情形。对一个保留指标写
\(\alpha_1=pk+r\)，\(0\le r<p\)，并以
\[
 \widetilde R_\alpha(n)=
 \theta_n^r\bigl(\theta_n^p-g_p(\theta_n)\bigr)^k
 \sigma(\theta_n)^{\alpha_2}
 (\sigma\tau(\theta_n))^{\alpha_3}
\]
替换原行。二项展开严格为
\[
 \widetilde R_\alpha
 =R_\alpha+
 \sum_{m=1}^k(-1)^m\binom{k}{m}
 R_{\alpha-pm e_1+me_j}.
\]
每个修正行的权重比 \(R_\alpha\) 小 \(m(p-H)>0\)，因此由 greedy 构造落在先前保留行的张成中。全部替换构成对角元为 \(1\) 的下三角变换，故替换前后的行列式相等。另一方面，\(\widetilde R_\alpha\) 的每个条目属于 \(p^kR\)。于是
\[
 \Delta\in p^{E_p}R,\qquad
 E_p=\sum_{\alpha\ \mathrm{retained}}\left\lfloor\frac{\alpha_1}{p}\right\rfloor.
\]

四次域范数 \(N_{K/\mathbb Q}(\Delta)\) 是非零整数，所以
\[
 p^{4E_p}\mid N_{K/\mathbb Q}(\Delta).
\]
不同的满足同一输入条件的素数可相乘。要将此变成对数下界，还需分别证明 \(\Delta\ne0\)、可用素数集合以及 \(E_p\) 的总和下界。

## 精确有限复放

实际于本机 Python 3.13 中复算 \(d=5\)、\(p=3\)、\(H=2\)。此时 \((5/3)=-1\)、\((2/3)=-1\)，所以 \(g_p=\sigma\tau\)。对全部 \(n\in\{0,1\}^4\) 验证 \(\theta_n^3-\sigma\tau(\theta_n)\in3R\)。再取三个评价点 \(a,b,1+a\)，以常数行、\(\sigma\tau\)-行和三次行组成一个已声明的下三角替换实例。精确四元组乘法得到
\[
 \Delta=15+21a-18b-3ab,qquad
 N_{K/\mathbb Q}(\Delta)=2{,}005{,}884,
\]
且 \(81=3^4\) 整除该范数。这个三行例只复核 Frobenius 同余、行替换和范数指数。它没有复核原文的全评价满秩、权重和或素数和估计。

## 来源与迁移边界

来源为 OpenAI 预印本 *Uniform exclusion of Landau–Siegel zeros*，PDF pp. 4–8，特别是式 (4.1)–(4.3)、Lemma 6、式 (5.2)–(5.7)。本机归档 SHA-256 为 `fab9f6e84ece2a37d834b2c031d8eb14e81413d9f6270791e7b5468b295214ef`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf)

原文的零点排除还使用一个假定的实零导出的惰性素数加权下界，以及选定 \(H,N\) 后的 Archimedean Hadamard 上界比较。它们不属于本构件。

对欧拉常数 \(\gamma\) 的候选行列式，使用这里的估值机制前必须另行提供三件事。其一，\(\gamma\) 相关行可嵌入带上述 Frobenius 同余的整数代数环。其二，替换后行的较早跨度与非零子式有独立证明。其三，所得素数估值下界在同一归一化下超过 \(\gamma\) 线性形式的分母和解析余项界。现有 \(\gamma\) 技能没有给出这三项桥接，因此本页不产生 \(\gamma\) 的线性形式、整性或余项衰减结论。
