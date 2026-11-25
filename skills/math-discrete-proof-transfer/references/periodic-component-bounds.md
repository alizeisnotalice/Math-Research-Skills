# 周期图的连通分支与有限例外点

设无向局部有限图 \(H\) 的顶点嵌入 \(\mathbb Z^d\)，并在有限指数子格 \(\Gamma\) 的平移下不变。若 \(H\) 无无限简单射线，则每个连通分支有限。证明是从分支的一点构造有限简单路径树。树有限分支，若分支有无限多顶点则树有任意深的路径，按 König 引理给出一条射线。

若同一有限分支含 \(x,x+v\)，其中 \(0\ne v\in\Gamma\)，则平移 \(v\) 是图自同构且将这个分支送回自身。沿 \(nv\) 的轨道无限，给出矛盾。因此每个分支向 \(\mathbb Z^d/\Gamma\) 的投影为单射。可以用轨道代表数 \(r=|V(H)/\Gamma|\) 作为统一上界。

设另一个图 \(G\) 删除有限顶点集 \(E\) 后是 \(H\) 的子图。记 \(b\) 为从 \(E\) 连到 \(G\setminus E\) 的边数。每个同 \(E\) 相交的 \(G\) 分支至多遇到 \(b\) 个 \(G\setminus E\) 的分支，因此
\[
  \sup_C |C|\le\max(r, |E|+br).
\]
也可用 \(b\le\sum_{e\in E}\deg_G(e)\)。如果考察的是删边后重接的图，需实际检查 \(G\setminus E\subseteq H\)。

## 由有限商图验证无射线

给每个顶点轨道选定代表。每条有向商边 \(u\to w\) 记录位移 \(g\in\Gamma\)，即从 \(u\) 的代表连到 \(w\) 的代表加 \(g\)。平行边和自环都保留，反向位移是 \(-g\)。对每个商分支用生成树计算从根到各轨道的位移势 \(h(u)\)。逐边检查 \(h(w)-h(u)=g\)。若成立，任意闭路的位移为零，任一起点可达的每个轨道至多有一个实际顶点。若某边失败，经树路径补成闭路，其非零位移可反复平移拼接，触及无限多个顶点，构成无限分支。König 引理再给出简单射线。该判别要求商边表完整，闭路的位移约束不能以模子格的剩余类代替。

有限位移例。用 \(\Gamma=3\mathbb Z^2\)，商轨道 \(u=(0,0), w=(2,0)\)，先只连 \(u\to w+(-3,0)\) 和反向边，势差为 \((-3,0)\)。若加一条 \(u\to w\) 的零位移边，出现位移为 \((3,0)\) 的闭路。具体输入与计算见 [有限图例](../scripts/check_periodic_components.py)。

来源为 OpenAI 预印本 *Bounded-Step Walks on Gaussian Primes*，PDF p. 3, Proposition 2.1。原文取 \(d=2\)、\(\Gamma=Q\mathbb Z^2\)，有限例外是筛掉的 Gaussian 素数的单位倍。有限商图位移判别是从周期性另行推导的核验方法。主定理仍取决于具体 Gaussian 素数模型是否有满足条件的有限筛。PDF SHA-256 为 a032c3f94f247e90de8077457439a0aad38325ae6f2557c2d08bfb63bfae78d4。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf)
