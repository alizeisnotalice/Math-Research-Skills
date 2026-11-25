# 支撑函数与直和体积积

输入是满维的原点对称凸体 \(A\subset\mathbb R^k\)、\(B\subset\mathbb R^\ell\)，\(k,\ell\ge1\)。使用互相对偶的坐标和各自维数的 Lebesgue 测度。定义 \(A^\circ=\{u:h_A(u)\le1\}\)，其中 \(h_A(u)=\sup_{x\in A}\langle x,u\rangle\)。由双极定理，\(p_A=h_{A^\circ}\)，其中 \(p_A\) 为 \(A\) 的 Minkowski 泛函。

1. \(A\oplus_\infty B=A\times B\) 的泛函是两个泛函的最大值。\(\ell_1\) 直和 \(A\oplus_1 B=\operatorname{conv}((A\times\{0\})\cup(\{0\}\times B))\) 的泛函是 \(p_A(x)+p_B(y)\)。从凸包到泛函条件用凸性。反向把两个非零坐标分别归一化，以各自泛函值为权重，余重放在原点。
2. 对 \(A\oplus_1 B\) 的两组坐标切片测试线性泛函，得到 \((A\oplus_1 B)^\circ=A^\circ\times B^\circ\)。再取极得到 \((A\times B)^\circ=A^\circ\oplus_1 B^\circ\)。对于互补但不正交的子空间，先选产品坐标，再用 \( (TA)^\circ=T^{-\top}A^\circ\) 回到原空间。体积的两项行列式因子互相抵消。
3. \(\ell_1\) 直和在 \(x\in A\) 的纤维是 \((1-p_A(x))B\)。由 \(|\{p_A\le t\}|=t^k|A|\) 计算其体积
   \[
   |A\oplus_1 B|
   = k|A||B|\int_0^1 t^{k-1}(1-t)^\ell\,dt
   = \frac{|A||B|}{\binom{k+\ell}{k}}.
   \]
   \(\ell_\infty\) 直和的体积是 \(|A||B|\)。因此对 \(P(A)=|A||A^\circ|\)，任一操作 \(*\in\{1,\infty\}\) 均满足
   \[
   P(A\oplus_* B)=\binom{k+\ell}{k}^{-1}P(A)P(B).
   \]

从一维中心区间开始，体积积为 4。递归使用两种直和，得到的每个 \(d\) 维 Hanner 体都有体积积 \(4^d/d!\)。极性在树的每个节点交换直和类型。这个递推给出候选族的精确值。全局下界和等号分类另需论证。平移会改变极性使用的原点。若输入未指定对称中心与参考原点，先核对坐标。

用 SymPy 1.14.0 展开被积多项式并逐项精确积分，核对了 \(1\le k,\ell\le8\) 的 64 组 Beta 因子和 Hanner 递推。公式的一般性来自纤维积分。

已核对 OpenAI 预印本 *The symmetric Mahler conjecture and its equality cases*（2026-09-22）PDF 5–6 页 §2、Lemmas 2.1–2.2，使用范围限于直和、极性和递归体积积。SHA-256 为 `0560a02b890de6637a1e007f2d438e8dec93575b4e12a66a6313511348ddd6a6`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf)
