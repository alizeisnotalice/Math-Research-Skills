# Diophantine 逼近构件验收（2026-11-26）

本轮从补充文献中提炼三个独立入口，并将一项同时逼近并入现有技能。源文定位、实际依赖和有限回放随技能安装。文献级阅读范围见 [补充文献索引](../skills/math-research/references/supplemental-sources/README.md)。

| 入口 | 原始依据与采用范围 | 实际验收 |
| --- | --- | --- |
| [整数线性形式的高度与余项](../skills/math-integer-linear-form-rates/SKILL.md) | EXT-0154，Zudilin Proposition 1。独立推导给定分母的精确下界，覆盖辅助整行列式为零与非零两种情况。EXT-0208，Postelmans–Van Assche Lemma 1.2 给共享分母的非消失接口。 | 本机有理算术核对 \(\sqrt2\) 的 Pell 单位例，包括 \(b=1,\ldots,64\) 的 4,224 个分子与分母组合、\(b=5\) 输出 \(64/15625\) 和无衰减输入拒绝。 |
| [Hankel–Padé 有限证书](../skills/math-hankel-pade-certificates/SKILL.md) | EXT-0320，Theorem 3.1 的精确有限分式和余项。Theorem 2.1 的无限 Hankel 子序列、Mahler 函数方程和逐层非零分开检查。 | Catalan 系数得到 \(P=1-2z\)、\(Q=1-3z+z^2\)；核对延迟出现的余项和奇异 Hankel 阶的拒绝状态。 |
| [交错倒数和的连分数判据](../skills/math-alternating-reciprocal-criteria/SKILL.md) | EXT-0322，Proposition 1 与 Theorem 1(ii)–(iii)。分别保留增长充分条件、简单连分数条件和 Roth 定理接口。 | 有限 \(B=(1,3,15,255)\) 与越界 \(B=(2,5,29,869)\) 均核对截断恒等式；仅前一组满足已给定指标的增长门槛。 |
| [Bell 多项式的欧拉常数与 zeta 逼近](../skills/math-gamma-continued-fraction-recurrence/references/bell-gamma-zeta-approximants.md) | EXT-0058，Theorem 1 和 Examples 1–2。给定 \(a,\mu,n\) 时生成共同分母、精确分子及整性诊断。 | \(a=2\) 与原有 Pilehrood 有限和逐项一致至 \(n=12\)，\(a=3,\mu=2\) 保留 \(\gamma^2+5\zeta(2)\) 的伴随常数，\(a=4,\mu=3\) 复现前三个非平凡初值。 |

审查过程发现，有理逼近趋于目标、同分母的两条余项都非零，以及 Mahler 函数方程成立，分别只提供各自的局部证据。等比例余项可能抵消，有限 Hankel 表也无法给出非零子列的无限量词。工具入口保留了这些判断，并标明 \(\gamma\) 无理性仍须独立证明。
