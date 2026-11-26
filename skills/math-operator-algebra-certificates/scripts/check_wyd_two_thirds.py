#!/usr/bin/env python3
"""Exact rational replay of the p=2/3 boundary-sign obstruction."""

from __future__ import annotations

from fractions import Fraction
import json


class QComplex:
    def __init__(self, real: Fraction | int = 0, imag: Fraction | int = 0):
        self.real, self.imag = Fraction(real), Fraction(imag)

    def __add__(self, other: object) -> "QComplex":
        other = coerce(other)
        return QComplex(self.real + other.real, self.imag + other.imag)

    __radd__ = __add__

    def __neg__(self) -> "QComplex":
        return QComplex(-self.real, -self.imag)

    def __sub__(self, other: object) -> "QComplex":
        return self + (-coerce(other))

    def __rsub__(self, other: object) -> "QComplex":
        return coerce(other) - self

    def __mul__(self, other: object) -> "QComplex":
        other = coerce(other)
        return QComplex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "QComplex":
        other = coerce(other)
        denominator = other.real * other.real + other.imag * other.imag
        return QComplex((self.real * other.real + self.imag * other.imag) / denominator,
                        (self.imag * other.real - self.real * other.imag) / denominator)

    def __pow__(self, power: int) -> "QComplex":
        result = QComplex(1)
        for _ in range(power):
            result *= self
        return result


def coerce(value: object) -> QComplex:
    return value if isinstance(value, QComplex) else QComplex(value)  # type: ignore[arg-type]


def divided_product(values: list[QComplex], index: int) -> QComplex:
    others = [j for j in range(3) if j != index]
    return (values[index] - values[others[0]]) * (values[index] - values[others[1]])


def check() -> dict[str, str | bool]:
    # Source p=2/3: delta=1/2, a=3/2, b=2, nodes (-1+i0,1,4).
    a, b = Fraction(3, 2), Fraction(2)
    u = [QComplex(0, -1), QComplex(1), QComplex(8)]
    w = [QComplex(-2, -2), QComplex(0), QComplex(-1)]
    x_to_b = [QComplex(1), QComplex(1), QComplex(16)]
    x_to_minus_b = [QComplex(1), QComplex(1), QComplex(Fraction(1, 16))]
    du = (u[0] - u[1]) * (u[1] - u[2]) * (u[2] - u[0])
    dw = (w[0] - w[1]) * (w[1] - w[2]) * (w[2] - w[0])
    delta = sum((w[i] * (u[(i + 1) % 3] - u[(i + 2) % 3]) for i in range(3)), QComplex())
    term_a = -(a * delta**2) / (6 * du * dw)
    term_u = -(a * a) / 3 * sum((x_to_b[i] / divided_product(u, i) for i in range(3)), QComplex())
    term_v = -Fraction(1, 3) * sum((x_to_minus_b[i] / divided_product(w, i) for i in range(3)), QComplex())
    total = term_a + term_u + term_v
    expected = QComplex(Fraction(-271, 1456), Fraction(-11, 182))
    if total.real != expected.real or total.imag != expected.imag or not total.imag < 0:
        raise AssertionError("source boundary value was not reproduced")
    return {
        "A_delta": f"{term_a.real}+({term_a.imag})i",
        "U_delta": f"{term_u.real}+({term_u.imag})i",
        "V_delta": f"{term_v.real}+({term_v.imag})i",
        "H_delta": f"{total.real}+({total.imag})i",
        "imaginary_part_strictly_negative": True,
    }


if __name__ == "__main__":
    print(json.dumps(check(), sort_keys=True))
