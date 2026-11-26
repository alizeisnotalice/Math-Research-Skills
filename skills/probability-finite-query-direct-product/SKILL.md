---
name: probability-finite-query-direct-product
description: Verify a finite deterministic, adaptively interleaved query tree against an exact capped direct-product bound for independent Boolean-input tasks.
---

# Finite capped query direct products

Use this skill to audit a *specified finite deterministic decision tree* that solves independent copies of a Boolean query problem. It computes the optimal one-copy success probability exactly and checks the tree's individual query caps and joint success probability by full enumeration.

Use the checker only after fixing a finite domain `D` of equal-length bit strings, a rational probability law on `D`, a Boolean target value, a query budget `L`, and a tree. The tree can query the copies in any adaptive interleaving, but its leaf must output one bit per copy. Run it from this directory:

```bash
python3 scripts/verify_capped_direct_product.py examples/positive.json
```

The proof, schema, and limits are in [the capped direct-product reference](references/capped-query-direct-product.md). In particular, this does not verify quantum query algorithms, non-product input laws, an unbounded or unspecified policy class, or an auxiliary observation that depends on the input copies.
