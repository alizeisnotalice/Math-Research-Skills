# Papp 论文：区间多项式证书的可移植边界

## 已核对来源

- Dávid Papp, *Semi-Infinite Programming using High-Degree Polynomial
  Interpolants and Semidefinite Programming*, **SIAM Journal on Optimization**
  27(3), 1858–1879 (2017), DOI
  [10.1137/15M1053578](https://doi.org/10.1137/15M1053578)。本地原稿为
  arXiv:1512.06796v2 (22 Mar 2017)，SHA-256
  `eaa51628b8b3a5a3cf585e1a53b95e97c4bcdb3fc7ba3e5ba93e032ca4ad8993`。
- 已直接阅读本地 PDF 第 5–8 页：命题 1–3、式 (4)–(5)、定理 4–5、引理 6。
  期刊身份和 DOI 以 SIAM 书目页另行核对；这里的页码指 arXiv 本地 PDF。

## 可安全抽取的结论

在 `[-1,1]` 上，文中第 6 页的式 (4)–(5) 使用一元区间非负性的加权平方和
表示：奇次数采用 `(1+t)q+(1-t)r`，偶次数采用
`(1+t)(1-t)q+s`，其中各项是平方和。仿射换元到 `[a,b]` 后，本目录脚本检查

```text
偶型：p = S_free + (x-a)(b-x) S_weighted,
奇型：p = (x-a) S_left + (b-x) S_right.
```

每个 `S` 由调用者显式给出为有理系数多项式平方之和；脚本以
`fractions.Fraction` 展开并逐系数核验恒等式。因此接受结果是对**给定多项式和
给定闭区间**的严格非负性证明。`interval-negative-witness.json` 则以区间内有理点
的严格负值给出严格反例。

## 与插值 / SIP 的关系和限制

Papp 的定理 4（第 6 页）把 `2k+1` 个节点的非负 `SOS_{2k}` 插值值表示成 PSD
Gram 矩阵的线性约束；定理 5（第 7 页）给出 Hermite 数据的对应形式。那是构造
高次数 SDP 模型的数值友好表示，并不表示“节点值非负”本身可推出整个区间非负。
本工具刻意不接收浮点 Gram 矩阵，也不解决 SDP；它只验显式的有理平方和证明对象。

若用多项式 `p_n` 近似原函数 `f`，原文命题 1（第 5 页）仅在 `f` 至 `f^(k-1)`
绝对连续、`f^(k)` 有界变差且 `n >= k+1` 时给出
`||f-p_n||_∞ <= 4 V(f^(k))/(pi k (n-k)^k)`（在其 Chebyshev 设定）。要从
`p_n` 的证书转移到 `f` 的非负性，必须实际提供一个方向正确的误差界，例如
`p_n(x) >= E` 和 `||f-p_n||∞ <= E`。本脚本不估计 `E`，所以不能为未采样函数、
一般 SIP 可行性、最优性或交换算法收敛背书。

## 与现有技能的去重判断

- B02 已覆盖一般 SIP 的全局分离、有限采样不能认证全域约束、以及停止/收敛条件。
  本附件只提供一个单变量多项式约束的有限、可复现的**最终证书检查**，不替代 B02
  的全局分离 oracle。
- C03 已描述一般 Gram/SOS、矩层级和数值 Gram 有理化的注意事项。本附件不实现
  多变量 SOS、moment hierarchy、PSD 分解或 SDP 求解；显式有理平方项使验证不依赖
  浮点特征值。因此它是 B02 的窄接口，而不是 C03 的第二份实现。

## 复现

```sh
PY=/Users/zzh/.venvs/main/bin/python
$PY scripts/check_interval_sos_certificate.py examples/interval-even-positive.json
$PY scripts/check_interval_sos_certificate.py examples/interval-odd-positive.json
$PY scripts/check_interval_sos_certificate.py examples/interval-negative-witness.json
```

三个输入都只使用 Python 标准库；输出 `verified-nonnegative` 或
`verified-negative-witness` 才是成功。证书恒等不成立、端点无序、包含浮点数或见证点
没有严格负值时，程序以退出码 2 拒绝。
