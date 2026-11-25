# 冻结方形瓦片与有限化

令
\[
E(D,V,L)=\{(s,p+sV(p)):p\in D,\ |s|\le L\},
\]
其中 (D\subset\mathbb R^2) 紧，(V) 在 (D) 的开邻域中为 (C^1)。若
\[
\operatorname{tr}DV(p)=0,\qquad -L^{-2}<\det DV(p)\le0\quad(p\in D),
\]
则对任意 \(\varepsilon>0\)，存在有限个紧非退化方形 (T_i) 与常速度 (g_i)，使
\[
E(D,V,L)\subset\bigcup_i\{(s,\xi):\xi\in T_i+sg_i\},
\qquad
\sum_i|T_i|J_h(g_i)\le\int_DJ_h(V(p))\,dp+\varepsilon.
\]
方形可以有不同方向。(D) 可以零面积，也可以有正面积边界。

## 冻结的线性覆盖

对迹零矩阵 (A)，存在正交基使
\[
A=\begin{pmatrix}0&b\\c&0\end{pmatrix},\qquad bc=-\det A.
\]
若 (0\le\alpha\beta<1)，中心为
\[
(i+\alpha j,\,\beta i+j),\qquad(i,j)\in\mathbb Z^2,
\]
的闭单位方块覆盖整个平面。对目标 (u)，令
\[
j=\lfloor u_2-\beta i+1/2\rfloor,
\quad F(i)=\lfloor u_1-\alpha j+1/2\rfloor.
\]
当 \(\alpha\beta\ge0\) 时 (F) 单调，且 (F(i)=\alpha\beta i+O(1)\)。由 \(\alpha\beta<1\) 取得一个有限不变整数区间，迭代到不动点，两个坐标误差均不超过半边长。该论证含 \(\alpha\beta=0\) 的平方零剪切。

对仿射速度 (W(p)=v_0+A(p-p_0))，缩放边长为 \(\tau\)，在时间 (s) 的参数为 \(sb,sc\)，其积为
\[
s^2bc=-s^2\det A\in[0,1).
\]
故相同方格覆盖每个高度。由 Cayley--Hamilton，
\[
(I+sA)^{-1}=\frac{I-sA}{1+s^2\det A}.
\]
严格下界 \(1+L^2\det A>0\) 是把实际非线性标签追溯到有限中心 collar 所必需的条件。

## 从局部线性化到有限表

在边长 \(\delta\) 的每个粗方块 (S\) 选择 (b_S\in S\cap D)，冻结
\[
V_S(p)=V(b_S)+DV(b_S)(p-b_S).
\]
令 \(\omega\) 为邻域中 (DV) 的连续模，则
\[
|V(p)-V_S(p)|\le\sqrt2\,\omega(\sqrt2\delta)\delta.
\]
细方格取边长 \(\tau=\delta^2\)。上式和统一的逆矩阵界使真正需要的格心距 (S) 至多
\[
R_\delta=C\{\tau+L\sqrt2\,\omega(\sqrt2\delta)\delta\}=o(\delta).
\]
所以每个粗方块只保留其 (R_\delta)-collar 内有限多个格心。collar 的相对面积消失，Riemann 型和由包含 (D) 的缩小外邻域收敛到积分。这里不需要 \(\partial D\) 的零面积。

## 可复核的小模型

本机 Python `Fraction` 枚举了三组 \((\alpha,\beta)\)，即 \((2/5,3/5)\)、\((-2/5,-3/5)\) 和 \((0,13/7)\)。对每组 (49^2) 个七分之一网格目标点，整数不动点均存在，且两个坐标误差均不超过 (1/2)。这复现有限格点机制，不代替任意实参数的单调不动点证明。

## 原文定位

- OpenAI, *Finite cylinder approximation of ruled sets*, PDF pp. 2--7, Proposition 1.1、Theorem 1.2、Lemmas 2.1--2.3。SHA-256 `06959ab19716522a939868729297d06016fa80b763407815ef5eecd470c279ae`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Finite-cylinder-approximation-of-ruled-sets-September-27-2026/main.pdf)
