# 组内变差与熵势函数

令 \(Q\subset\Delta_d\) 非空、紧、凸，并含一个各坐标为正的向量。坐标分块，每块的 \(Q\)-质量固定。令 \(f_0,\ldots,f_S\in[0,1]^d\) 逐坐标非增，\(\Delta_t=f_{t-1}-f_t\)。给定 \(\eta>0\)、\(0<\kappa<1/2\)，每个 \(\Delta_t\) 在各块中的范围均至多 \(\kappa/\eta\)。定义
\[
\widehat g_t=-f_{t-1},\quad u_t=\widehat g_t+(1-2\kappa)\Delta_t,\quad v_{t-1}=\sum_{j<t}u_j .
\]
取 \(p_t\) 为 \(H(p)+\eta\langle v_{t-1}+\widehat g_t,p\rangle\) 在 \(Q\) 的最大者。对任意 \(p^\ast\in Q,0\le s\le S\)，有
\[
\sum_{t\le s}\langle f_t+\kappa\Delta_t,p_t\rangle
\le\sum_{t\le s}\langle f_t,p^\ast\rangle+\eta^{-1}\log d+2\kappa .
\]

设 \(\Phi(v)=\max_{Q}[H(p)+\eta\langle v,p\rangle]\)。严格凹性给唯一性。若有零坐标，向正的可行点移动小步 \(a\) 的熵增加含正的 \(a\log(1/a)\) 项，压倒线性代价，故最大者为正。由一阶条件及熵的 Bregman 恒等式，任意概率 \(p\in Q\) 的目标差至少为 \(D_{\rm KL}(p\Vert p_t)\)。

从 \(v_{t-1}\) 到 \(v_{t-1}+\widehat g_t\) 的势增量至多 \(\eta\langle\widehat g_t,p_t\rangle\)。再把 \(\Delta_t=m_t+r_t\) 分为各块的最小值 \(m_t\) 及剩余量 \(r_t\)。\(\langle m_t,p\rangle\) 对 \(p\in Q\) 固定。用 KL 惩罚放松第二增量到全概率单纯形，只需估计 \(\log\sum_i p_{t,i}e^{\eta(1-2\kappa)r_{t,i}}\)。在 \(0\le x\le\kappa\) 上，\(e^{(1-2\kappa)x}\le1+(1-\kappa)x\)，因对数右侧减 \((1-2\kappa)x\) 的导数非负。因此第二增量至多 \(\eta(1-\kappa)\langle \Delta_t,p_t\rangle\)。望远镜求和，以 \(p^\ast\) 测试末势，用 \(\sum_{t\le s}\Delta_t\le\mathbf1\) 控制 \(2\kappa\) 损失。若每次实际向量有 \(\ell_1\) 偏差 \(\zeta\)，目标增加至多 \(s\zeta\)，因每个成本坐标在 \([0,1]\)。

本机 mpmath 70 位对块质量 \((0.6,0.4)\)、四坐标三轮固定成本、\(\eta=2,\kappa=1/4\) 检查三个前缀，末轮左端约 \(1.430821598\)，右端约 \(2.335147181\)。该有限计算用块内显式 Gibbs 解，公式的一般性来自势函数证明。

- OpenAI 预印本 PDF 28–29 页，Lemma 7.2、式 (7.3)–(7.8)。SHA-256 7ecda63faaa7d6a3ff36852775a6a015a8d832ace341a534af86a375d1d89807。[An Almost-Linear Approximation Scheme for Edit Distance](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/paper.pdf)
