# 数学文献复核与精确工具整合

本轮逐项复核索引中的十份文献，为九份登记了可独立核对的构件。一份继续登记完整形式化核验，相关论文各处尚未核完的主定理依赖仍留在逐篇记录中。全索引共 5,390 个 SHA-256 身份。 [逐篇查询](../skills/math-research/references/literature-source-lookup.md)

## 本机数学验收

- 新增有理系数首一多项式的 Böttcher 形式共轭技能。用截断 Horner 乘法递推，并逐项代回 \(\Psi(z^d)=f(\Psi(z))\)。二次原例和有理三次例均通过，后者另用 SymPy 展开复核。解析与 Julia 集结论保留原先的全局依赖。 [Böttcher 形式共轭](../skills/math-local-bottcher-formal-conjugacy/SKILL.md)
- 两份 VP/VNP PDF 在去除单一首页戳记、规整空白后，70 页 pypdf 提取文字均一致。PDFium 独立得到相同顺序的正文 Unicode 字形，边界框最大偏差小于 0.46 点。两份各保留独立哈希。采用范围为物理页 60 的 Ryser 公式及系数消去，四阶例的 256 个行选取项恰有 24 个留下。 [Ryser 公式与版本](../skills/math-cycle-weighted-permanent/references/ryser-coefficient-cancellation.md)
- MATLAB 对两份 3-SAT 原稿所用的三比特符号恒等式穷举 4,096 个设置。512 个同异或情形含 64 个对角项和 448 个消去项，失败数为零。递归算法、计算成本模型与复杂性结论需要各自的证明链。 [三比特符号规则](../skills/math-discrete-proof-transfer/references/eight-square-sign-rule.md)
- 并入四项明确条件下的工具。渗流使用加性黏合推出近一概率，2,592 个有理用例验收严格性。交换子工具核验 Riccati 条件下的非交换块乘法与范数为 2 的精确见证。Xi 的三角合同只传递主子式符号。流体工具只核验隐式变量的精确时间和轴向导数，三个 SymPy 例的残差均为零。 [渗流](../skills/probability-percolation-renormalization/references/additive-gluing-near-one.md) · [交换子](../skills/math-operator-algebra-certificates/references/identity-corner-commutator.md) · [Xi 主子式](../skills/math-xi-theta-finite-certificates/references/sra-leading-congruence-gate.md) · [流体链式法则](../skills/math-geometric-pde-reductions/references/swirl-implicit-coordinate-derivatives.md)
- 三臂直接 Bernoulli RKHS 例的最优分配由 KL 的单调性和精确整数比较证明，覆盖连续备择参数。最优成本为 \(1/\log(7/3)\)。MATLAB R2026b 在 3,001 点上复现数值 \(1.1802225011438288\)。 [完整证明与回放](../skills/probability-bandit-information-bounds/examples/positive.md)

## 形式化核验

Aaronson–Ambainis 固定源码的顶层模块已由 Lean 4.33.0 成功编译。官方公理检查器从构建日志读到 13 条声明，四条必需顶层定理均有记录，检查零错误。允许公理为 `propext`、`Classical.choice` 和 `Quot.sound`。用有理数复算了 Walsh 影响力和两种离散立方体之间的方差与常数变换。扩大到辅助声明的公理报告还需要 `DetBij.Bijection` 的额外编译产物。本轮冻结时，从空环境出发的独立内核回放正在运行。 [当前来源状态](../skills/math-research/references/recent-non-openai-sources.md)

## 安装资源

35 处旧 Worker 路径已接回当前包中同编号的真实附件。其余本轮识别的裸历史档案定位明确标记为历史记录。已发布链接可在空目录安装后打开，附件和原始 PDF 仍按来源名字、原件 SHA-256 及历史档案路径查找。 [证据与档案指引](../skills/math-research/references/evidence.md)
