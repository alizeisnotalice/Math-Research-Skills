# 有限支撑矩多面体：极点/面精确核验

本附件为 `math-b03-generalized-moments` 增添一个**有限、列举支撑**的精确核验器。它并不把有限表上的结论外推为任意 Borel/Radon 测度上的极点定理，也不把某个 Moment--SOS 松弛的可行解当作原问题的原子测度。

## 已复核来源与版本

- Didier Henrion、Martin Kružík、Stephan Weis, *Extreme points and faces in the moment problem*, [arXiv:2606.21391v1](https://arxiv.org/abs/2606.21391), 19 June 2026, 17 pages；截至 2026-11-26，arXiv 页面仅列 v1，未列正式发表版本。下载清单中的本地字节 SHA-256 为 `b77447cac7b06cc49ca166f359e0e48e9e72da6fa3047c53f13057f1d49263de`，其首页标为 `Draft of June 23, 2026`。arXiv HTML 当前页首写 `Draft of August 24, 2026`，故不能将两种排印日期或本地 PDF 与在线 HTML 视作逐字同版；下列仅用两者共同可核的有限维推论。
- 本次实际核对的证明链：Theorem 2.6 给出对单点等式约束时“最小面上的约束映射单射”等价于极点的方向；Definition 4.1 要求有限原子表示的原子互异且权重严格正；Definition 4.4 与随后定理把原子像的仿射独立性用于有限个矩约束；Corollary 4.15 对有限原子、单点矩目标给出等价。该论文的更一般必要方向还需要其关于 `Q` 是概率单纯形面、极端点/拓扑与可积性的假设，未由本程序声称。

可审计的在线定位：arXiv HTML v1 §2, Theorem 2.6；§4.1 Definition 4.1、Definition 4.4、其后极点充分定理及 Corollary 4.15；§4.2 Theorem 4.21。该来源是预印本，故本附件不依赖其未逐行复核的无限维推广。

## 精确有限模型与判据

输入一个**已经列完的**原子集合 `x_0,...,x_{n-1}`，以及每个原子的矩向量 `m(x_i) in Q^d`。程序处理的可行集严格为

\[
  P(b)=\{w\in\mathbb R^n: w_i\ge0,\quad A w=b,\quad G w\ge r\},\qquad
  A_{\bullet i}=(1,m(x_i))^\mathsf T,
\]

其中首行是质量归一化，`b=(1,q)^T`。没有额外不等式时，若给定可行 `w`，令 `S={i:w_i>0}`，则

\[
  w\in\operatorname{ext}P(b) \Longleftrightarrow
  \{A_{\bullet i}:i\in S\}\text{ 线性无关}.
\]

这是有限矩阵事实：任意中点分解的差 `h` 满足 `Ah=0`，并且 `w_i=0` 与两端非负性一起迫使 `h_i=0`；所以仅须在严格正支撑上检查核。若还给出线性不等式 `Gw>=r`，每一个在 `w` 取等号的行也必须满足 `g h=0`。因此一般精确判据是：把 `A`、零质量坐标行与所有活跃不等式行叠成 `M_active`，则 `w` 为极点当且仅当 `M_active` 满列秩。反过来，若其有非零核向量 `h`，选

\[
  \epsilon=\min_{h_i\ne0} w_i/|h_i|>0
\]

并同时以每个非活跃不等式的松弛量限制 `epsilon`，即可得到两个不同的可行点 `w+epsilon h`、`w-epsilon h`，以 `w` 为中点。程序输出整个有理证书。

这也解释两种常见误用：

- **冗余矩行不增加极点能力。** 例如同时给出 `E[X]` 与 `E[2X]`，精确 RREF 会忽略第二个秩贡献；不得以“约束条数”代替矩阵秩。
- **零质量原子不是支撑点。** `w_i=0` 是非负性约束的活跃坐标；它不应计入仿射独立支撑。`face_zero_indices` 只核验所声明的坐标面成员资格，不会人为限制全局多面体中的中点分解。

## 使用方式

```sh
python3 scripts/finite_moment_face.py examples/nonextreme_redundant_moments.json
python3 scripts/finite_moment_face.py examples/extreme_with_active_zero.json
```

输入只能使用 JSON 整数或字符串有理数（如 `"-3/7"`）；浮点数被拒绝。输出中的 `extreme`/`not_extreme` 只针对上式的**固定有限原子表、显示的线性等式/不等式与坐标非负性**。若有未列举的连续支撑、严格正密度、绝对连续性、非线性形状条件，或底层测度空间的 `C` 不是已转化的有限多面体，必须回到 B03 的一般条件检查；不能直接套本判据。
