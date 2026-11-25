---
name: math-f08-matrix-trace-energy
description: 核验有限维 PSD Gram 矩阵的 \(\operatorname{tr}(P^{3/2})\) Hessian、Loewner 比较与正能量望远镜，并在需要时检查有限维 trace Young 等号。
---

# F08 · 矩阵迹能量与望远镜证书

用于有限维 Gram 矩阵、二叉平均或热流离散化中的正能量增量。令
\[
  \Phi(P)=\operatorname{tr}(P^{3/2}),\qquad P\succeq0.
\]
先声明工作在实对称或复 Hermitian 矩阵上，并说明每一个方向是否在
\(\operatorname{supp}P=(\ker P)^\perp\) 上。它不证明三角 Hilbert 变换、Lieb--Thirring 不等式或任何无限维极限结论。

## Hessian、顺序比较与中点增量

若 Hermitian \(K\) 在 \(P\) 上有支撑，定义
\[
 \mathcal B_P(K,L)=\frac32\operatorname{Re}\langle K,
 (\mathsf L_{\sqrt P}+\mathsf R_{\sqrt P})^{-1}L\rangle_{HS},
 \qquad b_P(K)=\mathcal B_P(K,K).
\]
在 \(P\) 的正特征子空间中，若特征值为 \(p_i>0\)，则
\[
 b_P(K)=\frac32\sum_{i,j}\frac{|K_{ij}|^2}{\sqrt{p_i}+\sqrt{p_j}}.
\]
因此固定支撑的正定锥上
\[
 d\Phi_P(K)=\frac32\operatorname{tr}(\sqrt P K),
 \qquad d^2\Phi_P(K,L)=\mathcal B_P(K,L).
\]

对半正定边界，先限制到支撑，或以 \(P+\eta I\) 正则化后令 \(\eta\downarrow0\)。方向不消去 \(\ker P\) 时，上式没有定义，不能把有限差分当成 Hessian 证书。

若 \(P\preceq aQ\)、\(a\ge1\)，则每个 \(P\)-支持的 \(K\) 也是 \(Q\)-支持的，并且
\[
 b_P(K)\ge a^{-1/2}b_Q(K).
\]
实际使用时要检查 Loewner 不等式，不能只比较 trace 或逐项特征值。它来自平方根的算子单调性及 Sylvester 算子的逆序。

若 \(-T\preceq U\preceq T\)，则 \(U\) 自动在 \(T\) 上有支撑，且
\[
 \frac{\Phi(T+U)+\Phi(T-U)}2-\Phi(T)
 \ge\frac{1}{2\sqrt2}b_T(U).
\]
这给出一个可检查的二叉能量增量。遇到多分支平均时，先把每个孩子写成有共同父矩阵的 \(T\pm U\) 配对，逐对应用它。任意正权平均需要另行证明对应的凸性或分解，不可直接沿用常数。

## 望远镜账本

设每个父节点的子节点可按 \(T\pm U\) 配对，每对两端权重相同。令 \(E_k\) 为第 \(k\) 层 \(\Phi\) 的加权和。若总子权重等于父权重，则上述中点增量给出 \(E_{k+1}\ge E_k\)。对有限层范围，逐层相加得到
\[
 \sum_{k=m}^{n-1}(E_{k+1}-E_k)=E_n-E_m.
\]
报告中需列出节点到父节点的唯一性、每层权重守恒及最终 \(E_n\) 的独立上界。单个 \(\Phi\) 增量为正不足以形成全局界。

## 可选的有限维 trace Young 门槛

对 \(0<\sigma<1\)，令 \(p=1+\sigma\)、\(q=1+\sigma^{-1}\)、
\(D_\sigma=\sigma^\sigma/(1+\sigma)^{1+\sigma}\)。有限维 \(W,Z\succeq0\) 满足
\[
 D_\sigma\operatorname{tr}(W^p)-\operatorname{tr}(WZ)+\operatorname{tr}(Z^q)\ge0.
\]
等号当且仅当 \(W=qZ^{q-1}\)。这个等号断言包含零特征子空间，需在有限维谱分解中逐项检查。它只能控制这里的代数密度项，不能取代谱算子、作用泛函或可积性论证。

固定来源和页码、半正定支撑约定及有限 replay 见 [来源与复算](references/sources.md)。运行 [复算脚本](scripts/check_trace_energy.py) 核对二阶差分、Loewner 中点间隙、二叉望远镜和 trace Young 等号。
