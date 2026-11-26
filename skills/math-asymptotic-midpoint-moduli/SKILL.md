---
name: math-asymptotic-midpoint-moduli
description: 在已认证的树、段森林或 Daugavet-L1 结构上，调用渐近中点模量与可数分支 diamond 失真界；不把有限算术或抽象范数当作结构证书。
---

# 渐近中点模量与分支 diamond 审计

只有在调用方已给出所需 Banach 空间结构证书时，才使用本技能。先声明规范、参数范围、待用的渐近模量定义以及结论是下界、零模量还是失真门槛。有限算术检查不建立无限弱零树、范数分解、投影估计或紧性。

## 选择正确接口

- **任意高度弱零分支树：** 必须给出每一高度的树 `u_s^(h)`、弱零子列、`m <= ||u_s^(h)|| <= M`、兄弟分离至少 `c`，以及等价范数 `alpha||x|| <= N(x) <= beta||x||`。此时可用树阻碍接口得到
  `delta_N(alpha*c/(2*beta*M))=0`。若正模量增量为 `gamma`，先选择满足
  `alpha*m*(1+gamma/2)^h > beta*M` 的高度；该不等式只是矛盾步骤的算术门槛。
- **可数分支 diamond：** 先认证来源所用的段森林、head/tail 投影、原子池化和尾部界
  `||Q_H y|| <= 2 sqrt(R^2-||p||^2)`。在相应来源前提下再使用 `D^2 >= 1+k/4`、
  `k <= 256D^2` 或较弱的 `D > sqrt(k)/144`；不可由一条有限嵌入或一个失真数自动推出这些条件。
- **Daugavet 的 `L1` 子空间：** 必须认证单位球在测度意义下的预紧性和 Daugavet slice 性质。对给定有限 `epsilon`-网，明确给出 `b_i`、`sgn(b_i)` 与核交 `F`；只有在来源的 clipping 门槛成立时，才用 `||C(y)||_1 <= 1/2+epsilon` 推出 `H_E(x,t) >= t/2`。
- **有界树势或段镜：** 先提供来源定义的 norming sets、祖先 heads、势/锥预算，或精确段森林范数、`Q_H` 与 lens 假设。才可用局部中点不等式或 inward-crossing 估计；它们不是任意范数空间的凸性定理。

## 精确门槛重放

脚本只复算已供应参数的有理算术，**不**认证上述无限或几何前提。运行下列来源样例：

```bash
python3 scripts/tree_diamond_threshold_wave5.py tree \
  --alpha 1 --beta 2 --m 1 --M 5 --c 1 --gamma 1
```

它应输出 `minimal_height=6`、`left_at_height="729/64"`、`right="10"` 和
`modulus_argument="1/20"`。对 diamond 的已认证输入，可运行：

```bash
python3 scripts/tree_diamond_threshold_wave5.py diamond --k 4 --distortion 2
```

它仅报告两个数值门槛是否成立。输入必须是精确有理数；负或零参数不适用。

## 停止条件

没有每层弱零分支、等价范数常数、段森林投影/池化估计、Daugavet 紧性证书或来源定义的势预算时，停止在已知的有限计算，不报告中点模量或 diamond 失真结论。不要把来源的特定空间定理迁移到一般反射 Banach 空间。

## OpenAI 原稿中的方法

- [Finite clipping in a Daugavet L1 subspace](references/openai-wave5-daugavet-clipping.md)
- [Countably branching diamond lower-bound interface](references/openai-wave5-diamond-distortion.md)
- [Midpoint lenses in segment spaces](references/openai-wave5-segment-lenses.md)
- [Bounded-tree obstruction to asymptotic midpoint uniform convexity](references/openai-wave5-tree-midpoint-obstruction.md)
- [Midpoint convexity from bounded tree potentials](references/openai-wave5-tree-potentials.md)
