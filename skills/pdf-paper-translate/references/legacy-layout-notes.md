# 旧流程专项参考

仅在当前任务需要其下载渠道或版面操作时参考；执行入口、输出格式和工具可用性以当前主技能及用户要求为准。

# 学术论文 PDF → 中文排版

## 适用场景
用户给一个论文 PDF 链接、本地路径或一个文献包（zip／多篇 PDF），要求"翻译并生成 PDF（或 Word）"。

**两条产出路线，先按需求选：**
- **手写 XeLaTeX 路线**（正文 Step 1–5）：单篇、图表丰富、要复用原图、追求版面精致的论文 → 产出高质量单篇 PDF。
- **Pandoc 路线**（见文末「Pandoc 路线」）：多篇合集、需要同时给 PDF + Word、或用户要在 Word 里批注 → 产出 Markdown 源 + DOCX + PDF 三件套。**Word 需求只有这条路能走**，手写 LaTeX 不生 docx。

本机基线：pandoc 3.11（`/opt/homebrew/bin/pandoc`）、XeLaTeX/TeX Live 2026 含 ctex、受管 Python 已装 PyMuPDF。**没有** pdftotext / pdfinfo / mutool。

## 环境
- Python 用受管解释器：`/Users/zhengzhihao/.workbuddy/binaries/python/envs/default/bin/python`（已装 PyMuPDF/fitz、Pillow、numpy）。
- 编译用 `/Library/TeX/texbin/xelatex`（TeX Live 2026，含 ctex）。
- 本机**没有** pdftotext / pdfinfo / mutool，别去找。

## Step 1 — 取文本与总体结构
```python
import fitz
d = fitz.open(pdf)
for i, p in enumerate(d):
    print(i+1, len(p.get_images(full=True)), len(p.get_text()))
```
导出全文到一个 txt，再分段 Read（一次读太多会超上下文）。
**注意**：`page.get_text()` 抽数学公式会丢括号、打乱上下标顺序 → 公式必须按物理含义重建，不能照抄文本层。

## Step 2 — 裁剪并复用原图
用 `scripts/extract_figs.py`（基于 `FIG. N.` caption 定位 + 行墨迹投影）。
- 300 dpi 渲染灰度 → 在 caption 的 x 区间内算每行墨迹 → 从 caption 上沿向上走，空白行连续超过 `GAP_TOL≈4pt` 即停。
- **已知坑**：彩色热图（2D 光谱那种）浅色区灰度 >200 会被当成空白，导致图被截断。必须把裁好的图拼成 **montage 一次性目视核验**，异常的图手动改 `fig_boxes.json` 里的 rect 重裁。
- 不要用 `get_images()`：论文插图多为矢量，抓不到。
- 首页标题/作者的中文名在文本层取不到 → 渲染首页高倍位图（dpi=600，裁作者行）用视觉读取，不要瞎猜汉字。

## Step 3 — 写 XeLaTeX 中文稿
- `\documentclass[11pt,a4paper,fontset=macnew]{ctexart}`；`geometry` 上下 2.5cm、左右 2.4cm。
- 正文单栏（重公式的论文比双栏好排得多）；图用原图 `\includegraphics`，caption 译成中文；参考文献保留原文语种，用 `thebibliography` 手工录入。
- 编号对齐原文：正文 `\thesection=\Roman{section}`；附录 `\appendix` 后 `\renewcommand{\theequation}{\thesection\arabic{equation}}` 且每个附录 `\setcounter{equation}{0}`，得到 (A1)(B3)…
- 长公式：**`equation` 套 `aligned` 是不可分页的整体**，13 行的公式会在页底留下 7~8cm 空白。凡是行数 ≥3 的关键长公式，改写成顶层 `align` + 前 n−1 行 `\nonumber`，并在导言区加 `\allowdisplaybreaks[4]`。
- 版面：优先 `[htbp]` + `\usepackage[section]{placeins}`，并把 `\topfraction=0.93`、`\textfraction=0.07`、`\floatpagefraction=0.75`。用 `[H]` 会到处留大空白。
- 中文语体：`\sloppy` + `\emergencystretch=2em`，可消掉绝大多数 Overfull。
- 图内英文注释较多时，在 caption 末尾补一行「图中英文标注：xxx—中文」。

