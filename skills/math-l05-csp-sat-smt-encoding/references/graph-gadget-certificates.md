# 局部图 gadget 证书

本页收录已从下列五篇 OpenAI 预印本的本地逐页提取文本中核对的**局部**图编码。它用于把有限 CSP / projection / comparison 约束落到一个具体图实例时检查目标值转移；不验收任何全文 hardness 定理、外部起点、Fourier / PCP 解码或近似阈值。

每次使用均须重写变量域、权重、平行 occurrence、是否允许 loop、以及“固定端点后”还是“优化后”的量词。有限真值表或本页的局部等式不替代全局 soundness 证明。

## 已复核的精确 gadget

### Min-UnCut：带符号需求的奇偶路径

来源：*Constant-factor hardness of Min-UnCut*，SHA-256
`3300408a7ae8900efc7ae23fc7ae3a4678750e57de9b5d89d063ff596c710100`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Constant-factor-hardness-of-Min-UnCut-September-23-2026/paper.pdf)，§7.2–7.3，PDF/提取页 34–35，Lemma 7.2。

设原变量取符号 `y_u,y_v∈{-1,+1}`，一个单位需求为
`y_u y_v=r`，其中 `r=+1` 表示 equality，`r=-1` 表示 inequality。为每一单位需求另建私有内部顶点：

- `r=+1`：以一条 4-edge path 连接 `u` 与 `v`；
- `r=-1`：以一条 3-edge path 连接 `u` 与 `v`。

边在端点符号相同（uncut）时计一。若路径顶点依次为
`x_0,…,x_L`，uncut 边数为 `q`，则
`x_0x_L=(-1)^(L-q)`。故在固定原端点后，内部点可使该 path 的最小 uncut 数恰为

`1{y_u y_v≠r}`。

这要求不同单位需求不共享内部点；自需求也须保留为私有的 4-cycle（equality）或 triangle（inequality），而不是删去。已以穷举二元路径赋值核对：长度 4 对 equality、长度 3 对 inequality 的满足/失败最小 uncut 值分别为 `0/1`。该枚举只认证此有限 gadget。

### Permutation constraint：四边细分

来源：*The Unique Games Theorem*，SHA-256
`04d0290a9cb7ee815060f82cf556cee893d32b5255613160ca8b8d02a5fe1289`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf)，§7.1，PDF/提取页 36–37，Lemma 7.1。

对一个 occurrence 的 permutation constraint `a_v=ρ(a_u)`，以三个私有内部顶点替换为
`u--p_e--q_e--r_e--v`。从 `u` 到 `v` 的前三条边置 identity，末边置 `ρ`；若按 bipartite 的左到右方向写边，按需写逆 permutation。固定原端点标签时：

- 原 occurrence 满足，当且仅当内部标签可使 4 条边全满足；
- 原 occurrence 不满足时，最多满足 3 条边，且可达到 3 条。

因此，对已无权化的 occurrence multigraph `H'`，且每次 occurrence 均使用独立内部点，有精确恒等式

`val(B)=1-(1-val(H'))/4`。

loop 变为有三个不同内部点的四环，平行 occurrence 也因内部点私有而不合并。已枚举二元 translation 情形，得到满足时 `4/4`、违背时 `3/4` 的最优边满足数；一般 permutation 的局部论证由末边的唯一可延拓标签给出。该式不包含此前对有理 occurrence weights 的 rounding 误差；rounding 须单独估计。

### DFVS：加权顶点的整簇克隆

来源：*Constant-factor hardness of directed feedback vertex set*，SHA-256
`606657a956af61c2d133e59134ec98234d6e5386413ab601c1e7d493d1f0e4f2`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/paper.pdf)，§8，PDF/提取页 26–27，Lemma 8.1。

令 `G` 为有 `S≥1` 个顶点的**无 loop**有向图，顶点正有理成本 `w_v≤C`。置 `c_v=ceil(S w_v)`；把每个 `v` 换成独立集 `C_v`（大小 `c_v`），并把每条弧 `u→v` 换成所有 `C_u→C_v` 弧。则

`DFVS(Ĝ)=min_{F 是 G 的 DFVS} Σ_{v∈F} c_v`。

