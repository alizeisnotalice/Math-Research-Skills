---
name: math-rational-logarithm-independence-gate
description: Exactly test whether positive rational inputs have a nontrivial multiplicative power relation, before applying logarithmic-ratio or linear-form results. It does not prove an irrationality exponent or a lower bound.
---

# Positive-rational power-relation gate

Use this skill when a theorem about real logarithms requires positive rational
numbers to be multiplicatively independent (also called `NoPowerRelation`).
It supplies an exact finite test for that hypothesis only.

For positive rationals \(a_1,\ldots,a_n\), form the integer matrix
\(E=(v_p(a_j))_{p,j}\), with one row for every prime appearing in a numerator
or denominator.  A nonzero \(h\in\mathbb Z^n\) satisfies
\(\prod_j a_j^{h_j}=1\) exactly when \(Eh=0\).  Thus the inputs are
multiplicatively independent exactly when `rank(E) == n` over \(\mathbb Q\).

Run the exact checker with canonical positive-rational strings:

```bash
python3 -B scripts/check_positive_rational_power_independence.py 2 3 5/7
```

The JSON output includes the ordered primes, exact integer valuation matrix,
rank, and Boolean conclusion.  Save that output with the theorem application.
Reject zero and negative inputs; a supplied `1` is correctly dependent.

The check does **not** establish a theorem about logarithms, choose a logarithm
branch, evaluate a height convention, or make an ineffective constant
effective.  In particular, it is only a caller-side premise check for the
source results documented in:

- [the irrationality-exponent source premise](references/gregory-chudnovsky-log-exponent-premise.md), and
- [the linear-logarithm-form source premise](references/gregory-chudnovsky-linear-log-form-premise.md).