## Step 4 — 编译与验收
```bash
/Library/TeX/texbin/xelatex -interaction=nonstopmode main.tex   # 跑 3 次，交叉引用才收敛
```
验收三项，全过才算完成：
1. `grep -c Overfull` = 0
2. 日志无 `undefined` 引用 / `LaTeX Error`
3. 逐页量页底空白：`(pix.height-72) - last_ink_row`，> 150pt 的页要查明原因（通常是长公式或大图放不下）

## Step 5 — 交付
把最终 PDF 复制到工作区根目录并 `present_files`；`.tex` 源码另存一份便于用户二次编辑。

## 交叉核对（若用户另给参考译本）
用户有时会递来另一份译本让"核对翻译错误"。逐段比对时按这个优先级看：
1. **术语一致性**（rephasing→重聚相、bath→浴、Ohmic→欧姆型…），术语不统一比单个词译错更伤可读性；
2. **是否忠实原文符号**——原文明显笔误的下标/系数也照录，翻译不该偷偷"改正"；
3. **语体**（被动堆叠、"并不实际"这类生硬直译）；
4. 参考译本的好做法（如图内英文加注）可以吸收。

---

# 路线三：版式复刻（「排版要和原文一致」）

**触发语**：「排版要和原文一致」「按原文版式排」「复刻原文版面」「不要统一模板」。
含义是：**每篇译稿要排成与它自己那篇原文的版式一致**，而不是把 N 篇套进同一个模板。
（Pandoc 统排就是「统一模板」，所以被否掉的就是那条路。）

## 铁律：先逆向测量，再动手排

不要凭感觉定参数。用 `scripts/probe.py <原文.pdf> [页码…]` 一次拿全：
页面尺寸 / 栏位与栏宽（行首 x 直方图）/ 正文字号与行距 / 标题层级 / 图区域 / 首页文本块 bbox。

```bash
python probe.py 原文.pdf          # 默认探测前 12 页
python probe.py 原文.pdf 2 3      # 只测第 2、3 页
```

版面结论建议做成一张表存档（页尺寸、栏数、栏位 x、正文 pt/行距、标题 pt），
后续所有参数从表里取，别在一次会话里反复重测。

## 页面尺寸必须用 `bp`

TeX 的 `pt` 与 PDF 的 `bp` 不同（1bp=1/72in，1pt=1/72.27in，**差 0.37%**）。
用 `pt` 排 576×774 的页面会得到 573.85×771.11。**`geometry` 里一律写 `bp`**。

```latex
\usepackage[paperwidth=576bp,paperheight=774bp,left=0bp,right=0bp,top=0bp,bottom=0bp]{geometry}
```

## 单栏论文：不用 flowfram

`geometry` + `\setlength{\parindent}{…bp}` + `float` 宏包的 `[H]` 钉图即可。
图注、节标题字号用 `\fontsize{}{}\selectfont` 显式指定。

## 多栏 / 栏中插图 / 文字绕图：只能用 flowfram

`multicols` 做不到不对称栏位与栏中插图。flowfram 要点（都踩过坑）：

1. **坐标 (x,y) 的 y 自页面【底边】向上量**：
   `y_ff = 页高 − 顶端y − 框高`。搞反会让内容整块上下/左右跑偏。
2. `\newflowframe[页]{宽}{高}{x}{y_ff}[名]`、`\newstaticframe[页]{宽}{高}{x}{y_ff}[名]`、
   `\begin{staticcontents*}{名}…\end{staticcontents*}`。
3. **静态框内容默认垂直居中，且不支持 `[t]`/`[b]`**
   （写 `\begin{staticcontents*}[t]{S}` 会报 `Frame type 'static' does not support option(s): t`）。
   要顶对齐，把内容包进 **`\vbox to <框高>{…\vfil}`** —— 实测内容正好落在框顶。
   宁可把框高设大一点（多出的空间被 `\vfil` 吃掉），也不要设小。
