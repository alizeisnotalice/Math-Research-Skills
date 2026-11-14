<!-- Card revision: W15; source originally fully read in the earlier W16 batch. -->
# Roberto Fernández and Aldo Procacci (2007), “Cluster Expansion for Abstract Polymer Models: New Bounds from an Old Approach”

- Source: *Communications in Mathematical Physics* 274, 123–140 (2007), arXiv:math-ph/0605041v2. Local PDF: `evidence/fulltexts/C03.pdf` (16 pages; SHA-256 `12cccb408b6810f1808f8ccde3f418f37020a2edd4b4bc5b86217d5ceccb0b3a`).
- Reading: full paper, PDF pp. 1–16. This revision corrects the source ID from the prior misnamed `C04` card.
- Scope: hard-core abstract-polymer partition functions; a sufficient convergence criterion, not an unrestricted series test.

## Result and assumptions

The polymer set (P) is countable with a simple incompatibility graph; the model uses nonnegative activities ρ and the hard-core rule. For each root polymer γ₀, let (N^*_{\gamma_0}) be its closed incompatible neighborhood and let \(\Xi_{N^*_{\gamma_0}}(\mu)\) be the finite-subset partition polynomial summing only mutually compatible polymers in that neighborhood, with activities μ. Theorem 1 (PDF pp. 5–6, printed p. 5) states that if μ≥0 satisfies, **for every** γ₀∈P,
\[
\rho_{\gamma_0}\,\Xi_{N^*_{\gamma_0}}(\mu)\le \mu_{\gamma_0},
\]
then the rooted cluster series \(\Pi_{\gamma_0}(\rho)\) converges and \(\rho_{\gamma_0}\Pi_{\gamma_0}(\rho)\le\mu_{\gamma_0}\). The neighborhood polynomial only includes mutually compatible neighbors; this is the improvement over a product over all incompatible polymers.

The proof represents the connected-graph coefficients through the Penrose partition identity, bounds the resulting tree terms using the compatibility restrictions (PDF pp. 14–15), and compares the result with Dobrushin/Kotecký–Preiss criteria. Theorem 4 (PDF pp. 7–8, printed p. 7) gives monotone iteration: if (T_\rho(\mu)\le\mu), iterates from ρ increase to a fixed point and remain bounded above by iterates from μ and by μ. This is a convergence certificate under the displayed hypotheses, not global optimization of an arbitrary series.

## Transfer limit

No hard-core polymer encoding or activity bound uniform in B051’s input block length and run tails has been established. Even if such a representation were found, one would still need to justify passage through the entropy-rate limit and supremum over input laws.
