# 离散条件输运与路径因果输运

给定两个有限边缘，选择三种接口之一。`conditional` 输入原子所在的层标签，核对两侧每层总质量一致，再令跨层质量的总和为零。`causal` 输入同一有限时间网格上的两组不同路径，要求目标前缀的条件律在源端同一前缀的所有正质量延拓上相同。`bicausal` 另外施加交换两侧得到的反向条件。

## 从条件核到线性约束

在时刻 \(t<T\)，令 \(A\) 为一个源端前缀块，\(B\) 为一个目标前缀块，\(i\in A\) 为正质量源路径。因果性的等式为

\[
\mu(A)\sum_{j\in B}\pi_{ij}
=\mu_i\sum_{k\in A,\,j\in B}\pi_{kj}.
\]

在固定边缘下，除以正的 \(\mu(A)\mu_i\) 后，两边就是目标事件在源完整路径及源前缀下的条件概率。充要性来自这些块生成有限滤过。零质量原子在非负耦合中不携带质量。每个 \(A\) 省去一条路径等式，因为对 \(i\) 求和左右相等。每个时刻省去最后一个目标块，因为对 \(B\) 求和后由边缘等式自动成立。双向版本把交换后的系数填回原单元顺序。

编译后的系数表交给[附加等式输运的现有检查器](finite-constrained-transport.md)。给定耦合、边缘势和自由符号的等式乘子，可逐单元检查原始可行性、对偶松弛和精确零间隙。`--constraints-only` 返回生成的等式顺序，即 `equality_multipliers` 的顺序。

有限层标签版本对应 Hosseini–Hsu–Taghvaei 的本机稿物理页 4、12 的等坐标约束。有限路径公式是 Acciaio–Backhoff Veraguas–Zalashko 的本机 v2 物理页 4–5、25 的因果核和湮灭约束在有限字母表上的展开。调用范围为给定有理边缘及成本的有限 LP。连续模型需要各自的正则条件律、连续性及拓扑条件。[条件输运正式版本](https://epubs.siam.org/doi/10.1137/23M1618922) · [因果输运 v2](https://arxiv.org/abs/1611.02610v2)

```sh
python3 scripts/finite_information_transport_certificate.py examples/finite-causal-transport.json
python3 scripts/finite_information_transport_certificate.py examples/finite-conditional-transport.json
```

在因果例中，目标第一步为 0 的概率必须独立于源第二步，最优值为 1。对角计划违反这条等式。在条件例中，两个边缘层质量相同，方案须留在原层，最优值为 2。非最优或不可行见证退出 1，输入错误退出 2。
