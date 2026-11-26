# 依赖复核、专项分类及可运行证书

本轮对剩余 66 份来源逐篇重算 SHA-256、核对物理页和实际调用条件。31 份形成限域构件，1 份由既有接口覆盖，1 份归入限定引用。仍有 17 份候选和 16 份待取得必要证据。现行待核共 33 份，逐篇记录可用结论和仍需查证的部分。[来源检索](../skills/math-research/references/literature-source-lookup.md)

| 分册 | 本轮复核 | 新采用构件 | 当前待核 |
| --- | ---: | ---: | ---: |
| 历史 | 7 | 7 | 0 |
| 近期 | 28 | 11 | 17 |
| 补充 | 31 | 13 | 16 |

## 实际复算

- **平面中心平方极大算子。** 固定公开版本的两套整数程序得到相同的周期矩形并集有理比值，约为 \(1.7027237335962937\)。两套 Arb 程序均通过比较核 C1–C4，分别在 219732 个子格及 443754 个叶格核对 \(AK\) 的非负性。结合 Lin 的比较和源文的周期平滑传递，复现 \(1.7027237335\le c_2\le3.59123\)。范围为平面、轴平行、中心平方。[下界及传递](../skills/math-centered-cube-endpoint-budget/references/tomar-square-periodic-lower.md) · [上界证书](../skills/math-centered-cube-endpoint-budget/references/tomar-square-kernel-upper.md)
- **特殊函数。** 用 Python 3.12.13 和 python-flint 0.9.0 复跑固定版本的 \(\Xi\) 矩证书，五组区间矩比较通过。对 \(\zeta(2)\) 的源附录实际复算参数球、区间不等式与尾界，保留已定位的超几何、渐近和有限计算到全局结论的证明依赖。[Xi 有限证书](../skills/math-xi-theta-finite-certificates/SKILL.md) · [\(\zeta(2)\) 参数核验](../skills/math-integer-linear-form-rates/references/ext0316-zeta2-2026-parameter-certificate.md)
- **鞅讲义恢复。** 通过 Mörters 的讲义目录和实际 PDF 物理页 17、19 核对一致可积离散鞅的终端条件期望表示及 Lévy 向上定理，保留可积、递增滤过及极限可测性输入。[鞅与停时](../skills/probability-martingale-stopping/SKILL.md)
- **有限图与群。** 花瓣图检查器在外层为空时采用 \(D(K_a,x)=(1+x)^a-1\)，在 456 个小例中和直接枚举相符。交错群脚本按源文 Theorem 1 区分基本 terrace 的逆元对计数和有向条件。A3 例和 A7 打包数据均通过基本计数，实际有向标记均为 false。[花瓣图](../skills/math-petal-join-domination-polynomial/SKILL.md) · [基本 terrace](../skills/math-finite-permutation-terrace-certificates/SKILL.md)
- **精确离散边界。** 预先检查整点箱点数，再用倍增坐标在整数中验算中心化恒等式。\((2,3)\) 箱的精确最大曼哈顿长度为 12。半群程序枚举不可约超半群交分解，例子得到长度集合 \(\{2,3\}\)，并单独核对空交边界。[曼哈顿排序](../skills/math-lattice-box-manhattan-ordering/SKILL.md) · [数值半群](../skills/math-two-generator-graded-semigroup-certificates/SKILL.md)

## 分类和调用

将 116 个专项入口分为 9 个稳定领域，保留所有既有技能名、类别、兼容别名及运行依赖。新增 12 个专题入口，另将 5 个相关构件接入已有入口，覆盖数值半群、q-整数、有限算子矩阵、群对数距离和论文代码复现。目录 JSON 可按 specialty 读取，研究总入口也可按领域直达对应小节。[专项分类](../skills/math-research/references/research-specialists.md) · [研究总入口](../skills/math-research/SKILL.md)

暂存材料只包含精确来源位置、作用范围及可复用附件。本机保存源页核对、代码回放和安装证据。欧拉常数无理性仍是开放问题。
