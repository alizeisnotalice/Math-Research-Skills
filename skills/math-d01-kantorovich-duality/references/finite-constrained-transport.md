# 有限附加线性约束输运的精确见证

`scripts/finite_constrained_transport_certificate.py` 只核验给定的有限离散耦合、边缘势和附加等式约束乘子；所有输入为有理数，所有等式、松弛量和间隙均精确计算。它的价值是防止把受约束输运误证成普通 OT：即使约束右端为零，乘子项也不能从逐胞不等式中删去。

## 原文与适用范围

Danila Zaev, “On the Monge–Kantorovich Problem with Additional Linear Constraints,” [arXiv:1404.4962v1](https://arxiv.org/abs/1404.4962), submitted 19 April 2014；本地 PDF SHA-256 为 `335316951595dde0686a29e2d5a482d11054c4d8e448dff06b9c40ed663df864`。该记录只列 v1。Theorem 2.1（PDF pp. 5–7）针对 Polish 边缘、\(c\in CL(\mu)\) 与 \(W\subset CL(\mu)\)，给出

\[
 \inf_{\pi\in\Pi_W(\mu)}\int c\,d\pi
 =\sup\Bigl\{\sum_k\int f_k\,d\mu_k:
       \sum_k f_k(x_k)+\omega(x)\le c(x),\ \omega\in W\Bigr\},
\]

其中 \(\Pi_W\) 的定义是 \(\int\omega\,d\pi=0\) 对所有 \(\omega\in W\)。其证明使用普通 \(CL(\mu)\) 对偶和紧凸 minimax。论文不保证一般对偶最大元；Theorem 3.6 只给 \((c,W)\)-单调性的必要性，不能作充分最优性判据。

本脚本的有限产品集版本是独立的有限线性规划证书，并不声称验证上述无限空间的拓扑、可积性或强对偶前提。

## 有限 LP 的正确符号

令单元质量为 \(\pi_z\ge0\)，边缘等式为 \(A\pi=b\)，额外等式为 \(W_r\pi=d_r\)。最小化 \(c\cdot\pi\) 的对偶是

\[
 \max_{\phi,\lambda}\; b\cdot\phi+\sum_r\lambda_rd_r
 \quad\text{s.t.}\quad
 \sum_k\phi_k(z_k)+\sum_r\lambda_rW_r(z)\le c(z).
\]

所有 \(\lambda_r\) 都是自由符号的等式乘子。Zaev 的湮灭约束有 \(d_r=0\)：这会让 \(\lambda_rd_r\) 在目标值中消失，但不允许从逐胞约束中删除 \(\lambda_rW_r\)。脚本逐项核对恒等式

\[
c\cdot\pi-(b\cdot\phi+\lambda\cdot d)
=\sum_z\pi_z\,[c(z)-A^T\phi(z)-W^T\lambda(z)]
+\lambda\cdot(W\pi-d)+\phi\cdot(A\pi-b).
\]

因此，“原始可行 + 对偶可行 + 精确零间隙”是有限 LP 的最优达值见证；只给一个计划、只解普通无约束 OT、或给出近似小数都不是该证书。

## 示例

示例的两个边缘均为 \((1/2,1/2)\)，成本按单元顺序 \((0,0),(0,1),(1,0),(1,1)\) 为 \((0,2,2,0)\)。普通 OT 会取对角线并达到 0。额外约束 \(W=(1,-1,-1,1)\) 的积分必须为 0，强制每个单元质量为 \(1/4\)，成本变为 1。

取两个边缘势都为 \((1/2,1/2)\)，等式乘子 \(\lambda=-1\)，则每个单元的
\(\phi(x)+\psi(y)+\lambda W(x,y)\) 恰好等于成本；原始值与对偶值均为 1。这是乘子必需性的最小正例。

```sh
python3 scripts/finite_constrained_transport_certificate.py \
  examples/finite-constrained-transport.json
```

把乘子错误改为 0，会在对角单元产生负松弛，故对偶不可行；把均匀计划改回对角计划会违反附加等式。两种失败均应被报告为未获最优见证。

正式发表版本为 Mathematical Notes 98(5) (2015), 725–741。上述页码对应本机 arXiv v1。[正式题录及版本记录](https://www.mathnet.ru/eng/mzm10896)