4. **分页控制**（最反直觉的一条）：
   - `\newpage` / `\pagebreak` = 跳到**下一个流动框**，不是下一页；
   - `\clearpage` = 跳到**下一页**（自动补齐当前页剩余的所有框）。
   想「这一节另起一页」必须用 `\clearpage`。用 `\newpage` 会静默无效，很难看出来。
5. 多栏时同一页要按顺序声明所有 flowframe，正文会自动逐框流动；
   文字绕图 = 让「够高的 flowframe」绕开图所占的静态框区域。

## 插图必须「按区域整体渲染」

**不要**只抠内嵌位图。期刊插图的坐标轴、刻度、轴标题、子图编号（`3a.`）往往是
**矢量文字或矢量线稿**，只抠位图会丢内容；`doc.extract_image(xref)` 还有两个坑：
拿到的是原始压缩流、带 `/Decode` 反相标志时整张反色、部分图 bbox 打印为 `1,1,-1,-1`。

正确做法：**把图区域整块渲染**（文本+矢量+位图一起出图）。

```python
clip = fitz.Rect(x0 - 2, y0 - 2, x1 + 2, y1 + 2)      # 外扩 2bp，保住描边框线
pix = page.get_pixmap(clip=clip, dpi=600)
```
用 `scripts/regions.py` 自动找区域（把所有矢量路径 ∪ 位图 bbox 按邻近间隙连通聚类）：
```bash
python regions.py 原文.pdf 3                      # 列出第 3 页的图区域
python regions.py 原文.pdf 3 --render out/ g      # 渲染成 out/g1.png, g2.png…，并输出 y_ff 表
```
- 有的图带**描边外框**（`get_drawings()` 里的 `type=s` 大矩形），要把框也包进 clip。
- 并排的两张子图、四联图，**不要靠 caption 自动归属**（并排图会被同一 caption 抢走、四联图会重复）
  —— 用区域聚类出来的框逐个核验，必要时人工列 (页, rect) 清单。

## 字体

- 拉丁正文/标题：直接用原文的字体族。期刊多是 Times/Helvetica 系 →
  `\setmainfont{Times New Roman}`、`\sffamily` 走 Helvetica。
- 中文正文：`\setCJKmainfont{Songti SC}`；中文无衬线标题：`\setCJKsansfont{PingFang SC}`，
  并显式声明粗体字族：`\newCJKfontfamily\heisb{PingFang SC}[BoldFont=PingFang SC Semibold]`
  （否则 `\textbf` 拿不到 Semibold）。
- 字号一律 `\fontsize{<pt>}{<行距pt>}\selectfont` 显式给，不用 `\large` 之类相对命令。

## 页码/分页必然对不齐 —— 提前想好空白放哪

中译文普遍比英文原文**短 20%~35%**（汉字密度高 + 参考文献不译），
所以「页数一致」通常做不到。不要为了凑页数去改字号行距（那反而不忠实）。
正确的处理顺序：
1. 先把**每页的版面结构**做对（页尺寸、栏位、图表落位、标题层级）——这是用户真正在看的；
2. 再把自然分页跑出来，看空白落在哪；
3. **只做最小干预**：例如「参考文献另起一页」用 `\clearpage`，
   避免节标题成为孤行用 `\newpage`（跳下一栏）；
4. 然后**明确告诉用户**：译文篇幅约为原文的百分之多少，所以末页留白更多。

**不要把机构仓储封面页也复刻进去**：很多下载来的 PDF 第 1 页是
BearWorks / Research Gateway / 各类 Repository 的下载封面（Roboto/Calibri 字体、
含 "BearWorks"、"Citation for published version"、"Download date" 字样）。
它是仓储的门面，不是论文版式 → 跳过，从论文正文第 1 页排，并在交付说明里提一句。
判断方法：`probe.py` 首页字号与字体与后页明显不同、且页面尺寸可能与正文不同。

## 验收：别只靠肉眼

