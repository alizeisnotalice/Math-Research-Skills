# M. A. A. Boon, O. Boxma, and E. M. M. Winands (2014), “On Open Problems in Polling Systems”

- Source: Queueing Systems 68, 365–374 (2011), DOI https://doi.org/10.1007/s11134-011-9247-9; the local manuscript is arXiv:1408.0142v1 (posted 2014, manuscript dated January 2011). Local PDF: `evidence/fulltexts/R01.pdf` (9 pages; SHA-256 `8071919c7b7182597728c1d6fde6ec33ee675457af9dc472a7e64a023fa34b93`).
- Reading status: full text, all 9 PDF pages.
- Direct relevance: A007, general renewal arrivals under large switch-over times.

## Exact problem statement

Section 4.2, Conjecture 4.2 (PDF p. 5) states that a cyclic polling system with general renewal arrival processes converges to a deterministic limit as the deterministic switch-over times become large. Open Problem 2 (PDF p. 7) asks for a rigorous proof of Conjecture 4.2. The article distinguishes the Poisson-arrival large-switch-over result, where the scaled waiting time has a uniform limit on a known interval, from the general-renewal case. The conjecture applies to the stated cyclic polling context and branching-type service disciplines; do not broaden it without rechecking assumptions.

The accompanying proof idea is explicitly heuristic: it uses a law-of-large-numbers argument and does not resolve dependence between visit periods. The article reports numerical phase-type evidence, which is not a proof.

## Migration gap for A007

The generalized question in the formal dossier asks for a steady-state/fluid limit and the induced candidate waiting-time law. The source’s conjecture is a convergence statement, not an established theorem giving every such scaled law for arbitrary renewal input. A proof must augment the state by renewal ages/residual lives and control their evolution at random polling times, establish tightness and interchange of stationary and large-switch-over limits, and verify the load/service-discipline assumptions.
