# 路径型最小匹配跟随：来源、证明与边界

## 固定来源

下表针对本机 `Math_Research_Literature/02_Recent_Math_Papers/OpenAI/current/` 的逐字节版本。
链接固定到 OpenAI `math` 仓库提交 `3344da59991ed94f9ba711217b29c1d760badfa6`；它们是
预印本定位，不表示本技能已核验其中其余主定理。

| 角色 | 本机相对路径 | SHA-256 / 页数 | 实际核对位置 | 固定原件 |
|---|---|---|---|---|
| 多重集匹配与任意初始失配的惰性模拟 | `current/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026.pdf` | `db9f0de04f757cf331b18404e7816d1fdbcf4842d79266cfd40f51d69926969e` / 71 | pp. 5–6, §2.1, Lemma 2.1 及证明 | [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026.pdf) |
| 标号实际服务器的 matching-potential lazification | `current/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026.pdf` | `2e665c0419f62ed427a64157dc31b6e3abf76b40810f0596d12ae5ef4ede8554` / 16 | pp. 4–5, §2.1, Lemma 2.2 及证明 | [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026.pdf) |

本次用 `pypdf` 重读这两份本机 PDF：页数分别为 71 和 16，且 SHA-256 与此表相符；
分别在正文中检得 `Lemma 2.1(Lazy simulation)` 与 `Lemma 2.2.`。前者直接给出任意
初始 `A_0,C_0` 的版本；后者独立写出标号服务器与虚拟配置的势函数论证。

## 独立的路径证明

令 `\Phi_t=M(A_t,C_t)`。配置是带重数的有限多重集，因此最小值由有限个排列之一达到。
在 `C_t` 中固定一个请求副本。若 `A_{t-1}` 已覆盖该请求，令 `A_t=A_{t-1}`，移动费
`m_t=0`。否则取一组达到 `M(A_{t-1},C_t)` 的匹配，令与该请求副本相连的实际服务器移至
请求点。该边原长正是 `m_t`；保留所有其他边并把此边改为长度零，产生从 `A_t` 到 `C_t`
的可行匹配，故

\[
  m_t+\Phi_t\le M(A_{t-1},C_t). \tag{1}
\]

将一个 `A_{t-1}` 至 `C_{t-1}` 的最小匹配与一个 `C_{t-1}` 至 `C_t` 的最小匹配拼接，
得到从 `A_{t-1}` 至 `C_t` 的配对路径。每条拼接路径用度量三角不等式缩短为一条边，故

\[
  M(A_{t-1},C_t)\le\Phi_{t-1}+M(C_{t-1},C_t). \tag{2}
\]

结合 (1)–(2) 后从 `t=1` 到 `H` 求和，内部势相消：

\[
 \sum_{t=1}^H m_t+\Phi_H
 \le \Phi_0+\sum_{t=1}^H M(C_{t-1},C_t).
\]

丢弃非负的 `\Phi_H` 即得技能入口中的式子。重复位置不会破坏该论证：副本先临时标号，
最后最小化忽略标号。固定顺序选取排列和请求副本使操作可复现；若 `C_t` 仅依赖已揭示
前缀，则这些选择也是因果的。

## 未采用的结论

第一篇随后叙述的有限分布估计和最终随机 k-server 主结论依赖其余各节的树分配、分区、
舍入和紧致性步骤。第二篇的有限流系统还显式引用 companion theorem 的存在性。这里没有
复核或转述那些前提链，故不声称 `O(log^2 k)`、可计算决策表，或对 `OPT` 的任何竞争比。
