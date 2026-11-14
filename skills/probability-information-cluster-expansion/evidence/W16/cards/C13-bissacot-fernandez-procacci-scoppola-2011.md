<!-- Reader: W15; full-text read of shared D01 arXiv v2 PDF; review pending. -->
# Rodrigo Bissacot, Roberto Fernández, Aldo Procacci, and Benedetto Scoppola (2011), “An Improvement of the Lovász Local Lemma via Cluster Expansion”

- Source: *Combinatorics, Probability and Computing* 20(5), 709–719 (2011), DOI [10.1017/S0963548311000253](https://doi.org/10.1017/S0963548311000253); arXiv:0910.1824v2 (26 March 2010).
- Read copy: `evidence/fulltexts/C13.pdf`, 10 PDF pages, SHA-256 `644f3e1331a2945188901fdf7a89195b455e0a6173e12488405b719206138ca1`. W15 read pp. 1–10, all sections and appendix.
- Title-page author order in the actual PDF is Rodrigo Bissacot, Roberto Fernández, Aldo Procacci, Benedetto Scoppola. This corrects prior inventory author-name errors.

## Full-text coverage and result

| Source section | PDF pages | What the source does |
|---|---:|---|
| 1, Introduction | 1–2 | Explains the Shearer/independent-set polynomial/hard-core gas connection and the cluster-expansion route. |
| 2, Results | 2–5 | Recalls the classical LLL and Shearer theorem, gives the hard-core partition-function formulation, Proposition 3, cluster-expansion Theorem 4, improved LLL Theorem 5, and lopsidependency Theorem 6. |
| 3, Applications | 5–8 | Applies the criteria to independent transversals, Latin transversals, and (k)-SAT. |
| Appendix | 8–9 | Proves the key partition-function/cluster-series implication around equation (2.19), using a positive series and fixed-point majorants. |
| References | 10 | Bibliography. |

Theorem 5 assumes a finite family of events with a dependency graph (G), event probabilities (p_x), and nonnegative parameters (mu_x) satisfying
\[
p_x\le \frac{\mu_x}{\phi_x^*(\mu)},\qquad
\phi_x^*(\mu)=\sum_{R\subseteq\Gamma^*(x): R\text{ independent}}\prod_{y\in R}\mu_y.
\]
Here `Γ^*(x)` is the closed neighborhood. The probability exponent is a different polynomial over the open neighborhood,
\[
\widetilde\phi_x^*(\mu)=\sum_{R\subseteq\Gamma_G(x): R\text{ independent}}\prod_{y\in R}\mu_y,
\qquad \phi_x^*(\mu)=\mu_x+\widetilde\phi_x^*(\mu).
\]
The exact Theorem 5 conclusion (PDF p. 4, Eq. (2.19)) is
\[
\Pr\!\left(\bigcap_{x\in X}\overline{A_x}\right)\ge
\prod_{x\in X}(1-p_x)^{\widetilde\phi_x^*(\mu)}>0.
\]
Replacing `\widetilde\phi_x^*` in the conclusion by the closed-neighborhood `\phi_x^*` gives a weaker consequence because `0<1-p_x≤1`, but it is not the theorem’s displayed exponent. The lopsided version requires a valid lopsidependency graph. The cluster-expansion criterion is a comparison tool only after the events, dependency graph, and required polymer/hard-core representation are actually supplied.

The appendix proof of (2.19) (PDF pp. 8–9) uses the rooted positive cluster series `Π_x`: its logarithmic-derivative identity is `−∂_{ρ_x} log Z_G(−ρ)=Π_x(ρ)`. Equation (A.1) bounds the logarithm of the partition function through its negative-activity value; (A.2)–(A.4) express the partition-function ratio via an integral of the series `Σ_x(ρ)`. Proposition 10 supplies a positive convergent majorant and fixed-point comparison: the map `T_x^ρ` in (A.5) and relation (A.6) bound `Π_x(ρ)` by `\widetilde\phi_x^*(\mu)/(1−ρ_x)`. Integrating this open-neighborhood exponent yields the stated product bound. The closed-neighborhood polynomial appears in the admissible-radius/condition, while the majorant gives the open-neighborhood polynomial in the probability exponent.

## Transfer boundary

The theorem concerns avoidance probabilities for finite event systems, not channel capacity or an adaptive bandit. No verified polymer representation of the optimized deletion-channel information rate is available in this dossier. Thus C13 cannot certify convergence of the B051 capacity expansion by itself.
