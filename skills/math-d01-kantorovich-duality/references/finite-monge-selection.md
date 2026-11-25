# 有限胞腔 Monge 选择与 Laguerre 截距证书

本页收录两个可分别使用的有限维构件。它们来自两篇 OpenAI 预印本。两篇的整体 Coulomb 反例、Brenier 映射稳定性与一般正则性结论均不随本页采用。

## 1. 质量失配排除确定性分支选择

设 (B,H_1(B),\ldots,H_m(B)\subset\mathbb R^d) 两两不交，且每个

\[
  H_j:B\longrightarrow H_j(B)
\]

是到开像的同胚。给定 (\nu(B)=1)，定义

\[
  \mu=a\nu+b\sum_{j=1}^m(H_j)_\#\nu,
  \qquad a>b>0.
\]

若 (T_\#\mu=\mu)，则不可能同时有

\[
  T(x)\in\{H_1(x),\ldots,H_m(x)\}
  \quad\text{对 \(\nu\)-几乎处处的 }x\in B.
\]

证明只需令 (S_j=\{x\in B:T(x)=H_j(x)\})。由不交性及单射性，

\[
 \mu(S_j)=a\nu(S_j),\qquad
 \mu(H_j(S_j))=b\nu(S_j).
\]

而 (S_j\subset T^{-1}(H_j(S_j)))，测度保持给出

\[
 a\nu(S_j)\le b\nu(S_j).
\]

故每个 (S_j) 都是 \(\nu\)-零集，和“分支选择”矛盾。此证书需实际确认每个 (H_j(S_j)) 是 Borel 集。开像同胚保证这一点。仅比较整个胞腔的总质量或任意分区的质量并不能替代这个像集计算。

## 2. 分离胞腔上的图计划逼近

令 (K_0,\ldots,K_r) 为两两距离至少 (\eta>0) 的紧集。设概率边缘 (\mu) 限制到每个非空胞腔时绝对连续。若三边缘耦合 (\pi_0) 只支撑在三个**不同**胞腔的直积上，则可将每个 (K_a) 分成有限 Borel 胞腔 (A_i)，直径至多 (\delta)，并构造 Borel 图计划

\[
  \pi_\delta=(\operatorname{Id},T_2,T_3)_\#\mu
\]

使它与 (\pi_0) 在每个 (A_i\times A_j\times A_k) 上的质量相同。

具体地，写

\[
 q_{ijk}=\pi_0(A_i\times A_j\times A_k).
\]

边缘条件允许将每个源胞腔 (A_i) 分割为质量 (q_{ijk}) 的集合 (B_{ijk})。绝对连续性给出从归一化的 (\mu|_{B_{ijk}}) 到归一化 (\mu|_{A_j})、(\mu|_{A_k}) 的 Borel 推前映射。逐块粘合后，(q_{ijk}) 的三组边缘和精确验证 (T_{2\#}\mu=T_{3\#}\mu=\mu)。

对三边缘 Coulomb 成本

\[
 c(x_1,x_2,x_3)=\sum_{\ell<r}|x_\ell-x_r|^{-1},
\]

任一激活直积中的两组三元组坐标差均至多 \(\delta)，而每对点距离至少 \(\eta)。因此

\[
 |c(x)-c(y)|\le \frac{6\delta}{\eta^2},
 \qquad
 \left|\int c\,d\pi_\delta-\int c\,d\pi_0\right|
 \le \frac{6\delta}{\eta^2}.
\]

这里不通过弱收敛跨越 Coulomb 奇异性。必须先验证每个激活胞腔三元组落在三个不同的分离分量，且图计划在同一分离区域内实现。

## 3. 正质量 Laguerre 胞腔的截距选择

令 (K\subset\mathbb R^d) 是紧凸体且具有非空内部，(\rho=|K|^{-1}\mathbf 1_Kdx)。给定互异站点 (y_1,\ldots,y_N) 和截距 (c\)，定义

\[
 P_i=K\cap\bigcap_{j\ne i}
 \{x:x\mathbin\cdot(y_i-y_j)+c_i-c_j\ge0\},
 \quad M_i=\rho(P_i),\quad B_i=\int_{P_i}x\,d\rho.
\]

只在 (M_i>0) 对所有 (i) 时使用下列微分。公共面的系数为

\[
 g_{ij}=\frac{1}{|K|\,|y_i-y_j|}\int_{F_{ij}}1\,dS,
 \qquad
 b_{ij}=\frac{1}{|K|\,|y_i-y_j|}\int_{F_{ij}}x\,dS.
\]

对截距方向 (q\)，质量导数是加权图 Laplacian

\[
 (Gq)_i=DM_i[q,0]=\sum_{j\ne i}g_{ij}(q_i-q_j).
\]

正质量胞腔的正面积邻接图连通，故

\[
 q\mathbin\cdot Gq=\sum_{i<j}g_{ij}(q_i-q_j)^2,
 \qquad \ker G=\operatorname{span}\{\mathbf1\},
 \qquad \operatorname{ran}G=\{z:\sum_i z_i=0\}.
\]

于是对任何 (m_i>0)、\(\sum_i m_i=1\)，存在唯一归一化截距

\[
 M_i=m_i,\qquad \sum_i m_ic_i=0,
\]

并且它关于互异站点是 \(C^1\) 的。这个结论只提供固定质量的局部坐标。胞腔退化、质量趋零、站点碰撞或未控制 (G^{-1}) 时，都不可据此写出统一稳定常数。

固定站点时，原文还证明一条可选的矩估计

\[
 \sum_i\frac{|DB_i[q,0]|^2}{M_i}
 \le162R^2\sum_i\frac{|DM_i[q,0]|^2}{M_i}
 \quad(K\subset\{|x|\le R\}).
\]

应用该式前仍须保留全部正质量门槛。它是关于截距扰动的界，不给任意源测度、一般密度或一般 Brenier 映射的稳定性。

## 精确有限检查

在 (K=[0,1]\subset\mathbb R) 中取 (y_1=0,y_2=1)、目标质量 \((m_1,m_2)=(1/3,2/3))。归一化截距为

\[
 (c_1,c_2)=(2/9,-1/9),
\]

第一胞腔为 \([0,1/3]\)。对质量归一方向 (q=(2,-1))，有

\[
 DM[q,0]=(3,-3),\qquad DB[q,0]=(1,-1).
\]

它直接核对了图 Laplacian 公式、矩一阶公式和上述常数界的方向。此有限检查不替代任意凸体上的微分证明。

## 固定来源与边界

- OpenAI, *A counterexample to the Monge ansatz for the three-marginal Coulomb cost*，固定版本 `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`，PDF pp. 3–4, Lemma 2.1，及 pp. 9–10, Proposition 6.1/Lemma 6.2，SHA-256 `46caabb46552913329e6a1a6226ad2dc196bd231d117562d0495f19a5832ae70`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-counterexample-to-the-Monge-ansatz-for-the-three-marginal-Coulomb-cost-September-25-2026/paper.pdf)
- OpenAI, *Sharp One-Third Stability of Brenier Maps*，同一固定提交，PDF pp. 6–9, Propositions 3.1、3.2 与 Lemma 4.1，SHA-256 `e9821deea8e836aaae6ed84cfb489e3695e1d6ce36add7e14c54100d2209f184`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/article.pdf)

两文当前均为本机归档的预印本。本页采用已逐页核对且可直接重证的有限胞腔步骤，未将其全局主定理作为已独立认证结果。
