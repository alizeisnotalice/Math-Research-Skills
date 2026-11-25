# 数学研究技能目录

共 170 个可调用入口。目录按职责分类，保留原技能名。标有兼容入口的技能转入对应主流程。

## 研究总入口

| 技能 | 用途 |
| --- | --- |
| [math-research](../skills/math-research/SKILL.md) | 统筹数学研究、证明核验与计算实验：按问题选择数学方法和概率专题，衔接数学计算、文献、写作和交付技能。研究任务需要确定方法和执行工具时使用；单纯语言润色与普通电脑操作使用各自技能。 |

## 计算与绘图工具

| 技能 | 用途 |
| --- | --- |
| [ipad-math-node](../skills/ipad-math-node/SKILL.md) | 通过 USB 数据线使用 iPad Math Node 应用执行支持的数学计算；核验设备和应用状态，提交有界任务并保存实际结果。适用于用户要求利用 iPad CPU 辅助研究。 |
| [local-hybrid-math](../skills/local-hybrid-math/SKILL.md) | 合理调度本机 CPU 与 GPU，实测并优化 MATLAB、Mathematica/Wolfram Language、Python 的矩阵、数组、FFT、批量模拟等数学计算。用于 Apple Silicon/Metal、PyTorch MPS、GPUArray/gpuArray、加速、线程数、内存与精度问题；按规模、精度和含传输的实测耗时选择后端，保存运行证据，MATLAB 用后及时关闭。 |
| [math-tool-router](../skills/math-tool-router/SKILL.md) | 按任务、精度和实际可用性调用本机数学工具，执行或核验数学推导、符号计算、数值计算、优化及计算实验。适用于在 Python、MATLAB、Mathematica/Wolfram、本机 CPU/GPU 和已授权设备间选路，也支持直接指定工具。 |
| [mathematica-math](../skills/mathematica-math/SKILL.md) | 用 Mathematica/Wolfram Language 进行可复现的数学符号推导、数值计算、优化与绘图，并核验结果；数学任务需要实际调用 Mathematica 时使用，不用于一般 Notebook 编辑。 |
| [mathematica-research](../skills/mathematica-research/SKILL.md)（兼容 → mathematica-math） | 兼容旧版 Mathematica 研究调用名；指定该入口时使用 mathematica-math 的计算与核验流程。 |
| [matlab-plotting](../skills/matlab-plotting/SKILL.md) | 使用本机 MATLAB 实际运行脚本，制作或修改论文与数学建模图；支持 CSV、Excel、MAT 和公式，检查中文、公式与排版，交付 PNG/PDF、可编辑 FIG 和可复现 .m 源码。用户要求 MATLAB 绘图、论文图美化、多子图或已有 MATLAB 图修改时使用。 |
| [python-math](../skills/python-math/SKILL.md) | 使用本机 Python 实际执行数学运算、SymPy 符号推导、NumPy/SciPy 数值计算与优化、有限枚举及结果验证；先选择已有解释器和数学库，再保存脚本、运行并检查结果。用户要求用 Python 跑计算或研究任务适合 Python 时使用。 |
| [remote-math-compute](../skills/remote-math-compute/SKILL.md) | 通过雷电桥或其他网络调用用户授权的远程电脑进行数学计算；核验 SSH 主机身份、发现远程 Python/MATLAB/Mathematica、分配独立任务并收集可复现结果。适用于 Mac mini 借用 MacBook 等跨机器研究计算。 |

## 数学方法（A–N）

