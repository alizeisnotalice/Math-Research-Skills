# Prévost 的 Legendre–Padé 分数部分证书

Marc Prévost 在 Theorem 1 和式 (3.2) 定义 (0le mle n) 时的 (L_{n,m}) 与 (J_{n,m})。本机原件 SHA-256 为 `2751e941f6c44c0c6a7823e97a10a9614253f5d6ad0d9763ddfe33a1dceb400c)。恒等式在物理页 5，Markov–Stieltjes 表示在页 7–9，分部积分在页 9–10。[arXiv:math/0507231v1](https://arxiv.org/abs/math/0507231v1)。

设 (d_n=operatorname{lcm}(1,dots,n))。用精确的二项式系数构造
[
 L_{n,m}=sum_{k=0}^n(-1)^{n+k}inom nkinom{n+k}klog(n-m+k+1),
 qquad gamma=2H_n-L_{n,m}+J_{n,m}.
]
有理对数包围沿用本技能的二进归约和正项级数。当包围落在一个整数区间内时才能提取分数部分的包围。

## 从原文积分推导有限余项界

取 (a=n-m) 与 (D=1-(1-u)t)。页 9–10 的分部积分给出
[
 (-1)^mJ_{n,m}=int_0^1!!int_0^1
 rac{w(t)}{D}left(rac{u(1-u)(1-t)}Dight)^a
 left(rac{u(1-u)t}Dight)^m dt,du.
]
其中 (w(t)>0)。令 (lambda=(1-t)/D)，则 (1-lambda=ut/D)。幂的乘积等于 (u^a(1-u)^nlambda^a(1-lambda)^m)。在 (0lelambdale1) 上，最后两个因子的乘积最多为 ((a/n)^a(m/n)^m)，零指数的因子取 1。由原文的 Markov–Stieltjes 公式，
[
 0<int_0^1rac{w(t)}D,dt=rac1{log u}+rac1{1-u}<1
 qquad(0<u<1).
]
右侧严格界来自 (log(1/u)<1/u-1)。积分得到可直接计算的严格上界
[
 0<d_n(-1)^mJ_{n,m}
 < B_{n,m}=d_n(a/n)^a(m/n)^mrac{a!,n!}{(a+n+1)!}.
]

若 (B_{n,m}le1) 且 ({d_n(-1)^mL_{n,m}}ge B_{n,m})，则排除所有既约分母 (bmid d_n)。因为 (d_ngamma) 和 (2d_nH_n) 在该假设下为整数，分数部分必须等于落在 ((0,1)) 的 (d_n(-1)^mJ_{n,m})。有限计算由上面的严格有理界承担。

```sh
python3 -B scripts/prevost_fractional_gate.py 4 1 --terms 24
```

当 (n=4,m=1) 时排除 (bmid12)。单个证书只排除所列分母。要推出无理性，还需覆盖所有可能的分母。