```python
# 1) 页面尺寸逐页与原文一致
import fitz
o, r = fitz.open(orig), fitz.open(rep)
print([(round(p.rect.width), round(p.rect.height)) for p in o][:5])
print([(round(p.rect.width), round(p.rect.height)) for p in r][:5])

# 2) 图文落位：对比图区域框
#    复刻版用 get_image_info(xrefs=True) 拿实际落位，与原文的区域框逐个比 Δx/Δy（目标 ≤3bp）
```
再生成**原文左 / 复刻右 的逐页对照拼图**（Pillow 纵向拼接），这是最快也最有说服力的验收手段。
验收还要卡：`xelatex` 退出码 0、`grep -c 'Missing character'` = 0、日志无 `^!`。

## 并行做法（多篇时）

篇数多时值得并行：先写一份**作业规范 `.md`**（把输入输出路径、工具、
flowfram 坐标约定、bp 规则、区域渲染、中文坑、验收标准全写进去），
然后每个子单元只发「必读规范 + 你负责的篇目 + 该篇已测要点 + 回报格式」。
要点：
- 每篇/每组给**独立子目录**，避免互相覆盖；
- 明确禁止调用 `present_files`、禁止动别人目录；
- 已实测到的参数（页尺寸/栏位/图区域 rect）**直接写进 prompt**，省掉它们重测；
- 要求回报里带「没有解决的问题」，并明说不要谎报完成。

---

# Pandoc 路线：多篇合集 → Markdown + DOCX + PDF

## 何时走这条
- 用户要 **Word**（要批注、要投期刊模板、要给别人改）→ 只能 pandoc。
- 用户要一个**文献包／多篇**一次翻完 → pandoc 合并比手写 LaTeX 省一个数量级。
- 用户只要"能读的中文译稿"，不苛求原图复用 → pandoc 更快。

不适用：必须复用原插图的单篇精排（走上面的手写 XeLaTeX 路线）。

## 取文本
```python
import fitz, glob, os
for p in sorted(glob.glob(os.path.join(src, "*.pdf"))):
    doc = fitz.open(p)
    txt = "".join(f"\n\n===== [PAGE {i+1}] =====\n\n" + pg.get_text("text")
                  for i, pg in enumerate(doc))
    open(os.path.join(out, os.path.basename(p)[:-4] + ".txt"), "w", encoding="utf-8").write(txt)
```
先统计每篇页数与字符数，据此决定是否要跟用户确认翻译颗粒度（全文逐段 vs 核心精译）。
**中译英之外还要留意：包里可能本来就有中文文献**——发现一篇是中文就不要再"翻译"，改成清洗整理后作附录，并在前言里说明。

## ⚠️ pandoc → DOCX 的五个坑（都踩过，务必遵守）

| 写法 | docx 结果 | 正确写法 |
| --- | --- | --- |
| `... \tag{6}` | **编号直接丢失** | `... \qquad(6)`（编号放进公式内） |
| `\begin{aligned} a&=b\\ &=c \end{aligned}` | `&` **字面输出**成 `&` | `\begin{array}{rcl} a&=&b\\ &&=c \end{array}` |
| `\begin{array}{rl} a=&b\\ &c \end{array}` | `&` 字面输出 | **两列 array 不生效，必须 ≥3 列**，改 `{rcl}` 并补成 `&=&` / `&&` |
| `D_1A=0\quad\&\quad D_1B=0` | `\&` 字面输出 | `D_1A=0\ \text{ 且 }\ D_1B=0` |
| `\begin{cases}` 内含 `&` | ✅ 正常 | 保持 |
| `pmatrix` / `bmatrix` / `vmatrix` | ✅ 正常 | 保持 |

补充：**中文字体只在 PDF 路径生效**；docx 由 Word 决定字体，不用管。

## 编排：分页 + 合并
把每篇 `.md` 按顺序拼，篇间插**双写分页**（PDF 认 `\newpage`，DOCX 认 openxml）：
```python
sep = ("\n\n\\newpage\n\n```{=openxml}\n"
       "<w:p><w:r><w:br w:type=\"page\"/></w:r></w:p>\n```\n\n")
