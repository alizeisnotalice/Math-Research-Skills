# 有限 Ising 轮廓与私有比特树实现

这个参考页提供两个有限体积、可逐项检验的表示步骤。它们不产生临界点、尺度极限、FKG、任意边界单调性或 SLE 结论。

## 两端点轮廓的完成与自旋

令 (V\subset\mathbb Z^2) 的方块并集是 Jordan 域闭包。取两个不同的双对偶边界顶点 (f_{\rm in},f_{\rm out})，并为它们各选一条域外 stub。令 (E_V) 是所有与至少一个 (V) 中顶点相交的原始键所穿过的 dual 边。允许的内部边集满足
\[
 d_f(P)+\mathbf 1_{f=f_{\rm in}}+\mathbf 1_{f=f_{\rm out}}
 \equiv0\pmod2.
\]
还必须预先给定一组确定的域外 completion (P^\circ\)，它包含两条 stub，在两个标记处为奇度而在其余位置为偶度。

于是 (P\cup P^\circ) 处处为偶度。任意从一个 primal 顶点到无穷远的路径与它的交数的奇偶性定义一个自旋，取无穷远处为 (+1)。偶度保证定义与路径无关。限制回 (E_V) 给出与 completion 所决定边界自旋相容的自旋配置的双射。若 dual 边 (e) 穿过原始键 (e^\bullet)，则
\[
 \sigma_x\sigma_y=-1 \quad\Longleftrightarrow\quad e\in P.
\]
因此，在固定环境和 \(\beta\) 下，轮廓边际权重为
\[
 \mu(P)\propto \exp\!\left(-2\beta\sum_{e\in P}J_{e^\bullet}\right).
\]
completion 只改变恒定的外部能量和边界自旋的构造，归一化后的这个 (P) 权重不含 (P^\circ)。要从边集取单条接口，必须另选局部的四价边配对规则，且将其记录为输入，不能从奇偶条件推出唯一曲线。

来源为 OpenAI 预印本 *Quenched SLE\(_3\) Universality for the Weak Random-Bond Ising Model*，PDF pp. 3--4，式 (1.4)--(1.5) 和 Lemma 1.1。SHA-256 为 `dbf1578546653fc59b7ad8779a385741f0367c68f4147dc25e8ed251440fcb53`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Quenched-SLE3-Universality-for-the-Weak-Random-Bond-Ising-Model-October-5-2026/quenched-sle3-weak-random-bond-ising.pdf)

该页不采用同文后续的 quenched SLE 结论。它需要尺度流、交叉估计和临界点识别等额外输入。

## 私有中心比特实现树因子

设 (T) 是一棵有限连通树，(t\in\{-1,+1\}^{V(T)}) 是一个指定物理自旋图样。对每一条树边 (e=uv)，分配两枚只被这棵树使用的比特，并令
\[
 D_e=b_{e,1}-b_{e,2},\qquad
 \mathbb E[D_e\mid\sigma]=0,
 \qquad q_e(\sigma_u,\sigma_v)=\mathbb E[D_e^2\mid\sigma]>0.
\]
给每个顶点乘上
\[
 1+c_{v,t}\mathbf1_{\{\sigma_v=t_v\}}
     \prod_{e\ni v}D_e.
\]
在给定物理自旋后对这些私有比特求和。展开式中，如果所选顶点集是非空真子集，树的连通性给出一条恰有一个端点被选中的边。该边的未配对中心变量迫使该项期望为零。因而只有空集和全树保留，得到
\[
 1+\mathbf1_{\{\sigma_{V(T)}=t\}}
      \prod_{v\in V(T)}c_{v,t}
      \prod_{uv\in E(T)}q_{uv}(t_u,t_v).
\]
对于近于一的正目标因子 (F)，逐个自旋图样设置
\(\varepsilon_t=F(t)-1\)，并选择系数使上式的乘积等于
\(\varepsilon_t\)。每个图样必须用不重叠的私有比特。有限局部表与有限树的翻译轨道数使得能先选足够多的 bit channels，再在系数足够小时保持所有修正因子严格正。

这只实现输入的有限正局部树因子。使用它比较两套 pinned/free 边界时，原文的有序耦合只允许每个相邻 incidence 属于
\[
 (\mathrm{free},+),\qquad(-,\mathrm{free}),\qquad(-,+).
\]
两个同号 pin 的比较没有被这条论证覆盖。也不能从这个局部实现推出任意 pinned 自旋的 FKG 性。

来源为 OpenAI 预印本 *SLE\(_3\) Universality for Weak Finite-Range Ising Interactions*，PDF pp. 55--58，Propositions 6.1 和 6.3。SHA-256 为 `44a7837e35328259a54a4c68311ad7f015175eed48681a8b1786d9cc00bc092c`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/SLE3-universality-for-weak-finite-range-Ising-interactions-September-23-2026/paper.pdf)

## 实际有限回放

本轮用有理数穷举了一条边的树。取未耦合私有比特和
\(c_u=c_v=1/4\)，则 \(\mathbb E D_e^2=2\)。指定自旋图样的比特求和因子为
\(1+(1/4)^2\cdot2=9/8\)，其余三个图样的因子均为 1；四个 bit 配置上的每个局部修正因子均严格为正。还检查了两边的内部路径和 completion 形成的四边循环，各顶点 completed degree 都为 2。这些有限检查复现中心抵消和奇偶完成，不能认证任何无限体积或尺度极限陈述。
