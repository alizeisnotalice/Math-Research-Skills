# 颜色固定与有限核抽样

## 用颜色细化固定一个类型映射

设 \(F=(P\sqcup Q,L)\) 是有限二部图。以两个部分作为初始颜色，令 \(\ell_t(u)\) 为第 \(t\) 轮颜色，\(h_t(u)\) 为邻点的第 \(t-1\) 轮颜色直方图。假定某一 \(R\) 后 \(\ell_R\) 在每个部分内离散。

对任一保部分映射 \(f:P\sqcup Q\to P\sqcup Q\)，第 \(t\) 轮先定义
\[
 F_t(f)=-\sum_u\lVert h_t(f(u))\rVert_2^2
 +2\sum_u\sum_{v\in N_F(u)}
 h_t(f(u))\bigl(\ell_{t-1}(f(v))\bigr).
\]
这个量由顶点分数和 \(P\times Q\) 型对分数实现。具体地，类型 \(a\) 的顶点分数取 \(-\lVert h_t(a)\rVert_2^2\)，类型对 \((a,b)\) 的分数为
\[
 2h_t(a)(\ell_{t-1}(b))+2h_t(b)(\ell_{t-1}(a)).
\]
第二项对应每条无向边的两条有向邻接项。

如果 \(f\) 保持第 \(t-1\) 轮颜色，则
\[
 F_t(\operatorname{id})-F_t(f)
 =\sum_u\lVert h_t(f(u))-h_t(u)\rVert_2^2.
\]
因此该差是非负整数，且为零恰当且仅当 \(f\) 也保持第 \(t\) 轮颜色。这里没有使用 \(f\) 的单射性或邻接保持性，故可控制有重复类型的映射。

令
\[
 M=\max_{f,\,1\le t\le R}|F_t(f)-F_t(\operatorname{id})|,
 \qquad B=M+2,
 \qquad Q(f)=\sum_{t=1}^R B^{R-t}F_t(f).
\]
任何非恒等保部分映射在其第一个失色轮次至少损失 \(B^{R-t}\)，之后各轮的最大总收益严格更小。因此 \(\operatorname{id}\) 是 \(Q\) 的唯一最大元，并与所有竞争映射有正间隙。实际使用前必须核对色细化是在两个部分内离散的，且待优化的映射族确实只允许保部分映射。

## 从有限 \([0,1]\) 核抽样简单图

设 \(H\) 是有 \(v\) 个顶点、\(e\) 条边的有限简单图，\(U\) 是有限概率空间上的对称 \([0,1]\)-值核。写
\[
 \mu=\mathbb E U(X,Y),\qquad \tau=t(H,U),\qquad
 \Delta=\mu^e-\tau>0.
\]
令 \(z_1,\ldots,z_n\) 独立按该概率空间取样。给定标签后，对每一对不同的宿主顶点 \(\{a,b\}\) 独立地以概率 \(U(z_a,z_b)\) 放边，不放自环。所得 \(G_n\) 是有限简单图，且
\[
 \mathbb E p(G_n)=(1-1/n)\mu,
 \qquad
 \left|\mathbb E t(H,G_n)-\tau\right|
 \le {\binom v2\over n}.
\]
第二式中，单射的源顶点映射恰有期望 \(\tau\)。映射中至少识别一对源顶点的比例不超过 \(\binom v2/n\)。这些非单射映射仍被 \(t(H,G_n)\) 计入。不同源映射之间不要求独立。

若
\[
 n>{\binom v2+e\mu^e\over\Delta},
\]
则 \((1-1/n)^e\ge1-e/n\) 和上式给出
\[
 \mathbb E t(H,G_n)<(\mathbb E p(G_n))^e\le\mathbb E[p(G_n)^e].
\]
最后一步是 \(x\mapsto x^e\) 的凸性。因此存在一个样本满足 \(t(H,G_n)<p(G_n)^e\)。这个结论的输入是已经证明的核缺口 \(\Delta>0\)。抽样引理本身不构造该缺口，也不证明任意二部图的密度不等式。

## 有限核回放

取 \(H=K_3\)，原子空间 \(\{0,1\}\) 取均匀测度，并令 \(U(x,y)=\mathbf1_{x\ne y}\)。则 \(\mu=1/2\)、\(\tau=0\)、\(e=3\)。对于 \(n=3\)，上述抽样的每个宿主图均是二部图，所以 \(t(K_3,G_3)=0\)，而 \(\mathbb E p(G_3)=1/3\)。逐一枚举八个标签三元组也给出 \(\mathbb E p(G_3)=1/3\)，碰撞上界为 \(\binom32/3=1\)。这是传递公式的精确小例，不是原文二部模板的反例构造。

来源为 OpenAI 预印本 *A counterexample to Sidorenko's conjecture*，PDF pp. 14、16–17，Lemmas 3.4 与 3.6。SHA-256 为 `0c0d7b5eb1ed43c00ed2f60d2347b7d5511bad2218efe12c28fd9968ee549b0f`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf)

原文的核缺口来自一个特定 35 顶点、66 边二部图以及后续有限域秩层和奇异构型估计。该长链没有由本参考页采纳。这里保留的只是色细化固定和严格有限核缺口的抽样传递。
