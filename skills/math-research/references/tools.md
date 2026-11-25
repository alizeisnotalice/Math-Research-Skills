# MATLAB 与电脑工具说明

数学计算的后端选择和探测由 [数学工具引导](../../math-tool-router/SKILL.md) 负责。

## MATLAB

发现当前 `detect_matlab_toolboxes`/`evaluate_matlab_code`/`run_matlab_file` 等实际工具名及参数。首次确认版本和所需工具箱；长代码存 `.m` 后运行。使用局部变量或函数，避免污染用户会话；不要 `clear all`、`close all`、`restoredefaultpath` 或未保存工作直接退出已有会话。保存脚本与核验后的结果。命令行优先使用自动退出的 `-batch`。核对本次启动的软件已退出，对既有会话只释放本次创建的资源。MCP 不可用时按 `matlab-plotting` 的 CLI 指南选择已安装 MATLAB，不默认其存在于 PATH。

## 何时操作电脑

- 文件读取、改脚本、批处理与 Git：使用文件/终端工具，采用明确路径；不可把仅打开软件记成计算完成。
- 云端文献或文档：连接器足够时先用连接器；需网页登录或交互时再选当前可用浏览器工具。已有 `ego-browser` 等技能仅在对应浏览器确实可用时读取，不复制其通用实现进本仓库。
- 原生 Notebook、MATLAB 桌面或图形编辑：只有任务需要界面且没有可行专用接口时，使用当前原生电脑控制工具。工具缺失时可用应用正式支持的 CLI/脚本接口；不编造点击、截图或已观察的界面状态。
- 操作范围来自用户任务和当前授权。读取/可恢复编辑按授权继续；对外发送、发布、购买及其他有实际外部影响的动作遵循会话已有授权，不从本技能自行增加权限。

新项目默认位于 `/Volumes/data/CodexProjects`；中间件与缓存按当前用户约定放 `/Volumes/data/CodexTemp`。尊重 TMPDIR/TMP/TEMP/XDG_CACHE_HOME；data 未挂载则停止依赖磁盘的写入。此处是当前用户的本机存储约定，不用于猜测其他电脑的布局。
