---
name: math-gamma-gregory-series-interval
description: 用 Gregory 系数的 Fontana–Mascheroni 级数计算欧拉常数 γ 的严格有理区间，核对精确系数、剩余质量和给定有理候选。
---

# 欧拉常数的 Gregory 级数区间

给定正整数 \(N\)，由 \(z/\log(1+z)\) 的有理幂级数系数计算 \(S_N\)，并用剩余系数质量 \(R_N\) 得到严格上界 \(S_N+R_N/(N+1)\)。先读[公式、原始来源与误差证明](references/blagouchine-coppo-gregory-series.md)。

~~~sh
python3 -B scripts/gregory_series_interval.py --terms 5
~~~

从输出的分子和分母重建精确端点。用于比较指定有理量或核对 Gregory 系数。若要推断无理性，需另证整性、非零性和分母增长下的有效收缩。
