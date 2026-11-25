# 张量方差证明

本页从上一页的矩坐标证书出发。记 \(\tau=D_z^2\phi\)、\(M=\tau^{-1}\)，均以目标坐标 \(x\) 表示。对偶测试函数先取实值、偶的 \(f\in C_c^\infty(\mathbb R^n)\)，并定义
\[
B=\tau(D_x^2f)\tau,
\qquad W=\delta_\mu B,
\qquad u=\delta_\mu W,
\]
其中 \(\delta_\mu\) 是负加权散度。令 \(H=D_x^2V\)。经两次紧支撑分部积分，已核读的张量恒等式给出
\[
\mathbb E u^2\ge
 \mathbb E\operatorname{tr}(MBHB)+\mathbb E(W^\top HW).
\tag{4}
\]
它来自 Bochner 项与一个点态平方和。这个恒等式只能在已满足矩坐标方程、测试函数确实紧支撑的条件下使用。

对软 slab 项 \(H_i=D^2\psi_i\)，有
\[
H_i\succeq0,
\qquad x\cdot\nabla\psi_i=q\psi_i,
\qquad H_ix=(q-1)\nabla\psi_i.
\tag{5}
\]
令 \(a_i=\mathbb E\psi_i>0\)、\(d_i=\mathbb E(u\psi_i)\)。矩坐标分部积分给出
\[
m_i:=\mathbb E\operatorname{tr}(\tau H_i)=q a_i,
\qquad d_i=\mathbb E\operatorname{tr}(BH_i).
\tag{6}
\]
第一次数 Cauchy--Schwarz 在 Hilbert--Schmidt 内积中给出
\[
d_i^2\le m_i\,\mathbb E\operatorname{tr}(MBH_iB).
\tag{7}
\]
第二次在半正定二次型 \(H_i\) 中给出
\[
\mathbb E(W^\top H_iW)\ge\frac{(q-1)d_i^2}{m_i}.
\tag{8}
\]
因为 \(H=2rI+\sum_iH_i\)，把 (7)--(8) 代入 (4) 得
\[
\mathbb Eu^2\ge\sum_i\frac{q d_i^2}{m_i}
=\sum_i\frac{d_i^2}{a_i}.
\tag{9}
\]

若双散度函数 \(u\) 在中心化偶 \(L^2(\mu)\) 中稠密，(9) 延拓到所有这样的 \(u\)。令 \(u=\sum_i b_i\psi_i-\mathbb E\sum_i b_i\psi_i\)，再用 Cauchy--Schwarz，得到
\[
\operatorname{Var}_\mu\!\left(\sum_i b_i\psi_i\right)
\le\sum_i b_i^2a_i.
\]
稠密性需要矩坐标上界 \(\tau\preceq\Lambda I\)、局部正定和对应的紧支撑 Hessian 恒等式。它不能由形式上的散度计算替代。

## 精确高斯 sanity check

取 \(n=2,q=2,r=1\)、\(p_1=e_1,p_2=e_2\)、\(h_1=1,h_2=2\)。则
\[
V=2x_1^2+\frac54x_2^2,
\quad \mathbb E\psi_1=\frac14,
\quad \mathbb E\psi_2=\frac1{10},
\quad \operatorname{Var}(\psi_1)=\frac18,
\quad \operatorname{Var}(\psi_2)=\frac1{50}.
\]
独立性使交叉协方差为零。对 \((b_1,b_2)=(3,-4)\)，左端为
\(9/8+16/50=289/200\)，右端为 \(9/4+16/10=77/20\)。这验证了一个精确有限参数实例。它不替代 (4) 或稠密性论证。

来源定位

- OpenAI 预印本 PDF 12--16 页，Lemmas 6.1、证明 Proposition 2.1 中的式 (7.1)--(7.6)，SHA-256 `d5c7e764dee425e8172446d0a9dacc2d657a69e8f8b46ac5b68957200a5f09cc`。[固定归档](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/paper.pdf)
