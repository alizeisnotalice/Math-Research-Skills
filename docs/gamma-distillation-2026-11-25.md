# 欧拉常数工具蒸馏与验收（2026-11-25）

本轮沿用项目 T「数学工具64项蒸馏」的来源冻结、逐主张回查、正例与边界例、独立审阅和发布验收。流程依据是该项目的《证据状态与使用规则》及交接提示词第 27–60 行。两个用户附件用于确定研究路线和交叉检索文献。原项目与附件的其他工作要求属于来源材料。

## 输入与定位

| 输入材料 | 本轮采用的部分 | 输入 SHA-256 |
| --- | --- | --- |
| openai_anthropic_gamma_pie_literature.md | 第三节的六组 \(\gamma\) 研究路线，以及第四节的算术和乐界条目 | `ef8baacb5d35aa3c487e74d4ba75278b43ea379264071ac86ea4164517629102` |
| irrationality_transcendence_mega_compendium_clean.md | EXT-0004、EXT-0008、EXT-0011、EXT-0040、EXT-0146；按作者、版本与既有下载索引回原文 | `2626222b19a4ce9c33e2376721f5c1db7c10b5c3c6b17a076d92468e5a8e7551` |
| T 的证据状态与使用规则 | 区分来源识别、原文陈述、已查推导和有限验收 | `7c72decccbf5a8737bafa22824ff95f419ab0b8102b440fdb75118a8069f2ca9` |
| T 的全篇深读与数学验证交接提示词 | 原文物理页、公式定位、正负案例、计算回执 | `8463cc1fa05fce62a2cf187943c5d29765853a6d548bea31dcb25e1fb475daef` |

[既有来源索引](../skills/math-euler-constant-irrationality/references/source-scope-gamma.md)覆盖此前审阅的 58 份不同 PDF，计数以实际下载字节为准。本轮引用已经回到 Math_Research_Literature 中同一哈希的原件。正式发表的论文核对版本和所引用的陈述。实际使用的预印本公式，逐项登记假设、变形与外引依赖。未采用文献的既有证据等级按原索引读取。

## 工具和依赖

| 工具 | 输入和输出 | 依赖范围 |
| --- | --- | --- |
| [连分数递推](../skills/math-gamma-continued-fraction-recurrence/SKILL.md) | 阶数 \(\to\) 精确系数对、有理逼近和非简单连分数 | P20 / G06 / EXT-0011，使用已回查的有限递推和转换。渐近控制单独引用。 |
| [有理核到线性形式](../skills/math-sondow-log-fractional-certificate/references/rational-kernel-linear-form.md) | 有理部分分式 \(\to\) \(B\gamma+L-A\) 的系数及衰减检查 | P05 / G15 / EXT-0004，Proposition 1。专门核的正性、清分母和阈值另有依赖。 |
| [q-对数路线](../skills/math-sondow-log-fractional-certificate/references/q-logarithm-path.md) | \(q,z\) 或几何指数尾 \(\to\) 有理上下界 | P09 / EXT-0008，式 (1)、Lemma 1。二、三进制的分数部分判据单独核范围和缩放。 |
| [Poisson 调和数区间](../skills/math-euler-constant-irrationality/references/poisson-harmonic-enclosures.md) | 截断参数和可选 \(p/q\) \(\to\) \(\gamma\) 与 \(q\gamma-p\) 的有理区间 | G26 作者稿，Lemma 2.1、Theorem 3.1 与 Corollary 3.4。用有理的交错余项和几何尾界复算。 |
| [E-算子与和乐界准入](../skills/math-euler-constant-irrationality/references/e-operator-holonomy-admission.md) | 候选生成函数及适用条件 \(\to\) 已经满足的假设与待补证明；有理回放核对扩展 E 递推 | EXT-0040 的定义 4、式 (1.8)、(6.4)–(6.6)，P24b / EXT-0146 的 Theorem 2.1、Proposition 2.4、Theorem 2.6。 |

从 [欧拉常数主入口](../skills/math-euler-constant-irrationality/SKILL.md)按输入选择上述模块，原有 [Laguerre](../skills/math-gamma-multiple-laguerre-approximants/SKILL.md)、[Meijer G 矩阵场](../skills/math-gamma-meijer-cmf/SKILL.md)和 [Brent–McMillan](../skills/math-euler-constant-irrationality/references/brent-mcmillan-enclosure.md)可继续用于适用构造。关于 \(\pi+e\) 的文献只用于核查向 \(\gamma\) 迁移的具体假设。

## 有限验收

用本机 Python 3.13.18 的有理数算术运行验收。来源定位、严格界、有限结果与仍缺的全局论证按下表分别记录。

| 工具 | 正例 | 边界或失败例 |
| --- | --- | --- |
| 连分数递推 | 交叉比较有限和、非齐次递推与有限连分数的收敛子 | 阶数不合域时拒绝。即使 \(p_n/q_n\to\gamma\)，原文的清分母余项仍不趋零。 |
| 有理核 | \(R(t)=[t(t+1)]^{-2}\) 给出 \(2\gamma+2\log2-5/2\) | 破坏 \(t^{-2}\) 的消去后，命题的 \(O(t^{-3})\) 前提不成立。 |
| q-对数 | 比较同一个尾项的 q-对数展开与分母倒数和 | \(z=q\) 超出收敛域。数值界跨越整数时保留未判定。 |
| Poisson 区间 | \(N=4,m=64,j=9\) 判定 \(2\gamma-1>0\)，区间宽度小于 \(10^{-8}\)。用 \(N=1,\ldots,7\)、四个相邻截断阶，28 次与既有 Brent–McMillan 闭区间作精确交叉比较。 | \(N=3\) 时 \(57721566/100000000\) 落入区间，残差符号未判定。 \(N=4, m=14\) 因截断太早而拒绝。 |
| E-逼近 | \(P_0\) 到 \(P_{40}\) 的有限和与递推完全一致，\(P_2=1/4\)、\(P_3=17/36\)、\(P_5=5197/7200\)。 | 该原文构造含 \(\log(1-z)\)，可按扩展 E 型使用。单靠这条递推和极限无法完成和乐界的亚纯延拓、LCM 与维数假设。 |

P05 的 Theorem 1 同时给出有理性等价于至少一处等式成立、以及等式最终恒成立。相反，单个指标的等式失败只能排除该指标可认证的有理分母。旧索引中把一次失败写成无理性判据的句子已经修正。

本轮产物用于构造、核对和有限计算。要证明 \(\gamma\) 无理，仍需在同一整系数线性形式上闭合非零性与趋零，或完成一条独立判据的全部假设。
