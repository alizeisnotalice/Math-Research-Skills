# Brent--McMillan B1 的有限递推

对整数 \(n\ge1\)，Brent--McMillan 定义

\[
 U(n)=\sum_{k\ge0}\frac{n^{2k}}{(k!)^2}(H_k-\log n),\qquad
 V(n)=\sum_{k\ge0}\frac{n^{2k}}{(k!)^2}.
\]

利用 \(\gamma+\log n=(S_0(2n)-K_0(2n))/I_0(2n)\) 和正实轴上的 Bessel 界，原文式 (5) 给出

\[
0<\frac{U(n)}{V(n)}-\gamma<\pi e^{-4n}.
\]

式 (9)--(10) 允许不显式形成阶乘地递推 \(A_k,B_k,U_k,V_k\)。默认运行 [B1 递推](../scripts/brent_mcmillan_b1.py) 以安装了 mpmath 的 Python 作有限截断数值评估。输出单独给出无限和的解析 Bessel 误差界，有限截断及浮点误差另行估计。

`--rigorous` 以有理数输出有限 B1 区间。令 \(b_k=(n^k/k!)^2\)，\(S_N=\sum_{k=0}^N b_kH_k\)，\(V_N=\sum_{k=0}^N b_k\)。当

\[
r=\frac{n^2}{(N+2)^2}<1,
\]

时，脚本使用

\[
0\le S-S_N\le b_{N+1}\left(
\frac{H_{N+1}}{1-r}+\frac{r}{(N+2)(1-r)^2}\right)=:T_N.
\]

每个新增权重对应的 \(H_k\) 不小于先前加权平均，故 \(S_N/V_N\le S/V\)。再以正项指数级数给出 \(e^{4n}\) 的下界，并以 \(22/7>\pi\) 支配 Bessel 余项。对 atanh 级数所得有理端点 \(\ell\le\log n\le h\)，脚本认证

\[
\frac{S_N}{V_N}-h-\frac{22/7}{E}\le\gamma
\le\frac{S_N+T_N}{V_N}-\ell,
\]

其中 \(E<e^{4n}\) 是所取正项部分和。这给出严格有限区间，也只给出有限分母排除。研究无理性仍需同一指标子列上的额外算术论证。

```sh
python3 scripts/brent_mcmillan_b1.py 2 --rigorous --tail-index 12 --exp-terms 80 --log-digits 40
```

本机以此命令获得含 \(\gamma\) 的正宽有理区间，并以 100 位独立数值计算交叉核对。`--tail-index 0` 在 \(n=2\) 时因 \(r=1\) 被拒绝。

## 版本和勘误

本机一页原件 SHA-256 `e4290e83059ffd586850d06c1b474b93d7dc22bf2362abe946e04bc6593da7dc` 仅含摘要。为复核本条，另从作者页面取得正式刊载扫描件，*Mathematics of Computation* 34 (1980), 305--312，8 个物理页，SHA-256 `fce10ae904100a2e85955fb2c3affd9d4c5e65079986cc73bd0c8192423496c1`。采用刊载页 306--307（PDF 物理页 2–3） 的式 (2)、(5)--(10)。刊载页 308 的式 (13) 是 B2 的渐近 K_0 展开，不能作为严格 B1 截断证书。

作者勘误仅修改刊载页 310、式 (17) 后 \(V_p(z)\) 的一个因子，即把 \((z/k!)^p\) 改为 \((z^k/k!)^p\)。这不触及 B1 的式 (2)、(5)--(10)。B3 原文中所述经验相对误差也不提升为定理。

来源。Richard P. Brent and Edwin M. McMillan, *Some new algorithms for high-precision computation of Euler's constant*, *Mathematics of Computation* 34 (1980), 305--312，DOI `10.1090/S0025-5718-1980-0551307-4`。作者的[论文与勘误页](https://maths-people.anu.edu.au/~brent/pub/pub049.html)和[扫描件](https://maths-people.anu.edu.au/~brent/pd/rpb049.pdf)在 2026-11-26 核对。
