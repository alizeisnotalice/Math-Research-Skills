# 指定速度场、慢时钟与有限盒输运

本页处理有限或已给定的光滑构造。它不从任意力推出光滑解，也不把计算编码、不可判定性、长期稳定性或 Navier--Stokes 无外力命题作为结论。

## 1. 残差和比较类

在
\[
 U_t+(U\cdot\nabla)U=-\nabla p+\nu\Delta U+f,
 \qquad \operatorname{div}U=0,
\]
给定光滑无散度 (U) 且 (U(0)=0) 时，取
\[
 F_\nu[U]=U_t+(U\cdot\nabla)U-\nu\Delta U,
 \qquad p=0,
\]
即有一个显式受迫解。全空间的比较还要求每个有限时间区间上
\[
 U\in C H^2\cap C^1L^2,\qquad U,\nabla U\text{ 有界}.
\]
若竞争解属于所声明的经典或强解类，并且其压力项可按相应类消去，则 (w=v-U) 满足
\[
 \frac12\frac{d}{dt}\lVert w\rVert_2^2+\nu\lVert\nabla w\rVert_2^2
 \le \lVert\nabla U\rVert_{\infty,\mathrm{op}}\lVert w\rVert_2^2.
\]
零初值由 Gronwall 给出 (v=U)。在 \(\mathbb R^3\) 上，不能只写“压力相消”：可使用 (p\in H^1) 的逼近、(p\in L^2) 的 cutoff 边界项，或已经证明 \(\nabla p\in L^2\) 时的 Fourier 正交。环面上，连续的周期压力和空间分部积分即可，均值零条件固定压力常数。

这一局部结论来自 *Incompressible Box Transport and Finite Computation*，PDF pp. 3--5，Lemma 2.1--2.2，SHA-256 `2505dc09d3f2c24b91b8a1bd4ae58876095f1d1407ead933464b79731ae5d312`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Incompressible-Box-Transport-and-Finite-Computation-October-6-2026/manuscript.pdf)

## 2. 保留全部有限时间的慢时钟

令 (W(s,x)) 是 (s\ge0) 上光滑无散度场，(W(0)=0)，每个混合导数有界。全空间版本还要求支撑位于一个固定紧集。若 (g(0)=0)、(g\) 光滑、非减且映满 ([0,\infty))，则
\[
 u(t,x)=g'(t)W(g(t),x),
\]
的残差是
\[
 F_\nu[u]=g''W-\nu g'\Delta W+(g')^2\{\partial_sW+(W\cdot\nabla)W\},
\]
其中右端都在 (s=g(t)) 处取值。物质流满足
\[
 X_u(t,a)=X_W(g(t),a).
\]
因此只要目标事件只看任意有限逻辑时间，且 (g) 满射，两个流的全时间到达事件相同。对 (g(t)=\log(1+t))，来源给出每个固定时空导数的 ((1+t)^{-1-j}) 型衰减。若 (g\) 的极限有限，它遗漏之后的逻辑时间，不能用于该等价。

*Scalar Potentials and Slow Clocks for Forced Fluid Computation*，PDF pp. 3--5，Lemma 2.1 和 Lemma 3.1，SHA-256 `82005335f0aac60fbd7f84ba2d4aee576671a54cc39b2662e263063e62ac45e1`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation-September-27-2026/manuscript.pdf)

## 3. 仅在环面上的 Helmholtz 压力转移

令 (g) 是平坦三维环面上的光滑均值零体力。解
\[
 \Delta\phi=\operatorname{div}g,\qquad \int\phi=0,
\]
并替换
\[
 (g,p)\longmapsto(g-\nabla\phi,p-\phi).
\]
速度保持不变，新力无散度。Fourier 模式 (k\ne0) 上
\[
 \widehat\phi(k)=-\frac{i\xi_k\cdot\widehat g(k)}{|\xi_k|^2}.
\]
故混合导数界、时间 (L^2) 界以及给定的周期性、最终平稳性或逐阶衰减均被保留。这个投影一般改变压力，并不保持欧氏空间中的紧支撑。

