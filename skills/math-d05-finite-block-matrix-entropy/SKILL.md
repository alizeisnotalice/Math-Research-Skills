---
name: math-d05-finite-block-matrix-entropy
description: 为有限维三块 Gram 矩阵核验零块熵下界，使用 log-det 表示、Schur 补和符号平均分离块内熵与标量熵。
---

# D05 · 有限三块矩阵熵证书

用于有限维通道 Stinespring/Kraus 矩阵、Gram 矩阵或带一个零角块的二乘二块矩阵。输入是同形的复矩阵
\[
 A,B,C\in\mathbb C^{d\times e},\qquad
 M=\begin{pmatrix}A&B\\C&0\end{pmatrix},
\]
以及其平方 Frobenius 质量 \(x=\operatorname{tr}(AA^*)\)、\(y=\operatorname{tr}(BB^*)\)、\(z=\operatorname{tr}(CC^*)\)。本技能只给有限维的熵证书。它不推出广义振幅阻尼信道的经典容量、纠缠性质或无限维通道结论。

## 零块熵证书

先检查 \(x+y+z=1\)。对半正定、迹一矩阵采用
\[
 S(R)=-\operatorname{tr}(R\log R),
\]
并令 \(g(u)\) 是迹一的二乘二矩阵、行列式 \(u\in[0,1/4]\) 的熵。它可由特征值
\[
 \lambda_\pm=\frac{1\pm\sqrt{1-4u}}2
\]
直接计算。则
\[
 S(MM^*)\ge xS(AA^*/x)+yS(BB^*/y)+zS(CC^*/z)+g(yz),
\]
且质量为零的项省去。这里的归一化和零块位置是实质条件。任意两乘二块矩阵、任意块范数压缩或一般块稀疏图不能直接调用这个式子。

若需要重新证明或审计该证书，读[推导与来源](references/zero-block-proof.md)。核心门槛是

1. 对等迹半正定矩阵，用 \(\log\det(I+rR)\) 的 \(dr/r^2\) 积分表示熵差。
2. Schur 补中的两个对角块必须严格正定。这里它们为 \(I+rBB^*\) 与 \(I+rC^*C\)，所以即使原始块奇异也合法。
3. 先以 \(A\) 的奇异值分解固定坐标，再同步按对角 \(\pm1\) 符号平均。只有共同的符号共轭保持 \(A\) 时，联合凸性才能删除 \(BB^*\) 和 \(C^*C\) 的非对角项。
4. 最后将逐坐标标量赤字以正齐次凹函数合并。若质量不归一，先明确熵的非归一约定并单独缩放。

### 已验证的局部扩展

给定块矩阵
\[
 T=\begin{pmatrix}
 \alpha XX^*+\beta YY^*&KXY^*\\
 KYX^*&\eta XX^*+\delta YY^*
 \end{pmatrix},
\]
其中 \(\operatorname{tr}(XX^*)=\operatorname{tr}(YY^*)=1\)，四个系数非负、和为一且
\(\alpha\delta-\beta\eta=K^2\)，令
\(u=(\alpha+\beta)(\eta+\delta)-K^2\)。将系数沿
\((\beta,\eta)\) 的线段拆为两个端点，可以把每个端点写成上述零块 Gram 矩阵。因此
\[
 S(T)\ge(\alpha+\eta)S(XX^*)+(\beta+\delta)S(YY^*)+g(u).
\]
此结论不要求 \(X,Y\) 正交或其 Gram 矩阵可交换。系数等式、归一化和有限维性都需逐项核验。

运行[有限复算](scripts/check_zero_block_entropy.py)以高精度复核标量零块的等号、两组三元质量的标量赤字超可加性，及上述系数拆分。它不是对任意量子信道的容量证明。
