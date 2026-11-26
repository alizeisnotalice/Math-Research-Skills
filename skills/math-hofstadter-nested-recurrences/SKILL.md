---
name: math-hofstadter-nested-recurrences
description: 用精确整数递推计算广义 Hofstadter 函数 F_k 的有限前缀，并核对已给出的点态比较。
---

# 广义 Hofstadter 嵌套递推

给定整数 \(k\ge1\) 和截断 \(N\ge0\)，计算
\[
F_k(0)=0,\qquad F_k(n)=n-F_k^{\circ k}(n-1)\quad(n>0).
\]
递推只访问先前指标，故用整数数组精确计算。脚本可比较同一有限范围内的 \(F_k\)、\(F_{k+1}\)，并检查来源给出的阈值 \(n>12(k+1)(k+6)\)。

```sh
python3 -B scripts/evaluate_hofstadter_family.py 2 300
```

输出有限前缀的最小差、比较是否通过和实际核对的严格阈值区间。输入范围有限，任何成功输出都不证明对全部 \(n\) 的不等式。全局点态排序和严格阈值结论依赖来源的归纳证明或其形式化验证。

## 来源

[有限递推和比较的来源边界](references/ext0359-hofstadter-nested-recurrence.md)记录递推、两个定理和形式化主张。
