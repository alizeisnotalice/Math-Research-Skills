# de Roux–Carr–Ravi：实例相关秩一切的精确验收

## 来源与版本核对

- Daniel de Roux, Robert Carr, R. Ravi, *Instance-specific linear relaxations of
  semidefinite optimization problems*, **Mathematical Programming Computation**
  17, 385–435 (2025), DOI
  [10.1007/s12532-025-00275-1](https://doi.org/10.1007/s12532-025-00275-1)。出版方页
  显示接收于 2024-11-21、在线发表 2025-03-06，且是开放获取。
- 本地候选是 arXiv:2302.08118v3 (2024-02-20)，SHA-256
  `6dc834a2467f2aa63765536d22320d72d5d04c7ddde6f7b4547754e7c0d42572`。
  已直接读本地 PDF 第 1–5 页和附录 A 第 44 页：模型 (SDP)/(LS)、Observation 1 和其证明。

## 有限证书及其独立证明

对最小化 SDP

```text
min <C,X>  s.t. <A_i,X>=b_i (i=1,...,r),  X >= 0,
```

取有限向量集 `v_j`，将 PSD 条件换成 LP 的秩一必要条件
`v_j^T X v_j >= 0`。若给出精确有理的 `y, alpha_j >= 0`，且

```text
C - sum_i y_i A_i = sum_j alpha_j v_j v_j^T,                 (D)
```

则每个 LP 可行 `X` 都有

```text
<C,X> = b^T y + sum_j alpha_j v_j^T X v_j >= b^T y.
```

若另给一个对 SDP 可行的 `X_bar`，满足 `<C,X_bar>=b^T y`，它也满足这些 LP 切，
于是 SDP 与这个**指定的有限 LP**都恰取 `b^T y`。这一步只是逐项 Frobenius
内积和非负性，可独立于数值求解器验证。

本脚本检查 (D)、所有仿射等式、目标相等及 `X_bar` 的 PSD。PSD 检查采用所有主子式
的精确有理行列式（等价于实对称 PSD），所以为控制组合数仅允许维数 `n<=12`。它不把
浮点特征值阈值当作 PSD 证明。

## 与论文的关系及适用边界

预印本 Observation 1（第 4 页，证明在第 44 页）在原/对偶严格可行并已知最优对偶
`y*` 时，取其 slack 的一组正交特征向量作切，可得到与 SDP 值相同的有限 LP。附录的
论证正是把 slack 写成非负秩一和，并使用强对偶。这里的检查器采用更可审计的有限版本：
要求提交者额外提供精确 primal equality witness，故不需要程序代替用户断言严格可行、
强对偶或“该对偶已最优”。

这不是预先可用的 SDP-to-LP 通法：从某个 SDP 数值解导出 `y*`、特征向量、准确有理
分解及 primal witness 都可能和求原 SDP 一样难。切集改变时该证书也不转移；最小化方向
不能不加推导地用于最大化。

## 与 C01/C03 的去重判断

- C01 已覆盖二次提升、PSD 外松弛方向、秩一缺失及特定两球精确性；本附件只验证一个
  已给的实例相关 LP 与 SDP 的**同值闭合证书**，不建模、求解或宣称一般精确提升。
- C03 覆盖多项式 Gram/SOS 与 moment/SOS 层级。本附件的矩阵是线性 SDP 的有限秩一
  PSD 切，既不做多项式正性也不做层级收敛，故没有复制 C03。

## 复现

```sh
PY=/Users/zzh/.venvs/main/bin/python
$PY scripts/verify_psd_lp_matching.py examples/two_by_two_exact_match.json
$PY scripts/verify_psd_lp_matching.py examples/rejected_bad_slack.json  # 必须退出 2
```

正例为 `C=diag(1,2), trace(X)=1`：`y=1`，slack 是 `e_2 e_2^T`，且
`X_bar=diag(1,0)`，所以精确值为 1。负例故意把切替换成 `e_1 e_1^T`，因 slack
恒等式失败而拒绝。
