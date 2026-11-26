---
name: math-zeta-arithmetic-estimates
description: 根据指定的 ζ 函数采样、平滑核和参数区间接入等差级数矩比较与光滑数零点修正。适用于检查扭权、测量模型和误差来源。
---

# ζ 函数的算术平均与光滑数误差

从原文列出连续积分或离散采样、平滑权、扭因子、采样步长与参数区间。把要比较的主项和误差并排写出。

- 对离散 ζ 二阶矩，检查底数比的共振情形、平滑函数及丢番图条件是否与调用一致。固定底数或指定扭因子时保留各自的误差项。
- 对光滑数估计，先对齐 Ψ 的归一化、渐近区域和截断高度，再应用零点修正。保留原文的黎曼猜想条件。
- 输出版本、实际调用的参数域、误差层级和剩余假设。

## 补充来源中的方法

- [Smooth integers and the zeta-zero correction](references/c07-07-smooth-integers.md)
- [Vertical arithmetic progression zeta moments](references/c07-07-zeta-progression.md)

## 文献复核采用的构件

- [Hurwitz-zeta fourth moment under a strict irrationality-exponent premise](references/hurwitz-zeta-fourth-moment-ext0377.md)
- [Conditional discrete mixed-universality admission](references/kacinskaite-matsumoto-discrete-universality-ext0153.md)
