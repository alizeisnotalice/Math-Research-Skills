# 本机配置与测试范围

2026-11-15–16 实测；更换硬件、软件或负载后复测。

| 项目 | 实际检测 |
|---|---|
| 机器 | Mac mini / Mac18,5，Apple M6，12 核 CPU，16 GiB 统一内存 |
| GPU | Apple M6，12 核，Metal 4 |
| 系统 | macOS 27.2，arm64 |
| 数学 Python | `$HOME/.venvs/main/bin/python`，3.13.18 |
| 已有库 | PyTorch 2.15.0；NumPy 2.5.4；SciPy 1.18.1 |
| GPU 实测 | PyTorch MPS built/available，实际张量结果 `mps:0` |
| MATLAB | `/Applications/MATLAB_R2026b.app/bin/matlab`，26.2 Update 1 |
| MATLAB 原生 GPU | `gpuDeviceCount('available') == 0`；GPU 部分采用本机 Python Metal 桥接 |
| Wolfram | `/usr/local/bin/wolframscript`；Wolfram 15.0，MacOSX-ARM64 |
| Wolfram GPU 实测 | 原生 GPUArray 的逐元素运算、一维 Fourier；输入和输出均为 GPUArray |

默认 Python 3.15 与已有 GPU venv 不同。保留 venv 路径，不要解析其 Python 符号链接后绕开环境。MATLAB 包装接受 `Python=...`，其次读取 `LOCAL_GPU_PYTHON`，最后检查 `$HOME/.venvs/main/bin/python`。

使用 `gpu_math.py probe --report <项目内绝对路径>` 复测 MPS；用 `hybrid_math.py` 的 `--refresh-calibration` 重新校准 CPU/GPU。硬件复测可调用 `system_profiler`，只保存芯片、内存与 GPU 字段，勿保存序列号或 UUID。

原始测试代码与报告保存在 `/Volumes/data/CodexProjects/Local-GPU-Math-Skill-20261115`；此路径是历史证据，不是 skill 执行依赖。

运行依赖使用已有环境。Wolfram 数值测试首次自动获取的官方 Accelerators 组件已校验后放在 `/Volumes/data/CodexData/runtimes/wolfram-paclets`，后续内核用 `-pacletbase` 指向该目录。运行库不打进 skill 包。
