# 正四面体应用、截断和边界

## 共享边界和首次越界

对一对有限角扇形族，只要端点值夹住横向坐标，取第一个达到或超过目标值的分割节点，即得到相邻两扇形的闭区间夹逼。该步骤无需节点值单调。对于两个互补 sweep，若各自被选中的截距都超过径向 cap，则两条径向不等式加总会和预设的共同径向预算冲突。此方法在原文中依赖正四面体的具体坐标、共享边界方程及特定 cap，不能推广成任意两柱面族的覆盖判据。

当面积按扇形求和时，把每一项写成一元光滑函数并在 tilt 的平方处 Taylor 展开。若二阶导有统一界，余项被区间长度加权，总误差不随扇形数累积。原文对特定三角形构造得到负的二次系数和四阶余项。此技能不采用该数值阈值，也不认证任何一般半投影面积反例。

## apex 的截断顺序

若速度 (G(pt,t)) 仅在 (t>0) 光滑，先固定 \(\rho>0\)。小区域 (0\le t\le\rho) 可以用有限个常速方格柱面直接覆盖。原文的一个例子取 \(\lceil2/\rho\rceil+1\) 个边长 (2(1+kc)\rho) 的方格，总加权标签面积至多
\[
16(1+kc)^2\rho.
\]
然后才把模式 1 用于紧集 \(\{(pt,t):\rho\le t\le H(p),\ |p|\le1\}\)。即使 \(DG\) 随 \(\rho\downarrow0\) 变大，固定 \(\rho\) 后平方零条件仍足够。不能先让 \(\rho\) 取极限再调用有限逼近定理。

## 文献状态和定位

- OpenAI, *Finite angular cylinder covers below the half-area bound*, PDF pp. 6--11，Proposition 3.1、Corollary 3.2、Proposition 4.1、Theorem 5.1。SHA-256 `edbcf76e6573c125cf3cf085ef7a2b23c3028768ff683dd76f9af5756e7bd6be`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Finite-angular-cylinder-covers-below-the-half-area-bound-September-27-2026/main.pdf)
- OpenAI, *Slope-field perturbations of the two-cylinder covering*, PDF pp. 18--21，Lemmas 6.1--6.3、Proposition 6.4。SHA-256 `6e6336ef3860f900f59ea95a73637d67f24d4f6de20a67f98a8b19396473e7ef`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Slope-field-perturbations-of-the-two-cylinder-covering-September-27-2026/main.pdf)

四篇均为本机 OpenAI 归档中的预印本。这里独立整理了有限化和边界控制构件。高维或普适的 cylinder-covering 主张、原文特定常数及完整正四面体反例仍须按相应原文和依赖单独审计。
