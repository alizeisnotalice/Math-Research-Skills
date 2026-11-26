#!/usr/bin/env python3
"""Certify a supplied first-order right factor of a linear Mahler operator."""

import ast
import json
import operator
from pathlib import Path
import sys

import sympy as sp


X = sp.Symbol("x")


def rational_expression(value: str) -> sp.Expr:
    operations = {ast.Add: operator.add, ast.Sub: operator.sub,
                  ast.Mult: operator.mul, ast.Div: operator.truediv}

    def read(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return sp.Integer(node.value)
        if isinstance(node, ast.Name) and node.id == "x":
            return X
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            operand = read(node.operand)
            return -operand if isinstance(node.op, ast.USub) else operand
        if isinstance(node, ast.BinOp):
            left, right = read(node.left), read(node.right)
            if isinstance(node.op, ast.Pow) and right.is_Integer:
                return left ** right
            if type(node.op) in operations:
                return operations[type(node.op)](left, right)
        raise ValueError("use x, integers, rational arithmetic and integer powers")

    result = sp.cancel(read(ast.parse(value, mode="eval").body))
    if result.has(sp.zoo, sp.nan, sp.oo):
        raise ValueError("rational expression has a zero denominator")
    return result


def main(input_path: str) -> None:
    data = json.loads(Path(input_path).read_text(encoding="utf-8"))
    base = data["base"]
    if type(base) is not int or base < 2:
        raise ValueError("base must be an integer at least 2")
    coefficients = [rational_expression(value) for value in data["coefficients"]]
    candidate = rational_expression(data["u"])
    if len(coefficients) < 2 or coefficients[0] == 0 or coefficients[-1] == 0:
        raise ValueError("require nonzero first and last operator coefficients")
    if candidate == 0:
        raise ValueError("u must be nonzero")
    product = sp.Integer(1)
    residual = coefficients[0]
    for index, coefficient in enumerate(coefficients[1:], start=1):
        product = sp.cancel(product * candidate.subs(X, X ** (base ** (index - 1))))
        residual = sp.cancel(residual + coefficient * product)
    numerator, denominator = map(sp.expand, sp.fraction(sp.cancel(residual)))
    print(json.dumps({
        "base": base,
        "order": len(coefficients) - 1,
        "right_factor": f"M - ({sp.sstr(candidate)})",
        "residual_numerator": sp.sstr(numerator),
        "residual_denominator": sp.sstr(denominator),
        "right_factor_certified": numerator == 0,
        "scope": "Exact verification of a supplied rational right factor only."
    }, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_mahler_right_factor.py INPUT.json")
    try:
        main(sys.argv[1])
    except (OSError, ValueError, KeyError, TypeError, SyntaxError) as error:
        raise SystemExit(str(error)) from error
