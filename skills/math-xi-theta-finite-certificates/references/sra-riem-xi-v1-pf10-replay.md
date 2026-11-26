# Replayed v1 PF_10 finite layer

Supporting source: Suvrit Sra, *On some positivity properties of the Riemann Xi function*, public author-preprint repository [`suvrit/preprints`](https://github.com/suvrit/preprints), commit `cd53b549a7fd5a7a903e4b3147fef8f4d4b4e39e`, `preprints/riem-xi/v1/code/`.  This is the source's v1 code package; it is not an attachment to v3 and must not be cited as a certificate for the v3 PF_1810540931075 assertion.

All eleven files in the package's `SHA256SUMS` were verified before replay.  The supplied runner was then executed unchanged with Python 3.13.18, `mpmath==1.3.0`, and `sympy==1.14.0`; its four scripts returned zero.  The replay summary hash is `6d1c37f42d0f5c35a5bb8bb6ef848e00b53caae0b61d65bdec71c519c80865f3`; each output log hash equals the corresponding expected `verification_*.txt` hash from the source manifest.  The replay covered scalar directed bounds, exact symbolic Laguerre identities, two log-concavity scalar bounds, eleven Xi endpoint sign enclosures, finite order-2 through order-10 checks, closed central/structured covers, and tail inequalities.  The final PF script printed `ALL LAMBDA PF_10 CERTIFICATES PASSED`.

## Admissible scope

Conditional on the paper's analytic reductions and its external premise that the zeta zeros are verified on the critical line through height `3e12`, this is a reproducible finite arithmetic replay of the v1 PF_10 layer.  It does not independently prove the analytic reductions, re-verify the published height computation, prove RH, detect arbitrary zeros, or establish a result at order above 10.

The v3 local PDF has SHA-256 `d3cd19f47a11051eb024ca7f81e9f7c799c1e407ad076a3f3854975873fdcab4`; its physical pp. 50 and 53 describe a different order-256 certificate with 270 selected zeros and a 683-piece cover.  The pinned public v3 path contains no corresponding selected indices, Arb data, directed outputs, signed matrices, cover list, or audit.  Consequently this v1 record must never be used to infer v3's PF_1810540931075 conclusion.
