---
name: math-l10-prefix-code-decompositions
description: 用前缀码 episode 的 split identity 与同字 Boolean-affine recovery，构造或审计有限状态/有限向量空间的序列图语言；不用于认可来源的任何整体星高结论或复杂度界。
---

# 前缀码分裂与线性部分恢复

用于把一个有限状态计算拆为“跳过的 episode”与“可实际切开的
episode”，或用于先验证仿射 episode 更新、再取回其线性部分。固定来源、
PDF 哈希和逐篇核对范围在[来源与状态](references/sources.md)。三份来源都仍是
本机清单中的 `scholarly_review: pending`；本技能只采用以下可独立陈述的代数
接口。

## 先固定三个不同的集合

令输入字母表为有限集 \(\Sigma\)。`E` **不是新字母表**：它是
\(E\subseteq\Sigma^+\) 的一个前缀码，即没有 \(E\) 中的词是另一个的真前缀。
因此 \(E^*\) 中的词有唯一的 episode 分解。随后固定

\[
D'\subseteq D\subseteq E.
\]

- `D` 是这一次图语言的允许 episode 域；外层 `D*` 不能省略。
- `D'` 是已能精确图测试的跳过域；它不是“剩余字母”或 `D` 的补集。
- `D\\D'` 才是必须提供至少一个可行切分的 episode。`E\\D` 完全不在本次
  图语言域中。

每个 \(e\in D\) 必须在切分前已经确定一个总确定性更新
\(G_e:S\to S\)，其中 \(S\) 有限。不得让 `P` 或 `Q` 的猜测反过来定义
\(G_e\)。

## Split identity：需要验证的两个量词

令 \(W_{x,y}\) 是 `D'*` 上从 \(x\) 到 \(y\) 的**精确**图语言。为每个
\(x,y\in S\) 给出 \(P_x,Q_y\subseteq\Sigma^*\)。采用此接口前，逐条证明：

1. **对所有独立成功对的可靠性：** 若 \(w\in D^*\) 有前缀 \(uv\)，且
   \(u\in P_x,v\in Q_y\)，则 \(uv\) 恰是 `w` 的第一个 episode \(e\)，并且
   \(G_e(x)=y\)。它必须也排除空的成功对；不能只检验“同一 metadata”的配对。
2. **仅对非跳过 episode 的存在性：** 对每个 \(e\in D\\setminus D'\) 和
   每个 \(x\in S\)，存在分解 \(e=uv\)，满足
   \(u\in P_x\)、\(v\in Q_{G_e(x)}\)。无需为 `D'` 另找切分。

这两项成立时，`D*` 上的精确图语言为

\[
 D^*\cap\left[W_{x,y}\ \cup\
 \left(\bigcup_{a\in S}W_{x,a}P_a\right)
 \left(\bigcup_{b,c\in S}Q_bW_{b,c}P_c\right)^*
 \left(\bigcup_{r\in S}Q_rW_{r,y}\right)\right].
\]

证明中的对齐顺序不可跳过：先由 `W` 的前缀码分解对齐到真实边界，再将相邻
`P,Q` 用第 1 项证明为恰好一个真实 episode。反向包含才可逐个切开
`D\\D'` 中的 episode，并把相邻 `D'`-runs 吸入 `W`。当 \(D'=\varnothing\) 时，
`W_{x,y}` 仅在 \(x=y\) 时为 \(\{\epsilon\}\)，否则为空；这不是任意的基例。

若在广义星高的语境中，`D`、所有 `P_x` 与 `Q_y` 各自已有高度至多一，且所有
`W` 高度至多 \(H\)，上式给出的只是局部递推上界
\(\max\{2,1+H\}\)。使用前仍须分别给出这些语言的原字母表表达式；该式本身
不产生它们，也不认证任何整体高度结论。

## 同一词上的 Boolean-affine recovery

仅在有限向量空间 \(U\)（这里取 \(\mathbb F_2\) 亦可）上，每个 episode 有
固定的仿射更新

\[
G_e(v)=vL_e+b_e,
\]

时使用。令 \(R_{v,z}\) 是 **同一域 \(D^*\)、同一个完整 episode 序列** 的仿射
复合图语言。则其线性部分积把 \(v\) 送至 \(y\) 的图语言为

\[
 \bigcup_{f\in U}\left(R_{v,y+f}\cap R_{0,f}\right).
\]

理由是整个复合仍为 \(v\mapsto vL+b\)：同一词在零处的输出给出 \(b\)，而在
\(v\) 处的输出等于 \(y+b\) 当且仅当 \(vL=y\)。交集两边必须测试同一个词；
把两个不同 episode 序列的成功测试相交是无效替换。这里只有有限并、交与补的
布尔操作，故不会抬高已有的共同高度界。线性部分不要求可逆。

## 实施与验收

1. 写出 \(\Sigma,E,D',D,S\)、episode 的唯一分解约定与所有 \(G_e\)。先做
   前缀码检验；没有此前提不能把任意内部因子宣称为 episode 边界。
2. 将可靠性写成“任意独立的 `P`/`Q` 猜测”的全称命题；将存在性限定为
   \(D\\setminus D'\)。两者绝不可互换。
3. 若使用 affine recovery，记录 `R` 两个查询确实用了同一个完整词，并直接
   计算复合的零输出。
4. 可运行 `python3 scripts/check_finite_instance.py`。它以精确的 \(\mathbb F_2\)
   整数算术枚举 \(E=\{0,10,11\}\) 的长度至多 6 的 episode 序列，核验前缀码、
   split 公式的有限实例以及 affine-recovery 恒等式。它是回归检查，不是上述一般
   引理或来源预印本的证明。

交付时标明 `已逐行证明的局部接口`、`精确有限核验`、`条件性推论` 或
`来源声称/待核`。不要从本技能声称来源的整体结论、算法、表达式大小、运行时间，
或已完成同行评议。
