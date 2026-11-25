---
name: local-hybrid-math
description: 合理调度本机 CPU 与 GPU，实测并优化 MATLAB、Mathematica/Wolfram Language、Python 的矩阵、数组、FFT、批量模拟等数学计算。用于 Apple Silicon/Metal、PyTorch MPS、GPUArray/gpuArray、加速、线程数、内存与精度问题；按规模、精度和含传输的实测耗时选择后端，保存运行证据，MATLAB 用后及时关闭。
---

# 本机 CPU / GPU 协同数学计算

优先优化实际任务总耗时。CPU 与 GPU 都是候选后端；不要把 GPU 利用率本身作为目标。符号推导、精确数、高精度、区间证明继续使用合适的 CPU 数学工具，数值批处理按实测选择。

## 工作流程

1. 明确运算、尺寸/批次数、精度、误差容限和输出。新项目用 `/Volumes/data/CodexProjects`，缓存与临时数据用 `/Volumes/data/CodexTemp`；data 未挂载时停止依赖它的写入。
2. 阅读 [本机配置](references/host.md)，检查现有解释器、软件、GPU 和可用内存。更换版本/机器后复测。不要把默认 Python 当作已配置的数学环境。
3. 按任务选路，先做小规模对照与计时，再扩大：

   | 任务/调用端 | 候选路径 | 按需读取 |
   |---|---|---|
   | Python 数组/矩阵 | NumPy CPU、PyTorch CPU 各线程数、PyTorch Metal | [Python 调度](references/python.md) |
   | MATLAB | MATLAB 原生 CPU；`local_compute` 自动 CPU/Metal；`local_gpu` 显式 Metal | [MATLAB](references/matlab.md) |
   | Mathematica | 原生 CPU；Apple `GPUArray` 支持的数组与 FFT | [Wolfram](references/wolfram.md) |
   | 其他数学运算 | 使用相应数学 skill，单独实测其本机后端 | [调度原则](references/scheduling.md) |

4. 自动调度使用 [hybrid_math.py](scripts/hybrid_math.py)：相同实际尺寸上校准，比较含上传/下载的耗时；仅在收益足够时采用 GPU，缓存本机校准结果。float64 走 CPU。显式 GPU 不可用时失败；自动选择 CPU 要在报告中标明。
5. 对大量重复作业保持同一解释器和 GPU 数组，合并小作业、分块大作业；CPU 做预处理、独立推导与结果校验。先测收益，再增加 CPU/GPU 重叠；统一内存争用和线程过量都可能降低性能。
6. 保存代码、种子/输入、版本、选择依据、实际设备、精度误差及总耗时。计算证据与严格证明分开。
7. MATLAB 保存后及时退出，优先用 [批处理启动器](scripts/run_matlab_batch.py) 的 `-batch` 与进程检查。不要只关闭图窗，也不要无差别终止用户已有会话。Wolfram 批处理保存后结束内核。

## 精度与资源

- 本机 Apple GPU 数值路径用 float32 / Real32，FFT 为 ComplexReal32。双精度、任意精度和有向舍入需求优先 CPU；不静默降精度。
- 显式 GPU MATLAB 接口默认拒绝 double；传 single 或明确 `AllowPrecisionLoss=true`。自动接口的 double 默认留在 CPU。Wolfram 包装同样要求 Real32 或显式转换选项。
- PyTorch GPU 路径在导入前关闭 MPS CPU fallback，检查实际结果设备，计时前后同步。Wolfram 只对官方支持且实际保留 GPUArray 的算子报告 GPU 成功。
- 通用脚本当前支持 `matmul`、`sin_exp`（sin(x)exp(-x²)）、`sum`；新算子需实际设备、精度和失败案例验证。不能据此宣称任意 MATLAB/Wolfram 函数自动用 GPU。
- 通用 Python/桥接作业估算内存上限 512 MiB；Wolfram 示例输入上限 128 MiB。原生 CPU 大任务另按可用内存预算。先分块，保留系统内存保护；并行时限制总预算、CPU 线程与 GPU 作业数。
- 默认容差是示例。按问题条件数、输入精度和累积误差设置阈值。通过 CPU/GPU 对照不是数学证明。

## 交付

报告实际 CPU/GPU 路径、选择依据、测试范围、误差、端到端耗时和 MATLAB 退出情况。性能结论附尺寸、线程数、是否预热、是否含传输/校验。运行结果写入项目，不写进已安装 skill。官方依据见 [sources.md](references/sources.md)。
