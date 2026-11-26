---
name: math-parameterized-norm-form-certificates
description: Verify the published solution families of the Bajpai--Bennett cubic norm-form equation and the Bennett--Ghadermazi extremal cubic Thue equation at supplied integer parameters.
---

# Parameterized cubic norm-form certificates

For an integer \(t>1\), verify the two displayed solutions of
\[
x^3-(t^3-1)y^3+3(t^3-1)xy+(t^3-1)^2=\mathord\pm1.
\]
The exact checker evaluates the polynomial at \((t^2,2t)\) and
\((t^2,-t)\), and rejects parameters outside the theorem's domain.

```sh
python3 -B scripts/check_bajpai_bennett_norm_form.py 2
```

The complete classification follows from the published theorem and its
linear-form and finite-exponent reduction.  The checker certifies the supplied
families only.  It does not search all integer pairs or turn the source method
into a general norm-form solver.  Read [the source scope](references/bajpai-bennett-norm-form.md)
when relying on completeness.

For the distinct Bennett--Ghadermazi family, supply its exact binary cubic,
right-hand side 1, and integer parameter. Use [the extremal cubic Thue source](references/bennett-ghadermazi-extremal-cubic-thue.md).
The checker evaluates five displayed families and the exceptional pair `(6,-5)`
at `t=-1`. The source theorem supplies completeness for those exact inputs.
