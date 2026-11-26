# OpenAI 与历史预印本依赖复核

逐项复核了 OpenAI 逐篇索引原先保留的 186 份稿件，以及历史依赖索引此前留下的 70 条记录。45 批共 256 张来源卡均验收了原 PDF 的 SHA-256、实际物理页数、所引页、记录顺序及技能路由。复核的对象是可迁移的构件和其控制性假设。OpenAI 原稿按已固定的仓库版本定位。[OpenAI 原稿版本历史](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/history.md)

## 可调用构件

| 构件 | 可复核输出 |
| --- | --- |
| [有限可逆 Markov 尾界](../skills/probability-markov-spectral-mixing/references/finite-markov-chernoff.md) | 给定平稳分布、转移矩阵、整数观测和有理参数，验证矩阵半正定性并给出严格尾概率上界。样例精确尾概率为 \(27/128\)，上界为 \(125/288\)。 |
| [平稳 Markov 增量](../skills/probability-markov-spectral-mixing/references/openai_critical_slowing_stationary_increment.md) | 输入有限可逆链和观测，核验 Dirichlet 能量与给定时间滞后的二阶增量。样例得到增量 \(1/2\)、能量 \(1/4\)、上界 \(3/2\)。 |
| [附加线性约束的 Kantorovich 输运](../skills/math-d01-kantorovich-duality/references/finite-constrained-transport.md) | 对给定有限原始耦合、势和自由符号乘子检查边缘、约束、逐格松弛、互补性与零间隙。 |
| [单系数块双二次 Gram 证书](../skills/math-c03-moment-sos-certificates/references/qi-cui-xu-monic-xsymmetric-gram.md) | 核对半正定因子、Kronecker Gram、逐项多项式系数以及构造的 SOS 秩界。 |
| [等差坐标 CRT 计数](../skills/math-l16-prime-sieve-certified-transfers/references/jacobsthal-progression-coordinate-crt.md) | 对给定有限模数与区间精确比对容斥、允许余数类和直接枚举。样例计数为 520。 |
| [有限 HBL 表示证人](../skills/math-hbl-finite-presentation/SKILL.md) | 对给定有限图与链分解精确核验表示条件。 |
| [有限蜂窝格有符号通量](../skills/math-honeycomb-finite-boundary-flux/SKILL.md) | 在圆分域精确枚举有限简单边界域的自避路径。三角域边长 1–3、六三角形六边形及凹域均重放了有符号通量。凸域另外检查出边转角。 |

HBL 和蜂窝格通量各有单独的技能入口。其余构件分别并入既有 Markov、输运、矩与 SOS 和有限筛查技能。验收使用本机 Python 3.13.18 的整数或有理数。有限图证人、给定矩阵证书及有限区域枚举的范围由各工具输入确定。

## 依赖处置

- OpenAI 索引覆盖 763 份 PDF。本轮后有 171 项已安装构件、7 项限域参考、425 项候选、102 项待核、17 项仅版本、9 项邻近材料及 32 项历史归档。[OpenAI 逐篇索引](../skills/math-research/references/openai-sources/README.md)
- 历史依赖索引的 181 项现行处置包括 26 项已覆盖、21 项引用核对、71 项邻近材料、47 项候选及 16 项待核。[历史依赖复核](../skills/math-research/references/historical-sources/dependency-recheck/README.md)
- 历史原稿中记录了会阻断迁移的具体前提。例子包括将平移推前视为绝对连续、将逐路径的最终控制视为 \(L^\infty\) 一致界，以及把具有周期因子的渐近前项视为常数。引用页、版本身份和条件见逐条来源记录。
