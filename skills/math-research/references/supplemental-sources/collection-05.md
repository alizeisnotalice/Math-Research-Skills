# 研究方向补充的补充文献

[回到索引](README.md)。

## Cantelli_Fourier/Ion_Klaassen_VanDenHeuvel_Sharp_Chebyshev_Gauss.pdf · Sharp inequalities of Bienaymé–Chebyshev and Gauß type for possibly asymmetric intervals around the mean

- 原件。本地 arXiv:2208.08813v2（2022-10-10）；书目列正式版 DOI 10.1007/s11749-022-00844-9，未逐页比对正式版。PDF 物理页 1, 3, 5, 11, 12, 13。SHA-256 fa7a746d63ff91496ea45cf1258842568f20a587ce5bb455ef3fd9b45a4009a6。
- 形状约束的尖锐矩尾界。§2 Thm.2.2；§5 Thm.5.2--5.4；§6 Thm.6.1--6.3。对均值0、方差1变量给出不对称两侧尾的分段尖锐上界；在单峰或单峰且众数=均值等附加形状条件下，给出比一般 Chebyshev/Cantelli 更强的单侧与不对称界及达到等号的分布。
- 构件候选。一般界由平移缩放后的二阶矩界；单峰界依赖 Vysochanskiĭ--Petunin 或 Khintchine 单峰表示及随后一维优化。 仅核对本地 v2 的陈述、极值构造和证明路线；正式版文本及附录长证明未逐项复核。若建工具，须把分布类别、标准化、阈值分段和端点等号条件作为强制输入，不能泛化为任意浓缩界。

## Centered_Cube/Aubrun_Maximal_Inequality_High_Dimensional_Cubes.pdf · Maximal inequality for high-dimensional cubes

- 原件。Confluentes Mathematici 1 (2009), DOI 10.1142/S1793744209000067。PDF 物理页 1, 2, 4, 7。SHA-256 a75fbe79bfea488fc8ecc125aabee4b60c89ffb6ace3e95de1f2827cd7b2cc93。
- 高维中心立方体极大算子下界。Thm.1、Thm.2；§1.3；§2.2--2.3。对中心轴平行立方体 Hardy--Littlewood 极大算子的最佳弱(1,1)常数 Θ_n，证明任意 ε∈(0,1) 有 Θ_n≥c(ε)(log n)^(1−ε)；格点测度的坐标经验过程经 Brownian bridge、KMT 耦合和 LIL 提供大超水平集。
- 既有方法覆盖。格点计数到经验过程、Donsker/KMT 近似以及 Brownian bridge 的迭代对数律；不是一般上界证书。 正式论文仅作版本/结论核对；没有逐审 KMT 与 LIL 的外部证明。现有专项技能已要求同一中心化、归一化和全尺度弱端点核验。
- 相关入口。[math-centered-cube-endpoint-budget](../../../math-centered-cube-endpoint-budget/SKILL.md)。

## Centered_Cube/Iakovlev_Stromberg_Maximal_Function_Cubes_High_Dimensions.pdf · Lower bounds for the weak type (1,1) estimate for the maximal function associated to cubes in high dimensions

- 原件。Mathematical Research Letters 20 (2013), DOI 10.4310/MRL.2013.v20.n5.a7。PDF 物理页 1, 2, 3, 11, 12。SHA-256 76827e09e5d4ef0122945c35ba1c88881001900511aa858d44bec7306bfa02af。
- 高维中心立方体极大算子下界。§2 theorem；§§3--5；Appendix B Lemma 2。对同一中心立方体极大算子证明 A_d≥c d^(1/4)。构造整数格点乘积测度，以坐标偏中心层给出超水平集，再限制为有限测度并平滑为 L1 函数。
- 既有方法覆盖。偏中心坐标的组合计数、层交叠估计、有限截断和原子到 L1 的平滑迁移；严格/非严格阈值与几何归一化须保留。 正式论文仅核对主结论和迁移步骤；未逐审全部层交叠常数。现有专项技能已有原子下界、严格超水平集与平滑桥的审计门。
- 相关入口。[math-centered-cube-endpoint-budget](../../../math-centered-cube-endpoint-budget/SKILL.md)。

