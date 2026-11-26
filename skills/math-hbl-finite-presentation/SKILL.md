---
name: math-hbl-finite-presentation
description: 对已给定的有理有限子空间图和边权，精确核验 HBL 有效表示并分解平衡边流；不搜索表示或计算一般 HBL 常数。
---

# 有限 HBL 图表示核验

当 Hölder--Brascamp--Lieb (HBL) 数据已给出一个**候选**有限子空间有向图、线性映射和有理边权时，使用 `scripts/hbl_presentation_check.py`。它以 `Fraction` 做秩、包含、投影像变化、平衡和质量的精确核验，并把每个标量边流分解为从 `0` 到 `H` 的链流。

先读 [有限证人说明](references/finite-witness-guide.md)。该工具不枚举全部子空间，不寻找图表示，不接受浮点输入，也不计算最优常数；输出 `valid: true` 仅表示给定有理编码通过已实现的有限证人条件。

```bash
python3 scripts/hbl_presentation_check.py examples/loomis_whitney_r2_valid.json
python3 scripts/hbl_presentation_check.py examples/loomis_whitney_r2_bad_summary.json
```

第二个命令应以非零状态退出：两个 θ 各自仍平衡，但 summary 的总质量为 `1/2`，不是有效表示。对实数（非有理）矩阵、近似秩、缺失边权或企图由失败输出断言 HBL 常数无穷的请求，应停止并另行使用可认证的区间/符号方法或理论论证。
