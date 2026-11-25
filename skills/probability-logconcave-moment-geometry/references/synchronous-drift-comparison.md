# 同步漂移的 Wasserstein 比较

令 \(H,\bar H\in C^2(\mathbb R^n)\) 的 Hessian 有全局正下界和有限上界，且 \(D^2H\succeq mI\)、\(m>0\)。令 \(\mu,\bar\mu\) 为其归一化 Gibbs 概率。两条 Langevin 方程都取噪声 \(\sqrt2\,dB_t\)，并以同一 Brownian 路径驱动。从具有这两份平稳边缘的任意平方可积耦合出发，差 \(Z=X-Y\) 的平方可用强单调性及 Cauchy–Schwarz 控制：
\[
\frac{d}{dt}\mathbb E|Z|^2\le-2m\mathbb E|Z|^2
+2\sqrt{\mathbb E|Z|^2}\big(\mathbb E_{\bar\mu}|\nabla H-\nabla\bar H|^2\big)^{1/2}.
\]
先对平方根做正则化以覆盖零差，再解标量微分不等式。边缘始终平稳，令 \(t\to\infty\) 得
\[
W_2(\mu,\bar\mu)\le m^{-1}\big(\mathbb E_{\bar\mu}|\nabla H-\nabla\bar H|^2\big)^{1/2}.
\]
梯度差在第二份平稳概率下平均，强单调常数取第一势。源稿的近二次模型为 \(H(z)=|z|^2/2+F(x+rz)\)。若 \(\nabla F\) 的 Lipschitz 常数为 \(\lambda\)，可取 \(m=1-\lambda r^2>0\)，即便 \(F\) 自身非凸。

本机核验同协方差单位矩阵的两个高斯位移 \((0,0)\) 与 \((1,2)\)。平方 Wasserstein 距离和上界的平方都是 5，耦合用平移，反向界由均值的 Cauchy–Schwarz 给出。该比较独立于预印本只计精确 oracle 查询的主复杂度主张。

- OpenAI 预印本 PDF 5–6 页，Lemma 2.2、式 (2.5)。SHA-256 9e9a41553023f95e18b673f130c2086def56ba2b7a4cd851337a39eb114bf679。[Subpolynomial query complexity for well-conditioned log-concave sampling](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/article.pdf)
