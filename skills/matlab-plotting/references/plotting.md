# 论文绘图：按需要查阅

## 数据与图意

CSV/Excel 使用 `readtable`，含非标准表头时可指定 `VariableNamingRule="preserve"`，通过 `T.("中文列名")` 访问；先核对工作表、表头、单位、维度与缺失值。MAT 使用 `whos('-file',path)` 后按需 `load(path,'variable')`，不把整份文件倒入持久工作区。Excel 不默认使用 COM 或桌面 Excel。

缺失点保留断线或明确说明处理方式，不擅自插值、平滑、删异常值。排序、分组和聚合必须符合数据语义。对时间序列保留原时间单位；公式绘图记录域、采样与参数。统计误差的定义及样本量写入说明，不能把固定示意误差当作研究结果。

| 需求 | 原生函数与注意事项 |
| --- | --- |
| 趋势、模型比较 | `plot`；采样点与拟合曲线区分，多个系列辅以线型 |
| 二变量关系 | `scatter`；第三变量编码需有色条或尺寸图例 |
| 离散组 | `bar`；核对组顺序、类别标签，不误导性截断基线 |
| 误差或区间 | `errorbar`；显式交代 SD/SE/CI 等定义 |
| 矩阵热图 | `heatmap`；图表对象不同于 axes；缺失值颜色单独定义 |
| 连续二维场 | `imagesc`/`contourf`；核对 Y 方向和色轴，保持物理比例 |
| 三维场 | `surf`；坐标单位、视角、色条要清晰，必要时配等高线 |
| 多面板 | `tiledlayout` + `nexttile`；共享图例、色条及轴范围按图意设置 |

## 字体、尺寸和布局

- `paper_style` 优先探测 PingFang SC、Noto Sans CJK SC、Microsoft YaHei、Arial Unicode MS、Heiti SC；不存在时警告，不能声称已验证中文。可用 `listfonts` 查看真实字体。
- 中文和普通文本通常使用 `Interpreter='none'`，公式单独设置 `'latex'`。TeX/LaTeX 有独立排版机制，不保证服从 FontName；不要承诺仅靠 FontName 就能改变数学字体。
- 指定期刊最终尺寸时以最终缩放后的字号为准，常用单栏宽约 8.5 cm、双栏宽约 17–18 cm，具体服从用户投稿要求。
- 默认 helper 设置的是 Figure 画布尺寸；`exportgraphics` 紧边裁切会影响最终外框尺寸。R2025a+ 可显式使用 `Width`、`Height`、`Units`、`Padding`。例如要精确宽度，PNG 与 PDF 分别指定 `Width=8.5, Units="centimeters"`；保留自适应高度避免拉伸，并检查像素和 PDF 页面尺寸。
- 外置图例不要超出保存目标；多子图导出整个 figure 或 tiled layout。使用嵌套 panel 的图若遇到 adjacent containers 错误，导出正确的布局容器，或重新组织布局，不静默丢掉子图。
- 已有图修改保持轴尺度、数据、颜色映射及注释语义；不要为了统一样式把对数轴变线性轴。

## 交付与检查

PNG 默认 300 DPI；PDF 的矢量/栅格取决于 `ContentType` 和图形元素，不能仅凭扩展名声称纯矢量。FIG 只保留图形可编辑性，完整可复现还需要 `.m`、数据引用及辅助函数。重开 FIG 时指定 `new`/`invisible`，只关闭本次打开的句柄。

在源码旁交付所需 helper，使用相对路径。随机示例设置种子；纯公式示例可直接重建。外部原始数据只在授权范围内附带，数据未附带时说明路径和必需字段。

## 参考与依赖选择

本技能的脚本为原创实现，参考以下项目的职责划分和工作流，没有复制其代码：

- [MATLAB MCP Server](https://github.com/matlab/matlab-mcp-server)：MATLAB 执行与代码检查。
- [MATLAB Agentic Toolkit](https://github.com/matlab/matlab-agentic-toolkit)：工具与技能协作方式。
- [export_fig](https://github.com/altmany/export_fig)：原生导出无法满足特殊出版需求时评估；引入前检查版本、许可证和所需外部依赖。
- [gramm](https://github.com/piermorel/gramm)：复杂统计可视化的可选方案；部分统计方法依赖工具箱。
- [exportgraphics 官方文档](https://www.mathworks.com/help/matlab/ref/exportgraphics.html)：原生导出、尺寸和格式限制。
- [MATLAB macOS 命令行](https://www.mathworks.com/help/matlab/ref/matlabmacos.html)：`-batch`、退出码与启动参数。

默认只使用 MATLAB 内置绘图，不自动安装上述第三方绘图库。检索日期：2026-09-26。
