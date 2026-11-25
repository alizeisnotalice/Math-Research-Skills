# 有限测试空间与奇异边界

## 验证双向包含

对每个参数 \(y\) 自行选择的 Gram 因子 \(B(y)\) 可以给出逐参数的 PSD 判别。要成为原坐标的 LMI，单个固定矩阵铅笔须对原坐标仿射。要成为精确提升，则需给出固定有限维矩阵铅笔及辅助变量，使投影等于目标集合。

一种可复用构造是从参数化铅笔 \(L_\theta\) 和有限测试函数 \(f_a\) 出发，引入线性泛函 \(\lambda\)。把全部 \(f_af_b(L_\theta)_{ij}\) 与输出坐标函数纳入同一有限维函数空间。测试矩阵的条目是 \(H(\lambda)_{(i,a),(j,b)}=\lambda(f_af_b(L_\theta)_{ij})\)。\(H(\lambda)\succeq0\) 等价于对每个 \(q\in\operatorname{span}(f_a)^m\) 有 \(\lambda(q^\top L_\theta q)\ge0\)。

1. 正向从目标点找到参数化 PSD 铅笔的见证。用该点上的求值泛函满足矩阵约束及输出方程。
2. 反向对任意可行泛函构造测试向量，把测试的配对值**恒等地**化为输出坐标的不等式。记录每个测试的次数上界，保证向量在所宣称的测试空间里。只知道测试矩阵 PSD 时，尚无表示测度或参数求值可用。
3. 核对推出的条件在全部边界上足以恢复原判别，包括核空间和极限。用具体见证完成双向包含后，才统计独立的辅助变量数及矩阵尺寸。

## 用核测试覆盖奇异块

给定 \(X\succeq0\)、矩阵 \(B_j\) 以及对称 \(Z\)，以 \(X\) 为各主对角块、以 \(B_j\) 为各交叉块的箭头形矩阵 PSD，当且仅当
\[
\operatorname{ran}B_j\subseteq\operatorname{ran}X\quad(\forall j),\qquad
Z-\sum_j B_j^\top X^\dagger B_j\succeq0.
\]
必要性来自沿 \(\ker X\) 对交叉项作任意实倍数测试。范围条件成立时 \(XX^\dagger B_j=B_j\)，配方把二次型拆为若干 \(X\) 的二次型和一个广义 Schur 补。

若有限测试推导了对所有 \(u\) 及对称 \(D\) 的
\[
u^\top\left[ Z+\sum_j B_j^\top(DXD-2D)B_j\right]u\ge0,
\]
取 \(D=t vv^\top\)、\(v\in\ker X\) 并允许任意 \(t\in\mathbb R\)。系数 \(-2\sum_j(v^\top B_j u)^2\) 必须为零，由此恢复每个 \(B_j\) 的值域条件。代入 \(D=X^\dagger\)，得到广义 Schur 补。这个步骤在 \(X\) 奇异时仍成立。

本机 SymPy 1.14.0 精确检查了 \(X=\operatorname{diag}(2,0)\) 的 25 个有理边界和内部实例。负向案例 \(B=(3,b)^\top\) 的核测试有系数 \(-2b^2\)，相应二阶主子式为 \(-b^2\)。只算伪逆时看不到 \(b\) 分量。

同族手稿中的 23 变量例子展示了原坐标的表示障碍和精确提升可以同时成立。其精确提升用 \(100\times100\) PSD 矩阵及 307 个辅助变量。第三篇中的高维无提升构造使用另一个锥；这里使用其逐参数 Gram 判别与广义 Schur 补，主定理所需的种子证书和解析构造另作审计。

## 原文定位

- PDF 2、8–9 页，Theorem 1.1 与正定切片上的缩放和 Schur 补。 SHA-256：c0522a9b099318b2b79a90219749b18e1f917b4c0c0c5337e420640d1989dddf。[A nonspectrahedral hyperbolicity cone](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026/nonspectrahedral-hyperbolicity-cone.pdf)
- PDF 5–9 页，Lemma 3.1、Proposition 4.1 及 (23)–(25)。 SHA-256：6b16fbcc207da5cceeb0aa1160ab8706a482340a7af3c46a38071c2cc76b3e75。[An Exact Semidefinite Lift of a Nonspectrahedral Hyperbolicity Cone](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026/Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone.pdf)
- PDF 3–5 页，Propositions 2.1–2.2。 SHA-256：48c3a89da2a380d18a71abf7d31ce49cc3488675607de304fcade3a8ae457b1a。[Hyperbolicity Cones Without Semidefinite Lifts](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026/nonliftable-hyperbolicity.pdf)
