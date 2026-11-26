# Qi–Cui–Xu：单系数块的双二次 SOS Gram 构造

## 已核对来源

- Liqun Qi, Chunfeng Cui, Yi Xu, *Sum of Squares Decompositions and Rank Bounds
  for Biquadratic Forms*, **Mathematics** 14(4), 635 (2026), DOI
  [10.3390/math14040635](https://doi.org/10.3390/math14040635)。正式开放获取版本
  已核对。
- 本地 PDF 的 SHA-256 为
  `a260d9a8da70b44cb94ef3671bf04c937eabd6e544c875cf1ba1b450b7b04aa7`，对应
  arXiv:2601.04965v3（2026-01-20）。已直接阅读本地 pp. 6–16：定义 2.1、式 (3)、
  定理 2.3/2.5/2.7 和第 3 节构造。

## 可验算的窄构造

对论文式 (3) 的 monic、`x`-symmetric 形式，输入为整数 `m>=2` 与有理对称矩阵
`A,B in S^n`，其中 `diag(B)=0`：

```text
P(x,y) = (x^T x)(y^T y)
       + ((1^T x)^2-x^T x)(y^T A y) + (x^T x)(y^T B y).
Q = I+B-A,                 R = I+B+(m-1)A.
```

定理 2.3 给出该类中 `P>=0` 与 `Q,R` PSD 的等价；定理 2.5 的证明给出 Gram

```text
M = I_m kron Q + (1/m) 11^T kron (R-Q).
```

在索引 `(i,j)->i*n+j` 下，若提交的四指标系数
`T[i][j][k][l]` 等于 `M[i*n+j][k*n+l]`，则逐系数恒等式给出
`P(x,y)=(x kron y)^T M(x kron y)`。`Q,R` PSD 时，对 `1_m` 方向和其正交补的块对角化
得到 `diag(R,Q,...,Q)`，故 `M` PSD；定理 2.7 的构造方格数为
`rank(R)+(m-1)rank(Q)`。

CLI 使用有理 `Fraction`、全部主子式以及有理消元秩检查；不以浮点特征值判定 PSD。
小块维数限制为 `n<=12`，但没有对 `mn` Gram 做主子式枚举，因为上述精确块分解已经是
其 PSD 证明。`--emit-gram` 输出显式有理 Gram。

## 去重与非适用范围

C03 的既有内容是一般 moment/SOS 层级与任意 Gram 的方向检查；本附件只处理上述两块
`Q,R`、固定 Kronecker 公式及明确的双二次系数张量，因此是一个可复现实例构造接口，而
非另一份一般 SOS/SDP 求解器。它不会：

- 判定任意双二次型 PSD 或 SOS；
- 从浮点矩阵恢复精确证书；
- 输出有理系数平方因子（PSD Gram 保证实数 bilinear-square 分解，显式 factor 可能含根式）；
- 使用 Blekherman 的有序非对角 copositive/SPN 结果。后者属于 C02，且与双二次 Gram
  构造没有可安全合并的假设。

## 复现

```sh
PY=python3
$PY scripts/check_monic_xsymmetric_biquadratic_gram.py examples/valid_m2_n2.json --emit-gram
$PY scripts/check_monic_xsymmetric_biquadratic_gram.py examples/rejected_tensor_mismatch.json # exit 2
$PY scripts/check_monic_xsymmetric_biquadratic_gram.py examples/rejected_nonpsd_q.json        # exit 2
```

正例 `m=n=2, A=diag(1/4,0), B=0` 有 `Q=diag(3/4,1)`、
`R=diag(5/4,1)`，并精确检查给出的 16 个张量系数。第二例把一个交叉系数错误改为 0；
第三例令 `Q=diag(-1,1)`，都必须被拒绝。
