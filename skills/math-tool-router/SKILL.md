---
name: math-tool-router
description: 按任务、精度和实际可用性调用本机数学工具，执行或核验数学推导、符号计算、数值计算、优化及计算实验。适用于在 Python、MATLAB、Mathematica/Wolfram、本机 CPU/GPU 和已授权设备间选路，也支持直接指定工具。
---

# 数学工具引导

先确定计算要回答什么问题、所需精度及可接受误差。用户指定软件、后端或设备时优先落实，检查本轮接口、可执行文件、解释器、许可和所需库。选定一条执行路线后读取对应技能。具体数学方法和专题由 `math-research` 选择。

| 工作 | 执行路线 |
| --- | --- |
| 精确整数、有理数、有限枚举、数据处理 | `python-math`。优先使用项目已有解释器，能用标准库精确完成时直接运行。 |
| 符号求导、恒等式、参数求解、高精度 | `mathematica-math` 或 `python-math` 的已验证符号环境。声明定义域、分支与精确输入。 |
| 数值线性代数、ODE、优化、MAT 数据 | 按工具箱、已有代码和精度在当前 MATLAB MCP、MATLAB CLI 或 Python 数值栈之间选择。MATLAB 执行细节见 [MATLAB 工具说明](../math-research/references/tools.md#matlab)。 |
| MATLAB 绘图和 FIG | `matlab-plotting`。保存可复现源码及实际导出文件。 |
| 已成为瓶颈的批量数组、矩阵或 FFT | 使用 `local-hybrid-math` 实测 CPU 和可用 GPU 的端到端性能，在满足精度与内存预算的后端中选择。 |
| 已授权借用 MacBook 或 USB iPad | 分别使用 `remote-math-compute` 和 `ipad-math-node`，以当前身份、连接和实际支持的任务为准。 |

## 运行和核验

- 先查看本轮实际暴露的 MCP 工具。需要探测本机 CLI、应用候选或 Python 解释器时，复用 [probe_tools.py](../math-research/scripts/probe_tools.py)。`--python /path/to/python` 指定已有解释器，`--smoke python` 和 `--smoke wolfram` 执行有界试算。发现路径和模块只是候选，实际导入、调用和结果检查分别记录。 Wolfram 包装器探测失败时，按 Mathematica 技能核验已安装内核的直接批处理。
- 从最小有用计算开始。复现所需脚本、最小输入、实际版本、精度和关键参数随结果保存。核对约束、残差、边界或精确身份。严格计算证书要检查算术与覆盖范围，浮点结果说明容差与适用范围。
- 软件缺失、连接失败或许可不可用时，说明失败在哪一步。用户允许替代且任务能保留所需语义时，用当前可用后端完成并报告实际路线。指定交付必须来自某软件时，准确记录尚未完成的部分。
- 临时文件按项目约定放在 data 盘。先保存并核验产物，再关闭本次启动的进程并检查退出。已有会话只释放本次创建的资源，保留用户的未保存工作。超时只清理本次进程组。
