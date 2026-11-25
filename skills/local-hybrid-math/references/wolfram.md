# Mathematica / Wolfram：CPU 与原生 Apple GPU

本机 Wolfram 15 原生 GPUArray 已实测。符号、精确/任意精度运算继续使用 CPU；适合的 Real32 数组与 FFT 可与 GPU 比较。

```wl
Get["/Volumes/data/CodexData/skills/local-hybrid-math/scripts/LocalGPUMath.wl"];
x=NumericArray[N[Range[4096]/1024.-2.],"Real32"];
r=LocalGPUMath`MetalEvaluate["SinExp",x];
If[!TrueQ[r["ok"]],Exit[2]];
y=r["result"];
```

`"SinExp"` 为 Sin(x)Exp(-x²)，`"Fourier"` 接受实数向量，使用 Wolfram 默认 FourierParameters，结果为 ComplexReal32。包装检查输入和最终运算数组均为 GPUArray，物化后计时，并与 CPU 相同 Real32 舍入输入比较。CPU 原生候选是 `Sin[Normal[x]] Exp[-Normal[x]^2]` 或 `Fourier[Normal[x]]`。

列表输入只有显式 `"AllowPrecisionLoss"->True` 才转换。已有任意精度/精确输入需要保留精度时使用 CPU，不转 GPU。当前包装容差为示例；按问题修改并实际复测。

创建 GPUArray 不能证明所有后续操作使用 GPU。官方文档说明不支持的操作可能回退 CPU；新算子先查当前 Apple 支持表，再验证设备与误差。其他矩阵任务可通过 `RunProcess` 参数列表调用 Python 自动调度器，检查 ExitCode、ok 与实际 device。

## 粒度与驻留

本机一次实际比较：4096 元素的逐元素 CPU 约 0.084 ms，GPU（输入驻留、含输出物化）约 0.977 ms；1048576 元素约 7.35 ms 与 4.41 ms。这个结果只指导相似规模的 warm 计算；首次 GPU 初始化、输入上传与 CPU 对照另计。

在 Notebook 的多步 GPU 计算中尽量保留 GPUArray，最后才 Normal；短任务选 CPU。换函数、尺寸或软件版本需重新测量，不能套用固定倍率。

## 批处理

`run_wolfram_batch.py --script <绝对.wl路径> --report <项目退出报告> --log <data临时日志>` 使用 `-script` 和 data 上的 `-pacletbase`，不改全局初始化或许可证。默认内核是 `/Applications/Wolfram.app/Contents/MacOS/WolframKernel`，可覆盖。

脚本保存后 `Exit[]`；正常脚本结束也退出。超时只清理自己启动的内核。交互 Notebook 则清除不用的数组，保存后按需结束本次内核。首次某些数值功能可能获取官方组件，缓存和临时文件应落在 data。
