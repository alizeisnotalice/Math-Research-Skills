# 平移极体的锥 Laplace 归约与对称极体的有限条带逼近

在有限维中处理极体体积积、支撑函数包含和多面体逼近时，以下两条已复核的工具分别覆盖不同的前提。它们不能互相替换。

## 何时读取本页

读取本页的情形包括。

- 目标是 `|K| |(K-z)^∘|`，而极性中心 `z` 需要保留或最小化。
- 需要把一般凸体的极体体积积改写为正锥及其正对偶上的 Laplace 积分。
- 原点对称的凸体需要由有限条带体从外逼近，并保持极体的包含方向。

这里的两个来源均为 OpenAI 预印本。下述公式和有限维推导已按对应 PDF 页直接核对。整篇 Mahler 猜想证明、其刚性结论和 symplectic-width 结论各自还依赖同文其余部分及引用结果。

## 一般凸体的平移锥归约

令 `K ⊂ R^n` 为凸体，取任意 `z_0 ∈ int K`，并设

\[
 L=K-z_0,\qquad m=n+1,\qquad
 C=\{(y,t):t\geq0,\ y\in tL\}.
\]

本节的锥对偶为**正对偶**

\[
 D=C^*=\{w:\langle w,x\rangle\geq0\text{ for every }x\in C\},
\]

它不是通常以 `≤1` 定义的凸体极。对 `V=(0,1)` 和 `U=(0,m)`，定义

\[
 \chi_C(V)=\int_C e^{-\langle V,x\rangle}\,dx,
 \qquad
 \chi_D(U)=\int_D e^{-\langle U,w\rangle}\,dw.
\]

截面计算给出

\[
 \chi_C(V)=\int_0^\infty e^{-t}t^n|K|\,dt=n!|K|,
\]

而 `D` 在高度 `t` 的截面是 `-tL^∘`，从而

\[
 \chi_D(U)=\int_0^\infty e^{-mt}t^n|L^\circ|\,dt
 =n!m^{-m}|(K-z_0)^\circ|.
\]

所以

\[
 \chi_C(V)\chi_D(U)
 =(n!)^2m^{-m}|K|\,|(K-z_0)^\circ|.
\]

任何在归一化 `\langle U,V\rangle=m` 下证明的下界
`\chi_C(V)\chi_D(U)\geq1`，因此只推出

\[
 |K|\,|(K-z_0)^\circ|\geq \frac{m^m}{(n!)^2}.
\]

### 中心与对称性的边界

- 上述恒等式适用于每个 `z_0 ∈ int K`，没有中心对称假设。
- Santaló 点是使 `|(K-z)^∘|` 最小的特定内点。选择它需要单独的存在性和唯一性论证，不能由锥恒等式本身推出。
- 如果已知 `K=-K`，可以取 `z_0=0`。这只是一个特例，不能反过来把一般凸体改写为原点对称问题。
- 仿射变换的坐标改写为 `(C,D,U,V)\mapsto(BC,B^{-T}D,BU,B^{-T}V)`。两个积分的雅可比因子互相抵消。

### 有理有限检查

取 `n=1`、`K=[0,1]` 和 `z_0=1/3`。则

\[
 L=[-1/3,2/3],\quad L^\circ=[-3,3/2],\quad
 |K|\,|L^\circ|=9/2.
\]

这里 `m=2`，故 `\chi_C(V)=1`、`\chi_D(U)=2^{-2}(9/2)=9/8`，与
`(1!)^2 2^{-2}(9/2)=9/8` 完全一致。若改取该区间的 Santaló 点 `z_0=1/2`，极体长度为 `4`，显示平移选择确实改变体积积。

来源为 [The Mahler Conjecture for General Convex Bodies, Lemma 2.1, p. 6](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/paper.pdf)，版本 2026-09-22，PDF SHA-256 `f2d35982e2e7dfe55474092a7db4c558419fb892b412bf122b20d43b51229eff`。

## 原点对称极体的有限条带逼近

令 `K=-K ⊂ R^n` 为凸体，`\alpha>0`，`\lambda=1+\alpha`。以下构造只在这个对称前提下使用。由 `0\in\operatorname{int}K`，`K^∘` 是紧的原点对称凸体。令

\[
 \rho=\min_{|v|=1}h_{K^\circ}(v)>0.
\]

取 `d\leq \alpha\rho/(1+\alpha)`，在 `K^∘` 中取有限 `d`-网 `b_1,\ldots,b_m`，设

\[
 P=\operatorname{conv}\{\pm b_1,\ldots,\pm b_m\},
 \qquad K'=P^\circ
 =\{x:|\langle b_j,x\rangle|\leq1\ (1\leq j\leq m)\}.
\]

对每个单位向量 `v`，网逼近支撑点给出

\[
 h_P(v)\geq h_{K^\circ}(v)-d
 \geq \lambda^{-1}h_{K^\circ}(v).
\]

以支撑函数刻画包含关系并取极，得到保方向的结论

\[
 K\subset K'\subset(1+\alpha)K,
 \qquad (K')^\circ=P\subset K^\circ.
\]

`P\subset K^∘` 的方向不应倒置。它表示外逼近的条带体 `K'` 具有内逼近的极体。若以数值网格实现，必须另行给出覆盖半径 `d` 的证书，抽样支撑函数值不能代替全方向包含。

### 有理有限检查

在 `R^2` 取 `K=[-1,1]^2`，令 `b_1=e_1,b_2=e_2`。则

\[
 P=\operatorname{conv}\{\pm e_1,\pm e_2\}=K^\circ,
 \qquad K'=\{x:|x_1|\leq1,\ |x_2|\leq1\}=K.
\]

因此对每个 `\alpha>0`，精确地有 `K\subset K'\subset(1+\alpha)K` 与 `(K')^∘=K^∘`。此检查同时固定了“条带交的极等于法向量凸包”的方向。

来源为 [Symplectic Balls in Symmetric Polar Products, Lemma 5.1, pp. 15–16](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/paper.pdf)，版本 2026-09-22，PDF SHA-256 `643930d71faeb8ba5aa5cda35465d20697f2955dce9a91ff729fb3ebd90c76ee`。

## 调用检查单

1. 先记录使用的是一般凸体的平移极，还是原点对称极。两者的中心和假设不同。
2. 使用锥归约时，写出 `z_0`、正对偶符号和 `U,V` 的归一化。
3. 使用有限条带逼近时，给出有限网的覆盖半径或等价的全方向支撑函数证书。
4. 取极后重查包含方向，并把严格内点条件与闭凸体条件分开记录。
