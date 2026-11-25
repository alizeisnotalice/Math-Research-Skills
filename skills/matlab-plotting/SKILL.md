---
name: matlab-plotting
description: 使用本机 MATLAB 实际运行脚本，制作或修改论文与数学建模图；支持 CSV、Excel、MAT 和公式，检查中文、公式与排版，交付 PNG/PDF、可编辑 FIG 和可复现 .m 源码。用户要求 MATLAB 绘图、论文图美化、多子图或已有 MATLAB 图修改时使用。
---

# MATLAB 论文绘图

把数据或公式转成实际执行并经视觉检查的 MATLAB 图。优先使用可用的官方 MATLAB MCP；没有 MCP 时直接使用本机 MATLAB。不能用其他绘图库生成图片后声称来自 MATLAB。

## 工作流程

1. **读取输入。** 检查文件、列名、变量、单位、缺失值、样本数及用户要求。CSV/Excel 用 `readtable`，MAT 先 `whos('-file', path)`，再按变量加载。公式核对定义域与参数。只询问无法从材料确定、且会改变图意的关键问题；未提供单位时不要编造。
2. **确定图意。** 时间/连续趋势用折线，关系用散点，离散组比较用柱状，二维场用热图/等高线，三维场用曲面。误差棒必须知道表示 SD、SE、CI 还是其他量；缺少依据时不自行计算或补画。演示数据明确标为演示，不能混入研究结果。
3. **保存源码。** 先保存 `.m` 再执行。脚本名使用 `make_plot.m` 这样的合法 MATLAB 标识符，不使用连字符。以 `fileparts(mfilename('fullpath'))` 定位配套文件；不要依赖智能体会话里的工作区变量。MATLAB `run` 会临时切换到脚本目录，输入输出用明确路径。只画已有结果，不顺带重跑大型仿真或更改模型。已有 FIG 用 `openfig(path,'new','invisible')` 打开副本，另存新文件；修改现有脚本时保留数据处理语义。
4. **执行与核验。** 按下节选择调用方式，先检查脚本，再实际运行。核对曲线数据与输入对应、输出文件存在且非空；脚本成功不等于图片合格。
5. **看图后修改。** 使用图像查看工具打开实际导出的 PNG，检查中文缺字、公式、单位、图例遮挡、裁切、颜色、比例和多子图对齐。修改后重新执行并检查受影响的图片。无法看图时明确说明未完成视觉验收。
6. **交付。** 默认提供 PNG、PDF、FIG、`.m` 及必要辅助文件；图片在会话中预览。说明数据来源、关键变换、执行后端和未解决限制。绝对路径仅用于本次调用；源码尽量用相对路径以便迁移。

用户要求使用远端，或 [数学工具引导](../math-tool-router/SKILL.md) 已根据本次授权选择远端时，按 [远程数学计算](../remote-math-compute/SKILL.md) 核验身份、软件与许可。

## 调用方式

### 官方 MCP 优先

先从当前工具列表发现 MATLAB 工具，名称可能有服务器前缀；不要只凭配置文件存在判定可用。首次使用 `detect_matlab_toolboxes` 确认版本及依赖，使用 `check_matlab_code(script_path=绝对路径)` 检查，再 `run_matlab_file(script_path=绝对路径)`。短探测或检查可用 `evaluate_matlab_code(code=..., project_path=绝对路径)`。

脚本显式加入自己交付包内的辅助函数路径。函数局部状态或专用变量名避免污染持久会话；不要使用 `clear all`、`close all`、`restoredefaultpath` 或未保存工作直接退出用户会话；重置搜索路径会移除 MCP 自身函数。只关闭本次创建的图。新环境接入和工具参数见 [MCP 接入](references/mcp-setup.md)。

### 命令行备用

`<skill>` 表示当前技能目录，替换为真实绝对路径。

