# 检索渠道与全文定位

| 用途 | 渠道 | 注意 |
|---|---|---|
| 跨学科题录/DOI | Crossref、OpenAlex、Semantic Scholar、出版方 | 元数据和密钥规则按当前文档/响应确认 |
| 数学、物理、计算机 | arXiv、期刊/会议官网、dblp、OpenReview | arXiv 是预印本，接收状态另查 |
| 生物医学 | PubMed、Europe PMC、PMC、出版方 | PubMed 记录不等于 PMC 有全文；全文批量复用检查许可 |
| 中文 | 知网、万方、国家哲学社会科学文献中心、机构库、期刊官网 | 区分题录、摘要与授权全文，网络首发年份单列 |
| 仓储/接受稿 | CORE、OpenAIRE、HAL、Zenodo、机构库、作者主页 | 条目可能只有题录，也可检查文件列表，不根据页面无下载链接直接断言无全文 |
| 发现线索 | Google Scholar、普通网页搜索 | 片段不能核验结论，反爬失败不等于零结果 |
| DOI 开放副本 | Unpaywall DOI lookup、OpenAlex locations | 索引空结果不证明付费墙，落地页不等于 PDF |

Crossref 文本检索不是布尔检索引擎；arXiv 支持 `ti:`、`au:`、`cat:` 和 AND/OR。不同来源排名不直接拼成统一影响力排序。DOI 精确解析仍需与用户题名/作者核对。

## 官方 API 文档

- [Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)：`https://api.crossref.org/works` 与 `/works/{doi}`，可无邮箱请求；联系值只用用户提供的邮箱。
- [arXiv](https://info.arxiv.org/help/api/user-manual.html)：`https://export.arxiv.org/api/query`，串行调用至少间隔 3 秒，保持小批次和版本 ID，多个进程也避免突发。
- [Unpaywall](https://unpaywall.org/api)：`https://api.unpaywall.org/v2/{doi}?email=...`，需要邮箱，不伪造；保留 `url_for_pdf`、落地页和版本。只用 DOI lookup，不依赖搜索端点。
- [OpenAlex](https://developers.openalex.org/)：检查当前认证与配额，不固化“永久免费免密钥”假设。
- [PubMed](https://www.ncbi.nlm.nih.gov/books/NBK25501/) 与 [PMC OA](https://pmc.ncbi.nlm.nih.gov/tools/oa-service/)：按官方全文许可和接口限制获取。

源站故障、限流与权限错误单列，不伪装成无匹配。TLS 失败保留诊断，修复信任配置或换既有浏览器，不默认关闭校验。正式版未取得时可交付身份关系已核验的公开预印本/接受稿，显式注明版本。
