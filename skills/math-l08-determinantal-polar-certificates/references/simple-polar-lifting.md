# 核坐标恢复和多齐次界

令 \(P\) 为复系数多项式，\(\Psi:\mathbb C^{h+1}\to\mathbb C^N\) 是固定仿射映射，\(w_1,\ldots,w_h\) 为固定环境方向。假设方程
\[
P\circ\Psi=0,\qquad (\partial_{w_j}P)\circ\Psi=0\quad(1\le j\le h)
\]
有 \(\mu>0\) 个所选互异简单根。若 \(P\) 是 \(n\) 阶仿射行列式的系数逐项极限，则
\[
\begin{split}
\mu&\le [H^{h+1}U^{n-1}V^{n-1}](H+U)^n(H+V)^{n-1}(U+V)^h\\
&\le 2^h\binom{2n-1}{h+1},\qquad
n\ge\frac{h+1}{4e}\mu^{1/(h+1)}.
\end{split}
\]

1. 对每个所选根用复隐函数定理。因每个待比较的多项式度数至多 \(n\)，系数空间为有限维。指定任意一个足够接近的矩阵行列式 \(Q=\det A\) 便保留全部所选根，邻域不交。只需 \(Q\) 的系数接近。
2. 每个保留根处 \(\mathrm d(Q\circ\Psi)\ne0\)，故矩阵余子式矩阵非零且 \(A\) 的秩恰为 \(n-1\)。一个共同线性坐标可同时在有限条右核线上非零，令右核第一坐标为 1。提升到 \(\mathbb P^{h+1}\times\mathbb P^{n-1}\times\mathbb P^{n-1}\) 后，分别用 \(Ap=0\)、\((b^\top A)_j=0\ (j\ge2)\)、\(b^\top(\partial_{w_i}A)p=0\)。正规化 \(p_1=1\) 时，右核等式与其余左等式蕴含被省略的左等式。
3. 在每个提升点，可选可逆 \((n-1)\) 阶子块 \(E\)，使左右核其余坐标由 \(-E^{-1}\gamma\) 与 \(-\beta E^{-1}\) 恢复。消元后为 Schur 标量 \(S=a-\beta E^{-1}\gamma\) 及其环境方向微分。原极方程由消元后的方程经可逆三角变换得到，对角因子为 \(\pm\det E\)。辅助的两块 Jacobian 分别是 \(E,E^\top\)。所以原来的简单根提升后仍简单。
4. 三组方程的多齐次次数分别为 \((1,1,0),(1,0,1),(0,1,1)\)。多齐次简单根上界可用把每个方程替换为相应因子中的一般位置超平面乘积来数。每个简单根在小扰动下保留。一般位置的乘积系统有恰好所列系数个简单根；在连接两个系统的复参数直线，坏参数由项目空间上的秩亏闭条件给出有限集，简单根数在其补集上恒定。于是任意有限的所选简单根都受系数界约束。令 \(U=V=1\) 得较粗二项式上界，再用 \(\binom{a}{b}\le(ea/b)^b\)。

本机 SymPy 以 \(Q(x,y)=xy-1\) 和 \(w=(1,1)\) 验证两个复简单根 \((\pm\mathrm i,\mp\mathrm i)\)。核向量为 \((1,-x)\)，二乘二简单性行列式为 \(y-x\)，\(n=2,h=1\) 的多齐次系数为 3。

OpenAI 预印本 PDF 27–31 页，Lemma 8.2、Proposition 8.3 的局部核提升与计数。用于永久式的特定光滑切片构造需再核对。SHA-256 9eb71358fe8d9e08b450286ec6f40cb9f1452f3a49ed7801429485c2676526a6。[A cubic lower bound for border determinantal complexity of the permanent](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026.pdf)


## 整系数秩证书跨特征零域

由整系数多项式、乘法及普通微分构造的有限线性算子，在单项式基中的矩阵可直接用整数生成。每个子式是整数，非零性在任意特征零域上保持。因此这种矩阵的复数域秩界，只要确实是同一个算子，便可传给其它特征零域。若来源使用带权正规化基，核对那一步为复数域内的可逆换基。作为最小核验，本机 SymPy 得二阶微分作用在 \(x^2\) 的系数为 2，在特征零上的一阶子式非零，在特征二变零。线路复杂度上界或特定矩阵族的秩估计仍各自需要证明。

- OpenAI 预印本 PDF 19 页，Corollary 6.1 使用整数秩传递。SHA-256 c8b7c21cad425efeb1d244695e92c3e790448ff1a2c624fda0d988a043abacf9。[Homogeneous depth-five lower bounds for iterated matrix multiplication](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026.pdf)
