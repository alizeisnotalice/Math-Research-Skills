# Exact even-k paired-basis reflection

`check_even_reflection.py` verifies the finite count-LP interface in the
four-page source `f8669d7c...` (physical pp. 1--3), after the paired
dual-feasible-basis gate was checked in Berend--Ernst--Kontorovich--Kumar,
*Journal of Theoretical Probability* 39, article 58 (2026), Theorem 3.3. [反射预印本](https://arxiv.org/abs/2609.25595) · [正式发表的上游定理](https://doi.org/10.1007/s10959-026-01487-4)

Run the positive certificate:

```sh
python3 -B scripts/check_even_reflection.py examples/even-reflection-n11-k4-p13.json
```

It uses only exact `Fraction` arithmetic.  The checker requires an interior
rational `p`, even `k`, a supplied disjoint set of adjacent pairs in
`{0,...,n-1}`, and endpoint `n`.  It solves the `k+1` binomial-moment equations
on the supplied basis, checks

`w_{n-1-s}^{I*}(1-p) = p(n-s)/((1-p)(s+1)) w_s^I(p)`,

and verifies the paired dual polynomial on every integer count node.  Thus its
optimality conclusion is limited to the two supplied feasible finite bases.
It does not search bases or certify endpoint reflection, equality of objective
values, order/connectedness, or odd-k assertions.

Negative controls must exit `2`:

```sh
python3 -B scripts/check_even_reflection.py examples/even-reflection-invalid-odd-k.json
python3 -B scripts/check_even_reflection.py examples/even-reflection-invalid-nonseparated-pairs.json
```

The exact regression suite checks the published boundary weights as well as
both rejections:

```sh
python3 -B test_check_even_reflection.py
```
