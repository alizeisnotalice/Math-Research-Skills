# 余下文献的依赖复核与 Google 修订蒸馏

Google 本机目录的六份 PDF 共 274 个物理页。本轮复算 SHA-256，并与 Google Research 固定目录逐篇比对。五份现行稿与本机一致，双矩阵稿的引文修订已有版本记录。相同目录在 11 月 26 日北京时间 07:54 更新了另一篇组合拍卖论文。该 36 页修订版登记为独立来源，采用物理页 6–7 的静态价格 LP 证书。[Google 来源和四项精确回放](../skills/math-research/references/google-cogentic-2026-11-25.md)。[Google Research 固定目录](https://github.com/google-research/google-research/tree/3f540f420bfae7e6ce48365a68d0ae003feb2f87/cogentic_research_papers)

其余 33 份本机文献全部核对 PDF 哈希、页数和实际采用范围。17 份接入有限构件，9 份列为候选，7 份因关键证明环节或原件缺失保留。当前逐篇索引可检索 5,390 个 SHA-256 身份。共享归档 5,410 个 PDF 路径均与已登记的本机清单逐字节一致，去重后为 5,389 份。一份内部写作资料单独登记。索引多出的两份是 Google 的双矩阵和组合拍卖官方修订。[逐篇检索](../skills/math-research/references/literature-source-lookup.md)

## 技能及数学验收

- [有限递推核验](../skills/math-recurrence-finite-screening/SKILL.md)统一三个有限任务。按源稿枚举 \(2\le k\le248,\ 2\le m<n\le358\) 的 15,695,862 对 \(k\)-Pell 指标，使用精确整数完全幂检测，得到零个相依对。同一入口检查有限 \(k\)-Lucas 拼接和单位常数项递推的双向传播。另在 [LRS 模见证](../skills/math-l17-filtered-linear-algebra-certificates/references/modular-lrs-nonzero-witness-skolem.md) 枚举给定模的最终周期。三个来源采用的是此有限判定。
- [有限图族见证](../skills/math-finite-graph-family-witnesses/SKILL.md)重建两个 HKO 原稿小图和装饰树有理符号比较。[自由群表示轨迹](../skills/math-free-group-presentation-traces/SKILL.md)精确约化给定的 Andrews–Curtis 轨迹并回放逆轨迹，核验目标的有序性。
- [正有理数的乘法独立](../skills/math-rational-logarithm-independence-gate/SKILL.md)用素赋值矩阵的有理秩认证两份 Chudnovsky 原稿共用的输入条件。对 \(2,3,5/7\) 得到秩 3，对 \(2,8\) 得到秩 1。另用精确有理数复算 [\(e^{1/n}\) 的 Hermite–Padé 形式核](../skills/math-integer-linear-form-rates/references/ext-0333-e-root-kernel.md)的低阶余项消失，示例的系数分母最小公倍数为 8。
- 扩展现有算子和随机矩阵技能。Hua–Bellman 六矩阵例的最小特征值与核矩阵行列式均由 Arb 256 位有向包围，两个区间都严格落在零以下。WYD \(p=2/3\) 的边界替换给出精确虚部 \(-11/182\)。Clifford 三生成元的张量例以整数矩阵逐项验证反交换和平方恒等式。[Hua–Bellman 区间](../skills/math-operator-algebra-certificates/references/hua-counterexample-source.md)。[WYD 边界](../skills/math-operator-algebra-certificates/references/wyd-boundary-obstruction-source.md)。[Clifford 实例](../skills/probability-random-matrix-tensor/references/clifford-series-source.md)
- 外部代码回放区分有限重建与全局结论。关于整数在有理数中丢番图可定义性的稿件提供了带四个有限算术套件的构造脚本。该脚本通过 25 个原文件哈希、精确重建及有限检查，原脚本标记全局算术定理尚未证明。Pandigital 的五位 Motor-X 冒烟检查处理 158,855 类和 828 个值，失败次数为 0。[有限回放范围](../skills/math-l03-rational-and-interval-certificates/references/ext-0372-pandigital-replay.md)

## 仍需复核的依赖

16 份记录保留了下一步依赖。包括 \(\Xi\) 预印本的完整区间载荷、与特定 PDF 逐字节绑定的 Lean 工程、轨道或高度估计中的全量论证、以及部分公开代码的可访问版本。Aaronson–Ambainis 原件已匹配公开固定源码，固定 Mathlib 缓存取齐后，本机 Lean 4.33.0 单独检查声明文件 `AaronsonAmbainis/Conjecture.lean` 成功。完整构建在 260 秒限时前完成四个模块。主证明、公理输出和内核回放仍待完成。[同期来源索引](../skills/math-research/references/recent-non-openai-sources.md)

当前 OpenAI 原稿依既定口径按原文陈述与假设直接蒸馏。新构件仅承担各自登记的有限命题及调用条件。
