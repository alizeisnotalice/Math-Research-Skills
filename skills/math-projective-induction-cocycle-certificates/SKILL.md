---
name: math-projective-induction-cocycle-certificates
description: 用有限 Cayley 表和有理相位精确核验图子群上的射影诱导校正、乘子、代表元变换和有限指标维数。
---

# Finite projective-induction certificates

Use this skill when a proposed finite-index graph correspondence supplies finite
groups \(\Gamma,\Lambda\), subgroups \(A,B\), an isomorphism
\(\delta:A\to B\), and projective phase data.  It checks the finite algebraic
interface in the source's Lemma 2.1 before that interface is used in a larger
argument.

1. Encode both groups by complete Cayley tables, phases as rational exponents
   modulo one, and the graph representation phase on \(A\).
2. Run `python -B scripts/check_projective_induction.py examples/c2_graph.json`.
   A valid certificate checks normalization and the cocycle law, graph closure,
   `c(s,tx)c(t,x)=c(st,x)`, the projective transport law, optional changes of
   coset representatives, and the two finite-index dimension counts.
3. Treat `invalid:` with exit 2 as a failed input contract, not as a proof that
   a different choice of representatives cannot work.

See [the finite transfer proof](references/finite-projective-induction.md).
The computation is exact over \(\mathbb Q/\mathbb Z\); it does **not** prove
normality, bifiniteness, ICC hypotheses, or arithmetic rigidity for infinite
groups.  Those require separately supplied analytic hypotheses.
