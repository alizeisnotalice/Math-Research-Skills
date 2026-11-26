---
name: math-petal-join-domination-polynomial
description: Exhaustively verify the finite domination-polynomial identity for a clique joined to repeated copies of a small petal graph.
---

# Petal-join domination polynomial

Use this skill to verify, on small finite instances, the domination polynomial of `J_m=K_a ∨ mB`.  It compares direct subset enumeration with the identity

`D(J_m,x) = (1+x)^(a+b*m) - (1+x)^(b*m) + D(B,x)^m`,

where `b=|V(B)|`.  This is a finite identity checker, not a locator or asymptotic bound for complex roots.

## Procedure

1. Give the simple graph `B` by `n` and zero-based edges, and choose nonnegative `a,m` with `a>=1`.
2. Run `scripts/check_petal_join.py`.
3. Preserve the direct and formula coefficient lists, plus the command, as the finite certificate.
4. If using a transformed root equation, separately state its substitution and nonvanishing domain; this script does not certify root locations.

## Boundaries

- Enumeration costs `2^(a+m*b)` and is for small cases.
- A coefficient identity does not imply the source's domination-root asymptotics or spectral-radius claims.
- Inputs are checked for simple-graph validity.

## Source

See `references/repeated-petal-domination-identity.md`, distilled only from the printed repeated-petal join identity and not from root estimates.

## 文献复核采用的构件

- [Source note: repeated-petal joins](references/repeated-petal-domination-identity.md)
