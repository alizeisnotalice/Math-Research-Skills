# Binary-form unit-solution count with an explicit discriminant gate

**Source and version.** Shabnam Akhtari, *Representation of Unity by Binary Forms*, arXiv:1011.4507v1, physical pp. 1--2. The local source is SHA-256 `e238d7b3ae58b53b26d23e3c0d30001ff610ac46e9b5674cd379c1a42daf6942`. The article appeared in *Transactions of the American Mathematical Society* 364 (2012), 2129--2155, DOI [10.1090/S0002-9947-2011-05507-8](https://doi.org/10.1090/S0002-9947-2011-05507-8).

For an integral homogeneous binary form \(F\) of degree \(n\geq3\), the source's Theorem 1.1 applies when \(F\) is irreducible and
\[
 |\operatorname{Disc}(F)|>D_0(n)=2^{22}(n+1)^{10}n^n.
\]
It bounds the number of classes of integer solutions to \(|F(x,y)|=1\) by \(11n-2\), where \((x,y)\) and \((-x,-y)\) are one class. Its signature refinement is source-specific and is not produced by the checker.

Run `scripts/check_binary_form_unit_bound.py` on descending coefficients of \(F(x,1)\). It uses exact integer factorization over \(\mathbb Q\) and an exact polynomial discriminant. A positive result checks the finite algebraic premises of the cited theorem. It does not enumerate the solutions or reprove the theorem's geometry-of-numbers and logarithmic-form argument.

```sh
python3 scripts/check_binary_form_unit_bound.py examples/akhtari-binary-form-positive.json
python3 scripts/check_binary_form_unit_bound.py examples/akhtari-binary-form-boundary.json
```
