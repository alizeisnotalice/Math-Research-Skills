---
name: math-weil-deligne-purity-lfactor
description: Certify the local L-factor half-plane and Frobenius determinant consequence of supplied pure weight-zero Frobenius-semisimple Weil–Deligne data. Use only after the Weil–Deligne representation, inertia invariants, and purity witnesses have been established externally.
---

# Pure Weil–Deligne local-factor certificate

Use this skill for the narrow local consequence of a *supplied* finite-dimensional Frobenius-semisimple Weil–Deligne pair `(r, N)` over a local function field of residue cardinality `Q`, when a monodromy-weight purity certificate is already available.  It does not construct a parameter, calculate inertia invariants, or prove purity or temperedness.

For the convention
\[
L(s,(r,N))=\det(1-Q^{-s}r(\operatorname{Fr})\mid(\ker N)^{I_k})^{-1},
\]
weight-zero purity implies that this factor is holomorphic and nonzero on `Re(s) > 0`; symmetry of the monodromy filtration implies `|det r(Fr)| = 1`.  Read [the certificate contract](references/purity-lfactor-certificate.md) before representing algebraic spectra as exact modulus-squared witnesses.

Run the finite consistency check only after each listed value has an independent exact provenance:

```bash
python3 scripts/check_purity_lfactor.py examples/positive.json
python3 scripts/check_purity_lfactor.py examples/reject-missing-inclusion.json
```

The second invocation must fail.  A successful run certifies only the stated conclusion from the supplied certificate; it never establishes the global Ramanujan/temperedness theorem, local-global compatibility, genericity, or numerical-to-exact spectral conversion.

## OpenAI 原稿中的方法

- [Conditional local-parameter normalization for imaginary-quadratic modularity](references/openai-arithmetic-2.md)
