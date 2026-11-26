# 跨批次查找论文及使用记录

从本机已安装的文献索引按 SHA-256、题名、主题词或技能入口反查。脚本搜索 OpenAI、Google Cogentic、近期其他原稿、补充文献、历史分批索引、既有技能引用复核与欧拉常数专题。相同 SHA-256 的不同来源卡列在同一条结果下，各自保留版本及数学适用范围。

~~~sh
python3 scripts/find_literature_source.py --sha 2b8298fa7
python3 scripts/find_literature_source.py --text 'Hankel determinants' --limit 10
python3 scripts/find_literature_source.py --skill math-b03-generalized-moments --collection historical
~~~

结果返回索引文件的绝对路径和行号。先读对应条目，再据其中的物理页码、版本和外部依赖调用方法。`--text` 会检查标题及来源说明。多次指定 `--collection` 会合并指定的集合。找不到结果时，若已知原件则进一步定位纸面来源或查尚未登记的本机队列。

如需复核历史来源，加入状态筛选，例如：

~~~sh
python3 scripts/find_literature_source.py --status hold
python3 scripts/find_literature_source.py --status candidate --skill math-b03-generalized-moments
python3 scripts/find_literature_source.py --status adopted
~~~

状态字段反映历史来源卡上明示的分类。已采用构件另有 adoption_recorded 标记，可与同篇原件中仍待审的其他命题同时存在。其他来源分册各有自身的证据字段，直接查对应页。

存在逐项依赖复核记录时，检索结果把这条记录排在前面。状态筛选使用它的当前处置，较早的卡仍可用来追溯。已采用筛选根据明确登记的构件记录定位，适用条件以所链接的技能正文为准。[依赖复核索引](historical-sources/dependency-recheck/README.md)

旧证据包缺少 PDF 时，可用其索引中的完整 SHA-256 加上参数 --archive-root /Volumes/共享/Math_Research_Literature。返回的 verified_archive_pdf 是实算哈希匹配的一个现有文件。未找到时该字段为空。SHA 核对不认证缺失的原审核表、案例或证明。