| 技能 | 用途 |
| --- | --- |
| [math-a01-fractional-normalization](../skills/math-a01-fractional-normalization/SKILL.md) | 审查齐次归一化与分式规划中的正分母、Charnes–Cooper 变换、松弛方向及达到条件。 |
| [math-a02-outer-relaxation-budget](../skills/math-a02-outer-relaxation-budget/SKILL.md) | 构造或审查外放松映射，核对正支配、约束保持、界方向和误差预算。 |
| [math-a03-compactness-concentration](../skills/math-a03-compactness-concentration/SKILL.md) | 分析近极值序列的紧性、集中、逃逸与极限传递，核对归一化和质量保持。 |
| [math-a04-shared-nonanticipative-mip](../skills/math-a04-shared-nonanticipative-mip/SKILL.md) | 审查共同选择的混合整数模型与非前视约束，检查不同情形是否由同一决策实现。 |
| [math-b01-lagrange-farkas](../skills/math-b01-lagrange-farkas/SKILL.md) | 推导或核验 Lagrange 对偶与 Farkas 证书，检查约束资格、对偶方向及不可行性证据。 |
| [math-b02-semi-infinite-exchange](../skills/math-b02-semi-infinite-exchange/SKILL.md) | 处理半无限规划与约束生成，核对分离子问题、交换步骤、停止条件和全域覆盖。 |
| [math-b03-generalized-moments](../skills/math-b03-generalized-moments/SKILL.md) | 用广义矩问题组织概率或解析界，核对矩约束、对偶多项式和达到条件。 |
| [math-b04-qualification-facial-minimax](../skills/math-b04-qualification-facial-minimax/SKILL.md) | 检查约束资格、面约化及极小极大交换，定位强对偶或量词交换所需的假设。 |
| [math-c01-semidefinite-lifting](../skills/math-c01-semidefinite-lifting/SKILL.md) | 审查半定提升的建模、秩约束与松弛方向，区分 SDP 界和原问题可行解。 |
| [math-c02-completely-positive-copositive](../skills/math-c02-completely-positive-copositive/SKILL.md) | 分析完全正锥和共正锥表述，核对锥对偶、有限近似及最优性证书范围。 |
| [math-c03-moment-sos-certificates](../skills/math-c03-moment-sos-certificates/SKILL.md) | 构建或核验矩与 SOS 层级，检查正多项式证书、截断阶数、紧性和解恢复。 |
| [math-c04-branch-and-bound](../skills/math-c04-branch-and-bound/SKILL.md) | 组织分支定界中的可行界、松弛界、剪枝和终止证书，检查全局覆盖。 |
| [math-d01-kantorovich-duality](../skills/math-d01-kantorovich-duality/SKILL.md) | 核验 Kantorovich 输运对偶及势函数，检查代价、可积性和原始对偶可行性。 |
| [math-d02-gibbs-entropy-duality](../skills/math-d02-gibbs-entropy-duality/SKILL.md) | 推导 Gibbs 变分与熵对偶，检查参考测度、归一化、有限熵和等号条件。 |
| [math-d03-parameterized-free-energy](../skills/math-d03-parameterized-free-energy/SKILL.md) | 分析指定参数的自由能弱式，核对参数范围、变分方向和与目标问题的接口。 |
| [math-d04-entropy-chain-rule](../skills/math-d04-entropy-chain-rule/SKILL.md) | 使用熵链式分解分析联合与条件分布，核对可测性、条件核和积分合法性。 |
| [math-d05-finite-block-matrix-entropy](../skills/math-d05-finite-block-matrix-entropy/SKILL.md) | 为有限维三块 Gram 矩阵核验零块熵下界，使用 log-det 表示、Schur 补和符号平均分离块内熵与标量熵。 |
| [math-e01-occupation-measure-flow-lp](../skills/math-e01-occupation-measure-flow-lp/SKILL.md) | 建立占用测度、有限时域概率流和流守恒 LP，核对真实过程、边界通量、终止时刻、风险原子与可实现性。 |
| [math-e02-nonlocal-hjb-supersolution](../skills/math-e02-nonlocal-hjb-supersolution/SKILL.md) | 构造或审查非局部 HJB 超解，核对生成元、边界条件与验证不等式方向。 |
| [math-e03-tree-bellman-cross-layer-budget](../skills/math-e03-tree-bellman-cross-layer-budget/SKILL.md) | 分析树 Bellman 跨层预算势，核对层间递推、公共预算与终端结算。 |
| [math-e04-snell-envelope-optimal-stopping](../skills/math-e04-snell-envelope-optimal-stopping/SKILL.md) | 处理最优停止与 Snell 包络，核对滤过、可积性、停止时及极限传递。 |
| [math-e05-mean-payoff-potential-certificates](../skills/math-e05-mean-payoff-potential-certificates/SKILL.md) | 为有限确定性二人均值收益博弈构造或审查权重扰动、闭合势函数区域及逐路径高低收益证书；不用于认证求解复杂度或随机博弈结论。 |
| [math-e06-online-metric-lazy-following](../skills/math-e06-online-metric-lazy-following/SKILL.md) | 将任意按请求可见的 k-server 模拟配置轨迹转为强惰性实际服务，并以最小匹配势逐路径核验移动账本；不用于断言全局竞争比或构造模拟轨迹。 |
| [math-f01-geometric-mean-kernel-two-winner-audit](../skills/math-f01-geometric-mean-kernel-two-winner-audit/SKILL.md) | 审查几何平均核与两赢家分支估计，检查同输入耦合和分支选择条件。 |
| [math-f02-tensor-fourier-positivity-soft-square-supremum](../skills/math-f02-tensor-fourier-positivity-soft-square-supremum/SKILL.md) | 核验张量 Fourier 正性及软度平方上确界估计，区分频域正性与所需最大界。 |
| [math-f03-hilbert-schmidt-radial-layer-square-envelope](../skills/math-f03-hilbert-schmidt-radial-layer-square-envelope/SKILL.md) | 审查 Hilbert–Schmidt 径向层叠与平方包络，检查层间求和和核的适用条件。 |
| [math-f04-poisson-gamma-abel-square-function](../skills/math-f04-poisson-gamma-abel-square-function/SKILL.md) | 使用 Poisson–Gamma 与 Abel 平方函数方法，核对参数积分、权重和接口条件。 |
| [math-f05-l2-spectral-parameter-schur-test](../skills/math-f05-l2-spectral-parameter-schur-test/SKILL.md) | 推导 L² 谱参数估计与 Schur 检验，检查核界、测度、权重和常数依赖。 |
| [math-f06-menshov-rademacher-maximal-partial-sums](../skills/math-f06-menshov-rademacher-maximal-partial-sums/SKILL.md) | 核验 Rademacher–Menshov 最大部分和估计，检查正交性、索引与对数损失。 |
| [math-f07-marcinkiewicz-zygmund-vector-extension](../skills/math-f07-marcinkiewicz-zygmund-vector-extension/SKILL.md) | 审查 Marcinkiewicz–Zygmund 向量值延拓，核对算子类型、指数范围和随机化条件。 |
| [math-f08-matrix-trace-energy](../skills/math-f08-matrix-trace-energy/SKILL.md) | 核验有限维 PSD Gram 矩阵的 \(\operatorname{tr}(P^{3/2})\) Hessian、Loewner 比较与正能量望远镜，并在需要时检查有限维 trace Young 等号。 |
| [math-f09-positive-resolvent-densities](../skills/math-f09-positive-resolvent-densities/SKILL.md) | 在凸数值域上构造或审计正的边界 resolvent 密度与共同压缩表示，核对外部坐标、度量收缩和所有系数尺寸的量词。 |
| [math-g01-carleson-measure-box-and-tent-test](../skills/math-g01-carleson-measure-box-and-tent-test/SKILL.md) | 检验 Carleson 测度的盒、帐篷与嵌入条件，核对几何族、尺度及常数。 |
| [math-g02-outer-lp-size-and-tree-stopping](../skills/math-g02-outer-lp-size-and-tree-stopping/SKILL.md) | 使用外测度 Lp、大小函数和树停止方法，核对外测度结构与嵌入假设。 |
| [math-g03-directional-capture-tree-quadratic-audit](../skills/math-g03-directional-capture-tree-quadratic-audit/SKILL.md) | 审查方向性捕获树的二次型及来源算子，核对方向、选择器和耦合结构。 |
| [math-g04-rubio-de-francia-square-function-scope-check](../skills/math-g04-rubio-de-francia-square-function-scope-check/SKILL.md) | 核验树上 Rubio de Francia 平方函数估计的适用范围与频率几何条件。 |
| [math-g05-tree-carleson-square-function-tc-a4-audit](../skills/math-g05-tree-carleson-square-function-tc-a4-audit/SKILL.md) | 审查 TC-A4 Carleson 型平方函数界，核对树结构、输入范围和具体假设。 |
| [math-h01-uniform-cramer-moderate-deviations](../skills/math-h01-uniform-cramer-moderate-deviations/SKILL.md) | 核验一致 Cramér 中偏差和三角阵尾估计，检查一致参数范围、矩条件和误差。 |
| [math-h02-exponential-tilting-saddlepoint](../skills/math-h02-exponential-tilting-saddlepoint/SKILL.md) | 分析指数倾斜与鞍点尾近似，核验鞍点、精确倾斜恒等式、Mills 界及误差范围。 |
| [math-h03-fan-grama-liu-martingale-expansion](../skills/math-h03-fan-grama-liu-martingale-expansion/SKILL.md) | 应用或审查 Fan–Grama–Liu 鞅展开，核对条件矩、滤过及展开误差。 |
| [math-h04-exact-rate-function-variance-strata](../skills/math-h04-exact-rate-function-variance-strata/SKILL.md) | 计算或核对精确率函数与方差分层，保持参数域和各层尾估计的一致性。 |
| [math-h05-chernoff-hoeffding-bernstein](../skills/math-h05-chernoff-hoeffding-bernstein/SKILL.md) | 选择和核验 Chernoff、Hoeffding、Bernstein 尾界，检查独立性、矩条件和常数。 |
| [math-i01-ordered-increment-conditional-bernstein](../skills/math-i01-ordered-increment-conditional-bernstein/SKILL.md) | 在有序滤过下核验条件 Bernstein 矩并推导指数超鞅与尾界，区分条件和无条件假设。 |
| [math-i02-filtration-projections-compensators](../skills/math-i02-filtration-projections-compensators/SKILL.md) | 处理滤过、可选或可预测投影及补偿子，核对适应性、可积性和版本。 |
| [math-i03-fourth-moment-suffix-maximal-comparison](../skills/math-i03-fourth-moment-suffix-maximal-comparison/SKILL.md) | 审查后缀四阶矩与最大值到末端比较，核对过程结构、矩界及比较范围。 |
| [math-i04-random-carleson-occupancy-llogl](../skills/math-i04-random-carleson-occupancy-llogl/SKILL.md) | 分析随机 Carleson 占用与 LlogL 条件，检查随机测度、占用结构和可积性。 |
| [math-j01-inhomogeneous-jump-generator](../skills/math-j01-inhomogeneous-jump-generator/SKILL.md) | 推导非齐次跳跃过程的真实生成元，核对时间依赖、跳核及状态空间。 |
| [math-j02-killed-process-duhamel-first-jump](../skills/math-j02-killed-process-duhamel-first-jump/SKILL.md) | 使用杀死过程、Duhamel 或首次跳跃标签分解，核对杀死项和边界结算。 |
| [math-j03-nonlocal-balayage-exit-measure](../skills/math-j03-nonlocal-balayage-exit-measure/SKILL.md) | 分析非局部 balayage 与退出测度，核对退出规则、调和条件和核表示。 |
| [math-j04-jump-compensation-fubini-exit-settlement](../skills/math-j04-jump-compensation-fubini-exit-settlement/SKILL.md) | 核验跳跃补偿、随机 Fubini 与退出财富结算，检查可积性及停止边界项。 |
| [math-j05-frozen-coordinate-iterated-compensation-interface](../skills/math-j05-frozen-coordinate-iterated-compensation-interface/SKILL.md) | 审查用户明确提供项目契约的非齐次跳跃冻结坐标与迭代补偿，核对条件结构、标签和合法换序。通用补偿公式使用跳事件补偿技能。 |
| [math-k01-chan-lai-asymptotically-gaussian-fields](../skills/math-k01-chan-lai-asymptotically-gaussian-fields/SKILL.md) | 核验 Chan–Lai 渐近高斯场方法，检查局部协方差、尾近似和一致性条件。 |
| [math-k02-pickands-piterbarg-double-sum](../skills/math-k02-pickands-piterbarg-double-sum/SKILL.md) | 使用 Pickands–Piterbarg 双重求和分析极值尾，核对局部结构、重叠项和余项。 |
| [math-k03-dirksen-mixed-tail-generic-chaining](../skills/math-k03-dirksen-mixed-tail-generic-chaining/SKILL.md) | 应用 Dirksen 混合尾泛链界，检查增量尾、半度量、熵或泛链泛函。 |
| [math-k04-anti-concentration-empirical-process](../skills/math-k04-anti-concentration-empirical-process/SKILL.md) | 审查反集中与经验过程估计，核对指标集、过程假设和概率误差范围。 |
| [math-k05-talagrand-convex-concentration](../skills/math-k05-talagrand-convex-concentration/SKILL.md) | 核验 Talagrand 凸集中方法，检查乘积结构、凸距离及所用版本。 |
| [math-k06-random-greedy-priority-unfolding](../skills/math-k06-random-greedy-priority-unfolding/SKILL.md) | 核验有限线性三角超图中的优先级贪心删边、成对存活递归、独立展开和首次重复耦合；只在已给定的局部模板与访问预算下转移到有限过程。 |
| [math-l01-lower-bound-test-parameters](../skills/math-l01-lower-bound-test-parameters/SKILL.md) | 选择下界测试参数向量，核对输入可行性、归一化和可认证的下界范围。 |
| [math-l02-adversarial-input-search](../skills/math-l02-adversarial-input-search/SKILL.md) | 开展对抗输入优化与反例搜索，区分有限搜索证据、可行构造和全局断言。 |
| [math-l03-rational-and-interval-certificates](../skills/math-l03-rational-and-interval-certificates/SKILL.md) | 构造或核验区间算术、有理对偶与证明型数值证书，检查舍入和全域覆盖。 |
| [math-l04-mathematical-programming-workflow](../skills/math-l04-mathematical-programming-workflow/SKILL.md) | 组织数学规划软件的建模与结果核验，检查求解器、容差、可行性和界方向。 |
| [math-l05-csp-sat-smt-encoding](../skills/math-l05-csp-sat-smt-encoding/SKILL.md) | 将有限数学条件编码为 CSP、SAT 或 SMT，核对量词、完备性及可检查证书。 |
| [math-l06-tensor-rank-accounting](../skills/math-l06-tensor-rank-accounting/SKILL.md) | 审查矩阵乘法张量提取中的直接和形状、辅助张量秩收费、共享腿分离与固定参数容量账本。用于有明确有限秩证书的张量退化；不把熵计算或数值搜索单独当作指数证明。 |
| [math-l07-noncommutative-matrix-tests](../skills/math-l07-noncommutative-matrix-tests/SKILL.md) | 对非交换公式或无环路径程序，按特征、是否含逆门及树模型选择有理/有限域矩阵 hitting point 或 hitting list，并核验截断字级数与 affine-pencil 定义域条件。不要用于共享电路或未承诺的 rational expression。 |
| [math-l08-determinantal-polar-certificates](../skills/math-l08-determinantal-polar-certificates/SKILL.md) | 用固定仿射切片上的简单极方程零点核验复数域的仿射行列式表示尺寸下界，含系数极限模型。检查方向、简单性、左右核和多齐次计数。 |
| [math-l09-deletion-trace-rank-moments](../skills/math-l09-deletion-trace-rank-moments/SKILL.md) | 对独立删除信道的秩统计、矩生成函数恒等式与局部 TV/Hellinger 比较做精确推导或审计；不用于直接认可一般 trace reconstruction 定理。 |
| [math-l10-prefix-code-decompositions](../skills/math-l10-prefix-code-decompositions/SKILL.md) | 用前缀码 episode 的 split identity 与同字 Boolean-affine recovery，构造或审计有限状态/有限向量空间的序列图语言；不用于认可来源的任何整体星高结论或复杂度界。 |
| [math-l11-gaussian-projection-density](../skills/math-l11-gaussian-projection-density/SKILL.md) | 在精确 Gaussian 线性观测下建立或审查局部质量到投影密度、共同标签纤维与有限状态选择界。用于有限状态回归下界的局部几何步骤，不把预印本中的完整流式下界当作默认定理。 |
| [math-l12-automata-relation-monoids](../skills/math-l12-automata-relation-monoids/SKILL.md) | 对有限自动机的局部计算接口、有限关系幺半群角限制同构与上下文分离做精确推导或审计；不用于直接断言一般状态下界。 |
| [math-l13-finite-graph-refinement](../skills/math-l13-finite-graph-refinement/SKILL.md) | 复核两个显式有限简单图的 Weisfeiler–Leman 元组颜色，区分联合替换与分离多重集，或按 F2 线性系统核对有限图同态的奇偶提升。 |
| [math-l14-nonarchimedean-cover-descent](../skills/math-l14-nonarchimedean-cover-descent/SKILL.md) | 在完备代数闭非阿基米德域上，核对有限 étale Galois 覆盖在指定连通域的分支稳定子度数，并在素于残余特征的条件下传递环域单位的根；不用于断言全局覆盖存在。 |
| [math-l15-exact-unit-fraction-transforms](../skills/math-l15-exact-unit-fraction-transforms/SKILL.md) | 对严格介于 0 和 1 的有理数，精确去除单位分数重复项，或以有界贪心步骤把剩余分母推进到指定区间；不用于和等于 1 的展开。 |
| [math-l16-prime-sieve-certified-transfers](../skills/math-l16-prime-sieve-certified-transfers/SKILL.md) | 审查或应用素数筛中的有限局部条件、尾部剔除、Kummer 完全分裂与加权区间到稠密度转移；显式保留条件性解析输入，不把分裂判别或有限算例写成素数密度定理。 |
| [math-l17-filtered-linear-algebra-certificates](../skills/math-l17-filtered-linear-algebra-certificates/SKILL.md) | 精确核验有限维空间的首项基证书及共同降算子过滤比较；不把有限样例或几何预印本主定理当作一般证明。 |
| [math-l18-multiplicative-kernel-tensorization](../skills/math-l18-multiplicative-kernel-tensorization/SKILL.md) | 用素数指数分解核验整数族的乘法 GCD 核估计；检查局部集中、Euler 乘积与临界指数。适用于含 LCM、GCD 或约化乘积的非负双序列估计。 |
| [math-l19-coordinate-ring-certificates](../skills/math-l19-coordinate-ring-certificates/SKILL.md) | 验证坐标环构造中的 cusp 关系、非单位除法消元和环境临界点证书。适用于需要从显式关系证明商环为多项式环的局部代数步骤。 |
| [math-l20-binary-character-congruences](../skills/math-l20-binary-character-congruences/SKILL.md) | 在有限初等二群角色族中寻找与零顶点同余的非零顶点。适用于 2-adic 群环求值和有限个指定系数的精确匹配，要求核验二进制维数、精度和测试数。 |
| [math-l21-local-to-global-lattice-certificates](../skills/math-l21-local-to-global-lattice-certificates/SKILL.md) | 用有限商模的主分解拼接指定局部整格，并核对乘子阶、最大阶饱和与局部单位陪集。适用于数域中的 order-ideal 或局部格计数。 |
| [math-l22-arithmetic-progression-certificates](../skills/math-l22-arithmetic-progression-certificates/SKILL.md) | 用二进尺度求和把有限无等差数列密度界转为加权界，或用已验证的循环着色构造长区间无单色等差数列的证书。 |
| [math-m01-convex-hull-extreme-points](../skills/math-m01-convex-hull-extreme-points/SKILL.md) | 用仿射相关消元压缩有限凸组合，用 Krein–Milman 定位紧凸集的极点闭凸包；核对拓扑、紧性与表示类型。 |
| [math-m02-separation-support-certificate](../skills/math-m02-separation-support-certificate/SKILL.md) | 构造 Hahn–Banach 分离或支撑函数证书，检查闭性、拓扑和分离方向。 |
| [math-m03-near-extremizer-stability](../skills/math-m03-near-extremizer-stability/SKILL.md) | 分析近极值稳定性与刚性，核对亏损量、对称性、距离和紧性缺口。 |
| [math-m04-measurable-supremum-selection](../skills/math-m04-measurable-supremum-selection/SKILL.md) | 处理可测上确界、解析投影和可测选择，核对参数空间、可测性及选择器范围。 |
| [math-m05-cut-metric-construction](../skills/math-m05-cut-metric-construction/SKILL.md) | 在有限树分解上拼接二元 cut law，构造嵌套 cut 坐标图，或把有限 Lp 度量精确离散到有限坐标，核对边缘、零质量、重参数化与距离公式。 |
| [math-m06-covering-space-obstructions](../skills/math-m06-covering-space-obstructions/SKILL.md) | 核验覆盖空间、秩一局部系与有限复形中的拓扑或全纯凸性障碍，重点检查提升、扭曲同调、周期覆盖与 CW 维数是否真正匹配。 |
| [math-m07-planar-current-height-duality](../skills/math-m07-planar-current-height-duality/SKILL.md) | 在有限平面 XY 图上把整数 Fourier 电流精确转为 Bessel 高度与积分连接，核对边界、源项、孔洞周期和规范变换。适用于有限图身份，不给出临界指数或尺度极限。 |
| [math-m08-hamiltonian-fixed-locus-transfer](../skills/math-m08-hamiltonian-fixed-locus-transfer/SKILL.md) | 用有限阶或 involution Hamiltonian 映射上的不变小扰动，将干净固定子流形的固定点问题转为其上的临界点问题，并核验短周期排除与非退化块。 |
| [math-n01-john-loewner-ellipsoid](../skills/math-n01-john-loewner-ellipsoid/SKILL.md) | 使用 John 或 Löwner 椭球与容量方法，核对凸体假设、归一化和常数依赖。 |
| [math-n02-log-concave-marginal-inequalities](../skills/math-n02-log-concave-marginal-inequalities/SKILL.md) | 核验 Prékopa–Leindler、BBL 与对数凹边际不等式，检查指数、积分和等号条件。 |
| [math-n03-oscillation-and-geometric-remainder](../skills/math-n03-oscillation-and-geometric-remainder/SKILL.md) | 分析 van der Corput、半密度与振荡抵消的几何余项，核对相位和一致参数范围。 |
| [math-n04-summable-error-entropy-descent](../skills/math-n04-summable-error-entropy-descent/SKILL.md) | 组织可求和误差与熵递减论证，检查逐层预算、收敛传递和累计误差。 |
| [math-n05-translative-covering-density](../skills/math-n05-translative-covering-density/SKILL.md) | 用带缓冲的窗口周期化研究凸体平移覆盖密度。适用于从有限基本域证明覆盖上界、从所有有限余类的排除推出下界，以及核对重叠计数、余类去重和单格点阵的同步剪切与补全。 |
| [math-n06-projection-body-volume](../skills/math-n06-projection-body-volume/SKILL.md) | 审查投影体的未极化体积泛函、凸多面体的直积恒等式与一阶变分测度。适用于构造或核对投影体体积比、单纯形比较及椭球下界接口。 |
| [math-n07-pair-energy-fourier-bounds](../skills/math-n07-pair-energy-fourier-bounds/SKILL.md) | Derive lower bounds for planar pair energies from Fourier-positive Schwartz minorants and transfer all Gaussian bounds to nonnegative completely monotone potentials. Use for locally finite configurations with centered disk density, including singular potentials and extended energies. |
| [math-n08-ruled-cylinder-finite-approximation](../skills/math-n08-ruled-cylinder-finite-approximation/SKILL.md) | 将带迹零、非椭圆横向微分的三维线段扫掠转成有限柱面覆盖，并核对垂直底面积。适用于有限化可变方向线段族，不用于一般柱面覆盖猜想或任意速度场。 |
| [math-n09-soft-slab-variance](../skills/math-n09-soft-slab-variance/SKILL.md) | 对偶次线性形式的强凸软 slab 势构造或审查方差界。核对矩坐标证书、逐项 Hessian 正性与张量估计，输出可用于参数对数凹性的有限维方差结论。 |
| [math-n10-dirichlet-slab-energy](../skills/math-n10-dirichlet-slab-energy/SKILL.md) | 用中心高斯路径相关估算凸域加入多条带约束的 Dirichlet 本征值代价，并由所有对角权重的界构造同一个逐坐标能量见证。 |
| [math-n11-solenoidal-localization-and-packets](../skills/math-n11-solenoidal-localization-and-packets/SKILL.md) | 将局部轴对称不可压缩模型嵌入受迫 Navier--Stokes 场，或审查光滑 Euler 母流上的高频波包输运。区分外力、解类和仅主导项的 WKB 账本；不认证爆破结论。 |
| [math-n12-frostman-energy-preprocessing](../skills/math-n12-frostman-energy-preprocessing/SKILL.md) | 将有界支撑测度的 Frostman 球质量界、有限 Riesz 能量、紧限制与随机正交投影相互转换，并核对维数范围。 |

