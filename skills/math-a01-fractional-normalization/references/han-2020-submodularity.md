# Han 单比值子模性精确判定

此资料仅扩展 A01 对**一个** binary ratio 的检查；它不替代 A01 中的 CCT、一般分式规划、多个比值之和或近似算法的边界说明。

## 已核对的来源

- Shaoning Han, Andrés Gómez, Oleg A. Prokopyev, *Fractional 0–1 programming and submodularity*, [arXiv:2012.07235v1](https://arxiv.org/abs/2012.07235), 14 Dec 2020。
- 本机原件：`01_Existing_Skill_Sources/Papers/38/Han_2020_Fractional 0-1 programming and submodularity__38deac7237303114.pdf`；SHA-256 `38deac7237303114fbd5b439961b710b4d8110f47dd10a2aa528390dc008807f`。本次读取 pp. 1, 3--8，并以 arXiv 的作者提交 v1 对照。正式版为 *Journal of Global Optimization* 84(1) (2022), 77–93。 [期刊版](https://doi.org/10.1007/s10898-022-01131-5)

论文的式 (2) 是多个单比值的和；这里的脚本只检查其中一个

\[
h(S)=\frac{\sum_{r\in S}a_r}{b_0+\sum_{r\in S}b_r}.
\]

## 可使用的定理边界

对给定的可行族 \(\mathcal F\subseteq2^N\)，必须逐项确认：

- A1：每个可行集合的分母严格为正；
- A2：\(a_i\ge0\), \(b_0\ge0\), \(b_i>0\)；
- A3：\(\mathcal F\) downward closed；
- **Theorem 1 的额外前提** \(b_0>0\)。

在这些条件下，Theorem 1（pp. 5--6）给出严格充要条件：对全部 \(S\subseteq N\) 和不同 \(i,j\notin S\)，只要 \(S\cup\{i,j\}\in\mathcal F\)，就检查

\[
h(S\cup\{i\})+h(S\cup\{j\})
\le \frac{a_i}{b_i}+\frac{a_j}{b_j}.
\]

全部成立当且仅当 \(h\) 在该 \(\mathcal F\) 上子模。脚本还用精确有理数计算同一三元组的直接二阶差

\[
h(S\cup\{i,j\})-h(S\cup\{j\})-h(S\cup\{i\})+h(S),
\]

作为逐条一致性检查。若 \(D=b_0+\sum_{r\in S}b_r\)，二阶差等于上述不等式左侧减右侧乘 \(b_i b_j/[D(D+b_i+b_j)]\)。在正分母条件下，该乘子严格为正。

论文 Proposition 1 仅说明“单调不减”足以推出子模性；不能把非单调误判成非子模。论文 Example 1 正是非单调而子模的例子。\(b_0=0\) 也不在 Theorem 1 的范围内；Proposition 3 在存在三个不同 \(a_i/b_i\) 的可行集合时给出非子模性，但不构成 \(b_0=0\) 的完整判据，故脚本只报告 `out_of_scope`。

## 调用

数值必须是 JSON 整数或有理数字符串（如 `"7/9"`）；拒绝 JSON float。省略 `feasible_masks` 表示 \(2^N\)。若指定它，则用从零开始的 bitmask，并由脚本验证 A3。第 \(i\) 个变量对应 bit `1 << i`。

```sh
python3 scripts/check_han_single_ratio.py examples/han-paper-example.json
```

退出码：`0` 表示在定理范围内且子模，`1` 表示已找到精确反例，`2` 表示超出该定理范围，`3` 表示输入错误或人为设置的枚举资源上限。默认 `--max-n 20` 只是防止无意的指数枚举，并非数学前提；若提高该上限，应记录实际运行范围和时间。

脚本的 `submodular` 只证明给定的有限 `a,b,b0,\mathcal F` 实例通过该定理。它不证明多个比值的和具有同一性质，不提供 greedy 的适用条件或近似保证，也不处理零、变号或负系数分母。
