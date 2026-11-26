# 近期、历史与补充文献复核及技能整合

本轮在 22 个独立批次复核 196 份本机原件。逐份复算 SHA-256、核对物理页数及所取的数学陈述。46 份提取可调用构件，1 份确认有既有方法，24 份保留为引用，5 份归入邻近材料，3 份排除现有版本所提路线。其余 72 份候选和 45 份待核来源保留了各自的必要条件。全库仍登记 5,389 份不同 SHA-256。候选或待核由 332 份降到 253 份。

| 来源 | 本轮复核 | 提取构件 | 复核后全分册待核 |
| --- | ---: | ---: | ---: |
| 欧拉常数专题 | 4 | 2 | 0 |
| 历史分册 | 33 | 6 | 25 |
| 近期原稿 | 74 | 19 | 52 |
| 补充分册 | 85 | 19 | 176 |

## 实际复算和边界

- **欧拉常数。** 取得 Brent–McMillan 1980 年正式刊载全文及作者勘误。从 B1 的单侧 Bessel 余项、正项级数尾与有理对数界得出严格区间。系统 Python 对 \(n=3,N=24\) 给出端点严格落在 \(0.577214\) 与 \(0.577235\) 内。Fresán–Jossen 的指数动机入口保留指数周期猜想作为算术推论的前提。欧拉常数无理性仍未解决。[B1 的严格区间](../skills/math-euler-constant-irrationality/references/brent-mcmillan-b1-1980.md) · [刊载及勘误](https://maths-people.anu.edu.au/~brent/pub/pub049.html) · [指数动机](../skills/math-euler-constant-irrationality/references/exponential-motive-conditional-gate-fresan-jossen.md)
- **奇调和级数表达式。** 对稿件末页给出的表达式，以 10 项有理 atanh 展开控制 \(\log 2\)，对正项级数保留到 \(20\) 并用 \(1/720000\) 控制余项。该表达式在 \((0.58197,0.58198)\)。独立的 100 项 Gregory 有理区间给出 \(\gamma\in(0.576,0.579)\)。两个区间分离。[专题来源](../skills/math-euler-constant-irrationality/references/source-scope-gamma.md)
- **随机约束的盒质量。** 保留分布在截断区域外的质量上界。均匀分布 \([0,1]\) 截断至 \([0,1/2]\) 的算例中，省略该项给出 \(1/2\) 的错误上界。补回后，上界为 \(1\)。覆盖证明、质量和尾界由调用方提供。[盒质量证书](../skills/math-l03-rational-and-interval-certificates/references/stochastic-box-mass-enclosure.md)
- **有限代数与级数。** RM(7,14) 给定 ANF 的容斥与完整真值表均给出权重 354。周期 \(L(1,f)\) 工具在 \(q=3\) 与 \(q=4\) 的样例分别返回零判据不成立和成立。Milne 的 \(r_{16}\) 卷积和 theta 展开在前 24 个正次数整数系数上一致。Macdonald 加权永久式检查每个 \(1-q^j\)，并拒绝 \(q=-1\) 的二阶除零样例。[ANF](../skills/probability-boolean-fourier-invariance/references/rm714-source.md) · [周期 \(L(1,f)\)](../skills/math-dirichlet-l-derivative-sine-reduction/references/periodic-l1-exact-criterion-ext0421.md) · [Milne 卷积](../skills/math-hankel-pade-certificates/references/milne-r16-divisor-convolution.md) · [加权永久式](../skills/math-cycle-weighted-permanent/SKILL.md)

## 技能入口

新增 12 个独立入口。其中 Ax–Schanuel 将平坦主丛、模 \(j\)、纯 VHS、混合 VHS 和矩阵指数集中分流，并分别记录各定理的维数缺陷、特殊子簇和闭包前提。将 Mahler 一阶右因子接入 Hankel–Padé、将 ANF 权重接入布尔函数专题。鞅入口集中处理预极限的过滤、括号与可积性，弱极限识别集中在测度收敛入口。固定链的混合与参数化谱扰动各有明确入口。欧拉常数主入口补上 Prévost–Hurwitz 和 Casoratian，并使部分安装自动带入这些运行依赖。[Ax–Schanuel](../skills/math-ax-schanuel-dimension-defect/SKILL.md) · [分类目录](../catalog/README.md) · [概率入口](../skills/math-research/references/probability.md)

本机源文件保持原位。提交到仓库的技能包收录来源定位、限定陈述、代码和最小输入，审查批次及安装证据分别保存在本机。
