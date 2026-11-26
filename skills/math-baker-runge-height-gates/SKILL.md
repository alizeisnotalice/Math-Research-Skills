---
name: math-baker-runge-height-gates
description: 在已给出射影模型、除子和 S-整模型时，核对 Baker--Runge 型积分点高度界的交叠条件与例外集；不计算未给出的有效常数。
---

# Baker--Runge 高度界门槛

仅在调用方已明确给出数域上的光滑射影簇、每个 ample effective divisor、全局高度和 S-整模型时使用。先读[Le Fourn 的定理接口](references/le-fourn-tubular-baker-runge.md)。

- 对每个指定的 \(m_B\)-重交点，核对给出的 \(\phi_P\) 的支集和归一化；没有这些函数，不能调用结论。
- 分别记录 \(m_B,m_Y,|M_L^\infty|,|S\setminus M_L^\infty|\)，并逐字核对严格不等式 \((m_B-1)|M_L^\infty|+m_Y|S\setminus M_L^\infty|<n\)。
- 输出只能是源定理给出的、去除有效严格闭集 \(Z\) 后的高度上界。除非项目已另行构造有效 Nullstellensatz、对数形式和调节子数据，不得声称数值常数 \(C\) 或 \(C_1(d,s)\) 已算出。

曲线且给出非恒定函数 \(\phi\) 时，改用同一参考中的 Corollary 1.2；逐极点核对 \((H)_P\) 和 \(|S\setminus M_L^\infty|<n\)。这不是 S-整点枚举器，也不替代局部高度比较或 Baker 下界。
