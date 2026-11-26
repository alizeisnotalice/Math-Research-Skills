# Finite cyclic-relation certificates

Google Cogentic's *Discrete Logarithms in Finite Fields of Fixed Characteristic in Sub-Quasi-Polynomial Time* uses a relation matrix over \(\mathbb Z/M_L\mathbb Z\) in Lemma 6.3(2), physical pp. 30–31 of the fixed local PDF. Its `SolveModM` performs determinant-one row operations, rejects a nonunit pivot, and derives exponents only after the rows span the required module. The fixed primary source is [Google Research commit 4a7bc8ab0bc7](https://github.com/google-research/google-research/blob/4a7bc8ab0bc7/cogentic_research_papers/discrete_logarithm/paper.pdf).

`check_cyclic_relation_certificate.py` adds the group-level replay that the generic modular checker deliberately omits. It accepts a finite unit group `(Z/group_modulus Z)^*`, an exponent modulus \(M\), a generator \(\gamma\), elements \(\delta_j\), and rows satisfying

\[
\prod_j \delta_j^{A_{rj}}=\gamma^{a_r}.
\]

It checks each supplied element has \(M\)-th power one, checks every displayed group relation, applies the existing exact Bézout row elimination over \(\mathbb Z/M\mathbb Z\), and replays \(\delta_j=\gamma^{y_j}\). If the relation rows span the module, the conclusion also follows by the same row operations. The final replay detects implementation or input mismatches.

This is an offline finite certificate. It does not search for discrete logarithms, infer the group order, establish a relation-sampling probability, verify an elliptic-curve descent, or establish the paper's complexity bound.

```sh
python3 scripts/check_cyclic_relation_certificate.py --self-test
python3 scripts/check_cyclic_relation_certificate.py examples/cyclic-relation-positive.json
python3 scripts/check_cyclic_relation_certificate.py examples/cyclic-relation-bad-relation.json
```
