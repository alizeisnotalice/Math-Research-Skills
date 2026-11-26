# Static-item-price LP inequality certificate

## Source binding

This card records one finite interface from *Nearly Tight O(log log log m) Prophet Inequalities for Subadditive Combinatorial Auctions*. The first official PDF is the blob `9a43382537bba2b07435ca752093a257541791e4` at Google Research commit `ee4298226f21649f45c0d0427f7c0f3f682d2a20`, 36 physical pages, 807,446 bytes, SHA-256 `ccaae3a13b5307bd9999f57b5abe9840f36b96533bd72de2de44e4ff15fb3e8f`. The current official PDF is the blob `b7304c90b9c5127c7b74ca9121f685567cec5b8f` at commit `3f540f420bfae7e6ce48365a68d0ae003feb2f87`, 36 physical pages, 812,579 bytes, SHA-256 `f49ea5630c1aaead322a0b7f87ac145181af4e86c574df5965cf9e30ba7b31aa`.

The substantive PDF addition is a concurrent-work citation and pagination changes. It does not alter the unequal-marginals definitions, Lemma 2.1, or Proposition 2.2. This component uses current physical pages 6--7, printed Section 2.1 and Lemma 2.1. The public files are [initial PDF](https://github.com/google-research/google-research/blob/ee4298226f21649f45c0d0427f7c0f3f682d2a20/cogentic_research_papers/subadditive_prophet_inequalities/Subadditive_Prophet_Inequalities.pdf) and [current PDF](https://github.com/google-research/google-research/blob/3f540f420bfae7e6ce48365a68d0ae003feb2f87/cogentic_research_papers/subadditive_prophet_inequalities/Subadditive_Prophet_Inequalities.pdf).

## Finite certificate

For a finite item set \(U\), let \(v:2^U\to\mathbb R_{\ge0}\), a cap vector \(q\in[0,1]^U\), and a distribution \(\lambda\in\Delta(q)\) be supplied explicitly. A nonnegative price vector \(p\) and claimed lower bound \(\gamma\) form this local certificate exactly when

\[
p(T)+\sum_{S\subseteq U}\lambda_S\bigl(v(S\setminus T)-p(S)\bigr)\ge \gamma
\qquad\text{for every }T\subseteq U.
\]

The checker verifies the complete value table, probability normalization, marginal caps, price nonnegativity, and every subset inequality using rational arithmetic. It checks the displayed conclusion of Lemma 2.1 for supplied witnesses. It does not solve the minimax LP, prove that \(\gamma=g_v(q)\), construct \(p\) or \(\lambda\), derive the ghost-sample decoupling, or establish the paper's asymptotic \(O(\log\log\log m)\) welfare ratio.

The input also records the buyer arrival order and a fixed tie rule as metadata. These fields prevent a finite price check from being relabeled as a static-price prophet guarantee under a changed order or tie convention.

## Reproduction

Run `python3 scripts/check_static_price_lp_certificate.py examples/cogentic-static-price-single-item.json`. The bundled one-item certificate has \(q=1/2\), \(\lambda(\varnothing)=\lambda(\{0\})=1/2\), \(p_0=1/2\), and \(\gamma=1/4\). Both subset inequalities are equalities. Replacing the price by zero rejects the certificate.
