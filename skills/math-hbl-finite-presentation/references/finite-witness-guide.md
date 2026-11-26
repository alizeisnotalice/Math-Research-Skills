# 有限有理 HBL 证人的精确范围

## 已核原始来源与版本

本构件来自 Philip T. Gressman, *Finiteness of the Hölder--Brascamp--Lieb Constant Revisited*, `arXiv:2503.15656v1`（2025-03-19，19 页）。本地候选原件 SHA-256 为 `bea725db0a35d152930d77f874ce61c2fec93beebea024c8f32bd5d192244d1a`。2026-11-26 核对的主 arXiv 记录只列 v1，并仅有 arXiv/DataCite DOI `10.48550/arXiv.2503.15656`；未把它当作已发表期刊版本。

阅读定位：定义在 PDF 物理页 2--3（HTML §1，图分解、平衡权和 valid presentation），Theorem 1 在物理页 3；Proposition 1 的有限链分解在物理页 9--10（HTML §2.1）；由 valid presentation 给出有限 HBL 常数的因子分解在物理页 12--13（HTML §2.3）。原文 Theorem 1 的完整双向结论依赖其后续解析论证；本工具只机械核验一个已提供的有限证人。

## 输入的严格语义

`ambient_dimension=d` 表示 (H=\mathbb R^d)。每个 `vertices[].basis` 是该子空间的**行向量**生成集（可以冗余）；每个 `maps[].matrix` 是 (\pi_i:H\to H_i) 的矩阵；`theta[map_id][edge_id]` 和 `tau` 必须是整数或形如 `"p/q"` 的精确有理数。每条边必须从 (V) 指向包含 (V) 的、秩恰多 1 的子空间。除 `0`/`H` 外的顶点分别必须有入/出边。

工具逐一检查：

1. 每个 θᵢ 非负、在中间顶点平衡、从 `0` 流出的总质量等于 τᵢ；
2. 对边 (V\subset W)，以有理高斯消元判定 \(\pi_i(V)\ne\pi_i(W)\)；
3. 只在该像变的边上相加 θᵢ，所得 σ 也必须平衡且总质量为 1；
4. 若以上均通过，对每一个标量 θᵢ 给出精确的 `0→H` 链流分解并逐边重构复核。

第 4 项是对 Gressman Proposition 1 的可执行有限情形：正流进入中间顶点时，平衡和非负性保证可选一条正流继续；每轮减去路径上的最小正有理权，至少消去一条正边，所以有限终止。

## 可得结论与不可得结论

若输入准确编码实线性数据且结果为 `valid: true`，它是对原文定义中 finite valid presentation 前提的精确核验；可将“该给定证人通过”与原文的 valid-presentation ⇒ finite-constant 方向并列引用。此脚本本身没有实现归一化 edge-function 的可测性/积分因子分解，因而不输出常数 (C)，也不自行代替原文的解析证明。

`valid: false` 只否定**这份编码的候选证人**，绝不否定别的图表示，也不证明 HBL 常数无穷。一般实矩阵或数值矩阵的“秩”不是本脚本的输入域；转换为有理模型前须给出严格误差/等式证书。零权允许且会在链分解中省略；冗余基允许，因全部子空间测试均按有理行秩进行。
