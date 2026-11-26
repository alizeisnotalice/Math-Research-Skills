---
name: math-finite-cyclic-difference-pv
description: Certify the finite cyclic Picard–Vessiot-ring construction for a caller-supplied finite-order diagonal representation; do not use it to solve general inverse difference-Galois problems.
---

# Finite cyclic difference Picard–Vessiot certificate

Use this only after the caller has supplied a matrix `h` of finite order `m`, a diagonalization
`h = P diag(zeta^e_i) P^-1` with `zeta` primitive of order `m`, and the promised exact base
field `K` containing `zeta`.  Check `gcd(m,e_1,...,e_n)=1` with the included script.

Then the finite construction is `R = K[t]/(t^m-1)`, `sigma(t)=zeta*t`, and
`Z=P diag(t^e_i) P^-1`; it gives `sigma(Z)=hZ`.  Record the diagonalization and the Bezout
certificate: it explains why the entries of `Z` and `det(Z)^-1` recover `t`.

This is a certificate for the finite cyclic branch only.  It does not construct `A(x)` for an
arbitrary algebraic group, prove a general Picard–Vessiot realization theorem, or verify the
paper's coefficient-group and rigidity arguments.  Read
[the source scope](references/finite-cyclic-pv-source.md) before relying on the construction.
