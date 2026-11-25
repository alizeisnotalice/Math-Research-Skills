---
name: math-m01-convex-hull-extreme-points
description: 用仿射相关消元压缩有限凸组合，用 Krein–Milman 定位紧凸集的极点闭凸包；核对拓扑、紧性与表示类型。
---

# M01 · 凸组合与极点

1. 先明确所需表示是有限凸组合、闭凸包逼近还是积分表示。指定环境拓扑和仿射维数。
2. 对有限维的有限凸组合，找支撑点的仿射依赖，沿依赖移动权重直到至少一个系数归零。重复后至多保留仿射维数加一项。标准单纯形的重心达到此上界，每个顶点本身只需一项。见[消元证明和锐性](references/method.md)。
3. 要用 Krein–Milman，核对集合非空、紧且凸，以及环境空间为 Hausdorff 局部凸空间。得到的是其极点的闭凸包表示。若还要求有限支撑或积分表示，另证相应结论。

采用 Bachir 的暴露点变体时按[来源与阅读状态](references/provenance.md)核对其紧可度量、函数分离及 Φ-凸条件。历史来源的物理位置见[便携证据索引](references/handoff-evidence-index.csv)和[审核账本定位](references/portable-audit-access.md)。旧中心立方体课题可按[课题接口](references/cube-interface.md)核对附加条件。

见[三角形重心](examples/positive.md)和[条件缺失例](examples/negative.md)。
