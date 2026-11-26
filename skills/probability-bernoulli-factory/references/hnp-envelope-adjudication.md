# HNP envelope dependency adjudication for the debiased factory

## Primary sources actually checked

- Holtz, Nazarov, Peres, *New coins from old, smoothly*, [arXiv:0808.1936v3](https://arxiv.org/abs/0808.1936), last revised 2010-01-25; journal reference *Constructive Approximation* 33 (2011), 331--363, DOI `10.1007/s00365-010-9108-5`. The official arXiv PDF was temporarily obtained for this check (and then removed from the staging root), SHA-256 `d7d15d66f964800f8a50999e3a515194d56d45388f90812917f21cedf2044f23`; all 29 pages were checked. Relevant physical locations: Result 3 pp. 3--4, Theorem 8 and Lemma 9 p. 6, and the sufficiency construction §5 pp. 18--24.
- Koskela, Karvonen, Łatuszyński, Spanò, *A debiased Bernoulli factory and unbiased estimation of a probability*, [arXiv:2510.01941v2](https://arxiv.org/abs/2510.01941), last revised 2026-09-01; local PDF dated 2026-09-02, SHA-256 `85bc6a2ec6b57416f3b492bb6d45d5fe0cd5353061f77f95ac2a946cb95bca18`. Relevant physical locations: Theorem 1 p. 3; Theorem 2 and proof pp. 4--7; implementability §4 pp. 8--9.

## What HNP directly verifies

For a noninteger `alpha>0`, `f:[0,1]->(0,1)`, and `f in C^alpha[0,1]`, HNP Theorem 8 gives full-degree Bernstein polynomials `g_n,h_n` satisfying Result 3(i), (ii'), (iii), (iv), with a uniform gap

`h_n(x)-g_n(x)=O(Delta_n(x)^alpha)`,

where `Delta_n(x)=max(sqrt(x(1-x)/n),1/n)`. Thus the uniform crude consequence used by the debiasing paper is `h_n-g_n=O(n^(-alpha/2))`. Result 3(iii)--(iv) gives exactly the two facts needed in Theorem 1 of the debiasing paper:

- writing the degree-`n` Bernstein coefficients as `a(n,k),b(n,k)` gives `0<=a<=b<=1` and `g_n<=f<=h_n`;
- after degree elevation, `g_m preceq_n g_n` and `h_m succeq_n h_n`. In coefficient form these are the hypergeometric inequalities quoted as the debiasing paper's (3)--(4). Hence `H_n(m,k)<=a(n,k)` and the corresponding upper inequality really are supported, not merely pointwise monotonicity.

The converse in Result 3 needs `h_n-g_n -> 0` pointwise and gives a stopping simulation. HNP's fair-coin setting changes Result 3(ii) from integer Bernstein event counts to dyadic multiples (`ii'`, physical p. 4); Lemma 9 fills between b-adic degrees and says that this dyadic condition can be restored with an exponentially small added gap.

## Proof-chain check

HNP §5 is not a bare citation: it constructs b-adic approximants `f_n`, first keeps their Bernstein coefficients in a fixed interior interval (physical pp. 19--20), then sets

`g_n=f_n-D B_n(phi_n)`, `h_n=f_n+D B_n(phi_n)`

with `phi_n=theta_alpha n^(-alpha)+[x(1-x)/n]^(alpha/2)` (physical p. 21, (47)--(48)). Lemma 25 gives the gap order. The coefficient domination at physical p. 24 completes the required increasing/decreasing Bernstein-order consistency. This verifies the dependency used by the debiasing theorem.

For integer smoothness `rho`, the debiasing proof's “may assume rho noninteger” is valid only with the parameter choice made explicit: from `lambda<(rho-1)/2`, choose a noninteger `eta` with `max(3,2lambda+1)<eta<rho`, apply HNP to `C^eta`, and use `lambda<(eta-1)/2`. Without this intermediate `eta`, applying HNP Theorem 8 at an integer exponent would be invalid.

## Verified limits and release consequences

1. **Verified theorem route.** The HNP dependency is adequate for the existence and compatibility/envelope gap assertions used by Koskela et al. The randomized-telescoping proof still separately needs its own hypergeometric identity, power-law survival calculation, and sufficiently-large-start bound; HNP alone does not prove `[0,1]` boundedness of `psi`.
2. **No generic executable construction.** HNP §5 proves existence through `Q_{n,r}`, b-adic choices and constants. Koskela et al. §4 expressly says deriving arrays and a usable initial threshold requires difficult/implicit constants. Therefore the release should not expose “input smooth f -> coefficients/start k” as a runnable general algorithm.
3. **Primitive-randomness/output distinction.** HNP's `ii'` supplies a fair-coin-assisted stopping factory for its own envelopes. The debiased `psi` is a `[0,1]`-valued unbiased estimator; to return a bit needs an independent uniform-threshold step (or separately specified exact fair-bit implementation). Its power-law `L` survival weights generally are not finite dyadic table probabilities. Do not silently identify a bounded estimator, a real-uniform Bernoulliization, and a finite-fair-bit factory.
4. **Cost is still unresolved by this citation.** HNP counts paired p-coin/fair-coin stages in its simulation-rate convention. Koskela's `L` is an independent p-coin count. Neither citation converts the other clock, and HNP's gap rate alone does not prove finite `E[L]` for the debiasing power law. The existing sufficient condition (`rho>5` for a selectable finite mean of that specific law) remains construction-specific.

## Adjudication

**Dependency accepted, with an interface qualifier.** It supports Theorem 1's compatible Bernstein envelopes and uniform rate; it does not independently certify a numerical envelope generator, start threshold, primitive random-bit cost, or a generic operational factory. The finite ledger overlay is therefore admissible only as an exact finite-table audit, not as a proof that arbitrary supplied smooth targets meet HNP/Koskela hypotheses.
