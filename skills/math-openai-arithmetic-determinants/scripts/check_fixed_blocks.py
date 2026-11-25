"""Reconstruct the Family 005 fixed blocks and check invertibility mod 101."""
from math import prod

from check_taylor_contact import scaled_chebyshev, shift_and_multiply

MOD = 101


def inverse(value):
    return pow(value, -1, MOD)


def fixed_rows():
    moments, minus, plus = ([0] * 65 for _ in range(3))
    moments[0], minus[1] = 2, 2
    for d in range(2, 65):
        if d % 2 == 0:
            moments[d] = d * moments[d-2] * inverse(d+1) % MOD
        minus[d] = ((d-1)*minus[d-2] + moments[d-2] + moments[d-1]) * inverse(d) % MOD
        plus[d] = ((d-2)*plus[d-2] + 2*inverse(d-1)) * inverse(d-1) % MOD
    rational_moment = [plus[:59]] + [[minus[i]]+[0]*58 for i in range(1, 65)]
    harmonic, harmonic_square = [0], [0]
    for i in range(1, 65):
        harmonic.append((harmonic[-1]+inverse(i)) % MOD)
        harmonic_square.append((harmonic_square[-1]+inverse(i)**2) % MOD)
        for j in range(1, 59):
            rational_moment[i][j] = (rational_moment[i-1][j-1]-moments[i-1]*inverse(j)) % MOD
    log_moment = [
        [(3*inverse(2) * (-harmonic_square[i] if i==j else
           (harmonic[i]-harmonic[j])*inverse(i-j))) % MOD
         for j in range(59)] for i in range(65)
    ]
    result = []
    for r in range(49):
        order = abs(r-4)
        p = shift_and_multiply(scaled_chebyshev(order, False), 62-order, 2)
        d = shift_and_multiply(scaled_chebyshev(order-1, True), 63-order, 2,
                               1 if r>4 else -1) if order else {}
        row = [(sum(v*rational_moment[i][j] for i,v in p.items())
                -sum(v*log_moment[i][j] for i,v in d.items())) % MOD for j in range(7, 59)]
        for _ in range(4):
            row = [(a-b) % MOD for a,b in zip(row, row[1:])]
        result.append(row)
    return result


def certificate(rows, sign):
    matrix = [[(a+sign*b) % MOD for a,b in zip(rows[i], rows[i+1])] for i in range(48)]
    pivots, swaps = [], []
    for i in range(48):
        pivot_row = next((j for j in range(i, 48) if matrix[j][i]), None)
        if pivot_row is None:
            raise ArithmeticError(f"singular matrix for sign={sign} at step {i}")
        if i != pivot_row:
            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]
            swaps.append((i, pivot_row))
        pivot = matrix[i][i]
        pivots.append(pivot)
        for j in range(i+1, 48):
            factor = matrix[j][i] * inverse(pivot)
            for k in range(i, 48):
                matrix[j][k] = (matrix[j][k]-factor*matrix[i][k]) % MOD
    return pivots, swaps, ((-1)**len(swaps) * prod(pivots)) % MOD


if __name__ == "__main__":
    rows = fixed_rows()
    for sign in (0, 1, -1):
        pivots, swaps, determinant = certificate(rows, sign)
        print(f"sign={sign}; determinant={determinant}; swaps={swaps}; pivots={pivots}")