```sh
python3 "<skill>/scripts/run_matlab.py" --detect
python3 "<skill>/scripts/run_matlab.py" "/absolute/path/make_plot.m" \
  --workdir "/absolute/path/project" --timeout 300
```

可传 `--matlab "/Applications/MATLAB_R2026a.app/bin/matlab"`，或设置 `MATLAB_EXECUTABLE`；否则依次检查 PATH 和 macOS Applications。Python 3 标准库即可，首版只在 macOS ARM64 验收。

`--workdir` 是启动目录；`run` 执行期间的相对路径以脚本所在目录为准。日志默认位于工作目录的 `work/matlab-runs/<唯一运行编号>/`，可用 `--log-dir` 改变父目录。先输出日志与状态文件路径，完成后输出 JSON；返回码 0 成功、2 输入错误、124 超时、130 键盘中断、143 SIGTERM 取消，其余为 MATLAB/启动失败。状态 JSON 记录 PID、实际命令和执行时间。超时只停止本次创建的进程组，产物可能不完整。

MCP 不存在或确认尚未开始执行时可切换命令行。代码错误先修复代码；连接丢失、超时或工具返回不明时先检查日志、进程和文件，确认原任务已停止再重跑，不能盲目双重执行。许可证、权限、Qt 报错见 [故障与兼容](references/troubleshooting.md)。

## 图形与导出

默认白底、简洁彩色、10 pt 字号、1.5 pt 曲线、约 16×10 cm；用户指定的期刊尺寸、字体、样图和配色优先。颜色同时辅以线型或标记。中文文本用支持 CJK 的字体；公式单独用 LaTeX，避免把中文标签整体交给 LaTeX 解释器。

配套函数可复制到交付目录的 `helpers/`，随源码交付；也可把所需逻辑内联到源码。不要让交付脚本只依赖本机私有技能路径。

```matlab
plotRoot = fileparts(mfilename('fullpath'));
addpath(fullfile(plotRoot, 'helpers'));
fig = figure('Visible', 'off');
paper_style(fig); % 绘制前建立局部配色、字体与线宽默认值
ax = axes(fig);
% 在这里使用已经核对的数据绘图
% 中文标签使用 Interpreter='none'；公式单独设置 Interpreter='latex'
paper_style(fig); % 绘制后统一轴、图例与色条；不重写已有数据颜色和线型
files = paper_export(fig, fullfile(plotRoot, 'figure_01'));
close(fig);
```

- `paper_style(fig, Width=16, Height=10, FontSize=10, FontName="")`：宽高单位 cm；自动探测已安装中文字体，不修改 `groot` 全局设置。尺寸是画布尺寸，紧边导出的尺寸可能不同；需要精确投稿尺寸时按绘图规范设置导出尺寸并检查结果。
- `paper_export(fig, basePath, Resolution=300, ContentType="vector", SVG=false, Overwrite=false, Padding=6)`：导出 PNG/PDF/FIG，按需 SVG；`basePath` 不带扩展名，R2025a+ 导出默认保留 6 pt 外边距。复跑自己本次生成的文件可显式设置 `Overwrite=true`，不要覆盖用户原图。
- 线图和常规多子图默认矢量 PDF；复杂曲面或密集透明图用 `ContentType="image"` 或 `"auto"`，向用户说明 PDF 含栅格内容。PNG 始终是栅格图。
- 对修改已有图，默认样式辅助函数可能改变尺寸、字体与轴框；只需局部修正时直接设置相关属性，不强行套用整套风格。

更多数据读取、图型选择、精确尺寸和来源见 [论文绘图规范](references/plotting.md)。无需默认安装 export_fig、gramm 或整个 Agentic Toolkit。


## 计算结束后释放内存

保存脚本、结果及必要工作区，确认本次启动的 MATLAB 已退出。命令行批处理自然退出。可确认由本次任务新建的独立会话才可主动退出。既有桌面或 MCP 会话只释放本任务创建的图形和资源，保留原有会话与工作。
