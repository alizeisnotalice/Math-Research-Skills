# Kleiner：距离二原子反转的精确有限审计

## 适用结论

令 `S` 是**有限个相互独立** Bernoulli 变量之和，允许参数在 `[0,1]`，令
`k>=0`、`r>=1`。定义

`T_{k,r}=inf { E[S] : P(S=k+r)>P(S=k) }`。

Kleiner 的 Theorem 1.1（arXiv:2610.10664v1，pp. 1--2，证明 pp. 3--10）给出

`T_{k,1}=k+1/(k+2)`；
`T_{k,2}=k+Delta_k`；
`T_{k,r}=k+1 (r>=3)`。

其中

`d_k=max(2, floor((9+sqrt(8k+33))/8))`，

`Delta_k=(d_k sqrt((k+1)(k+2))-k sqrt(d_k(d_k-1)))/(sqrt((k+1)(k+2))+sqrt(d_k(d_k-1)))`。

严格反转必推出 `E[S]>T_{k,r}`；该阈值是下确界，**不**声称反向蕴含。`r=2,k>=1` 的边界由 `Bin(k+d_k,q_k)` 实现相等而非严格反转，且 `q_k/(1-q_k)` 的平方为 `((k+1)(k+2))/(d_k(d_k-1))`。

## 何时调用脚本

对一组有理 Bernoulli 参数，调用：

```sh
python3 scripts/kleiner_reversal_threshold.py audit \
  --input examples/kleiner_strict_distance_two.json --k 1 --r 2
python3 scripts/kleiner_reversal_threshold.py boundary --k 24
```

脚本拒绝 JSON 浮点数和布尔值；用 `Fraction` 递推得到两个 atom 和均值。距离二的均值比较通过平方非负量完成：绝不把根式转为浮点数。`boundary` 的 `exact_tie_check=1` 是二项系数比与边界 odds-square 的精确有理恒等式。

## 边界

- 不适用于相关指标、无限 Bernoulli 和、尾概率比较、凸序或一般离散分布。
- 即使 `mean_vs_threshold=greater`，也不推出 atom 反转；本定理只提供严格反转的必要下界及其 sharpness。
- 文献的 Remark 9.1 通过近似扩张到独立 Poisson 成分；本脚本刻意只处理有限 Bernoulli 输入，避免把极限论证伪装为有限精确计算。
- Gnedin（arXiv:2408.06477v1）目前未作为本接口依据：既有 skill 对其局部导数恒等式已有独立可用条目，但已排除带印刷错误的扩展 Darroch/峰值公式分支。

## 文献与版本核验

- Igor Kleiner, *Why Distance Two Is Exceptional for Poisson--Binomial Point Probabilities*, arXiv:2610.10664v1, 2026-10-07；本地审阅副本 SHA-256 `9df17152724abd81f19257eccaf4f362526ebbdfcc5e8c905045156809926b81`。2026-11-26 在 arXiv 正式记录核对，未见正式发表版本。
- Alexander Gnedin, *Cross Modality of the Extended Binomial Sums*, arXiv:2408.06477v1, 2024-08-12；本地审阅副本 SHA-256 `d3662771c1c4171cefa00fced6ca176a43f96d3fe3a6f52585ffc52381f151ce`。同日以 arXiv 记录核对，未见正式发表版本。
