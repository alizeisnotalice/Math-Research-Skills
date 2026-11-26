# 取整截面比值域的倍数稳定性

设 \(f:X\to Z\) 是正规射影簇之间的 contraction，\(D\) 是 \(X\) 上的有理 Cartier 除子，并已给出
\[
 D\sim_{\mathbb Q} f^*A
\]
其中 \(A\) 是 \(Z\) 上 ample 有理 Cartier 除子。写
\[
 V_m(D)=H^0(X,\mathcal O_X(\lfloor mD\rfloor)).
\]
这个接口在调用者已经验证这些几何前提、并实际给出非零截面时，可作两项严格的截面域账本。

1. 任意同一 \(V_m(D)\) 中两个非零截面的商属于嵌入的 \(\mathbb C(Z)\subset\mathbb C(X)\)。
2. 若 \(0\ne s\in V_m(D)\)，则对每个 \(k\ge1\)，映射
   \[
   V_m(D)\longrightarrow V_{km}(D),\qquad u\longmapsto s^{k-1}u
   \]
   是单射，并保留任意两个非零像的商。因此一旦度 \(m\) 的完整线性系比值生成 \(\mathbb C(Z)\)，每个正倍数 \(km\) 也恰好生成 \(\mathbb C(Z)\)。

这是 field-generation 的有限后继步骤，不是“\(|\lfloor mD\rfloor|\) 给出双有理映射”的证书。使用它之前，必须逐项保留 caller-supplied 的 normal/projective、connected-fibre contraction、\(D\sim_{\mathbb Q}f^*A\)、以及对应截面非零性证据。

## 可复核证明

对第二项，截面不等式为
\(\operatorname{div}(u)+\lfloor mD\rfloor\ge0\) 和
\(\operatorname{div}(s)+\lfloor mD\rfloor\ge0\)。相加得到
\[
 \operatorname{div}(s^{k-1}u)+k\lfloor mD\rfloor\ge0.
\]
逐素除子有 \(k\lfloor mD\rfloor\le\lfloor kmD\rfloor\)，故像确在 \(V_{km}(D)\)。函数域无零因子给出单射，且
\((s^{k-1}u)/(s^{k-1}v)=u/v\)。这里没有使用 \(mD\) Cartier。

对第一项，取足够可整除的正整数 \(a\)，使 \(amD\) 与 \(amA\) 都是 Cartier，并固定一个有理函数把 \(amD\sim f^*(amA)\) 的主除子差写明。令 \(E=\lfloor mD\rfloor\)。因 \(aE\le amD\)，\(u^a,v^a\) 在同一个固定平凡化下首先是 \(\mathcal O_X(aE)\) 的截面，继而都是同一 \(f^*\mathcal O_Z(amA)\) 的截面；这一包含正是 pole inequalities 的使用。由 projection formula 和 \(f_*\mathcal O_X=\mathcal O_Z\)，它们对应于底上的两个截面，所以 \((u/v)^a\in\mathbb C(Z)\)。contraction 使 \(\mathbb C(Z)\) 在 \(\mathbb C(X)\) 中相对代数闭，故 \(u/v\in\mathbb C(Z)\)。这一步依赖上述几何前提，不能由除子系数表或数值等价替代。

## 最小代数例

令 \(X=Z=\mathbb P^1\)、\(f=\mathrm{id}\)、\(A=[\infty]\)、\(D=\tfrac32[\infty]\)、\(m=1\)。则 \(mD\) 不是 Cartier，但
\(\lfloor D\rfloor=[\infty]\)，故 \(V_1(D)=\langle1,t\rangle\) 的比值域为 \(\mathbb C(t)\)。取 \(s=1\)，而
\(\lfloor kD\rfloor=\lfloor3k/2\rfloor[\infty]\)；上式把 \(\langle1,t\rangle\) 注入该空间，并保留比值 \(t/1\)。这只是该截面不等式的实例，不替代一般 contraction 前提。

## 边界

本构件不证明 abundance、某个截面系非空、相对分母界、统一次数、完整系统生成、Iitaka fibration 或双有理性；也不从一个有限除子—交叉数账本推断 \(D\sim_{\mathbb Q}f^*A\)。这些是 [有限除子—交叉数账本](../SKILL.md) 的刻意外部边界。

来源：*Uniform effective log Iitaka fibrations for fourfolds*，OpenAI/math pinned commit `3344da59991ed94f9ba711217b29c1d760badfa6`，SHA-256 `8036215575dbf6199927ae50571f50d8e89928b091dc07fa723fec2cbfe5a41e`，物理页 7--8，Lemma 2.3 及其证明。
