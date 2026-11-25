# 受迫 Navier--Stokes：势截断与端点 jet

## 已定位来源与范围

- OpenAI, *Finite time blowup for Navier--Stokes*，官方固定 PDF：[navier-stokes.pdf](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)，166 页，SHA-256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`。本机盘点条目为 `standalone/Finite-time-blowup-for-Navier-Stokes.pdf`，状态为 `standalone-official-CDN`，学术复核为 `pending`。
- 本接口定位到 PDF p. 1, Theorem 1.1；pp. 117--118, Proposition 10.1；pp. 118--120, Lemmas 10.2--10.3。它们支持下面的局部化/延拓机制，不等于对论文其余爆破构造的认证。

## 局部化引理的可移植部分

采用
\[
 \partial_t u-\nu\Delta u+(u\mathbin\cdot\nabla)u+\nabla p=f,
 \qquad \nabla\mathbin\cdot u=0.
\]
设局部轴对称场在一个邻域写成
\[
 u_{\rm loc}=\operatorname{curl}A+B e_\theta,
\]
其中在其定义域内已经被核对为 Cartesian 光滑。取紧支撑的轴对称时空截断 `c(r,z,t)`，并定义
\[
 u=\operatorname{curl}(cA)+cB e_\theta,\qquad p=cp_{\rm loc}.
\tag{L}
\]
这里须截断 `A` 再取 curl。第一项的散度恒为零；第二项在圆柱坐标中满足
\[
 \nabla\mathbin\cdot(cB e_\theta)
 =r^{-1}\partial_\theta(cB)=0,
\]
因为 `c,B` 均与 `theta` 无关。这个等式是一次精确分量检查；它**不**证明 (L) 在 `r=0` 光滑，轴线处的 Cartesian 延拓仍须作为独立假设逐项核验。

令 (L) 的方程残差定义为 `f`。在 `c=1` 的局部模型区，`u,p` 与局部解一致；截断交换项只在过渡区出现。故要构造全局的光滑外力，过渡区必须避开局部奇点，或局部残差须在那里对目标时刻平坦到所需阶数。

## 端点延拓的最低条件

令目标时刻为 `T`。需要对每个空间多重指标 `alpha` 与每个 `j>=0`，证明
\[
 \partial_x^\alpha\partial_t^j f(\cdot,t)
 \longrightarrow \partial_x^\alpha F_j
 \quad(t\uparrow T)
\]
在空间上一致，并有共同的紧支撑。\(F_j\) 是空间函数。不同空间导数的极限须等于 \(\partial_x^\alpha F_j\)，而时间方向的兼容性来自各阶导数是同一残差 \(f\) 的逐阶一侧端点极限。原文在远离奇点的区域验证正常延拓，在奇点附近用局部残差的平坦性控制各阶导数。单有速度范数估计不能给出这些端点极限。

令 \(\sigma=t-T\)，取在零的邻域恒为 \(1\) 的光滑紧支撑截断 \(\chi_0\)。对 \(\sigma\ge0\) 定义
\[
 \widetilde f(x,T+\sigma)
 =\sum_{j\ge0}\chi_0(b_j\sigma)\frac{\sigma^j}{j!}F_j(x).
\]
每项的任意固定低阶时空导数在 \(b_j\to\infty\) 时一致趋零，只要时间求导阶数小于 \(j\)。对足够大的 \(j\) 选择 \(b_j\) 使总阶数至多 \(\lfloor j/2\rfloor\) 的导数上界为 \(2^{-j}\)。每个固定导数阶数的尾部于是可一致求和。在端点逐项求导得到所需 \(F_j\)，故可与 \(t<T\) 的残差光滑拼接。全部项可放在同一有界时间区间内。

## 结论边界

来源 Theorem 1.1（PDF p. 1）声称的对象是带 `f in C_c^infty(R^3 x (0,infty))`、零初值的经典受迫解；本接口只使用上述局部机制。外力一般无需无散度，且这里没有得到无外力 Navier--Stokes、弱解、适合弱解或任意初值的结论。
