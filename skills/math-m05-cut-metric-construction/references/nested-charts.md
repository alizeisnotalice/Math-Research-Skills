# 二符号嵌套坐标图

来源为 OpenAI《Planar Graph Metrics Embed into L1 with Constant Distortion》，PDF 第 13 页，Lemma 3.1，版本与文件哈希见 [sources.md](sources.md)。

在 \(\mathbb R\times\{-1,1\}\) 上取半 Lebesgue 乘计数测度。每个点的集合由阈值 \(h(v)+\sigma\kappa P(v)\) 决定。固定 \(\sigma\) 时，两条半线的对称差长度是 \(|\Delta h+\sigma\kappa\Delta P|\)。平均两个符号并使用
\[
 \frac{|a+b|+|a-b|}{2}=\max\{|a|,|b|\}
\]
得到主文的局部 L1 公式。

若一列以 \(h\) 为严格增长坐标，且 \(P\) 在该列的 Lipschitz 常数为 \(L\)，\(\kappa L<1\) 蕴含 \(H\mapsto H\pm\kappa P(H)\) 严格增加。于是阈值集合沿列嵌套，任意两高度的对称差正好是高度增量。识别点或 switch 两侧需先核对 \(P\) 值相等。

当 \(P=\psi(h)\) 时，\(\phi_\sigma(H)=H+\sigma\kappa\psi(H)\) 在 \(\kappa\operatorname{Lip}(\psi)<1\) 下递增且满射。用 \(z'=\phi_\sigma^{-1}(z)\) 改写半线阈值，得到相同集合的零场描述。证明 Lebesgue 边缘不变时，计算任意区间 \((a,b)\) 的两个符号原像长度平均：
\[
 \frac{\phi_+(b)-\phi_+(a)+\phi_-(b)-\phi_-(a)}2=b-a.
\]

此式不跨图表。若两个点的集合借由不同的标签变量描述，必须先建立实际集合一致性或显式的共同耦合，不能直接代入 \(\max\) 公式。
