# 旧流程专项参考

仅在当前任务需要其下载渠道或版面操作时参考；执行入口、输出格式和工具可用性以当前主技能及用户要求为准。

# 批量下载学术文献 PDF

## 适用场景
用户给一份文献清单（DOI / 链接 / 题录表 / txt），要求"把这些文献下载下来"。

**核心原则：先探清"哪些合法可得"，再动手。** 绝不使用盗版渠道（sci-hub 之类）。付费墙文献就老老实实标注"未取得"并给出合法补取路径——这比硬凑一份来源不明的 PDF 有价值得多。

**产出两样东西：**
1. 一个目录，里面是可打开的 PDF（文件名带清单编号前缀，便于与清单对齐）
2. 一份 `00_下载说明与清单.md`：分「已取得」「未取得及原因」「顺带发现的线索」「技术要点」四段

---

## 本机环境（先记住，能省掉大量试错）

| 事实 | 后果 |
| --- | --- |
| 环境变量里有 `HTTP_PROXY=http://127.0.0.1:55485`（沙箱透明代理，会做 TLS 中间人） | 直连 HTTPS 常报 `SSL_ERROR_SYSCALL` / "unable to establish a secure connection"。**加 `-k` 即可绕过**，对公开学术 PDF 可以接受 |
| DNS 是**全局 fake-IP**（所有域名解析到 `28.0.0.x` / `28.0.2.x`） | **不要用 `--resolve <host>:443:<真实IP>` 试图绕开**——能查到真实 IP（走 Cloudflare DoH），但链路本身仍要过代理，连不通。也别以为是 DNS 问题 |
| Chromium 在沙箱内被直接 SIGKILL（`rc=137`，`--version` 都无输出） | **不要指望无头浏览器绕 Cloudflare**。ms-playwright 里的 chromium 装了也白装 |
| Python 受管解释器已装 `fitz`(PyMuPDF) | 校验 PDF 页数/标题直接用 |
| 没有 `pdftotext` / `mutool` / `wget` | 用 `curl` + PyMuPDF |

---

## 路线阶梯（按顺序试，命中即停）

### ① 清单里给的直链 / 作者主页
先用 `curl -sL -k` 试。作者自存版（大学个人主页）往往一次就中，这是最干净的路。
```bash
curl -sL -k --max-time 90 -A "$UA" -o out.pdf -w "http=%{http_code} size=%{size_download}\n" "$URL"
head -c 4 out.pdf   # 必须看到 %PDF
```

### ② 开放获取判定：OpenAlex（首选，免费无 key）
```
https://api.openalex.org/works/doi:<DOI>
```
读 `open_access.is_oa` / `oa_status` 和 `locations[].pdf_url`。
- `oa_status: gold|hybrid|green|bronze` → 有开放副本，但**别急着直接用 `locations[].pdf_url`**（Springer 的 `content/pdf/` 直链有机器人挑战，见 ④）
- `closed` → 直接跳到 ④ 找快照；仍拿不到就判付费墙

Unpaywall（`https://api.unpaywall.org/v2/<DOI>?email=<你的邮箱>`）作为交叉验证。

### ③ 预印本平台（拿到也算，但必须标注版本差异）
- arXiv：`https://arxiv.org/abs/<id>` → `/pdf/<id>`
- HAL：`https://hal.science/<halId>` ← ⚠️ 现在挂了 **Anubis 反爬**（需浏览器执行 JS），`curl` 只会拿到 `Making sure you're not a bot!` 页面，**别再试各种 URL 变体了，直接放弃并给用户浏览器链接**

### ④ Wayback Machine —— 破 Cloudflare 的关键手段 ⭐
**症状：** bepress 系机构仓储（`digitalcommons.*`、`bearworks.*`）的 `viewcontent.cgi` 直链返回 **403 + 一个 6KB 的「Just a moment...」Cloudflare 挑战页**。加完整浏览器头、加 Referer、加 Sec-Fetch-* **全都没用**。

**做法：**
```bash
# 1) 查快照
curl -s "https://archive.org/wayback/available?url=<urlencoded 原URL>"
# 2) 用 id_ 原始文件模式下载（关键！缺了 id_ 会拿到 Wayback 包装过的 HTML）
curl -sL -k -o out.pdf "https://web.archive.org/web/<时间戳>id_/<原URL>"
```
- **`id_` 后缀是全部要点**，别用 `/web/<ts>/<url>` 的裸形式。
- Springer 的 `content/pdf/<doi>.pdf` 同样有挑战页（返回约 3 KB 的 JS 页，`sig` 是 `<!DO`），走 Wayback 快照可解决。
- archive.org 有速率限制：连续查会返回 **HTTP 429 且响应体为空**（`json.load` 会抛 `JSONDecodeError: Expecting value`）。查一条 `sleep 3~5`，或改用 curl 直查不解析 JSON。

