<!-- Reader: W15; every page of the seven-page version-of-record scan was rendered and read; review pending. -->
# J. L. Lebowitz and O. Penrose (1964), “Convergence of Virial Expansions”

- **Identity/version:** *Journal of Mathematical Physics* 5(7), 841–847 (July 1964), DOI [10.1063/1.1704186](https://doi.org/10.1063/1.1704186). Read the complete 7-page version-of-record scan from [Joel Lebowitz’s Rutgers publication archive](https://cmsr.rutgers.edu/images/people/lebowitz_joel/publications-archived/jll.pub_35.pdf); AIP bibliographic record [here](https://pubs.aip.org/aip/jmp/article/5/7/841/509096/Convergence-of-Virial-Expansions). SHA-256 191484953805cfcf606b4add0c873c25caa6a99ec74b27804765480902ddd2b4.
- **Reader and extent:** W15 rendered and visually read physical PDF pp. 1–7 (printed pp. 841–847), including equations and end matter. Coverage by section is in evidence/W16/reading_coverage.json.

## Model and bounds

The paper studies a classical continuum gas in $\nu=1,2,3$ dimensions with pair potential $\phi$. In the notation of §1, stability means
\[
\sum_{1\le i<j\le n}\phi(x_i-x_j)\ge -n\Phi,
\]
and the Mayer integral must be finite:
\[
B=\int_{\mathbb R^\nu}\left|e^{-\phi(r)/(\kappa T)}-1\right|\,d^\nu r<\infty.
\]
Set $u=e^{2\Phi/(\kappa T)}\ge1$, with $u=1$ for a nonnegative potential. Pressure and density are expanded in fugacity as
\[
p(z,V)/(\kappa T)=\sum_{\ell\ge1}b_\ell(V)z^\ell,\qquad
\rho(z,V)=\sum_{\ell\ge1}\ell b_\ell(V)z^\ell;
\]
the virial coefficients $\beta_k(V)$ use density as the expansion variable. These quantities belong to the paper’s classical-gas model.

The main explicit conclusion of §3 (PDF physical p. 3, printed p. 843) follows from the Penrose coefficient estimate, the inverse density/fugacity relation, and a contour/Lagrange-inversion bound. The coefficient estimate is
\[
|\ell b_\ell(V)|\le u^{\ell-2}(\ell B)^{\ell-1}/\ell!,\qquad \ell\ge2.
\]
For $g(w)=(1-e^{-w})/w$ and $v=w(1+u)/u$, Eq. (3.11) yields the finite-volume virial-radius lower bound
\[
\mathcal R(V)\ge \max_{0\le v<(u+1)/u}\frac{v-v^2g(v/2)}{(u+1)B}\ge \frac{0.28952}{(u+1)B}.
\]
The source reports the maximizing $v$ as about 0.62984 and uses the conservative displayed constant 0.28952. Do not merge the two coefficient estimates that follow on the same physical page: Eq. (3.13) is the **finite-volume virial-coefficient** estimate
\[
k|\beta_k(V)|\le\left(\frac{(u+1)B}{0.28952}\right)^k,\qquad k=1,2,\ldots,
\]
whereas Eq. (3.14), after combination with Eq. (1.5), bounds the **infinite-volume irreducible Mayer cluster integrals**:
\[
k|\beta_k|\le\left(\frac{(u+1)B}{0.28952}\right)^k,\qquad k=1,2,\ldots.
\]
Eq. (3.15) then gives the corresponding lower bound for the infinite-volume virial radius. These are distinct coefficients and limits, not a finite-volume estimate with the $V$ merely suppressed. The derivation depends on the stable-potential Mayer bound; it is not a generic coefficient theorem detached from that model.

For hard-core potentials, §4 also gives an upper bound by maximum density: $\mathcal R(V)\le\rho_M(V)$; when the stated infinite-volume/no-phase-transition conditions hold, the corresponding infinite-volume radius is at most $\rho_M$. The paper emphasizes that the virial radius can be strictly smaller than close-packing/maximal density, including because of singularities away from the positive real axis.

## Proof and limit structure

1. **Finite-volume cluster control (§3, PDF p. 3):** apply the Penrose bound on $b_\ell(V)$; choose $|z|<1/(euB)$ and write $we^{-w}=uB|z|$, $0\le w<1$. The monotonicity of $we^{-w}$ gives a unique $w$ in this range.
2. **Density lower estimate and inversion (§2–3, PDF pp. 2–3):** bound the nonlinear part of $\rho(z,V)$ relative to $z$; the resulting lower bound on $|\rho(z,V)|$ and contour formula for $\beta_k(V)$ give the finite-volume Eq. (3.13), then optimize the scalar expression to get the radius bound Eq. (3.11). The source separately combines Eq. (3.13) with Eq. (1.5) to state Eq. (3.14) for infinite-volume irreducible Mayer cluster integrals; its infinite-volume radius implication is Eq. (3.15). The maximum in the scalar numerator is attained near $v=0.62984$.
3. **Thermodynamic limit (§§5–6, PDF pp. 4–6):** the analytic-continuation theorem requires a bounded simply connected complex-$\rho$ domain $D$, with a real interval $\rho_1<\rho<\rho_2$ below maximum density, on which the finite-volume pressure continuation is single-valued and regular for all sufficiently large $V$. The Vitali theorem then yields uniform convergence on interior contour regions from boundedness and real-interval pointwise convergence. A separate relation compares the $\liminf$ of finite-volume radii with the infinite-volume radius; do not erase the analytic-continuation or volume-limit conditions.
4. **Extensions (§7, PDF pp. 6–7):** related coefficient-radius estimates are stated for other density expansions, and §8 summarizes the lower bound, hard-core upper bound, and one-dimensional hard-rod example.

## Numerical check and scope

evidence/W16/lebowitz_penrose_constant_check.py uses 70-digit Python Decimal arithmetic and bisection on the derivative of $f(v)=v(2e^{-v/2}-1)$. It obtains $v_*=0.62984611569\ldots$, $\max f=0.28953399614\ldots$, consistent with the source’s conservative displayed constant 0.28952. For one-dimensional hard rods, $u=1$, $B=2a$, so the source lower bound gives $a\mathcal R\ge0.28952/4=0.07238$; this is the article’s displayed example. Output is saved in evidence/W16/lebowitz_penrose_constant_check_results.txt. This is arithmetic verification only, not a proof of the cluster estimate or radius theorem.

For B051 this is auxiliary structural evidence about how cluster-coefficient control can imply virial-radius bounds in a specified classical gas. It supplies no polymer representation for the optimized deletion-channel information rate, no uniformity over input processes, and no exchange of entropy-rate/input-supremum/small-deletion limits. It proves neither a B051 higher-order coefficient nor convergence of a B051 series.

