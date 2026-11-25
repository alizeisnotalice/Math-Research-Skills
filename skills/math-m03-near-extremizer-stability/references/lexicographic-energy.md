# 依次最大化与均方估计

给定非空紧集 \(K\subset[0,M]^2\) 和可测随机对 \((s_j,t_j)\in K\)。概率空间可以随 \(j\) 变化，\(K\) 固定。令
\[
A=\max_{(s,t)\in K}s,\qquad B=\max\{t:(A,t)\in K\}.
\]
对每个 \(\varepsilon>0\)，存在 \(\delta>0\) 使 \(s>A-\delta\) 时有 \(t\le B+\varepsilon\)。否则存在第一坐标趋于 \(A\)、第二坐标下界为 \(B+\varepsilon\) 的点列。紧性给出与 \(B\) 定义矛盾的极限点。用 Markov 不等式计量其余事件，得到
\[
\mathbb E t_j\le B+\varepsilon+\frac{M}{\delta}\mathbb E(A-s_j).
\]
所以 \(\mathbb E(A-s_j)\to0\) 时 \(\limsup_j\mathbb E t_j\le B\)。没有 \(K\) 的定量描述时，\(\delta\) 可依赖 \(\varepsilon\)，此结论给定性控制。

若 \(t_j=\|G_j\|^2\)，另有参考向量 \(a_j\) 满足 \(\|a_j\|^2\to B\) 且 \(\|\mathbb EG_j-a_j\|\to0\)，则利用
\[
\mathbb E\|G_j-a_j\|^2
=\mathbb E t_j-\|a_j\|^2-2\langle a_j,\mathbb E G_j-a_j\rangle
\]
得到均方差趋于零。只控制坐标能量时，向量可能在同一球面上改变方向。若每轮分别取紧集，还要额外验证上面的 \(\delta\) 能统一选取。

本机 Python Fraction 对 \(K=\{(3,1),(2,9),(0,3),(3,2)\}\)、\(\varepsilon=1/2,\ \delta=1,\ M=9\) 检查了 165 个分母为 8 的离散概率向量，全部满足上界。

手稿把 \(K\) 取为全部 Lipschitz 片的两列导数平方范数的公共闭包，并另用线段端点和尺度界控制向量均值。这两步在应用中需要单独证实。此条目覆盖紧性引理和均方转换。

## 原文定位

- PDF 5–8 页，Lemma 3、式 (6) 和 Proposition 4 的应用范围。 SHA-256：9c9b7e794d3a66305eda83409e40ca56eed2c09eb687c6abd5ec367f6e980b15。[A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/main.pdf)
