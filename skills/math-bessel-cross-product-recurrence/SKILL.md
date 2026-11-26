---
name: math-bessel-cross-product-recurrence
description: 在已给定的 Bessel/modified-Bessel 定义域内，使用离散 Riccati 恒等式与二阶交叉积递推；不把有限递推代数当作圆板谱重数或超越性证明。
---

# Bessel 交叉积的离散 Riccati 递推

固定 `m in Q` 与 `x>0`，并使用
`W_m=I'_m J_m-I_m J'_m=I_{m+1}J_m+I_mJ_{m+1}` 和
`F_m=I_m/(x I_{m-1})`。调用前必须确认涉及的 modified-Bessel 分母非零；在来源的 `m in Q_{>=0}` 或整数情形、`x>0`，正性给出这一门槛。

## 可调用的代数步骤

在标准三项递推

```text
J_{m+1}=2m J_m/x-J_{m-1},
I_{m+1}=-2m I_m/x+I_{m-1}
```

下，先核对离散 Riccati 恒等式

```text
x^2 F_{m+1} F_m = 1-2m F_m.
```

随后可将相邻交叉积关系写为

```text
W_{m+1}=2m F_m W_m-(1-2mF_m)W_{m-1}.
```

因此，对已经给出的连续初值 `W_{m-1},W_m` 与满足 Riccati 关系的 `F` 数据，可逐步消去后续 `W` 项，并把共同零点条件化成关于 `x,F_m(x)` 的有限代数关系。每一步都要保存分母条件、指标偏移和所得多项式；不能把形式递推当作证明某个共同零点存在或不存在。

## 边界

这项方法不验证 Bessel 函数的零点超越性、消元多项式非零、三个指标不能同零、夹持圆板本征值重数，或任何 Schanuel 型推论。若 `x` 不在正实轴、`m` 不在来源允许范围，或未给出非零分母证明，停止在形式恒等式层面。

## 补充来源中的方法

- [Bessel cross-product recurrence](references/supp07-bessel-cross-product.md)
