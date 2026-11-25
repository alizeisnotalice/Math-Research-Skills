# 来源、作者声明及形式化边界

OpenAI 钉在公开提交 3344da59991ed94f9ba711217b29c1d760badfa6。以下为官方逐族形式化说明并链接原论文；本技能未重跑整套 Lean，不能将子结果写成全文形式化或已独立复核。

- [OpenAI 192：Gopalan–Servedio 反例](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/docs/192.md)：一级有符号（以及绝对值）Walsh 系数和除以实次数平方根可无界；不是 A28。
- [OpenAI 119：Courtade–Kumar / Hellinger](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/docs/119.md)：均匀布尔立方体的独立对称位噪声下二元信息收缩；不是连续状态依赖噪声。
- [OpenAI 238：Thorp 洗牌及配套论文](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/docs/238.md)：全排列 TV、真实外路径律下的平均条件估计，不是逐环境。
- [OpenAI 379：7 篇主稿及 Lean 范围](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/docs/379.md)：用明确形式化范围内固定 r 的 \(C_r^k\) 向日葵阈值；更强显式 r 依赖未列作形式化。
- [OpenAI 130：精确有限 DFT](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/docs/130.md)：其算法模型不是单个布尔函数的谱支撑。
- [Anthropic：Fermat 形式化，2026-09-04](https://www.anthropic.com/research/formalizing-fermats-last-theorem)：Prove2Me 组织依赖，用 Lean 核验，Comparator 比对最终声明与 Mathlib 的 FLT 声明；迁移证明验收流程，不迁移 FLT 定理。

- [Anthropic 公开固定提交：Critical continuity of bond percolation](https://github.com/anthropics/formal-math/blob/795efb86f191735c5481675763537cfb4ff37e55/percolation/README.md)，[原说明 PDF](https://github.com/anthropics/formal-math/blob/795efb86f191735c5481675763537cfb4ff37e55/percolation/summary.pdf)：README 陈述有限 Bernoulli 加权图的条件协方差层级及加性拼接，通过 Kozma–Nitzan 的单独归约到 \(\mathbb Z^d\) 临界键渗流。文件只按固定提交引用，未确认 main 缺失原因、外部审查或本机 Lean 重跑；仅借鉴有限引理到渐近桥的组织方法。

## 2026-11-25 项目基线（开工前刷新）
- [固定二叉 DR R4](https://github.com/alizeisnotalice/Math-Research-2/blob/main/critical-binary-derrida-retaux/rounds/004.md)、[R5](https://github.com/alizeisnotalice/Math-Research-2/blob/main/critical-binary-derrida-retaux/rounds/005.md)。
- [连续 Cantelli R208](https://github.com/alizeisnotalice/Math-Research-2/blob/main/continuous-cantelli/rounds/208.md)。
- [自由边界双峰 R54](https://github.com/alizeisnotalice/Math-Research-2/blob/main/free-boundary-grid-twin-peaks/rounds/054.md)。
- [不公平多项式 R68](https://github.com/alizeisnotalice/Math-Research-2/blob/main/unfair-01-polynomials/rounds/068.md)。
- A28 R76 实读于本地 codex/a28-fourier-sparsity，提交 bf3d43ee18fe2ba2f3feb864cd285d116a2119d7，路径 fourier-sparsity-dimension/rounds/076.md；提交号及已读证明不等价于公开推送。