open('combined.md','w',encoding='utf-8').write(sep.join(
    open(os.path.join(d,f),encoding='utf-8').read() for f in order))
```

## 构建命令
```bash
# DOCX —— 秒级
pandoc combined.md -o combined.docx --toc --toc-depth=2

# PDF —— 正常 **6~15 秒**（实测：61 页 6s、139 页 11s）
pandoc combined.md -o combined.pdf --pdf-engine=xelatex \
  -V documentclass=ctexart -V classoption=fontset=none \
  -V CJKmainfont="Songti SC" -V CJKsansfont="PingFang SC" -V CJKmonofont="Songti SC" \
  -V mainfont="Times New Roman" \
  -V geometry:margin=2.2cm -V fontsize=11pt --toc --toc-depth=2 \
  --include-in-header=/abs/path/fixsym.tex > pdfbuild.log 2>&1
```

**⚠️ 耗时是故障指示器**：这个体量本该秒级完成。若跑了几分钟还没结束或返回 exit 137，
**不要去调超时／改后台策略，先去查 `pdfbuild.log` 里的字体报错**——`ctexart` 找不到
`STXihei` 时会进入重试循环，表面症状就是"编译极慢 / 被 SIGTERM"。另一条诊断线索：
前一轮踩坑时把 stderr 管进了 `grep`，错误被过滤掉，于是只剩"文件不存在"的假象。

### 字体三连坑（本机实测，务必照抄上面的参数）
1. **`ctexart` 必须显式给 `fontset`，否则报 `The font "STXihei" cannot be found` → `Emergency stop` → 无 PDF 产出。**
   本机已无「华文细黑」。用 `-V classoption=fontset=none`（最可控，配合下面三个 CJK 变量）
   或 `-V classoption=fontset=macnew`。**不要不写**，也不要只靠 `-V documentclass=ctexart` 的 auto 检测。
2. **`-V mainfont` 不能省**：默认 Latin Modern 缺 `π`(U+03C0)、`↔`(U+2194) 等字形。
   症状是**表格里的纯文本 `π/20` 直接变成不可见字符**（文本层抽出 `\uffff`），公式里的 π 反而正常（数学字体另算）——很容易漏检。
   设 `mainfont="Times New Roman"` 后归零。
3. **`-V CJKsansfont` 建议补上**：`fontset=none` 下 ctex 不加载任何中文字体，
   标题走 `\sffamily`，不给 `CJKsansfont` 中文标题可能取不到字形。配 `PingFang SC`。
4. **符号类字符要显式改派给中文字体**（`--include-in-header` 传一个小 `.tex`）：
   xeCJK 按 Unicode 区段划分归属，`①②③`(U+2460-2462)、`★`(U+2605)、`†`(U+2020)、
   `−`(U+2212)、`→`(U+2192)、`↔`(U+2194) 会被判成拉丁字符 → 落到 Times New Roman →
   日志刷 `Missing character`（**字形静默消失，肉眼翻 PDF 很容易漏**）。
   本机实测：这些字形 **Songti SC 全有**，改派即可，不必改文本。
   ```latex
   \xeCJKDeclareCharClass{CJK}{"2460, "2461, "2462, "2605, "2020, "2212, "2192, "2194}
   ```
5. **三个字符本机任何字体都没有，只能在文本层规避**（写译稿时就不要用）：
   `♭`(U+266D)、`♮`(U+266E) —— Songti SC 无；`✅`(U+2705)/`❌`(U+274C)/`⚠`(U+26A0)
   是彩色 emoji，TeX 不可用。
   - `♭` → 写 `$A\flat$`（数学字体有）；`⚠️`/`✅`/`❌` → 直接剥掉，改写成文字（`未取得·付费墙`）。
   - 剥 emoji 后会留下 `|  已译 |` 这种双空格，记得 `re.sub(r'^(\|)  +', r'\1 ', s, flags=re.M)` 收一下。
6. **写译稿时从一开始就用 `\qquad(n)`，不要用 `\tag{n}`**。`\tag` 在 docx 里会整块丢失，
   事后补救要全量正则替换（本轮稿子有 **97 处**要回改）。同理别用 `\begin{aligned}`。

其他：
- `-V lang=zh-CN`（写在 YAML front matter 里也行）能让目录标题显示为「目录」而不是「Contents」。
- 日志里 `Could not load translations for zh-CN` / `The term Table has no translation defined` 是**无害告警**，别去修。
- **诊断套路**：pandoc 出错时不要把 stderr 管进 `grep`（会被过滤掉，只剩「文件不存在」）。
  正确做法是 `> pdfbuild.log 2>&1` 落盘再看；或先 `pandoc ... -o x.tex --standalone`（秒级），
  再 `/Library/TeX/texbin/xelatex -interaction=nonstopmode -halt-on-error x.tex` 直接暴露 LaTeX 层报错。
- 小文件探针（几行中文 + 公式）编译只要几秒，**换字体方案时先在探针上验，别拿 60 页稿去试错**。

## 验收（版式复刻路线）：三处会误判成「复刻缺内容」的坑

复刻版（xeCJK + flowfram，见「路线三」）的验收与 pandoc 路线不同，下列三处极易得出**假结论**：

1. **图注正则必须同时匹配中英文。** 只写 `^(Fig|Figure)` 会把复刻版的「图1」「表I」全部漏掉，
   输出「复刻图 0 条」，看起来像整篇没排图。正确写法：
   ```python
   re.match(r"(?i)^(fig(ure)?\.?\s*\d|图\s*\d)", t)                          # 图注
   re.match(r"(?i)^(table\s*[IVX\d]|表\s*[IVX一二三四五六七八九十\d])", t)     # 表注
   ```
2. **原文的 image 数量会虚高，不能直接当「应复刻图数」。** 两个来源：
   - 同一位置常**叠加 2 张位图**（透明层/蒙版），`get_images()` 会数两遍；
   - 页面**横线**（页眉分隔线，常见 372×0.5bp）、公式块、整页背景图也会算成 image。
   正确口径：用 `page.get_image_bbox()` 过滤 **宽 ≥60bp 且高 ≥60bp 且宽 <900bp** 才是真实插图。
   同理，原文若为**全矢量图**（Springer / arXiv 的部分文章），位图数会是 0——复刻把矢量区域渲染成位图，
   于是出现「原文 0 张 / 复刻 6 张」的假差异，**这不是多图**。
3. **判定「是否漏内容」看编号体系，不看页数。** 中文译文篇幅约为英文的 2/3，页数天然对不上
   （实测差 −3 ~ +2 页）。逐篇提取「图 1…N / 表 1…N / 章节标题」清单与原文比对，
   数量与顺序一致即内容完整。**不要为了凑页数去拉伸行距**——那反而破坏版式忠实度。

`page.get_text("dict")` 的**文本块数量级**同理要留意：复刻版（210 块）会明显少于原文（321 块），
这是中文单块容纳更多行所致，**不是缺段**。

## 并行分派教训（大篇目必读）

- **一个 agent 最多扛 1 篇大论文。** 实测让一个 agent 管 2 篇（其中一篇 20+ 页）会做到一半报废，
  且**报废时已做出的 PDF 不会自动归档**，需人工回收。
- 指令里必须强制**「先求完整、再求精确」三阶段**，并明确禁止越阶：
  ①**骨架完整**（全文 + 公式 + 参考文献排入，图先占位，立刻得到能翻到最后一页的 PDF）
  → ②**补插图** → ③**逐页校准**。要在 prompt 里写明「阶段 1 完成前绝对不要陷入单张图的像素级对齐」。
  实测：加了三阶段约束后，5 篇大论文全部产出可用初版。
- **判定 teammate 是否还活着**：文件 20 分钟无更新 **且** `SendMessage` 返回 `Not in a team` = 已终止。
  **不要**凭任务状态 `paused` 或 `lifecycle=alive` 就认为它仍在运行（那只是持久化元数据）。
- 回收半成品时优先查 `Too many }'s` 这类**非致命错误**：xelatex 在 `-interaction=nonstopmode` 下
  会继续跑完并产出 PDF，错误只留在 `.log`。本轮 10 号有 6 处 `\exer{...}\ …。］}` 段末多了一个 `}`，
  靠 `grep -c '^!' *.log` 才暴露。

