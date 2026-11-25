# 数学方法索引

先检索当前问题的对象与方法，只读取相关技能。以下描述用于选路，具体定理与假设以技能及原文为准。

## A · 归一化、外放松与紧性

- [math-a01-fractional-normalization](../../math-a01-fractional-normalization/SKILL.md)：审查齐次归一化与分式规划中的正分母、Charnes–Cooper 变换、松弛方向及达到条件。
- [math-a02-outer-relaxation-budget](../../math-a02-outer-relaxation-budget/SKILL.md)：构造或审查外放松映射，核对正支配、约束保持、界方向和误差预算。
- [math-a03-compactness-concentration](../../math-a03-compactness-concentration/SKILL.md)：分析近极值序列的紧性、集中、逃逸与极限传递，核对归一化和质量保持。
- [math-a04-shared-nonanticipative-mip](../../math-a04-shared-nonanticipative-mip/SKILL.md)：审查共同选择的混合整数模型与非前视约束，检查不同情形是否由同一决策实现。
## B · 对偶、矩问题与交换

- [math-b01-lagrange-farkas](../../math-b01-lagrange-farkas/SKILL.md)：推导或核验 Lagrange 对偶与 Farkas 证书，检查约束资格、对偶方向及不可行性证据。
- [math-b02-semi-infinite-exchange](../../math-b02-semi-infinite-exchange/SKILL.md)：处理半无限规划与约束生成，核对分离子问题、交换步骤、停止条件和全域覆盖。
- [math-b03-generalized-moments](../../math-b03-generalized-moments/SKILL.md)：用广义矩问题组织概率或解析界，核对矩约束、对偶多项式和达到条件。
- [math-b04-qualification-facial-minimax](../../math-b04-qualification-facial-minimax/SKILL.md)：检查约束资格、面约化及极小极大交换，定位强对偶或量词交换所需的假设。
## C · 锥规划、SOS 与全局优化

- [math-c01-semidefinite-lifting](../../math-c01-semidefinite-lifting/SKILL.md)：审查半定提升的建模、秩约束与松弛方向，区分 SDP 界和原问题可行解。
- [math-c02-completely-positive-copositive](../../math-c02-completely-positive-copositive/SKILL.md)：分析完全正锥和共正锥表述，核对锥对偶、有限近似及最优性证书范围。
- [math-c03-moment-sos-certificates](../../math-c03-moment-sos-certificates/SKILL.md)：构建或核验矩与 SOS 层级，检查正多项式证书、截断阶数、紧性和解恢复。
- [math-c04-branch-and-bound](../../math-c04-branch-and-bound/SKILL.md)：组织分支定界中的可行界、松弛界、剪枝和终止证书，检查全局覆盖。
## D · 输运、熵与自由能

- [math-d01-kantorovich-duality](../../math-d01-kantorovich-duality/SKILL.md)：核验 Kantorovich 输运对偶及势函数，检查代价、可积性和原始对偶可行性。
- [math-d02-gibbs-entropy-duality](../../math-d02-gibbs-entropy-duality/SKILL.md)：推导 Gibbs 变分与熵对偶，检查参考测度、归一化、有限熵和等号条件。
- [math-d03-parameterized-free-energy](../../math-d03-parameterized-free-energy/SKILL.md)：分析指定参数的自由能弱式，核对参数范围、变分方向和与目标问题的接口。
- [math-d04-entropy-chain-rule](../../math-d04-entropy-chain-rule/SKILL.md)：使用熵链式分解分析联合与条件分布，核对可测性、条件核和积分合法性。
- [math-d05-finite-block-matrix-entropy](../../math-d05-finite-block-matrix-entropy/SKILL.md)：为有限维三块 Gram 矩阵核验零块熵下界，使用 log-det 表示、Schur 补和符号平均分离块内熵与标量熵。
## E · 占用测度、Bellman 与停止

