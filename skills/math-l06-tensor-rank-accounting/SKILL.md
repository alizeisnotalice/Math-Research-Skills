---
name: math-l06-tensor-rank-accounting
description: 审查矩阵乘法张量提取中的直接和形状、辅助张量秩收费、共享腿分离与固定参数容量账本。用于有明确有限秩证书的张量退化；不把熵计算或数值搜索单独当作指数证明。
---

# 张量秩账本与共享腿分离

用于从有限个三线性张量退化、限制和精确秩证书推出矩阵乘法指数界，或审查这类推导。先固定底域、`rank` 还是 `border rank`、每个输出的有向形状 \(\langle a,b,c\rangle\)、以及所有极限的顺序。不要把一个有限搜索、某一组熵参数或“已找到的输出块”写成一般指数界。

## 直接和先于指数

若在任意固定域上已经给出**精确**秩证书
\[
 R\!\left(\bigoplus_{j=1}^s\langle a,b,c\rangle\right)\le R_*,
\]
其中所有 \(s\) 个分量有相同的、未循环置换的有向三元形状，则
\[
 s(abc)^{\omega/3}\le R_*.
\]
这是将一个共同输出形状转为 \(\omega\) 约束时的默认账本。若形状、方向或变量集不相同，不得先把它们称为“相同矩阵乘法”；应保留逐项的渐近和不等式，或先给出把每个分量变成同一有向形状的限制。

对形如
\[
 T^{\otimes n}\otimes A\rightsquigarrow
 \bigoplus_{\ell=1}^{L}\langle a,b,c\rangle,
 \qquad R(T)\le r_0,\quad R(A)\le R_A,
\]
的有限构造，严格比较为
\[
 L(abc)^{\omega/3}\le r_0^nR_A.
\]
因此，为排除候选 \(\beta\)，须以同一对数单位核对
\[
 \log L-\log R_A+\frac\beta3\log(abc)>n\log r_0.
\]
辅助因子只能以它实际给出的输出重数抵消其秩收费；不能在张量恒等式中“约掉” \(A\)。若基础成本只是 border rank，改用适用的 border-rank 渐近和不等式，并单列插值/特征限制，不能直接套用本节的精确秩式。

## 共享一腿的两种分离

### 显式 Fourier 分离