## 专项研究核验

| 技能 | 用途 |
| --- | --- |
| [euclidean-tensor-geometry](../skills/euclidean-tensor-geometry/SKILL.md) | Apply or audit OpenAI family 379 Euclidean tensor prices, Strassen spectral invariants, and common-placement network bounds in arithmetic complexity and combinatorics. 中文触发：欧几里得张量几何、张量价格、渐近谱、跨割下界。Do not use for generic tensor numerics or classical maximal operators without a proved model bridge. |
| [math-centered-cube-endpoint-budget](../skills/math-centered-cube-endpoint-budget/SKILL.md) | Audit or extend centered axis-parallel cube Hardy–Littlewood weak-(1,1) bounds: all-scale source/receiver budgets, joint high-capacity remainders, and finite-dimensional square/cube certificates. Use for centered-cube-upper-bound, the Round 830 remainder, or cubical endpoint constants; not for Euclidean balls, Kakeya tubes, or strong rectangular maxima. |
| [math-discrete-proof-transfer](../skills/math-discrete-proof-transfer/SKILL.md) | 为固定二叉 Derrida–Retaux/H3、连续 Cantelli、自由边界方格双峰 A022、非负因子 A30/A175、布尔 Fourier 谱维数 A28/A165 审核可迁移引理并制作可独立核验的证书。另用于周期图的有限连通分支与例外顶点预算。不要因同名 Fourier、稳定性或张量术语就迁移结论。 |
| [math-euler-constant-irrationality](../skills/math-euler-constant-irrationality/SKILL.md) | 研究欧拉–马歇罗尼常数 γ 的无理性。构造或审计 γ 的 Padé、多重正交、超几何、递推、整数线性形式、分母消去与 Sondow 型判据，也用于核对 E/G 函数、算术 Gevrey 与 Stokes 常数方法能否转移到 γ。 |
| [math-gamma-meijer-cmf](../skills/math-gamma-meijer-cmf/SKILL.md) | 用 Kalisch 等的 Meijer G 保守矩阵场构造欧拉常数 γ 的 Apéry 型候选逼近。复跑已知三阶轨迹，核对对偶矩阵、CVM 换基、收敛判据和约分后的算术质量。 |
| [math-gamma-multiple-laguerre-approximants](../skills/math-gamma-multiple-laguerre-approximants/SKILL.md) | 用 Wolfs–Van Assche 的混合型多重 Laguerre 显式有限和生成欧拉常数有理逼近，并审计算术整化、约分、余项和渐近障碍。 |
| [math-openai-arithmetic-determinants](../skills/math-openai-arithmetic-determinants/SKILL.md) | 从 OpenAI 算术预印本提取 Taylor 接触消元、整数多项式行构造、行列式算术下界与解析上界比较。用于设计或审查 Catalan 常数、π 与欧拉常数研究中的行列式候选。 |
| [math-sondow-log-fractional-certificate](../skills/math-sondow-log-fractional-certificate/SKILL.md) | 从 Sondow 的双积分与对数线性形式构造可严格计算的欧拉常数分母排除证书。用于生成 S_n 对数权重、认证分数部分阈值、估计余项或寻找使判据在无穷多个指标成立的方法。 |

