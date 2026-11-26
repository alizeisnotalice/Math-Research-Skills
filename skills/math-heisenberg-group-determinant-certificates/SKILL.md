---
name: math-heisenberg-group-determinant-certificates
description: Exactly compute the finite group-determinant matrix of a supplied sparse element of the order-125 Heisenberg group, with a replay for one documented witness.
---

# Finite H5 group-determinant certificate

This is an exact finite computation for the order-125 Heisenberg group with
coordinate product (a,b,c)(A,B,C)=(a+A,b+B,c+C+b*A) modulo 5.

It has one embedded source witness, 1+x+y+y^2+xy^2, and uses fraction-free
integer elimination on the literal 125 by 125 group-determinant matrix:

    python3 scripts/check_h5_witness.py
    python3 scripts/check_h5_witness.py --zero

The first is the documented positive finite identity; the second is a
boundary case and must return determinant zero. The script does not establish
a spectrum classification, a least-value claim, or any cyclotomic/5-adic
theorem. See references/h5-witness.md.

## 文献复核采用的构件

- [Order-125 Heisenberg group determinant witness](references/h5-witness.md)
