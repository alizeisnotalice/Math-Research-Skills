---
name: math-l07-noncommutative-matrix-tests
description: 对非交换公式或无环路径程序，按特征、是否含逆门及树模型选择有理/有限域矩阵 hitting point 或 hitting list，并核验截断字级数与 affine-pencil 定义域条件。不要用于共享电路或未承诺的 rational expression。
---

# 非交换矩阵测试

本技能把 Family 116 的三篇预印本中可定位的构件组织为一个三路接口。先写明：系数域、特征、变量数 `n`、size 上界 `s`、表达式是否为**树**、是否有逆门，以及所需的是构造、单次求值还是 identity 证明。

## 路由

| 输入模型 | 使用的矩阵测试 | 不能省略的条件 |
| --- | --- | --- |
| characteristic zero，division-free noncommutative formula | 一个由 `n,s` 决定的有理矩阵 tuple | 公式树；系数可在任意特征零域。 |
| positive characteristic `p`，division-free formula | `F_p` 上一个 tuple | `p` 是承诺的素数；`n,s` 按原文的一元参数；公式树。 |
| `Q` 上含 inverse gates 的 rational formula | 有理 matrix **list** | 每个 inverse gate 必须在命中点可逆；表达式须 admissible 且为树。 |

无环 algebraic path program 可走前两条 division-free 路由，其 size 参数改为顶点数。共享子表达式的 arithmetic circuit 不在三篇的保证内；不得把 formula 的 size 界移植到 circuit。含逆门的 ABP、非 `Q` 有理公式、复用 DAG 或未承诺定义域，先停止并另行证明化约。

## 已直接核验的截断接口

在特征零的 division-free 路由中，取

```text
J_i(a)(z) = integral_0^z a(t)/(t+i) dt
(T_i)[r,q] = (-1)^(r-q-1) / (r*i^(r-q))    for 0 <= q < r < d,
             0                                otherwise.
```

对字 `w=i1...ik`，以右端先作用的矩阵积计算
`T[i1] ... T[ik] e0`；它是 `h_w=J_i1 ... J_ik(1)` 的前 `d` 个 Taylor 系数。运行下列有限精确重放，确认索引、乘法方向和交换子符号：

```sh
python3 scripts/replay_truncation.py --dimension 7
```

该重放只验证截断公式及 `x1*x2-x2*x1` 的有限例子；它**不**证明 universal hitting 定理。若把矩阵维度取为原文的 size 函数，必须同时满足其字级数线性无关和消失阶界的假设，见 [来源与界限](references/sources.md)。

## 含逆门的定义域纪律

对每个 inverse-node occurrence 建立其 affine pencil。先验算所有逆门 pencil 同时可逆，按树递归保证原公式在该点有定义。另设根的 augmentation pencil。它的 Schur 补为根值取负，故其可逆性还保证根值可逆。一个已定义但奇异的非零矩阵值也足以给出单点非零证据。

候选点上记录 tuple 编号、各逆门是否可逆、根值的一个精确非零条目及底域。来自原文构造的完整有理 list 使用根增强来认证命中。只有 list 的全类保证及其适用条件已经建立时，所有点未命中才可作为恒等证据。任意自选的有限样本可以搜索非零见证。


## 证据范围

三个主结论来自尚待 scholarly review 的本机预印本；本技能固定其版本和页码，但不把它们升级为独立认证结论。实际实现时报告所走路由、模型承诺、矩阵维度、精确域、命中/未命中及哪些源稿定理被条件性采用。固定来源、可复用命题及不适用边界见 [来源与界限](references/sources.md)。