## 概率研究专题

| 技能 | 用途 |
| --- | --- |
| [probability-analytic-endpoint-methods](../skills/probability-analytic-endpoint-methods/SKILL.md) | Audit weak-type endpoints, Lorentz and Hardy endpoint methods, and Riesz-transform claims by matching exact input class, output norm, domain, and theorem hypotheses. |
| [probability-bandit-information-bounds](../skills/probability-bandit-information-bounds/SKILL.md) | Analyze stochastic bandit regret and best-arm identification using KL change of measure, structured alternatives, RKHS confidence regions, and sampling allocations; use for direct Bernoulli-mean kernel bandits or fixed-budget versus fixed-confidence distinctions. |
| [probability-bernoulli-extremal-orders](../skills/probability-bernoulli-extremal-orders/SKILL.md) | Audit independent Bernoulli sums, fixed-mean and fixed-moment extrema, dependence-sensitive convex order, log-concavity, exact tail comparisons, and approximation budgets. |
| [probability-bernoulli-factory](../skills/probability-bernoulli-factory/SKILL.md) | Select and audit exact coin factories, fixed-depth event representations, and random-stopping constructions with assumptions, output types, and cost clocks explicit. |
| [probability-boolean-fourier-invariance](../skills/probability-boolean-fourier-invariance/SKILL.md) | Analyze Boolean-cube Fourier, coordinate influence, noise stability, low-influence invariance, and bounded-independence PTF questions. Use when the model is a Boolean function or product-space polynomial transfer; use the Gaussian approximation skill for sharp Hermite or Gaussian sign-approximation constants. |
| [probability-brownian-potential-fractals](../skills/probability-brownian-potential-fractals/SKILL.md) | Analyze Brownian path sets, planar SLE and loop-erasure interfaces, potential-capacity comparisons, or reflected Brownian couplings using the exact source scopes in the accompanying references. |
| [probability-concentration-chaining](../skills/probability-concentration-chaining/SKILL.md) | Apply and audit concentration inequalities, large-deviation bounds, empirical-process/chaining estimates, and anti-concentration results while preserving model assumptions and the distinction between upper tails and small-ball bounds. |
| [probability-determinantal-dependence](../skills/probability-determinantal-dependence/SKILL.md) | Audit determinantal laws, negative dependence, and singularity claims for spanning-tree and forest measures. |
| [probability-first-passage-growth](../skills/probability-first-passage-growth/SKILL.md) | Analyze first-passage percolation, geodesics and Busemann functions, random growth and competition, and max-flow questions when the exact weight law, lattice, dimension, or direction hypotheses matter. |
| [probability-flow-poset-growth](../skills/probability-flow-poset-growth/SKILL.md) | Audit finite directed capacity flows, edge-disjoint path covers, Dilworth chain covers, LIS/RSK and sparse Poisson growth; keep boundary, model and double-limit hypotheses explicit. |
| [probability-forests-electrical-networks](../skills/probability-forests-electrical-networks/SKILL.md) | Analyze uniform and minimal spanning forests, electrical networks, mass transport, unimodular random networks, and related finite spanning-tree inequalities. |
| [probability-gaussian-polynomial-approximation](../skills/probability-gaussian-polynomial-approximation/SKILL.md) | Analyze Hermite expansions, Gaussian polynomial moments and tails, anti-concentration, and approximation of Gaussian sign or indicator functions. Use when the input is a real polynomial under standard Gaussian measure; keep low-influence invariance and PTF boundary results within their stated hypotheses. |
| [probability-generating-function-boundaries](../skills/probability-generating-function-boundaries/SKILL.md) | Audit two-dimensional queue-length PGF equations and complex boundary reductions while preserving event epochs, empty-boundary terms, analytic hypotheses, and probability admissibility. |
| [probability-harmonic-measure-coding](../skills/probability-harmonic-measure-coding/SKILL.md) | Analyze harmonic and boundary measures on trees, symbolic codings, exact dimensions, and equivalence versus singularity of pushforward measures on a common metric space. |
| [probability-infection-witness-methods](../skills/probability-infection-witness-methods/SKILL.md) | Build and audit finite causal witnesses for deterministic monotone infection closures, with separate model routes for random-set zero forcing, synchronous graph-H bootstrap, and Hamming-plane Young growth. |
| [probability-information-cluster-expansion](../skills/probability-information-cluster-expansion/SKILL.md) | Analyze entropy-rate variational problems, synchronization and deletion-channel capacity, renewal polling limits, and convergence of cluster or asymptotic expansions. |
| [probability-integer-polynomial-factorization](../skills/probability-integer-polynomial-factorization/SKILL.md) | Analyze finite-support integer convolution through probability-generating polynomials, monic nonnegative-real factors, and exact bounded algebraic certificates; preserve support gaps and coefficient-domain assumptions. |
| [probability-logconcave-moment-geometry](../skills/probability-logconcave-moment-geometry/SKILL.md) | Analyze moment comparisons, centroid-body expansion, convex geometry, and transport or functional inequalities for log-concave laws. |
| [probability-markov-spectral-mixing](../skills/probability-markov-spectral-mixing/SKILL.md) | Analyze finite reversible Markov-chain mixing and spectral gaps, especially heat-bath Glauber dynamics for ferromagnetic Ising models; use when a claim depends on update clocks, graph geometry, or correlation inequalities. |
| [probability-martingale-stopping](../skills/probability-martingale-stopping/SKILL.md) | Analyze martingales, stopping rules, maximal inequalities, stochastic integrals, and martingale-problem limits with explicit filtration and integrability checks. |
| [probability-measure-convergence](../skills/probability-measure-convergence/SKILL.md) | Analyze weak convergence, tightness, conditional laws, changing integrands, and martingale-problem limits. Use when a proof passes from stochastic models to limits of probability measures or needs a precise convergence mode. |
| [probability-moment-polynomial-duality](../skills/probability-moment-polynomial-duality/SKILL.md) | Build finite-support probability bounds for Boolean k-wise laws, event/count moment data, and degree-bounded polynomial duals. Use when the support and full constrained marginal or moment map can be stated; route Fourier and invariance proofs to the existing Boolean skill, and treat tensor/tree recursion as uncovered here. |
| [probability-nonlinear-law-dynamics](../skills/probability-nonlinear-law-dynamics/SKILL.md) | Analyze fixed points and iteration of probability-law operators, including nested stationary-law maps, nonlinear Markov updates, and recursive distributional equations; use when the proof needs operator-specific existence, uniqueness, stability, or global convergence. |
| [probability-optimization-certificates](../skills/probability-optimization-certificates/SKILL.md) | Build and audit finite-dimensional optimization bounds and proof certificates used inside probability arguments, including duality, interval validation, and exact LP/MIP checks. |
| [probability-percolation-renormalization](../skills/probability-percolation-renormalization/SKILL.md) | Analyze iid percolation, finite-range block arguments, bootstrap closure, and random-host propagation only after matching the model, observable, and hypotheses to an exact source interface. |
| [probability-permutation-subset-sums](../skills/probability-permutation-subset-sums/SKILL.md) | Analyze invariant k-subsets of random permutations through cycle counts, Poisson limits, and random subset-sum reachability while keeping fixed-k limits separate from adjacent-k monotonicity. |
| [probability-planar-isoperimetry](../skills/probability-planar-isoperimetry/SKILL.md) | Analyze isoperimetric profiles and curvature methods on planar graphs or tessellations when the boundary statistic, embedding, and theorem hypotheses can be matched. |
| [probability-poset-counting-sampling](../skills/probability-poset-counting-sampling/SKILL.md) | Count linear extensions and related finite poset families, derive entropy bounds, or build exact samplers; also use for finite graph-labeling peak constraints that admit a verifiable counting recurrence. |
| [probability-prophet-online-selection](../skills/probability-prophet-online-selection/SKILL.md) | Analyze prophet inequalities, optimal thresholds, online resource allocation, and stochastic matching while preserving the arrival model and benchmark. |
| [probability-queueing-heavy-traffic](../skills/probability-queueing-heavy-traffic/SKILL.md) | Analyze queueing-network stability and heavy-traffic limits using fluid/Lyapunov methods, polling models, state-space collapse, BAR, and reflected diffusions. Renewal/Palm epoch conversion and exact coupling/total-variation questions are out of scope here. |
| [probability-random-graph-energy-landscapes](../skills/probability-random-graph-energy-landscapes/SKILL.md) | Analyze synchronization, phase-locking, and energy-landscape claims for graph-coupled oscillator models; choose a theorem only when its graph, coupling, symmetry, quotient, and probability hypotheses match. |
| [probability-random-matrix-tensor](../skills/probability-random-matrix-tensor/SKILL.md) | Prove or audit random matrix and tensor norm bounds, Banach type-2 estimates, and noncommutative martingale inequalities. Use when the norm, covariance model, or row/column square-function assumptions need precise source-based checking. |
| [probability-random-recursive-trees-asymptotics](../skills/probability-random-recursive-trees-asymptotics/SKILL.md) | Analyze asymptotic moments, profiles, fringe statistics, and limit laws for size-dependent or recursively grown random trees while preserving the construction, sampling rule, and theorem hypotheses. |
| [probability-random-spatial-tree-geometry](../skills/probability-random-spatial-tree-geometry/SKILL.md) | Route questions across spatial network geometry, random-tree walks and boundary measures only after fixing the exact model; use the locally scoped, independently reviewed theorem interfaces and keep open maximum, monotonicity, and cross-model transfers explicit. |
| [probability-reflected-diffusion-coupling](../skills/probability-reflected-diffusion-coupling/SKILL.md) | Model and audit couplings of reflected diffusions when boundary geometry, the coupling class, coalescence, meeting tails, or Neumann spectra affect the proof. |
| [probability-renewal-palm-coupling](../skills/probability-renewal-palm-coupling/SKILL.md) | Analyze renewal and Palm sampling, queueing recurrence and stationary limits, and when a coupling yields exact or total-variation convergence. |
| [probability-self-avoiding-walks-and-sle](../skills/probability-self-avoiding-walks-and-sle/SKILL.md) | Analyze rigorous self-avoiding-walk growth and graph methods, and audit proposed links from planar lattice walks to continuum SLE. |
| [probability-spectral-perturbation-certificates](../skills/probability-spectral-perturbation-certificates/SKILL.md) | Audit finite-dimensional parameter-dependent eigenvalues and reversible Markov spectral gaps, including changing stationary measures, crossings, Poisson response, and rigorous interval enclosures. |
| [probability-stationary-law-interfaces](../skills/probability-stationary-law-interfaces/SKILL.md) | Prove or audit stationary laws for Markov environments, tree flows, IPS and drift-jump systems; use for generator/core, flux, coupling, Palm/occupation, regeneration, or projective-limit arguments. |
| [probability-stochastic-geometry-localization](../skills/probability-stochastic-geometry-localization/SKILL.md) | Prove or audit Poisson growing-ball cover-time and spatial-network localization claims, including measure optimization, Poissonization, and boundary tails, while checking the exact model and transfer hypotheses. |
| [probability-variational-limits](../skills/probability-variational-limits/SKILL.md) | Audit limits of stochastic optimization values, expectations, minimax problems, and selected optimizer laws; match weak convergence, uniform integrability, Gamma convergence, LDP/Laplace principles, and second-parameter estimates to their exact hypotheses. |

