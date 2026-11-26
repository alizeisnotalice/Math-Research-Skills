---
name: math-tool-router
description: 按任务、精度和实际可用性调用本机数学工具，执行或核验数学推导、符号计算、数值计算、优化及计算实验。适用于在 Python、MATLAB、Mathematica/Wolfram、本机 CPU/GPU 和已授权设备间选路，也支持直接指定工具。
---

# 数学工具引导

先确定计算要回答什么问题、所需精度及可接受误差。用户指定软件、后端或设备时优先落实，检查本轮接口、可执行文件、解释器、许可和所需库。选定一条执行路线后读取对应技能。具体数学方法和专题由 `math-research` 选择。

| 工作 | 执行路线 |
| --- | --- |
| 精确整数、有理数、有限枚举、数据处理 | `python-math`。优先使用项目已有解释器，能用标准库精确完成时直接运行。 |
| 欧拉常数的有理区间、连分数和对数线性形式 | 按所给输入选择 [欧拉常数工具](../math-euler-constant-irrationality/SKILL.md)，运行相应的精确 Python 脚本。 |
| 有理安全值、单色矩形分割树、边卡组反演、静态价格 LP、有限群关系与平方根见证 | 按 [Google Cogentic 构件索引](../math-research/references/google-cogentic-2026-11-25.md) 选择精确算术或枚举脚本。 |
| Diophantine 逼近的精确有限证书 | 用 [整数线性形式](../math-integer-linear-form-rates/SKILL.md) 转换已证高度与余项界，用 [Hankel–Padé](../math-hankel-pade-certificates/SKILL.md) 审查有限系数和正矩投影下界，用 [交错倒数连分数](../math-alternating-reciprocal-criteria/SKILL.md) 核对分母增长与截断。 |
| 单比值子模性、有限 Markov 桥、树度量输运 | 分别用 [单比值判据](../math-a01-fractional-normalization/references/han-2020-submodularity.md)、[终点桥](../math-h02-exponential-tilting-saddlepoint/references/aguilar-gatto-finite-bridge.md) 和 [树输运](../math-d01-kantorovich-duality/references/tree-metric-transport.md) 生成精确证书。 |
| 有限原子后验树的停止证书 | 用 [后验树与停止见证](../math-e04-snell-envelope-optimal-stopping/references/finite-atomic-posterior-tree.md) 校验精确重心、停止后验和树内 Snell 值。 |
| 一元区间非负、固定原子矩极点、有限链退出、独立 Bernoulli 原子比较 | 分别用 [区间平方和](../math-b02-semi-infinite-exchange/references/papp-univariate-interval-positivity.md)、[矩多面体](../math-b03-generalized-moments/references/finite-moment-face-guide.md)、[ETFSP 区间](../math-j03-nonlocal-balayage-exit-measure/references/etfsp-finite-certificate.md) 和 [精确原子比较](../probability-bernoulli-extremal-orders/references/kleiner_distance_two_exact.md)。 独立 Bernoulli 和的分布、尾概率及四种顺序用[精确分布比较](../probability-bernoulli-extremal-orders/references/exact-bernoulli-sum.md)。 |
| 二元线性码的均匀边缘、给定 SDP 与秩一切 LP 同值 | 分别用 [低阶列关系](../probability-boolean-fourier-invariance/references/binary-code-marginals.md) 和 [秩一切证书](../math-c01-semidefinite-lifting/references/roux-carr-ravi-rank-one-cut-certificates.md)。 |
| 离散矩的形状、有限 e-process、齐次 Mahler 转移 | 分别用 [概率形状](../math-b03-generalized-moments/references/discrete-shape-exact-guide.md)、[逆矩](../probability-martingale-stopping/references/finite_inverse_moment_type_ii.md) 和 [间隙转移](../math-hankel-pade-certificates/references/badziahin-mahler-gap-transfer.md)。 |
| 齐次化 QCQP、稀疏矩、全时域退出或 Wishart 矩 | 使用 [QCQP 同值](../math-c01-semidefinite-lifting/references/arima-kim-kojima-finite-qcqp-certificate.md)、[原子团分解](../math-b03-generalized-moments/references/ideal-sparse-finite-guide.md)、[相型退出](../math-j03-nonlocal-balayage-exit-measure/references/finite-exit-phase-type.md) 或 [精确 Wishart 矩](../probability-random-matrix-tensor/references/wishart-polynomial-moments.md)。 |
| 一维分段 ODE 的严格残差界 | 用 [分段 ODE 证书](../math-l03-rational-and-interval-certificates/references/piecewise-ode-residual.md)核对接缝、正零阶系数和端点输入，给出函数误差界。 |
| 可逆链的指数尾、附加等式输运、结构双二次型 | 用 [有限马尔可夫尾界](../probability-markov-spectral-mixing/references/finite-markov-chernoff.md)、[有限输运证书](../math-d01-kantorovich-duality/references/finite-constrained-transport.md) 或 [双二次 Gram](../math-c03-moment-sos-certificates/references/qi-cui-xu-monic-xsymmetric-gram.md)。 |
| 给定离散开关网络、环面有限谱包或除子表 | 分别使用[条件置换核](../probability-switch-network-cylinders/SKILL.md)、[环面谱密度](../math-torus-packet-spectral-density/SKILL.md)或[除子账本](../math-ag-divisor-intersection-ledger/SKILL.md)精确核验。 |
| 精确算子代数、有限上同调或几何方程 | 按输入选择[算子代数证书](../math-operator-algebra-certificates/SKILL.md)、[同调与上同调转移](../math-cohomological-transfer/SKILL.md)或[几何方程及归约](../math-geometric-pde-reductions/SKILL.md)。 |
| 非阿基米德解析 jet、完备逆塔或 Weil–Deligne 谱输入 | 按[非阿基米德转移](../math-nonarchimedean-analytic-transfer/SKILL.md)或[局部 L 因子证书](../math-weil-deligne-purity-lfactor/SKILL.md)核对完备性、谱数据和取值范围。 |
| 有理多项式在有理区间上的严格定号 | 用[精确 Bernstein 系数](../math-l03-rational-and-interval-certificates/references/rational-polynomial-sign.md)核对显式分割及开闭端点。 |
| 有限边连通概率、符号约束的区间及算术幂级数 | 给定独立边和接线规则用[精确连通概率](../probability-percolation-renormalization/references/openai-wave3.md)。核验严格上界记录用[有理区间](../math-l03-rational-and-interval-certificates/references/openai-semidecidable-bracketing.md)。核验有限 Taylor 前缀用[Mahler 的有限 Hankel 阶](../math-hankel-pade-certificates/references/mahler-function-transcendence-admission.md)。 |
| 两个实轴有限概率律的 Wasserstein–1 | 用[单调耦合与 1-Lipschitz 势函数证书](../probability-measure-convergence/references/finite-scalar-wasserstein.md)精确比较有理原子律。 |
| 用有理级数核对欧拉常数区间 | [Gregory 系数工具](../math-gamma-gregory-series-interval/SKILL.md)对给定正整数计算精确系数及严格尾界。 |
| 条件层匹配或有限路径因果输运 | 用[信息约束输运](../math-d01-kantorovich-duality/references/finite-information-transport.md)编译等式并核验有理原始和对偶见证。 |
| Hardy 算子在有理阶梯函数上的二次亏损 | 用 [亏损证书](../math-m03-near-extremizer-stability/references/hardy-quadratic-deficit.md) 逐段积分，计入无穷尾段并返回精确对数式。 |
| 有端点消失条件的 Euler–Maclaurin 求积 | 用 [求积误差证书](../math-euler-maclaurin-quadrature-certificates/SKILL.md) 检查多项式、网格及误差的有理包围。 |
| 标准化单峰分布的尖锐尾界 | 用 [单峰尾界证书](../probability-unimodal-tail-certificates/SKILL.md) 检查事件方向、阈值和取等构造。 |
| 符号求导、恒等式、参数求解、高精度 | `mathematica-math` 或 `python-math` 的已验证符号环境。声明定义域、分支与精确输入。 |
| 给定整数核方向的可分离凸整数优化 | 用 [Graver 增广](../math-l04-mathematical-programming-workflow/references/graver-augmentation.md) 查可行增广及方向表的最优性条件。 |
| 正有理数的乘法独立、显式整数递推的有限剩余区间 | 运行[素赋值矩阵秩核验](../math-rational-logarithm-independence-gate/SKILL.md)或[有限递推核验](../math-recurrence-finite-screening/SKILL.md)。 |
| 给定小图的三直径或装饰树独立多项式、自由群表示的给定变换轨迹 | 运行[有限图族见证](../math-finite-graph-family-witnesses/SKILL.md)或[自由群表示轨迹回放](../math-free-group-presentation-traces/SKILL.md)。 |
| 首一多项式在无穷远的形式 Böttcher 共轭 | 用[精确 Laurent 递推](../math-local-bottcher-formal-conjugacy/SKILL.md)计算有理系数并代回截断方程。 |
| 数值线性代数、ODE、优化、MAT 数据 | 按工具箱、已有代码和精度在当前 MATLAB MCP、MATLAB CLI 或 Python 数值栈之间选择。MATLAB 执行细节见 [MATLAB 工具说明](../math-research/references/tools.md#matlab)。 |
| MATLAB 绘图和 FIG | `matlab-plotting`。保存可复现源码及实际导出文件。 |
| 已成为瓶颈的批量数组、矩阵或 FFT | 使用 `local-hybrid-math` 实测 CPU 和可用 GPU 的端到端性能，在满足精度与内存预算的后端中选择。 |
| 已授权借用 MacBook 或 USB iPad | 分别使用 `remote-math-compute` 和 `ipad-math-node`，以当前身份、连接和实际支持的任务为准。 |

## 运行和核验

- 先查看本轮实际暴露的 MCP 工具。需要探测本机 CLI、应用候选或 Python 解释器时，复用 [probe_tools.py](../math-research/scripts/probe_tools.py)。`--python /path/to/python` 指定已有解释器，`--smoke python` 和 `--smoke wolfram` 执行有界试算。发现路径和模块只是候选，实际导入、调用和结果检查分别记录。 Wolfram 包装器探测失败时，按 Mathematica 技能核验已安装内核的直接批处理。
- 从最小有用计算开始。复现所需脚本、最小输入、实际版本、精度和关键参数随结果保存。核对约束、残差、边界或精确身份。严格计算证书要检查算术与覆盖范围，浮点结果说明容差与适用范围。
- 软件缺失、连接失败或许可不可用时，说明失败在哪一步。用户允许替代且任务能保留所需语义时，用当前可用后端完成并报告实际路线。指定交付必须来自某软件时，准确记录尚未完成的部分。
- 临时文件按项目约定放在 data 盘。先保存并核验产物，再关闭本次启动的进程并检查退出。已有会话只释放本次创建的资源，保留用户的未保存工作。超时只清理本次进程组。

## 复跑论文关联代码

先固定公开代码提交、算术后端、输入、命令、实际执行范围和输出。区分算术样例、模型条件和形式定理；形式化结论要核对工具链、构建、所依赖公理及声明与论文的对应关系。对已定位代码先选择可复验的有界部件，记录精确算术或容差。参见[A25 有限代码回放](references/a25-crossover-replay.md)。
