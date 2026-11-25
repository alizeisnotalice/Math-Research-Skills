# 规范函数的一阶变分测度

令 \(K\subset\mathbb R^n\) 为凸体，先平移使 \(0\in\operatorname{int}K\)，再缩放使 \(|K|=\kappa_n\)。其规范函数为 \(g_K\)。在 \(g_K\) 可微的球面方向定义概率测度
\[
 \int\psi(x)\,d\eta_K(x)
=\mathbb E_\sigma\big[g_K(u)^{-n}\psi(\nabla g_K(u))\big].
\]
不可微方向构成零测集，梯度版本不影响该定义。

对每个原点对称凸体 \(M\)，一阶体积变分给出
\[
\tau_{\eta_K}(M):=\int h_M\,d\eta_K
\ge\left(\frac{|M|}{\kappa_n}\right)^{1/n}.
\]
等号当且仅当 \(K\) 是 \(M\) 的平移正倍数。取 \(M=[-y,y]\)，纤维长度的变化给出
\[
h_{\Pi K}(y)=\frac{n\kappa_n}{2}
\int|\langle x,y\rangle|\,d\eta_K(x).
\]
这里的因子 \(1/2\) 必须保留。该测度有有界支撑并张成 \(\mathbb R^n\)。

该接口来自 *Petty’s projection-volume conjecture in dimensions at least four*，固定归档 PDF 第 4--7 页 Lemma 2.1、Corollary 2.3、Proposition 2.5，SHA-256 `ce25657d3f42aebbc5c6623367c257e46ff79cde62069bebc3324daa282d98e1`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/paper.pdf)

该段证明调用 Brunn--Minkowski 不等式及其等号条件。原手稿随后用额外的谱估计、变分极小化和仿射位置推出整体下界。这里的接口只提供已定位的一阶变分和投影表示，不能单独替代那些后续步骤。
