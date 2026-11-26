# 有限增广 CTMC 的 ETFSP 核验组件

本文档配套 `scripts/etfsp_finite_certificate.py`。它实现的是有限、带一个显式弃置态的 CTMC 的定向有理数证书；它不是对可数状态 ETFSP 极限定理的替代证明。

## 已核对来源和范围

Kuntz, Thomas, Stan, Barahona, *The Exit Time Finite State Projection Scheme: Bounding Exit Distributions and Occupation Measures of Continuous-Time Markov Chains*, **SIAM J. Sci. Comput.** 41 (2019), A748–A769, DOI `10.1137/18M1168261`; 预印本为 [arXiv:1801.09507v3](https://arxiv.org/abs/1801.09507)。本地原始 PDF 哈希 `0178f07ee92816cf4cba7861597f548038409453a8d2af0fbfb8b4490a9e19a0`，页眉为 arXiv v3（2019-01-25）。

论文的 Theorem 1.1 是可数状态、稳定且保守的最小 CTMC 的 ETFSP 下界、误差及穷尽收敛结论；Theorem 2.6 给出把域外状态吸收后的时间变化律与退出/占用测度密度的关系。其占用测度的有限总变差陈述另有可积性要求。这个脚本只采用可直接独立证明的有限有界部分，故不把数值 ODE 解、有限网格或一次截断称作该收敛定理的验证。

## 输入模型及语义

输入给出一个有限保守生成元 `Q`（每个非对角元非负，且对角元恰为非对角行和的负数），并把状态严格分为：

- `domain`：尚未物理退出且仍在保留截断内的状态；
- `physical_exit`：已经真实离开研究域的吸收态；
- `loss_state`：从保留截断跳到未建模部分的唯一吸收态。

禁止把 `loss_state` 算进 `physical_exit`。若原 CTMC 与这个增广链在首次到达 `loss_state` 前耦合相同，则在时域 `[0,t]` 有

\[
  \mathbb P(\text{tracked physical exit})
  \le \mathbb P(\tau\le t)
  \le \mathbb P(\text{tracked physical exit})+\mathbb P(\text{loss by }t).
\]

同理，任一保留域内状态的真实占用时间介于杀死链的该状态占用时间与“该值加上 `loss_state` 的占用时间”之间。上界只是耦合所得的有限时域界，不能被误作无穷状态占用误差的自动可计算界。

初值落在 `physical_exit` 对应 `t=0` 的真实退出原子并被计入跟踪退出；初值 `loss_state` 被拒绝，因为这不是对原退出事件的可辨识起点。

## 证书公式

取有理数 `λ >= max_i(-q_ii)`，令 \(P=I+Q/\lambda\)，\(y=\lambda t\)，初始行向量为 \(\gamma\)。对任意状态/事件集合 \(A\)，

\[
 \mathbb P(X_t\in A)=e^{-y}\sum_{n=0}^{\infty}\frac{y^n}{n!}(\gamma P^n)(A).
\]

脚本保留到 `N=terms`。非负余项满足

\[
 \sum_{n>N}\frac{y^n}{n!}\le
 \frac{y^{N+1}/(N+1)!}{1-y/(N+2)},\qquad N+2>y.
\]

而 \(e^{-y}\) 通过把 \(y=ku\), \(0\le u\le1\)，再用 \(e^{-u}\) 的奇/偶 Taylor 部分和夹住；因此所有输出端点都是精确有理数。占用量用

\[
 \int_0^t e^{-\lambda s}\frac{(\lambda s)^n}{n!}\,ds
 =\lambda^{-1}\!\left(1-e^{-y}\sum_{k=0}^{n}\frac{y^k}{k!}\right)
\]

并给每个坐标加上不超过 \(t\) 乘上述 Poisson 尾界的余项。故输出不是浮点抽样，而是包含真值的有理区间；十进制仅为阅读便利。

## 运行和验收

```sh
python3 scripts/etfsp_finite_certificate.py \
  examples/etfsp-finite-loss-example.json -o /path/to/certificate.json
```

该示例有从 `inside` 到真实退出的速率 1、到截断弃置的速率 2。在 `t=1`，精确值为：跟踪真实退出 \((1-e^{-3})/3\)，弃置质量 \(2(1-e^{-3})/3\)，域内概率 \(e^{-3}\)，域内占用 \((1-e^{-3})/3\)。每一个值必须落入脚本所报区间。还应确认两类拒绝：`λ` 小于最大离开率，以及弃置态非吸收。它们防止把不合法 uniformization 或会回流的“丢失质量”当作下界证书。

## 不应声称的结论

- 不从一个有限截断推出 Theorem 1.1 的单调穷尽或总变差收敛；需原文的最小链、稳定/保守性、初始速率可积性、截断穷尽和时间条件。
- 不把 `loss_state` 的质量称为物理退出质量；它只给可能漏掉的退出路径上界。
- 不把这里的有限时域占用余项转换为全时间占用 TV 误差；后者还需要独立、严格的 \(\mathbb E[\tau]\) 上界以及相应假设。
