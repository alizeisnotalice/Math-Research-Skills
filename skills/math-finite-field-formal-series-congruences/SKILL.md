---
name: math-finite-field-formal-series-congruences
description: Verify finite coefficient windows for elementary formal-series fixed points over a prime field, with explicit truncation boundaries.
---

# Finite-field formal-series congruences

Use this tool when a proposed formal-power-series identity over `F_p` must be checked coefficient-by-coefficient on a **finite** window.  It is a verifier for the displayed recurrence; it does not identify OEIS sequences or promote a finite check to an infinite theorem.

## Procedure

1. State the prime `p`, the cutoff `N`, the recurrence, and the requested conclusion.
2. Run `scripts/check_frobenius_fixed_point.py --prime p --cutoff N` for the canonical recurrence `F=x+F(x^p)`.
3. Treat its output as exact arithmetic modulo `p` through degree `N` only.  For an infinite assertion, separately supply the x-adic uniqueness argument and verify its hypotheses.
4. Record the command, parameters, and output.  Do not label a matching prefix a proof of an unrelated generating-function identity.

## Boundaries

- The script accepts only a prime modulus and a nonnegative finite cutoff.
- Its canonical support statement is the recurrence consequence `a_n=1` exactly when `n` is a power of `p` (including `p^0=1`) within the requested range.
- Frobenius and x-adic uniqueness are mathematical lemmas, not a substitute for checking the defining functional equation of a named sequence.

## Source

See `references/hanna-frobenius-xadic-congruence.md`.  The source prints the characteristic-two Frobenius, x-adic uniqueness, and power-of-two support lemmas; this skill deliberately retains only a finite, typed verifier.

## 文献复核采用的构件

- [Source note: Frobenius and x-adic fixed points](references/hanna-frobenius-xadic-congruence.md)
