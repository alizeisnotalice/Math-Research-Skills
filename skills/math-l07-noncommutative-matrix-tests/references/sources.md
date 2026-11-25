# Family 116 的固定来源与使用边界

所有链接固定到 `openai/math` 提交 `3344da59991ed94f9ba711217b29c1d760badfa6`。本机 inventory 中三个条目均为 `scholarly_review: pending`；页码是 PDF 的物理页。

## 特征零、无除法的单点

*One Rational Matrix Hitting Point for Noncommutative Formulas*，13 页，SHA-256 `984d0d4287bc29fc4772a2254aabafb9ee8886c56eeafeef0a746c7fc06869ed`，本机相对位置 `current/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026.pdf`，固定[原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026.pdf)。

- Theorem 1.1（p.2）声称：对 size-上界 `s`、`n` 变量的 division-free formula，在 characteristic zero 中存在统一有理 tuple，维度至多 `2ns^2`。
- Lemma 2.1（p.5–6）给出字级数线性无关；Lemma 3.1 / Proposition 3.2（p.6–8）把 formula tree 化为严格上三角的 coefficient representation 与 rational differential system。
- Theorem 4.2（p.9–10）给出消失阶界；p.10–11 的 (13)–(15) 给出本技能直接重放的截断矩阵和检测等式。该等式与 `x1*x2-x2*x1` 的 `z^3` 系数 `-1/24` 已作有理算术复算。
- Proposition 5.1（p.11–12）把同一构造延伸到给定顶点数的 acyclic path program。它不声称任意共享 circuit 的 polynomial bound。

## 正特征、无除法的单点

*Uniform Matrix Hitting Points in Every Positive Characteristic*，14 页，SHA-256 `06284554d3db1df4569dff00d12df083815bf1bafc401f9c97f4ba9cc09119fc`，本机相对位置 `current/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/uniform-matrix-hitting-points-positive-characteristic.pdf`，固定[原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/uniform-matrix-hitting-points-positive-characteristic.pdf)。

- Theorem 1.1（p.1–2）声称一台机器在 promised prime `p`、一元 `n,s` 下输出 `F_p` matrices，维度 `O(n^3s^6)`；包括 `p=2` 和系数的任意扩域。
- Theorem 4.1（p.8）是乘法移位系统的 order bound；p.11–13 以 `F[t]/(t^E)` 的 regular-at-zero 截断，将 rational-function witness 变成有限域矩阵。
- 此分支不允许把 characteristic-zero 的 (1/i) 积分矩阵直接约化模 `p`：当 `p` 整除分母时该对象无定义。必须使用该文的 shift/truncation 构造，或另给证明。

## `Q` 上有逆门的 hitting list

*Polynomial Hitting Lists for Noncommutative Rational Formulas*，25 页，SHA-256 `8f6fe5057bd59278bfb88ccf38342c09602e547f35a757b8eadc30ece76cec0e`，本机相对位置 `current/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026.pdf`，固定[原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026.pdf)。

- p.1 的 operational definitions：admissible 意味着在某个正维矩阵 tuple 有已定义求值；nonzero 是某个已定义求值非零。二者都针对原 expression，而非只针对 free-field element。
- Lemma 4.1 与 Proposition 4.2（p.13–15）把每个 subtree 化为 affine pencil；所有 inverse-node pencils 和 root augmentation 必须同时可逆，才证明原树每一逆门已定义且最终值可逆。
- Proposition 5.1 / 5.3 与 Theorem 1.1（p.16–21）声称从三参数构造并在有理网格 specialize 出 polynomial-size list。它是条件性来源结论；本技能不提供该大构造的替代实现。

## 审计程度

已独立检查特征零文的 Theorem 4.2 核心链（p.8–10）：`Z_{j+1}=q Z'_j-jq'Z_j+Z_jP` 的次数递推、Cauchy–Binet 下由 `G` 可逆保持 minor ideal、以及 Wronskian 的 distinct-order 界可推出其所用消失阶上界。此为对该局部论证的审阅，不是对三篇全文或其所有复杂度界的外部同行认证。
