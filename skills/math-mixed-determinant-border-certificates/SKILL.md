---
name: math-mixed-determinant-border-certificates
description: Exactly check the finite rank-one bordering identity for a caller-supplied tuple of rational symmetric matrices in the mixed-determinant construction.
---

# Mixed-determinant bordering identity

For rational symmetric base matrices A_j and border data (a_j, alpha_j), this
tool checks the exact identity used in the mixed-determinant induction:

    p_(d+1,m)(A_1^+,...,A_m^+)
    = (sum alpha_j) p_(d,m)(A_1,...,A_m)
      - sum_j D_j[a_j a_j^*] p_(d,m).

The directional derivative is evaluated exactly from the affine rank-one
update. Input matrices and vectors are JSON rationals expressed as integers or
strings accepted by Fraction.

    python3 scripts/check_border_identity.py examples/d1m2-positive.json
    python3 scripts/check_border_identity.py examples/d1m2-boundary.json

The second input intentionally changes one lower-right expected result and
must be rejected. This finite identity is not a spectrahedral-cone proof, a
hyperbolicity proof, or an implementation of the inductively constructed
pencil. See references/mixed-determinant-border.md.

## 文献复核采用的构件

- [Mixed-determinant rank-one border identity](references/mixed-determinant-border.md)
