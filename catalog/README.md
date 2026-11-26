# 数学研究技能目录

共 270 个可调用入口。目录按职责分类，保留原技能名。标有兼容入口的技能转入对应主流程。

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
| [math-l17-filtered-linear-algebra-certificates](../skills/math-l17-filtered-linear-algebra-certificates/SKILL.md) | 精确核验有限维空间的首项基、共同降算子过滤以及整系数对称矩阵的 Krylov 列秩；不把有限样例或几何预印本主定理当作一般证明。 |
| [math-l18-multiplicative-kernel-tensorization](../skills/math-l18-multiplicative-kernel-tensorization/SKILL.md) | 用素数指数分解核验整数族的乘法 GCD 核估计；检查局部集中、Euler 乘积与临界指数。适用于含 LCM、GCD 或约化乘积的非负双序列估计。 |
| [math-l19-coordinate-ring-certificates](../skills/math-l19-coordinate-ring-certificates/SKILL.md) | 验证坐标环构造中的 cusp 关系、非单位除法消元和环境临界点证书。适用于需要从显式关系证明商环为多项式环的局部代数步骤。 包含线性多项式结式与专门化最大公因数的有限检查。 |
| [math-l20-binary-character-congruences](../skills/math-l20-binary-character-congruences/SKILL.md) | 在有限初等二群角色族中寻找与零顶点同余的非零顶点。适用于 2-adic 群环求值和有限个指定系数的精确匹配，要求核验二进制维数、精度和测试数。 |
| [math-l21-local-to-global-lattice-certificates](../skills/math-l21-local-to-global-lattice-certificates/SKILL.md) | 用有限商模的主分解拼接指定局部整格，并核对乘子阶、最大阶饱和与局部单位陪集。适用于数域中的 order-ideal 或局部格计数。 |
| [math-l22-arithmetic-progression-certificates](../skills/math-l22-arithmetic-progression-certificates/SKILL.md) | 用二进尺度求和把有限无等差数列密度界转为加权界，或用已验证的循环着色构造长区间无单色等差数列的证书。 |
| [math-l23-packed-nonnegative-recurrences](../skills/math-l23-packed-nonnegative-recurrences/SKILL.md) | 核验用单个自然数的定宽数位计算非负整数递推。用于移位叠加、模截断、分拆表及逐字段进位检查。 |
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
| [math-ag-divisor-intersection-ledger](../skills/math-ag-divisor-intersection-ledger/SKILL.md) | 对已给定的精确除子、公共解消与交叉数表核验局部代数几何接口；不构造几何对象或采纳丰度/Iitaka 主定理。 支持点吹起中零循环的整系数推拉。 |
| [math-algebraic-group-logarithm-distance](../skills/math-algebraic-group-logarithm-distance/SKILL.md) | 对给定交换代数群、代数点和代数 Lie 子代数，核对 Gaudron 有理情形对数到 Lie 子空间距离下界的调用前提。 |
| [math-algebraic-transfer-certificates](../skills/math-algebraic-transfer-certificates/SKILL.md) | 核对已给定的余留映射、整系数转移、链提升、格拼接或有限对称张量资料。适用于 Gersten 与 Milnor 障碍、升 HNN 扩张的同调输入和纤维函子条件。 |
| [math-alternating-reciprocal-criteria](../skills/math-alternating-reciprocal-criteria/SKILL.md) | 用 Sondow 的交错倒数和—连分数判据，严格区分可证明的无理性、有限前缀核验，以及需要整条简单连分数假设的超越性结论。适用于 Pierce 展开或快速增长分母的交错倒数和；不用于仅凭数值近似宣称无理或超越。 |
| [math-asymptotic-midpoint-moduli](../skills/math-asymptotic-midpoint-moduli/SKILL.md) | 在已认证的树、段森林或 Daugavet-L1 结构上，调用渐近中点模量与可数分支 diamond 失真界；不把有限算术或抽象范数当作结构证书。 |
| [math-average-degree-tree-embedding](../skills/math-average-degree-tree-embedding/SKILL.md) | 在有限简单无向图中，按平均度严格阈值核对给定树的嵌入，并返回可检查的顶点映射。 |
| [math-ax-schanuel-dimension-defect](../skills/math-ax-schanuel-dimension-defect/SKILL.md) | 对已明确的平坦联络、模 j、Hodge 周期映射或矩阵指数数据，选择相应 Ax--Schanuel 维数缺陷定理并核对不可省略的几何前提。 |
| [math-baker-runge-height-gates](../skills/math-baker-runge-height-gates/SKILL.md) | 在已给出射影模型、除子和 S-整模型时，核对 Baker--Runge 型积分点高度界的交叠条件与例外集；不计算未给出的有效常数。 |
| [math-bessel-cross-product-recurrence](../skills/math-bessel-cross-product-recurrence/SKILL.md) | 在已给定的 Bessel/modified-Bessel 定义域内，使用离散 Riccati 恒等式与二阶交叉积递推；不把有限递推代数当作圆板谱重数或超越性证明。 |
| [math-bimatrix-kite-mixing](../skills/math-bimatrix-kite-mixing/SKILL.md) | 核验双矩阵博弈的后悔值、s-kite 条件与精确最佳回应混合。适用于已有候选策略的局部改进与有限证书，不把尚未独立复核的全局近似 Nash 声明当作可用定理。 |
| [math-cat0-inductive-barycenters](../skills/math-cat0-inductive-barycenters/SKILL.md) | Transfer a finite centred distribution in a complete CAT(0) metric cone into an inductive-barycenter energy bound, with exact Euclidean finite-support replay. Use for certified cone geometry, not generic group-action or sampling claims. |
| [math-centered-cube-endpoint-budget](../skills/math-centered-cube-endpoint-budget/SKILL.md) | Audit or extend centered axis-parallel cube Hardy–Littlewood weak-(1,1) bounds: all-scale source/receiver budgets, joint high-capacity remainders, and finite-dimensional square/cube certificates. Use for centered-cube-upper-bound, the Round 830 remainder, or cubical endpoint constants; not for Euclidean balls, Kakeya tubes, or strong rectangular maxima. |
| [math-clique-free-random-multiplier](../skills/math-clique-free-random-multiplier/SKILL.md) | Construct and exactly check the finite-support random multiplier from the clique-free neighborhood recursion for a supplied finite weighted K_r-free graph. |
| [math-cmzv-rational-pullback](../skills/math-cmzv-rational-pullback/SKILL.md) | Place specified iterated integrals or multiple polylogarithms in a cyclotomic MZV space through a verified rational-pullback criterion. |
| [math-cohomological-transfer](../skills/math-cohomological-transfer/SKILL.md) | 核验链复形权截断、Mayer–Vietoris 条件、图状神经上链延拓以及已给代数或谱数据上的局部化与张量消失。 |
| [math-conformal-dimension-perron-brackets](../skills/math-conformal-dimension-perron-brackets/SKILL.md) | 对给定扩张共形 Markov 分区、认证导数区间和有理比较向量，验证非负转移矩阵的谱半径界并判断指数与维数的方向。 |
| [math-conformal-domain-estimates](../skills/math-conformal-domain-estimates/SKILL.md) | Manage gated conformal-domain coordinate-energy and univalent inverse-integral-means transfers. Use only with the specified normalization, boundary, and source-model hypotheses; not for arbitrary holomorphic maps or planar compactness. |
| [math-cycle-type-likelihood-bounds](../skills/math-cycle-type-likelihood-bounds/SKILL.md) | Compare two supplied finite cycle-type laws under an explicit iid observation model, with Hellinger affinity and Bayes-error bounds. |
| [math-cycle-weighted-permanent](../skills/math-cycle-weighted-permanent/SKILL.md) | Compute finite Macdonald cycle-weighted permanents and their scalar normalizations exactly for rational q and t. |
| [math-cyclotomic-euler-t-parity](../skills/math-cyclotomic-euler-t-parity/SKILL.md) | 对满足收敛条件的根单位 cyclotomic Euler T-sum，调用围道留数奇偶归约到较低阶和；不提供未展开余项的数值公式，也不采纳猜想的 multiple-t 奇偶性。 |
| [math-differential-operator-minimization](../skills/math-differential-operator-minimization/SKILL.md) | Minimize a supplied rational-coefficient differential operator for a specified formal solution, after certifying the Ore factor, degree-bound and initial-series subroutines. |
| [math-dirichlet-l-derivative-sine-reduction](../skills/math-dirichlet-l-derivative-sine-reduction/SKILL.md) | 对给定偶周期有理数据，精确生成 Dirichlet 型级数在零点导数的形式对数权重。核对周期、对称性、零索引和分母。 |
| [math-discrete-proof-transfer](../skills/math-discrete-proof-transfer/SKILL.md) | 为固定二叉 Derrida–Retaux/H3、连续 Cantelli、自由边界方格双峰 A022、非负因子 A30/A175、布尔 Fourier 谱维数 A28/A165 审核可迁移引理并制作可独立核验的证书。另用于周期图的有限连通分支与例外顶点预算。不要因同名 Fourier、稳定性或张量术语就迁移结论。 |
| [math-double-elliptic-orbit-confinement](../skills/math-double-elliptic-orbit-confinement/SKILL.md) | Apply the source-scoped confinement theorem for finite translation orbits on a surface with two elliptic fibrations and non-torsion sections. |
| [math-edge-deck-reconstruction-audit](../skills/math-edge-deck-reconstruction-audit/SKILL.md) | 审计有限简单图的无标号单边删除卡组，精确比较候选反例并核对边重构定理的图类和密度门槛。适用于小图枚举、边卡组断言和来源结论的适用范围检查。 |
| [math-elliptic-quasielliptic-function-independence](../skills/math-elliptic-quasielliptic-function-independence/SKILL.md) | 对已给定椭圆格、指数参数和 Serre 函数参数，依据经认证的线性无关条件调用函数层面的代数独立性；不从数值特殊值或“几乎处处”结论推断特定点独立性。 |
| [math-euler-constant-irrationality](../skills/math-euler-constant-irrationality/SKILL.md) | 研究欧拉–马歇罗尼常数 γ 的无理性。构造或审计 γ 的 Padé、多重正交、超几何、递推、整数线性形式、分母消去与 Sondow 型判据，也用于核对 E/G 函数、算术 Gevrey 与 Stokes 常数方法能否转移到 γ。 |
| [math-euler-maclaurin-quadrature-certificates](../skills/math-euler-maclaurin-quadrature-certificates/SKILL.md) | 为满足端点消失条件的多项式 Euler--Maclaurin 求积构造精确余项与可复核误差包围；不用于未经认证的一般浮点积分。 |
| [math-euler-series-continued-fraction](../skills/math-euler-series-continued-fraction/SKILL.md) | Convert a finite nondegenerate rational series segment to Euler generalized continued-fraction data exactly. Use for finite algebraic identity checks, not for convergence or irrationality claims. |
| [math-exponential-algebraic-methods](../skills/math-exponential-algebraic-methods/SKILL.md) | 根据指数方程的模型选择复环面或阿贝尔簇上的存在定理，或明确承担 Schanuel、EAC 等前提后的指数多项式与幂映射结论。 |
| [math-exponential-logarithm-algebraic-independence](../skills/math-exponential-logarithm-algebraic-independence/SKILL.md) | 核对 Mahler 1931/32 指数与对数代数独立性及多项式非消失下界的精确适用条件。 |
| [math-f2-group-ring-cancellation](../skills/math-f2-group-ring-cancellation/SKILL.md) | Verify a finite characteristic-two group-ring cancellation certificate from two labelled components and a supplied exact group-label product oracle; it does not establish torsion-freeness or nonzero factors. |
| [math-fermat-hodge-lattice-quotients](../skills/math-fermat-hodge-lattice-quotients/SKILL.md) | Reduce a certified Fermat middle-Hodge lattice quotient to an explicit group-ring quotient, while preserving the geometric and arithmetic premises needed for the reduction. |
| [math-fibonacci-valuation-reductions](../skills/math-fibonacci-valuation-reductions/SKILL.md) | 对给定 Fibonacci 指数的精确整除前提，检查 F_l 的精确幂整除并应用三分支的指数约化；不宣称解完原始指数丢番图方程。 |
| [math-finite-field-formal-series-congruences](../skills/math-finite-field-formal-series-congruences/SKILL.md) | Verify finite coefficient windows for elementary formal-series fixed points over a prime field, with explicit truncation boundaries. |
| [math-finite-nonassociative-algebra-audits](../skills/math-finite-nonassociative-algebra-audits/SKILL.md) | 核验指定有理轴代数乘法表、消去后的线性泛函，或素域上的仿射 medial rack 恒等式和见证。 |
| [math-finite-permutation-terrace-certificates](../skills/math-finite-permutation-terrace-certificates/SKILL.md) | Verify a supplied ordering of all even permutations as a finite directed-terrace certificate; includes a reader for the public packed A7 witness format. |
| [math-function-field-period-transcendence](../skills/math-function-field-period-transcendence/SKILL.md) | 在已给定的正特征 Drinfeld 模、t-motive 与解析平凡化数据下，定位周期、准周期、第三类周期和 Carlitz 张量周期的条件性超越/代数独立接口。 |
| [math-g-function-restricted-approximation](../skills/math-g-function-restricted-approximation/SKILL.md) | 对已认证为有理系数非有理 G-函数的有理值，调用有效的固定基底分母逼近下界；也用于限制其 b 进制展开中的长重复数字块。 |
| [math-gamma-continued-fraction-recurrence](../skills/math-gamma-continued-fraction-recurrence/SKILL.md) | 用精确递推生成并审查 Hessami Pilehrood 的欧拉常数有理逼近与非简单连分数。适用于有限系数、收敛子和分母高度核对，不用于无理性结论。 |
| [math-gamma-gregory-series-interval](../skills/math-gamma-gregory-series-interval/SKILL.md) | 用 Gregory 系数的 Fontana–Mascheroni 级数计算欧拉常数 γ 的严格有理区间，核对精确系数、剩余质量和给定有理候选。 |
| [math-gamma-meijer-cmf](../skills/math-gamma-meijer-cmf/SKILL.md) | 用 Kalisch 等的 Meijer G 保守矩阵场构造欧拉常数 γ 的 Apéry 型候选逼近。复跑已知三阶轨迹，核对对偶矩阵、CVM 换基、收敛判据和约分后的算术质量。 |
| [math-gamma-multiple-laguerre-approximants](../skills/math-gamma-multiple-laguerre-approximants/SKILL.md) | 用 Wolfs–Van Assche 的混合型多重 Laguerre 显式有限和生成欧拉常数有理逼近，并审计算术整化、约分、余项和渐近障碍。 |
| [math-geometric-g-function-special-points](../skills/math-geometric-g-function-special-points/SKILL.md) | 对已给出的一参数代数族、退化、周期矩阵与特殊纤维数据，选择 G-函数局部关系、特殊点高度或模曲线非典型交的定理接口。 |
| [math-geometric-pde-reductions](../skills/math-geometric-pde-reductions/SKILL.md) | 核对给定几何模型的高度方程、标量曲率归一化、Neumann 能量、径向 ODE 不变域、弱流代表元和单相极小子的维数归约。 包含固定顶点倾斜比较与给定加权幂零坐标的局部检查。 |
| [math-gfunction-representability-obstructions](../skills/math-gfunction-representability-obstructions/SKILL.md) | Apply a Picard--Vessiot obstruction to a proposed rational representation of a G-function by supplied solution families, singularity bounds and differential-Galois data. |
| [math-graded-character-order](../skills/math-graded-character-order/SKILL.md) | Certify finite graded multiplicity comparisons through cumulative coefficient differences and optimal ordered matching. |
| [math-graph-spectral-moment-certificates](../skills/math-graph-spectral-moment-certificates/SKILL.md) | Compute adjacency trace moments and short-cycle counts of finite simple graphs, and exact integral circulant spectra and energy by Ramanujan sums. |
| [math-grid-piecewise-translation-embedding](../skills/math-grid-piecewise-translation-embedding/SKILL.md) | Certify a finite cellwise translation embedding between two strict-size subsets of a specified square cell grid. Use after a geometric argument has supplied an allowable common grid; it does not polygonize sets or prove a general equidecomposition theorem. |
| [math-hankel-pade-certificates](../skills/math-hankel-pade-certificates/SKILL.md) | 对整数幂级数做精确 Hankel 行列式与 Padé 有限证书，核验正矩投影的有理下界，并审计 Mahler–Hankel 定理的独立准入门槛；不以有限计算断言超越性或无理度指数。 |
| [math-harmonic-sum-recurrences](../skills/math-harmonic-sum-recurrences/SKILL.md) | 用精确有理算术生成和核对广义超调和数的有限系数。适用于需要把嵌套调和定义化为有限递推、初等对称和或普通调和数的场景；不用于无限 Euler 和、zeta 值化简或无理性结论。 |
| [math-hbl-finite-presentation](../skills/math-hbl-finite-presentation/SKILL.md) | 对已给定的有理有限子空间图和边权，精确核验 HBL 有效表示并分解平衡边流；不搜索表示或计算一般 HBL 常数。 |
| [math-heisenberg-group-determinant-certificates](../skills/math-heisenberg-group-determinant-certificates/SKILL.md) | Exactly compute the finite group-determinant matrix of a supplied sparse element of the order-125 Heisenberg group, with a replay for one documented witness. |
| [math-hofstadter-nested-recurrences](../skills/math-hofstadter-nested-recurrences/SKILL.md) | 用精确整数递推计算广义 Hofstadter 函数 F_k 的有限前缀，并核对已给出的点态比较。 |
| [math-holomorphic-local-to-global-transfer](../skills/math-holomorphic-local-to-global-transfer/SKILL.md) | Transfer specified holomorphic local data to descent, gluing, integrability, or universal-cover product conclusions only after the matching geometric gate has been established. Not for arbitrary local charts or holomorphic distributions. |
| [math-honeycomb-finite-boundary-flux](../skills/math-honeycomb-finite-boundary-flux/SKILL.md) | 在有限、单连通蜂窝三角形域中认证零环权重的带相位边界通量恒等式及凸域正性界；不用于条带渐近、桥质量或一般自避游走。 |
| [math-integer-linear-form-rates](../skills/math-integer-linear-form-rates/SKILL.md) | 用已经证明的整数线性形式高度与双边余项界，生成给定分母的有理逼近下界或推导无理性指数上界。适用于核对 Apéry 型证据和同时逼近的非消失条件。 |
| [math-lacunary-recurrence-transcendence](../skills/math-lacunary-recurrence-transcendence/SKILL.md) | Apply a Subspace-Theorem transcendence criterion to lacunary reciprocal series after certifying the conjugate-root representation, sublinear heights and all-index gap condition. |
| [math-lattice-heat-asymptotics](../skills/math-lattice-heat-asymptotics/SKILL.md) | Prove and safely use the first large-time correction for the continuous-time nearest-neighbor lattice heat kernel. Use for the exact dispersion 2(1-cos k), tensor-product dimensions, and clearly separated physical scaling. |
| [math-lienard-half-arc-matching](../skills/math-lienard-half-arc-matching/SKILL.md) | 将已验证的 Lienard 半平面弧坐标匹配转化为周期轨道与孤立零点问题；不用于未经认证的数值积分或周期数上界。 |
| [math-likely-intersections-density](../skills/math-likely-intersections-density/SKILL.md) | Apply the conditional likely-intersection density theorem for a verified definable complex quotient presentation and its Ax--Schanuel witnesses. |
| [math-linear-difference-hypertranscendence](../skills/math-linear-difference-hypertranscendence/SKILL.md) | 对移位、q-差分或 Mahler 线性差分方程，在已给定的函数域与系数域中应用有理函数或超越函数二分，并核验参数化差分 Galois 前提。 |
| [math-logrank-rectangle-rank-halving](../skills/math-logrank-rectangle-rank-halving/SKILL.md) | 从有限 Boolean 通信矩阵的单色矩形出发，精确核验互补块秩分裂，并把给定矩形或协议分割转为 rank-halving 递归证书。用于审计 Log-Rank 路线的有限接口，不搜索大矩形或认证高秩渐近定理。 |
| [math-mahler-purity-filtration](../skills/math-mahler-purity-filtration/SKILL.md) | Apply the generalized-Mahler Hahn/Puiseux purity filtration to a supplied Mahler equation, while tracking exceptional arithmetic-growth layers and decomposition hypotheses. |
| [math-mahler-system-admission](../skills/math-mahler-system-admission/SKILL.md) | Apply scoped basis, lifting and purity theorems for supplied Mahler equations or systems after certifying the coefficient field, transformation, regularity and orbit hypotheses. |
| [math-mixed-littlewood-pseudoadic](../skills/math-mixed-littlewood-pseudoadic/SKILL.md) | 对满足有限素数支撑和增长条件的伪绝对值序列，调用已发表的混合 Littlewood 存在性定理；不把它当作给定 alpha 的有限逼近算法。 |
| [math-modular-holonomic-telescoping](../skills/math-modular-holonomic-telescoping/SKILL.md) | 用显式极点数据、带权 q 展开和经证实的 valence 界检查亚纯模形式导出的 holonomic 递推。 |
| [math-modular-unlikely-intersections](../skills/math-modular-unlikely-intersections/SKILL.md) | Route a specified modular-curve or abelian-family unlikely-intersection problem through the available degeneration, height, Galois-orbit and conditional Lang--Trotter theorems. |
| [math-motivic-euler-sum-unramifiedness](../skills/math-motivic-euler-sum-unramifiedness/SKILL.md) | 对已精确匹配的 motivic Euler-sum 字族或已认证余作用账本，调用非分歧判据；不把 motivic 结论误写成数值 period 恒等式。 |
| [math-mzv-newton-harmonic-relations](../skills/math-mzv-newton-harmonic-relations/SKILL.md) | Check finite Newton/binomial duality for positive multiple-harmonic indices exactly. Use to prepare finite inputs for Kawashima-type MZV relations, not to prove MZV independence or Euler-constant claims. |
| [math-nevanlinna-functional-transcendence](../skills/math-nevanlinna-functional-transcendence/SKILL.md) | 核对非恒定整函数的 Nevanlinna 特征分离、测度有限的异常集及源定理给出的函数域超越次数。 |
| [math-nonarchimedean-analytic-transfer](../skills/math-nonarchimedean-analytic-transfer/SKILL.md) | 在完备非阿基米德环境中，核对有理或形式的有限阶解析 jet 转移、近似根余项及稠密压缩逆塔上的 Roos 差分。 |
| [math-nonnegative-matrix-path-certificates](../skills/math-nonnegative-matrix-path-certificates/SKILL.md) | Verify the odd-power path certificate for finite entrywise-nonnegative symmetric matrices, with exact finite arithmetic where the inputs are rational. |
| [math-one-special-parking-equality](../skills/math-one-special-parking-equality/SKILL.md) | Enumerate the invariant one-special-preference parking set for a finite positive length list and check the subset-sum equality criterion. |
| [math-openai-arithmetic-determinants](../skills/math-openai-arithmetic-determinants/SKILL.md) | 从 OpenAI 算术预印本提取 Taylor 接触消元、整数多项式行构造、行列式算术下界与解析上界比较。用于设计或审查 Catalan 常数、π 与欧拉常数研究中的行列式候选。 |
| [math-operator-algebra-certificates](../skills/math-operator-algebra-certificates/SKILL.md) | 核验算子代数中的幺正压缩修复、平移卷积核、谱相位迹、自伴谱编码及 C* 截断转运。按已给投影、严格谱隙、迹或比较见证选择。 |
| [math-order-two-casoratian-audit](../skills/math-order-two-casoratian-audit/SKILL.md) | Audit supplied rational second-order recurrences by exact Casoratian and consecutive quotient identities. It certifies finite identities only. |
| [math-padic-abelian-intersection-bounds](../skills/math-padic-abelian-intersection-bounds/SKILL.md) | Apply the source-scoped Buium--Coleman reduction bounds for a smooth p-adic curve inside an abelian variety after an unramified model and jet-space data have been certified. |
| [math-parameterized-norm-form-certificates](../skills/math-parameterized-norm-form-certificates/SKILL.md) | Verify the published solution families of the Bajpai--Bennett cubic norm-form equation and the Bennett--Ghadermazi extremal cubic Thue equation at supplied integer parameters. |
| [math-permanent-inequality-contracts](../skills/math-permanent-inequality-contracts/SKILL.md) | Audit finite permanent inequalities for stochastic matrices and symmetrizable inverse M-matrices, retaining each source theorem's hypotheses and equality scope. |
| [math-petal-join-domination-polynomial](../skills/math-petal-join-domination-polynomial/SKILL.md) | Exhaustively verify the finite domination-polynomial identity for a clique joined to repeated copies of a small petal graph. |
| [math-prevost-hurwitz-pade-remainder](../skills/math-prevost-hurwitz-pade-remainder/SKILL.md) | Construct and audit Prévost's finite [n/m] exp(-t) Padé coefficients and its signed Euler-constant/Hurwitz-zeta remainder; preserve all auxiliary zeta and logarithm terms. |
| [math-primary-pseudopolynomial-certificates](../skills/math-primary-pseudopolynomial-certificates/SKILL.md) | 精确核对主伪多项式的有限 binomial 变换、素数乘积整除条件和已给出的全指标前提。 |
| [math-projective-induction-cocycle-certificates](../skills/math-projective-induction-cocycle-certificates/SKILL.md) | 用有限 Cayley 表和有理相位精确核验图子群上的射影诱导校正、乘子、代表元变换和有限指标维数。 |
| [math-q-series-rational-approximants](../skills/math-q-series-rational-approximants/SKILL.md) | 对给定有理 q 和 z 生成 Tschakaloff 递推的精确多项式系数，核验有限整数化缩放及余项分离。 |
| [math-quantum-permanent-score](../skills/math-quantum-permanent-score/SKILL.md) | Check finite partition-score lower bounds from a supplied nonnegative orbital coefficient profile. |
| [math-regular-graph-low-induced-edge-count](../skills/math-regular-graph-low-induced-edge-count/SKILL.md) | Exhaustively count finite vertex subsets whose induced subgraph has at most a given number of edges, while checking regularity. |
| [math-selberg-riesz-criteria](../skills/math-selberg-riesz-criteria/SKILL.md) | 对给定 Selberg 类 L-函数数据和经认证的系数渐近，调用 Riesz 型 Meijer-G 判据的 GRH 蕴含或反向判据。 |
| [math-semiclassical-orthogonal-deformations](../skills/math-semiclassical-orthogonal-deformations/SKILL.md) | 对给定半经典正交权及移动奇点，核验递推系数的 Toda 变形方程和 Freud 权的 Painleve IV 化简。 |
| [math-sondow-log-fractional-certificate](../skills/math-sondow-log-fractional-certificate/SKILL.md) | 从 Sondow 的双积分与对数线性形式构造可严格计算的欧拉常数分母排除证书。用于生成 S_n 对数权重、认证分数部分阈值、估计余项或寻找使判据在无穷多个指标成立的方法。 |
| [math-special-point-bound-gates](../skills/math-special-point-bound-gates/SKILL.md) | Apply Paulin's explicit special-point discriminant and root-of-unity order bounds to a supplied curve in P1 x Gm after checking its field, polynomial and geometric hypotheses. |
| [math-strip-poisson-smoothing](../skills/math-strip-poisson-smoothing/SKILL.md) | Transfer a symmetric complex-center profile in a fixed strip to complete monotonicity using hyperbolic-secant Poisson smoothing. |
| [math-subanalytic-preparation](../skills/math-subanalytic-preparation/SKILL.md) | 用明确给定的次解析族、泛参数域和纤维模型整理有理幂次展开与边界余项；记录常数和阈值的参数依赖。 |
| [math-symmetric-polynomial-ratio-certificates](../skills/math-symmetric-polynomial-ratio-certificates/SKILL.md) | Evaluate finite complete-homogeneous and Schur Turan ratios exactly on rational inputs, preserving the stated partition and positivity domains. |
| [math-syracuse-exact-words](../skills/math-syracuse-exact-words/SKILL.md) | Verify a supplied finite valuation word for the accelerated positive odd 3x−1 Syracuse map, including its exact source and affine identity. Do not use it to infer predecessor density or a Collatz-type conjecture. |
| [math-three-strip-token-bound](../skills/math-three-strip-token-bound/SKILL.md) | Certify the finite three-strip/token boundary bound for a sequence of equal-cardinality planar threshold cuts with matched exchanges; not a halving-line asymptotic solver. |
| [math-torus-packet-spectral-density](../skills/math-torus-packet-spectral-density/SKILL.md) | 对给定有理分段仿射扭转与有限角向 Fourier 包，精确计算模一推前的阶梯谱密度、色间正交门槛和可选 L1 密度差。 |
| [math-tube-maximal-transfer](../skills/math-tube-maximal-transfer/SKILL.md) | Transfer a specified three-dimensional tube or curved extension packet estimate through its declared maximal, capacity, and level-set interfaces. Not a generic Kakeya, restriction, or incidence certificate. |
| [math-two-generator-graded-semigroup-certificates](../skills/math-two-generator-graded-semigroup-certificates/SKILL.md) | 对互素双生成数值半群的总度分层进行精确计数，并核验对应 T-graded 广义数值半群的 Wilf 型有限不等式。 |
| [math-unfair-polynomial-trinomial-factors](../skills/math-unfair-polynomial-trinomial-factors/SKILL.md) | Apply the trinomial case of the unfair 0–1 polynomial theorem after checking its normalized finite-support and nonnegative-coefficient hypotheses. |
| [math-weil-deligne-purity-lfactor](../skills/math-weil-deligne-purity-lfactor/SKILL.md) | Certify the local L-factor half-plane and Frobenius determinant consequence of supplied pure weight-zero Frobenius-semisimple Weil–Deligne data. Use only after the Weil–Deligne representation, inertia invariants, and purity witnesses have been established externally. |
| [math-zeta-arithmetic-estimates](../skills/math-zeta-arithmetic-estimates/SKILL.md) | 根据指定的 ζ 函数采样、平滑核和参数区间接入等差级数矩比较与光滑数零点修正。适用于检查扭权、测量模型和误差来源。 |
| [math-zeta-polynomial-expansion-coefficients](../skills/math-zeta-polynomial-expansion-coefficients/SKILL.md) | 精确生成指定 Riemann ζ 多项式展开系数中的 γ、ζ(2),…,ζ(m+1) 与有理余项；不数值求 ζ，也不认证无穷级数收敛。 |