## 文献检索与获取

| 技能 | 用途 |
| --- | --- |
| [academic-literature-search](../skills/academic-literature-search/SKILL.md) | 检索、筛选和核验中英文学术文章，输出相关性说明、可追溯来源及 BibTeX 引用。 用于查论文、找相关研究、了解研究进展、补充参考文献，以及按需查找主张的文献证据。 |
| [cnki-search](../skills/cnki-search/SKILL.md) | 在中国知网（CNKI）上检索学术论文并导出参考文献。Use when Codex needs to find CNKI papers, search Chinese academic literature, retrieve paper metadata/details/references, or produce GB/T 7714-style citations from queries mentioning 知网, CNKI, 中国知网, 文献检索, 论文搜索, 参考文献, 期刊论文, 学位论文, or 会议论文. |
| [literature-download](../skills/literature-download/SKILL.md)（兼容 → literature-search-download） | 兼容按题录或 DOI 清单批量下载文献的旧入口；使用 literature-search-download 的按清单获取流程。 |
| [literature-search-download](../skills/literature-search-download/SKILL.md) | 检索中英文学术文献、核验题录与版本、下载可获取的论文全文，交付 PDF、BibTeX 和可追溯清单。用于“找论文并下载”、按 DOI/题名/文献表批量获取全文，也支持只检索或只下载；不自动扩展为论文翻译或系统综述。 |

