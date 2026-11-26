# Mod-p-cubed binomial master formulas (EXT-0065)

Verified source: arXiv:1407.0636v6, local SHA-256 `3cfa52090a1adf1b2b963a43455b0a58a89662f922df2a45ce4e64caff7e3d11`, 30 physical pages.

Physical p.5, Theorem 2.1 states that, for `p>3` and `a in Z_p` with `a not ==0 (mod p)`, the complete binomial sum is congruent modulo `p^3` to `(-1)^{<a>_p}+(a-<a>_p)(p+a-<a>_p)E_{p-3}(-a)` (and its displayed alternate Euler-polynomial form). Its proof writes `a=<a>_p+pt`, uses the source's previous finite-sum relation, and converts alternating power sums through Euler/Bernoulli polynomial identities.

Physical p.18, Theorem 4.1 handles the distinct kernel `(2k-1)^-1`, requiring `a` avoid `0,-1,+/-1/2 mod p`. The proof explicitly decomposes that kernel into the p.18 displayed rational expression, combines Theorem 3.1 and Lemma 4.2, and only then specializes (e.g. `a=-1/4`). Keep every exclusion and imported identity as a dependency; neither formula is a generic p-adic interpolation rule.
