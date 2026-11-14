# GitHub 项目调研

日期：2026-10-04。依据官方 README，未安装或审计全部实现；后续采用需重新确认版本、许可、工具和依赖。

| 项目 | README 声明的用途 | 采用的思路 |
|---|---|---|
| [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | 多来源检索、CLI/MCP、统一结果、OA 回退 | 发现/获取分离、来源错误单列、统一记录 |
| [jannisborn/paperscraper](https://github.com/jannisborn/paperscraper) | 多学科题录、本地快照、PDF/XML 获取、文献计量 | 真实检索式/日期、可追溯快照 |
| [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | 本地论文库、arXiv 元数据/BibTeX、LaTeX 章节读取 | 版本 ID、文件/引用关联、下载/阅读分开 |

选择原创 Codex 技能与小型 Python CLI，不移植上游代码、不强依赖第三方服务器。已有两个技能保留，此技能统一检索与下载，也可独立运行。

paper-search-mcp 适合后续扩展，但其可选 Sci-Hub 接口不启用。其他项目的计量、监控和深入阅读不是本技能默认范围。采用第三方工具时固定实际验证过的版本，先读官方 CLI help，不猜参数。

自带代码依据 Crossref、arXiv 和 Unpaywall 官方 API 文档原创编写；本次仅借鉴工作流设计。