### ⑤ 机构仓储落地页解析
若清单给的是落地页而非直链，**先把落地页抓下来，从 HTML 里抽真实 PDF 链接**，比猜 article id 靠谱：
```bash
grep -oE 'https?://[^"'"'"' <>]*(viewcontent|\.pdf|download)[^"'"'"' <>]*' page.html | sort -u
```
⚠️ **注意判断"这个仓储到底有没有存全文"**：同一位作者、同一个仓储，有的条目有 `viewcontent.cgi` 链接，有的只有题录。**没有下载链接 = 该仓储没存全文**，不代表被拦截，别浪费时间绕。

### ⑥ 判付费墙，给出补取路径
Unpaywall 说 `closed` + Wayback 无存档 + 各预印本平台无 → **判定为付费墙**，停止尝试（**不要**去找盗版源）。在清单里写清：
- 出版社与 DOI
- **代为取得的摘要**（用 WebSearch 抓 ResearchGate / ERIC / Springer 文章页的摘要文本，这对用户很有用）
- 合法补取路径：图书馆订阅 / 馆际互借(ILL) / 向作者索要 / 出版社单篇购买

### ⑦ 网络不可达的条目
若 https 报 `SSL_ERROR_SYSCALL`、http 空回复、DoH 查到真实 IP 后直连仍超时 → **是链路被阻断**，不是技术问题。如实标注，让用户换网络（手机热点）自己取。

---

## 校验：别信 `size`，信 `%PDF`
```python
import fitz, glob, os
for f in sorted(glob.glob('*.pdf')):
    d = fitz.open(f)
    print(f, round(os.path.getsize(f)/1024), 'KB', d.page_count, '页', d[0].get_text()[:80].replace('\n',' '))
```
**必须逐篇核对页数是否与题录相符**（例如 AJP 69(2):162–173 应约 12–13 页）。页数对不上说明下到了摘要页 / 错误论文 / 拦截页。
**失败产物要立刻删掉**——落盘的 Cloudflare 挑战页和 Anubis 页都是 `.pdf` 后缀的 HTML，混在目录里极易误认为成功。

---

## 报告模板要点

`00_下载说明与清单.md` 至少包含：

1. **总览表**：已取得 N 篇（列编号）/ 付费墙 N 篇 / 不可达 N 篇
2. **已取得表**：文件名 | 页数 | **版本说明**（作者稿？预印本？网络首发版？正式版？）| 获取途径
   - ⚠️ **版本差异必须显式标注**：拿到 arXiv 预印本 ≠ 拿到期刊正式版，页码/图号可能不同。这是最容易坑到用户的地方
3. **未取得表**：原因 + 已代取的摘要 + 合法补取路径
4. **顺带发现的线索**：相关性更高或免费的文献、该领域的文献总目录（如 Springer 的 *Pendulums in the Physics Education Literature: A Bibliography* 这类），对用户价值很高
5. **技术要点**：本次踩到的坑，便于复用

**打包交付**：`present_files` 只分享文件不分享文件夹，所以要打 zip。⚠️ **macOS 的 `zip` 命令默认不写 UTF-8 文件名标志**，中文文件名在 Windows 上解压会乱码，`unzip -l` 看也是乱码。**改用 Python `zipfile`**：
```python
import zipfile, os
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(os.listdir(root)):
        if not f.startswith('.'): z.write(os.path.join(root, f), os.path.join(root, f))
```

---

## 反模式（都踩过，别重复）

| 别做 | 为什么 |
| --- | --- |
| 用无头 Chromium 过 Cloudflare | 沙箱内被 SIGKILL（rc=137）；即便装 playwright-core 也起不来 |
| 反复重试同一个被拦的直链、换着花样加请求头 | Cloudflare 托管挑战不看请求头，浪费 10+ 分钟 |
| 用 `--resolve` 配真实 IP 直连 | 本机是全局 fake-IP + 强制代理，链路绕不过去 |
| 把 stderr 管进 `grep` 看错误 | 错误信息会被过滤，只剩"文件不存在"，看不出真因 |
| 把没验证的 `<!DO` 开头的文件留在目录里 | 用户会以为下到了 |
| 为付费墙文献去找非官方镜像站 | 合规红线，不做 |
