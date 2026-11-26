---
name: math-euler-constant-irrationality
description: 研究欧拉–马歇罗尼常数 γ 的无理性。构造或审计 γ 的 Padé、多重正交、超几何、递推、整数线性形式、分母消去与 Sondow 型判据，也用于核对 E/G 函数、算术 Gevrey 与 Stokes 常数方法能否转移到 γ。
---

# 欧拉常数无理性

目标是证明 γ=limₙ(Hₙ−log n) 不属于 Q。先注明本轮目标，例如复现一个式子、改善一个整化界、证明相邻余项的分离，或核对一条完整证明。引用最新成果前查一手版本。[方法和来源选择](references/methods.md) 提供分支及起始材料。

## 按输入调用论文工具

- 从整数指标生成对数权重、认证有限分母排除，用 [Sondow 证书](../math-sondow-log-fractional-certificate/SKILL.md)。
- 从阶数直接生成 Hessami Pilehrood 的有理收敛子与非简单连分数，用 [欧拉常数连分数递推](../math-gamma-continued-fraction-recurrence/SKILL.md)。
- 生成精确多重 Laguerre 系数及原始/约分整数对，或用 Rivoal、Aptekarev 递推作同尺度比较，读 [多重 Laguerre 逼近](../math-gamma-multiple-laguerre-approximants/SKILL.md)。
- 生成 γ 的单调有理下界，或审计正矩表示的整化与容量条件，用 [Hankel 正矩工具](../math-hankel-pade-certificates/SKILL.md)。下界逼近与无理性判据分别核对。
- 从参数轨迹、对偶矩阵和预备的换基得到递推，用 [Meijer G 保守矩阵场](../math-gamma-meijer-cmf/SKILL.md)。
- 需要给定输入的严格数值区间、\(q\gamma-p\) 的有限符号或分母排除时，用 [Brent–McMillan 有理区间](references/brent-mcmillan-enclosure.md)。
- 从 Poisson 调和数的单对数展开认证有限残差符号，用 [Poisson 调和区间](references/poisson-harmonic-enclosures.md)。
- 按 \(d,m\) 生成显式整系数变换和严格有理区间，用 [Elsner 变换](references/elsner-transform.md)。
- 对逐尺度对数项、Euler–Gompertz 辅助常数或很快的有理逼近，用 [混合形式和高度](references/mixed-log-height-audit.md)。
- 对二进制级数和有限 Gregory 恒等式，用 [有限有理级数](references/finite-rational-series.md)。
- 当整系数余项及高度已有证明，用 [整数线性形式的指数率](../math-integer-linear-form-rates/SKILL.md) 推导逼近下界和无理性指数门槛。
- 对 E/G 函数、1-求和与算术和乐候选路线，读 [算术 Gevrey 与 CDT 接口](references/arithmetic-gevrey.md)。需要检查普通 E-逼近、含对数扩展或和乐界能否应用时，用 [E-算子与和乐界准入](references/e-operator-holonomy-admission.md)。

- 设计行列式或研究伴随常数的局部消元时，读 [OpenAI 算术行列式构造](../math-openai-arithmetic-determinants/SKILL.md)。先证明目标矩与消元机制对应。

## 推进证明

1. **写清恒等式。** 固定指标、基底、初值、积分区域或分支。目标若写成 Rₙ=qₙγ−pₙ，先证明没有未经消去的 log、ζ 值或其他常数。递推须有等价的初值和极限识别；发现程序与数值吻合属于候选证据。
2. **单独做整化。** 取正整数 Dₙ，证明 Dₙpₙ、Dₙqₙ 为整数。逐素数估计分母或公因子时，写清范围、重数、异常指标和所需统一性。约分必须发生在同一对系数上。记录真正的整数形式 Lₙ=DₙRₙ，若已经整系数则取 Dₙ=1。
3. **对同一个 Lₙ 证明非零且趋零。** 给出严格符号、余项下界或可证明的非消失子列。若 γ=a/b，则 bLₙ 是整数，故在非零子列上不可能趋零。只知道 pₙ/qₙ→γ 时，另算 |Dₙqₙ|·|γ−pₙ/qₙ|。乘入分母的增长可能耗尽全部解析增益。
4. **使用等价判据时单列未证量词。** 例如 Sondow 的分数部分判据须对无穷多个 n 达到门槛。每个有限 n 的有理分母排除范围另行记录。代换成另一种对数或积分形式时，说明新形式怎样使未证条件变得可控。
5. **检验跨路线转移。** 用 E/G 函数值或周期关系时写出目标属于哪个对象类、取值点及奇点类型，以及定理需要的算术和解析条件。对 Stokes 常数明确扇区、归一化和连接系数。猜想写入条件性结论；一般周期定理须先证明覆盖本对象。
6. **按实际工作选择本机工具。** 读 [数学工具引导](../math-tool-router/SKILL.md)。精确 Python/SymPy 或 Wolfram 用于复核初值、递推、分母和有限 p 进数据；高精度与有向区间用于探路、认证有限符号或余项。保存计算输入、输出和范围，按证据类型陈述检验结果。

每轮至少记录目标、所用版本、实际公式、整化后误差及非消失状态、已闭合步骤和下一条缺失引理。遇到附带其他常数的线性形式，记录可证的线性独立性结论。需要单独审查源文献时，正式论文核对题录、版本和所引陈述，预印本逐条核对实际依赖和关键证明。

## 核对相邻首项余项的定号

若相邻首项的余项已经化为给定有理多项式，使用 [Bernstein 区间定号](../math-l03-rational-and-interval-certificates/references/rational-polynomial-sign.md) 拆分并核对指定区间，如 \(0<t\le 1/16\)。短核存在性、整化和对无限指标的适用性分别记录。

对 Prévost 带参数 `m` 的 Legendre–Padé 线性形式，用 [有限分母排除](../math-sondow-log-fractional-certificate/references/prevost-legendre-fractional-gate.md) 核验精确余项上界和分数部分。

用 [Prévost 的二进 Padé 有理逼近](../math-sondow-log-fractional-certificate/references/prevost-pade-rational-interval.md)计算给定二进参数的近似分母和有限严格区间。
