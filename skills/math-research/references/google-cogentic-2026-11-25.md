# Google Cogentic 数学论文蒸馏与验收

2026 年 11 月 25 日 Google Research 仓库发布六篇 Cogentic 原稿。六份本机下载件均与固定提交 `4a7bc8ab0bc7` 逐字节一致，合计 274 个 PDF 物理页。独立审阅限于下列采用的构件、适用条件和全局主张的入口依赖。目录与各篇 README 将 Lean 4 工程列为后续伴随材料，当前发布记录没有可供本次编译的项目。[固定发布提交](https://github.com/google-research/google-research/commit/4a7bc8ab0bc7)

| 本机原件 | 页数 | SHA-256 | 论文 | 相关技能 | 处理状态 |
| --- | ---: | --- | --- | --- | --- |
| 01_integer_factorization.pdf | 54 | `9ac07593ca90c0f315af0b0214320823a43e7c905e6700948261ebb09a4d537d` | Unconditional Integer Factorization in Time L_N[1/3, O(1)] | [math-l16-prime-sieve-certified-transfers](../../math-l16-prime-sieve-certified-transfers/SKILL.md) | 已采用构件 |
| 02_discrete_logarithm.pdf | 36 | `fba12f4d5e98152d52226887c4af2606039725f898bffecbc8a4d91ccaf9d0d7` | Discrete Logarithms in Finite Fields of Fixed Characteristic in Sub-Quasi-Polynomial Time | [math-l03-rational-and-interval-certificates](../../math-l03-rational-and-interval-certificates/SKILL.md) | 已采用构件 |
| 03_bimatrix_nash_equilibrium.pdf | 41 | `ed65664e8817e323a1613f95f4fc98689719c86fb2708974bb69cc1edc139485` | An Exact Polynomial-Time Algorithm for 1/5-Approximate Nash Equilibria in Bimatrix Games | [math-bimatrix-kite-mixing](../../math-bimatrix-kite-mixing/SKILL.md) | 已采用构件 |
| 04_deterministic_factoring_l34.pdf | 59 | `0ccf115516dab3cbeee15167f2dea62fcb29d03a19224cb4a9ae69a5ce402993` | Unconditional Deterministic Subexponential Integer Factoring and Quadratic Nonresidue Construction | [math-l16-prime-sieve-certified-transfers](../../math-l16-prime-sieve-certified-transfers/SKILL.md) | 已采用构件 |
| 05_logrank_conjecture.pdf | 37 | `9c941a918c5e5cea1624adee676c010efb85b60b3cd77455640cd578f54f6bc9` | Breaking the Square-Root Barrier for the Log-Rank Conjecture | [math-logrank-rectangle-rank-halving](../../math-logrank-rectangle-rank-halving/SKILL.md) | 已采用构件 |
| 06_edge_reconstruction.pdf | 47 | `170b2fc1f241cc8325e0b5573d444e061b1b7bb8fb3083a3ac88cabd0ce4f196` | Unconditional Edge Reconstruction of Simple Graphs of Linear Density | [math-edge-deck-reconstruction-audit](../../math-edge-deck-reconstruction-audit/SKILL.md) | 已采用构件 |

本机来源目录名为 `10_Google_Cogentic_2026-11-25/PDF/`。11 月 26 日与仓库主分支比较，五篇 PDF 的字节一致。双矩阵博弈更新版仍为 41 页，SHA-256 为 `32196e6a64d13fbd216c7e7353a3b44a46e8389eb3d15bad48ffb3dd926cc337`，更新了 Li–Li 的既有结果比较及出处。两版的 kite 定义、Lemma 2.3(a) 与其证明一致。[更新版论文目录](https://github.com/google-research/google-research/tree/master/cogentic_research_papers/bimatrix_nash_equilibrium)


## 第三次蒸馏与实际验收

本机的六份原件 SHA-256 和 274 个物理页已重新核对。以 Google Research 主分支解析到的固定提交 `3f540f420bfa` 重新获取原稿，五篇逐字节一致，双矩阵博弈的 41 页修订版哈希为 `32196e6a64d13fbd216c7e7353a3b44a46e8389eb3d15bad48ffb3dd926cc337`。本轮核对的 Lemma 2.2 零和原始及对偶 LP 与推导在两版一致。六份原稿的说明仍将 Lean 4 工程指向伴随发布，本轮没有取得工程进行编译。[本轮核对的固定 Google Research 目录](https://github.com/google-research/google-research/tree/3f540f420bfae7e6ce48365a68d0ae003feb2f87/cogentic_research_papers)

| 原件 | 原文定位与本轮接入 | 实际调用结果 |
| --- | --- | --- |
| 01 整数分解 | 物理页 44，Lemma 5.3。核对给定分解、平方根与掩码，按 CRT 和二元秩计算给定记录下的概率。共用隐藏根的多掩码推导另列。[Dixon 条件概率](../../math-l16-prime-sieve-certified-transfers/references/cogentic-dixon-transcript.md) | 对模数 15、45、105 枚举根集合，精确比对 180 组输入。样例三条相关掩码的秩为 2，至少一次分裂的概率为 \(3/4\)。 |
| 02 离散对数 | 物理页 30–31，Lemma 6.3(2)。在给定单位群中代回每条乘积关系、模线性消元和最终幂等式。[循环关系证书](../../math-l03-rational-and-interval-certificates/references/cogentic-cyclic-relation-certificates.md) | 模 17 得到指数 \((5,3)\)，检测了错误关系和欠定系统。 |
| 03 双矩阵博弈 | 物理页 6–7，Lemma 2.2。用两组有理零和 LP 对偶见证，得到 minimax 策略对的后悔上界。[零和安全值证书](../../math-bimatrix-kite-mixing/references/security-screen-certificate.md) | 枚举核验 256 个 \(2\times2\) 零一收益矩阵对，并拒绝了篡改的 minimax 见证。 |
| 04 确定性整数分解 | 物理页 55–57。检查给定的指数、底数和待检素因子，并认证 gcd 分裂结果。[给定指数分裂](../../math-l16-prime-sieve-certified-transfers/references/cogentic-supplied-exponent-splitting.md) | 对 \(n=91,a=2,E=12\)，\(q=2\) 给出因子 7，\(q=3\) 得到 gcd 1，合数输入 \(q=4\) 被拒绝。 |
| 05 Log-Rank | 物理页 35–36，Proposition A.3。逐节点核验给定递归的单色块、交叉块秩及完全覆盖。[协议分割树证书](../../math-logrank-rectangle-rank-halving/references/protocol-tree-certificate.md) | \(3\times3\) 样例有 3 个分割节点、5 个单色叶。非单色叶被拒绝。 |
| 06 边重构 | 物理页 10–11，Lemma 2.3。在已知原图无孤立点且 \(4\le n\le6,m\ge4\) 的有限接口中，从边卡组用三角反演恢复顶点删除卡组。[顶点卡组恢复](../../math-edge-deck-reconstruction-audit/references/vertex-deck-from-edge-deck.md) | 核对了 26 个 \(n=4,5\) 的无标号图及六环样例，并拒绝有孤立点的图输入。 |

六个构件均用本机 Python 3.13.18 执行整数或有理数回放。原稿中的全局复杂度、\(1/5\) 近似保证、统一单色矩形密度与一般线性密度边重构分别留有独立证明依赖。本机欧拉常数专题可复用整数同余或有限群证书；这批原稿没有给出 \(\gamma\) 的整数线性形式或全指标的非零与衰减界。

## 博弈、通信复杂性与图

- **双矩阵博弈的 \(1/5\) 近似。** 物理页 2–3，Theorem 1.1，原稿声称有理收益的确定性多项式时间保证。采用的是物理页 7–10 的 Lemma 2.3(a)。对已有策略，认证 kite 条件后做一次精确最佳回应混合。滤波、Volterra 不等式和全域有理代数证书构成主定理的未独立核验链。[双矩阵 kite 混合](../../math-bimatrix-kite-mixing/SKILL.md)
- **Log-Rank 的平方根屏障。** 物理页 2，Theorem 1.1，原稿声称 \(D^{cc}(M)\le 750\cdot 2^{38} r^{1/2-5\cdot10^{-6}}\)。核对了 \(2^{38}\) 的 PDF 上标。采用物理页 35–36，Proposition A.3 的单色矩形秩分裂和带统一矩形密度假设的归约。主定理关于 KL 稳定符号矩阵的结构估计与高秩矩形存在结论仍依赖 Theorem 3.1 及其证明。[单色矩形与秩减半](../../math-logrank-rectangle-rank-halving/SKILL.md)
- **线性密度图的边重构。** 物理页 1–2，Theorem 1.1，原稿声称有限简单图在 \(m\ge1000n,\ n\ge4\) 时可边重构。采用物理页 8，Lemma 2.2(1) 的 Edge–Kelly 有限子图计数，以及物理页 2 的经典小图碰撞。全局密度论证依赖物理页 46 汇合的 Propositions 6.5、7.3、8.4，仍待独立核验。[边卡组与 Edge–Kelly](../../math-edge-deck-reconstruction-audit/SKILL.md)

## 数论

| 原稿与所查范围（物理页） | 作者提出的主结论与主要依赖 | 本轮实际可调用的内容 |
| --- | --- | --- |
| *Unconditional Integer Factorization in Time* \(L_N[1/3,O(1)]\)，pp. 1–10、44–48 | Theorem 1.1 声称对任意整数 \(N\ge2\)，零错误 Las Vegas 完全分解的最坏情形期望时间为 \(L_N[1/3,105]\)，确定性工作空间为 \(L_N[1/3,40]\)。总体界依赖平滑权、下降、筛法与有效 Chebotarev 的联接。 | 保留版本与依赖。后验素数性、乘积核验只涉及已给定的输出，不能给出找到输出的时间上界。 |
| *Discrete Logarithms in Finite Fields of Fixed Characteristic in Sub-Quasi-Polynomial Time*，pp. 1–3、7、29–35 | 主定理声称固定特征下的零错误期望位复杂度为 \(\exp((2+o(1))(\ln n)^2/\ln\ln\ln n)\)。椭圆曲线下降、单值群与分裂计数进入复杂度证明。 | 提取最终的有限群见证检查。输入已经给定 \(x\) 或 \(E\)，输出精确幂等式，可在素域或一般模整数单位群上检查。 |
| *Unconditional Deterministic Subexponential Integer Factoring and Quadratic Nonresidue Construction*，pp. 1–6、22–29、55–59 | Theorems 1.1–1.3 声称一般确定性分解的 \(O(\exp(3(\ln N)^{3/4}))\) 位复杂度、给定公共指数的分裂算法和二次非剩余构造。核心依赖二次域理想、Burgess 型矩估计与相关确定性构造。 | 保留版本、素数阶整除假设与依赖。分解或非剩余搜索的全局复杂度边界仍待独立核验。 |

有限群检查由既有 L03 承载。验证 \(\,g^x=h\,\) 或 \(\,g^E=1,\ h^E\ne1\,\) 只针对已给出的见证。[有限群算术证书](../../math-l03-rational-and-interval-certificates/references/finite-subgroup-witness.md)

## 本轮有限验收

本机 Python 3.13.18 使用精确有理数或整数。三个新增技能均有正例和边界输入。各计算的复现命令在对应技能中。

- 双矩阵博弈。在 \(2\times2\) 的零一双矩阵和分母 4 的策略格点中，逐一核对了进入 \(K_{1/5}\) 的 3048 个输入，混合后双方后悔均不大于 \(1/5\)。区域外的例子报告条件未通过。
- Log-Rank。完整枚举 \(3\times3\) 的零一矩阵及其非空矩形，精确比较 10,658 个单色矩形的两块秩。非单色输入被拒绝。
- 边卡组。重标号四环仍同构且同卡组。\(2K_2\) 与 \(K_{1,2}\sqcup K_1\) 同卡组但不同构。Edge–Kelly 从四环的卡组恢复单边的 8 个有序嵌入，且在图案与宿主同边数时拒绝使用恒等式。
- 有限群。模 17 的成员见证、非成员充分证书和条件未满足的例子分别给出正确状态。指数证书条件不满足时，成员关系仍待判定。

本轮采用的局部引理与检查器均有明确输入范围。六篇原稿的整体新定理均保留为源文主张。

## 第二次蒸馏与实际验收

六份下载件的 SHA-256 和 274 个物理页已复算。Google 现行的双矩阵博弈稿使用更新后的书目信息，其余五份现行 PDF 与本机原件一致。本批沿用下载件的固定定位。[Google Research 版本目录](https://github.com/google-research/google-research/tree/master/cogentic_research_papers)

| 论文 | 本次采用的有限构件 |
| --- | --- |
| 01 整数分解 | 核对物理页 1–6 的算法接口和已给定因子列表的验证。延用素性与乘积检查，记录平滑权、下降和复杂度的依赖。[两篇算术稿复核](../../math-l16-prime-sieve-certified-transfers/references/cogentic-finite-arithmetic.md) |
| 02 离散对数 | 物理页 31 Lemma 6.3(2)。在给定的模整数关系矩阵上做精确 Bézout 消元，检查余行并代回原方程。模 12 示例认证解 \((5,3)\)，欠定和矛盾示例分别报告状态。[模整数线性关系](../../math-l03-rational-and-interval-certificates/references/modular-unimodular-relations.md) |
| 03 双矩阵博弈 | 物理页 5–6 Lemma 2.1(b)。最大余数舍入保持总质量，并给出 \(\ell^1\) 误差 \(\le d/D\)。本机用有理数枚举 8,967 个输入，包含余数并列。[单纯形舍入](../../math-bimatrix-kite-mixing/references/simplex-denominator-rounding.md) |
| 04 确定性分解 | 物理页 55 Lemma 11.1。对已认证的有限子群指数界，核查素域群阶的整除传递。本机整数算术复跑 231 个有限实例。[指数传递](../../math-l16-prime-sieve-certified-transfers/references/cogentic-finite-arithmetic.md) |
| 05 Log-Rank | 物理页 35–36 Proposition A.3。扩展原秩检查器，给出单色块、低秩交叉块、剩余块的行列索引与精确面积。示例原密度为 \(4/9\)，选中块秩为 1，余块密度为 \(1/3\)。[递归节点](../../math-logrank-rectangle-rank-halving/references/source-audit.md) |
| 06 边重构 | 物理页 8–10 Lemmas 2.2–2.3。从完整卡组的度数恢复原图度多重集，单独处理星图及孤立点。对 4 至 6 顶点、至少 4 边的 33,062 个标号简单图进行精确回放。[度序列](../../math-edge-deck-reconstruction-audit/references/edge-kelly-degree-sequence.md) |

上述有限构件可独立调用。六篇论文的全局主定理及其完整复杂度和形式化证明仍待独立验收。

## 第四次蒸馏与实际验收

本机六份下载件在北京时间 11 月 26 日上午进入归档。Google Research 仓库将首发标在 11 月 25 日。本轮从当前可查的固定提交逐篇复算原件与远端 PDF 的 SHA-256 及页数。五份字节一致，双矩阵稿修订了引文，所用物理页 8–10 的提取文本仅有两处引文编号变动。[首发提交](https://github.com/google-research/google-research/commit/4a7bc8ab0bc770e71a259b7966c500496b99010a)。[版本目录](https://github.com/google-research/google-research/tree/3f540f420bfae7e6ce48365a68d0ae003feb2f87/cogentic_research_papers)。

| 本机原件 | 原文定位 | 本轮接入方法 | 本机精确验收 |
| --- | --- | --- | --- |
| 01_integer_factorization.pdf | 物理页 43–44，Lemma 5.2 | [3-adic 代数平方见证](../../math-l16-prime-sieve-certified-transfers/references/cogentic-3adic-algebraic-square-certificate.md) | 模 9 穷举 729 个剩余类，正例恰有两根，改动后的目标无根。 |
| 02_discrete_logarithm.pdf | 物理页 34，Lemma 2.1(3) | [Frobenius 不可约性判别](../../math-l03-rational-and-interval-certificates/references/google-cogentic-frobenius-irreducibility.md) | 在二元域穷举首一四次及以下多项式，与直接试除一致。 |
| 03_bimatrix_nash_equilibrium.pdf | 物理页 8–10，Lemma 2.3(b) | [固定行锚点的严格 LP 对偶分离](../../math-bimatrix-kite-mixing/references/wave5-google03-dual-separator.md) | 有理见证的最小分离裕量为 7/20。等号边界被拒绝。 |
| 04_deterministic_factoring_l34.pdf | 物理页 57，Theorem 1.1 证明的步骤 1–2 | [偶数与完全幂的因子预检查](../../math-l16-prime-sieve-certified-transfers/references/cogentic-perfect-power-precheck-wave5.md) | 27 给出因子 3。91 的结果为未判定。 |
| 05_logrank_conjecture.pdf | 物理页 12–13，Lemma 3.2(1) | [低密度乘积测度下的零单色矩形](../../math-logrank-rectangle-rank-halving/references/cogentic-low-density-zero-rectangle.md) | 给定三阶矩阵的实秩为 2，最大零矩形测度为 4/9。 |
| 06_edge_reconstruction.pdf | 物理页 8–9，Lemma 2.2(1) | [等边卡组的 Möbius 重叠奇偶性](../../math-edge-deck-reconstruction-audit/references/mobius-overlap-parity.md) | 在经典小图碰撞上，4 个子集的奇偶恒等式与排列下界均通过精确核验。 |

工具以给定小规模输入核验各自有限结论。原稿的全局复杂度、近似保证、单色矩形结果及线性密度下的边重构仍按论文所载主张登记，伴随 Lean 工程仍待取得。

| 版本 | 页数 | SHA-256 | 论文 | 相关技能 | 处理状态 |
| --- | ---: | --- | --- | --- | --- |
| Google Research 修订稿 | 41 | `32196e6a64d13fbd216c7e7353a3b44a46e8389eb3d15bad48ffb3dd926cc337` | An Exact Polynomial-Time Algorithm for 1/5-Approximate Nash Equilibria in Bimatrix Games | [math-bimatrix-kite-mixing](../../math-bimatrix-kite-mixing/SKILL.md) | 已采用构件 |

## 11 月 26 日补充蒸馏

用本机 Python 复算归档六份 PDF 的 SHA-256 和 274 个物理页。对照当日官方固定目录，五份现行稿与下载件完全相同，双矩阵稿仍为上述已登记修订。目录同一提交修订了另一篇组合拍卖论文。[Google Research 当日目录](https://github.com/google-research/google-research/tree/3f540f420bfae7e6ce48365a68d0ae003feb2f87/cogentic_research_papers)

| 来源 | 原文定位 | 采用的有限构件 | 本机精确回放 |
| --- | --- | --- | --- |
| 03 双矩阵博弈 | 物理页 11，MaximinKiteNE Step 2 | [交换玩家角色的后悔值传递](../../math-bimatrix-kite-mixing/references/player-role-normalization.md) | 非方阵例子把后悔值 `(5/32,5/24)` 精确换为 `(5/24,5/32)`。收益越出归一化区间时拒绝。 |
| 05 Log-Rank | 物理页 35，Proposition A.3 的首段证明 | [全二叉协议树的叶数平衡](../../math-logrank-rectangle-rank-halving/references/protocol-tree-balancing.md) | 2 至 10 叶的 6,917 种有序全二叉树均通过整数划分核验。 |
| 06 边重构 | 物理页 12–14，Lemma 3.1(1a–c) | [度有序 Kruskal 构件](../../math-edge-deck-reconstruction-audit/references/degree-ordered-kruskal-nonbridge.md) | 核验了全部 38 个四顶点连通标号图及一个五顶点非正则图。 |
| Google 组合拍卖修订 | 物理页 6–7，Lemma 2.1 | [组合拍卖静态价格 LP 不等式](../../probability-prophet-online-selection/references/cogentic-subadditive-static-price-lp-certificate.md) | 单物品正例的两个子集约束均以 \(1/4\) 取等。把价格改成零会违反约束。 |

组合拍卖原稿首发于 11 月 24 日。11 月 26 日北京时间 07:54 的官方修订补入独立并行工作引文。两个官方 PDF 均为 36 页，采用的局部不等式一致。此处登记当前版，首发稿留作版本对照。[官方修订提交](https://github.com/google-research/google-research/commit/3f540f420bfae7e6ce48365a68d0ae003feb2f87)

| 版本 | 页数 | SHA-256 | 论文 | 相关技能 | 处理状态 |
| --- | ---: | --- | --- | --- | --- |
| Google Research 修订稿（独立论文） | 36 | `f49ea5630c1aaead322a0b7f87ac145181af4e86c574df5965cf9e30ba7b31aa` | Nearly Tight O(log log log m) Prophet Inequalities for Subadditive Combinatorial Auctions | [probability-prophet-online-selection](../../probability-prophet-online-selection/SKILL.md) | 已采用构件 |
