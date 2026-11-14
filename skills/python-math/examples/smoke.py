"""Demonstration only: exercise installed SymPy, NumPy and SciPy."""
from fractions import Fraction
import json
import numpy as np
import scipy
from scipy.integrate import quad
import sympy as sp

x = sp.Symbol('x', real=True)
symbolic_residual = sp.simplify(sp.diff(sp.sin(x), x) - sp.cos(x))
a = np.array([[2., 1.], [1., 3.]])
b = np.array([1., 2.])
solution = np.linalg.solve(a, b)
linear_residual = float(np.linalg.norm(a @ solution - b))
integral, error_estimate = quad(lambda t: t*t, 0., 1., epsabs=1e-12)
assert Fraction(1, 3) + Fraction(1, 6) == Fraction(1, 2)
assert symbolic_residual == 0
assert linear_residual < 1e-12
assert abs(integral - 1/3) < 1e-12
print(json.dumps({'kind':'toolchain-demonstration', 'rational_sum':'1/2',
                 'symbolic_residual':str(symbolic_residual),
                 'linear_solution':solution.tolist(), 'linear_residual':linear_residual,
                 'quadrature_value':integral, 'quadrature_error_estimate':error_estimate,
                 'versions':{'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__}}, indent=2))
