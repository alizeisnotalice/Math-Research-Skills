# Scoped 3-adic algebraic-square witness

**Scoped reference.** This is a finite checker for a *supplied* algebraic
square witness in a small quotient of `Z/(3^e)[X]`; it is not an integer
factorization procedure.

## Source and locus

Y. Cai, V. Gupta, Y. Jiang, C. Liaw, A. Mehta, G. Velegkas, and D. Wang,
*Unconditional Integer Factorization in Time* `L_N[1/3, O(1)]`, Cogentic
release PDF, SHA-256
`9ac07593ca90c0f315af0b0214320823a43e7c905e6700948261ebb09a4d537d`,
54 physical pages.  Section 5, **Lemma 5.2, “Deterministic 3-adic
Newton–Hensel algebraic square root,” physical pp. 43–44**, constructs and
checks a bounded representative `beta_hat(X)` in an unramified quotient with
irreducible reduction modulo 3.  The continuation on physical p. 44 states
the exact verification step: reduce `beta_hat(X)^2` against the supplied
polynomial and compare it to the target; return the candidate on success and
`NOT_SQUARE` otherwise.  It also records the unit/residue and bounded
representative conditions needed in that construction.

## Admissible finite interface

For a deliberately small, explicit instance provide:

- a monic polynomial `f` with degree 2 or 3 whose reduction has no root over
  `F_3` (therefore it is irreducible in these degrees);
- an exponent `e >= 1`, a coefficient bound, a candidate `beta`, and a
  target `gamma`;
- all polynomials as coefficient lists in increasing power order.

The checker verifies, using only integer modular arithmetic, that

\[
 \beta^2 \equiv \gamma\pmod{(f,3^e)},
\]

that the listed representative is within its supplied bound, and that the
candidate is a nonzero residue in the finite field quotient modulo 3.  On the
optional tiny enumeration it independently counts every residue-class square
root, so an assertion that the exhibited roots are exactly `beta` and
`-beta` is a finite certificate for that input only.

Run:

```sh
python3 scripts/check_cogentic_3adic_square.py examples/cogentic-3adic-square-valid.json
python3 scripts/check_cogentic_3adic_square.py examples/cogentic-3adic-square-invalid.json
```

The valid fixture uses `f=X^3+2X+1`, whose reduction has no root in `F_3`,
and modulus `9`; the checker exhaustively inspects its `9^3=729` residue
classes.  The invalid fixture changes the target constant coefficient and is
rejected as a square witness.

## Boundary

This add-on is intentionally distinct from the installed **Dixon square-root
transcript** (Lemma 5.3, physical p. 44: masks and a conditional splitting
probability), from supplied-exponent `gcd` splitting, and from primality or
prime-sieve certificates.  It neither finds a relation, performs a split,
returns factors, nor establishes the asymptotic complexity claim.  The
source's general Newton--Hensel construction has additional parameters and
proof obligations; retain them when using that construction rather than
promoting this bounded finite checker to a general routine.

[固定版论文](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/integer_factorization/paper.pdf)。
