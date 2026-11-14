# 来源、取舍与覆盖范围

编写及 PDF 优先修订日期：2026-10-27。用户明确要求“以我给你的 PDF 为准”。因此 PDF 是本技能的写作标准；GitHub 项目和 T 项目材料只作兼容的辅助。技能为重新编写的数学论文工作流，未安装或复制整个外部技能包，未执行外部安装脚本。

## 用户提供的写作规范

原件：`/Users/zhengzhihao/Downloads/数学论文写作规范_动机结构与自然表达.pdf`。
技能随附副本：[user-writing-guidelines.pdf](local-assets.md#asset-e4e986445439)。六页均实际提取读取；第 3 页另渲染核对公式。文中旧稿数值、作者判断及参考文献未在本次逐项重新认证。

|来源页|吸收内容|技能位置|
|---|---|---|
|1–2|导师的四部分结构、引言顺序、标准/原创引理、编号、应用、材料归位|入口及 structure-and-motivation.md|
|3|先说明构造需求，再引入工具及其用途；RS 示例的均值提醒|structure-and-motivation.md|
|4–5|具体主张替换空泛评价、合并重复防御、内部审核移出正文|natural-expression.md|
|6|背景取舍、工具来源、贡献比较、证明目标与交稿检查|结构与证明参考|

规范明确区分导师要求和编辑建议，技能保留这一区别。四部分结构、引言内容顺序、前人/本文成果的编号区分是须落实的要求；不因 GitHub 模板、旧稿或一般期刊习惯自动放宽。用户后续明确改用别的规范时再调整。原件引述的 Melas、Bourgain、Ledoux、Rudin、Tao 只保留为回查线索；本次没有重读这些原始论文，不能声称其逐条文献核验已完成。

## 实际读取的 GitHub 项目

### zLanqing/codex-claude-academic-skills

- [仓库](https://github.com/zLanqing/codex-claude-academic-skills)
- [research-writing-skill/SKILL.md](https://github.com/zLanqing/codex-claude-academic-skills/blob/main/research-writing-skill/SKILL.md)
- 实际读取仓库说明与上述技能文件全文（60 行）。
- 吸收：先组织论证；区分来源与推断；保持术语、公式和引用一致；按需加载参考文件。
- 数学适配：把实验章节导向改为定理、引理、证明及应用；以当前请求/稿件决定语言；不以数据指标替代纯数学证明。

### SNL-UCSB/paper-writing-skill

- [仓库](https://github.com/SNL-UCSB/paper-writing-skill)
- [语义检查](https://github.com/SNL-UCSB/paper-writing-skill/blob/main/author_profile/gate_semantic.md)
- [表达参考](https://github.com/SNL-UCSB/paper-writing-skill/blob/main/author_profile/craft_reference.md)
- 实际读取仓库说明及上述两个参考文件全文（分别 175、171 行）。
- 吸收：段落功能、定义的引入、跨章节一致性、主张和依据对应、先结构后文字。
- 未继承固定访谈题数、实验论文写作顺序、零被动语态、固定压缩比例、禁止所有重复或要求无限迭代至审核“零问题”等规则。数学论文的限定条件和证明细节不能因这些机制被删去。

这里只概括少量组织方法，核心数学流程、项目主题索引和示例由本次独立编写。没有复制其脚本或成套模板。若未来实际复制外部代码或大段文本，应另核原文件许可并保留要求的版权声明；本机私人研究材料不因此获得对外发布授权。

## T 项目的实际处理范围

项目根目录：`/Users/zhengzhihao/Desktop/T`。

1. 遍历非 `.git`、`node_modules`、虚拟环境与缓存目录的文件，登记选定扩展名，得到 **643,683 个候选文件条目**。这是文件枚举，不能称全部语义阅读。
2. 对除钓鱼资料与模板合集外的 `.md`、`.tex`、`.bib` 候选文本实际读取字节、计算 SHA-256、提取标题与预览，共 **76,174 份文本，按字节去重后 16,074 份**；读取错误为 0。它包含原文转换、研究和审核记录及部分非数学材料，不能把该数直接称为数学论文数量或全文深读数量。
3. 根据主题和来源用途，读取下列代表性的写作、证明、结果范围与修订材料，并整理 64 项工具索引。大型稿件只读取列明章节或开头片段；所有本地材料的实际定位见交付包的来源清单。
4. PDF/Word、海量 JSON、脚本、实验输出主要在文件清单层登记，未逐件语义审查；未展开现有压缩档案，未重跑各研究项目，未重新认证任何 Cn 或全局最优主张。

## 直接使用的本地材料

下列路径相对 T 项目；引用是写作经验的来源，不是对每份稿件主定理的背书。

|材料|本次实际范围与用途|
|---|---|
|`数学工具64项蒸馏/01_64项工具索引.md`|全文；64 类工具及迁移边界|
|同目录 `02_工具依赖图.md`、`05_证据状态与使用规则.md`|全文；方法关系与证明依赖、阅读与核验状态分开|
|`research_library/math_skill_sources_20261007/CONFLICTS.md`|全文；系数位置勘误与原文回查|
|`output/hl_cube_paper_20261013/frontmatter.tex`、`README.md`|全文；引言、方法动机、全部整数维数、论文与数值分工|
|`Math-Research-finite-paper-n3/cube-finite-dim-bounds/papers/n3/main.tex`|第 1–380 行；对象、障碍、有限源、全尺度及连续判据，未重算证书|
|`Math-Research-cube-dim-5/cube-dim-5-bounds/paper/main.tex`|第 1–160 行；定理、下界几何与严格平滑余量|
|同目录 `paper/README.md` 与 `full_audit177/{exposition_final_review,manuscript_final_review}/report.md`|全文；准确值/展示值、导数与范数范围、非负上包及编译/核验分工|
|`Math-Research-cube-dim-6/cube-dim-6-bounds/README.md`、对应七维 `README.md`|全文；模型改进与原问题界的区别、同一目录内多阶段状态|
|`Math-Research-euclidean-20261011/euclidean-ball-maximal/README.md`|在批量输出中阅读已返回的章节；团簇、来源与全局拼接，未逐轮阅读证明|
|`output/tex/` 中四课题的 20260919 简版 `.tex`|实际读取源码，批量输出有截断；读取到的模型、量词、包络与真实高阶、权和应用边界用于归纳|
|`SJ_数值可行性验证_20260930/数值验证报告.md` 与 `反例攻关/00_复核入口.md`|全文；数值诊断与连续误差、网格量词、充分条件与原目标|
|`output/merit_factor_research/{README.md,global_bounds/README.md}`|各开头 5,000 字符，连同标题索引；构造、松弛与全局最优|
|同目录 `astra_moment_extrema_audit_20260926.md`|前 100 行；固定阶矩与增长阶数、典型概率与极值|
|`output/centered_cube_20261016_guidance_extracted.txt`|读取提取文本，输出有截断且公式损失；仅用于费用分工/局部全局的概念，未将缺失公式写入技能|
|`量子计算译文二次校订版/二次校订说明.md`|全文；限定词、数学公式与源文冲突，不代表读完二十篇论文|

## 如何继续维护

修改默认写法时区分用户明确要求、特定稿件要求和一般编辑建议。新项目主要更新主题索引和具体证据，不把暂时的研究结论或内部审核状态写进技能核心。引用原论文和具体数值时，仍回到该稿件的当前真实来源重新核对。
