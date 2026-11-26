# Exact replay

```sh
python3 -B scripts/check_prevost_hurwitz_pade.py
```

For `(m,n,s)=(1,1,0)`, all Hurwitz-zeta coefficients vanish and the source's
signed remainder yields the rigorous coarse bracket `1/2 < gamma < 3/4`.
The second case retains a nonzero Hurwitz-zeta coefficient to ensure that the
checker does not silently collapse the general identity into a gamma-only
claim.  Both a zero total Padé degree and `s=-1` are rejected.

指定三个参数时，脚本输出精确系数和有符号余项封套。

~~~sh
python3 scripts/check_prevost_hurwitz_pade.py --m 1 --n 1 --s 0
python3 scripts/check_prevost_hurwitz_pade.py --m 1 --n 2 --s=-1/2
~~~

余项中的 \(\zeta(r,s+1)\) 用首项 \((s+1)^{-r}\) 与单调积分
\((s+1)^{1-r}/(r-1)\) 控制。其他 Hurwitz 和对数项按原式保留。
