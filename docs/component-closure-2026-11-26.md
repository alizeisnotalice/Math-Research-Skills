# 原稿依赖复核与精确构件验收

本轮从已发布索引选出全部 590 条候选与待核记录，其中 OpenAI 原稿 527 份，历史来源 63 份。59 组都逐项核验本机 SHA-256、PDF 物理页数、引用位置、固定版本和技能路径。复核了拟采用的证明步骤和所需假设。现有技能的来源涉及已发表版本时，核对对应引用。索引仍覆盖 763 份 OpenAI 原件，并为复核后的相关技能注明路径。[OpenAI 逐篇索引](../skills/math-research/references/openai-sources/README.md) · [历史依赖复核](../skills/math-research/references/historical-sources/dependency-recheck/README.md)

## 通过验收的数学工具

14 个精确检查器合并到现有入口或按独立数学接口发布。20 份来源增加了明确的已采用构件记录。多份共用证明机制的来源使用同一工具。

| 构件 | 核验的数学范围与样例 |
| --- | --- |
| [Hardy 二次亏损](../skills/math-m03-near-extremizer-stability/references/hardy-quadratic-deficit.md) | 有理阶梯函数，含无穷尾积分。18 组带符号输入的 SymPy 积分与有理和对数式一致。 |
| [偶次数三项式](../skills/probability-integer-polynomial-factorization/references/even-trinomial-obstruction.md) | 非负余因子的奇偶分拆与强制递推。长指数 6、短系数 \(1/2\) 时冲突系数至少为 \(11/8\)。 |
| [弱型阈值预算](../skills/math-f06-menshov-rademacher-maximal-partial-sums/references/weighted-weak-aggregation.md) · [仿射张量乘积导数](../skills/math-f02-tensor-fourier-positivity-soft-square-supremum/references/product-derivative-certificate.md) | 给定非负算子的分量弱型界与阈值预算，或给定逐因子阻尼和导数条件。分别核验有理并集上界和有限对称和。 |
| [局部仿射选择](../skills/math-m04-measurable-supremum-selection/references/local-affine-simplex-selector.md) | 给定有理单纯形和凸图的半空间描述，验证图成员关系。样例的重心坐标为 \((5/12,1/4,1/3)\)。 |
| [单困难坐标共正枚举](../skills/math-c02-completely-positive-copositive/references/one-difficult-coordinate.md) · [对角占优双二次 SOS](../skills/math-c03-moment-sos-certificates/references/biquadratic-dd-sos.md) | 给定正定主块、谱下界和 KKT 见证得到有限整数枚举范围。双二次型的非负余量和平方展开由有理数逐项重构。 |
| [对称二点余秩](../skills/probability-random-matrix-tensor/references/symmetric-binary-corank-tail.md) · [散度型残差修复](../skills/math-l03-rational-and-interval-certificates/references/divergence-residual-repair.md) | 对称二点正例的尾概率和主子块上界均为 \(1/8\)。一维散度型正例的修复残差为零，修正后的系数通过 Bernstein 正性验收。 |
| [四个树递归势](../skills/math-e03-tree-bellman-cross-layer-budget/references/two_recursive_potential_tree_energy.md) | 核对四个给定势的平方递推、共同增量、取等条件和叶能量。边界样例的两边相等。 |
| [有限开关网络](../skills/probability-switch-network-cylinders/SKILL.md) | 三份原稿的公共有限构件。样例中心化能量为 \(2/3,1/6,1/24\)，条件置换核按时间顺序合成。 |
| [环面谱包](../skills/math-torus-packet-spectral-density/SKILL.md) · [有限除子账本](../skills/math-ag-divisor-intersection-ledger/SKILL.md) | 有理分段仿射模一推前的样例总质量为 \(5/2\)，密度差的 \(L^1\) 值为 \(5/4\)。除子账本核验五个给定有限表，几何对象及交叉数由输入提供。 |
| [纯度迭代与尾质量](../skills/probability-nonlinear-law-dynamics/references/finite-purity-squaring.md) | 对 120 个三原子有理概率向量复算归一化平方与正确尾界。反例 \((13/14,1/14,0)\) 使原稿 (3.3) 的有理平方比较差为 \(985/9604\)。后续依赖该式的传播仍待独立证明。 |

脚本和算例在本机 Python 3.13.18、SymPy 1.14.0 上通过 33 项命令回放及上述精确核对。五项已安装概率技能的历史状态说明已更正，现行入口按实际数学条件选路。

## 剩余证明和采用条件

OpenAI 索引现有 184 份已安装构件、13 份限定参考、312 份候选、178 份待核、19 份版本或题录、25 份邻近材料和 32 份历史归档。待核数上升源于重新检查候选的控制性前提。原稿 `(3.3)` 的反例已记入来源条目，现行技能使用独立推导的较弱界。历史索引的 181 条记录中，32 条待实现或进一步验证，19 条留有证明、版本或可读性缺口。

逐份复算共享文献库的哈希后有 5,410 条 PDF 路径与 5,389 个唯一哈希。当前七个来源集合共有 5,388 个可检索原件，另一份私人材料保留在本机。检索覆盖反映原件和分类身份，采用结论时以逐条的证明依赖和适用范围为准。[可检索的来源入口](../skills/math-research/references/literature-source-lookup.md)
