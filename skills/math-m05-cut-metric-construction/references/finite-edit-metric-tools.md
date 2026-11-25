# 有限 \(\ell_1\) 平移频谱与 edit-metric 列表工具

本页把有限 \(\ell_1\) cut 表示用于两类有限对象。

- Abel 群上的**平均**平移位移
- 有限 \(\ell_1\) 度量上带重复元素列表的直方图比较

它们支持 edit-distance 构造中的分析步骤，不能单独给出字符串的全局嵌入下界或上界。

## Abel 群的平均位移

令 \(G\) 为有限 Abel 群，使用归一化 Haar 测度。对任意 \(F:G\to\ell_1\)，定义
\[
 V_F(z)=\mathbb E_x\|F(x+z)-F(x)\|_1.
\]
把有限像上的 cut 表示拉回 \(G\)，并对每个指示函数用 Parseval，可得非负权 \(H(\chi)\) 使
\[
 V_F(z)=\sum_{\chi\in\widehat G}|1-\chi(z)|^2H(\chi).
 \tag{1}
\]
该式不要求 \(F\) 单射。它只控制以 \(x\) 平均的位移，不能推出每个 \(x\) 的距离下界。

本机精确核验取 \(G=\mathbb Z/3\mathbb Z\)、\(F=\mathbf1_{\{0\}}\) 和 \(z=1\)。直接平均给出 \(V_F(1)=2/3\)。两个非平凡字符各有权 \(1/9\)，其 multiplier 都为 \(3\)，故 (1) 的右端同为 \(2/3\)。

### 素数阶直积的检测

取整数 \(b,h\ge1\)、\(P\ge1\)，令 \(G=\prod_{j=1}^bG_j\)，\(v_j\in G_j\) 的阶为两两不同的素数 \(p_j\in[P,2P]\)，并令 \(\tau=\sum_jv_j\)。对整数 \(u\) 和任意 \(H:G\to\ell_1\)，有
\[
 V_H(uv_1)\le(2P)^{2h}V_H(\tau)
 +\frac2h\sum_{j=1}^b
 \mathbb E_{a\in\mathbb Z/p_j\mathbb Z}V_H(av_j).
 \tag{2}
\]
只需在子群 \(\prod_j\langle v_j\rangle\) 的每个陪集上分别比较频率。第一坐标为零的频率对目标位移无贡献。其余频率的支持少于 \(h\) 时，互异素数使共同相位距整数至少 \((2P)^{-h}\)。频率支持至少 \(h\) 时，坐标平均的 multiplier 总和至少为 2 倍支持数，再由 \(2/h\) 系数支付目标 multiplier。先对 cut 指示函数应用此比较，再由非负权重求和。

这里必须同时保留互异素数、共同对角平移和群平均。该不等式不能用于任意周期、非 Abel 状态空间或点态 word distance。

本机以有理算术在 \(\mathbb Z/3\mathbb Z\times\mathbb Z/5\mathbb Z\) 上检查了 (2) 的 \(P=3,h=1,u=1\) 情形。取 15 个群元素的 337 个指示切样本，每个样本均满足该不等式。

## 随机 cut 分割与列表直方图

令 \(X\) 有限、\(\rho(u,v)=\|f(u)-f(v)\|_1\)，\(\alpha>0\)。从 cut 表示中，独立保留每个 cut \(A\) 的概率为 \(1-e^{-\alpha a_A}\)，按所有被保留 cuts 的成员位划分 \(X\)。得到有限支撑的随机分割 \(\pi\)，且
\[
 \Pr[\pi(u)=\pi(v)]=e^{-\alpha\rho(u,v)}.
 \tag{3}
\]
对含重复项的等长列表 \(L,L'\)，令 \(H_\pi L\) 为各分割块的出现次数向量。按分割概率取有限 \(\ell_1\) 直和，得到确定映射 \(H_\alpha\)，满足
\[
 \|H_\alpha(L)-H_\alpha(L')\|_1
 =\mathbb E_\pi\|H_\pi L-H_\pi L'\|_1.
 \tag{4}
\]
如果所有跨列表元素的 \(\rho\) 距离至少为 \(a\)，每个列表长度为 \(s\)，则
\[
 \|H_\alpha(L)-H_\alpha(L')\|_1
 \ge2s(1-s^2e^{-\alpha a}).
 \tag{5}
\]
如果存在配对，且两侧各有 \(t\) 个未配对项，则
\[
 \|H_\alpha(L)-H_\alpha(L')\|_1
 \le2t+2\alpha\sum_{(u,v)\text{ paired}}\rho(u,v).
 \tag{6}
\]
式 (5) 的事件是没有跨列表元素落在同一分割块。式 (6) 对每个配对使用 \(1-e^{-r}\le r\)。列表的重复出现必须按出现次数计数。

## 有序标签行的 LCS 放大

两串均由 \(T\) 行组成，每行依次包含 \(m\ge2\) 个长度 \(B\) 的块，且第 \(i\) 个块的字母只在 \(\Gamma_i\) 中，\(\Gamma_i\) 两两不交。若每个不分裂源行至少有 \(d\) 个未匹配源位置，令 \(g=(m-1)B\)，则任一递增匹配的共同未匹配数 \(E\) 满足
\[
 E\ge \frac{Tdg}{d+g}\ge\frac T2\min(d,g).
 \tag{7}
\]
一个分裂行的两个连续匹配若进入不同目标行，标签顺序强制它们之间至少有 \(g\) 个未匹配目标位置。不同分裂源行得到的不匹配区间互不重叠。将分裂行数由 \(E/g\) 控制，再与不分裂行的源侧缺口相加即得 (7)。

等长行、相同块顺序和两两不交标签是该结论的输入，不可从通常的 LCS 或 edit distance 定义省略。

## 原文定位与状态

- OpenAI，*Edit Distance in \(\ell_1\): Matching Bounds up to Constants in the Exponent*，PDF 3--6 页，Lemma 2.1、Proposition 2.2、Lemmas 2.3--2.4。SHA-256 `c554cfee6ede3e18215a79cd4de7fb89a8aad26f8255c0ea72b9ed1aaef302b3`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/paper.pdf)
- OpenAI，*Finite-Circle Obstructions, Binary Codes, and Histogram Embeddings for Edit Distance*，PDF 4--5、27 页，Lemma 2.2、Lemmas 8.5--8.6。SHA-256 `8b30fa34409155e66c2d653aa31e61eacb441f91124caeee4c8d64dc528e70c8`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/paper.pdf)
- OpenAI，*Tree Constructions for the \(\ell_1\) Distortion of Binary Edit Distance*，PDF 5--6、10、16--17 页，Lemmas 2.1--2.2、3.4、5.2。SHA-256 `696bf7848724daa24c77dbb61626c434d129a6b74dca595585f4204657c22cae`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/paper.pdf)

三篇的二进制 edit-distance 指数级失真主定理还使用各自的递归构造、算术分支和参数闭合。这里没有把这些全局定理或其常数作为可直接调用的结论。
