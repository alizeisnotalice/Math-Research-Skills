# 专项数学方法

按对象找到可调用的证明构件和精确检查器。先核对输入及来源的适用范围。

## 欧拉常数、丢番图逼近与算术

- [math-harmonic-sum-recurrences](../../math-harmonic-sum-recurrences/SKILL.md) · 用精确有理算术生成和核对广义超调和数的有限系数。适用于需要把嵌套调和定义化为有限递推、初等对称和或普通调和数的场景；不用于无限 Euler 和、zeta 值化简或无理性结论。
- [math-dirichlet-l-derivative-sine-reduction](../../math-dirichlet-l-derivative-sine-reduction/SKILL.md) · 对给定偶周期有理数据，精确生成 Dirichlet 型级数在零点导数的形式对数权重。核对周期、对称性、零索引和分母。
- [math-euler-series-continued-fraction](../../math-euler-series-continued-fraction/SKILL.md) · Convert a finite nondegenerate rational series segment to Euler generalized continued-fraction data exactly. Use for finite algebraic identity checks, not for convergence or irrationality claims.
- [math-mzv-newton-harmonic-relations](../../math-mzv-newton-harmonic-relations/SKILL.md) · Check finite Newton/binomial duality for positive multiple-harmonic indices exactly. Use to prepare finite inputs for Kawashima-type MZV relations, not to prove MZV independence or Euler-constant claims.
- [math-zeta-arithmetic-estimates](../../math-zeta-arithmetic-estimates/SKILL.md) · 根据指定的 ζ 函数采样、平滑核和参数区间接入等差级数矩比较与光滑数零点修正。适用于检查扭权、测量模型和误差来源。
- [math-function-field-period-transcendence](../../math-function-field-period-transcendence/SKILL.md) · 在已给定的正特征 Drinfeld 模、t-motive 与解析平凡化数据下，定位周期、准周期、第三类周期和 Carlitz 张量周期的条件性超越/代数独立接口。
- [math-euler-constant-irrationality](../../math-euler-constant-irrationality/SKILL.md) · 研究欧拉–马歇罗尼常数 γ 的无理性。构造或审计 γ 的 Padé、多重正交、超几何、递推、整数线性形式、分母消去与 Sondow 型判据，也用于核对 E/G 函数、算术 Gevrey 与 Stokes 常数方法能否转移到 γ。
- [math-sondow-log-fractional-certificate](../../math-sondow-log-fractional-certificate/SKILL.md) · 从 Sondow 的双积分与对数线性形式构造可严格计算的欧拉常数分母排除证书。用于生成 S_n 对数权重、认证分数部分阈值、估计余项或寻找使判据在无穷多个指标成立的方法。
- [math-gamma-continued-fraction-recurrence](../../math-gamma-continued-fraction-recurrence/SKILL.md) · 用精确递推生成并审查 Hessami Pilehrood 的欧拉常数有理逼近与非简单连分数。适用于有限系数、收敛子和分母高度核对，不用于无理性结论。
- [math-gamma-gregory-series-interval](../../math-gamma-gregory-series-interval/SKILL.md) · 用 Gregory 系数的 Fontana–Mascheroni 级数计算欧拉常数 γ 的严格有理区间，核对精确系数、剩余质量和给定有理候选。
- [math-gamma-meijer-cmf](../../math-gamma-meijer-cmf/SKILL.md) · 用 Kalisch 等的 Meijer G 保守矩阵场构造欧拉常数 γ 的 Apéry 型候选逼近。复跑已知三阶轨迹，核对对偶矩阵、CVM 换基、收敛判据和约分后的算术质量。
- [math-gamma-multiple-laguerre-approximants](../../math-gamma-multiple-laguerre-approximants/SKILL.md) · 用 Wolfs–Van Assche 的混合型多重 Laguerre 显式有限和生成欧拉常数有理逼近，并审计算术整化、约分、余项和渐近障碍。
- [math-openai-arithmetic-determinants](../../math-openai-arithmetic-determinants/SKILL.md) · 从 OpenAI 算术预印本提取 Taylor 接触消元、整数多项式行构造、行列式算术下界与解析上界比较。用于设计或审查 Catalan 常数、π 与欧拉常数研究中的行列式候选。
- [math-alternating-reciprocal-criteria](../../math-alternating-reciprocal-criteria/SKILL.md) · 用 Sondow 的交错倒数和—连分数判据，严格区分可证明的无理性、有限前缀核验，以及需要整条简单连分数假设的超越性结论。适用于 Pierce 展开或快速增长分母的交错倒数和；不用于仅凭数值近似宣称无理或超越。
- [math-integer-linear-form-rates](../../math-integer-linear-form-rates/SKILL.md) · 用已经证明的整数线性形式高度与双边余项界，生成给定分母的有理逼近下界或推导无理性指数上界。适用于核对 Apéry 型证据和同时逼近的非消失条件。
- [math-hankel-pade-certificates](../../math-hankel-pade-certificates/SKILL.md) · 对整数幂级数做精确 Hankel 行列式与 Padé 有限证书，核验正矩投影的有理下界，并审计 Mahler–Hankel 定理的独立准入门槛；不以有限计算断言超越性或无理度指数。