## 论文写作、翻译与表达

| 技能 | 用途 |
| --- | --- |
| [academic-paper-translator](../skills/academic-paper-translator/SKILL.md) | 将数学、物理、计算机领域的英文学术文献忠实翻译为简体中文，支持 PDF、Word、网页和粘贴文本，保留公式与图表，默认交付中文 Word 和 PDF。 用于英文论文翻译、文献汉化、整篇或指定章节翻译；长文可由多个 subagent 分工。单纯文献检索、摘要提炼或论文润色不触发本技能。 |
| [academic-paper-writing](../skills/academic-paper-writing/SKILL.md) | 起草、修改和点评中英文学术论文（academic paper writing / scientific writing），按需拆解范文并建立有出处的句式库。 适用于科研论文的章节写作、结构诊断与写作训练；单纯文献检索、论文翻译或竞赛论文排版使用对应专项 skill。 |
| [anti-defensive-writing](../skills/anti-defensive-writing/SKILL.md) | 起草或修订论文、摘要、引言、讨论及技术说明时，删去重复自我否定、无信息免责声明和层叠保留语，直接表达有证据的观点；保留影响结论成立的假设、范围、方法限制和真实不确定性。 |
| [math-paper-writing](../skills/math-paper-writing/SKILL.md) | 以用户提供的《数学论文写作规范_动机结构与自然表达》PDF 为准，起草、修改和点评中英文数学研究论文，落实文章结构、方法动机、证明与自然表达，检查量词和计算证据。 尤其适用于调和分析、极大算子、概率与随机过程、几何分析、优化及计算辅助证明；纯文献检索、逐篇翻译和单纯竞赛排版使用对应技能。 |
| [pdf-paper-translate](../skills/pdf-paper-translate/SKILL.md)（兼容 → academic-paper-translator） | 兼容学术论文 PDF 翻译的旧入口；转入 academic-paper-translator，保留指定的输出格式与排版要求。 |

