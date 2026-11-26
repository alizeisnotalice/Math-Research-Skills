# 对称二点随机矩阵：有限 corank 尾部的精确枚举器

## 已核对来源

- *The sharp exponential rate of singularity for symmetric Bernoulli matrices*,
  OpenAI Math 固定提交 `3344da59991ed94f9ba711217b29c1d760badfa6`，本地 PDF
  SHA-256 `8dfe5c0b8a0ca85cdad9b7194ed70217b1efa8618de7b80ec1fbe4db7b33674c`。
  已直接阅读 p. 4 的 Lemmas 2.2–2.3（principal rank 与 fair-bit tail）。
- *The sharp singularity rate for biased symmetric sign matrices*, 同一固定提交，本地 PDF
  SHA-256 `62c6a85b5437d9da99317ed5cb27ac6789316ee154f72863d923dd4c75389b6d`。
  已直接阅读 p. 9 的 Equation (3.1) 及其 principal-block/Schur-complement 证明。

## 可独立使用的有限结论

设 `A` 是 `d` 阶对称随机矩阵，上三角（含对角）坐标独立，且每个坐标的任一原子概率
不超过 `b`。在所选域中两个可能取值必须不同；`H` 为固定对称偏移。对任意 `1<=k<=d`，

```text
P(corank(A+H) >= k)
 <= sum_{j=k}^d binom(d,j) b^(j(j+1)/2)
 <= 2^d b^(k(k+1)/2).
```

理由是：rank 为 `d-j` 的对称矩阵有一个可逆的 `d-j` 阶主子矩阵；揭示该主块及交叉块后，
Schur 补唯一强制余下对称 `j*j` 块的 `j(j+1)/2` 个坐标。按主指标集与 `j` 做并集界。
这只依赖有限域/特征零域中的线性代数和独立性。

`exact_symmetric_binary_corank.py` 取更窄但可完全审计的接口：域固定为 Q、两种不同有理值、
相同的精确有理二点 product law、固定有理对称偏移，并在 `d<=5` 时穷举全部上三角坐标。
所以输出的实际尾概率、完整 corank 分布与上界都是 `Fraction` 的严格值。它把“独立性”作为
被构造出的 product sample space，而不是从数据或伪随机样本中猜测。

## 边界及技能归属

这适合作为 `probability-random-matrix-tensor` 的窄补件：该技能已有随机矩阵范围审计，
但当前附件处理的是有限维的对称 corank 事件，而非谱范数、Wishart 矩或非交换矩鞅。
它不是一般矩阵秩例程，因为同时给出经 principal-block 强制得到的分布无关尾界，并对完整
product model 复核实际概率。

不要把它用于：相关上三角条目、在目标域中两值合并、一般多原子分布、无穷维极限，或两篇
论文的 sharp `2^{-n+o(n)}` 奇异率。后者依赖各自的格、势函数、稀疏尾部与路径论证，未在此
转移。

## 复现

```sh
PY=python3
$PY scripts/exact_symmetric_binary_corank.py examples/valid_fair_two_by_two_corank_two.json
$PY scripts/exact_symmetric_binary_corank.py examples/valid_biased_offset_two_by_two.json
$PY scripts/exact_symmetric_binary_corank.py examples/rejected_collapsed_values.json # exit 2
```

第一例中 `d=2,k=2`，实际概率和 union bound 都等于 `1/8`。第三例两值在 Q 中相同，故源
定理的“每个强制坐标至多一个可取值”前提失效，程序拒绝。
