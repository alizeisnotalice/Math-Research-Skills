# 有限匹配开关：路径圆柱与空槽置换核


## 合同

给定有限槽位集和有限层数。每层必须是所有槽位的完美匹配；每条边有独立公平的 `identity/swap` coin。指定若干外部卡的完整路径时，检查：每条路径每层确实沿该匹配边走、任一边上同时经过的路径要求相同 coin、各路径在每个边界时刻不相撞。

在这些条件下，路径事件恰为某些 `(time, matching-edge)` coin 坐标被固定的 cylinder。因此其余 coin 仍独立且公平。删去每个边界时刻的外部卡所占槽位并按槽号重标，未暴露的 coin 给出初始空槽到末端空槽的随机双射，即固定对称群上的条件置换核。相邻时间区间使用同一中间重标，故后段置换在左，内核按时间顺序卷积。

对一个自由标签，条件分布在 free–free 边平均、在 observed–free 边沿已固定的唯一自由路线运输。自由槽上的均匀分布同样演化；故其差的和为零，并且每步平方 \(\ell_2\) 范数不增加。脚本枚举未固定 coin 立方体，逐项核对上述递推及区间核合成。

## 已核对来源

三个相同固定提交 `3344da59991ed94f9ba711217b29c1d760badfa6` 的 OpenAI Math 预印本给出这一共同有限部件：

- [Conditional information under deterministic coordinate sweeps](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Conditional-information-under-deterministic-coordinate-sweeps-September-26-2026/main.pdf), 本地 SHA `ad4125b0a60530a3f364c0bb4e61d34eb1277b2477f50b3383411cecadd092d0`, pp. 6, 8–9：Lemma 2.1 的 cylinder/path-flow 归纳，以及 signed-vector one-edge update；
- [Conditional permutations in a revealed switching environment](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Conditional-permutations-in-a-revealed-switching-environment-September-26-2026/paper.pdf), SHA `59a17db01074b8bb4124cad3b8ea3ecd70cc009b339b78bde5366a4825bc87e3`, pp. 3–4：重标 free slots 后的置换核与相邻区间合成；
- [Optimal-order mixing of the Thorp shuffle](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/paper.pdf), SHA `9b02c5b13a61d6c071b9a12849d0177a4ece970f3b182893a1c3d14b660c5984`, p. 5：同一 cylinder、平均/运输和平方范数不增加的独立证明。


## 示例与验收

`two-layer-one-revealed-card.json` 有四个槽位、两层匹配，并暴露路径 \(0\to1\to3\)。其 cylinder 固定两个 coin，余下两个 coin 形成四个等概率 completion。自由标签从槽 2 出发，末端精确分布为

\[
 (1/4,\,1/2,\,1/4,\,0),
\]

其中最后一个位置被外部卡占据。初始的“点质量减自由均匀”能量为 \(2/3\)，两层后为 \(1/24\)。脚本还必须确认两个单层 slot kernels 的乘积等于完整两层 kernel。

```sh
python3 scripts/switch_cylinder_slot_certificate.py \
  examples/two-layer-one-revealed-card.json
```

拒绝条件包括：不沿匹配边的路径、同一 time-edge 上冲突的 coin 要求、边界碰撞、非完美匹配，以及大于 20 个未访问 coin 的未枚举请求。最后一项是精确枚举的资源界，不是一般网络的数学失败。