## 验收：不要靠看图，靠文本层
本会话模型可能读不了图，直接用代码校验，比目视更可靠：
```python
# PDF：查原始 LaTeX 泄漏
import fitz, re
full = "\n".join(p.get_text() for p in fitz.open('combined.pdf'))
for pat in [r'\\begin', r'\\end', r'\\frac', r'\\tag', r'\\qquad', r'\\left', r'\$']:
    print(pat, len(re.findall(pat, full)))     # 全 0 才算过

# DOCX：解 document.xml，查公式内残留 & 与反斜杠
import zipfile, re
x = zipfile.ZipFile('combined.docx').read('word/document.xml').decode('utf-8')
maths = re.findall(r'<m:oMath>.*?</m:oMath>', x, re.S)
bad = [t for m in maths
       if (t := ''.join(re.findall(r'<m:t[^>]*>([^<]*)</m:t>', m)))
       and ('&amp;' in t or '\\' in t or 'begin' in t)]
print('公式数', len(maths), '异常', len(bad), bad[:3])
print('分页数', x.count('w:type="page"'))     # 应等于 篇数-1
```
注意 `&lt;` / `&gt;`（`<` `>` 的 XML 转义）是**误报**，只认 `&amp;`。
DOCX 的目录是 Word 域，需用户在 Word 里按 F9 更新才显示页码——交付时要提一句。

