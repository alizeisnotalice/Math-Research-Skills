---
name: math-dirichlet-l-derivative-sine-reduction
description: 对给定偶周期有理数据，精确生成 Dirichlet 型级数在零点导数的形式对数权重。核对周期、对称性、零索引和分母。
---

# 周期 Dirichlet 级数的一阶导数

给定整数周期 \(q>1\) 和全部既约剩余类上的有理值。函数在非单位上取零，满足 \(f(q-a)=f(a)\)。若还要使用 \(s=1\) 处的收敛结论，单独核对周期和。

将 \(a\) 和 \(q-a\) 配对后，按 \(\log(2\sin(\pi a/q))\) 的参数生成形式系数。\(q=2\) 只有一个自配对项，其系数是 \(-f(1)/2\)。第二种归一化仅在周期至少有两个不同素因子时输出。

~~~sh
python3 scripts/formal_log_sine_weights.py --input examples/q15_even_rational_data.json
python3 scripts/formal_log_sine_weights.py --input examples/q2_singleton_rational_data.json
~~~

输出解释限定为给定 $f$ 的形式系数。后续的严格对数值、线性独立性与非零性分别需要适合的计算或定理输入。

## 补充来源中的方法

- [Even periodic Dirichlet-type data: formal log-sine reduction at `s=0`](references/dirichlet-l-derivative-log-sine-reduction.md)

## 文献复核采用的构件

- [Exact periodic \(L(1,f)\) criterion data](references/periodic-l1-exact-criterion-ext0421.md)
