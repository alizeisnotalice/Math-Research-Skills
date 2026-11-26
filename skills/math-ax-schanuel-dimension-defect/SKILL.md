---
name: math-ax-schanuel-dimension-defect
description: 对已明确的平坦联络、模 j、Hodge 周期映射或矩阵指数数据，选择相应 Ax--Schanuel 维数缺陷定理并核对不可省略的几何前提。
---

# Ax--Schanuel 维数缺陷分流

本技能适用于调用方已经给出代数几何对象、解析分支或叶、相关 Zariski 闭包和其维数的情形。先选定一个模型，再读取相应来源接口。它输出可引用的“严格维数缺陷蕴含特殊投影”结论，前提缺失时只报告缺失项。

## 模型选择

- 给定 \(G\)-主丛、平坦联络、水平叶和稀疏微分 Galois 群，读[平坦联络](references/ext0085-flat-principal-connection.md)。
- 给定 \(\mathfrak H^n\) 上的 \(j\) 图或其二阶 jet，读[模 \(j\)](references/ext0094-modular-j.md)。
- 给定纯极化整变 Hodge 结构及周期映射，读[纯 VHS](references/ext0097-pure-vhs.md)。
- 给定可容许分级极化混合变 Hodge 结构及混合周期映射，读[混合 VHS](references/ext0098-mixed-vhs.md)。
- 给定含原点的矩阵指数双代数子簇，读[\(GL_n\) 矩阵指数](references/ext0103-matrix-exponential.md)。

维数不等式的方向由具体模型决定。不得把一个模型中的环境维数、群维数、紧对偶维数或双代数像维数移植到另一个模型。有限样本、近似维数、数值矩阵指数或有限个函数值不能认证解析分支、不可约性、Zariski 闭包、特殊子簇排除或微分 Galois 群。

## 调用前的最小清单

记录所用预印本版本、代数环境、解析对象、闭包所在空间、每个维数和“特殊”定义。核对所有严格不等式、指定投影和结论中的特殊子簇类型。使用源文定理时保留其证明所依赖的定义性、体积、点计数、主丛或标量 Ax--Schanuel 输入。

没有完整的模型数据时，保留为来源引用或候选方法。不要从本技能推导点值的代数独立性、Schanuel 猜想、一般方程可解性或可计算的特殊子簇识别器。
