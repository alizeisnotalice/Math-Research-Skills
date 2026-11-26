---
name: math-recurrence-finite-screening
description: Exact bounded residual checks for k-Pell multiplicative dependence, decimal k-Lucas concatenations, and unit-constant two-sided recurrences. Never promotes a finite box to a global recurrence theorem.
---

# Exact finite recurrence screening

Use this skill when a recurrence paper has reduced a problem to an explicit finite residual box, or when a caller supplies a box to inspect.  It uses integer arithmetic only and emits the identities actually found.  It is not a Binet, LLL, Matveev, root-separation, or global-completeness certificate.

## Procedure

1. Fix the recurrence convention and every index bound.  Do not silently change the source's initial values or digit rule.
2. Run `scripts/recurrence_screen.py` with one JSON input:

   ```sh
   python3 scripts/recurrence_screen.py < examples/kpell-source-box.json
   python3 scripts/recurrence_screen.py < examples/klucas-small-box.json
   python3 scripts/recurrence_screen.py < examples/abc-toy-family.json
   ```

3. Save the command, JSON input, interpreter version, output, and the literal finite box.  A zero result means only that box has no hit.
4. For `abc_common_values`, require a monic characteristic polynomial with constant coefficient `+1` or `-1`; this is what makes the displayed two-sided propagation exact over the integers.  It does not establish any specialization, irreducibility, root separation, valuation, or logarithmic-form hypothesis.

## Modes

- `kpell_dependence`: compares exact primitive bases of positive k-Pell terms.  Equal bases are a necessary-and-sufficient integer test for the proper-perfect-power reduction used by the source's finite screen.
- `klucas_concat`: tests `L[n] == L[m] * 10^digits(L[p]) + L[p]` with the source's base-10 digit convention.
- `abc_common_values`: propagates supplied initial values in both directions and groups equal absolute values.

## Boundaries

The program rejects invalid parameter ranges and nonunit constant coefficients.  It does not check the papers' global hypotheses.  In particular, use it to replay a stated residual computation, never to infer an all-index conclusion.

## Sources

- `references/ext-0416-kpell.md`
- `references/ext-0418-klucas.md`
- `references/ext-0395-abc.md`

## 文献复核采用的构件

- [Generalized ABC recurrence finite interface](references/ext-0395-abc.md)
- [k-generalized Pell finite residual screen](references/ext-0416-kpell.md)
- [k-generalized Lucas finite concatenation screen](references/ext-0418-klucas.md)
