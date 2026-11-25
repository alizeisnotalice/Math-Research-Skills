# 设施质量拆分与阈值预算

## 保持 LP 质量的设施拆分

给定度量设施、开设变量 \(y_i\) 和分配变量 \(0\le x_{ij}\le y_i\)，每客户要求 \(\sum_i x_{ij}=1\)。把每个 \(i\) 表示成长度 \(y_i\) 的区间，并令客户分配是其初段 \([0,x_{ij})\)。在所有端点处分割，得到至多 \(|J|+1\) 个正质量片。原约束和费用原样转移。输出为整数开设时，合并同一原设施的片不增加开设数，也不改变距离。

给客户定义 \(V_j=\sum_i x_{ij}d(i,j)\)。按非降 \(V_j\) 选剩余客户为代表 \(s\)，吸收满足 \(d(s,j)\le M V_j\) 的客户。两代表间距离 \(>M\max(V_s,V_t)\)。令 \(L_s\) 为最近其它代表距离，\(\delta<1/2\)，从 \(s\) 的分配片中取 \(d(i,s)\le\delta L_s\) 的包。两个包若交，三角不等式给出 \(d(s,t)\le2\delta d(s,t)\)，矛盾。包外质量 \(c_s\) 满足 \(\delta L_sc_s\le V_s\)。单代表时取所有分配，\(c_s=0\)。此步骤只设置分离与质量条件，整数开设数量和舍入费用须在后续另证。

## 选一个阈值同时控制剩余数与付款

给定 \(V_i\ge0\)、尺度 \(b>0\)、固定排除数 \(q_0\) 和额外计数 \(\ell\)，考察 \(t_j=t_0 2^{-j}\) 的 \(J\) 个阈值。令 \(m_j=q_0+\#\{i:V_i>t_jb\}\)。对每个 \(i\)，所有严格低于 \(V_i\) 的 \(t_jb\) 的和至多 \(2V_i\)，故
\[
\sum_{j=0}^{J-1}t_jb(m_j+\ell)\le 2t_0b(q_0+\ell)+2\sum_iV_i.
\]
挑其中最小预算可兑现平均界，而该阈值还满足 \(m_j\le q_0+\sum_iV_i/(t_jb)\)。与具备特定成本的代理设施对应时，代理存在、不同簇之间的互不冲突、及统一归一化都另需证明。

本机对 \(b=2,t_0=1/2,q_0=\ell=1,V=(1,3,4),J=6\) 精确得到总预算 \(283/32\)、所选最小预算 \(5/32\)。

- OpenAI 预印本 PDF 7 页，设施切片、代表与分包。SHA-256 c8176d1671beb83d3a459ff65e5c632d94364ec7e542930bf19fad0b75524d50。[The approximation threshold for metric k-median](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/main.pdf)
- OpenAI 预印本 PDF 10 页，Theorem 3.3 中的几何阈值预算。SHA-256 823fdb284a7d3c0e3089869ba2da3d394db4f19b1c2ab56477ce6ae1b232614b。[Single-exponential recovery and bounded-price strictness for metric k-median](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/paper.pdf)
