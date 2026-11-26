---
name: math-linear-difference-hypertranscendence
description: 对移位、q-差分或 Mahler 线性差分方程，在已给定的函数域与系数域中应用有理函数或超越函数二分，并核验参数化差分 Galois 前提。
---

# 线性差分方程的超越性接口

用于已知解属于指定 Laurent 或亚纯函数域的线性差分方程。先固定基础域、算子、导数、解所在的函数域及系数。不得把有限系数计算、数值级数或一个递推关系当作超越性证明。

- 对 shift \(x\mapsto x+h\)、q-difference \(x\mapsto qx\) 和 Mahler \(x\mapsto x^p\) 分支，先核对 [通用二分定理](references/linear-difference-dichotomy-ext0588.md) 中逐项列出的域、常数和 Laurent 前提。若适用，输出只能是解属于基础域或在该基础域上微分超越的二分。
- 对高阶 Mahler 系统的全部导数代数独立性，另读 [Mahler 参数化 Galois 门槛](references/mahler-parametrized-galois-ext0587.md)。调用方必须提供经典差分 Galois 群包含 \(\mathrm{SL}_n\) 的证明及首末系数商为 monomial 的证明。
- 值的代数独立性需要单独认证代数点避开奇点和所用专化定理的全部假设。函数微分超越性本身不推出任意点值结论。
