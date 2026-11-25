# 固定随机位的均匀索引逼近

设 \(M\ge1\)、\(Y\) 为 \(k\ge0\) 个独立公平位表示的均匀整数，令 \(N=2^k\)。返回 \(J=\lfloor MY/N\rfloor\)。整个映射只需要一次整数乘法和除法。

令 \(N=aM+r\)，\(0\le r<M\)。把 \(Y\) 的整数域按 \([jN/M,(j+1)N/M)\) 分块，每块含 \(a\) 或 \(a+1\) 个整数。其中恰有 \(r\) 块较大。直接求和，得到
\[
d_{\mathrm{TV}}(\operatorname{Law}(J),\operatorname{Unif}\{0,\ldots,M-1\})
=\frac{r(M-r)}{NM}.
\]
因此 \(M2^{-k}\le\zeta\) 是误差不超过 \(\zeta\) 的充分条件，实际误差可用余数式计算。精确均匀恰在 \(r=0\) 时成立。多次或条件抽样时，预算须对实际调用的 \(M\) 核对，并为每次新抽样使用相应的新公平位；可用逐次耦合与并集界控制任何一次失配。

本机对 \(0\le k\le10\)、\(1\le M\le31\) 共 341 种参数完整枚举输入与桶计数，均核对余数式。此处只用有限索引近似，未采用表计数主定理。

来源为 OpenAI 预印本，PDF 33 页，Lemma 6.4。SHA-256 10bad4277d11b9d1c69842fd8e9028c67edb9ebce6092ad6332703975c8fd7e7。[An FPRAS for Cell-Bounded Contingency Tables](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/main.pdf)