## 调和分析、动力系统与几何方程

- [math-bessel-cross-product-recurrence](../../math-bessel-cross-product-recurrence/SKILL.md) · 在已给定的 Bessel/modified-Bessel 定义域内，使用离散 Riccati 恒等式与二阶交叉积递推；不把有限递推代数当作圆板谱重数或超越性证明。
- [math-subanalytic-preparation](../../math-subanalytic-preparation/SKILL.md) · 用明确给定的次解析族、泛参数域和纤维模型整理有理幂次展开与边界余项；记录常数和阈值的参数依赖。
- [math-asymptotic-midpoint-moduli](../../math-asymptotic-midpoint-moduli/SKILL.md) · 在已认证的树、段森林或 Daugavet-L1 结构上，调用渐近中点模量与可数分支 diamond 失真界；不把有限算术或抽象范数当作结构证书。
- [math-conformal-domain-estimates](../../math-conformal-domain-estimates/SKILL.md) · Manage gated conformal-domain coordinate-energy and univalent inverse-integral-means transfers. Use only with the specified normalization, boundary, and source-model hypotheses; not for arbitrary holomorphic maps or planar compactness.
- [math-tube-maximal-transfer](../../math-tube-maximal-transfer/SKILL.md) · Transfer a specified three-dimensional tube or curved extension packet estimate through its declared maximal, capacity, and level-set interfaces. Not a generic Kakeya, restriction, or incidence certificate.
- [math-centered-cube-endpoint-budget](../../math-centered-cube-endpoint-budget/SKILL.md) · Audit or extend centered axis-parallel cube Hardy–Littlewood weak-(1,1) bounds: all-scale source/receiver budgets, joint high-capacity remainders, and finite-dimensional square/cube certificates. Use for centered-cube-upper-bound, the Round 830 remainder, or cubical endpoint constants; not for Euclidean balls, Kakeya tubes, or strong rectangular maxima.
- [math-euler-maclaurin-quadrature-certificates](../../math-euler-maclaurin-quadrature-certificates/SKILL.md) · 为满足端点消失条件的多项式 Euler--Maclaurin 求积构造精确余项与可复核误差包围；不用于未经认证的一般浮点积分。
- [math-hbl-finite-presentation](../../math-hbl-finite-presentation/SKILL.md) · 对已给定的有理有限子空间图和边权，精确核验 HBL 有效表示并分解平衡边流；不搜索表示或计算一般 HBL 常数。
- [math-torus-packet-spectral-density](../../math-torus-packet-spectral-density/SKILL.md) · 对给定有理分段仿射扭转与有限角向 Fourier 包，精确计算模一推前的阶梯谱密度、色间正交门槛和可选 L1 密度差。
- [math-cat0-inductive-barycenters](../../math-cat0-inductive-barycenters/SKILL.md) · Transfer a finite centred distribution in a complete CAT(0) metric cone into an inductive-barycenter energy bound, with exact Euclidean finite-support replay. Use for certified cone geometry, not generic group-action or sampling claims.
- [math-geometric-pde-reductions](../../math-geometric-pde-reductions/SKILL.md) · 核对给定几何模型的高度方程、标量曲率归一化、Neumann 能量、径向 ODE 不变域、弱流代表元和单相极小子的维数归约。 包含固定顶点倾斜比较与给定加权幂零坐标的局部检查。
- [math-lattice-heat-asymptotics](../../math-lattice-heat-asymptotics/SKILL.md) · Prove and safely use the first large-time correction for the continuous-time nearest-neighbor lattice heat kernel. Use for the exact dispersion 2(1-cos k), tensor-product dimensions, and clearly separated physical scaling.
- [math-lienard-half-arc-matching](../../math-lienard-half-arc-matching/SKILL.md) · 将已验证的 Lienard 半平面弧坐标匹配转化为周期轨道与孤立零点问题；不用于未经认证的数值积分或周期数上界。

## 算子代数、上同调与代数几何

