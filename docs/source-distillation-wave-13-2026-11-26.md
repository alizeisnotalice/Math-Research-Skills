# 文献依赖复核与技能入口整理

本轮逐项复核余下的 16 份文献。5 份提供了本地方法，1 份已确认期刊出版信息及本机预印本版本，10 份仍有具体证明依赖或版本待查。逐篇索引保留原件 SHA-256、物理页和当前采用范围。 [逐篇来源检索](../skills/math-research/references/literature-source-lookup.md)

## 数学复核

- 对两类 Mycielski 张量积逐项核对前缀计数、折叠图、相邻窗口边及奇长度闭合。穷举 \(2^9+2^{11}\) 个定向得到 56 条不同的状态约束，可用同一个二着色。代表性回放覆盖 \(k=3\) 及循环接缝。临界图技能另外接入后继色路径，精确输出双向路径或给定图的实际重新着色。 [奇窗口证明与回放](../skills/math-finite-graph-family-witnesses/references/odd-fold-window-certificate.md) · [后继色路径证书](../skills/math-finite-graph-family-witnesses/references/successor-colour-paths.md)
- 核对临界图计数链中的 Choi–Sieniawski v1 Lemmas 5–6、Kim–Picollelli 期刊版 Theorem 2.4 及 Gao–Huo–Liu–Ma 期刊版 Theorem 3.1。已采用的重新着色是原稿的局部构件，临界图全局取等分类仍需完成余下各情形证明。 [计数预印本](https://arxiv.org/abs/2611.13580v1) · [临界图期刊构造](https://doi.org/10.37236/12623) · [指定端点路径期刊版](https://doi.org/10.1093/imrn/rnaa324)
- 在恢复的作者 `master` 代码版本上，以 Arb 384 位定向区间重建连续幂和稿件的指数上界，物理 Table 2 的 24 行全部一致。尚需单独核验 Sage 模方法和 Pari/GP Thue 阶段。 [连续幂和区间证书](../skills/math-l03-rational-and-interval-certificates/references/ext-0436-section7.md)
- 精确回放 v21 的 207 条二次行与 229 变量四次式。3,312 个单项式全部匹配，并拒绝了 10 处人为改动。带并自由积的构件另行核对了条件正规形。 [四次式编译](../skills/math-l19-coordinate-ring-certificates/references/v21-quartic-compilation-ledger.md) · [带并自由积](../skills/math-free-group-presentation-traces/references/amalgam-word-source.md)
- 核对 Kumar–Sena 的本机预印本及期刊题录。ETH 的 Hexagon PDF 与固定公开源码 PDF 在去除指定戳记并规整空白后，MATLAB R2026b 提取的 145,793 个字符完全相同。VP 摘取文本仍有差异，确切版本绑定待查。 [Kumar–Sena 期刊版](https://doi.org/10.1515/forum-2024-0441) · [同期文献索引](../skills/math-research/references/recent-non-openai-sources.md)
- 恢复并回放 Sra v1 的四项有限 \(PF_{10}\) 检查，输出与作者清单完全一致。v3 所需的 270 个选定零点、区间与 683 段覆盖数据仍待取得。 [Xi 有限回放](../skills/math-xi-theta-finite-certificates/references/sra-riem-xi-v1-pf10-replay.md)

## 安装入口

重写 20 个概率技能的主要入口，再修复生成函数边界与有序增量条件 Bernstein 两项的失效定位。 在空目录安装全部 286 项技能后，入口中失效的行内资源定位从 95 处降为零。用选择条件和现行方法链接代替入口层的长篇历史材料。发布验证同时检查入口中以行内代码指向的资源是否列入安装清单。旧阅读卡按各自证据范围使用。 [维护与安装](maintenance.md)

Aaronson–Ambainis 的固定版本源码审计与声明检查通过。增量 Lean 构建在 1,500 秒时限内新增完成 42 个模块。主证明、公理结果和内核回放仍待完成。 [来源状态](../skills/math-research/references/recent-non-openai-sources.md)
