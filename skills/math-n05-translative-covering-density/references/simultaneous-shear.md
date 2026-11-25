# 同步剪切与严格补全

当有限个纵向选择模式必须共用一个水平格点阵时，本页给出两个可复用接口。它们服务于单格点阵覆盖的构造，不替代对截面体积、孔洞比例或模式生成机制的证明。

## 同步剪切接口

令 `T = R^m / Lambda_h` 是同一个满秩格点阵给出的环面，所有测度均为**归一化 Haar 测度**。对每个标签 `a`，设可测孔洞集 `U_a subset T` 满足

`|U_a| <= eta_a`，其中 `eta_a > 0`。

`R^q` 中的带标签有限模式称为“按后缀二元”，如果固定任意后缀坐标后，下一个坐标至多有两个可能值，且有两个值时它们恰好相差 `1`。每个模式点对应一个固定标签。设 `P_q` 是 `R^q` 中有限带标签模式的有限族，`0 <= q <= D`，并假设它们对取最后坐标切片封闭。令

`Q = sum_{q=0}^D |P_q|`，并取 `L_* > max(1,Q)`。

则存在实向量 `Z_1,...,Z_D in R^m`，使任意 `P in P_q` 都有

`| intersection_{ell in P} (U_{a(ell)} + pi_Lambda_h(sum_{j=1}^q ell[j] Z_j)) |
 <= L_*^(|P|-1) product_{ell in P} eta_{a(ell)}`。

这里标量 `ell[j] Z_j` 先在 `R^m` 中相乘，再投影到 `T`。因此模式节点及其分支基点无需取整数，真正需要的是两个兄弟值之差为 `1`。同一组 `Z_j` 对所有模式共同有效。

### 证明核对

按 `q` 归纳。末坐标只有一个值时，最后坐标切片属于 `P_{q-1}`，公共平移不改变测度。若两个末值为 `v` 与 `v+1`，前 `q-1` 步得到的两个交集记为 `A,B`，对应切片大小为 `k_1,k_2`。将 `Z_q` 在 `Lambda_h` 的一个基本平行体中均匀抽取。平移不变性给出

`|(A + pi(v Z_q)) intersection (B + pi((v+1) Z_q))|
 = |A intersection (B + pi(Z_q))|`。

Fubini 给出其期望为 `|A||B|`。归纳假设将此上界为

`L_*^(k_1+k_2-2) product_{ell in P} eta_{a(ell)}`。

以所需右端 `L_*^(k_1+k_2-1) product eta` 为阈值，Markov 不等式使该模式失败概率至多 `1/L_*`。对 `P_q` 并集界后仍小于 1，故可固定一个同时适用的 `Z_q`。切片封闭性、同一水平环面和兄弟间距 1 是此归纳的必要输入。

本接口不适用于无限模式族、随模式改变的水平环面、无界或未量化的孔洞集，或同一后缀下有三个以上不同的下一坐标值。

## 从孔洞比例到精确覆盖

设 `K subset R^n` 是凸体，`Gamma` 为满秩格点阵，及

`delta = 1 - |pi_Gamma(K)|`。

若存在正整数 `k` 满足严格不等式

`delta < (1-delta) k^(-n)`，

则

`(1 + 1/k) K + Gamma = R^n`。

证明中，`x -> kx` 在 `R^n / Gamma` 上的原像计数给出

`|pi_Gamma(K/k)| >= k^(-n) (1-delta) > delta`。

于是 `pi_Gamma(K)` 与每个集合 `x - pi_Gamma(K/k)` 相交，故两者的 Minkowski 和覆盖整个环面。凸性提供

`K + K/k = (1+1/k)K`。

此处不要求中心对称，也不要求 `0 in K`。使用此判据时保留严格不等式。很小的正孔洞比例仍允许未覆盖点。

## 本机核验与来源

本页逐页核对 OpenAI 预印本 *A single-lattice covering bound of order n log n*，2026-09-23，PDF 第 18--20 页，Lemma 6.1 与 Lemma 6.2。固定归档 SHA-256 为 `c7dc74641f89bce3f456410280429a47b3e214365a9467b494e14ee6b2348cbb`。官方固定版本为 [openai/math commit 3344da59991ed94f9ba711217b29c1d760badfa6 的 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/paper.pdf)。

作为有限环面算术检查，使用本机 Python 穷举 `Z/11Z` 上 `|A|=4`、`|B|=3` 的全部 11 个平移。未归一化交集基数的平均为 `12/11`，精确等于 `|A||B|/11`，等价地归一化平均为 `(4/11)(3/11)`。以期望的四倍为阈值时无失败平移，Markov 上界为 `1/4`。该计算只核对剪切证明中的 Fubini 恒等式的有限模型，不能替代连续环面的证明或本页之外的覆盖密度结论。
