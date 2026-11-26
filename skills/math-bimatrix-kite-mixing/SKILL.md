---
name: math-bimatrix-kite-mixing
description: "核验双矩阵博弈的后悔值、s-kite 条件与精确最佳回应混合。适用于已有候选策略的局部改进与有限证书，不把尚未独立复核的全局近似 Nash 声明当作可用定理。"
---

# 双矩阵博弈 Kite 混合

给定有理收益矩阵及一个有理策略对，先用精确有理数计算双方后悔值。若后悔对落在
\(s\)-kite 区域，调用脚本输出一个经精确认证的 \(s\)-近似 Nash 均衡。

\[
K_s=\{(r_1,r_2)\in\mathbb R^2_{\geq0}:
(1-s)r_1+sr_2\leq s,\quad sr_1+(1-s)r_2\leq s\}.
\]

这个局部变换来自 Google Research 固定提交 `4a7bc8ab0bc7` 的 Cogentic 论文
*An Exact Polynomial-Time Algorithm for 1/5-Approximate Nash Equilibria in
Bimatrix Games*，本机原件 SHA-256
`ed65664e8817e323a1613f95f4fc98689719c86fb2708974bb69cc1edc139485`，PDF
物理页 7--10 的 Lemma 2.3(a)。输入收益必须是 \([0,1]\) 内的有理数，且
\(0<s<1/2\)。

- 脚本确认策略属于单纯形、计算精确后悔与 kite 不等式。
- 若 \(r_1>s\)，它将行策略向一个行最佳回应混合，权重为
  \(1-s/r_1\)。若 \(r_2>s\)，按对称方式混合列策略。
- 若原策略不在 \(K_s\)，脚本停止并只报告诊断，不能据此输出 \(s\)-近似均衡。

将 INPUT.json 传给 [精确混合脚本](scripts/kite_mixing.py)。输入、输出格式和有限验收见
[范围与验收](references/source-and-scope.md)。这个工具没有实现论文的
`MaximinKiteNE` 滤波器、Volterra 论证或其 \(1/5\) 的全局主张。正式使用那些
结论前，需要独立核验整篇证明，或取得并实际编译所声称的 Lean 形式化。

## 策略舍入

策略迭代需要有理格点时，用[精确分母单纯形舍入](references/simplex-denominator-rounding.md)。给定维数 \(d\) 和分母 \(D\)，舍入保持总质量、采用固定规则处理并列，且 \(\ell^1\) 误差至多 \(d/D\)。

## 双矩阵博弈的零和安全值

给定两个零和 LP 的有理解时，使用 [安全值证书](references/security-screen-certificate.md) 核对原始与对偶可行性、最优值匹配，以及对应 minimax 策略对的精确后悔上界。
