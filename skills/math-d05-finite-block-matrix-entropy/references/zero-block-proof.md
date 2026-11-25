# 零块熵证明与来源边界

设 \(U,V\succeq0\) 有相同迹。有限维中
\[
 S(U)-S(V)=\int_0^\infty
 \frac{\log\det(I+rU)-\log\det(I+rV)}{r^2}\,dr.
\]
等迹使原点的被积括号为 \(O(r^2)\)，积分分部后按特征值求原函数即可。它允许 \(U,V\) 尺寸不同和有零特征值。

对正定 \(D,E\) 及固定 \(Z\)，定义
\[
 G_Z(D,E)=\log\det(D+ZE^{-1}Z^*)-\log\det D.
\]
它对 \((D,E)\) 联合凸。沿仿射线，把对应的二乘二块矩阵写为 \(\mathcal C=\mathcal D+\mathcal H\)。以 \(\mathcal D^{-1/2}\) 共轭后，差为反 Hermitian 矩阵 \(K\)。\((I+K)^{-1}\) 是收缩，行列式二阶导数化为 Hilbert--Schmidt 范数之差，从而非负。该证明要求 \(D,E\) 正定。

在零块设置中，将 \(A\) 奇异值对角化，写 \(A=\operatorname{diag}(\sqrt{x_i})\)，\(y_i=(BB^*)_{ii}\)、\(z_i=(C^*C)_{ii}\)。对全部对角符号矩阵同步平均 \(D=I+rBB^*\) 与 \(E=I+rC^*C\)。联合凸性给出其对角压缩的下界。由 Schur 补和上述积分，矩阵熵赤字不超过
\[
 \sum_iF(x_i,y_i,z_i),
\]
其中 \(F\) 是三项离散熵和同质量、乘积为 \(yz\) 的二谱熵之间的差。\(F\) 正一齐次且凹，所以 \(\sum_iF(x_i,y_i,z_i)\le F(\sum_i x_i,\sum_i y_i,\sum_i z_i)\)。这给出入口的零块证书。

来源是 OpenAI 预印本 *Classical capacity and entropy inequalities for generalized amplitude damping*，PDF pp. 5–8，Theorem 2.1 与 Lemmas 2.2–2.4。SHA-256 为 `5656514823b55d5a4dbb15b284a2637952b957a451aef2e6428f3efbb88f6442`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/paper.pdf)

PDF pp. 9–14 将此有限块不等式用于热阻尼的多次使用与 Holevo 优化。那一整条通道论证包含特定通道参数、纯态分解、逐位置凸性和 ensemble 上界，本技能没有独立认证为一般通道结论。Family 272 的 PPT/可分性文章使用不同的 CP、PPT 和 Choi 转移结构，未并入本入口。
