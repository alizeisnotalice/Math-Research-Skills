---
name: math-ag-divisor-intersection-ledger
description: 对已给定的精确除子、公共解消与交叉数表核验局部代数几何接口；不构造几何对象或采纳丰度/Iitaka 主定理。
---

# 有限除子—交叉数账本

这个构件是 L19 的坐标环消元以外的互补接口：当调用者已经给出公共光滑解消上的除子系数、全体素除子支持或有限交叉数表时，运行 `scripts/ag_divisor_intersection_ledger.py` 进行有理数精确核验。

它可审计五类窄结论：

1. 有效 nef Cartier 除子的分量权重和为零时的逐分量零度数；
2. 公共解消上两个有理形式的除子相等，从而其商无除子；
3. 列全的除子支持中不存在水平分量；
4. 几何基变换后的整 Weil 除子等于给定的主除子证人；
5. 已构造 mixed-intersection 曲线类的零/正 pairing 表。

所有几何前提（normality、properness、解消、nefness、全支持性、pullback 与交叉数的计算）都必须在 JSON 的 `attestations` 明确由调用者提供。脚本仅验证其后可有限复放的系数等式/不等式，且拒绝浮点数。它不计算 Weil pullback、检查一个映射是否 birational/contractive、证明正交性、验证 generic fibre、构造 rational section，或证明 MMP、abundance、uniform index、Iitaka birationality 或 normalized-volume 主结论。

```bash
python3 scripts/ag_divisor_intersection_ledger.py examples/positive_ledger.json
python3 scripts/ag_divisor_intersection_ledger.py examples/negative_form_mismatch.json
```

第二个例子应返回非零状态：公共解消账本中 `E` 的两个系数不等，故不能声称有常数比值；另一个任务也以正的加权度数拒绝逐分量零结论。输入字段、来源页码和每项条件见 [账本契约](references/ledger-contract.md)。

## 取整除子截面的比值域

使用[取整除子截面的比值域](references/rounded-section-ratio-field.md)。检查收缩映射与有理拉回线性等价，再转移到正次数倍数。

## 光滑一维因子的赋值扩张

使用[光滑一维因子的赋值扩张](references/smooth-factor-valuation.md)。给定有限正 log-discrepancy 的除子赋值，核对 Gauss 扩张后长度主项和归一化。
