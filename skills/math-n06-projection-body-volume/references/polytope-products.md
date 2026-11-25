# 面法向量与笛卡尔直积

令 \(P\subset\mathbb R^d\) 为满维凸多面体。对每个面 \(F\)，记其 \((d-1)\)-维面积为 \(s_F\)，外法单位向量为 \(\nu_F\)。则
\[
h_{\Pi P}(u)=\frac12\sum_Fs_F|\langle\nu_F,u\rangle|,
\qquad
\Pi P=\sum_F\left[-\frac{s_F\nu_F}{2},\frac{s_F\nu_F}{2}\right].
\]
系数 \(1/2\) 来自几乎每一条平行于 \(u\) 的穿透线有一个入射面和一个出射面。忽略低维面或与 \(u\) 平行面的投影之前，须先说明它们的 \((d-1)\)-维投影测度为零。

若 \(A\subset\mathbb R^r\)、\(B\subset\mathbb R^s\) 都是满维凸多面体，\(r,s\ge2\)，且环境空间采用正交分解 \(\mathbb R^{r+s}=\mathbb R^r\times\mathbb R^s\)，则积体的面只有两类 \(F\times B\) 与 \(A\times G\)。因此
\[
\Pi(A\times B)=(|B|\Pi A)\times(|A|\Pi B),
\qquad R_{r+s}(A\times B)=R_r(A)R_s(B).
\]
证明第二式时必须直接保留正确的归一化指数
\[
\frac{|B|^r|A|^s|\Pi A||\Pi B|}
 {(|A||B|)^{r+s-1}}
=\frac{|\Pi A|}{|A|^{r-1}}\frac{|\Pi B|}{|B|^{s-1}}.
\]
这条文献内的证明仅陈述并证明了多面体情形。它不等同于关于极投影体的公式，也不为 \(r=1\) 或 \(s=1\) 提供已审计接口。

来源为 *A product counterexample to the simplex maximum for projection-body volume*，固定归档 PDF 第 2--3 页，Lemma 2 与 Proposition 3，SHA-256 `1d2211bb8d175f40fb55554586f02538fc9f4c04ecdc9793999a6f7ec514720a`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/paper.pdf)