**验收第 3 项：缺字形清零。**
```bash
grep -c 'Missing character' pdfbuild.log        # 必须为 0
grep -o 'Missing character: There is no . (U+[0-9A-F]*)' pdfbuild.log | sort -u   # 有输出就逐个处理
```
只有 `Missing character` 数 = 0 且 `\x00`/`\uffff` 在文本层为 0，才算排版干净。

**验收第 4 项：各篇独立起页。** 用字号定位一级标题（pandoc → `\section` 为 14.4pt）：
```python
import fitz
d = fitz.open('combined.pdf')
for i, p in enumerate(d):
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                if s['size'] > 13.4 and len(s['text'].strip()) > 3:
                    print(i+1, s['size'], s['text'][:50])
```
页码应当是严格递增且**互不相同**的一串。
注意别用"关键词出现在页首 60 字"来判页——**页眉会把每页都命中**，得到一堆噪声。

## 交付
- 先写一份 `00_前言与阅读路线.md` 放在合集最前：**本篇包含什么（表）+ 建议阅读路线 + 术语对照表 + 翻译原则与已知局限 + 题录速查表**。用户拿到一堆译稿时，这份前言的价值高于任何单篇。
- 每篇译稿独立 `.md`（便于检索/二次加工）＋ 一个 `combined.{docx,pdf}` 合集。
- 原 PDF 文本层损坏（尤其中文老刊）时，公式要**按物理上下文重排**并加「译者注」；明显笔误（下标写错、`g/L_x` 应为 `g/L_y`、`0.1 F` 应为 `0.1 μF`）也照录＋注明，**不要静默修改**。
- 参考文献列表保留原文语种不译，便于检索。
- 交付文件名带日期，如 `XXX_中文译稿_20260928.pdf`。
- **分篇 Markdown 打包必须用 Python `zipfile`，不要用 `zip` 命令**：`zip` 不写 UTF-8 文件名字段，
  中文名在访达/Windows 解压后全是乱码（`00_�??�?�?…`）。`zipfile.write()` 会自动置 UTF-8 标志位。
- 上一轮已交付过的篇目会产生**旧版重叠**：本轮请用更明确的新文件名（如加"全卷9篇"），
  并把旧产物移进 `旧版_第一批N篇/` 子目录，避免用户拿到两份不知哪份最新。
- 若有上一轮已译、本轮未重译的篇目，按**用户清单的编号**统一重命名进合集
  （`02_…`、`07_…`），并回头改各篇 `# 标题` 里的旧编号——否则前言目录与正文编号会打架。
