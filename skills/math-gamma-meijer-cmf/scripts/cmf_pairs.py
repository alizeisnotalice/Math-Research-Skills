"""Generate integer projection pairs for the worked gamma CMF trajectory."""
import argparse
import json
from math import gcd


def dual_step(j):
    return ((6*j*j + 13*j + 10, -8*j - 5, 3),
            (3*j**3 + 3*j*j - 3*j - 6, -3*j*j + 3*j + 3, j - 2),
            (j**4 - 2*j**3 - 6*j*j - 3*j + 3, 6*j*j + 2*j - 1, 1 - 2*j))


def advance(row, matrix):
    return tuple(sum(a*b for a, b in zip(row, column)) for column in zip(*matrix))


def pairs(indices):
    p, q = (1, 1, 0), (1, 1, 1)
    selected = set(indices)
    results = {}
    for j in range(max(selected)):
        step = dual_step(j)
        p = advance(p, step)
        q = advance(q, step)
        n = j + 1
        if n in selected:
            if q[0] == 0:
                results[n] = {"n": n, "P": p[0], "Q": q[0], "reduced_pair": None}
                continue
            divisor = gcd(p[0], q[0])
            sign = 1 if q[0] > 0 else -1
            results[n] = {"n": n, "P": p[0], "Q": q[0], "gcd": divisor,
                          "reduced_pair": [sign*p[0]//divisor, sign*q[0]//divisor]}
    return [results[n] for n in indices]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", nargs="+", type=int)
    args = parser.parse_args()
    if min(args.n) < 1:
        parser.error("n must be positive")
    print(json.dumps(pairs(args.n), indent=2))


if __name__ == "__main__":
    main()
