# 历史文献主题复核与数学工具验收

已将 452 份此前未进入本轮来源索引的原件按数学主题登记。每条记录附原件 SHA-256、实际查阅的 PDF 物理页和适用范围。扫描及无法常规提取的 21 份用本机文字识别逐份定位，另复查 7 份文字层损坏的文件并修正题录。选择当前技能时以卡片记录的判断为准。 [历史文献入口](../skills/math-research/references/historical-sources/README.md)

规范共享文献库有 5,410 个 PDF 路径、5,389 份去重原件。六个历史技能来源目录的 4,219 个 PDF 路径只产生 2,547 个原件哈希，全部已经纳入共享库。加入本批后，尚有 2992 份未被专门来源索引或本轮复核登记。此计数用于逐篇推进。已登记记录里仍有证明依赖待核的候选和证据不足的条目。

## 欧拉常数及相关常数

Ferguson 的投影比值 \(P_n/Q_n\) 已接入 Hankel–Padé 技能和欧拉常数总入口。核对了原稿 Theorem 1、Lemma 2、三个矩表示和所用证明，修正了原稿 γ 推前密度的 Jacobian 对数。Python 3.13.18、SymPy 1.14.0 复算 γ 的前 16 个非恒定矩，精确检查 \(n=0,\dots,8\) 的三个来源例（\(\zeta(k)\) 取 \(k=2,3,4,5\)）和一个均匀测度算例。7 个 γ 的整块行列式另用 Berkowitz 算法对照，9 个 γ 比值均严格小于Brent–McMillan 有理区间的下端。本次检查给出有理下界，γ 的无理性沿这条路线还需全局整数线性形式与衰减证明。 [Hankel 正矩投影](../skills/math-hankel-pade-certificates/references/hankel-projection-bounds.md)

## 既有技能的范围复核

- 半无限交换补入 Basu–Martin–Ryan 的 Theorem 2.4 和 Example 3.5。给定可数指标，采用全实序列或收敛序列作为约束空间时，允许的正对偶泛函可以不同。SymPy 验证全域余量平方恒等式，另外以有理算术回放 \(1\le i,M\le64\) 的 4,096 个输入。 [有限支撑对偶的边界](../skills/math-b02-semi-infinite-exchange/references/gale-truncation-boundary.md)
- 已发表文献按实际版本和所引结果记录。扫描本中的 O’Neil–Weiss 刊物和 Barbour–Hall 作者均回核正式出版记录。 [历史分析文献](../skills/math-research/references/historical-sources/analysis.md) · [历史概率文献](../skills/math-research/references/historical-sources/probability.md)

## 新增的可调用构件

- Bayraktar–Cox–Stoev 的有限原子权重框架接入 Snell 技能。核验整树的后验重心，并逐坐标比较停时后验和初始后验的期望。校验对 100 组奖励表枚举了 400 条策略，样例收益和树内最优值同为 \(5/4\)，另外核对 2,048 节点链和四个无效输入。 [有限后验树](../skills/math-e04-snell-envelope-optimal-stopping/references/finite-atomic-posterior-tree.md)
- Onn 的 Graver 增广接入数学规划技能。验收在 240 个二次目标及整数值表实例上与小盒独立穷举一致。对 \(10^{81}\) 宽度的凸线搜索，精确定位 \(10^{80}+3\) 的最优步长。缺少方向的正反对照保留为条件性检查。 [Graver 增广](../skills/math-l04-mathematical-programming-workflow/references/graver-augmentation.md)
