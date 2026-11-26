# 跨批次查找论文及使用记录

从本机已安装的文献索引按 SHA-256、题名、主题词或技能入口反查。脚本搜索 OpenAI、Google Cogentic、近期其他原稿、补充文献、历史分批索引、既有技能引用复核与欧拉常数专题。相同 SHA-256 的不同来源卡列在同一条结果下，各自保留版本及数学适用范围。

~~~sh
python3 scripts/find_literature_source.py --sha 2b8298fa7
python3 scripts/find_literature_source.py --text 'Hankel determinants' --limit 10
python3 scripts/find_literature_source.py --skill math-b03-generalized-moments --collection historical
~~~

结果返回索引文件的绝对路径和行号。先读对应条目，再据其中的物理页码、版本和外部依赖调用方法。`--text` 会检查标题及来源说明。多次指定 `--collection` 会合并指定的集合。找不到结果时，若已知原件则进一步定位纸面来源或查尚未登记的本机队列。

用状态筛选当前可调用方法或待整理的来源。没有状态标注的条目仍可按题名、SHA 或技能检索。

~~~sh
python3 scripts/find_literature_source.py --collection openai --status installed
python3 scripts/find_literature_source.py --collection openai --status held --summary
python3 scripts/find_literature_source.py --collection historical --status candidate --skill math-b03-generalized-moments
python3 scripts/find_literature_source.py --collection supplemental --status adopted
python3 scripts/find_literature_source.py --summary
~~~

- OpenAI 状态取自逐篇索引的分类页。值 `candidate` 表示已有构件候选，`held` 表示还有方法待定位，`installed` 表示已登记当前技能构件。
- 历史分册有新依赖记录时，筛选使用新记录的处置。匹配项仍给出相符旧卡的位置。补充分册采用已明确登记的构件、候选或待查标记。
- `adopted` 匹配明确登记的采用记录。源卡的范围和假设仍由对应方法说明给出。
- `--summary` 按原件 SHA 在各分册内去重，汇总所有匹配项。`unclassified` 表示该分册没有脚本可读的状态标注。总数跨分册去重，因此同一原件出现在多本索引时，分册小计可以大于总数。

旧证据包缺少 PDF 时，可用其索引中的完整 SHA-256 加上参数 --archive-root /Volumes/共享/Math_Research_Literature。返回的 verified_archive_pdf 是实算哈希匹配的一个现有文件。未找到时该字段为空。SHA 核对不认证缺失的原审核表、案例或证明。