- [math-e01-occupation-measure-flow-lp](../../math-e01-occupation-measure-flow-lp/SKILL.md)：建立占用测度、有限时域概率流和流守恒 LP，核对真实过程、边界通量、终止时刻、风险原子与可实现性。
- [math-e02-nonlocal-hjb-supersolution](../../math-e02-nonlocal-hjb-supersolution/SKILL.md)：构造或审查非局部 HJB 超解，核对生成元、边界条件与验证不等式方向。
- [math-e03-tree-bellman-cross-layer-budget](../../math-e03-tree-bellman-cross-layer-budget/SKILL.md)：分析树 Bellman 跨层预算势，核对层间递推、公共预算与终端结算。
- [math-e04-snell-envelope-optimal-stopping](../../math-e04-snell-envelope-optimal-stopping/SKILL.md)：处理最优停止与 Snell 包络，核对滤过、可积性、停止时及极限传递。
- [math-e05-mean-payoff-potential-certificates](../../math-e05-mean-payoff-potential-certificates/SKILL.md)：为有限确定性二人均值收益博弈构造或审查权重扰动、闭合势函数区域及逐路径高低收益证书；不用于认证求解复杂度或随机博弈结论。
- [math-e06-online-metric-lazy-following](../../math-e06-online-metric-lazy-following/SKILL.md)：将任意按请求可见的 k-server 模拟配置轨迹转为强惰性实际服务，并以最小匹配势逐路径核验移动账本；不用于断言全局竞争比或构造模拟轨迹。
## F · Fourier、谱与平方函数

- [math-f01-geometric-mean-kernel-two-winner-audit](../../math-f01-geometric-mean-kernel-two-winner-audit/SKILL.md)：审查几何平均核与两赢家分支估计，检查同输入耦合和分支选择条件。
- [math-f02-tensor-fourier-positivity-soft-square-supremum](../../math-f02-tensor-fourier-positivity-soft-square-supremum/SKILL.md)：核验张量 Fourier 正性及软度平方上确界估计，区分频域正性与所需最大界。
- [math-f03-hilbert-schmidt-radial-layer-square-envelope](../../math-f03-hilbert-schmidt-radial-layer-square-envelope/SKILL.md)：审查 Hilbert–Schmidt 径向层叠与平方包络，检查层间求和和核的适用条件。
- [math-f04-poisson-gamma-abel-square-function](../../math-f04-poisson-gamma-abel-square-function/SKILL.md)：使用 Poisson–Gamma 与 Abel 平方函数方法，核对参数积分、权重和接口条件。
- [math-f05-l2-spectral-parameter-schur-test](../../math-f05-l2-spectral-parameter-schur-test/SKILL.md)：推导 L² 谱参数估计与 Schur 检验，检查核界、测度、权重和常数依赖。
- [math-f06-menshov-rademacher-maximal-partial-sums](../../math-f06-menshov-rademacher-maximal-partial-sums/SKILL.md)：核验 Rademacher–Menshov 最大部分和估计，检查正交性、索引与对数损失。
- [math-f07-marcinkiewicz-zygmund-vector-extension](../../math-f07-marcinkiewicz-zygmund-vector-extension/SKILL.md)：审查 Marcinkiewicz–Zygmund 向量值延拓，核对算子类型、指数范围和随机化条件。
- [math-f08-matrix-trace-energy](../../math-f08-matrix-trace-energy/SKILL.md)：核验有限维 PSD Gram 矩阵的 \(\operatorname{tr}(P^{3/2})\) Hessian、Loewner 比较与正能量望远镜，并在需要时检查有限维 trace Young 等号。
- [math-f09-positive-resolvent-densities](../../math-f09-positive-resolvent-densities/SKILL.md)：在凸数值域上构造或审计正的边界 resolvent 密度与共同压缩表示，核对外部坐标、度量收缩和所有系数尺寸的量词。
## G · Carleson 与树结构

- [math-g01-carleson-measure-box-and-tent-test](../../math-g01-carleson-measure-box-and-tent-test/SKILL.md)：检验 Carleson 测度的盒、帐篷与嵌入条件，核对几何族、尺度及常数。
- [math-g02-outer-lp-size-and-tree-stopping](../../math-g02-outer-lp-size-and-tree-stopping/SKILL.md)：使用外测度 Lp、大小函数和树停止方法，核对外测度结构与嵌入假设。
- [math-g03-directional-capture-tree-quadratic-audit](../../math-g03-directional-capture-tree-quadratic-audit/SKILL.md)：审查方向性捕获树的二次型及来源算子，核对方向、选择器和耦合结构。
- [math-g04-rubio-de-francia-square-function-scope-check](../../math-g04-rubio-de-francia-square-function-scope-check/SKILL.md)：核验树上 Rubio de Francia 平方函数估计的适用范围与频率几何条件。
- [math-g05-tree-carleson-square-function-tc-a4-audit](../../math-g05-tree-carleson-square-function-tc-a4-audit/SKILL.md)：审查 TC-A4 Carleson 型平方函数界，核对树结构、输入范围和具体假设。
## H · 中偏差与指数倾斜

