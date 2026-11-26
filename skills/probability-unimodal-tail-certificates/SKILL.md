---
name: probability-unimodal-tail-certificates
description: 用 Ion–Klaassen–van den Heuvel 的结果核验标准化标量单峰分布的尖锐单侧及非对称双侧尾界，精确检查阈值、公式及取等构造。
---

# 标准化单峰分布的尖锐尾界

用于标量单峰分布的标准化单侧或非对称双侧尾界。要求有限均值 \(\mu\) 和有限正方差 \(\sigma^2\)。

设 \(Z=(X-\mu)/\sigma\)，按定理保留闭尾事件 \(P(Z\ge v)\) 或 \(P(Z\le-u\ \text{or}\ Z\ge v)\)。允许原子。要改变事件的严格性，需检查端点质量。

## 选择尾界

### 单侧尾界

对每个 \(v\ge0\)，标准化单峰变量 \(Z\) 满足

\[
 P(Z\ge v)\le B_1(v):=
 \begin{cases}
 \dfrac{3-v^2}{3(1+v^2)},&0\le v\le\sqrt{5/3},\\[4pt]
 \dfrac{4}{9(1+v^2)},&v\ge\sqrt{5/3}.
 \end{cases}
\]

两段在 \(v=\sqrt{5/3}\) 处相接。原文给出 \(v>0\) 的取等分布。\(v=0\) 可报告尾界，含 \(1/v\) 的取等公式在此无定义。

### 非对称双侧尾界

按原定理的阈值方向

\[
 \sqrt3\le v\le u,
\]

尖锐上界为

\[
 P(Z\le-u\ \text{or}\ Z\ge v)\le B_2(u,v):=
 \begin{cases}
 \dfrac49\dfrac{4+(u-v)^2}{(u+v)^2},&v\le u\le v+2/v,\\[4pt]
 \dfrac4{9(1+v^2)},&u\ge v+2/v.
 \end{cases}
\]

两段在 \(u=v+2/v\) 相接，且各自在所列闭区间可取等。遇到 \(u<v\) 时，可先证明反射后仍符合所引用的单峰和事件定义。

## 取等分布

单侧第一段 \(0<v\le\sqrt{5/3}\) 将质量 \((3-v^2)/(3(1+v^2))\) 放在 \(v\)，剩余质量在 \([-(3+v^2)/(2v),v]\) 上均匀分布。第二段将质量 \((3v^2-1)/(3(1+v^2))\) 放在 \(-1/v\)，剩余质量在 \([-1/v,(1+3v^2)/(2v)]\) 上均匀分布。

双侧第一段设 \(Z=(v-u)/2+UY\)，其中 \(U\sim\operatorname{Unif}[0,1]\) 与 \(Y\) 独立。

\[
\begin{array}{c|c}
Y&\text{probability}\\ \hline
-3(u+v)/4&\frac43\frac{2+v(v-u)}{(u+v)^2}\\
0&1-\frac43\frac{4+(v-u)^2}{(u+v)^2}\\
3(u+v)/4&\frac43\frac{2+u(u-v)}{(u+v)^2}.
\end{array}
\]

双侧第二段沿用阈值 \(v\) 的单侧第二段取等分布。

## 实际调用

先确认单峰性、均值和正方差。对整数、分数或有限小数阈值，脚本用 Python `Fraction` 检查分段、归一化和尾部质量。超出双侧原定理的阈值范围时返回 `unavailable`。

```sh
python3 scripts/certify_unimodal_tail.py --mode one-sided --v 2
python3 scripts/certify_unimodal_tail.py --mode asymmetric --u 3 --v 2
python3 scripts/certify_unimodal_tail.py --mode verify
```

解析尾界及取等依据见 [原文和版本](references/ion-klaassen-van-den-heuvel.md)。本机稿 Theorems 5.2、5.4 在正式版对应 Theorems 5.2、5.5。
