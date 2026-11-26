---
name: math-geometric-g-function-special-points
description: 对已给出的一参数代数族、退化、周期矩阵与特殊纤维数据，选择 G-函数局部关系、特殊点高度或模曲线非典型交的定理接口。
---

# 几何 G-函数与特殊点

当问题已给出代数族、定义域曲线、退化或基准纤维、比较同构和特殊点条件时，使用本技能整理 G-函数周期关系和高度结论。先选择实际模型，再读取对应来源卡。

- 椭圆曲线的一参数族与指定 CM 纤维，使用 [CM 局部值](references/cm-elliptic-local-values.md)。
- 主极化阿贝尔曲面的一参数 Hodge-generic 族与 QM 纤维，使用 [QM 局部值](references/qm-abelian-surfaces.md)。
- 平滑射影族的退化周期与特殊模空间，先核对 Urbanik 定理 1.3 所需的相关自同态的 Hodge 猜想，再使用 [几何 G-函数高度](references/geometric-g-functions-atypicality.md)。
- Torelli 轨迹的边界、属数和 Hodge-generic 条件，使用 [Torelli 非典型交](references/torelli-unlikely-intersections.md)。
- 模曲线幂中给定的强特殊交，使用 [超奇异约化](references/supersingular-modular-intersections.md)，并把同时超奇异稀疏性假设保留在结论中。
- 非紧 Hilbert 模曲线及有效高度和计数输入，使用 [有效 André--Oort](references/effective-hilbert-andre-oort.md)。

调用方必须提供族、基域、相关周期或比较矩阵、特殊纤维或特殊子簇、所需的 Hodge-generic 性、退化和高度条件。局部关系或高度界不自动给出目标常数的数值值、代数独立性、特殊点枚举或 Zilber--Pink 的一般结论。
