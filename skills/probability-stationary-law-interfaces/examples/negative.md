# Negative examples: balance tests can miss the boundary

## Interior generator tests do not prove invariance

On \([0,1]\), let \(\Phi_t(x)=\min(x+t,1)\) and start from the uniform law. For every \(f\in C_c^1((0,1))\), the interior generator is \(Lf=f'\) and \(\int_0^1 Lf(x)\,dx=0\). Yet the flow accumulates mass at 1, and
\[
\mathbb E[X_t]=\frac12+t-\frac{t^2}{2}\ne\frac12\qquad(0<t<1).
\]
The boundary-compatible test \(g(x)=x-x^2/2\), with \(g'(1)=0\), has \(\int Lg\,d\mu=1/2\). This shows why a generator identity on interior tests alone is insufficient. It is a general interface counterexample, not an A028 model or source-quota item. Exact SymPy output is saved in `../evidence/math/reader/verify_stationary_scope_output.json`.

## A candidate can fail a necessary identity

For the A17 finite-prefix Left-Hamm process, take ordered positions \(0<x_1<\cdots<x_k\), deterministic drift \(\dot x_i=x_i\), and unit-intensity space-time Poisson marks independent of the initial state: a mark \(z\in(x_{i-1},x_i)\), with \(x_0=0\), moves particle \(i\) to \(z\). On the two-particle prefix, the iid Exp(1) gap candidate has density \(e^{-x_2}\) on \(0<x_1<x_2\). For \(f_a=e^{-a x_2}\), its generator is \(Lf_a=-a x_2e^{-a x_2}+\int_{x_1}^{x_2}(e^{-az}-e^{-a x_2})\,dz\), and exact integration gives \(\int Lf_a\,d\mu=-a/(1+a)^3\ne0\). This is a valid necessary stationarity test: for any finite initial prefix, \(X_k(t)\le X_k(0)e^t\), so relevant Poisson marks on a bounded time interval are dominated by a finite-rate process; for \(f_a\), the drift term is bounded and the jump compensator is bounded by \(X_2\), which has finite candidate mean. Marks at collision/endpoints have zero intensity, so there is no omitted boundary term. The finite-prefix dynamics are also compatible under coordinate deletion: marks above \(x_k\) do not affect the first \(k\) coordinates. These checks justify the two-particle exclusion only; they do not produce an invariant law or an infinite stationary process. The short A17 model statement is [Aldous’s Left-Hamm problem page](https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html), which is a model-definition pointer and not a source-quota item. The one-particle exponential test integrates to zero and remains necessary only. No transfer to classical Hammersley or source/sink variants is valid without a new generator and boundary analysis. Exact SymPy output and scope are recorded in the L11 math output.

## Do not merge different evidence statuses

- **Qian–Xiao is held at zero credit.** Its PDF p. 6 candidate formula starts the normalizer at `k=1`, while pp. 17–18 use `k=0`. Do not silently change the source formula and then present the corrected identity as a reviewed theorem; see the candidate card（本机附件：`references/cards/QIAN_XIAO2024_GW_DIRICHLET_ENVIRONMENT.md`）.
- **The Grosskinsky thesis units are supplementary at zero quota.** Chapter 2 and Appendix A.1 were read as the actual dependent units, not as a complete 138-page thesis and not as an admitted method row; see the thesis card（本机附件：`references/cards/GROSSKINSKY2004_DOCTORAL_THESIS_CHAPTER2.md`）.
- **Behme–Schnurr is split by scope.** The CIR Example 4.3(i) is admitted with a separate actual-transition proof. The generic polynomial-characteristic, jump/core converse and multidimensional claims remain held. Do not use the CIR subcase to certify the generic branch; see the CIR card（本机附件：`references/cards/BEHME_SCHNURR2018_LAPLACE_INVARIANCE.md`）.
