---
name: math-graph-spectral-moment-certificates
description: Compute adjacency trace moments and short-cycle counts of finite simple graphs, and exact integral circulant spectra and energy by Ramanujan sums.
---

# Finite graph spectral-moment certificates

Use this skill for a supplied finite simple graph when a proof needs exact low trace moments, selected short-cycle counts, or a necessary integral-spectrum test. The checker verifies the adjacency matrix, computes \(\operatorname{tr}(A^2)\) and \(\operatorname{tr}(A^4)\), independently enumerates simple 4-cycles, and checks the associated fourth-moment identity.

For an odd-girth claim, supply `odd_girth`. The checker then verifies the vanishing of lower odd trace moments and compares \(\operatorname{tr}(A^g)\) with \(2g\) times the enumerated simple \(g\)-cycles. This is a finite identity check. It does not prove a graph family classification, a spectral reduction, or the existence of a counterexample.

```sh
python3 -B scripts/check_spectral_moments.py examples/cycle-five.json
python3 -B scripts/check_spectral_moments.py examples/cycle-six.json
```

Read [the source scope](references/sun-graph-trace-moments.md) when using the generalized-sun source. For a claimed integral graph, provide an independent exact characteristic-polynomial or eigenvalue certificate in addition to these trace moments.

For an integral circulant graph specified by its order and a divisor set,
use [Ramanujan sums](references/icg-ramanujan-finite-energy.md) to construct
all integer eigenvalues, then compare their trace moments with adjacency
enumeration and compute its exact energy.
