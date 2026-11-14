"""Exact bounded rational-factor sanity enumeration for A175.

This is deliberately a rational-factor subcase only; it says nothing about
irrational real coefficient factors or unbounded degrees.
"""
from itertools import product
from pathlib import Path
import json
import sympy as sp

x = sp.symbols('x')
rows = []
total_polynomials = 0
total_nontrivial_splits = 0
nonnegative_rational_splits = 0
nonbinary_nonnegative_splits = []

for degree in range(1, 9):
    for bits in product((0, 1), repeat=max(0, degree - 1)):
        coeffs = [1, *bits, 1]  # low to high: constant and leading coefficient 1
        C = sp.Poly.from_list(list(reversed(coeffs)), gens=x, domain=sp.QQ).as_expr()
        total_polynomials += 1
        _, facs = sp.factor_list(C, x)
        choices = [range(m + 1) for _, m in facs]
        for exponents in product(*choices):
            A = sp.Integer(1)
            for (factor, _), exponent in zip(facs, exponents):
                A *= factor**exponent
            A = sp.Poly(A, x, domain=sp.QQ).monic()
            if A.degree() <= 0 or A.degree() >= degree:
                continue
            B = sp.Poly(C, x, domain=sp.QQ).exquo(A).monic()
            total_nontrivial_splits += 1
            ac = [sp.Rational(v) for v in reversed(A.all_coeffs())]
            bc = [sp.Rational(v) for v in reversed(B.all_coeffs())]
            if all(v >= 0 for v in ac) and all(v >= 0 for v in bc):
                nonnegative_rational_splits += 1
                binary = all(v in (0, 1) for v in ac + bc)
                if not binary:
                    nonbinary_nonnegative_splits.append({
                        'C': str(C), 'A': str(A.as_expr()), 'B': str(B.as_expr())
                    })
    rows.append({'degree': degree, 'polynomials': 2**max(0, degree - 1)})

out = {
    'scope': 'All canonical monic 0-1 polynomials with constant term 1 of degrees 1..8 (the support-normalized case); all nontrivial rational factor splits obtained by distributing irreducible factors. Factor splits are oriented.',
    'exact_arithmetic': 'SymPy Poly over QQ; coefficient sign and binary checks are exact.',
    'counts_by_degree': rows,
    'total_polynomials': total_polynomials,
    'total_nontrivial_rational_factor_splits': total_nontrivial_splits,
    'splits_with_both_factors_nonnegative': nonnegative_rational_splits,
    'nonbinary_nonnegative_rational_splits': nonbinary_nonnegative_splits,
    'limitation': 'Finite degree and rational factors only. Does not rule out irrational real nonnegative factors or prove A175.'
}
p=Path(__file__).with_name('a175_q_factor_enum.json')
p.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
