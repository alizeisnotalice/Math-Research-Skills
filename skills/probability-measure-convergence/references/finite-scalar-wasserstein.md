# 精确一维 Wasserstein–1 证书

输入两个有限实轴概率律。每个原子写成 [位置, 质量]，两个数都用整数或精确有理数字符串。工具合并同位置质量，忽略零质量原子，并核对每个概率律的质量恰为 1。

~~~sh
python3 -B scripts/finite_scalar_wasserstein.py examples/finite-w1-crossing-cdfs.json
~~~

在有序原子上每次匹配两边最左端未耗尽的质量，输出完整单调耦合和成本 \(\sum_{x,y}\pi(x,y)|x-y|\)。设 \(a_i\) 为两个支撑并集的有序节点，\(H_i=F_\mu(a_i)-F_\nu(a_i)\)。输出的势函数在 \((a_i,a_{i+1})\) 上斜率为 \(-\operatorname{sgn}H_i\)，两端向外常值延拓。它是 1-Lipschitz，故任意耦合的成本至少为 \(\int f\,d(\mu-\nu)\)。有限分部求和给出
\[
 \int f\,d(\mu-\nu)
   =-\sum_i H_i\bigl(f(a_{i+1})-f(a_i)\bigr)
   =\sum_i |H_i|(a_{i+1}-a_i).
\]
单调耦合跨每个截点的质量全部沿同一方向流动，其跨截点的质量为 \(|H_i|\)。耦合成本与此下界相等，给出精确最优性证书。

对于逃逸质量例 \(\mu_n=(1-1/n)\delta_0+\delta_n/n,\ \nu=\delta_0\)，任意有界连续 \(f\) 的期望偏差至多 \(2\|f\|_\infty/n\)，故有弱收敛。单调耦合与势函数对所有 \(n\ge1\) 给出 \(W_1=1\)。一阶矩尾无法一致消失。研究一般弱极限时，应把有限算例与统一尾部条件分别登记。
