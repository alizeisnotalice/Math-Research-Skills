# 欧拉常数与极大算子的补充文献

[回到索引](README.md)。

## 3ff85a296fd4 · Rational approximation of Euler’s constant using multiple orthogonal polynomials

- 原件。23页作者修订稿；PDF 元数据创建/修改于 2025-03-31，首页未给 arXiv 版本号。与已索引 arXiv:2404.09799v3/正式刊文同题同作者，但本件哈希不同，未逐式确认版本等同。。PDF 物理页 1, 3, 6, 9, 12, 13, 21, 22, 23。SHA-256 3ff85a296fd4ebd0d4b29427f9f1bb845225cd0fd9617bf16b80a347c3461d03。
- 欧拉常数的混合型多重 Laguerre 有理逼近。§1 Theorem 1.2（p.3）；§2 Proposition 2.2（p.6）与混合型积分表示（p.9）；递推/鞍点分析（pp.12–13）；§5（p.21）。对 x>0，混合型多重正交构造给出 γ+log x 的有理函数逼近及整数化；x=1 给 γ 的整数线性形式。文中同时明确其误差—高度质量仍不足以推出 γ 无理；§5 的更快族是待完成的思路而非已证明可用定理。
- 既有方法覆盖。可复用部分依赖混合型正交的积分/系数恒等式、整数化以及同一归一化下的余项与高度比较；p.21 仅称可望通过鞍点分析证明，不能作为依赖链。现有 skill 已逐项保留这些门槛。 已核对本作者稿的身份、主定理和关键构造页；未逐式比对本哈希作者稿与 arXiv v3 或期刊排版版，故不把版本等同性或 §5 建议当作已核验结论。
- 相关入口。[math-gamma-multiple-laguerre-approximants](../../../math-gamma-multiple-laguerre-approximants/SKILL.md)。

## f07cf3d7f3f1 · Bounds for the weak type (1,1) constant of the centred maximal operator over squares

- 原件。Tejasvi Singh Tomar，12页作者在线稿；首页标 hexagon:2611.00479v1，PDF 元数据 2026-11-15。本件哈希不同于现有索引副本；仅以本件正文核对。。PDF 物理页 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12。SHA-256 f07cf3d7f3f1980917c2bc6e7b426e900119f1cbc91c0f19e87dedaff2c4b998。
- 二维中心正方形极大算子弱型常数的核比较与周期测度证书。Theorems 1.2–1.3（pp.1–2）；Theorem 2.2（p.3）；§§3–5（pp.4–8）；Lemmas 6.1–6.2及 Theorem 1.3 证明（pp.8–9）；Appendix B（p.11）。在二维轴平行中心正方形对象中，条件性核比较把可采纳偶 L1 核的半积分转成 c₂ 上界；本稿给出参数 α=47/40、R=33/20、h=1/32 的核并声称 1.7027237335≤c₂≤3.59123，另以有限周期原子测度给下界。该几何和证明义务不能直接迁移至高维方体。
- 既有方法覆盖。数值上下界的决定性步骤是外部证书：核的 C1–C4 全域符号检查、精确矩形并集面积，以及对应 Lean/Arb 程序。PDF 说明这些材料在 Zenodo/GitHub；本次未获取或重放证书，故只保留条件性工作流。 已核对本文对象、条件性比较定理、参数和证书依赖；未重放外部 Lean/Arb/精确算术证书，未验证本哈希与现有索引副本是否逐字相同，也未把二维结论外推。
- 相关入口。[math-centered-cube-endpoint-budget](../../../math-centered-cube-endpoint-budget/SKILL.md)。
