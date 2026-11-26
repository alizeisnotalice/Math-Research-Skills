---
name: math-euler-maclaurin-quadrature-certificates
description: 为满足端点消失条件的多项式 Euler--Maclaurin 求积构造精确余项与可复核误差包围；不用于未经认证的一般浮点积分。
---

# Euler--Maclaurin 求积误差证书

用于需要把 Euler--Maclaurin 求积的离散主项转换为可检查误差包围的任务。此技能的可执行范围刻意很窄：有理系数多项式、精确有理端点和均匀网格。它不是通用数值积分器，也不会把相邻网格差或双精度残差称为证书。

## 选择与前提

1. 只有在要使用 Bailey--Borwein 的 Theorem 3 型离散误差主项时运行 [脚本](scripts/em_certificate.py)。输入的 `m,n` 均至少为 1；网格数为正整数；区间端点严格有序。
2. 脚本逐一精确检查 $D^r f(a)=D^r f(b)=0$（$0\le r\le2m+2n$）。任何一项不为零即拒绝；此时不能套用 Theorem 3 的离散主项。
3. 通过后脚本用有理算术计算 Euler--Maclaurin 余项 $E(h,m)$、Theorem 3 主项 $E_2(h,m)$，并以导数多项式的三角不等式给出 $\int|D^{2m+2n}f|$ 的可验证上界。输出的包围还显式依赖一个用户提供的、已经认证的 $\pi$ 有理包围；脚本核验其格式和方向，但不能自行证明该包围包含 $\pi$。
4. 报告时分别写出：精确多项式恒等式、条件性的 $\pi$ 包围、以及由该包围得到的有理区间。不要把本技能的有限多项式验收推广到非多项式函数、无限区间变换或未证导数界。

最小调用：

```sh
python3 scripts/em_certificate.py input.json
python3 scripts/em_certificate.py --self-test
```

输入字段和推导边界见 [证书格式与来源](references/certificate-format.md)。`--self-test` 同时运行一个正例和一个缺端点条件的拒绝例；这是脚本行为检查，非一般函数的数学证明。

## 与其他技能的关系

本技能提供的是特定的 Euler--Maclaurin 余项分解和精确有限输入检查。若需要通用有理/区间证书、向外舍入或优化对偶证书，转用 `math-l03-rational-and-interval-certificates`；不要把该技能替代为本技能，也不要反过来把 L03 的通用框架当作本论文定理的实现。
