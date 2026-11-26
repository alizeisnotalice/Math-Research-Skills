# 第二批历史文献复核与可调用构件

本批从上次尚待登记的 2,992 个哈希中逐一核对 673 份原件。仓库索引收录 672 份文献，记录其版本、SHA-256、实际查阅物理页及适用范围。另有一份本机写作规范只在本机账本登记。共享库剩余待登记原件为 2,319 份。 [第二批文献索引](../skills/math-research/references/historical-sources/wave-02/README.md)

按数学用途登记优化 137 份、分析及几何 127 份、概率 408 份。27 个潜在构件和 12 个证据缺口保留相应的原文位置。三条上一批的候选依赖在这次核验后已接入技能。

| 可调用构件 | 实际验收 |
| --- | --- |
| Elsner 的欧拉常数整系数变换 | SymPy 核对 5 个导数恒等式。26 个 \((d,m)\) 用有理算术与 Brent–McMillan 区间交叉核对，同时检查严格余项符号、误差界和默认对数截断宽度。\(d=2,m=1\) 按期刊版使用单列的双边界。 [计算及期刊来源](../skills/math-euler-constant-irrationality/references/elsner-transform.md) |
| 单个二元比值的子模性 | 112 个向下封闭可行族与独立的全对集合不等式一致。复现期刊来源正例、精确反例；\(b_0=0\) 按定理的适用范围拒绝。另验证 32 变量的稀疏可行族。 [Han 判据](../skills/math-a01-fractional-normalization/references/han-2020-submodularity.md) |
| 有限 Markov 终点桥 | 64 个固定时域模型共 3,533 条路径与直接枚举一致，同时检查终点重加权的两个支持方向。不可达目标的负例精确拒绝。 [终点桥证书](../skills/math-h02-exponential-tilting-saddlepoint/references/aguilar-gatto-finite-bridge.md) |
| 树度量的原始–对偶输运 | 128 棵有理加权树与独立逐边切割一致，原始耦合和对偶势给出同一个精确成本。该证书作用于输入的树度量。 [树输运证书](../skills/math-d01-kantorovich-duality/references/tree-metric-transport.md) |

计算使用 Python 3.13.18 与 SymPy 1.14.0。上述验收覆盖明确输入的算术和解析适用条件。Elsner 变换的对数项若要用于欧拉常数无理性，仍需证明同一组系数的消去及整化误差。

复核还撤去了 H02 的失效历史文件定位。标题含 fractional、Chernoff 或 radial 的旧附件各按实际数学对象归档，相关性由来源卡中的具体假设和结论决定。
