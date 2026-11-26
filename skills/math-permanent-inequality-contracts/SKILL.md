---
name: math-permanent-inequality-contracts
description: Audit finite permanent inequalities for stochastic matrices and symmetrizable inverse M-matrices, retaining each source theorem's hypotheses and equality scope.
---

# Permanent inequality contracts

Use this skill when a proposed argument invokes one of the three permanent inequalities documented below.  Keep the matrix class, normalization, and source status explicit; none of the references licenses an inequality for an arbitrary nonnegative matrix.

For a finite rational matrix asserted to be a positively diagonally symmetrizable inverse M-matrix, run the exact checker before using the Koteljanskii conclusion.  The checker certifies only the supplied finite instance; it does not prove the Gaussian/FKG theorem from which the general result follows.

```sh
python3 scripts/check_koteljanskii_inverse_m.py examples/positive-2x2.json
```

Read the matching source contract before use:

- [Entropy averaging and the van der Waerden lower bound](references/sra-entropy-averaging-vdw.md)
- [Gamma-normalized Brégman--Minc bound](references/sra-bregman-minc-gamma.md)
- [Koteljanskii inequality for symmetrizable inverse M-matrices](references/sra-koteljanskii-inverse-m.md)
