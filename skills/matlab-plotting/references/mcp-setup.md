# 官方 MATLAB MCP 接入

仅在安装/迁移 MCP 或排查工具不可见时阅读。本技能的命令行路径不依赖 MCP。

## 本机配置

验收环境：macOS ARM64，MATLAB R2026a Update 4。官方 server 固定为 v0.14.0；二进制单独安装，不打包进可移植技能包。

本机二进制位置：`~/.local/share/matlab-mcp/v0.14.0/matlab-mcp-server`。

```sh
codex mcp add matlab -- "/absolute/path/matlab-mcp-server" \
  --matlab-root="/Applications/MATLAB_R2026a.app" \
  --matlab-session-mode=new \
  --matlab-display-mode=nodesktop \
  --disable-telemetry=true
```

使用当前工作区作为 MCP root，不把本次任务目录写死为全局启动目录。调用 `evaluate_matlab_code` 时传入实际 `project_path`；脚本自行定位数据和输出。

迁移安装时从 [官方 Releases](https://github.com/matlab/matlab-mcp-server/releases) 选择对应平台版本，核对发布资产 SHA-256；不要运行第三方安装脚本。不覆盖已有同名配置，先检查是否需要合并。Codex 配置有其他 MCP 服务时只更新 `matlab` 条目。修改前保留原配置备份，备份不放进对外交付包。

新配置可能需要新任务或重启 Codex 才会加载。`codex mcp list` 只验证注册；真实验收必须完成协议握手、工具发现和 MATLAB 脚本运行。通过独立 MCP 客户端验证成功，不等于当前任务已动态获得这些工具。

## 工具接口（v0.14.0）

| 工具 | 用途 | 输入 |
| --- | --- | --- |
| `detect_matlab_toolboxes` | 检查 MATLAB 与工具箱 | 无 |
| `check_matlab_code` | 静态检查 | `script_path` 绝对 `.m` 路径 |
| `run_matlab_file` | 执行已保存脚本 | `script_path` 绝对 `.m` 路径 |
| `evaluate_matlab_code` | 简短探测、验证变量或文件 | `code`、`project_path` |
| `run_matlab_test_file` | 执行 MATLAB 单元测试 | `script_path` |

以当前 `tools/list` 的 schema 为准。检查结果中的性能/风格建议不都需要修改；先处理会导致图错误的问题。工具调用结果可能包含图片，但仍以实际保存文件作为交付证据。

独立会话避免影响用户桌面 MATLAB。若用户明确要求连接现有会话，遵循官方 `existing` 模式配置；这需要额外 toolbox 和 `shareMATLABSession()`，不可直接把 `new` 改为 `existing` 并保留互斥启动参数。

来源：[官方 MCP README](https://github.com/matlab/matlab-mcp-server)、[官方 Agentic Toolkit](https://github.com/matlab/matlab-agentic-toolkit)。检索日期：2026-09-26。
