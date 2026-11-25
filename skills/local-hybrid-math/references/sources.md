# 官方依据

2026-11-15–16 核对，配合本机实际测试。文档支持范围不能代替具体操作的精度、设备与性能验证。

- [MathWorks R2026b GPU Computing Requirements](https://www.mathworks.com/help/parallel-computing/gpu-computing-requirements.html)：MATLAB 原生 GPU 的 NVIDIA 硬件要求；本地 CUDA 实现与 count=0 实测交叉核对。
- [PyTorch 2.15 MPS backend](https://docs.pytorch.org/docs/2.15/notes/mps.html)：显式 MPS、可用性检查，Metal 不支持 float64/complex128。
- [Wolfram GPU Computing with Apple](https://reference.wolfram.com/language/guide/GPUComputing-Apple.html.en)：Apple 原生数组、FFT 和函数支持。
- [Wolfram GPUArray](https://reference.wolfram.com/language/ref/GPUArray.html)：NumericArray 类型、GPUArrayQ、Normal 与不支持操作的 CPU 回退。
- [Wolfram $UserBasePacletsDirectory](https://reference.wolfram.com/language/ref/%24UserBasePacletsDirectory.html.en)：`-pacletbase` 与组件存储目录。
- [WolframKernel](https://reference.wolfram.com/language/ref/program/WolframKernel.html.en)：独立 `-script` 批处理。

运行代码使用现有本机环境。其他 GPU 平台、新算子与新版本应单独验证。
