# 共同精确标签的有限测度恒等式

当多个 posterior replicas 条件于同一个 \((A,Y)\) 时，不能把单点条件密度的 a.e. 版本直接代入 \(Y=Au_1\)。应先使用有限测度恒等式。

设 \(P_0\) 是 \(S^{d-1}\) 上均匀概率或 \(\mathbb R^d\) 上标准 Gaussian，\(\nu=fP_0\)，其中 \(f\) 有界非负 Borel。令 \(k,m\ge1\)、\(t=m+1\)、\(k+m\le d-2\)。对 full-rank \(A\)，令 \(p_A\) 是投影密度，\(\nu_{A,y}\) 为正纤维上的正规条件概率，且

\[
 J(u)=\prod_{i=2}^{t}\operatorname{dist}(u_i,
 \operatorname{aff}(u_1,\ldots,u_{i-1})).
\]

那么对任意非负 Borel \(H\)，

\[
\begin{aligned}
 &\int\gamma_{k,d}(dA)\int p_A(y)^t
 \int H(A,y,u)\,\nu_{A,y}^{\otimes t}(du)\,dy\\
 &= (2\pi)^{-km/2}\int J(u)^{-k}\nu^{\otimes t}(du)
 \int H(A,Au_1,u)\,\gamma_{F_u^{k,d}}(dA).
\end{aligned}
\]

右侧的 \(\gamma_{F_u^{k,d}}\) 是 annihilate tuple differences 的 Gaussian fiber law。恒等式是有限测度恒等式，不是两种未加权概率实验的同分布。

## 版本纪律

球平均或 Gaussian approximate identities 给出的 jointly measurable \(p_A(y)\) 与通常 disintegration density 对 Lebesgue-a.e. \(y\) 一致。来源只进一步证明：在上述有限 reference measure

\[
 \nu^{\otimes t}(du)\gamma_{F_u^{k,d}}(dA)
\]

下，它们在约束点 \(y=Au_1\) 几乎处处一致、有限且为正。任何 posterior-replica likelihood 的除法都只能在这个正质量集合上进行，并先作截断再用单调收敛。

对概率先验 \(p=fP_0\)，来源由此得到（在相应 reference measure 下）

\[
 \frac{dQ}{dR}(u,A)=(2\pi)^{-km/2}J(u)^{-k}p_A(Au_1)^{-m}.
\]

这个公式是后续信息论路线的入口，不自动给出 entropy 可积性或流式 lower bound；这些仍要独立核对先验上界、inverse moments 和所有 conditioning。
