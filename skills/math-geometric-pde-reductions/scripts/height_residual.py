#!/usr/bin/env python3
"""Exact coordinate residual for the necessary Darboux height equation."""
import argparse
import ast
import json
import operator
import sys

import sympy as sp
from sympy.matrices.exceptions import NonInvertibleMatrixError


def read_expression(source: str, symbols: dict[str, sp.Expr]) -> sp.Expr:
    source = source.replace("^", "**")
    binary = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
              ast.Div: operator.truediv, ast.Pow: operator.pow}
    unary = {ast.UAdd: operator.pos, ast.USub: operator.neg}
    functions = {"sin": sp.sin, "cos": sp.cos, "exp": sp.exp, "sqrt": sp.sqrt}

    def visit(node: ast.AST) -> sp.Expr:
        if isinstance(node, ast.Name) and node.id in symbols:
            return symbols[node.id]
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return sp.Rational(ast.get_source_segment(source, node).replace("_", ""))
        if isinstance(node, ast.BinOp) and type(node.op) in binary:
            return binary[type(node.op)](visit(node.left), visit(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in unary:
            return unary[type(node.op)](visit(node.operand))
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id in functions and len(node.args) == 1 and not node.keywords):
            return functions[node.func.id](visit(node.args[0]))
        raise ValueError("use x, y, pi, exact arithmetic or sin/cos/exp/sqrt with one argument")

    result = visit(ast.parse(source, mode="eval").body)
    if result.has(sp.zoo, sp.oo, -sp.oo, sp.nan):
        raise ValueError("input contains a singular constant")
    return result


def identity_state(expr: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> bool | None:
    if expr == 0:
        return True
    if expr.is_number and expr.is_zero is False:
        return False
    numerator, denominator = sp.fraction(sp.cancel(expr))
    if numerator.is_polynomial(x, y) and denominator.is_polynomial(x, y):
        return bool(sp.Poly(numerator, x, y).is_zero)
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--g11", required=True, help="g_xx as a SymPy expression")
    parser.add_argument("--g12", required=True, help="g_xy=g_yx as a SymPy expression")
    parser.add_argument("--g22", required=True, help="g_yy as a SymPy expression")
    parser.add_argument("--z", required=True, help="height as a SymPy expression")
    args = parser.parse_args()
    x, y = sp.symbols("x y", real=True)
    symbols = {"x": x, "y": y, "pi": sp.pi}
    try:
        a, b, c, z = (read_expression(value, symbols) for value in (args.g11, args.g12, args.g22, args.z))
        g = sp.Matrix([[a, b], [b, c]])
    except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as exc:
        print(json.dumps({"status": "invalid-input", "error": str(exc)}))
        return 2
    det_g = sp.simplify(g.det())
    if identity_state(det_g, x, y) is True:
        print(json.dumps({"status": "singular-metric", "det_g": str(det_g)}))
        return 2
    try:
        g_inv = sp.simplify(g.inv())
    except NonInvertibleMatrixError:
        print(json.dumps({"status": "singular-metric", "det_g": str(det_g)}))
        return 2
    coords = (x, y)
    gamma = [[[sp.simplify(sum(g_inv[k, ell] * (sp.diff(g[ell, j], coords[i]) +
                 sp.diff(g[ell, i], coords[j]) - sp.diff(g[i, j], coords[ell])) / 2
                 for ell in range(2))) for j in range(2)] for i in range(2)] for k in range(2)]
    dz = sp.Matrix([sp.diff(z, c) for c in coords])
    hess = sp.Matrix(2, 2, lambda i, j: sp.simplify(sp.diff(z, coords[i], coords[j]) -
                     sum(gamma[k][i][j] * dz[k] for k in range(2))))
    # K = <R(partial_x, partial_y) partial_y, partial_x>/det(g), with
    # R(X,Y)Z = nabla_X nabla_Y Z - nabla_Y nabla_X Z - nabla_[X,Y] Z.
    r_xyy = [sp.simplify(sp.diff(gamma[ell][1][1], x) - sp.diff(gamma[ell][0][1], y) +
             sum(gamma[m][1][1] * gamma[ell][0][m] - gamma[m][0][1] * gamma[ell][1][m]
                 for m in range(2))) for ell in range(2)]
    curvature = sp.simplify(sum(g[0, ell] * r_xyy[ell] for ell in range(2)) / det_g)
    grad_norm_sq = sp.simplify((dz.T * g_inv * dz)[0])
    residual = sp.simplify(hess.det() - curvature * det_g * (1 - grad_norm_sq))
    state = identity_state(residual, x, y)
    output = {"status": "zero" if state is True else "nonzero" if state is False else "undecided",
              "det_g": str(det_g), "K": str(curvature), "grad_norm_sq": str(grad_norm_sq),
              "hessian": [[str(hess[i, j]) for j in range(2)] for i in range(2)],
              "residual": str(residual)}
    print(json.dumps(output, sort_keys=True))
    return 0 if state is True else 1 if state is False else 2


if __name__ == "__main__":
    sys.exit(main())
