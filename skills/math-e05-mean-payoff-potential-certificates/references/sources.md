# 固定来源与定位

所有定位均针对本机 `Math_Research_Literature/02_Recent_Math_Papers/OpenAI/current/` 下的文件。
下表的 SHA-256 固定字节版本；官方链接固定到 OpenAI `math` 仓库提交
`3344da59991ed94f9ba711217b29c1d760badfa6`。这些是预印本定位，并不代表同行评审或
复杂度结论已由本技能复核。

| 角色 | 本机相对路径 | SHA-256 / 页数 | 已使用定位 | 固定原件 |
|---|---|---|---|---|
| 扰动、盒势带、紧边路径 | `current/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf` | `5d8d8876fd2982fd3a1a1f751893b40d38f6d400b7d669cf3f49d920ae4193d0` / 27 | p.5 式(2.1)–(2.2)；pp.6–7 Prop.2.2 及证明 | [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf) |
| 盒比较和阈值恢复 | `current/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf` | `4ab7552f58266134879a520c0d9a21a002438521e782418017ffe9bc1ecf23f3` / 41 | pp.6–8 Lemmas 2.1–2.4、Prop.2.5 | [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf) |
| 简单环删除与前缀界 | `current/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/mean-payoff-parity.pdf` | `78583f3170d29154e93c491ac9142abeb65bb45b6a0a5e8436fd30c5200fe3c4` / 14 | p.4 Lemma 2.2 及证明 | [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/mean-payoff-parity.pdf) |
| 随机折扣的限定背景 | `current/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/stochastic-mean-payoff-games.pdf` | `77e967a1db5965db666692bdd37226ed8eeb5223b8d355e614f23f0ebc0b007d` / 20 | pp.1–4 Theorem 2.1；只采用 `f_u` 的收缩事实 | [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/stochastic-mean-payoff-games.pdf) |

## 采用与未采用的断言

本技能给出了自行展开的有限确定性图证明：整数扰动的符号、闭合势证书、简单环删除和
逐前缀界。它没有采用或认证四篇论文的递归求解器、运行时间、随机化成功率、折扣极限
的量化常数、Blackwell/平稳策略结果，或均值收益 parity 游戏的完整算法。确定性论文的
basic iteration/box comparison 也被原文标为 companion work 的输入，故这里不作为独立
来源结论转述。