设
\[
 A=\sum_{h=1}^{M} A_h,\qquad A_h\in X\otimes Y_h\otimes Z_h,
\]
其中 \(Y_h\) 两两不交，\(Z_h\) 两两不交，且原张量没有把不匹配的 \(Y_h\)、\(Z_{h'}\) 连在一起的项。若底域含有原始 \(5M\) 次单位根，则有显式退化
\[
 A^{\oplus 5M}\rightsquigarrow
 \bigoplus_{h=1}^{M}\bigl(A_h\otimes B_X(M)\bigr),
 \qquad B_X(M)=x\sum_{u=1}^{M}y_uz_u,
\]
右侧每个 \(A_h\) 使用自己的 \(X\) 副本。这个前提同时保证 \(5M\) 在域中可逆；在特征整除 \(5M\) 或缺少该单位根时不可套用。

审查该构造时，逐项检查 Fourier 相位筛选只留下
\(u-v+2(g-h)=0\pmod {5M}\)。因为其绝对值小于 \(5M\)，这是整数等式；赋予三腿权重后总权重为 \((g-h)^2\)，故最低项恰为 \(g=h,u=v\)。不要只因“两腿能读出标签”就假定第三腿已经分离。

### 群张量补齐缺失标签

若 \(U=\sum_{s=1}^{K}U_s\) 的 \(X_s\) 与 \(Y_s\) 家族分别两两不交、而 \(Z\) 变量可重叠，在本手稿的复数域设置下，可用有限阿贝尔群乘法张量 \(A_G\) 给第三腿补标签。所需的有限构造应实际给出标签点、各侧局部零化和群方程；得到的形式为
\[
 U\otimes A_G\rightsquigarrow
 \bigoplus_{s=1}^{K}\bigl(U_s\otimes\langle1,m,1\rangle\bigr).
\]
在来源的球面/仿射切片选择中，可取 \(m=K\)，并有
\(R(A_G)=|G|\)、\(\log |G|=\log K+O(\sqrt{\log K})\)。这是渐近收费估计，不是免收费：每次实际使用都记录 \(G\)、\(|G|\)、复用是否是已分离直和上的 block-diagonal 映射，以及 \(\log R(A_G)\)。

这里群张量的秩计算使用群字符分解；更换底域时须另证分解与秩。

该步骤保留原始坐标和系数，允许未解析局部指标之间相关；但这是**局部性**结论，不保证先前限制后目标纤维非零。每个被计数的完整路径仍须单独证明存活。

## 条件类型与交错容量

用多层标签时，仅在以下条件全部成立时才以条件熵记账：完整标签记录唯一确定原始分量；在先前标签固定的条件池内，下一个标签可由两条指定腿各自读取；每个指定记录在全部局部限制后存活。对有理分布，先选使所有条件计数为整数的 \(N\)，再做局部 exact-type 投影；不得投影到没有任何一腿可读取的联合类型。

异质联合提取还须把人口、正宽度和有理类型分母全部固定在 \(N\to\infty\) 之前。对各腿累加实际熵容量 \(C_X,C_Y,C_Z\)，只在
\[
 E=\min\{C_X,C_Y,C_Z\}>0
\]
且哈希、兼容性及变量删除都已证明后，才声称指数数量的独立输出。交错多批次时先固定批次数 \(K\)，后令可整除的 \(N\to\infty\)，最后才可令 \(K\) 变化；不能把一个随 \(N\) 生长的调度直接代入极限。最后的每个输出必须由精确历史计数、同一终端类型和同一物理方向给出同一 \(\langle a_N,b_N,c_N\rangle\)。

## 有限验收清单

在报告严格指数界前，保存并逐项核验：

1. 底域、根/特征条件、每个基本张量的有限秩分解，以及每次退化的三腿局部线性映射或首项权重；
2. 输出直和的三腿变量确实不交，及每个输出的有向 \((a,b,c)\)；
3. 所有辅助张量的精确秩上界、使用次数和 block-diagonal 复用理由；
4. 全部有理类型分母、\(N\) 的整除条件、正容量/正窗口与每条受控路径的非零性；
5. 若参数含对数或数值熵，以有理或定向区间算术认证严格余量，且把舍入误差加入同一秩账本；
6. 极限顺序：先固定有限构造和参数，再取 \(N\)；任何额外调度参数另行固定并最后处理。

有限数值搜索、近似熵值、或“某些变量没有冲突”的观察最多是候选证据。它们不替代上述直和、秩收费与局部可读性证明。

本机使用 \(M=2,3,4,5\) 和分别含所需单位根的有限域，对 978 组索引精确检查了相位和权重筛选。这个计算核对有限 Fourier 消去，张量变换和指数结论仍使用相应的数学条件。

对同一放置下的等值约束、价格运输、普通和、固定格式闭包、齐次分量 border 投影和双线性化，读 [谱价格的有限转移](references/spectral-price-transfers.md)。该页不建立任何 VP/VNP 分离、矩阵乘法指数或 rank–border-rank 等价。

## 来源与范围

- *Staggered extraction for exact matrix multiplication over every field*，PDF pp. 4–5（相同有向直接和的精确秩不等式），pp. 9–13、26–27（固定有理参数、正容量及极限顺序）。本机 SHA-256 `85aa655473a156ad16db5bc59190d487a55db864d1014af0610c9c1f5b08490b`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026.pdf)
- *Complex Matrix Multiplication Below 2.258 and Rectangular Bounds*，PDF pp. 10–14（辅助秩收费、群标签分离、条件类型账本）。本机 SHA-256 `97ffc7fc55cae485ec1f001a66c4ece8a293215b1ecfc8f9ec50ef4913c8e9f0`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026.pdf)
- *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*，PDF pp. 4–7（单位根 Fourier 共享腿分离及熵式）。本机 SHA-256 `9c430672ddf2a1d0d2335c55c03b0b1fdea72f5a000c586bf130c2e984f19ae6`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf)

这些来源是本地预印本；本技能迁移有限构造的条件和账本，不认证其 headline 指数、数值证书或未实际运行的随附验证程序。

## OpenAI 原稿中的方法

- [Even-spin tensor saturation](references/openai-spin-204.md)

- [Equal-or-far finite-field filter](references/openai-equal-or-far-filter.md)
