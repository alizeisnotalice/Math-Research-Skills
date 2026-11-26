# Arima–Kim–Kojima：有限 QCQP 的后验精确证书

## 已核对来源

- Naohiko Arima, Sunyoung Kim, Masakazu Kojima, *Exact SDP Relaxations for a
  Class of Quadratic Programs with Finite and Infinite Quadratic Constraints*,
  **SIAM Journal on Optimization** 36(4), 1973–1996 (2026), DOI
  [10.1137/24M1692745](https://doi.org/10.1137/24M1692745)。SIAM 正式页已核对。
- 本地 PDF 是 arXiv:2409.07213v3（2026-06-09/封面日期 10 Jun 2026），SHA-256
  `01257b41bc5a72ebb2fea41c69442337285364fb9195c5a2d80d5f462ec4fef1`。
  已直接阅读 pp. 1–14：问题 (2)–(5)、定理 1.1–1.6、有限/无限集区分和定理 1.4 的
  proof 开端。

## 本附件验证什么

只处理**明确列出的有限**齐次二次约束：

```text
min z^T Q z
s.t. z^T B_j z >= 0  (j=1,...,m),  z_n=1.
```

提交者给出有理数 `tau`、`mu_j>=0`、可行 `z_*`，并使

```text
S = Q - tau e_n e_n^T - sum_j mu_j B_j >= 0,
z_*^T Q z_* = tau.
```

于是任意可行 `z` 有
`z^T Q z = tau + z^T S z + sum_j mu_j z^T B_j z >= tau`，而 `z_*` 达到它。
同一逐项内积论证也给出 Shor SDP 的下界；`z_*z_*^T` 是该 SDP 的可行 rank-one
矩阵，故 QCQP 与该 SDP 同值。脚本用 `Fraction` 和全部主子式的精确行列式验证，维数
上限为 12，以避免把浮点特征值容差误作证明。

这是一份**后验有限最优性/同值证书**，而非“SDP 松弛总是精确”的判定器。它不需要、
也不会声称检查论文的所有 ROG/face 条件。

## 与论文和既有技能的边界

论文定理 1.1 通过 `J` 的 rank-one-generated（ROG）性质给出目标无关的精确凸松弛框架；
定理 1.2 的 (I)/(II) 是有限矩阵集的充分条件，定理 1.3 是有限 NIQCC 情形，定理 1.4
允许特定无限集和 facial 条件。它们含集合包含、face/ROG 或全域二次区域条件，不可被本
脚本的一次有限矩阵检查替代。反过来，本脚本也不依赖这些充分条件，而是直接核验某一个
目标和显式证书。

- B02 负责半无限索引、分离和全域覆盖。本附件拒绝隐式或无限约束族，不能替代分离。
- C01 处理一般 SDP lifting、秩条件和松弛方向；这里固定齐次 QCQP、`z_n=1` 与非负
  拉格朗日乘子，以得到可提交的全局最优性证书，而不是另一个一般 SDP 工具。
- C03 是矩/SOS 层级和多项式 Gram 证书；本附件没有 SOS/moment hierarchy 或阶数收敛。
- `c7947b4` 已加入 C01 的 `verify_psd_lp_matching.py`：它核验“给定 SDP 与给定秩一
  切 LP”之间的对偶 slack 分解和同值。本附件不构造 LP 或接受任意切集；它固定有限
  QCQP 的 Shor 形式，以非负二次约束乘子和一个锚定 rank-one 点证明原 QCQP/SDP 同值。
  两者共享精确 PSD 基础检查，但待证模型和结论接口不同，故不复制 C01 的 LP 证书。

## 复现和限制测试

```sh
PY=/Users/zzh/.venvs/main/bin/python
$PY scripts/verify_finite_qcqp_sdp_certificate.py examples/valid_interval_linear_objective.json
$PY scripts/verify_finite_qcqp_sdp_certificate.py examples/rejected_indefinite_slack.json          # exit 2
$PY scripts/verify_finite_qcqp_sdp_certificate.py examples/rejected_missing_homogenization.json    # exit 2
```

正例是 `min -u` subject to `1-u^2>=0`。取 `tau=-1, mu=1/2, z_*=(1,1)`，slack 为
`[[1/2,-1/2],[-1/2,1/2]]`。第二例使 slack 不定；第三例漏掉必须的齐次化锚点，因此都
不能作为证书。
