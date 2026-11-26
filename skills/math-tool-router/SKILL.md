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
| 有理博弈策略、单色矩形递归、有限图卡组、模整数线性关系 | 按 [Google Cogentic 构件索引](../math-research/references/google-cogentic-2026-11-25.md) 选择精确算术或枚举脚本。 |
| Diophantine 逼近的精确有限证书 | 用 [整数线性形式](../math-integer-linear-form-rates/SKILL.md) 转换已证高度与余项界，用 [Hankel–Padé](../math-hankel-pade-certificates/SKILL.md) 审查有限系数和正矩投影下界，用 [交错倒数连分数](../math-alternating-reciprocal-criteria/SKILL.md) 核对分母增长与截断。 |
| 单比值子模性、有限 Markov 桥、树度量输运 | 分别用 [单比值判据](../math-a01-fractional-normalization/references/han-2020-submodularity.md)、[终点桥](../math-h02-exponential-tilting-saddlepoint/references/aguilar-gatto-finite-bridge.md) 和 [树输运](../math-d01-kantorovich-duality/references/tree-metric-transport.md) 生成精确证书。 |
| 有限原子后验树的停止证书 | 用 [后验树与停止见证](../math-e04-snell-envelope-optimal-stopping/references/finite-atomic-posterior-tree.md) 校验精确重心、停止后验和树内 Snell 值。 |
| 一元区间非负、固定原子矩极点、有限链退出、独立 Bernoulli 原子比较 | 分别用 [区间平方和](../math-b02-semi-infinite-exchange/references/papp-univariate-interval-positivity.md)、[矩多面体](../math-b03-generalized-moments/references/finite-moment-face-guide.md)、[ETFSP 区间](../math-j03-nonlocal-balayage-exit-measure/references/etfsp-finite-certificate.md) 和 [精确原子比较](../probability-bernoulli-extremal-orders/references/kleiner_distance_two_exact.md)。 |
| 二元线性码的均匀边缘、给定 SDP 与秩一切 LP 同值 | 分别用 [低阶列关系](../probability-boolean-fourier-invariance/references/binary-code-marginals.md) 和 [秩一切证书](../math-c01-semidefinite-lifting/references/roux-carr-ravi-rank-one-cut-certificates.md)。 |
| 离散矩的形状、有限 e-process、齐次 Mahler 转移 | 分别用 [概率形状](../math-b03-generalized-moments/references/discrete-shape-exact-guide.md)、[逆矩](../probability-martingale-stopping/references/finite_inverse_moment_type_ii.md) 和 [间隙转移](../math-hankel-pade-certificates/references/badziahin-mahler-gap-transfer.md)。 |
| 齐次化 QCQP、稀疏矩、全时域退出或 Wishart 矩 | 使用 [QCQP 同值](../math-c01-semidefinite-lifting/references/arima-kim-kojima-finite-qcqp-certificate.md)、[原子团分解](../math-b03-generalized-moments/references/ideal-sparse-finite-guide.md)、[相型退出](../math-j03-nonlocal-balayage-exit-measure/references/finite-exit-phase-type.md) 或 [精确 Wishart 矩](../probability-random-matrix-tensor/references/wishart-polynomial-moments.md)。 |
| 一维分段 ODE 的严格残差界 | 用 [分段 ODE 证书](../math-l03-rational-and-interval-certificates/references/piecewise-ode-residual.md)核对接缝、正零阶系数和端点输入，给出函数误差界。 |
| 有端点消失条件的 Euler–Maclaurin 求积 | 用 [求积误差证书](../math-euler-maclaurin-quadrature-certificates/SKILL.md) 检查多项式、网格及误差的有理包围。 |
| 标准化单峰分布的尖锐尾界 | 用 [单峰尾界证书](../probability-unimodal-tail-certificates/SKILL.md) 检查事件方向、阈值和取等构造。 |
| 符号求导、恒等式、参数求解、高精度 | `mathematica-math` 或 `python-math` 的已验证符号环境。声明定义域、分支与精确输入。 |
| 给定整数核方向的可分离凸整数优化 | 用 [Graver 增广](../math-l04-mathematical-programming-workflow/references/graver-augmentation.md) 查可行增广及方向表的最优性条件。 |
| 数值线性代数、ODE、优化、MAT 数据 | 按工具箱、已有代码和精度在当前 MATLAB MCP、MATLAB CLI 或 Python 数值栈之间选择。MATLAB 执行细节见 [MATLAB 工具说明](../math-research/references/tools.md#matlab)。 |
| MATLAB 绘图和 FIG | `matlab-plotting`。保存可复现源码及实际导出文件。 |
| 已成为瓶颈的批量数组、矩阵或 FFT | 使用 `local-hybrid-math` 实测 CPU 和可用 GPU 的端到端性能，在满足精度与内存预算的后端中选择。 |
| 已授权借用 MacBook 或 USB iPad | 分别使用 `remote-math-compute` 和 `ipad-math-node`，以当前身份、连接和实际支持的任务为准。 |

## 运行和核验

- 先查看本轮实际暴露的 MCP 工具。需要探测本机 CLI、应用候选或 Python 解释器时，复用 [probe_tools.py](../math-research/scripts/probe_tools.py)。`--python /path/to/python` 指定已有解释器，`--smoke python` 和 `--smoke wolfram` 执行有界试算。发现路径和模块只是候选，实际导入、调用和结果检查分别记录。 Wolfram 包装器探测失败时，按 Mathematica 技能核验已安装内核的直接批处理。
- 从最小有用计算开始。复现所需脚本、最小输入、实际版本、精度和关键参数随结果保存。核对约束、残差、边界或精确身份。严格计算证书要检查算术与覆盖范围，浮点结果说明容差与适用范围。
- 软件缺失、连接失败或许可不可用时，说明失败在哪一步。用户允许替代且任务能保留所需语义时，用当前可用后端完成并报告实际路线。指定交付必须来自某软件时，准确记录尚未完成的部分。
- 临时文件按项目约定放在 data 盘。先保存并核验产物，再关闭本次启动的进程并检查退出。已有会话只释放本次创建的资源，保留用户的未保存工作。超时只清理本次进程组。
