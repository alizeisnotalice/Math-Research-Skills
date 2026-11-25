---
name: math-n10-dirichlet-slab-energy
description: 用中心高斯路径相关估算凸域加入多条带约束的 Dirichlet 本征值代价，并由所有对角权重的界构造同一个逐坐标能量见证。
---

# N10 · Dirichlet 条带能量

- 添加线性条带约束时，先固定 Rayleigh 商中的矩阵 Q 和 Brownian 运动的协方差率 2Q。用内缩的闭凸约束应用高斯相关，并以更小的开条带分别估计生存率。见[加条带的代价](references/dirichlet-energy.md)。
- 当每个正对角权重各有一个 Rayleigh 商见证，但目标要求同一个函数控制全部偏导时，把坐标能量的上闭集做有限维分离。用平方密度插值证明其凸性，用固定有界支撑的 Sobolev 紧性证明闭性。
