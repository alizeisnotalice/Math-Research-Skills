---
name: math-centered-cube-endpoint-budget
description: "Audit or extend centered axis-parallel cube Hardy–Littlewood weak-(1,1) bounds: all-scale source/receiver budgets, joint high-capacity remainders, and finite-dimensional square/cube certificates. Use for centered-cube-upper-bound, the Round 830 remainder, or cubical endpoint constants; not for Euclidean balls, Kakeya tubes, or strong rectangular maxima."
---

# 中心立方体极大算子的弱端点工具

本入口用于指定专题的研究核验。预印本及项目材料按固定版本引用，使用具体结论前核验原文假设、证明依赖和迁移步骤。涉及既有课题状态时，先对照当前项目记录。

先固定要证明的命题：对 $Q_b(x)=x+[-b/2,b/2]^n$、非负有限测度 $\mu$，以 Lebesgue 体积量超水平集；尺宽 $b$ 是全边长。$L^1$ 上界与有限原子搜索之间必须给出适用于**严格超水平集**的逼近桥；不得把有限窗、单半径或有限样本之证据当作全尺度上界。逐项注明其是一般维数的渐近阶，还是固定维数常数。

## 一般上界：诊断双重坏余量，而非独立使用两条平均界

1. 先取当前仓库最新轮与原母式。若仍走 Round 813–830 路线，读 [原流及两道门](references/round-830.md)。保存原记录两端的实际来源、两端 Lebesgue 接收者、所有者的互不交性、原分母和窗/体积档。每步写明冻结的信息和选择的测度；在不同条件律下得到的两个概率不能相乘。
2. 在同一已冻结原流上登记：固定右来源时的有序跨尺度接触率、固定完整双臂时的共同容量比、以及两个坏事件的**原测度交集**。分别记录原层与扩展层的权重和回代损失。删去一类记录后重新定义伴随采样，只在新余流上启动下一门，不可给前一轮成功事件偷偷重新归一化。
3. 先找会破坏候选单调性的小配置：少接触但高共享、同源跨窗复用、接收点落在共同中心盒外。几何薄交不等于实际来源质量小；截面体积不等于端点质量。有限构造只推翻它实际满足假设的命题。
4. 输出预算账：旧流质量 = 已支付块 + 未支付块；每块写 $\sqrt n$、对数、窗档数与回代的真实幂次。必须把新收缩或上界代回顶层不等式，逐项处理 $|R|, V, \|\mu\|$，才可报告全局结果。若交集仍开，交付一个有量词的剩余引理或可复核障碍，不报“闭合百分比”。

## 固定维数：用两个方向分离的证书

- **下界**：有限原子 $(p_i,w_i)$ 与能确认严格越阈的接收区域。对非空子集 $S$，取 $b_S^n<\sum_{i\in S} w_i/\lambda$，以各坐标区间 $[\max_{i\in S}p_{ij}-b_S/2,\ \min_{i\in S}p_{ij}+b_S/2]$ 的积给出内证矩形；严格不等式可消除边点和浮点误差。只计并集一次。若目标定义为 $L^1$ 输入，在较小紧致内部矩形上保留半径松弛、以支撑充分小的光滑核替换原子、再取极限。列出有理/区间保证及容积计算。
- **上界**：先证明比较或对偶证书的可行性蕴含全量词目标，再验证空间变量 $x$、参数、奇异区、分段接缝、无穷尾都被覆盖；有限约束 LP 的最优点不自动给连续上界。二维旋转比较法可以作为候选证书，不可直接升维。见 [出版源与迁移边界](references/source-transfer.md)。

最终把每项标成已证恒等式、引用结果（包含所需精确假设）、数值证书、数值实验或待证。固定维数上下界只与**同几何、同中心化、同归一化**比较。OpenAI 的圆盘 Sobolev 端点、管状 Kakeya、凸体格覆盖和欧几里得张量定价都不是这里的立方体 $L^1\to L^{1,\infty}$ 上界。

## 文献复核采用的构件

- [Square-maximal comparison premise from a nonlocal kernel](references/lin-square-comparison-premise.md)