## 数学建模竞赛

| 技能 | 用途 |
| --- | --- |
| [math-modeling-audit](../skills/math-modeling-audit/SKILL.md) | 审计数学建模竞赛项目的模型假设、算法结论、实验账本与论文数值，恢复多版本项目的可信状态。适用于检查建模结果是否可靠、核对论文与代码数据、区分历史重算和新实验、定位证据缺口；不用于单纯论文排版或替代用户开展新实验。 |
| [math-modeling-delivery](../skills/math-modeling-delivery/SKILL.md) | 将数学建模结果组织为题目要求的 Excel、论文图表、附录和可复现支撑包。适用于核对输出采样与精度、同步结果及源码、清理重复材料、制作 ZIP/RAR 和提交前一致性核验；不自动代签、上传或重跑正式实验。 |
| [math-modeling-paper](../skills/math-modeling-paper/SKILL.md) | 编排或局部修订中文数学建模竞赛论文，处理页数口径、页码与页脚、摘要精确加粗、图表位置、附录及 PDF 最小改动验收。适用于保留指定基线格式、修复大块空白、按 Word 标注修改摘要或生成数学建模排版提示词；不用于改写未经授权的模型结论。 |

## 指定模型咨询

| 技能 | 用途 |
| --- | --- |
| [astra-delegate](../skills/astra-delegate/SKILL.md) | 在用户请求 Astra 协助证明、审查或分析时，优先使用可用的 Codex Astra 子 Agent；需要使用用户自己的 OpenAI Platform API 时，执行独立的 Astra 模型咨询。 |