*Universal Computation with Eventually Stationary Navier--Stokes Forcing*，PDF p. 6，Proposition 2.4，SHA-256 `0af659c5a6f8e7b07c66d3301055e8a80e616c938ffb6027272e42097374d0d5`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/manuscript.pdf)

## 4. 有限正对角盒映射

设 (Q_i=a_i+\prod_{j=1}^3[-h_{ij},h_{ij}]) 和 (Q'_i=b_i+\prod_{j=1}^3[-k_{ij},k_{ij}]) 是两个有限有理实心盒族。每个盒的半宽为正，源盒彼此不交，目标盒彼此不交。对每个 (i)，令 (s_{ij}=k_{ij}/h_{ij}>0)，并要求 (\prod_j s_{ij}=1)。

原文构造一条紧支撑光滑无散度场，时间支撑在 ([1/4,3/4])，使得其时间一流在每个 (Q_i) 的一个开邻域上恰为
\[
 a_i+y\longmapsto b_i+\operatorname{diag}(s_{i1},s_{i2},s_{i3})y.
\]
构造先共同扩张中心、在分开的停车位改变形状，再逐个沿避开当前静止盒的有理折线路径运输，最后共同收缩。每段使用平坦时间开关和局部 curl 或 Hamiltonian 片段。这里“两个族分别不交”是实质条件。源盒和目标盒之间可相交，因为所有源盒先被撤到停车位，才开始送达。

这个盒输运可作为已经证实有限几何假设下的输入。它不自动给出无限表、周期拼接、普适计算或统一的导数常数。

*Incompressible Box Transport and Finite Computation*，PDF pp. 9--11，Lemma 3.3 和 Theorem 3.4，SHA-256 `2505dc09d3f2c24b91b8a1bd4ae58876095f1d1407ead933464b79731ae5d312`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Incompressible-Box-Transport-and-Finite-Computation-October-6-2026/manuscript.pdf)

## 5. 同一来源簇中尚未普适化的材料

下表把 Family 376 的其余手稿留作来源定位，避免把编译器步骤误作一般流体工具。

| 论文 | 已核对定位 | 状态 |
| --- | --- | --- |
| *Finite Instructions and Solenoidal Shear Flows*，`0cdc2abd…` | PDF pp. 2, 13--14 的有限可逆记录器与全矩形 shear | 需要完整规则域、逆记录和正分离余量。 |
| *Prefix Instructions and Incompressible Flows*，`8cd58142…` | PDF pp. 2, 52--53 的守卫前缀和三维补偿 | 依赖注入规则、完整逆和满时钟。 |
| *Velocity-Field Detection of Computation in Forced Navier--Stokes Flows*，`a69fca6b…` | PDF pp. 3--4 的 (U=(a,w)) 被动标量化 | 只在已给二维无散度 (a) 和已解标量方程时适用。 |
| *A Fixed Particle Test for Computation in a Forced Viscous Flow*，`87defbd4…` | PDF pp. 3, 5, 8--12 | 记录器和分支插值依赖同族投影、解析构造。 |
| *Computation under Rapidly Vanishing Navier--Stokes Forcing*，`931c0784…` | PDF pp. 3--4, 7--18 | 依赖前一编译器及尺度分离极限。 |
| *Geometric Programs for Solenoidal Forcing*，`1e540905…` | PDF pp. 2, 28--29 | 依赖 shear 记录器。 |

完整 SHA、固定链接与“候选或保留”状态见本机逐篇账本。它们不改变前四节的明确输入输出。

运行 [代数回放](../scripts/check_prescribed_velocity.py) 可检查残差、慢时钟、周期 Helmholtz 投影和正对角行列式。该回放不构造紧支撑路由流。
