# Fourier 矩阵的等宽 Newton 分解

来自 OpenAI Family 130 的 *An explicit power saving for the exact discrete Fourier transform*，物理第 13 页 Lemma 3.2 与式 (3.1)–(3.2)。本机归档 SHA-256 670d0115ea2553e65f22167c176d2f31218d4d41726fe4e5702e2b149cad0896。[固定版本](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/main.pdf)

设 r≥1，u 在所给域中有精确乘法阶 r，F_{ik}=u^(ik)（0≤i,k<r）。定义 H₀=1，Hⱼ=∏_{s=1}^j(1−u^s)，以及 dₖ=(−1)^k u^(k(k−1)/2)。各 Hⱼ 在 0≤j<r 非零。记 T_{ik}=1/H_{i−k} 当 i≥k，否则为零。取

\[
N=\operatorname{diag}(H_i)\,T\,\operatorname{diag}(d_k),\qquad
F=N\,\operatorname{diag}(N_{kk})^{-1}N^{\mathsf T}.
\]

从系数矩阵 P 的第 k 列为 Newton 多项式 ∏_{j<k}(X−u^j) 的系数出发。P 为单位上三角，N=FP 为下三角。对称性及单位 LDU 分解的唯一性给出公式。右侧是转置，使用复数时不能替换成共轭转置。r=1 时所有矩阵退化为单位元。

验证新用法时先核对根的阶、所有除法的单位条件和等宽假设。此恒等式给出对角和三角 Toeplitz 因子，通过不同算法实施时须另计标量准备、宽度与操作数。Family 130 的另一篇 *Finite tensor savings and exact Fourier circuits* §3 也用等宽分解，最终电路结论是非一致的无界子序列。两稿的复杂性结论都依赖所列的精确运算模型。把局部分解移植到有限域，不会自动移植复数算法的复杂性，更不给出单个布尔函数的 Fourier 谱维数界。[另一篇固定版本](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/main.pdf)
