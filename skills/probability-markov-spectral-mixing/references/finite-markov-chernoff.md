# 有限可逆马尔可夫链的 Chernoff 证书

设有限链从严格正的平稳分布 \(\pi\) 出发，\(P\) 满足详细平衡，\(f\) 是逐状态整数函数。取有理数 \(u>1\) 并写 \(b_i=u^{f(i)}\)、\(D=\mathrm{diag}(\sqrt{b_i})\)、\(W=\mathrm{diag}(\pi_i)\)。精确核验候选 \(r>0\) 的矩阵条件
\[
r\,\mathrm{diag}(\pi_i/b_i)-WP\succeq0.
\]
它等价于 \(rI-DPD\) 在 \(L^2(\pi)\) 上半正定。详细平衡使 \(DPD\) 自伴。由于其矩阵元非负，对任意实向量 \(\xi\)，
\[
\big|\langle \xi,DPD\,\xi\rangle_\pi\big|
\le \langle |\xi|,DPD\,|\xi|\rangle_\pi
\le r\,\|\xi\|_\pi^2.
\]
故即便 \(P\) 有负特征值，仍有 \(\|DPD\|_{L^2(\pi)}\le r\)。这一步只用有限对称二次型和逐项非负性。

若 \(S_m=\sum_{t=1}^m f(X_t)\)，按路径展开有
\[
\mathbb E_\pi[u^{S_m}]=\langle D\mathbf1,(DPD)^{m-1}D\mathbf1\rangle_\pi
\le (\pi b)\,r^{m-1}.
\]
因此将右边除以 \(u^k\) 给出 \(\Pr(S_m\ge k)\) 的上界。对左尾可改用 \(-f\) 和 \(-k\)。零次幂 \(m=1\) 时同一表达式有效。

[脚本](../scripts/certify_markov_chernoff.py)输入有理矩阵、概率向量、倾斜参数、候选算子上界、整数观测值及整数阈值。它用有理 Schur 补核验半正定性。零主元的剩余同行必须全零。它核验调用者给出的 \(r\)，并将概率上界截到 1。候选 \(r\) 被拒绝时可以更换候选再核验。

~~~sh
python3 scripts/certify_markov_chernoff.py examples/markov-chernoff-two-state.json
~~~

Kachaiev 的 *A short operator proof of Hoeffding inequalities for Markov chains* 本机原件 SHA-256 728e0a8fa8c27bffc107612988c991770cf36861734152025fb5a6f299dc9beb 的物理页 3–5（§2）用马尔可夫乘积的算子分解推导一般 MGF 控制。这里采用对有限、平稳、可逆链的独立二次型证明，直接认证给定倾斜。更一般的非可逆链、时变观测和矩阵值 Hoeffding 依赖额外论证。[固定预印本](https://arxiv.org/abs/2609.23098v1)
