---
name: math-l17-filtered-linear-algebra-certificates
description: 精确核验有限维空间的首项基证书及共同降算子过滤比较；不把有限样例或几何预印本主定理当作一般证明。
---

# L17 · 首项基与共同降算子证书

用于两类**有限代数**步骤：(i) 从有限维函数/多项式空间抽取首项指数；(ii) 用同一对升降算子比较两个有限过滤。它不证明 Seshadri、P=W 或任何几何主定理，也不替代对函数空间、Cohomology 或预印本中几何输入的核验。

## 固定来源与边界

- OpenAI, *Maximal Multipoint Seshadri Constants in Higher Dimensions*, version `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`, `preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/main.pdf`, SHA-256 `dc7a580f2b1d6cf6b62646bbee59e3b6a9f69628c0a23c9bff0452b6a2199997`, p. 5, Lemma 2.2.
- OpenAI, *P=W in composite rank for fixed determinant*, same pinned commit, `preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026.pdf`, SHA-256 `52c828f91521d93c3fe4dab01c3c1d8bdaa580c1470834711c6d97f1d73c1193`, pp. 8–9, Proposition 2.4.

两份来源在本技能中只提供问题动机。下述有限代数结论已按定义重推；来源的几何主结论、外部引用和更大证明链仍是“来源声称/待核”。

## A. 首项基：可认证的部分

令 `K` 为域，`W` 是 `K{x_1,...,x_q}` 的有限维子空间。必须固定一个**全序、良序且对加法相容**的单项式序；`ν(f)` 表示非零 `f` 的最小指数。则：

1. 消元地选取 `f_1,...,f_d`：先选 `W` 中最小可达首项并把该项系数归一，再取该系数泛函的核继续。每一步维数恰减一，所以 `d=dim W` 后停止。
2. 选出的首项严格递增。任一非零线性组合由首个非零系数的 `f_i` 决定首项，故 `ν(W\{0})` 恰为这 `d` 个指数，特别地其基数是 `dim W`。
3. 对非零 `f,g`，加法相容性使除首项对以外的乘积指数严格大于 `ν(f)+ν(g)`；该指数的系数为两个非零首项系数之积。因此 `ν(fg)=ν(f)+ν(g)`。

这也给出有标签乘法空间的安全接口：若 `W_{k,γ}W_{ℓ,η}⊆W_{k+ℓ,γ+η}`，逐标签抽取首项后只能断言首项单项式空间的乘法闭包。不得由此断言 jet-surjectivity、退化平坦性或任何 Seshadri 常数结论。

### 首项门槛

- 仅有浮点系数、未说明的 tie-break、非良序（例如任意 Laurent 支撑）或未知的被截断尾项时，不能出具首项证书。
- 对解析幂级数，有限截断只有在已证明没有遗漏的更小项时才可作证书；否则它只是探索。
- 乘积式还要求系数环无零因子。有限精确多项式可直接检查；一般收敛幂级数须说明其所在整环。

## B. 共同降算子：可认证的部分

令 `H` 是特征零域上的有限维空间，`F_•,G_•` 是有限、穷尽、分离的递增整数过滤。若 `e,f∈End(H)` 对任一 `A∈{F,G}` 满足

```text
e(A_k) ⊆ A_{k+2},       f(A_k) ⊆ A_{k-2},
E^i : Gr^A_{r-i} H → Gr^A_{r+i} H  是所有 i≥0 的同构,
[[f,e],e] = -2e,        [u,v]=uv-vu,
```

其中两份 associated graded 的 Lefschetz 中心同为 `r`，则 `F_k=G_k`。

重推要点如下。对任一 `Gr^A H` 的 primitive string，定义标准降算子 `F₀(E^jv)=j(ℓ-j+1)E^{j-1}v`。它满足 `[[F₀,E],E]=-2E`。在 `End(Gr^A H)` 的有限维 `sl₂` 模中，`(ad E)^2` 在 weight `-2` 部分单射；所以关系强制 `Gr^A(f)=F₀`。因而 `h=[e,f]` 保持两过滤，且在 `Gr^A_k` 上为标量 `k-r`。从

```text
(h-(k-r)) A_k ⊆ A_{k-1}
```

连乘得到以互异根分裂的湮灭多项式，故 `h` 半单并且

```text
A_k = ⨁_{j≤k} ker(h-(j-r)).
```

右端与 `A` 无关，得到比较结论。额外分次被 `e,f` 以 `+2,-2` 保持时，该等式逐分次成立。

### 共同降算子门槛

- 必须实际检查两份过滤的升/降包含、两份 associated graded 的全部 Lefschetz 同构、相同整数中心和完整交换子式；只看到一个 Lefschetz 算子不足以比较过滤。
- 有限维、特征零和穷尽/分离不可省略。无穷维完备化、近似过滤或只在部分次数已知的 Lefschetz 资料只能给条件性路线。
- 交换子方向容易出错：本技能使用 `h=[e,f]`，因而来源中写作 `[[f,e],e]=-2e`。若采用别的括号约定，先逐项换算。

## 有限精确检查

运行：

```sh
python3 scripts/check_finite_instances.py
```

脚本只用 `Fraction`，实际执行：一个精确首项 RREF/乘积实例；一个三维 `sl₂` string 上的两过滤、Lefschetz 映射和交换子检查；并确认故意破坏的降算子被拒绝。它是实现与门槛的有限证据，不是上述一般证明，也不是外部问题的证书。

用于新的有限实例时，交付精确系数、全序单项式表，或 `e,f` 矩阵和每个过滤子空间的一组精确基；逐项报告上述门槛的通过/失败。若任一门槛失败，只保留已检查的首项/RREF 或矩阵恒等式，不输出过滤相等结论。

## C. 成对交空间与三角矩阵枢轴

对有指定配对的有限子空间族，或按对角线逐项确定的三角矩阵，读[交空间和枢轴证书](references/intersection-rank-certificates.md)。该参考分别给出行列式消失阶数的交空间界，和有限块秩差定义的局部匹配。两种证书都要求精确域上线性代数，不能据此替代几何交数或无限矩阵算子的全局结论。

**Finite-field affine-line pairing (OpenAI 2026, Lemma 2.2; Proposition 2.3 bridge).** For a supplied `GF(2^r)` polynomial of total degree at most `q-2`, use `scripts/check_affine_line_sums.py` to validate the representation and enumerate all affine lines, obtaining exact zero line and full-space sums. In the characteristic-two hole-pairing route, apply this only after independently validating the low-degree interpolation basis and deletion/incidence hypotheses; it does not certify the global group-algebra construction.

## 双次数多项式的降算算子

给定变量组、双次数及可选有理系数时，用[Foulkes–Howe 降算证书](references/foulkes-howe-lowering.md)构造稀疏算子矩阵并核对精确秩。

## OpenAI 原稿中的方法

- [Projective point--hyperplane Gram certificate](references/openai-direct-wave-2.md)
