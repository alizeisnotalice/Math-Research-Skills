# 无外力 Euler：光滑母流上的波包输运

## 已定位来源与范围

- OpenAI, *Finite time blowup for the Euler equation*，官方固定 PDF：[euler.pdf](https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf)，57 页，SHA-256 `a0c234518e6c489e16996805023eb2e75c00b7c03455f7a3a5be2c124954bfdd`。本机盘点条目为 `standalone/Finite-time-blowup-for-the-Euler-equation.pdf`，状态为 `standalone-official-CDN`，学术复核为 `pending`。
- 本接口定位到 PDF p. 1, Theorem 1.1；pp. 3--4, equations (2.2)--(2.5)；pp. 34--36, equation (4.1) 与 Proposition 4.1 的设置。它们只支持下列光滑母流上的输运与尺度记录。

## 精确输运恒等式

设无外力 Euler 母流在所考察的时空管上光滑，并沿一条母流粒子轨道记
\[
 M=\nabla u,\qquad
 \dot m=-M^\mathsf{T}m,
 \qquad
 \dot v=-Mv+2m\frac{m\mathbin\cdot Mv}{|m|^2}.
\tag{E}
\]
其中 `m` 是非零相位余向量，`v` 是横向振幅。对 (E) 的直接代入给出
\[
 \frac{d}{dt}(m\mathbin\cdot v)
 =-(m\mathbin\cdot Mv)-(m\mathbin\cdot Mv)
   +2(m\mathbin\cdot Mv)=0.
\]
这是一次精确代数核对，故初始时 `m dot v=0` 时输运中仍为零。它依赖 `m!=0`，也依赖母流足够光滑以使沿轨道 ODE 有意义。

## 高频尺度账本

对每个有限频率 `k`，可从光滑 cutoff `chi`、光滑轮廓 `f_delta` 与输运的 `m,v` 形成原型包。若速度幅度按 `k^(-1)` 缩放，则一次微分产生尺度为一的主导张量项
\[
 \alpha\,\chi\,v\otimes m\; f_\delta'(k\,m_0\mathbin\cdot y),
\]
而未命中快速相位的导数仍携带 `k^(-1)`。这解释“速度小而梯度主导”的 WKB 记账；其常数、坐标转换与误差阶须在具体的母流、phase 和范数下重新计算。

上式不是一个精确非线性 Euler 解，也不自动散度自由。有限 `k` 的平滑性只来自输入包和母流的平滑性；要把它接入 Euler 方程，仍须单独处理散度校正、压强、截断交换项、误差传播及母流在目标时间前的全区间控制。

## 结论边界

来源 Theorem 1.1（PDF p. 1）声称由紧支撑光滑、无散度初值产生有限最大寿命的光滑 Euler 解，并给出梯度爆破与 BKM 积分发散。该完整长证明链不由本接口认证。这里不涉及外力 Euler、弱解、耗散解、凸积分解，也不将 (E) 外推到母流不光滑、`m=0` 或无限频率极限。
