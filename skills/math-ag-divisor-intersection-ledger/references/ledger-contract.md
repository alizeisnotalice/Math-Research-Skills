# 有限账本契约、来源与边界

## 为什么这是一组共同接口

本构件把六项已读局部接口中可被有限符号数据复放的部分放在同一本账上：

| 账本任务 | 已核来源与物理位置 | 仅在何种外部几何前提下可解释 |
|---|---|---|
| `mixed_intersection_table` | *Schnell fiber spaces and good canonical models*, SHA `7abe2cb2832b55efb9d29c43441cc662848090c26a19c909e7fbef6e3ee1ce2a`, OpenAI pinned preprint, p. 5, Lemma 2.3 | (q:W\to V) smooth/projective-to-normal birational、(D,A) 如原文，且 pairing 的几何构造已独立完成。 |
| `vertical_divisor` | *Uniform Pluricanonical Iitaka Fibrations*, SHA `88c226e29ee72119478882f48b674d5bd0d4813a331dfa35067fef758e0e4df8`, p. 6, Lemma 3.1 | normal projective contraction、完整除子支持、normal projective generic fibre。 |
| `common_resolution_forms` | *Uniform indices for semi-log-canonical log Calabi--Yau pairs*, SHA `588f61707a03040f0265823b76aa32e17f238bfed772f79bdcd8f9867746a126`, p. 5, Lemma 2.1 | 公共光滑解消、normal proper integral resolution、两形式实际满足各自 (\operatorname{Div}(\theta)=-m\Delta)。 |
| `same_degree_principal_descent` | *Uniform log Iitaka fibrations and bounded moduli denominators*, SHA `0fee79cbeaa3ae4f119c3ca2fc961e0b7c8af1b6853af22bb3cdcacf1b55a9d5`, p. 6, Lemma 2.4 | characteristic-zero geometrically integral normal projective variety、整 Weil 除子及正确 base-change 索引。 |
| `intersection_zero_sum` | *Log abundance in numerical dimension one for threefolds in positive characteristic*, SHA `0938366c005f8930975b5a6633517cd5a50fe196c0fd3b58b0debc21c83b5277`, p. 4, Lemma 2.2 and (3) | (N) nonzero effective nef Cartier、(H) ample Cartier、完整 prime-component list。 |

同一批的 *Uniform effective log Iitaka fibrations for fourfolds*（SHA `8036215575dbf6199927ae50571f50d8e89928b091dc07fa723fec2cbfe5a41e`, pp. 7--8）给出 ratio-in-​base-field 与 section multiplication 的**理论**接口；它需要实际 rounded section spaces 和 divisorial pole inequalities，不能由仅有系数表的脚本替代，故此构件仅保留其共同的“完整除子支持/垂直性”账本边界。*The ordinary-double-point gap in every dimension* 是另一个 ready 项，但依赖渐近 valuation-ideal lengths，故不混入本有限除子账本。

所有来源均为 pinned `OpenAI/math` commit `3344da59991ed94f9ba711217b29c1d760badfa6` 的 2026 预印本；本构件没有把它们记作同行评议期刊定理。

## JSON 任务

顶层为 `{ "tasks": [...] }`。每个任务都必须有列于脚本中的全真 `attestations`。这些 boolean 不是证明；它们是为防止把符号表验算误称为几何验证而留下的明确缺口。

`intersection_zero_sum` 的每个 `components` 行为 `{id,multiplicity,degree}`，并用精确式

\[
  \sum_T a_T(N\cdot H\cdot T)=N^2\cdot H
\]

重放 source 的非负加权和步骤。只有所有 `multiplicity` 是正整数、所有 `degree` 非负且和为零，才推出每个 listed degree 为零。

`common_resolution_forms` 比较公共解消上 `pulled_back_divisor_theta_x` 与 `..._y`。相等时脚本只得出 quotient divisor 为零；“它是常数”和 B-birational 解释仍明确依赖 proper normal integral 的外部前提。

`vertical_divisor` 的行标为 `horizontal` 或 `vertical`，并要求列表是完整的。它只检查每个水平项系数是否为零；函数来自 base field 的结论依赖原文 generic-fibre normal/projective 论证。

`same_degree_principal_descent` 比较 base-changed divisor 与已供给的 principal witness。它不构造函数，也不检查 faithful-flat descent；条件成立时才可调用原文同次数 descent。

`mixed_intersection_table` 要求 `0<=k<y<=d`，所有 exceptional pairings 与 semiample pairing 为零、base pairing 严格正。它不验证 pairings 的 projection-formula 或 transverse-intersection 来源。

## 明确排除

`valid: false` 只拒绝当前有限账本或缺失的 attestation，不反驳另一份 resolution、form、section 或 model。`valid: true` 不证明主论文中的 canonical nonvanishing、good model、index bound、section field generation、MMP 终止、abundance 或任何 uniformity。浮点近似、未列全的素除子、数值等价代替除子相等、仅在 generic fibre 上的未延拓形式，都在输入域外。
