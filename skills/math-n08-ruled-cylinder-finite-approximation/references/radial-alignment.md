# 径向对齐的一柱面一分割单元

设 (P\) 是二维欧氏平面，(e\perp P) 是单位向量，(a,b\in P) 线性无关，(R\) 连续，(w\in C^1([\alpha,\beta];P))。考虑
\[
S=\{p_0+\rho(a+tb)+s(e+w(t)):
t\in[\alpha,\beta],\ 0\le\rho\le R(t),\ |s|\le L\}.
\]
若
\[
w'(t)=\lambda(t)(a+tb),
\]
则每个带指定 tag 的有限分割区间 (I\) 只需一个平行于 (e+w(c_I)) 的柱面。其截距可取紧非退化三角形，全部柱面覆盖 (S)。网格趋零时总垂直底面积一致收敛到
\[
\kappa\int_\alpha^\beta
\frac{R(t)^2}{2\sqrt{1+\|w(t)\|^2}}\,dt,
\qquad\kappa=|\det_P(a,b)|.
\]

## 交叉误差为什么是二阶

固定 (I\)，长度为 (d_I)，中点为 (m_I)，标签为 (c_I)。沿冻结方向移到截距面后写成 (p_0+ua+vb)。对任意扫掠点，直接积分给出
\[
u=\rho+s\int_{c_I}^t\lambda(\xi)\,d\xi,
\qquad
v-tu=s\int_{c_I}^t\lambda(\xi)(\xi-t)\,d\xi.
\]
因此，若 (M=\max|\lambda|\)，(R_I=\max_I R)，则
\[
-LMd_I\le u\le R_I+LMd_I,
\quad |v-m_Iu|\le\frac{d_I}{2}|u|+\frac{LM}{2}d_I^2.
\]
第一项是径向坐标可吸收的一阶移动。剩余横向误差为 (O(d_I^2))。取一个尖端向负径向方向外推 (O(d_I)) 的三角形，即可同时吸收负 collar 和此横向误差。其新增面积为 (O(d_I^2))，求和由 \(\sum_Id_I^2\le\operatorname{mesh}(\beta-\alpha)\) 消失。

把每个三角形正交投影到冻结轴的垂直平面不会退化，投影面积的精确系数为 \((1+\|w(c_I)\|^2)^{-1/2}\)。实际扫掠的冻结投影包含 \(s=0\) 的径向扇形，其面积给出同一积分的下和。由一致连续性，上下和有相同极限。三角形有限面积与实际扫掠投影面积通常不同。

此模式不能用于一般 (w\)。条件 (w'(t)\parallel a+tb) 正是横向误差降为二阶的理由。径向参数为零、\(\lambda=0\) 或 tag 不取中点都被上述估计覆盖。

## 原文定位

- OpenAI, *Finite triangular approximation of radial sweeps*, PDF pp. 2--5，Theorem 1.1 及证明。SHA-256 `6e7f63022190f390e00a26a7f822d46b73290167bab9d9f1e94ef099f519fefd`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Finite-triangular-approximation-of-radial-sweeps-September-27-2026/main.pdf)
