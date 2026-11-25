# 有限块与无限尾部逆证书

给定带有和范数的 Banach 直和 \(X=X_f\oplus X_t\)，其中 \(X_f\) 有限维，且 \(S:X\to X\) 有界。对 \( \eta\in\{-1,1\} \) 求解 \((I-\eta S)x=r\)。

1. 认证 \(V=(I-\eta S_{ff})^{-1}\) 存在，给出对其算子范数的认证上界 \(v\)。仅需近似逆时，可用有限矩阵残差与 Neumann 级数认证。
2. 认证 \(a\ge\|S_{tt}\|\)、\(b\ge\|S_{tf}\|\)、\(c\ge\|S_{ft}\|\)。设 \(q=a+bvc<1\)。消去 \(x_f=V(r_f+\eta S_{ft}x_t)\) 后有
   \[
   (I-\eta S_{tt}-S_{tf}VS_{ft})x_t=r_t+\eta S_{tf}Vr_f .
   \]
   左侧扰动在整个尾空间上范数至多 \(q\)，用 Neumann 级数得到有界逆。
3. 分块残差传递为
   \[
   \|x_t\|\le(\|r_t\|+bv\|r_f\|)/(1-q),\qquad
   \|x_f\|\le v\|r_f\|+vc\|x_t\|.
   \]
   对近似表 \(\tilde x\)，改用右侧 \(r-(I-\eta S)\tilde x\) 得误差包围。尾部的零近似系数仍可能产生非零尾残差。
4. 若原系统是 \(x_1-Sx_2=g_1,\ x_2-Sx_1=g_2\)，对和与差分别使用两次证书。总解的唯一性限于所选系数空间与已固定的额外数据。

本机 SymPy 1.14.0 对一个有理三维分块矩阵、两种符号及 27 个右端向量核对了 54 组消元解和范数界。

需要同时证明该有界算子在指定空间上原本定义的解析意义。无限尾界不能由截断表本身给出。手稿给出四块范数和近似表残差的具体证书，本文仅复核有限块消元、全尾逆的充分条件及残差传递。原文表格、区间积分及后续全域符号证书未作重跑。

## 原文定位

- PDF 13–15 页，Lemmas 3.2–3.3、Proposition 3.4。 SHA-256：3a532659c4aa989d4d9cca9d33810940b61c835597bb0b1b50c16d3487001329。[A sharp Fourier certificate for planar circle packing](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-sharp-Fourier-certificate-for-planar-circle-packing-September-23-2026/paper.pdf)
