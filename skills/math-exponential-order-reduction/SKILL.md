---
name: math-exponential-order-reduction
description: Compute and verify the finite extended-order reduction used for pairwise-coprime equations a^x+b^y=c^z before any logarithmic or gap-principle argument.
---

# Exponential-equation order reduction

For pairwise-coprime integers \(a,b,c>1\) and a divisor \(d>2\) of \(c\), define \(e_d(u)\) as the least positive exponent with \(u^{e_d(u)}\equiv\pm1\pmod d\). Set
\[
g=\gcd(e_d(a),e_d(b)),\quad A=a^{e_d(a)/g},\quad B=b^{e_d(b)/g}.
\]
The source lemma gives an exact exponent rescaling between positive solutions of \(a^x+b^y=c^z\) and those of \(A^X+B^Y=c^z\).

```sh
python3 -B scripts/order_reduce.py 2 3 13 13
python3 -B scripts/order_reduce.py 2 3 5 5 --solution 1 1 1
```

The script computes finite residue orders and, for a supplied solution, checks original and rescaled equations exactly. It neither counts all solutions nor supplies the source's logarithmic bounds or gap principle.

## 文献复核采用的构件

- [Extended-order reduction before the gap argument](references/miyazaki-pink-order-reduction.md)
