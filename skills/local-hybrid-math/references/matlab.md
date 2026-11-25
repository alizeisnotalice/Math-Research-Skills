# MATLAB：原生 CPU 与本机 Metal

本机 R2026b 的原生可用 GPU 数实测为 0。CPU 运算使用 MATLAB 自己的数值库；GPU 运算经本机 Python/PyTorch 调用 Apple Metal。原生 `gpuArray` 的硬件要求见官方来源。

只在本次会话添加 skill 的 scripts 目录：

```matlab
addpath('/Volumes/data/CodexData/skills/local-hybrid-math/scripts');
A=single([1 2 3;-1 0 4]); B=single([2 -1;0 3;1 2]);
[C,r]=local_compute("matmul",struct('a',A,'b',B));
```

`local_compute` 默认优先原生 CPU，避免为短任务启动外部解释器。double 输入留在 CPU，混合 single/double 的原生 CPU 候选提升为 double。

想实测 GPU 竞争时：

```matlab
[C,r]=local_compute("matmul",struct('a',A,'b',B),BenchmarkGPU=true);
```

它同时保留实际原生 CPU 结果，测量完整桥接墙钟耗时（Python 启动、MAT 传输、GPU 计算、CPU 对照），只有 GPU 至少快 10% 才选用；本次会话按形状/类型记住测量。初次测速有额外耗时。显式 `Backend="cpu"` 或 `Backend="mps"` 可固定路径。

GPU 专用包装也可直接用：

```matlab
[C,r]=local_gpu("matmul",struct('a',A,'b',B));
[Y,r]=local_gpu("sin_exp",struct('x',single(X)));
[S,r]=local_gpu("sum",struct('x',single(X)));
assert(r.ok && startsWith(string(r.device),"mps"));
```

GPU 接口默认拒绝 double；显式 `AllowPrecisionLoss=true` 才转 float32，并报告舍入误差。`Python="/绝对路径/venv/bin/python"` 覆盖环境选择。需要 double 则直接用原生 CPU。

MAT 文件传输保留行列布局和 single 类型，支持大于 JSON 上限的矩阵；返回后清理临时文件。默认 scratch 在 `/Volumes/data/CodexTemp/local-gpu-math`。结果和报告另存到项目。

多步 GPU 任务应从 MATLAB 一次启动项目专用 Python 脚本，在 Python 内保持设备数组；不要每轮启动解释器。即使 GPU 内核更快，短桥接通常仍由 MATLAB CPU 获胜。

## 保存与退出

优先用 `run_matlab_batch.py --script <绝对.m路径> --report <项目内退出报告> --log <data临时日志> --timeout 180`。它通过 `-batch` 运行，记录退出码与启动前后主进程，超时只清理自己启动的进程组。

脚本中先保存结果。`close all` 只关闭图窗；交互会话应在保存用户工作后 `quit` 并核验主进程退出。MathWorks 许可证辅助服务与 MATLAB 主计算进程分别记录，不把辅助服务当作计算仍在运行。