- [math-h01-uniform-cramer-moderate-deviations](../../math-h01-uniform-cramer-moderate-deviations/SKILL.md)：核验一致 Cramér 中偏差和三角阵尾估计，检查一致参数范围、矩条件和误差。
- [math-h02-exponential-tilting-saddlepoint](../../math-h02-exponential-tilting-saddlepoint/SKILL.md)：分析指数倾斜与鞍点尾近似，核验鞍点、精确倾斜恒等式、Mills 界及误差范围。
- [math-h03-fan-grama-liu-martingale-expansion](../../math-h03-fan-grama-liu-martingale-expansion/SKILL.md)：应用或审查 Fan–Grama–Liu 鞅展开，核对条件矩、滤过及展开误差。
- [math-h04-exact-rate-function-variance-strata](../../math-h04-exact-rate-function-variance-strata/SKILL.md)：计算或核对精确率函数与方差分层，保持参数域和各层尾估计的一致性。
- [math-h05-chernoff-hoeffding-bernstein](../../math-h05-chernoff-hoeffding-bernstein/SKILL.md)：选择和核验 Chernoff、Hoeffding、Bernstein 尾界，检查独立性、矩条件和常数。
## I · 滤过、补偿与随机占用

- [math-i01-ordered-increment-conditional-bernstein](../../math-i01-ordered-increment-conditional-bernstein/SKILL.md)：在有序滤过下核验条件 Bernstein 矩并推导指数超鞅与尾界，区分条件和无条件假设。
- [math-i02-filtration-projections-compensators](../../math-i02-filtration-projections-compensators/SKILL.md)：处理滤过、可选或可预测投影及补偿子，核对适应性、可积性和版本。
- [math-i03-fourth-moment-suffix-maximal-comparison](../../math-i03-fourth-moment-suffix-maximal-comparison/SKILL.md)：审查后缀四阶矩与最大值到末端比较，核对过程结构、矩界及比较范围。
- [math-i04-random-carleson-occupancy-llogl](../../math-i04-random-carleson-occupancy-llogl/SKILL.md)：分析随机 Carleson 占用与 LlogL 条件，检查随机测度、占用结构和可积性。
## J · 非齐次跳跃过程

- [math-j01-inhomogeneous-jump-generator](../../math-j01-inhomogeneous-jump-generator/SKILL.md)：推导非齐次跳跃过程的真实生成元，核对时间依赖、跳核及状态空间。
- [math-j02-killed-process-duhamel-first-jump](../../math-j02-killed-process-duhamel-first-jump/SKILL.md)：使用杀死过程、Duhamel 或首次跳跃标签分解，核对杀死项和边界结算。
- [math-j03-nonlocal-balayage-exit-measure](../../math-j03-nonlocal-balayage-exit-measure/SKILL.md)：分析非局部 balayage 与退出测度，核对退出规则、调和条件和核表示。
- [math-j04-jump-compensation-fubini-exit-settlement](../../math-j04-jump-compensation-fubini-exit-settlement/SKILL.md)：核验跳跃补偿、随机 Fubini 与退出财富结算，检查可积性及停止边界项。
- [math-j05-frozen-coordinate-iterated-compensation-interface](../../math-j05-frozen-coordinate-iterated-compensation-interface/SKILL.md)：审查用户明确提供项目契约的非齐次跳跃冻结坐标与迭代补偿，核对条件结构、标签和合法换序。通用补偿公式使用跳事件补偿技能。
## K · 随机场极值与集中

