# Density-only Fourier bounds and shifted mixtures

## Density-only Fourier bound

Let \(C\subset\mathbb R^2\) be locally finite. Put \(C_R=C\cap B_R\), \(N_R=\#C_R\), and assume
\[
\frac{N_R}{\pi R^2}\longrightarrow1.
\]
For a real, even Schwartz function \(f\) with \(\widehat f\ge0\), the ordered off-diagonal sum obeys
\[
\liminf_{R\to\infty}\frac1{N_R}
 \sum_{\substack{x,y\in C_R\\x\ne y}} f(x-y)
 \ge \widehat f(0)-f(0). \tag{1}
\]

For a finite radius, Fourier inversion gives
\[
\sum_{x,y\in C_R}f(x-y)=\int_{\mathbb R^2}\widehat f(\xi)|M_R(\xi)|^2\,d\xi,
\qquad M_R(\xi)=\sum_{x\in C_R}e^{2\pi i x\cdot\xi}.
\]
The relevant local mass estimate is
\[
\liminf_{R\to\infty}\frac1{N_R}\int_{|\xi|\le\delta}|M_R(\xi)|^2\,d\xi\ge1\quad(\delta>0). \tag{2}
\]
To prove it, choose a smooth \(0\le\varphi\le1\) that equals one on \(B_1\) and is supported in \(B_{1+d}\). Fourier inversion gives
\[
\int M_R(\xi)R^2\widehat\varphi(R\xi)\,d\xi=N_R.
\]
Schwartz decay controls the portion outside \(B_\delta\). Cauchy--Schwarz and Plancherel bound the local integral from below by \((1-o(1))N_R^2/(R^2\|\varphi\|_2^2)\). Since \(\|\varphi\|_2^2\le\pi(1+d)^2\), the centered density limit gives the normalized lower bound \((1+d)^{-2}\). Let \(d\downarrow0\).

If \(\widehat f(0)>0\), continuity gives \(\widehat f\ge\widehat f(0)-\eta\) near zero. Combine this with (2) and \(\widehat f\ge0\), then remove exactly \(N_R\) diagonal terms of value \(f(0)\). If \(\widehat f(0)=0\), the diagonal-included sum is already nonnegative. For an interaction \(\Phi\), (1) remains valid with \(f\) replaced in the summand by \(\Phi\) only after checking \(\Phi(z)\ge f(z)\) for every \(z\ne0\).

## Shifted positive mixtures

Assume that for every \(\alpha>0\),
\[
\liminf_{R\to\infty}\frac1{N_R}
 \sum_{\substack{x,y\in C_R\\x\ne y}}e^{-\pi\alpha|x-y|^2}
\ge\sum_{a\in A\setminus\{0\}}e^{-\pi\alpha|a|^2}. \tag{3}
\]
Here \(A\) is a reference set and all terms are nonnegative. Let \(g:(0,\infty)\to[0,\infty)\) be smooth and completely monotone. Then
\[
\liminf_{R\to\infty}\frac1{N_R}
 \sum_{\substack{x,y\in C_R\\x\ne y}}g(|x-y|^2)
\ge\sum_{a\in A\setminus\{0\}}g(|a|^2), \tag{4}
\]
with values in \([0,\infty]\).

For \(\varepsilon>0\), set \(F_\varepsilon(t)=g(\varepsilon+t)\). It has a finite positive representation
\[
F_\varepsilon(t)=\int_{[0,1]}v^t\,d\rho_\varepsilon(v),\qquad
\rho_\varepsilon([0,1])=g(\varepsilon),\quad\rho_\varepsilon(\{0\})=0. \tag{5}
\]
For an arbitrary radius sequence \(R_n\to\infty\), define
\[
A_n(v)=\frac1{N_{R_n}}\sum_{\substack{x,y\in C_{R_n}\\x\ne y}}v^{|x-y|^2}.
\]
Every \(A_n\) is continuous and nonnegative on \([0,1]\). At \(0<v<1\), apply (3) with \(\alpha=-\log(v)/\pi\). At the endpoints, \(A_n(0)=0\), while \(A_n(1)=N_{R_n}-1\to\infty\). Fatou and Tonelli apply to (5), so the lower bound follows for \(F_\varepsilon\). Since \(g\) is decreasing, \(g(t)\ge F_\varepsilon(t)\). Let \(\varepsilon\downarrow0\) only in the reference-set sum and use monotone convergence. Do not interchange that limit with the configuration lower limit.

## Finite exact check

For \(g(t)=1/t\), \(F_\varepsilon(t)=1/(\varepsilon+t)\) has the representation \(d\rho_\varepsilon(v)=v^{\varepsilon-1}\,dv\). Exact rational arithmetic verified
\[
\int_0^1v^{\varepsilon-1+m}\,dv=\frac1{\varepsilon+m}
\]
for \(\varepsilon\in\{1/2,1,3/2,2\}\) and \(m=0,\ldots,12\), giving 52 checks. This verifies the shifted representation in a singular-potential example. It does not prove (3) for any configuration.

## Conditional periodic-energy extensions

Two further source results remain conditional research references. For simple density-one periodic configurations, a heat-trace formula compares periodic Riesz or logarithmic energies across possibly different period lattices after diagonal and background cancellation. A separate reduction takes lower bounds for every square torus to a full-plane Coulomb lower bound. Both require their stated field normalizations, admissibility and approximation results. They are not consequences of (1)--(4), so this skill does not route ordinary pair-energy tasks through them.

## Source record

- *An atomic certificate for triangular-lattice universal optimality*, OpenAI preprint, 2026-09-26, PDF pp. 6--8, Lemma 2.2, Proposition 2.3 and Lemma 2.4. SHA-256 `83e0d874119abae56db94fb1ecd6ebb794753d4982464b4f9788e5158708be93`. [Fixed PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/paper.pdf)
- *Universal optimality of the triangular lattice*, OpenAI preprint, 2026-09-23, PDF pp. 33, 36--38, Proposition 6.1, Lemma 7.1 and Proposition 7.2. SHA-256 `50daa477c52b1f3e179764794506f0037d26c2ec130d1d6e817626f4e0b689f3`. [Fixed PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026/paper.pdf)
- *Triangular minimality for planar Coulomb renormalized energy*, OpenAI preprint, 2026-09-23, PDF pp. 10--11, Lemma 2.3 and Proposition 2.4. SHA-256 `6f640e977aed5d3b876e6a275a85c8549575051fb21181fb3159fba8596fcc4a`. [Fixed PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/paper.pdf)
