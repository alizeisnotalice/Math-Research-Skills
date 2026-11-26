---
name: math-local-bottcher-formal-conjugacy
description: 对有理系数首一多项式在无穷远构造并精确检验形式 Böttcher Laurent 共轭。适用于给定多项式和截断阶的系数计算。
---

# Böttcher 形式共轭

按首一多项式及领先项为 \(z^{-1}\) 的归一化输入。提供常数项到次高项的有理系数和所需的非负 Laurent 最高次。

~~~sh
python3 -B scripts/check_formal_conjugacy.py examples/quadratic-conjugacy.json
~~~

输出记录整个已核验的 Laurent 次数区间。给定非首一多项式时先证明其归一化换元及领先项。将形式结果用于解析论证时另行核对所用分支、收敛域和全局动力条件。 [递推证明与原文定位](references/formal-infinity-conjugacy-ext0118.md)
