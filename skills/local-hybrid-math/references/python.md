# Python 自动选择 CPU / Metal

使用已有 `$HOME/.venvs/main/bin/python`。`hybrid_math.py` 需要现有 NumPy/PyTorch，MAT 传输还需要 SciPy；不会自动安装或切换系统环境。

## 请求与执行

在项目中保存请求 JSON：

```json
{
  "operation": "matmul",
  "dtype": "float64",
  "backend": "auto",
  "verify": "full",
  "inputs": {
    "a": {"data": [1, 2, 3, 4, 5, 6], "shape": [2, 3]},
    "b": {"data": [1, 2, 3, 4, 5, 6], "shape": [3, 2]}
  }
}
```

用参数列表执行：

```python
subprocess.run([python, hybrid_script, "--request", request_path,
                "--report", report_path], check=True, timeout=120)
```

`python`、`hybrid_script` 和输入输出均用实际绝对路径。检查退出码、报告 `ok`、`device`、`selection` 和 `verification`。

- `backend`：`auto`、`cpu`、`mps`。float64 自动留在 CPU；显式 GPU 不可用或不支持该精度时失败。
- `dtype`：必须明确 `float32` 或 `float64`。向低精度转换需 `allow_precision_loss:true`，报告输入舍入误差。
- `operation`：`matmul` 使用 `a,b`；`sin_exp` 和 `sum` 使用 `x`。`sin_exp` 为 sin(x)exp(-x²)。
- `verify`：默认 `full`，全输出与 CPU float64 对照；`sample` 对矩阵取最多 64 个确定位置、数组最多 128 个位置，求和仍核完整标量；`none` 必须显式选，报告为未验证计算。
- `rtol/atol`：float32 示例默认 5e-4/5e-5，float64 为 1e-10/1e-12。按任务修改。

输入格式：

| 形式 | 约定 |
|---|---|
| `{"data":[...],"shape":[m,n]}` | 一维扁平 C/逐行顺序 |
| `{"npy":"/绝对路径/a.npy"}` | 禁止 pickle，通常存 float32/float64 |
| `{"mat":"/绝对路径/input.mat","variable":"a"}` | MAT-v5/v7；不支持 MATLAB v7.3/HDF5 |

超过 100000 个元素的输出用 `output_npy` 或 `output_mat` 的新绝对路径。MAT 输出变量是 `result`；已有输出和输入不会被覆盖。估算作业超过 512 MiB 时拆分。

CPU 参考基于**相同计算类型的已舍入输入**，输入舍入误差另外列出。`sample` 通过只表示抽查通过；`none` 的 `ok` 仅表示执行成功。科学结论还需适合问题的数学验证。

## 重复批处理

将 skill 的 scripts 加入本次 Python `sys.path` 后 `import hybrid_math`，循环调用 `hybrid_math.run_job(request)`，让解释器和校准缓存复用。该函数会改变本进程 PyTorch CPU 线程设置，应在自己拥有的进程中使用，不要多个线程同时对它调参。

并行作业启动前设置 `LOCAL_MATH_CPU_BUDGET=4` 等明确预算，调度器会把 CPU 候选线程数限制在预算内，并在导入库前设置 OMP/OpenBLAS/Accelerate 的线程上限。多个 CPU 作业的预算之和不应超过可用核数。未设置时单个作业可比较本机全部核数；NumPy 默认线程由现有 BLAS 管理，实际测速决定选择。

多步 GPU 算法直接使用 PyTorch，导入前设置 `PYTORCH_ENABLE_MPS_FALLBACK=0`，显式 `device="mps"`，确认每个关键结果的设备。输入一次上传、循环保持 MPS 数组、最后下载一次。用 `benchmark_residency.py --report <绝对路径>` 比较实际多步 Markov 传播的 CPU/GPU 成本。

原生 GPU 专用接口 `gpu_math.py probe/run` 保留，始终要求 MPS。它不是自动调度器，不能把 CPU 结果算作 GPU 成功。

## 计时

GPU 异步执行，计时前后同步。自动调度报告区分校准、含传输的选定操作、核验和本次作业总耗时；解释器导入与外部调用开销另计。小任务 CPU 获胜是正常结果。

长会话及时删除无需的张量，必要时 `torch.mps.empty_cache()`；仍被引用的数组不会因此释放。短脚本退出后释放上下文。
