# 固定维 Fourier 分离与 Ramanujan 残余因子

本页记录两个互不替代的有限或局部构件。它们不提供素数分布、零点自由
区域、Dickman 极限或任何 γ 的线性形式。

## 固定维光滑条件的 Fourier 分离

令 (b) 固定，(F\in C_c^\infty(\mathbb R^b)) 的支撑包含于一个固定有界盒。
令 (L\ge2)。假设对每个 (j\ge0)，存在只依赖于 (j) 的常数
(C_j)，使所有 (j) 阶偏导满足

\[
  \|\partial^\alpha F\|_\infty\le C_j L^{C(j+1)}
  \qquad (|\alpha|=j),
\]

其中 (C) 和盒均须先于精度目标固定。Fourier 反演将 (F) 写成坐标乘积
相位的积分。取任意 (j>b)，对 Fourier 系数作 (j) 次分部积分得到

\[
 |\widehat F(\xi)|\ \ll_j\ L^{C(j+1)}(1+|\xi|)^{-j}.
\]

因此其绝对积分为 (L^{O(1)})。若 (C'>C) 固定，在区域
(\max_i|\xi_i|>L^{C'}) 上同样的估计给出

\[
 \int_{\max_i|\xi_i|>L^{C'}} |\widehat F(\xi)|\,d\xi
 \ll_j L^{C(j+1)-C'(j-b)}.
\]

给定固定 (A>0)，在 (C') 已固定后选择足够大的 (j)，尾部为
(O_A(L^{-A}))。顺序很重要。(C') 不能随 (A) 或后续参数增长，维数
(b) 也不能增长。对于归一化的对数坐标，坐标 Fourier 相位对应乘法幂扭曲。
多个固定维切换项的绝对 Fourier 质量相乘时，只有在切换数为
(O(\log\log x)) 且每项质量是固定对数幂时，才能仍将乘积写为对数幂。
任何质数和估计都必须另行供应。

来源为 OpenAI 预印本 *Prime Predecessors with an Even Number of Prime
Factors*，PDF p. 4，Lemma 2.4。SHA-256 为
`8ee2d8f79198dd5f09c5fbf71e309a63493d1c089772499614ee58dc8575eae9`。
[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/paper.pdf)

## 通道投影后的精确残余类因子

写

\[
 c_n(h)=\sum_{r\bmod n\atop (r,n)=1}e(hr/n)
\]

为 Ramanujan 和。令 (q) 平方自由、(j\ge1)。则

\[
 \frac{1}{\varphi(jq)^2}
 \sum_{h\bmod jq\atop (h,q)=1}|c_{jq}(h)|^2
 =
 \begin{cases}
 \dfrac{j}{\varphi(j)\varphi(q)},&(j,q)=1,\\[4pt]
 0,&(j,q)>1.
 \end{cases}
\]

若 (p\mid(j,q))，则 (p^2\mid jq) 而 (p\nmid h)。由原始根筛掉
(p^{a-1}) 的和可知 (c_{p^a}(h)=0)（(a\ge2)），再以 Chinese
remainder 分解即为零。若 ((j,q)=1)，乘法性给
(c_{jq}(h)=c_j(h)c_q(h))。平方自由 (q) 的单位频率满足
(|c_q(h)|=1)，而正交性给

\[
 \sum_{h\bmod j}|c_j(h)|^2=j\varphi(j).
\]

这是对一段已经完成 channel/residue 投影后的有限和的计算。它不能把
Ramanujan 因子转换成未证明的筛法主项。若再求和于平方自由 (q)，还须独立
验证系数、绝对收敛和所需的 (j)-一致尾界。

来源为 OpenAI 预印本 *The joint Dickman law for consecutive integers*，PDF
p. 63，式 (8.12)。SHA-256 为
`e66b4e8a1fe197d3bb2c195548cd3bdd3fba8595db1356e571205a6baab43cb3`。
[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf)

## 实际有限复算

本机以整数公式

\[
 c_n(h)=\sum_{d\mid(n,h)}d\mu(n/d)
\]

精确检查了 (j\in\{1,2,4,6,9,12\}) 与平方自由
(q\in\{1,2,3,5,6,10,15\}) 的 42 个组合，全部满足上式。另检查
((m,n)=(4,9),(5,12),(7,8)) 的 252 个 (h\) 值，全部满足
(c_{mn}(h)=c_m(h)c_n(h))。这是有限算术重放，不能替代上述一般证明。
