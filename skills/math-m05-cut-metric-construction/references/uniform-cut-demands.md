# 单位需求割与保留小质量

## 从平均度量约束到割容量

在 \(n\ge2\) 个点上给定满足三角不等式的平方 Hilbert 距离 \(d\)，允许不同顶点间距离为零。假设平均有序对距离至少 \(a>0\)，而每个逐对受 \(d\) 支配的有限维 \(\ell_1\) 距离平均值至多 \(b>0\)。给每个非平凡割 \(S\) 一个非负变量 \(t_S\)，最大化 \(\sum_S |S|(n-|S|)t_S\)，约束 \(\sum_S t_S\delta_S(i,j)\le d(i,j)\) 对 \(i<j\)。可行 \(t\) 直接给出 \(\ell_1\) 距离，平均假设给目标至多 \(n^2b/2\)。每个 \(t_S\) 被某个跨割 \(d(i,j)\) 界住，最优值可达。

对偶给非负容量 \(c_{ij}\)，每个割的容量至少 \(|S|(n-|S|)\)，并且 \(\sum_{i<j}c_{ij}d(i,j)\le n^2b/2\)。单位需求的割比因此至少 1。用总无序对距离 \(D=\sum_{i<j}d(i,j)\ge n^2a/2\) 归一化，平方 Hilbert 距离 \(d/D\) 满足 Goemans–Linial SDP 的单位需求归一化，目标至多 \(b/a\)。正容量边形成连通图，因为每个非平凡割容量为正。任选其生成树并应用三角不等式，得到 SDP 值为正。有限 LP 可能含指数多个割变量。

要把概率标记 \(w_v\) 换为均匀副本，可对每个 \(v\) 保留 \(1+\lfloor Mw_v\rfloor\) 个副本，赋予同标记副本距离零。推前的均匀律与 \(w\) 的全变差至多 \(|V|/M\)，乘积律偏差至多 \(2|V|/M\)。即使 \(w_v=0\)，仍保留它对逐对收缩的约束。控制有界配对期望时须乘函数的振幅。

## 低容量割与辅助顶点

设原需求概率为 \(\mu\)，有可复制的概率 \(\widehat\mu\le2\mu\)。取副本权 \(w_i\)，对正质量键有 \(w_i\le2\widehat\mu_i\)，零质量键副本总质量 \(\alpha\le1\)。通过代表点和足够重的簇内边，确保待分析的低容量割在每个簇中取相同标签。对每个 \(\widehat\mu_i=0\) 的键到正质量键 \(j\) 加权 \(2\kappa w_i\widehat\mu_j\)。

把零质量的 \(w\)-抽样键重抽为独立的 \(\widehat\mu\) 键，标签改变的概率记为 \(L\)。加边的割代价正好 \(2\kappa L\)。重抽后的分布 \(\rho\le(2+\alpha)\widehat\mu\le6\mu\)。独立耦合两个抽样点，在重抽前后比较标签不同的事件，得
\[
z(1-z)\le36\operatorname{Var}_\mu(h)+L,\qquad z=\mathbb E_wh.
\]
若总割容量 \(T\le\kappa z(1-z)\)，则 \(2\kappa L\le T\)，代入得 \(T\le72\kappa\operatorname{Var}_\mu(h)\)。这个比较在 \(z\) 很小时仍保留量级。给定 \(T\le\kappa/4\) 的低容量分支，可用容量 \(2\kappa\) 的簇内边保证同色。对任意切割的强界仍需原始容量的 soundness 输入。

本机以 \(w=(36,4,1)/41\)、\(\mu=\widehat\mu=(9/10,1/10,0)\) 精确检查了全部 8 个二元标记。另对三点平方距离 \(d_{12}=d_{23}=1,d_{13}=2\) 检查单位容量的割与 SDP 归一化，两边对应的平均距离为 \(8/9\)。

- OpenAI 预印本 PDF 16–18 页，Lemma 6.1 与式 (6.7) 的单位需求和复制造成的全变差。SHA-256 d47a50531670a4f9c16025fcaeadd90ba1b5ecc8942999156cfcc1eb88fc902a。[Near-square-root logarithmic integrality gaps for uniform sparsest cut](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026.pdf)
- OpenAI 预印本 PDF 45–46 页，式 (125)–(129) 的支撑保持和零权键重抽；连续模型的容量分离主张另证。SHA-256 75f6af00a38589bf57470aee3c1ad3e0b2ad8c9f676e656cb5fdec311f90baf8。[Constant-factor hardness of uniform sparsest cut](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026.pdf)
