---
name: math-order-two-casoratian-audit
description: Audit supplied rational second-order recurrences by exact Casoratian and consecutive quotient identities. It certifies finite identities only.
---

# Exact order-two recurrence / Casoratian audit

Use this tool for two supplied rational solutions of

\[
  a_n u_{n+1}=b_nu_n+c_nu_{n-1}\qquad(n\geq1).
\]

It computes every displayed quantity with `fractions.Fraction`.  With
\(W_n=u_nv_{n+1}-u_{n+1}v_n\), the source-derived finite identity is

\[
 W_n=-\frac{c_n}{a_n}W_{n-1},\qquad
 \frac{v_{n+1}}{u_{n+1}}-\frac{v_n}{u_n}
 =\frac{W_n}{u_nu_{n+1}},
\]

where the second equality is reported only when both displayed denominators are
nonzero.  The input gives a finite list of `a`, `b`, `c`, and two pairs of
initial values.  It is not a recurrence finder, an asymptotic solver, or an
irrationality test.

```sh
python3 scripts/casoratian_audit.py examples/delannoy.json --require-complete-quotients
```

The Delannoy fixture exactly checks the example in the source.  The
`zero-denominator.json` fixture deliberately leaves one quotient unresolved;
with `--require-complete-quotients` it must fail.  This makes an unchecked
division, a finite convergence observation, or a recurrence alone insufficient
to claim a limit or arithmetic property.

## Scope gate

To turn a recurrence into a statement about a target constant, separately prove
all of the following on the claimed infinite range: (1) the proposed sequences
are the required solutions and the normalization identifies their quotient with
the target; (2) every needed denominator is nonzero; (3) any limiting/root
separation claim; and (4) for irrationality, a common integer scaling,
nonzero linear form, and shrinking bound.  This tool establishes none of those
items merely from finite data.

For an already proved integer linear form and uniform height/remainder bounds,
route the resulting data to `math-integer-linear-form-rates`; do not use this
finite auditor as its substitute.

Read [the source note](references/chamberland-straub-casoratian.md) before
transferring the identity to another recurrence.
