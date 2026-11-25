---
name: math-f09-positive-resolvent-densities
description: 在凸数值域上构造或审计正的边界 resolvent 密度与共同压缩表示，核对外部坐标、度量收缩和所有系数尺寸的量词。
---

# F09 · 正 resolvent 密度与共同边界表示

用于有限维矩阵的凸数值域计算中，需要把解析函数演算表示为边界上的正密度，或需要检验某一相似变换后的收缩矩阵是否给出同一套所有系数尺寸的压缩。它给出局部核与表示证书，不认证 Crouzeix 常数、最佳相似常数或任意谱集结论。

## 两条可用入口

### 原矩阵的 exterior resolvent

固定有界开凸域 \(\Omega\) 和一个给定的外部共形坐标 \(G\)，其中 \(G\) 在 \(|t|>r\) 单射，\(0<r<1\)，把 \(|t|>1\) 映到 \(\mathbb C\setminus\Omega\)，并在无穷远有简单极点。令
\[
 q(t)=tG'(t),\qquad
 K_A(t)=q(t)(G(t)I-A)^{-1},\qquad E_A(t)=K_A(t)+K_A(t)^* .
\]
若 \(W(A)\subset\Omega\)，则 \(G(t)I-A\) 在单位圆上可逆，且
\[
 E_A(t)\succeq0,\qquad \int_{\mathbb T}E_A(t)\,d\sigma(t)=2I.
\]
直接核对的恒等式是
\[
 (G(t)I-A)^*E_A(t)(G(t)I-A)
 =q(t)(G(t)I-A)^*+\overline{q(t)}(G(t)I-A).
\]
右端在单位向量 \(x\) 上的值为
\(2\operatorname{Re}[q(t)(G(t)-x^*Ax)]\)。它的非负性需要 \(q(t)\) 确为 \(\partial\Omega\) 的外法向量，以及 \(x^*Ax\in\Omega\)。仅有谱包含或 \(\|A\|\) 有界都不能替代数值域条件。

在上述坐标的无穷远展开
\[
 \frac{q(t)}{G(t)-z}=\sum_{k\ge0}b_k(z)t^{-k}
\]
定义标量 Faber 多项式 \(b_k\)。谱与单位圆有正距离时，\(K_A=\sum_{k\ge0}b_k(A)t^{-k}\) 在单位圆绝对一致收敛。该衰减是给定 \(A,G\) 的结论，不能从仅有的形式幂级数推断。

### 一个度量控制所有系数尺寸

另一条入口从 \(W(A)\subset\Omega\)、一个内圆盘坐标 \(f:\Omega\to\mathbb D\) 和 \(T=f(A)\) 开始。需要一个正定 \(H\) 使
\[
 T^*HT\preceq H,\qquad S=H^{1/2},\qquad A'=SAS^{-1},\qquad D=STS^{-1}=f(A'),\qquad \rho(D)<1.
\]
因而 \(D^*D\preceq I\)，允许 \(\|D\|=1\)。在 \(|\zeta|=1\) 定义
\[
 \Phi_D(\zeta)=(I-D/\zeta)^{-1}+[(I-D/\zeta)^{-1}]^*-I.
\]
则
\[
 (I-D/\zeta)^*\Phi_D(\zeta)(I-D/\zeta)=I-D^*D\succeq0.
\]
\(\rho(D)<1\) 还保证 \(\sum_{j\ge0}\|D^j\|<\infty\)，从而
\[
 \Phi_D(\zeta)=I+\sum_{j\ge1}(\zeta^{-j}D^j+\zeta^jD^{*j}),
 \qquad \int_{\mathbb T}\zeta^j\Phi_D(\zeta)\,d\sigma(\zeta)=D^j \quad(j\ge0).
\]
第二式的正幂约定很容易反向，提交前应以 \(j=1\) 实测或逐项积分复核。

若上述内圆盘坐标及外坐标给出边界重新参数化 \(\psi=f\circ G\)，且其角 Jacobian \(j(t)>0\) 已单独核对，则
\[
 \Lambda(t)=j(t)\Phi_D(\psi(t)),\qquad \int_{\mathbb T}\Lambda\,d\sigma=I.
\]
对每一个独立选择的系数尺寸 \(m\)，
\[
 V_m b=(\Lambda^{1/2}\otimes I_m)b
\]
是等距嵌入。对在 \(\Omega\) 邻域全纯的 \(M_m(\mathbb C)\)-值函数 \(v\)，可用同一 \(\Lambda\) 写出
\[
 v[A']=V_m^*\,M_{I_n\otimes(v\circ G)}\,V_m.
\]
密度只依赖 \(T,H,f,G\)，不依赖 \(m\) 或 \(v\)。这里的结论要求已经建立标量复合函数演算与边界变量替换。一个针对某个 \(m\) 的数值 quadrature 不足以推出“共同”表示。

## 使用边界

- 若 \(H\) 只是候选矩阵，应先精确或严格地验证 \(H\succ0\)、Lyapunov 不等式和 \(\rho(D)<1\)。一般相似变换不会自动产生这种 \(H\)。
- 原矩阵的 \(E_A\) 与相似后的 \(\Lambda\) 是不同的正系统，质量分别为 \(2I\) 和 \(I\)。不可互换，也不可把 \(W(A')\subset\Omega\) 当作 \(E_A\) 的前提。
- 当 \(\Omega\) 是线段或点时，先通过独立的解析凸外逼近取极限。这个极限可给固定函数的不等式，却不构造该退化集合上的 \(G\)、\(\Lambda\) 或最佳相似度量。
- 常数二、最小条件数和完整 Crouzeix 定理属于两篇预印本的完整后续比较链，未由本技能的局部核认证。

运行 [数值回放](scripts/check_positive_resolvents.py) 检查圆盘坐标下的正性、质量和前三个矩。它只检验指定有限矩阵与离散积分，不能替代边界正性证明。

来源、物理页码和未接纳的主结论见 [来源核对](references/sources.md)。
