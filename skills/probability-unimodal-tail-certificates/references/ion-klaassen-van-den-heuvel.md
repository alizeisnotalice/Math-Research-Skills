# Ion--Klaassen--van den Heuvel source card

## Identified source

R. A. Ion, C. A. J. Klaassen, and E. R. van den Heuvel, *Sharp inequalities of Bienaymé--Chebyshev and Gauß type for possibly asymmetric intervals around the mean*, TEST **32** (2023), 566--601, DOI [10.1007/s11749-022-00844-9](https://doi.org/10.1007/s11749-022-00844-9).

Local source actually read: `Ion_Klaassen_VanDenHeuvel_Sharp_Chebyshev_Gauss.pdf`, arXiv:2208.08813v2, dated 2022-10-10, SHA-256 `fa7a746d63ff91496ea45cf1258842568f20a587ce5bb455ef3fd9b45a4009a6`.  Its absolute local path is intentionally not part of the public package.

The official publisher page confirms the published metadata (24 January 2023; TEST 32, 566--601) and displays the same statements: [Theorem 5.2](https://link.springer.com/article/10.1007/s11749-022-00844-9) Eq. (27) and published Theorem 5.5 Eq. (30).  The local v2 statement was cross-checked directly against that official HTML on 2026-11-26.  The published revision renumbers local v2 Theorem 5.4 as Theorem 5.5; the asymmetric formula is unchanged.

## Exact read locations and admitted interface

| Local arXiv v2 locator | Published locator | Admitted use |
| --- | --- | --- |
| PDF p. 11, Theorem 5.2, Eq. (5.27) | Theorem 5.2, Eq. (27) | sharp one-sided upper bound for a standardized unimodal law, including its two equality laws |
| PDF pp. 11--12, Theorem 5.4, Eq. (5.30) | Theorem 5.5, Eq. (30) | sharp asymmetric two-sided upper bound only when \(\sqrt3\le v\le u\), including its two equality constructions |

`Standardized` here means \(EZ=0\) and \(EZ^2=1\), obtained from a scalar \(X\) with finite mean \(\mu\) and finite **positive** variance \(\sigma^2\) by \(Z=(X-\mu)/\sigma\).  The cited class is a unimodal distribution, with no requirement that the mode be zero or coincide with the mean.  The statements concern closed-tail events and allow the atomic/uniform extremizers displayed in the paper.

## Do not transfer

- Do not apply Eq. (30) below \(v=\sqrt3\), with reversed direct orientation \(u<v\), or with nonpositive thresholds.
- Do not present Eq. (30) as a theorem for arbitrary asymmetric intervals; its stated threshold range is essential.
- Do not use the equality law containing `1/v` at \(v=0\).  Eq. (27) remains stated at zero, but the source equality construction begins at \(v>0\).
- Do not replace the population unimodality assumption by an observed histogram, a kernel-density plot, or finite sample checks.
- The `4/9` factor is not a generic Cantelli improvement: it belongs to the cited unimodal-law classes and threshold regimes.

## Actual dependency boundary

For the one-sided result, the local proof invokes the source's Theorem 5.1 (Vysochanskiĭ--Petunin) after shifting \(W=Z+1/v\), then verifies the extremizers.  The asymmetric improvement is proved in the local Appendix A.2 via Khintchine's unimodal representation and a constrained optimization.  This skill imports the theorem statements and their explicitly supplied equality cases, not a new proof of those dependencies.