证明接口是双向的：整簇删除可提升 `G-F` 的拓扑序；反向地，对任意 `Ĝ` 的删除集 `Q`，只有整簇全删的原顶点集合 `F_Q={v:C_v⊆Q}`，若未打破原环，则从每个存活簇取一点会提升为 `Ĝ-Q` 的环。于是部分删簇不会改善最优值。并有 `S w_v≤c_v<S w_v+1`，用于**另行**控制舍入加性误差。

此 gadget 只适用于完整簇间二部弧、正成本和无 loop；不证明 rank/test-vertex 归约本身的 soundness。

## 已核对、但不是独立小 gadget 的图接口

### Max-Cut：偶/奇查询的稳定性分解

来源：*A Direct Proof of Optimal Max-Cut Hardness*，SHA-256
`32a11e793f6e379c8d750f8f3560a6b0648bee56441efd25bceea9c2b7ffb849`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/paper.pdf)，§4.1–4.2，PDF/提取页 9–10，Lemma 4.2。

仅对该文式 (4.1) 的 sampler：两份经 affine projection 的 tree-code word 查询，第二份取负，且 slice-table entries 按相关系数 `t` 耦合。将每个 cut table 分为对 `w↦-w` 的 even/odd 部分，并按右端点与 row smoothing 取文中的 `Ā_y, Ġ_y`，则有精确式

`cut(σ)=1/2 + (1/2) E Stab_t(Ġ_y) - (1/2) E Stab_t(Ā_y)`。

这里 cross terms 消失的理由是 simultaneous slice negation 对 odd 部分变号、对 even 部分不变，因而其 Fourier 支撑总奇偶性不同；`t≥0` 时 stability 非负，所以可得对应上界。不要把该恒等式迁移到任意 correlated-query 图：须逐项重验负号、两份 row resampling、切片及条件平均的独立性。

### Vertex Cover：兼容标签范数的精确邻接测试

来源：*The Factor-Two Hardness Threshold for Vertex Cover*，SHA-256
`4c8faec31a1af3d0c640485e464ecedd99fb984f4a2c3b457f032685013804ab`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/paper.pdf)，§3.1–3.2，PDF/提取页 5–8，Lemmas 3.1–3.2、Proposition 3.3。

给定 Label Cover 的局部 query-label 对 `(i,λ)`，只允许每个 query 至多一个标签、重叠变量一致、且联合 scope 内每个 source constraint 均满足的 selections `I`。定义

`||z||_* = max_{I compatible} |Σ_{(i,λ)∈I} z_{i,λ}|`。

对该文固定的 seed tuple `c` 与 grid weights `s`，顶点为 `(c,s)`，并在不同顶点 `v,w` 间当且仅当

`||S_v+S_w||_*≤2t`

置边。局部支撑至多含 `2d` 个 query blocks，故可枚举每块的“无标签或一个有效标签”并检查 overlap 与 scope 内约束；文中在固定参数下将该判据化为精确有理/整数比较。这个接口可用于审计**已给定** local-label 结构的 edge list，不自动给出独立集密度、短列表译码或 Vertex Cover gap。

## 其余组合接口与保留项

*The Unique Games Theorem* 的 §4（PDF/提取页 18–22）还给出 parity equation tuples 的 exact table keys、`K`-translation folding 与 projection pullback sharing（式 4.4–4.5）；这些是 matrix/permutation test 的表示一致性接口，不是图目标的值保持 gadget。其 §5 的 shortcode inverse theorem 是外部结构输入，未在此审计。

*Constant-factor hardness of Min-UnCut* 的 folded bit test、affine-hint outer game 与 finite Gaussian replacement（§3、§5–§7）只作为上述 path demands 的来源；本页没有验收其 inner decoding、outer soundness 或完整 gap。

*Constant-factor hardness of directed feedback vertex set* 的 rank vertices、wildcard tests、shared-prefix conditioning 和 pivotal-label budget（§§3–7）只作为 cloning 输入的来源；本页没有验收该归约由低 DFVS 解码游戏标签的全局论证。

五篇的 source contracts 彼此独立：Max-Cut 从 affine 2-to-1 输入起步，Min-UnCut 从 3Lin/equation gap 起步，DFVS 从不完美完备性的 2-to-1 输入起步，Vertex Cover 从 Label Cover 起步，Unique Games 从 parity gap 与其明确列出的外部 shortcode 输入起步。不得把它们串写为“先有 Unique Games 再自动得到其余编码”。