- [math-holomorphic-local-to-global-transfer](../../math-holomorphic-local-to-global-transfer/SKILL.md) · Transfer specified holomorphic local data to descent, gluing, integrability, or universal-cover product conclusions only after the matching geometric gate has been established. Not for arbitrary local charts or holomorphic distributions.
- [math-algebraic-transfer-certificates](../../math-algebraic-transfer-certificates/SKILL.md) · 核对已给定的余留映射、整系数转移、链提升、格拼接或有限对称张量资料。适用于 Gersten 与 Milnor 障碍、升 HNN 扩张的同调输入和纤维函子条件。
- [math-ag-divisor-intersection-ledger](../../math-ag-divisor-intersection-ledger/SKILL.md) · 对已给定的精确除子、公共解消与交叉数表核验局部代数几何接口；不构造几何对象或采纳丰度/Iitaka 主定理。 支持点吹起中零循环的整系数推拉。
- [math-cohomological-transfer](../../math-cohomological-transfer/SKILL.md) · 核验链复形权截断、Mayer–Vietoris 条件、图状神经上链延拓以及已给代数或谱数据上的局部化与张量消失。
- [math-f2-group-ring-cancellation](../../math-f2-group-ring-cancellation/SKILL.md) · Verify a finite characteristic-two group-ring cancellation certificate from two labelled components and a supplied exact group-label product oracle; it does not establish torsion-freeness or nonzero factors.
- [math-nonarchimedean-analytic-transfer](../../math-nonarchimedean-analytic-transfer/SKILL.md) · 在完备非阿基米德环境中，核对有理或形式的有限阶解析 jet 转移、近似根余项及稠密压缩逆塔上的 Roos 差分。
- [math-operator-algebra-certificates](../../math-operator-algebra-certificates/SKILL.md) · 核验算子代数中的幺正压缩修复、平移卷积核、谱相位迹、自伴谱编码及 C* 截断转运。按已给投影、严格谱隙、迹或比较见证选择。
- [math-projective-induction-cocycle-certificates](../../math-projective-induction-cocycle-certificates/SKILL.md) · 用有限 Cayley 表和有理相位精确核验图子群上的射影诱导校正、乘子、代表元变换和有限指标维数。
- [math-weil-deligne-purity-lfactor](../../math-weil-deligne-purity-lfactor/SKILL.md) · Certify the local L-factor half-plane and Frobenius determinant consequence of supplied pure weight-zero Frobenius-semisimple Weil–Deligne data. Use only after the Weil–Deligne representation, inertia invariants, and purity witnesses have been established externally.

## 图、组合、博弈与复杂性

- [euclidean-tensor-geometry](../../euclidean-tensor-geometry/SKILL.md) · Apply or audit OpenAI family 379 Euclidean tensor prices, Strassen spectral invariants, and common-placement network bounds in arithmetic complexity and combinatorics. 中文触发：欧几里得张量几何、张量价格、渐近谱、跨割下界。Do not use for generic tensor numerics or classical maximal operators without a proved model bridge.
- [math-discrete-proof-transfer](../../math-discrete-proof-transfer/SKILL.md) · 为固定二叉 Derrida–Retaux/H3、连续 Cantelli、自由边界方格双峰 A022、非负因子 A30/A175、布尔 Fourier 谱维数 A28/A165 审核可迁移引理并制作可独立核验的证书。另用于周期图的有限连通分支与例外顶点预算。不要因同名 Fourier、稳定性或张量术语就迁移结论。
- [math-bimatrix-kite-mixing](../../math-bimatrix-kite-mixing/SKILL.md) · 核验双矩阵博弈的后悔值、s-kite 条件与精确最佳回应混合。适用于已有候选策略的局部改进与有限证书，不把尚未独立复核的全局近似 Nash 声明当作可用定理。
- [math-logrank-rectangle-rank-halving](../../math-logrank-rectangle-rank-halving/SKILL.md) · 从有限 Boolean 通信矩阵的单色矩形出发，精确核验互补块秩分裂，并把给定矩形或协议分割转为 rank-halving 递归证书。用于审计 Log-Rank 路线的有限接口，不搜索大矩形或认证高秩渐近定理。
- [math-edge-deck-reconstruction-audit](../../math-edge-deck-reconstruction-audit/SKILL.md) · 审计有限简单图的无标号单边删除卡组，精确比较候选反例并核对边重构定理的图类和密度门槛。适用于小图枚举、边卡组断言和来源结论的适用范围检查。
- [math-honeycomb-finite-boundary-flux](../../math-honeycomb-finite-boundary-flux/SKILL.md) · 在有限、单连通蜂窝三角形域中认证零环权重的带相位边界通量恒等式及凸域正性界；不用于条带渐近、桥质量或一般自避游走。
- [math-clique-free-random-multiplier](../../math-clique-free-random-multiplier/SKILL.md) · Construct and exactly check the finite-support random multiplier from the clique-free neighborhood recursion for a supplied finite weighted K_r-free graph.
- [math-grid-piecewise-translation-embedding](../../math-grid-piecewise-translation-embedding/SKILL.md) · Certify a finite cellwise translation embedding between two strict-size subsets of a specified square cell grid. Use after a geometric argument has supplied an allowable common grid; it does not polygonize sets or prove a general equidecomposition theorem.
- [math-three-strip-token-bound](../../math-three-strip-token-bound/SKILL.md) · Certify the finite three-strip/token boundary bound for a sequence of equal-cardinality planar threshold cuts with matched exchanges; not a halving-line asymptotic solver.