## Derrida_Retaux/Chen_Hu_Shi_Sustainability_Probability.pdf · The sustainability probability for the critical Derrida–Retaux model

- 原件。本地 arXiv:2108.05610v1（2021-08-12）；本次未比对后续期刊版。PDF 物理页 1, 2, 3, 4。SHA-256 85df56eb9355c081e97913256dd0544c16a7b271093f9c6f8283ad7c9c21ed15。
- 固定子代 DR 临界存活。Thm.A、Thm.1.2；§1 对 pivotal vertices/open paths 的说明。对固定 m≥2、整数值临界递推 X_{n+1}=(Σ_{i=1}^m X_n^(i)−1)^+，在 E[t^Y0]<∞（t>m）下得到 P(Y_n≥1)=n^(−2+o(1)) 与 E Y_n=n^(−2+o(1))。
- 既有方法覆盖。关键路线是层级树中的 pivotal-vertex 恒等式、open paths 与中间代分析；本次只核对引言所列定理和路线，未逐审证明依赖。 预印本 v1；因未提议从中新增组件，未对全部证明依赖逐条验收。现有固定二叉 DR 工具只可用于其精确模型，m/初值/指数矩条件须另行匹配。
- 相关入口。[math-discrete-proof-transfer](../../../math-discrete-proof-transfer/SKILL.md)。

## Derrida_Retaux/Chen_etal_A_Max_Type_Recursive_Model.pdf · A max-type recursive model: some properties and open questions

- 原件。本地 arXiv:1705.04787v2（2019-06-26）；书目列正式章节 DOI 10.1007/978-981-15-0302-3_6，未逐页比对。PDF 物理页 1, 2, 3, 4, 5, 6, 7, 8。SHA-256 616cefe3bbbd7ca6b52ea34b649d22b072c030f10837a313cd0f967ac81ef929。
- 固定子代 DR 生成函数与临界猜想。Thm.1--3；Conj.1--4；(7)--(19)。对固定 m 的 max-type 递推，给出临界判据与 E[m^X_n]→1；在三阶 m-加权矩有限时给出 E[m^X_n]−1 的 n^(−1) 双边界，并把 n^(−2) 存活、条件几何极限、矩和 PGF 渐近明确标为猜想。
- 既有方法覆盖。生成函数精确递推及其在 s=m 的导数不变量/乘积估计；猜想不能当作可调用结论。 仅核对本地 v2 的主定理、猜想标签和生成函数恒等式；正式章节版本及技术性乘积估计证明未逐项复核。
- 相关入口。[math-discrete-proof-transfer](../../../math-discrete-proof-transfer/SKILL.md)。

## Derrida_Retaux/Chen_etal_Derrida_Retaux_Conjecture.pdf · The Derrida–Retaux conjecture on recursive models

- 原件。本地 arXiv:1907.01601v3（2020-05-03），首页为 Submitted to the Annals of Probability；期刊版未逐页比对。PDF 物理页 1, 2, 3, 4。SHA-256 6b59863dff962960dffefafe99620f49ab276fca1a559cf61404ae01c82ce4ed。
- DR 自由能临界本质奇性。Thm.A；Thm.1.1--1.3；§1.2。对混合初值的固定 m 递推，有限 E[(X0*)^3m^X0*] 时证明自由能在 p↓p_c 的指数尺度为 exp(−(p−p_c)^(−1/2+o(1)))；重尾尾指数 2<α≤4 和 α=2 时给出不同的本质奇性尺度。
- 既有方法覆盖。临界判据后，证明使用正则性、XY coupling/bridge inequality、层级树 open paths 与截尾；本次未核对这些技术引理的完整证明链。 预印本 v3；不把所述尺度转移到随机子代、实值初值或不同尾类。现有固定二叉 DR 路由保留模型、正则性和版本核对门。
- 相关入口。[math-discrete-proof-transfer](../../../math-discrete-proof-transfer/SKILL.md)。

