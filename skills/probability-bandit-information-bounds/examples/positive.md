# Direct Bernoulli allocation on three RKHS arms

Take the linear kernel on \(\{(1,0),(0,1),(1/2,1/2)\}\), the direct Bernoulli
mean \(\theta^\mathsf Tx\) with \(\theta=(7/10,3/10)\), and a parameter
radius of \(\sqrt2\). The best arm has mean \(7/10\), and the other two means
are \(3/10\) and \(1/2\).

A confusing alternative keeps the first mean fixed. Its parameter is
\((7/10,q)\) with \(7/10<q\le1\), which makes arm 2 the best arm. The third
mean is \((7/10+q)/2\), so it can overtake arm 1 only in the same family.
All these alternatives are inside the given radius. The information
constraint and regret cost are
\[
\eta_2 d(3/10,q)+\eta_3 d(1/2,(7/10+q)/2)\ge1,\qquad
(2/5)\eta_2+(1/5)\eta_3,
\]
where \(d\) is the Bernoulli relative entropy and \(\eta_2,\eta_3\ge0\).
Use only the divergences of sampled arms when evaluating the limiting case \(q=1\).

For each \(p\in(0,1)\), \(d(p,x)\) increases for \(x>p\) because its
derivative is \((x-p)/(x(1-x))\). Both displayed divergences are therefore
minimized as \(q\downarrow7/10\). Continuity at the tie gives an equivalent
single inequality \(A\eta_2+B\eta_3\ge1\), where
\[
A=(2/5)\log(7/3),\qquad B=(1/2)\log(25/21).
\]
Arm 2 supplies strictly more information per unit regret because
\(A>2B\). Exponentiating the equivalent logarithmic inequality reduces it
to the integer comparison \(49\cdot21^5>9\cdot25^5\).
The optimum is \((\eta_2,\eta_3)=(1/A,0)\), with cost \(1/\log(7/3)\).

From the skill directory run the numerical replay in base MATLAB.

~~~sh
matlab -batch "run('scripts/replay_rkhs_bernoulli_allocation.m')"
~~~

It includes a 3,001-point grid and prints the two limiting divergences and
the allocation. The proof above covers the continuum for this model.
The general B056 algorithm and its OSSB transfer still require their own
oracle, estimation and exploration conditions. [MATLAB replay](../scripts/replay_rkhs_bernoulli_allocation.m)
