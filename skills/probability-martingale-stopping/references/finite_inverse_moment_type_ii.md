# 有限 test-supermartingale 的 e-power 与 Type-II 审计

## 可复用的有限接口

现有 skill 的 `evidence/W02/cards/W02-S027.md` 已保留 Forré 全文阅读、指数 ceiling 和 horizon-tilt 的来源卡；本组件只新增一个没有既有脚本的**精确有理有限实例审计器**，不重复实现 Rényi ceiling 或 i.i.d. oracle 设计。

设 `E_n>0` 为相对于过滤的条件 e-variable，即

`E_0[E_n | F_(n-1)] <= 1`，并令 `W_t=product_{n<=t} E_n`。固定 `alpha in (0,1]`，在
`W_n>1/alpha` 时拒绝。固定整数 `s>=1`；若有确定常数 `m_n` 满足

`E_1[E_n^(-s) | F_(n-1)] <= m_n`，

则迭代塔性质并以 Markov 不等式给出

`P_1(W_t<=1/alpha) <= alpha^(-s) product_{n<=t} m_n`。

该式直接上界固定时域的 II 类错误。若用同一阈值与严格不等式定义首次拒绝时刻 `tau_alpha`，则 `{tau_alpha>t} ⊆ {W_t<=1/alpha}`，同一上界也适用。要计算序贯错误的确切值，须另记运行最大值。脚本的 scheduled independent binary 子类中，`m_n` 是精确有理数，且 `E_1[W_t^(-s)]=product m_n`，所以该接口可完全以有理运算复现。

## e-power 不能替代逆矩条件

`E_1[log E_n]>0` 只约束对数乘数的均值，不能推出上述 `m_n<1`，也不能单独给出有限 horizon 的 Type-II 上界。Forré Theorem 3.7 的严格量词是：固定 `c, alpha, t` 后，改变**测试问题和设计**，仍能使每一步条件 e-power 恰为 `c` 而 `P_1(tau_alpha>t)` 任意接近一。它不是“对固定 `(P0,P1)`，任何正 e-power 设计都没有界”的结论。

示例 `finite_e_power_failure.json` 是较弱但完全有理的有限见证：三个 e-variable 在 `P1` 下均有正 e-power，然而在 `alpha=1/20`、horizon 3 时两种 Type-II error 都恰为 `9/10`。第一步的 `E_1[E_1^-1]` 很大，恰好显示缺少了逆矩收缩假设；它不取代原文“任意 c、任意 eta”的指数构造。

相对地，`finite_inverse_moment_bound.json` 有 40 个相同有理步骤，`E_1[E_n^-1]=7/8<1`，所以脚本输出严格小于一的有限 Type-II 上界和精确枚举值。

## 运行

```sh
python3 scripts/audit_binary_eprocess.py \
  --input examples/finite_inverse_moment_bound.json
python3 scripts/audit_binary_eprocess.py \
  --input examples/finite_e_power_failure.json
```

浮点与布尔 JSON 值被拒绝。输入过程是独立、确定调度的二元乘子，故只覆盖 predictability 的一个简单子类；不据此声称适应性过程、复合假设、无限时间、i.i.d. Chernoff--Stein attainability 或最优性。

## 文献核验与来源范围

- Patrick Forré, *The Type-II Error of Test Supermartingales: e-Power versus the Chernoff--Stein Exponent*, arXiv:2609.27765v1, 2026-08-19，47 pp. 本地副本 SHA-256 `1de97d7700ddbf8cb99c03f6753a2dd371ebc4e47ed5bffdaad4cec2eb80aa4e`。2026-11-26 已由 arXiv 官方记录核对；未见期刊/会议正式版。
- 反例的精确量词：Theorem 3.7 与 pp. 12--15 的 Construction 3.2、Remark 3.8。
- 逆矩上界方向：p. 15 Remark 3.12；其源头的条件 Hölder 方向见 Theorem 4.9（pp. 18--19）。Theorem 4.9 给的是由模型 Rényi 型量控制可达 exponent 的**下界方向**，而非从 e-power 推导有限 Type-II 界；不要倒置不等式。