- [math-k01-chan-lai-asymptotically-gaussian-fields](../../math-k01-chan-lai-asymptotically-gaussian-fields/SKILL.md)：核验 Chan–Lai 渐近高斯场方法，检查局部协方差、尾近似和一致性条件。
- [math-k02-pickands-piterbarg-double-sum](../../math-k02-pickands-piterbarg-double-sum/SKILL.md)：使用 Pickands–Piterbarg 双重求和分析极值尾，核对局部结构、重叠项和余项。
- [math-k03-dirksen-mixed-tail-generic-chaining](../../math-k03-dirksen-mixed-tail-generic-chaining/SKILL.md)：应用 Dirksen 混合尾泛链界，检查增量尾、半度量、熵或泛链泛函。
- [math-k04-anti-concentration-empirical-process](../../math-k04-anti-concentration-empirical-process/SKILL.md)：审查反集中与经验过程估计，核对指标集、过程假设和概率误差范围。
- [math-k05-talagrand-convex-concentration](../../math-k05-talagrand-convex-concentration/SKILL.md)：核验 Talagrand 凸集中方法，检查乘积结构、凸距离及所用版本。
- [math-k06-random-greedy-priority-unfolding](../../math-k06-random-greedy-priority-unfolding/SKILL.md)：核验有限线性三角超图中的优先级贪心删边、成对存活递归、独立展开和首次重复耦合；只在已给定的局部模板与访问预算下转移到有限过程。
## L · 计算搜索与严格证书

- [math-l01-lower-bound-test-parameters](../../math-l01-lower-bound-test-parameters/SKILL.md)：选择下界测试参数向量，核对输入可行性、归一化和可认证的下界范围。
- [math-l02-adversarial-input-search](../../math-l02-adversarial-input-search/SKILL.md)：开展对抗输入优化与反例搜索，区分有限搜索证据、可行构造和全局断言。
- [math-l03-rational-and-interval-certificates](../../math-l03-rational-and-interval-certificates/SKILL.md)：构造或核验区间算术、有理对偶与证明型数值证书，检查舍入和全域覆盖。
- [math-l04-mathematical-programming-workflow](../../math-l04-mathematical-programming-workflow/SKILL.md)：组织数学规划软件的建模与结果核验，检查求解器、容差、可行性和界方向。
- [math-l05-csp-sat-smt-encoding](../../math-l05-csp-sat-smt-encoding/SKILL.md)：将有限数学条件编码为 CSP、SAT 或 SMT，核对量词、完备性及可检查证书。
- [math-l06-tensor-rank-accounting](../../math-l06-tensor-rank-accounting/SKILL.md)：审查矩阵乘法张量提取中的直接和形状、辅助张量秩收费、共享腿分离与固定参数容量账本。用于有明确有限秩证书的张量退化；不把熵计算或数值搜索单独当作指数证明。
- [math-l07-noncommutative-matrix-tests](../../math-l07-noncommutative-matrix-tests/SKILL.md)：对非交换公式或无环路径程序，按特征、是否含逆门及树模型选择有理/有限域矩阵 hitting point 或 hitting list，并核验截断字级数与 affine-pencil 定义域条件。不要用于共享电路或未承诺的 rational expression。
- [math-l08-determinantal-polar-certificates](../../math-l08-determinantal-polar-certificates/SKILL.md)：用固定仿射切片上的简单极方程零点核验复数域的仿射行列式表示尺寸下界，含系数极限模型。检查方向、简单性、左右核和多齐次计数。
- [math-l09-deletion-trace-rank-moments](../../math-l09-deletion-trace-rank-moments/SKILL.md)：对独立删除信道的秩统计、矩生成函数恒等式与局部 TV/Hellinger 比较做精确推导或审计；不用于直接认可一般 trace reconstruction 定理。
- [math-l10-prefix-code-decompositions](../../math-l10-prefix-code-decompositions/SKILL.md)：用前缀码 episode 的 split identity 与同字 Boolean-affine recovery，构造或审计有限状态/有限向量空间的序列图语言；不用于认可来源的任何整体星高结论或复杂度界。
- [math-l11-gaussian-projection-density](../../math-l11-gaussian-projection-density/SKILL.md)：在精确 Gaussian 线性观测下建立或审查局部质量到投影密度、共同标签纤维与有限状态选择界。用于有限状态回归下界的局部几何步骤，不把预印本中的完整流式下界当作默认定理。
- [math-l12-automata-relation-monoids](../../math-l12-automata-relation-monoids/SKILL.md)：对有限自动机的局部计算接口、有限关系幺半群角限制同构与上下文分离做精确推导或审计；不用于直接断言一般状态下界。
- [math-l13-finite-graph-refinement](../../math-l13-finite-graph-refinement/SKILL.md)：复核两个显式有限简单图的 Weisfeiler–Leman 元组颜色，区分联合替换与分离多重集，或按 F2 线性系统核对有限图同态的奇偶提升。
- [math-l14-nonarchimedean-cover-descent](../../math-l14-nonarchimedean-cover-descent/SKILL.md)：在完备代数闭非阿基米德域上，核对有限 étale Galois 覆盖在指定连通域的分支稳定子度数，并在素于残余特征的条件下传递环域单位的根；不用于断言全局覆盖存在。
- [math-l15-exact-unit-fraction-transforms](../../math-l15-exact-unit-fraction-transforms/SKILL.md)：对严格介于 0 和 1 的有理数，精确去除单位分数重复项，或以有界贪心步骤把剩余分母推进到指定区间；不用于和等于 1 的展开。
- [math-l16-prime-sieve-certified-transfers](../../math-l16-prime-sieve-certified-transfers/SKILL.md)：审查或应用素数筛中的有限局部条件、尾部剔除、Kummer 完全分裂与加权区间到稠密度转移；显式保留条件性解析输入，不把分裂判别或有限算例写成素数密度定理。
- [math-l17-filtered-linear-algebra-certificates](../../math-l17-filtered-linear-algebra-certificates/SKILL.md)：精确核验有限维空间的首项基证书及共同降算子过滤比较；不把有限样例或几何预印本主定理当作一般证明。
- [math-l18-multiplicative-kernel-tensorization](../../math-l18-multiplicative-kernel-tensorization/SKILL.md)：用素数指数分解核验整数族的乘法 GCD 核估计；检查局部集中、Euler 乘积与临界指数。适用于含 LCM、GCD 或约化乘积的非负双序列估计。
- [math-l19-coordinate-ring-certificates](../../math-l19-coordinate-ring-certificates/SKILL.md)：验证坐标环构造中的 cusp 关系、非单位除法消元和环境临界点证书。适用于需要从显式关系证明商环为多项式环的局部代数步骤。
- [math-l20-binary-character-congruences](../../math-l20-binary-character-congruences/SKILL.md)：在有限初等二群角色族中寻找与零顶点同余的非零顶点。适用于 2-adic 群环求值和有限个指定系数的精确匹配，要求核验二进制维数、精度和测试数。
- [math-l21-local-to-global-lattice-certificates](../../math-l21-local-to-global-lattice-certificates/SKILL.md)：用有限商模的主分解拼接指定局部整格，并核对乘子阶、最大阶饱和与局部单位陪集。适用于数域中的 order-ideal 或局部格计数。
- [math-l22-arithmetic-progression-certificates](../../math-l22-arithmetic-progression-certificates/SKILL.md)：用二进尺度求和把有限无等差数列密度界转为加权界，或用已验证的循环着色构造长区间无单色等差数列的证书。
- [math-l23-packed-nonnegative-recurrences](../../math-l23-packed-nonnegative-recurrences/SKILL.md)：核验用单个自然数的定宽数位计算非负整数递推。用于移位叠加、模截断、分拆表及逐字段进位检查。
## M · 凸性、极点与选择

