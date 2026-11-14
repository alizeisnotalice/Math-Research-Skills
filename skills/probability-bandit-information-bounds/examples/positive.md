# Positive example: direct Bernoulli mean with a finite RKHS feature map

Take \(\mathcal X=\{(1,0),(0,1),(1/2,1/2)\}\), linear kernel \(k(x,z)=x^Tz\), \(\theta=(0.7,0.3)\), and \(f_\theta(x)=\theta^Tx\). Then \(f(x)=(0.7,0.3,0.5)\), \(\|\theta\|_2=\sqrt{0.58}<\sqrt2\), and \(\max_x k(x,x)=1\). Observations are **directly** \(Y\sim\mathrm{Ber}(f_\theta(x))\).

An alternative that keeps the optimal-arm mean fixed and makes arm 2 optimal has \(\lambda=(0.7,q)\), \(q\in(0.7,1]\), so every armwise value remains a valid Bernoulli mean. The three armwise means under \(\lambda\) are \((0.7,q,(0.7+q)/2)\). The structured lower-bound information is therefore
\[
\eta_2d(0.3,q)+\eta_3d(0.5,(0.7+q)/2)\ge1\quad\forall q\in(0.7,1],
\]
with regret cost \(0.4\eta_2+0.2\eta_3\); sampling the best arm supplies zero information on this confusing alternative. The actual MATLAB script `evidence/W15/rkhs_bernoulli_ossb_demo.m` evaluated a 3,001-point grid including the tie limit. It found \(d(0.3,0.7)=0.338919144155\), \(d(0.5,0.7)=0.087176693572\), and grid allocation \((\eta_2,\eta_3)=(2.950556,0)\), cost \(1.180222501\). This is a finite-grid calculation illustrating the LP, not a proof that the grid enforces the continuum of alternatives or that OSSB conditions hold.