## 概率研究专题

| 技能 | 用途 |
| --- | --- |
| [probability-analytic-endpoint-methods](../skills/probability-analytic-endpoint-methods/SKILL.md) | Audit weak-type endpoints, Lorentz and Hardy endpoint methods, and Riesz-transform claims by matching exact input class, output norm, domain, and theorem hypotheses. |
| [probability-bandit-information-bounds](../skills/probability-bandit-information-bounds/SKILL.md) | Analyze stochastic bandit regret and best-arm identification using KL change of measure, structured alternatives, RKHS confidence regions, and sampling allocations; use for direct Bernoulli-mean kernel bandits or fixed-budget versus fixed-confidence distinctions. |
| [probability-bernoulli-extremal-orders](../skills/probability-bernoulli-extremal-orders/SKILL.md) | Compute or compare independent Bernoulli sum laws exactly, apply fixed-mean and fixed-moment extremal reductions, and check dependence-sensitive convex order, atom comparisons, or Poisson approximation budgets. |
| [probability-bernoulli-factory](../skills/probability-bernoulli-factory/SKILL.md) | Select and audit exact coin factories, fixed-depth event representations, and random-stopping constructions with assumptions, output types, and cost clocks explicit. |
| [probability-boolean-fourier-invariance](../skills/probability-boolean-fourier-invariance/SKILL.md) | Analyze Boolean-cube Fourier, coordinate influence, noise stability, low-influence invariance, and bounded-independence PTF questions. Use when the model is a Boolean function or product-space polynomial transfer; use the Gaussian approximation skill for sharp Hermite or Gaussian sign-approximation constants. |
| [probability-brownian-potential-fractals](../skills/probability-brownian-potential-fractals/SKILL.md) | Analyze Brownian path sets, planar SLE and loop-erasure interfaces, potential-capacity comparisons, or reflected Brownian couplings using the exact source scopes in the accompanying references. |
| [probability-concentration-chaining](../skills/probability-concentration-chaining/SKILL.md) | Select scoped concentration, deviation, chaining, anti-concentration, and certificate methods after matching the probability model, tail regime, and exact parameters. |
| [probability-determinantal-dependence](../skills/probability-determinantal-dependence/SKILL.md) | Audit determinantal laws, negative dependence, and singularity claims for spanning-tree and forest measures. |
| [probability-finite-query-direct-product](../skills/probability-finite-query-direct-product/SKILL.md) | Verify a finite deterministic, adaptively interleaved query tree against an exact capped direct-product bound for independent Boolean-input tasks. |
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
| [probability-markov-spectral-mixing](../skills/probability-markov-spectral-mixing/SKILL.md) | Analyze mixing, spectral gaps and update clocks for a specified finite reversible Markov chain, including heat-bath Glauber dynamics, graph geometry and ferromagnetic Ising correlation bounds. |
| [probability-martingale-stopping](../skills/probability-martingale-stopping/SKILL.md) | Analyze martingales, stopping rules, maximal inequalities, and stochastic integrals. Check filtration, brackets and integrability for a specified process or before passing to a process limit. |
| [probability-measure-convergence](../skills/probability-measure-convergence/SKILL.md) | Analyze weak convergence, tightness, conditional laws, changing integrands, and martingale-problem limits. Use when a proof passes from stochastic models to limits of probability measures or needs a precise convergence mode. |
| [probability-moment-polynomial-duality](../skills/probability-moment-polynomial-duality/SKILL.md) | Build finite-support probability bounds for Boolean k-wise laws, event/count moment data, and degree-bounded polynomial duals. Use when the support and full constrained marginal or moment map can be stated; route Fourier and invariance proofs to the existing Boolean skill, and treat tensor/tree recursion as uncovered here. |
| [probability-nonlinear-law-dynamics](../skills/probability-nonlinear-law-dynamics/SKILL.md) | Analyze fixed points and iteration of probability-law operators, including nested stationary-law maps, nonlinear Markov updates, and recursive distributional equations; use when the proof needs operator-specific existence, uniqueness, stability, or global convergence. |
| [probability-optimization-certificates](../skills/probability-optimization-certificates/SKILL.md) | Assemble and audit a finite optimization certificate inside a probability proof after the stochastic model, encoded finite problem, proof type, and remaining transfer are explicit. |
| [probability-percolation-renormalization](../skills/probability-percolation-renormalization/SKILL.md) | Analyze iid percolation, finite-range block arguments, bootstrap closure, and random-host propagation only after matching the model, observable, and hypotheses to an exact source interface. |
| [probability-permutation-subset-sums](../skills/probability-permutation-subset-sums/SKILL.md) | Analyze invariant k-subsets of random permutations through cycle counts, Poisson limits, and random subset-sum reachability while keeping fixed-k limits separate from adjacent-k monotonicity. |
| [probability-planar-isoperimetry](../skills/probability-planar-isoperimetry/SKILL.md) | Analyze planar-graph or tessellation isoperimetry when the embedding, set class, and exact perimeter convention can be matched to a scoped method. |
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
| [probability-spectral-perturbation-certificates](../skills/probability-spectral-perturbation-certificates/SKILL.md) | Audit a parameterized family of finite reversible chains or other finite-dimensional spectral problems for eigenvalue crossings, derivatives, Poisson response, changing stationary measures or rigorous parameter intervals. |
| [probability-stationary-law-interfaces](../skills/probability-stationary-law-interfaces/SKILL.md) | Prove or audit stationary laws for Markov environments, tree flows, IPS and drift-jump systems; use for generator/core, flux, coupling, Palm/occupation, regeneration, or projective-limit arguments. |
| [probability-stochastic-geometry-localization](../skills/probability-stochastic-geometry-localization/SKILL.md) | Prove or audit Poisson growing-ball cover-time and spatial-network localization claims, including measure optimization, Poissonization, and boundary tails, while checking the exact model and transfer hypotheses. |
| [probability-switch-network-cylinders](../skills/probability-switch-network-cylinders/SKILL.md) | 对有限完美匹配开关网络核验暴露路径、固定开关坐标、自由槽位的条件置换核及精确能量演化。 |
| [probability-unimodal-tail-certificates](../skills/probability-unimodal-tail-certificates/SKILL.md) | 用 Ion–Klaassen–van den Heuvel 的结果核验标准化标量单峰分布的尖锐单侧及非对称双侧尾界，精确检查阈值、公式及取等构造。 |
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