## Derrida_Retaux/Collet_Eckmann_Glaser_Martin_Spin_Glass_CERN.pdf · Study of the iterations of a mapping associated to a spin glass model

- 原件。本地 CERN TH.3754（1983）；文献链称有 1984 正式版，本次未取得并逐页比对。PDF 物理页 1, 3, 6, 8, 9, 14。SHA-256 c61ffad3ea72b56852782a2a20f9e31f9f23003139eed7d00809a309b2a5784b。
- 早期二元 DR 生成函数迭代。摘要；II--IV 的生成函数判据。扫描件研究概率生成函数映射的迭代，并按 F(2)−2F'(2) 的符号讨论向0/1的极限及临界情形；它是后续固定二叉 DR 临界判据的历史来源。
- 版本与引用。基于生成函数系数非负、解析延拓和导数差的迭代关系；本地 OCR 对核心公式损坏，不能从本扫描件提取精确可部署常数。 只完成身份和主题级核对；应以可读正式版重核公式、假设与页码后再作为定理来源。
- 相关入口。[math-discrete-proof-transfer](../../../math-discrete-proof-transfer/SKILL.md)。

## Derrida_Retaux/Derrida_Shi_Toy_Model_Depinning.pdf · Results and conjectures on a toy model of depinning

- 原件。本地 arXiv:2005.10208v1（2020-05-20）；书目列正式版 DOI 10.17323/1609-4514-2020-20-4-695-709，未逐页比对。PDF 物理页 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13。SHA-256 196b22e2dbfebfc19fbdb819237a8deb7293ea08dade2390ccb7fe64c6018b6b。
- DR 模型综述与开放问题。§2--§8；§10。综述固定二叉 DR 的临界存活、条件分布、PGF、自由能和树表示；明确列出 n^(−2) 常数、条件几何律和 BKT 型自由能等尚未完全解决的猜想，并区分已知较弱结果与启发。
- 版本与引用。该文主要汇总既有结果和猜想；树/open-path 表示及重尾分支依赖被引用的原始论文，非本综述的新证明组件。 不把综述中的预测转成技能定理；正式版本和所引用原始定理须在实际采用时分别核对。
- 相关入口。[math-discrete-proof-transfer](../../../math-discrete-proof-transfer/SKILL.md)。

## Derrida_Retaux/Li_Zhang_Generalized_DR_Asymptotic.pdf · Asymptotic behavior of the generalized Derrida–Retaux recursive model

- 原件。Journal of Statistical Physics 192:98 (2025), DOI 10.1007/s10955-025-03480-3；本地页同时标 arXiv:2411.13068v3（2025-08-18）。PDF 物理页 1, 2, 3, 4, 5。SHA-256 487ec3f399cdf48298d7855a4be016612235cc05b736d91da7cf791293c328fe。
- 几何子代广义 DR 的闭合族渐近。(1.3)、Thm.1.1--1.3、Cor.1.5--1.8。当子代数服从均值 m 的几何分布且初始律为几何型 G(r0,p0) 时，律族在广义 DR 递推下闭合为二维递推 (r_n,p_n)；按极限参数分出超临界、次临界和临界，并给出生存概率、矩、条件律和 PGF 的高阶渐近。
- 构件候选。决定性步骤是几何子代 PGF 与 G(r,p) 的闭合、随后二维参数递推及离散渐近分析；随机几何子代与现有固定二叉 DR 不是同一模型。 正式论文作版本/结论级核对；尚未逐审 Thm.1.1 的闭合计算及 Thm.1.3 的完整渐近证明。若建新工具，必须限定几何子代和 G(r,p) 初值，不能外推到任意子代或任意初值。
