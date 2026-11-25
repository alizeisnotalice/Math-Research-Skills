---
name: math-n09-soft-slab-variance
description: 对偶次线性形式的强凸软 slab 势构造或审查方差界。核对矩坐标证书、逐项 Hessian 正性与张量估计，输出可用于参数对数凹性的有限维方差结论。
---

# N09 · 软 slab 势的矩坐标方差

输入为维数 \(n\ge2\)、调节参数 \(r>0\)、偶整数 \(q\ge2\)、非零向量 \(p_i\in\mathbb R^n\)、宽度 \(h_i>0\)，以及
\[
 \psi_i(x)=\left(\frac{\langle p_i,x\rangle}{h_i}\right)^q,
 \qquad V(x)=r|x|^2+\sum_i\psi_i(x),
 \qquad d\mu=Z^{-1}e^{-V(x)}dx.
\]
这些向量可以不张成 \(\mathbb R^n\)。二次调节项给出 \(D^2V\succeq2rI\)，使 \(\mu\) 为全空间的平滑偶概率测度。

目标是验证
\[
 \operatorname{Var}_\mu\!\left(\sum_i b_i\psi_i\right)
 \le\sum_i b_i^2\mathbb E_\mu\psi_i
 \tag{1}
\]
及其对参数化势的对数凹性后果。这里的调节参数 \(r\) 与矩坐标定理中使用的强凸常数 \(m=2r\) 分开记录。

## 执行

1. 先验证每个 \(p_i\ne0\)、\(q\) 为偶整数，并明确 \(r>0\)。若从几何 slab 极限开始，先固定 \(q,r\)，不能把 \(q\to\infty\) 或 \(r\downarrow0\) 当作方差工具本身的一部分。
2. 建立或审计 [矩坐标证书](references/moment-coordinate-certificate.md)。它需要偶的平滑势、\(D^2V\succeq mI\)，以及把 \(e^{-\phi}dz\) 推到 \(\mu\) 的全局 Hessian 梯度微分同胚。证书给出 \(0<D^2\phi\preceq4m^{-1}I\)。
3. 对紧支撑偶测试函数构造双散度测试。按 [张量证明](references/tensor-variance-proof.md) 分别核对 \(H_i=D^2\psi_i\succeq0\)、齐次恒等式和两次 Cauchy--Schwarz。结论先只在这个稠密测试类成立。
4. 只有在矩坐标证书所给的全局上界与局部正定性满足密度引理时，才把对偶不等式延拓到所有中心化偶 \(L^2(\mu)\) 函数，并由对偶性得到 (1)。

## 边界

此入口不处理奇次幂、非线性缺乏 PSD Hessian 的项、没有二次调节的退化势，或任意一般的偶凸加项。它也不自动证明 slab 极限、Wulff 体的体积不等式、对数 Brunn--Minkowski 结论或对一般测度的转移。使用那些步骤时须分别核对逼近、单调收敛与实际引用的定理。

原文是 OpenAI 预印本，局部方差接口和其引用的矩坐标定理已经定位核读，不能据此认证整篇全局结论。
