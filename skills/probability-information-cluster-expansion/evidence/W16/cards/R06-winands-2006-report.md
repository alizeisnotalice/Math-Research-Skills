<!-- Reader: W15; full report PDF read; review pending. -->
# E. M. M. Winands (2006 report; journal version 2011), “Branching-type Polling Systems with Large Setups”

- Read copy identity: Eindhoven University of Technology SPOR-Report 200616, dated 6 December 2006; 17-page repository PDF `evidence/fulltexts/R06.pdf`, SHA-256 `db52e247f57f466491394f5049de27ee1aa8f0b801c0a938da791345e8cbf10c`. W15 read this report’s 17 pages, including its repository cover, appendix and references.
- Distinct journal record: *OR Spectrum* 33(1), 77–97 (2011), published online 2009, DOI [10.1007/s00291-009-0174-7](https://doi.org/10.1007/s00291-009-0174-7); the [VU publication record](https://research.vu.nl/en/publications/branching-type-polling-systems-with-large-setups/) verifies the journal metadata. Do not label the local 2006 report as the 2011 journal PDF.
- Model: cyclic `N`-queue polling system, independent Poisson arrivals, service times with the stated finite moments, total load `ρ<1`, and nonidling branching-type service disciplines. Property 2.1 (PDF p. 4) requires that each type-`i` customer present at the start of a visit is independently replaced by a random customer population with PGF `hᵢ`; the exhaustiveness is `Φᵢ=1−∂ᵢhᵢ(1)∈(0,1]`.

## Theorems and limits

For deterministic setups, Theorem 3.3 (PDF pp. 7–9) takes total setup `S→∞` with fixed setup ratios and gives a uniform limit for `Wᵢ/S`. In the source notation its endpoints are

`Wᵢ/S ⇒ [(1−ρᵢ)/(1−ρ)] Uᵢ`, where `Uᵢ` is uniform on `[(1−Φᵢ)/Φᵢ, 1/Φᵢ]`.

The policy enters through `Φᵢ`; the theorem also derives limiting queue-length and moment statements. The proof uses the multitype branching/offspring PGFs and a waiting-time LST decomposition, expands the transforms under `S→∞`, and recognizes the limit transform as uniform.

Theorem 3.10 (PDF pp. 10–11) is a separate **ordered two-stage limit** for general stochastic setups: first `ρ↑1` in the heavy-traffic regime, then mean setup `[S]→∞`, with finite first and second setup moments. It gives

`(1−ρ)Wᵢ/[S] ⇒ (1−ρᵢ) Uᵢ`, where `Uᵢ` is uniform on `[(1−Φᵢ)/Φᵢ, 1/Φᵢ]`.

This does not prove a stochastic-setup, fixed-`ρ` limit as setup scale alone tends to infinity. Section 4’s numerical experiments with non-Poisson/renewal arrivals are evidence for a conjecture only; they do not prove the general-renewal extension.

## Full-text map

| Section | PDF pages | Coverage |
|---|---:|---|
| Repository cover and report title page | 1–2 | Identifies the 2006 report/version and abstract. |
| §1, Introduction | 3–4 | Polling background and branching-type scope. |
| §2, Model description and notation | 4–6 | Arrivals, service, setup, Property 2.1 and exhaustiveness. |
| §3.1, Preliminaries | 6–7 | Offspring PGFs and discipline examples. |
| §3.2, Deterministic setups | 7–10 | Large deterministic-setup delay and queue-length limit theorems. |
| §3.3, General setups under heavy traffic | 10–11 | Ordered heavy-traffic then large-mean-setup limit. |
| §4, Discussion and extensions | 12–15 | Applications, simulations, comparisons and open extensions. |
| Appendix A and references | 15–17 | Phase-type fitting details and bibliography. |

## Transfer limit

The branching replacement property, Poisson arrivals, and the stated deterministic or ordered heavy-traffic setup regimes must be checked before using the limits. The report does not prove the general-renewal A007 conjecture or a fixed-load stochastic-setup fluid law.
