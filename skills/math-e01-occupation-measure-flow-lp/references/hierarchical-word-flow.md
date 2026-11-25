# 子串计数与 Euler 日程

令 \(V\) 是包含空串的有限子串封闭集合。给每个非空 \(s\) 一个非负整数 \(m(s)\)，满足 \(m(s)\ge\sum_c m(cs)\) 及 \(m(s)\ge\sum_c m(sc)\)，集合外计数为零。用重数
\[
u(s)=m(s)-\sum_c m(cs),\qquad d(s)=m(s)-\sum_c m(sc)
\]
分别添加 \(\operatorname{pref}(s)\to s\) 和 \(s\to\operatorname{suf}(s)\) 的边。非空词的入度和出度都为 \(m(s)-\sum_{c,e}m(cse)\)。空词的平衡由其它顶点与全度数和得出。两种边的总重数均为 \(W=\sum_{c} m(c)\)。若一个要求词在 \(V\) 中无真扩张且有正计数，则它出现在使用支持中。

若通过已认证的连接操作得到使用支持弱连通的平衡有向图，且空词是一个使用顶点，就可从空词作 Euler 回路。每次向上边追加一个字符。当前顶点始终是输出串的后缀，向下边只删当前顶点的首字符，所以每个经过的请求词均出现。输出长度是实际向上边数。要比较近似比，还须证明强制次数的最优下界 \(W\le\mathrm{OPT}\) 以及补连接的成本；基本流平衡本身不提供这两项。

本机核验 \(V=\{\varnothing,a,aa,aaa\}\) 的两种整计数。次数 \(3,2,1\) 给连通基图且 \(W=3\)，次数 \(1,1,1\) 虽满足扩张约束且平衡，却只使用 \(aa,aaa\)，且 \(W=1\)。后例迫使另检周期所需的重复次数与空词连通。

- OpenAI 预印本 PDF 4–5、18 页，Lemma 2.1 的下界条件、Lemma 2.2 和 Euler 输出检查。SHA-256 45ef658ae322212b4c83626fd2bfa0ad8e459f6564b4bd0395e0c9ee8eb30dfe。[A Polynomial-Time 2-Approximation for Shortest Common Superstring](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/paper.pdf)