- [math-m01-convex-hull-extreme-points](../../math-m01-convex-hull-extreme-points/SKILL.md)：用仿射相关消元压缩有限凸组合，用 Krein–Milman 定位紧凸集的极点闭凸包；核对拓扑、紧性与表示类型。
- [math-m02-separation-support-certificate](../../math-m02-separation-support-certificate/SKILL.md)：构造 Hahn–Banach 分离或支撑函数证书，检查闭性、拓扑和分离方向。
- [math-m03-near-extremizer-stability](../../math-m03-near-extremizer-stability/SKILL.md)：分析近极值稳定性与刚性，核对亏损量、对称性、距离和紧性缺口。
- [math-m04-measurable-supremum-selection](../../math-m04-measurable-supremum-selection/SKILL.md)：处理可测上确界、解析投影和可测选择，核对参数空间、可测性及选择器范围。
- [math-m05-cut-metric-construction](../../math-m05-cut-metric-construction/SKILL.md)：在有限树分解上拼接二元 cut law，构造嵌套 cut 坐标图，或把有限 Lp 度量精确离散到有限坐标，核对边缘、零质量、重参数化与距离公式。
- [math-m06-covering-space-obstructions](../../math-m06-covering-space-obstructions/SKILL.md)：核验覆盖空间、秩一局部系与有限复形中的拓扑或全纯凸性障碍，重点检查提升、扭曲同调、周期覆盖与 CW 维数是否真正匹配。
- [math-m07-planar-current-height-duality](../../math-m07-planar-current-height-duality/SKILL.md)：在有限平面 XY 图上把整数 Fourier 电流精确转为 Bessel 高度与积分连接，核对边界、源项、孔洞周期和规范变换。适用于有限图身份，不给出临界指数或尺度极限。
- [math-m08-hamiltonian-fixed-locus-transfer](../../math-m08-hamiltonian-fixed-locus-transfer/SKILL.md)：用有限阶或 involution Hamiltonian 映射上的不变小扰动，将干净固定子流形的固定点问题转为其上的临界点问题，并核验短周期排除与非退化块。
## N · 凸几何、振荡与误差

