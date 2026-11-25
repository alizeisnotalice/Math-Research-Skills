# Adaptive positive-certificate budget

Use this component to bound the expected number of successful transactions that separately certify one increasing Boolean event. It is a finite product-space lemma. It does not give a prophet inequality, a competitive ratio, an optional-stopping theorem, a result for correlated inputs, or a certificate bound that reuses earlier positive answers.

## Pinned, checked source

OpenAI, *One Sample Suffices for Matroid Prophet Inequalities against an Almighty Adversary*, 23 September 2026, Family 111, Lemma 4.1 ("Disjoint-query certificates"), PDF p. 12 (printed p. 12 of 27). The audited PDF has SHA-256 `4bcbebba491320129402440fc3892ec876a04b3afb933305b214e9341d953c7e`; the pinned copy is [OpenAI math commit `3344da59991ed94f9ba711217b29c1d760badfa6`](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/final.pdf).

The local evidence locator is `.local/literature-distillation/openai-inventory.jsonl` (Family `111`); its page extraction is `/Volumes/data/CodexTemp/Math-Research-Skills/openai-corpus.gruR7ANo/pages/4bcbebba491320129402440fc3892ec876a04b3afb933305b214e9341d953c7e.json` (SHA-256 `1c9841a47b42d4dc760680fc27fdb6ab4fc8529d8e4f8efbebd7d0821d784a60`). The inventory records scholarly review as pending. This card audits only Lemma 4.1, not the paper's matroid-prophet results.

## Exact interface

Let `V0` be finite and let its coordinates be independent Bernoulli variables, with arbitrary individual Bernoulli laws. Let `A ⊆ 2^V0` be increasing and write

\[
\delta=\mathbb P(A^c)>0.
\]

An adaptive procedure queries coordinates, partitioning its queries into transactions. The next coordinate, transaction boundaries, and stopping decisions may depend on the revealed transcript and on an auxiliary random seed independent of all Bernoulli bits. It must satisfy all of the following.

1. No coordinate is queried more than once.
2. There is a deterministic finite upper bound on the number of transactions.
3. A transaction is called successful only when the coordinates returning one **within that transaction itself** form a positive certificate for `A`: setting those coordinates to one forces `A` regardless of every other coordinate.

Then, with `N_success` the number of successful transactions,

\[
\mathbb E N_{\mathrm{success}}\le \log(1/\delta),
\]

where `log` is natural logarithm.

### Conditional and stopping boundary

The source conditions first on the independent auxiliary seed. Under any possible query transcript, coordinates not yet queried retain their joint original product law, because the transcript fixes values only at predictably selected coordinates. Thus a conditional application after an entry transcript is valid only after freezing that transcript, identifying the remaining finite coordinate set and a fixed increasing event for its conditional experiment, and establishing its conditional product law and failure probability `δ`.

Adaptive stopping is included only in the finite form above: there are at most `|V0|` queries and a deterministically bounded number of transactions, so stopped paths are padded with zero increments before summing conditional identities. This card does not license an unbounded-transaction limit, a stopping-time passage, or conditioning on information that destroys the product law.

## Proof mechanism to retain in an audit

For a remaining set `V`, let `p(V)` be the failure probability when already removed coordinates are set to zero. In the current transaction, if `I` is its currently observed positive set, let `p_I(V)` additionally force `I` to one and set

\[
Z=p_I(V)/p(V).
\]

The source's one-coordinate conditional calculation bounds the expected decrement of `Z` by the increment of `log p(V)`. At a successful transaction end, its positive certificate forces `p_I(V)=0`, so the success indicator is bounded by the transaction's net decrement. Reset `I` between transactions but retain the depleted `V`; the logarithmic increments telescope from `log δ` to at most zero. The transaction-local certificate condition is exactly what makes this reset legitimate.

## Exact local replay

We ran the following finite enumeration locally. Take four independent fair bits, `A={there is at least one 1}`, and four one-query transactions, with transaction `i` successful exactly when bit `i` is one. A single positive bit is a certificate for `A`, each coordinate is queried once, and `δ=1/16`. Enumeration gives total successful transactions `32` over `16` outcomes, hence `E N_success=2`, while `log(1/δ)=log(16)≈2.772588722239781`.

```bash
python3 - <<'PY'
from fractions import Fraction
from itertools import product
from math import log

n = 4
outcomes = list(product((0, 1), repeat=n))
successes = sum(sum(x) for x in outcomes)
mean = Fraction(successes, len(outcomes))
delta = Fraction(1, 2**n)
print(f'n={n}; |Omega|={len(outcomes)}; delta={delta}; total_successes={successes}')
print(f'E[number_successes]={mean}; log(1/delta)={log(1 / float(delta)):.15f}')
PY
```

This is an exact finite check of the interface, not a proof beyond the cited lemma.
