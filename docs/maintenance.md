# 维护与安装

规范文件位于 `skills/<name>/`，`catalog/skills.json` 提供分类、名称与兼容目标，`catalog/skill-files.json` 列出公开文件、SHA-256 和大小。源仓库修改后先重建清单并验证，再安装到本机。

## 安装与恢复

`python3 scripts/install_skills.py` 只预览。加 `--apply` 后更新清单内文件，相同字节不重写；未在清单中的本地全文、证据和其他文件保留。部分安装也包含总入口和工具引导的依赖及兼容入口对应的主技能。根目录中已有的 CODEX_HOME 符号链接按真实位置解析；技能内部被替换路径出现符号链接时拒绝写入，避免误改其他目录。

每次实际替换前创建 `.local/install-backups/<运行号>/`，保存旧字节、模式和 `journal.json`。先核对备份，再逐个原子替换，最后核验全部选定文件。中断时保留 journal，检查实际状态后恢复或重试，不把部分安装称为成功。

恢复先预览，再实际执行：

```sh
python3 scripts/install_skills.py --restore /absolute/path/journal.json
python3 scripts/install_skills.py --restore /absolute/path/journal.json --apply
```

恢复仅处理该次安装的文件；对安装之后又被编辑的文件拒绝覆盖。原来没有的文件只在其字节仍匹配本次安装内容时移除。不会删除其他文件或整个技能目录。

`.local/` 是持久本机材料，属于项目备份范围，禁止提交。安装备份和远端推送均不代表用户“备份”磁盘上的实际备份已完成；本次任务不更改备份配置。

## 计算运行

项目位于 `/Volumes/data/CodexProjects/Math-Research-Skills`。验证和可再生日志位于 `/Volumes/data/CodexTemp/Math-Research-Skills`，遵守 TMPDIR/TMP/TEMP/XDG_CACHE_HOME。data 未挂载时停止依赖磁盘的写入，不回退系统盘。Python 运算的重要脚本与最终输入/结果保留在研究项目，临时日志使用独立运行目录。

MATLAB 正式计算完成、输出保存并核验后及时退出进程。用户原有未保存工作先妥善保留；CLI 使用 `-batch`，超时只清理本次创建的进程组。

## 校验范围

结构校验检查 YAML、命名、兼容路由、校验和、明确的相对链接、脚本语法和公开包边界。旧来源清单可能列出未公开的 PDF/ZIP，不应用它验证当前公开子集。原作者阅读卡与数学验证记录作为来源保留，工具链演示仅证明对应功能实际执行，不验证技能中的全部数学结论。

新建或实质修改的技能另用当前可用 skill-creator 的 `scripts/quick_validate.py` 检查。安装和执行器的测试覆盖预览、保留旧证据、备份恢复、后续编辑保护、依赖失败与进程超时。
