# 合数模数的有限线性关系证书

本构件实现 Cogentic 离散对数稿 Lemma 6.3(2) 中可独立复核的有限代数部分。源文件 `02_discrete_logarithm.pdf` 的 SHA-256 为 `fba12f4d5e98152d52226887c4af2606039725f898bffecbc8a4d91ccaf9d0d7`，物理页 31。

输入是 \(M\ge2\) 和有限关系 \(E y=a\pmod M\)。脚本认证每一列得到可逆主元，回代后的多余行全为零，并把结果代回每条原始关系。`pivot_not_unit`、`underdetermined` 和 `inconsistent_relations` 均不给出解。前两个状态只说明未满足满张成条件，最后一个状态给出了矛盾余行。

原文把行关系解释在阶为 \(M\) 的循环群中，形式为 \(\prod_j\delta_j^{E_{rj}}=\gamma^{a_r}\)。在这个额外前提下，行操作导出 \(\delta_j=\gamma^{y_j}\)。本脚本不接收群元素、不尝试离散对数，也不认证原文的下降过程、抽样满秩概率或复杂度界。

原稿中的有效群关系隐含多余行一致性。通用 JSON 输入没有该隐含条件，所以实现显式检查残余行。这会拒绝 `[[0],[1]] y=[1,1] mod 2`，不会错误返回 `y=1`。

```sh
python3 scripts/check_modular_linear_relations.py --self-test
python3 scripts/check_modular_linear_relations.py examples/positive-composite-system.json
```