- [math-n01-john-loewner-ellipsoid](../../math-n01-john-loewner-ellipsoid/SKILL.md)：使用 John 或 Löwner 椭球与容量方法，核对凸体假设、归一化和常数依赖。
- [math-n02-log-concave-marginal-inequalities](../../math-n02-log-concave-marginal-inequalities/SKILL.md)：核验 Prékopa–Leindler、BBL 与对数凹边际不等式，检查指数、积分和等号条件。
- [math-n03-oscillation-and-geometric-remainder](../../math-n03-oscillation-and-geometric-remainder/SKILL.md)：分析 van der Corput、半密度与振荡抵消的几何余项，核对相位和一致参数范围。
- [math-n04-summable-error-entropy-descent](../../math-n04-summable-error-entropy-descent/SKILL.md)：组织可求和误差与熵递减论证，检查逐层预算、收敛传递和累计误差。
- [math-n05-translative-covering-density](../../math-n05-translative-covering-density/SKILL.md)：用带缓冲的窗口周期化研究凸体平移覆盖密度。适用于从有限基本域证明覆盖上界、从所有有限余类的排除推出下界，以及核对重叠计数、余类去重和单格点阵的同步剪切与补全。
- [math-n06-projection-body-volume](../../math-n06-projection-body-volume/SKILL.md)：审查投影体的未极化体积泛函、凸多面体的直积恒等式与一阶变分测度。适用于构造或核对投影体体积比、单纯形比较及椭球下界接口。
- [math-n07-pair-energy-fourier-bounds](../../math-n07-pair-energy-fourier-bounds/SKILL.md)：Derive lower bounds for planar pair energies from Fourier-positive Schwartz minorants and transfer all Gaussian bounds to nonnegative completely monotone potentials. Use for locally finite configurations with centered disk density, including singular potentials and extended energies.
- [math-n08-ruled-cylinder-finite-approximation](../../math-n08-ruled-cylinder-finite-approximation/SKILL.md)：将带迹零、非椭圆横向微分的三维线段扫掠转成有限柱面覆盖，并核对垂直底面积。适用于有限化可变方向线段族，不用于一般柱面覆盖猜想或任意速度场。
- [math-n09-soft-slab-variance](../../math-n09-soft-slab-variance/SKILL.md)：对偶次线性形式的强凸软 slab 势构造或审查方差界。核对矩坐标证书、逐项 Hessian 正性与张量估计，输出可用于参数对数凹性的有限维方差结论。
- [math-n10-dirichlet-slab-energy](../../math-n10-dirichlet-slab-energy/SKILL.md)：用中心高斯路径相关估算凸域加入多条带约束的 Dirichlet 本征值代价，并由所有对角权重的界构造同一个逐坐标能量见证。
- [math-n11-solenoidal-localization-and-packets](../../math-n11-solenoidal-localization-and-packets/SKILL.md)：将局部轴对称不可压缩模型嵌入受迫 Navier--Stokes 场，或审查光滑 Euler 母流上的高频波包输运。区分外力、解类和仅主导项的 WKB 账本；不认证爆破结论。
- [math-n12-frostman-energy-preprocessing](../../math-n12-frostman-energy-preprocessing/SKILL.md)：将有界支撑测度的 Frostman 球质量界、有限 Riesz 能量、紧限制与随机正交投影相互转换，并核对维数范围。
