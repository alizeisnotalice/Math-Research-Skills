# 矩坐标证书

令 \(V\in C^\infty(\mathbb R^n)\) 为偶势，且
\[
D^2V\succeq mI,\qquad m>0,
\]
并令 \(d\mu=Z^{-1}e^{-V}dx\)。这个强凸常数是矩坐标常数。对于本 Skill 的软 slab 势，\(m=2r\)，而非调节参数 \(r\) 本身。

证书应给出偶函数 \(\phi\in C^\infty(\mathbb R^n)\)，使
\[
d\nu(z)=e^{-\phi(z)}dz,
\qquad x=\nabla\phi(z),
\qquad (\nabla\phi)_\#\nu=\mu,
\]
其中 \(\nabla\phi\) 是 \(\mathbb R^n\) 到自身的微分同胚，并满足
\[
0<D_z^2\phi\preceq 4m^{-1}I.
\tag{2}
\]
正定性是逐点的。一般没有全空间一致的正下界。把
\(\tau(x)=D_z^2\phi((\nabla\phi)^{-1}x)\) 视作目标坐标中的矩阵场。后续密度论证只使用 \(0<\tau\preceq4m^{-1}I\)。

## 可核的构造链

可将证书归约为一族有界目标。对 \(R>0\)，令
\[
 Z_R=\int_{B_R}e^{-V(x)}dx,
 \qquad g_R(x)=Z_R^{-1}e^{-V(x)}\quad(x\in B_R).
\]
\(B_R\) 有光滑严格凸边界，\(g_R\) 平滑、严格正且因 \(V\) 偶而重心为零。Berman--Berndtsson 的第二边值问题给出平滑凸 \(\phi_R\)，使 \(\nabla\phi_R\) 把 \(\mathbb R^n\) 微分同胚地映至 \(B_R\)，并且
\[
\det D^2\phi_R=Z_R\exp(V(\nabla\phi_R)-\phi_R).
\tag{3}
\]
Klartag 的 Hessian 估计适用，因为 \(\rho_R=V+\log Z_R\) 在每个 \(B_R\) 上平滑、其所有导数有界且 \(D^2\rho_R\succeq mI\)。于是
\(D^2\phi_R\preceq4m^{-1}I\)，常数不依赖 \(R\)。

从此处取得全空间证书仍需实际完成以下分析。以 \(\nabla\phi_R^{-1}(0)=0\) 的平移归一化，建立 \(R\)-一致的线性下界和局部 \(C^k\) 控制。上界、(3) 的局部行列式下界和 Evans--Krylov/Schauder 紧性给出局部光滑极限。最后验证推前式、梯度像稠密并由支持平面论证满射。没有这些极限步骤时，只有一族有界目标证书，不能把它替换为全空间坐标。

## 实际核读的来源范围

- Berman--Berndtsson 的已发表 Theorem 1.1 要求凸体 \(P\) 含原点于内部、\(g\) 为 \(P\) 上的正平滑密度、且 \(g\,dp\) 的重心为零。它给出满足 \(g(\nabla\phi)\det D^2\phi=e^{-\phi}\) 的平滑凸势和到 \(\operatorname{int}P\) 的梯度微分同胚。其用于 \(P=B_R\)、\(g=g_R\) 的条件已逐条核对。
- Klartag 的 arXiv:1309.2767v1 Proposition 3.1 和 Remark 3.5 还要求支撑体边界光滑且处处正曲率、密度势在该有界体内平滑且各阶导数有界、及 \(D^2\rho\succeq mI\)。它给出明确常数 \(4/m\)。这一 arXiv 版本对应 2014 年正式出版的章节，但此处引用的是已逐页定位的 v1 断言。
- Cordero-Erausquin--Klartag 的正式发表的 *Moment measures* 给出一般有限、非退化、零重心测度的 essentially-continuous 解。它不单独给出上述平滑性和 Hessian 上界，不能替代前两项。

固定来源与页码

- OpenAI, *The logarithmic Brunn--Minkowski conjecture*, PDF 6--8 页，Lemma 3.1 与其有界球极限证明，SHA-256 `d5c7e764dee425e8172446d0a9dacc2d657a69e8f8b46ac5b68957200a5f09cc`。[固定归档](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/paper.pdf)
- R. Berman and B. Berndtsson, *Real Monge--Ampère equations and Kähler--Ricci solitons on toric log Fano varieties*, Ann. Fac. Sci. Toulouse 22(4), 2013, Theorem 1.1。[正式版本](https://doi.org/10.5802/afst.1386)
- B. Klartag, *Logarithmically-concave moment measures I*, arXiv:1309.2767v1, PDF 8--12 页，Proposition 3.1 和 Remark 3.5。[核读版本](https://arxiv.org/pdf/1309.2767)
- D. Cordero-Erausquin and B. Klartag, *Moment measures*, J. Funct. Anal. 268(12), 2015, Theorem 2。[正式版本](https://doi.org/10.1016/j.jfa.2015.04.001)
