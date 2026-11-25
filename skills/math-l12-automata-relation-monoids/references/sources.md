# 固定来源与验证边界

本技能只使用下列本机 OpenAI Math Release 预印本。两者在库存中均为 `scholarly_review: pending`；固定归档提交为 `3344da59991ed94f9ba711217b29c1d760badfa6`。因此下列“来源定位”不等同于正式发表或独立认证。

| 文献 | 本机相对路径 | SHA-256 | 已用页码 | 本技能采用的内容 |
|---|---|---|---|---|
| *An exponential state lower bound for two-way nondeterministic complementation* (2026-09-25) | `current/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/paper.pdf` | `302292b182622e126913eaa4ee8d73ecdd98b148e3364028a7cb9dfa6ac897b4` | 4–5, 11 | Proposition 2.3 的 singleton-context 分离；Lemma 4.2 的 relation-corner restriction isomorphism。 |
| *An exponential two-way deterministic state lower bound for one-way liveness* (2026-09-25) | `current/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/main.pdf` | `612819217a2929102a0e55c00cc4fb606b733d1f90dda513d42bf47783e0a92e` | 8, 18–19 | Lemma 2.4 的同一角同构；Lemma 5.2 的 context-separation 满射。 |

抽取文本定位分别是：

- `/Volumes/data/CodexTemp/Math-Research-Skills/openai-corpus.gruR7ANo/pages/302292b182622e126913eaa4ee8d73ecdd98b148e3364028a7cb9dfa6ac897b4.json`
- `/Volumes/data/CodexTemp/Math-Research-Skills/openai-corpus.gruR7ANo/pages/612819217a2929102a0e55c00cc4fb606b733d1f90dda513d42bf47783e0a92e.json`

## 未随本技能认证的链条

两个原始手稿的完整下界还各自依赖大量额外环节：局部计算到 diagram monoid 的表示、最小秩/最小幂等角、单位提升、support 或 missing-class 损失控制、逐步 relation addition 与指数递推。它们不因角同构或有限小规模枚举而得到验证。

特别地，129a 的确定化推论还引用外部的 2DFA 线性状态补封闭变换；本技能不采用该外部步骤。129a、129b 都使用随 `|H|` 增长的全关系字母表，均不提供固定字母表或 transition-table-size 下界。
