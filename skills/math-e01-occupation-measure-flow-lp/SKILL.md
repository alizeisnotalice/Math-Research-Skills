---
name: math-e01-occupation-measure-flow-lp
description: 建立占用测度、有限时域概率流和流守恒 LP，核对真实过程、边界通量、终止时刻、风险原子与可实现性。
---

# E01 · 占用测度与流守恒

先确定原过程、初始律、可用动作、结束规则和目标。判断目标是轨迹控制值、弱测度界、峰值、停止风险还是分位风险。时间固定、随机停止及折扣约定决定流的归一化与可行域。

- 有限前向转移图的终点命中概率、状态访问质量和接受率，用[前向概率流与反向递推](references/finite-forward-flow.md)。对折扣 MDP，把每个动作的占用质量计入源状态和折扣后的去向，按状态验证流平衡。恢复策略时除以该状态占用总质量，仅在正质量处这样定义。
- 连续控制先写测试函数域和生成元。核对初末质量、扩散或跳跃项、时间边缘及界面通量，再判断由路径得到的测度约束和从可行测度恢复过程的条件。
- 处理峰值与风险时，记录共同确定性终止时刻是否真的进入模型。对标准 ES，分位点有原子时允许拆分其质量。若采用弱 LP、矩层级或放松控制，说明最优化方向及实际可行像。
- 针对扩散、均场、峰值 ES、切换和旧中心立方体模型，按[模型假设与原文核验](references/model-evidence.md)逐条选用。来源版本和适用范围见[来源与阅读状态](references/provenance.md)，原文定位见[便携证据索引](references/handoff-evidence-index.csv)。

输出原始问题、流平衡式以及证明或证书所支持的方向与可达到性。有限模型的可行性只能在其已证明的还原条件下传回原过程。

对子串次数构造分层有向多图时，使用[子串计数与 Euler 日程](references/hierarchical-word-flow.md)核对守恒、支持连通性和追加字符的输出。

若只需把固定边上的部分有符号流延拓到有限图其余边，或在森林上精确解散度方程，使用[部分流延拓与树叶消元](references/tree-flow-extension.md)。

## 文献复核采用的构件

- [Scalar-codomain no-gap guard for occupation relaxations](references/scalar-codomain-no-gap-occupation.md)
