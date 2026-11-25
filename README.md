# Math-Research-Skills

面向本机数学研究的技能库。整合本机技能及 Math-Research 的 64 项原始方法，并继续从文献提取可复核的数学工具。

从 **[`math-research`](skills/math-research/SKILL.md)** 开始。它按问题选择数学方法、概率专题、Python / MATLAB / Mathematica、文献与写作工作流；需要操作文件、网页或原生应用时，先检查当前可用工具。详细目录见 [全部技能](catalog/README.md)。

| 类别 | 内容 |
| --- | --- |
| 研究总入口 | `math-research` |
| 计算与绘图工具 | `math-tool-router`、`local-hybrid-math`、 `ipad-math-node`、`remote-math-compute`、`python-math`、`mathematica-math`、Mathematica 旧名兼容入口、`matlab-plotting` |
| 数学方法 | A–N：归一化、对偶、锥规划、熵、Bellman、Fourier、Carleson、概率尾界、跳跃过程、随机场、计算证书、凸几何等 |
| 专项研究核验 | 中心立方体弱端点、离散证明迁移、欧几里得张量几何、欧拉常数无理性 |
| 概率研究专题 | 测度收敛、鞅、集中、随机矩阵、Markov 混合、渗流、随机树、SLE、在线选择等 |
| 文献检索与获取 | 主题检索、知网、检索与下载、旧下载入口 |
| 论文写作、翻译与表达 | 数学论文、一般学术论文、反防御性写作、论文翻译、旧 PDF 翻译入口 |
| 数学建模竞赛 | 模型与账本审计、论文排版、交付支撑包 |
| 指定模型咨询 | 用户明确要求时的 Astra 咨询 |

## 使用与安装

在 Codex 中调用 `$math-research`；需要选用和执行数学工具时直接调用 `$math-tool-router`，需要 Python 运算时也可调用 `$python-math`。技能名保持不变，原有引用仍可使用。三个兼容入口汇入对应主流程，避免维护相互冲突的默认行为。

安装默认先预览，不删除本机原有文献、证据、缓存和其他技能：

```sh
python3 scripts/install_skills.py
python3 scripts/install_skills.py --apply
```

默认安装到 `${CODEX_HOME:-~/.codex}/skills`，也可用 `--target /absolute/path/skills`。仅安装部分入口可重复使用 `--skill`；会一并安装总入口及必要的兼容目标。替换文件前逐一备份到 `.local/install-backups/`，安装后核对文件哈希。恢复方式见 [维护与安装](docs/maintenance.md)。

Python 技能检查已有环境与实际模块导入，支持精确计算、SymPy、NumPy/SciPy 和高精度运算，并提供记录日志、超时和取消的执行器。需要的库尚未安装时明确报告；技能不自动安装软件。

MATLAB 技能在计算、导出与结果核验完成后保存脚本和结果，**及时退出 MATLAB，释放内存**。命令行用自动退出的 `-batch`；退出前保留未保存工作。

论文写作按任务选择 `math-paper-writing` 或 `academic-paper-writing`，表达精简使用 `anti-defensive-writing`。精简保留决定数学结论成立的假设、量词和证据范围。

## 来源与公开边界

旧仓库来源：[`alizeisnotalice/Math-Research`](https://github.com/alizeisnotalice/Math-Research)，固定提交 `ff7112e09e8aa0adc7f66b2f79cad1c88f13f1fa`。64 个方法在本机均已有差异，采用本机修订并记录双方逐文件哈希；旧 T 项目保持只读。详见 [迁移记录](provenance/README.md)。

公开版包含技能正文、参考说明、来源卡、示例和必要计算代码。原本机的论文全文、全文提取件、逐页截图、交付 ZIP 和编译缓存保留在原处；约 6 GB 的非运行附件不进入 Git。需要原文时按来源索引获取，缺少附件时按技能内的附件说明处理。

此次整理验证技能结构、文件、工具运行和安装行为。历史“已读”“审核通过”等记录保持其原来源含义，具体数学结论按任务重新核验。本次发布不为第三方文献或来源资料新增许可证。

## 维护

```sh
python3 -m pip install -r requirements-dev.txt  # 仅开发校验需要 PyYAML
python3 scripts/rebuild_catalog.py
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

运行目录与数据约定、详细验证记录见 [维护文档](docs/maintenance.md) 和 [本次整理验收](docs/validation-2026-11-15.md)。
